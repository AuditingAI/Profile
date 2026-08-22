const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout="LAYOUT_WIDE"; p.author="Yasir A. Malik";
p.title="A Map of the International Business Field";
const NAVY="1F4E79",DEEP="0E2237",GOLD="8A6410",GOLDL="D2A73F",PAPER="FBFAF7",
      INK="14171C",MUTE="767D86",SOFT="E9EFF6",WARM="FBF6EA",WARMB="E4D3A8",
      WHITE="FFFFFF",RULE="D8D4CB",TEAL="1C6B63";
const DISP="Georgia",BODY="Cambria",MONO="Courier New";
const W=13.33;
const mark=(s,d)=>s.addText([{text:"Audit ",options:{bold:true,color:d?GOLDL:NAVY}},
  {text:"the ",options:{italic:true,color:d?"8C949E":MUTE,fontSize:9}},
  {text:"Algorithm",options:{bold:true,color:d?GOLDL:NAVY}}],
  {x:0.5,y:0.14,w:3,h:0.26,fontFace:DISP,fontSize:11,margin:0});

/* ══ SLIDE 1 ══════════════════════════════════════════ */
let s=p.addSlide(); s.background={color:PAPER};
s.addShape(p.ShapeType.rect,{x:0,y:0,w:W,h:1.3,fill:{color:DEEP},line:{width:0}});
mark(s,true);
s.addText("GEB 7365  ·  after Chandra & Newburry (1997), Figure 1, p. 397",
  {x:0.5,y:0.44,w:7,h:0.24,fontFace:MONO,fontSize:9,color:GOLDL,margin:0,charSpacing:1.2});
s.addText("The Field Never Integrated",
  {x:0.5,y:0.68,w:7.2,h:0.5,fontFace:DISP,fontSize:30,bold:true,color:WHITE,margin:0});
s.addShape(p.ShapeType.rect,{x:8.15,y:0.42,w:0.03,h:0.72,fill:{color:GOLDL},line:{width:0}});
s.addText("Run the maps with management split into its sub-fields and two things break — then a third integration point appears.",
  {x:8.35,y:0.42,w:4.5,h:0.75,fontFace:BODY,fontSize:12.5,italic:true,color:"DCE3EA",margin:0});

/* panel A */
s.addShape(p.ShapeType.rect,{x:0.5,y:1.55,w:5.55,h:3.45,fill:{color:WHITE},line:{color:RULE,width:1}});
s.addText("(A)",{x:0.72,y:1.64,w:0.38,h:0.24,fontFace:MONO,fontSize:9.5,bold:true,color:NAVY,margin:0,charSpacing:1.1});
s.addText("The circle is too coarse",{x:1.16,y:1.62,w:2.6,h:0.26,fontFace:DISP,fontSize:14,bold:true,color:INK,margin:0});
const ring=(x,y,w,h,c)=>s.addShape(p.ShapeType.ellipse,
  {x,y,w,h,fill:{color:WHITE,transparency:100},line:{color:c||NAVY,width:1.25}});
ring(1.62,2.12,0.80,1.95); ring(2.02,2.02,1.05,1.05); ring(3.20,2.10,1.05,1.05); ring(1.72,3.28,1.00,1.00);
s.addShape(p.ShapeType.ellipse,{x:2.15,y:2.35,w:1.95,h:1.95,
  fill:{color:SOFT,transparency:22},line:{color:NAVY,width:2}});
s.addText("IB",{x:2.15,y:2.92,w:1.95,h:0.4,align:"center",fontFace:DISP,fontSize:20,bold:true,color:NAVY,margin:0});
ring(3.05,3.30,0.78,0.78,TEAL); ring(3.72,3.48,0.68,0.68,TEAL); ring(4.32,3.60,0.58,0.58,TEAL);
const lab=(t,x,y,w,c,sz)=>s.addText(t,{x,y,w,h:0.2,align:"center",fontFace:MONO,
  fontSize:sz||9,color:c||"454B54",margin:0});
lab("Economics",0.96,2.30,1.0); lab("Finance",2.05,1.93,1.0); lab("Accounting",3.25,1.93,1.0);
lab("Marketing",1.24,4.30,1.0);
lab("STRAT",3.14,4.14,0.60,TEAL,8.5); lab("HR",3.86,4.24,0.40,TEAL,8.5); lab("OB",4.46,4.34,0.40,TEAL,8.5);
s.addText("MANAGEMENT\nfanned",{x:5.02,y:3.56,w:0.95,h:0.36,fontFace:MONO,fontSize:8.5,bold:true,color:TEAL,margin:0,charSpacing:0.8});
s.addText("One circle per discipline hides the real picture: strategy sits deep inside IB, HR partly, OB barely touches it.",
  {x:0.72,y:4.58,w:5.1,h:0.34,fontFace:BODY,fontSize:11,color:"454B54",margin:0});

/* panel B */
s.addShape(p.ShapeType.rect,{x:6.28,y:1.55,w:6.55,h:3.45,fill:{color:WHITE},line:{color:RULE,width:1}});
s.addText("(B)",{x:6.50,y:1.64,w:0.38,h:0.24,fontFace:MONO,fontSize:9.5,bold:true,color:NAVY,margin:0,charSpacing:1.1});
s.addText("The crossbars run both ways",{x:6.94,y:1.62,w:3.0,h:0.26,fontFace:DISP,fontSize:14,bold:true,color:INK,margin:0});
[{x:7.00,top:2.20,n:"ECON"},{x:8.00,top:2.34,n:"FIN"},{x:9.00,top:2.54,n:"ACCT"},{x:12.05,top:2.62,n:"MKTG"}]
 .forEach(c=>{
  s.addText(c.n,{x:c.x-0.42,y:c.top-0.26,w:0.84,h:0.2,align:"center",fontFace:MONO,fontSize:9,bold:true,color:NAVY,margin:0});
  s.addShape(p.ShapeType.line,{x:c.x,y:c.top,w:0,h:4.28-c.top,line:{color:NAVY,width:2.25,endArrowType:"triangle"}});
});
s.addText("MGMT",{x:9.90,y:1.96,w:1.7,h:0.2,align:"center",fontFace:MONO,fontSize:9,bold:true,color:TEAL,margin:0});
s.addShape(p.ShapeType.line,{x:9.98,y:2.16,w:1.54,h:0,line:{color:TEAL,width:1,dashType:"dash"}});
s.addShape(p.ShapeType.line,{x:10.05,y:2.26,w:0,h:2.02,line:{color:TEAL,width:2.25,endArrowType:"triangle"}});
s.addShape(p.ShapeType.line,{x:10.75,y:3.02,w:0,h:1.26,line:{color:TEAL,width:2,endArrowType:"triangle"}});
s.addShape(p.ShapeType.line,{x:11.45,y:4.24,w:0,h:-1.06,line:{color:TEAL,width:2,endArrowType:"triangle",dashType:"dash"}});
lab("strat",9.72,4.32,0.66,TEAL,8); lab("HR",10.45,4.32,0.6,TEAL,8); lab("OB",11.15,4.32,0.6,TEAL,8);
const bar=(x1,x2,y,c)=>s.addShape(p.ShapeType.rect,{x:x1,y,w:x2-x1,h:0.12,
  fill:{color:c||NAVY,transparency:55},line:{color:c||NAVY,width:0.75}});
bar(7.00,8.00,2.84); bar(8.00,9.00,3.20); bar(10.05,12.05,3.56,TEAL);
s.addText("OB flows back INTO management (Hofstede, GLOBE)",
  {x:10.60,y:2.66,w:2.2,h:0.34,fontFace:MONO,fontSize:7.5,color:TEAL,margin:0});
s.addShape(p.ShapeType.rect,{x:6.60,y:4.56,w:5.2,h:0.32,fill:{color:WHITE,transparency:100},
  line:{color:NAVY,width:1.25,dashType:"dash"}});
s.addText("Minor IB field integration — only on strategy issues",
  {x:6.60,y:4.62,w:5.2,h:0.22,align:"center",fontFace:MONO,fontSize:9,color:NAVY,margin:0});
s.addText("time",{x:12.42,y:3.80,w:0.7,h:0.2,fontFace:MONO,fontSize:8,color:MUTE,margin:0});

/* extension band */
s.addShape(p.ShapeType.rect,{x:0.5,y:5.18,w:12.33,h:1.74,fill:{color:WARM},line:{color:GOLD,width:2,dashType:"dash"}});
s.addText("THE THIRD INTEGRATION POINT",{x:0.78,y:5.32,w:9,h:0.22,fontFace:MONO,fontSize:9,bold:true,color:GOLD,margin:0,charSpacing:1.3});
s.addText("Management gave IB the integral plan for operations. Nobody has written the integral plan for evidence.",
  {x:0.78,y:5.56,w:9.6,h:0.36,fontFace:DISP,fontSize:17,bold:true,color:INK,margin:0});
s.addText("Both maps describe integration as TOPICAL — disciplines meet where their subject matter overlaps, which is rare and accidental. There is a second kind. Every sub-field above becomes international at the same moment: when it must collect comparable evidence from specialists in more than one country. That is structural, and field-wide by construction.",
  {x:0.78,y:5.96,w:9.6,h:0.84,fontFace:BODY,fontSize:11.5,color:"454B54",margin:0});
s.addShape(p.ShapeType.line,{x:10.62,y:5.40,w:0,h:1.30,line:{color:WARMB,width:1}});
s.addText("6",{x:10.85,y:5.48,w:1.2,h:0.64,fontFace:DISP,fontSize:40,bold:true,color:GOLD,margin:0});
s.addText("eligible per 100,000\nmeasured, before fielding",{x:10.85,y:6.14,w:1.95,h:0.44,fontFace:MONO,fontSize:8.5,color:MUTE,margin:0});
s.addText("Yasir A. Malik   ·   github.com/AuditingAI/Profile   ·   1 / 2",
  {x:0.5,y:7.02,w:8,h:0.22,fontFace:MONO,fontSize:8.5,color:MUTE,margin:0,charSpacing:0.5});
s.addNotes("Run map (a) with management fanned: strategy sits deep inside IB, HR partly, OB barely. One circle per discipline is too coarse. Run map (b): the crossbars are between SUB-FIELDS, and OB flowed back into management from IB rather than out of it. Both maps treat integration as topical. Method is a third, structural integration point.");

/* ══ SLIDE 2 · FAQ ════════════════════════════════════ */
s=p.addSlide(); s.background={color:WHITE}; mark(s,false);
s.addText("Questions I expect",{x:0.5,y:0.52,w:8,h:0.5,fontFace:DISP,fontSize:28,bold:true,color:INK,margin:0});
s.addText("and the answers I am prepared to defend",{x:0.5,y:1.04,w:8,h:0.28,fontFace:BODY,fontSize:13,italic:true,color:MUTE,margin:0});

const faqs=[
 ["Isn't a shared difficulty just a shared tool? Physics and biology both need microscopes.",
  "It is not a tool, it is a definition. What makes a study international is comparison across countries — and comparison requires comparable populations. The constraint sits at the definition of the field, not at its equipment."],
 ["Doesn't strategy already cover this?",
  "Strategy is topical integration — the disciplines meet because their subject matter overlaps. This is structural: it binds every sub-field the moment it goes cross-national, whether or not the topics have anything in common."],
 ["Where is the evidence?",
  "Screening a commercial research panel of 334,976 members against one specialist professional criterion returned roughly twenty eligible people — near six per hundred thousand. Visible on the platform's own configuration screen before any money was committed."],
 ["Which discipline does this belong to?",
  "None of them, and that is the argument. It is a constraint on the act of comparing, so it sits between the circles rather than inside one."],
 ["How would you test it?",
  "Replicate the prevalence check across countries for the same specialist role, and report the distribution. If reachability varies sharply by country, comparative designs in every one of these sub-fields are resting on an assumption nobody states."],
 ["Are you claiming the existing maps are wrong?",
  "No. They are right about topical integration and honest that neither map resolves every classification difficulty. I am proposing a second axis they do not draw — not replacing theirs."]];

faqs.forEach((f,i)=>{
  const col=i%2, row=Math.floor(i/2);
  const x=0.5+col*6.42, y=1.58+row*1.78;
  s.addShape(p.ShapeType.rect,{x,y,w:6.15,h:1.62,fill:{color:PAPER},line:{color:RULE,width:1}});
  s.addText("Q",{x:x+0.24,y:y+0.16,w:0.3,h:0.24,fontFace:MONO,fontSize:10,bold:true,color:GOLD,margin:0});
  s.addText(f[0],{x:x+0.6,y:y+0.14,w:5.35,h:0.42,fontFace:DISP,fontSize:12.5,bold:true,color:INK,margin:0});
  s.addText("A",{x:x+0.24,y:y+0.66,w:0.3,h:0.24,fontFace:MONO,fontSize:10,bold:true,color:NAVY,margin:0});
  s.addText(f[1],{x:x+0.6,y:y+0.62,w:5.35,h:0.88,fontFace:BODY,fontSize:10.5,color:"454B54",margin:0});
});
s.addText("Yasir A. Malik   ·   github.com/AuditingAI/Profile   ·   2 / 2",
  {x:0.5,y:7.02,w:8,h:0.22,fontFace:MONO,fontSize:8.5,color:MUTE,margin:0,charSpacing:0.5});
s.addNotes("The microscope objection is the one that matters. Answer: it is not a shared tool, it is a shared definition — comparison across countries requires comparable populations, so the constraint sits at the definition of the field. Do not overclaim past that: this is a second axis, not a replacement.");

p.writeFile({fileName:"Malik_GEB7365_IB_Field_Map.pptx"}).then(f=>console.log("wrote",f));
