# Batch 18: PLANCKS 2021 UK/IE Preliminary & International Final 教学解析笔记

本文件收录 **PLANCKS 2021 英国与爱尔兰初赛（Kent 承办，共 10 题）** 与 **PLANCKS 2021 国际决赛（Porto 承办，共 12 题）** 共 22 道赛题的完整两阶段独立盲解、交叉验证/官方解答比对与竞赛教学拆解。

---

## 第一部分：PLANCKS 2021 英国与爱尔兰初赛 (Preliminary, Q1–Q10)

---

### 1. `plancks-2021-preliminary-problem-slice-q1` — Prologue – Where Our Host Discovers Gravity

- **难度分级**：D2
- **核心物理模型**：二体万有引力径向落体与退化开普勒轨道
- **教学标签**：`二体问题` `约化质量` `万有引力` `退化椭圆轨道` `开普勒第三定律`

#### 一、题目概述与拆解
两个质量均为 \(m_1 = m_2 = m = 1\text{ kg}\) 的质点从相距 \(r_0 = 1\text{ m}\) 处静止释放，仅在相互万有引力 \(F = -G m^2 / r^2\) 作用下相向运动，经过 \(t_c = 26\text{ h } 42\text{ min} = 96120\text{ s}\) 在中点相遇，求引力常数 \(G\)。
1. **约化质量转化**：建立相对坐标 \(r = x_2 - x_1\)，约化质量 \(\mu = \frac{m_1 m_2}{m_1 + m_2} = \frac{m}{2}\)，运动方程为 \(\mu \ddot{r} = -\frac{G m^2}{r^2} \implies \ddot{r} = -\frac{2Gm}{r^2}\)。
2. **退化开普勒第三定律法**：初速为零的二体纯径向引力运动可视为偏心率 \(e \to 1\)、远日点距离为 \(r_0\)、近日点距离为 \(0\) 的退化椭圆轨道，其半长轴为 \(a = \frac{r_0}{2}\)。由二体开普勒第三定律：
   \[
   T = 2\pi \sqrt{\frac{a^3}{G(m_1 + m_2)}} = 2\pi \sqrt{\frac{(r_0/2)^3}{2Gm}} = \frac{\pi}{2}\sqrt{\frac{r_0^3}{Gm}}.
   \]
   从远日点静止落到引力中心所需碰撞时间恰为半个周期：
   \[
   t_c = \frac{T}{2} = \frac{\pi}{4}\sqrt{\frac{r_0^3}{Gm}}.
   \]
3. **能量积分直接验证**：由机械能守恒 \(\frac{1}{2}\mu \dot{r}^2 - \frac{Gm^2}{r} = -\frac{Gm^2}{r_0}\)，得 \(\frac{dr}{dt} = -\sqrt{4Gm\left(\frac{1}{r} - \frac{1}{r_0}\right)}\)。令 \(r = r_0 \cos^2\theta\)（\(\theta\) 从 \(0\) 到 \(\pi/2\)），积分得：
   \[
   t_c = \sqrt{\frac{r_0^3}{4Gm}}\int_0^{\pi/2} 2\cos^2\theta\,d\theta = \frac{\pi}{4}\sqrt{\frac{r_0^3}{Gm}}.
   \]
4. **数值计算**：反解 \(G\) 并代入 \(r_0 = 1\text{ m},\ m = 1\text{ kg},\ t_c = 96120\text{ s}\)：
   \[
   G = \frac{\pi^2 r_0^3}{16 m t_c^2} = \frac{\pi^2}{16 \times (96120)^2} \approx 6.678 \times 10^{-11}\text{ m}^3\,\text{kg}^{-1}\,\text{s}^{-2}.
   \]

#### 二、盲解心得与交叉验证
- **盲解直觉**：考场上直接用退化开普勒椭圆半周期公式 \(t_c = T/2\) 可免去三角换元积分，十秒内得出解析式。
- **难点与易错点**：
  - **易错点 1**：漏掉约化质量因子 \(1/2\)，误以为单个质点向固定中心坠落（或把 \(\ddot{r}\) 写成 \(-Gm/r^2\)），导致算出的 \(G\) 偏大一倍。
  - **易错点 2**：套用开普勒第三定律时误把 \(a = r_0\) 代入（正确半长轴应为 \(a = r_0 / 2\)）。

---

### 2. `plancks-2021-preliminary-problem-slice-q2` — The First Guests Arrive

- **难度分级**：D2
- **核心物理模型**：流体静力学悖论（帕斯卡桶）与斜面刚体纯滚动
- **教学标签**：`流体静力学悖论` `帕斯卡定律` `圆台体积积分` `刚体纯滚动` `转动惯量`

#### 一、题目概述与拆解
- **(a) 流体静力学悖论**：三个底面积均为 \(A\) 的圆形酒杯，杯壁分别以与竖直方向夹角 \(\theta\) 外倾、竖直（参考体积 \(V_2 = V\)）、以夹角 \(\theta\) 内倾。要求杯底受到的总积分液体压力 \(\int_{\text{base}} P\,dA\) 相等，求 \(V_1\) 和 \(V_3\)。
  - 杯底水平，压强处处为 \(P = \rho g h\)，故杯底总压力 \(F = \rho g h A\) 仅取决于液面高度 \(h\)！因此三个酒杯必须倒入**相同高度** \(h = \frac{V}{A}\) 的液体（Isaac 正确）。
  - 设底面半径为 \(R_0 = \sqrt{A/\pi}\)，在高度 \(z \in [0, h]\) 处，截面半径为 \(R_{1,3}(z) = R_0 \pm z\tan\theta\)。积分求体积：
    \[
    V_{1,3} = \int_0^h \pi (R_0 \pm z\tan\theta)^2\,dz = \pi R_0^2 h \pm \pi R_0 h^2 \tan\theta + \frac{1}{3}\pi h^3 \tan^2\theta.
    \]
    消去 \(R_0 = \sqrt{A/\pi}\) 和 \(h = V/A\)，得到：
    \[
    V_1 = V + \frac{\sqrt{\pi} V^2}{A^{3/2}}\tan\theta + \frac{\pi V^3}{3 A^3}\tan^2\theta, \qquad
    V_3 = V - \frac{\sqrt{\pi} V^2}{A^{3/2}}\tan\theta + \frac{\pi V^3}{3 A^3}\tan^2\theta.
    \]
- **(b) 豆罐头斜面纯滚动**：倾角为 \(\alpha\) 的斜面上，实心均匀圆柱（满罐，\(I_{\text{full}} = \frac{1}{2}Mr^2\)）与质量集中在边缘的薄圆筒（空罐，\(I_{\text{empty}} = Mr^2\)）无滑滚下。
  - 由能量守恒或牛顿-欧拉方程 \(M a = M g \sin\alpha - f,\ I(a/r) = f r\)，得：
    \[
    a = \frac{g\sin\alpha}{1 + I/(Mr^2)} \implies a_{\text{full}} = \frac{2}{3}g\sin\alpha, \qquad a_{\text{empty}} = \frac{1}{2}g\sin\alpha.
    \]
    因 \(\frac{2}{3} > \frac{1}{2}\)，满罐加速度更大、滚得更快。

#### 二、盲解心得与交叉验证
- **物理洞察**：为什么 \(V_1 > V > V_3\) 而杯底总压力相同？因为外倾杯壁对液体有向上的法向支撑分力，承担了多余液体的重量；内倾杯壁对液体有向下的压力分量，补足了缺失液体的重量。
- **难点与易错点**：
  - **易错点 1**：误将杯底总压力等同于杯中液体总重量 \(\rho g V_i\)。
  - **易错点 2**：积分 \(R(z)^2\) 时漏写二次项 \(\frac{\pi V^3}{3A^3}\tan^2\theta\)。

---

### 3. `plancks-2021-preliminary-problem-slice-q3` — Coming or Going?

- **难度分级**：D3
- **核心物理模型**：双平面波叠加与量子回流效应 (Quantum Backflow)
- **教学标签**：`量子力学` `概率流密度` `平面波叠加` `量子干涉` `量子回流效应`

#### 一、题目概述与拆解
给定一维自由粒子薛定谔方程的两个正动量（\(p_1, p_2 > 0\)）平面波叠加态 \(\psi(x,t) = A e^{i\theta_1(x,t)} + B e^{i\theta_2(x,t)}\)，其中 \(A, B > 0\)，\(\theta_n(x,t) = \frac{1}{\hbar}\left(p_n x - \frac{p_n^2 t}{2m}\right) + \gamma\)。
- **(a) 概率流密度计算**：
  利用 \(\frac{\partial \psi}{\partial x} = \frac{i}{\hbar}\left(p_1 A e^{i\theta_1} + p_2 B e^{i\theta_2}\right)\)，代入 \(j(x,t) = \frac{\hbar}{m}\operatorname{Im}\left(\psi^* \frac{\partial \psi}{\partial x}\right)\)：
  \[
  j(x,t) = \frac{1}{m}\left[ p_1 A^2 + p_2 B^2 + A B (p_1 + p_2)\cos\big(\theta_1(x,t) - \theta_2(x,t)\big) \right].
  \]
- **(b) 反常（Bizarre）现象分析**：
  当两束平面波发生相消干涉，即 \(\cos(\theta_1 - \theta_2) = -1\) 时，概率流取极小值：
  \[
  j_{\min} = \frac{1}{m}\left( p_1 A^2 + p_2 B^2 - A B (p_1 + p_2) \right) = \frac{1}{m}(A - B)(p_1 A - p_2 B).
  \]
  若 \(A > B\) 且 \(p_1 A < p_2 B\)，则 \(A - B > 0\) 而 \(p_1 A - p_2 B < 0\)，故 \(j_{\min} < 0\)！尽管叠加态仅包含向右传播（\(p_1, p_2 > 0\)）的动量本征态，但在相消干涉区域附近，局域概率流却**向左（负方向）倒流**！
- **(c) 物理起源解释**：
  这种现象称为**量子回流（Quantum Backflow）**。其根源在于量子相干干涉与位置-动量算符的非对易性：在相消干涉波谷处，振幅较大但动量较小的波 \(A e^{i\theta_1}\) 与振幅较小但动量较大的波 \(B e^{i\theta_2}\) 叠加，导致总波函数局域相位梯度 \(\partial_x \arg\psi\) 变为负值（类似光学中的超振荡现象）。动量本征值为正仅要求空间平均流 \(\langle j \rangle = \frac{p_1 A^2 + p_2 B^2}{m} > 0\)，并不保证局域流算符处处正定。
- **(d) 多平面波波包的推广**：
  对于由连续多个正动量平面波组成的归一化波包，量子回流在局域时空内依然可以发生（在给定点处出现负概率流，使右侧总概率在有限时间段内减少，最大回流概率受限于无量纲 Bracken–Melloy 常数 \(c_{\text{bm}} \approx 0.03845\)）；但由于自由粒子色散关系 \(\omega(k) = \hbar k^2 / (2m)\) 非线性，不同动量分量群速度不同，波包随时间演化解聚色散，回流干涉条纹只是暂态局域效应，且全空间积分的总平均动量始终严格为正。

#### 二、盲解心得与交叉验证
- **因式分解技巧**：看到题设条件 \(A > B\) 且 \(p_1 A < p_2 B\)，立刻提示我们将 \(j_{\min}\) 分组分解为 \((A-B)(p_1 A - p_2 B)/m\)，瞬间揭示符号反转机制。

---

### 4. `plancks-2021-preliminary-problem-slice-q4` — Electrostatics by Conformal Mapping

- **难度分级**：D4
- **核心物理模型**：二维静电场的保角变换法与抛物面尖端场强增强
- **教学标签**：`静电场` `镜像法` `拉普拉斯方程` `保角变换` `尖端放电效应`

#### 一、题目概述与拆解
线电荷密度为 \(q\) 的无限长直导线平行于 \(z\) 轴放置，导体边界接地（\(V = 0\)）。
- **(a) 导体平面前的电势 \(V(x,y)\)**：
  设导体平面为 \(x = 0\)，导线位于 \((d, 0)\)（复坐标 \(z = x + iy = d\)）。由镜像法，在 \((-d, 0)\) 处放置镜像线电荷 \(-q\)，二维电势为：
  \[
  V(x,y) = \frac{q}{2\pi\varepsilon_0}\ln\left|\frac{z + d}{z - d}\right| = \frac{q}{4\pi\varepsilon_0}\ln\frac{(x+d)^2 + y^2}{(x-d)^2 + y^2}.
  \]
- **(b) 抛物柱面导体 \(x = \frac{y^2}{4\alpha^2}\) 的保角变换与电势**：
  抛物线 \(x = \frac{y^2}{4\alpha^2}\) 顶点在原点 \(z = 0\)，焦点在 \(z = \alpha^2\)。寻找解析映射 \(w(z) = u + iv\) 将抛物线映射为虚轴 \(u = 0\)，且顶点 \(z = 0\) 映射为 \(w = 0\)：
  令 \(z = \alpha^2 - (w + \alpha)^2\)，则当 \(u = 0\)（即 \(w = iv\)）时，\(x + iy = \alpha^2 - (\alpha + iv)^2 = v^2 - 2i\alpha v\)，消去 \(v\) 恰满足 \(x = \frac{y^2}{4\alpha^2}\)！反解得保角变换：
  - **情形 1（导线位于抛物面外侧凸尖端前方 \(z_0 = -d\)，对应避雷针尖端模型）**：
    \[
    w(z) = \sqrt{\alpha^2 - z} - \alpha, \qquad w_0 = w(-d) = \sqrt{\alpha^2 + d} - \alpha > 0.
    \]
    代入半平面电势公式得：
    \[
    W(x,y) = \frac{q}{2\pi\varepsilon_0}\ln\left|\frac{w(z) + w_0}{w(z) - w_0}\right| = \frac{q}{2\pi\varepsilon_0}\ln\left|\frac{\sqrt{\alpha^2 - z} + \sqrt{\alpha^2 + d} - 2\alpha}{\sqrt{\alpha^2 - z} - \sqrt{\alpha^2 + d}}\right|.
    \]
  - **情形 2（导线位于抛物面凹腔内部 \(z_0 = +d\)，反射镜模型）**：
    取 \(w(z) = \alpha - \sqrt{\alpha^2 - z}\)（或对 \(d > \alpha^2\) 沿虚轴对称处理），像平面源点为 \(w_0 = \alpha - \sqrt{\alpha^2 - d}\)，电势表达式仅需将上式中的 \(\sqrt{\alpha^2 + d}\) 替换为 \(\sqrt{\alpha^2 - d}\)。
- **(c) 抛物面顶点处的电场增强因子**：
  在平面镜情形下，导线正对点（原点）的场强为 \(E_{\text{plane}} = \left|\frac{\partial V}{\partial x}\right|_{z=0} = \frac{q}{\pi\varepsilon_0 d}\)。
  在抛物面情形下，利用保角变换下场强的缩放定律 \(E_{\text{tip}} = E_w(0)\left|\frac{dw}{dz}\right|_{z=0}\)，其中 \(E_w(0) = \frac{q}{\pi\varepsilon_0 w_0}\)，且 \(\left|\frac{dw}{dz}\right|_{z=0} = \left|-\frac{1}{2\sqrt{\alpha^2 - z}}\right|_{z=0} = \frac{1}{2\alpha}\)。
  因此，对于外侧凸尖端（\(z_0 = -d\)），场强增强因子为：
  \[
  \eta = \frac{E_{\text{tip}}}{E_{\text{plane}}} = \frac{d}{2\alpha w_0} = \frac{d}{2\alpha\left(\sqrt{\alpha^2 + d} - \alpha\right)} = \frac{1}{2}\left(1 + \sqrt{1 + \frac{d}{\alpha^2}}\right) > 1.
  \]
  （若导线置于凹腔内侧 \(z_0 = +d\)，则顶点场强之比为 \(\frac{1}{2}\left(1 + \sqrt{1 - \frac{d}{\alpha^2}}\right) < 1\)，表现为凹腔屏蔽衰减。）

#### 二、盲解心得与交叉验证
- **极限验证**：当 \(\alpha \to \infty\) 时，抛物面退化为平面 \(x = 0\)，增强因子 \(\eta = \frac{1}{2}\left(1 + \sqrt{1 + d/\alpha^2}\right) \to 1\)；当曲率半径极小（\(\alpha^2 \ll d\)）时，\(\eta \approx \frac{\sqrt{d}}{2\alpha} \gg 1\)，定量给出了尖端曲率半径越小、表面感应电荷面密度与场强越集中的经典结论。

---

### 5. `plancks-2021-preliminary-problem-slice-q5` — Parastatistics

- **难度分级**：D2
- **核心物理模型**：广义量子统计（巨正则系综与最大占据数为 2 的 Gentile 副统计）
- **教学标签**：`统计物理` `巨正则系综` `配分函数` `副统计` `玻色与费米分布`

#### 一、题目概述与拆解
假设某种假想全同粒子在每个单粒子量子态（给定全套量子数，能量为 \(\epsilon\)）上最多可容纳 \(2\) 个粒子（即占据数 \(n \in \{0, 1, 2\}\)）。
- **(a) 推导热力学平衡分布函数 \(n(\epsilon)\)**：
  记 \(\beta = \frac{1}{k_B T}\)，令单态玻尔兹曼因子为 \(x = e^{-\beta(\epsilon - \mu)}\)。单量子态的巨配分函数为：
  \[
  \mathcal{Z}_1 = \sum_{n=0}^{2} e^{-n\beta(\epsilon - \mu)} = 1 + x + x^2.
  \]
  因此该量子态的平均粒子占据数为：
  \[
  n(\epsilon) = \frac{\sum_{n=0}^{2} n e^{-n\beta(\epsilon - \mu)}}{\mathcal{Z}_1} = \frac{x + 2x^2}{1 + x + x^2} = \frac{e^{(\epsilon - \mu)/(k_B T)} + 2}{e^{2(\epsilon - \mu)/(k_B T)} + e^{(\epsilon - \mu)/(k_B T)} + 1}.
  \]
- **(b) 高温极限（\(T \to \infty\)）及其物理性质**：
  - 若固定化学势 \(\mu\) 令 \(T \to \infty\)（即 \(\beta(\epsilon - \mu) \to 0,\ x \to 1\)），则 \(n(\epsilon) \to \frac{1 + 2}{1 + 1 + 1} = 1\)，此时 \(n = 0, 1, 2\) 三种占据状态等概率出现（各占 \(1/3\)）。
  - 若固定系统的总粒子数 \(N\) 处于高温经典稀疏极限，则化学势 \(\mu \to -\infty\)，逸度 \(z = e^{\beta\mu} \ll 1\)，使得 \(e^{\beta(\epsilon - \mu)} \gg 1\)（即 \(x \ll 1\)）。此时忽略高阶项 \(x^2\)，分布函数退化为经典的麦克斯韦-玻尔兹曼分布 \(n(\epsilon) \approx e^{-(\epsilon - \mu)/(k_B T)}\)，量子简并效应消失。
- **(c) 低温极限（\(T \to 0\)）及其物理性质**：
  当 \(T \to 0\)（\(\beta \to \infty\)）时，设零温化学势（费米能）为 \(\mu(0) = \epsilon_F\)：
  - 当 \(\epsilon < \epsilon_F\) 时，\(e^{\beta(\epsilon - \mu)} \to 0\)，故 \(n(\epsilon) \to 2\)（费米面以下所有量子态均被双占据填满）；
  - 当 \(\epsilon > \epsilon_F\) 时，\(e^{\beta(\epsilon - \mu)} \to \infty\)，故 \(n(\epsilon) \to 0\)（费米面以上完全空置）；
  - 在 \(\epsilon = \epsilon_F\) 处，\(n(\epsilon_F) = 1\)。
  因此零温分布呈高度为 \(2\) 的阶跃函数，既不会像玻色子那样发生宏观粒子凝聚到单一基态的 BEC 现象，又比普通无自旋费米子具有翻倍的相空间容纳密度（费米能量低于同粒子数密度的费米子系统）。

#### 二、盲解心得与交叉验证
- **与自旋简并的本质区别**：切忌将本题结果写成 \(\frac{2}{e^{\beta(\epsilon - \mu)} + 1}\)！后者对应每个能量本征值下有两个独立自旋量子态、每个态最多容纳 1 个费米子（单能级巨配分函数为 \((1+x)^2 = 1 + 2x + x^2\)，单占据权重为 2）；而本题是同一套量子数态最多容纳 2 个不可区分粒子（巨配分函数为 \(1 + x + x^2\)，单占据权重为 1）。

---

### 6. `plancks-2021-preliminary-problem-slice-q6` — Condensed Matter

- **难度分级**：D3
- **核心物理模型**：任意维幂律色散凝聚态系统的态密度与基态平均能量
- **教学标签**：`固体物理` `色散关系` `态密度` `费米球积分` `石墨烯与维数推广`

#### 一、题目概述与拆解
二维材料的电子色散关系为 \(\epsilon(\mathbf{k}) = \epsilon_F \left(\frac{|\mathbf{k}|}{k_F}\right)^\alpha\)（\(\alpha > 0\)，其中 \(\alpha = 2\) 对应自由电子，\(\alpha = 1\) 对应石墨烯线性狄拉克锥）。
- **(a) 二维态密度 \(g(\epsilon)\)**：
  设二维样品面积为 \(A\)，自旋（及谷）简并度为 \(g_s\)（对普通电子 \(g_s = 2\)）。二维 \(\mathbf{k}\) 空间中半径 \(k\) 以内的量子态总数为：
  \[
  N(k) = g_s \frac{A}{(2\pi)^2}\left(\pi k^2\right) = \frac{g_s A k^2}{4\pi}.
  \]
  由色散关系反解 \(k(\epsilon) = k_F \left(\frac{\epsilon}{\epsilon_F}\right)^{1/\alpha}\)，代入得能量低于 \(\epsilon\) 的累积量子态数：
  \[
  N(\epsilon) = \frac{g_s A k_F^2}{4\pi}\left(\frac{\epsilon}{\epsilon_F}\right)^{2/\alpha} = N \left(\frac{\epsilon}{\epsilon_F}\right)^{2/\alpha},
  \]
  其中 \(N = N(\epsilon_F) = \frac{g_s A k_F^2}{4\pi}\) 为基态总电子数。对 \(\epsilon\) 求导即得二维态密度：
  \[
  g(\epsilon) = \frac{dN}{d\epsilon} = \frac{g_s A k_F^2}{2\pi \alpha \epsilon_F}\left(\frac{\epsilon}{\epsilon_F}\right)^{\frac{2}{\alpha}-1} = \frac{2N}{\alpha \epsilon_F}\left(\frac{\epsilon}{\epsilon_F}\right)^{\frac{2}{\alpha}-1}.
  \]
- **(b) 二维基态单粒子平均能量 \(E/N\)**：
  在零温基态下，电子填满 \(0 \le \epsilon \le \epsilon_F\) 的所有态，单粒子平均能量为：
  \[
  \frac{E}{N} = \frac{\int_0^{\epsilon_F} \epsilon\, g(\epsilon)\,d\epsilon}{\int_0^{\epsilon_F} g(\epsilon)\,d\epsilon} = \frac{\int_0^{\epsilon_F} \epsilon^{\frac{2}{\alpha}}\,d\epsilon}{\epsilon_F \int_0^{\epsilon_F} \epsilon^{\frac{2}{\alpha}-1}\,d\epsilon} = \frac{\frac{1}{2/\alpha + 1}}{\frac{1}{2/\alpha}}\epsilon_F = \frac{2}{2 + \alpha}\epsilon_F.
  \]
- **(c) 推广至 \(d\) 维材料（\(d\) 不必为整数）**：
  在 \(d\) 维 \(\mathbf{k}\) 空间中，半径为 \(k\) 的超球体积正比于 \(k^d\)（精确体积为 \(V_d(k) = \frac{\pi^{d/2}}{\Gamma(d/2+1)}k^d\)）。因此累积态数满足标度律 \(N_d(\epsilon) \propto k(\epsilon)^d \propto \epsilon^{d/\alpha}\)，态密度满足：
  \[
  g_d(\epsilon) = \frac{dN_d}{d\epsilon} = \frac{d}{\alpha \epsilon_F} N \left(\frac{\epsilon}{\epsilon_F}\right)^{\frac{d}{\alpha}-1}.
  \]
  于是 \(d\) 维基态单粒子平均能量为：
  \[
  \frac{E}{N} = \frac{\int_0^{\epsilon_F} \epsilon \cdot \epsilon^{\frac{d}{\alpha}-1}\,d\epsilon}{\int_0^{\epsilon_F} \epsilon^{\frac{d}{\alpha}-1}\,d\epsilon} = \frac{d}{d + \alpha}\epsilon_F.
  \]

#### 二、盲解心得与交叉验证
- **标度律秒杀技巧**：计算 \(E/N\) 时无需纠结 \(d\) 维球体积前置系数 \(\pi^{d/2}/\Gamma(d/2+1)\) 与简并度 \(g_s\)，直接利用 \(g_d(\epsilon) \propto \epsilon^{d/\alpha - 1}\) 即可一步算出积分比 \(\frac{d/\alpha}{d/\alpha + 1} = \frac{d}{d + \alpha}\)。当 \(d=3, \alpha=2\) 时给出著名的三维费米气体结论 \(E/N = \frac{3}{5}\epsilon_F\)。

---

### 7. `plancks-2021-preliminary-problem-slice-q7` — A Rotating Glass of Mead

- **难度分级**：D1
- **核心物理模型**：旋转流体的自由液面平衡方程（牛顿水桶旋转抛物面）
- **教学标签**：`流体力学` `非惯性系` `离心惯性力` `等势面` `旋转抛物面`

#### 一、题目概述与拆解
轴对称开口容器盛有液体，绕竖直对称轴（\(z\) 轴）以角速度 \(\omega\) 稳定旋转，取转轴处液面高度 \(z(0) = 0\)，求自由液面剖面曲线方程 \(z(r)\)。
1. **共转系有效力场平衡**：在随容器以角速度 \(\omega\) 共转的非惯性系中，液体静止。距轴 \(r\) 处流体微元受竖直向下的重力加速度 \(-g\hat{z}\) 与水平向外的离心惯性加速度 \(+\omega^2 r\hat{r}\)。
2. **自由液面斜率方程**：液体自由表面必与合等效重力场 \(\mathbf{g}_{\text{eff}} = \omega^2 r\hat{r} - g\hat{z}\) 处处正交，故切线斜率满足：
   \[
   \frac{dz}{dr} = \frac{\omega^2 r}{g}.
   \]
3. **积分求解**：结合边界条件 \(z(0) = 0\)，积分得旋转抛物面方程：
   \[
   z(r) = \frac{\omega^2 r^2}{2g}.
   \]

#### 二、盲解心得与交叉验证
- **历史彩蛋**：题干说「Isaac 觉得他以前见过这个形状」，既指牛顿《自然哲学的数学原理》中论证绝对空间的**牛顿水桶实验**，也指牛顿发明的**抛物面反射望远镜**（旋转水银面即可自然形成焦距 \(f = \frac{g}{2\omega^2}\) 的理想抛物面反射镜）。

---

### 8. `plancks-2021-preliminary-problem-slice-q8` — A Harmonious Synthesiser

- **难度分级**：D3
- **核心物理模型**：双频 LC 谐振合成器电路设计与十二平均律纯五度调谐
- **教学标签**：`LC谐振电路` `耦合振荡` `本征频率` `十二平均律` `纯五度音程`

#### 一、题目概述与拆解
现有两个电感（\(L\) 和 \(\beta L\)）与两个电容（\(C\) 和 \(\alpha C\)，调谐参数 \(\alpha, \beta \in [0, 100]\)）。
- **(a) 双频谐振电路拓扑设计与论证**：
  - 若将四个元件简单无分支地串联成一个单环，总电感为 \((1+\beta)L\)，总串联电容为 \(\frac{\alpha}{1+\alpha}C\)，系统仅有一个独立振荡自由度和单一非零频率。要同时产生两个谐振频率，电路必须包含**两个独立的 LC 储能振荡自由度**（二阶双谐振网络）：
  - **拓扑方案一（双并联 LC 谐振槽串联 / 8 字形双环路）**：将 \((L \parallel C)\) 组成的并联 LC 谐振回路与 \((\beta L \parallel \alpha C)\) 组成的并联 LC 谐振回路串联。第一组谐振回路以固有频率 \(\omega_1 = \frac{1}{\sqrt{LC}}\) 振荡，第二组以固有频率 \(\omega_2 = \frac{1}{\sqrt{\alpha\beta LC}}\) 振荡，两端总电压 \(V(t) = V_1(t) + V_2(t) = A_1\cos(\omega_1 t + \phi_1) + A_2\cos(\omega_2 t + \phi_2)\) 即为两个音调的叠加。
  - **拓扑方案二（双网孔耦合 LC 电路 / Foster 网络）**：在主串联回路 \((L, C)\) 的电容 \(C\) 两端并联串联支路 \((\beta L, \alpha C)\)。由总回路阻抗为零：
    \[
    i\omega L + \frac{1}{i\omega C + \frac{1}{i\omega\beta L + \frac{1}{i\omega\alpha C}}} = 0 \implies \alpha\beta (\omega^2 LC)^2 - (\alpha + \alpha\beta + 1)(\omega^2 LC) + 1 = 0.
    \]
    该二次方程判别式 \(\Delta = (\alpha + \alpha\beta + 1)^2 - 4\alpha\beta = (\alpha - 1)^2 + \alpha\beta(\alpha\beta + 2\alpha + 2) > 0\) 恒成立，故必然同时存在两个不同的正本征频率 \(\omega_1, \omega_2\)。
- **(b) 十二平均律纯五度（相差 7 个半音）的参数选择**：
  - 在十二平均律中，相邻半音频率之比为常数 \(r\)，且 \(12\) 个半音构成一个八度（频率翻倍 \(r^{12} = 2\)），故 \(r = 2^{1/12}\)。
  - 纯五度跨越 \(7\) 个半音，其高低音频率之比为：
    \[
    \frac{f_2}{f_1} = \frac{\omega_2}{\omega_1} = 2^{7/12} \approx 1.498307 \quad (\text{极接近五度相生律的 } 3/2 = 1.5).
    \]
  - **对应参数 \((\alpha, \beta)\)**：
    - 对**方案一**，\(\frac{\omega_1}{\omega_2} = \sqrt{\alpha\beta} = 2^{7/12}\)（或 \(2^{-7/12}\)），故只需满足 \(\alpha\beta = 2^{7/6} \approx 2.2449\)（或 \(\alpha\beta = 2^{-7/6} \approx 0.4454\)）。例如取：
      \[
      \alpha = 1, \qquad \beta = 2^{7/6} \approx 2.245 \quad (\text{或 } \alpha = 1,\ \beta = 2^{-7/6} \approx 0.4454).
      \]
    - 对**方案二**，令两根之比 \(\frac{x_2}{x_1} = \left(\frac{\omega_2}{\omega_1}\right)^2 = 2^{7/6} \equiv \kappa\)。由韦达定理 \(\frac{(x_1 + x_2)^2}{x_1 x_2} = \frac{(\alpha + \alpha\beta + 1)^2}{\alpha\beta} = \frac{(\kappa + 1)^2}{\kappa} \approx 4.690\)。若固定 \(\alpha = 1\)，则 \(\frac{(\beta + 2)^2}{\beta} \approx 4.690\)，解得 \(\beta \approx 2.493\)（注意当 \(\beta > 0\) 时 \((\beta+2)^2/\beta \ge 8\)，故对方案二需调节 \(\alpha < 1\)，例如取 \(\alpha = 0.25,\ \beta = 1\) 时可调谐出目标比值；具体而言，对任意比值 \(\kappa\)，最小和根比出现在 \(\alpha\beta = 1\) 时，此时 \(\frac{(\alpha+2)^2}{1} = \frac{(\kappa+1)^2}{\kappa} = 4.690 \implies \alpha = \sqrt{4.690} - 2 \approx 0.1657,\ \beta = 1/\alpha \approx 6.036\)！）。

#### 二、盲解心得与交叉验证
- **对方案二的极值检验**：在耦合回路方案二中，韦达定理给出 \(\frac{x_1}{x_2} + \frac{x_2}{x_1} + 2 = \frac{(\alpha + \alpha\beta + 1)^2}{\alpha\beta}\)。若误取 \(\alpha = 1\)，左端对于纯五度 \(\kappa = 2^{7/6} \approx 2.245\) 要求 \(2.245 + 0.445 + 2 = 4.69\)，而右端 \(\frac{(\beta+2)^2}{\beta} \ge 8\) 无实数解（因为耦合劈裂下限限制了两模接近程度）！只有取 \(\alpha \approx 0.166,\ \beta \approx 6.04\) 才能在耦合单网孔中实现纯五度，这也说明命题人预设的标准简明答案正是方案一（\(\alpha\beta = 2^{7/6} \approx 2.245\) 或 \(2^{-7/6} \approx 0.445\)）！

---

### 9. `plancks-2021-preliminary-problem-slice-q9` — Bernoulli’s Airship

- **难度分级**：D3
- **核心物理模型**：刚性飞艇阿基米德净升力、伯努利小孔泄流与真空球壳屈曲极限
- **教学标签**：`阿基米德浮力` `伯努利方程` `气体泄流与可燃性` `真空飞艇` `薄壳屈曲力学`

#### 一、题目概述与拆解
已知英国 R101 飞艇参数：全长 \(L = 236.8\text{ m}\)，最大直径 \(D = 40.5\text{ m}\)，高 \(42.67\text{ m}\)，空重 \(m_{\text{empty}} = 116,857\text{ kg}\)；密度 \(\rho_{\text{air}} = 1.29\text{ kg/m}^3\)，\(\rho_{\text{H}} = 0.0899\text{ kg/m}^3\)，\(\rho_{\text{He}} = 0.179\text{ kg/m}^3\)。
- **(a) 氢气的有效升力（Useful Lift）**：
  - **体积估算**：
    - 模型 A（旋转椭球近似）：\(V_{\text{ell}} = \frac{\pi}{6} L D^2 = \frac{\pi}{6}(236.8)(40.5)^2 \approx 2.034 \times 10^5\text{ m}^3\)。
    - 模型 B（圆柱近似）：\(V_{\text{cyl}} = \frac{\pi}{4} L D^2 \approx 3.051 \times 10^5\text{ m}^3\)（注：历史上 R101 内部独立气囊的实际总容积约为 \(1.56 \times 10^5\text{ m}^3\)，也可由题图中间圆台分段累加估算为 \(\sim 2.0 \times 10^5\text{ m}^3\)）。
  - **升力计算**：单位体积氢气的毛升力密度为 \(\Delta \rho_{\text{H}} = \rho_{\text{air}} - \rho_{\text{H}} = 1.29 - 0.0899 = 1.2001\text{ kg/m}^3\)。
    扣除空重 \(m_{\text{empty}}\) 后，**有效升力（净载重质量与力）**通用公式为：
    \[
    m_{\text{useful, H}} = (\rho_{\text{air}} - \rho_{\text{H}})V - m_{\text{empty}}, \qquad F_{\text{useful, H}} = m_{\text{useful, H}} g.
    \]
    - 按椭球模型（\(V \approx 2.034 \times 10^5\text{ m}^3\)）：毛升力质量 \(244,100\text{ kg}\)，有效升力质量 \(m_{\text{useful}} \approx 127,200\text{ kg}\)（有效升力 \(F_{\text{useful}} \approx 1.25\text{ MN}\)）；
    - 按历史实际气囊体积（\(V \approx 1.56 \times 10^5\text{ m}^3\)）：毛升力质量 \(187,200\text{ kg}\)，有效升力质量 \(m_{\text{useful}} \approx 70,300\text{ kg}\)（\(F_{\text{useful}} \approx 0.69\text{ MN}\)）。
- **(b) 一战防空气球（系留高度 1500 m）为何难被普通枪弹击落**：
  1. **压差极小与伯努利泄流极慢**：防空气球为非刚性软式气球，内部气压与外部大气压几乎相等，最大超压仅来源于气球高度 \(H \sim 30\text{ m}\) 产生的浮力静水压差 \(\Delta P \approx (\rho_{\text{air}} - \rho_{\text{H}})g H \approx 1.2 \times 9.81 \times 30 \approx 350\text{ Pa}\)。由**伯努利方程**，氢气从弹孔逸出的流速为：
     \[
     v = \sqrt{\frac{2\Delta P}{\rho_{\text{H}}}} \approx \sqrt{\frac{2 \times 350}{0.0899}} \approx 88\text{ m/s}.
     \]
     一发 \(7.7\text{ mm}\) 步枪/机枪弹孔面积仅 \(A_{\text{hole}} = \frac{\pi}{4}d^2 \approx 4.65 \times 10^{-5}\text{ m}^2\)，单孔体积泄流率仅为 \(Q = A_{\text{hole}} v \approx 4.1 \times 10^{-3}\text{ m}^3/\text{s}\)（每秒仅漏 \(4\text{ L}\)！）。即使气球被打出上百个弹孔，漏光数千立方米氢气也需要数小时乃至数天，且气球蒙皮张力极低不会像高压橡胶气球那样爆裂。
  2. **缺乏氧气与点火源**：气球内部为纯氢气（远高于氢气在空气中 \(75\%\) 的爆炸上限 UEL），内部无氧气助燃；普通铅芯/铜被甲子弹穿透织物时摩擦热量极小，无法在外部空气混合边界引燃氢气。直到一战中后期发明了白磷燃烧弹/曳光弹（如 Pomeroy / Buckingham 弹），才能有效击落防空气球。
- **(c) 改用氦气的利弊与未采用原因**：
  - **升力变化**：氦气毛升力密度为 \(\Delta \rho_{\text{He}} = \rho_{\text{air}} - \rho_{\text{He}} = 1.29 - 0.179 = 1.111\text{ kg/m}^3\)，为氢气的 \(\frac{1.111}{1.2001} \approx 92.6\%\)（毛升力下降 \(7.4\%\)）。但由于结构空重 \(m_{\text{empty}} = 116,857\text{ kg}\) 固定不变，**有效载荷（净升力）**会大幅下降约 \(14\% \sim 25\%\)（例如椭球模型下净升力从 \(127.2\text{ t}\) 降至 \(109.1\text{ t}\)，损失 \(18.1\text{ t}\) 载荷）。
  - **优势与未采用原因**：氦气为惰性气体，绝对不可燃，安全性极高；但氦气只能从少数富氦天然气田中提取，成本极其高昂，且当时全球氦气产量几乎被美国垄断（美国 1925/1927《氦气法案》禁止向外国出口战略氦气），导致英国（R101）和德国（兴登堡号）只能使用廉价易得的氢气。
- **(d) 真空飞艇的升力与可行性论证**：
  - **升力计算**：真空内部密度 \(\rho_{\text{vac}} = 0\)，毛升力密度为 \(\rho_{\text{air}} = 1.29\text{ kg/m}^3\)，相比氢气毛升力仅提高 \(\frac{1.29}{1.2001} - 1 \approx 7.5\%\)。对椭球模型，毛升力质量为 \(262,400\text{ kg}\)，扣除原空重后净升力为 \(145,500\text{ kg}\)（比氢气多出约 \(18.3\text{ t}\)）。
  - **工程可行性**：在传统材料下**完全不可行**！氢气飞艇内外等压（\(\Delta P \approx 0\)），蒙皮只需承受微小的气动载荷；而真空飞艇外壳必须承受完整的外部大气压强 \(P_{\text{atm}} \approx 1.013 \times 10^5\text{ Pa}\)（即每平方米表面承受超过 \(10\) 吨的向内挤压！）。根据薄壳弹性屈曲理论（Buckling），半径为 \(R\)、壁厚为 \(t\) 的球壳临界失稳外压为 \(P_{\text{cr}} = \frac{2E}{\sqrt{3(1-\nu^2)}}\left(\frac{t}{R}\right)^2\)，而漂浮条件要求壳体质量小于排开空气质量 \(\frac{t}{R} < \frac{\rho_{\text{air}}}{3\rho_s}\)，联立要求壳体材料满足 \(\frac{E^{1/2}}{\rho_s} > \frac{[27(1-\nu^2)]^{1/4} P_{\text{atm}}^{1/2}}{\sqrt{2}\rho_{\text{air}}} \approx 4.5 \times 10^2\text{ Pa}^{1/2}\,\text{m}^3/\text{kg}\)。钢铁、铝合金等传统金属材料若做得足够厚以抵抗大气压压瘪，其自重将远超空气浮力；唯有未来采用超高比刚度的三维石墨烯/金刚石蜂窝夹层或超材料双层桁架结构，才有可能制造出真空浮空器。

#### 二、盲解心得与交叉验证
- **点题关键**：第 (b) 问务必用好标题里的提示词 `Bernoulli`，写出 \(v = \sqrt{2\Delta P / \rho_{\text{H}}}\) 算出小孔跑气速度，既有定量计算又有物理深度。

---

### 10. `plancks-2021-preliminary-problem-slice-q10` — Epilogue – Where Our Host Tries to Go to Bed

- **难度分级**：D3
- **核心物理模型**：半无限一维晶格上的有偏随机游走与首达吸收概率（赌徒破产问题）
- **教学标签**：`统计物理` `随机游走` `马尔可夫链` `首达概率` `赌徒破产问题`

#### 一、题目概述与拆解
经典粒子在一维无限晶格上从 \(x = 0\) 出发做离散随机游走：每步以概率 \(p = 0.6\) 向左移动（\(-1\)），以概率 \(q = 1 - p = 0.4\) 向右移动（\(+1\)）。求粒子最终到达右侧 \(x = +10\) 处的概率。
1. **单步首达概率与马尔可夫转移方程**：
   设从任意格点 \(k\) 出发、最终能首次到达右侧相邻格点 \(k+1\) 的概率为 \(\alpha\)。由无限晶格的空间平移不变性，\(\alpha\) 与起始位置 \(k\) 无关；且从 \(0\) 最终到达 \(+10\) 必须依次完成 \(0 \to 1 \to 2 \to \dots \to 10\) 共 \(10\) 个统计独立的首次到达过程，故总概率为：
   \[
   P_{10} = \alpha^{10}.
   \]
2. **用一步全概率公式求解 \(\alpha\)**：
   从 \(x = 0\) 迈出第一步：
   - 以概率 \(q = 1 - p\) 向右一步直接到达 \(x = +1\)（此时成功概率为 \(1\)）；
   - 以概率 \(p\) 向左一步退到 \(x = -1\)，此后若要到达 \(x = +1\)，必须先从 \(-1\) 首次到达 \(0\)（概率为 \(\alpha\)），再从 \(0\) 首次到达 \(+1\)（条件概率亦为 \(\alpha\)），故该分支成功概率为 \(\alpha^2\)。
   因此 \(\alpha\) 满足二次方程：
   \[
   \alpha = (1 - p) + p\alpha^2 \implies p\alpha^2 - \alpha + (1 - p) = 0 \implies (p\alpha - (1 - p))(\alpha - 1) = 0.
   \]
3. **物理根选取与数值计算**：
   方程有两个根 \(\alpha_1 = 1\) 和 \(\alpha_2 = \frac{1 - p}{p}\)。由于 \(p = 0.6 > 1 - p = 0.4\)，随机游走的整体平均漂移向左（\(\langle \Delta x \rangle = q - p = -0.2 < 0\)），粒子有正概率逃逸至 \(x \to -\infty\) 永不返回，故向右首达概率必严格小于 \(1\)：
   \[
   \alpha = \frac{1 - p}{p} = \frac{0.4}{0.6} = \frac{2}{3}.
   \]
   于是粒子最终能到达右侧第 10 级台阶的概率为：
   \[
   P_{10} = \left(\frac{1 - p}{p}\right)^{10} = \left(\frac{2}{3}\right)^{10} = \frac{1024}{59049} \approx 0.0173415 \quad (1.734\%).
   \]

#### 二、盲解心得与交叉验证
- **有限边界极限验证**：若在左侧 \(x = -M\) 处设置吸收壁（经典赌徒破产问题），特征方程 \(p\lambda^2 - \lambda + q = 0\) 的通解为 \(P(x) = A + B(p/q)^x\)，代入 \(P(-M) = 0,\ P(N) = 1\) 得 \(P(0) = \frac{1 - (q/p)^M}{(p/q)^N - (q/p)^M}\)。当 \(p > q\) 且令左边界 \(M \to \infty\) 时，\((q/p)^M \to 0\)，立即收敛到 \(P(0) = \left(\frac{q}{p}\right)^N = \left(\frac{2}{3}\right)^{10}\)！
- **易错点警示**：千万不要把题目算成「连走 10 步向右」的概率 \((0.4)^{10} \approx 1.05 \times 10^{-4}\)，那样漏掉了所有中途向左退步再向右折返的无穷多条路径！


---

## 第二部分：PLANCKS 2021 国际决赛 (International Final, Q1–Q12)

---

### 11. `plancks-2021-final-combined-slice-q1` — Quantum Mechanics

- **难度分级**：D3
- **核心物理模型**：三维各向同性谐振子在磁场中的微扰跃迁与多费米子满壳层抗磁磁化率
- **教学标签**：`量子力学` `三维谐振子` `含时微扰论` `泡利不相容原理` `朗道与拉莫尔抗磁性`

#### 一、题目概述与拆解
质量为 \(m\)、电荷为 \(q\) 的粒子置于频率为 \(\omega_0\) 的三维各向同性谐振子势 \(V(\mathbf{R}) = \frac{1}{2}m\omega_0^2 \mathbf{R}^2\) 中。
- **第 1 问（交变磁场下的基态含时微扰跃迁）**：
  外加均匀交变磁场 \(\mathbf{B}(t) = B_0 \sin(\omega t)\hat{e}_z\)。在对称规范（库仑规范 \(\nabla\cdot\mathbf{A} = 0\)）下，矢势为 \(\mathbf{A} = \frac{1}{2}\mathbf{B}\times\mathbf{R} = \frac{1}{2}B(t)(-y\hat{e}_x + x\hat{e}_y)\)。最小耦合哈密顿量为：
  \[
  \hat{H} = \frac{(\hat{\mathbf{p}} - q\mathbf{A})^2}{2m} + \frac{1}{2}m\omega_0^2 \hat{\mathbf{R}}^2 = \hat{H}_0 - \frac{q B_0}{2m}\sin(\omega t)\hat{L}_z + \frac{q^2 B_0^2}{8m}\sin^2(\omega t)\left(\hat{x}^2 + \hat{y}^2\right).
  \]
  1. **选择定则与允许跃迁**：
     三维谐振子基态 \(|0,0,0\rangle = |k=0, l=0, m=0\rangle\) 的轨道角动量量子数 \(l = 0, m = 0\)，故 \(\hat{L}_z|0,0,0\rangle = 0\)，线性顺磁项**不诱导任何跃迁**！
     二次抗磁项中，将坐标用升降算符表示为 \(\hat{x} = \sqrt{\frac{\hbar}{2m\omega_0}}(a_x + a_x^\dagger),\ \hat{y} = \sqrt{\frac{\hbar}{2m\omega_0}}(a_y + a_y^\dagger)\)，作用在基态上有：
     \[
     (\hat{x}^2 + \hat{y}^2)|0,0,0\rangle = \frac{\hbar}{2m\omega_0}\left(2|0,0,0\rangle + \sqrt{2}|2,0,0\rangle + \sqrt{2}|0,2,0\rangle\right).
     \]
     因此，从基态出发的一阶含时微扰**唯一允许的非平庸跃迁**是跃迁到 \(N = 2\) 壳层的两个态 \(|2,0,0\rangle\) 和 \(|0,2,0\rangle\)（若在球坐标表象 \(\{|k,l,m\rangle\}\) 下，由题表知 \(|2,0,0\rangle + |0,2,0\rangle = -\frac{2}{\sqrt{3}}|k=2,l=0,m=0\rangle - \sqrt{\frac{2}{3}}|k=0,l=2,m=0\rangle\)，即允许跃迁到 \(|2,0,0\rangle_{klm}\) 与 \(|0,2,0\rangle_{klm}\)，选择定则为 \(\Delta N = 2,\ \Delta l = 0, 2,\ \Delta m = 0\)）。
  2. **跃迁振幅与跃迁概率**：
     对末态 \(|f\rangle \in \{|2,0,0\rangle, |0,2,0\rangle\}\)，跃迁频率 \(\omega_{fi} = \frac{E_f - E_i}{\hbar} = 2\omega_0\)，矩阵元为：
     \[
     V_{fi}(t') = \langle f | \hat{V}(t') | 0,0,0\rangle = \frac{q^2 B_0^2 \hbar}{8\sqrt{2} m^2 \omega_0}\sin^2(\omega t').
     \]
     一阶跃迁振幅为：
     \[
     A_{if}^{(1)}(t) = -\frac{i}{\hbar}\int_0^t V_{fi}(t') e^{i\omega_{fi} t'}\,dt' = -\frac{i q^2 B_0^2}{16\sqrt{2} m^2 \omega_0}\int_0^t \left(1 - \frac{e^{2i\omega t'} + e^{-2i\omega t'}}{2}\right)e^{2i\omega_0 t'}\,dt'.
     \]
     跃迁概率由模方给出：\(P_{i\to f}(t) = \left|A_{if}^{(1)}(t)\right|^2\)（共振发生在 \(2\omega = 2\omega_0 \implies \omega = \omega_0\) 处）。
- **第 2 问（20 个自旋 1/2 费米子的基态能量与恒定磁场抗磁磁化率）**：
  - **(a) 基态总能量**：
    第 \(n = n_x + n_y + n_z\) 壳层能量为 \(E_n = \left(n + \frac{3}{2}\right)\hbar\omega_0\)，包含自旋 \(s = 1/2\)（\(g_s = 2\)）的总简并度为 \(g_n = 2 \times \frac{(n+1)(n+2)}{2} = (n+1)(n+2)\)：
    - \(n = 0\)：容纳 \(g_0 = 2\) 个粒子，能量 \(2 \times \frac{3}{2}\hbar\omega_0 = 3\hbar\omega_0\)；
    - \(n = 1\)：容纳 \(g_1 = 6\) 个粒子，能量 \(6 \times \frac{5}{2}\hbar\omega_0 = 15\hbar\omega_0\)；
    - \(n = 2\)：容纳 \(g_2 = 12\) 个粒子，能量 \(12 \times \frac{7}{2}\hbar\omega_0 = 42\hbar\omega_0\)。
    总粒子数 \(2 + 6 + 12 = 20\) 恰好填满 \(n = 0, 1, 2\) 三个闭壳层！故基态总能量为：
    \[
    E_{\text{GS}} = (3 + 15 + 42)\hbar\omega_0 = 60\hbar\omega_0.
    \]
  - **(b) 抗磁磁化率为常数**：
    在恒定磁场 \(\mathbf{B} = B\hat{e}_z\) 下，由于 \(n = 0, 1, 2\) 三个壳层完全填满，满壳层系统的总自旋 \(\hat{\mathbf{S}}_{\text{tot}}|\Psi_0\rangle = 0\)、总轨道角动量 \(\hat{\mathbf{L}}_{\text{tot}}|\Psi_0\rangle = 0\)，故自旋与轨道顺磁项的一阶能量修正严格为零。
    能量修正完全来自拉莫尔抗磁项：
    \[
    \Delta E = \frac{q^2 B^2}{8m}\sum_{i=1}^{20}\langle \hat{x}_i^2 + \hat{y}_i^2 \rangle = \frac{q^2 B^2 \hbar}{8 m^2 \omega_0}\sum_{i=1}^{20}(n_{x,i} + n_{y,i} + 1).
    \]
    由各向同性对称性，\(\sum_{i=1}^{20} n_{x,i} = \sum_{i=1}^{20} n_{y,i} = \frac{1}{3}\sum_{i=1}^{20} n_i = \frac{1}{3}(2\times 0 + 6\times 1 + 12\times 2) = 10\)，故：
    \[
    \Delta E = \frac{q^2 B^2 \hbar}{8 m^2 \omega_0}(10 + 10 + 20) = \frac{5\hbar q^2}{m^2 \omega_0}B^2.
    \]
    磁化强度 \(M = -\frac{\partial E}{\partial B} = -\frac{10\hbar q^2}{m^2 \omega_0}B\)，故抗磁磁化率 \(\chi = \frac{\partial M}{\partial B} = -\frac{10\hbar q^2}{m^2 \omega_0}\) 为与 \(B\) 无关的负常数！

#### 二、对照官方解答与教学拆解
- **解法对比**：官方解答在 2(b) 中通过逐一写出 \(|k,l,m\rangle\) 反对称双粒子波函数来说明 \(\langle L_z \rangle = \langle S_z \rangle = 0\)，未算出 \(\Delta E\) 的具体数值系数（且将 \(60\hbar\omega_0\) 笔误写为 \(87\hbar\omega_0\)）。利用满壳层球对称性与直角坐标量子数求和则能一步算出精确抗磁磁化率 \(\chi = -\frac{10\hbar q^2}{m^2 \omega_0}\)。

---

### 12. `plancks-2021-final-combined-slice-q2` — Tight-Binding Models in a Magnetic Field

- **难度分级**：D4
- **核心物理模型**：磁场中紧束缚晶格的 Peierls 代换、Harper 方程与石墨烯相对论朗道能级
- **教学标签**：`固体物理` `紧束缚模型` `Peierls代换` `Harper方程与Hofstadter蝴蝶` `石墨烯朗道能级`

#### 一、题目概述与拆解
- **第一部分：正方晶格（Square Lattice）**
  - **1.1 Peierls 相位与一维 Harper 方程**：
    设正方晶格格点为 \(\mathbf{R}_{m,n} = a(m\hat{e}_x + n\hat{e}_y)\)。取朗道规范 \(\mathbf{A} = (-By, 0, 0)\)，使磁场相位仅出现在沿 \(x\) 方向的键上：\(\langle \psi_{m,n}|\mathcal{H}|\psi_{m\pm 1, n}\rangle = -t e^{\mp i 2\pi n \phi/\phi_0}\)（其中 \(\phi = B a^2\) 为单胞磁通，\(\phi_0 = h/e\)）。
    由于系统保持 \(x\) 方向平移不变性，令 \(c_{m,n} = e^{i k_x m a}\psi_n\)，代入紧束缚方程即得一维 **Harper 方程**：
    \[
    -t(\psi_{n+1} + \psi_{n-1}) + V_n(k_x)\psi_n = \epsilon \psi_n, \qquad V_n(k_x) = -2t\cos\left(k_x a - 2\pi n\frac{\phi}{\phi_0}\right).
    \]
  - **1.2 特征磁场估算与连续极限**：
    当 \(a \sim 1\text{ \AA} = 10^{-10}\text{ m}\) 时，\(\phi = \phi_0\) 要求磁场 \(B = \frac{h}{e a^2} \approx 4.14 \times 10^5\text{ T}\)，远超实验室可实现的稳恒磁场（\(\sim 10\text{ T}\)），故实际问题中恒有 \(\frac{\phi}{\phi_0} \ll 1\)。此时周期势 \(V_n(k_x)\) 的空间波长 \(\lambda = \frac{\phi_0}{\phi}a = M a \gg a\)。
    令 \(y = na\)，将慢变波函数展开为 \(\psi_{n+1} + \psi_{n-1} \approx 2\psi(y) + a^2\frac{d^2\psi(y)}{dy^2}\)，得到一维有效薛定谔方程：
    \[
    -t a^2 \frac{d^2\psi(y)}{dy^2} + V(y, k_x)\psi(y) = \epsilon\psi(y), \qquad V(y, k_x) = -2t - 2t\cos\left(k_x a - \frac{2\pi\phi}{\phi_0 a}y\right).
    \]
  - **1.3 谐振子近似、朗道能级与简并度**：
    在势能极小值点 \(y_0 = \frac{\phi_0}{\phi}\frac{k_x a}{2\pi}a\) 附近令 \(\tilde{y} = y - y_0\)，展开余弦项：
    \[
    V(\tilde{y}) \approx -4t + t\left(\frac{2\pi\phi}{\phi_0 a}\right)^2 \tilde{y}^2.
    \]
    对比一维谐振子 \(-\frac{\hbar^2}{2m^*}\partial_{\tilde{y}}^2 + \frac{1}{2}m^*\omega^2 \tilde{y}^2\)（其中能带底有效质量 \(m^* = \frac{\hbar^2}{2ta^2}\)），立得本征频率与能谱：
    \[
    \hbar\omega = 4\pi t \frac{\phi}{\phi_0} = \frac{\hbar e B}{m^*}, \qquad \epsilon_r = -4t + \left(r + \frac{1}{2}\right)\hbar\omega \quad (r = 0, 1, 2, \dots).
    \]
    由 \(x\) 方向周期性边界条件 \(k_x = \frac{2\pi}{N_L a}j\)，回旋中心 \(y_0(j) = \frac{M a}{N_L}j\) 落在样品宽度 \(0 \le y_0 < N_W a\) 内的个数即为每个朗道能级的简并度：
    \[
    p = \frac{N_W N_L}{M} = \frac{B A}{\phi_0}.
    \]
    只有当激发能远小于势阱深度 \(2t\)，即 \(r \hbar\omega \ll 2t \implies r \ll \frac{\phi_0}{\phi} = M\) 时，抛物线谐振子近似才成立。

- **第二部分：石墨烯蜂窝晶格（Graphene Lattice）**
  - **2.1–2.2 布洛赫约化与轨道规范变换**：
    沿基矢 \(\mathbf{a}_1\) 方向应用布洛赫定理（波矢 \(k_1\)），将六角原胞磁通记为 \(\varphi\)。对连接同指标 \(n\) 的键引入 Peierls 相位后，通过局域轨道相位重定义 \(\tilde{a}_n, \tilde{b}_n\)，将双原子紧束缚方程化为对称形式：
    \[
    \epsilon \tilde{a}_n = -t\left[2\cos\left(\frac{k_1 a}{2} - n\pi\frac{\varphi}{\phi_0}\right)\tilde{b}_n - \tilde{b}_{n-1}\right], \qquad
    \epsilon \tilde{b}_n = -t\left[2\cos\left(\frac{k_1 a}{2} - n\pi\frac{\varphi}{\phi_0}\right)\tilde{a}_n - \tilde{a}_{n+1}\right].
    \]
  - **2.3 连续极限、升降算符代数与石墨烯相对论朗道能级**：
    零能狄拉克谷位于 \(2\cos\left(\frac{k_1 a}{2} - n_0\pi\frac{\varphi}{\phi_0}\right) = 1\)（即相位角 \(\theta_0 = \pm\frac{\pi}{3}\)）。在 \(n_0\) 附近令 \(y = (n - n_0)a\)，展开 \(2\cos(\theta_0 - \delta\theta) \approx 1 \pm \sqrt{3}\pi\frac{\varphi}{\phi_0}\frac{y}{a}\) 及 \(\tilde{b}_{n\mp 1} \approx \psi_b(y) \mp a\partial_y \psi_b(y)\)，得到旋量矩阵本征方程：
    \[
    \begin{bmatrix} 0 & \hat{A}^\dagger \ \hat{A} & 0 \end{bmatrix} \begin{bmatrix} \psi_a(y) \ \psi_b(y) \end{bmatrix} = \epsilon \begin{bmatrix} \psi_a(y) \ \psi_b(y) \end{bmatrix},
    \]
    其中 \(\hat{A} = -t a\left(\partial_y + \frac{\sqrt{3}\pi\varphi}{\phi_0 a^2}y\right),\ \hat{A}^\dagger = -t a\left(-\partial_y + \frac{\sqrt{3}\pi\varphi}{\phi_0 a^2}y\right)\)。计算对易子：
    \[
    [\hat{A}, \hat{A}^\dagger] = 2\sqrt{3}\pi t^2 \frac{\varphi}{\phi_0} \equiv c.
    \]
    构造标准玻色产生湮灭算符 \(\hat{a} = \hat{A}/\sqrt{c},\ \hat{a}^\dagger = \hat{A}^\dagger/\sqrt{c}\)（满足 \([\hat{a}, \hat{a}^\dagger] = 1\)），旋量本征态为 \((|n-1\rangle, \pm|n\rangle)^T\)，立即解出著名的**石墨烯相对论朗道能级**：
    \[
    \epsilon_n = \pm \sqrt{c\,n} = \pm t\sqrt{2\sqrt{3}\pi\frac{\varphi}{\phi_0}n} = \pm \frac{\hbar v_F}{l_B}\sqrt{2n} \qquad (n = 0, 1, 2, \dots),
    \]
    其中六角原胞面积 \(\varphi/B = \frac{\sqrt{3}}{2}a^2\)，费米速度 \(v_F = \frac{\sqrt{3}ta}{2\hbar}\)，磁长度 \(l_B = \sqrt{\frac{\hbar}{eB}}\)。

#### 二、对照官方解答与教学拆解
- **核心亮点**：本题展示了如何从晶格紧束缚模型出发，分别在抛物线色散（正方晶格）和线性狄拉克色散（石墨烯）下导出截然不同的朗道能级标度律：\(\epsilon_n \propto (n + 1/2)B\) vs \(\epsilon_n \propto \pm\sqrt{nB}\)。

---

### 13. `plancks-2021-final-combined-slice-q3` — The Evolution of Accretion Disks

- **难度分级**：D3
- **核心物理模型**：天体物理薄吸积盘的垂向流体静力学平衡、粘滞角动量输运扩散方程与自引力判据
- **教学标签**：`天体物理` `吸积盘` `流体静力学平衡` `粘滞扩散方程` `高斯引力定理`

#### 一、题目概述与拆解
- **第 1 问（垂向高斯密度分布）**：
  在几何薄盘近似 \(|z| \ll r\) 下，质量为 \(M_*\) 的中心恒星在 \((r, z)\) 处产生的垂向引力加速度为：
  \[
  g_z = -\frac{G M_* z}{(r^2 + z^2)^{3/2}} \approx -\frac{G M_*}{r^3}z = -\Omega_K^2(r) z.
  \]
  代入垂向流体静力学平衡方程 \(\frac{1}{\rho}\frac{\partial P}{\partial z} = g_z\) 及等温状态方程 \(P = \rho c_s^2(r)\)：
  \[
  \frac{1}{\rho}\frac{\partial \rho}{\partial z} = -\frac{\Omega_K^2}{c_s^2}z \implies \rho(r,z) = \rho_0(r)\exp\left(-\frac{z^2}{2 H^2(r)}\right), \qquad H(r) = \frac{c_s(r)}{\Omega_K(r)}.
  \]
- **第 2 问（吸积盘面密度粘滞演化主方程）**：
  柱坐标下轴对称薄盘的质量守恒（连续性）方程为：
  \[
  r\frac{\partial \Sigma}{\partial t} + \frac{\partial}{\partial r}\left(r \Sigma V_r\right) = 0.
  \]
  结合定常引力势下（\(\partial_t \Omega = 0\)）的角动量守恒方程 \(r\frac{\partial}{\partial t}(r^2\Omega\Sigma) + \frac{\partial}{\partial r}(r^2\Omega \cdot r\Sigma V_r) = \frac{1}{2\pi}\frac{\partial G}{\partial r}\)，利用质量守恒消去 \(\frac{\partial(r\Sigma)}{\partial t}\) 得：
  \[
  r\Sigma V_r \frac{d}{dr}(r^2\Omega) = \frac{1}{2\pi}\frac{\partial G}{\partial r} = \frac{\partial}{\partial r}\left(\nu\Sigma r^3 \frac{d\Omega}{dr}\right).
  \]
  代入开普勒角速度 \(\Omega(r) = \sqrt{G M_*}\,r^{-3/2}\)，有 \(\frac{d(r^2\Omega)}{dr} = \frac{1}{2}\sqrt{GM_*}\,r^{-1/2}\) 及 \(r^3\frac{d\Omega}{dr} = -\frac{3}{2}\sqrt{GM_*}\,r^{1/2}\)，解出径向质量通量：
  \[
  r\Sigma V_r = -3 r^{1/2}\frac{\partial}{\partial r}\left(\nu\Sigma r^{1/2}\right).
  \]
  再代回质量守恒方程即证得：
  \[
  \frac{\partial \Sigma}{\partial t} = \frac{3}{r}\frac{\partial}{\partial r}\left[r^{1/2}\frac{\partial}{\partial r}\left(\nu\Sigma r^{1/2}\right)\right].
  \]
- **第 3 问（常粘滞扩散方程与粘滞演化时标）**：
  当 \(\nu = \text{const}\) 时，引入变量代换 \(R = 2 r^{1/2}\)（故 \(\frac{\partial}{\partial r} = r^{-1/2}\frac{\partial}{\partial R} = \frac{2}{R}\frac{\partial}{\partial R}\)）与 \(f = \frac{3}{2}\Sigma R = 3\Sigma r^{1/2}\)。代入演化方程化简得：
  \[
  \frac{\partial f}{\partial t} = D \frac{\partial^2 f}{\partial R^2}, \qquad D = \frac{12\nu}{R^2} = \frac{3\nu}{r}.
  \]
  特征粘滞演化时标为：
  \[
  t_{\text{visc}} \sim \frac{R^2}{D} = \frac{r^2}{3\nu} \sim \frac{r^2}{\nu}.
  \]
  **天文观测测定方法**：可通过统计不同年龄星团中年轻恒星（如 T Tauri 星）原行星盘的红外超（Infrared Excess）留存比例随星团年龄的衰减时标，或测量质量吸积率 \(\dot{M}_{\text{acc}}\)（由紫外连续谱超或 H\(\alpha\) 发射线光度得出）与气体盘总质量 \(M_{\text{disk}}\)（由 ALMA 毫米波尘埃/CO 谱线测得）之比 \(t_{\text{visc}} \sim M_{\text{disk}} / \dot{M}_{\text{acc}}\) 来获得。
- **第 4 问（吸积盘自引力不可忽略的判据）**：
  将吸积盘近似为均匀面密度 \(\Sigma = \frac{M_{\text{disk}}}{\pi R_{\text{disk}}^2}\) 的无限大薄板。由引力高斯定理，盘面正上方由吸积盘自身质量产生的垂向引力加速度为：
  \[
  g_{\text{disk}} = 2\pi G \Sigma = \frac{2 G M_{\text{disk}}}{R_{\text{disk}}^2}.
  \]
  在盘外缘表面 \(r = R_{\text{disk}}, z = H\) 处，中心恒星提供的垂向引力加速度为 \(g_{*,z} = \frac{G M_* H}{R_{\text{disk}}^3}\)。当 \(g_{\text{disk}} > g_{*,z}\) 时盘自引力不可忽略，即：
  \[
  \frac{2 G M_{\text{disk}}}{R_{\text{disk}}^2} > \frac{G M_* H}{R_{\text{disk}}^3} \implies \frac{M_{\text{disk}}}{M_*} > 0.5\left(\frac{H}{R_{\text{disk}}}\right).
  \]

#### 二、对照官方解答与教学拆解
- **完全吻合**：四个小问与官方参考解答完全一致。需特别注意第 4 问高斯定理求无限大平板引力场时，上下两个底面均穿出引力通量，故 \(2 A g_{\text{disk}} = 4\pi G (\Sigma A) \implies g_{\text{disk}} = 2\pi G \Sigma\)。

---

### 14. `plancks-2021-final-combined-slice-q4` — Fluids and Fourier Transform Applied to Solid State Physics

- **难度分级**：D3
- **核心物理模型**：不可压缩流体球形空泡的 Rayleigh 坍缩时间与电介质 Lorentz 振子时频响应
- **教学标签**：`流体力学` `Rayleigh-Plesset空泡坍缩` `Beta与Gamma函数` `Lorentz振子模型` `傅里叶变换与阶跃响应`

#### 一、题目概述与拆解
- **第一部分：理想不可压缩流体中的球形空泡坍缩（Rayleigh Bubble Collapse）**
  - **1.1 坍缩时间公式推导**：
    设时刻 \(t\) 空泡半径为 \(R(t)\)。由球对称不可压缩连续性方程 \(\nabla\cdot\mathbf{v} = \frac{1}{r'^2}\frac{\partial(r'^2 v)}{\partial r'} = 0\)，得径向流速分布 \(v(r', t) = \frac{R^2 \dot{R}}{r'^2}\)（\(r' \ge R\)）。
    我们可以用两种独立方法导出 \(\dot{R}\)：
    - **方法一（功能原理 / 虚拟质量法）**：全空间流体的总动能为：
      \[
      E_k = \int_R^\infty \frac{1}{2}\rho v(r',t)^2 \cdot 4\pi r'^2\,dr' = 2\pi\rho R^4 \dot{R}^2 \int_R^\infty \frac{dr'}{r'^2} = 2\pi\rho R^3 \dot{R}^2.
      \]
      该动能等于无穷远处恒定压强 \(p_0\) 在空泡体积收缩过程中所做的机械功 \(W = p_0 \cdot \frac{4}{3}\pi (R_0^3 - R^3)\)，故：
      \[
      2\pi\rho R^3 \dot{R}^2 = \frac{4}{3}\pi p_0 (R_0^3 - R^3) \implies \frac{dR}{dt} = -\sqrt{\frac{2p_0}{3\rho}\left(\frac{R_0^3}{R^3} - 1\right)}.
      \]
    - **方法二（欧拉方程积分法）**：将 \(v = f(t)/r'^2\)（其中 \(f = R^2\dot{R}\)）代入径向欧拉方程 \(\frac{\partial v}{\partial t} + v\frac{\partial v}{\partial r'} = -\frac{1}{\rho}\frac{\partial p}{\partial r'}\) 并从 \(R\) 积分至 \(\infty\)，得 \(-\frac{\dot{f}}{R} + \frac{1}{2}\dot{R}^2 = \frac{p_0}{\rho}\)，即 \(-\frac{1}{2 R^2}\frac{d}{dR}(R^3 \dot{R}^2) = \frac{p_0}{\rho}\)，积分同样给出上式。
    分离变量从 \(R_0\) 积分到 \(0\)，即证得坍缩总时间：
    \[
    T = \sqrt{\frac{3\rho}{2p_0}}\int_0^{R_0}\frac{dr}{\sqrt{(R_0/r)^3 - 1}}.
    \]
  - **1.2 Beta/Gamma 函数解析求值与数值积分**：
    令 \(x = r/R_0\)，再令 \(u = x^3\)（\(dx = \frac{1}{3}u^{-2/3}du\)），无量纲积分化为：
    \[
    I_0 = \int_0^1 \frac{x^{3/2}}{\sqrt{1 - x^3}}\,dx = \frac{1}{3}\int_0^1 u^{\frac{5}{6}-1}(1 - u)^{\frac{1}{2}-1}\,du = \frac{1}{3}B\left(\frac{5}{6}, \frac{1}{2}\right) = \frac{\Gamma(5/6)\Gamma(1/2)}{3\,\Gamma(4/3)} \approx 0.746834.
    \]
    因此瑞利坍缩时间为 \(T = \sqrt{\frac{3}{2}}I_0 R_0\sqrt{\frac{\rho}{p_0}} \approx 0.91468\,R_0\sqrt{\frac{\rho}{p_0}}\)。
    数值积分时，由于上限 \(x = 1\) 处被积函数发散，可将区间拆分为 \([0, 0.99]\)（用 Simpson 法得 \(0.632\)）与 \([0.99, 1]\)（用中点法或奇点解析展开 \(2\sqrt{(1-x)/3}\) 得 \(0.115\)），相加得 \(0.747\)，与精确解完全吻合。

- **第二部分：电介质极化强度的洛伦兹振子响应（Polarization Field）**
  记有效共振频率为 \(\tilde{\omega}_0 = \sqrt{\omega_0^2 - \nu\omega_p^2}\)，静态极化率为 \(\chi_0 = \frac{\epsilon_0 \omega_p^2}{\tilde{\omega}_0^2}\)。
  - **2.1 频域极化率与 \(\gamma \to 0^+\) 极限**：
    对运动方程 \(\ddot{P} + \gamma\dot{P} + \tilde{\omega}_0^2 P = \epsilon_0\omega_p^2 E(t)\) 作傅里叶变换（\(e^{-i\omega t}\) 约定）：
    \[
    \tilde{R}(\omega) = \tilde{\chi}(\omega) = \frac{\epsilon_0\omega_p^2}{\tilde{\omega}_0^2 - \omega^2 - i\gamma\omega} = \frac{\epsilon_0\omega_p^2(\tilde{\omega}_0^2 - \omega^2)}{(\tilde{\omega}_0^2 - \omega^2)^2 + \gamma^2\omega^2} + i\frac{\epsilon_0\omega_p^2\gamma\omega}{(\tilde{\omega}_0^2 - \omega^2)^2 + \gamma^2\omega^2}.
    \]
    在 \(\gamma \to 0^+\) 极限下，利用 \(\lim_{\gamma\to 0^+}\frac{\gamma}{\Delta^2 + \gamma^2} = \pi\delta(\Delta)\)（对 \(\omega > 0\)）：
    \[
    \chi_r(\omega) = \mathcal{P}\frac{\epsilon_0\omega_p^2}{\tilde{\omega}_0^2 - \omega^2} = \frac{\chi_0}{1 - \omega^2/\tilde{\omega}_0^2}, \qquad
    \chi_i(\omega) = \frac{\pi}{2}\chi_0 \tilde{\omega}_0 \delta(\omega - \tilde{\omega}_0).
    \]
  - **2.2 无阻尼极限下对阶跃电场 \(E(t) = E_0\Theta(t)\) 的响应**：
    当 \(t > 0\) 时，求解初值问题 \(\ddot{P} + \tilde{\omega}_0^2 P = \epsilon_0\omega_p^2 E_0\)（\(P(0) = \dot{P}(0) = 0\)），或对脉冲响应函数 \(R(t) = \chi_0\tilde{\omega}_0\sin(\tilde{\omega}_0 t)\Theta(t)\) 卷积，得：
    \[
    P(t) = \chi_0 E_0\big[1 - \cos(\tilde{\omega}_0 t)\big]\Theta(t).
    \]
    物理图像：由于无阻尼耗散，极化强度在 \(0\) 与 \(2\chi_0 E_0\) 之间围绕静态平衡值 \(\chi_0 E_0\) 永不停息地简谐振荡。
  - **2.3 弱阻尼（\(\gamma/\tilde{\omega}_0 \ll 1\)）下的暂态振荡与稳态极限**：
    当 \(0 < \gamma \ll \tilde{\omega}_0\) 时，阶跃电场下的精确解为非齐次稳态特解 \(\chi_0 E_0\) 与齐次欠阻尼通解的叠加：
    \[
    P(t) = \chi_0 E_0\left[1 - e^{-\gamma t/2}\left(\cos(\omega' t) + \frac{\gamma}{2\omega'}\sin(\omega' t)\right)\right]\Theta(t) \approx \chi_0 E_0\Big[1 - e^{-\gamma t/2}\cos(\omega' t)\Big]\Theta(t),
    \]
    其中阻尼振荡频率为 \(\omega' = \sqrt{\tilde{\omega}_0^2 - \frac{\gamma^2}{4}}\)，振荡包络振幅按 \(e^{-\gamma t/2}\) 指数衰减，机械振荡能量按 \(e^{-\gamma t}\) 指数衰减。当 \(t \to \infty\) 时，暂态振荡完全耗散，极化强度趋于恒定的静电极化值：
    \[
    P(t \to \infty) = \chi_0 E_0 = \frac{\epsilon_0 \omega_p^2 E_0}{\omega_0^2 - \nu\omega_p^2}.
    \]

#### 二、对照官方解答与教学拆解
- **官方解答勘误警示**：在 2.3 问中，官方解答误写为 \(P(t) = \chi_0 E_0 e^{-\gamma t/2}(1 - \cos\omega_0' t)\)，把整个括号乘上了 \(e^{-\gamma t/2}\)！这会导致 \(t \to \infty\) 时 \(P(\infty) = 0\)，显然违背了外加恒定电场 \(E_0\) 持续存在时的静电极化平衡律。正确的形式必须是 \(P(t) \approx \chi_0 E_0(1 - e^{-\gamma t/2}\cos\omega_0' t)\)，衰减的只是围绕平衡位置 \(\chi_0 E_0\) 的振荡项！

---

### 15. `plancks-2021-final-combined-slice-q5` — Exoplanets

- **难度分级**：D2
- **核心物理模型**：系外行星视向速度法探测、辐射平衡温度、Jeans 大气逃逸与原行星盘亚开普勒气体拖曳
- **教学标签**：`天体物理` `系外行星` `视向速度法` `黑体辐射平衡` `大气逃逸与气体拖曳`

#### 一、题目概述与拆解
- **第 1 问（视向速度法与恒星摆动速度计算）**：
  恒星（\(M_{\text{star}}\)）与行星（\(M_{\text{planet}}\)）绕公共质心做角速度同为 \(\Omega = \frac{2\pi}{P}\) 的圆周运动。由质心系总动量为零（或质心定义 \(M_{\text{star}} a_{\text{star}} = M_{\text{planet}} a_{\text{planet}}\)）及 \(V = \Omega a\)，得：
  \[
  \frac{M_{\text{star}}}{M_{\text{planet}}} = \frac{a_{\text{planet}}}{a_{\text{star}}} = \frac{V_{\text{planet}}}{V_{\text{star}}} \implies \frac{V_{\text{star}}}{V_{\text{planet}}} = \frac{M_{\text{planet}}}{M_{\text{star}}}.
  \]
  代入木星轨道参数 \(a_{\text{planet}} = 5.2\text{ AU} = 7.80 \times 10^8\text{ km}\)，周期 \(P = 12\text{ yr} \approx 3.784 \times 10^8\text{ s}\)：
  \[
  V_{\text{planet}} = \frac{2\pi a_{\text{planet}}}{P} \approx 12.95\text{ km/s} \implies V_{\text{star}} = 10^{-3} V_{\text{planet}} \approx 0.0129\text{ km/s} = 12.9\text{ m/s}.
  \]
- **第 2 问（行星热平衡温度推导）**：
  半径为 \(R_\star\)、表面温度为 \(T_\star\) 的恒星总光度为 \(L_\star = 4\pi R_\star^2 \sigma T_\star^4\)。在距离 \(D\) 处，半径为 \(R_p\)、反照率为 \(A_B\) 的行星截获并吸收的辐射功率为：
  \[
  P_{\text{in}} = (1 - A_B)\left(\pi R_p^2\right)\frac{4\pi R_\star^2 \sigma T_\star^4}{4\pi D^2}.
  \]
  行星表面温度均匀（设为 \(T_p\)，有效红外发射率为 \(\epsilon\)），向外热辐射总功率为 \(P_{\text{out}} = 4\pi R_p^2 \epsilon \sigma T_p^4\)。由热平衡 \(P_{\text{in}} = P_{\text{out}}\) 得：
  \[
  T_p = \left(\frac{1 - A_B}{4\epsilon}\right)^{1/4} T_\star\sqrt{\frac{R_\star}{D}} \propto T_\star\sqrt{\frac{R_\star}{D}}.
  \]
  比例系数 \(\left(\frac{1 - A_B}{4\epsilon}\right)^{1/4}\) 反映了行星的**邦德反照率（Albedo \(A_B\)）**、大气温室效应发射率 \(\epsilon\) 以及截获截面 \(\pi R_p^2\) 与全球辐射面积 \(4\pi R_p^2\) 的几何比值 \(1/4\)。
- **第 3 问（热木星氢大气的抗蒸发留存判据）**：
  行星质量 \(M_p = 0.5 M_J = 0.949 \times 10^{27}\text{ kg}\)，平均密度与木星相同（\(\rho_p = \rho_J\)），故半径 \(R_p = 2^{-1/3} R_J \approx 0.7937 \times 70,000\text{ km} \approx 5.56 \times 10^4\text{ km}\)。
  行星表面逃逸速度为：
  \[
  v_{\text{esc}} = \sqrt{\frac{2 G M_p}{R_p}} \approx 47.7\text{ km/s}.
  \]
  在 \(T_p = 1250\text{ K}\) 下，氢分子（\(\text{H}_2\)，\(m = 2 m_p \approx 3.34 \times 10^{-27}\text{ kg}\)）的热运动方均根速率为：
  \[
  v_{\text{th}} = \sqrt{\frac{3 k_B T_p}{m_{\text{H}_2}}} \approx 3.94\text{ km/s} \quad (\text{即使对离解氢原子 H 亦仅有 } 5.57\text{ km/s}).
  \]
  由于 \(v_{\text{esc}} \approx 12\,v_{\text{th}} \gg 6\,v_{\text{th}}\)（金斯逃逸参数 \(\lambda \gg 1\)），该热木星的大气层**能够抵抗热蒸发并长期留存**。
- **第 4 问（原行星盘中气体的亚开普勒旋转速度）**：
  固体尘埃颗粒不受气压梯度影响，仅在恒星引力作用下做开普勒圆周运动：
  \[
  \frac{v_{\text{dust}}^2}{r} = \frac{G M}{r^2} = \Omega^2 r \implies v_{\text{dust}} = \Omega r.
  \]
  盘中气体除受恒星指向中心的引力外，还受到径向压强梯度力 \(-\frac{1}{\rho}\frac{\partial P}{\partial r}\) 的向外支撑：
  \[
  \frac{v_{\text{gas}}^2}{r} = \frac{G M}{r^2} + \frac{1}{\rho}\frac{\partial P}{\partial r}.
  \]
  由于气体的密度和温度均随径向距离 \(r\) 的增大而减小，压强梯度为负，按特征尺度近似有 \(\frac{\partial P}{\partial r} \approx -\frac{P}{r} = -\frac{\rho c^2}{r}\)。代入上式即证得：
  \[
  \frac{v_{\text{gas}}^2}{r} = \Omega^2 r - \frac{c^2}{r} \implies v_{\text{gas}} = \Omega r\left(1 - \frac{c^2}{r^2\Omega^2}\right)^{1/2} = v_{\text{dust}}\left(1 - \frac{c^2}{r^2\Omega^2}\right)^{1/2}.
  \]

#### 二、对照官方解答与教学拆解
- **官方解答符号勘误**：在第 4 问中，官方解答在近似 \(\frac{\partial P}{\partial r} \approx \frac{P}{r}\) 时漏掉了压强随半径递减的**负号**，导致最终写成了 \(\left(1 + \frac{c^2}{\Omega^2 r^2}\right)^{1/2}\)，与题干要求证明的 \(\left(1 - \frac{c^2}{r^2\Omega^2}\right)^{1/2}\) 符号相反。物理上正是因为 \(\frac{\partial P}{\partial r} < 0\)（向外气压支撑抵消部分引力），气体旋转才比尘埃慢（\(v_{\text{gas}} < v_{\text{dust}}\)），从而对固体卵石产生迎面逆风阻力使其坠向恒星！

---

### 16. `plancks-2021-final-combined-slice-q6` — Cosmology

- **难度分级**：D2
- **核心物理模型**：牛顿宇宙学近似下的弗里德曼方程推导与三维空间曲率有效势演化分析
- **教学标签**：`宇宙学` `牛顿引力近似` `弗里德曼方程` `物质能量密度演化` `宇宙空间曲率与有效势`

#### 一、题目概述与拆解
- **第 1 问（标度因子 \(a(t)\) 的牛顿运动方程）**：
  由牛顿球壳定理，距原点 \(a(t)\) 处质量为 \(m\) 的星系仅受球内总质量 \(M\) 的万有引力作用：
  \[
  m\ddot{a} = -\frac{G M m}{a^2} \implies \ddot{a} = -\frac{G M}{a^2}.
  \]
- **第 2 问（第一积分 / 机械能守恒式）**：
  两边同乘 \(\dot{a}\) 对时间积分：
  \[
  \dot{a}\ddot{a} = -\frac{G M \dot{a}}{a^2} \implies \frac{d}{dt}\left(\frac{1}{2}\dot{a}^2\right) = \frac{d}{dt}\left(\frac{G M}{a}\right) \implies \frac{1}{2}\dot{a}^2 = \frac{G M}{a} - \frac{k}{2},
  \]
  其中 \(-k/2\) 为单位质量总机械能（积分常数）。
- **第 3 问（导出弗里德曼方程）**：
  将均匀无压尘埃球质量 \(M = \frac{4}{3}\pi a(t)^3 \rho(t)\) 代入上式，两边同除以 \(\frac{1}{2}a^2\)，即得哈勃膨胀率 \(H = \dot{a}/a\) 的弗里德曼方程：
  \[
  H^2 \equiv \left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho(t) - \frac{k}{a^2}.
  \]
- **第 4 问（物质密度与标度因子的关系）**：
  球内总质量 \(M = \frac{4}{3}\pi a(t)^3 \rho(t) = \text{const}\)，故无压物质密度随标度因子的三次方反比衰减：
  \[
  \rho(t) = \frac{3M}{4\pi a(t)^3} = \rho_0\left(\frac{a_0}{a(t)}\right)^3 \propto a(t)^{-3}.
  \]
- **第 5 问（有效势 \(V_{\text{eff}}(a)\) 与三类空间几何宇宙的演化）**：
  利用 \(M = \frac{4}{3}\pi \rho a^3 = \text{const}\)，有效势为：
  \[
  V_{\text{eff}}(a) = -\frac{4\pi G}{3}\rho(t) a(t)^2 = -\frac{G M}{a(t)} \propto -\frac{1}{a},
  \]
  弗里德曼方程化为一维质点能量守恒形式 \(\frac{1}{2}\dot{a}^2 + V_{\text{eff}}(a) = -\frac{k}{2}\)。
  - **a. 闭合宇宙（\(k > 0\)，三维球面 \(S^3\)）**：有效总能量 \(-k/2 < 0\)（引力束缚态）。标度因子 \(a(t)\) 从大爆炸奇点 \(a=0\) 膨胀至最大转折半径 \(a_{\max} = \frac{2GM}{k}\)（此时 \(\dot{a} = 0\)），随后逆转收缩直至发生「大挤压（Big Crunch）」，轨迹为旋轮线（Cycloid）。
  - **b. 平坦宇宙（\(k = 0\)，三维欧氏空间 \(E^3\)）**：有效总能量 \(-k/2 = 0\)（抛物线逃逸临界态）。宇宙永远持续膨胀但膨胀速率渐近趋于零（\(\dot{a} \to 0\)），标度因子按幂律演化：\(a(t) = \left(\frac{9GM}{2}\right)^{1/3} t^{2/3} \propto t^{2/3}\)。
  - **c. 开放宇宙（\(k < 0\)，三维双曲空间 \(H^3\)）**：有效总能量 \(-k/2 > 0\)（双曲线非束缚态）。宇宙永远膨胀，且在 \(t \to \infty\)（\(V_{\text{eff}} \to 0\)）时膨胀速率趋于正常数 \(\dot{a} \to \sqrt{-k}\)，标度因子渐近线性增长 \(a(t) \propto t\)。

#### 二、对照官方解答与教学拆解
- **图形要点**：与官方解答完全一致。画 \(V_{\text{eff}}(a)\) 时务必注意它是 \(-GM/a\) 型反比例吸引势阱（位于第四象限，随 \(a\) 增大单调上升趋近于 \(0\)），绝不能因为题目写了 \(-4\pi G\rho a^2/3\) 就误画成开口向下的抛物线！

---

### 17. `plancks-2021-final-combined-slice-q7` — Nanotechnology

- **难度分级**：D3
- **核心物理模型**：自旋电子学双电流巨磁阻 (GMR) 模型、磁隧道结 (MTJ) Simmons 隧穿电流与量子点三维限域能隙
- **教学标签**：`凝聚态与纳米物理` `自旋电子学与巨磁阻` `莫特双电流模型` `WKB量子隧穿与Simmons方程` `量子点能隙蓝移`

#### 一、题目概述与拆解
- **第 1 问（纳米磁结的工作原理与二进制比特读取）**：
  铁磁材料（FM）在费米面附近的电子态密度具有自旋劈裂，导电过程可分解为自旋向上（\(\uparrow\)）和自旋向下（\(\downarrow\)）两个独立的并联自旋通道（**莫特双电流模型**）。器件由一层磁化方向固定的参考层（Pinned Layer）、中间纳米级非磁性隔离层（NM）和一层磁化方向可随外部磁场自由翻转的自由层（Free Layer）组成：
  - 当两铁磁层磁化方向**平行（P）**时，多数自旋电子在两层中均只受微弱散射，形成低阻短路通道，器件处于**低电阻态 \(R_P\)**（对应逻辑比特 `0`）；
  - 当两铁磁层磁化方向**反平行（AP）**时，无论自旋向上还是向下的电子都会在其中一层铁磁体中成为少数自旋并遭受强烈散射，器件处于**高电阻态 \(R_{AP}\)**（对应逻辑比特 `1`）。
- **第 2 问（自旋阀的最大巨磁阻 GMR 表达式）**：
  设单层铁磁电极对多数自旋和少数自旋的电阻分别为 \(r\) 和 \(R\)（忽略非磁金属层电阻）：
  - **平行构型（P）**：两自旋通道电阻分别为 \(2r\) 与 \(2R\)，并联总电阻为：
    \[
    R_P = \frac{(2r)(2R)}{2r + 2R} = \frac{2rR}{r + R}.
    \]
  - **反平行构型（AP）**：两自旋通道电阻均为 \(r + R\)，并联总电阻为：
    \[
    R_{AP} = \frac{r + R}{2}.
    \]
  - **最大磁阻灵敏度（GMR）**：
    \[
    \text{GMR} = \frac{R_{AP} - R_P}{R_P} = \frac{\frac{r+R}{2} - \frac{2rR}{r+R}}{\frac{2rR}{r+R}} = \frac{(R - r)^2}{4 r R} \quad \left(\text{若按归一化定义 }\frac{R_{AP} - R_P}{R_{AP}}\text{ 则为 }\left(\frac{R - r}{R + r}\right)^2\right).
    \]
- **第 3 问（磁隧道结 MTJ 的隧穿电流一般表达式）**：
  对夹有厚度为 \(L\)（或 \(\delta z\)）、势垒高度为 \(U_0\) 的绝缘层（MIM 结构）：
  1. **势垒透射系数**：由一维定态薛定谔方程连续性条件解得精确透射率 \(D(E_z) = \left[\cosh^2(k_2 L) + \frac{1}{4}\left(\frac{k_2}{k_1} - \frac{k_1}{k_2}\right)^2\sinh^2(k_2 L)\right]^{-1}\)（其中 \(k_1 = \frac{\sqrt{2m E_z}}{\hbar},\ k_2 = \frac{\sqrt{2m(U_0 - E_z)}}{\hbar}\)）。在厚势垒 WKB 近似（\(k_2 L \gg 1\)）下：
     \[
     D(E_z) \approx \exp\left(-\frac{2}{\hbar}\int_{z_1}^{z_2}\sqrt{2m\big(U(z) - E_z\big)}\,dz\right) \approx \exp\left(-A\,\delta z\sqrt{\mu + \bar{\varphi} - E_z}\right),
     \]
     其中 \(\bar{\varphi}\) 为平均势垒高度，\(A = \frac{2\beta\sqrt{2m}}{\hbar}\)。
  2. **三维动量积分与 Simmons 方程**：对横向动量 \(p_x, p_y\)（\(E_r = \frac{p_r^2}{2m}\)）积分得到净供给函数 \(\xi(E_z, eV) = \frac{m e}{2\pi^2\hbar^3}\int_0^\infty [f_1(E_z + E_r) - f_2(E_z + E_r + eV)]\,dE_r\)。在零温近似下对纵向能量 \(E_z\) 完成积分，即得著名的 **Simmons 隧穿电流密度公式**：
     \[
     J = \frac{e}{4\pi^2 \beta^2 \hbar (\delta z)^2}\left\{\bar{\varphi}\exp\left(-A\,\delta z\sqrt{\bar{\varphi}}\right) - (\bar{\varphi} + eV)\exp\left(-A\,\delta z\sqrt{\bar{\varphi} + eV}\right)\right\}.
     \]
- **第 4 问（量子点的能隙公式与能带曲率效应）**：
  - **4.1 量子点能隙与体材料能隙的关系（Brus 方程）**：
    电子与空穴在三维空间受限于尺度为 \(d\) 的纳米颗粒（无限深势阱）：
    - 若为边长 \(d\) 的三维立方体势阱，零点限域能为 \(\Delta E_{\text{cube}} = \frac{3h^2}{8 m^* d^2}\)；
    - 若为直径 \(d = 2R\) 的三维球形无限深势阱（基态波矢 \(k = \frac{\pi}{R} = \frac{2\pi}{d}\)），零点限域能为 \(\Delta E_{\text{sphere}} = \frac{h^2}{2 m^* d^2} = \frac{\hbar^2 \pi^2}{2 m^* R^2}\)（其中 \(\frac{1}{m^*} = \frac{1}{m_e^*} + \frac{1}{m_h^*}\) 为激子约化有效质量）。
    计入介电屏蔽下的电子-空穴库仑吸引能修正 \(E_{\text{Coul}} = -\frac{1.8 e^2}{2\pi \varepsilon \varepsilon_0 d}\)，量子点总有效带隙为：
    \[
    E_g(d) = E_g(\text{bulk}) + \frac{h^2}{2 m^* d^2} - \frac{1.8 e^2}{2\pi \varepsilon \varepsilon_0 d}.
    \]
  - **4.2 强弯曲抛物线能带对能隙的影响**：
    由能带有效质量定义 \(\frac{1}{m^*} = \frac{1}{\hbar^2}\frac{d^2 E}{dk^2}\)，若能带抛物线弯曲强烈（即曲率 \(\frac{d^2 E}{dk^2}\) 很大），则载流子的**有效质量 \(m^*\) 很小**；由 \(E_g(d)\) 公式可知，\(m^*\) 越小，量子限域动能项 \(\frac{h^2}{2m^* d^2}\) 越大，因此量子点的带隙 \(E_g(d)\) 将**显著增大（发生强烈的量子限域蓝移）**。

#### 二、对照官方解答与教学拆解
- **官方解答第 2 问勘误**：官方解答在写平行态并联电阻时，误把电导 \(G_P = \frac{1}{2r} + \frac{1}{2R} = \frac{r+R}{2rR}\) 当作了电阻 \(R_P\)，导致其最终 GMR 表达式量纲不自洽。正确结果应为 \(R_P = \frac{2rR}{r+R}\) 及 \(\text{GMR} = \frac{(R - r)^2}{4rR}\)。

---

### 18. `plancks-2021-final-combined-slice-q8` — Cosmological Consequences of Scalar Fields

- **难度分级**：D4
- **核心物理模型**：宇宙学标量场 (Quintessence 与快子场) 动力学演化、慢滚状态方程与精细结构常数红移演化
- **教学标签**：`宇宙学与广义相对论` `标量场暗能量` `克莱因-戈登方程` `慢滚近似` `精细结构常数演化`

#### 一、题目概述与拆解
- **第 1 问（两类标量场的宇宙学演化方程与加速膨胀条件）**：
  将能量密度与压强代入宇宙流体连续性方程 \(\dot{\rho} = -3H(\rho + p)\)：
  1. **正则标量场（Quintessence）**：\(\rho_1 = \frac{1}{2}\dot{\phi}^2 + V_1(\phi),\ p_1 = \frac{1}{2}\dot{\phi}^2 - V_1(\phi) \implies \rho_1 + p_1 = \dot{\phi}^2\)。求导得 \(\dot{\rho}_1 = \dot{\phi}(\ddot{\phi} + V_1'(\phi)) = -3H\dot{\phi}^2\)，消去 \(\dot{\phi}\) 得克莱因-戈登方程：
     \[
     \ddot{\phi} + 3H\dot{\phi} + \frac{dV_1}{d\phi} = 0.
     \]
     宇宙加速膨胀要求 \(\ddot{a} > 0 \iff w_1 = \frac{p_1}{\rho_1} < -\frac{1}{3}\)，即 \(\frac{1}{2}\dot{\phi}^2 - V_1 < -\frac{1}{3}\left(\frac{1}{2}\dot{\phi}^2 + V_1\right) \iff \dot{\phi}^2 < V_1(\phi)\)（**慢滚条件**：动能远小于势能 \(\dot{\phi}^2 \ll V_1(\phi)\) 时 \(w_1 \to -1\)）。
  2. **相对论快子标量场（Tachyon / DBI Field）**：\(\rho_2 = \frac{V_2(\phi)}{\sqrt{1 - \dot{\phi}^2}},\ p_2 = -V_2(\phi)\sqrt{1 - \dot{\phi}^2} \implies \rho_2 + p_2 = \frac{V_2(\phi)\dot{\phi}^2}{\sqrt{1 - \dot{\phi}^2}}\)。对 \(\rho_2\) 求时间导数代入连续性方程：
     \[
     \frac{\ddot{\phi}}{1 - \dot{\phi}^2} + 3H\dot{\phi} + \frac{1}{V_2(\phi)}\frac{dV_2}{d\phi} = 0.
     \]
     其状态方程参数为 \(w_2 = \frac{p_2}{\rho_2} = -(1 - \dot{\phi}^2)\)，故加速膨胀条件 \(w_2 < -\frac{1}{3}\) 要求 \(\dot{\phi}^2 < \frac{2}{3}\)（当 \(\dot{\phi}^2 \ll 1\) 时 \(w_2 \to -1\)）。
- **第 2 问（慢滚标量场的状态方程 \(w(z)\) 与弗里德曼方程）**：
  对第一类标量场，在慢滚近似（\(\dot{\phi}^2 \ll V_1(\phi)\)）下：
  - 一方面，\(\rho_\phi \approx V_1(\phi) \approx \text{const}\)，且 \(1 + w(z) = \frac{\dot{\phi}^2}{\rho_\phi} \propto \dot{\phi}^2\)；
  - 另一方面，演化方程中忽略 \(\ddot{\phi}\) 项得 \(3H\dot{\phi} \approx -V_1'(\phi) \approx \text{const} \implies \dot{\phi} \propto \frac{1}{H(z)}\)。
  联立两式得 \(1 + w(z) \propto \frac{1}{H^2(z)}\)，用当前时刻值（\(z=0\)）归一化即证得式 (5)：
  \[
  w(z) = -1 + (1 + w_0)\frac{H_0^2}{H^2(z)}.
  \]
  在平坦宇宙（\(\Omega_m + \Omega_\phi = 1\)）中，由连续性方程 \(\frac{d\ln\rho_\phi}{dz} = \frac{3(1 + w(z))}{1 + z}\)，在一阶慢滚近似下将分母 \(H^2(y)/H_0^2\) 取为零阶背景 \(\Omega_m(1+y)^3 + \Omega_\phi\) 积分：
  \[
  \int_0^z \frac{3(1 + w_0)}{\Omega_m(1+y)^3 + \Omega_\phi}\frac{dy}{1+y} = \frac{1 + w_0}{\Omega_\phi}\ln\left[\frac{(1+z)^3}{\Omega_m(1+z)^3 + \Omega_\phi}\right],
  \]
  代入 \(H^2(z)/H_0^2 = \Omega_m(1+z)^3 + \Omega_\phi \exp\left(3\int_0^z \frac{1+w}{1+y}dy\right)\) 即证得式 (6)：
  \[
  \frac{H^2(z)}{H_0^2} = \Omega_m(1 + z)^3 + \Omega_\phi\left[\frac{(1 + z)^3}{\Omega_m(1 + z)^3 + \Omega_\phi}\right]^{\frac{1 + w_0}{\Omega_\phi}}.
  \]
- **第 3 问（平坦 \(\Lambda\)CDM 背景下耦合标量场的精确红移演化解）**：
  忽略标量场对背景膨胀的贡献时，平坦 \(\Lambda\)CDM 宇宙的弗里德曼方程为：
  \[
  H^2 = \left(\frac{\dot{a}}{a}\right)^2 = H_0^2\left[\Omega_m\left(\frac{a_0}{a}\right)^3 + \Omega_\Lambda\right] \equiv H_0^2 E^2(z).
  \]
  令 \(y = \sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\left(\frac{a}{a_0}\right)^{3/2}\)，则 \(\dot{y} = \frac{3}{2}H_0\sqrt{\Omega_\Lambda}\sqrt{1 + y^2}\)，结合 \(a(0) = 0\) 积分解得精确背景标度因子：
  \[
  \frac{a(t)}{a_0} = \left(\frac{\Omega_m}{\Omega_\Lambda}\right)^{1/3}\sinh^{2/3}\left(\frac{3}{2}H_0\sqrt{\Omega_\Lambda}\,t\right) = \left(\frac{\Omega_m}{\Omega_\Lambda}\right)^{1/3}\sinh^{2/3}\left(\frac{b t}{2}\right), \qquad b \equiv 3 H_0\sqrt{\Omega_\Lambda}.
  \]
  将演化方程 (7) 左端写为 \(\frac{1}{a^3}\frac{d}{dt}(a^3\dot{\phi})\)，代入 \(a^3(t)\) 对时间积分一次（取 \(\dot{\phi}(0) = 0\)）：
  \[
  \dot{\phi}(t) = -3\Omega_m H_0^2 \frac{a_0^3}{a^3}\left[\eta_m t + \frac{\eta_\Lambda}{2b}\big(\sinh(bt) - bt\big)\right].
  \]
  再利用 \(\frac{a_0}{a} = 1 + z\) 将时间积分转换为对红移 \(z\) 的积分（满足 \(\phi(z=0) = 0\)），最终得到对数型解析解：
  \[
  \phi(z) = 2\eta_m\ln(1 + z) + \frac{2(\eta_\Lambda - 2\eta_m)}{3\sqrt{\Omega_\Lambda}}\left[\ln\left(\frac{1 + \sqrt{\Omega_\Lambda}}{\sqrt{\Omega_m}}\right) - E(z)\ln\left(\frac{\sqrt{\Omega_\Lambda} + E(z)}{\sqrt{\Omega_m(1 + z)^3}}\right)\right].
  \]
- **第 4 问（导致精细结构常数对数演化 \(\Delta\alpha/\alpha \propto \ln(1+z)\) 的暗能量状态方程）**：
  要使积分 \(\frac{\Delta\alpha}{\alpha}(z) = \zeta\int_0^z \sqrt{3 f_\phi(y)[1 + w_\phi(y)]}\frac{dy}{1+y} \propto \ln(1 + z)\) 对任意 \(z\) 成立，被积函数中的平方根因子必须为常数！代入 \(z = 0\) 处的当前值（\(f_\phi(0) = \Omega_\phi,\ w_\phi(0) = w_0\)），得守恒关系：
  \[
  f_\phi(z)\big[1 + w(z)\big] = \frac{\rho_\phi(z)\big[1 + w(z)\big]}{\rho_m(z) + \rho_\phi(z)} = \Omega_\phi(1 + w_0) = \text{const}.
  \]
  **捷径解法**：利用连续性方程 \(\frac{d\rho_\phi}{d\ln(1+z)} = 3\rho_\phi(1 + w)\)，上式直接给出关于 \(\rho_\phi(z)\) 的一阶线性常微分方程：
  \[
  \frac{d\rho_\phi}{d\ln(1+z)} = 3\Omega_\phi(1 + w_0)\big[\rho_{m,0}(1 + z)^3 + \rho_\phi(z)\big]!
  \]
  （或者按官方解答对 \(f_\phi(1+w) = \text{const}\) 求导得 \(\frac{dw}{dz} = -3(1 + w_0)\frac{w}{1+z}\left[\frac{1+w}{1+w_0} - \Omega_\phi\right]\)）。利用初值 \(\rho_\phi(0) = \rho_{\phi,0},\ w(0) = w_0\) 及 \(\Omega_m + \Omega_\phi = 1\) 求解该一阶线性方程，立即得到哈勃参数与状态方程的显式解：
  \[
  \frac{H^2(z)}{H_0^2} = \Omega_m(1 + z)^3 + \frac{\Omega_\phi}{\Omega_m(1 + w_0) - w_0}\Big[\Omega_m(1 + w_0)(1 + z)^3 - w_0(1 + z)^{3\Omega_\phi(1 + w_0)}\Big],
  \]
  \[
  w(z) = \frac{\big[1 - \Omega_\phi(1 + w_0)\big]w_0}{\Omega_m(1 + w_0)\big[1 - \Omega_\phi(1 + w_0)\big](1 + z)^{3[1 - \Omega_\phi(1 + w_0)]} - w_0}.
  \]

#### 二、对照官方解答与教学拆解
- **方法升华**：在第 4 问中，官方解答通过求导构造关于 \(w(z)\) 的非线性微分方程再积分；而我们发现利用 \(\rho_\phi(1+w) = \frac{1}{3}\frac{d\rho_\phi}{d\ln(1+z)}\) 可直接将条件 \(f_\phi(1+w) = \Omega_\phi(1+w_0)\) 转化为关于 \(\rho_\phi\) 的**一阶常系数线性微分方程** \(\frac{d\rho_\phi}{d\ln a} + 3\Omega_\phi(1+w_0)\rho_\phi = -3\Omega_\phi(1+w_0)\rho_{m,0}(a_0/a)^3\)，三行即可写出通解！

---

### 19. `plancks-2021-final-combined-slice-q9` — Electromagnetism

- **难度分级**：D2
- **核心物理模型**：带电粒子在半无限匀强磁场与静电场边界的回旋反射与重返轨迹几何
- **教学标签**：`电磁学` `洛伦兹力与回旋半径` `半无限磁场边界反射` `正则动量守恒` `静电势垒折射`

#### 一、题目概述与拆解
质子（电荷 \(e\)，质量 \(m\)）通过距离半无限磁场边界 \(x = 0\) 为 \(l\) 的点 \(P(-l, 0)\)，以速率 \(v\)、与边界法线（\(+x\) 轴）成夹角 \(\theta\) 射入 \(x > 0\) 的匀强磁场区。
- **第 1 问（求离开磁场时的出射角 \(\phi\)）**：
  质子在匀强磁场中做匀速圆周运动（回旋半径 \(R = \frac{mv}{eB}\)）。由圆关于弦（边界 \(x = 0\)）的垂直平分线的镜面对称性（或沿 \(y\) 方向的正则动量守恒 \(p_y = mv_y - eBx = \text{const}\)，在 \(x=0\) 处给出 \(v_{y,\text{out}} = v_{y,\text{in}} = v\sin\theta\)，结合动能守恒 \(v_{x,\text{out}} = -v_{x,\text{in}} = -v\cos\theta\)），出射角必等于入射角：
  \[
  \phi = \theta.
  \]
- **第 2 问（求进出口间距 \(d\)）**：
  当磁场垂直纸面向里时，质子逆时针偏转（劣弧，圆心角为 \(\pi - 2\theta\)），弦长即为进出口距离：
  \[
  d = 2 R\cos\theta = \frac{2 m v\cos\theta}{e B}.
  \]
- **第 3 问（磁场反向垂直纸面向外，求使质子重返 P 点的入射角 \(\theta\)）**：
  当磁场反向（向外）时，质子从 \(Q(0, l\tan\theta)\) 射入后顺时针偏转（走圆心角为 \(\pi + 2\theta\) 的优弧），在 \(Q\) 点正下方距离 \(d = 2R\cos\theta\) 的 \(U(0, l\tan\theta - 2R\cos\theta)\) 处射出，且出射速度方向指向**左上方**（与 \(-x\) 轴夹角为 \(\theta\)，斜率为 \(-\tan\theta\)）。
  要使出射直线恰好经过 \(P(-l, 0)\)，出射点 \(U\) 与入射点 \(Q\) 必须关于过 \(P\) 点的水平轴 \(y = 0\) 对称，即 \(y_U = -l\tan\theta\)：
  \[
  2 l\tan\theta = d = 2 R\cos\theta \implies R\sin^2\theta + l\sin\theta - R = 0.
  \]
  解此二次方程并取正根（\(0 \le \theta \le \pi/2\)，代入 \(R = \frac{mv}{eB}\)），得：
  \[
  \theta = \arcsin\left[\sqrt{\left(\frac{e B l}{2 m v}\right)^2 + 1} - \frac{e B l}{2 m v}\right].
  \]
- **第 4 问（磁场区同时保持恒定静电势 \(V \neq 0\) 时的间距 \(d\)）**：
  边界处的静电力垂直于边界（沿 \(x\) 方向），故质子跨越边界时切向速度守恒：\(v_y' = v_y = v\sin\theta\)。
  由总机械能守恒 \(\frac{1}{2}m v'^2 + eV = \frac{1}{2}m v^2\)，进入场区后的法向速度分量为：
  \[
  v_x' = v'\cos\theta' = \sqrt{v'^2 - v^2\sin^2\theta} = \sqrt{v^2\cos^2\theta - \frac{2eV}{m}}.
  \]
  代入第 2 问公式 \(d = \frac{2 m v'\cos\theta'}{e B} = \frac{2 m v_x'}{e B}\)，立得：
  \[
  d = \frac{2m}{eB}\sqrt{v^2\cos^2\theta - \frac{2eV}{m}}.
  \]

#### 二、对照官方解答与教学拆解
- **完全吻合**：四问结果与官方参考解答完全一致。用「法向速度分量直接决定弦长 \(d = \frac{2 m v_{x,\text{in}}}{eB}\)」的观点看第 4 问，可以直接由一维法向动能定理 \(\frac{1}{2}m v_x'^2 = \frac{1}{2}m v_x^2 - eV\) 一步写出答案。

---

### 20. `plancks-2021-final-combined-slice-q10` — Statistical Mechanics of Pressure, Buoyancy and Soap Bubbles

- **难度分级**：D4
- **核心物理模型**：外势约束气体的正则系综局域压强定义、阿基米德浮力微观统计推导与肥皂泡气压计
- **教学标签**：`统计物理` `正则系综` `局域压强与软球探针极限` `阿基米德浮力微观推导` `Young-Laplace肥皂泡方程`

#### 一、题目概述与拆解
- **第 1 部分：不同约束几何下的粒子数密度分布**
  - **1.1 正则系综推导**：对 \(N\) 个无相互作用粒子，对动量积分后单粒子空间概率密度正比于 \(e^{-\beta V(\mathbf{r})}\)，故粒子数密度为：
    \[
    \rho(\mathbf{r}) = \left\langle \sum_{i=1}^N \delta(\mathbf{r} - \mathbf{r}_i)\right\rangle = C e^{-\beta V(\mathbf{r})}, \qquad C = \frac{N}{\int d^3\mathbf{r}\,e^{-\beta V(\mathbf{r})}}.
    \]
  - **1.2 三种势场的密度分布特征**：
    - **c. 边长为 \(L\) 的硬壁立方箱**：箱内 \(V(\mathbf{r}) = 0\)，密度均匀 \(\rho(\mathbf{r}) = \frac{N}{L^3}\)；箱外 \(\rho = 0\)。
    - **d. 半径为 \(R\) 的半无限竖直圆柱重力场（\(V = mgz,\ z > 0\)）**：水平截面均匀，高度方向呈玻尔兹曼指数衰减（大气压高公式）：\(\rho(\mathbf{r}) = \frac{N\beta mg}{\pi R^2}e^{-\beta mgz}\)。
    - **e. 三维谐振子势阱 \(V(\mathbf{r}) = \frac{1}{2}k|\mathbf{r}|^2\)**：呈三维各向同性高斯分布：\(\rho(\mathbf{r}) = N\left(\frac{\beta k}{2\pi}\right)^{3/2}e^{-\frac{1}{2}\beta k r^2}\)。

- **第 2 部分：作为统计量的局域压强（软球探针法）**
  - **2.1–2.3 排斥力与局域压强表达式**：
    中心在 \(\mathbf{r}_0\) 的探针球对粒子的排斥力为 \(\mathbf{F}(\mathbf{r}') = -\nabla' U_{\text{sph}}(r') = -\frac{d U_{\text{sph}}}{dr'}\hat{\mathbf{r}}'\)。在正则系综下对角度积分得径向分布函数，其中角度积分因子为：
    \[
    \mathcal{I}(r') = \int_0^{2\pi}d\phi'\int_0^\pi d\theta'\sin\theta'\,e^{-\beta V(\mathbf{r}_0 + \mathbf{r}')}.
    \]
    \(\langle \mathbf{F}\cdot\hat{\mathbf{r}}' \rangle\) 表示气体粒子与探针球碰撞在径向传递的平均总法向力，除以球面积 \(4\pi R^2\) 即为球面承受的局域压强 \(P(\mathbf{r}_0) = \frac{\langle \mathbf{F}\cdot\hat{\mathbf{r}}' \rangle}{4\pi R^2}\)。
  - **2.4 硬壁极限（\(U_0 \to +\infty\)）积分恒等式证明**：
    利用恒等式 \(\left[-\frac{dU_{\text{sph}}}{dr'}\right]e^{-\beta U_{\text{sph}}(r')} = \frac{1}{\beta}\frac{d}{dr'}\left(e^{-\beta U_{\text{sph}}(r')}\right)\)，当 \(U_0 \to +\infty\) 时，\(e^{-\beta U_{\text{sph}}(r')} \to \Theta(r' - R)\)，其导数为狄拉克 \(\delta\) 函数 \(\delta(r' - R)\)（或用分部积分法），立得：
    \[
    \int_0^\infty dr'\,r'^2\left[-\frac{dU_{\text{sph}}}{dr'}\right]e^{-\beta U_{\text{sph}}(r')}\mathcal{I}(r') = \frac{1}{\beta}\int_0^\infty dr'\,r'^2\delta(r' - R)\mathcal{I}(r') = \frac{1}{\beta}R^2\mathcal{I}(R).
    \]
  - **2.5 慢变外势下的理想气体局域状态方程**：
    当 \(V(\mathbf{r})\) 在探针半径 \(R\) 尺度上缓慢变化时，\(\mathcal{I}(R) \approx 4\pi e^{-\beta V(\mathbf{r}_0)}\)，且分母配分函数积分可忽略探针体积，代入得：
    \[
    P(\mathbf{r}_0) = \frac{N}{4\pi R^2}\frac{\frac{1}{\beta}R^2 \cdot 4\pi e^{-\beta V(\mathbf{r}_0)}}{\int d^3\mathbf{r}\,e^{-\beta V(\mathbf{r})}} = k_B T \rho(\mathbf{r}_0).
    \]
    取硬壁容器势（体积 \(V_b\) 内 \(V=0\)，外部 \(V=+\infty\)），则 \(\rho = N/V_b\)，还原出 \(P = \frac{N k_B T}{V_b}\)。
  - **2.6 谐振子势阱 \(V(r) = \frac{1}{2}kr^2\) 中的压强与一阶修正**：
    探针球位于原点时，\(\mathcal{I}(R) = 4\pi e^{-\frac{1}{2}\beta k R^2}\)，分母高斯积分为 \(\left(\frac{2\pi}{\beta k}\right)^{3/2}\)。定义有效体积 \(V_{\text{eff}} = \frac{4\pi}{3}\left(\frac{k_B T}{k}\right)^{3/2}\)（或 \(\left(\frac{2\pi k_B T}{k}\right)^{3/2}\)），精确压强与小 \(k\) 展开为：
    \[
    P_{\text{sph}} = N k_B T\left(\frac{k}{2\pi k_B T}\right)^{3/2} e^{-\frac{k R^2}{2 k_B T}} = \sqrt{\frac{2}{9\pi}}\frac{N k_B T}{V_{\text{eff}}}\left(1 - \frac{k R^2}{2 k_B T} + \cdots\right).
    \]
    一阶修正项 \(-\frac{k R^2}{2 k_B T} < 0\) 为负，因为球面 \(r = R\) 处的势能高于中心原点，导致球面处气体密度（或粒子动能）低于中心处。

- **第 3 部分：阿基米德浮力原理的微观统计推导**
  - **3.1–3.2 沿 \(\hat{\mathbf{u}}\) 方向的平均力与常势场零浮力解释**：
    气体对球施加的力与球对气体的排斥力方向相反，投影到 \(\hat{\mathbf{u}}\)（取为 \(z'\) 轴，\(\hat{\mathbf{r}}'\cdot\hat{\mathbf{u}} = \cos\theta'\)）即得题给公式。当 \(V(\mathbf{r}) = \text{const}\) 时，\(\int_0^\pi \cos\theta'\sin\theta'\,d\theta' = 0 \implies \mathcal{J}(r') = 0\)，因为各向同性均匀气压在球面各处对称抵消，无净浮力。
  - **3.3 硬壁极限下导出阿基米德定律**：
    取 \(\hat{\mathbf{u}}\) 沿 \(\nabla V(\mathbf{r}_0)\) 方向，在 \(\mathbf{r}_0\) 附近作一阶泰勒展开：
    \[
    e^{-\beta V(\mathbf{r}_0 + \mathbf{r}')} \approx e^{-\beta V(\mathbf{r}_0)}\Big(1 - \beta |\nabla V(\mathbf{r}_0)| r'\cos\theta'\Big).
    \]
    代入角度积分 \(\mathcal{J}(R)\)，常数项积分为 \(0\)，一次项给出：
    \[
    \mathcal{J}(R) = -2\pi\beta R|\nabla V(\mathbf{r}_0)|e^{-\beta V(\mathbf{r}_0)}\int_0^\pi \cos^2\theta'\sin\theta'\,d\theta' = -\frac{4\pi}{3}\beta R|\nabla V(\mathbf{r}_0)|e^{-\beta V(\mathbf{r}_0)}.
    \]
    结合 2.4 问的径向极限 \(\frac{1}{\beta}R^2\mathcal{J}(R)\)，消去 \(\beta\) 即得矢量浮力公式：
    \[
    \mathbf{F} = -\frac{4}{3}\pi R^3 \rho(\mathbf{r}_0)\big(-\nabla V(\mathbf{r}_0)\big).
    \]
    在均匀重力场 \(V(z) = mgz\) 中，\(-\nabla V = -mg\hat{\mathbf{z}}\)，故向上浮力大小为 \(F_A = V_b \rho(z) mg\)（恰好等于排开流体的重量）！

- **第 4 部分：肥皂泡作为局域气压计**
  - **4.1 导出 Young–Laplace 方程**：
    按题设 \(E_{\text{surf}} = \gamma A = 4\pi R^2\gamma\)，当半径虚位移 \(dR\) 时，\(dE_{\text{surf}} = 8\pi\gamma R\,dR\)。由虚功原理 \((P_{\text{in}} - P_{\text{out}})4\pi R^2 dR = dE_{\text{surf}} = 8\pi\gamma R\,dR\)，得：
    \[
    P_{\text{out}} - P_{\text{in}} = -\frac{2\gamma}{R}.
    \]
  - **4.2 外部气压与半径的一一对应关系**：
    泡内理想气体压强为 \(P_{\text{in}} = \frac{N k_B T}{\frac{4}{3}\pi R^3}\)，故：
    \[
    P_{\text{out}}(R) = \frac{N k_B T}{\frac{4}{3}\pi R^3} - \frac{2\gamma}{R}.
    \]
    在任何物理区域（\(P_{\text{out}} > 0\)，即 \(\frac{3 N k_B T}{4\pi R^3} > \frac{2\gamma}{R}\)）内，对 \(R\) 求导得：
    \[
    \frac{dP_{\text{out}}}{dR} = -\frac{9 N k_B T}{4\pi R^4} + \frac{2\gamma}{R^2} < -\frac{6\gamma}{R^2} + \frac{2\gamma}{R^2} = -\frac{4\gamma}{R^2} < 0.
    \]
    由于导数恒负，\(P_{\text{out}}(R)\) 在 \(P_{\text{out}} > 0\) 的全部物理定义域内是**严格单调递减函数（单射）**，故测量肥皂泡半径 \(R\) 可唯一确定外部气压 \(P_{\text{out}}\)。

#### 二、对照官方解答与教学拆解
- **完全吻合**：全部推导与官方解答完全一致，且我们在 4.2 问中给出了 \(P_{\text{out}} > 0 \implies \frac{dP_{\text{out}}}{dR} < -\frac{4\gamma}{R^2} < 0\) 的严格单调性不等式证明。

---

### 21. `plancks-2021-final-combined-slice-q11` — Medical Physics

- **难度分级**：D2
- **核心物理模型**：医学核磁共振 (NMR) 中的拉莫尔进动、旋转参考系变换与射频脉冲拉比翻转
- **教学标签**：`原子与医学物理` `核磁共振(NMR)` `拉莫尔进动` `旋转参考系变换` `拉比振荡与π/2脉冲`

#### 一、题目概述与拆解
质子置于均匀静磁场 \(\vec{B}_0 = B_0\hat{z}\) 中，磁矩与总角动量满足 \(\vec{\mu} = \gamma\vec{J}\)，初始时刻 \(\vec{\mu}\) 与 \(\vec{B}_0\) 夹角为 \(\theta_0\)。
- **第 1 问（磁矩运动方程与拉莫尔进动证明）**：
  磁场对磁矩施加的力矩为 \(\vec{\tau} = \frac{d\vec{J}}{dt} = \vec{\mu}\times\vec{B}_0\)。代入 \(\vec{\mu} = \gamma\vec{J}\) 得运动方程：
  \[
  \frac{d\vec{\mu}}{dt} = \gamma\,\vec{\mu}\times\vec{B}_0.
  \]
  证明进动：
  1. 两边点乘 \(\vec{\mu}\) 得 \(\vec{\mu}\cdot\frac{d\vec{\mu}}{dt} = 0 \implies |\vec{\mu}| = \text{const}\)（磁矩模长不变）；
  2. 两边点乘 \(\vec{B}_0\) 得 \(\frac{d\mu_z}{dt} = 0 \implies \mu_z = |\vec{\mu}|\cos\theta_0 = \text{const}\)（与磁场夹角 \(\theta_0\) 恒定）；
  3. 横向分量满足 \(\dot{\mu}_x = \gamma B_0\mu_y,\ \dot{\mu}_y = -\gamma B_0\mu_x\)，解得 \(\mu_x(t) = |\vec{\mu}|\sin\theta_0\cos(\omega_0 t + \phi_0),\ \mu_y(t) = -|\vec{\mu}|\sin\theta_0\sin(\omega_0 t + \phi_0)\)，即磁矩绕 \(\vec{B}_0\) 轴做匀速圆锥进动。
- **第 2 问（进动角频率 \(\omega_0\)）**：
  由 \(|d\vec{\mu}| = |\vec{\mu}|\sin\theta_0\,d\phi = \gamma|\vec{\mu}|B_0\sin\theta_0\,dt\)，立得拉莫尔进动频率：
  \[
  \omega_0 = \frac{d\phi}{dt} = \gamma B_0.
  \]
- **第 3 问（旋转参考系 \((x', y', z')\) 中的运动方程）**：
  旋转参考系角速度为 \(\vec{\Omega} = -\omega_0\hat{z}\)。由惯性系与旋转系的时间导数算子关系 \(\left(\frac{d\vec{\mu}}{dt}\right)_{\text{lab}} = \left(\frac{d\vec{\mu}}{dt}\right)_{\text{rot}} + \vec{\Omega}\times\vec{\mu}\)：
  \[
  \left(\frac{d\vec{\mu}}{dt}\right)_{\text{rot}} = \gamma\,\vec{\mu}\times\vec{B}_0 - \vec{\Omega}\times\vec{\mu} = \gamma\,\vec{\mu}\times\left(\vec{B}_0 + \frac{\vec{\Omega}}{\gamma}\right) = \gamma\,\vec{\mu}\times\left(B_0\hat{z} - \frac{\omega_0}{\gamma}\hat{z}\right) = \vec{0}.
  \]
  故在旋转系中磁矩保持恒定静止。
- **第 4 问（共振射频脉冲 \(\vec{B}_1(t)\) 下绕 \(x'\) 轴的进动）**：
  外加圆偏振射频场 \(\vec{B}_1(t) = B_1\cos(\omega t)\hat{x} - B_1\sin(\omega t)\hat{y}\) 同样以角速度 \(-\omega\hat{z}\) 在 \(xy\) 平面内顺时针旋转。当满足共振条件 \(\omega = \omega_0\) 时，该射频场与旋转系同步，在旋转系中表现为沿 \(x'\) 轴的恒定磁场 \(\vec{B}_1 = B_1\hat{x}'\)！
  此时旋转系运动方程化为：
  \[
  \left(\frac{d\vec{\mu}}{dt}\right)_{\text{rot}} = \gamma\,\vec{\mu}\times\left[\left(B_0 - \frac{\omega_0}{\gamma}\right)\hat{z}' + B_1\hat{x}'\right] = \gamma\,\vec{\mu}\times(B_1\hat{x}').
  \]
  这表明在旋转系中，磁矩以拉比角频率 \(\omega_1 = \gamma B_1\) 绕 \(x'\) 轴做匀速进动。
- **第 5 问（将磁矩翻转到 \(y'\) 轴所需的脉冲时间 \(\tau\)）**：
  绕 \(x'\) 轴旋转发生在 \(y'z'\) 平面内。若初始时刻磁矩位于 \(y'z'\) 平面且与 \(z'\) 轴夹角为 \(\theta_0\)，则将其翻转到 \(y'\) 轴（\(\theta = \pi/2\)）需转过角度 \(\Delta\theta = \frac{\pi}{2} - \theta_0\)，所需脉冲持续时间为：
  \[
  \tau = \frac{\frac{\pi}{2} - \theta_0}{\omega_1} = \frac{\frac{\pi}{2} - \theta_0}{\gamma B_1} \quad \left(\text{特例：若从 }\theta_0 = 0\text{ 的平衡态出发，则为 }\frac{\pi}{2\gamma B_1}\right).
  \]

#### 二、对照官方解答与教学拆解
- **完全吻合**：与官方参考解答完全一致，特别是第 5 问保留了第 1 问给定的初始角 \(\theta_0\)，得到 \(\tau = \frac{\pi/2 - \theta_0}{\gamma B_1}\)。

---

### 22. `plancks-2021-final-combined-slice-q12` — Optics

- **难度分级**：D3
- **核心物理模型**：光纤通信中的热光干涉、色散展宽带宽极限、克尔自相位调制 (SPM) 与光孤子形成
- **教学标签**：`光学与激光物理` `光学干涉与热光效应` `群速度色散展宽` `非线性光学克尔效应` `自相位调制与光孤子`

#### 一、题目概述与拆解
- **第 1 问（双光束到达时间差）**：
  光脉冲分别穿过 \(L = 1\text{ m}\) 的空气（\(n_{\text{air}} = 1.000\)）和石英玻璃（\(n_g = 1.458\)），到达靶的时间差为：
  \[
  \Delta t = \frac{L(n_g - n_{\text{air}})}{c} = \frac{1\text{ m} \times (1.458 - 1.000)}{3.000 \times 10^8\text{ m/s}} = 1.527 \times 10^{-9}\text{ s} = 1.527\text{ ns}.
  \]
- **第 2 问（相长干涉变相消干涉的最小温度变化）**：
  从相长干涉变为相消干涉，光程差需改变半个波长 \(\Delta(\text{OPD}) = L\frac{dn_g}{dT}\Delta T = \frac{\lambda_0}{2}\)。代入 \(\lambda_0 = 590\text{ nm},\ L = 1\text{ m},\ \frac{dn_g}{dT} = 8.7 \times 10^{-6}\text{ K}^{-1}\)：
  \[
  \Delta T = \frac{\lambda_0}{2 L (dn_g/dT)} = \frac{590 \times 10^{-9}}{2 \times 1 \times 8.7 \times 10^{-6}} \approx 0.03391\text{ K}.
  \]
- **第 3 问（300 km 光纤色散限制下的最大传输频率 \(F\)）**：
  设数据传输频率为 \(F\)，每个脉冲时隙为 \(2\tau = \frac{1}{F} \implies \tau = \frac{1}{2F}\)。高斯脉冲满足 \(\Delta t \cdot \Delta f = 1 \implies \Delta f = \frac{1}{\tau} = 2F\)，对应波长宽度 \(\Delta\lambda = \frac{\lambda_0^2}{c}\Delta f = \frac{2\lambda_0^2 F}{c}\)。
  经过 \(L = 300\text{ km} = 3 \times 10^5\text{ m}\) 传播后，不同波长分量的群/相时延展宽为 \(\Delta t_{\text{travel}} = \frac{L}{c}\left|\frac{dn}{d\lambda}\right|\Delta\lambda\)。要求展宽不超过初始脉宽的 \(25\%\)（即 \(\Delta t_{\text{travel}} \le 0.25\tau = \frac{0.25}{2F}\)）：
  \[
  \frac{L}{c}\left|\frac{dn}{d\lambda}\right|\frac{2\lambda_0^2 F}{c} \le \frac{0.25}{2F} \implies F^2 \le \frac{0.25\,c^2}{4 L \lambda_0^2 |dn/d\lambda|} = \frac{0.25\,f_0^2}{4 L |dn/d\lambda|}.
  \]
  代入 \(f_0 = \frac{c}{\lambda_0} = 1.9355 \times 10^{14}\text{ Hz}\)，\(\left|\frac{dn}{d\lambda}\right| = 5.4 \times 10^{-6}\text{ nm}^{-1} = 5.4 \times 10^3\text{ m}^{-1}\)，\(L = 3 \times 10^5\text{ m}\)：
  \[
  F^2 \le 1.445 \times 10^{18}\text{ Hz}^2 \implies F_{\max} \approx 1.202 \times 10^9\text{ Hz} = 1.202\text{ GHz}
  \]
  （注：官方解答算出了完全相同的 \(F^2 = 1.445 \times 10^{18}\text{ Hz}^2\)，但在开平方时笔误写成了 \(1.700\text{ GHz}\)）。
- **第 4 问（克尔非线性效应引起的 1 m 光纤脉冲频谱展宽）**：
  对底宽 \(\tau = 200\text{ ps}\)、能量 \(E = 200\text{ nJ}\)、直径 \(D = 10\ \mu\text{m}\) 的三角形脉冲：
  - 光纤横截面积：\(A = \frac{\pi D^2}{4} = 7.854 \times 10^{-11}\text{ m}^2\)；
  - 三角形峰值功率与峰值光强：\(P_p = \frac{2E}{\tau} = 2.000 \times 10^3\text{ W}\)，\(I_p = \frac{P_p}{A} = 2.546 \times 10^{13}\text{ W/m}^2\)；
  - 峰值非线性折射率变化：\(\Delta n_p = n_2 I_p = 3.0 \times 10^{-20} \times 2.546 \times 10^{13} = 7.639 \times 10^{-7}\)；
  - 前沿（历时 \(\tau/2 = 100\text{ ps}\)）折射率随时间的变化率：\(\frac{d(\Delta n)}{dt} = \frac{\Delta n_p}{10^{-10}\text{ s}} = 7.639 \times 10^3\text{ s}^{-1}\)；
  - 传播 \(L = 1\text{ m}\) 时的光程变化率（等效多普勒退行速度）：\(v_{\text{eff}} = L\frac{d(\Delta n)}{dt} = 7.639 \times 10^3\text{ m/s}\)。
  由多普勒频移公式（或自相位调制公式 \(\delta f = -\frac{v_{\text{eff}}}{c}f_0\)），脉冲前沿产生的红移量为：
  \[
  \delta f = -\frac{v_{\text{eff}}}{c}f_0 = -\frac{7.639 \times 10^3}{3.000 \times 10^8}\times 1.9355 \times 10^{14}\text{ Hz} = -4.929 \times 10^9\text{ Hz} \quad (\Delta\lambda \approx +0.0395\text{ nm}).
  \]
  脉冲后沿对称地产生等量蓝移（\(+4.929\text{ GHz}\)）。初始高斯频宽为 \(\Delta f_0 = \frac{1}{\tau} = 5.00 \times 10^9\text{ Hz}\)，故经 \(1\text{ m}\) 非线性传播后的总频谱宽度为：
  \[
  \Delta f' = \Delta f_0 + 2|\delta f| = 5.00 \times 10^9 + 2 \times 4.929 \times 10^9 = 1.486 \times 10^{10}\text{ Hz} = 14.86\text{ GHz} \quad (0.119\text{ nm}).
  \]
- **第 5 问（50 km 反常色散与非线性平衡的孤子脉冲能量计算）**：
  在 \(1550\text{ nm}\) 反常色散区，脉冲前沿非线性红移（波长变长、群速度变慢），后沿非线性蓝移（波长变短、群速度变快）。设非线性相移发生在起始长度 \(L_{\text{NL}} = 1\text{ m}\) 内，使脉冲总频宽变为 \(\Delta f' = \Delta f_0 + 2|\delta f|\)。
  经过 \(L_{\text{disp}} = 50\text{ km} = 5 \times 10^4\text{ m}\) 传播后，要求前后沿极值频率到达时间差恰好为 \(\Delta t_{\text{travel}} = 100\text{ ps} = 10^{-10}\text{ s}\)：
  \[
  \Delta t_{\text{travel}} = \frac{L_{\text{disp}}}{c}\left|\frac{dn}{df}\right|\Delta f' = 10^{-10}\text{ s}, \qquad \left|\frac{dn}{df}\right| = \left|\frac{dn}{d\lambda}\right|\frac{c}{f_0^2} = 4.324 \times 10^{-17}\text{ Hz}^{-1}.
  \]
  由此解出所需的总频宽：
  \[
  \Delta f' = \frac{c \times 10^{-10}}{L_{\text{disp}}|dn/df|} = \frac{3 \times 10^8 \times 10^{-10}}{5 \times 10^4 \times 4.324 \times 10^{-17}} \approx 1.388 \times 10^{10}\text{ Hz} = 13.88\text{ GHz}.
  \]
  - **精确物理计算**：所需双边非线性频移为 \(2|\delta f| = \Delta f' - \Delta f_0 = (13.88 - 5.00)\text{ GHz} = 8.88\text{ GHz}\)，即单边频移 \(|\delta f| = 4.44\text{ GHz}\)。由于 \(|\delta f| \propto E\)，对比第 4 问（当 \(E = 200\text{ nJ}\) 时 \(|\delta f| = 4.929\text{ GHz}\)），若非线性作用长度为 \(L_{\text{NL}} = 1\text{ m}\)，所需脉冲能量为 \(E = 200\text{ nJ} \times \frac{4.44}{4.929} \approx 180\text{ nJ}\)（若把 \(L = 50\text{ km}\) 代入 \(v\) 则再除以 \(5\times 10^4\)）。
  - **官方解答算式说明**：官方解答在将相对论多普勒公式 \(\Delta f = -\left(1 - \sqrt{\frac{1-v/c}{1+v/c}}\right)f\) 作非相对论近似时，误将 \(1 - \frac{1}{1+v/c} = \frac{v}{c+v}\) 写成了 \(\frac{c}{c+v}\)（漏减了 \(1\)！），并把 \(L = 50\text{ km}\) 同时代入了 \(v\)，从而算出了 \(6.852\text{ mJ}\)。我们在笔记中同时给出正确的多普勒/SPM 线性近似与官方解答原式，方便读者对照核查。

#### 二、对照官方解答与教学拆解
- **两处官方解答勘误总结**：
  1. 第 3 问末尾：\(\sqrt{1.445 \times 10^{18}\text{ Hz}^2} = 1.202\text{ GHz}\)（官方解答笔误写作 \(1.700\text{ GHz}\)）；
  2. 第 5 问多普勒近似：\(1 - \sqrt{\frac{1-v/c}{1+v/c}} \approx \frac{v}{c}\)（官方解答误写作 \(\frac{c}{c+v}\)，在 \(v \ll c\) 时趋于 \(1\) 而非 \(0\)）。
