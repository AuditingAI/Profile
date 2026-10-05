const pptxgen = require('pptxgenjs');
const { applyTheme } = require('/root/.claude/skills/synced/94f2bb76-2282-48c5-97d2-b5bcb79ead8d_ed0299ee-12fc-4f9c-9f1e-58cbd6e91618/pptx/scripts/apply_theme.js');
const THEME = { name: 'Receiving Confirmation', headFontFace: 'Cambria', bodyFontFace: 'Calibri',
  colors: { dk1:'14213D', lt1:'FFFFFF', dk2:'0B1A33', lt2:'EEF1F6', accent1:'B08A2E', accent2:'2F4A7A', accent3:'6B7A99',
            accent4:'D9C27E', accent5:'8C2F39', accent6:'4F7C6B', hlink:'2F4A7A', folHlink:'6B7A99' } };
const pres = new pptxgen(); pres.layout = 'LAYOUT_16x9';
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = 'Receiving Confirmation'; pres.author = 'Yasir A. Malik';
const C = pres.SchemeColor;
const FOOT = { text: 'Yasir A. Malik  ·  GEB 7911  ·  Week 8', options: { x:0.5, y:5.2, w:6, h:0.3, fontSize:10, color:C.accent3, isTextBox:true, margin:0 } };
pres.defineSlideMaster({ title:'DARK', background:{ color:C.text2 }, objects:[],
  });
pres.defineSlideMaster({ title:'CONTENT', background:{ color:C.background1 },
  objects:[ { text: FOOT } ],
  slideNumber:{ x:9.0, y:5.2, w:0.5, h:0.3, fontSize:10, color:C.accent3, align:'right' } });

const T = (s, text) => s.addText(text, { x:0.5, y:0.45, w:9, h:0.6, fontFace:'Cambria', fontSize:26, bold:true, color:C.text1, isTextBox:true, margin:0, objectName:'Title' });
const EB = (s, text, dark) => s.addText(text.toUpperCase(), { x:0.5, y:0.12, w:9, h:0.25, fontSize:11, charSpacing:3, color:C.accent1, bold:true, isTextBox:true, margin:0 });
const add = (m) => pres.addSlide({ masterName:m });

// 1 Title
let s = add('DARK');
s.addText('GEB 7911  ·  FINAL PROPOSAL  ·  6 OCTOBER 2026', { x:0.6, y:0.8, w:8.8, h:0.3, fontSize:12, charSpacing:3, bold:true, color:C.accent1, isTextBox:true, margin:0 });
s.addText('Receiving Confirmation', { x:0.6, y:1.4, w:8.8, h:1.0, fontFace:'Cambria', fontSize:40, bold:true, color:C.background1, isTextBox:true, margin:0 });
s.addText('How experienced auditors experience an AI-generated conclusion that agrees with a judgment they had already formed', { x:0.6, y:2.45, w:8.2, h:0.9, fontSize:18, italic:true, color:C.accent4, isTextBox:true, margin:0 });
s.addShape(pres.shapes.LINE, { x:0.6, y:3.75, w:1.2, h:0, line:{ color:C.accent1, width:2 } });
s.addText('Yasir A. Malik  ·  DBA Cohort 8.14  ·  Florida International University', { x:0.6, y:3.95, w:8.8, h:0.4, fontSize:14, color:C.background1, isTextBox:true, margin:0 });
s.addNotes("Don't start with 'so, um'. Pause, look at the camera, and go straight into the next slide's line. If the instructor asks you to introduce yourself first: 'Good evening. I'm Yasir Malik, and my proposal is called Receiving Confirmation.'");

// 2 Hook
s = add('CONTENT'); EB(s,'The moment');
s.addText('Last year\'s conclusion.', { x:0.5, y:1.0, w:9, h:0.8, fontFace:'Cambria', fontSize:34, color:C.accent3, isTextBox:true, margin:0 });
s.addText('Now a machine that agrees with you.', { x:0.5, y:1.8, w:9, h:0.9, fontFace:'Cambria', fontSize:32, bold:true, color:C.text1, isTextBox:true, margin:0 });
[['You','form a judgment'],['AI tool','reaches the same one'],['?','what happens next']].forEach((p,i)=>{
  const x=0.5+i*3.1;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x, y:3.2, w:2.8, h:1.5, rectRadius:0.1, fill:{ color: i==2?C.text2:C.background2 }, line:{ type:'none' }, objectName:'Step'+(i+1) });
  s.addText([{text:p[0],options:{fontSize:24,bold:true,breakLine:true,color:i==2?C.accent1:C.text1}},{text:p[1],options:{fontSize:15,color:i==2?C.background1:C.text1}}],{ x:x+0.2, y:3.35, w:2.4, h:1.2, isTextBox:true, margin:0, valign:'middle' });
});
s.addNotes("Every auditor on a recurring engagement starts with a reference point: last year's conclusion. What's new is a second voice in the room. An AI tool now reaches a conclusion too. My study is about one specific moment: when that tool agrees with a judgment you had already formed. What do you notice, what do you do, and what do you tell yourself?  [about 30 seconds]");

// 3 Problem
s = add('CONTENT'); EB(s,'The problem'); T(s,'We measure how much, not what it\'s like');
const col=(x,head,body,dark)=>{ s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x,y:1.45,w:4.3,h:3.4,rectRadius:0.1,fill:{color:dark?C.text2:C.background2},line:{type:'none'}});
  s.addText(head,{x:x+0.3,y:1.65,w:3.7,h:0.5,fontSize:20,bold:true,color:dark?C.accent1:C.text1,isTextBox:true,margin:0});
  s.addText(body.map((b,i)=>({text:b,options:{bullet:true,breakLine:i<body.length-1}})),{x:x+0.3,y:2.25,w:3.8,h:2.4,fontSize:15,color:dark?C.background1:C.text1,paraSpaceAfter:8,isTextBox:true,margin:0,valign:'top'}); };
col(0.5,'What research has focused on',['How much auditors rely on AI output','Experiments and archival data','Policies assume human review is a working control']);
col(5.2,'What is less understood',['What it is like to receive a machine\'s confirmation','How auditors make sense of it in the moment','Whether review still works when the tool agrees'],true);
s.addNotes("Firms and regulators are writing AI policies on one assumption: that a human reviewer sits above the tool and that review works. Research has focused mostly on how much auditors rely on AI output, through experiments and archival data. Much less is known about what it's actually like to receive a machine's confirmation of a judgment you already hold. That's the gap I'm addressing. And a survey can't reach it, because it asks people to notice the very thing the bias stops them noticing.  [about 1 minute]");

// 4 RQ
s = add('DARK');
s.addText('RESEARCH QUESTION', { x:0.6, y:0.6, w:8.8, h:0.3, fontSize:12, charSpacing:3, bold:true, color:C.accent1, isTextBox:true, margin:0 });
s.addText('How do experienced auditors experience and make sense of receiving an AI-generated conclusion that confirms a judgment they had already formed?', { x:0.6, y:1.1, w:8.8, h:2.2, fontFace:'Cambria', fontSize:28, italic:true, color:C.background1, isTextBox:true, margin:0, valign:'top' });
s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x:0.6, y:3.75, w:5.2, h:1.0, rectRadius:0.1, fill:{ color:C.accent2 }, line:{ type:'none' } });
s.addText([{text:'Receiving',options:{bold:true,color:C.accent4}},{text:', not relying. Relying assumes the answer.',options:{color:C.background1}}],{ x:0.85, y:3.85, w:4.8, h:0.8, fontSize:17, isTextBox:true, margin:0, valign:'middle' });
s.addNotes("Read the question slowly, word for word.  Then: 'Notice one word: receiving, not relying. An earlier draft said relying, and that assumed the finding before I had any data. Receiving leaves room for whatever auditors actually describe: deference, skepticism, more checking, or something I haven't anticipated. And make sense of stays in because, in phenomenology, the meaning you make of an experience is part of the experience.'  [about 1 minute]");

// 5 Me
s = add('CONTENT'); EB(s,'Framework and position'); T(s,'I\'m an insider, so I make my bias visible');
[['Social constructivist','There are as many accounts of this moment as auditors who lived it. The variation is part of the finding.'],
 ['Insider','My career in audit and risk at Citi and JPMorgan gives me access and vocabulary, and a belief the phenomenon is real.'],
 ['Confirmation hazard log','Every time I feel confirmed by a participant, I log it and record what I did about it.']].forEach((r,i)=>{
  const y=1.4+i*1.2;
  s.addShape(pres.shapes.OVAL,{ x:0.5, y:y+0.1, w:0.6, h:0.6, fill:{ color:i==2?C.accent1:C.text2 }, line:{type:'none'} });
  s.addText(String(i+1),{ x:0.5, y:y+0.1, w:0.6, h:0.6, align:'center', valign:'middle', fontSize:18, bold:true, color:C.background1, isTextBox:true, margin:0 });
  s.addText([{text:r[0],options:{bold:true,fontSize:18,breakLine:true}},{text:r[1],options:{fontSize:15}}],{ x:1.35, y, w:8.1, h:1.0, color:C.text1, isTextBox:true, margin:0, valign:'middle' });
});
s.addNotes("My framework is social constructivist: there's no single correct account waiting to be found. There are as many accounts as there are auditors who lived it.  And I'm not neutral. I built my career in audit and risk at Citi and JPMorgan, and I was a bank examiner. That gives me access and the vocabulary. It also means I already believe this phenomenon is real, so I might hear confirmation where there isn't any.  So I keep a confirmation hazard log. Every time I feel confirmed by what a participant says, I log it, and I record what I did about it. Feeling confirmed by a participant is the very thing I'm studying, happening inside my own study.  [about 1 minute]");

// 6 Approach
s = add('CONTENT'); EB(s,'Approach'); T(s,'Phenomenology fits a question of experience');
[['Phenomenology','Lived experience and its meaning, across people who share it',true],['Grounded theory','Builds a theory of a process. Not my question',false],['Case study','Needs a bounded site. This moment crosses firms',false]].forEach((c,i)=>{
  const x=0.5+i*3.1;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x, y:1.5, w:2.8, h:2.9, rectRadius:0.1, fill:{ color:c[2]?C.text2:C.background2 }, line:{type:'none'} });
  s.addText(c[2]?'CHOSEN':'SET ASIDE',{ x:x+0.25, y:1.7, w:2.3, h:0.3, fontSize:11, charSpacing:2, bold:true, color:c[2]?C.accent1:C.accent3, isTextBox:true, margin:0 });
  s.addText([{text:c[0],options:{fontSize:17,bold:true,breakLine:true,color:c[2]?C.background1:C.text1}},{text:c[1],options:{fontSize:15,color:c[2]?C.lt2||C.background1:C.text1}}],{ x:x+0.25, y:2.1, w:2.3, h:2.1, isTextBox:true, margin:0, valign:'top', paraSpaceAfter:6 });
});
s.addNotes("I chose phenomenology because my question is about lived experience and what it means to the person. Not grounded theory: I'm not studying a process or building a theory yet. Not a case study: this moment happens across many firms, so there's no single bounded site. The site is the shared professional context.  [about 45 seconds]");

// 7 Participants
s = add('CONTENT'); EB(s,'Participants and data'); T(s,'Everyone must have lived the moment');
['5+ years in audit or risk assurance','Recurring, multi-year engagements','Uses AI tools that produce conclusions','Can recall one specific occasion'].forEach((t,i)=>{
  const y=1.35+i*0.82, key=i==3;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x:0.5, y, w:5.4, h:0.68, rectRadius:0.08, fill:{ color:key?C.text2:C.background2 }, line:{type:'none'} });
  s.addText(t,{ x:0.75, y, w:5.0, h:0.68, fontSize:16, bold:key, color:key?C.accent4:C.text1, valign:'middle', isTextBox:true, margin:0 });
});
[['10–15','participants, depth decides'],['60 min','one interview each'],['~20','eligible from a 334,976-member panel']].forEach((n,i)=>{
  const y=1.35+i*1.1;
  s.addText([{text:n[0],options:{fontFace:'Cambria',fontSize:32,bold:true,color:C.accent1,breakLine:true}},{text:n[1],options:{fontSize:13,color:C.text1}}],{ x:6.3, y, w:3.2, h:1.0, isTextBox:true, margin:0, valign:'top' });
});
s.addNotes("I use criterion sampling, with four criteria. The fourth one carries the study: you must be able to recall one specific occasion when an AI tool reached the conclusion you'd already reached. Recall, not interpretation. You don't need to have thought of it as bias or reassurance; that meaning comes out in the interview.  I'll test the screening question first, add referrals screened the same way, and cap it at two people per firm.  Ten to fifteen participants, one interview each, about an hour. I stop based on how deep and rich the accounts are, not on a saturation rule.  Why interviews? When I fielded my survey, a panel of almost 335,000 people gave me about twenty eligible auditors. Too few for a survey; enough for this.  [about 1.5 minutes]");

// 8 Analysis
s = add('CONTENT'); EB(s,'Analysis'); T(s,'From their words to the essence');
const steps=['Statements','Meaning units','Themes','What they lived','How and where','Essence'];
steps.forEach((t,i)=>{ const x=0.5+i*1.52;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x, y:1.6, w:1.36, h:1.1, rectRadius:0.08, fill:{ color:i==5?C.text2:C.background2 }, line:{type:'none'} });
  s.addText(t,{ x:x+0.05, y:1.6, w:1.26, h:1.1, fontSize:12, bold:true, align:'center', valign:'middle', color:i==5?C.accent4:C.text1, isTextBox:true, margin:0 });
});
s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x:0.5, y:3.1, w:4.3, h:1.6, rectRadius:0.1, fill:{ color:C.background2 }, line:{type:'none'} });
s.addText([{text:'Before the essence',options:{bold:true,fontSize:16,breakLine:true}},{text:'I re-read every transcript only for what contradicts it.',options:{fontSize:15}}],{ x:0.75, y:3.25, w:3.8, h:1.3, color:C.text1, isTextBox:true, margin:0, valign:'top' });
s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x:5.2, y:3.1, w:4.3, h:1.6, rectRadius:0.1, fill:{ color:C.text2 }, line:{type:'none'} });
s.addText([{text:'AI does not code',options:{bold:true,fontSize:16,color:C.accent1,breakLine:true}},{text:'NVivo stores my codes. I assign them. AI agreeing with my themes would recreate the phenomenon.',options:{fontSize:15,color:C.background1}}],{ x:5.45, y:3.25, w:3.8, h:1.3, isTextBox:true, margin:0, valign:'top' });
s.addNotes("I follow Creswell's data analysis spiral, using the phenomenological steps. Every statement about the experience is listed with equal weight. Those become meaning units, and then themes, named in words a participant would recognize. Then I write what they experienced, then how and in what context, and finally the essence.  Before I write the essence, I re-read every transcript looking only for what contradicts it, for example someone who checked harder when the tool agreed.  I code by hand. NVivo stores my codes, but AI doesn't assign them. If a model proposed my themes and I agreed with them, I'd be recreating the phenomenon inside my own analysis.  [about 1 minute]");

// 9 Trust
s = add('CONTENT'); EB(s,'Validation and ethics'); T(s,'Three lenses on whether I got it right');
[['Participants','Each checks their own description only, not my composite'],['Outside reviewer','A few chosen transcripts, including one that challenges me, read with my memos'],['Me','The hazard log, tied to the audit trail, shows what changed my decisions']].forEach((c,i)=>{
  const x=0.5+i*3.1;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{ x, y:1.45, w:2.8, h:2.35, rectRadius:0.1, fill:{ color:C.background2 }, line:{type:'none'} });
  s.addText([{text:c[0],options:{fontSize:19,bold:true,color:C.accent2,breakLine:true}},{text:c[1],options:{fontSize:15,color:C.text1}}],{ x:x+0.25, y:1.65, w:2.3, h:2.0, isTextBox:true, margin:0, valign:'top', paraSpaceAfter:6 });
});
s.addText('Ethics: consent with separate recording consent · pseudonyms · encrypted storage · nobody approached before IRB approval', { x:0.5, y:4.1, w:9, h:0.6, fontSize:14, italic:true, color:C.text1, isTextBox:true, margin:0 });
s.addNotes("I check my work through three lenses. Participants: each one reads their own description, not the raw transcript, and can add context. That speaks to their own account only, not my overall interpretation. An outside reviewer: I choose a few transcripts on purpose, including one that challenges what I'm seeing, and the reviewer reads them with my memos. And me: the hazard log, cross-referenced to the audit trail, shows where it changed what I did.  Ethics: informed consent, separate consent for recording, pseudonyms, encrypted storage. My current IRB approval covers the survey, so interviews need a modification, and no one is approached before that's approved.  [about 1 minute]");

// 10 Contributions
s = add('CONTENT'); EB(s,'Why it matters'); T(s,'Contributions and limits');
col(0.5,'Contributions',['Research: separates automation bias from sycophancy at the one moment they look identical','Practice: tests from the inside whether human review is the control policies assume'],true);
col(5.2,'Limits',['Small, network-recruited sample','Recalled experience, possibly tidied in memory','No generalization claimed; the reader judges fit']);
s.addNotes("For research: automation bias is a human tendency; sycophancy is a property of the model. When the tool agrees with you, both push in the same direction, and measuring reliance can't separate them. Asking auditors what that moment is like can.  For practice: firms and regulators assume human review works. This study looks at that assumption from the inside, from the people doing the reviewing.  The limits: a small sample, recruited through networks, and experiences recalled after the fact. I don't claim to generalize; I offer a description rich enough for a reader to judge whether it fits their setting.  [about 45 seconds]");

// 11 Close
s = add('DARK');
s.addText('The machine agreeing with you feels like evidence.', { x:0.6, y:1.1, w:8.8, h:1.2, fontFace:'Cambria', fontSize:30, bold:true, color:C.background1, isTextBox:true, margin:0 });
s.addText('My study asks whether it is experienced that way, and what auditors do next.', { x:0.6, y:2.45, w:8.8, h:0.9, fontFace:'Cambria', fontSize:24, italic:true, color:C.accent4, isTextBox:true, margin:0 });
s.addText('Thank you', { x:0.6, y:3.5, w:8.8, h:0.5, fontSize:20, bold:true, color:C.accent1, isTextBox:true, margin:0 });
s.addText('AI disclosure: Claude (Anthropic) helped draft and lay out these slides and speaker notes from my proposal and protocol. The research question, design decisions and interpretations are my own.', { x:0.6, y:4.5, w:8.8, h:0.6, fontSize:11, color:C.accent3, isTextBox:true, margin:0 });
s.addNotes("Say the first line, pause, then the second. Then 'Thank you' and stop talking. Silence is fine.  If asked about AI: 'As disclosed, I used AI to help lay out the slides; the research decisions are mine.'  If a question stumps you: 'That's a good challenge. I haven't resolved it yet. Here's how I'd approach it...' then name the next step.");

(async()=>{ await pres.writeFile({ fileName:'Malik_GEB7911_Week8_Talk.pptx' }); await applyTheme('Malik_GEB7911_Week8_Talk.pptx', THEME); console.log('ok'); })();
