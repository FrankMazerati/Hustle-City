(() => {
  const canvas = document.getElementById("renderCanvas");
  const loading = document.getElementById("loading");
  const title = document.getElementById("view-title");
  const kicker = document.getElementById("view-kicker");
  const heading = document.getElementById("detail-heading");
  const copy = document.getElementById("detail-copy");
  const featureList = document.getElementById("feature-list");
  const tabs = [...document.querySelectorAll("[data-view]")];
  if (!window.BABYLON) { loading.textContent = "3D library did not load. Check your connection and reload."; return; }

  const engine = new BABYLON.Engine(canvas, true, { preserveDrawingBuffer:false, stencil:true, antialias:true, adaptToDeviceRatio:true });
  engine.setHardwareScalingLevel(Math.min(1.5, Math.max(1, window.devicePixelRatio || 1)));
  const scene = new BABYLON.Scene(engine);
  scene.clearColor = new BABYLON.Color4(.035,.052,.078,1);
  const camera = new BABYLON.ArcRotateCamera("creatorCamera", -Math.PI/2.2, 1.12, 115, new BABYLON.Vector3(0,8,0), scene);
  camera.attachControl(canvas, true);
  camera.lowerRadiusLimit = 12; camera.upperRadiusLimit = 260;
  camera.wheelPrecision = 45; camera.panningSensibility = 65;
  const hemi = new BABYLON.HemisphericLight("ambient", new BABYLON.Vector3(0,1,0), scene); hemi.intensity = .82;
  const key = new BABYLON.DirectionalLight("key", new BABYLON.Vector3(-.5,-1,.4), scene); key.position = new BABYLON.Vector3(45,90,-40); key.intensity = 1.15;

  const mats = {};
  function mat(name, color, metallic=0, rough=.55, emissive=null) {
    const m = new BABYLON.StandardMaterial(name, scene); m.diffuseColor = BABYLON.Color3.FromHexString(color);
    m.specularColor = new BABYLON.Color3(metallic ? .65 : .18, metallic ? .65 : .18, metallic ? .65 : .18);
    m.specularPower = metallic ? 80 : 24; m.alpha = 1;
    if (emissive) m.emissiveColor = BABYLON.Color3.FromHexString(emissive);
    mats[name]=m; return m;
  }
  mat("ground","#202a35"); mat("concrete","#707c89"); mat("glass","#34536a",.55,.18);
  mat("steel","#9da7b1",.82,.25); mat("gold","#c49a56",.78,.24); mat("dark","#111923",.35,.38);
  mat("white","#e7e6df",.15,.3); mat("blue","#277ca8",.5,.28); mat("red","#a74b4b",.45,.3);
  mat("green","#3f8b70",.35,.35); mat("purple","#7655a6",.4,.3); mat("neon","#e4bf77",.2,.3,"#6e4b1c");
  const groups = {him:[],hcta:[],fashion:[]};
  const all = [];
  function keep(mesh, group) { groups[group].push(mesh); all.push(mesh); return mesh; }
  function box(name, pos, scale, material, group, parent=null) {
    const m=BABYLON.MeshBuilder.CreateBox(name,{width:scale[0],height:scale[1],depth:scale[2]},scene);
    m.position.set(...pos); m.material=mats[material]; if(parent)m.parent=parent; return keep(m,group);
  }
  function cyl(name,pos,diam,height,material,group) {
    const m=BABYLON.MeshBuilder.CreateCylinder(name,{diameter:diam,height,tessellation:24},scene);
    m.position.set(...pos);m.material=mats[material];return keep(m,group);
  }
  function line(name, points, material, group, width=0.22) {
    const m=BABYLON.MeshBuilder.CreateTube(name,{path:points.map(p=>new BABYLON.Vector3(...p)),radius:width,tessellation:8},scene);
    m.material=mats[material];return keep(m,group);
  }
  function label(textValue, pos, group, color="#f0d39a") {
    const plane=BABYLON.MeshBuilder.CreatePlane("label-"+textValue.replace(/\W/g,""),{width:Math.max(8,textValue.length*.52),height:2.1},scene);
    plane.position.set(...pos);plane.billboardMode=BABYLON.Mesh.BILLBOARDMODE_ALL;
    const tex=new BABYLON.DynamicTexture("labelTexture",{width:1024,height:256},scene,false);
    tex.hasAlpha=true;tex.drawText(textValue,35,170,"bold 82px Arial",color,"transparent",true);
    const lm=new BABYLON.StandardMaterial("labelMat",scene);lm.diffuseTexture=tex;lm.emissiveColor=new BABYLON.Color3(.8,.8,.8);lm.disableLighting=true;lm.backFaceCulling=false;
    plane.material=lm;return keep(plane,group);
  }
  function base(group) { box(group+"-ground",[0,-1.2,0],[150,1,110],"ground",group); }
  function track(x1,x2,z,group,color) {
    box(group+"-bed",[(x1+x2)/2,-.45,z],[x2-x1,.28,4],"dark",group);
    for(let x=x1;x<=x2;x+=3.4) box(group+"-tie-"+x,[x,-.22,z],[.42,.22,5.2],"concrete",group);
    for(const dz of [-1.65,1.65]) box(group+"-rail-"+dz,[(x1+x2)/2,-.05,z+dz],[x2-x1,.24,.22],"steel",group);
    line(group+"-routeglow",[[x1,.15,z-1.65],[x2,.15,z-1.65]],color,group,.055);
  }
  function train(x,z,group,accent) {
    box(group+"-trainbody",[x,1.15,z],[24,2.5,5],"white",group);
    box(group+"-trainstripe",[x,1.3,z-2.54],[22,.42,.12],accent,group);
    box(group+"-trainnose",[x+12.2,1.18,z],[1.4,2.2,4.5],"steel",group);
    for(let i=-9;i<=9;i+=4.5) box(group+"-window"+i,[x+i,1.65,z-2.58],[3.1,1.05,.1],"glass",group);
    for(const wx of [-8,8]) for(const wz of [-1.7,1.7]) cyl(group+"-wheel"+wx+wz,[x+wx,.0,z+wz],1.0,.55,"dark",group);
    box(group+"-roof",[x,.2+2.5,z],[16,.18,3.7],"steel",group);
  }
  function station(group,x,z,name,accent) {
    box(group+"-platform",[x,0,z],[38,.5,13],"concrete",group);
    for(let px=x-15;px<=x+15;px+=10) { box(group+"-column"+px,[px,5,z+4],[.75,10,.75],"steel",group); box(group+"-roofbeam"+px,[px,10,z],[.9,.5,12],"steel",group); }
    box(group+"-canopy",[x,10.1,z],[40,.45,14],"dark",group);
    box(group+"-sign",[x,8,z-6.8],[12,2,.4],accent,group);
    label(name,[x,14,z],group);
  }
  // HIM: intercity terminal and long-distance passenger train. Illustrative scene only; not a map alignment.
  base("him"); station("him",0,8,"HIM CENTRAL TERMINAL","gold"); track(-48,48,-3,"him","gold"); train(-4,-3,"him","gold");
  box("him-concourse",[0,4,28],[52,8,22],"glass","him");
  box("him-concourse-roof",[0,8,28],[54,.7,24],"steel","him");
  label("INTERCITY ARRIVALS / DEPARTURES",[0,15,28],"him");
  box("him-arrivals-desk",[-13,1,35],[10,2,2],"gold","him");
  box("him-luggage",[-1,1,35],[10,2,2],"dark","him");
  // HCTA: separate local system, with three environment examples displayed as independent teaching pieces.
  base("hcta");
  track(-45,45,-25,"hcta","blue"); train(-8,-25,"hcta","blue"); station("hcta",-8,-14,"HCTA LOCAL STATION","blue");
  box("hcta-elevateddeck",[-30,7,15],[50,.8,5],"steel","hcta");
  for(let x=-52;x<=-8;x+=22) box("hcta-pier"+x,[x,3,15],[1.4,7,1.4],"concrete","hcta");
  track(-52,-8,15,"hcta","purple"); label("ELEVATED RAIL EXAMPLE",[-30,13,15],"hcta");
  box("hcta-undergroundcut",[28,-1,15],[46,3,8],"dark","hcta");
  track(5,51,15,"hcta","red"); label("UNDERGROUND / SURFACE MODE EXAMPLES",[28,5,15],"hcta");
  box("hcta-surfaceplatform",[28,0,31],[34,.5,8],"concrete","hcta");
  label("LOCAL ACCESS TO DISTRICTS + NEIGHBORHOODS",[0,17,-40],"hcta");
  // Fashion Hub: a vertical tower with 100 visible floor bands, no horizontal resort sprawl.
  base("fashion");
  box("fashion-plaza",[0,-.4,4],[70,.45,54],"concrete","fashion");
  // Tower body is deliberately tall and narrow; 100 floor bands are represented as repeated visible slabs.
  box("tower-core",[0,51,0],[22,102,22],"glass","fashion");
  for(let f=1;f<=100;f++){
    const y=f*1.02;
    box("tower-floor-"+f,[0,y,0],[23.2,.16,23.2],f%10===0?"gold":"steel","fashion");
    if(f%5===0) box("tower-lightband-"+f,[0,y+.15,-11.65],[18,.12,.12],"neon","fashion");
  }
  box("tower-podium",[0,2,0],[29,4,29],"dark","fashion");
  box("tower-crown",[0,103,0],[25,1.5,25],"gold","fashion");
  label("HUSTLE TOWERS · 100 FLOORS",[0,111,0],"fashion");
  box("mall-entry",[-24,2,0],[15,4,12],"glass","fashion");
  label("MALL / RETAIL",[ -24,6,0],"fashion");
  box("casino-entry",[24,2,0],[14,4,12],"dark","fashion");
  label("CASINO AREAS",[24,6,0],"fashion");
  box("concierge-entry",[0,2,23],[22,4,9],"white","fashion");
  label("FOOD CONCIERGE LOUNGES",[0,7,23],"fashion");
  box("helpdesk-a",[-21,1,20],[5,2,3],"gold","fashion");label("WELCOME DESK A",[-21,4,20],"fashion");
  box("helpdesk-b",[21,1,20],[5,2,3],"gold","fashion");label("WELCOME DESK B",[21,4,20],"fashion");
  label("HEAVENLY HALLWAY",[0,9,-22],"fashion");
  label("KICKING / SOCIAL AREAS · MEANING TO CONFIRM",[0,5,-34],"fashion","#d5b7ff");
  label("CAESAR'S PALACE · PLACEMENT TO CONFIRM",[0,13,35],"fashion");

  let current="him";
  function activate(view) {
    current=view;
    all.forEach(m=>m.setEnabled(false));
    groups[view].forEach(m=>m.setEnabled(true));
    tabs.forEach(t=>t.classList.toggle("active",t.dataset.view===view));
    if(view==="him"){
      kicker.textContent="INTERCITY RAIL";title.textContent="Hustle International Metro";
      heading.textContent="Intercity arrival and departure";
      copy.textContent="HIM connects Hustle City with other cities and regions. Its terminal is the arrival point for Frank Maserati and his companion. Exact city routes and station locations remain unapproved.";
      features(["Intercity service","Passenger terminal","Arrivals and departures","City-to-city expansion"]);
      camera.setTarget(new BABYLON.Vector3(0,7,8));camera.radius=115;
    } else if(view==="hcta"){
      kicker.textContent="LOCAL CITY TRANSIT";title.textContent="Hustle City Transit Authority";
      heading.textContent="One local network, three operating environments";
      copy.textContent="HCTA connects downtown, all six central districts, and every designated outer neighborhood. Elevated, underground, and street-level operation are supported design environments; actual line alignments and mode assignments remain open.";
      features(["Elevated rail","Underground rail","Street-level rail","HIM transfer access","District and neighborhood stations","Compatible vehicle / track families"]);
      camera.setTarget(new BABYLON.Vector3(0,2,0));camera.radius=140;
    } else {
      kicker.textContent="FASHION HUB · VERTICAL LANDMARK";title.textContent="Hustle Towers — 100 Floors";
      heading.textContent="A vertical destination, not a sprawling campus";
      copy.textContent="This early massing preview shows a narrow, 100-floor tower. Requested program includes malls, multiple casino areas, multiple food concierge lounges, multiple welcoming help desks, the Heavenly Hallway, and kicking areas. Caesar's Palace placement is still to be confirmed.";
      features(["100-floor vertical tower","Mall / retail spaces","Multiple casino areas","Multiple food concierge lounges","Multiple welcome help desks","Heavenly Hallway","Kicking areas — meaning to confirm","Caesar's Palace — relationship to confirm"]);
      camera.setTarget(new BABYLON.Vector3(0,48,0));camera.radius=165;
    }
  }
  function features(items){featureList.innerHTML=items.map(x=>'<div class="feature"><strong>'+x.replace(/</g,"&lt;")+'</strong><span>Requested design element · detail pending review</span></div>').join("");}
  tabs.forEach(t=>t.addEventListener("click",()=>activate(t.dataset.view)));
  document.getElementById("resetCamera").addEventListener("click",()=>{camera.alpha=-Math.PI/2.2;camera.beta=1.12;camera.radius=current==="fashion"?165:current==="hcta"?140:115;camera.setTarget(current==="fashion"?new BABYLON.Vector3(0,48,0):current==="hcta"?new BABYLON.Vector3(0,2,0):new BABYLON.Vector3(0,7,8));});
  activate("him");
  engine.runRenderLoop(()=>scene.render());
  window.addEventListener("resize",()=>engine.resize());
  loading.classList.add("hidden");
})();