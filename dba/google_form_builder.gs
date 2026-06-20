/**
 * DBA Survey Preview — One-Click Google Form Builder
 *
 * What this does:
 *   - Creates a new Google Form titled "DBA Survey Preview Feedback"
 *   - Adds: 3 sample survey items (so testers see the real instrument's
 *     style), 5 feedback questions, 2 demographics, a Preview ID field
 *     for cross-linking with the existing Survey_Preview.html
 *   - Creates a Response Sheet (auto-linked, every submission lands there)
 *   - Logs the Form URL, the Edit URL, and the Response Sheet URL
 *
 * How to run (works on mobile + desktop):
 *   1. On your Pixel 10, open Chrome → https://script.google.com
 *   2. Sign in with yasiramalik@gmail.com
 *   3. Tap "New project"
 *   4. Delete the boilerplate code, paste THIS entire file
 *   5. Tap the Save icon
 *   6. Tap Run → it asks for permissions on first run → allow
 *   7. Look at "Execution log" — it shows three URLs:
 *        • Form URL  → this is what you share with testers in WhatsApp
 *        • Edit URL  → use this to tweak the form later
 *        • Sheet URL → your research-grade backend (every response auto-lands here)
 *   8. Open the Sheet URL — keep that tab open during the test window
 *
 * Re-running the script will create a NEW form each time. Run it only once.
 */

function createPreviewForm() {
  const FORM_TITLE = 'DBA Survey Preview — Feedback';
  const FORM_DESC = [
    'Thanks for taking 5 minutes to help test this survey before it goes',
    'to real audit professionals. Your answers help me catch any issues',
    'in wording or flow.',
    '',
    'This is a PREVIEW. Nothing here is part of the formal data collection',
    'for the FIU DBA research project (IRB-25-0462). The formal pilot uses',
    'a separate, IRB-approved instrument hosted on FIU Qualtrics.',
    '',
    'Estimated time: 5 minutes. Anonymous — no identifying information is',
    'collected or required.',
  ].join('\n');

  const form = FormApp.create(FORM_TITLE);
  form.setDescription(FORM_DESC);
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setRequireLogin(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Thanks — feedback recorded. You can close this tab. — Yasir');

  // ===== Section 1: Preview metadata =====
  form.addPageBreakItem()
      .setTitle('Quick metadata')
      .setHelpText('30 seconds — sets the context.');

  form.addTextItem()
      .setTitle('Preview ID (if you took the HTML preview, paste the 8-character code)')
      .setHelpText('Looks like ABC23XYZ. Leave blank if you only took this Google Form.')
      .setRequired(false);

  form.addMultipleChoiceItem()
      .setTitle('What device are you using?')
      .setChoiceValues(['iPhone', 'Android phone', 'iPad / tablet', 'Desktop / laptop'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Are you in an audit-related role currently or in the recent past?')
      .setChoiceValues(['Yes — external audit',
                        'Yes — internal audit',
                        'Yes — other audit-related role',
                        'No — but happy to help test the flow'])
      .setRequired(true);

  // ===== Section 2: Sample items (so testers see the survey's style) =====
  form.addPageBreakItem()
      .setTitle('Three sample items from the survey')
      .setHelpText('Tap whatever feels right — your specific answers do not matter for this preview. The goal is to confirm the wording is clear.');

  const likert = ['1 — Strongly disagree', '2 — Disagree',
                  '3 — Neither agree nor disagree',
                  '4 — Agree', '5 — Strongly agree'];

  form.addMultipleChoiceItem()
      .setTitle('My firm provides specific training on cognitive biases (such as anchoring) that can affect audit judgments.')
      .setChoiceValues(likert)
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('When I join a continuing engagement, I form my own view before reading prior auditors\' conclusions.')
      .setChoiceValues(likert)
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('My work is reviewed by a qualified auditor who was not involved in forming the original judgment.')
      .setChoiceValues(likert)
      .setRequired(true);

  // ===== Section 3: Feedback on the preview (the actual research input) =====
  form.addPageBreakItem()
      .setTitle('Your feedback on the preview')
      .setHelpText('This is what I actually need. Be honest.');

  form.addMultipleChoiceItem()
      .setTitle('Instructions and item wording were clear.')
      .setChoiceValues(likert)
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('The sample items sounded natural for an audit professional.')
      .setChoiceValues(likert)
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('A 15–20 minute version of this would feel reasonable.')
      .setChoiceValues(likert)
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('Which item(s), if any, were confusing or felt off?')
      .setHelpText('Specific wording feedback is gold. "All clear" is also fine.')
      .setRequired(false);

  form.addParagraphTextItem()
      .setTitle('Anything else I should know before I send this to real auditors?')
      .setRequired(false);

  // ===== Section 4: Optional contact (for follow-up only, not data) =====
  form.addPageBreakItem()
      .setTitle('Optional — name for the backlog only')
      .setHelpText('So I can thank you. Skip if you prefer anonymous.');

  form.addTextItem()
      .setTitle('Your name or initials (optional, not analyzed)')
      .setRequired(false);

  // ===== Hook up the Response Sheet =====
  const ss = SpreadsheetApp.create(FORM_TITLE + ' (Responses)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  // ===== Output the URLs you need =====
  const formUrl  = form.getPublishedUrl();      // what you share with testers
  const editUrl  = form.getEditUrl();           // tweak the form later
  const sheetUrl = ss.getUrl();                 // your research backend
  const shortUrl = form.shortenFormUrl(formUrl); // wa.me-friendly short URL

  const banner =
    '\n========== DBA Preview Form READY ==========\n' +
    'FORM URL (share this with testers):\n  ' + formUrl + '\n\n' +
    'SHORT FORM URL (better for WhatsApp):\n  ' + shortUrl + '\n\n' +
    'EDIT URL (only you — to change questions later):\n  ' + editUrl + '\n\n' +
    'RESPONSE SHEET URL (your live backend):\n  ' + sheetUrl + '\n' +
    '============================================\n';

  Logger.log(banner);

  // Also show a popup if the script editor is open in browser
  try {
    const ui = SpreadsheetApp.getUi();
    ui.alert('DBA Preview Form Ready',
             'Open the Execution log to copy the URLs.\n\n' +
             'Short form URL (for WhatsApp):\n' + shortUrl,
             ui.ButtonSet.OK);
  } catch (e) {
    // running outside a spreadsheet context — no UI available, that's fine
  }

  return { formUrl, shortUrl, editUrl, sheetUrl };
}
