#!/usr/bin/env python3
"""Build separate, whitelist-only public and private static distributions."""
from __future__ import annotations
import hashlib
import json
import re
import shutil
from pathlib import Path
from translations import load_translations, source_fingerprint

ROOT=Path(__file__).resolve().parents[1]
TOPICS={
 "力学":r"mechanic|inertia|brick|bounc|rolling|mass|orbit|comet|satellite|oscillat|pendulum|运动|母球|转动|弹簧|引力|受力|动量|刚体|振动",
 "电磁学":r"electri|magnet|resistor|circuit|induct|capacitan|LC\b|电场|磁场|电路|电阻|二极管|回旋",
 "热学与统计":r"heat|therm|gas|entropy|zipper|temperature|black.?body|热|气体|温度|熵|热容",
 "光学与波动":r"lens|optic|diffrac|photon|light|resonator|wave|光纤|干涉|偏振|光学|电光|衍射|光束",
 "流体与连续介质":r"fluid|water|flow|hydro|added mass|droplet|液体|流体|水流|压强",
 "相对论与天体":r"relativ|dark matter|galaxy|black hole|rocket|spacetime|星际|相对论|黑洞|引力波|天体",
 "量子与现代物理":r"quantum|superconduct|molecular|nuclear|electron gas|量子|超导|分子|原子核",
 "数学物理":r"quaternion|möbius|icosahedron|lattice|4d sun|boundary condition|四元数|本征"
}
CONTEST_NAMES={'CPhO':'全国中学生物理竞赛','PanPhO':'泛珠三角物理奥林匹克'}
PUBLIC_KEYS={"id","contest","contest_label","year","stage","role","question","title","granularity","parent_id","source_page","source_tier","topics","tag_status","difficulty","model","teaching_tags","domain","skills"}

def label(r):
    r=dict(r)
    r['contest_label']=CONTEST_NAMES.get(r['contest'],r['contest'])
    r.pop('math',None)
    if r["contest"]=="CPhO":
        stage={"semifinal-theory":"复赛理论","final-theory":"决赛理论","final-experiment-1":"决赛实验一","final-experiment-2":"决赛实验二"}.get(r["stage"],r["stage"])
        r["stage"]=stage
        if r['granularity']!='problem':r["title"]=f"第{r.get('edition',r['year']-1983)}届 · {stage} · "+{"problem":"试题","solution":"参考解答","combined":"试题与解答"}.get(r["role"],"资料")
        else:r['title']=r['title'].replace('semifinal-theory','复赛理论').replace('final-theory','决赛理论')
    if r["contest"]=="PanPhO":
        stage={"paper-1":"综合试卷一","paper-2":"综合试卷二","mechanics":"力学基础试"}.get(r["stage"],r["stage"])
        r["stage"]=stage
        if r["granularity"]!="problem":r["title"]=f"泛珠 {r['year']} · {stage} · "+("题目" if r["role"]=="problem" else "参考解答")
    text=r.get("title","")+" "+r.get("text","")[:16000]
    if r["contest"]=="Physics Cup":
        text=r["title"] # avoid broad solution text overwhelming topic labels.
    r["topics"]=[k for k,p in TOPICS.items() if re.search(p,text,re.I)][:4]
    if r["stage"]=="力学基础试":r["topics"]=["力学"]
    r["difficulty"]="pending"
    r["tag_status"]="preliminary"
    return r

def supplement():
    urls={2022:["https://www.gaokzx.com/c/202209/64909.html","https://www.gaokzx.com/c/202211/65667.html"],2023:["https://www.zizzs.com/Fup/document/202309/09-16_125141-10170.pdf","https://www.zizzs.com/c/202309/122245.html"],2024:["https://www.gaokzx.com/gk/shitiku/128220.html","https://www.sohu.com/a/822589502_472787"],2025:["https://www.gaokzx.com/gk/shitiku/146976.html","https://www.gaokzx.com/gk/gaozhongjingsai/148500.html"],2026:["https://www.enjoyphysics.cn/ShowPaper/1740","https://www.gk100.com/read_2339838566.htm"]}
    return [dict(id=f"cpho-{y}-{i}-source",contest="CPhO",year=y,stage="复赛补充入口" if i==0 else "决赛补充入口",role="combined",granularity="paper",title=f"第{y-1983}届 · "+("复赛" if i==0 else "决赛")+" · 待核验来源",source_page=u,url=u,source_tier="third_party",collection_status="pending",files=[],archive_note="仅定位到第三方入口，尚未完整收齐或核对原件。") for y,arr in urls.items() for i,u in enumerate(arr)]

def main():
    raw=json.loads((ROOT/"catalog/extended-resources.json").read_text())
    # Publish only existing usable originals; never emit source-only placeholders.
    def usable(r):
        if r['contest']=='Physics Cup' and r['role']=='solution' and not r.get('solution_attachments'):return False
        return bool(r.get('reader_html')) or any(f['path'].endswith('.pdf') and (ROOT/f['path']).is_file() for f in r.get('files',[]))
    resources=[label(r) for r in raw if usable(r)]
    resource_ids={r['id'] for r in resources}
    questions=[label(q) for q in json.loads((ROOT/"catalog/questions.json").read_text()) if q.get('parent_id','').removesuffix('-answer') in resource_ids and usable(q)]
    teach_path=ROOT/"catalog/teaching-analysis.json"
    teach=json.loads(teach_path.read_text()) if teach_path.exists() else {}
    for q in questions:
        t=teach.get(q['id'])
        if not t:continue
        q['difficulty']=t['difficulty'];q['model']=t['model'];q['teaching_tags']=t['teaching_tags']
        q['domain']=t['domain'];q['skills']=t['skills'];q['tag_status']='analysed'
        if t.get('better_title'):q['title']=t['better_title']
        q['teaching']=t['teaching'] # stripped from the public build by PUBLIC_KEYS
    translations=load_translations()
    question_ids={q['id'] for q in questions}
    assert set(translations)<=question_ids, ('Translations without usable questions',set(translations)-question_ids)
    for q in questions:
        if q['id'] in translations:
            assert q['role']=='problem' and q['contest'] in ('Physics Cup','PLANCKS')
            q['translation_zh']=dict(translations[q['id']],source_sha256=source_fingerprint(q))
            q['title_zh']=translations[q['id']]['title']
    valid_ids=resource_ids|{q['id'] for q in questions}
    for q in questions:q['solution_ids']=[x for x in q.get('solution_ids',[]) if x in valid_ids]
    for mode in ("public","internal"):
        base=ROOT/"sites"/mode;dist=base/"dist";dist.mkdir(parents=True,exist_ok=True)
        for name in ("index.html","app.css","app.js","reader.css"):shutil.copyfile(ROOT/"web"/name,dist/name)
        html=(dist/'index.html').read_text().replace('<!-- MATH_SCRIPTS -->','<script defer src="math-config.js"></script><script defer src="vendor/tex-svg-full.js"></script>' if mode=='internal' else '')
        (dist/'index.html').write_text(html)
        if mode=='internal':
            shutil.copytree(ROOT/'web/vendor',dist/'vendor',dirs_exist_ok=True)
            shutil.copyfile(ROOT/'web/math-config.js',dist/'math-config.js')
        css=(dist/"app.css").read_text().replace("@import url('');\n","");(dist/"app.css").write_text(css)
        file_map={}
        def internal(r):
            r=dict(r)
            original_files=r.get('files',[])
            files=[]
            for f in r.get("files",[]):
                if f['path'].endswith('.txt'):continue
                f=dict(f);source=ROOT/f["path"]
                assert source.resolve().is_relative_to((ROOT/"originals").resolve()),source
                dest="files/"+f["sha256"][:20]+source.suffix.lower()
                if dest not in file_map:
                    (dist/"files").mkdir(exist_ok=True);shutil.copyfile(source,dist/dest);file_map[dest]=f["path"]
                f["path"]=dest;files.append(f)
            r["files"]=files
            r['solution_attachments']=[dict(a,pages=[dict(im) for im in a.get('pages',[])]) for a in r.get('solution_attachments',[])]
            for i,attachment in enumerate(r['solution_attachments'],1):
                attachment['path']=next(f['path'] for f in files if f['url']==attachment['url'])
                for im in attachment['pages']:
                    source=ROOT/im['path'];dest=f"solution-crops/{r['id']}/{i}/{source.name}"
                    (dist/dest).parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(source,dist/dest);im['path']=dest
            if r.get('reader_html'):
                for before,after in sorted(((f['path'],'files/'+f['sha256'][:20]+Path(f['path']).suffix.lower()) for f in original_files),key=lambda pair:-len(pair[0])):
                    r['reader_html']=r['reader_html'].replace(before,after)
            r.pop('text',None)
            r.pop('additional_solution_sources',None)
            r.pop('solution_download_failures',None)
            images=[]
            for im in r.get("images",[]):
                im=dict(im);source=ROOT/im["path"];dest="crops/"+r["id"]+"/"+source.name
                (dist/dest).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dist/dest);im["path"]=dest
                match=next((f for f in r["files"] if f["kind"]=="original" and f["path"].endswith(".pdf")),None)
                im["original"]=match["path"] if match else ""
                images.append(im)
            r["images"]=images
            # Never publish host paths; retain origins only in the private catalog outside dist.
            r.pop("local_path",None)
            return r
        if mode=="public":
            rr=[{k:v for k,v in r.items() if k in PUBLIC_KEYS} for r in resources]
            qq=[{k:v for k,v in r.items() if k in PUBLIC_KEYS} for r in questions]
        else:
            rr=[internal(r) for r in resources];qq=[internal(q) for q in questions]
            for p in (dist/'files').iterdir():
                if 'files/'+p.name not in file_map:p.unlink() # generated copies only; originals retained.
        data=dict(mode=mode,date="2026-11-16",resources=rr,problems=qq,fileCount=len(file_map))
        payload="window.ATLAS = "+json.dumps(data,ensure_ascii=False,separators=(",",":"))+";\n"
        (dist/"data.js").write_text(payload)
        if mode=="public":
            assert set(p.name for p in dist.iterdir())=={"index.html","app.js","app.css","reader.css","data.js"},"Public directory contains unexpected assets"
            assert not any(k in payload for k in ['"text":','"files":','"images":','originals/','/home/','crops/','"local_path"'])
        (base/".gitignore").write_text("node_modules/\n.sites-runtime/\n.env*\n*.log\n")
        print(mode,len(rr),len(qq),len(file_map),sum(p.stat().st_size for p in dist.rglob("*") if p.is_file()))
    # GitHub Pages publishes this allowlisted public directory ONLY.
    docs=ROOT/'docs';docs.mkdir(exist_ok=True)
    allowed={'index.html','app.js','app.css','reader.css','data.js'}
    assert all(p.name in allowed and p.is_file() for p in docs.iterdir()),'Unexpected file in Pages directory'
    for name in allowed:shutil.copyfile(ROOT/'sites/public/dist'/name,docs/name)

if __name__=="__main__":main()
