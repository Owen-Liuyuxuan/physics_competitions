#!/usr/bin/env python3
"""Create traceable question crops; keep uncertain boundaries in a review queue."""
from __future__ import annotations
import json
import re
from pathlib import Path
import pymupdf as fitz
from plancks_boundaries import PAPERS, split_paper

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"derived/questions"
CN={c:i+1 for i,c in enumerate("一二三四五六七八九十")}

def lines(page):
    result=[]
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines",[]):
            result.append(("".join(s["text"] for s in line["spans"]).strip(),line["bbox"]))
    return result

def crop(doc,start,end,ident,original,status):
    images=[]; texts=[]
    folder=OUT/ident;folder.mkdir(parents=True,exist_ok=True)
    sp,sy=start;ep,ey=end
    for p in range(sp,ep+1):
        page=doc[p]
        top=max(0,sy-7) if p==sp else 35
        bottom=min(page.rect.height-30,ey-8) if p==ep else page.rect.height-30
        if bottom-top<12:continue
        rect=fitz.Rect(25,top,page.rect.width-25,bottom)
        target=folder/f"page-{p+1}.jpg"
        page.get_pixmap(matrix=fitz.Matrix(1.65,1.65),clip=rect).save(target,jpg_quality=87)
        images.append(dict(path=str(target.relative_to(ROOT)),page=p+1,rect=list(rect),original=original,status=status))
        texts.append(page.get_text(clip=rect))
    return images,"\n\n".join(texts)

def question(base,q,title,start,end,doc,role=None,reviewed=False):
    ident=base["id"]+f"-slice-q{q}"
    status="reviewed" if reviewed else "review_needed"
    f=next(f for f in base["files"] if f["path"].endswith(".pdf"))
    images,text=crop(doc,start,end,ident,f["path"],"边界已抽查" if reviewed else "自动切片，待复核")
    return dict(id=ident,contest=base["contest"],year=base["year"],stage=base["stage"],
                role=role or base["role"],question=q,title=title,granularity="problem",
                parent_id=base["id"],source_page=base["source_page"],url=base["url"],
                source_tier=base["source_tier"],files=base["files"],images=images,text=text,
                boundary_status=status,source_sha256=f["sha256"],solution_ids=[])

def main():
    resources=json.loads((ROOT/"catalog/extended-resources.json").read_text())
    questions=[];review=[]
    for r in resources:
        if r["contest"]=="Physics Cup" and r["role"]=="problem":
            q=dict(r,id=r["id"]+"-reader",parent_id=r["id"],granularity="problem",images=[],text="",solution_ids=[r["id"]+"-solutions"])
            txt=next((f for f in r.get("files",[]) if f["path"].endswith(".txt")),None)
            if txt:q["text"]=(ROOT/txt["path"]).read_text()
            pdf=next((f for f in r.get("files",[]) if f["path"].endswith(".pdf")),None)
            if pdf:
                doc=fitz.open(ROOT/pdf["path"])
                q["images"],pdftext=crop(doc,(0,30),(len(doc)-1,doc[-1].rect.height-25),q["id"],pdf["path"],"单题PDF原页，附件版本待复核")
                q["text"]=pdftext or q["text"]
                q["boundary_status"]="single_problem_pdf"
            else:
                q["boundary_status"]="webpage_snapshot"
                q["archive_note"]="此题原生来源为网页；以原文提取及原始图下载阅读，不伪造PDF题面。"
            questions.append(q)
            continue
        pdfs=[f for f in r.get("files",[]) if f["path"].endswith(".pdf")]
        if not pdfs:continue
        if r["id"] in PAPERS:
            doc=fitz.open(ROOT/pdfs[0]["path"])
            questions.extend(split_paper(r,doc,question))
            continue
        if r["contest"]=="PanPhO" and r["stage"]=="paper-2":
            doc=fitz.open(ROOT/pdfs[0]["path"])
            marks=[]
            for pi,p in enumerate(doc):
                for text,box in lines(p):
                    m=re.match(r"^(?:Problem|Question)\s*([12])(?:\b|:)",text,re.I)
                    if m:marks.append((int(m[1]),pi,box[1],text))
            if len(marks)<2 or [m[0] for m in marks[:2]]!=[1,2]:
                review.append(dict(resource_id=r["id"],reason="综合卷二未识别到连续题号"));continue
            # The 2026 question file includes a separate answer sheet starting Q1 again.
            end=(marks[2][1],marks[2][2]) if len(marks)>2 else (len(doc)-1,doc[-1].rect.height-30)
            titles={2019:["引力波","同步现象"],2020:["引力常数的精密测量","不同维度的物理"],2021:["准晶体","黑洞物理"],2022:["时空变介电常数","网络的分数维数"],2023:["真空泡泡","洛伦兹互易性"],2024:["时空变介电常数","度量修正的测地线与热传导"],2025:["高尔夫球手的噩梦","超短电磁脉冲"],2026:["直流与交流导体模型","强激光与等离子体有质动力"]}
            for i,(q,pi,y,text) in enumerate(marks[:2]):
                stop=(marks[i+1][1],marks[i+1][2]) if i==0 else end
                title=titles[r["year"]][q-1]
                mismatch=r["year"]==2024 and r["role"]=="solution" and q==1
                if mismatch:title="引力波测量中的误差估计 · 官方文件版本疑点"
                row=question(r,q,title+(" · 参考解答" if r["role"]=="solution" else ""),(pi,y),stop,doc)
                if mismatch:row["archive_note"]="官方2024解答文件Q1标题与题目文件Q1不一致，未建立自动题解配对，需核查版本。"
                questions.append(row)
            continue
        if r["contest"]=="CPhO" and "theory" in r["stage"]:
            doc=fitz.open(ROOT/pdfs[0]["path"])
            marks=[]
            for pi,p in enumerate(doc):
                for text,box in lines(p):
                    m=re.match(r"^([一二三四五六七八九十])[、．.]",text)
                    if m:
                        q_num=CN[m[1]]
                        if marks and marks[-1][0]==q_num and marks[-1][1]==pi and abs(box[1]-marks[-1][2])<30:
                            continue
                        marks.append((q_num,pi,box[1],text))
            # Reject non-sequential detections and section resets; leave originals intact.
            if [m[0] for m in marks] != list(range(1,len(marks)+1)) or not 4<=len(marks)<=10:
                review.append(dict(resource_id=r["id"],reason="无法可靠识别连续大题号",detected=[m[0] for m in marks]));continue
            names=["空气弹簧","母球纯滚动","隧道二极管与负微分电阻","回旋加速器","相对论星际飞行器","光纤陀螺仪","双黑洞引力波","电光调制器"]
            for i,(q,pi,y,text) in enumerate(marks):
                end=(marks[i+1][1],marks[i+1][2]) if i+1<len(marks) else (len(doc)-1,doc[-1].rect.height-30)
                title=names[q-1] if r["year"]==2020 and r["stage"]=="semifinal-theory" else f"{r['year']} {r['stage']} · 第{q}题"
                questions.append(question(r,q,title,(pi,y),end,doc))
        elif r["contest"]!="Physics Cup":
            review.append(dict(resource_id=r["id"],reason="逐题边界待适配；可直接下载整卷"))
    for q in questions:
        if q["contest"] in ("CPhO","PanPhO","PLANCKS") and q["role"]=="problem":
            q["solution_ids"]=[s["id"] for s in questions if s["contest"]==q["contest"] and s["year"]==q["year"] and s["stage"]==q["stage"] and s["question"]==q["question"] and s["role"]=="solution"]
            if q["contest"]=="PanPhO" and q["year"]==2024 and q["question"]==1:
                q["solution_ids"]=[]
                q["archive_note"]="官网所链解答Q1与本题标题不一致，故未自动关联；可在整卷索引核查。"
        q["solution_ids"]=[ident for ident in q.get("solution_ids",[]) if any(r["id"]==ident for r in resources+questions)]
    (ROOT/"catalog/questions.json").write_text(json.dumps(questions,ensure_ascii=False,indent=2)+"\n")
    (ROOT/"catalog/crop-review-queue.json").write_text(json.dumps(review,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(question_records=len(questions),problem_records=sum(r["role"]=="problem" for r in questions),crop_images=sum(len(r.get("images",[])) for r in questions),pending_papers=len(review))))

if __name__=="__main__":main()
