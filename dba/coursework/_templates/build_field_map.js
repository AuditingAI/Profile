const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout="LAYOUT_WIDE"; p.author="Yasir A. Malik";
p.title="A Map of the International Business Field";
const NAVY="1F4E79",DEEP="0E2237",GOLD="8A6410",GOLDL="D2A73F",
      PAPER="FBFAF7",INK="14171C",MUTE="767D86",SOFT="E9EFF6",WARM="FBF6EA",
      WARMB="E4D3A8",WHITE="FFFFFF",RULE="D8D4CB";
const DISP="Georgia",BODY="Cambria",MONO="Courier New";
const W=13.33;
const s=p.addSlide(); s.background={color:PAPER};

s.addShape(p.ShapeType.rect,{x:0,y:0,w:W,h:1.3,fill:{color:DEEP},line:{width:0}});
s.addText([{text:"Audit ",options:{bold:true,color:GOLDL}},
           {text:"the ",options:{italic:true,color:"8C949E",fontSize:9}},
           {text:"Algorithm",options:{bold:true,color:GOLDL}}],
  {x:0.5,y:0.14,w:3,h:0.26,fontFace:DISP,fontSize:11,margin:0});
s.addText("GEB 7365  ·  after Chandra & Newburry (1997), Figure 1, p. 397",
  {x:0.5,y:0.44,w:7,h:0.24,fontFace:MONO,fontSize:9,color:GOLDL,margin:0,charSpacing:1.2});
s.addText("The Field Never Integrated",
  {x:0.5,y:0.68,w:7.2,h:0.5,fontFace:DISP,fontSize:30,bold:true,color:WHITE,margin:0});
s.addShape(p.ShapeType.rect,{x:8.15,y:0.42,w:0.03,h:0.72,fill:{color:GOLDL},line:{width:0}});
s.addText("Two maps, one diagnosis: International Business is where five disciplines overlap — and they only ever met on strategy.",
  {x:8.35,y:0.42,w:4.5,h:0.75,fontFace:BODY,fontSize:12.5,italic:true,color:"DCE3EA",margin:0});

s.addShape(p.ShapeType.rect,{x:0.5,y:1.55,w:5.55,h:3.45,fill:{color:WHITE},line:{color:RULE,width:1}});
s.addText("(A)",{x:0.72,y:1.64,w:0.38,h:0.24,fontFace:MONO,fontSize:9.5,bold:true,color:NAVY,margin:0,charSpacing:1.1});
s.addText("IB as the overlap",{x:1.16,y:1.62,w:2.0,h:0.26,fontFace:DISP,fontSize:14,bold:true,color:INK,margin:0});
const ring=(x,y,w,h)=>s.addShape(p.ShapeType.ellipse,
  {x,y,w,h,fill:{color:WHITE,transparency:100},line:{color:NAVY,width:1.25}});
ring(1.62,2.12,0.80,1.95); ring(2.02,2.02,1.05,1.05); ring(3.20,2.10,1.05,1.05);
ring(1.72,3.28,1.00,1.00); ring(3.32,3.32,1.00,1.00);
s.addShape(p.ShapeType.ellipse,{x:2.15,y:2.35,w:1.95,h:1.95,
  fill:{color:SOFT,transparency:22},line:{color:NAVY,width:2}});
s.addText("IB",{x:2.15,y:3.06,w:1.95,h:0.45,align:"center",fontFace:DISP,fontSize:22,bold:true,color:NAVY,margin:0});
const lab=(t,x,y,w)=>s.addText(t,{x,y,w,h:0.22,align:"center",fontFace:MONO,fontSize:9,color:"454B54",margin:0});
lab("Economics",0.96,2.30,1.0); lab("Finance",2.05,1.93,1.0); lab("Accounting",3.25,1.93,1.0);
lab("Marketing",1.24,4.30,1.0); lab("Management",3.42,4.34,1.15);
s.addText("The field is defined by where the disciplines cross — not by a territory of its own.",
  {x:0.72,y:4.60,w:5.1,h:0.32,fontFace:BODY,fontSize:11,color:"454B54",margin:0});

s.addShape(p.ShapeType.rect,{x:6.28,y:1.55,w:6.55,h:3.45,fill:{color:WHITE},line:{color:RULE,width:1}});
s.addText("(B)",{x:6.50,y:1.64,w:0.38,h:0.24,fontFace:MONO,fontSize:9.5,bold:true,color:NAVY,margin:0,charSpacing:1.1});
s.addText("Five parallel descents",{x:6.94,y:1.62,w:2.6,h:0.26,fontFace:DISP,fontSize:14,bold:true,color:INK,margin:0});
const cols=[{x:7.05,top:2.18,name:"ECON"},{x:8.10,top:2.32,name:"FIN"},
 {x:9.15,top:2.52,name:"ACCT"},{x:10.20,top:2.40,name:"MGMT"},{x:11.25,top:2.60,name:"MKTG"}];
cols.forEach(c=>{
  s.addText(c.name,{x:c.x-0.42,y:c.top-0.28,w:0.84,h:0.22,align:"center",
    fontFace:MONO,fontSize:9,bold:true,color:NAVY,margin:0});
  s.addShape(p.ShapeType.line,{x:c.x,y:c.top,w:0,h:4.30-c.top,
    line:{color:NAVY,width:2.25,endArrowType:"triangle"}});
});
const bar=(x1,x2,y)=>s.addShape(p.ShapeType.rect,{x:x1,y,w:x2-x1,h:0.13,
    fill:{color:NAVY,transparency:55},line:{color:NAVY,width:0.75}});
bar(7.05,8.10,2.86); bar(8.10,9.15,3.24); bar(10.20,11.25,3.52);
s.addShape(p.ShapeType.rect,{x:6.72,y:4.36,w:5.10,h:0.36,
  fill:{color:WHITE,transparency:100},line:{color:NAVY,width:1.25,dashType:"dash"}});
s.addText("Minor IB field integration — only on strategy issues",
  {x:6.72,y:4.43,w:5.10,h:0.24,align:"center",fontFace:MONO,fontSize:9.5,color:NAVY,margin:0});
s.addShape(p.ShapeType.rect,{x:12.02,y:2.86,w:0.20,h:0.13,
  fill:{color:NAVY,transparency:55},line:{color:NAVY,width:0.75}});
s.addText("some\nintegration",{x:12.28,y:2.76,w:0.9,h:0.38,fontFace:MONO,fontSize:8,color:MUTE,margin:0});
s.addText("time",{x:12.28,y:3.92,w:0.9,h:0.22,fontFace:MONO,fontSize:8,color:MUTE,margin:0});
s.addText("Each discipline developed on its own track. The bars are the only crossings.",
  {x:6.50,y:4.80,w:6.1,h:0.28,fontFace:BODY,fontSize:11,color:"454B54",margin:0});

s.addShape(p.ShapeType.rect,{x:0.5,y:5.20,w:12.33,h:1.72,
  fill:{color:WARM},line:{color:GOLD,width:2,dashType:"dash"}});
s.addText("THE EXTENSION — A SECOND CROSSBAR, THIRTY YEARS ON",
  {x:0.78,y:5.34,w:9,h:0.24,fontFace:MONO,fontSize:9,bold:true,color:GOLD,margin:0,charSpacing:1.3});
s.addText("Strategy was never the only place these five could meet. Method is the other one.",
  {x:0.78,y:5.60,w:9.6,h:0.36,fontFace:DISP,fontSize:17,bold:true,color:INK,margin:0});
s.addText("Finance, accounting, marketing, management and economics all become international at the same moment — when the question is asked in more than one country at once. Every one of them then hits the same wall: reaching the same specialist population in each country. That constraint is field-wide, and it is not a strategy issue.",
  {x:0.78,y:6.00,w:9.6,h:0.80,fontFace:BODY,fontSize:11.5,color:"454B54",margin:0});
s.addShape(p.ShapeType.line,{x:10.62,y:5.42,w:0,h:1.28,line:{color:WARMB,width:1}});
s.addText("6",{x:10.85,y:5.50,w:1.2,h:0.64,fontFace:DISP,fontSize:40,bold:true,color:GOLD,margin:0});
s.addText("eligible per 100,000\nmeasured, before fielding",
  {x:10.85,y:6.16,w:1.95,h:0.44,fontFace:MONO,fontSize:8.5,color:MUTE,margin:0});
s.addText("Yasir A. Malik   ·   github.com/AuditingAI/Profile",
  {x:0.5,y:7.02,w:8,h:0.24,fontFace:MONO,fontSize:8.5,color:MUTE,margin:0,charSpacing:0.5});
s.addNotes("Chandra & Newburry map the field as an overlap of five disciplines that developed in parallel and integrated only on strategy. The extension: method is a second integration point — every discipline hits the same population-reachability wall the moment the question becomes cross-national.");
p.writeFile({fileName:"Malik_GEB7365_IB_Field_Map.pptx"}).then(f=>console.log("wrote",f));
