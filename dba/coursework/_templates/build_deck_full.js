const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout="LAYOUT_WIDE"; p.author="Yasir A. Malik";
p.title="Two Ways to Know";

const NAVY="1F4E79",DEEP="0E2237",GOLD="8A6410",GOLDL="D2A73F",
      PAPER="FBFAF7",INK="14171C",MUTE="767D86",SOFT="E9EFF6",WARM="FBF6EA",
      WARMB="E4D3A8",WHITE="FFFFFF";
const DISP="Georgia",BODY="Cambria",MONO="Courier New";
const W=13.33,H=7.5,M=0.75;

const mark=(s,d=false)=>s.addText(
  [{text:"Audit ",options:{bold:true,color:d?GOLDL:NAVY}},
   {text:"the ",options:{italic:true,color:d?"8C949E":MUTE,fontSize:11}},
   {text:"Algorithm",options:{bold:true,color:d?GOLDL:NAVY}}],
  {x:M,y:0.3,w:3,h:0.3,fontFace:DISP,fontSize:13,margin:0});
const foot=(s,t)=>s.addText(t,{x:M,y:H-0.6,w:W-2*M,h:0.28,fontFace:MONO,
  fontSize:9,color:MUTE,margin:0,charSpacing:0.6});
const title=(s,t,sub)=>{
  s.addText(t,{x:M,y:0.95,w:W-2*M,h:0.7,fontFace:DISP,fontSize:32,bold:true,color:INK,margin:0});
  if(sub)s.addText(sub,{x:M,y:1.72,w:10.5,h:0.45,fontFace:BODY,fontSize:14,color:MUTE,italic:true,margin:0});
};
const qtag=(s,x,y,n,t)=>{
  s.addShape(p.ShapeType.ellipse,{x,y,w:0.5,h:0.5,fill:{color:SOFT},line:{color:NAVY,width:1.3}});
  s.addText(n,{x,y:y+0.11,w:0.5,h:0.28,align:"center",fontFace:MONO,fontSize:12,bold:true,color:NAVY,margin:0});
  s.addText(t,{x:x+0.68,y:y+0.07,w:5,h:0.3,fontFace:MONO,fontSize:10.5,bold:true,color:NAVY,charSpacing:1.3,margin:0});
};
// paired answer block: navy=Gioia, gold=Maznevski
const pair=(s,y,gio,maz,h=1.25)=>{
  s.addShape(p.ShapeType.rect,{x:M,y,w:5.7,h,fill:{color:SOFT},line:{width:0}});
  s.addText("GIOIA",{x:M+0.25,y:y+0.13,w:2,h:0.25,fontFace:MONO,fontSize:9,bold:true,color:NAVY,charSpacing:1.3,margin:0});
  s.addText(gio,{x:M+0.25,y:y+0.42,w:5.2,h:h-0.55,fontFace:BODY,fontSize:14,color:INK,margin:0});
  s.addShape(p.ShapeType.rect,{x:6.88,y,w:5.7,h,fill:{color:WARM},line:{width:0}});
  s.addText("MAZNEVSKI",{x:7.13,y:y+0.13,w:2.4,h:0.25,fontFace:MONO,fontSize:9,bold:true,color:GOLD,charSpacing:1.3,margin:0});
  s.addText(maz,{x:7.13,y:y+0.42,w:5.2,h:h-0.55,fontFace:BODY,fontSize:14,color:INK,margin:0});
};
let s;

/* 1 title */
s=p.addSlide(); s.background={color:DEEP}; mark(s,true);
s.addText("GEB 7911 · Scholarly Exchange · Week 1",{x:M,y:2.0,w:8,h:0.3,fontFace:MONO,fontSize:11,color:GOLDL,charSpacing:1.6,margin:0});
s.addText("Two Ways to Know",{x:M,y:2.4,w:11,h:1.1,fontFace:DISP,fontSize:52,bold:true,color:WHITE,margin:0});
s.addText("Gioia & Chittipeddi (1991) and Maznevski & Chudoba (2000), read against the eight analysis questions",
  {x:M,y:3.6,w:10,h:0.7,fontFace:BODY,fontSize:17,color:"B9C2CC",margin:0});
[0,1,2,3].forEach(i=>s.addShape(p.ShapeType.rect,{x:M+i*0.26,y:4.6,w:0.16,h:0.16,
  fill:i%2?{color:GOLDL}:{color:DEEP},line:{color:GOLDL,width:1.3}}));
s.addText("Yasir A. Malik   ·   Dr. Cristina Gonzalez   ·   21 August 2026",
  {x:M,y:H-1.2,w:11,h:0.3,fontFace:MONO,fontSize:10,color:"8C949E",margin:0,charSpacing:0.5});
s.addText("github.com/AuditingAI/Profile",{x:M,y:H-0.88,w:8,h:0.3,fontFace:MONO,fontSize:10,color:GOLDL,margin:0,charSpacing:0.5});

/* 2 at a glance */
s=p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"Same family. Different bet.");
[[M,NAVY,SOFT,"STUDY A","Sensemaking and sensegiving in strategic change initiation",
  "Gioia & Chittipeddi (1991)\nStrategic Management Journal 12(6)",
  "One university. One president. Watched live, from inside.",
  "Bet: get close enough to see how meaning is made."],
 [6.88,GOLD,WARM,"STUDY B","Bridging space over time: global virtual team dynamics and effectiveness",
  "Maznevski & Chudoba (2000)\nOrganization Science 11(5): 473–492",
  "Three teams. One multinational. Twenty-one months.",
  "Bet: watch long enough to see the pattern repeat."]]
.forEach(([x,c,bg,tag,t,cite,ctx,bet])=>{
  s.addShape(p.ShapeType.rect,{x,y:2.3,w:5.7,h:4.05,fill:{color:bg},line:{width:0}});
  s.addText(tag,{x:x+0.3,y:2.5,w:3,h:0.28,fontFace:MONO,fontSize:10,bold:true,color:c,charSpacing:1.5,margin:0});
  s.addText(t,{x:x+0.3,y:2.85,w:5.1,h:0.95,fontFace:DISP,fontSize:17,bold:true,color:INK,margin:0});
  s.addText(cite,{x:x+0.3,y:3.85,w:5.1,h:0.6,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
  s.addText(ctx,{x:x+0.3,y:4.55,w:5.1,h:0.6,fontFace:BODY,fontSize:15,color:INK,margin:0});
  s.addText(bet,{x:x+0.3,y:5.3,w:5.1,h:0.8,fontFace:BODY,fontSize:15,italic:true,color:c,margin:0});
});
foot(s,"Both are qualitative, longitudinal and interpretive. They differ on where the researcher stands.");

/* 3 loop */
s=p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"Gioia — the finding, drawn","Understanding it yourself and selling it to others alternate. Each round changes the next.");
[{x:0.95,t:"ENVISION",u:"what does it mean?",f:false},{x:4.05,t:"SIGNAL",u:"tell everyone",f:true},
 {x:7.15,t:"RE-VISION",u:"they pushed back",f:false},{x:10.25,t:"ENERGIZE",u:"sell version two",f:true}]
.forEach((b,i)=>{
  s.addShape(p.ShapeType.rect,{x:b.x,y:2.75,w:2.35,h:1.15,fill:b.f?{color:NAVY}:{color:SOFT},line:{color:NAVY,width:1.5}});
  s.addText(b.t,{x:b.x,y:2.92,w:2.35,h:0.32,align:"center",fontFace:DISP,fontSize:15,bold:true,color:b.f?WHITE:NAVY,margin:0});
  s.addText(b.u,{x:b.x,y:3.28,w:2.35,h:0.3,align:"center",fontFace:BODY,fontSize:11,color:b.f?"C9D6E4":MUTE,margin:0});
  if(i<3)s.addShape(p.ShapeType.line,{x:b.x+2.35,y:3.33,w:0.75,h:0,line:{color:NAVY,width:2,endArrowType:"triangle"}});
});
s.addShape(p.ShapeType.line,{x:1.0,y:4.5,w:11.5,h:0,line:{color:NAVY,width:1.6,dashType:"dash",endArrowType:"triangle"}});
s.addText("…and it runs again",{x:1.0,y:4.58,w:11.5,h:0.35,align:"center",fontFace:BODY,fontSize:13,italic:true,color:NAVY,margin:0});
s.addShape(p.ShapeType.rect,{x:M,y:5.4,w:0.14,h:0.14,fill:{color:PAPER},line:{color:NAVY,width:1.2}});
s.addText("SENSEMAKING — inward",{x:M+0.24,y:5.35,w:3.4,h:0.26,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
s.addShape(p.ShapeType.rect,{x:4.6,y:5.4,w:0.14,h:0.14,fill:{color:NAVY},line:{color:NAVY,width:1.2}});
s.addText("SENSEGIVING — outward",{x:4.84,y:5.35,w:4,h:0.26,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
foot(s,"Verify the four phase names against the paper — the alternation is the claim, the labels are the detail.");

/* 4 rhythm */
s=p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"Maznevski — the finding, drawn","Effective teams keep a beat. Face-to-face sets the tempo; mediated work fills the gaps.");
const rx=1.1, ry=2.85, rh=1.95;
s.addShape(p.ShapeType.line,{x:rx,y:ry+rh,w:10.9,h:0,line:{color:"C9C4B9",width:1}});
[0,1,2,3].forEach(k=>{
  const x=rx+0.35+k*2.75;
  s.addShape(p.ShapeType.rect,{x,y:ry,w:0.42,h:rh,fill:{color:GOLD},line:{width:0}});
  s.addText("F2F",{x:x-0.45,y:ry-0.4,w:1.3,h:0.3,align:"center",fontFace:MONO,fontSize:11,bold:true,color:GOLD,margin:0});
});
for(let k=0;k<12;k++){
  const grp=Math.floor(k/3), x=rx+1.15+grp*2.75+(k%3)*0.45;
  if(x>11.6) continue;
  s.addShape(p.ShapeType.rect,{x,y:ry+rh-0.72,w:0.26,h:0.72,fill:{color:WARMB},line:{width:0}});
}
s.addText("time  →",{x:rx,y:ry+rh+0.12,w:2,h:0.3,fontFace:MONO,fontSize:10,color:MUTE,margin:0});
s.addText("The unit of analysis is the interaction incident — not the team, not the meeting. That choice is what makes the rhythm visible.",
  {x:M,y:5.5,w:11.6,h:0.7,fontFace:BODY,fontSize:15,color:INK,margin:0});
foot(s,"Maznevski, M. L., & Chudoba, K. M. (2000). Organization Science, 11(5), 473–492.");

/* 5 Q1+Q2 */
s=p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"What each one was curious about");
qtag(s,M,2.25,"01","RESEARCH PROBLEM — the gap");
pair(s,2.9,"Change studied as outcomes — what changed, did it work. Not as an interpretive process.",
       "Virtual teams modelled statically — inputs, process, outputs — with no account of how they work over time.");
qtag(s,M,4.5,"02","RESEARCH QUESTION");
pair(s,5.15,"How is change initiated? What does a leader do, cognitively and socially, to start one?",
       "How do global virtual teams operate over time, and what separates the effective ones?");

/* 6 Q3+Q4 */
s=p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"Where they stood, and how they worked");
qtag(s,M,2.25,"03","CONTEXT — setting is part of the claim");
pair(s,2.9,"One large public university, a newly arrived president, studied as it happened.",
       "Three global virtual teams inside one multinational, followed roughly twenty-one months.");
qtag(s,M,4.5,"04","APPROACH");
pair(s,5.15,"Interpretive ethnographic case study. One organization, one process, followed through.",
       "Longitudinal comparative case study, with adaptive structuration theory as the lens.");

/* 7 Q5 dark */
s=p.addSlide(); s.background={color:DEEP}; mark(s,true);
s.addText("05  RESEARCHER ROLE",{x:M,y:1.0,w:6,h:0.3,fontFace:MONO,fontSize:11,color:GOLDL,charSpacing:1.6,margin:0});
s.addText("This is where they part company",{x:M,y:1.4,w:11.5,h:0.8,fontFace:DISP,fontSize:34,bold:true,color:WHITE,margin:0});
s.addShape(p.ShapeType.rect,{x:M,y:2.75,w:5.4,h:1.75,fill:{color:"18354F"},line:{color:GOLDL,width:1.6}});
s.addText("INSIDE",{x:M,y:2.95,w:5.4,h:0.4,align:"center",fontFace:DISP,fontSize:19,bold:true,color:GOLDL,margin:0});
s.addText("Gioia — one author embedded in the change, one deliberately outside it",
  {x:M+0.45,y:3.42,w:4.5,h:0.85,align:"center",fontFace:BODY,fontSize:14,color:"B9C2CC",margin:0});
s.addShape(p.ShapeType.rect,{x:6.88,y:2.75,w:5.4,h:1.75,fill:{color:DEEP},line:{color:GOLDL,width:1.6,dashType:"dash"}});
s.addText("ACROSS",{x:6.88,y:2.95,w:5.4,h:0.4,align:"center",fontFace:DISP,fontSize:19,bold:true,color:GOLDL,margin:0});
s.addText("Maznevski — observers across three sites, position less foregrounded",
  {x:7.33,y:3.42,w:4.5,h:0.85,align:"center",fontFace:BODY,fontSize:14,color:"B9C2CC",margin:0});
s.addText("Gioia's split  =  engagement team  /  independent reviewer",
  {x:M,y:5.0,w:11.5,h:0.45,align:"center",fontFace:DISP,fontSize:22,italic:true,color:WHITE,margin:0});
s.addText("Positioning designed into the method — not a limitation buried in an appendix.",
  {x:M,y:5.55,w:11.5,h:0.4,align:"center",fontFace:BODY,fontSize:15,color:"8C949E",margin:0});
s.addNotes("If I say one thing, this. Auditors already know the structure — preparer and reviewer, engagement partner and EQ reviewer.");

/* 8 Q6+Q7 */
s=p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"Doing the work");
qtag(s,M,2.25,"06","DATA GATHERING");
pair(s,2.9,"Participant observation over time, interviews with the president and senior team, documents and archives.",
       "Observation of meetings both face-to-face and mediated, interviews, and communication records.");
qtag(s,M,4.5,"07","DATA ANALYSIS");
pair(s,5.15,"First order — informants' own words. Second order — researchers' theory. Held apart so the reader sees the join.",
       "Coded interaction incidents, then looked for temporal patterning across them.");

/* 9 Q8 */
s=p.addSlide(); s.background={color:PAPER}; mark(s);
title(s,"08 · Complex account — written as process, not table",
  "Both report what happened, in order, and why each step made the next necessary.");
["Envisioning","Signalling","Re-visioning","Energizing"].forEach((t,i)=>{
  const x=M+i*3.05,f=i%2===1;
  s.addShape(p.ShapeType.rect,{x,y:2.9,w:2.65,h:1.35,fill:f?{color:NAVY}:{color:WHITE},line:{color:NAVY,width:1.5}});
  s.addText(t,{x,y:3.35,w:2.65,h:0.45,align:"center",fontFace:DISP,fontSize:16,bold:true,color:f?WHITE:NAVY,margin:0});
  if(i<3)s.addShape(p.ShapeType.line,{x:x+2.65,y:3.57,w:0.4,h:0,line:{color:NAVY,width:2,endArrowType:"triangle"}});
});
s.addText("Gioia — a narrative of phases that feed each other",{x:M,y:4.45,w:11.5,h:0.3,fontFace:MONO,fontSize:10,color:NAVY,charSpacing:1.1,margin:0});
s.addShape(p.ShapeType.rect,{x:M,y:5.05,w:11.83,h:1.1,fill:{color:WARM},line:{width:0}});
s.addText("Maznevski — a rhythm model: a repeating temporal structure, with the form of interaction matched to how complex the decision is.",
  {x:M+0.3,y:5.25,w:11.2,h:0.75,fontFace:BODY,fontSize:15,color:INK,margin:0});
foot(s,"A quantitative paper would report which variables moved. Neither of these does.");

/* 10 why n=1 */
s=p.addSlide(); s.background={color:WHITE}; mark(s);
title(s,"Why a tiny n is not the weakness","Neither paper claims to represent a population — so sample size was never the promise.");
s.addText("SURVEY",{x:M,y:2.4,w:3,h:0.3,fontFace:MONO,fontSize:10,color:MUTE,charSpacing:1.4,margin:0});
for(let r=0;r<3;r++)for(let c=0;c<14;c++)
  s.addShape(p.ShapeType.ellipse,{x:M+c*0.34,y:2.8+r*0.34,w:0.18,h:0.18,fill:{color:"DDE1E6"},line:{width:0}});
s.addText("credibility = how many",{x:M,y:3.95,w:5,h:0.3,fontFace:BODY,fontSize:14,italic:true,color:MUTE,margin:0});
s.addText("CASE STUDY",{x:M,y:4.6,w:3,h:0.3,fontFace:MONO,fontSize:10,color:NAVY,charSpacing:1.4,margin:0});
s.addShape(p.ShapeType.ellipse,{x:M,y:5.0,w:0.42,h:0.42,fill:{color:NAVY},line:{width:0}});
s.addShape(p.ShapeType.line,{x:M+0.6,y:5.21,w:3.1,h:0,line:{color:NAVY,width:2,endArrowType:"triangle"}});
s.addText("visible route",{x:M+0.6,y:5.34,w:3.1,h:0.28,align:"center",fontFace:MONO,fontSize:9,color:MUTE,margin:0});
s.addShape(p.ShapeType.rect,{x:4.5,y:4.98,w:1.9,h:0.48,fill:{color:SOFT},line:{color:NAVY,width:1.3}});
s.addText("the claim",{x:4.5,y:5.08,w:1.9,h:0.3,align:"center",fontFace:MONO,fontSize:10,color:NAVY,margin:0});
s.addText("credibility = shown work",{x:M,y:5.7,w:6,h:0.3,fontFace:BODY,fontSize:14,italic:true,color:NAVY,margin:0});
s.addShape(p.ShapeType.rect,{x:7.4,y:2.4,w:5.18,h:3.6,fill:{color:SOFT},line:{width:0}});
s.addText("“The reader is shown the route from what was observed to what is claimed, and judges that route.”",
  {x:7.75,y:2.85,w:4.5,h:1.6,fontFace:DISP,fontSize:19,italic:true,color:NAVY,margin:0});
s.addText("That is the whole answer to “but it is only one case.”",
  {x:7.75,y:4.75,w:4.5,h:0.8,fontFace:BODY,fontSize:14,color:MUTE,margin:0});

/* 11 my own work — dark */
s=p.addSlide(); s.background={color:DEEP}; mark(s,true);
s.addText("WHERE THIS LANDS IN MY OWN WORK",{x:M,y:1.0,w:8,h:0.3,fontFace:MONO,fontSize:11,color:GOLDL,charSpacing:1.6,margin:0});
s.addText("I learned this the expensive way",{x:M,y:1.4,w:11.5,h:0.8,fontFace:DISP,fontSize:34,bold:true,color:WHITE,margin:0});
[["334,976","panel members screened"],["~20","met the eligibility criteria"],["4","valid responses of 23 raw"]]
.forEach(([n,l],i)=>{
  const x=M+i*3.9;
  s.addText(n,{x,y:2.75,w:3.5,h:0.85,fontFace:DISP,fontSize:42,bold:true,color:GOLDL,margin:0});
  s.addText(l,{x,y:3.65,w:3.5,h:0.5,fontFace:BODY,fontSize:14,color:"B9C2CC",margin:0});
});
s.addText("Twenty people is a catastrophic sample for a survey and a workable one for an interview study. Method is not a preference — it is a function of what the population can supply.",
  {x:M,y:4.55,w:11.5,h:1.0,fontFace:DISP,fontSize:19,italic:true,color:"DCE3EA",margin:0});
s.addText("My screening log, 22 July — before this course began: the open-text responses were “worth a short qualitative synthesis regardless of what quantitative path is chosen.”",
  {x:M,y:5.75,w:11.5,h:0.8,fontFace:BODY,fontSize:14,color:"8C949E",margin:0});
s.addNotes("This is mine, not borrowed. The data record reached the memo's conclusion a month before the course started.");

/* 12 close */
s=p.addSlide(); s.background={color:DEEP}; mark(s,true);
s.addText("What I take from it",{x:M,y:1.5,w:10,h:0.6,fontFace:DISP,fontSize:30,bold:true,color:WHITE,margin:0});
s.addText("“Their n is one organization. The credibility doesn't come from representativeness — they never claim it. It comes from showing you the route from what was observed to what is claimed, and from splitting the research team so one person keeps distance from the thing being studied.”",
  {x:M,y:2.45,w:11.5,h:2.3,fontFace:DISP,fontSize:21,italic:true,color:"DCE3EA",margin:0,lineSpacing:33});
[0,1,2,3].forEach(i=>s.addShape(p.ShapeType.rect,{x:M+i*0.26,y:5.05,w:0.16,h:0.16,
  fill:i%2?{color:GOLDL}:{color:DEEP},line:{color:GOLDL,width:1.3}}));
s.addText("Yasir A. Malik   ·   github.com/AuditingAI/Profile",{x:M,y:H-0.92,w:9,h:0.3,
  fontFace:MONO,fontSize:10,color:GOLDL,margin:0,charSpacing:0.5});

p.writeFile({fileName:"Malik_GEB7911_ScholarlyExchange_FULL.pptx"}).then(f=>console.log("wrote",f));
