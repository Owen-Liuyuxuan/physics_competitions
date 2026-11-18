# Batch 26: 第35届全国中学生物理竞赛复赛与决赛理论试题（CPhO 2018）独立盲解与教学拆解

> **说明**：本笔记严格执行两阶段教练协议：
> - **Phase 1（独立盲解）**：仅查看 `derived/questions/cpho-2018-*-problem-slice-q*/page-*.jpg` 原题图像与附图，独立构建物理模型、完成全步骤推导，并作量纲与极限校核；
> - **Phase 2（对照拆解）**：随后逐页核对 `cpho-2018-*-solution-slice-q*/page-*.jpg` 官方参考解答，对比思路优劣、勘正官方笔误/物理漏洞（如复赛第6题第(3)问腔内多次反射遗漏导致的 \(10\text{ K}\) 偏差、复赛第5题解法三/五强行令 \(C=0\)、决赛第2题第(2)问根号内系数笔误、决赛第4题波腹指标范围疏漏等），并提炼面向高中竞赛生与本科普物学生的核心难点与迁移方法。

---

# 复赛理论试题（Semifinal Theory）

## 1. 第35届复赛理论第1题 · 空间站水平发射物体的轨道判据、落地速度与坠落时间 (`cpho-2018-semifinal-theory-problem-slice-q1`)

- **难度评级**：`D2`
- **物理模型**：有心平方反比引力场中的开普勒轨道极值（近地点/远地点判据）与径向-时间积分动力学模型
- **教学标签**：`开普勒轨道判据`、`角动量与机械能守恒`、`近地点与坠地边界`、`径向运动时间积分`、`量纲与极限校验`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **物体绕地球做周期运动的初速度条件**
   设小物体的质量为 \(m\)，发射点到地心的距离为 \(r_0 = R + h\)。由于初速度 \(\vec{v}_0\) 方向与到地心连线垂直（即水平发射），发射点必为轨道的拱点（近地点或远地点）。物体绕地球做周期运动（圆或椭圆闭合轨道）须同时满足两个条件：
   - **束缚态条件（总机械能为负）**：
     \[
     E = \frac{1}{2}m v_0^2 - \frac{GMm}{R+h} < 0 \implies v_0 < \sqrt{\frac{2GM}{R+h}}.
     \]
   - **不坠地条件（近地点距地心 \(r_p > R\)）**：
     当 \(v_0 \ge \sqrt{\frac{GM}{R+h}}\) 时，发射点 \(r_0 = R + h\) 为圆轨道位置或椭圆近地点，故最小地心距 \(r_{\min} = R + h > R\) 自动满足。当 \(v_0 < \sqrt{\frac{GM}{R+h}}\) 时，发射点为椭圆远地点；设临界情形下椭圆近地点恰好与地面相切（\(r_p = R\)），此时速度大小为 \(v_p\)，由角动量守恒与机械能守恒有：
     \[
     m v_0 (R + h) = m v_p R \implies v_p = \frac{R+h}{R} v_0,
     \]
     \[
     \frac{1}{2}m v_0^2 - \frac{GMm}{R+h} = \frac{1}{2}m v_p^2 - \frac{GMm}{R}.
     \]
     将 \(v_p\) 代入能量方程整理：
     \[
     \frac{1}{2}v_0^2 \left[\left(\frac{R+h}{R}\right)^2 - 1\right] = GM\left(\frac{1}{R} - \frac{1}{R+h}\right) \implies \frac{1}{2}v_0^2 \frac{h(2R+h)}{R^2} = \frac{GMh}{R(R+h)}.
     \]
     消去 \(h > 0\)，解得临界最小发射速度：
     \[
     v_{0\min} = \sqrt{\frac{2GMR}{(R+h)(2R+h)}}.
     \]
     （校验：\(h \to 0\) 时 \(v_{0\min} \to \sqrt{GM/R}\)，即近地第一宇宙速度；\(h \gg R\) 时 \(v_p \to \sqrt{2GM/R}\)，与抛物线逃逸相吻合。）
     若要求不撞击地面持续绕地球做周期运动（排除贴地擦过情形），初速度大小须满足：
     \[
     \sqrt{\frac{2GMR}{(R+h)(2R+h)}} < v_0 < \sqrt{\frac{2GM}{R+h}}.
     \]

2. **能落到地面时落地速度的大小、方向及飞行时间**
   当 \(0 \le v_0 \le v_{0\min}\) 时物体落到地面（\(v_0 = v_{0\min}\) 为相切擦地临界，\(v_0 = 0\) 为竖直自由落体）。
   - **落地速度大小 \(v_1\)**：由机械能守恒（\(r = R + h \to r = R\)）：
     \[
     \frac{1}{2}m v_1^2 - \frac{GMm}{R} = \frac{1}{2}m v_0^2 - \frac{GMm}{R+h} \implies v_1 = \sqrt{v_0^2 + \frac{2GMh}{R(R+h)}}.
     \]
   - **落地速度方向（与当地水平方向夹角 \(\alpha\)）**：由角动量守恒，落地时速度的水平（切向）分量 \(v_{1\theta}\) 满足 \(m v_{1\theta} R = m v_0 (R + h)\)，故：
     \[
     v_{1\theta} = \frac{R+h}{R} v_0.
     \]
     因此速度斜向下与当地水平面的夹角 \(\alpha \in [0, \pi/2]\) 满足：
     \[
     \cos\alpha = \frac{v_{1\theta}}{v_1} = \frac{(R+h)v_0}{R\sqrt{v_0^2 + \frac{2GMh}{R(R+h)}}} = \frac{(R+h)v_0}{\sqrt{R^2 v_0^2 + \frac{2GMRh}{R+h}}}, \qquad \alpha = \arccos\left[\frac{(R+h)v_0}{\sqrt{R^2 v_0^2 + \frac{2GMRh}{R+h}}}\right].
     \]
     （校验：\(v_0 = 0 \implies \alpha = \pi/2\) 竖直落地；\(v_0 = v_{0\min} \implies \cos\alpha = 1 \implies \alpha = 0\) 水平相切。）
   - **发射到落地所需时间 \(t\)**：在极坐标 \((r, \theta)\) 中，令 \(r_0 = R + h\)。由角动量守恒 \(r^2\dot{\theta} = v_0 r_0\) 与机械能守恒：
     \[
     \frac{1}{2}\left[\left(\frac{\mathrm{d}r}{\mathrm{d}t}\right)^2 + r^2\dot{\theta}^2\right] - \frac{GM}{r} = \frac{1}{2}v_0^2 - \frac{GM}{r_0}.
     \]
     消去 \(\dot{\theta}\)，且因发射后物体单调下落（在 \(r_0\) 处 \(\dot{r}=0\) 且 \(\ddot{r} = \frac{v_0^2}{r_0} - \frac{GM}{r_0^2} < 0\)，在到达近地点 \(r_p \le R\) 前恒有 \(\dot{r} < 0\)）：
     \[
     \frac{\mathrm{d}r}{\mathrm{d}t} = -\frac{1}{r}\sqrt{-v_0^2 r_0^2 + 2GM r + \left(v_0^2 - \frac{2GM}{r_0}\right)r^2}.
     \]
     分离变量并积分（\(r\) 从 \(R+h\) 积到 \(R\)）：
     \[
     t = \int_R^{r_0} \frac{r\,\mathrm{d}r}{\sqrt{a + br + cr^2}},
     \]
     其中
     \[
     a = -v_0^2 r_0^2, \qquad b = 2GM, \qquad c = v_0^2 - \frac{2GM}{r_0} < 0.
     \]
     计算判别式 \(\Delta = b^2 - 4ac\)：
     \[
     \Delta = 4G^2M^2 + 4 v_0^2 r_0^2 \left(v_0^2 - \frac{2GM}{r_0}\right) = 4\left(GM - v_0^2 r_0\right)^2 > 0.
     \]
     因 \(v_0^2 \le v_{0\min}^2 < \frac{GM}{r_0}\)，有 \(GM - v_0^2 r_0 > 0\)，故 \(\sqrt{\Delta} = 2(GM - v_0^2 r_0)\)。套用题给积分公式：
     \[
     t = \left[\frac{\sqrt{a + br + cr^2}}{c} - \frac{b}{2(-c)^{3/2}}\arcsin\frac{2cr + b}{\sqrt{\Delta}}\right]_{R}^{r_0}.
     \]
     在上限 \(r = r_0\) 处：\(a + br_0 + cr_0^2 = 0\)，且 \(\frac{2cr_0 + b}{\sqrt{\Delta}} = \frac{2v_0^2 r_0 - 2GM}{2(GM - v_0^2 r_0)} = -1\)，故 \(\arcsin(-1) = -\frac{\pi}{2}\)。
     在下限 \(r = R\) 处：
     \[
     a + bR + cR^2 = \frac{2GMRh}{R+h} - v_0^2 h(2R+h),
     \]
     \[
     \frac{2cR + b}{\sqrt{\Delta}} = \frac{v_0^2 R(R+h) - GM(R-h)}{(R+h)\left[GM - v_0^2(R+h)\right]} = \frac{v_0^2 R(R+h) - GM(R-h)}{GM(R+h) - v_0^2(R+h)^2}.
     \]
     汇总得：
     \[
     t = \frac{R+h}{2GM - v_0^2(R+h)}\sqrt{\frac{2GMRh}{R+h} - v_0^2 h(2R+h)} + GM\left[\frac{R+h}{2GM - v_0^2(R+h)}\right]^{3/2}\left[\frac{\pi}{2} + \arcsin\frac{v_0^2 R(R+h) - GM(R-h)}{GM(R+h) - v_0^2(R+h)^2}\right].
     \]
     （极限检验：① \(v_0 = v_{0\min}\) 时根号项为零，\(\arcsin\) 宗量为 \(+1\)，给出 \(t = \pi\sqrt{\frac{(2R+h)^3}{8GM}}\)，恰好为半长轴 \(a_{\text{ell}} = \frac{2R+h}{2}\) 的半个椭圆周期；② \(v_0=0, h\ll R\) 时展开得 \(t \approx \sqrt{2h/g}\)，完全自洽。）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（2）问的全部结论与官方解答（`page-1.jpg`–`page-3.jpg`）完全一致，连第（2）问最终时间表达式（⑮式）及相切临界时间都逐项吻合。官方第（1）问还额外给出了一种极其精妙的**韦达定理解法（解法二）**：消去近/远地点速度 \(v_2\) 后，得到关于 \(1/r_2\) 的一元二次方程，已知 \(1/r_1\) 必为其中一根，由韦达定理直接读出另一拱点倒数 \(\frac{1}{r_2} = \frac{1}{r_1}\left(\frac{2GM}{r_1 v_1^2} - 1\right)\)，再令 \(0 < \frac{1}{r_2} < \frac{1}{R}\) 一步锁定区间！
- **官方细节注记**：官方解答（2）式⑥写了严格不等号 \(v_0 < v_{0\min}\)，实际在边界 \(v_0 = v_{0\min}\) 处轨迹与地表相切（算贴地擦过），官方并在最后补充给出了该临界值下的半周期落地时间。
- **核心难点与典型易错点**：
  - 难点1：由“周期运动”同时导出双边速度约束——上界由 \(E<0\)（不逃逸）决定，下界由近地点 \(r_p > R\)（不坠地）决定。
  - 难点2：判断时间积分过程中 \(\mathrm{d}r/\mathrm{d}t\) 单调负号，以及正确提取 \(\sqrt{\Delta} = 2(GM - v_0^2 r_0) > 0\) 的正根号符号。
  - 易错点1：只写 \(v_0 \ge \sqrt{GM/(R+h)}\) 而漏掉“发射点作为远地点”的椭圆轨道区域（\(v_{0\min} < v_0 < \sqrt{GM/(R+h)}\)）。
  - 易错点2：求积分上下限时错误丢弃 \(r = r_0\) 处 \(\arcsin(-1) = -\pi/2\) 的常数项，导致整体少掉 \(\frac{\pi}{2}\)。
- **教练总结与迁移建议**：在有心引力轨道极值问题中，优先把“已知一点切向速度求另一拱点”转化为关于 \(1/r\) 的二次方程并用韦达定理，可避免机械区分发射点究竟是近地点还是远地点。

---

## 2. 第35届复赛理论第2题 · 干摩擦水平弹簧振子的分阶段制动、往返次数与总路程 (`cpho-2018-semifinal-theory-problem-slice-q2`)

- **难度评级**：`D2`
- **物理模型**：含库仑干摩擦的片断简谐振动（移动平衡点与静摩擦死区）及功能原理能量耗散模型
- **教学标签**：`干摩擦阻尼振动`、`静摩擦死区`、`分段功能原理`、`往返次数判据`、`等差振幅衰减`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

记静/滑摩擦死区半宽为 \(x_d = \frac{\mu m g}{k} > 0\)。当小球速度为零且所处位置 \(x\) 满足 \(|x| \le x_d\) 时，弹簧弹力 \(k|x| \le \mu mg\)，小球将永久静止。

1. **至多只能向右运动时的最终静止位置与 \(A_0\) 条件**
   “至多只能向右运动”包含“静止不动”与“向右运动一次后停止（不再向左运动）”两类情况：
   - **情况 1a（始终静止）**：若 \(0 < A_0 \le x_d = \frac{\mu m g}{k}\)，初始弹力 \(kA_0 \le \mu mg\)，小球无法克服最大静摩擦，最终静止于初始位置：
     \[
     x_f = -A_0 \qquad \left(0 < A_0 \le \frac{\mu m g}{k}\right).
     \]
   - **情况 1b（向右运动一次后停止）**：若 \(A_0 > x_d\)，小球向右运动，由功能原理，至第一次速度为零位置 \(x_1\) 时：
     \[
     \frac{1}{2}k A_0^2 - \frac{1}{2}k x_1^2 = \mu m g (A_0 + x_1) \implies x_1 = A_0 - 2x_d = A_0 - \frac{2\mu mg}{k}.
     \]
     此后不再向左运动的条件为 \(k x_1 \le \mu mg \iff x_1 \le x_d\)（此时必有 \(x_1 > -x_d\)），即 \(\frac{\mu mg}{k} < A_0 \le \frac{3\mu mg}{k}\)。其中：
     - 当 \(\frac{\mu mg}{k} < A_0 \le \frac{2\mu mg}{k}\) 时，停在原点左侧或原点：\(x_f = A_0 - \frac{2\mu mg}{k} \le 0\)；
     - 当 \(\frac{2\mu mg}{k} < A_0 \le \frac{3\mu mg}{k}\) 时，停在原点右侧：\(x_f = A_0 - \frac{2\mu mg}{k} > 0\)。
   综上，至多只能向右运动的总条件为 \(0 < A_0 \le \frac{3\mu mg}{k}\)。

2. **完成第一次向右运动至原点右边后，至多只能向左运动**
   完成第一次向右运动至原点右边要求 \(x_1 > 0 \iff A_0 > \frac{2\mu mg}{k}\)。此后“至多只能向左运动”按字面亦含两分支：
   - 若 \(\frac{2\mu mg}{k} < A_0 \le \frac{3\mu mg}{k}\)，停在 \(x_1 = A_0 - \frac{2\mu mg}{k} \in (0, x_d]\)，不向左折返；
   - 若 \(A_0 > \frac{3\mu mg}{k}\)，小球自 \(x_1\) 向左运动，再次停下于 \(x_2\)，由功能原理 \(\frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2 = \mu mg(x_1 - x_2)\) 得：
     \[
     x_2 = 2x_d - x_1 = \frac{4\mu mg}{k} - A_0.
     \]
     此后不再向右折返要求 \(x_2 \ge -x_d \iff A_0 \le \frac{5\mu mg}{k}\)。其中 \(\frac{3\mu mg}{k} < A_0 \le \frac{4\mu mg}{k}\) 时 \(x_f = \frac{4\mu mg}{k} - A_0 \ge 0\)；\(\frac{4\mu mg}{k} < A_0 \le \frac{5\mu mg}{k}\) 时 \(x_f = \frac{4\mu mg}{k} - A_0 < 0\)。

3. **只能完成 \(n\) 次往返运动的最终静止位置与 \(A_0\) 条件**
   每完成半次摆动，只要起点在死区外（\(|x_{j-1}| > x_d\)），转向点坐标便满足递推 \(x_j = (-1)^{j-1}(A_0 - 2jx_d)\)。按题意“向右经过原点，然后向左经过原点，算 1 次往返”，完成第 \(n\) 次往返即要求第 \(2n\) 个转向点在原点左侧（\(x_{2n} < 0\)，对应 \(A_0 > 4nx_d\)），同时第 \((n+1)\) 次往返未能完成（即 \(x_{2n+2} \ge 0\) 若能启动第 \(2n+2\) 程，等价于 \(A_0 \le (4n+4)x_d\)；注：到达原点 \(x=0\) 停止不算“经过原点”）。
   因此完成 \(n\) 次往返的总区间为 \(\frac{4n\mu mg}{k} < A_0 \le \frac{4(n+1)\mu mg}{k}\)（对 \(n=0\) 亦成立），内部细分四小段（对应 \(j = 2n, 2n+1, 2n+2\) 三种停顿程数）：
   - 当 \(\frac{4n\mu mg}{k} < A_0 \le \frac{(4n+1)\mu mg}{k}\) 时（经历 \(2n\) 程停于第 \(n\) 次向左过原点后）：
     \[
     x_f = \frac{4n\mu mg}{k} - A_0 < 0;
     \]
   - 当 \(\frac{(4n+1)\mu mg}{k} < A_0 \le \frac{(4n+3)\mu mg}{k}\) 时（第 \(2n+1\) 程向右停下，其中在 \(\frac{(4n+2)\mu mg}{k}\) 处跨过原点，但此后不能向左折返）：
     \[
     x_f = A_0 - \frac{2(2n+1)\mu mg}{k} \quad \text{（}\le 0 \text{ 或 } > 0\text{）};
     \]
   - 当 \(\frac{(4n+3)\mu mg}{k} < A_0 \le \frac{4(n+1)\mu mg}{k}\) 时（第 \(2n+2\) 程向左折返，但停在原点右侧或恰好停在原点，未能向左经过原点）：
     \[
     x_f = \frac{4(n+1)\mu mg}{k} - A_0 \ge 0.
     \]

4. **只能完成 \(n\) 次往返运动的总路程 \(s\)**
   由全过程功能原理 \(\frac{1}{2}kA_0^2 - \frac{1}{2}kx_f^2 = \mu m g s \implies s = \frac{k}{2\mu mg}(A_0^2 - x_f^2)\)，代入上述三段 \(x_f\) 表达式直接化简：
   - 若 \(\frac{4n\mu mg}{k} < A_0 \le \frac{(4n+1)\mu mg}{k}\)：
     \[
     s = 4n\left(A_0 - \frac{2n\mu mg}{k}\right);
     \]
   - 若 \(\frac{(4n+1)\mu mg}{k} < A_0 \le \frac{(4n+3)\mu mg}{k}\)：
     \[
     s = 2(2n+1)\left(A_0 - \frac{(2n+1)\mu mg}{k}\right);
     \]
   - 若 \(\frac{(4n+3)\mu mg}{k} < A_0 \le \frac{4(n+1)\mu mg}{k}\)：
     \[
     s = 4(n+1)\left(A_0 - \frac{2(n+1)\mu mg}{k}\right).
     \]
   （注：若 \(n=0\) 且 \(0 < A_0 \le \mu mg/k\)，总路程 \(s=0\) 仍符合首式。）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（3）、（4）问与官方解答（`page-4.jpg`–`page-6.jpg`）完全一致，官方第（4）问同样采用全过程功能原理 \(s = \frac{k}{2\mu mg}(A_0^2 - x^2)\) 一步求得三大区间路程（⑱⑲⑳式）。
- **官方细节与微妙差异勘察**：
  1. 第（2）问中，题干写的是“完成第一次向右运动至原点右边后，**至多**只能向左运动”，严格按汉语逻辑理应包含“到达 \(x_1 \in (0, x_d]\) 后根本不再向左运动”的 \(\frac{2\mu mg}{k} < A_0 \le \frac{3\mu mg}{k}\) 段；但官方解答第（2）问仅给出了向左运动一段并停下的 \(\frac{3\mu mg}{k} < A_0 \le \frac{5\mu mg}{k}\)（因前者已在第（1）问⑥⑦式写出）。
  2. 官方 `page-4.jpg` 第（1）问倒数第5行在推导 \(x \le 0\) 情况时，误用了尚未定义的符号 \(B_1\)（写成 \(F = k|B_1| = 2\mu mg - kA_0 \le \mu mg\)，实指 \(k|x|\)）。
- **核心难点与典型易错点**：
  - 难点1：准确区分“到达原点右边且不折返”“跨过原点但未完成反向过原点”等细碎的半程边界，理解第 \(n\) 次往返与第 \(n+1\) 次往返之间跨越了 \(2n, 2n+1, 2n+2\) 三个不同静止阶段。
  - 易错点1：第（1）问漏掉 \(0 < A_0 \le \mu mg/k\) 的零位移静止情形；或第（3）问误以为完成 \(n\) 次往返就必然停在 \(x_{2n}\)，忽略了还可以多走半程停在 \(x_{2n+1}\)（即使过了原点右侧也不构成完整一次往返）甚至走近一程停在 \(x_{2n+2} \ge 0\)。
  - 易错点2：求总路程时逐段累加位移再求和，远不如直接对首末状态套用 \(\frac{1}{2}kA_0^2 - \frac{1}{2}kx_f^2 = \mu m g s\) 快速且不易错。
- **教练总结与迁移建议**：带干摩擦的弹簧振子有两个万能抓手：① 每次单向半程端点对称于等效平衡点 \(\mp x_d\)，故绝对振幅每次精确缩减 \(2x_d\)；② 求总路程永远用全局功能原理 \(s = \frac{k}{2\mu mg}(A_0^2 - x_f^2)\)。

---

## 3. 第35届复赛理论第3题 · 打击中心碰撞悬杆的轴力演化及撤轴后的抛体翻转 (`cpho-2018-semifinal-theory-problem-slice-q3`)

- **难度评级**：`D3`
- **物理模型**：刚体定轴打击中心碰撞、物理摆质心加速反力分解及自由平抛—自转耦合运动
- **教学标签**：`打击中心`、`转轴支反力`、`复合摆等效摆长`、`平抛与绕质心转动`、`质心运动定理`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **杆的打击中心到 \(O\) 点的距离 \(d\)**
   设水平外冲量 \(J\)（或力 \(F\)）垂直作用于静止细杆距 \(O\) 点为 \(d\) 处，转轴对杆水平作用力为零。由定轴转动定理与质心运动定理：
   \[
   I_0 \alpha = \frac{1}{3}M l^2 \alpha = F d, \qquad M a_{cx} = M \frac{l}{2} \alpha = F.
   \]
   消去 \(F\) 与 \(\alpha\) 得打击中心距 \(O\) 的距离：
   \[
   d = \frac{I_0}{M(l/2)} = \frac{\frac{1}{3}Ml^2}{\frac{1}{2}Ml} = \frac{2}{3}l.
   \]

2. **撤除转轴前杆转过 \(\theta\)（\(0 \le \theta < \pi\)）角时转轴对杆的作用力**
   弹丸嵌入杆中距 \(O\) 点 \(d = \frac{2}{3}l\) 处，因打击过程中转轴水平力为零，系统水平动量守恒：\(m v_0 = (M+m)v_c\)，或由对 \(O\) 点角动量守恒：
   \[
   m v_0 \left(\frac{2}{3}l\right) = \left[\frac{1}{3}Ml^2 + m\left(\frac{2}{3}l\right)^2\right]\omega_0 = \frac{3M+4m}{9}l^2 \omega_0 \implies \omega_0 = \frac{6 m v_0}{(3M+4m)l}.
   \]
   复合系统总质量 \(M_{\text{tot}} = M + m\)，复合质心 \(C\) 到 \(O\) 的距离为：
   \[
   L_c = \frac{M\frac{l}{2} + m\frac{2l}{3}}{M + m} = \frac{3M+4m}{6(M+m)}l,
   \]
   系统绕 \(O\) 的转动惯量 \(I = \frac{3M+4m}{9}l^2\)。注意等效单摆摆长为：
   \[
   l_{\text{eff}} = \frac{I}{M_{\text{tot}} L_c} = \frac{\frac{3M+4m}{9}l^2}{\frac{3M+4m}{6}l} = \frac{2}{3}l,
   \]
   与 \(M, m\) 无关！由机械能守恒，转过 \(\theta\) 角（如图沿**顺时针**方向转过 \(\theta\)）时角速度 \(\omega\) 与角加速度 \(\beta'\)（取顺时针反向，即减速）满足：
   \[
   \frac{1}{2}I\omega^2 = \frac{1}{2}I\omega_0^2 - (M+m)g L_c (1 - \cos\theta) \implies \omega^2 = \omega_0^2 - \frac{3g}{l}(1 - \cos\theta),
   \]
   \[
   I \beta' = -(M+m)g L_c \sin\theta \implies \beta' = -\frac{3g}{2l}\sin\theta.
   \]
   （注：杆能转半圈到达 \(\theta=\pi\) 要求 \(\omega_0^2 > \frac{6g}{l}\)，即 \(v_0 > \frac{3M+4m}{m}\sqrt{\frac{gl}{6}}\)。）
   在图 \(x\)-\(y\) 坐标系中，顺时针转过 \(\theta\) 时复合质心坐标为 \(x_c = -L_c\sin\theta\)，\(y_c = -L_c\cos\theta\)。对时间求二阶导数得质心加速度分量：
   \[
   a_{cx} = -L_c\cos\theta\,\beta' + L_c\sin\theta\,\omega^2 = L_c\sin\theta\left(\frac{3g}{2l}\cos\theta + \omega^2\right),
   \]
   \[
   a_{cy} = L_c\sin\theta\,\beta' + L_c\cos\theta\,\omega^2 = L_c\left(\omega^2\cos\theta - \frac{3g}{2l}\sin^2\theta\right).
   \]
   由质心运动定理 \(F_x = (M+m)a_{cx}\)、\(F_y = (M+m)(g + a_{cy})\)，代入 \((M+m)L_c = \frac{3M+4m}{6}l\) 与 \(\omega^2 = \frac{36m^2 v_0^2}{(3M+4m)^2 l^2} - \frac{3g}{l}(1 - \cos\theta)\) 化简：
   \[
   F_x = \left[\frac{6m^2 v_0^2}{(3M+4m)l} - \frac{3M+4m}{2}g + \frac{3(3M+4m)}{4}g\cos\theta\right]\sin\theta,
   \]
   \[
   F_y = \frac{1}{4}Mg + \left[\frac{6m^2 v_0^2}{(3M+4m)l} - \frac{3M+4m}{2}g + \frac{3(3M+4m)}{4}g\cos\theta\right]\cos\theta.
   \]
   （巧合验证：在切向投影 \(F_\theta = \frac{1}{4}Mg\sin\theta\) 中弹丸质量 \(m\) 彻底消失，因弹丸恰位于自由落体切向加速度点 \(l_{\text{eff}} = \frac{2}{3}l\) 处。）

3. **撤除转轴后 \(B\) 端的运动轨迹 \(x_B(t)\) 和 \(y_B(t)\)**
   杆转至 \(\theta = \pi\)（竖直向上）撤轴瞬间，角速度为：
   \[
   \omega_1 = \sqrt{\frac{36m^2 v_0^2}{(3M+4m)^2 l^2} - \frac{6g}{l}}.
   \]
   此时质心位于 \((0, L_c)\)，速度水平向右 \(v_{cx}(0) = L_c\omega_1\)、\(v_{cy}(0) = 0\)。撤轴后复合杆只受重力，质心做平抛运动，同时杆绕质心以恒定角速度 \(\omega_1\) 顺时针匀速转动（重力对质心力矩为零）。故在 \(t \ge 0\) 且着地前：
   \[
   x_C(t) = L_c \omega_1 t, \qquad y_C(t) = L_c - \frac{1}{2}gt^2,
   \]
   而 \(B\) 端相对质心的矢量为 \((l - L_c)(\sin(\omega_1 t), \cos(\omega_1 t))\)，叠加得：
   \[
   x_B(t) = L_c \omega_1 t + (l - L_c)\sin(\omega_1 t),
   \]
   \[
   y_B(t) = L_c - \frac{1}{2}g t^2 + (l - L_c)\cos(\omega_1 t),
   \]
   其中 \(L_c = \frac{3M+4m}{6(M+m)}l\)，\(l - L_c = \frac{3M+2m}{6(M+m)}l\)。

4. **撤除转轴后再转半圈时 \(O\)、\(B\) 两点的高度差**
   注意题设中 \(O\) 为固定坐标原点（\(y_O = 0\)，题干虽提到杆上端 A 初始“可视为与 \(O\) 点重合”，但第（4）问若指杆两端 A、B 则高度差平庸为 \(l\) 且用不到第（3）问；因此第（4）问中的 \(O\) 指空间固定原点 \((0,0)\)）。再转半圈所需时间 \(t_1 = \frac{\pi}{\omega_1}\)，此时 \(\cos(\omega_1 t_1) = -1\)，\(B\) 点纵坐标为：
   \[
   y_B(t_1) = L_c - \frac{1}{2}g\left(\frac{\pi}{\omega_1}\right)^2 - (l - L_c) = 2L_c - l - \frac{g\pi^2}{2\omega_1^2} = \frac{ml}{3(M+m)} - \frac{g\pi^2}{2\left[\frac{36m^2 v_0^2}{(3M+4m)^2 l^2} - \frac{6g}{l}\right]}.
   \]
   故 \(O(0,0)\) 与 \(B\) 两点的高度差为：
   \[
   h = |y_B(t_1)| = \left|\frac{\pi^2 g (3M+4m)^2 l^2}{12\left[6m^2 v_0^2 - (3M+4m)^2 gl\right]} - \frac{ml}{3(M+m)}\right|.
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解全4问的每一步与官方解答（`page-7.jpg`–`page-9.jpg`）完全一致！第（2）问中官方（⑬⑭式）与盲解仅把 \((M+m)g\) 与 \(-\frac{3M+4m}{4}g\) 合并与否的形式差异，展开验证逐项相等；第（4）问官方明确写明“即此时杆 B 端的 \(y\) 坐标的绝对值”（⑱–⑳式），证实了我们对第（4）问“\(O\) 指固定坐标原点而非杆端 A”的判断。
- **官方巧妙点**：官方在求第（2）问初角速度 \(\omega_0\) 时，直接利用第（1）问打击中心物理定义（水平轴力为零 \(\implies\) 水平动量守恒 \(mv_0 = (M+m)v_c\)，从而 \(\omega_0 = v_c / L_c\)）一步得出，比再算一遍 \(I\) 更加体现了前后小问的递进。
- **核心难点与典型易错点**：
  - 难点1：弹丸嵌入打击中心后，复合杆的等效摆长恰好仍保持为 \(\frac{2}{3}l\)（不随 \(M, m\) 变化），从而极大简化 \(\omega(\theta)\) 与 \(\beta'(\theta)\)。
  - 难点2：第（4）问理解 \(O\) 是坐标系固定原点，且因 \(v_0\) 大小未知，\(y_B(t_1)\) 可正可负，必须加绝对值 \(|y_B(t_1)|\)。
  - 易错点1：算第（2）问支反力时漏掉重力的 \(g\) 或弄反顺时针转角 \(\theta\) 对应的 \(a_{cx}, a_{cy}\) 正负号。
  - 易错点2：误以为撤轴后杆仍绕某端转动或因重力产生绕质心力矩，实际上重力过质心，绕质心角速度严格保持恒定 \(\omega_1\)。
- **教练总结与迁移建议**：刚体定轴转到某位置突然撤轴，瞬间遵循“**质心位置连续、质心速度连续、绕质心角速度连续**”三大守恒/连续律；而算支反力时先切向/法向投影常比直接直角坐标更不容易算错向心加速度方向。

---

## 4. 第35届复赛理论第4题 · Ioffe-Pritchard 四线磁阱的磁场分布、简谐束缚与逃逸鞍点 (`cpho-2018-semifinal-theory-problem-slice-q4`)

- **难度评级**：`D3`
- **物理模型**：四线二维磁四极场（含复势紧致表示）、偏置轴向磁场合成三维简谐磁势阱与二维逃逸鞍点
- **教学标签**：`Ioffe-Pritchard磁阱`、`长直导线磁场叠加`、`泰勒展开线性化`、`复势简化计算`、`鞍点逃逸动能`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

（注：原题附图 `page-9.jpg` 在导线 2、3 之间及 4 下方存在 `.doc` 转 PDF 造成的符号叠影残片，由四极磁阱对称性及角标可确认四根导线电流方向依次为：导线 1 位于 \((-a,a)\) 垂直纸面向里 \(-I\hat{k}\)，导线 2 位于 \((a,a)\) 向外 \(+I\hat{k}\)，导线 3 位于 \((a,-a)\) 向里 \(-I\hat{k}\)，导线 4 位于 \((-a,-a)\) 向外 \(+I\hat{k}\)。）

1. **四根通电导线在导线外产生的总磁场空间分布**
   单根载流 \(I_j\hat{k}\) 位于 \((x_j, y_j)\) 的长直导线在 \((x, y)\) 处产生的磁场为 \(\vec{B}_j = \frac{\mu_0 I_j}{2\pi}\frac{-(y-y_j)\hat{i} + (x-x_j)\hat{j}}{(x-x_j)^2 + (y-y_j)^2}\)。叠加四根导线得：
   \[
   \begin{aligned}
   \vec{B}(x,y) &= \frac{\mu_0 I}{2\pi}\left[\frac{y-a}{(x+a)^2+(y-a)^2} - \frac{y-a}{(x-a)^2+(y-a)^2} + \frac{y+a}{(x-a)^2+(y+a)^2} - \frac{y+a}{(x+a)^2+(y+a)^2}\right]\hat{i} \\
   &\quad + \frac{\mu_0 I}{2\pi}\left[-\frac{x+a}{(x+a)^2+(y-a)^2} + \frac{x-a}{(x-a)^2+(y-a)^2} - \frac{x-a}{(x-a)^2+(y+a)^2} + \frac{x+a}{(x+a)^2+(y+a)^2}\right]\hat{j}.
   \end{aligned}
   \]
   **复数紧致化技巧**：记复坐标 \(z = x + iy\)，每根导线贡献 \(B_x - iB_y = \frac{\mu_0 I_j}{2\pi i (z - z_j)}\)。利用四角复数 \(z_{2,4} = \pm a(1+i)\)、\(z_{1,3} = \pm a(-1+i)\) 且 \(z_2^2 = 2ia^2, z_1^2 = -2ia^2\)，合并为：
   \[
   B_x - iB_y = \frac{\mu_0 I}{2\pi i}\left(\frac{2z}{z^2 - 2ia^2} - \frac{2z}{z^2 + 2ia^2}\right) = \frac{4\mu_0 I a^2}{\pi}\frac{z}{z^4 + 4a^4}.
   \]
   由此在极坐标 \(z = r e^{i\theta}\) 下立得磁感应强度大小的空间全分布：
   \[
   |\vec{B}(r,\theta)| = \frac{4\mu_0 I a^2}{\pi}\frac{r}{\sqrt{r^8 + 8a^4 r^4\cos(4\theta) + 16a^8}}.
   \]

2. **原点附近的线性近似表达式**
   在 \(|x|, |y| \ll a\)（即 \(|z| \ll a\)）时，直接从复公式取首项 \(z^4 \ll 4a^4\)（或对四项逐一作泰勒一阶展开）：
   \[
   B_x - iB_y \approx \frac{4\mu_0 I a^2}{\pi}\frac{z}{4a^4} = \frac{\mu_0 I}{\pi a^2}(x + iy) \implies \vec{B}(x,y) \approx \frac{\mu_0 I}{\pi a^2}(x\hat{i} - y\hat{j}).
   \]

3. **原点 \(O\) 附近原子所受磁场的作用力**
   叠加匀强轴向磁场 \(\vec{B}_0 = B_0\hat{k}\)（不妨设 \(B_0 > 0\)，一般写作 \(|B_0|\)），原点附近总磁场大小为：
   \[
   |\vec{B}_{\text{tot}}| \approx \sqrt{B_0^2 + \left(\frac{\mu_0 I}{\pi a^2}\right)^2 (x^2 + y^2)} \approx B_0 + \frac{1}{2B_0}\left(\frac{\mu_0 I}{\pi a^2}\right)^2 (x^2 + y^2).
   \]
   束缚势能为 \(V(x,y) = \mu|\vec{B}_{\text{tot}}| \approx \mu B_0 + \frac{\mu}{2B_0}\left(\frac{\mu_0 I}{\pi a^2}\right)^2 (x^2 + y^2)\)，呈现二维各向同性简谐势阱特征！故原子在原点附近所受磁力为指向原点的线性回复力：
   \[
   \vec{F} = -\nabla V = -\frac{\mu}{B_0}\left(\frac{\mu_0 I}{\pi a^2}\right)^2 (x\hat{i} + y\hat{j}).
   \]

4. **\(x\)-\(y\) 平面上最易逸出的位置与临界逃逸动能**
   总束缚势能 \(V(r,\theta) = \mu\sqrt{B_0^2 + |\vec{B}(r,\theta)|^2}\) 是 \(|\vec{B}(r,\theta)|\) 的严格单调递增函数。由前述极坐标解析式，对于任意固定半径 \(r > 0\)，分母 \(\sqrt{r^8 + 8a^4 r^4\cos(4\theta) + 16a^8}\) 在 \(\cos(4\theta) = +1\)（即 \(\theta = 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}\)，也就是 **\(x\) 轴和 \(y\) 轴方向**）取最大值，从而 \(|\vec{B}|\) 和势能 \(V\) 取最小值——因此原子最容易沿 \(x\) 轴和 \(y\) 轴方向逸出。
   沿 \(x\) 轴（\(y = 0\)）势能极大值即鞍点位置满足 \(\frac{\mathrm{d}}{\mathrm{d}r}\left(\frac{r}{r^4 + 4a^4}\right) = 0\)：
   \[
   4a^4 - 3r^4 = 0 \implies r_* = \left(\frac{4}{3}\right)^{1/4}a.
   \]
   故最易逸出点为 \(x\)-\(y\) 平面上的四个鞍点：
   \[
   \left(\pm\left(\frac{4}{3}\right)^{1/4}a,\; 0\right), \qquad \left(0,\; \pm\left(\frac{4}{3}\right)^{1/4}a\right).
   \]
   在该鞍点处，\(|\vec{B}|_{\text{saddle}} = \frac{4\mu_0 I a^2}{\pi}\frac{(4/3)^{1/4}a}{\frac{16}{3}a^4} = \frac{3^{3/4}}{2\sqrt{2}}\frac{\mu_0 I}{\pi a}\)，故鞍点势能为：
   \[
   V_{\text{saddle}} = \mu\sqrt{B_0^2 + \frac{3\sqrt{3}}{8}\left(\frac{\mu_0 I}{\pi a}\right)^2}.
   \]
   处于阱底原点 \(O\) 的原子势能为 \(V_O = \mu B_0\)，故恰好能逸出磁阱的原子（在原点处）所具有的动能为势垒高度：
   \[
   E_k = V_{\text{saddle}} - V_O = \mu B_0\left[\sqrt{1 + \frac{3\sqrt{3}}{8}\left(\frac{\mu_0 I}{\pi a B_0}\right)^2} - 1\right].
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解四问的全部公式与官方解答（`page-9.jpg`–`page-11.jpg`）完全一致！官方在第（4）问末尾写为 \(\mu B_0\left[\sqrt{1 + \frac{3\sqrt{3}}{8}\left(\frac{\mu_0 I}{\pi a B_0}\right)^2} - 1\right]\)（⑳式），与盲解形式都一模一样。
- **方法亮点对比**：官方第（1）（2）问逐根导线展开泰勒级数、第（4）问由电流分布对称性定性判定最稀疏磁感线位于 \(x, y\) 轴；盲解引入的二维静磁**复势法** \(B_x - iB_y = \frac{4\mu_0 I a^2}{\pi}\frac{z}{z^4+4a^4}\) 不仅把四项分式一步化简为单个分式（极易做线性近似），而且通过 \(\cos(4\theta)\) 的解析单调性**严格证明**（而非仅仅定性断言）势垒鞍点必落在 \(x, y\) 轴上！
- **核心难点与典型易错点**：
  - 难点1：区分“四线电流产生的二维四极场”与“轴向偏置场 \(\vec{B}_0\)”的正交叠加关系——前者在原点为零但线性增长，后者提供非零谷底 \(B_0\) 使得 \(|\vec{B}_{\text{tot}}|\) 在原点光滑二次可微（物理上正是为了避免马约拉纳自旋翻转损失！）。
  - 难点2：第（4）问在二维面上寻找势垒最低的逃逸鞍点（minimax 问题）。
  - 易错点1：忘加 \(\vec{B}_0\) 的正交平方项或直接对线性近似式 \(|\vec{B}| \propto r\) 求极值（线性近似无极值，必须回到全空间分布求鞍点）。
  - 易错点2：将四根导线的矢径 \((x-x_j)\hat{i} + (y-y_j)\hat{j}\) 与切向右手螺旋方向 \((-(y-y_j)\hat{i} + (x-x_j)\hat{j})\) 符号搞混。
- **教练总结与迁移建议**：遇多根平行长直导线（或二维线电荷）问题，极力推荐记住复数对应关系 \(B_x - iB_y = \frac{\mu_0 I}{2\pi i(z - z_0)}\)，可一举完成叠加、多极展开和等值线极值证明。

---

## 5. 第35届复赛理论第5题 · 旋转参考系中的拉莫尔进动与经典正常塞曼效应 (`cpho-2018-semifinal-theory-problem-slice-q5`)

- **难度评级**：`D3`
- **物理模型**：转动非惯性系（科里奥利力与离心力抵消磁洛伦兹力）与二维耦合简谐振子拉莫尔分裂模型
- **教学标签**：`旋转参考系`、`拉莫尔进动`、`科里奥利力抵消洛伦兹力`、`经典塞曼效应`、`复坐标本征模态`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **旋转参考系中的动力学方程与求解**
   选取绕 \(+z\) 轴（磁场方向）以角速度 \(\vec{\omega} = \omega\hat{k}\) 转动的参考系 \(S'\)。对电荷为 \(-e\) 的价电子，设其在 \(S'\) 系中的位矢为 \(\vec{r}'=(x',y',z')\)、速度为 \(\vec{v}'=(\dot{x}',\dot{y}',\dot{z}')\)。则实验室速度为 \(\vec{v} = \vec{v}' + \vec{\omega}\times\vec{r}'\)。
   在转动系 \(S'\) 中，电子受到回复力 \(-m\omega_0^2\vec{r}'\)、洛伦兹力 \(-e\vec{v}\times\vec{B}\)、离心力 \(-m\vec{\omega}\times(\vec{\omega}\times\vec{r}')\) 与科里奥利力 \(-2m\vec{\omega}\times\vec{v}'\)。利用 \(eB = 2m\omega_L\) 记 \(\vec{\omega}_L = \omega_L\hat{k}\)，展开合力：
   - 速度相关项：\(-e\vec{v}'\times\vec{B} - 2m\vec{\omega}\times\vec{v}' = 2m(\vec{\omega}_L - \vec{\omega})\times\vec{v}'\)。为使电子在 \(S'\) 系中做各向无关的纯简谐振动（消去交叉速度项），必须取角速度：
     \[
     \omega = \omega_L = \frac{eB}{2m}.
     \]
   - 位置相关项（当 \(\omega = \omega_L\) 时）：
     \(-e(\vec{\omega}_L\times\vec{r}')\times\vec{B} = -2m\omega_L^2(x'\hat{i}' + y'\hat{j}')\)，离心力 \(= +m\omega_L^2(x'\hat{i}' + y'\hat{j}')\)，两者合并为 \(-m\omega_L^2(x'\hat{i}' + y'\hat{j}')\)！
   因此，\(S'\) 系直角坐标分量运动方程为：
   \[
   \ddot{x}' = -(\omega_0^2 + \omega_L^2)x', \qquad \ddot{y}' = -(\omega_0^2 + \omega_L^2)y', \qquad \ddot{z}' = -\omega_0^2 z'.
   \]
   记 \(\Omega = \sqrt{\omega_0^2 + \omega_L^2}\)，其一般解为三维简谐振动（\(x'\)-\(y'\) 平面内可为一般椭圆）：
   \[
   x'(t) = A_1\cos(\Omega t + \varphi_1), \qquad y'(t) = A_2\cos(\Omega t + \varphi_2), \qquad z'(t) = A_3\cos(\omega_0 t + \varphi_3).
   \]

2. **变换回实验室参考系直角坐标**
   取 \(t=0\) 时两系重合，由绕 \(z\) 轴逆时针转角 \(\omega_L t\) 的坐标变换：
   \[
   x = x'\cos(\omega_L t) - y'\sin(\omega_L t), \qquad y = x'\sin(\omega_L t) + y'\cos(\omega_L t), \qquad z = z'.
   \]
   代入积化和差公式，记 \(\omega_\pm = \sqrt{\omega_0^2 + \omega_L^2} \pm \omega_L\)，得：
   \[
   \begin{aligned}
   x(t) &= \left[\frac{A_1}{2}\cos(\omega_+ t + \varphi_1) - \frac{A_2}{2}\sin(\omega_+ t + \varphi_2)\right] + \left[\frac{A_1}{2}\cos(\omega_- t + \varphi_1) + \frac{A_2}{2}\sin(\omega_- t + \varphi_2)\right], \\
   y(t) &= \left[\frac{A_1}{2}\sin(\omega_+ t + \varphi_1) + \frac{A_2}{2}\cos(\omega_+ t + \varphi_2)\right] - \left[\frac{A_1}{2}\sin(\omega_- t + \varphi_1) - \frac{A_2}{2}\cos(\omega_- t + \varphi_2)\right], \\
   z(t) &= A_3\cos(\omega_0 t + \varphi_3).
   \end{aligned}
   \]

3. **证明光谱一分为三与弱场频率间隔**
   将上式同频率简谐分量用振幅矢量法合并为：
   \[
   x(t) = A_+\cos(\omega_+ t + \varphi_+) + A_-\cos(\omega_- t + \varphi_-), \qquad y(t) = A_+\sin(\omega_+ t + \varphi_+) - A_-\sin(\omega_- t + \varphi_-), \qquad z(t) = A_3\cos(\omega_0 t + \varphi_3).
   \]
   可见原子内价电子一般处于三个确定圆频率 \(\omega_+\)、\(\omega_0\)、\(\omega_-\) 的谐振叠加态，按经典偶极辐射理论发出三条圆频率分别为 \(\omega_+ = \sqrt{\omega_0^2 + \omega_L^2} + \omega_L\)、\(\omega_0\)、\(\omega_- = \sqrt{\omega_0^2 + \omega_L^2} - \omega_L\) 的谱线（原 \(\omega_0\) 谱线一分为三）。
   在弱磁场下（\(\omega_L \ll \omega_0\)），\(\sqrt{\omega_0^2 + \omega_L^2} = \omega_0\left[1 + \frac{1}{2}\left(\frac{\omega_L}{\omega_0}\right)^2 + \cdots\right] \approx \omega_0\)，略去高阶小量得：
   \[
   \omega_+ \approx \omega_0 + \omega_L, \qquad \omega_0, \qquad \omega_- \approx \omega_0 - \omega_L.
   \]
   相邻两条谱线的圆频率间隔为 \(\Delta\omega = \omega_L = \frac{eB}{2m}\)（普通频率间隔 \(\Delta\nu = \frac{eB}{4\pi m}\)；两侧边线总间隔 \(2\omega_L\)）。

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解全过程与官方解答解法（一）（`page-12.jpg`–`page-14.jpg`）高度吻合（官方在 \(y'\) 中采用 \(\sin\) 而盲解采用 \(\cos\)，展开后等价）。
- **官方重要漏洞与笔误勘察（高价值教学点！）**：
  1. 官方共给出五种解法，其中**解法（三）和解法（五）（`page-16.jpg`, `page-18.jpg`）在极坐标角动量积分中存在逻辑瑕疵**：从 \(\frac{\mathrm{d}}{\mathrm{d}t}(\rho^2\dot{\theta}') = 0 \implies \rho^2\dot{\theta}' = C\) 后，官方竟声称“**此式对于所有 \(\rho\) 都成立，故常量 \(C = 0\)**”！这是错误的：\(\rho(t)\) 是随时间变化的坐标而非可任意单独赋值的独立自由变量；一般初始条件 \(x_0, y_0, v_{x0}, v_{y0}\) 下，转动系内角动量 \(C = \rho_0^2(\dot{\theta}_0 - \omega_L)\) 一般不为零（对应二维椭圆轨道），只有过原点的直线振动才满足 \(C = 0\)。令 \(C = 0\) 会人为丢失平面内 4 个初始自由度中的 1 个（虽然特征频率仍只有 \(\omega_\pm\)）。
  2. 官方 `page-16.jpg` 第9行将“\(\pm\omega_L\)”印刷错排为“\(\mu\omega_L\)”（Symbol 字体 \(\pm\) 乱码），且事实上由科里奥利力方向唯一决定转动角速度只能取 \(+\omega_L\)。
- **核心难点与典型易错点**：
  - 难点1：在转动系写洛伦兹力时，速度必须是**实验室绝对速度** \(\vec{v} = \vec{v}' + \vec{\omega}\times\vec{r}'\)，不可错把 \(\vec{v}'\) 直接代入 \(-e\vec{v}'\times\vec{B}\)。
  - 难点2：不能在刚列出旋转系微分方程时就提前忽略 \(\omega_L^2\)，因为题干明确是在第（3）问才提出 \(\omega_L \ll \omega_0\) 弱场近似；第（1）（2）问必须保留精确的 \(\sqrt{\omega_0^2 + \omega_L^2}\)。
  - 易错点1：科里奥利力与离心力的符号、方向错乱，导致角速度取成 \(-\omega_L\) 或把等效弹性系数写成 \(\omega_0^2 - \omega_L^2\)。
- **教练总结与迁移建议**：在拉莫尔定理应用中，洛伦兹力额外牵连项 \(-e(\vec{\omega}\times\vec{r}')\times\vec{B}\) 恰好是离心力的 \(-2\) 倍，因此与离心力合起来永远是向内的 \(-m\omega_L^2\vec{r}'_\perp\)，正是这一“\(1 - 2 = -1\)”的符号结构保证了即使 \(\omega_0 = 0\)（自由回旋电子）在拉莫尔转动系中也受向心回复力做频率为 \(\omega_L\) 的简谐振动（回旋圆周运动半径与频率的投影）！

---

## 6. 第35届复赛理论第6题 · 同心球壳真空辐射—球壳热传导稳态耦合与腔内多次反射勘误 (`cpho-2018-semifinal-theory-problem-slice-q6`)

- **难度评级**：`D3`
- **物理模型**：黑体对外辐射平衡、球对称稳态热传导与漫反射灰体同心球腔（克里斯蒂安森公式）模型
- **教学标签**：`斯特藩-玻尔兹曼定律`、`球壁稳态傅里叶导热`、`灰体同心球腔多次反射`、`角系数与克里斯蒂安森公式`、`官方解答勘误`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **球壳外表面温度 \(T_2\)**
   稳态下，由内球传至球壳外表面的总热功率 \(Q = 44.0\text{ W}\) 全部以外表面（黑体，半径 \(R_2 = 1.00\text{ m}\)）向温度 \(T = 2.73\text{ K}\) 的宇宙微波背景辐射散失：
   \[
   Q = 4\pi R_2^2 \sigma \left(T_2^4 - T^4\right) \implies T_2 = \left(T^4 + \frac{Q}{4\pi R_2^2\sigma}\right)^{1/4}.
   \]
   代入数据（\(\sigma = 5.67\times 10^{-8}\text{ W}\cdot\text{m}^{-2}\cdot\text{K}^{-4}\)）：
   \[
   T_2 = \left(2.73^4 + \frac{44.0}{4\pi \times 1.00^2 \times 5.67\times 10^{-8}}\right)^{1/4} \approx \left(55.55 + 6.1753\times 10^7\right)^{1/4} \approx 88.65\text{ K} \approx 88.6\text{ K}.
   \]

2. **球壳内表面温度 \(T_1\)**
   在球壳壁（\(R_1 \le \rho \le R_2\)）内，由稳态能量守恒，任意半径 \(\rho\) 球面穿过的总热流 \(Q\) 为常数。据傅里叶热传导定律：
   \[
   Q = -4\pi\rho^2\kappa\frac{\mathrm{d}T}{\mathrm{d}\rho} \implies \int_{R_1}^{R_2}\frac{Q}{\rho^2}\,\mathrm{d}\rho = -4\pi\kappa\int_{T_1}^{T_2}\mathrm{d}T \implies Q\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = 4\pi\kappa(T_1 - T_2).
   \]
   故：
   \[
   T_1 = T_2 + \frac{Q}{4\pi\kappa}\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = 88.647 + \frac{44.0}{4\pi\times 1.00\times 10^{-2}}\left(\frac{1}{0.900} - \frac{1}{1.00}\right) \approx 88.647 + 38.905 = 127.55\text{ K} \approx 128\text{ K}.
   \]

3. **内球温度 \(T_0\)（同心漫反射灰体球腔净辐射功率）**
   记内球表面为 \(0\)（面积 \(A_0 = 4\pi r^2\)，比辐射率 \(e = 0.800\)），球壳内表面为 \(1\)（面积 \(A_1 = 4\pi R_1^2\)，比辐射率 \(E = 0.800\)）。据题意“各表面的热辐射都是各向同性的”（朗伯漫发射与漫反射），由基尔霍夫定律，两表面吸收比分别为 \(e, E\)，漫反射率分别为 \(1-e, 1-E\)。
   - **立体角角系数计算**：从表面 \(0\) 发出（或漫反射）的辐射 100% 落在表面 \(1\) 上，即 \(F_{0\to 1} = 1\)；从表面 \(1\) 上任意面元向腔内漫发射/漫反射的辐射中，落到内球 \(0\) 上的份额（在球心张半顶角 \(\sin\theta_m = r/R_1\) 锥内）为：
     \[
     F_{1\to 0} = \frac{\int_0^{\theta_m} \cos\theta\cdot 2\pi\sin\theta\,\mathrm{d}\theta}{\int_0^{\pi/2}\cos\theta\cdot 2\pi\sin\theta\,\mathrm{d}\theta} = \sin^2\theta_m = \frac{r^2}{R_1^2},
     \]
     而其余份额 \(F_{1\to 1} = 1 - \frac{r^2}{R_1^2}\) 将**重新照射到球壳内表面 \(1\) 自身**！
   - **有效辐射（辐射度 \(J_0, J_1\)）法求解**：设单位面积离开表面 \(0, 1\) 的总辐射通量（发射+反射）为 \(J_0, J_1\)，入射通量为 \(G_0, G_1\)，则：
     \[
     G_0 = J_1, \qquad G_1 = \frac{r^2}{R_1^2}J_0 + \left(1 - \frac{r^2}{R_1^2}\right)J_1,
     \]
     \[
     J_0 = e\sigma T_0^4 + (1-e)G_0, \qquad J_1 = E\sigma T_1^4 + (1-E)G_1.
     \]
     净传热功率 \(Q = A_0(J_0 - G_0) = A_0(J_0 - J_1)\)。消去 \(J_0, J_1\)：
     由 \(J_0 - J_1 = e(\sigma T_0^4 - J_1) \implies \sigma T_0^4 - J_1 = \frac{Q}{e A_0}\)；
     由 \(J_1 = E\sigma T_1^4 + (1-E)\left[J_1 + \frac{r^2}{R_1^2}(J_0 - J_1)\right] \implies E(J_1 - \sigma T_1^4) = (1-E)\frac{Q}{A_1}\)。
     两式联立消去 \(J_1\) 即得著名的**克里斯蒂安森公式（Christiansen's formula）**：
     \[
     Q = \frac{4\pi r^2\sigma(T_0^4 - T_1^4)}{\dfrac{1}{e} + \dfrac{r^2}{R_1^2}\left(\dfrac{1}{E} - 1\right)}.
     \]
     （物理解释检验：① 当 \(R_1 \to \infty\) 时，球壳趋于无限大黑体空腔，\(\frac{r^2}{R_1^2}\to 0\)，\(Q \to 4\pi r^2 e\sigma(T_0^4 - T_1^4)\) 且与 \(E\) 无关；② 当 \(R_1 \to r\) 时，趋于无限大平行灰板夹层，\(Q \to \frac{4\pi r^2\sigma(T_0^4 - T_1^4)}{\frac{1}{e} + \frac{1}{E} - 1}\)。）
     解出 \(T_0\) 并代入 \(r = 0.200\text{ m}, R_1 = 0.900\text{ m}, e = E = 0.800, Q = 44.0\text{ W}, T_1 = 127.552\text{ K}\)：
     \[
     T_0 = \left\{T_1^4 + \frac{Q}{4\pi r^2\sigma}\left[\frac{1}{e} + \frac{r^2}{R_1^2}\left(\frac{1}{E} - 1\right)\right]\right\}^{1/4} \approx \left(2.647\times 10^8 + 1.5438\times 10^9 \times 1.2623\right)^{1/4} \approx 216.91\text{ K} \approx 217\text{ K}.
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比及重要官方勘误发现**：
  - 第（1）（2）问 \(T_2 = 88.6\text{ K}\)、\(T_1 = 128\text{ K}\) 与官方解答（`page-20.jpg`）完全吻合。
  - **官方第（3）问（`page-21.jpg` ⑩–⑳式）存在严重物理漏算，导致 \(T_0\) 偏差达 \(10\text{ K}\)**！
    在官方解答 `page-21.jpg` ⑪式中，它正确计算了 \(k = (r/R_1)^2\)（从表面 II 射向表面 I 的份额），记录了被 II 反射到 I 的热量 \(Q_{\mathrm{IIr}}^{(1)} = k(1-E)Q_{\mathrm{I}0}\)，**却彻底丢弃了其余未被 II 吸收且未射向 I 的份额 \((1-k)(1-E)Q_{\mathrm{I}0}\)**（这部分能量打在 II 自身另一侧，继续被 II 多次吸收/反射！）。官方等于凭空将 \((1-k)(1-E)Q_{\mathrm{I}0}\) 湮灭，破坏了能量守恒，得出错误公式：
    \[
    Q''_{\text{官方}} = 4\pi E e \sigma r^2 \frac{T_0^4 - T_1^4}{1 - (1-e)(1-E)k} \implies T_{0,\text{官方}} = 227\text{ K}.
    \]
    **极端物理判据证伪**：在官方公式中令外球壳半径 \(R_1 \to \infty\)（即 \(k \to 0\)），竟得到 \(Q''_{\text{官方}} \to 4\pi E e \sigma r^2(T_0^4 - T_1^4)\)，分母多出一个不合物理的因子 \(E = 0.800\)——这违背了“极大非黑空腔等效为理想黑体（吸收率 \(\to 1\)）”的基本热力学事实！
    若按严格漫反射闭合腔统计全部自反射，有效吸收因子由 \(E\) 提升为 \(\frac{E}{E + k(1-E)}\)，立即还原为准确的克里斯蒂安森公式，算出真实温度为 **\(T_0 \approx 217\text{ K}\)**（\(216.9\text{ K}\)），比官方 \(227\text{ K}\) 低整整 \(10\text{ K}\)！
- **核心难点与典型易错点**：
  - 难点1：正确建立漫反射灰体封闭空腔中的多次反射与角系数平衡（用“有效辐射度 \(J\)”三串联热阻法比直接列无穷级数更不易漏掉 \(1\to 1\) 通道！）。
  - 易错点1：如官方解答那样，在追踪光子/热流无穷次反射时忘记凹面 II 会对自身照射 \((1 - r^2/R_1^2)\)，导致能量不守恒。
  - 易错点2：把同心球壳漫反射公式与平行板/镜面反射公式 \(\frac{1}{e} + \frac{1}{E} - 1\) 混为一谈（镜面反射会得出 \(225\text{ K}\)）。
- **教练总结与迁移建议**：凡遇到封闭灰体辐射传热问题，永远优先用**净辐射度法（有效辐射 \(J_i\) + 角系数 \(F_{ij}\)）**而非手算无穷反射级数——前者通过 \(F_{1\to 0} + F_{1\to 1} = 1\) 强迫检查全部光子去向，绝不会像级数展开那样漏掉凹面自反射分支！

---

## 7. 第35届复赛理论第7题 · 螺旋弹簧激光衍射图像测量与 DNA 双螺旋 X 射线结构反演 (`cpho-2018-semifinal-theory-problem-slice-q7`)

- **难度评级**：`D3`
- **物理模型**：螺旋线的交叉双狭缝（巴比涅互补）衍射-干涉图样与光栅层线、单丝包络反演几何模型
- **教学标签**：`巴比涅原理`、`单丝衍射与多缝干涉`、`螺旋线X形衍射`、`DNA双螺旋51号照片`、`图像标尺精密测量`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

将竖直螺旋线参数化为 \((x,y,z) = (R\cos\phi, \frac{p}{2\pi}\phi, R\sin\phi)\)。垂直轴线水平照射时，螺旋前、后两侧正对光束的线段在光屏平面投影交角为 \(2\alpha\)（或记两条交叉丝夹角为 \(\varphi = 2\alpha\)），单侧丝相对水平轴倾角满足 \(\tan\alpha = \frac{p}{2\pi R}\)。因每段细丝产生的衍射条纹沿垂直于丝的方向扩展，左右交叉两丝的衍射臂形成“X”形图案，且 X 形两臂之间的夹角亦等于两交叉丝夹角 \(2\alpha\)（每个臂与竖直中线夹角为 \(\alpha\)）。

1. **图 a 弹簧丝直径 \(d_1\)、弹簧圈半径 \(R\) 与螺距 \(p\) 的估算**
   对 `page-22.jpg` 图 a 右侧图像（标尺总高 \(555\text{ px}\) 对应实际尺寸 \(7.8\text{ cm}\)，比例尺 \(0.1405\text{ mm/px}\)）进行精密测量：
   - **丝径 \(d_1\)**：沿 X 臂方向观察到明显的单丝（互补于单缝）衍射暗纹包络极小值。在上方和下方清晰区域内测量相邻单丝衍射暗纹中心沿竖直方向间距 \(\Delta y_{\min} \approx 55.2\text{ px} \approx 7.76\text{ mm}\)，结合臂倾角 \(\alpha \approx 13.5^\circ\)（见下），沿臂方向的暗纹间距为 \(X_1 = \Delta y_{\min}/\cos\alpha \approx 7.98\text{ mm}\)。由单缝衍射暗纹公式 \(d_1 \frac{X_1}{L} = \lambda\)（\(\lambda = 633\text{ nm}\)，\(L = 4.2\text{ m}\)）得：
     \[
     d_1 = \frac{\lambda L}{X_1} \approx \frac{633\times 10^{-9}\times 4.2}{7.98\times 10^{-3}}\text{ m} \approx 0.33\text{ mm}.
     \]
   - **螺距 \(p\)**：相邻螺圈间在竖直方向周期为 \(p\)，构成竖直周期光栅。测得图像上共 47 个清晰水平亮斑层线间距，平均竖直层线间距 \(\Delta y = 10.85\text{ px} \approx 1.525\text{ mm}\)（对应沿 X 臂方向亮斑间距 \(X_2 = \Delta y/\cos\alpha \approx 1.57\text{ mm}\)，对应垂直于丝的相邻丝法向间距 \(d_2 = p\cos\alpha = \lambda L / X_2 \approx 1.69\text{ mm}\)）。由光栅方程 \(p \frac{\Delta y}{L} = \lambda\) 得：
     \[
     p = \frac{\lambda L}{\Delta y} \approx \frac{633\times 10^{-9}\times 4.2}{1.525\times 10^{-3}}\text{ m} \approx 1.74\text{ mm}.
     \]
   - **弹簧圈半径 \(R\)**：由线性拟合图 a 上下两半部分左右两臂间距随 \(y\) 的变化率，得 \(\tan\alpha \approx 0.240\)（即半角 \(\alpha \approx 13.5^\circ\)，全交叉角 \(2\alpha \approx 27^\circ\)）。由 \(\tan\alpha = \frac{p}{2\pi R}\) 得：
     \[
     R = \frac{p}{2\pi\tan\alpha} \approx \frac{1.74\text{ mm}}{2\pi\times 0.240} \approx 1.16\text{ mm}.
     \]

2. **图 b DNA 双螺旋半径 \(R'\) 与螺距 \(p'\) 的估算**
   对 `page-23.jpg` 图 b（标尺总高 \(511\text{ px}\) 对应 \(9.4\text{ cm}\)，比例尺 \(0.1840\text{ mm/px}\)，已知 \(\lambda' = 0.15\text{ nm}\)，\(L' = 9.0\text{ cm}\)）测量第 1、2、3、5 级亮斑位置（第 4 级因双螺旋两条糖-磷酸骨架链相移 \(\approx 3/8\) 螺距相干消光而“失踪”）：
   - **螺距 \(p'\)**：测得第 1、2、3、5 级亮斑的平均竖直层线间距为 \(\Delta y' \approx 19.1\text{ px} \approx 3.51\text{ mm}\)。由层线公式：
     \[
     p' = \frac{\lambda' L'}{\Delta y'} \approx \frac{0.15\text{ nm}\times 9.0\text{ cm}}{0.351\text{ cm}} \approx 3.84\text{ nm}.
     \]
     （附注：最上下端第 10 级子午线强碱基堆积斑点距中心约 \(212\text{ px} \approx 3.90\text{ cm}\)，此时 \(\tan(2\theta) = 3.90/9.0 \implies 2\theta \approx 23.4^\circ\) 略偏离小角线性区，对应碱基间距 \(\approx 0.38\text{ nm}\)。）
   - **螺旋半径 \(R'\)**：对第 2、3、5 级斑点横向间距与纵向距离拟合，得 X 形臂与竖直方向半夹角 \(\tan\alpha' \approx 0.90\)（\(\alpha' \approx 42^\circ\)，全交叉角 \(2\alpha' \approx 84^\circ\)）。按与（1）相同的等效交叉狭缝几何关系：
     \[
     R' = \frac{p'}{2\pi\tan\alpha'} \approx \frac{3.84\text{ nm}}{2\pi\times 0.90} \approx 0.68\text{ nm}.
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：
  - 图 a：官方测得 \(\phi = 30^\circ\)（半角 \(15^\circ\) vs 盲解 \(13.5^\circ\)）、\(X_1 = 7.9\text{ mm}\)（vs 盲解 \(7.98\text{ mm}\)）、\(X_2 = 1.7\text{ mm}\)（vs 盲解 \(1.57\text{ mm}\)），算得 \(d_1 = 0.34\text{ mm}\)、\(p = 1.6\text{ mm}\)、\(R = 0.96\text{ mm}\)，与盲解（\(0.33\text{ mm}, 1.74\text{ mm}, 1.16\text{ mm}\)）在实验图形读取误差（\(\sim 10\%\)）内完全一致！
  - 图 b：官方测得 \(\phi' = 84^\circ\)（与盲解 \(84^\circ\) 完全一致！）、沿臂条纹周期 \(X' = 4.7\text{ mm}\)（注意盲解竖直层线间距 \(3.51\text{ mm} / \cos 42^\circ = 4.72\text{ mm}\)，吻合至 \(0.5\%\)！），算得 \(p' = 3.9\text{ nm}\)、\(R' = 0.68\text{ nm}\)（vs 盲解 \(3.84\text{ nm}, 0.68\text{ nm}\)，完全吻合！）。
- **物理深度拓展（为何模型测得 \(R' \approx 0.68\text{ nm}\) 而非真实 B-DNA 的 \(1.0\text{ nm}\)？）**：在完整的连续螺旋 X 射线衍射理论（Cochran–Crick–Vand 贝塞尔函数理论）中，第 \(n\) 层线的亮斑极大值位于贝塞尔函数 \(J_n(2\pi R'\xi)\) 的第一主极大处，而 \(J_n(u)\) 的首极大位置在 \(u_1 \approx 1.84, u_2 \approx 3.05, u_3 \approx 4.20 > n\)（比近似直线关系 \(u=n\) 向外偏大约 \(40\%\)）。由于本题及官方采用简化的“两条倾斜狭缝”模型（等价于取 \(u \approx n\)），使得视在交叉角 \(\phi'/2 \approx 42^\circ\) 偏大，由此反推出的等效半径 \(0.68\text{ nm}\) 偏小约 \(30\%\)（乘以 \(1.4\) 即得真实的 B-DNA 磷酸骨架半径 \(\sim 1.0\text{ nm}\)）。
- **核心难点与典型易错点**：
  - 难点1：识别图 a 右图中“两套空间周期”的物理成因——大周期 \(X_1\) 对应单根钢丝直径 \(d_1\) 的单缝包络极小，小周期 \(X_2\) 对应相邻平行钢丝间距 \(d_2 = p\cos(\phi/2)\) 的多缝干涉极大！
  - 难点2：分清投影中倾斜钢丝的“平行段法向间距 \(d_2\)”与“竖直轴向螺距 \(p\)”之间差一个 \(\cos(\phi/2)\) 几何因子，并注意“按图测量时必须先换算回真实尺寸比例尺（图片缩放倍率）”。
  - 易错点1：把弹簧圆周展开三角关系 \(\tan\theta = \frac{2\pi R}{p}\) 误写成 \(\frac{2R}{p}\)（漏掉 \(\pi\)！）。
  - 易错点2：测量图 b 时忘了乘以 \(\cos(\phi'/2)\) 或用错 \(X'\)（沿斜臂测量 vs 沿竖直中轴测量：若直接沿竖直方向量层线间距 \(\Delta y'\)，直接套 \(p' = \lambda' L' / \Delta y'\)；若沿斜臂方向量斑点间距 \(X'\)，则需 \(p' = \frac{\lambda' L'}{X'\cos(\phi'/2)}\)，两者完全等价，切忌混用！）。
- **教练总结与迁移建议**：将复杂三维螺旋结构转化为“前后两段交叉平行光栅”的等效几何光学模型，是诺奖级结构生物学（富兰克林 51 号照片）与大学物理实验（圆珠笔弹簧激光衍射）的经典桥梁。测图类题目务必在图上标注清晰的量取线段并写明比例换算因子。

---

## 8. 第35届复赛理论第8题 · \(^{57}\mathrm{Fe}\) 核反冲与无反冲穆斯堡尔共振吸收及微频移测量 (`cpho-2018-semifinal-theory-problem-slice-q8`)

- **难度评级**：`D2`
- **物理模型**：原子核发射/吸收 \(\gamma\) 光子的反冲能量损失、自然线宽区间重叠判据与多普勒速度补偿测量法
- **教学标签**：`穆斯堡尔效应`、`核反冲能`、`自然线宽与共振重叠`、`相对论多普勒频移`、`微小频移测量`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **发射光子的反冲能与频率差**
   不计能级宽度时，无反冲发射光子频率为 \(\nu_0 = \frac{E_0}{h}\)。考虑静止 \(^{57}\mathrm{Fe}^*\) 核质量 \(m_{\mathrm{Fe}}\) 发射频率为 \(\nu_e\) 的光子后获得反冲速度 \(v\)，由能量与动量守恒：
   \[
   E_0 = h\nu_e + \frac{1}{2}m_{\mathrm{Fe}}v^2, \qquad 0 = \frac{h\nu_e}{c} - m_{\mathrm{Fe}}v.
   \]
   得反冲能 \(E_R = \frac{h^2\nu_e^2}{2m_{\mathrm{Fe}}c^2}\)。注意到 \(\frac{E_0}{m_{\mathrm{Fe}}c^2} \approx \frac{2.31\times 10^{-15}}{9.5\times 10^{-26}\times 9\times 10^{16}} \approx 2.7\times 10^{-7} \ll 1\)，故可用 \(h\nu_e \approx E_0\) 近似：
   \[
   E_R \approx \frac{E_0^2}{2m_{\mathrm{Fe}}c^2} = \frac{(2.31\times 10^{-15})^2}{2\times 9.5\times 10^{-26}\times (3.0\times 10^8)^2} \approx 3.12\times 10^{-22}\text{ J} \approx 3.1\times 10^{-22}\text{ J}.
   \]
   考虑与不考虑核反冲的发射光子频率之差为：
   \[
   \nu_e - \nu_0 = -\frac{E_R}{h} \approx -\frac{3.12\times 10^{-22}}{6.6\times 10^{-34}} \approx -4.73\times 10^{11}\text{ Hz} \approx -4.7\times 10^{11}\text{ Hz} \quad (\text{频差大小 } 4.7\times 10^{11}\text{ Hz}).
   \]

2. **吸收光子的反冲能与频率差**
   静止基态 \(^{57}\mathrm{Fe}\) 核吸收频率为 \(\nu_a\) 的光子跃迁到第一激发态并获得反冲速度 \(v'\)，由能量与动量守恒：
   \[
   h\nu_a = E_0 + \frac{1}{2}m_{\mathrm{Fe}}v'^2, \qquad \frac{h\nu_a}{c} = m_{\mathrm{Fe}}v'.
   \]
   同理由 \(h\nu_a \approx E_0 \ll m_{\mathrm{Fe}}c^2\)，吸收过程反冲能为：
   \[
   E'_R \approx \frac{E_0^2}{2m_{\mathrm{Fe}}c^2} \approx 3.1\times 10^{-22}\text{ J},
   \]
   频率之差为：
   \[
   \nu_a - \nu_0 = +\frac{E'_R}{h} \approx +4.7\times 10^{11}\text{ Hz}.
   \]

3. **静止自由核之间能否发生共振吸收**
   **不能发生共振吸收**。理由如下：计及第一激发态在 \([E_0-\Gamma, E_0+\Gamma]\) 内取值（宽度 \(2\Gamma\)），静止发射核发出的光子频率分布范围为 \(\left[\nu_e - \frac{\Gamma}{h},\; \nu_e + \frac{\Gamma}{h}\right]\)，静止吸收核能共振吸收的光子频率分布范围为 \(\left[\nu_a - \frac{\Gamma}{h},\; \nu_a + \frac{\Gamma}{h}\right]\)。发生共振吸收要求两区间存在交集，即：
   \[
   \nu_a - \frac{\Gamma}{h} \le \nu_e + \frac{\Gamma}{h} \iff \nu_a - \nu_e = \frac{2E_R}{h} \le \frac{2\Gamma}{h} \iff \Gamma \ge E_R.
   \]
   然而由题给数据：
   \[
   \Gamma \simeq 3.2\times 10^{-13} E_0 = 3.2\times 10^{-13}\times 2.31\times 10^{-15}\text{ J} \approx 7.4\times 10^{-28}\text{ J},
   \]
   对比反冲能 \(E_R \approx 3.12\times 10^{-22}\text{ J}\)，有：
   \[
   \frac{E_R}{\Gamma} \approx 4.2\times 10^5 \gg 1.
   \]
   反冲能比能级半宽大 5 个数量级以上，发射谱与吸收谱之间存在 \(2E_R \approx 8.4\times 10^5\Gamma\) 的巨大鸿沟，完全没有重叠，故无法发生共振吸收。

4. **晶体内无反冲共振吸收的速度 \(V\) 范围与 \(10^{-10}\) 相对频移测量方案**
   - **共振吸收的运动速度范围**：置于晶体中无反冲时，发射与吸收光子频率范围均为 \(\left[\nu_0 - \frac{\Gamma}{h},\; \nu_0 + \frac{\Gamma}{h}\right]\)。设吸收晶体沿光子入射直线方向以速度 \(V\) 相对发射晶体运动（\(V \ll c\)，沿相向或相离方向；若规定朝向/远离带符号 \(V\)，则多普勒频移为 \(\Delta\nu = \pm\frac{V}{c}\nu_0\)）。要使吸收晶体参考系中的接收频率区间 \(\left[\nu_0(1\pm\frac{V}{c}) - \frac{\Gamma}{h},\; \nu_0(1\pm\frac{V}{c}) + \frac{\Gamma}{h}\right]\) 与 \(\left[\nu_0 - \frac{\Gamma}{h},\; \nu_0 + \frac{\Gamma}{h}\right]\) 仍有交集，中心频移绝对值不得超过 \(2\Gamma/h\)：
     \[
     \frac{|V|}{c}E_0 \le 2\Gamma \implies |V| \le \frac{2\Gamma}{E_0}c = 2\times 3.2\times 10^{-13}\times 3.0\times 10^8\text{ m/s} = 1.92\times 10^{-4}\text{ m/s} \approx 0.19\text{ mm/s}.
     \]
     即速度大小范围为 \(0 \le V \le 0.19\text{ mm/s}\)（带符号区间 \(-0.19\text{ mm/s} \le V \le 0.19\text{ mm/s}\)；注：若运动方向与光子传播方向成角 \(\theta\)，则为 \(|V\cos\theta| \le 0.19\text{ mm/s}\)）。
   - **测量相对频率变化 \(10^{-10}\) 的原理与计算**：由于 \(\frac{\Delta\nu}{\nu_0} = 10^{-10} \gg \frac{2\Gamma}{E_0} = 6.4\times 10^{-13}\)，静止吸收晶体不再发生共振吸收（透射计数高）。利用**多普勒速度调制法**，让吸收晶体沿光线方向以可精确控制的速度 \(V'\) 运动（若光子频率升高则远离运动，若降低则迎向运动），扫描 \(V'\) 并监测透射 \(\gamma\) 光子计数，当计数率跌落至极小值（恢复共振吸收）时，补偿频移恰好抵消待测频移：
     \[
     \frac{V'}{c} = \left|\frac{\nu - \nu_0}{\nu_0}\right| = 10^{-10} \implies V' = 10^{-10}\times 3.0\times 10^8\text{ m/s} = 3.0\times 10^{-2}\text{ m/s} = 3.0\text{ cm/s}.
     \]
     此速度在实验室极易高精度控制，且共振峰半宽仅 \(\sim 0.19\text{ mm/s}\)，相对测量分辨率优于 \(1\%\)（如著名的庞德-雷布卡引力红移实验）。

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解全4问与官方解答（`page-25.jpg`–`page-27.jpg`）完全一致！特别是第（4）问关于两端点区间重叠给出 \(\pm\frac{2\Gamma}{E_0}c = \pm 0.19\text{ mm/s}\)（⑲式）而非 \(\pm\frac{\Gamma}{E_0}c\)，与官方的区间端值分析逐字相同。
- **核心难点与典型易错点**：
  - 难点1：理解第（4）问两个各占宽度 \(2\Gamma\)（半宽 \(\Gamma\)）的连续分布窗口相交条件是中心距 \(\le 2\Gamma\)，而非 \(\le \Gamma\)。
  - 难点2：第（4）问后半问的实验思想——以宏观机械运动（cm/s 量级的多普勒扫描）作为超高精度“频率游标卡尺”去标定 \(10^{-10}\) 量级（远小于任何光学光谱仪分辨极限）的 \(\gamma\) 光子频移。
  - 易错点1：把发射谱和吸收谱的重叠间距误算成 \(E_R\) 而漏掉发射向下移、吸收向上移共差 \(2E_R\)；或在计算 \(\nu_e - \nu_0\) 时忽略正负号说明。
  - 易错点2：问速度大小范围 \(V\) 时忽略题干问的是“速度 \(V\) 的**大小**”（应为 \(0 \le V \le 0.19\text{ mm/s}\)，官方最后写为带符号 \(-0.19\text{ mm/s} \le V \le 0.19\text{ mm/s}\) 并注明正负对应接近或远离）。
- **教练总结与迁移建议**：穆斯堡尔效应是极佳的现代物理命题模板——用“自由核反冲 \(E_R \gg \Gamma\)（不共振）”与“晶格整体反冲 \(E_R \to 0\)（超窄线宽 \(\Gamma/E_0 \sim 10^{-13}\)）”作强对比，随后自然引向 Pound-Rebka 引力红移测定。记住：**两个半宽为 \(\Gamma\) 的盒子重叠，最大偏移允许 \(2\Gamma\)**。

---

# 决赛理论试题（Final Theory）

## 9. 第35届决赛理论第1题 · 光滑桌面上可动半球表面小球的纯滚、起滑判据与脱离速度 (`cpho-2018-final-theory-problem-slice-q1`)

- **难度评级**：`D4`
- **物理模型**：可水平反冲曲面上的纯滚动约束、非惯性系质心与转动动力学、摩擦起滑判据及瞬时无反冲脱离模型
- **教学标签**：`可动曲面纯滚动`、`水平动量守恒`、`非惯性系惯性力`、`滚动起滑临界条件`、`脱离瞬间无加速原理`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

（注：原题附图 `page-1.jpg` 在半球左侧多出一条与题干无关的杂散黑线，属于电子排版残迹；题干明确半球半径为 \(R\)、质量为 \(M\)，小球半径为 \(r\)、质量为 \(m\)。）

1. **纯滚动过程中半球运动的速度大小 \(V_M(\theta_1)\) 和加速度大小 \(a_M(\theta_1)\)**
   记两球心连线长度 \(L = R + r\)。设小球转至角位置 \(\theta\) 时，半球向左运动的速度大小为 \(V_M\)，小球质心相对半球沿圆弧顺时针转过的角速度为 \(\dot{\theta}\)，小球绕自身质心的转动角速度为 \(\omega\)。
   - **纯滚动运动学约束**：因半球只做平动不转动，在半球参考系中，接触点无相对滑动要求小球质心相对半球弧线切向速率等于轮缘切向速率：
     \[
     r \omega = (R + r)\dot{\theta}.
     \]
   - **系统水平方向动量守恒**（桌面光滑，无水平外力）：
     \[
     -M V_M + m\left[(R+r)\dot{\theta}\cos\theta - V_M\right] = 0 \implies V_M = \frac{m(R+r)\cos\theta}{M+m}\dot{\theta}.
     \]
   - **机械能守恒**（纯滚动静摩擦力做功为零）：
     \[
     mg(R+r)(1 - \cos\theta) = \frac{1}{2}M V_M^2 + \frac{1}{2}m\left[(R+r)\dot{\theta}\cos\theta - V_M\right]^2 + \frac{1}{2}m(R+r)^2\dot{\theta}^2\sin^2\theta + \frac{1}{2}\left(\frac{2}{5}mr^2\right)\omega^2.
     \]
     将 \(V_M = \frac{m(R+r)\cos\theta}{M+m}\dot{\theta}\) 与 \(r\omega = (R+r)\dot{\theta}\) 代入，整理动能项系数：
     \[
     \frac{1}{2}m(R+r)^2\dot{\theta}^2\left[\frac{M + m\sin^2\theta}{M+m} + \frac{2}{5}\right] = \frac{m(R+r)^2\dot{\theta}^2}{10(M+m)}\left[7(M+m) - 5m\cos^2\theta\right].
     \]
     由此解得角速度平方及 \(\theta_1\) 处半球速度大小 \(V_M(\theta_1)\)：
     \[
     \dot{\theta}^2 = \frac{10(M+m)g(1 - \cos\theta)}{(R+r)\left[7(M+m) - 5m\cos^2\theta\right]},
     \]
     \[
     V_M(\theta_1) = m\cos\theta_1\sqrt{\frac{10(R+r)g(1 - \cos\theta_1)}{(M+m)\left[7(M+m) - 5m\cos^2\theta_1\right]}}.
     \]
   - **半球加速度大小 \(a_M(\theta_1)\)**：对 \(V_M^2 = \frac{10m^2(R+r)g(1-\cos\theta)\cos^2\theta}{(M+m)[7(M+m)-5m\cos^2\theta]}\) 两边关于时间 \(t\) 求导（\(2V_M\dot{V}_M = \frac{\mathrm{d}V_M^2}{\mathrm{d}\theta}\dot{\theta}\)），消去 \(V_M\) 并利用 \(\frac{m(R+r)\dot{\theta}}{M+m} = \frac{V_M}{\cos\theta}\) 化简（其中 \(-10mc^2\) 项恰好抵消）：
     \[
     \dot{V}_M(\theta_1) = \frac{5mg\sin\theta_1\left[7(M+m)(3\cos\theta_1 - 2) - 5m\cos^3\theta_1\right]}{\left[7(M+m) - 5m\cos^2\theta_1\right]^2}.
     \]
     注意当 \(7(M+m)(3\cos\theta_1 - 2) - 5m\cos^3\theta_1\) 由正转负时（约 \(\theta_1 \gtrsim 48^\circ\)），半球由向左加速转变为向左减速（即 \(\dot{V}_M < 0\)），因此加速度**大小**应取绝对值：
     \[
     a_M(\theta_1) = \left|\dot{V}_M(\theta_1)\right| = \frac{5mg\sin\theta_1\left|7(M+m)(3\cos\theta_1 - 2) - 5m\cos^3\theta_1\right|}{\left[7(M+m) - 5m\cos^2\theta_1\right]^2}.
     \]

2. **开始滑动角位置 \(\theta_2\) 满足的方程**
   设角位置 \(\theta \le \theta_2\) 时球面间正压力为 \(N\)、静摩擦力为 \(f\)（方向沿切线向上），记半球的**带符号向左加速度**为 \(\tilde{a}_M = \dot{V}_M\)。
   对半球水平方向列牛顿第二定律：
   \[
   N\sin\theta - f\cos\theta = M\tilde{a}_M.
   \]
   在半球非惯性参考系（受向右惯性力 \(m\tilde{a}_M\hat{i}\)）中，对小球质心沿径向与切向列方程，并结合绕质心转动方程 \(fr = \frac{2}{5}mr^2\frac{\mathrm{d}\omega}{\mathrm{d}t} = \frac{2}{5}m(R+r)\ddot{\theta}\)：
   \[
   mg\cos\theta - N - m\tilde{a}_M\sin\theta = \frac{m(R+r)^2\dot{\theta}^2}{R+r} = \frac{(M+m)^2 V_M^2}{m(R+r)\cos^2\theta},
   \]
   \[
   mg\sin\theta + m\tilde{a}_M\cos\theta - f = m(R+r)\ddot{\theta} = \frac{5}{2}f \implies f = \frac{2m}{7}\left(g\sin\theta + \tilde{a}_M\cos\theta\right).
   \]
   起滑临界条件为 \(f(\theta_2) = \mu N(\theta_2)\)，故 \(\theta_2\) 满足方程：
   \[
   \frac{2}{7}\left[g\sin\theta_2 + \tilde{a}_M(\theta_2)\cos\theta_2\right] = \mu\left[g\cos\theta_2 - \tilde{a}_M(\theta_2)\sin\theta_2 - \frac{(M+m)^2 V_M^2(\theta_2)}{m^2(R+r)\cos^2\theta_2}\right],
   \]
   整理即：
   \[
   \frac{2}{7}g\sin\theta_2 - \mu g\cos\theta_2 + \tilde{a}_M(\theta_2)\left(\frac{2}{7}\cos\theta_2 + \mu\sin\theta_2\right) + \frac{\mu(M+m)^2 V_M^2(\theta_2)}{(R+r)m^2\cos^2\theta_2} = 0,
   \]
   或等价地由 \(M\tilde{a}_M = N(\sin\theta_2 - \mu\cos\theta_2)\) 直接消去 \(f\) 表出（当 \(7(M+m)(3\cos\theta_2 - 2) - 5m\cos^3\theta_2 \ge 0\) 时 \(\tilde{a}_M(\theta_2) = +a_M(\theta_2)\)，否则 \(\tilde{a}_M(\theta_2) = -a_M(\theta_2)\)）。

3. **脱离半球时小球质心相对半球的速度大小 \(v_m(\theta_3)\)**
   小球在 \(\theta_2 < \theta < \theta_3\) 区间存在滑动摩擦耗散，虽然中间段能量不再守恒，但在**刚好脱离半球瞬间 \(\theta = \theta_3\)**，正压力 \(N(\theta_3) = 0\)，从而滑动摩擦力 \(f(\theta_3) = \mu N(\theta_3) = 0\) 亦同时归零！
   由半球水平动力学方程 \(M\tilde{a}_M(\theta_3) = N(\theta_3)\sin\theta_3 - f(\theta_3)\cos\theta_3 = 0\)，可知**脱离瞬间半球的加速度严格为零**（\(\tilde{a}_M(\theta_3) = 0\)）！
   因此在半球参考系中，脱离瞬间小球质心不受惯性力作用，且与半球刚性约束尚未出现法向分离速度，故其相对圆周运动的向心力完全由重力的径向分量提供：
   \[
   m\frac{v_m^2(\theta_3)}{R+r} = mg\cos\theta_3 \implies v_m(\theta_3) = \sqrt{(R+r)g\cos\theta_3}.
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解与官方解答（`page-1.jpg`–`page-3.jpg`）高度一致，第（1）问 \(V_M(\theta_1)\) 与 \(a_M(\theta_1)\)、第（2）问 \(\theta_2\) 所满足的方程⑬式以及第（3）问脱离速度 \(v_m(\theta_3) = \sqrt{(R+r)g\cos\theta_3}\) 完全吻合。
- **官方细微瑕疵辨析**：
  1. 题目第（1）问要求“半球运动的速度大小 \(V_M(\theta_1)\) 和加速度**大小** \(a_M(\theta_1)\)”，官方解答 `page-2.jpg` ⑤式写出的 \(a_M(\theta_1) = -\frac{5mg\sin\theta_1[14(M+m)-21(M+m)\cos\theta_1+5m\cos^3\theta_1]}{[7(M+m)-5m\cos^2\theta_1]^2}\) 未加绝对值号，实际上是带符号的向左加速度 \(\dot{V}_M\)（当 \(\theta_1\) 超过减速临界角 \(\sim 48^\circ\) 后该表达式为负！）。
  2. 官方第（2）问⑬式直接将这个带符号的 \(a_M(\theta_2)\) 代入起滑方程，如果考生真的按第（1）问字面求出了非负绝对值 \(|a_M|\) 再盲目代回⑬式，一旦 \(\theta_2\) 落在半球减速区间就会导致正负号错误——教学中务必向学生澄清“带符号分量 \(\dot{V}_M\)”与“大小 \(|\dot{V}_M|\)”的区别！
- **核心难点与典型易错点**：
  - 难点1：正确建立可动曲面上的纯滚动运动学约束 \(r\omega = (R+r)\dot{\theta}\)——由于半球本身**不转动**，无论半球如何平动加速，在半球平动系内看纯滚动几何与静止半球完全一样，不会像“大球自身也在转动”那样混入额外的牵连角速度。
  - 难点2：第（3）问看透“\(N=0 \implies f=0 \implies a_M=0\)”的瞬时解耦机制——不必求解 \(\theta_2 \to \theta_3\) 复杂的变质量/耗散微分方程也能一步写出 \(v_m(\theta_3)\)。
  - 易错点1：把小球对实验室的速度 \(\vec{v}_{\text{lab}}\) 误代入向心加速度公式 \(v^2/(R+r)\)，或者在半球系中列法向方程时忘记扣除水平惯性力在法向的投影 \(-m\tilde{a}_M\sin\theta\)。
  - 易错点2：将转动方程 \(fr = I\dot{\omega}\) 中的转动角速度 \(\omega\) 误以为是绝对角速度加减某个假想转动，或者错写为 \(\omega = R\dot{\theta}/r\) 而漏掉小球的半径 \(r\)（即错把 \(R+r\) 写成 \(R\)）。
- **教练总结与迁移建议**：凡遇“可平移斜面/曲面上小物体脱离”的题目，先检查**脱离瞬间的法向解耦定理**（\(N=0 \implies\) 支承体水平加速度归零），几乎总能直接把复杂的多体脱离条件退化为单摆式向心力等式 \(v_{\text{rel}}^2/L = g\cos\theta\)！

---

## 10. 第35届决赛理论第2题 · 平行板电容器内带电导板的非弹性往返弹跳及周期计算 (`cpho-2018-final-theory-problem-slice-q2`)

- **难度评级**：`D3`
- **物理模型**：恒压电源串联可变双电容系统的静电起振、完全非弹性碰撞周期重置与线性增力一维运动积分
- **教学标签**：`电容器静电压力`、`导体表面平均场强`、`静电平衡电荷重分布`、`线性增力运动时间积分`、`官方勘误`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **电源电动势 \(U\) 的最小条件**
   设两固定极板 1（上）、2（下）间距为 \(d\)、面积为 \(S\)，电源接通后极板 1 与 2 间电势差恒为 \(U\)（不妨设板 1 电势 \(U\)、板 2 电势 \(0\)）。初始时导电薄平板 3 与极板 2 接触并等势，故 3 与 2 间场强为零，3 与 1 间场强 \(E_1 = U/d\)，板 3 上表面带负电荷 \(Q_3 = -\frac{\varepsilon_0 S U}{d}\)。
   当板 3 向上离开板 2 距离 \(x\)（\(0 < x < d\)）时，板 3 对外绝缘，总电荷量保持为 \(-Q = -\frac{\varepsilon_0 S U}{d}\)。设板 3 上方气隙（厚 \(d-x\)）场强为 \(E_1\)（向下），下方气隙（厚 \(x\)）场强为 \(E_2\)（向下），则由高斯定理与总电压条件：
   \[
   \varepsilon_0(E_2 - E_1) = -\frac{\varepsilon_0 U}{d} \implies E_1 - E_2 = \frac{U}{d}, \qquad E_1(d-x) + E_2 x = U.
   \]
   联立解得：
   \[
   E_1 = \frac{U}{d}\left(1 + \frac{x}{d}\right), \qquad E_2 = \frac{U}{d}\frac{x}{d}.
   \]
   极板 3 上下两面受静电力之和（向上为正，注意每面静电压强为 \(\frac{1}{2}\varepsilon_0 E^2\)，即电荷面密度乘以其自身两侧平均场强）：
   \[
   F_e(x) = \frac{1}{2}\varepsilon_0 S\left(E_1^2 - E_2^2\right) = \frac{1}{2}\varepsilon_0 S(E_1 - E_2)(E_1 + E_2) = \frac{\varepsilon_0 S U^2}{2d^2}\left(1 + \frac{2x}{d}\right).
   \]
   令 \(B = \frac{\varepsilon_0 S U^2}{m d^3}\)，板 3 上升过程加速度为：
   \[
   a(x) = \left(\frac{1}{2}Bd - g\right) + B x.
   \]
   可见一旦向上离开板 2，\(F_e(x)\) 随 \(x\) 线性增大！故能够脱离板 2 并到达板 1 的条件为刚起跳时合力向上（严格来说，若 \(\frac{1}{2}Bd = g\) 处于不稳定平衡，起动时间发散；工程/竞赛临界最小电动势取平衡阈值）：
   \[
   \frac{\varepsilon_0 S U^2}{2d^2} \ge mg \implies U_{\min} = d\sqrt{\frac{2mg}{\varepsilon_0 S}} \qquad (\text{严格往返需 } U > U_{\min}).
   \]
   （当板 3 撞击板 1 后，电荷中和并重新充为 \(+Q = +\frac{\varepsilon_0 S U}{d}\)，由对称性置换 \(x \leftrightarrow d-x\)，向下的静电力为 \(\frac{\varepsilon_0 S U^2}{2d^2}(1 + \frac{2(d-x)}{d})\)，再叠加上向下的重力 \(mg\)，必然加速下落撞回板 2，无额外阈值要求。）

2. **平板 3 往返运动的周期 \(T\)**
   由于每次碰撞均为完全非弹性碰撞且瞬时完成电荷重置，每一程初速度均严格为零，周期 \(T = t_{\text{up}} + t_{\text{down}}\)。
   - **上升时间 \(t_{\text{up}}\)（\(x: 0 \to d\)）**：
     记 \(a_0 = \frac{1}{2}Bd - g > 0\)。由 \(v\frac{\mathrm{d}v}{\mathrm{d}x} = a_0 + Bx\) 积分得：
     \[
     v = \sqrt{B x^2 + 2a_0 x} \implies t_{\text{up}} = \int_0^d \frac{\mathrm{d}x}{\sqrt{Bx^2 + 2a_0 x}}.
     \]
     套用题给积分公式（\(a = B, b = 2a_0 = Bd - 2g\)）：
     \[
     t_{\text{up}} = \frac{1}{\sqrt{B}}\ln\left[\frac{2Bd + b + 2\sqrt{B(Bd^2 + bd)}}{b}\right] = \frac{1}{\sqrt{B}}\ln\left[\frac{3Bd - 2g + \sqrt{8Bd(Bd - g)}}{Bd - 2g}\right].
     \]
     代入 \(B = \frac{\varepsilon_0 S U^2}{m d^3}\)（即 \(Bd = \frac{\varepsilon_0 S U^2}{m d^2}\)）：
     \[
     t_{\text{up}} = \frac{d}{U}\sqrt{\frac{md}{\varepsilon_0 S}}\ln\left[\frac{3\varepsilon_0 S U^2 - 2mgd^2 + 2U\sqrt{2\varepsilon_0 S(\varepsilon_0 S U^2 - mgd^2)}}{\varepsilon_0 S U^2 - 2mgd^2}\right].
     \]
   - **下降时间 \(t_{\text{down}}\)（\(y = d - x: 0 \to d\)）**：
     下降时方程与上升完全对称，仅重力方向相反（\(-g \to +g\)），故只需将 \(t_{\text{up}}\) 中的 \(-g\) 换为 \(+g\)：
     \[
     t_{\text{down}} = \frac{1}{\sqrt{B}}\ln\left[\frac{3Bd + 2g + \sqrt{8Bd(Bd + g)}}{Bd + 2g}\right] = \frac{d}{U}\sqrt{\frac{md}{\varepsilon_0 S}}\ln\left[\frac{3\varepsilon_0 S U^2 + 2mgd^2 + 2U\sqrt{2\varepsilon_0 S(\varepsilon_0 S U^2 + mgd^2)}}{\varepsilon_0 S U^2 + 2mgd^2}\right].
     \]
   总周期为：
   \[
   T = t_{\text{up}} + t_{\text{down}} = \frac{d}{U}\sqrt{\frac{md}{\varepsilon_0 S}}\left\{\ln\left[\frac{3\varepsilon_0 S U^2 - 2mgd^2 + 2U\sqrt{2\varepsilon_0 S(\varepsilon_0 S U^2 - mgd^2)}}{\varepsilon_0 S U^2 - 2mgd^2}\right] + \ln\left[\frac{3\varepsilon_0 S U^2 + 2mgd^2 + 2U\sqrt{2\varepsilon_0 S(\varepsilon_0 S U^2 + mgd^2)}}{\varepsilon_0 S U^2 + 2mgd^2}\right]\right\}.
   \]
   （极限校核：令 \(g \to 0\)，括号内两个对数均简化为 \(\ln(3 + 2\sqrt{2}) = 2\ln(1+\sqrt{2})\)，直接求解 \(\ddot{u} = B u\)，\(u(0)=d/2\) 运动到 \(u=3d/2\) 有 \(\cosh(\sqrt{B}t) = 3 \implies t = \frac{1}{\sqrt{B}}\ln(3+2\sqrt{2})\)，精确吻合！）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比及重要官方勘误发现**：
  - 第（1）问与第（2）问前段推导（包括以 \(B = \frac{\varepsilon_0 S U^2}{md^3}\) 表出的 \(t_1, t_2\)）盲解与官方解答（`page-3.jpg`–`page-7.jpg`）完全一致！
  - **官方解答第（2）问出现一处代数抄写笔误（`page-7.jpg` ⑲式及 ⑳式）**：
    官方在 `page-7.jpg` 第1行正确写出了：
    \[
    t_2 = \sqrt{\frac{1}{B}}\ln\left[\frac{(3Bd + 2g) + \sqrt{8Bd(Bd + g)}}{Bd + 2g}\right].
    \]
    但在将 \(B = \frac{\varepsilon_0 S U^2}{m d^3}\) 代入 \(\sqrt{8Bd(Bd+g)}\) 时，正确化简应为：
    \[
    \sqrt{8 \frac{\varepsilon_0 S U^2}{m d^2}\left(\frac{\varepsilon_0 S U^2}{m d^2} + g\right)} = \frac{2U}{m d^2}\sqrt{2\varepsilon_0 S\left(\varepsilon_0 S U^2 + mgd^2\right)}.
    \]
    而官方 ⑲、⑳ 式却误将因子 \(2\) 错放进内层括号里，写成了 **`2U\sqrt{\varepsilon_0 S(2\varepsilon_0 S U^2 + mgd^2)}`**，导致 \(mgd^2\) 项平白丢失了一个系数 \(2\)！（相比之下，`page-5.jpg` 中 \(t_1\) 的 ⑩ 式把 \(2\) 放在外面是完全正确的，恰成反差）。
  - 此外，`page-5.jpg` 第7行官方把“最终将撞到极板 **1** 上”误笔写成“极板 2 上”。
- **核心难点与典型易错点**：
  - 难点1：脱离极板后板 3 上下两气隙的电场求解——必须同时联立“板 3 孤立电荷守恒（\(E_1 - E_2 = U/d\)）”与“电源总电压恒定（\(E_1(d-x) + E_2 x = U\)）”。
  - 难点2：正确计算板 3 受到的静电力 \(F_e = \frac{1}{2}\varepsilon_0 S(E_1^2 - E_2^2)\)（静电压强差），并在 \(g \to 0\) 极限下用双曲余弦函数交叉检验积分结果。
  - 易错点1：算板 3 在板 2 上刚起跳时的静电力漏掉 \(1/2\) 因子，误以为 \(F_e = Q E_1 = \frac{\varepsilon_0 S U^2}{d^2}\)（实际刚起跳时极板一侧无场强，平均场强为 \(E_1/2\)）。
  - 易错点2：板 3 离开板 2 后误以为其所受静电力保持常数 \(\frac{\varepsilon_0 S U^2}{2d^2}\) 不变，忽视了移动过程中极板 1 和 2 上的感应电荷随电容改变而不断流过电源，使 \(F_e(x)\) 随 \(x\) 线性增大！
- **教练总结与迁移建议**：遇带电导体板在恒压平板电容器内运动的题目，牢记**虚功原理（协能法）**或**双侧静电压强差 \(\frac{1}{2}\varepsilon_0(E_{\text{上}}^2 - E_{\text{下}}^2)\)**；若求完时间积分得到复杂根式对数，一定用 \(g = 0\) 退化为 \(\ddot{x} \propto (d/2 + x) \implies \cosh\) 解析解检验系数，极易抓出漏掉因子 \(2\) 的低级错误！

---

## 11. 第35届决赛理论第3题 · 旋转定滑轮驱动连续软绳的变质量动力学与欧拉—绞盘公式推广 (`cpho-2018-final-theory-problem-slice-q3`)

- **难度评级**：`D4`
- **物理模型**：含变质量连续吸积/卸载与离心力修正的动态欧拉—绞盘（Euler-Eytelwein）摩擦驱动系统
- **教学标签**：`变质量软绳动力学`、`动态欧拉绞盘公式`、`离心力对正压力修正`、`一阶线性微分方程积分`、`打滑与共速临界`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

滑轮逆时针以恒定角速度 \(\omega\) 转动，绳速未达 \(\omega R\) 前，滑轮带动绳子沿**右侧上升、上方左移、左侧下降**方向以速率 \(v(t) < \omega R\) 运动，滑轮对绳微元的滑动摩擦力沿逆时针方向。

1. **绳子达最大速度前各部分的动力学方程组**
   - **左侧竖直段（长 \(L\)，向下运动）**：在 \(\mathrm{d}t\) 时间内由滑轮转入质量 \(\lambda v\,\mathrm{d}t\)，同时有同样质量触地；软绳堆落地面不向上传递支持反力（地面仅对刚触地微元施冲量，下端张力为零）。对长 \(L\) 的竖直段（质量 \(\lambda L\)）取向下为正，由动量定理/牛顿第二定律：
     \[
     \lambda L g - T_1 = \lambda L \frac{\mathrm{d}v}{\mathrm{d}t}.
     \]
   - **右侧竖直段（长 \(L\)，向上运动）**：在 \(\mathrm{d}t\) 时间内须将地面静止的一段绳微元 \(\mathrm{d}m = \lambda v\,\mathrm{d}t\) 从 \(0\) 加速到 \(v\)，故地面处绳刚被拉起处的张力 \(T'\) 满足 \(T'\,\mathrm{d}t = (\lambda v\,\mathrm{d}t)v \implies T' = \lambda v^2\)。取向上为正，对长 \(L\) 的右侧竖直段有：
     \[
     T_2 - \lambda L g - \lambda v^2 = \lambda L \frac{\mathrm{d}v}{\mathrm{d}t}.
     \]
   - **滑轮上的微元段**：从右侧相切点（\(\varphi = 0\)，张力 \(T_2\)）起沿逆时针方向以圆心角 \(\varphi \in [0, \pi]\) 坐标化（左侧相切点 \(\varphi = \pi\)，张力 \(T_1\)）。取角度间隔 \(\mathrm{d}\varphi\)、弧长 \(R\,\mathrm{d}\varphi\)、质量 \(\lambda R\,\mathrm{d}\varphi\) 的小段软绳，设单位长度支持力为 \(N(\varphi)\)（即微元受法向支持力 \(\mathrm{d}N = N R\,\mathrm{d}\varphi\) 或记为 \(N_1\,\mathrm{d}\varphi\)），滑动摩擦力为 \(\mu\,\mathrm{d}N\) 沿逆时针切向，重力在法向（向内）与切向（顺时针阻碍）分量分别为 \(\lambda R g\sin\varphi\,\mathrm{d}\varphi\) 与 \(-\lambda R g\cos\varphi\,\mathrm{d}\varphi\)。沿切向与径向（向内）列动力学方程：
     \[
     \frac{\mathrm{d}T}{\mathrm{d}\varphi}\mathrm{d}\varphi + \mu\,\mathrm{d}N - \lambda R g\cos\varphi\,\mathrm{d}\varphi = \lambda R\,\mathrm{d}\varphi\frac{\mathrm{d}v}{\mathrm{d}t},
     \]
     \[
     T\,\mathrm{d}\varphi - \mathrm{d}N + \lambda R g\sin\varphi\,\mathrm{d}\varphi = (\lambda R\,\mathrm{d}\varphi)\frac{v^2}{R} = \lambda v^2\,\mathrm{d}\varphi.
     \]
     记 \(\mathcal{N} = \frac{\mathrm{d}N}{\mathrm{d}\varphi}\)（即单位弧度支持力；若用每单位长度支持力 \(N\) 则 \(\mathcal{N} = N R\)），消去 \(\mathcal{N}\) 得一阶线性微分方程：
     \[
     \frac{\mathrm{d}T}{\mathrm{d}\varphi} + \mu T = \lambda R g(\cos\varphi - \mu\sin\varphi) + \lambda R\left(\frac{\mathrm{d}v}{\mathrm{d}t} + \mu\frac{v^2}{R}\right).
     \]

2. **绳子可达到的最大速度大小**
   利用积分因子 \(e^{\mu\varphi}\)，将上述微分方程乘 \(e^{\mu\varphi}\) 后从 \(\varphi = 0\)（\(T=T_2\)）积到 \(\varphi = \pi\)（\(T=T_1\)）：
   \[
   T_1 e^{\mu\pi} - T_2 = \lambda R g \int_0^\pi e^{\mu\varphi}(\cos\varphi - \mu\sin\varphi)\,\mathrm{d}\varphi + \lambda R\left(\frac{\mathrm{d}v}{\mathrm{d}t} + \mu\frac{v^2}{R}\right)\int_0^\pi e^{\mu\varphi}\,\mathrm{d}\varphi.
   \]
   利用题给积分公式算得：
   \[
   \int_0^\pi e^{\mu\varphi}(\cos\varphi - \mu\sin\varphi)\,\mathrm{d}\varphi = \left[\frac{e^{\mu\varphi}}{1+\mu^2}\left(2\mu\cos\varphi + (1-\mu^2)\sin\varphi\right)\right]_0^\pi = -\frac{2\mu}{1+\mu^2}\left(e^{\mu\pi} + 1\right),
   \]
   从而：
   \[
   T_2 - T_1 e^{\mu\pi} = \frac{2\mu\lambda R g}{1+\mu^2}\left(e^{\mu\pi} + 1\right) - \frac{\lambda R}{\mu}\left(e^{\mu\pi} - 1\right)\left(\frac{\mathrm{d}v}{\mathrm{d}t} + \mu\frac{v^2}{R}\right).
   \]
   另一方面由左右两段竖直方程直接组合 \(T_2 - T_1 e^{\mu\pi}\)：
   \[
   T_2 - T_1 e^{\mu\pi} = \lambda v^2 - \lambda L g(e^{\mu\pi} - 1) + \lambda L(e^{\mu\pi} + 1)\frac{\mathrm{d}v}{\mathrm{d}t}.
   \]
   两式联立消去 \(T_1, T_2\)（注意 \(\lambda v^2\) 与 \(-\lambda v^2(e^{\mu\pi}-1)\) 合并后恰好只剩 \(-\lambda v^2 e^{\mu\pi}\)！）：
   \[
   \left[L(e^{\mu\pi}+1) + \frac{R}{\mu}(e^{\mu\pi}-1)\right]\frac{\mathrm{d}v}{\mathrm{d}t} = Lg(e^{\mu\pi}-1) + \frac{2\mu R g}{1+\mu^2}(e^{\mu\pi}+1) - e^{\mu\pi}v^2.
   \]
   当滑轮线速度 \(\omega R\) 足够大（绳子全程相对滑轮打滑）时，令 \(\frac{\mathrm{d}v}{\mathrm{d}t} = 0\) 得滑动极限速度：
   \[
   v_{\text{slip}} = \sqrt{Lg\left(1 - e^{-\mu\pi}\right) + \frac{2\mu R g}{1+\mu^2}\left(1 + e^{-\mu\pi}\right)}.
   \]
   若 \(\omega R < v_{\text{slip}}\)，则绳子加速至 \(v = \omega R\) 后即与滑轮停止相对滑动（转入静摩擦跟随），无法继续加速！因此绳子可达到的最大速度分两种情况：
   \[
   v_{\max} = \begin{cases}
   \sqrt{Lg\left(1 - e^{-\mu\pi}\right) + \dfrac{2\mu R g}{1+\mu^2}\left(1 + e^{-\mu\pi}\right)}, & R\omega \ge \sqrt{Lg\left(1 - e^{-\mu\pi}\right) + \dfrac{2\mu R g}{1+\mu^2}\left(1 + e^{-\mu\pi}\right)}, \\
   R\omega, & R\omega < \sqrt{Lg\left(1 - e^{-\mu\pi}\right) + \dfrac{2\mu R g}{1+\mu^2}\left(1 + e^{-\mu\pi}\right)}.
   \end{cases}
   \]
   （极限物理检验：当 \(\mu \to \infty\) 时，\(v_{\text{slip}} \to \sqrt{Lg}\)——并非趋于无穷，而是在 \(v = \sqrt{Lg}\) 处左侧顶部离心项 \(\lambda v^2\) 恰好抵消左段张力 \(T_1 = \lambda L g\) 使接触支持力归零，终止欧拉指数放大！物理完全自洽。）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（2）问的方程组、最终 \(v_{\max}\) 表达式与分情况讨论条件（`page-8.jpg`–`page-10.jpg` ⑫–⑭式）**完全一致**！官方还提供了用待定系数法直接求非齐次微分方程通解的解法（二）（`page-9.jpg` ⑥–⑨式），并附注指出若只求最大速度可直接在一开始令 \(\frac{\mathrm{d}v}{\mathrm{d}t} = 0\) 计算（但在竞赛解答中写出完整动力学方程是第（1）问要求）。
- **核心难点与典型易错点**：
  - 难点1：变质量左、右两段的不对称性——**“地上提起”需额外消耗张力 \(\lambda v^2\)（\(T' = \lambda v^2\)），而“软绳落堆”下端张力为零（\(T_{\text{bot}}=0\)）**，两者的不对称正好提供了稳态时 \(T_2 - T_1 = \lambda v^2\) 的主要阻力。
  - 难点2：滑轮上离心效应 \(\lambda v^2\,\mathrm{d}\varphi\) 与重力弧长项的耦合积分，以及最终 \(v_{\max} = \min(R\omega, v_{\text{slip}})\) 的物理饱和判据。
  - 易错点1：把左右两段绳子的边界张力对称化——误以为右侧没有 \(\lambda v^2\) 阻力，或者误以为左侧地面也给悬绳施向上推力 \(\lambda v^2\)。
  - 易错点2：忘掉绳子速度不能超过滑轮线速度 \(R\omega\)（滑动摩擦力方向的成立前提是 \(v < R\omega\)！）。
  - 易错点3：切向摩擦力和角参数 \(\varphi\) 方向配反，导致出现 \(e^{+\mu\pi}\) 与 \(e^{-\mu\pi}\) 倒置（检验法则：有摩擦才能越拉越快，故稳态 \(T_2 > T_1\) 必对应 \(T_2 \sim T_1 e^{+\mu\pi}\)）。
- **教练总结与迁移建议**：动态欧拉绞盘公式的核心修正就是把静止张力 \(T\) 替换为“净张力 \(T - \lambda v^2\)”；而处理软绳连续离地/触地的铁律是“**从静止表面加速拉起：\(T = \lambda v^2\)；自由软垂落至地面：\(T = 0\)**”。

---

## 12. 第35届决赛理论第4题 · 有限长衰减弦的稳态受迫驻波与双端驱动选模共振 (`cpho-2018-final-theory-problem-slice-q4`)

- **难度评级**：`D3`
- **物理模型**：有限长有限/无衰减弦的稳态受迫边值问题（包含全反射稳态自洽归一化）与对称/反对称双端受迫共振选模模型
- **教学标签**：`受迫振动与驻波`、`有界衰减行波叠加`、`边值问题共振条件`、`双端同相与反相驱动`、`官方边界勘误`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **右端 \(P_2\) 固定（\(y(L,t)=0\)）、左端 \(P_1\) 受迫（\(y(0,t)=A_0\cos\omega t\)）**
   - **(i) 存在传播衰减常数 \(\gamma > 0\) 时弦上各处振幅 \(A(x)\)**
     记波数 \(k = \frac{\omega}{u}\)。在稳态下，弦上机械波是向右衰减波（空间因子 \(e^{-\gamma x - ikx}\)）与在 \(P_2\) 反射并在两端间无穷次往返叠加后的向左衰减波（向 \(-x\) 传播、振幅随 \(L-x\) 衰减，即随 \(x\) 呈 \(e^{+\gamma x + ikx}\) 变化）的总稳态合成。采用复振幅法设稳态通解为：
     \[
     \tilde{y}(x,t) = \left[C_1 e^{-(\gamma + ik)x} + C_2 e^{+(\gamma + ik)x}\right] e^{i\omega t}.
     \]
     由右端固定条件 \(\tilde{y}(L,t)=0 \implies C_2 = -C_1 e^{-2(\gamma + ik)L}\)；由左端驱动条件 \(\tilde{y}(0,t) = A_0 \implies C_1 + C_2 = A_0\)，直接解得全弦稳态复位移：
     \[
     \tilde{y}(x,t) = A_0 \frac{\sinh\left[(\gamma + ik)(L - x)\right]}{\sinh\left[(\gamma + ik)L\right]} e^{i\omega t}.
     \]
     利用恒等式 \(|\sinh(a + ib)|^2 = \sinh^2 a + \sin^2 b = \frac{1}{2}\left[\cosh(2a) - \cos(2b)\right]\)，得弦上任意位置 \(x \in [0, L]\) 处振动的振幅：
     \[
     A(x) = A_0 \sqrt{\frac{\sinh^2[\gamma(L-x)] + \sin^2\left[\frac{\omega(L-x)}{u}\right]}{\sinh^2(\gamma L) + \sin^2\left(\frac{\omega L}{u}\right)}} = A_0 \sqrt{\frac{\cosh[2\gamma(L-x)] - \cos\left[\frac{2\omega(L-x)}{u}\right]}{\cosh(2\gamma L) - \cos\left(\frac{2\omega L}{u}\right)}}.
     \]
     （边界检验：\(A(0) = A_0\)，\(A(L) = 0\)；且当 \(L \to \infty\) 时退化为 \(A_0 e^{-\gamma x}\)，完全自洽。）

   - **(ii) 忽略衰减（\(\gamma = 0\)）时的驻波表达式、波腹与波节位置**
     令 \(\gamma \to 0\)（并假设非共振状态 \(\sin(\frac{\omega L}{u}) \neq 0\)），上式直接退化为实驻波：
     \[
     y(x, t) = A_0 \frac{\sin\left[\frac{\omega(L - x)}{u}\right]}{\sin\left(\frac{\omega L}{u}\right)}\cos(\omega t).
     \]
     - **波节**（\(y(x,t) \equiv 0\)）：\(\frac{\omega(L - x_n)}{u} = m\pi\)，即：
       \[
       x_n = L - \frac{m\pi u}{\omega}, \qquad m \text{ 为满足 } 0 \le m \le \frac{\omega L}{\pi u} \text{ 的非负整数}.
       \]
     - **波腹**（\(\left|\sin\left[\frac{\omega(L-x)}{u}\right]\right| = 1\)）：\(\frac{\omega(L - x_a)}{u} = \left(l + \frac{1}{2}\right)\pi\)，即：
       \[
       x_a = L - \left(l + \frac{1}{2}\right)\frac{\pi u}{\omega}, \qquad l \text{ 为满足 } 0 \le l \le \frac{\omega L}{\pi u} - \frac{1}{2} \text{ 的非负整数}.
       \]

2. **\(P_1\)、\(P_2\) 双端同时驱动（\(\gamma = 0\)）时的振动表达式与共振条件**
   由线性叠加原理，将总受迫振动分解为“\(P_1\) 驱动、\(P_2\) 固定”与“\(P_2\) 驱动、\(P_1\) 固定”（把 \(x\) 换为 \(L-x\) 并加初相 \(\varphi_0\)）两个单端受迫解之和：
   \[
   y(x,t) = A_0 \frac{\sin\left[\frac{\omega(L-x)}{u}\right]}{\sin\left(\frac{\omega L}{u}\right)}\cos(\omega t) + A_0 \frac{\sin\left(\frac{\omega x}{u}\right)}{\sin\left(\frac{\omega L}{u}\right)}\cos(\omega t + \varphi_0).
   \]
   - **当 \(\varphi_0 = 0\)（两端同相振动）时**：利用和差化积 \(\sin[\frac{\omega(L-x)}{u}] + \sin(\frac{\omega x}{u}) = 2\sin(\frac{\omega L}{2u})\cos[\frac{\omega}{u}(x - \frac{L}{2})]\) 及 \(\sin(\frac{\omega L}{u}) = 2\sin(\frac{\omega L}{2u})\cos(\frac{\omega L}{2u})\)，**偶次模因子 \(\sin(\frac{\omega L}{2u})\) 恰好约去**：
     \[
     y(x,t) = A_0 \frac{\cos\left[\frac{\omega}{u}\left(x - \frac{L}{2}\right)\right]}{\cos\left(\frac{\omega L}{2u}\right)}\cos(\omega t).
     \]
     共振发生在分母趋零处：\(\cos\left(\frac{\omega L}{2u}\right) = 0 \implies\)
     \[
     \omega = \frac{(2n + 1)\pi u}{L}, \qquad n = 0, 1, 2, \dots \quad (\text{仅激发奇次对称简正模}).
     \]
   - **当 \(\varphi_0 = \pi\)（两端反相振动，\(\cos(\omega t + \pi) = -\cos\omega t\)）时**：利用和差化积 \(\sin[\frac{\omega(L-x)}{u}] - \sin(\frac{\omega x}{u}) = 2\cos(\frac{\omega L}{2u})\sin[\frac{\omega}{u}(\frac{L}{2} - x)]\)，**奇次模因子 \(\cos(\frac{\omega L}{2u})\) 约去**：
     \[
     y(x,t) = A_0 \frac{\sin\left[\frac{\omega}{u}\left(\frac{L}{2} - x\right)\right]}{\sin\left(\frac{\omega L}{2u}\right)}\cos(\omega t).
     \]
     共振发生在分母趋零（且 \(\omega > 0\)）处：\(\sin\left(\frac{\omega L}{2u}\right) = 0 \implies\)
     \[
     \omega = \frac{2n\pi u}{L}, \qquad n = 1, 2, 3, \dots \quad (\text{仅激发偶次反对称简正模}).
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：
  - 第（1）（i）问：官方解答（`page-11.jpg` ①–⑤式）先写出向正/负方向传播并在 \(x=L\) 相互抵消的一对衰减行波（待定振幅 \(A_1\)），再用 \(A(x=0) = A_0\) 反解 \(A_1\)——这种“用稳态左端总振幅归一化行波系数”的处理本质上自动计入了无穷次往返反射，经恒等变换其 ⑤ 式与盲解复指数双曲正弦公式 **100% 等价**！（盲解复指数法同时确定了各点准确相位，且更紧凑）。
  - 第（2）问：公式 ⑯–⑲ 与盲解完全一致！
- **官方疏漏勘察（`page-12.jpg` ⑭式波腹整数范围错误）**：
  官方 `page-12.jpg` ⑬式写出波腹坐标 \(x_a = L - \pi\frac{u}{2\omega} - l\pi\frac{u}{\omega}\)，但紧接着在 ⑭ 式给出的整数 \(l\) 范围却是 **`0 < l < \frac{L\omega}{\pi u}`**！这存在双重边界错误：① 严格不等号 \(l > 0\) 漏掉了离固定端最近的第一个波腹 \(l = 0\)（\(x_a = L - \frac{\lambda}{4}\)）；② 当 \(\frac{L\omega}{\pi u} - \frac{1}{2} < l < \frac{L\omega}{\pi u}\) 时（例如 \(L = 0.6\lambda \implies \frac{L\omega}{\pi u} = 1.2\)，\(l=1\)），会产生 \(x_a < 0\) 落在弦左端之外的伪解！正确约束应为 \(0 \le l \le \frac{L\omega}{\pi u} - \frac{1}{2}\)。
- **核心难点与典型易错点**：
  - 难点1：理解第（1）（i）问的“稳态边值归一化”——不能直接把入射行波 \(x=0\) 的振幅设成 \(A_0\)，而必须令“向右波 + 向左反射波”的**合成总振动**在 \(x=0\) 处等于 \(A_0\cos\omega t\)！
  - 难点2：第（2）问通过化简分母约去无效极点，看出驱动对称性（同相 vs 反相）对简正模的选择定则。
  - 易错点1：在（1）（i）中直接将 \(y_+(0,t) = A_0\cos\omega t\) 再叠加反射波，致使 \(x=0\) 振幅不等于 \(A_0\)，且在（1）（ii）中失去 \(\sin(\omega L/u)\) 共振分母。
  - 易错点2：第（2）问忘记约去 \(\sin(\frac{\omega L}{2u})\) 或 \(\cos(\frac{\omega L}{2u})\)，误以为 \(\varphi_0 = 0\) 和 \(\varphi_0 = \pi\) 的共振频率都是全部 \(\frac{n\pi u}{L}\)。
- **教练总结与迁移建议**：受迫驻波题如果直接从“一次入射 + 一次反射”出发往往满足不了驱动端振幅条件；最稳妥的通法永远是**写出完整通解（两个相反方向基模的线性组合）\(\to\) 代入两端边界条件反解系数**。至于波腹波节位置范围，直接代入不等式 \(0 \le x \le L\) 解出指标区间最为可靠，切莫凭印象抄范围。

---

## 13. 第35届决赛理论第5题 · 太空绝热容器小孔分子泻流的温度演化与反冲加速动力学 (`cpho-2018-final-theory-problem-slice-q5`)

- **难度评级**：`D4`
- **物理模型**：麦克斯韦速度分布通量加权统计（克努森分子泻流）、无外力变质量火箭动量/能量守恒耦合冷却演化
- **教学标签**：`麦克斯韦分子泻流`、`泻流平均动能2kT`、`容器冷却绝热方程`、`气体动力学反冲`、`通量积分计算`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

（注：原题 `page-13.jpg` 第3行“气体的初始温度为 \(T_0\)”后存在排版残留字符“\(P_0\ P_0\)”，因题给 \(N_0, V, T_0\) 已完全确定初始状态 \(P_0 = N_0 k T_0 / V\)，后续推导无需单独使用 \(P_0\)。）

1. **单位时间单位面积小孔泄出的气体分子数 \(\Phi\)**
   设小孔外法向为 \(+x\) 轴，记 \(A = \frac{m}{2kT}\)。只有 \(v_x > 0\) 的分子在 \(\mathrm{d}t\) 内从面积 \(S\)、长 \(v_x\mathrm{d}t\) 的斜柱体中飞出，故通量为：
   \[
   \Phi = \int_0^\infty n v_x f(v_x)\,\mathrm{d}v_x = n\sqrt{\frac{m}{2\pi k T}}\int_0^\infty v_x \exp\left(-\frac{m v_x^2}{2kT}\right)\mathrm{d}v_x.
   \]
   套用题给积分 \(\int_0^\infty x e^{-Ax^2}\,\mathrm{d}x = \frac{1}{2A}\) 得：
   \[
   \Phi = n\sqrt{\frac{A}{\pi}}\cdot\frac{1}{2A} = n\sqrt{\frac{k T}{2\pi m}} = \frac{1}{4}n\bar{v}.
   \]

2. **泄出气体分子相对容器的平均动能 \(\overline{E}_k\)**
   因为三维速度分布可分离为 \(f(v_x)f(v_y)f(v_z)\)，横向速率 \(v_y, v_z\) 与分子能否穿过小孔无关，仍保持常规热平衡分布 \(\frac{1}{2}m\overline{v_y^2} = \frac{1}{2}m\overline{v_z^2} = \frac{1}{2}kT\)（或用 \(\int_0^\infty x^2 e^{-Ax^2}\,\mathrm{d}x = \frac{1}{4}\sqrt{\pi/A^3}\) 验证）；而法向分速度 \(v_x > 0\) 按通量 \(v_x f(v_x)\) 加权：
   \[
   \frac{1}{2}m\overline{v_{x,\text{eff}}^2} = \frac{\int_0^\infty \frac{1}{2}m v_x^3 f(v_x)\,\mathrm{d}v_x}{\int_0^\infty v_x f(v_x)\,\mathrm{d}v_x} = \frac{1}{2}m\frac{1/(2A^2)}{1/(2A)} = \frac{m}{2A} = kT.
   \]
   故泄出分子相对容器的平均动能为：
   \[
   \overline{E}_k = kT + \frac{1}{2}kT + \frac{1}{2}kT = 2kT.
   \]

3. **\(t\) 时刻容器内气体的温度 \(T(t)\)**
   设 \(t\) 时刻容器内分子数为 \(N\)、温度为 \(T\)，容器（连同内部气体）沿 \(-x\) 方向以速率 \(u\) 运动。经 \(\mathrm{d}t\) 时间分子数改变 \(\mathrm{d}N < 0\)（泄出 \(-\mathrm{d}N\) 个分子，其相对容器的平均 \(x\) 速度记为 \(\bar{v}_x > 0\)）。由全系统（容器 + 全部气体）动量守恒与能量守恒：
   - 动量守恒：\((M + Nm)\mathrm{d}u = -m \bar{v}_x\,\mathrm{d}N\)；
   - 能量守恒（略去二阶小量）：
     \[
     (M + Nm)u\,\mathrm{d}u + \frac{3}{2}N k\,\mathrm{d}T + \frac{1}{2}k T\,\mathrm{d}N + m u \bar{v}_x\,\mathrm{d}N - \frac{1}{2}m\overline{v_x^2}\,\mathrm{d}N = 0.
     \]
   注意利用动量方程 \((M+Nm)u\,\mathrm{d}u + m u \bar{v}_x\,\mathrm{d}N = 0\) 精确相消（对**任意容器质量 \(M\)** 均成立！），又由第（2）问 \(\frac{1}{2}m\overline{v_x^2} = kT\)，化简得：
   \[
   \frac{3}{2}N k\,\mathrm{d}T = \frac{1}{2}k T\,\mathrm{d}N \implies \frac{\mathrm{d}N}{N} = 3\frac{\mathrm{d}T}{T} \implies \frac{N}{N_0} = \left(\frac{T}{T_0}\right)^3.
   \]
   再结合由第（1）问给出的分子泄漏速率方程（\(n = N/V\)）：
   \[
   \frac{\mathrm{d}N}{\mathrm{d}t} = -S\frac{N}{V}\sqrt{\frac{k T}{2\pi m}} \implies 3\frac{\mathrm{d}T}{T} = -\frac{S}{V}\sqrt{\frac{k}{2\pi m}} T^{1/2}\,\mathrm{d}t.
   \]
   分离变量积分（\(t=0\) 时 \(T=T_0\)）：
   \[
   \int_{T_0}^T T'^{-3/2}\,\mathrm{d}T' = -2\left(T^{-1/2} - T_0^{-1/2}\right) = -\frac{S}{3V}\sqrt{\frac{k}{2\pi m}}\,t,
   \]
   解出 \(T(t)\)：
   \[
   T(t) = T_0 \left(1 + \frac{S}{6V}\sqrt{\frac{k T_0}{2\pi m}}\,t\right)^{-2}.
   \]

4. **\(t\) 时刻容器运动速度的大小 \(u(t)\)（假设 \(M \gg N_0 m\)）**
   泄出分子的通量平均 \(x\) 向速度为：
   \[
   \bar{v}_x = \frac{\int_0^\infty v_x^2 f(v_x)\,\mathrm{d}v_x}{\int_0^\infty v_x f(v_x)\,\mathrm{d}v_x} = \frac{\frac{1}{4}\sqrt{\pi/A^3}}{\frac{1}{2A}} = \frac{1}{2}\sqrt{\frac{\pi}{A}} = \sqrt{\frac{\pi k T}{2m}}.
   \]
   （注：由此算出瞬时推力为 \(-\dot{N}m\bar{v}_x = S n\sqrt{\frac{kT}{2\pi m}}\cdot m\sqrt{\frac{\pi kT}{2m}} = \frac{1}{2}n k T S = \frac{1}{2}PS\)。）
   由动量方程 \(\mathrm{d}u = -\frac{m\bar{v}_x\,\mathrm{d}N}{M + Nm}\)，在 \(M \gg N_0 m\) 近似下分母取为 \(M\)，代入 \(T = T_0(N/N_0)^{1/3}\) 积分：
   \[
   u(t) \approx \frac{1}{M}\sqrt{\frac{\pi m k T_0}{2}}\int_{N(t)}^{N_0}\left(\frac{N}{N_0}\right)^{1/6}\mathrm{d}N = \frac{6 N_0}{7 M}\sqrt{\frac{\pi m k T_0}{2}}\left[1 - \left(\frac{N(t)}{N_0}\right)^{7/6}\right].
   \]
   代入 \(N(t) = N_0 \left(1 + \frac{S}{6V}\sqrt{\frac{kT_0}{2\pi m}}\,t\right)^{-6}\) 即得：
   \[
   u(t) = \frac{6 N_0}{7 M}\sqrt{\frac{\pi m k T_0}{2}}\left[1 - \left(1 + \frac{S}{6V}\sqrt{\frac{k T_0}{2\pi m}}\,t\right)^{-7}\right] = \frac{3 N_0 m}{7 M}\sqrt{\frac{2\pi k T_0}{m}}\left[1 - \left(1 + \frac{S}{6V}\sqrt{\frac{k T_0}{2\pi m}}\,t\right)^{-7}\right].
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解与官方解答（`page-13.jpg`–`page-16.jpg`）在物理思想、精确消去容器动能项（不依赖 \(M \gg N_0 m\) 的精确热力学冷却律 \(T \propto N^{1/3}\)）以及全部 4 问的最终表达式上 **100% 吻合**！仅见官方 `page-15.jpg` ⑰ 式末尾微分号把 \(\mathrm{d}v_x\) 印刷错写为 \(\mathrm{d}v_{mx}\)。
- **核心难点与典型易错点**：
  - 难点1：第（3）问必须严密验证容器整体平动动能增量 \((M+Nm)u\,\mathrm{d}u\) 与泄漏分子带走的交叉动能 \(m u \bar{v}_x\,\mathrm{d}N\) 精确相消，而非不加证明就认为“容器静止”。
  - 难点2：正确区分内部平均动能 \(\frac{3}{2}kT\) 与泻流平均动能 \(2kT\)，以及正确导出推力 \(F = \frac{1}{2}PS\)（而非 \(PS\)！）。
  - 易错点1：第（3）问直接用内部气体平均动能 \(\frac{3}{2}kT\) 代替泄出分子的平均动能 \(2kT\)，会错得出“气体泄漏但温度 \(T\) 恒定不变”的荒谬结论！
  - 易错点2：第（4）问直接按“开口对侧壁面压强不变、开口处缺口面积 \(S\)”错算反冲推力为 \(PS\)（比真实推力 \(\frac{1}{2}PS\) 大一倍），忽略了泻流孔附近无回弹反射分子导致的动量通量减半与腔壁等效压力重分布。
- **教练总结与迁移建议**：分子泻流（Knudsen effusion）所有计算都围绕“速度分布被通量加权多乘了一个 \(v_x\)”展开——分子数通量是 \(\langle v_x\rangle_+\)，动量通量（推力）是 \(m\langle v_x^2\rangle_+ = \frac{1}{2}nkT\)，动能通量是 \(\frac{1}{2}m\langle v_x(v_x^2+v_\perp^2)\rangle_+ = \Phi\cdot(2kT)\)。永远用**控制体动量/能量守恒**算反冲，绝不盲套“壁面缺口法”！

---

## 14. 第35届决赛理论第6题 · 负折射率介质的惠更斯作图、球面折射成像与组合透镜光路 (`cpho-2018-final-theory-problem-slice-q6`)

- **难度评级**：`D3`
- **物理模型**：负折射率超材料（波矢与能流反向、负光程）的惠更斯子波相位作图与傍轴球面折射高斯公式统一模型
- **教学标签**：`负折射率介质`、`惠更斯原理与负光程`、`球面折射成像公式`、`横向放大率正负号`、`组合透镜光路图`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **惠更斯原理证明折射定律（含图 a、图 b 子波与光线示意图）**
   设平行光以入射角 \(\theta_1 > 0\) 从左上方射向界面，入射等相位面 \(AB\) 于 \(t=0\) 到达 \(A\)，经 \(\Delta t\) 后 \(B\) 点波前传播距离 \(|BB'| = \frac{c}{n_1}\Delta t\) 到达界面 \(B'\)。
   - **图 a（\(n_1 > 0, n_2 > 0\)）**：子波在介质 2 中沿能流正向推进，以 \(A\) 为圆心向介质 2 作半径 \(r = |AA'| = \frac{n_1}{n_2}|BB'|\)（光程相等 \(n_2 r = n_1|BB'|\)）的半圆子波面；过 \(B'\) 作该圆的切线 \(B'A'\) 为新波前，折射线 \(AA'\) 与入射光线分居法线两侧（\(\theta_2 > 0\)）。由直角三角形 \(\triangle ABB'\) 与 \(\triangle AA'B'\)：\(|BB'| = |AB'|\sin\theta_1\)、\(r = |AB'|\sin\theta_2\)，故 \(n_1\sin\theta_1 = n_2\sin\theta_2\)。
   - **图 b（\(n_1 > 0, n_2 < 0\)）**：介质 2 中光程为负（相位随光线传播方向反向递增），\(A\) 点处与 \(B'\) 点等相位面的确定有两种等价惠更斯几何构造：
     - **构造一（介质 2 内由 \(B'\) 发波的等相位圆）**：在 \(B'\) 点向介质 2 内作半径 \(r = \frac{n_1}{|n_2|}|BB'|\)（使 \(n_1|BB'| + n_2|B'A'| = 0\)）的半圆子波面，从已提前激发的 \(A\) 点向该半圆作切线 \(AA'\)（切点 \(A'\) 在法线同侧偏左下方），折射光线从 \(B'\) 射向 \(A'\)（与入射光线位于法线**同侧**，\(\theta_2 < 0\)），由 \(|B'A'| = |AB'|\sin|\theta_2|\) 即得 \(n_1\sin\theta_1 = -n_2\sin|\theta_2| = n_2\sin\theta_2\)。
     - **构造二（介质 1 中虚线倒退等相位子波圆）**：以 \(A\) 为圆心、在介质 1 一侧用虚线画半径 \(r = \frac{n_1}{|n_2|}|BB'|\) 的等效反相半圆，过 \(B'\) 作切线 \(B'A'\)，射线由 \(A'\) 经 \(A\) 反向射入介质 2，折射线同样弯向法线同侧（\(\theta_2 < 0\)），同样给出 \(n_1\sin\theta_1 = n_2\sin\theta_2\)。

2. **\(n_1 > 0, n_2 < 0\) 球面傍轴成像公式、横向放大率与符号约定**
   **符号约定**：以球面顶点 \(O\) 为原点，规定**物方（左侧介质 1）实物距 \(s_1 > 0\)**（虚物在右侧则 \(s_1 < 0\)），**像方（右侧介质 2）实像距 \(s_2 > 0\)**（虚像在左侧则 \(s_2 < 0\)）；球心 \(C\) 位于顶点 \(O\) 右侧（凸面向入射光）时曲率半径 \(R > 0\)（反之 \(R < 0\)）；入射角 \(\theta_1\) 为正，折射光线与入射光线在法线同侧时折射角 \(\theta_2 < 0\)；横向放大率 \(\beta_{\text{mag}} = h_2 / h_1\)（正值表示正立像，负值表示倒立像）。
   结合原题图 c（物在 \(x\)、像在 \(y\) 位于 \(OC\) 之间，图中标出的 \(\alpha_1, \alpha_2, \beta\) 均为正锐角），设折射点 \(M\) 距光轴小高度为 \(h\)。在傍轴近似下：
   \[
   \alpha_1 \approx \frac{h}{s_1}, \qquad \alpha_2 \approx \frac{h}{s_2}, \qquad \beta \approx \frac{h}{R}.
   \]
   由三角形外角关系得 \(\theta_1 = \alpha_1 + \beta\)，且在 \(\triangle MyC\) 中外角 \(\alpha_2 = |\theta_2| + \beta \implies -\theta_2 = \alpha_2 - \beta\)。代入小角折射定律 \(n_1\theta_1 = n_2\theta_2\)：
   \[
   n_1\left(\frac{h}{s_1} + \frac{h}{R}\right) = -n_2\left(\frac{h}{s_2} - \frac{h}{R}\right) \implies \frac{n_1}{s_1} + \frac{n_2}{s_2} = \frac{n_2 - n_1}{R}.
   \]
   （形式与正折射率介质球面公式完全相同！）
   **横向放大率**：对高度为 \(h_1 > 0\) 的小竖直物 \(Q_1P_1\)，考察过球心 \(C\) 的光线（正入射 \(\theta_1 = 0 \implies \theta_2 = 0\) 直线不偏折穿透）及射向顶点 \(O\) 的光线（\(\theta_1 \approx h_1/s_1\)，负折射弯向光轴同侧上方成**正立实像** \(h_2 > 0\)）：
   \[
   \frac{h_2}{h_1} = \frac{R - s_2}{s_1 + R} = -\frac{n_1 s_2}{n_2 s_1} \quad (> 0, \text{ 正立放大/缩小实像}).
   \]
   即横向放大率公式仍统一表为 \(\beta_{\text{mag}} = -\frac{n_1 s_2}{n_2 s_1}\)（若仅取放大率绝对值则为 \(\left|\frac{n_1 s_2}{n_2 s_1}\right|\)）。

3. **薄凸透镜 + 球面组合系统会聚点计算与序号 4 光路图**
   平行光经焦距 \(f = 1.5R\) 的薄凸透镜（\(O'\) 距 \(O\) 为 \(d\)）后，若无球面将聚于 \(O\) 点右侧距 \(O\) 为 \(f - d\) 处，故对球面构成**虚物**，物距 \(s_1 = -(f - d) = -(1.5R - d) < 0\)（空气 \(n_1 = 1\)）。代入球面成像公式解出像距 \(s_2\)：
   \[
   s_2 = \frac{n_2 R s_1}{n_2 s_1 - (s_1 + R)} = \frac{n_2 R(f - d)}{(n_2 - 1)(f - d) + R}:
   \]
   - **序号 1**（\(n_2 = 1.5,\; d = 0.35R\)，\(f-d=1.15R\)）：\(s_2 = \frac{1.5\times 1.15}{0.5\times 1.15 + 1}R = \frac{23}{21}R \approx 1.10R\)；
   - **序号 2**（\(n_2 = 1.5,\; d = 0.85R\)，\(f-d=0.65R\)）：\(s_2 = \frac{1.5\times 0.65}{0.5\times 0.65 + 1}R = \frac{39}{53}R \approx 0.74R\)；
   - **序号 3**（\(n_2 = -1.5,\; d = 0.35R\)，\(f-d=1.15R\)）：\(s_2 = \frac{-1.5\times 1.15}{-2.5\times 1.15 + 1}R = \frac{23}{25}R = 0.92R\)；
   - **序号 4**（\(n_2 = -1.5,\; d = 0.85R\)，\(f-d=0.65R\)）：\(s_2 = \frac{-1.5\times 0.65}{-2.5\times 0.65 + 1}R = \frac{39}{25}R = 1.56R\)。
   **序号 4 光路示意**：平行光经凸透镜会聚朝 \(O\) 右侧 \(0.65R\)（位于 \(O\) 与球心 \(C\) 之间）射去。光线在球面 \(M\)（轴上方）处自空气射入时，其斜率 \(-h/(0.65R)\) 比法线 \(MC\) 斜率 \(-h/R\) 更陡峭（即入射光在法线**上方/外侧**）；因 \(n_2 = -1.5 < 0\) 发生负折射，折射光线折向法线 \(MC\) **同侧（即法线上方）**且偏折角 \(|\theta_2| = |\theta_1|/1.5 < |\theta_1|\)，从而斜率平缓下来，在介质 2 中跨越球心 \(C\) 最终**会聚在 \(O\) 右侧 \(s_2 = 1.56R\) 处**（正折射只会加速会聚到更近，负折射反而在本情形推迟了会聚！）。

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解与官方解答（`page-16.jpg`–`page-19.jpg`）高度一致！尤其值得一提的是：盲解在（1）问中独立想出的两套负折射惠更斯作图法，恰与官方的图 1b（解法一：\(B'\) 点圆切线法）与图 1b'（解法二：介质 1 虚线倒退相位圆法）完全对应；第（3）问表格 4 个数值 `1.10R, 0.74R, 0.92R, 1.56R` 及图 3 光路与官方一模一样！
- **官方细微差异注记**：官方第（2）问⑬式对放大率写成正的绝对值比 \(\frac{|Q_2P_2|}{|Q_1P_1|} = -\frac{s_2 n_1}{s_1 n_2}\)，而盲解明确赋予了符号意义（\(\beta_{\text{mag}} > 0\) 正立像，\(\beta_{\text{mag}} < 0\) 倒立像），当 \(n_2 < 0, s_1 > 0, s_2 > 0\) 时负折射球面直接成**正立实像**，这是一个极其反直觉但完全严谨的物理亮点！
- **核心难点与典型易错点**：
  - 难点1：负折射介质中“相位传播方向与能量（光线）方向相反”，导致常规在介质 2 内以 \(A\) 为圆心画前向子波的作图法失效，必须改用“\(B'\) 点半圆法”或“介质 1 倒退等相位面法”。
  - 难点2：第（3）问序号 4 光路中准确判断入射光线与球面法线 \(MC\) 谁更陡峭——只有比较 \(f - d = 0.65R < R\) 才知光线落于法线外侧，负折射后反倒向远轴端偏折至 \(1.56R > R\)（若如序号 3那样 \(f-d=1.15R > R\)，光线落于法线内侧，负折射后则更早聚在 \(0.92R < R\)）。
  - 易错点1：套用球面折射公式时误以为负折射率要改写公式形式或给 \(s_1\) 乱加负号；实际只要沿用“实物为正虚物为负，实像为正虚像为负，凸向入射光半径为正”的传统符号约定，公式 \(\frac{n_1}{s_1} + \frac{n_2}{s_2} = \frac{n_2 - n_1}{R}\) 无需任何改动！
- **教练总结与迁移建议**：负折射几何光学（如著名的 Veselago 平板完美透镜，\(n_2 = -1, R \to \infty \implies s_2 = -s_1\) 且成正立实像）的黄金法则：**只要严格坚持光线弯向法线“同侧”的几何规则与带符号折射率 \(n_2 < 0\)，经典高斯成像公式全部自动成立**。画光路时务必先画出过入射点的球面法线（连接球心 \(C\)），再对比斜率决定偏折侧。

---

## 15. 第35届决赛理论第7题 · 非抛物色散二维准粒子在电磁场中的回旋运动与非共线加速 (`cpho-2018-final-theory-problem-slice-q7`)

- **难度评级**：`D3`
- **物理模型**：各向同性非二次型色散关系 \(K(p) = \frac{p^2}{2m} + \alpha p\)（类 Rashba/Dirac-二次混合准粒子）的群速度与外场半经典动力学方程
- **教学标签**：`准粒子色散关系`、`动能定理求群速度`、`非抛物回旋周期`、`逆有效质量张量`、`非共线电场横向加速`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **真实自由粒子速度与动量关系**
   设任意外力 \(\vec{F} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t}\) 作用于粒子，在 \(\mathrm{d}t\) 内微位移为 \(\mathrm{d}\vec{r} = \vec{v}\,\mathrm{d}t\)，由动能定理：
   \[
   \mathrm{d}K = \vec{F}\cdot\mathrm{d}\vec{r} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t}\cdot\vec{v}\,\mathrm{d}t = \vec{v}\cdot\mathrm{d}\vec{p}.
   \]
   对 \(K = \frac{p^2}{2m} = \frac{\vec{p}\cdot\vec{p}}{2m}\) 求全微分得 \(\mathrm{d}K = \frac{\vec{p}}{m}\cdot\mathrm{d}\vec{p}\)，比较即 \(\left(\frac{\vec{p}}{m} - \vec{v}\right)\cdot\mathrm{d}\vec{p} = 0\)。因外力方向任意故 \(\mathrm{d}\vec{p}\) 任意，得：
   \[
   \vec{v} = \frac{\vec{p}}{m}.
   \]

2. **准粒子速度与动量关系**
   对 \(K = \frac{p^2}{2m} + \alpha p\)（其中 \(p = \sqrt{p_x^2 + p_y^2} > 0\)）求微分，注意到 \(\mathrm{d}p = \frac{\vec{p}\cdot\mathrm{d}\vec{p}}{p}\)：
   \[
   \mathrm{d}K = \left(\frac{\vec{p}}{m} + \alpha\frac{\vec{p}}{p}\right)\cdot\mathrm{d}\vec{p} = \vec{v}\cdot\mathrm{d}\vec{p} \implies \vec{v} = \frac{\vec{p}}{m} + \alpha\frac{\vec{p}}{p}.
   \]

3. **用动能 \(K\) 表示准粒子速率 \(v\)**
   由（2）式及 \(\alpha > 0\) 得 \(v = |\vec{v}| = \frac{p}{m} + \alpha\)，两边平方或配方：
   \[
   \frac{1}{2}m v^2 = \frac{1}{2}m\left(\frac{p}{m} + \alpha\right)^2 = \frac{p^2}{2m} + \alpha p + \frac{1}{2}m\alpha^2 = K + \frac{1}{2}m\alpha^2 \implies v = \sqrt{\alpha^2 + \frac{2K}{m}}.
   \]
   （同时解出动量大小 \(p = m(v - \alpha) = \sqrt{m^2\alpha^2 + 2mK} - m\alpha\)。）

4. **匀强磁场 \(\vec{B} = B\hat{k}\) 中匀速圆周运动的半径、周期与角动量大小**
   由半经典运动方程 \(\frac{\mathrm{d}\vec{p}}{\mathrm{d}t} = q\vec{v}\times\vec{B}\)，在匀速圆周运动中 \(v = \omega R\)，动量方向同步旋转故 \(\left|\frac{\mathrm{d}\vec{p}}{\mathrm{d}t}\right| = \omega p = \frac{v}{R}p\)，动力学方程给出：
   \[
   p\frac{v}{R} = |q|vB \implies R = \frac{p}{|q|B}.
   \]
   代入 \(p(K)\) 与 \(v(K)\)（若按通常假定 \(q > 0, B > 0\) 可去绝对值）：
   - **回旋半径**：
     \[
     R = \frac{\sqrt{m^2\alpha^2 + 2mK} - m\alpha}{|q|B} = \frac{m\left(\sqrt{\alpha^2 + \frac{2K}{m}} - \alpha\right)}{|q|B};
     \]
   - **回旋周期**：
     \[
     T = \frac{2\pi R}{v} = \frac{2\pi\left(\sqrt{m^2\alpha^2 + 2mK} - m\alpha\right)}{|q|B\sqrt{\alpha^2 + \frac{2K}{m}}} = \frac{2\pi m}{|q|B}\left(1 - \frac{\alpha}{\sqrt{\alpha^2 + \frac{2K}{m}}}\right);
     \]
   - **角动量大小**（相对圆心，\(L = |\vec{r}\times\vec{p}| = R p\)）：
     \[
     L = R p = \frac{p^2}{|q|B} = \frac{m^2}{|q|B}\left(\sqrt{\alpha^2 + \frac{2K}{m}} - \alpha\right)^2 = \frac{2m^2\alpha^2 + 2mK - 2m\alpha\sqrt{m^2\alpha^2 + 2mK}}{|q|B}.
     \]

5. **匀强电场 \(\vec{E} = E\hat{i}\) 中的加速度分量 \(a_x\) 和 \(a_y\)**
   由 \(\vec{v} = \left(\frac{p}{m} + \alpha\right)\hat{p}\) 且 \(v > \alpha\)，\(\vec{p}\) 与 \(\vec{v}\) 同向，夹 \(+x\) 轴角度均为 \(\theta\)，故 \(p_x = p\cos\theta,\; p_y = p\sin\theta\)，且 \(p = m(v - \alpha)\)。
   对极坐标下的动量方程 \(\dot{\vec{p}} = qE\hat{i}\) 求分量（方法二极坐标法最简）：
   \[
   \dot{p}\cos\theta - p\sin\theta\,\dot{\theta} = qE, \qquad \dot{p}\sin\theta + p\cos\theta\,\dot{\theta} = 0 \implies \dot{p} = qE\cos\theta, \qquad \dot{\theta} = -\frac{qE}{p}\sin\theta = -\frac{qE\sin\theta}{m(v-\alpha)}.
   \]
   将 \(v_x = v\cos\theta,\; v_y = v\sin\theta\) 对时间求导（其中 \(\dot{v} = \dot{p}/m = \frac{qE}{m}\cos\theta\)）：
   \[
   a_x = \dot{v}\cos\theta - v\sin\theta\,\dot{\theta} = \frac{qE}{m}\cos^2\theta + \frac{qE}{m}\frac{v\sin^2\theta}{v-\alpha} = \frac{qE}{m}\left(1 + \frac{\alpha\sin^2\theta}{v-\alpha}\right),
   \]
   \[
   a_y = \dot{v}\sin\theta + v\cos\theta\,\dot{\theta} = \frac{qE}{m}\sin\theta\cos\theta - \frac{qE}{m}\frac{v\sin\theta\cos\theta}{v-\alpha} = -\frac{qE}{m}\frac{\alpha\sin\theta\cos\theta}{v-\alpha}.
   \]
   （物理意义注：因 \(\alpha > 0\)，横向有效质量 \(m_\perp = m\frac{v-\alpha}{v} < m\)，而纵向有效质量 \(m_\parallel = m\)，各向异性逆有效质量导致仅受 \(x\) 向电场时产生垂直于电场的 \(y\) 向加速度！）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解全部五问与官方解答（`page-19.jpg`–`page-23.jpg`）**100% 一致**！官方第（5）问给出了三种解法：解法一在直角坐标直接联立 \(a_x, a_y\) 线性方程组；解法二在动量极坐标 \((p,\theta)\) 下求解；解法三在速度极坐标 \((v,\theta)\) 下求解——盲解恰好独立采用了最简练的极坐标法。
- **官方细微笔误注记**：官方 `page-21.jpg` 第（5）问解法一的中间行 eq. ⑰ 写出了 `a_x = \frac{\alpha}{v}\frac{dv_x}{dt} - \frac{\alpha v_x}{v^2}\frac{dv}{dt} + qE`，遗漏了末尾项的分母 \(m\)（应为 \(qE/m\)），在随后的 ⑲、⑳ 式中恢复正确。另官方第（4）问默认 \(q>0\) 省去了 \(|q|\) 符号。
- **核心难点与典型易错点**：
  - 难点1：从高中的“\(\vec{p} = m\vec{v}\)”定势中彻底解放，理解固体能带/准粒子中“**\(\vec{v} = \nabla_{\vec{p}}K\)（群速度）、\(\dot{\vec{p}} = \vec{F}_{\text{ext}}\)（晶体准动量牛顿定律）**”才是根本规律，两者一般不成正比！
  - 难点2：第（5）问正确分辨为什么受纯 \(x\) 向力却有 \(y\) 向加速度（因为 \(\vec{p}\) 方向旋转使得恒定大小的 \(\alpha\hat{p}\) 项改变方向，贡献垂直速度变化率 \(\alpha\dot{\hat{p}}\)）。
  - 易错点1：第（4）问算出角动量时错代成 \(L = m v R\) 而非真实的准粒子角动量 \(L = p R\)。
  - 易错点2：第（5）问在直角坐标求 \(\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\vec{p}}{p}\right)\) 时漏掉对分母 \(p = \sqrt{p_x^2 + p_y^2}\) 求导，或误以为 \(a_y = 0\)。
- **教练总结与迁移建议**：本题是本科《固体物理》半经典电子动力学与《分析力学》哈密顿正则方程 \(\dot{\vec{r}} = \frac{\partial H}{\partial \vec{p}}\) 完美下放高中竞赛的典范。切记两句话：① 只要能量-动量关系 \(K(\vec{p})\) 非二次抛物型，\(\vec{a}\) 与外力 \(\vec{F}\) 就不必共线（逆有效质量张量 \(m_{ij}^{-1} = \frac{\partial^2 K}{\partial p_i \partial p_j}\) 非标量对角阵）；② 匀强磁场中的回旋半径永远只取决于动量大小与电荷磁场比，即 \(R = \frac{p}{|q|B}\)，与色散形式无关！

---

## 16. 第35届决赛理论第8题 · 一维黑体辐射光压驱动理想反射镜的相对论动力学与卡诺热机等价性 (`cpho-2018-final-theory-problem-slice-q8`)

- **难度评级**：`D5`
- **物理模型**：狭义相对论光子-运动反射镜碰撞动力学、一维黑体辐射谱洛伦兹协变性与可逆卡诺辐射热机等价模型
- **教学标签**：`一维黑体辐射`、`相对论多普勒频移`、`辐射压做功效率`、`黑体谱洛伦兹变换`、`卡诺热机非协变性`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **实验室参考系中镜子克服阻力做功的动力学效率 \(\eta\)**
   设实验室参考系 \(S\) 中，单位时间内与以恒定速度 \(v\) 向右运动的理想反射镜发生碰撞的入射光子总能量为 \(\varepsilon_1\)（注：\(\varepsilon_1 = (1 - v/c)\int_0^\infty \varphi(\nu, T_1)\,\mathrm{d}\nu\)），反射后的光子总能量为 \(\varepsilon_2\)，镜子所受外部恒定阻力大小为 \(F\)。由于镜子做匀速直线运动，其自身能量（静能+动能）和动量均保持不变。对于“镜子 + 单位时间内与之碰撞的光子”体系，光子总动量大小为能量除以光速 \(c\)（入射向右 \(+\varepsilon_1/c\)，反射向左 \(-\varepsilon_2/c\)），应用动量定理与能量定理：
   \[
   -\frac{\varepsilon_2}{c} - \frac{\varepsilon_1}{c} = -F \implies \varepsilon_1 + \varepsilon_2 = F c,
   \]
   \[
   \varepsilon_2 - \varepsilon_1 = -F v \implies \varepsilon_1 - \varepsilon_2 = F v.
   \]
   （也可对单个光子用相对论两次多普勒红移推导得 \(\nu_{\text{ref}} = \frac{c-v}{c+v}\nu\)，结论相同。）两式相加得 \(2\varepsilon_1 = F(c + v)\)，故利用入射碰撞光子能量克服阻力做功的效率为：
   \[
   \eta = \frac{F v}{\varepsilon_1} = \frac{2v}{c + v}.
   \]

2. **证明反射镜参考系 \(S'\) 中入射与反射辐射均为一维黑体辐射及热机效率 \(\eta'\)**
   设实验室系 \(S\) 中入射一维黑体辐射温度为 \(T_1\)，其频率 \(\nu_1\) 处的能流密度谱为 \(\varphi_1(\nu_1) = \frac{2h\nu_1}{e^{h\nu_1/(k T_1)} - 1}\)。反射镜以速度 \(v\) 顺辐射方向运动，故在镜子静止系 \(S'\) 中，相对论多普勒效应使入射频率红移为：
   \[
   \nu'_1 = \nu_1 \sqrt{\frac{c - v}{c + v}} \equiv D \nu_1, \qquad D = \sqrt{\frac{c - v}{c + v}}.
   \]
   考察 \(S\) 系中时间间隔 \(\mathrm{d}t_1\) 内通过入射路径某固定截面的一段波列，它在 \(S'\) 系中被镜面接收的持续时间间隔为 \(\mathrm{d}t'_1\)（等效于碰撞时间 \(\mathrm{d}t_{\text{coll}} = \mathrm{d}t_1 / (1 - v/c)\) 经时间膨胀 \(\mathrm{d}t'_1 = \mathrm{d}t_{\text{coll}} / \gamma\)）。因波列内的**总波峰数（相位周期数）为洛伦兹不变量**，有：
   \[
   \nu_1 \mathrm{d}t_1 = \nu'_1 \mathrm{d}t'_1 \quad \left(\text{并有 } \mathrm{d}\nu'_1 = D\,\mathrm{d}\nu_1\right).
   \]
   同时 \(S\) 系中 \(\mathrm{d}t_1\) 内在 \([\nu_1, \nu_1 + \mathrm{d}\nu_1]\) 频带内穿过该截面的所有光子在 \(S'\) 系中悉数在 \(\mathrm{d}t'_1\) 内到达镜面（光子数亦为洛伦兹不变量），故：
   \[
   \frac{\varphi_1(\nu_1)\,\mathrm{d}\nu_1\,\mathrm{d}t_1}{h\nu_1} = \frac{\varphi'_1(\nu'_1)\,\mathrm{d}\nu'_1\,\mathrm{d}t'_1}{h\nu'_1}.
   \]
   代入 \(\nu_1\mathrm{d}t_1 = \nu'_1\mathrm{d}t'_1\) 与 \(\frac{\mathrm{d}\nu'_1}{\nu'_1} = \frac{\mathrm{d}\nu_1}{\nu_1}\)，立即得光谱不变量：
   \[
   \frac{\varphi'_1(\nu'_1)}{\nu'_1} = \frac{\varphi_1(\nu_1)}{\nu_1} \implies \varphi'_1(\nu'_1) = \frac{2 h \nu'_1}{e^{h\nu_1/(kT_1)} - 1} = \frac{2 h \nu'_1}{e^{h\nu'_1/(k T'_1)} - 1},
   \]
   其中入射辐射在 \(S'\) 系中仍严格为一维黑体辐射，有效温度为：
   \[
   T'_1 = \frac{\nu'_1}{\nu_1} T_1 = \sqrt{\frac{c - v}{c + v}}\,T_1.
   \]
   再看反射过程：在 \(S'\) 系中镜面静止，理想弹性反射不改变光子频率，即 \(\nu'_2 = \nu'_1\)，且光子数守恒与波峰数守恒仍成立，同理得 \(\frac{\varphi'_2(\nu'_2)}{\nu'_2} = \frac{\varphi'_1(\nu'_1)}{\nu'_1}\)，故反射辐射在 \(S'\) 系中亦为一维黑体辐射：
   \[
   \varphi'_2(\nu'_2) = \frac{2 h \nu'_2}{e^{h\nu'_2/(k T'_2)} - 1}, \qquad T'_2 = T'_1 = \sqrt{\frac{c - v}{c + v}}\,T_1.
   \]
   在 \(S'\) 系中，该理想卡诺热机吸热与放热温度相等（\(T'_2 = T'_1\)；且镜子静止位移为零，做功为零），故其热机效率为：
   \[
   \eta' = 1 - \frac{T'_2}{T'_1} = 0.
   \]

3. **实验室参考系 \(S\) 中的热机效率**
   将 \(S'\) 系中频率为 \(\nu'_2\) 的反射辐射（沿 \(-x\) 方向远离运动镜面）变换回实验室参考系 \(S\)，再次发生相对论多普勒红移：
   \[
   \nu_2 = \nu'_2 \sqrt{\frac{c - v}{c + v}} = \frac{c - v}{c + v}\nu_1.
   \]
   由与（2）完全相同的波峰数与光子数不变性推导，\(S\) 系中反射能流密度谱仍具有一维黑体辐射形式：
   \[
   \varphi_2(\nu_2) = \frac{2 h \nu_2}{e^{h\nu_2/(k T_2)} - 1}, \qquad T_2 = \frac{\nu_2}{\nu'_2} T'_2 = \frac{c - v}{c + v} T_1.
   \]
   （注：可进一步校验一维黑体能流 \(\Phi(T) \propto T^2\) 与熵流 \(\sigma_S(T) \propto T\)：镜子吸热熵流正比于 \((1-\beta)T_1\)，放热熵流正比于 \((1+\beta)T_2 = (1-\beta)T_1\)，总熵产生严格为零，确实对应可逆卡诺循环！）
   因此，在实验室参考系 \(S\) 中，热机工作在高温热源 \(T_1\) 与低温热源 \(T_2 = \frac{c-v}{c+v}T_1\) 之间，效率为：
   \[
   \eta = 1 - \frac{T_2}{T_1} = 1 - \frac{c - v}{c + v} = \frac{2v}{c + v}.
   \]
   与第（1）问从纯光子动力学求得的结果完美一致（体现了功与热量随惯性系变换而改变，效率并非洛伦兹不变量）。

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解全3问与官方解答（`page-23.jpg`–`page-25.jpg`）在思想路径、物理证明和最终结论上**完全一致**！尤其是第（1）问，我们在盲解过程中既验证了单光子两次多普勒频移法，也直接采用了全能量动量守恒法，后者恰与官方解答 ①–④ 式如出一辙。
- **官方排版细微印迹**：`page-24.jpg` ⑫–⑯式右侧残留了两处评分细则字符“（1 分）”、“（2 分）”。
- **核心难点与典型易错点**：
  - 难点1：黑体辐射谱在惯性系之间的变换证明——关键抓手是**“总光子数不变”**和**“总波峰数（相位 \(\nu\mathrm{d}t\)）不变”**两条洛伦兹协变律，两者一除立得 \(\varphi(\nu)/\nu\) 为相对论不变量！
  - 难点2：第（1）问明确 \(\varepsilon_1\) 的物理口径是**单位时间内实际撞击到运动镜面上的光子能量**（而非静止黑体源发出的全部光子能量），这正是其能够与热力学中“热机从高温热源实际吸收的热量 \(Q_1\)”严格等同的前提。
  - 易错点1：套用低速（非相对论）多普勒频移公式 \(\nu' = \nu(1 - v/c)\) 代替精确相对论公式 \(\nu\sqrt{\frac{c-v}{c+v}}\)，这在（2）（3）问中会错算出 \(T_2 = (1 - \frac{v}{c})^2 T_1\) 进而破坏卡诺效率 \(\frac{2v}{c+v}\) 的精确一致（只有在 \(v \ll c\) 一阶展开时才恰好都约等于 \(2v/c\)）。
  - 易错点2：误以为效率 \(\eta\) 和温度一样具有某类固定不变性，不敢在第（2）问得出 \(\eta' = 0\) 而第（3）问得出 \(\eta = \frac{2v}{c+v}\)。
- **教练总结与迁移建议**：本题堪称整套第35届决赛最具审美价值的压轴题！它把相对论多普勒效应（一次是静止源 \(\to\) 运动镜，二次是运动镜 \(\to\) 静止观测者）、黑体辐射协变性与可逆卡诺循环无缝融为一体。记住**“能流密度谱 \(\varphi(\nu)/\nu\) 是洛伦兹不变量（对应光子相空间占据数不变）”**，一切黑体辐射的洛伦兹变换都能在三行内精准完成。
