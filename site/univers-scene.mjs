/** Illustrations procédurales, sans images ni données d'observation.
 * Les positions sont déterministes. Le mélange dépend du défilement, pas du temps.
 * WebGL dessine les nuages ; un rendu Canvas conserve les scènes sans accélération.
 */
const TAU = Math.PI * 2;
const mix = (a, b, t) => a + (b - a) * t;
const GOLD = [1, .76, .42], BLUE = [.53, .73, 1], WHITE = [.93, .96, 1];

export function buildCosmicShapes(count) {
  let seed = 31973;
  const random = () => ((seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0) / 4294967296);
  const normal = () => Math.sqrt(-2 * Math.log(Math.max(random(), .000001))) * Math.cos(TAU * random());
  const nodes = Array.from({length: 23}, () => [random() * 2.5 - 1.25, random() * 1.8 - .9, random() - .5]);
  const shapes = [];
  for (let scene = 0; scene < 13; scene++) {
    const data = new Float32Array(count * 8);
    for (let i = 0; i < count; i++) {
      const a = random(), b = random(), c = random(), d = random();
      let x, y, z, color = BLUE, opacity = .65, size = .65 + Math.pow(d, 6) * 3;
      if (scene === 9 || scene === 12) {
        const bulge = i % 6 === 0;
        const r = bulge ? Math.abs(normal()) * .19 : Math.pow(a, .75) * 1.5;
        const arm = i % 2;
        const angle = i % 7 < 2 ? b * TAU : arm * TAU / 2 + 4.1 * Math.log(r + .22) + normal() * (.21 + .13 / (r + .2));
        const px = Math.cos(angle) * r, py = Math.sin(angle) * r;
        x = px * .94 - py * .2; y = px * .24 + py * .65;
        z = normal() * (bulge ? .12 : .026) * (1.3 - Math.min(r, 1));
        const tone = Math.min(1, Math.max(0, (r - .1) / .8));
        color = i % 9 < 2 ? WHITE : [1,.86,.62].map((value,k)=>mix(value,BLUE[k],tone));
        opacity = bulge ? .62 : .18 + b * .7;
        size *= bulge ? .85 : 1;
        if (scene === 9) { x *= .86; y *= .86; }
      } else if (scene === 0) {
        const r = .16 + a * 1.7, angle = b * TAU;
        x = Math.cos(angle) * r; y = Math.sin(angle) * r * .73; z = (c - .5) * .8;
        opacity = .05 + Math.pow(a, 3) * .38;
        color = i % 4 ? BLUE : GOLD;
      } else if (scene === 1) {
        const n = 24, plane = i % 5;
        x = ((i % n) / (n - 1) - .5) * 2.4 + normal() * .007;
        y = ((Math.floor(i / n) % n) / (n - 1) - .5) * 1.5 + normal() * .007;
        z = (plane - 2) * .2; color = plane % 2 ? BLUE : GOLD;
        opacity = .38; size *= .8;
      } else if (scene === 2 || scene === 5) {
        x = normal() * .64; y = normal() * .45; z = (c - .5) * .8;
        color = scene === 2 ? (i % 5 ? GOLD : [1,.42,.2]) : (i % 4 ? BLUE : GOLD);
        opacity = .12 + b * .35; size = 1 + d * 2.1;
      } else if (scene === 3 || scene === 4) {
        const group = i % 5;
        const centers = [[0,0],[.88,.48],[-.75,-.53],[.85,-.63],[-.95,.53]];
        const nucleon = Math.floor(i / 5) % (scene === 3 ? 3 : 4);
        const angle = nucleon * TAU / (scene === 3 ? 3 : 4);
        const offset = scene === 3 ? .135 : .1;
        const rad = Math.cbrt(a) * (scene === 3 ? .078 : .105), az = b * TAU;
        const cosPolar = c * 2 - 1, sinPolar = Math.sqrt(1 - cosPolar * cosPolar);
        x = centers[group][0] + Math.cos(angle) * offset + rad * sinPolar * Math.cos(az);
        y = centers[group][1] + Math.sin(angle) * offset + rad * sinPolar * Math.sin(az);
        z = rad * cosPolar;
        color = nucleon % 2 ? BLUE : GOLD; opacity = .4; size *= .8;
      } else if (scene === 6) {
        const group = i % 7 < 5 ? 0 : i % 7 === 5 ? 1 : 2;
        const centers = [[.08,.04],[-.74,-.55],[.97,.6]];
        const scale = group === 0 ? 1 : .42;
        const nucleus = i % 14 === 0;
        // Nuage probabiliste, pas une orbite d'électron ; tailles schématiques.
        const r = nucleus ? Math.cbrt(a) * .035 : -Math.log(Math.max(.00001,a * b)) * .14;
        const angle = c * TAU, polar = random() * 2 - 1, s = Math.sqrt(1 - polar * polar);
        x = centers[group][0] + r * s * Math.cos(angle) * scale;
        y = centers[group][1] + r * s * Math.sin(angle) * scale;
        z = r * polar * scale;
        color = nucleus ? GOLD : BLUE; opacity = nucleus ? .24 : .15 + d * .4;
        size = nucleus ? 1 : .55 + d;
      } else if (scene === 7 || scene === 8 || scene === 11) {
        const n = i % nodes.length, start = nodes[n];
        const end = nodes[(n + 1 + n % 4) % nodes.length];
        const along = a;
        const diffuse = scene === 7 ? .12 : scene === 8 ? .055 : .027;
        const curl = Math.sin(along * Math.PI) * .13;
        x = mix(start[0], end[0], along) + normal() * diffuse;
        y = mix(start[1], end[1], along) + Math.sin(n * 2.3) * curl + normal() * diffuse;
        z = mix(start[2], end[2], along) + normal() * diffuse;
        color = scene === 11 ? (i % 3 ? GOLD : BLUE) : BLUE;
        opacity = scene === 7 ? .075 : scene === 8 ? .28 : .36;
        if (scene === 8 && i % 6 === 0) {
          x = start[0] + normal() * .014; y = start[1] + normal() * .014; z = start[2];
          color = GOLD; opacity = .8; size *= 1.7;
        }
      } else if (scene === 10) {
        const central = i % 5 < 2, r = central ? Math.cbrt(a) * .115 : .2 + Math.sqrt(a) * 1.12;
        const angle = b * TAU;
        x = Math.cos(angle) * r; y = Math.sin(angle) * r * (central ? 1 : .32); z = (c - .5) * (central ? .2 : .02);
        color = GOLD; opacity = central ? .055 : .12; size *= central ? .45 : .5;
      }
      // Étoiles d'arrière-plan seulement pour les époques où elles existent.
      if ((scene >= 8 || scene === 12) && i > count * .965) {
        x = (a - .5) * 5.8; y = (b - .5) * 3.4; z = (c - .5) * 1.5;
        color = i % 4 ? BLUE : GOLD; opacity = .2 + d * .7; size = .7 + Math.pow(d, 10) * 4;
      }
      const off = i * 8;
      data.set([x,y,z,...color,opacity,size],off);
    }
    shapes.push(data);
  }
  return shapes;
}

const VERTEX = `
attribute vec3 aFrom; attribute vec3 aTo;
attribute vec4 cFrom; attribute vec4 cTo;
attribute float sFrom; attribute float sTo;
uniform vec2 uResolution; uniform vec2 uCenter;
uniform float uMix; uniform float uTime; uniform float uScale; uniform float uDpr; uniform float uCloud;
varying vec4 vColor;
void main(){
  vec3 p=mix(aFrom,aTo,uMix);
  float a=sin(uTime*.045)*.07;
  p.xz=mat2(cos(a),-sin(a),sin(a),cos(a))*p.xz;
  p.xy+=vec2(sin(p.y*5.+uTime*.14),cos(p.x*4.+uTime*.12))*.008*uCloud;
  float perspective=2.8/(2.8+p.z*.45);
  vec2 pos=uCenter+p.xy*uScale*perspective;
  gl_Position=vec4(pos/uResolution*2.-1.,0.,1.);
  gl_Position.y=-gl_Position.y;
  gl_PointSize=clamp(mix(sFrom,sTo,uMix)*3.6*uDpr*perspective,1.,34.);
  vColor=mix(cFrom,cTo,uMix);
  float leftFade=smoothstep(.24,.49,pos.x/uResolution.x);
  vColor.a*=mix(leftFade,1.,step(uResolution.x,760.));
}
`;
const FRAGMENT = `
precision mediump float; varying vec4 vColor;
void main(){
  float r=length(gl_PointCoord-.5)*2.;
  if(r>1.) discard;
  float core=exp(-r*r*24.);
  float halo=exp(-r*r*5.)*.13;
  gl_FragColor=vec4(vColor.rgb, (core+halo)*vColor.a);
}
`;
const BACK_VERTEX = `attribute vec2 aPosition; varying vec2 vUV; void main(){vUV=aPosition*.5+.5;gl_Position=vec4(aPosition,0.,1.);}`;
const BACK_FRAGMENT = `
precision mediump float;
varying vec2 vUV; uniform vec2 uResolution; uniform vec2 uCenter;
uniform float uScale; uniform float uTime; uniform float uFrom; uniform float uTo; uniform float uMix;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p); f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1.,0.)),f.x),mix(hash(i+vec2(0.,1.)),hash(i+1.),f.x),f.y);}
float fbm(vec2 p){float n=0.;float a=.5;for(int i=0;i<4;i++){n+=a*noise(p);p=p*2.04+3.8;a*=.5;}return n;}
vec3 field(float scene,vec2 p){
  vec3 gold=vec3(.94,.72,.44), blue=vec3(.27,.48,.76);
  float n=fbm(p*5.+uTime*.004);
  float r=length(p);
  if(scene>11.5 || (scene>8.5 && scene<9.5)){
    vec2 q=vec2(p.x*.98+p.y*.3,(-p.x*.24+p.y*.94)/.64);
    float rr=length(q), a=atan(q.y,q.x);
    float arms=pow(.5+.5*cos(a*2.-8.2*log(rr+.22)+n*.8),5.);
    float disk=exp(-rr*1.8)*(1.-smoothstep(.8,1.7,rr));
    float cloud=pow(n,2.7)*arms*disk;
    return blue*cloud*3.6+gold*exp(-rr*10.)*1.3+gold*pow(n,3.)*disk*.18;
  }
  if(scene>1.5 && scene<2.5) return gold*pow(n,2.)*exp(-r*r*.9)*.55;
  if(scene>5.5 && scene<6.5){
    float atom=exp(-length(p-vec2(.08,.04))*5.);
    float farther=exp(-length(p-vec2(-.74,-.55))*13.)+exp(-length(p-vec2(.97,.6))*13.);
    return blue*(atom*.17+farther*.09)+gold*exp(-length(p-vec2(.08,.04))*45.)*.55;
  }
  if(scene>4.5 && scene<5.5) return blue*n*exp(-r*r)*.13;
  if(scene>9.5 && scene<10.5){
    if(r<.116){float z=sqrt(1.-(r/.116)*(r/.116));return vec3(1.,.68,.25)*(.55+.45*z)*(.7+.3*fbm(p*180.));}
    return gold*exp(-r*13.)*.7;
  }
  if(scene>6.5 && scene<8.5) return blue*pow(n,4.)*exp(-r*r*.3)*.24;
  if(scene>10.5 && scene<11.5) return gold*pow(n,5.)*exp(-r*r*.5)*.24;
  return vec3(0.);
}
void main(){
  vec2 pixel=vec2(vUV.x,1.-vUV.y)*uResolution;
  vec2 p=(pixel-uCenter)/uScale;
  vec3 light=mix(field(uFrom,p),field(uTo,p),uMix);
  float mask=mix(smoothstep(.25,.56,vUV.x),1.,step(uResolution.x,760.));
  light*=mask;
  gl_FragColor=vec4(vec3(.051,.063,.059)+light,.92);
}
`;

function shader(gl,type,source){
  const s=gl.createShader(type); gl.shaderSource(s,source); gl.compileShader(s);
  if(!gl.getShaderParameter(s,gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
  return s;
}
function program(gl,vs,fs){
  const p=gl.createProgram(), v=shader(gl,gl.VERTEX_SHADER,vs), f=shader(gl,gl.FRAGMENT_SHADER,fs);
  gl.attachShader(p,v); gl.attachShader(p,f); gl.linkProgram(p);
  gl.deleteShader(v); gl.deleteShader(f);
  if(!gl.getProgramParameter(p,gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
  return p;
}
function attr(gl,p,name,size,stride,offset){
  const id=gl.getAttribLocation(p,name); if(id<0)return;
  gl.enableVertexAttribArray(id); gl.vertexAttribPointer(id,size,gl.FLOAT,false,stride,offset);
}
function uniforms(gl,p,values){
  for(const [key,value] of Object.entries(values)){
    const loc=gl.getUniformLocation(p,key);
    if(Array.isArray(value))gl.uniform2f(loc,...value); else gl.uniform1f(loc,value);
  }
}

export function createCosmos(originalCanvas) {
  let canvas=originalCanvas, ctx=null, gl=null, main=null, background=null, lost=false;
  const count=matchMedia('(max-width: 760px)').matches ? 16000 : 48000;
  const shapes=buildCosmicShapes(count);
  let buffers, quad, maxAttributes=0, previousFrom=-1, previousTo=-1;
  const fallback=()=>{
    if(gl){ const fresh=canvas.cloneNode(false); canvas.replaceWith(fresh); canvas=fresh; }
    gl=null; ctx=canvas.getContext('2d'); canvas.dataset.renderer='canvas';
  };
  try{
    gl=canvas.getContext('webgl',{alpha:true,antialias:false,depth:false,premultipliedAlpha:false});
    if(!gl) fallback();
    else {
      main=program(gl,VERTEX,FRAGMENT); background=program(gl,BACK_VERTEX,BACK_FRAGMENT);
      buffers=[gl.createBuffer(),gl.createBuffer()]; quad=gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER,quad); gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),gl.STATIC_DRAW);
      canvas.dataset.renderer='webgl';maxAttributes=gl.getParameter(gl.MAX_VERTEX_ATTRIBS);
      canvas.addEventListener('webglcontextlost',e=>{e.preventDefault(); lost=true;});
    }
  }catch(error){ console.warn('Rendu WebGL indisponible, passage au rendu Canvas.',error.message); fallback(); }
  let w=0,h=0,dpr=1;
  function resize(){
    const box=canvas.getBoundingClientRect(); w=box.width;h=box.height;dpr=Math.min(devicePixelRatio||1,1.75);
    canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);
    if(ctx)ctx.setTransform(dpr,0,0,dpr,0,0);
  }
  function draw({from=12,to=12,blend=0,time=0,phase=0}){
    if(lost){fallback();resize();lost=false;}
    if(!w||!h)return;
    const mobile=w<=760;
    const intro=from===12&&to===12;
    const center=[w*(mobile?.52:.73),h*(intro&&!mobile?.3:.47)];
    let scale=Math.min(w*(mobile?.41:.38),h*.77);
    const inflationWeight=(from===1?1-blend:0)+(to===1?blend:0);
    scale*=1+inflationWeight*(phase-.3)*.6;
    if(gl){
      gl.viewport(0,0,canvas.width,canvas.height);gl.disable(gl.DEPTH_TEST);gl.disable(gl.BLEND);
      gl.useProgram(background);gl.bindBuffer(gl.ARRAY_BUFFER,quad);attr(gl,background,'aPosition',2,0,0);
      const common={uResolution:[w,h],uCenter:center,uScale:scale,uTime:time};
      uniforms(gl,background,{...common,uFrom:from,uTo:to,uMix:blend});
      gl.drawArrays(gl.TRIANGLES,0,6);
      // Le programme suivant réutilise les emplacements d'attributs : réinitialiser
      // les tableaux évite qu'un ancien buffer court borne un nouveau drawArrays.
      const max=maxAttributes;
      for(let i=0;i<max;i++)gl.disableVertexAttribArray(i);
      gl.useProgram(main);
      [from,to].forEach((scene,index)=>{
        gl.bindBuffer(gl.ARRAY_BUFFER,buffers[index]);
        if((index===0?previousFrom:previousTo)!==scene)gl.bufferData(gl.ARRAY_BUFFER,shapes[scene],gl.STATIC_DRAW);
        attr(gl,main,index===0?'aFrom':'aTo',3,32,0);
        attr(gl,main,index===0?'cFrom':'cTo',4,32,12);
        attr(gl,main,index===0?'sFrom':'sTo',1,32,28);
      });
      previousFrom=from;previousTo=to;
      uniforms(gl,main,{...common,uMix:blend,uDpr:dpr,uCloud:1});
      gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE);
      gl.drawArrays(gl.POINTS,0,count);
      for(let i=0;i<max;i++)gl.disableVertexAttribArray(i);
    }else if(ctx){
      ctx.clearRect(0,0,w,h);
      const a=shapes[from], b=shapes[to], stride=Math.ceil(count/6500);
      for(let i=0;i<count;i+=stride){
        const o=i*8, x=center[0]+mix(a[o],b[o],blend)*scale, y=center[1]+mix(a[o+1],b[o+1],blend)*scale;
        const opacity=mix(a[o+6],b[o+6],blend)*(mobile?1:Math.max(0,Math.min(1,(x/w-.27)/.25)));
        const c=[0,1,2].map(k=>Math.round(mix(a[o+3+k],b[o+3+k],blend)*255));
        ctx.fillStyle=`rgba(${c.join(',')},${opacity})`;
        const size=mix(a[o+7],b[o+7],blend);
        ctx.beginPath();ctx.arc(x,y,Math.max(.4,size*.7),0,TAU);ctx.fill();
      }
    }
    canvas.dataset.scene=String(blend>.5?to:from);
  }
  resize();
  return {draw,resize,get canvas(){return canvas;},get renderer(){return gl?'webgl':'canvas';}};
}
