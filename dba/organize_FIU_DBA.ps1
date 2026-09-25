# organize_FIU_DBA.ps1 — Safe reorganizer for the FIU-DBA 7.10 OneDrive folder
# USAGE (PowerShell):
#   1) DRY RUN (default — prints plan, changes nothing):   .\organize_FIU_DBA.ps1
#   2) INVENTORY (writes FIU_inventory.csv, changes nothing): .\organize_FIU_DBA.ps1 -Inventory
#   3) APPLY (actually moves files):                        .\organize_FIU_DBA.ps1 -Apply
# NOTHING IS EVER DELETED. Unknown files -> _UNSORTED_REVIEW; suspected-obsolete -> _TO_BE_DELETED_REVIEW.

param(
    [switch]$Apply,
    [switch]$Inventory,
    [string]$Root = "C:\Users\yasir\OneDrive - Florida International University\FIU-DBA 7.10"
)

if (-not (Test-Path $Root)) { Write-Error "Root not found: $Root"; exit 1 }

$folders = @(
    "00_READ_FIRST",
    "01_NotebookLM_Library",
    "02_GEB7913_Research_Project\Manuscript",
    "02_GEB7913_Research_Project\Data_PRIVATE",
    "02_GEB7913_Research_Project\Correspondence",
    "02_GEB7913_Research_Project\Admin_IRB",
    "02_GEB7913_Research_Project\Simulated_Exercise",
    "03_Dissertation_Pipeline\AI_Audit_Risk_Research",
    "03_Dissertation_Pipeline\Sampling_Relaunch",
    "04_Course_Archive",
    "05_Reference_Library",
    "_UNSORTED_REVIEW",
    "_TO_BE_DELETED_REVIEW"
)

# Inventory mode: list every file recursively, then stop.
if ($Inventory) {
    $out = Join-Path $Root "FIU_inventory.csv"
    Get-ChildItem -Path $Root -File -Recurse |
        Select-Object FullName, Length, LastWriteTime, Extension |
        Export-Csv -Path $out -NoTypeInformation -Encoding UTF8
    Write-Host "Inventory written to $out — send this file to Claude to tailor the rules." -ForegroundColor Green
    exit 0
}

Write-Host ("MODE: " + $(if ($Apply) {"APPLY — files WILL move"} else {"DRY RUN — printing plan only (re-run with -Apply to execute)"})) -ForegroundColor Cyan

# Create target folders
foreach ($f in $folders) {
    $p = Join-Path $Root $f
    if (-not (Test-Path $p)) {
        if ($Apply) { New-Item -ItemType Directory -Path $p -Force | Out-Null }
        Write-Host "[folder] $f"
    }
}

# Classification rules: first match wins. (pattern on file NAME, case-insensitive)
$rules = @(
    @{ Pat = '~\$|(_old|_copy|_backup|superseded|\bv1\b|\(1\)|\(2\))'; Dest = "_TO_BE_DELETED_REVIEW" },
    @{ Pat = 'FULL_DRAFT|STUDY_OVERVIEW|OPEN_QUESTIONS';               Dest = "00_READ_FIRST" },
    @{ Pat = 'chapter|manuscript|research[ _]?paper|appendix|proposal'; Dest = "02_GEB7913_Research_Project\Manuscript" },
    @{ Pat = 'qualtrics|export|responses|\.csv$|\.sav$|dataset';        Dest = "02_GEB7913_Research_Project\Data_PRIVATE" },
    @{ Pat = 'rey|email|correspond|meeting|minutes';                    Dest = "02_GEB7913_Research_Project\Correspondence" },
    @{ Pat = 'irb|consent|citi|evaluation|mentoring|ugs|hold';          Dest = "02_GEB7913_Research_Project\Admin_IRB" },
    @{ Pat = 'simulat|jamovi|exercise';                                 Dest = "02_GEB7913_Research_Project\Simulated_Exercise" },
    @{ Pat = 'ai[_ ]|llm|gpt|scholar|reading[ _]list|brief';            Dest = "03_Dissertation_Pipeline\AI_Audit_Risk_Research" },
    @{ Pat = 'prolific|cloudresearch|recruit|outreach|screener|sample'; Dest = "03_Dissertation_Pipeline\Sampling_Relaunch" },
    @{ Pat = 'textbook|hair|kahneman|standard|pcaob|coso|book';         Dest = "05_Reference_Library" },
    @{ Pat = 'week|module|assignment|syllabus|lecture|class';           Dest = "04_Course_Archive" }
)

$log = @()
# Only loose files in the ROOT are classified (existing subfolders left intact this pass).
Get-ChildItem -Path $Root -File | ForEach-Object {
    $name = $_.Name
    if ($name -eq 'FIU_inventory.csv' -or $name -like 'organize_FIU_DBA*') { return }
    $dest = "_UNSORTED_REVIEW"
    foreach ($r in $rules) { if ($name -imatch $r.Pat) { $dest = $r.Dest; break } }
    $target = Join-Path $Root $dest
    $log += [pscustomobject]@{ File = $name; MoveTo = $dest }
    Write-Host ("  {0}  ->  {1}" -f $name, $dest)
    if ($Apply) { Move-Item -LiteralPath $_.FullName -Destination $target -Force }
}

$logPath = Join-Path $Root ("reorg_log_{0}.csv" -f (Get-Date -Format "yyyyMMdd_HHmm"))
$log | Export-Csv -Path $logPath -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host ("{0} files planned/moved. Log: {1}" -f $log.Count, $logPath) -ForegroundColor Green
if (-not $Apply) { Write-Host "Nothing was moved. Review the plan above, then re-run with -Apply." -ForegroundColor Yellow }
Write-Host "Existing SUBFOLDERS were not touched. Run -Inventory and send FIU_inventory.csv to Claude to plan subfolder migration." -ForegroundColor Yellow
