#!/usr/bin/env python3
"""Strict integrity, LaTeX safety, cross-reference, and public-isolation checker for the study system."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"
PUBLIC_ALLOWED = {"index.html", "app.js", "app.css", "reader.css", "data.js"}


def scan_strings(obj, fname, path=""):
    errors = []
    if isinstance(obj, str):
        for ch in obj:
            if ord(ch) < 32 and ch != "\n":
                errors.append(f"{fname}:{path} contains ASCII control char {repr(ch)} in {obj[:60]!r}")
        if re.search(r"\\\\[a-zA-Z]", obj):
            errors.append(f"{fname}:{path} contains accidental double backslash before letter in {obj[:80]!r}")
        if re.search(r"TODO|TBD|待补充", obj):
            errors.append(f"{fname}:{path} contains unfinished placeholder in {obj[:60]!r}")

        # Math delimiter & brace balance checks
        dd = re.findall(r"(?<!\\)\$\$", obj)
        if len(dd) % 2 != 0:
            errors.append(f"{fname}:{path} unpaired $$ in {obj[:80]!r}")
        no_dd = re.sub(r"(?<!\\)\$\$", "", obj)
        ss = re.findall(r"(?<!\\)\$", no_dd)
        if len(ss) % 2 != 0:
            errors.append(f"{fname}:{path} unpaired $ in {obj[:80]!r}")
        if obj.count(r"\(") != obj.count(r"\)"):
            errors.append(f"{fname}:{path} unpaired \\(\\) in {obj[:80]!r}")
        if obj.count(r"\[") != obj.count(r"\]"):
            errors.append(f"{fname}:{path} unpaired \\[\\] in {obj[:80]!r}")

        for match in re.findall(r"\$\$(.*?)\$\$|(?<!\$)\$([^$]+)\$(?!\$)", obj, re.S):
            expr = "".join(match)
            depth = 0
            for ch in re.sub(r"\\[{}]", "", expr):
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                if depth < 0:
                    errors.append(f"{fname}:{path} negative brace depth in math {expr[:80]!r}")
                    break
            if depth != 0:
                errors.append(f"{fname}:{path} unbalanced brace depth in math {expr[:80]!r}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            errors.extend(scan_strings(v, fname, f"{path}.{k}"))
    elif isinstance(obj, list):
        for idx, v in enumerate(obj):
            errors.extend(scan_strings(v, fname, f"{path}[{idx}]"))
    return errors


def main():
    questions = [
        q for q in json.loads((ROOT / "catalog/questions.json").read_text())
        if q.get("role") == "problem"
    ]
    qids = {q["id"] for q in questions}
    assert len(qids) == 283, f"Expected 283 problems, got {len(qids)}"

    framework = json.loads((CURRICULUM / "framework.json").read_text())
    math_tools = json.loads((CURRICULUM / "math_tools.json").read_text())
    advanced_models = json.loads((CURRICULUM / "advanced_models.json").read_text())
    mapping = json.loads((CURRICULUM / "problem_mapping.json").read_text())
    topics = [json.loads(p.read_text()) for p in sorted((CURRICULUM / "topics").glob("*.json"))]

    # Depth floors
    assert len(topics) == 8, f"Expected 8 topics, got {len(topics)}"
    assert len(framework["workflow_steps"]) == 5
    assert len(framework["study_plans"]) == 3
    assert len(framework["archetypes"]) == 9
    assert len(framework["pitfall_clinics"]) == 6
    assert len(math_tools) == 10
    assert len(advanced_models) == 12
    total_sub = sum(len(t["syllabus_matrix"]) for t in topics)
    total_cm = sum(len(t["core_models"]) for t in topics)
    total_sc = sum(len(t["secondary_conclusions"]) for t in topics)
    total_ve = sum(len(t["virtual_examples"]) for t in topics)
    assert total_sub >= 40, total_sub
    assert total_cm >= 32, total_cm
    assert total_sc >= 40, total_sc
    assert total_ve == 16, total_ve

    # Valid ID sets
    topic_ids = {t["id"] for t in topics}
    sub_by_topic = {t["id"]: {s["code"] for s in t["syllabus_matrix"]} for t in topics}
    arch_ids = {a["id"] for a in framework["archetypes"]}
    math_ids = {m["id"] for m in math_tools}
    adv_ids = {a["id"] for a in advanced_models}

    # Exact 283/283 mapping check
    assert set(mapping.keys()) == qids, (
        "Mapping mismatch",
        sorted(qids - set(mapping.keys()))[:5],
        sorted(set(mapping.keys()) - qids)[:5],
    )
    for pid, m in mapping.items():
        assert m["primary_topic"] in topic_ids, (pid, m["primary_topic"])
        assert m["subtopic"] in sub_by_topic[m["primary_topic"]], (pid, m["subtopic"])
        assert all(s in topic_ids and s != m["primary_topic"] for s in m["secondary_topics"]), pid
        assert m["tier"] in {"L1", "L2", "L3", "L4"}, pid
        assert 1 <= len(m["archetypes"]) <= 2 and set(m["archetypes"]) <= arch_ids, pid
        assert 1 <= len(m["math_tools"]) <= 3 and set(m["math_tools"]) <= math_ids, pid
        assert set(m["advanced_models"]) <= adv_ids, pid
        assert len(m["study_note"].strip()) >= 12, pid

    # Check all curriculum cross-references
    for arch in framework["archetypes"]:
        assert set(arch["benchmark_problem_ids"]) <= qids, arch["id"]
    for pit in framework["pitfall_clinics"]:
        for ex in pit["examples"]:
            assert ex["id"] in qids, (pit["id"], ex["id"])
    for m in math_tools:
        assert set(m["featured_problem_ids"]) <= qids, m["id"]
    for adv in advanced_models:
        assert set(adv["prerequisite_math_ids"]) <= math_ids, adv["id"]
        assert set(adv["linked_problem_ids"]) <= qids, adv["id"]
    for t in topics:
        assert set(t["recommended_math_ids"]) <= math_ids, t["id"]
        assert set(t["recommended_adv_ids"]) <= adv_ids, t["id"]
        for cm in t["core_models"]:
            assert set(cm["sample_problem_ids"]) <= qids, (t["id"], cm["name"])
        for sc in t["secondary_conclusions"]:
            assert set(sc["related_problem_ids"]) <= qids, (t["id"], sc["title"])
        for ve in t["virtual_examples"]:
            assert set(ve["transfers_to_ids"]) <= qids, (t["id"], ve["id"])
        for pit in t["topic_pitfalls"]:
            assert set(pit["ref_ids"]) <= qids, (t["id"], pit["title"])

    # Scan all curriculum JSON strings for control chars, double-backslash, LaTeX balance
    all_errors = []
    for p in sorted(CURRICULUM.rglob("*.json")):
        all_errors.extend(scan_strings(json.loads(p.read_text()), p.relative_to(ROOT)))
    assert not all_errors, "\n".join(all_errors[:20])

    # Check built study-data.js
    study_js = ROOT / "web/study-data.js"
    assert study_js.is_file(), "Missing web/study-data.js; run python3 scripts/build_study.py"
    payload = json.loads(study_js.read_text().removeprefix("window.STUDY_DATA = ").rstrip(";\n"))
    assert len(payload["problems"]) == 283
    assert payload["stats"]["total_problems"] == 283

    # Check sites/public/dist and docs isolation if present
    for pub_dir in (ROOT / "docs", ROOT / "sites/public/dist"):
        if pub_dir.exists():
            names = {p.name for p in pub_dir.iterdir()}
            assert names == PUBLIC_ALLOWED, (pub_dir, names)

    # Check internal dist study files if sites/internal/dist exists
    int_dist = ROOT / "sites/internal/dist"
    if int_dist.exists():
        for name in ("study.html", "study.css", "study.js", "study-data.js"):
            if (ROOT / "web" / name).is_file():
                assert (int_dist / name).is_file(), f"Missing {int_dist / name}; run build_sites.py"

    print(
        f"PASS: 283/283 problem mappings; {len(topics)} topics ({total_sub} subtopics, {total_cm} core models, "
        f"{total_sc} secondary conclusions, {total_ve} virtual examples); {len(math_tools)} math tools; "
        f"{len(advanced_models)} advanced models; 0 LaTeX/escape errors."
    )


if __name__ == "__main__":
    main()
