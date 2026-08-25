const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE";                 // 13.3 x 7.5
p.author = "Yasir A. Malik";
p.title  = "Sensemaking and Sensegiving";

const NAVY="1F4E79", DEEP="0E2237", GOLD="8A6410", GOLDL="D2A73F",
      PAPER="FBFAF7", INK="14171C", MUTE="767D86", SOFT="E9EFF6", WHITE="FFFFFF";
const DISP="Georgia", BODY="Cambria", MONO="Courier New";

const W=13.3, H=7.5, M=0.75;

function mark(s,{dark=false}={}){
  const c1 = dark?GOLDL:NAVY, c2 = dark?"8C949E":MUTE;
  s.addText([{text:"Audit ",options:{bold:true,color:c1}},
             {text:"the ",options:{italic:true,color:c2,fontSize:11}},
             {text:"Algorithm",options:{bold:true,color:c1}}],
    {x:M,y:0.3,w:3,h:0.3,fontFace:DISP,fontSize:13,margin:0});
}
function foot(s,txt){
  s.addText(txt,{x:M,y:H-0.62,w:W-2*M,h:0.28,fontFace:MONO,fontSize:9,
    color:MUTE,margin:0,charSpacing:0.6});
}
function title(s,t,sub){
  s.addText(t,{x:M,y:0.95,w:W-2*M,h:0.75,fontFace:DISP,fontSize:34,bold:true,
    color:INK,margin:0});
  if(sub) s.addText(sub,{x:M,y:1.78,w:9.6,h:0.45,fontFace:BODY,fontSize:15,
    color:MUTE,italic:true,margin:0});
}
// small motif: outline square = sensemaking, filled = sensegiving
function motif(s,x,y,filled){
  s.addShape(p.ShapeType.rect,{x,y,w:0.14,h:0.14,
    fill:filled?{color:NAVY}:{color:PAPER}, line:{color:NAVY,width:1.2}});
}

/* 1 ── title ─────────────────────────────────────────────── */
let s = p.addSlide(); s.background={color:DEEP};
mark(s,{dark:true});
s.addText("Scholarly Exchange · Week 1",{x:M,y:2.15,w:8,h:0.3,fontFace:MONO,
  fontSize:11,color:GOLDL,charSpacing:1.6,margin:0});
s.addText("Sensemaking and Sensegiving",{x:M,y:2.5,w:10.5,h:1.0,fontFace:DISP,
  fontSize:46,bold:true,color:WHITE,margin:0});
s.addText("Gioia & Chittipeddi (1991) — an article analysis across eight questions",
  {x:M,y:3.55,w:9.5,h:0.5,fontFace:BODY,fontSize:17,color:"B9C2CC",margin:0});
[0,1,2,3].forEach(i=>s.addShape(p.ShapeType.rect,
  {x:M+i*0.26,y:4.35,w:0.16,h:0.16,fill:i%2?{color:GOLDL}:{color:DEEP},
   line:{color:GOLDL,width:1.3}}));
s.addText("Yasir A. Malik   ·   GEB 7911 Qualitative Research Methods   ·   Dr. Cristina Gonzalez",
  {x:M,y:H-1.25,w:11,h:0.3,fontFace:MONO,fontSize:10,color:"8C949E",margin:0,charSpacing:0.5});
s.addText("github.com/AuditingAI/Profile",{x:M,y:H-0.92,w:8,h:0.3,fontFace:MONO,
  fontSize:10,color:GOLDL,margin:0,charSpacing:0.5});
s.addNotes("Two researchers watched a new university president start a strategic change, in real time. One was inside the process, one deliberately stayed outside.");

/* 2 ── the loop ──────────────────────────────────────────── */
s = p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"The finding, in one picture",
  "Understanding it yourself and selling it to others are not two stages — they alternate.");
const bx=[{x:0.95,t:"ENVISION",u:"what does it mean?",f:false},
          {x:4.05,t:"SIGNAL",u:"tell everyone",f:true},
          {x:7.15,t:"RE-VISION",u:"they pushed back",f:false},
          {x:10.25,t:"ENERGIZE",u:"sell version two",f:true}];
bx.forEach((b,i)=>{
  s.addShape(p.ShapeType.rect,{x:b.x,y:2.75,w:2.35,h:1.15,
    fill:b.f?{color:NAVY}:{color:SOFT}, line:{color:NAVY,width:1.5}});
  s.addText(b.t,{x:b.x,y:2.92,w:2.35,h:0.32,align:"center",fontFace:DISP,
    fontSize:15,bold:true,color:b.f?WHITE:NAVY,margin:0});
  s.addText(b.u,{x:b.x,y:3.28,w:2.35,h:0.3,align:"center",fontFace:BODY,
    fontSize:11,color:b.f?"C9D6E4":MUTE,margin:0});
  if(i<3) s.addShape(p.ShapeType.line,{x:b.x+2.35,y:3.33,w:0.75,h:0,
    line:{color:NAVY,width:2,endArrowType:"triangle"}});
});
s.addShape(p.ShapeType.line,{x:1.0,y:4.55,w:11.5,h:0,
  line:{color:NAVY,width:1.6,dashType:"dash",endArrowType:"triangle"}});
s.addText("…and it runs again — each round changes the next",
  {x:1.0,y:4.62,w:11.5,h:0.35,align:"center",fontFace:BODY,fontSize:13,
   italic:true,color:NAVY,margin:0});
motif(s,M,5.45,false);
s.addText("SENSEMAKING — inward, working out what it means",
  {x:M+0.24,y:5.4,w:5,h:0.26,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
motif(s,M,5.82,true);
s.addText("SENSEGIVING — outward, shaping how others see it",
  {x:M+0.24,y:5.77,w:5,h:0.26,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
foot(s,"Verify the four phase names against the paper — the alternation is the claim, the labels are the detail.");
s.addNotes("The contribution: before this, 'work it out' and 'communicate it' were treated as separate stages. They showed the two keep swapping places.");

/* 3 ── problem + question ───────────────────────────────── */
s = p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"What they were curious about");
[["01","RESEARCH PROBLEM","Change had been studied as outcomes — what changed, did it work. Nobody was treating it as an interpretive process."],
 ["02","RESEARCH QUESTION","How is change initiated? What does a leader actually do, cognitively and socially, to start one?"]]
.forEach(([n,h,t],i)=>{
  const y=2.35+i*1.85;
  s.addShape(p.ShapeType.ellipse,{x:M,y:y,w:0.62,h:0.62,fill:{color:SOFT},line:{color:NAVY,width:1.4}});
  s.addText(n,{x:M,y:y+0.16,w:0.62,h:0.3,align:"center",fontFace:MONO,fontSize:13,bold:true,color:NAVY,margin:0});
  s.addText(h,{x:M+0.95,y:y+0.02,w:6,h:0.32,fontFace:MONO,fontSize:11,bold:true,
    color:NAVY,charSpacing:1.4,margin:0});
  s.addText(t,{x:M+0.95,y:y+0.42,w:7.4,h:1.1,fontFace:BODY,fontSize:16,color:INK,margin:0});
});
s.addShape(p.ShapeType.rect,{x:9.3,y:2.35,w:3.25,h:3.35,fill:{color:"F4F6F9"},line:{color:"E1E6EC",width:1}});
s.addText("“Not ‘did the change work.’ That is the usual question, and they skipped it.”",
  {x:9.6,y:2.75,w:2.65,h:1.6,fontFace:DISP,fontSize:16,italic:true,color:NAVY,margin:0});
s.addText("The gap they named",{x:9.6,y:4.6,w:2.65,h:0.3,fontFace:MONO,fontSize:10,
  color:MUTE,charSpacing:1.2,margin:0});
foot(s,"Gioia, D. A., & Chittipeddi, K. (1991). Strategic Management Journal, 12(6).");

/* 4 ── context + approach, n=1 ──────────────────────────── */
s = p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"One university. One president. Watched live.");
s.addText([{text:"03  CONTEXT",options:{bold:true}}],
  {x:M,y:2.4,w:5,h:0.3,fontFace:MONO,fontSize:11,color:NAVY,charSpacing:1.4,margin:0});
s.addText("A large public university, a newly arrived president launching strategic planning — studied as it happened, not reconstructed afterwards. The setting is part of the claim, not background.",
  {x:M,y:2.8,w:5.6,h:1.5,fontFace:BODY,fontSize:16,color:INK,margin:0});
s.addText([{text:"04  APPROACH",options:{bold:true}}],
  {x:M,y:4.5,w:5,h:0.3,fontFace:MONO,fontSize:11,color:NAVY,charSpacing:1.4,margin:0});
s.addText("Interpretive ethnographic case study. One organization, one process, followed over time rather than sampled.",
  {x:M,y:4.9,w:5.6,h:1.1,fontFace:BODY,fontSize:16,color:INK,margin:0});
// n=1 visual
const gx=7.1, gy=2.75;
for(let r=0;r<4;r++) for(let c=0;c<8;c++){
  const cx=gx+c*0.42, cy=gy+r*0.42;
  s.addShape(p.ShapeType.ellipse,{x:cx,y:cy,w:0.2,h:0.2,fill:{color:"DCE0E5"},line:{width:0}});
}
s.addShape(p.ShapeType.ellipse,{x:gx+3*0.42-0.09,y:gy+1*0.42-0.09,w:0.38,h:0.38,
  fill:{color:NAVY},line:{color:PAPER,width:2}});
s.addText("n = 1",{x:gx+2.6,y:gy+2.05,w:1.6,h:0.4,fontFace:DISP,fontSize:22,bold:true,
  color:NAVY,align:"center",margin:0});
s.addText("and that was never the weakness",{x:gx-0.4,y:gy+2.55,w:5,h:0.3,
  fontFace:BODY,fontSize:13,italic:true,color:MUTE,align:"center",margin:0});
foot(s,"They never claim to represent a population — so sample size was never the promise they made.");

/* 5 ── researcher role — the key slide ──────────────────── */
s = p.addSlide(); s.background={color:DEEP}; mark(s,{dark:true});
s.addText("05  RESEARCHER ROLE",{x:M,y:1.0,w:6,h:0.3,fontFace:MONO,fontSize:11,
  color:GOLDL,charSpacing:1.6,margin:0});
s.addText("They built the reviewer into the method",
  {x:M,y:1.42,w:11.5,h:0.85,fontFace:DISP,fontSize:36,bold:true,color:WHITE,margin:0});
s.addShape(p.ShapeType.rect,{x:M,y:2.85,w:5.4,h:1.9,fill:{color:"18354F"},line:{color:GOLDL,width:1.6}});
s.addText("INSIDE",{x:M,y:3.1,w:5.4,h:0.4,align:"center",fontFace:DISP,fontSize:20,bold:true,color:GOLDL,margin:0});
s.addText("embedded in the change — close enough to see it happen",
  {x:M+0.5,y:3.6,w:4.4,h:0.8,align:"center",fontFace:BODY,fontSize:14,color:"B9C2CC",margin:0});
s.addShape(p.ShapeType.rect,{x:6.65,y:2.85,w:5.4,h:1.9,fill:{color:DEEP},
  line:{color:GOLDL,width:1.6,dashType:"dash"}});
s.addText("OUTSIDE",{x:6.65,y:3.1,w:5.4,h:0.4,align:"center",fontFace:DISP,fontSize:20,bold:true,color:GOLDL,margin:0});
s.addText("deliberately apart — holds the distance so the read can be challenged",
  {x:7.15,y:3.6,w:4.4,h:0.8,align:"center",fontFace:BODY,fontSize:14,color:"B9C2CC",margin:0});
s.addText("=  engagement team  /  independent reviewer",
  {x:M,y:5.15,w:11.3,h:0.45,align:"center",fontFace:DISP,fontSize:22,italic:true,color:WHITE,margin:0});
s.addText("Their own positioning is part of the design — not a limitation buried in an appendix.",
  {x:M,y:5.7,w:11.3,h:0.4,align:"center",fontFace:BODY,fontSize:15,color:"8C949E",margin:0});
s.addNotes("If I say one thing in the room, this is it. Auditors already know this structure — preparer and reviewer, engagement partner and EQ reviewer.");

/* 6 ── data + analysis ladder ───────────────────────────── */
s = p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"How they got there");
s.addText("06  DATA GATHERING",{x:M,y:2.4,w:5,h:0.3,fontFace:MONO,fontSize:11,
  bold:true,color:NAVY,charSpacing:1.4,margin:0});
[["Participant observation","over time, in the room"],
 ["Interviews","the president and senior team"],
 ["Documents and archives","the paper trail"]].forEach(([a,b],i)=>{
  const y=2.85+i*0.78;
  s.addShape(p.ShapeType.rect,{x:M,y:y+0.06,w:0.16,h:0.16,fill:{color:NAVY},line:{width:0}});
  s.addText(a,{x:M+0.35,y:y,w:4.4,h:0.3,fontFace:BODY,fontSize:16,bold:true,color:INK,margin:0});
  s.addText(b,{x:M+0.35,y:y+0.3,w:4.4,h:0.28,fontFace:BODY,fontSize:13,color:MUTE,italic:true,margin:0});
});
s.addText("07  DATA ANALYSIS",{x:6.9,y:2.4,w:5,h:0.3,fontFace:MONO,fontSize:11,
  bold:true,color:NAVY,charSpacing:1.4,margin:0});
s.addShape(p.ShapeType.rect,{x:6.9,y:4.35,w:5.6,h:0.85,fill:{color:SOFT},line:{color:NAVY,width:1.4}});
s.addText("FIRST ORDER — the informants' own words",
  {x:6.9,y:4.6,w:5.6,h:0.35,align:"center",fontFace:MONO,fontSize:12,color:NAVY,margin:0});
s.addShape(p.ShapeType.rect,{x:7.6,y:2.9,w:4.2,h:0.85,fill:{color:NAVY},line:{width:0}});
s.addText("SECOND ORDER — the researchers' theory",
  {x:7.6,y:3.15,w:4.2,h:0.35,align:"center",fontFace:MONO,fontSize:12,color:WHITE,margin:0});
s.addShape(p.ShapeType.line,{x:9.7,y:4.3,w:0,h:-0.5,
  line:{color:NAVY,width:2,endArrowType:"triangle"}});
s.addText("Held apart, so a reader can see exactly where the informants stop and the authors begin.",
  {x:6.9,y:5.4,w:5.6,h:0.7,fontFace:BODY,fontSize:14,italic:true,color:MUTE,margin:0});
foot(s,"That separation is where the credibility lives — the route from observation to claim is visible.");

/* 7 ── how written ──────────────────────────────────────── */
s = p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"Written as a process, not a table",
  "08 · Complex account — a narrative of phases that feed each other, not a matrix of variables.");
const ph=["Envisioning","Signalling","Re-visioning","Energizing"];
ph.forEach((t,i)=>{
  const x=M+i*3.05, filled=i%2===1;
  s.addShape(p.ShapeType.rect,{x,y:3.1,w:2.65,h:1.5,
    fill:filled?{color:NAVY}:{color:WHITE},line:{color:NAVY,width:1.5}});
  s.addText(t,{x,y:3.6,w:2.65,h:0.45,align:"center",fontFace:DISP,fontSize:17,
    bold:true,color:filled?WHITE:NAVY,margin:0});
  if(i<3) s.addShape(p.ShapeType.line,{x:x+2.65,y:3.85,w:0.4,h:0,
    line:{color:NAVY,width:2,endArrowType:"triangle"}});
});
s.addShape(p.ShapeType.line,{x:M,y:5.05,w:11.55,h:0,line:{color:"C9C4B9",width:1}});
s.addText("time  →",{x:M,y:5.15,w:2,h:0.3,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
s.addText("A quantitative paper would report which variables moved. This one reports what happened, in order, and why each step made the next one necessary.",
  {x:M,y:5.7,w:11.5,h:0.7,fontFace:BODY,fontSize:16,color:INK,margin:0});
foot(s,"Gioia, D. A., & Chittipeddi, K. (1991). Strategic Management Journal, 12(6).");

/* 8 ── contrast: Maznevski ──────────────────────────────── */
s = p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"The contrast case",
  "Maznevski & Chudoba (2000) — same family of method, opposite answer on question 05.");
// rhythm chart
const rx=M, ry=2.9, rw=7.4;
s.addShape(p.ShapeType.line,{x:rx,y:ry+1.9,w:rw,h:0,line:{color:"D8D4CB",width:1}});
[0,1,2].forEach(k=>{
  const x=rx+0.3+k*2.5;
  s.addShape(p.ShapeType.rect,{x,y:ry,w:0.34,h:1.9,fill:{color:GOLD},line:{width:0}});
  s.addText("F2F",{x:x-0.35,y:ry-0.38,w:1.05,h:0.3,align:"center",fontFace:MONO,
    fontSize:11,bold:true,color:GOLD,margin:0});
});
[0,1,2,3,4,5,6,7,8].forEach(k=>{
  const x=rx+0.95+ (k%3)*0.42 + Math.floor(k/3)*2.5;
  s.addShape(p.ShapeType.rect,{x,y:ry+1.3,w:0.22,h:0.6,fill:{color:"E4D3A8"},line:{width:0}});
});
s.addText("mediated work fills the gaps",{x:rx,y:ry+2.0,w:rw,h:0.3,align:"center",
  fontFace:MONO,fontSize:10,color:MUTE,margin:0});
s.addText("Effective global virtual teams keep a rhythm.",
  {x:rx,y:ry+2.5,w:rw,h:0.4,fontFace:DISP,fontSize:19,bold:true,color:GOLD,margin:0});
s.addShape(p.ShapeType.rect,{x:8.6,y:2.55,w:3.95,h:3.5,fill:{color:"FBF6EA"},line:{color:"E4D3A8",width:1}});
s.addText("Three teams · one multinational · ~21 months",
  {x:8.9,y:2.85,w:3.4,h:0.6,fontFace:MONO,fontSize:11,color:GOLD,margin:0});
s.addText("Unit of analysis is the interaction incident — not the team, not the meeting.",
  {x:8.9,y:3.6,w:3.4,h:1.0,fontFace:BODY,fontSize:15,color:INK,margin:0});
s.addText("Researchers observe across sites rather than from inside one.",
  {x:8.9,y:4.75,w:3.4,h:1.0,fontFace:BODY,fontSize:15,italic:true,color:MUTE,margin:0});
foot(s,"Maznevski, M. L., & Chudoba, K. M. (2000). Organization Science, 11(5), 473–492.");

/* 9 ── close ────────────────────────────────────────────── */
s = p.addSlide(); s.background={color:DEEP}; mark(s,{dark:true});
s.addText("What I take from it",{x:M,y:1.5,w:10,h:0.6,fontFace:DISP,fontSize:32,
  bold:true,color:WHITE,margin:0});
s.addText("“Their n is one organization. The credibility doesn't come from representativeness — they never claim it. It comes from showing you the route from what was observed to what is claimed, and from splitting the research team so one person keeps distance from the thing being studied.”",
  {x:M,y:2.5,w:11.5,h:2.2,fontFace:DISP,fontSize:22,italic:true,color:"DCE3EA",margin:0,lineSpacing:34});
[0,1,2,3].forEach(i=>s.addShape(p.ShapeType.rect,
  {x:M+i*0.26,y:5.0,w:0.16,h:0.16,fill:i%2?{color:GOLDL}:{color:DEEP},
   line:{color:GOLDL,width:1.3}}));
s.addText("Yasir A. Malik   ·   github.com/AuditingAI/Profile",
  {x:M,y:H-0.95,w:9,h:0.3,fontFace:MONO,fontSize:10,color:GOLDL,margin:0,charSpacing:0.5});
s.addNotes("Close on the method point, not a summary. That is the sentence the course is actually about.");

p.writeFile({fileName:"Malik_GEB7911_ScholarlyExchange_Gioia.pptx"})
 .then(f=>console.log("wrote",f));
