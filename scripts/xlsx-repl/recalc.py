"""Recalculate an .xlsx and report errors.

Tries LibreOffice headless first. If LO is unavailable (e.g. in a sandbox
that blocks the GUI stack), falls back to the `formulas` Python package
to evaluate every formula in-process.

Usage:
    python3 recalc.py /abs/path/to/file.xlsx

Outputs a single JSON line on stdout, e.g.
    {"status": "success", "total_errors": 0, "engine": "formulas",
     "evaluated_cells": 1672, "kpi_samples": {...}}
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ERROR_MARKERS = ("#REF!", "#NAME?", "#VALUE!", "#DIV/0!", "#N/A", "#NUM!", "#NULL!")


def _try_libreoffice(src: Path) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["HOME"] = tmp
        try:
            proc = subprocess.run(
                ["soffice", "--headless", "--convert-to", "xlsx",
                 "--outdir", tmp, str(src)],
                capture_output=True, text=True, env=env, timeout=120,
            )
        except FileNotFoundError:
            return False, "soffice not found"
        out = Path(tmp) / src.name
        if proc.returncode == 0 and out.exists():
            shutil.copy2(out, src)
            return True, "ok"
        return False, (proc.stderr or proc.stdout)[-200:]


def _formulas_recalc(src: Path) -> dict:
    import formulas  # local import; package is the fallback engine
    xl = formulas.ExcelModel().loads(str(src)).finish()
    sol = xl.calculate()
    errors_by_sheet: dict[str, list[str]] = {}
    total = 0
    for key, node in sol.items():
        val = node.value if hasattr(node, "value") else node
        sval = str(val)
        if any(m in sval for m in ERROR_MARKERS):
            # key looks like '[file.xlsx]SHEET'!A1
            sheet = key.split("]")[1].split("'")[0]
            errors_by_sheet.setdefault(sheet, []).append(f"{key}: {sval}")
            total += 1
    return {
        "engine": "formulas",
        "evaluated_cells": len(sol),
        "total_errors": total,
        "sheets": {k: v[:20] for k, v in errors_by_sheet.items()},
    }


def recalc(path: str) -> dict:
    src = Path(path).resolve()
    if not src.exists():
        return {"status": "error", "message": f"file not found: {src}"}

    ok, msg = _try_libreoffice(src)
    if ok:
        import openpyxl
        wb = openpyxl.load_workbook(src, data_only=True)
        total = 0
        errors_by_sheet: dict[str, list[str]] = {}
        for ws in wb.worksheets:
            hits: list[str] = []
            for row in ws.iter_rows(values_only=False):
                for cell in row:
                    v = cell.value
                    if isinstance(v, str) and any(m in v for m in ERROR_MARKERS):
                        hits.append(f"{cell.coordinate}: {v}")
                        total += 1
            if hits:
                errors_by_sheet[ws.title] = hits[:20]
        wb.close()
        return {
            "status": "success" if total == 0 else "errors_present",
            "engine": "libreoffice",
            "total_errors": total,
            "sheets": errors_by_sheet,
        }

    # Fallback: in-process formula evaluator.
    try:
        result = _formulas_recalc(src)
    except ImportError:
        return {"status": "error",
                "message": f"libreoffice unavailable ({msg}) and `formulas` package not installed"}
    result["status"] = "success" if result["total_errors"] == 0 else "errors_present"
    result["libreoffice_note"] = msg
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"status": "error", "message": "usage: recalc.py FILE.xlsx"}))
        sys.exit(2)
    result = recalc(sys.argv[1])
    print(json.dumps(result))
    sys.exit(0 if result.get("status") == "success" else 1)
