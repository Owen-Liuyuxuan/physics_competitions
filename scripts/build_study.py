#!/usr/bin/env python3
"""Build web/study-data.js and notes/CPHO_FINAL_SYLLABUS_AND_STUDY_GUIDE.md from curriculum/ and catalog/."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
from translations import load_translations

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"

STAGE_LABELS = {
    "semifinal-theory": "复赛理论",
    "final-theory": "决赛理论",
    "paper-2": "综合卷二",
    "单题挑战": "单题挑战",
    "国际决赛": "国际决赛",
    "英爱预赛": "英爱预赛",
}

CONTEST_LABELS = {
    "CPhO": "全国中学生物理竞赛",
    "PanPhO": "泛珠三角物理奥林匹克",
    "Physics Cup": "Physics Cup",
    "PLANCKS": "PLANCKS",
}


def load_curriculum():
    framework = json.loads((CURRICULUM / "framework.json").read_text())
    math_tools = json.loads((CURRICULUM / "math_tools.json").read_text())
    advanced_models = json.loads((CURRICULUM / "advanced_models.json").read_text())
    mapping = json.loads((CURRICULUM / "problem_mapping.json").read_text())
    topics = sorted(
        (json.loads(p.read_text()) for p in (CURRICULUM / "topics").glob("*.json")),
        key=lambda t: t["order"],
    )
    return framework, math_tools, advanced_models, mapping, topics


def build_problems(mapping, topics):
    questions = [
        q for q in json.loads((ROOT / "catalog/questions.json").read_text())
        if q.get("role") == "problem"
    ]
    teaching = json.loads((ROOT / "catalog/teaching-analysis.json").read_text())
    translations = load_translations()

    assert len(questions) == 283, f"Expected 283 problems, got {len(questions)}"
    assert set(mapping.keys()) == {q["id"] for q in questions}, "Problem mapping mismatch"

    topic_map = {t["id"]: t for t in topics}
    subtopic_names = {
        sub["code"]: sub["name"]
        for t in topics
        for sub in t["syllabus_matrix"]
    }

    records = []
    for q in sorted(
        questions,
        key=lambda x: (-int(x["year"]), x["contest"], x["stage"], int(x.get("question") or 0), x["id"]),
    ):
        pid = q["id"]
        ta = teaching[pid]
        m = mapping[pid]
        tinfo = ta["teaching"]
        tr = translations.get(pid)
        title = ta.get("better_title") or q.get("title", "")
        title_zh = tr["title"] if tr else ""

        records.append({
            "id": pid,
            "contest": q["contest"],
            "contest_label": CONTEST_LABELS.get(q["contest"], q["contest"]),
            "year": q["year"],
            "stage": q["stage"],
            "stage_label": STAGE_LABELS.get(q["stage"], q["stage"]),
            "question": q.get("question"),
            "title": title,
            "title_zh": title_zh,
            "difficulty": ta["difficulty"],
            "model": ta["model"],
            "teaching_tags": ta["teaching_tags"],
            "primary_topic": m["primary_topic"],
            "primary_topic_title": topic_map[m["primary_topic"]]["title"],
            "secondary_topics": m["secondary_topics"],
            "subtopic": m["subtopic"],
            "subtopic_name": subtopic_names[m["subtopic"]],
            "tier": m["tier"],
            "archetypes": m["archetypes"],
            "math_tools": m["math_tools"],
            "advanced_models": m["advanced_models"],
            "study_note": m["study_note"],
            "has_solution": bool(q.get("solution_ids")),
            "blind_highlight": tinfo.get("blind_highlight"),
            "level": tinfo["level"],
            "overview": tinfo["overview"],
            "decomposition": tinfo["decomposition"],
            "comparison": tinfo["comparison"],
            "hard_points": tinfo["hard_points"],
            "pitfalls": tinfo["pitfalls"],
            "takeaways": tinfo["takeaways"],
        })
    return records


def compute_stats(records, topics):
    by_contest = Counter(r["contest"] for r in records)
    by_cpho_stage = Counter(r["stage"] for r in records if r["contest"] == "CPhO")
    by_tier = Counter(r["tier"] for r in records)
    by_diff = Counter(r["difficulty"] for r in records)
    by_topic = {}
    for t in topics:
        tid = t["id"]
        prim = [r for r in records if r["primary_topic"] == tid]
        cross = [r for r in records if tid in r["secondary_topics"]]
        by_topic[tid] = {
            "primary_total": len(prim),
            "secondary_total": len(cross),
            "cpho_semi": sum(1 for r in prim if r["contest"] == "CPhO" and r["stage"] == "semifinal-theory"),
            "cpho_final": sum(1 for r in prim if r["contest"] == "CPhO" and r["stage"] == "final-theory"),
            "panpho": sum(1 for r in prim if r["contest"] == "PanPhO"),
            "physicscup": sum(1 for r in prim if r["contest"] == "Physics Cup"),
            "plancks": sum(1 for r in prim if r["contest"] == "PLANCKS"),
            "tiers": dict(sorted(Counter(r["tier"] for r in prim).items())),
        }

    return {
        "total_problems": len(records),
        "cpho_total": by_contest["CPhO"],
        "cpho_semi": by_cpho_stage["semifinal-theory"],
        "cpho_final": by_cpho_stage["final-theory"],
        "panpho_total": by_contest["PanPhO"],
        "physicscup_total": by_contest["Physics Cup"],
        "plancks_total": by_contest["PLANCKS"],
        "blind_highlight_count": sum(1 for r in records if r["blind_highlight"]),
        "with_solution_count": sum(1 for r in records if r["has_solution"]),
        "by_tier": dict(sorted(by_tier.items())),
        "by_difficulty": dict(sorted(by_diff.items())),
        "by_topic": by_topic,
        "by_subtopic": dict(sorted(Counter(r["subtopic"] for r in records).items())),
        "by_archetype": dict(sorted(Counter(a for r in records for a in r["archetypes"]).items())),
        "by_math": dict(sorted(Counter(x for r in records for x in r["math_tools"]).items())),
        "by_adv": dict(sorted(Counter(x for r in records for x in r["advanced_models"]).items())),
    }


def render_markdown_guide(framework, math_tools, advanced_models, topics, records, stats):
    by_id = {r["id"]: r for r in records}
    lines = [
        f"# {framework['meta']['title']}",
        "",
        f"> **{framework['meta']['subtitle']}**  ",
        f"> **覆盖范围**：{framework['meta']['repo_scope']}  ",
        f"> **使用说明**：{framework['meta']['disclaimer']}",
        "",
        "---",
        "",
        "## 一、全库 283 题备赛分布总览",
        "",
        f"- **总独立题目**：**{stats['total_problems']}** 题（仓内配对参考解答 {stats['with_solution_count']} 题，独立盲解亮点 / 官方勘误提示 **{stats['blind_highlight_count']}** 题）。",
        f"- **赛事构成**：CPhO {stats['cpho_total']} 题（复赛 {stats['cpho_semi']} + 决赛 {stats['cpho_final']}）、PLANCKS {stats['plancks_total']} 题、Physics Cup {stats['physicscup_total']} 题、PanPhO {stats['panpho_total']} 题。",
        f"- **梯次分级**：`L1 复赛筑基` {stats['by_tier'].get('L1',0)} 题 · `L2 复赛压轴→决赛过渡` {stats['by_tier'].get('L2',0)} 题 · `L3 决赛核心攻坚` {stats['by_tier'].get('L3',0)} 题 · `L4 集训队与国际前沿` {stats['by_tier'].get('L4',0)} 题。",
        "",
        "| 专题 | 主属题数 | CPhO 复赛 | CPhO 决赛 | PanPhO | Physics Cup | PLANCKS |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for t in topics:
        st = stats["by_topic"][t["id"]]
        lines.append(
            f"| {t['code']} · {t['title']} | {st['primary_total']} | {st['cpho_semi']} | {st['cpho_final']} | {st['panpho']} | {st['physicscup']} | {st['plancks']} |"
        )

    lines.extend(["", "---", "", "## 二、五步闭环专题精研流程", ""])
    for step in framework["workflow_steps"]:
        lines.append(f"### {step['code']} · {step['title']}（{step['duration']}）")
        lines.append(f"**核心目标**：{step['goal']}")
        for act in step["actions"]:
            lines.append(f"- {act}")
        lines.append(f"- **过关标准**：{step['exit_criterion']}")
        lines.append("")

    lines.extend(["---", "", "## 三、三种分阶段自复习路线", ""])
    for plan in framework["study_plans"]:
        lines.append(f"### {plan['name']}（{plan['badge']}）")
        lines.append(f"- **适用对象**：{plan['target']}")
        lines.append(f"- **每日节奏**：{plan['daily_rhythm']}")
        for ph in plan["phases"]:
            lines.append(f"  - **{ph['week']}**：{ph['goal']}")
        lines.append("")

    lines.extend(["---", "", "## 四、九大跨专题高频题型母版", ""])
    for arch in framework["archetypes"]:
        count = stats["by_archetype"].get(arch["id"], 0)
        lines.append(f"### {arch['code']} · {arch['name']}（全库关联 {count} 题）")
        lines.append(f"> {arch['tagline']}  （{arch['frequency_note']}）")
        lines.append("")
        lines.append("**识别信号**：")
        for s in arch["signal_cues"]:
            lines.append(f"- {s}")
        lines.append("")
        lines.append("**五步通用拆解模板**：")
        for idx, step in enumerate(arch["five_step_template"], 1):
            lines.append(f"{idx}. {step}")
        lines.append("")
        lines.append("**代表题例**：" + "、".join(
            f"`{pid}`（{by_id[pid]['title_zh'] or by_id[pid]['title']}）" for pid in arch["benchmark_problem_ids"]
        ))
        lines.append("")

    lines.extend(["---", "", "## 五、十大大学级数学工具箱目录", ""])
    for m in math_tools:
        count = stats["by_math"].get(m["id"], 0)
        lines.append(f"- **{m['code']} · {m['name']}**（{m['level_tag']} · 库内应用 {count} 题）：{m['why_it_matters']}")

    lines.extend(["", "---", "", "## 六、十二个高频本科 / 研究生下放前沿模型", ""])
    for adv in advanced_models:
        count = stats["by_adv"].get(adv["id"], 0)
        lines.append(f"### {adv['code']} · {adv['title']}（{adv['course_origin']} · 库内 {count} 题）")
        lines.append(f"- **高中物理桥梁**：{adv['plain_intuition']}")
        lines.append(f"- **命题脚手架规律**：{adv['exam_scaffolding_pattern']}")
        lines.append(f"- **失效边界**：{adv['validity_limits']}")
        lines.append("")

    lines.extend(["---", "", "## 七、八大专题考纲三级映射与题型要点", ""])
    for t in topics:
        lines.append(f"### {t['code']} · {t['title']}")
        lines.append(f"> {t['bridge_summary']}")
        lines.append("")
        lines.append("| 编号 | 子专题 | 复赛标准 | 决赛跃迁 | 大学/国际前沿 | 题数 |")
        lines.append("| --- | --- | --- | --- | --- | ---: |")
        for sub in t["syllabus_matrix"]:
            cnt = stats["by_subtopic"].get(sub["code"], 0)
            lines.append(f"| {sub['code']} | {sub['name']} | {sub['tier_a_semifinal']} | {sub['tier_b_final']} | {sub['tier_c_frontier']} | {cnt} |")
        lines.append("")
        lines.append("**精选二级结论与方法**：")
        for sc in t["secondary_conclusions"]:
            lines.append(f"- **{sc['title']}**（{sc['source_type']}）：{sc['formula']} —— *边界预警*：{sc['pitfall_warning']}")
        lines.append("")

    lines.extend(["---", "", "## 八、六类高频易错诊所与五维自检仪式", ""])
    for pit in framework["pitfall_clinics"]:
        lines.append(f"### {pit['title']}")
        lines.append(f"- **机理**：{pit['mechanism']}")
        lines.append(f"- **纠正法则**：{pit['remedy_rule']}")
    lines.append("")
    lines.append(f"### {framework['self_audit_protocol']['title']}")
    for chk in framework["self_audit_protocol"]["checks"]:
        lines.append(f"- **{chk['name']}**：{chk['detail']}")

    return "\n".join(lines).rstrip() + "\n"


def main():
    framework, math_tools, advanced_models, mapping, topics = load_curriculum()
    records = build_problems(mapping, topics)
    stats = compute_stats(records, topics)

    payload = {
        "meta": framework["meta"],
        "stats": stats,
        "framework": framework,
        "math_tools": math_tools,
        "advanced_models": advanced_models,
        "topics": topics,
        "problems": records,
    }

    js_path = ROOT / "web" / "study-data.js"
    js_path.write_text(
        "window.STUDY_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    )
    md_path = ROOT / "notes" / "CPHO_FINAL_SYLLABUS_AND_STUDY_GUIDE.md"
    md_path.write_text(render_markdown_guide(framework, math_tools, advanced_models, topics, records, stats))

    print(f"Built {js_path.relative_to(ROOT)} ({js_path.stat().st_size} bytes, {len(records)} problems)")
    print(f"Built {md_path.relative_to(ROOT)} ({md_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
