/**
 * Application runner — runs on YOUR machine, never in the cloud.
 *
 * What it does
 *   1. Reads the queue that discovery commits to automation/queue/pending/.
 *   2. Opens each role in a real Chrome window using a PERSISTENT profile
 *      stored on your disk. The first time, you log in to the employer's
 *      careers portal yourself, in that window. The profile remembers the
 *      session — your password is typed once, into the bank's own site,
 *      and is never stored in this repo, this script, or any chat.
 *   3. On Workday portals (JPMorgan, State Street, Wells Fargo, Prudential)
 *      it clicks Apply and autofills the fields it can identify.
 *   4. It ALWAYS stops before the final submit. You review and click
 *      Submit yourself. Immigration, EEO, salary-history, and attestation
 *      questions are yours alone — the runner never touches them.
 *   5. It records the outcome back into the queue file and leaves the
 *      move/commit to you (or run with --commit to let it git-commit).
 *
 * Setup (once):
 *   cd automation/runner
 *   npm install
 *   npx playwright install chromium
 *
 * Run:
 *   node apply_runner.mjs             # work the queue, newest score first
 *   node apply_runner.mjs --login     # just open the browser to log in to portals
 *   node apply_runner.mjs --id <id>   # work a single queue entry
 *   node apply_runner.mjs --commit    # also git-commit queue updates
 */

import { chromium } from "playwright";
import { execSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import readline from "node:readline";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = process.env.REPO_ROOT ?? path.resolve(HERE, "..", "..");
const PENDING = path.join(ROOT, "automation", "queue", "pending");
const SUBMITTED = path.join(ROOT, "automation", "queue", "submitted");
const SKIPPED = path.join(ROOT, "automation", "queue", "skipped");

// The browser profile lives OUTSIDE the repo on purpose: the repo is public
// and sessions/cookies must never be committed. Delete this directory to
// log out of everything.
const PROFILE_DIR = process.env.RUNNER_PROFILE_DIR
  ?? path.join(os.homedir(), ".job-runner-profile");

// Facts the runner may type into a form. Nothing else is ever autofilled.
// These mirror automation/AGENT_CONTRACT.md — if they disagree, the
// contract wins and this file is wrong.
const FACTS = {
  firstName: "Yasir",
  lastName: "Malik",
  email: "YasirAMalik@gmail.com",
  phone: "7867048536",
  city: "Newark",
  state: "New Jersey",
  postal: "07103",
  country: "United States of America",
  linkedin: "https://linkedin.com/in/yasiramalik",
};

// Never touch a field whose label matches any of these. They are the
// candidate's to answer, every time.
const FORBIDDEN = /(sponsor|immigration|work authoriz|visa|citizen|veteran|disab|gender|race|ethnic|salary history|compensation history|signature|attest|certify|criminal|felony)/i;

const args = process.argv.slice(2);
const has = (f) => args.includes(f);
const argOf = (f) => { const i = args.indexOf(f); return i >= 0 ? args[i + 1] : null; };

function loadQueue() {
  if (!fs.existsSync(PENDING)) return [];
  return fs.readdirSync(PENDING)
    .filter((f) => f.endsWith(".json"))
    .map((f) => ({ file: path.join(PENDING, f), entry: JSON.parse(fs.readFileSync(path.join(PENDING, f), "utf8")) }))
    .sort((a, b) => b.entry.score - a.entry.score || (b.entry.sponsor_employer ? 1 : 0) - (a.entry.sponsor_employer ? 1 : 0));
}

function ask(q) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise((res) => rl.question(q, (a) => { rl.close(); res(a.trim()); }));
}

function record(item, status, notes) {
  const now = new Date().toISOString().replace(/\.\d+Z$/, "Z");
  item.entry.status = status;
  item.entry.agent = {
    ...item.entry.agent,
    claimed_by: `local-runner/${os.hostname()}`,
    claimed_at: item.entry.agent?.claimed_at ?? now,
    submitted_at: status === "submitted" ? now : null,
    confirmation_ref: status === "submitted" ? "check Gmail for the employer confirmation" : null,
    notes,
  };
  const destDir = status === "submitted" ? SUBMITTED : status === "pending" ? PENDING : SKIPPED;
  fs.mkdirSync(destDir, { recursive: true });
  const dest = path.join(destDir, path.basename(item.file));
  fs.writeFileSync(dest, JSON.stringify(item.entry, null, 2) + "\n");
  if (dest !== item.file) fs.unlinkSync(item.file);
  if (has("--commit")) {
    execSync(`git add automation/queue && git commit -m "Queue: ${item.entry.company} — ${status}"`, { cwd: ROOT, stdio: "ignore" });
  }
}

/** Fill a Workday-style field by its label, skipping anything forbidden. */
async function fillByLabel(page, labelRe, value) {
  try {
    const field = page.getByLabel(labelRe).first();
    if (await field.count() === 0) return false;
    const label = (await field.getAttribute("aria-label")) ?? "";
    if (FORBIDDEN.test(label)) return false;
    await field.fill(value, { timeout: 3000 });
    return true;
  } catch { return false; }
}

async function autofill(page) {
  let filled = 0;
  const map = [
    [/first\s*name/i, FACTS.firstName],
    [/last\s*name|family\s*name/i, FACTS.lastName],
    [/e-?mail/i, FACTS.email],
    [/phone/i, FACTS.phone],
    [/city/i, FACTS.city],
    [/postal|zip/i, FACTS.postal],
    [/linkedin/i, FACTS.linkedin],
  ];
  for (const [re, val] of map) if (await fillByLabel(page, re, val)) filled++;
  return filled;
}

async function main() {
  fs.mkdirSync(PROFILE_DIR, { recursive: true, mode: 0o700 });
  const browser = await chromium.launchPersistentContext(PROFILE_DIR, {
    headless: process.env.HEADLESS === "1",  // visible by default; the
                                  // point is that you can see and finish it
    viewport: null,
    args: ["--start-maximized"],
  });
  const page = browser.pages()[0] ?? await browser.newPage();

  if (has("--login")) {
    await page.goto("https://careers.jpmorgan.com/us/en/sign-in");
    console.log("\nLog in in the browser window. The session is saved in");
    console.log(`${PROFILE_DIR} on this machine only. Close the window when done.`);
    await new Promise((res) => browser.on("close", res));
    return;
  }

  let queue = loadQueue();
  const only = argOf("--id");
  if (only) queue = queue.filter((q) => q.entry.id === only);
  if (queue.length === 0) {
    console.log("Queue is empty. Run discovery first, or pass --login to set up sessions.");
    await browser.close();
    return;
  }

  console.log(`\n${queue.length} role(s) in the queue.\n`);
  for (const item of queue) {
    const e = item.entry;
    console.log(`\n─ ${e.company} — ${e.title}`);
    console.log(`  score ${e.score}${e.sponsor_employer ? " · sponsor" : ""} · resume: ${e.package.resume}`);
    const go = await ask("  [a]pply now / [s]kip / [q]uit: ");
    if (go === "q") break;
    if (go !== "a") { record(item, "skipped", "skipped by operator"); continue; }

    await page.goto(e.url, { waitUntil: "domcontentloaded" });

    // Try the obvious Apply button; fine if it isn't there.
    for (const re of [/^apply$/i, /apply now/i, /apply with/i]) {
      try { await page.getByRole("link", { name: re }).or(page.getByRole("button", { name: re })).first().click({ timeout: 4000 }); break; } catch {}
    }

    const filled = await autofill(page);
    console.log(`  autofilled ${filled} field(s). Resume to upload: ${path.join(ROOT, e.package.resume)}`);
    console.log("  Finish the form in the browser — the runner never clicks Submit.");
    const done = await ask("  When finished: [s]ubmitted / [k]skipped / [b]locked-by-question: ");
    if (done === "s") record(item, "submitted", `autofilled ${filled} fields; submitted by operator`);
    else if (done === "b") record(item, "skipped", "form blocked on a question reserved for the candidate");
    else record(item, "skipped", "operator skipped after opening");
  }

  await browser.close();
  console.log("\nDone. Queue updated" + (has("--commit") ? " and committed." : " — review with git status, then commit."));
}

main().catch((err) => { console.error(err); process.exit(1); });
