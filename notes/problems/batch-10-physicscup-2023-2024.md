# Batch 10: Physics Cup 2023–2024 独立试做与教学拆解报告

本报告严格遵循两阶段协议（Phase 1 独立盲做推导 + Phase 2 对照官方获奖解答与 Jaan Kalda 评述进行教学拆解），涵盖 Physics Cup 2023 与 2024 全部 10 道题目。

---

## 1. `physicscup-2023-q1-reader` — Sinking cylinder (下沉的圆柱)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  半径为 \(R\)、高为 \(H\)、密度为 \(\rho_c\) 的均匀实心圆柱浸没在密度为 \(\rho_w\) 的无粘水中，底面距刚性平底距离为 \(z(t)\)（初始 \(z(0)=h\)）。已知 \(\rho_c > \rho_w\)，\(H < R\)，且 \(10\rho_c h \ll \rho_w R\)。
  由于缝隙极薄（\(h \ll R\)），当圆柱以速度 \(\dot{z} < 0\) 下沉时，圆柱底面下方狭缝中的水被强行向四周径向挤出，其径向流速 \(v_r\) 远大于圆柱下沉速度 \(|\dot{z}|\)，因此系统绝大部分动能集中在狭缝内径向被挤出的水体中。
- **连续性方程与流体动能**：
  在底面狭缝内取半径为 \(r\)（\(r \le R\)）、高为 \(z\) 的同轴圆柱控制体。由不可压缩流体的体积守恒：
  \[
  \pi r^2 (-\dot{z}) = 2\pi r z v_r(r) \implies v_r(r) = -\frac{r \dot{z}}{2z}
  \]
  检验竖直分量动能与径向动能之比：\(v_z \sim \dot{z}\)，故 \(E_{k,z} / E_{k,r} \sim (z/R)^2 \ll 1\)；而圆柱外部（\(r > R\)）流体的特征尺度为 \(R\)，流速 \(\sim \dot{z}(R/R) \sim \dot{z}\)，附加质量为 \(\mathcal{O}(\rho_w R^3)\)。
  狭缝内径向流动的总动能为：
  \[
  T_w = \int_0^R \frac{1}{2} \rho_w v_r^2 (2\pi r z \, \mathrm{d}r) = \frac{\pi \rho_w \dot{z}^2}{4z} \int_0^R r^3 \, \mathrm{d}r = \frac{\pi \rho_w R^4}{16 z} \dot{z}^2
  \]
  这相当于一个随位置 \(z\) 变化的等效质量 \(M_{\text{eff}}(z) = \frac{\pi \rho_w R^4}{8z}\)。对比圆柱自身质量 \(m_c = \pi R^2 H \rho_c\)，比值为：
  \[
  \frac{m_c}{M_{\text{eff}}(z)} = \frac{8 \rho_c H z}{\rho_w R^2} \le \frac{8 \rho_c H h}{\rho_w R^2} \ll 1
  \]
  （因为 \(H < R\) 且 \(10\rho_c h \ll \rho_w R\)）。因此圆柱自身动能与外部附加质量动能均可忽略（或作为一阶小量修正）。
- **机械能守恒与运动方程求解**：
  由机械能守恒（无粘流体且无涡），重力与浮力的合力做功全部转化为流体动能：
  \[
  \frac{\pi \rho_w R^4}{16 z} \dot{z}^2 + \frac{1}{2}\pi R^2 H \rho_c \dot{z}^2 = (\rho_c - \rho_w)\pi R^2 H g (h - z)
  \]
  先看主领阶（忽略圆柱惯性项）：
  \[
  \dot{z}^2 = \frac{16(\rho_c - \rho_w)g H}{\rho_w R^2} z(h - z) = \omega^2 z(h - z), \quad \omega = \frac{4}{R}\sqrt{\frac{(\rho_c - \rho_w)g H}{\rho_w}}
  \]
  分離变量积分（或令 \(z = h \cos^2\theta\)，\(\mathrm{d}z = -2\sqrt{z(h-z)}\,\mathrm{d}\theta\)）：
  \[
  t_{\text{fall}} = \int_0^h \frac{\mathrm{d}z}{\omega \sqrt{z(h-z)}} = \frac{\pi}{\omega} = \frac{\pi R}{4}\sqrt{\frac{\rho_w}{(\rho_c - \rho_w)g H}}
  \]
  若保留圆柱质量的一阶修正，被积函数多出因子 \(\sqrt{1 + \frac{8\rho_c H z}{\rho_w R^2}} \approx 1 + \frac{4\rho_c H z}{\rho_w R^2}\)，积分得：
  \[
  t_{\text{fall}} = \frac{\pi R}{4}\sqrt{\frac{\rho_w}{(\rho_c - \rho_w)g H}}\left(1 + \frac{2\rho_c H h}{\rho_w R^2}\right)
  \]

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做结果与官方完全一致！
  - **Eyal Walach 的经典踩坑与自救**：Eyal 在解答前半部分直接写下了错误公式 \(a = F_{\text{tot}} / M_{\text{eff}}(h) \propto h\)，误以为 \(h\) 做简谐振动且落底时间为 \(T/4 = \frac{\pi}{2\omega}\)（少了一个因子 2）！随后他在第二页意识到变质量系统不能直接用 \(F = M_{\text{eff}}a\)，而是应当对机械能守恒求导得到 \(2h\ddot{h} - \dot{h}^2 + \omega^2 h^2 = 0\)，并通过令 \(u = \sqrt{h}\) 化为 \(\ddot{u} + (\omega/2)^2 u = 0\)，发现是 \(\sqrt{h}\) 做简谐运动，从而修正了因子 2。
  - **Chung Wang Lam 与付礼中 (Lizhong Fu)** 保留了圆柱自身动能的一阶修正项 \(\left(1 + \frac{2\rho_c H h}{\rho_w R^2}\right)\)，获得了高精度奖励。
  - **Liao Haoding** 使用欧拉方程（或非定常伯努利方程）计算底面径向压强分布 \(p(r) - p(R)\)，再对底面积分求总压力，殊途同归。
- **核心难点与易错点**：
  1. **变有效质量系统的动力学陷阱（头号易错点）**：流体动能形式为 \(T = \frac{1}{2}M(z)\dot{z}^2\)，拉格朗日方程给出的是 \(M(z)\ddot{z} + \frac{1}{2}M'(z)\dot{z}^2 = F_z\)，绝非 \(M(z)\ddot{z} = F_z\)！因为当 \(z\) 减小时，不仅流体在加速，而且相同下沉速度 \(\dot{z}\) 对应的径向挤压比 \(R/(2z)\) 也在急剧增大（对流加速度项），这会产生巨大的向上缓冲反冲力，使得圆柱接近底部时反而**减速**并在触底瞬间速度降为零（软着陆，\(\dot{z} \propto \sqrt{z(h-z)}\)）。
  2. **下落时间与初始高度 \(h\) 无关的物理反直觉性**：主领阶结果中 \(h\) 完全消去，这是由于 \(z\) 越小时等效质量 \(M_{\text{eff}} \propto 1/z\) 越大，具备尺度不变性（等同于 \(\sqrt{z}\) 的简谐振动周期与振幅 \(\sqrt{h}\) 无关）。

---

## 2. `physicscup-2023-q2-reader` — Phase transitions in a wire (导线中的相变)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  细长导线长度 \(L\)，截面积 \(A\)（含极微小不均匀性），单位长度向环境散热功率为 \(W = \alpha(T - T_0)\)。电阻率在 \(T < T_c\) 时为 \(\rho_1\)，在 \(T > T_c\) 时突变为 \(\rho_2 = 2\rho_1\)。已知 \(P_0 = \alpha L(T_c - T_0)\)，\(V_0 = L\sqrt{\alpha \rho_1(T_c - T_0)/A}\)。
  两端电压 \(V(t)\) 极其缓慢地线性增加，直到整根导线完成相变，再以相同速率线性降回 0。
- **如果完全忽略纵向导热的悖论与纵向导热的必要性**：
  在均匀低温相（\(\rho = \rho_1\)）中，焦耳热与散热平衡：\(I^2 \rho_1 / A = \alpha(T - T_0)\)。当温度达到 \(T_c\) 时，临界电流为：
  \[
  I_{\uparrow} = \sqrt{\frac{\alpha A (T_c - T_0)}{\rho_1}} = \frac{P_0}{V_0}
  \]
  此时电压恰为 \(V_0\)，功率为 \(P_0\)。
  当 \(V\) 刚超过 \(V_0\) 时，导线最细（或 \(\alpha A\) 最小）的缺陷处率先达到 \(T_c\) 并转变为高阻相 \(\rho_2 = 2\rho_1\)。一旦该微元变为 \(\rho_2\)，在相同电流 \(I\) 下其发热功率翻倍（\(2I^2\rho_1/A\)），温度瞬间飙升至 \(T_2 > T_c\)！
  此时题目条件 (b) 极其关键：“沿导线的热通量**几乎处处（almost everywhere）**可以忽略”。为什么是“几乎处处”？因为在两相交界面（相畴壁，domain wall）处存在温度阶跃，纵向热传导率 \(\kappa\) 虽小，但在宽度 \(\delta \sim \sqrt{\kappa A / \alpha} \ll L\) 的交界区内温度梯度极大，纵向热传导直接决定了**相界面的移动方向与平衡条件**！
- **相界面平衡电流 \(I_t\) 的推导**：
  设沿导线坐标为 \(x\)，相界面位于 \(x = 0\)（\(x < 0\) 为高温相 \(\rho_2\)，\(x > 0\) 为低温相 \(\rho_1\)）。定常一维热传导方程为：
  \[
  \kappa A \frac{\mathrm{d}^2 T}{\mathrm{d}x^2} + \frac{I^2 \rho(x)}{A} - \alpha(T - T_0) = 0
  \]
  在远离界面的内部，\(T_1 = T_0 + \frac{I^2 \rho_1}{\alpha A}\)，\(T_2 = T_0 + \frac{I^2 \rho_2}{\alpha A}\)。
  在 \(x = 0\) 处，温度连续且等于相变温度 \(T(0) = T_c\)，热流连续即 \(\left.\frac{\mathrm{d}T}{\mathrm{d}x}\right|_{0^-} = \left.\frac{\mathrm{d}T}{\mathrm{d}x}\right|_{0^+}\)。
  将方程两边乘以 \(\frac{\mathrm{d}T}{\mathrm{d}x}\) 并在 \((-\infty, +\infty)\) 积分（或直接用指数衰减解 \(T(x) = T_1 + (T_c - T_1)e^{-x/\lambda}\) 和 \(T(x) = T_2 - (T_2 - T_c)e^{x/\lambda}\)，注意到两相中特征衰减长度 \(\lambda = \sqrt{\kappa A / \alpha}\) 相同！）：
  由一阶导数连续：
  \[
  \frac{T_2 - T_c}{\lambda} = \frac{T_c - T_1}{\lambda} \implies \frac{T_1 + T_2}{2} = T_c
  \]
  即两相远离界面的稳态温度算术平均值必须等于 \(T_c\)！代入 \(\rho_2 = 2\rho_1\)：
  \[
  \frac{1}{2}\left(1 + 2\right)\frac{I_t^2 \rho_1}{\alpha A} = T_c - T_0 \implies I_t = \sqrt{\frac{2}{3}} I_{\uparrow} = \sqrt{\frac{2}{3}} \frac{P_0}{V_0}
  \]
- **全过程分段演化分析**：
  设高温相（\(\rho_2\)）占导线总长的比例为 \(f \in [0, 1]\)，则总电阻为 \(R(f) = (1 + f)R_1\)，其中 \(R_1 = \rho_1 L / A = V_0^2 / P_0\)。
  1. **第一段（全低温相升温）**：\(0 \le V < V_0\)。此时 \(f = 0\)，\(R = R_1\)，功率为开口向上的抛物线：
     \[
     P(V) = P_0 \left(\frac{V}{V_0}\right)^2
     \]
     在 \(V = V_0\) 时达到局部峰值 \(P = P_0\)。
  2. **第一处快速弛豫（相变触发与跌落）**：在 \(V = V_0\) 处，最薄弱点形核生成高温相。由于此时电流 \(I_{\uparrow} > I_t\)，高温相畴壁迅速向外扩张，导致总电阻 \((1+f)R_1\) 增大、电流 \(I = V_0 / [(1+f)R_1]\) 下降，直到电流降至平衡值 \(I_t = \sqrt{2/3} I_{\uparrow}\) 时相界面停止扩张！
     此时高温相比例瞬间跃变为 \(1 + f = \frac{V_0}{I_t R_1} = \sqrt{\frac{3}{2}}\)（即 \(f = \sqrt{1.5} - 1 \approx 0.225\)），功率从 \(P_0\) 迅速跌落至：
     \[
     P = V_0 I_t = \sqrt{\frac{2}{3}} P_0
     \]
  3. **第二段（两相共存与恒流扩张）**：随着 \(V\) 从 \(V_0\) 继续缓慢增大，为了维持相界面平衡，电流必须锁定在 \(I = I_t\)，高温相比例随电压线性增长：\(1 + f = \sqrt{\frac{3}{2}}\frac{V}{V_0}\)。此时 \(P = I_t V\) 随电压（时间）呈**斜率恒定的直线**：
     \[
     P(V) = \sqrt{\frac{2}{3}} P_0 \frac{V}{V_0}
     \]
     直到 \(f = 1\)（整根导线完全转变为 \(\rho_2\)），此时对应的最大电压与最大功率为：
     \[
     V_{\max} = 2 I_t R_1 = \sqrt{\frac{8}{3}} V_0, \quad P_{\max} = \frac{4}{3} P_0
     \]
  4. **第三段（全高温相降温）**：按题意，整根导线刚完成相变（在 \(V_{\max} = \sqrt{8/3}V_0\)）即开始以相同速率线性降低电压。此时整根导线处于 \(\rho_2 = 2\rho_1\) 相（没有相界面！），只要内部温度高于 \(T_c\)，就不会形核回低温相。此时 \(R = 2R_1\)，功率沿另一条抛物线下降：
     \[
     P(V) = \frac{1}{2} P_0 \left(\frac{V}{V_0}\right)^2
     \]
     直到全线温度降至 \(T_c\)，此时单相维持的最小电流为 \(I_{\downarrow} = \sqrt{\frac{\alpha A(T_c - T_0)}{2\rho_1}} = \frac{I_{\uparrow}}{\sqrt{2}}\)，对应电压与功率为：
     \[
     V_{\text{cool}} = I_{\downarrow} (2R_1) = \sqrt{2} V_0, \quad P_{\text{cool}} = P_0
     \]
  5. **第二处快速弛豫（低温相形核与功率跃升）**：在 \(V = \sqrt{2}V_0\) 时，最粗处率先冷却至 \(T_c\) 以下并形核出低温相 \(\rho_1\)。由于此时电流 \(I_{\downarrow} < I_t\)，低温相畴壁迅速扩张，总电阻减小，电流迅速回升至平衡电流 \(I_t = \sqrt{2/3} I_{\uparrow}\)，高温相比例突降为 \(1 + f = \sqrt{3/2}(\sqrt{2}) = \sqrt{3}\)（即 \(f = \sqrt{3} - 1 \approx 0.732\)）。功率在 \(V = \sqrt{2}V_0\) 处迅速从 \(P_0\) 跃升至：
     \[
     P = (\sqrt{2}V_0) I_t = \frac{2}{\sqrt{3}} P_0 = \sqrt{\frac{4}{3}} P_0
     \]
  6. **第四段（两相共存缩减）**：电压从 \(\sqrt{2}V_0\) 降至 \(f = 0\) 对应的电压 \(V_{\text{end}} = I_t R_1 = \sqrt{\frac{2}{3}} V_0\)。期间电流锁定为 \(I_t\)，功率随时间线性下降：
     \[
     P(V) = \sqrt{\frac{2}{3}} P_0 \frac{V}{V_0}
     \]
     在 \(V_{\text{end}} = \sqrt{\frac{2}{3}} V_0\) 处，低温相完全占领导线（\(f = 0\)），此时功率连续地达到 \(P_{\text{end}} = \frac{2}{3} P_0\)。
  7. **第五段（全低温相归零）**：当 \(V\) 从 \(\sqrt{2/3}V_0\) 降至 \(0\) 时，\(f = 0\)，功率沿初始抛物线回到零：
     \[
     P(V) = P_0 \left(\frac{V}{V_0}\right)^2
     \]

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 全部 5 个关键转折点的电压与功率坐标完全吻合：
    - 升温相变起点：\(V = V_0\)，功率从 \(P_0\) 极快降至 \(\sqrt{2/3}P_0\)；
    - 升温终点（折返点）：\(V = \sqrt{8/3}V_0\)，\(P = \frac{4}{3}P_0\)；
    - 降温相变起点：\(V = \sqrt{2}V_0\)，功率从 \(P_0\) 极快升至 \(\sqrt{4/3}P_0 = \frac{2}{\sqrt{3}}P_0\)；
    - 降温相变终点：\(V = \sqrt{2/3}V_0\)，\(P = \frac{2}{3}P_0\)（此处函数值连续但斜率折断）。
  - **Kalda 的精辟点评**：Kalda 特别指出，绝大多数参赛者把 \(V=V_0\) 和 \(V=\sqrt{2}V_0\) 处的功率跳变画成了数学上的绝对不连续（竖直虚线跳变），只有 Luka Passek-Kumerički 注意到题目说的是“热化特征时间远小于电压变化时间（而非零）”，因此在图上表现为极陡峭但连续的快速过渡斜线。
- **核心难点与易错点**：
  1. **忽视纵向热传导导致“两相共存条件”缺失**：如果完全令 \(\kappa = 0\)，任何电流 \(I \in (I_{\downarrow}, I_{\uparrow})\) 下高温相和低温相都各自稳定，根本无法确定两相比例 \(f(V)\)！必须引入微小的纵向导热系数 \(\kappa \to 0^+\)，通过相界面处的温度连续与热流连续，才能唯一确定畴壁不移动的麦克斯韦等面积法则/平衡电流 \(I_t = \sqrt{2/3}I_{\uparrow}\)。
  2. **过热与过冷迟滞回线（Hysteresis）物理机制**：升温时全线处于 \(\rho_1\)，必须等到 \(I = I_{\uparrow} > I_t\) 才能形核；一旦形核，系统立即跌落到双相共存态 \(I = I_t\)。同理，降温时全线处于 \(\rho_2\)，必须等到 \(I = I_{\downarrow} < I_t\) 才能形核低温相，然后跃升回 \(I_t\)。而在相变彻底完成瞬间（\(f=1\) 和 \(f=0\)），相界面消失，因此没有跳变，只有导数（斜率）间断。

---

## 3. `physicscup-2023-q3-reader` — Magnets in conducting liquid (导电液体中的磁铁)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  两个半径为 \(R\)、磁偶极矩为 \(m\) 的球形永磁体，初始球心距为 \(3R\)，磁矩方向均沿球心连线（设为 \(z\) 轴）同向排列。周围充满不可压缩的理想导电液体（电导率 \(\sigma \to \infty\)，磁通冻结，初始磁场未被排斥）。现将两磁球沿连线拉开至距离 \(L \gg R\)，估算维持该位置所需的外力 \(F\) 的量级（精确参数依赖关系）。
- **磁通冻结（Alfvén 定理）与不可压缩管体积守恒**：
  在理想磁流体（\(\sigma \to \infty\)）中，磁感线完全冻结在流体微元上。更关键的是：流体不可渗透磁球表面，因此**起止于两个磁球表面的任意一根磁通管（flux tube），其两端面积永远锚定在磁球表面上**！
  由于流体不可压缩，且流体只能沿磁感线流动或随磁通管一起变形，任何一条连接两磁球的闭合磁通管内部所包围的**流体总体积 \(V_{\text{tube}}\) 在拉伸过程中必须严格保持不变**！
- **拉伸后的磁场放大与磁能标度律**：
  在初始状态（球心距 \(3R\)，表面间距 \(R\)），连接两磁球的磁通管长度为 \(l_0 \sim R\)，截面积为 \(A_0 \sim R^2\)，体积为 \(V_0 \sim R^3\)，管内初始磁场强度量级为 \(B_0 \sim \frac{\mu_0 m}{R^3}\)，磁通量为 \(\Phi \sim B_0 A_0 \sim \frac{\mu_0 m}{R}\)。
  当两磁球被拉开至距离 \(L \gg R\) 时，这束连接两球的磁通管被拉伸成长度为 \(L\) 的细长管。
  由体积守恒（不可压缩液体）：
  \[
  A(L) \cdot L \sim V_0 \sim R^3 \implies A(L) \sim \frac{R^3}{L}
  \]
  由磁通守恒（理想导体磁通冻结）：
  \[
  B(L) \cdot A(L) = \Phi \sim B_0 A_0 \implies B(L) \sim B_0 \frac{A_0}{A(L)} \sim B_0 \frac{L}{R} \sim \frac{\mu_0 m L}{R^4}
  \]
  令人震惊的物理现象出现了：随着距离 \(L\) 增大，连接两球的磁通管因为体积守恒而变细（\(A \propto 1/L\)），导致管内磁场强度反而**正比于 \(L\) 线性增强**（\(B \propto L\)）！
- **磁场总能量与恢复力估算**：
  拉伸后磁通管内的总磁场能量为（管体积仍为 \(V_{\text{tube}} = V_0 \sim R^3\)）：
  \[
  U_B(L) \sim \frac{B(L)^2}{2\mu_0} V_{\text{tube}} \sim \frac{B_0^2}{2\mu_0} \left(\frac{L}{R}\right)^2 V_0 \sim \frac{1}{\mu_0}\left(\frac{\mu_0 m}{R^3}\right)^2 \left(\frac{L}{R}\right)^2 R^3 = \frac{\mu_0 m^2 L^2}{R^5}
  \]
  由虚功原理，维持两磁球间距为 \(L\) 所需的拉力为：
  \[
  F = \frac{\mathrm{d}U_B}{\mathrm{d}L} \sim \frac{\mu_0 m^2 L}{R^5}
  \]
  这就像一根磁流体“橡皮筋”，恢复力随拉伸距离 \(L\) 呈胡克定律式的线性增长！

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做结果 \(F \sim \frac{\mu_0 m^2 L}{R^5}\) 与官方完全一致！
  - 这道题在当年比赛极具杀伤力：直到第 2 条提示发布后才出现唯一一份正确解答（Luka Passek-Kumerički），Kalda 甚至专门邀请了前几届冠军（MIT 的 Dobrica Jovanovic 与 Princeton 的 Thomas Foster）撰写示范解答。
  - **Anindya Guria 的微分严格证明**：对于磁通量为 \(\mathrm{d}\Phi = B(z) \mathrm{d}A(z)\) 的无限细轴对称磁通管，其体积为 \(\mathrm{d}V = \int \mathrm{d}A(z)\,\mathrm{d}z = \mathrm{d}\Phi \int \frac{\mathrm{d}z}{B(z)}\)。由于每个磁通管的 \(\frac{\mathrm{d}V}{\mathrm{d}\Phi}\) 是运动不变量，在 \(L \gg R\) 时 \(B(z)\) 沿轴向均匀，故 \(\frac{\mathrm{d}V}{\mathrm{d}\Phi} \approx \frac{L}{B}\)，即 \(B \approx L \frac{\mathrm{d}\Phi}{\mathrm{d}V}\)。积分总磁能：
    \[
    U = \int \frac{B^2}{2\mu_0}\,\mathrm{d}V = \frac{L^2}{2\mu_0} \int \left(\frac{\mathrm{d}\Phi}{\mathrm{d}V}\right)^2 \mathrm{d}V \sim \frac{\mu_0 m^2 L^2}{R^5}
    \]
- **核心难点与易错点**：
  1. **只记磁通守恒、漏掉体积守恒（最普遍的错误）**：许多学生知道磁通冻结，但误以为磁通管半径保持为 \(R\)（即体积随 \(L\) 增大而变大），从而得出 \(B \sim B_0\)、\(U \propto L\)、\(F \sim \text{const}\) 的错误结论。为什么流体不能补充进磁通管？因为流体微元一旦穿过磁通管侧壁，就意味着切割磁感线（\(\vec{v} \times \vec{B} \neq 0\)），在理想导体中是不被允许的；同时两端又被刚性磁球表面封死（无滑移/不可穿透边界条件），所以每根连接两球的磁通管都是一个**完全封闭的等体积弹性袋**！
  2. **忽略非连接磁感线的合理性**：每个磁球自身回环（不连接另一球）的磁感线，在拉开至 \(L \gg R\) 时只发生局部变形，其能量保持在 \(\sim \frac{\mu_0 m^2}{R^3}\) 量级，与 \(L^2\) 项相比完全可以忽略。

---

## 4. `physicscup-2023-q4-reader` — Spaceship (宇宙飞船)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  飞船在 \(t=0\) 从地球出发，固有时为 \(\tau\)（题目记为 \(t\)，为避免与地球参考系坐标时混淆，这里记飞船固有时为 \(\tilde{\tau}\)，每段持续固有时间间隔为 \(\tau\)）。飞船固有加速度大小恒为 \(g\)，在每个 \(\tau\) 间隔末将引擎逆时针旋转 \(90^\circ\)，共经历四段（\(0 \to \tau \to 2\tau \to 3\tau \to 4\tau\)）。已知在 \(\tilde{\tau} = \tau\) 和 \(\tilde{\tau} = 4\tau\) 时刻，飞船相对地球的速度大小完全相等，均为 \(v\)。求 \(v\)。
- **方法选择：逆向速度合成 vs 四维矢量洛伦兹变换**：
  设在单段固有时间 \(\tau\) 内，飞船从瞬时静止开始以恒定固有加速度 \(g\) 直线加速，末速度大小恰为 \(v\)（因为第一段末 \(\tilde{\tau}=\tau\) 时相对地球速度为 \(v\)）。记 \(\beta = v/c\)，对应的洛伦兹因子为 \(\gamma = \frac{1}{\sqrt{1-\beta^2}} = \cosh(g\tau/c)\)，\(\beta = \tanh(g\tau/c)\)。
  设 \(S_0, S_1, S_2, S_3\) 分别为飞船在 \(\tilde{\tau} = 0, \tau, 2\tau, 3\tau\) 时刻的瞬时静止惯性系（其中 \(S_0\) 即地球系）。
  由于在每个阶段内飞船做一维双曲运动，且在每一段起点处飞船瞬时静止、引擎旋转 \(90^\circ\)（在飞船瞬时静止系中精确转过 \(90^\circ\)！）：
  - \(S_1\) 相对 \(S_0\) 的速度为 \(\vec{V}_{10} = (v, 0)\)；
  - \(S_2\) 相对 \(S_1\) 的速度为 \(\vec{V}_{21} = (0, v)\)；
  - \(S_3\) 相对 \(S_2\) 的速度为 \(\vec{V}_{32} = (-v, 0)\)；
  - 在 \(\tilde{\tau} = 4\tau\) 时刻，飞船相对 \(S_3\) 的速度为 \(\vec{u}_3 = (0, -v)\)。
  **关键技巧**：如果从 \(S_0 \to S_3\) 正向合成，由于不共线洛伦兹变换存在托马斯-维格纳转动（Thomas-Wigner rotation），非相邻参考系之间坐标轴会发生旋转；但如果采用**从 \(S_3 \to S_2 \to S_1 \to S_0\) 逐级逆向变换**，每次都是在相邻惯性系之间做单轴无转动洛伦兹变换，坐标轴始终平行对齐！
- **逐级逆向速度变换推导**：
  令 \(c = 1\)（即 \(v = \beta\)，\(\gamma^2(1-\beta^2) = 1 \implies \beta^2 = 1 - \gamma^{-2}\)）。
  1. 在 \(S_3\) 中：\(\vec{u}_3 = (0, -\beta)\)。
  2. 变换到 \(S_2\)（\(S_3\) 相对 \(S_2\) 沿 \(-x\) 方向运动，速度为 \(-\beta\)）：
     \[
     u_{2x} = -\beta, \quad u_{2y} = -\frac{\beta}{\gamma}
     \]
  3. 变换到 \(S_1\)（\(S_2\) 相对 \(S_1\) 沿 \(+y\) 方向运动，速度为 \(+\beta\)）：
     \[
     u_{1y} = \frac{u_{2y} + \beta}{1 + \beta u_{2y}} = \frac{\beta(1 - 1/\gamma)}{1 - \beta^2/\gamma} = \frac{\beta(\gamma - 1)}{\gamma - \beta^2}
     \]
     \[
     u_{1x} = \frac{u_{2x}}{\gamma(1 + \beta u_{2y})} = \frac{-\beta}{\gamma(1 - \beta^2/\gamma)} = -\frac{\beta}{\gamma - \beta^2}
     \]
  4. 变换到地球系 \(S_0\)（\(S_1\) 相对 \(S_0\) 沿 \(+x\) 方向运动，速度为 \(+\beta\)）：
     \[
     u_{0x} = \frac{u_{1x} + \beta}{1 + \beta u_{1x}} = \beta \frac{\gamma - \beta^2 - 1}{\gamma - 2\beta^2}
     \]
     \[
     u_{0y} = \frac{u_{1y}}{\gamma(1 + \beta u_{1x})} = \beta \frac{\gamma - 1}{\gamma(\gamma - 2\beta^2)}
     \]
- **求解代数方程**：
  在 \(\tilde{\tau} = 4\tau\) 时，飞船相对地球系 \(S_0\) 的速度大小为 \(\sqrt{u_{0x}^2 + u_{0y}^2} = \beta\)。两边消去 \(\beta^2\)：
  \[
  (\gamma - \beta^2 - 1)^2 + \left(\frac{\gamma - 1}{\gamma}\right)^2 = (\gamma - 2\beta^2)^2
  \]
  利用平方差公式右边减左边第一项：
  \[
  (\gamma - 2\beta^2)^2 - (\gamma - \beta^2 - 1)^2 = (1 - \beta^2)(2\gamma - 3\beta^2 - 1) = \left(\frac{\gamma - 1}{\gamma}\right)^2
  \]
  代入 \(1 - \beta^2 = \frac{1}{\gamma^2}\)：
  \[
  \frac{1}{\gamma^2}\left[2\gamma - 3\left(1 - \frac{1}{\gamma^2}\right) - 1\right] = \frac{(\gamma - 1)^2}{\gamma^2}
  \]
  两边同乘 \(\gamma^2\)：
  \[
  2\gamma - 4 + \frac{3}{\gamma^2} = \gamma^2 - 2\gamma + 1 \implies \gamma^4 - 4\gamma^3 + 5\gamma^2 - 3 = 0
  \]
  因式分解：
  \[
  (\gamma^2 - \gamma - 1)(\gamma^2 - 3\gamma + 3) = 0
  \]
  因 \(\gamma^2 - 3\gamma + 3 = (\gamma - 3/2)^2 + 3/4 > 0\) 无实根，且 \(\gamma > 1\)，故唯一物理根为黄金分割比 \(\phi\)：
  \[
  \gamma = \frac{1 + \sqrt{5}}{2} = \phi
  \]
  从而所求速度 \(v\) 为：
  \[
  v = c\sqrt{1 - \frac{1}{\gamma^2}} = c\sqrt{\frac{1}{\phi}} = c\sqrt{\frac{\sqrt{5} - 1}{2}} \approx 0.78615\,c
  \]

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做得到的黄金比例解 \(\gamma = \frac{1+\sqrt{5}}{2}\)、\(v = c\sqrt{\frac{\sqrt{5}-1}{2}}\) 与所有获奖解答完全一致！
  - **四种主流解法对比**：
    1. **三维速度逆向合成法**（Eppu Leinonen, Tejas Acharya, Alptürk Eski）：即我们上面盲做所用的方法，避开了维格纳转动，最为直观。
    2. **四维速度矩阵连乘法**（Luka Passek-Kumerički, Lukas Schicht）：直接写出沿 \(x\) 和沿 \(y\) 的四维洛伦兹 Boost 矩阵 \(\Lambda_x(\beta)\) 与 \(\Lambda_y(\beta)\)，作用在初始四维速度 \((1,0,0,0)^T\) 上：\(u^\mu(4\tau) = \Lambda_x(\beta)\Lambda_y(\beta)\Lambda_x(-\beta)\Lambda_y(-\beta) (1,0,0,0)^T\)，只需求时间分量 \(u^0 = \gamma\)！
    3. **四维洛伦兹不变量法（Kalda 的命题原意与 Filip Baciak 解法）**：利用内积不变量！已知 \(u_{(4\tau)} \cdot u_{(0)} = \gamma\)。由于洛伦兹变换保持四维内积不变，我们可以把该内积放到中间参考系 \(S_2\)（即 \(\tilde{\tau}=2\tau\) 的瞬时静止系）中计算：\(u_{(4\tau)} \cdot u_{(0)}\) 在 \(S_2\) 系中就是“从 \(S_2\) 出发经历 \(\Lambda_x(-\beta)\Lambda_y(-\beta)\) 后的四维速度”与“从 \(S_2\) 逆向经历 \(\Lambda_y(-\beta)\Lambda_x(-\beta)\) 到达 \(S_0\) 的四维速度”的内积！这样两边对称性极高，两行就能直接写出关于 \(\gamma\) 的方程！
- **核心难点与易错点**：
  1. **误以为在地球系中转过 \(90^\circ\) 或误以为 \(4\tau\) 后回到静止**：在伽利略变换下，四段对称加速后速度恰好归零；但在相对论中，由于洛伦兹 Boost 群的非阿贝尔性（\(\Lambda_x \Lambda_y \neq \Lambda_y \Lambda_x\)，伴随托马斯-维格纳进动），四段加速后不仅速度不为零，甚至可以依然保持高速 \(v \approx 0.786c\)！
  2. **正向速度合成的维格纳转动陷阱**：Tejas Acharya 在解答中专门指出，若正向试图合并 \(S_0 \to S_2\) 再加 \(\vec{V}_{32}\)，由于 \(S_2\) 的坐标轴相对 \(S_0\) 已经发生了维格纳旋转，直接套用平行/垂直速度合成公式会出错；而从 \(S_3 \to S_2 \to S_1 \to S_0\) 逆向递推则天然保证了每一步相邻系坐标轴平行。

---

## 5. `physicscup-2023-q5-reader` — Light sources (光源位置重构)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  平面上有三个完全相同的点光源 \(A, B, C\)，向四周均匀发射相干光。假定单光源振幅不随距离衰减，图中给出了平面上光强局部极大值点的分布，要求仅用尺规/GeoGebra 几何作图重构三个点光源的位置。
- **三波干涉局部极大值即全局极大值的证明**：
  设三个光源在平面某点 \(P\) 的合成复振幅为：
  \[
  E(P) = E_0 \left(e^{i\phi_A} + e^{i\phi_B} + e^{i\phi_C}\right) = E_0 e^{i\phi_A} \left(1 + e^{i\Delta\phi_1} + e^{i\Delta\phi_2}\right)
  \]
  其中 \(\Delta\phi_1 = k(r_B - r_A) + \alpha_1\)，\(\Delta\phi_2 = k(r_C - r_A) + \alpha_2\)。
  光强 \(I \propto |1 + e^{i\Delta\phi_1} + e^{i\Delta\phi_2}|^2 = 3 + 2\cos\Delta\phi_1 + 2\cos\Delta\phi_2 + 2\cos(\Delta\phi_1 - \Delta\phi_2)\)。
  只要 \(P\) 不在三角形退化奇点上，\((\Delta\phi_1, \Delta\phi_2)\) 可作为局部独立坐标。对 \(I\) 求一阶与二阶偏导可知：除了使三列波完全同相（\(\Delta\phi_1 = 2\pi n_1\)，\(\Delta\phi_2 = 2\pi n_2\)，对应最大光强 \(I = 9I_0\)）的点之外，其余驻点（如 \(1 + e^{i\Delta\phi_1} + e^{i\Delta\phi_2} = 0\) 对应光强极小值 0，或两个同相一个反相对应鞍点）均**不是**局部极大值！
  因此，图中所有局部极大值点都满足：
  \[
  r_B - r_A = n_1 \lambda - \frac{\alpha_1}{k}, \quad r_C - r_B = n_2 \lambda - \frac{\alpha_2}{k}, \quad r_C - r_A = (n_1 + n_2)\lambda - \frac{\alpha_1 + \alpha_2}{k}
  \]
- **双曲线族识别与对称轴尺规作图法**：
  对于固定的整数 \(n_1\)，满足 \(r_B - r_A = \text{const}\) 的轨迹是以 \(A, B\) 为焦点的**双曲线的一支**！
  观察原图中的点阵：可以清晰地找到**三条共线点列（直线）**！双曲线退化为直线的唯一可能是渐近退化或**中垂线**（\(r_B - r_A = 0\)）。由于这三条直线穿过了密集的中心条纹区且两侧分支关于它对称，这三条直线正是三对光源连线 \(AB, BC, CA\) 的**垂直平分线** \(g_{AB}, g_{BC}, g_{CA}\)（同时说明三个全同光源初相相同，\(\alpha_1 = \alpha_2 = 0\)，且三条中垂线交于 \(\triangle ABC\) 的外心）！
  接下来的核心几何问题是：已知以 \(A, B\) 为焦点的若干支双曲线上的离散点（每支有 \(\ge 5\) 个点，可用 GeoGebra 的 `Conic through 5 Points` 画出双曲线）以及虚轴（即中垂线 \(g_{AB}\)），如何作出实轴（即焦点连线 \(AB\)）？
  1. 任选一族双曲线中的某一支 \(\mathcal{H}_1\)，在其上任取一点 \(P_1\)，作平行于中垂线 \(g_{AB}\) 的直线交同一支双曲线于另一点 \(P_2\)；
  2. 作线段 \(P_1 P_2\) 的垂直平分线，由双曲线对称性，该垂直平分线即为**双曲线的实轴（穿过焦点 \(A\) 和 \(B\) 的直线 \(L_{AB}\)）**！（或者更简单：直接过中垂线与实轴的对称中心——只需用兩条平行弦中点连线即可定出实轴）。
  3. 对另外两族双曲线重复上述步骤，得到三条焦点连线 \(L_{AB}, L_{BC}, L_{CA}\)。
  4. 这三条直线的三个交点，即为三个点光源 \(A, B, C\) 的精确位置！

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 盲做几何重构方案与 Lukas Schicht、Marinus Lehmann、Lincoln Liu 等获奖解答完全一致！重构出的光源坐标为 \(G(-6, -2)\)、\(H(-0.04152, 3.33821)\)、\(I(1.49717, -8.61759)\)。
  - **Lukas Schicht 优美的几何复向量证明**：なぜ没有次极大值？考虑复平面上的向量 \(z = 1 + e^{i\Delta\phi_1} + e^{i\Delta\phi_2}\)。当固定 \(\Delta\phi_2\) 微调 \(\Delta\phi_1\) 时，\(z\) 在以 \(1+e^{i\Delta\phi_2}\) 为圆心、半径为 1 的圆上运动，模长最大要求 \(e^{i\Delta\phi_1}\) 与合成向量 \(z\) 同向（即 \(z = k_1 e^{i\Delta\phi_1}, k_1 > 1\)）。同理固定 \(\Delta\phi_1\) 微调 \(\Delta\phi_2\) 要求 \(z = k_2 e^{i\Delta\phi_2}, k_2 > 1\)。两式联立立即给出 \(e^{i\Delta\phi_1} = e^{i\Delta\phi_2} = 1\)，无需计算复杂的二阶海森矩阵（Hessian matrix）！
- **核心难点与易错点**：
  1. **误把双曲线焦点当成可以直接用工具读取的对象**：GeoGebra 标准菜单中没有“求圆锥曲线焦点”的按钮，但利用 `Conic through 5 Points` 画出双曲线后，先找共线的零级条纹（中垂线 \(H_0\)），再作平行于 \(H_0\) 的弦并取中垂线，即可一举定出穿过两焦点的实轴，三条实轴两两相交直接给出三个焦点（无需单独求每条双曲线的离心率 \(c = \sqrt{a^2+b^2}\)）！这一“三线交于三焦点”的拓扑巧合极大简化了尺规作图。
  2. **忽略远场散点的归属验证**：图中有几个离中心很远的孤立点（最左、最上、最下、最右），那是因为在靠近光源连线延长线附近，双曲线相交角极小，条纹间距被严重拉长。

---

## 6. `physicscup-2024-q1-reader` — Diving cylinder (落水圆柱体)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  慢动作视频展示了一个实心圆柱（半径 \(R\)、高 \(H\)、密度 \(\rho_c\)，底面保持水平）从空气中自由下落，拍击水面并没入水中。要求给出测量圆柱密度 \(\rho_c\) 的公式及所需测量的物理量。
- **为什么不能用沉入水后的加速运动，而必须用触水瞬间的碰撞？**：
  当圆柱完全进入水中后，其尾部会形成强烈的湍流尾迹、空泡（cavitation/air cavity）与涡街，阻力系数复杂且未知；而在圆柱底面**刚刚接触水面的极短瞬间（冲击阶段 Phase 1，历时 \(\tau \to 0^+\)）**，圆柱底部排开下方水体，瞬间给周围水体赋予动量！
  在这极短的碰撞时间内，重力、浮力、粘滞力与表面张力的冲量均可忽略，圆柱与水体组成的系统在竖直方向遵循**动量守恒（更准确地说是流体脉冲压力与附加质量动量守恒）**：
  \[
  m_c v_0 = (m_c + \Delta m) v_1
  \]
  其中 \(v_0\) 是触水前瞬间的速度，\(v_1\) 是触水后瞬间的速度，\(m_c = \pi R^2 H \rho_c\) 是圆柱质量，\(\Delta m\) 是平底面拍击水面时的**流体附加质量（added mass）**！
- **平底圆盘单侧附加质量 \(\Delta m\) 的严格推导**：
  在触水瞬间，水深远大于 \(R\)，水面在 \(r > R\) 处为自由表面（脉冲压强 \(\Pi = \int_0^\tau p\,\mathrm{d}t = 0\)）。由理想无旋流体运动方程 \(\vec{u} = \nabla \phi\)（其中速度势 \(\phi = -\Pi / \rho_w\) 满足拉普拉斯方程 \(\nabla^2 \phi = 0\)）：
  - 在圆盘下方（\(z = 0^+, r < R\)）：\(\frac{\partial \phi}{\partial z} = v_1\)；
  - 在自由液面上（\(z = 0, r > R\)）：\(\phi = 0 \implies u_r = \frac{\partial \phi}{\partial r} = 0\)（流线垂直于自由液面！）。
  由镜像对称性（将下半空间 \(z > 0\) 延拓到全空间），这完全等价于**全空间无界理想流体中，一个半径为 \(R\) 的无限薄圆盘以速度 \(v_1\) 沿法向运动所携带的附加质量的一半**！
  如何求半径为 \(R\) 的薄圆盘在全空间无旋流体中的附加质量 \(M_{\text{disk}}\)？
  利用静电学/静磁学类比（扁旋转椭球 \(\frac{r^2}{R^2} + \frac{z^2}{c^2} = 1\) 在 \(c \to 0\) 极限下的退磁因子/极化率）：
  把薄圆盘看作半轴为 \((R, R, c)\)（\(c \to 0\)）的超导扁椭球（法向磁场 \(B_n = 0\) 对应流体不可穿透法向速度 \(u'_n = 0\)）置于均匀外场 \(B_0\) 中。已知扁椭球内部退磁因子在 \(c \to 0\) 时满足 \(N_z \approx 1 - \frac{\pi c}{2R}\)，或直接由环形表面电流计算中心磁场：得到扁椭球的抗磁磁矩模为：
  \[
  m_{\text{mag}} = \frac{8 R^3}{3\mu_0} B_0
  \]
  由偶极场能量公式（或动量积分），全空间薄圆盘的附加质量为：
  \[
  M_{\text{disk}} = \frac{8}{3} \rho_w R^3
  \]
  由于触水瞬间只有圆盘**下半空间**（单侧）有水，上半空间是空气，因此单侧冲击附加质量恰好为全空间的一半：
  \[
  \Delta m = \frac{1}{2} M_{\text{disk}} = \frac{4}{3} \rho_w R^3
  \]
- **圆柱密度计算公式**：
  将 \(m_c = \pi R^2 H \rho_c\) 与 \(\Delta m = \frac{4}{3} \rho_w R^3\) 代入动量守恒方程 \(m_c v_0 = (m_c + \Delta m)v_1\)：
  \[
  \pi R^2 H \rho_c (v_0 - v_1) = \frac{4}{3} \rho_w R^3 v_1 \implies \rho_c = \frac{4}{3\pi} \frac{R}{H} \frac{v_1}{v_0 - v_1} \rho_w
  \]
  在视频中只需用像素尺测量圆柱半径与高度的像素比 \(R/H\)，并逐帧测量触水前后的位移斜率（像素/帧）得到无量纲速度比 \(\frac{v_1}{v_0 - v_1}\)，无需知道视频帧率或真实空间比例尺！

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做推导出的公式 \(\rho_c = \frac{4}{3\pi} \frac{R}{H} \frac{v_1}{v_0 - v_1} \rho_w\) 与 Val Karan、Guy Ginzberg、Michał Kołodziejczyk 及 Kalda 本人的第 50 题纪念解答完全一致！
  - **三种求单侧薄圆盘附加质量 \(\Delta m = \frac{4}{3}\rho_w R^3\) 的方法**：
    1. **介电质/超导扁椭球静电磁学类比法**（Val Karan, Guy Ginzberg Method 2, Michał Kołodziejczyk）：利用扁椭球在 \(c/R \to 0\) 极限下内部场均匀的性质，通过库仑积分或安培环路定理求得等效偶极矩，极其优雅地避开了偏微分方程。
    2. **扁球面坐标系（Oblate Spheroidal Coordinates）分离变量解拉普拉斯方程**（Guy Ginzberg Method 1）：硬核推导勒让德函数 \(P_1(\mu)\) 与第二类勒让德函数 \(Q_1(i\zeta)\)，在 \(\zeta_0 \to 0\) 极限下积分表面压强得 \(F = -\frac{4}{3}\rho_w R^3 \dot{u}\)。
    3. **镜像延拓法**：为什么自由液面边界条件 \(\phi(r>R, z=0) = 0\) 恰好等价于全空间薄圆盘对称平面？因为在全空间薄圆盘绕流中，根据关于 \(z=0\) 平面的反对称性（\(\phi(r, -z) = -\phi(r, z)\)），在圆盘外的 \(z=0\) 平面上天然满足 \(\phi(r>R, z=0) = 0\)！因此下半空间流场与全空间流场的下半部分**严格全同**，附加质量严格减半！
- **核心难点与易错点**：
  1. **误用机械能守恒**：触水瞬间是一个**完全非弹性碰撞**过程！脉冲压力以水中声速 \(c_s\) 建立无旋速度场的同时，机械能并不守恒（类似于两刚体非弹性碰撞产生耗散/激波或表面飞溅），必须使用脉冲动量定理 \(\Delta p_z = -\int \mathrm{d}A \int p\,\mathrm{d}t = \Delta m \cdot v_1\)。
  2. **漏掉单侧因子 \(1/2\)**：若直接查表套用浸没在无穷流体中圆盘的附加质量 \(\frac{8}{3}\rho_w R^3\)，会比正确值大一倍。
  3. **视频测量的折射伪影与水面位置识别**：测量圆柱底面入水后会受到容器壁和水面折射的严重干扰，因此应当追踪仍在空气中的**圆柱顶面**在触水前后几帧的坐标 \(Y(t)\)。

---

## 7. `physicscup-2024-q2-reader` — Image of a circle (圆的透镜成像)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  已知平面内某薄透镜的主光轴位于纸面内，一圆周经该理想薄透镜所成的实像为给定的椭圆 \(\Gamma\)，且给出了离椭圆较近的那个主焦点 \(F\)（即像方主焦点）。要求仅用尺规几何作图（不得试凑或数值输入）确定薄透镜的光心 \(O\)。
- **薄透镜射影变换（同素射影/透视仿射）的核心不变量分析**：
  设光心为 \(O(0,0)\)，主光轴为 \(x\) 轴，透镜所在平面为 \(y\) 轴，像方焦点为 \(F(f, 0)\)。物点 \((x, y)\) 与像点 \((x', y')\) 满足高斯成像公式与横向放大率关系：
  \[
  x' = \frac{fx}{x + f}, \quad y' = \frac{fy}{x + f}
  \]
  这一二维射影变换（Homography）具有以下极强的几何性质：
  1. **平行于光轴的物方直线，其像必过像方焦点 \(F\)**；且物方圆上平行于光轴的两条切线 \(d_A, d_C\)，其像必为**过焦点 \(F\) 作椭圆 \(\Gamma\) 的两条切线 \(F A', F C'\)**（切点为 \(A', C'\)）！
  2. 更妙的是：在原圆 \(\Omega\) 上，平行于光轴的两条切线的切点 \(A, C\) 分别是圆的最高点与最低点，因此**弦 \(AC\) 严格垂直于主光轴（即平行于透镜平面）**！由于平行于透镜平面的直线上各点物距 \(x\) 相同，横向放大率常数，其像**依然平行于透镜平面**！
     结论 1：**连接过 \(F\) 对椭圆所作两条切线的切点弦 \(A'C'\)，必然平行于薄透镜平面（即垂直于主光轴）！**（在射影几何中，\(A'C'\) 即焦点 \(F\) 关于椭圆 \(\Gamma\) 的极线 polar line！）
  3. 有了透镜平面方向（平行于 \(A'C'\)），过焦点 \(F\) 作 \(A'C'\) 的垂线，立刻就得到了**薄透镜的主光轴**！
     验证：原圆的水平直径 \(BD\)（垂直于 \(AC\)、平行于主光轴）过圆心，其像 \(B'D'\) 必过焦点 \(F\) 且平分平行于透镜的椭圆切线，因此主光轴必定同时穿过焦点 \(F\) 与椭圆的几何中心 \(O_{\Gamma}\)，且与椭圆交于 \(B', D'\) 两点（其中 \(B', D'\) 处的椭圆切线平行于 \(A'C'\)）！
- **确定光心 \(O\) 在主光轴上位置的两种纯几何作图法**：
  - **方法一（位似变换法 Homothety，最简洁）**：
    在原圆 \(\Omega\) 中，\(AC\) 是竖直直径，\(BD\) 是水平直径，\(ABCD\) 构成正方形（以 \(AC\) 为直径的圆就是原圆 \(\Omega\)！）。
    由于 \(A, O, A'\) 共线，\(C, O, C'\) 共线，且 \(AC \parallel A'C'\)，因此存在以**光心 \(O\) 为位似中心**的位似变换（负比例缩放），将竖直直径 \(AC\) 映射为切点弦 \(A'C'\)！
    在该位似变换下，整个原圆 \(\Omega\)（以 \(AC\) 为直径的圆）被映射为**以 \(A'C'\) 为直径的辅助圆 \(\Omega_{\text{aux}}\)**！
    原圆水平直径的两个端点 \(B\)（离透镜较近）和 \(D\)（离透镜较远），在位似变换下对应辅助圆 \(\Omega_{\text{aux}}\) 与 \(A'C'\) 中垂线（即主光轴！）的两个交点 \(U, V\)！
    由于 \(O\) 是位似中心，\(B, O, U\) 必共线；同时根据透镜成像规律，过光心 \(O\) 的光线不偏折，\(B, O, B'\) 也共线！这意味着 \(B, O, U, B'\) 四点全部在同一条直线上——但 \(U, B'\) 都在主光轴上，这怎么确定 \(O\)？（慢着！\(B, D\) 在原圆上不在主光轴上时才不共线！如果原圆圆心不在主光轴上，\(BD\) 平行于主光轴但**不与主光轴重合**！）
    让我们仔细看图：图中焦点 \(F\) 在 \(x\) 轴上，而椭圆 \(\Gamma\) 整体倾斜在 \(x\) 轴下方！这说明**原圆 \(\Omega\) 的圆心不在主光轴上**！
    太棒了！既然原圆圆心不在主光轴上：
    - 过 \(F\) 作椭圆的两条切线，切点为 \(A', C'\)，则弦 \(A'C'\) 平行于透镜平面！
    - 过 \(F\) 作 \(A'C'\) 的垂线，这就是**主光轴**！
    - 原圆的水平直径 \(BD\) 平行于主光轴，其像 \(B'D'\) 是**连接椭圆中心 \(O'\) 与焦点 \(F\) 的直线 \(FO'\)**，交椭圆于 \(B', D'\)（在该两点处椭圆切线平行于 \(A'C'\)）！
    - 以 \(A'C'\) 为直径作辅助圆，并作 \(A'C'\) 的垂直平分线（平行于主光轴，穿过 \(A'C'\) 的中点 \(M\)），交辅助圆于 \(U, V\) 两点！由于 \(BD\) 在原圆中垂直平分 \(AC\)，在以 \(O\) 为中心的位似变换下，\(B, D\) 被映射为 \(U, V\)（注意反向位似保持与透镜的远近顺序：离 \(F\) 较近的像点 \(D'\) 对应离透镜较远的物点 \(D\)，故 \(U\) 与 \(B'\) 分别位于直线 \(A'C'\) 的两侧）！
    - 连接 \(U B'\) 与 \(V D'\)，这两条直线的交点（同时也必落在过 \(F\) 垂直于 \(A'C'\) 的主光轴上）即为光心 \(O\)！
  - **方法二（焦平面直角性质法）**：
    物方两条相互垂直的直线（例如正方形 \(ABCD\) 的对角线 \(AB \perp BC\)），它们各自平行于过光心 \(O\) 的两条正交光线，因此在**像方焦平面**（过 \(F\) 且平行于 \(A'C'\) 的直线 \(l_F\)）上的两个交点 \(K, L\)（即直线 \(A'B'\)、\(C'B'\) 与焦平面 \(l_F\) 的交点）对光心 \(O\) 的张角必为 \(90^\circ\)（\(\angle KOL = 90^\circ\)）！同时根据对称性（\(\angle ABO = 45^\circ\)），\(\triangle KOL\) 是以 \(KL\) 为斜边的等腰直角三角形，或者以 \(KL\) 为直径作圆，与主光轴（或平行于 \(l_F\) 的切线）相交即可直接定出 \(O\)！

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做推导出的两种方法，恰好完整覆盖了 Kalda 在评述中总结的两大最佳解法流派：**B 类位似变换法（Andrei Vila，Kalda 的命题原意）** 与 **A 类焦平面正交光束交点法（Bayram Alp Şahin, Lukas Schicht, Val Karan）**！
  - 最终光心精确坐标为 \(O = (-1.12358, -0.58132)\)。
- **核心难点与易错点**：
  1. **误以为椭圆的长轴或短轴是主光轴**：当物方圆偏离主光轴放置时，经薄透镜射影变换成的椭圆是倾斜的，其长短轴既不平行也不垂直于主光轴！唯一能确定透镜方向的是焦点 \(F\) 关于椭圆的极线 \(A'C'\)（即过 \(F\) 的两条椭圆切线的切点连线）。
  2. **位似法中 \(U, V\) 与 \(B', D'\) 的配对方向陷阱**：在作出以 \(A'C'\) 为直径的圆及其垂线交点 \(U, V\) 后，究竟是连 \(UB' \cap VD'\) 还是 \(UD' \cap VB'\)？这两种连法都会交在主光轴上！正确判据是：实像在透镜同侧（与 \(F\) 同侧），物距越大则像距越小（越靠近 \(F\)）。设 \(D'\) 比 \(B'\) 更靠近 \(F\)，则物点 \(D\) 比 \(B\) 离透镜更远；而实像对应**负位似比**（中心在物与像之间），因此 \(U, V\) 相对 \(A'C'\) 的左右方位与 \(B, D\) 相对 \(AC\) 的左右方位相反，即应当将与 \(B'\) 位于 \(A'C'\) 异侧的点 \(U\) 与 \(B'\) 相连！

---

## 8. `physicscup-2024-q3-reader` — Scrap iron sorting (废铁分选)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  木桌上散落着软磁铁屑（相对磁导率 \(\mu_r \gg 1\)，磁滞可忽略），包含两类微粒：薄铁片（厚度远小于直径）与微小铁球。上方有一个球形永磁体（磁化方向竖直向下）从高处缓慢下移。当磁铁中心距桌面高度为 \(a\) 时，薄铁片被吸起；求微小铁球被吸起时的高度 \(b\)（铁屑尺寸远小于 \(a\)，忽略颗粒间相互作用）。
- **核心关键：退磁因子（Demagnetizing factor）导致的磁化强度差异**：
  球形永磁体在外部产生精确的磁偶极子场。在正下方距离球心为 \(z\) 的桌面上，外磁场 \(\vec{B}_0(z)\) 方向竖直向下，大小为：
  \[
  B_0(z) = \frac{\mu_0}{4\pi} \frac{2 m_{\text{mag}}}{z^3} \propto z^{-3}
  \]
  由于软铁颗粒尺寸远小于 \(z\)，颗粒可视为置于局域均匀外场 \(\vec{B}_0\) 中被磁化。
  设软铁的相对磁导率为 \(\mu \gg 1\)，内部本构关系为 \(\vec{B}_{\text{in}} = \mu_0(\vec{H}_{\text{in}} + \vec{M}) = \mu_0 \mu \vec{H}_{\text{in}}\)。
  1. **对于小铁球（球体的退磁因子 \(N = 1/3\)）**：
     均匀磁化球体内部产生的退磁场为 \(\vec{H}_d = -\frac{1}{3}\vec{M}\)（可由静电极化球内部场 \(\vec{E}' = -\frac{\vec{P}}{3\varepsilon_0}\) 或球体偶极场在极点处 \(B_n\) 连续推导）。
     因此球内部总磁场强度为 \(\vec{H}_{\text{in}} = \vec{H}_0 - \frac{1}{3}\vec{M} = \frac{\vec{B}_0}{\mu_0} - \frac{1}{3}\vec{M}\)。
     联立 \(\vec{M} = (\mu - 1)\vec{H}_{\text{in}}\) 得：
     \[
     \vec{M}_{\text{sphere}} = \frac{3(\mu - 1)}{\mu + 2} \frac{\vec{B}_0}{\mu_0} \xrightarrow{\mu \gg 1} \frac{3}{\mu_0} \vec{B}_0
     \]
  2. **对于薄铁片（平躺或竖立？注意磁转矩的取向效应！）**：
     等等！薄铁片在桌面上是如何取向的，或者磁化有多强？
     让我们仔细分析：
     - 如果薄铁片**平躺在桌面上**（法向沿竖直方向，即平行于外磁场 \(\vec{B}_0\)）：薄片沿厚度方向的退磁因子 \(N_\perp = 1\)！由 \(B_n\) 连续，\(\vec{B}_{\text{in}} = \vec{B}_0\)，故 \(\vec{H}_{\text{in}} = \frac{\vec{B}_0}{\mu_0 \mu}\)，磁化强度为：
       \[
       \vec{M}_{\text{plate},\perp} = \frac{\mu - 1}{\mu} \frac{\vec{B}_0}{\mu_0} \xrightarrow{\mu \gg 1} \frac{1}{\mu_0} \vec{B}_0
       \]
     - 慢着：薄铁片会不会在被吸起之前先被磁力矩立起来？如果薄铁片尺寸极小，平躺在桌面上时，法向与 \(\vec{B}_0\) 严格平行，处于对称平衡态（或者即便考虑退磁因子，平躺薄片与球体的磁化强度之比为 \(1 : 3\)）？
     等等，如果 \(M_{\text{sphere}} = 3 M_{\text{plate}}\)，那么单位体积所受磁力是小铁球更大（\(b = a \sqrt[7]{3} > a\)），还是薄铁片更大？
     让我们检查一下：小铁球的退磁因子 \(N = 1/3\)，平躺薄片的法向退磁因子 \(N = 1\)，因此平躺薄片的磁化强度 \(M_{\text{plate}} = B_0/\mu_0\) 只有小铁球 \(M_{\text{sphere}} = 3B_0/\mu_0\) 的 **\(1/3\)**！
     为什么题目说“The plates are lifted when the height is \(a\). What is the height \(b\) at which the magnet lifts the spheres?”？
     不管谁先被吸起，我们先算單位体积所受的磁力与重力的平衡：
     软铁颗粒在非均匀外场 \(\vec{B}_0(z)\) 中受到的向上的磁力为（注意 \(\vec{M} \propto \vec{B}_0\) 是感应磁矩）：
     \[
     F_z = V M_z \frac{\mathrm{d}B_0}{\mathrm{d}z} = \frac{1}{2} V \frac{\mathrm{d}}{\mathrm{d}z}\left(M_z B_0\right) \propto V z^{-7}
     \]
     当磁力等于重力 \(\rho_{\text{Fe}} V g\) 时颗粒被吸起（体积 \(V\) 消去！）。
     由于 \(F_z / V \propto M_z \frac{\mathrm{d}B_0}{\mathrm{d}z}\)，若平躺薄片的 \(M_{\text{plate}} = \frac{1}{\mu_0}B_0\)，小铁球的 \(M_{\text{sphere}} = \frac{3}{\mu_0}B_0\)，则：
     \[
     \frac{1}{a^7} = \frac{3}{b^7} \implies b = a \sqrt[7]{3}
     \]

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做结果 \(b = a\sqrt[7]{3}\) 与 Konstantin Rodionenko、Luka Passek-Kumerički、Kutay Kulbak 等获奖解答完全一致！
  - **Jaan Kalda 严厉指出的概念陷阱（导致大量优秀选手痛失最佳解答奖）**：
    许多选手直接写下偶极子受力公式 \(\vec{F} = \nabla(\vec{m}\cdot\vec{B}_0)\)，然后把 \(\vec{m} = V \chi_{\text{eff}} \vec{B}_0 / \mu_0\) 代入，直接对 \(B_0^2\) 求导，漏掉了因子 \(1/2\)（虽然在求比值 \(b/a\) 时该常数因子恰好约掉，所以最终答案没受影响，但被 Kalda 判定为严重概念错误而取消评奖资格）！
    **正确物理原理**：外磁场对磁偶极子施加的力只取决于瞬时磁矩 \(\vec{m}\)，在求梯度时必须保持 \(\vec{m}\) 不变，即：
    \[
    F_z = m_z \frac{\partial B_z}{\partial z} = V M_z(B_z) \frac{\partial B_z}{\partial z} = \frac{1}{2} V \chi_{\text{eff}} \frac{\partial (B_z^2/\mu_0)}{\partial z}
    \]
    如果从虚功原理（能量法）出发，外源做功 \(\vec{m}\cdot\mathrm{d}\vec{B}_0\) 中有一半转化为软磁颗粒内部极化/磁化自能 \(\int \vec{B}_0\cdot\mathrm{d}\vec{m} = \frac{1}{2}\vec{m}\cdot\vec{B}_0\)，因此系统的有效相互作用自由能是 \(U_{\text{eff}} = -\frac{1}{2}\vec{m}\cdot\vec{B}_0\)，求导同样给出因子 \(1/2\)（完全等同于静电场中线性电介质颗粒受力 \(\vec{F} = \frac{1}{2}\alpha \nabla(E^2)\)）！
- **核心难点与易错点**：
  1. **误以为 \(\mu \gg 1\) 时球体和薄片内部磁场或磁化强度相同**：在 \(\mu \to \infty\) 极限下，虽然软磁体内部 \(\vec{H}_{\text{in}} \to 0\)，但由于边值关系不同（平躺薄片受法向 \(B_n\) 连续约束，故 \(B_{\text{in}} = B_0 \implies \mu_0 M = B_0\)；球体则允许磁感线向球体集中，内部 \(B_{\text{in}} = 3B_0 \implies \mu_0 M = 3B_0\)），球体的磁化强度恰好是平躺薄片的 3 倍！
  2. **感应偶极子受力的 \(1/2\) 因子陷阱**：永久磁偶极子受力为 \(\nabla(\vec{m}\cdot\vec{B})\)，而线性感应磁偶极子（\(\vec{m} \propto \vec{B}\)）受力为 \(\frac{1}{2}\nabla(\vec{m}\cdot\vec{B}) = (\vec{m}\cdot\nabla)\vec{B}\)。

---

## 9. `physicscup-2024-q4-reader` — Satellites (双卫星最大相对速度)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  两颗卫星在同一平面内绕地球（质量 \(M\)）沿椭圆轨道运动，偏心率分别为 \(e_1, e_2\)，长轴夹角为 \(\alpha\)。卫星与地心连线的掠面速率（areal velocity）分别为 \(L_1, L_2\)。已知两卫星轨道周期之比为无理数。求两卫星的最大相对速度（并给出 \(\alpha = 90^\circ, L_1 = L_2\) 时的简化结果）。
- **开普勒轨道的速度矢端图（Hodograph）定理**：
  由开普勒第二定律，单位质量角动量（比角动量）大小为 \(h_i = r_i^2 \dot{\theta}_i = 2 L_i\)（\(i=1,2\)）。
  考虑牛顿第二定律或拉普拉斯-龙格-楞次矢量（偏心率矢量 \(\vec{e}\)）：
  \[
  \frac{\mathrm{d}\vec{v}}{\mathrm{d}t} = -\frac{GM}{r^2}\hat{r} = -\frac{GM}{h}\dot{\theta}\hat{r} = \frac{GM}{h}\frac{\mathrm{d}\hat{\theta}}{\mathrm{d}t} \quad (\text{若逆时针旋转，}\hat{n} = +\hat{z}, \frac{\mathrm{d}\hat{\theta}}{\mathrm{d}\theta} = -\hat{r})
  \]
  两边对时间积分，立刻得到速度矢量 \(\vec{v}\) 的分解式（或由 \(\vec{e} = \frac{\vec{v}\times\vec{h}}{GM} - \hat{r} \implies \vec{v} = \frac{GM}{h}\hat{n}\times(\vec{e} + \hat{r})\)）：
  \[
  \vec{v}_i = \frac{GM}{2L_i} \hat{n}_i \times (\vec{e}_i + \hat{r}_i) = \vec{u}_i + \vec{w}_i
  \]
  其中：
  - \(\vec{u}_i = \frac{GM}{2L_i} (\hat{n}_i \times \vec{e}_i)\) 是一个**常矢量**（在速度空间中的圆心平移矢量），方向垂直于长轴（沿短轴方向），大小为 \(u_i = \frac{GM e_i}{2L_i}\)；
  - \(\vec{w}_i = \frac{GM}{2L_i} (\hat{n}_i \times \hat{r}_i)\) 是一个**模长恒定、方向随真近点角 \(\theta_i\) 旋转的矢量**，其大小为 \(w_i = \frac{GM}{2L_i}\)！
  这正是著名的**哈密顿速度圆定理（Circular Hodograph）**：椭圆轨道质点的速度矢量端点在速度空间中精确描绘出一个半径为 \(R_{v,i} = \frac{GM}{2L_i}\)、圆心位于 \(\vec{u}_i\)（模长为 \(\frac{GM e_i}{2L_i}\)）的圆！
- **最大相对速度的几何极值与遍历性（Ergodicity）**：
  由于两卫星周期之比 \(T_1 / T_2 \notin \mathbb{Q}\) 为无理数，根据克罗内克稠密定理（Kronecker's theorem），在足够长的时间内，两卫星的角位置组合 \((\theta_1, \theta_2)\) 在二维环面 \(\mathbb{T}^2 = [0, 2\pi)^2\) 上稠密！
  因此，两个旋转矢量 \(\vec{w}_1, \vec{w}_2\) 的方向可以独立取遍任意角度，相对速度 \(\Delta \vec{v} = \vec{v}_2 - \vec{v}_1\) 的上确界（最大值）就等于**速度空间中两个速度圆上两点之间的最大欧氏距离**！
  两个圆上两点的最大距离显然等于**两圆圆心距加上两圆半径之和**：
  \[
  |\Delta \vec{v}|_{\max} = |\vec{u}_2 - \vec{u}_1| + R_{v,1} + R_{v,2}
  \]
  - **情况一（两卫星同向绕行，\(\hat{n}_1 = \hat{n}_2\)）**：
    两长轴夹角为 \(\alpha\)，故两圆心矢量 \(\vec{u}_1, \vec{u}_2\) 的夹角也为 \(\alpha\)。由余弦定理：
    \[
    |\vec{u}_2 - \vec{u}_1| = \frac{GM}{2}\sqrt{\left(\frac{e_1}{L_1}\right)^2 + \left(\frac{e_2}{L_2}\right)^2 - \frac{2e_1 e_2 \cos\alpha}{L_1 L_2}}
    \]
    故最大相对速度为：
    \[
    v_{\text{rel, max}} = \frac{GM}{2}\left[\frac{1}{L_1} + \frac{1}{L_2} + \sqrt{\frac{e_1^2}{L_1^2} + \frac{e_2^2}{L_2^2} - \frac{2e_1 e_2 \cos\alpha}{L_1 L_2}}\right]
    \]
  - **情况二（两卫星反向绕行，\(\hat{n}_1 = -\hat{n}_2\)）**：
    若其中一颗顺时针、另一颗逆时针，则 \(\vec{u}_2\) 反向，\(\cos\alpha\) 前的负号变为正号：
    \[
    v_{\text{rel, max}}^{(\text{opp})} = \frac{GM}{2}\left[\frac{1}{L_1} + \frac{1}{L_2} + \sqrt{\frac{e_1^2}{L_1^2} + \frac{e_2^2}{L_2^2} + \frac{2e_1 e_2 \cos\alpha}{L_1 L_2}}\right]
    \]
  - **特殊情况（\(\alpha = 90^\circ, L_1 = L_2 = L\)）**：
    此时 \(\cos 90^\circ = 0\)（同向与反向结果完全相同）：
    \[
    v_{\text{rel, max}} = \frac{GM}{2L}\left(2 + \sqrt{e_1^2 + e_2^2}\right) = \frac{GM}{L}\left(1 + \frac{1}{2}\sqrt{e_1^2 + e_2^2}\right)
    \]

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 独立盲做结果与 Sainavaneet Mukund、Val Karan、Andrei Vila、Lukas Schicht 等全部获奖解答完全一致！
  - **Kalda 的评述亮点**：
    1. 最简洁的证明速度矢端图是圆的方法：直接对牛顿第二定律积分（Andrei Vila）或利用龙格-楞次矢量三角形（Sainavaneet Mukund）。
    2. 只有 Lukas Schicht 和 Ayaan Maan 讨论了两颗卫星反向绕行（一顺一逆，导致 \(-\cos\alpha\) 变为 \(+\cos\alpha\)）的情况，获得了额外奖励分！
    3. Andrei Vila 专门引用了 Kronecker 稠密定理说明为什么周期比为无理数保证了三角不等式等号（上确界）可以任意逼近。
- **核心难点与易错点**：
  1. **陷入坐标空间的极坐标代数暴算**：如果在位置空间写 \(v_r(\theta) = \frac{GM}{h}e\sin\theta\)、\(v_\theta(\theta) = \frac{GM}{h}(1 + e\cos\theta)\)，再投影到固定笛卡尔系求 \(|\vec{v}_1(\theta_1) - \vec{v}_2(\theta_2)|^2\) 对两个独立角度 \(\theta_1, \theta_2\) 的二元函数极值，虽然最终也能通过三角恒等变换凑出结果，但计算量是速度圆几何法的十倍以上！一旦看出 \(\vec{v}(\theta)\) 是“常矢量 + 旋转常模矢量”，问题瞬间退化为小学几何的“两圆上两点最远距离 = 圆心距 + 两半径之和”！
  2. **比角动量 \(h\) 与掠面速率 \(L\) 的因子 2 关系**：题目定义的 \(L_i = \frac{\mathrm{d}A_i}{\mathrm{d}t}\) 是掠面速率，满足 \(h_i = |\vec{r}_i \times \vec{v}_i| = 2L_i\)，极易漏掉分母上的因子 2。

---

## 10. `physicscup-2024-q5-reader` — Water pipe (地下水管传热等待时间)

### Phase 1: 独立盲做记录 (Blind Solve)
- **物理图像与模型建立**：
  长 \(L\)、内半径 \(r\) 的地下水管被初始温度为 \(T_0\) 的無限大土壤包围（土壤比热 \(c\)、密度 \(\rho\)、热导率 \(\kappa\)，热扩散率 \(D = \frac{\kappa}{\rho c}\)；管壁材质与土壤相同）。\(t=0\) 时打开水龙头，温度恒为 \(T_1 > T_0\) 的热水从入口以恒定流速 \(v\) 注入管道（湍流使横截面水温均匀，水比热 \(c_w\)、密度 \(\rho_w\)）。求出口水温达到 \(\frac{1}{2}(T_0 + T_1)\) 所需的等待时间 \(\tau\) 的函数形式与参数量级估计（已知 \(\tau \gg L/v\)）。
- **快慢时间尺度分离与圆柱热传导对数分布**：
  因为等待时间 \(\tau \gg L/v\)（一团水走完管道的时间），在研究土壤缓慢升温的时间尺度上，管内水温分布 \(T_w(x, t)\) 处于**准定常状态**（\(\frac{\partial T_w}{\partial t} \ll v \frac{\partial T_w}{\partial x}\)）。
  在距离入口 \(x\) 处，考虑径向向土壤的传热：经过时间 \(t\) 后，热量在土壤中径向扩散的特征半径（热渗透深度）为：
  \[
  R(t) \sim r + \sqrt{4 D t} = r\left(1 + \sqrt{\frac{4\kappa t}{\rho c r^2}}\right)
  \]
  当 \(r < \tilde{r} < R(t)\) 时，该温升区（“热香肠”区域）内部近似满足二维轴对称准定常拉普拉斯方程：
  \[
  \frac{1}{\tilde{r}}\frac{\partial}{\partial \tilde{r}}\left(\tilde{r}\frac{\partial T_s}{\partial \tilde{r}}\right) \approx 0 \implies T_s(\tilde{r}) \approx T_w(x, t) - \frac{T_w(x, t) - T_0}{\ln\big(R(t)/r\big)} \ln\left(\frac{\tilde{r}}{r}\right)
  \]
  因此，在位置 \(x\) 处，单位长度水管向土壤散失的径向热功率 \(q(x, t) = -\left.2\pi r \kappa \frac{\partial T_s}{\partial \tilde{r}}\right|_{\tilde{r}=r}\) 为：
  \[
  q(x, t) \approx \frac{2\pi \kappa \big(T_w(x, t) - T_0\big)}{\ln\big(R(t)/r\big)}
  \]
- **沿管道的水温指数衰减方程**：
  对于管内流动的水体，能量平衡方程为：
  \[
  \pi r^2 \rho_w c_w v \frac{\partial T_w}{\partial x} = -q(x, t) \approx -\frac{2\pi \kappa \big(T_w - T_0\big)}{\ln\big(R(t)/r\big)}
  \]
  对 \(x\) 从 \(0\)（\(T_w = T_1\)）积分到出口 \(L\)：
  \[
  T_w(L, t) - T_0 = (T_1 - T_0) \exp\left[-\frac{2\kappa L}{\rho_w c_w r^2 v \ln\big(R(t)/r\big)}\right]
  \]
- **求解等待时间 \(\tau\) 的两个渐近极限区域**：
  令出口水温达到温水标准 \(T_w(L, \tau) - T_0 = \frac{1}{2}(T_1 - T_0)\)，两边取对数得核心方程：
  \[
  \ln\left(\frac{R(\tau)}{r}\right) = \frac{2\kappa L}{(\ln 2)\,\rho_w c_w r^2 v}
  \]
  代入 \(R(\tau)/r = \beta(\tau) \approx 1 + \sqrt{\frac{4\kappa \tau}{\rho c r^2}}\)，我们发现根据无量纲管长参数 \(\Lambda \equiv \frac{2\kappa L}{\rho_w c_w r^2 v}\) 的大小，存在两个截然不同的物理机制（Regimes）：
  1. **长管/极慢热渗透区（\(\Lambda \gg 1\)，即 \(\frac{\kappa L}{\rho_w c_w r^2 v} \gg 1\)，指数发散区）**：
     此时要求 \(\ln\big(R(\tau)/r\big) \gg 1\)，即热扩散半径 \(R(\tau) \gg r\)，故 \(\frac{R(\tau)}{r} \approx \sqrt{\frac{4\kappa \tau}{\rho c r^2}}\)。代入上式解得**指数律等待时间**：
     \[
     \ln\sqrt{\frac{4\kappa \tau}{\rho c r^2}} \approx \frac{2\kappa L}{(\ln 2)\,\rho_w c_w r^2 v} \implies \tau \sim \frac{\rho c r^2}{\kappa} \exp\left(\frac{4\kappa L}{(\ln 2)\,\rho_w c_w r^2 v}\right)
     \]
     （注：由于是指数级估计，指数内的常数因子如 \(4/\ln 2 \approx 5.77\) 或 \(4\) 取决于温度达到中点还是 \(1/e\)，但指数函数形式 \(\exp\left(\text{const}\cdot\frac{\kappa L}{\rho_w c_w r^2 v}\right)\) 是绝对核心！）
  2. **中短管/薄边界层区（\(\Lambda \ll 1\) 但仍满足 \(\tau \gg L/v\)，即 \(\frac{\rho_w c_w}{\rho c} \ll \frac{\kappa L}{\rho_w c_w r^2 v} \ll 1\)，平方律区）**：
     此时在等待时间内，热渗透薄层厚度 \(\delta(\tau) = R(\tau) - r \sim \sqrt{\frac{\kappa \tau}{\rho c}} \ll r\)，圆柱曲面可近似展平为一维半无限大平面热传导！
     此时 \(\ln\big(R(\tau)/r\big) = \ln\left(1 + \frac{\delta(\tau)}{r}\right) \approx \frac{\delta(\tau)}{r} \sim \sqrt{\frac{\kappa \tau}{\rho c r^2}}\)。
     代入核心方程：
     \[
     \sqrt{\frac{\kappa \tau}{\rho c r^2}} \sim \frac{\kappa L}{\rho_w c_w r^2 v} \implies \tau \sim \frac{\kappa \rho c L^2}{(\rho_w c_w v r)^2}
     \]
     检验此时 \(\tau \gg L/v\) 的条件：\(\frac{\tau}{L/v} \sim \frac{\kappa L}{\rho_w c_w r^2 v} \cdot \frac{\rho c}{\rho_w c_w} \gg 1\)，当土壤热容与水相当且 \(\Lambda\) 适中时完全可以满足。
  - **统一跨区表达式（Unified Interpolation Formula）**：
    直接保留 \(1 + \sqrt{\frac{4\kappa \tau}{\rho c r^2}} = \exp\left(\frac{2\kappa L}{(\ln 2)\rho_w c_w r^2 v}\right)\)，解得同时涵盖两个极限的统一公式：
    \[
    \tau \sim \frac{\rho c r^2}{4\kappa} \left[\exp\left(\frac{2\kappa L}{(\ln 2)\,\rho_w c_w r^2 v}\right) - 1\right]^2
    \]
    当指数项接近 1 时泰勒展开即给出平方律 \(\tau \propto L^2\)；当指数项远大于 1 时即给出指数律 \(\tau \propto \exp\left(\frac{4\kappa L}{(\ln 2)\rho_w c_w r^2 v}\right)\)！

### Phase 2: 对照官方解答与教学拆解 (Comparison & Breakdown)
- **对照 Jaan Kalda 评述与获奖解答**：
  - 这道题是 Physics Cup 2024 的压轴难题（仅 10 人做对，第 1 条提示前无人做对）。
  - 独立盲做推导出的统一公式 \(\tau = \frac{\rho c r^2}{4\kappa} \left[\exp\left(\frac{2\kappa L}{\rho_w c_w r^2 v \ln 2}\right) - 1\right]^2\) 以及两个极限区域的渐近行为，与 **Luka Passek-Kumerički** 的公式 (16)-(18) 及 **Konstantin Rodionenko** 的分段公式 (13) **一模一样**！
- **核心难点与易错点**：
  1. **二维圆柱热传导的对数奇异性（Logarithmic Singularity）**：在一维半无限大热传导中，热流反比于 \(\sqrt{t}\)，长期积分发散较快；而在三维球对称热传导中，稳态热阻有限（\(R_{\text{th}} = \frac{1}{4\pi \kappa r}\)），即使 \(t \to \infty\) 热损失功率也不会趋于零！唯独在**二维圆柱热传导**中，准稳态热阻 \(R_{\text{th}}(t) \sim \frac{1}{2\pi \kappa} \ln\left(\frac{\sqrt{Dt}}{r}\right)\) 随时间呈极其缓慢的**对数增长**！正是这个 \(\ln(\sqrt{Dt}/r)\)，经过反函数求解后，把等待时间 \(\tau\) 变成了管长 \(L\) 的**指数函数** \(\exp\left(\frac{4\kappa L}{\rho_w c_w r^2 v \ln 2}\right)\)！这是物理学中“量纲分析无法给出指数函数，必须依靠对数边值求解”的绝佳范例。
  2. **局部热平衡能量核算法的自洽验证**：Konstantin Rodionenko 与 Luka Passek-Kumerički 均通过计算半径 \(R(t) = \beta(t) r\) 内的总累积热能 \(Q(t) = \int_r^{\beta r} \rho c (T_s - T_0) 2\pi \tilde{r}\,\mathrm{d}\tilde{r} = \pi \rho c r^2 (T_w - T_0)\left(\frac{\beta^2 - 1}{2\ln\beta} - 1\right)\)，再由 \(\frac{\mathrm{d}Q}{\mathrm{d}t} = q(t) = \frac{2\pi \kappa (T_w - T_0)}{\ln\beta}\) 严格推导出 \(\beta(t)\) 的微分方程 \(\left(\beta - \frac{\beta^2-1}{2\beta\ln\beta}\right)\dot{\beta} = \frac{2\kappa}{\rho c r^2}\)，从而证明了无论在 \(\beta \to 1^+\) 还是 \(\beta \gg 1\) 下，\(\beta(t) \approx 1 + \sqrt{\frac{4\kappa t}{\rho c r^2}}\) 都与位置 \(x\) 及局部温差 \((T_w - T_0)\) 无关！
