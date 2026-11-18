# 全库 283 道物理竞赛单题教学拆解、难点与易错点综合报告

> **分析范围**：`catalog/questions.json` 中全部 **283 道**单题切片与阅读器题目（`CPhO` 137 题、`PanPhO` 16 题、`Physics Cup` 41 题、`PLANCKS` 89 题，年份跨度 2013–2026）。  
> **工作流程**：严格执行**两阶段分析**：Phase 1 仅基于原题图文与题面切片独立盲解并完成量纲/极限/多方法交叉检验；Phase 2 再对照仓库内参考解答与公开获奖评述（共 **239 题**在仓内配对官方/参考解答，另有 **44 题**仓内仅有题面或以数值/极限定理交叉检验验证），拆解解题思路、提炼难点与高频易错点，并写入 `catalog/teaching-batches/*.json` 与 `notes/problems/batch-*.md`。全库共有 **49 题**带有 `blind_highlight` 独立盲解更优或官方勘误高亮标注。  
> **状态说明**：本报告与全部教学标签/拆解数据均为 **AI 独立试做与对照分析结果，供教学整理与备赛参考，尚待一线教练或教师结合原卷人工复核**。

---

## 一、全库覆盖与统计概览

### 1.1 按赛事与解答配对情况统计

| 赛事 | 题数 | 年份与场次 | 仓内已配对参考解答 | 仅题面 / 无官方解答（独立交叉检验） | 难度区间 |
| --- | ---: | --- | ---: | ---: | --- |
| **CPhO** | 137 | 2013–2021（第30–38届）复赛、决赛理论 | 129 | 8（2015 复赛仅官方原题PDF，另行多方法交叉检验） | D1–D5 |
| **PanPhO** | 16 | 2019–2026 Paper 2 | 15 | 1（2024 Q1 卷面标题错配，另行交叉校验） | D3–D5 |
| **Physics Cup** | 41 | 2019–2026（含 2020 Q0） | 36 | 5（2020 Q0, Q2–Q5） | D2–D5 |
| **PLANCKS** | 89 | 2019–2026 预赛与国际决赛 | 59 | 30（2019 决赛、2021 预赛、2022 预赛） | D1–D4 |
| **合计** | **283** | **2013–2026** | **239** | **44** | **D1–D5** |

### 1.2 难度分级分布（D1–D5）

| 难度等级 | 定位 | 题数 | 占比 | 赛事分布 |
| --- | --- | ---: | ---: | --- |
| **D1** | 基础送分 / 竞赛入门核心模型 | 14 | 4.9% | CPhO 7, PLANCKS 7 |
| **D2** | 标准竞赛中档题（概念清晰、推导明确） | 81 | 28.6% | CPhO 44, PLANCKS 36, Physics Cup 1 |
| **D3** | 中高难度选拔题（多步骤耦合 / 技巧性变换） | 117 | 41.3% | CPhO 61, PanPhO 2, PLANCKS 40, Physics Cup 14 |
| **D4** | 高难度压轴 / 科研场景建模题 | 55 | 19.4% | CPhO 22, PanPhO 9, PLANCKS 6, Physics Cup 18 |
| **D5** | 顶尖研究级 / 极强综合与几何技巧难题 | 16 | 5.7% | CPhO 3, PanPhO 5, Physics Cup 8 |

### 1.3 受控领域（`domain`）与方法技能（`skills`）分布

全库共凝练 **1360 个**细粒度教学标签（`teaching_tags`），并映射至受控领域与方法维度（单题可多选）：

- **领域分布（`domain`）**：
  - 力学与刚体（94）、电磁学（84）、热学与统计（72）、光学与波动（67）、流体与连续介质（55）、数学物理与几何（46）、天体与引力（41）、量子与近代物理（40）、相对论（27）、电路与网络（17）、综合（8）
- **方法技能（`skills`）**：
  - 守恒律与能量法（85）、量纲与近似展开（76）、积分与极值优化（70）、类比与对称性（63）、微分方程与振动（53）、几何与作图（52）、参考系与坐标变换（43）、综合建模（37）、统计与概率（34）

---

## 二、Phase 1 盲解 vs. Phase 2 对照参考解答：什么是真正“难”的？（核心难点图谱）

对照 283 题两阶段求解轨迹，区分“计算繁琐”与**真正制约高中及本科竞赛生拿分的结构性难点（Hard Points）**：

1. **物理图像的重构与坐标/空间转化（常见于 Physics Cup、PanPhO）**
   - 例如把普通实空间的复杂动力学转化到**速度端图 / 速度空间**（`physicscup-2022-q2-reader` 的速度空间悬链线、`physicscup-2025-q5-reader` 的开普勒速度端图圆、`physicscup-2026-q1-reader` 的双曲线速度轨迹），或借助**射影几何同素变换 / 泰勒斯圆**还原立体成像（`physicscup-2020-q5-reader`、`physicscup-2022-q4-reader`、`physicscup-2025-q4-reader`）。
   - **难点本质**：题干不提示数学工具，学生若在惯常的 $x(t)$ 或近轴高斯公式里硬算，立刻陷入超越方程无法推进。

2. **隐含自由度与自能 / 多体交叉项的识别（区分 D3 与 D4/D5 的分水岭）**
   - 强磁场导体中的广义动量与**自身诱导极化自能**（`physicscup-2021-q1-reader`：Jaan Kalda 统计首批 8 份无提示提交中有 6 份漏掉主导的铜球自身极化项 $8\pi\varepsilon_0 B^2 R^3 v$；`physicscup-2020-q1-reader` 旋转球偶极相互作用的能量自能修正）。
   - 双导体球靠近时的**无穷电像级数与孤立导体电荷守恒补偿**（`cpho-2020-final-theory-problem-slice-q2`）。
   - 平均场 / 多体系统中“单粒子外场能量 $\times N$”与真实内部互作用能的**双计数因子 $1/2$**（`cpho-2021-final-theory-problem-slice-q5`）。

3. **多物理过程耦合下的分级近似链（常见于 PanPhO、PLANCKS 科研背景题）**
   - 例如等离子体自聚焦（`panpho-2026` 批次：需串接有质动力势、玻尔兹曼响应展开、平方根折射率展开、高斯傍轴展开三级泰勒展开）、假真空衰变瞬子隧穿与薄膜近似（`panpho-2023-paper-2-problem-slice-q1`）、吸积盘粘滞角动量输运与标度律估计（`plancks-2021-final-combined-slice-q3`）。
   - **难点本质**：需要判断哪一小量留在主项、哪一非线性修正决定临界条件，不能凭机械公式硬代。

4. **连续介质 / 波动与拓扑几何效应**
   - 如理想磁流体中的磁通冻结拉伸与等体积放大（`physicscup-2023-q3-reader`）、平底圆柱入水单侧扁椭球附加质量脉冲模型（`physicscup-2024-q1-reader`）、波破折叠焦散与多流态判据（`physicscup-2026-q2-reader`）、圆锥时空/共形映射与偏心圆域热传导（`panpho-2024-paper-2-problem-slice-q2`）。

---

## 三、全库高频“易错点”分类体系（Teaching Pitfalls）

结合 Phase 1 盲做时的险些踩坑记录、Jaan Kalda 赛事评述及 CPhO/PLANCKS 阅卷失分点，高发错误集中于以下六大类：

| 易错大类 | 典型表现与错因机制 | 库内代表题例 |
| --- | --- | --- |
| **1. 定理适用前提误用** | 把平行轴定理用于非质心轴；在非惯性系或含外力偶矩问题中套用质心参考系公式却漏掉惯性力/约束反力矩；混淆孤立导体（总电荷守恒）与接地导体（电势为零）。 | `cpho-2020-final-theory-problem-slice-q7`（半球体平行轴误用）<br>`cpho-2020-final-theory-problem-slice-q2`（漏球心补偿像电荷） |
| **2. 几何角、符号与正方向约定混淆** | 极角逆时针与拱线偏角顺时针反向；端面入射角与侧壁全反射角互余未取余角；离心角当成极角代入椭圆半径；电势导数 $\mathrm{d}\varphi/\mathrm{d}x = -E_x$ 符号搞反。 | `cpho-2021-final-theory-problem-slice-q2`（轨道极角方向）<br>`cpho-2021-final-theory-problem-slice-q4`（PB方程符号）<br>`plancks-2024-final-combined-slice-q6`（椭圆离心角陷阱）<br>`plancks-2026-final-problem-slice-q9`（波导互余角） |
| **3. 热统与多体因子 $1/2$、自由度及展开阶数遗漏** | 内能双计数漏 $1/2$；二维谐振子/理想气体能量均分自由度错数；高斯脉冲宽度（FWHM vs. $e^{-2}$ 强度/场强定义）差 $\sqrt{2}$ 或 $2$ 倍；压电/铁磁/等离子体极化方向导致色散符号反转。 | `cpho-2021-final-theory-problem-slice-q5`（磁能少 $1/2$）<br>`cpho-2020-final-theory-problem-slice-q5`（圆极化 $\mp$ 反号）<br>`panpho-2025-paper-2-problem-slice-q2`（脉冲半高全宽因子） |
| **4. 相对论不变量与动量/动能混淆** | 把高能粒子“总能量”当作“动能”；假设“动能相同”就等价于“速度或总能相同”；光子钟往返路程漏把水平位移 $VT'$ 除以 2；微扰展开把 $1-\sqrt{\frac{1-\beta}{1+\beta}}\approx\beta$ 误写为有限大值。 | `cpho-2020-final-theory-problem-slice-q6`（6.8 GeV 总能量 vs 动能）<br>`plancks-2020-final-problem-slice-q3`（光子钟 $VT'/2$）<br>`plancks-2021-final-combined-slice-q12`（多普勒近似） |
| **5. 边界条件、对称镜像与无穷项遗漏** | 紧贴边界双向发射漏算后向半球全反射逃逸锥；平行板间无穷镜像只算单像导致通量错 $1/2$；并联电阻写成电导形式引起量纲破坏；数值中间步骤过度取整引起最终有效数字偏离。 | `physicscup-2026-q5-reader`（水晶球双向逃逸锥）<br>`physicscup-2020-q4-reader`（无穷镜像偶极子通量）<br>`cpho-2021-final-theory-problem-slice-q1`（波带片中间结果取整） |
| **6. 量纲、单位换算与近似区间越界** | $\mu\text{m}\to\text{cm}$ 换算漏 $10^{-8}$；重离子能量 $\text{MeV/u}$ 漏乘核子数 $A=12$；非对易算符强行套用一阶截断 BCH 公式；用过时稳态或无阻尼模型代替临界阻尼过渡态。 | `plancks-2020-final-problem-slice-q4`（微米/厘米换算）<br>`plancks-2023-final-combined-slice-q7`（$^{12}\text{C}$ 漏乘核子数）<br>`plancks-2024-final-combined-slice-q2`（四元数不可直接用一阶 BCH） |

---

## 四、Phase 2 对照参考解答时识别出的原卷与解答勘误线索

在严格独立试做后再核对官方解答，能有效避免“盲从参考答案”。全库共记录多处疑似印刷笔误或官方解答细节瑕疵（**均已在对应题目的 `comparison` 与笔记中并列标注原式与勘误推导，仍建议人工复核原卷PDF**）：

- **排版与标题错配**：`panpho-2024-paper-2-problem-slice-q1` PDF 第 2 页顶部误沿用 2022 年卷二第 1 题的旧英文标题 `Spatiotemporal varying electric permittivity`；题目本身实际考查的是另一模型，阅卷与阅读切分需注意区分。
- **典型公式与计算笔误清单（部分摘录）**：
  - `plancks-2020-final-problem-slice-q1`：第 3 页将求解黄金比例所用的二次方程误印为 $T^2 - T - 1 = 0$，但所取根实为 $T^2 + T - 1 = 0$ 的正根 $(\sqrt{5}-1)/2$。
  - `plancks-2020-final-problem-slice-q4`：第 (b) 问计算迁移率 $\mu$ 时直接乘以 $1.33^2$ 而未将 $\mu\text{m}$ 换算为 $\text{cm}$（量纲/数量级差 $10^{-8}$）。
  - `plancks-2021-final-combined-slice-q5`：第 4 问将 $\partial P/\partial r$ 近似为 $P/r$ 时漏掉负号，得出 $(1+c^2/\Omega^2 r^2)^{1/2}$ 而非正确减号。
  - `plancks-2021-final-combined-slice-q7`：第 2 问误将并联电阻 $R_P$ 写成电导形式 $(r+R)/(2rR)$，使代入 GMR 后量纲不自洽。
  - `plancks-2021-final-combined-slice-q12`：第 3 问 $\sqrt{1.445\times 10^{18}\text{ Hz}^2}$ 误开方为 $1.700\text{ GHz}$（应为 $1.202\text{ GHz}$）；第 5 问将 $1-\frac{1}{1+v/c}$ 误印为 $\frac{c}{c+v}$。
  - `plancks-2023-final-combined-slice-q7`：第 (x) 问算碳核 $^{12}\text{C}$ 动量比时漏乘核子数 12 且倒置比值 $2/6$。
  - `plancks-2024-final-combined-slice-q6`：第 (b) 问将椭圆参数方程的离心角直接当成极角计算极大半径（盲解阶段已提前预警该常见误区）。
  - `plancks-2026-final-problem-slice-q5`：第 6 问表格第 4 行超大质量双黑洞的啁啾质量输入疑似存在计算器按键笔误。
  - `panpho-2025-paper-2-problem-slice-q2`：A2 小问在数值代入时由 $\sqrt{\ln 2} = 35\,\text{fs}/\tau_p$ 算出的数值存在笔误。
  - **CPhO 第30–36届（2013–2019）典型笔误与盲解优势摘录**（共新增 25 题高亮，全库合计 49 题）：
    - `cpho-2013-final-theory-problem-slice-q4`：原卷电路图电池正负极画反（左长右短）而官方解答仍按正电势代入。
    - `cpho-2015-final-theory-problem-slice-q2`：官方（10）–（12）式误将导轨长度 $500\,\text{m}$ 当作 $5.0/0.50$ 代入导致加速度与电流数值级联偏差。
    - `cpho-2016-semifinal-theory-problem-slice-q6`：原卷与官方图将第 $i+1$ 倍增级误绘在底边（排版错位），盲解用跨阳极电势差净电荷记账法亦大幅简化级数求和。
    - `cpho-2017-semifinal-theory-problem-slice-q5`：官方式 (14) $r_{\max}$ 符号笔误，且式 (19)–(20) 漏掉磁场上限 $B \le B_{\max}$ 约束存在物理反例。
    - `cpho-2018-semifinal-theory-problem-slice-q6`：第（3）问官方级数漏算球壳内壁自反射 $(1-k)(1-E)$ 份额，算出 $227\,\text{K}$ 而严格空腔黑体解约 $217\,\text{K}$。
    - `cpho-2019-semifinal-theory-problem-slice-q2`：补充 $\mu \in [\tan\theta, \tfrac{8}{3}\tan\theta)$ 期间向左倒滑分支（官方误断 $\mu \ge \tan\theta$ 即停死），并指出式 (24) $l^3$ 量纲笔误。

---

## 五、分学段教学与单题训练建议

### 5.1 高中物理竞赛生（CPhO 复赛/决赛 & PanPhO 提升）

1. **起步阶段（D1–D2，优先筛选标签含 `量纲分析` / `守恒律与能量法`）**：
   - 先用 CPhO 2013–2021 复赛 D1–D2 题与 PLANCKS D1–D2 概念建模题打牢“先做极限检验、先查正负号、先区分质心系与实验室系”三项基本功。
2. **核心突破（D3–D4，CPhO 压轴 + PanPhO Paper 2）**：
   - 重点训练**非典型几何/代数模型拆解**：如 `cpho-2020-final-theory-problem-slice-q2`（电像法逐级补偿）、`cpho-2021-final-theory-problem-slice-q4`（从物理图像写出泊松-玻尔兹曼边界条件而不死背结论）、`panpho-2020-paper-2-problem-slice-q1`（微元近似与量级自检）。
   - **刻意练习“中间不取整、量纲结尾验算”**：每题做完必须对所有字母表达式检验 $\theta\to 0$、$\alpha\to 0$ 或极限质量比下的退化行为。

### 5.2 本科物理竞赛生（PLANCKS & Physics Cup & 研究型建模）

1. **PLANCKS 全覆盖策略（多学科广度 + 科研建模 + 防粗心）**：
   - 题干往往带有真实科研论文背景（量子信息、天体吸积盘、二维材料、非线性光学），阅读量大。单题训练时用网站的**教学拆解四步法**：先提取物理模型（`model`）与主导量级（`量纲与近似展开`），再核对边界/渐近条件，特别警惕官方题面中的近似约定（例如 FWHM 定义、参考能量零点）。
2. **Physics Cup 拔高策略（D4–D5，思路重构训练）**：
   - **严禁过早看解答**：建议按“盲做 30 分钟 $\to$ 卡壳时仅查看网站里的 `teaching_tags` 关键词提示（如 `速度端图`、`射影几何`、`广义动量`） $\to$ 再独立推导”三段式训练。
   - 重点研读 `Physics Cup 2021 Q1`（铜哑铃自身极化）、`2022 Q2`（速度空间悬链线）、`2025 Q4/Q5`、`2026 Q1–Q5`，培养“寻找守恒量 / 几何变换 / 对偶性”的竞赛直觉。

---

## 六、分批次原始记录索引（`notes/problems/` & `catalog/teaching-batches/`）

全部 283 题均可在以下批次报告与 JSON 数据中检索：

- `batch-01-cpho-2020-semi`（8 题）：CPhO 2020 复赛理论 Q1–Q8
- `batch-02-cpho-2020-final`（7 题）：CPhO 2020 决赛理论 Q1–Q7
- `batch-03-cpho-2021-semi`（8 题）：CPhO 2021 复赛理论 Q1–Q8
- `batch-04-cpho-2021-final`（5 题）：CPhO 2021 决赛理论 Q1–Q5
- `batch-06-panpho-2023-2026`（8 题）：PanPhO 2023–2026 卷二
- `batch-07-plancks-2024`（10 题）：PLANCKS 2024 国际决赛 Q1–Q10
- `batch-08-physicscup-2019-2020`（与 `batch-14-physicscup-2020.json` 对应，合计 11 题）：Physics Cup 2019 Q1–Q5 + 2020 Q0–Q5
- `batch-09-physicscup-2021-2022`（10 题）：Physics Cup 2021–2022
- `batch-10-physicscup-2023-2024`（10 题）：Physics Cup 2023–2024
- `batch-11-physicscup-2025-2026`（10 题）：Physics Cup 2025–2026
- `batch-12-panpho-2019-2020`（4 题）：PanPhO 2019–2020 卷二
- `batch-13-panpho-2021-2022`（4 题）：PanPhO 2021–2022 卷二
- `batch-17-plancks-2019-2020`（19 题）：PLANCKS 2019 决赛 Q1–Q10 + 2020 决赛 Q1–Q9
- `batch-18-plancks-2021`（22 题）：PLANCKS 2021 预赛 Q1–Q10 + 决赛 Q1–Q12
- `batch-19-plancks-2022-2023`（20 题）：PLANCKS 2022 预赛 Q1–Q10 + 2023 决赛 Q1–Q10
- `batch-20-plancks-2025-2026`（18 题）：PLANCKS 2025 决赛 Q1–Q9 + 2026 决赛 Q1–Q9
- `batch-21-cpho-2013`（16 题）：CPhO 第30届（2013）复赛理论 Q1–Q8 + 决赛理论 Q1–Q8
- `batch-22-cpho-2014`（16 题）：CPhO 第31届（2014）复赛理论 Q1–Q8 + 决赛理论 Q1–Q8
- `batch-23-cpho-2015`（16 题）：CPhO 第32届（2015）复赛理论 Q1–Q8 + 决赛理论 Q1–Q8
- `batch-24-cpho-2016`（16 题）：CPhO 第33届（2016）复赛理论 Q1–Q8 + 决赛理论 Q1–Q8
- `batch-25-cpho-2017`（16 题）：CPhO 第34届（2017）复赛理论 Q1–Q8 + 决赛理论 Q1–Q8
- `batch-26-cpho-2018`（16 题）：CPhO 第35届（2018）复赛理论 Q1–Q8 + 决赛理论 Q1–Q8
- `batch-27-cpho-2019`（13 题）：CPhO 第36届（2019）复赛理论 Q1–Q7 + 决赛理论 Q1–Q6
