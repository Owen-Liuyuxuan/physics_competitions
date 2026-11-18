#!/usr/bin/env python3
"""Merge per-batch teaching analyses into catalog/teaching-analysis.json.

Adds two coarse, controlled-vocabulary layers on top of the free-form
``teaching_tags`` written during problem analysis, so the web filter stays usable:
``domain`` (物理领域) and ``skills`` (方法/易错主题).

Also extracts each problem's complete original Phase 1 blind-solve workflow
(``blind_process``) from ``notes/problems/batch-*.md`` and attaches verified
highlights (``blind_highlight``) where the independent blind solve found a
cleaner route than the official solution or caught official solution errata.
"""
from __future__ import annotations
import glob
import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIFFS = {"D1", "D2", "D3", "D4", "D5"}
TEACH_KEYS = ["level", "overview", "decomposition", "blind_attempt", "comparison", "hard_points", "pitfalls", "takeaways"]

DOMAIN = {
    "力学与刚体": r"刚体|转动惯量|碰撞|纯滚动|摩擦|抛体|弹簧|振动|简谐|微振动|质心|角动量|动量|陀螺|斜面|绳|摆|加速度|章动|滚动|冲量",
    "天体与引力": r"开普勒|轨道|卫星|变轨|引力|黑洞|暗物质|彗星|星际|霍曼|天体",
    "电磁学": r"电场|磁场|磁|电容|电感|电磁|静电|电荷|电流|麦克斯韦|洛伦兹力|安培|法拉第|偶极|超导|等离子体|回旋|高斯定理",
    "电路与网络": r"电阻|电路|RLC|二极管|网格|阻抗|LC|等效电阻|格点",
    "热学与统计": r"热|气体|熵|温度|配分函数|卡诺|辐射|玻尔兹曼|相变|多方过程|制冷|统计|分子拉链|扩散",
    "光学与波动": r"透镜|成像|衍射|干涉|偏振|光纤|光束|折射|光学|波带|光栅|萨格纳克|波动|波包|色散|激光|多普勒|圆锥曲线光学",
    "流体与连续介质": r"流体|水|液|压强|势流|附加质量|管|浮|表面张力|连续介质|晶体表面|台阶",
    "相对论": r"相对论|洛伦兹变换|固有时|四维|光子火箭|闵可夫斯基|维格纳|托马斯",
    "量子与近代物理": r"量子|原子|核|能级|自旋|玻尔|粒子|瞬子|隧穿|费米|电子气|朗道|外斯|磁矩",
    "数学物理与几何": r"四元数|莫比乌斯|正二十面体|分形|维数|作图|射影|共形|对称群|图论|拓扑|几何",
}
SKILLS = {
    "守恒律与能量法": r"守恒|能量|虚功|变分|拉格朗日|哈密顿|最小作用|功能原理",
    "类比与对称性": r"类比|对称|等效|镜像|电像|叠加|互易|不变量|共形|倒易",
    "量纲与近似展开": r"量纲|标度|近似|展开|微扰|泰勒|线性化|小量|无量纲|极限|数量级",
    "几何与作图": r"几何|作图|圆锥曲线|包络|射影|矢端|相似|三角|焦点|准线|交比|坐标变换",
    "微分方程与振动": r"微分方程|简谐|振动|共振|本征|模式|色散关系|传递矩阵|递推|不动点",
    "积分与极值优化": r"积分|极值|优化|求极|拉格朗日乘子|不等式|变分法|最大|最小|最优",
    "参考系与坐标变换": r"参考系|质心系|相对论速度|洛伦兹变换|旋转系|科里奥利|惯性系|非惯性|坐标系|变换",
    "统计与概率": r"概率|分布|配分函数|系综|熵|雅可比因子|统计",
}

# Curated strictly from verified Phase 2 comparisons against official/winner solutions in repo
BLIND_HIGHLIGHTS: dict[str, dict[str, str]] = {
    "panpho-2019-paper-2-problem-slice-q2": {
        "kind": "盲解路径更优",
        "note": "盲解提炼“分段简谐运动等时性原理”，从物理本质一步解释第 1 象限冲量为何只产生整体时间平移，省去官方逐象限展开微扰余弦的冗长推导。",
    },
    "panpho-2023-paper-2-problem-slice-q2": {
        "kind": "盲解洞察更深",
        "note": "盲解直接利用拉普拉斯方程谐和恒等式，从数学本质阐明单个二维标量边界条件为何恰好同时定出三个电磁多极镜像矩，比官方直接凑系数更透彻。",
    },
    "panpho-2025-paper-2-problem-slice-q1": {
        "kind": "盲解路径更优",
        "note": "盲解利用转动惯量张量对称性免去官方的薄圆盘切片积分，直接对任意球对称质量分布（任意 K）一步证出科里奥利力矩公式。",
    },
    "panpho-2025-paper-2-problem-slice-q2": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解与核心推导完全一致，并在对照时查出官方 A2 小问将 42 fs 误印为 4.2e-12 s（数量级差 100 倍且需注意半高全宽因子）。",
    },
    "physicscup-2025-q2-reader": {
        "kind": "盲解达到最佳解",
        "note": "盲解采用的外接长方体/柱坐标参数化方案与一等奖获奖解（Bruno Machado Feltran）完全一致，在三类正确解中数学形式最简。",
    },
    "plancks-2020-final-problem-slice-q1": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解一步得出全部推导，并识别出官方解答第 3 页方程符号印反（T^2-T-1=0 却取 T^2+T-1=0 之根）及多余印刷符号两处笔误。",
    },
    "plancks-2020-final-problem-slice-q4": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解核对量纲后指出官方第 (b) 问直接用斜率乘 1.33^2 而漏算微米换算为厘米的 10^-8 因子。",
    },
    "plancks-2021-final-combined-slice-q1": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "官方耗时显式构造反对称双粒子波函数并把基态能量 60ℏω0 笔误为 87ℏω0；盲解由满壳层对称性一步证得顺磁项为零，并算出精确抗磁解析系数。",
    },
    "plancks-2021-final-combined-slice-q4": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "盲解采用虚拟质量 M_eff = 4πρR^3 功能原理法替代官方球坐标欧拉方程积分，并纠出第 2.3 问官方欠阻尼特解误乘衰减因子的物理极限错误。",
    },
    "plancks-2021-final-combined-slice-q5": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解由静流体平衡物理本质指出 ∂P/∂r < 0 负号，纠出官方第 4 问根号内加减号印反的笔误。",
    },
    "plancks-2021-final-combined-slice-q7": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解通过量纲检验查出官方第 2 问将并联总电阻误写为电导公式 (r+R)/(2rR)，进而保证 GMR 表达式量纲严格自洽。",
    },
    "plancks-2021-final-combined-slice-q8": {
        "kind": "盲解路径更优",
        "note": "第 4 问盲解直接联立代数恒等式与连续性方程，省去官方“先求导化为 dw/dz 微分方程再积分”的步骤，求解更快捷。",
    },
    "plancks-2021-final-combined-slice-q12": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解精准查出官方第 3 问 √1.445 误开方为 1.700（应为 1.202 GHz）及第 5 问多普勒近似漏减 1 导致的数量级偏差。",
    },
    "plancks-2023-final-combined-slice-q1": {
        "kind": "盲解纠出官方笔误",
        "note": "独立推导与核心结论完全吻合，同时揪出官方式 (10)、角动量算符二阶导及第 5 页常数三处印刷笔误。",
    },
    "plancks-2023-final-combined-slice-q3": {
        "kind": "盲解路径更优",
        "note": "盲解提炼“双路径复共轭干涉公式 2B Re(e^{iφ}C)”，相比官方逐一写出全部矩阵元再相乘，代数运算量减少约三分之二。",
    },
    "plancks-2023-final-combined-slice-q7": {
        "kind": "盲解纠出官方笔误",
        "note": "盲解查出官方第 (x) 问式 (72) 忘将碳核能量 285 MeV/u 乘以核子数 12 且倒置比值 2/6 的双重笔误。",
    },
    "plancks-2023-final-combined-slice-q9": {
        "kind": "盲解纠出官方笔误",
        "note": "独立核算指出官方第 (iii) 问衰减指数 e^{-4185/200} 应极小（~10^-9）而非 0.2% 的数值疏忽。",
    },
    "plancks-2024-final-combined-slice-q1": {
        "kind": "盲解路径更优",
        "note": "盲解采用“先求顶点转动惯量 I_A、再退回质心 I_G”策略，使积分限齐次化并直接复用 I_A 完成第 (b) 问，省去官方二次平行轴移轴代数。",
    },
    "plancks-2024-final-combined-slice-q2": {
        "kind": "盲解纠出官方笔误",
        "note": "用单位四元数模长守恒检验，纠出官方末行数值代入误多乘 π 且将 k 印成 j 的印刷错误。",
    },
    "plancks-2024-final-combined-slice-q3": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方通分书写及 π 因子漏写细节，并澄清单圈镜像重聚 (3.15 ps) 与双圈全局复原 (6.30 ps) 的物理区别。",
    },
    "plancks-2024-final-combined-slice-q4": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方中途把极角余弦误印为 sinθ_0 = 2/3 并对调速度分量正余弦的印刷笔误。",
    },
    "plancks-2024-final-combined-slice-q6": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "盲解在第 (b) 问严格用极角极值分析，主动避开官方解答把椭圆参数方程离心角直接当极角的经典陷阱。",
    },
    "plancks-2026-final-problem-slice-q1": {
        "kind": "盲解纠出官方笔误",
        "note": "通过量纲一致性检验，指出官方第 2、4 问两处幂次印刷笔误。",
    },
    "plancks-2026-final-problem-slice-q5": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方第 6 问表格第 4 行超大质量双黑洞啁啾质量计算器输入笔误，还原 LISA 源高达 ~1.6e-17 的正确应变。",
    },
    "cpho-2013-semifinal-theory-problem-slice-q2": {
        "kind": "盲解路径更优",
        "note": "盲解直接以含入射块大系统用动量定理一步给出转轴冲量，省去官方正文先算质心再消去干扰系数 α+2 的冗余步骤。",
    },
    "cpho-2013-semifinal-theory-problem-slice-q8": {
        "kind": "盲解纠出官方笔误",
        "note": "查出官方第 14 页式 (7) 上方作差通分分子多印系数 2，并澄清强相对论背散射前向聚束与极值因果。",
    },
    "cpho-2013-final-theory-problem-slice-q4": {
        "kind": "盲解纠出官方笔误",
        "note": "发现原卷电路图电池正负极画反（左长右短）而官方解答仍按正电势计价的矛盾。",
    },
    "cpho-2013-final-theory-problem-slice-q7": {
        "kind": "盲解路径更优",
        "note": "盲解采用解析微扰展开一步锁定虚像坐标并补全一阶光程相消证明，免去官方繁琐辅助三角形构造。",
    },
    "cpho-2013-final-theory-problem-slice-q8": {
        "kind": "盲解纠出官方笔误",
        "note": "指出第 12 页坐标 x_1'' 误印成 x_2'' 及第 3 问漏列偶数项通项，补全张、王拍手统一时刻序列。",
    },
    "cpho-2014-final-theory-problem-slice-q2": {
        "kind": "盲解纠出官方笔误",
        "note": "发现官方参考解答（一）⑦⑧式及解答（二）⑧式 cosα 根号内第二项分母均漏印因子 4。",
    },
    "cpho-2014-final-theory-problem-slice-q5": {
        "kind": "盲解纠出官方笔误",
        "note": "确认原题转码误差 Δα = θ（实为 ≪ θ），并查出官方第（4）问（14）式分母漏掉因子 2。",
    },
    "cpho-2015-final-theory-problem-slice-q1": {
        "kind": "盲解路径更优",
        "note": "第（2）问盲解直接采用微扰柔度与柯西不等式，无需引入原长及二阶导数判别。",
    },
    "cpho-2015-final-theory-problem-slice-q2": {
        "kind": "盲解纠出官方笔误",
        "note": "发现官方（10）–（12）式误将导轨长度 500 m 当作 5.0/0.50 代入导致加速度与电流数值级联偏差。",
    },
    "cpho-2015-final-theory-problem-slice-q5": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方第（1）问式②③同时弄反液膜功与势能正负号（双错抵消）。",
    },
    "cpho-2015-final-theory-problem-slice-q8": {
        "kind": "盲解路径更优",
        "note": "第（3）问优先采用余切变量绕开边界 0/0 奇点，第（4）问避免强行有理化制造伪奇点。",
    },
    "cpho-2016-semifinal-theory-problem-slice-q4": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "盲解用弯折随动系稳恒流与整体动量定理免去微元混乱，并查出官方解法一式 (13)-(16) 张力写负与漏重力瑕疵。",
    },
    "cpho-2016-semifinal-theory-problem-slice-q6": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "第（1）问用跨阳极电势差净电荷记账法大幅简化级数求和；第（2）问揭露原卷与官方图把第 i+1 倍增级误绘在底边的排版错位事故。",
    },
    "cpho-2016-final-theory-problem-slice-q2": {
        "kind": "盲解路径更优",
        "note": "第（2）问沿随绳正交基投影实现张力与角加速度解耦，比官方直角坐标四元联立消元简洁约一半。",
    },
    "cpho-2016-final-theory-problem-slice-q5": {
        "kind": "盲解路径更优",
        "note": "第（2）问对非负不等式直接开方线性求解，省去官方平方后二次方程剔除增根分支。",
    },
    "cpho-2016-final-theory-problem-slice-q8": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "第（3）问用四动量不变式直接唯一锁定第四象限解，并查出官方式 (20) 有效数字误修约 0.5900（应为 0.5901）。",
    },
    "cpho-2017-semifinal-theory-problem-slice-q5": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方式 (14) r_max 符号笔误，以及式 (19)-(20) 漏掉磁场上限 B <= B_max 约束的实质性物理漏洞与反例。",
    },
    "cpho-2018-semifinal-theory-problem-slice-q4": {
        "kind": "盲解洞察更深",
        "note": "第（1）问采用二维静磁复势严密证明逃逸鞍点全局位于 x/y 轴，补全官方仅凭对称直觉的证明空缺。",
    },
    "cpho-2018-semifinal-theory-problem-slice-q5": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方解法（三）（五）由 ρ^2 θ' = C 误推角动量恒为零（丢失一般二维椭圆自由度）的逻辑漏洞。",
    },
    "cpho-2018-semifinal-theory-problem-slice-q6": {
        "kind": "盲解纠出官方笔误",
        "note": "查出第（3）问官方级数漏算球壳内壁自反射 (1-k)(1-E) 份额导致不合空腔黑体定律（算成 227 K，严格值约 217 K）。",
    },
    "cpho-2018-final-theory-problem-slice-q2": {
        "kind": "盲解纠出官方笔误",
        "note": "查出官方第 7 页式 (19)-(20) 根号内 mgd^2 漏乘因子 2 及极板编号笔误。",
    },
    "cpho-2018-final-theory-problem-slice-q4": {
        "kind": "盲解纠出官方笔误",
        "note": "纠出官方第 12 页式 (14) 波腹指标范围 0 < l < Lω/(πu) 既漏 l=0 又引入弦外伪解（应为 0 <= l <= Lω/(πu)-1/2）。",
    },
    "cpho-2019-semifinal-theory-problem-slice-q2": {
        "kind": "盲解更优 + 纠出笔误",
        "note": "补充 μ ∈ [tanθ, 8/3 tanθ) 期间向左倒滑分支（官方误断 μ >= tanθ 即停死），并指出式 (24) l^3 量纲笔误。",
    },
    "cpho-2019-semifinal-theory-problem-slice-q6": {
        "kind": "盲解路径更优",
        "note": "第（2）问全程保留高精度 β 算得 4.52%，指出官方用修约后 0.980c 代入导致 4.59% 精度漂移及文字标注对调。",
    },
    "cpho-2019-final-theory-problem-slice-q6": {
        "kind": "盲解纠出官方笔误",
        "note": "指出官方第 2 iv) 问直接以地表弧长 1900 km 代替垂直观测投影弦长 1614 km 及第 6 问氢质量分数遗漏细节。",
    },
}


def classify(text: str, table: dict[str, str]) -> list[str]:
    hits = [(len(re.findall(p, text)), name) for name, p in table.items()]
    hits = [h for h in hits if h[0] > 0]
    hits.sort(key=lambda h: (-h[0], h[1]))
    return [name for _, name in hits[:3]]


def _extract_block_p1(fname: str, blk: str) -> str:
    """Extract the full original Phase 1 blind-solve workflow from a batch markdown block."""
    lines = blk.splitlines()
    if fname == "batch-13-panpho-2021-2022.md":
        m_de = re.search(r"\*\*拆解\*\*\s*(.*?)\s*\*\*盲做\*\*", blk, re.S)
        m_bl = re.search(r"\*\*盲做\*\*[：:]?\s*(.*?)\s*\*\*对照\*\*", blk, re.S)
        text = ((m_de.group(1).strip() + "\n\n" if m_de else "") + (m_bl.group(1).strip() if m_bl else "")).strip()
        return textwrap.dedent(text).strip()

    secs: list[tuple[str, str]] = []
    cur_h: str | None = None
    cur_lines: list[str] = []
    for line in lines[1:]:
        if re.match(r"^#{3,4}\s+", line):
            if cur_h and line.startswith("#### ") and "batch-08" in fname:
                cur_lines.append(line)
                continue
            if cur_h is not None:
                secs.append((cur_h, "\n".join(cur_lines).strip()))
            cur_h, cur_lines = line, []
        elif cur_h is not None:
            cur_lines.append(line)
    if cur_h is not None:
        secs.append((cur_h, "\n".join(cur_lines).strip()))

    parts: list[str] = []
    for h, body in secs:
        is_p1 = any(
            k in h for k in ["Phase 1", "第一阶段", "独立盲", "盲做", "盲解", "题目拆解与求解脉络", "题目概述与拆解"]
        ) and "对照" not in h
        if fname == "batch-03-cpho-2021-semi.md" and "递进式解题拆解" in h:
            is_p1 = True
        if is_p1 and body:
            parts.append(body)

    text = "\n\n".join(parts).strip()
    text = re.sub(r"(\n---\s*)+$", "", text).strip()
    text = re.sub(r"\n## Part [^\n]+.*$", "", text, flags=re.S).strip()
    text = re.sub(r"(\n---\s*)+$", "", text).strip()
    return textwrap.dedent(text).strip()


def load_blind_processes(valid_ids: set[str]) -> dict[str, str]:
    """Parse all notes/problems/batch-*.md files and extract Phase 1 blind workflows per problem ID."""
    pat = re.compile(
        r"(?<![a-z0-9-])(" + "|".join(re.escape(i) for i in sorted(valid_ids, key=len, reverse=True)) + r")(?![a-z0-9-])"
    )
    out: dict[str, str] = {}
    for p in sorted(glob.glob(str(ROOT / "notes/problems/batch-*.md"))):
        fname = Path(p).name
        lines = Path(p).read_bytes().decode("utf-8").splitlines()
        idxs: list[tuple[int, str]] = []
        for i, line in enumerate(lines):
            if line.startswith("## ") or line.startswith("### "):
                m = pat.search(line)
                if m:
                    idxs.append((i, m.group(1)))
        for k, (start, pid) in enumerate(idxs):
            end = idxs[k + 1][0] if k + 1 < len(idxs) else len(lines)
            out[pid] = _extract_block_p1(fname, "\n".join(lines[start:end]))
    return out


def main() -> None:
    valid = {r["id"] for r in json.loads((ROOT / "catalog/questions.json").read_text()) if r["role"] == "problem"}
    blind_processes = load_blind_processes(valid)
    merged: dict[str, dict] = {}
    problems: list[str] = []
    for f in sorted(glob.glob(str(ROOT / "catalog/teaching-batches/*.json"))):
        try:
            data = json.loads(Path(f).read_text())
        except json.JSONDecodeError as exc:
            problems.append(f"{Path(f).name}: invalid JSON ({exc})")
            continue
        for ident, row in data.items():
            if ident not in valid:
                problems.append(f"{Path(f).name}: unknown id {ident}")
                continue
            miss = [k for k in ("difficulty", "model", "teaching_tags", "teaching") if k not in row]
            miss += [k for k in TEACH_KEYS if k not in row.get("teaching", {})]
            if miss or row["difficulty"] not in DIFFS:
                problems.append(f"{Path(f).name}: {ident} incomplete {miss} {row.get('difficulty')}")
                continue
            if ident in merged:
                problems.append(f"{Path(f).name}: duplicate {ident} (later file wins)")
            blob = row["model"] + " " + " ".join(row["teaching_tags"])
            row = dict(row)
            teaching = dict(row["teaching"])
            bp = blind_processes.get(ident, "")
            if len(bp) < 150:
                problems.append(f"{ident}: extracted blind_process short ({len(bp)} chars)")
            if bp:
                teaching["blind_process"] = bp
            if ident in BLIND_HIGHLIGHTS:
                teaching["blind_highlight"] = BLIND_HIGHLIGHTS[ident]
            row["teaching"] = teaching
            row["domain"] = classify(blob, DOMAIN) or ["综合"]
            row["skills"] = classify(blob, SKILLS) or ["综合建模"]
            row["source_batch"] = Path(f).name
            merged[ident] = row
    out = ROOT / "catalog/teaching-analysis.json"
    out.write_text(json.dumps(merged, ensure_ascii=False, indent=1) + "\n")
    bp_count = sum(1 for v in merged.values() if v["teaching"].get("blind_process"))
    bh_count = sum(1 for v in merged.values() if v["teaching"].get("blind_highlight"))
    print(f"merged {len(merged)} / {len(valid)} problems -> {out.relative_to(ROOT)} (blind_process: {bp_count}, blind_highlight: {bh_count})")
    missing = sorted(valid - set(merged))
    print("not yet analysed:", len(missing))
    for m in missing:
        print("  ", m)
    for p in problems:
        print("WARN", p)


if __name__ == "__main__":
    main()
