# Batch 19 · PLANCKS 2022 UK/IE Preliminaries & PLANCKS 2023 International Finals (Milan) 独立试做与教学拆解报告

本报告包含两部分共 20 道竞赛真题的完整两阶段解答与物理教练拆解：
- **Part I**：PLANCKS 2022 UK & Ireland Preliminaries（`plancks-2022-preliminary-problem-slice-q1` 至 `q10`，共 10 题）。由于题库仅收录原题切片，我们在第一阶段完成独立盲做推导后，于第二阶段采用**多路径交叉验证、量纲与极限检验**以及工程/物理模型精细对比来进行教学拆解。
- **Part II**：PLANCKS 2023 International Finals, Milan（`plancks-2023-final-combined-slice-q1` 至 `q10`，共 10 题）。严格遵循**第一阶段只看原题独立盲做**，**第二阶段对照官方解答（`plancks-2023-final-combined-answer-slice-q1` 至 `q10`）进行对比分析與教学拆解**。

---

# Part I: PLANCKS 2022 UK & Ireland Preliminaries

## Problem 1: The Stellar Engine Solution (`plancks-2022-preliminary-problem-slice-q1`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **物理模型与天体参数提取**：
   - 恒星 Blueberry 的黑体辐射峰值波长 \(\lambda_{\max} = 450\text{ nm} = 4.50 \times 10^{-7}\text{ m}\)，质量 \(M = 4 \times 10^{31}\text{ kg}\)，半径 \(R = 1.75 \times 10^{10}\text{ m}\)。
   - 反射镜（Shkadov 推进器）距离恒星中心 \(d_m = 2 \times 10^{10}\text{ m}\)。
   - 目标：在 \(t = 100\text{ Myr} = 100 \times 3.1536 \times 10^{13}\text{ s} = 3.1536 \times 10^{15}\text{ s}\) 内，将恒星平移 \(s = 5\text{ ly} = 5 \times 9.46 \times 10^{15}\text{ m} = 4.73 \times 10^{16}\text{ m}\)。
2. **恒星有效温度、总光度与镜面处辐射通量**：
   - 由维恩位移定律 \(\lambda_{\max} T_{\text{eff}} = b = 2.898 \times 10^{-3}\text{ m}\cdot\text{K}\)：
     \[
     T_{\text{eff}} = \frac{2.898 \times 10^{-3}}{450 \times 10^{-9}} = 6440\text{ K}
     \]
   - 由斯特藩-玻尔兹曼定律，恒星总光度 \(L\) 为：
     \[
     L = 4\pi R^2 \sigma T_{\text{eff}}^4 = 4\pi (1.75 \times 10^{10})^2 (5.6704 \times 10^{-8}) (6440)^4 \approx 3.754 \times 10^{29}\text{ W}
     \]
   - 在距离 \(d_m = 2 \times 10^{10}\text{ m}\) 处，能流密度（辐射强度）\(I\) 为：
     \[
     I = \frac{L}{4\pi d_m^2} = \sigma T_{\text{eff}}^4 \left(\frac{R}{d_m}\right)^2 \approx 7.468 \times 10^7\text{ W}\cdot\text{m}^{-2}
     \]
3. **第 (a)(i) 问：满足政府要求（最低成本与最小生态影响）的镜面面积**：
   - 恒星初速度为 0，在恒定推力 \(F\) 下做匀加速直线运动，要在时间 \(t\) 内移动距离 \(s\)，所需的最小加速度 \(a_{\min}\) 和最小推力 \(F_{\min}\) 为：
     \[
     s = \frac{1}{2} a_{\min} t^2 \implies a_{\min} = \frac{2s}{t^2} = \frac{2 \times 4.73 \times 10^{16}}{(3.1536 \times 10^{15})^2} \approx 9.512 \times 10^{-15}\text{ m}\cdot\text{s}^{-2}
     \]
     \[
     F_{\min} = M a_{\min} = 4 \times 10^{31} \times 9.512 \times 10^{-15} \approx 3.805 \times 10^{17}\text{ N}
     \]
   - 题目给出了完美反射镜的辐射压强公式 \(\langle P_{\text{rad}} \rangle = \frac{2I}{c}\)。在薄球冠近似（\(A \ll 4\pi d_m^2\)）下，反射镜受到的辐射推力（通过静力平衡传递给恒星的净推力）为 \(F = \langle P_{\text{rad}} \rangle A = \frac{2IA}{c}\)。由此解得最小反射镜面积：
     \[
     A_{\min} = \frac{F_{\min} c}{2I} = \frac{M s c}{I t^2} \approx \frac{3.805 \times 10^{17} \times 3 \times 10^8}{2 \times 7.468 \times 10^7} \approx 7.64 \times 10^{17}\text{ m}^2
     \]
   - *注（动量守恒精细辨析）*：若从“恒星+反射镜”整体系统外逸光子动量流看，被反射镜截获的立体角 \(\Omega = A/d_m^2\) 内的光子若原路反射回恒星并被恒星重吸收，则系统净推力来自对向未遮挡半球的多余光子动量流 \(F = \frac{IA}{c}\)，此时 \(A_{\min} = \frac{F_{\min}c}{I} \approx 1.53 \times 10^{18}\text{ m}^2\)；若如题干所述制成抛物面镜（parabolic mirror）将截获光子沿轴向向后准直反射且不打回恒星表面，则截获光子动量由 \(+p\) 变为 \(-p\)，贡献 \(\frac{2IA}{c}\)。由于 \(A_{\min}/(4\pi d_m^2) \sim 1.5 \times 10^{-4} \ll 1\)，遮挡占比仅 \(0.015\%\)，对文明日常光照影响极小。
4. **第 (a)(ii) 问：最短航行时间对应的最大面积**：
   - 要使时间最短，推进器应覆盖尽可能大的前向立体角，最大可取整个半球面（\(h = d_m\)）：
     \[
     A_{\max} = 2\pi d_m h_{\max} = 2\pi d_m^2 = 2\pi (2 \times 10^{10})^2 \approx 2.51 \times 10^{21}\text{ m}^2
     \]
   - （若进一步考虑反射光子不能被恒星自身半径 \(R\) 挡住，则最大半张角满足 \(\sin\theta_{\max} = \sqrt{1 - (R/d_m)^2}\) 或 \(\cos\theta_{\max} = R/d_m\)，对应 \(h = d_m - R = 2.5 \times 10^9\text{ m}\)，\(A \approx 3.14 \times 10^{20}\text{ m}^2\)）。
5. **第 (b) 问：证明静星体（Statite）平衡与距离 \(d_m\) 无关**：
   - 质量为 \(m_s\)、面积为 \(A\) 的反射镜在距离 \(d_m\) 处受到的恒星万有引力为：
     \[
     F_g = \frac{G M m_s}{d_m^2}
     \]
   - 受到的光压排斥力为：
     \[
     F_{\text{rad}} = \frac{2 I A}{c} = \frac{2 A}{c} \frac{L}{4\pi d_m^2} = \frac{L A}{2\pi c d_m^2}
     \]
   - 令 \(F_g = F_{\text{rad}}\)，两边同时约去 \(d_m^{-2}\)，得到平衡面密度条件 \(\sigma_m = \frac{m_s}{A} = \frac{L}{2\pi G M c}\)，与位置 \(d_m\) 完全无关！

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **多路径交叉验证**：
  - 对球冠在大张角 \(\theta_m\) 下的严格积分：每个立体角元 \(d\Omega = 2\pi\sin\theta\,d\theta\) 沿轴向的投影包含因子 \(\cos\theta\)，积分 \(\int_0^{\theta_m} 2\pi d_m^2 \sin\theta\cos\theta\,d\theta = \pi d_m^2 \sin^2\theta_m = \pi(2d_m h - h^2)\)。当 \(h \ll d_m\) 时，\(\pi(2d_m h - h^2) \approx 2\pi d_m h = A\)，验证了小张角下直接用球冠面积 \(A\) 乘光压的合理性。
- **核心难点与易错点**：
  - **难点**：区分“光打在镜面上的局部光压力 \(\frac{2IA}{c}\)”与“恒星-反射镜复合系统的净辐射反冲力”（需注意恒星自身重吸收与抛物面准直反射的区别）。
  - **易错点**：在计算 \(I\) 时漏乘因子 \((R/d_m)^2\)，误把恒星表面辐射出射度 \(\sigma T_{\text{eff}}^4\) 直接当作 \(d_m\) 处的能流密度 \(I\)。

---

## Problem 2: An Alternative Space Craft (`plancks-2022-preliminary-problem-slice-q2`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：齐奥尔科夫斯基公式推导**：
   - 设飞船瞬时总质量为 \(m\)，速度为 \(v\)，喷气相对飞船的速度大小为 \(u\)。
   - 在无外力空间中，微元时间 \(dt\) 内向后喷出质量为 \(-dm > 0\) 的燃料（速度为 \(v - u\)），飞船质量变为 \(m + dm\)，速度变为 \(v + dv\)。
   - 由动量守恒：
     \[
     m v = (m + dm)(v + dv) + (-dm)(v - u) \implies m\,dv = -u\,dm
     \]
   - 从初始总质量 \(m_i = m_s + m_f\)（初速 \(v_i = 0\)）积分至燃料耗尽时的空船质量 \(m_s\)：
     \[
     v_f = u \ln\left(\frac{m_s + m_f}{m_s}\right) = u \ln\left(1 + \frac{m_f}{m_s}\right)
     \]
2. **第 (b) 问：基于可观测宇宙原子总数 \(N = 10^{82}\) 的最大速度上限估算**：
   - 化学反应释放摩尔能量 \(q = 288\text{ kJ}\cdot\text{mol}^{-1}\)。若燃烧能完全转化为喷气动能 \(\frac{1}{2}\mu u^2 = q\)（其中 \(\mu\) 为每摩尔反应对应的喷气摩尔质量）：
     - 若按氢氧燃烧生成水 \(\text{H}_2 + \frac{1}{2}\text{O}_2 \to \text{H}_2\text{O}\)（标准燃烧热恰为 \(286\text{ kJ/mol}\)，\(\mu = 18\text{ g/mol} = 0.018\text{ kg/mol}\)）：
       \[
       u = \sqrt{\frac{2q}{\mu}} = \sqrt{\frac{2 \times 2.88 \times 10^5}{0.018}} = 4000\sqrt{2}\text{ m/s} \approx 5.66 \times 10^3\text{ m/s}
       \]
     - 若按纯 \(\text{H}_2\) 摩尔质量 \(\mu = 2\text{ g/mol} = 0.002\text{ kg/mol}\) 计算：\(u = 12000\sqrt{2} \approx 1.70 \times 10^4\text{ m/s}\)；若按单原子氢 \(\mu = 1\text{ g/mol} = 0.001\text{ kg/mol}\) 计算：\(u = \sqrt{5.76 \times 10^8} = 2.40 \times 10^4\text{ m/s}\)。
   - 极端情况下，将整个可观测宇宙的所有原子作为燃料（\(m_f / m_s \sim N = 10^{82}\)，空船仅由约 1 个原子构成）：
     \[
     \ln\left(1 + \frac{m_f}{m_s}\right) \approx \ln(10^{82}) = 82 \ln 10 \approx 188.8
     \]
   - 对应的最大末速度上限为：
     - 对 \(\mu = 18\text{ g/mol}\)：\(v_{\max} \approx 5657 \times 188.8 \approx 1.07 \times 10^6\text{ m/s} \approx 3.56 \times 10^{-3} c\)；
     - 对 \(\mu = 2\text{ g/mol}\)：\(v_{\max} \approx 16971 \times 188.8 \approx 3.20 \times 10^6\text{ m/s} \approx 1.07 \times 10^{-2} c\)；
     - 对 \(\mu = 1\text{ g/mol}\)：\(v_{\max} \approx 24000 \times 188.8 \approx 4.53 \times 10^6\text{ m/s} \approx 1.51 \times 10^{-2} c\)。
     可见即使烧光全宇宙的化学燃料，飞船速度也仅能达到约 \(10^{-2} c\) 量级，远无法接近光速！
3. **第 (c) 问：达到 \(v_f = 0.5 c\) 所需的反应能 \(q_{\text{req}}\)**：
   - 由于 \(v_{\max} \propto u \propto \sqrt{q}\)，在相同的质量比极限 \(\ln(10^{82}) \approx 188.8\) 下，所需的喷气速度为 \(u_{\text{req}} = \frac{0.5 c}{82 \ln 10} \approx 7.94 \times 10^5\text{ m/s}\)。
   - 所需摩尔反应能 \(q_{\text{req}} = q \left(\frac{0.5 c}{v_{\max}}\right)^2 = \frac{1}{2}\mu u_{\text{req}}^2\)：
     - 对 \(\mu = 18\text{ g/mol}\)：\(q_{\text{req}} \approx 5.68 \times 10^9\text{ J/mol} = 5.68\text{ GJ/mol}\)；
     - 对 \(\mu = 2\text{ g/mol}\)：\(q_{\text{req}} \approx 6.31 \times 10^8\text{ J/mol} = 631\text{ MJ/mol}\)；
     - 对 \(\mu = 1\text{ g/mol}\)：\(q_{\text{req}} \approx 3.16 \times 10^8\text{ J/mol} = 316\text{ MJ/mol}\)。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **出题人数据设计洞察**：
  - 注意题目给出的 \(q = 288\text{ kJ/mol}\) 满足 \(2 \times 288 = 576 = 24^2\)，且 \(288 / 18 = 16 = 4^2\)！这表明出题人特意凑了完全平方数，使 \(\sqrt{2q/\mu}\) 在 \(\mu = 1\text{ g/mol}\) 时恰好等于整数 \(24\text{ km/s}\)，在 \(\mu = 18\text{ g/mol}\) 时等于 \(4\sqrt{2}\text{ km/s}\)（若漏掉动能系数 \(1/2\) 则恰为 \(4\text{ km/s}\)）。
- **核心难点与易错点**：
  - **难点**：从宏观质量比跨度到宇宙原子总数 \(N = 10^{82}\) 的对数极值估算（理解对数暴政“Tyranny of the Rocket Equation”）。
  - **易错点**：在微元动量守恒中把喷出燃料在惯性系中的速度误写为 \(-u\) 而非 \(v - u\)，导致积分成了线性关系而非对数关系。

---

## Problem 3: What If... All Energy Was Electrical? (`plancks-2022-preliminary-problem-slice-q3`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：表面均匀带电球壳模型的电子“电学半径”**：
   - 假设电子电荷 \(e\) 均匀分布在半径为 \(r_e\) 的球面上。球壳内部（\(r < r_e\)）电场 \(E = 0\)；球壳外部（\(r > r_e\)）电场为 \(E(r) = \frac{ke}{r^2} = \frac{e}{4\pi\varepsilon_0 r^2}\)。
   - 空间总静电能可通过电场能量密度 \(u_E = \frac{1}{2}\varepsilon_0 E^2\) 积分（或由球形电容器自能 \(W = \frac{e^2}{2C}\)，其中 \(C = 4\pi\varepsilon_0 r_e\)）求得：
     \[
     W = \int_{r_e}^{\infty} \frac{1}{2}\varepsilon_0 \left(\frac{e}{4\pi\varepsilon_0 r^2}\right)^2 4\pi r^2\,dr = \frac{e^2}{8\pi\varepsilon_0 r_e} = \frac{k e^2}{2 r_e}
     \]
   - 令静电能等于电子静能 \(W = m c^2\)，解得电子的经典电学半径：
     \[
     r_e = \frac{k e^2}{2 m c^2} = \frac{9 \times 10^9 \times (1.6 \times 10^{-19})^2}{2 \times 9.1 \times 10^{-31} \times (3 \times 10^8)^2} \approx 1.41 \times 10^{-15}\text{ m}
     \]
     （注：若按习惯定义忽略因子 \(1/2\) 令 \(\frac{ke^2}{r_{\text{cl}}} = mc^2\)，则 \(r_{\text{cl}} \approx 2.81 \times 10^{-15}\text{ m}\)）。
2. **第 (b) 问：\(r_{\min} = 10^{-16}\text{ m}\) 球面外的电场有效质量对比**：
   -既然实验已验证库仑定律在 \(r \ge r_{\min} = 10^{-16}\text{ m}\) 处依然成立，则仅在 \(r > r_{\min}\) 区域内的电场能量对应的有效质量 \(m_{\text{eff}}\) 就至少为：
     \[
     m_{\text{eff}} = \frac{W(r > r_{\min})}{c^2} = \frac{k e^2}{2 r_{\min} c^2} = m \frac{r_e}{r_{\min}} \approx 1.28 \times 10^{-29}\text{ kg} \approx 14.1\,m
     \]
     （若不计 \(1/2\) 因子则为 \(2.56 \times 10^{-29}\text{ kg} \approx 28.1\,m\)）。
   - **物理结论**：\(r > 10^{-16}\text{ m}\) 的外部电场等效质量已经是电子实际观测质量的 **14 倍**以上！这说明经典纯电磁质量模型在 \(r < r_e\) 尺度下失效（在量子电动力学 QED 中，由于真空极化与重整化效应，裸质量包含负的自能抵消项）。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **多路径验证**：
  - 方法一：球壳自能 \(W = \frac{1}{2} q V(r_e) = \frac{1}{2} e \left(\frac{ke}{r_e}\right) = \frac{ke^2}{2r_e}\)。
  - 方法二：麦克斯韦应力张量/辐射压积分或能量密度 \(\frac{1}{2}\varepsilon_0 E^2\) 体积分，结果完全一致。
- **核心难点与易错点**：
  - **难点**：理解经典电子半径 \(r_e \sim 10^{-15}\text{ m}\) 与高能散射实验探测极限 \(10^{-16}\text{ m}\) 之间的质量悖论（这正是历史上洛伦兹-阿伯拉罕经典电子论向现代量子场论演进的关键动机）。
  - **易错点**：将自能公式误写为点电荷互能形式 \(\frac{ke^2}{r}\)，遗漏球面组装过程中的积分因子 \(\frac{1}{2}\)。

---

## Problem 4: Refuelling with Hemisphere Hydrodynamics (`plancks-2022-preliminary-problem-slice-q4`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：倒扣半球形漏斗被液体顶起时的临界体积 \(V\)**：
   - 设倒扣半球形漏斗（内半径 \(R\)，质量 \(m\)）底面紧贴水平橡胶垫，从顶部小孔注入密度为 \(\rho\) 的液体，当液面高度达到距底面 \(H\)（\(H < R\)）时漏斗被顶起。
   - **巧妙解法（控制体竖直平衡 vs 球面压强积分）**：
     - **方法一（流体控制体平衡）**：考察漏斗内的液体（体积为 \(V\)）。底面半径为 \(R\)，底面处液体表压强为 \(p_{\text{bottom}} = \rho g H\)，故橡胶垫对液体向上的支持力为 \(F_{\text{base}} = \pi R^2 \rho g H\)。液体受重力 \(\rho g V\) 和漏斗内壁向下的压力 \(F_{\text{up}}\)，由平衡条件得液体对漏斗向上的浮力为：
       \[
       F_{\text{up}} = \rho g (\pi R^2 H - V)
       \]
       而高度为 \(H\) 的半球台体积恰为：
       \[
       V = \int_0^H \pi(R^2 - z^2)\,dz = \pi R^2 H - \frac{1}{3}\pi H^3
       \]
       （或由题给球冠公式：顶部空球冠高为 \(h = R - H\)，故 \(V = \frac{2}{3}\pi R^3 - \frac{\pi(R-H)^2}{3}[3R - (R-H)] = \pi R^2 H - \frac{1}{3}\pi H^3\)）。
       两式相减，发现 \(\pi R^2 H - V\) 极其优美地化简为单项式：
       \[
       F_{\text{up}} = \frac{1}{3}\pi \rho g H^3
       \]
     - **方法二（直接积分验证）**：在高度 \(z \in [0, H]\) 处，压强 \(p(z) = \rho g(H-z)\)，球面环带面积的竖直投影为 \(dA_z = -d(\pi r^2) = 2\pi z\,dz\)，故 \(F_{\text{up}} = \int_0^H \rho g(H-z) 2\pi z\,dz = \frac{1}{3}\pi\rho g H^3\)，完全一致！
   - 令 \(F_{\text{up}} = mg\)，解得临界液面高度 \(H = \left(\frac{3m}{\pi\rho}\right)^{1/3}\)，代入体积表达式得此时漏斗内液体总体积：
     \[
     V = \pi R^2 \left(\frac{3m}{\pi\rho}\right)^{1/3} - \frac{m}{\rho}
     \]
     *注*：若假设液体一直注满至顶部小孔（\(H = R\)）才顶起，则 \(F_{\text{up}} = \rho g(\pi R^3 - V) = mg \implies V = \pi R^3 - \frac{m}{\rho}\)，但题干特别声明“Assume that this volume is strictly less than the total funnel volume”，故 \(H < R\) 的上述解为精确解。
2. **第 (b) 问：半满旋转漏斗的自由液面方程 \(z(r)\)**：
   - 在随漏斗以角速度 \(\omega\) 匀角速旋转的参考系中，液面处质元受重力 \(-g\hat{e}_z\) 与惯性离心力 \(\omega^2 r \hat{e}_r\)。由自由液面与有效势等势面重合（\(\frac{dz}{dr} = \frac{\omega^2 r}{g}\)），积分得旋转抛物面方程：
     \[
     z(r) = z_0 + \frac{\omega^2 r^2}{2g}
     \]
   - 其中轴心液面高度 \(z_0 = z(0)\) 由液体体积守恒确定（以半球最低点为原点 \(z=0\)）：
     - 由题图 2 标注，初始液面位于高度 \(h_0 = R/2\) 处，初始体积为 \(V_0 = \frac{\pi (R/2)^2}{3}(3R - R/2) = \frac{5}{24}\pi R^3\)（若按半球体积的一半理解，则 \(V_0 = \frac{1}{3}\pi R^3\)）。
     - 设旋转抛物面与球面 \(r^2 = 2Rz - z^2\) 交于高度 \(z_1\)（即 \(r_1^2 = 2Rz_1 - z_1^2 = \frac{2g}{\omega^2}(z_1 - z_0)\)）。由于抛物面与平面 \(z = z_1\) 围成的旋转体体积等于同底同高圆柱体积的一半 \(\frac{1}{2}\pi r_1^2 (z_1 - z_0) = \frac{\pi \omega^2 r_1^4}{4g}\)，体积守恒给出隐式代数方程：
       \[
       \frac{\pi z_1^2}{3}(3R - z_1) - \frac{\pi \omega^2}{4g}(2Rz_1 - z_1^2)^2 = V_0, \quad z_0 = z_1 - \frac{\omega^2}{2g}(2Rz_1 - z_1^2)
       \]
3. **第 (c) 问：满漏斗恒定功率加热蒸发时的液面下降规律 \(z(t)\)**：
   - 设以半球底部最低点为 \(z=0\)（故初始满漏斗对应 \(z(0) = R\)）。在时刻 \(t\)，液面高度为 \(z(t)\)，剩余液体体积为球冠体积 \(V(z) = \frac{\pi z^2}{3}(3R - z)\)。
   - 加热器功率为 \(P\)，液体处于沸点，单位质量汽化热为 \(q\)，则单位时间蒸发体积为 \(-\frac{dV}{dt} = \frac{P}{\rho q}\)。
   - 积分得 \(V(0) - V(t) = \frac{Pt}{\rho q}\)，即 \(z(t)\) 满足的三次代数方程与微分方程分别为：
     \[
     \frac{2}{3}\pi R^3 - \frac{\pi z^2(t)}{3}\big[3R - z(t)\big] = \frac{Pt}{\rho q}, \quad \frac{dz}{dt} = -\frac{P}{\pi \rho q z(2R - z)}
     \]
     （若以顶部球心处为 \(z=0\)、向下深度为 \(h(t) = R - z(t)\)，则 \(\pi R^2 h - \frac{1}{3}\pi h^3 = \frac{Pt}{\rho q}\)）。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **多路径交叉验证**：
  - 第 (a) 问中通过控制体与球面微元积分两条完全独立的路径导出 \(F_{\text{up}} = \frac{1}{3}\pi \rho g H^3\)，不仅消除了繁琐的球冠代数展开，而且当 \(H = R\) 时自动恢复经典结论 \(F_{\text{up}}(R) = \frac{1}{3}\pi \rho g R^3 = \pi R^3 \rho g - \frac{2}{3}\pi R^3 \rho g\)。
- **核心难点与易错点**：
  - **难点**：第 (a) 问识别出未注满时底面压强为 \(\rho g H\) 而非 \(\rho g R\)，并消去中间变量 \(H\)。
  - **易错点**：将向上的浮力误写为阿基米德排水重量 \(\rho g V\)（实际上容器壁对内部液体的竖直力是向下的，对容器壁则是向上的 \(\rho g(\pi R^2 H - V)\)）。

---

## Problem 5: Simple Harmonic Mattresses (`plancks-2022-preliminary-problem-slice-q5`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **单弹簧基准周期**：\(\tau = 2\pi\sqrt{\frac{m}{k}}\)，记各情形周期为 \(\tau_i = \lambda_i \tau\)，则 \(\lambda_i = \sqrt{\frac{k}{k_{\text{eff},i}}}\)。
2. **第 (a) 问：沿运动方向对称布置的两根弹簧（图 2）**：
   - 当质点向右偏离平衡位置 \(x\) 时，左弹簧伸长 \(L - l_0 + x\)，右弹簧伸长 \(L - l_0 - x\)。
   - 合力 \(F_x = -k(L - l_0 + x) + k(L - l_0 - x) = -2kx\)，有效劲度系数 \(k_{\text{eff},1} = 2k\)，故：
     \[
     \lambda_1 = \frac{1}{\sqrt{2}}
     \]
3. **第 (b) 问：垂直于运动方向对称布置的两根弹簧（图 3）**：
   - 平衡时两弹簧长度均为 \(L > l_0\)，存在预张力 \(T_0 = k(L - l_0)\)。
   - 当质点沿 \(x\) 移动微小位移 \(x\)（记 \(X = x/L \ll 1\)）时，弹簧长度 \(l = \sqrt{L^2 + x^2} = L\sqrt{1 + X^2} = L + \mathcal{O}(X^2)\)。
   - 每根弹簧拉力保持 \(T = k(l - l_0) = k(L - l_0) + \mathcal{O}(X^2)\)，其沿 \(-x\) 方向的分力为 \(T\sin\phi = T\frac{x}{l} = k\left(1 - \frac{l_0}{L}\right)x + \mathcal{O}(X^3)\)。
   - 两根弹簧合恢复力为 \(F_x = -2k\left(1 - \frac{l_0}{L}\right)x\)，故 \(k_{\text{eff},2} = 2k\frac{L - l_0}{L}\)，从而：
     \[
     \lambda_2 = \frac{1}{\sqrt{2\left(1 - \frac{l_0}{L}\right)}} = \sqrt{\frac{L}{2(L - l_0)}}
     \]
4. **第 (c) 问：斜向对称弹簧的几何展开与一阶恢复力**：
   - 在 \(\triangle BPE\) 中，\(BE = L\)，\(EP = x\)，\(\angle BEP = \pi - \theta\)。由余弦定理：
     \[
     l_1 = \sqrt{L^2 + x^2 + 2Lx\cos\theta} = L\sqrt{1 + 2X\cos\theta + X^2} = L(1 + X\cos\theta) + \mathcal{O}(X^2)
     \]
   - 端点的水平投影为 \(L\cos\theta + x\)，故 \(\cos\alpha = \frac{L\cos\theta + x}{l_1}\)：
     \[
     \cos\alpha = \frac{\cos\theta + X}{1 + X\cos\theta} = (\cos\theta + X)(1 - X\cos\theta) + \mathcal{O}(X^2) = \cos\theta + X(1 - \cos^2\theta) + \mathcal{O}(X^2)
     \]
   - 同理对右弹簧 \(AP\)，将 \(\theta\) 换为 \(\pi - \theta\)（或 \(X \to -X\)）：
     \[
     l_2 = L(1 - X\cos\theta) + \mathcal{O}(X^2), \quad \cos\beta = \cos\theta + X(\cos^2\theta - 1) + \mathcal{O}(X^2)
     \]
   - 按题干第 (c) 问后半部分要求：仅考虑相对于平衡长度 \(L\) 的附加弹力（即相当于取 \(L = l_0\) 无预张力情形），左弹簧附加拉力 \(F_1 = k(l_1 - L) = kx\cos\theta\)，右弹簧附加压力 \(F_2 = k(L - l_2) = kx\cos\theta\)，它们在 \(x\) 方向的一阶合分力为：
     \[
     F_{x,\text{pair}} = -F_1\cos\alpha - F_2\cos\beta = -kx\cos\theta(\cos\theta + \mathcal{O}(X)) - kx\cos\theta(\cos\theta + \mathcal{O}(X)) = -2kx\cos^2\theta
     \]
5. **第 (d) 问（正方形四弹簧，图 5）与第 (e) 问（正六边形六弹簧，图 6）**：
   - **口径一（直接调用第 (c) 问给出的成对恢复力公式 \(-2kx\cos^2\theta\)）**：
     - **(d) 正方形对角线四根弹簧**：可分为两对斜向弹簧，夹角均为 \(\theta = 45^\circ\)（\(\cos^2 45^\circ = 1/2\)）。总恢复力为 \(F_x = 2 \times (-2kx\cos^2 45^\circ) = -2kx\)，即 \(k_{\text{eff},3} = 2k\)，故：
       \[
       \lambda_3 = \frac{1}{\sqrt{2}}
       \]
     - **(e) 正六边形六根弹簧**：包含 1 对沿 \(x\) 轴弹簧（\(\theta = 0^\circ\)，贡献 \(-2kx\)）和 2 对夹角为 \(\theta = 60^\circ\) 的弹簧（\(\cos^2 60^\circ = 1/4\)，每对贡献 \(-2kx \times \frac{1}{4} = -\frac{1}{2}kx\)）。总恢复力为 \(F_x = -2kx + 2\times(-\frac{1}{2}kx) = -3kx\)，即 \(k_{\text{eff},4} = 3k\)，故：
       \[
       \lambda_4 = \frac{1}{\sqrt{3}}
       \]
   - **口径二（计入平衡预张力 \(T_0 = k(L - l_0) > 0\) 的严格通解）**：
     - 若 \(L > l_0\)，则总张力为 \(T_1 = T_0 + kx\cos\theta\)，\(T_2 = T_0 - kx\cos\theta\)。利用第 (c) 问导出的 \(\cos\alpha\) 和 \(\cos\beta\) 展开式，一对夹角为 \(\theta\) 的弹簧总恢复力为：
       \[
       F_{x,\text{pair}} = -T_1\cos\alpha + T_2\cos\beta = -2kx\cos^2\theta - 2T_0 X\sin^2\theta = -2kx\left(1 - \frac{l_0}{L}\sin^2\theta\right)
       \]
     - 代入正方形（两对 \(\theta = 45^\circ\)）得 \(k_{\text{eff},3} = 2k\left(2 - \frac{l_0}{L}\right) \implies \lambda_3 = \sqrt{\frac{L}{2(2L - l_0)}}\)；代入正六边形（一对 \(\theta=0^\circ\)、两对 \(\theta=60^\circ\)）得 \(k_{\text{eff},4} = 3k\left(2 - \frac{l_0}{L}\right) \implies \lambda_4 = \sqrt{\frac{L}{3(2L - l_0)}}\)。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **原题命题瑕疵洞察与张量对称性秒杀**：
  - 仔细审视第 (c) 问可以发现一个非常有趣的命题痕迹：出题人在 (c) 的前半部分特意要求证明 \(\cos\alpha = \cos\theta + X(1-\cos^2\theta)\)，这一项只有在乘以零阶预张力 \(T_0 = k(L-l_0)\) 时才会产生一阶恢复力 \(-2k(1-\frac{l_0}{L})\sin^2\theta\,x\)（且当 \(\theta = 90^\circ\) 时恰好退化为第 (b) 问的结论！）；但在 (c) 的后半部分，出题人却直接令 \(F_1 = F_2 = kx\cos\theta\)（相当于临时取了 \(l_0 = L\)），从而得到了 \(-2kx\cos^2\theta\)。我们在解答中同时给出了两种口径的结果，既贴合考场评分标准，又保持了物理严密性。
  - **二阶张量各向同性定理秒杀**：对于正 \(N\) 边形（\(N \ge 3\)）均匀分布的 \(N\) 根弹簧，平面内的有效劲度张量 \(K_{ij} = \sum_{a=1}^N k_{ij}^{(a)}\) 具有 \(C_N\) 旋转对称性，因而必为各向同性张量 \(K_{ij} = k_{\text{eff}}\delta_{ij}\)！其迹 \(\text{Tr}(K) = 2k_{\text{eff}}\) 等于单根弹簧纵向劲度 \(k_\parallel = k\) 与横向劲度 \(k_\perp = k(1 - l_0/L)\) 之和的 \(N\) 倍，故一眼可知 \(k_{\text{eff}} = \frac{N}{2}(k_\parallel + k_\perp)\)，无论沿哪个方向振动周期均完全相同！

---

## Problem 6: The Firefly Dance (`plancks-2022-preliminary-problem-slice-q6`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：无量纲同步动力学方程（Adler 方程）**：
   - 定义刺激源与萤火虫的**相位差（phase difference）** \(\phi(t) = \Theta(t) - \theta(t)\)。
   - 对时间求导并代入 \(\dot{\Theta} = \Omega\) 及 \(\dot{\theta} = \omega + A\sin(\Theta - \theta)\)：
     \[
     \dot{\phi} = \dot{\Theta} - \dot{\theta} = \Omega - \omega - A\sin\phi
     \]
   - 引入无量纲时间 \(\tau = At\) 和无量纲频率失配参数 \(\mu = \frac{\Omega - \omega}{A}\)，得到关于 \(\phi(\tau)\) 的一阶自治微分方程：
     \[
     \phi' = \frac{d\phi}{d\tau} = \mu - \sin\phi
     \]
   - 物理量 \(\phi\) 是**相位差（phase difference）**。
2. **第 (b) 问：三种参数区间下的相图 \((\phi', \phi)\) 与不动点稳定性**：
   - 考察一个周期区间 \(\phi \in [-\pi, \pi]\) 上的相轨迹 \(\phi'(\phi) = \mu - \sin\phi\)：
     - **(i) \(\mu = 0\)**：\(\phi' = -\sin\phi\)。在 \([-\pi, \pi]\) 上有三个不动点 \(\phi^* = -\pi, 0, \pi\)。当 \(\phi \in (-\pi, 0)\) 时 \(\phi' > 0\)（箭头向右），当 \(\phi \in (0, \pi)\) 时 \(\phi' < 0\)（箭头向左）。因此 \(\phi^* = 0\) 是唯一的**稳定不动点**（\(\frac{d\phi'}{d\phi}\big|_0 = -1 < 0\)），而 \(\phi^* = \pm\pi\) 是不稳定不动点。
     - **(ii) \(0 < \mu < 1\)**：曲线 \(\mu - \sin\phi\) 向上平移，在 \([-\pi, \pi]\) 内有两个不动点：\(\phi_s^* = \arcsin\mu \in (0, \frac{\pi}{2})\)（斜率 \(-\cos\phi_s^* < 0\)，两侧箭头指向它，为**稳定不动点**）和 \(\phi_u^* = \pi - \arcsin\mu \in (\frac{\pi}{2}, \pi)\)（斜率 \(-\cos\phi_u^* > 0\)，两侧箭头背离它，为**不稳定不动点**）。
     - **(iii) \(\mu > 1\)**：由于 \(\sin\phi \le 1 < \mu\)，恒有 \(\phi' = \mu - \sin\phi > 0\)，相轴上箭头处处向右，**不存在任何不动点**（在 \(\mu = 1\) 处发生鞍结分岔 Saddle-Node Bifurcation）。
3. **第 (c) 问：\(\mu = 0\) 时的完全同步（同时闪烁）**：
   - 当 \(\mu = 0\)（即 \(\Omega = \omega\)）时，除测度为零的初始反相点 \(\phi(0) = \pm\pi\) 外，一切初值均流向稳定不动点 \(\phi^* = 0\)，即 \(t \to \infty\) 时 \(\Theta(t) - \theta(t) \to 0\)，萤火虫与外部刺激源最终**同时闪烁**。
4. **第 (d) 问：\(\mu \in (0, 1)\) 时的锁相（Phase-locking）**：
   - 当 \(0 < \mu < 1\) 时，系统收敛至稳定不动点 \(\phi_s^* = \arcsin\mu\)。此时 \(\dot{\phi} = 0 \implies \dot{\theta} = \dot{\Theta} = \Omega\)，即萤火虫成功被牵引到与外部刺激相同的频率 \(\Omega\)，但两者之间保持一个恒定非零的相位滞后 \(\phi_s^* = \arcsin\left(\frac{\Omega-\omega}{A}\right)\)（因为 \(\omega < \Omega\)，萤火虫需要落后一个固定相角以获得持续的正向加速补偿 \(A\sin\phi_s^* = \Omega - \omega\)）。这种“频率完全一致、相位差恒定非零”的状态即称为**锁相（phase-locking）**。
5. **第 (e) 问：\(\mu > 1\) 时相位漂移（Phase drift）的最快与最慢位置**：
   - 漂移速率 \(\phi'(\tau) = \mu - \sin\phi\)：
     - **最快漂移**：当 \(\sin\phi = -1\)，即 \(\phi = \Theta - \theta = -\frac{\pi}{2}\pmod{2\pi}\)（或 \(\frac{3\pi}{2}\)）时，\(\phi'_{\max} = \mu + 1\)；
     - **最慢漂移**：当 \(\sin\phi = +1\)，即 \(\phi = \Theta - \theta = \frac{\pi}{2}\pmod{2\pi}\) 时，\(\phi'_{\min} = \mu - 1\)（即刚越过鞍结分岔后的“幽灵瓶颈”区域）。
6. **第 (f) 问：牵引范围（Range of entrainment / 阿诺德舌）**：
   - 能够实现频率牵引的充要条件是相空间存在稳定不动点，即 \(|\sin\phi^*| = |\mu| \le 1\)：
     \[
     \left|\frac{\Omega - \omega}{A}\right| \le 1 \implies \omega - A \le \Omega \le \omega + A
     \]
7. **第 (g) 问：\(\mu > 1\) 时的相位漂移周期 \(T\)**：
   - 相位差 \(\phi\) 走过 \(2\pi\) 所需的时间为：
     \[
     T = \int_0^{2\pi} \frac{dt}{d\phi}\,d\phi = \frac{1}{A}\int_0^{2\pi} \frac{d\phi}{\mu - \sin\phi}
     \]
   - 令万能代换 \(u = \tan\frac{\phi}{2}\)（\(\sin\phi = \frac{2u}{1+u^2}\)，\(d\phi = \frac{2\,du}{1+u^2}\)）：
     \[
     \int_{-\infty}^{\infty} \frac{2\,du}{\mu(1+u^2) - 2u} = \frac{2}{\mu}\int_{-\infty}^{\infty} \frac{du}{\left(u - \frac{1}{\mu}\right)^2 + \left(1 - \frac{1}{\mu^2}\right)} = \frac{2\pi}{\sqrt{\mu^2 - 1}}
     \]
   - 故物理漂移周期为：
     \[
     T = \frac{2\pi}{A\sqrt{\mu^2 - 1}} = \frac{2\pi}{\sqrt{(\Omega - \omega)^2 - A^2}}
     \]
   - 当 \(\mu \in [0, 1)\) 时，相位差 \(\phi(t)\) 被吸引并锁定在稳定不动点 \(\phi_s^*\)，永远不会完成 \(2\pi\) 的滑移循环，因此漂移周期 \(T \to \infty\)（或无定义）。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **多路径交叉验证**：
  - 对积分 \(\int_0^{2\pi}\frac{d\phi}{\mu-\sin\phi}\) 还可用复变函数留数定理验证：令 \(z = e^{i\phi}\)，\(\sin\phi = \frac{z - z^{-1}}{2i}\)，\(\oint_{|z|=1} \frac{dz}{i z [\mu - (z-z^{-1})/(2i)]} = -\oint \frac{2\,dz}{z^2 - 2i\mu z - 1}\)，单位圆内唯一极点为 \(z_+ = i(\mu - \sqrt{\mu^2-1})\)，留数给出 \(2\pi i \cdot \frac{-2}{2z_+ - 2i\mu} = \frac{2\pi}{\sqrt{\mu^2-1}}\)，与实积分结果完全一致。
  - 极限检验：当 \(\mu \gg 1\)（\(A \to 0\)）时，\(T \to \frac{2\pi}{\Omega - \omega}\)，退化为两个独立振子的普通拍频周期！
- **核心难点与易错点**：
  - **难点**：理解鞍结分岔（\(\mu = 1\)）附近的临界慢化标度律 \(T \propto (\mu - 1)^{-1/2}\) 以及万能代换积分。
  - **易错点**：在判断不动点稳定性时混淆 \(\phi = \arcsin\mu\) 与 \(\pi - \arcsin\mu\) 的导数符号。

---

## Problem 7: Bending Light in a Plane (`plancks-2022-preliminary-problem-slice-q7`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：利用费马原理导出光线轨迹方程 \(y(x)\)**：
   - 介质折射率仅与高度 \(y\) 有关：\(n(y) = \sqrt{1 + e^{-y/2}}\)。
   - 根据费马最短时间原理，光程泛函为：
     \[
     S = \int n(y)\,ds = \int n(y)\sqrt{1 + (y')^2}\,dx, \quad y' = \frac{dy}{dx}
     \]
   - 由于被积函数 \(L(y, y') = n(y)\sqrt{1 + (y')^2}\) 不显含水平坐标 \(x\)，由贝尔特拉米恒等式（Beltrami identity，或水平分层介质的连续斯涅尔定律 \(n(y)\cos\alpha(y) = \text{const}\)）得第一积分：
     \[
     y'\frac{\partial L}{\partial y'} - L = -\frac{n(y)}{\sqrt{1 + (y')^2}} = -C
     \]
   - 代入初始条件：在原点 \((x, y) = (0, 0)\) 处，\(n(0) = \sqrt{1 + e^0} = \sqrt{2}\)，光线沿 \(45^\circ\) 向上射出，故 \(y'(0) = \tan 45^\circ = 1\)。由此定出守恒常数 \(C\)：
     \[
     C = \frac{n(0)}{\sqrt{1 + y'(0)^2}} = \frac{\sqrt{2}}{\sqrt{1 + 1^2}} = 1
     \]
   - 将 \(C = 1\) 和 \(n(y) = \sqrt{1 + e^{-y/2}}\) 代回一阶微分方程：
     \[
     \frac{\sqrt{1 + e^{-y/2}}}{\sqrt{1 + (y')^2}} = 1 \implies 1 + (y')^2 = 1 + e^{-y/2} \implies \frac{dy}{dx} = e^{-y/4} \quad (y' > 0)
     \]
   - 分离变量积分：
     \[
     \int_0^y e^{u/4}\,du = \int_0^x dx' \implies 4\left(e^{y/4} - 1\right) = x
     \]
   - 解得光线轨迹的显式解析方程：
     \[
     y(x) = 4\ln\left(1 + \frac{x}{4}\right) \quad \left(\text{或 } x(y) = 4\big(e^{y/4} - 1\big)\right)
     \]
2. **第 (b) 问：光线轨迹图像特征绘制**：
   - 曲线过原点 \((0, 0)\)，在原点处切线斜率为 \(y'(0) = 1\)（\(45^\circ\) 角）；
   - 在 \(x > 0\) 区域，\(y(x) = 4\ln(1 + x/4)\) 单调递增且上凸（\(y''(x) = -\frac{1}{4(1+x/4)^2} < 0\)），随着 \(x \to \infty\)，高度 \(y \to \infty\)，斜率 \(y'(x) = \frac{1}{1+x/4} \to 0\)（光线逐渐向水平方向弯曲，但无最高点全反射，而是对数发散上升）。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **多路径交叉验证**：
  - 直接用欧拉-拉格朗日方程或光学哈密顿方程验证：对 \(y(x) = 4\ln(1+x/4)\) 求导得 \(y' = \frac{4}{x+4} = e^{-y/4}\)，代入 \(\frac{d}{dx}\left(\frac{n(y)}{\sqrt{1+y'^2}}\right) = \frac{d}{dx}(1) = 0\)，恒等成立！
  - 物理图像解释：因为 \(y \to \infty\) 时折射率下限 \(n(\infty) = 1\) 恰好等于初始斯涅尔不变量 \(n(0)\cos 45^\circ = 1\)，所以光线正好以 \(y = \infty\) 为渐近全反射临界层（斜率渐近趋于 0 而不会掉头向下）。
- **核心难点与易错点**：
  - **难点**：从费马泛函识别出 \(x\) 为循环坐标，直接写出 Beltrami 第一积分 \(\frac{n(y)}{\sqrt{1+(y')^2}} = C\)（即连续斯涅尔定律 \(n(y)\sin\theta_{\text{inc}}(y) = C\)）。
  - **易错点**：把斯涅尔定律中的入射角（光线与竖直法线 \(y\) 轴的夹角）与仰角（光线与水平 \(x\) 轴的夹角）弄混（本题 \(\theta_0 = 45^\circ\) 恰好正余弦相等，但若写为 \(n(y)\frac{y'}{\sqrt{1+y'^2}} = C\) 则完全错误）。

---

## Problem 8: A Magnetic Spa Day (`plancks-2022-preliminary-problem-slice-q8`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：球坐标下的偶极-偶极相互作用势参数化**：
   - 取 \(\mathbf{r} = r\hat{z}\)，则 \(\hat{r} = \hat{z}\)。在球坐标系中，\(\mathbf{d}_i = d_i(\sin\theta_i\cos\phi_i\hat{x} + \sin\theta_i\sin\phi_i\hat{y} + \cos\theta_i\hat{z})\)。
   - 计算点积：\(\mathbf{d}_i \cdot \hat{r} = d_i\cos\theta_i\)，以及：
     \[
     \mathbf{d}_1 \cdot \mathbf{d}_2 = d_1 d_2\big[\sin\theta_1\sin\theta_2(\cos\phi_1\cos\phi_2 + \sin\phi_1\sin\phi_2) + \cos\theta_1\cos\theta_2\big]
     \]
   - 利用 \(\cos\phi_1\cos\phi_2 + \sin\phi_1\sin\phi_2 = \cos(\phi_1 - \phi_2)\)，代入 \(V(\mathbf{r})\) 得：
     \[
     V(\mathbf{r}) = \frac{\mu_0 d_1 d_2}{4\pi r^3}\big(\sin\theta_1\sin\theta_2\cos(\phi_1 - \phi_2) - 2\cos\theta_1\cos\theta_2\big)
     \]
2. **第 (b) 问：高温极限 \(\lambda \ll 1\) 下的平均轴向力 \(\langle F_z \rangle\)**：
   - 记角向因子为 \(g(\Omega_1, \Omega_2) = \sin\theta_1\sin\theta_2\cos(\phi_1-\phi_2) - 2\cos\theta_1\cos\theta_2\)，则 \(\beta V = \frac{V}{k_B T} = \lambda g\)，其中 \(\lambda = \frac{\mu_0 d_1 d_2}{4\pi r^3 k_B T} \ll 1\)。
   - 在固定距离 \(r\)（沿 \(z\) 轴）下，两偶极子间的 \(z\) 方向力为：
     \[
     F_z = -\frac{\partial V}{\partial r} = \frac{3V}{r} = \frac{3 k_B T}{r}\lambda g
     \]
   - 在正则系综中对两个偶极子的立体角 \(d\Omega_i = \sin\theta_i\,d\theta_i\,d\phi_i\) 进行玻尔兹曼加权平均，并按 \(\lambda \ll 1\) 展开 \(e^{-\lambda g} = 1 - \lambda g + \mathcal{O}(\lambda^2)\)：
     \[
     \langle F_z \rangle = \frac{3 k_B T}{r}\lambda \frac{\langle g(1 - \lambda g + \dots)\rangle_0}{\langle 1 - \lambda g + \dots \rangle_0}
     \]
     其中 \(\langle \cdots \rangle_0 = \frac{1}{(4\pi)^2}\int d\Omega_1\int d\Omega_2 (\cdots)\) 表示自由各向同性平均。
   - 计算一阶与二阶角向矩：
     - 一阶矩：由于 \(\int_0^{2\pi}\cos(\phi_1-\phi_2)\,d\phi_1 = 0\) 且 \(\int_0^\pi \cos\theta_i\sin\theta_i\,d\theta_i = 0\)，故 \(\langle g \rangle_0 = 0\)（一阶热平均力为零）。
     - 二阶矩：交叉项关于 \(\phi_1\) 积分为零，利用 \(\langle \cos^2\theta \rangle_0 = \frac{1}{2}\int_{-1}^1 u^2\,du = \frac{1}{3}\)，\(\langle \sin^2\theta \rangle_0 = \frac{2}{3}\)，\(\langle \cos^2(\phi_1-\phi_2) \rangle_0 = \frac{1}{2}\)：
       \[
       \langle g^2 \rangle_0 = \langle \sin^2\theta_1 \rangle_0 \langle \sin^2\theta_2 \rangle_0 \langle \cos^2(\phi_1-\phi_2) \rangle_0 + 4\langle \cos^2\theta_1 \rangle_0 \langle \cos^2\theta_2 \rangle_0 = \frac{2}{3}\cdot\frac{2}{3}\cdot\frac{1}{2} + 4\cdot\frac{1}{3}\cdot\frac{1}{3} = \frac{2}{9} + \frac{4}{9} = \frac{2}{3}
       \]
   - 因此领头阶（\(\lambda^2\) 阶）平均力为：
     \[
     \langle F_z \rangle = -\frac{3 k_B T}{r}\lambda^2 \langle g^2 \rangle_0 = -\frac{2 k_B T}{r}\lambda^2 = -\frac{\mu_0^2 d_1^2 d_2^2}{8\pi^2 k_B T r^7}
     \]
   - 负号表明 \(\langle F_z \rangle < 0\)（指向 \(-z\) 即减小间距 \(r\) 的方向），故该力为**吸引力（attractive）**！物理本质是低能吸引取向态的玻尔兹曼权重 \(e^{-\beta V} > 1\) 高于高能排斥取向态的权重 \(e^{-\beta V} < 1\)。
3. **第 (c) 问：垂直方向（\(x, y\) 方向）平均力为零的对称性解释**：
   - 当两偶极子连线沿 \(z\) 轴时，系统的哈密顿量与玻尔兹曼分布对于绕 \(z\) 轴的任意旋转（\(\phi_1 \to \phi_1 + \alpha, \phi_2 \to \phi_2 + \alpha\)）以及反映变换（\(x \to -x, y \to -y\)）具有严格对称性。在 \(xy\) 平面内不存在任何特殊方向，因此横向力的热平均值 \(\langle F_x \rangle = \langle F_y \rangle = 0\) 恒成立。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **自由能路径验证（统计力学标准方法）**：
  - 计算配分函数 \(Z = \langle e^{-\beta V} \rangle_0 = 1 + \frac{1}{2}\lambda^2 \langle g^2 \rangle_0 + \mathcal{O}(\lambda^4) = 1 + \frac{1}{3}\lambda^2\)。
  - 亥姆霍兹自由能 \(F_{\text{Helmholtz}} = -k_B T \ln Z \approx -\frac{1}{3} k_B T \lambda^2 \propto -r^{-6}\)（即著名的 Keesom 取向范德瓦耳斯势 \(U_{\text{Keesom}} \propto -1/(T r^6)\)）。
  - 对 \(r\) 求负梯度：\(\langle F_z \rangle = -\frac{\partial F_{\text{Helmholtz}}}{\partial r} = \frac{1}{3} k_B T \frac{\partial (\lambda^2)}{\partial r} = -\frac{2 k_B T}{r}\lambda^2\)，结果完全一致且物理图像极为清晰！
- **核心难点与易错点**：
  - **难点**：球面上 \(\langle \sin^2\theta \rangle = 2/3\) 与 \(\langle \cos^2\theta \rangle = 1/3\) 的立体角积分测度 \(\frac{1}{2}\sin\theta\,d\theta\)。
  - **易错点**：做角度平均时漏掉雅可比因子 \(\sin\theta\)，误按 \(\frac{1}{\pi}\int_0^\pi \cos^2\theta\,d\theta = \frac{1}{2}\) 计算，从而算错系数。

---

## Problem 9: Droplets in SPACE (`plancks-2022-preliminary-problem-slice-q9`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：零重力下自由悬浮液滴的主模振荡本征频率估算**：
   - 驱动液滴形变振荡的物理量仅有：表面张力系数 \(\gamma\)（单位 \(\text{N}\cdot\text{m}^{-1} = \text{kg}\cdot\text{s}^{-2}\)）、液体密度 \(\rho\)（单位 \(\text{kg}\cdot\text{m}^{-3}\)）以及液滴平衡半径 \(R\)（单位 \(\text{m}\)）。
   - **方法一（量纲分析法）**：设本征角频率 \(\omega \propto \gamma^a \rho^b R^c\)，对比基本量纲 \([\text{M}], [\text{L}], [\text{T}]\)：
     \[
     \text{T}^{-1} = (\text{M}\cdot\text{T}^{-2})^a (\text{M}\cdot\text{L}^{-3})^b \text{L}^c = \text{M}^{a+b} \text{L}^{-3b+c} \text{T}^{-2a}
     \]
     解得 \(a = \frac{1}{2}\)，\(b = -a = -\frac{1}{2}\)，\(c = 3b = -\frac{3}{2}\)。因此主模本征角频率与频率分别为：
     \[
     \omega \sim \sqrt{\frac{\gamma}{\rho R^3}}, \quad f = \frac{\omega}{2\pi} \sim \frac{1}{2\pi}\sqrt{\frac{\gamma}{\rho R^3}}
     \]
   - **方法二（能量/力标度法验证）**：设液滴发生幅度为 \(\xi \ll R\) 的四极形变（体积守恒，表面积增量 \(\Delta S \sim \xi^2\)），恢复势能 \(U \sim \gamma \Delta S \sim \gamma \xi^2\)（等效劲度系数 \(k_{\text{eff}} \sim \gamma\)），参与振荡的有效质量 \(m_{\text{eff}} \sim \rho R^3\)，故 \(\omega \sim \sqrt{k_{\text{eff}}/m_{\text{eff}}} \sim \sqrt{\gamma/(\rho R^3)}\)。
2. **第 (b) 问：空间站天花板上悬挂液滴的最大可能半径 \(R_{\max}\)**：
   - 悬挂在天花板上的液滴受向下的重力 \(F_g \sim \rho R^3 g\)（其中 \(g\) 为空间站人工重力加速度）和沿接触周长 \(L_c \sim R\) 的表面张力向上拉住的毛细力 \(F_{\text{cap}} \sim \gamma R\)。
   - 当液滴半径增大至临界脱落状态时，重力与最大表面张力平衡：
     \[
     \gamma R_{\max} \sim \rho g R_{\max}^3 \implies R_{\max} \sim \sqrt{\frac{\gamma}{\rho g}}
     \]
     （即流体的**毛细长度 Capillary length** \(l_c = \sqrt{\frac{\gamma}{\rho g}}\)；若计及半球几何因子 \(2\pi R \gamma \sim \frac{2}{3}\pi R^3 \rho g\)，则 \(R_{\max} \approx \sqrt{\frac{3\gamma}{\rho g}}\)）。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **与瑞利精确理论对比**：
  - 瑞利（Lord Rayleigh, 1879）对无粘不可压缩液滴球谐模 \(Y_{lm}\) 的精确色散关系为 \(\omega_l^2 = \frac{l(l-1)(l+2)\gamma}{\rho R^3}\)。由于 \(l=0\) 违背体积不可压缩、\(l=1\) 对应质心平动（\(\omega_1 = 0\)），最低阶基模为四极形变 \(l=2\)，精确系数为 \(\omega_2 = \sqrt{\frac{8\gamma}{\rho R^3}} \approx 2.83\sqrt{\frac{\gamma}{\rho R^3}}\)（频率 \(f_2 = \frac{\sqrt{2}}{\pi}\sqrt{\frac{\gamma}{\rho R^3}} \approx 0.45\sqrt{\frac{\gamma}{\rho R^3}}\)），量纲法完美抓住了核心标度！
- **核心难点与易错点**：
  - **难点**：熟练运用白金汉 \(\Pi\) 定理（Buckingham \(\Pi\) theorem）将表面张力系数 \(\gamma\) 化为基本质量-时间量纲 \(\text{kg}\cdot\text{s}^{-2}\)（注意到其中不含长度量纲！）。
  - **易错点**：误以为表面张力 \(\gamma\) 的量纲中含有长度 \(\text{L}\)，实际上 \([\gamma] = \frac{[\text{Force}]}{[\text{Length}]} = \frac{\text{M}\cdot\text{L}\cdot\text{T}^{-2}}{\text{L}} = \text{M}\cdot\text{T}^{-2}\)，直接等效于弹簧劲度系数 \([k]\)！

---

## Problem 10: Oscillators on a Train (`plancks-2022-preliminary-problem-slice-q10`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **已知参数梳理**：
   - 谐振子固有周期 \(T = 2\pi\sqrt{\frac{m}{k}} = 1\text{ s}\)，固有角频率 \(\omega = \frac{2\pi}{T} = 2\pi\text{ rad/s}\)。
   - 列车从静止开始做匀加速直线运动，历时 \(\Delta t = 60\text{ s}\) 达到巡航速度 \(v_f = 30\text{ m/s}\)，故列车加速度为：
     \[
     a = \frac{v_f}{\Delta t} = \frac{30\text{ m/s}}{60\text{ s}} = 0.5\text{ m/s}^2
     \]
   - 题干中“质量 \(m\) 等于 1 个标准 Anthony”是典型的幽默干扰项（Red Herring），因为 \(m\) 在后续所有运动学量中完全约去！
2. **第 (a) 问：列车加速阶段的振子周期**：
   - 在加速列车的非惯性参考系中，质点除受弹簧恢复力 \(-kx\) 外，还受恒定的惯性力 \(F_{\text{in}} = -ma\)。运动方程为：
     \[
     m\ddot{x} = -kx - ma = -k\left(x + \frac{a}{\omega^2}\right)
     \]
   - 恒定惯性力仅将简谐振动的平衡位置平移至 \(x_{\text{eq}} = -\frac{a}{\omega^2}\)，并不改变势阱曲率（有效劲度系数仍为 \(k\)）。因此加速阶段的振动周期保持不变：
     \[
     T_{\text{acc}} = T = 1\text{ s}
     \]
3. **第 (b) 问：列车加速阶段的振动振幅**：
   - 在 \(t = 0\) 列车启动瞬间，质点静止于 \(x(0) = 0\)，\(\dot{x}(0) = 0\)。
   - 相对于加速系的新平衡位置 \(x_{\text{eq}} = -\frac{a}{\omega^2}\)，质点的初始偏移量即为振幅 \(A_{\text{acc}}\)（运动方程解为 \(x(t) = -\frac{a}{\omega^2}(1 - \cos\omega t)\)）：
     \[
     A_{\text{acc}} = \left|x(0) - x_{\text{eq}}\right| = \frac{a}{\omega^2} = \frac{a T^2}{4\pi^2} = \frac{0.5 \times 1^2}{4\pi^2} = \frac{1}{8\pi^2}\text{ m} \approx 1.27 \times 10^{-2}\text{ m} = 1.27\text{ cm}
     \]
4. **第 (c) 问：列车达到巡航速度后的振动振幅**：
   - 注意加速持续时间 \(\Delta t = 60\text{ s} = 60 T\) 恰好是振子周期 \(T = 1\text{ s}\) 的**整数倍**！
   - 在 \(t = \Delta t = 60\text{ s}\) 列车停止加速的时刻，相位 \(\omega \Delta t = 120\pi\)，此时质点在车厢系中的位置与速度分别为：
     \[
     x(\Delta t) = -\frac{a}{\omega^2}(1 - \cos 120\pi) = 0, \quad \dot{x}(\Delta t) = -\frac{a}{\omega}\sin 120\pi = 0
     \]
   - 当 \(t > 60\text{ s}\) 进入匀速巡航后，惯性力消失，平衡位置回到 \(x = 0\)。由于在 \(t = 60\text{ s}\) 瞬间质点恰好处于新平衡位置 \(x = 0\) 且相对车厢速度为零，此后质点将静止在势阱底部，故巡航阶段的振动振幅为：
     \[
     A_{\text{cruise}} = 0
     \]
   - （一般地，若加速时间为任意 \(\Delta t\)，则巡航振幅为 \(A_{\text{cruise}} = \sqrt{x(\Delta t)^2 + [\dot{x}(\Delta t)/\omega]^2} = \frac{2a}{\omega^2}\left|\sin\frac{\omega \Delta t}{2}\right|\)）。
5. **第 (d) 问：巡航振幅对末速度与加速过程的依赖关系讨论**：
   - 由通式 \(A_{\text{cruise}} = \frac{2a}{\omega^2}\left|\sin\left(\frac{\omega v_f}{2a}\right)\right|\) 可知，最终振幅**不仅取决于末速度 \(v_f\)，还强烈依赖于加速度 \(a\)（即加速过程）**！
   - **物理合理性解释**：
     - 若加速极其缓慢（绝热极限 \(a \to 0\)），质点始终紧贴平衡位置移动，最终振幅趋于 0；
     - 若瞬间加速（冲量极限 \(a \to \infty, \Delta t \to 0\) 且 \(a\Delta t = v_f\)），弹簧来不及形变，车厢瞬间获得速度 \(v_f\)，此时 \(A_{\text{cruise}} \to \frac{v_f}{\omega}\) 仅由 \(v_f\) 决定；
     - 若加速时间恰为周期的整数倍（\(\Delta t = nT\)），启动时惯性力切入激起的振荡与停止加速时惯性力撤去激起的振荡恰好反相相消（相干相消），使振子完全归零。

### 【第二阶段：多路径验证与教学拆解 (Verification & Breakdown)】
- **地面惯性系验证**：
  - 在地面系中，列车坐标 \(X_{\text{train}}(t) = \frac{1}{2}at^2\)（\(0 \le t \le \Delta t\)）。质点地面坐标 \(X(t) = X_{\text{train}}(t) + x(t) = \frac{1}{2}at^2 - \frac{a}{\omega^2}(1 - \cos\omega t)\)，地面速度 \(\dot{X}(t) = at - \frac{a}{\omega}\sin\omega t\)。在 \(t = \Delta t = 60T\) 时，\(X(\Delta t) = X_{\text{train}}(\Delta t)\) 且 \(\dot{X}(\Delta t) = a\Delta t = v_f\)，即质点在地面系中不仅与列车势阱中心重合，而且地面速度恰好等于列车巡航速度 \(v_f = 30\text{ m/s}\)！
- **核心难点与易错点**：
  - **难点**：洞察 \(\Delta t = 60\text{ s}\) 与 \(T = 1\text{ s}\) 的整周期通约性（Commensurability），识别出停止加速瞬间的相位刚好回到原点。
  - **易错点**：被题干中未知的“1 标准 Anthony”质量单位迷惑而卡壳，或者在 \(t = 60\text{ s}\) 撤去惯性力时误以为振幅仍保持 \(A_{\text{acc}} = \frac{a}{\omega^2}\)。

---

# Part II: PLANCKS 2023 International Finals (Milan)

## Problem 11 (2023 Final Q1): Quantum Mechanics (`plancks-2023-final-combined-slice-q1`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **模型与柱坐标分离变量**：
   - 质量为 \(m\) 的粒子限制在同轴圆柱壳空腔 \(a < r < A\)、\(0 < z < h\) 内，腔壁为无限高势垒（Dirichlet 边界条件 \(\psi = 0\)）。
   - 空腔内自由哈密顿量为 \(H = -\frac{\hbar^2}{2m}\nabla^2\)，采用分离变量 \(\Psi(r, \phi, z) = R(r)\Phi(\phi)Z(z)\)，总能量 \(E = E_{r\phi} + E_z\)。
   - 角向部分由周期性单值条件 \(\Phi(\phi + 2\pi) = \Phi(\phi)\) 得 \(\Phi_l(\phi) = \frac{1}{\sqrt{2\pi}}e^{il\phi}\)（\(l \in \mathbb{Z}\)）。
2. **第 (i) 与 (ii) 问：无磁场时的本征能级方程**：
   - **轴向部分 \(Z(z)\)**：
     - **(i) \(h \gg A\)（两端无限延伸）**：轴向自由平动，\(Z_k(z) = e^{ik_z z}\)（\(k_z \in \mathbb{R}\) 连续），\(E_z = \frac{\hbar^2 k_z^2}{2m}\)。
     - **(ii) 上下两端加盖封闭（\(Z(0) = Z(h) = 0\)）**：一维无限深势阱，\(Z_{n_z}(z) = \sqrt{\frac{2}{h}}\sin\left(\frac{n_z \pi z}{h}\right)\)（\(n_z = 1, 2, 3, \dots\)），\(E_z = \frac{\hbar^2 \pi^2 n_z^2}{2m h^2}\)。
   - **径向部分 \(R(r)\)**：
     - 令 \(u = k_\perp r = \frac{\sqrt{2m E_{r\phi}}}{\hbar}r\)，径向方程化为 \(l\) 阶贝塞尔方程：
       \[
       u^2 R''(u) + u R'(u) + (u^2 - l^2)R(u) = 0
       \]
     - 由于内半径 \(a > 0\)，原点 \(r = 0\) 不在求解域内，第一类和第二类贝塞尔函数 \(J_l(u), Y_l(u)\) 均正则可用：\(R(r) = c_1 J_l(k_\perp r) + c_2 Y_l(k_\perp r)\)。
     - 由内外壁边界条件 \(R(a) = 0\) 和 \(R(A) = 0\) 有非零解的条件（系数行列式为零），得到决定横向波数 \(k_\perp = \frac{\sqrt{2m E_{r\phi}}}{\hbar}\) 的超越方程：
       \[
       J_l(k_\perp a) Y_l(k_\perp A) - J_l(k_\perp A) Y_l(k_\perp a) = 0 \quad \left(\text{即 } \frac{J_l(k_\perp a)}{J_l(k_\perp A)} = \frac{Y_l(k_\perp a)}{Y_l(k_\perp A)}\right)
       \]
3. **第 (iii) 问：内圆柱包含均匀磁场时的 Aharonov-Bohm 效应**：
   - 磁场仅存在于内圆柱 \(r < a\) 内（\(\vec{B} = B\hat{z}\)），空腔 \(a < r < A\) 内 \(\vec{B} = 0\)。
   - 但空腔并非单连通区域！由斯托克斯定理 \(\oint \vec{A}\cdot d\vec{l} = \Phi_B = \pi a^2 B\)，在对称规范（\(\vec{A} = A_\phi(r)\hat{\phi}\)）下：
     \[
     A_\phi(r) = \begin{cases} \dfrac{B r}{2}, & r < a \\[6pt] \dfrac{B a^2}{2r} = \dfrac{\Phi_B}{2\pi r}, & r \ge a \end{cases}
     \]
   - 在空腔 \(a < r < A\) 内做最小电磁耦合替换 \(\vec{p} \to -i\hbar\nabla - q\vec{A}\)（若用高斯制则为 \(-i\hbar\nabla - \frac{e}{c}\vec{A}\)）：
     \[
     H = -\frac{\hbar^2}{2m}\left[\frac{\partial^2}{\partial z^2} + \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\left(\frac{\partial}{\partial \phi} - i\frac{q B a^2}{2\hbar}\right)^2\right]
     \]
   - 波函数单值性依然要求 \(\Phi(\phi) = e^{il\phi}\)（\(l \in \mathbb{Z}\)），此时角向算符本征值由 \(l^2\) 变为有效分数阶数 \(\tilde{l}^2 = \left(l - \frac{q B a^2}{2\hbar}\right)^2\)（在高斯制下为 \(\tilde{l} = \left|l - \frac{e B a^2}{2\hbar c}\right|\)）。
   - 因此径向本征能级由分数阶贝塞尔函数 \(J_{\tilde{l}}, Y_{\tilde{l}}\) 的边界条件方程给出：
     \[
     J_{\tilde{l}}(k_\perp a) Y_{\tilde{l}}(k_\perp A) - J_{\tilde{l}}(k_\perp A) Y_{\tilde{l}}(k_\perp a) = 0, \quad \tilde{l} = \left|l - \frac{q\Phi_B}{2\pi\hbar}\right|
     \]

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们的盲做推导与官方解答完全一致。
  - **官方解答中的三处印刷笔误提醒**：
    1. 官方解答式 (10) 将轴向驻波误印为 \(\sin\frac{2\pi n_z x}{h}\)（既多写了因子 2，又把 \(z\) 写成了 \(x\)；不过式 (11) 的能量 \(\frac{\hbar^2 n_z^2 \pi^2}{2mh^2}\) 是正确的）；
    2. 官方解答式 (13) 将角动量算符误印为二阶导数 \(L = -i\hbar\frac{\partial^2}{\partial \phi^2}\)（正确为一阶导数 \(-i\hbar\frac{\partial}{\partial \phi}\)）；
    3. 官方解答在第 5 页求 \(A_\phi\) 连续性时将积分常数误写为 \(c' = \frac{B_z a^2}{2r}\)（\(c'\) 应为常数 \(\frac{B_z a^2}{2}\)，代入 \(A_\phi = \frac{c'}{r}\) 得 \(\frac{B_z a^2}{2r}\)）。
- **核心难点与易错点**：
  - **难点**：理解多连通区域中的阿哈罗诺夫-玻姆（Aharonov-Bohm）效应——尽管粒子活动的空腔内处处 \(\vec{B}=0\)，但规范势 \(\vec{A} = \frac{\Phi_B}{2\pi r}\hat{\phi}\) 不可通过单值规范变换消除，使贝塞尔函数阶数发生磁通量依赖的分数平移 \(\tilde{l} = |l - \Phi_B/\Phi_0|\)。
  - **易错点**：受实心圆柱波导习惯影响，误将发散于 \(r=0\) 的第二类贝塞尔函数 \(Y_l\) 舍去（在 \(a > 0\) 的同轴环腔中必须同时保留 \(J_l\) 和 \(Y_l\)）。

---

## Problem 12 (2023 Final Q2): Thermodynamics (`plancks-2023-final-combined-slice-q2`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：证明表面张力系数依赖于电荷 \(q\)**：
   - 半径为 \(r\) 的肥皂泡具有内外两个气-液界面，总表面积为 \(\Sigma = 2 \times 4\pi r^2 = 8\pi r^2\)。
   - 导电球面电容为 \(C = 4\pi\varepsilon_0 r = \varepsilon_0 \sqrt{2\pi\Sigma}\)。肥皂泡薄膜的自由能微分为：
     \[
     dF_b = -S_b\,dT + \gamma\,d\Sigma + \frac{q}{C}\,dq
     \]
   - 由麦克斯韦关系（或直接对薄膜总自由能 \(F_b(T, \Sigma, q) = F_0(T) + \gamma_0(T)\Sigma + \frac{q^2}{2C(\Sigma)}\) 求面积偏导 \(\gamma = \left(\frac{\partial F_b}{\partial \Sigma}\right)_{T, q}\)）：
     \[
     \left(\frac{\partial \gamma}{\partial q}\right)_{T, \Sigma} = \left(\frac{\partial (q/C)}{\partial \Sigma}\right)_{T, q} = -\frac{q}{C^2}\frac{dC}{d\Sigma} = -\frac{q}{16\pi^2\varepsilon_0 r^2}\cdot\frac{1}{16\pi r} = -\frac{q}{64\pi^2\varepsilon_0 r^3}
     \]
   - 对 \(q\) 积分得带电肥皂泡的有效表面张力系数：
     \[
     \gamma(T, r, q) = \gamma_0(T) - \frac{q^2}{128\pi^2\varepsilon_0 r^3}
     \]
     （注：若按单层等效面积 \(A = 4\pi r^2\) 定义总有效张力 \(\tilde{\gamma} = 2\gamma\)，则 \(\tilde{\gamma} = \tilde{\gamma}_0 - \frac{q^2}{64\pi^2\varepsilon_0 r^3}\)）。
2. **第 (ii) 问：带电肥皂泡的平衡条件与解的唯一性证明**：
   - 系统（内部理想气体 + 肥皂膜）处于恒温 \(T_0\)、恒外压 \(p_0\) 环境中，可用热力学势（吉布斯自由能/可用能）\(\tilde{G}_0(r) = F_{\text{gas}}(T_0, V) + F_b(T_0, \Sigma, q) + p_0 V\) 描述，其中 \(V = \frac{4}{3}\pi r^3\)。
   - 对 \(r\) 求导令 \(\left(\frac{\partial \tilde{G}_0}{\partial r}\right)_{T_0, q} = 0\)：
     \[
     \frac{\partial \tilde{G}_0}{\partial r} = 4\pi r^2 \left(p_0 - p_g + \frac{4\gamma_0}{r} - \frac{q^2}{32\pi^2\varepsilon_0 r^4}\right) = 0
     \]
   - 代入理想气体状态方程 \(p_g = \frac{n R T_0}{\frac{4}{3}\pi r^3}\)，得到平衡半径 \(r_e\) 满足的方程：
     \[
     p_0 r_e^3 + 4\gamma_0 r_e^2 - \frac{q^2}{32\pi^2\varepsilon_0 r_e} = \frac{3 n R T_0}{4\pi}
     \]
   - **唯一性证明**：考察左端函数 \(h(r_e) = p_0 r_e^3 + 4\gamma_0 r_e^2 - \frac{q^2}{32\pi^2\varepsilon_0 r_e}\)（\(r_e > 0\)）。
     求导得 \(h'(r_e) = 3p_0 r_e^2 + 8\gamma_0 r_e + \frac{q^2}{32\pi^2\varepsilon_0 r_e^2} > 0\) 对一切 \(r_e > 0\) 恒成立！
     故 \(h(r_e)\) 在 \((0, +\infty)\) 上严格单调递增，且 \(\lim_{r_e \to 0^+} h(r_e) = -\infty\)（当 \(q \neq 0\) 时；若 \(q=0\) 则 \(h(0)=0 < \frac{3nRT_0}{4\pi}\)），\(\lim_{r_e \to +\infty} h(r_e) = +\infty\)。由介值定理，必存在**唯一**的正实根 \(r_e > 0\)。
   - 此外，为维持球形肥皂泡膜不发生瑞利电裂变（即有效表面张力 \(\gamma(T_0, r_e, q) > 0\)），需满足 \(q^2 < 128\pi^2\varepsilon_0 \gamma_0 r_e^3\)。
3. **第 (iii) 问：平衡的稳定性分析**：
   - 计算热力学势 \(\tilde{G}_0(r)\) 在平衡点 \(r = r_e\) 处的二阶导数。利用 \(\frac{\partial \tilde{G}_0}{\partial r} = 4\pi r \left[h(r) - \frac{3nRT_0}{4\pi}\right]\) 且 \(h(r_e) = \frac{3nRT_0}{4\pi}\)：
     \[
     \left.\frac{\partial^2 \tilde{G}_0}{\partial r^2}\right|_{r = r_e} = 4\pi r_e h'(r_e) = 4\pi r_e \left(3p_0 r_e^2 + 8\gamma_0 r_e + \frac{q^2}{32\pi^2\varepsilon_0 r_e^2}\right) > 0
     \]
     （或者直接对 \(4\pi r^2(p_0 - p_g + \frac{4\gamma_0}{r} - \frac{q^2}{32\pi^2\varepsilon_0 r^4})\) 求导并代入平衡条件消去 \(-4\gamma_0/r_e^2\)）。
   - 因为二阶导数恒大于零，该平衡点对于球对称径向涨落总是**热力学稳定**的（只要满足球形存在条件 \(\gamma > 0\)）。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们的盲做结果与官方解答完全吻合。
  - **官方解答中的两处细节辨析**：
    1. 官方解答在第 (i) 问写麦克斯韦关系时多写了一个负号 \(\left.\frac{\partial \gamma}{\partial q}\right|_{\Sigma, T} = -\left.\frac{\partial (q/C)}{\partial \Sigma}\right|_{q, T}\)，但在下一步求导 \(\frac{\partial(1/C)}{\partial\Sigma} = -\frac{1}{C^2}\frac{dC}{d\Sigma}\) 时又漏掉了一个负号，负负得正得到了正确的 \(\gamma = \gamma_0 - \frac{q^2}{128\pi^2\varepsilon_0 r^3}\)。直接对 \(F_b = \gamma_0\Sigma + \frac{q^2}{2C(\Sigma)}\) 求 \(\frac{\partial F_b}{\partial \Sigma}\) 可以避免此类符号失误。
    2. 在第 (iii) 问中，官方解答写出 \(\left.\frac{\partial^2 \tilde{G}_0}{\partial r^2}\right|_{\text{eq}} = 4\pi r_e^2\left[-\frac{\partial p_g}{\partial V}\frac{dV}{dr} - \frac{4\gamma_0}{r_e^2} + \frac{q^2}{8\pi^2\varepsilon_0 r_e^5}\right]\)。表面上看中间有一项负的 \(-\frac{4\gamma_0}{r_e^2}\)，但只要将平衡方程 \(\frac{3p_g}{r_e} = \frac{3p_0}{r_e} + \frac{12\gamma_0}{r_e^2} - \frac{3q^2}{32\pi^2\varepsilon_0 r_e^5}\) 代入 \(-\frac{\partial p_g}{\partial V}\frac{dV}{dr} = \frac{3p_g}{r_e}\)，就会化为全正项 \(\frac{3p_0}{r_e} + \frac{8\gamma_0}{r_e^2} + \frac{q^2}{32\pi^2\varepsilon_0 r_e^5} > 0\)！这正是我们在盲做中采用的提取因子 \(4\pi r\) 法的威力。
- **核心难点与易错点**：
  - **难点**：构建包含表面自由能、静电能与外压功的热力学势 \(\tilde{G}_0\)，并区分“径向稳定性（\(\partial^2 \tilde{G}_0/\partial r^2 > 0\)）”与“瑞利非球形裂变稳定性（\(\gamma_{\text{eff}} > 0\)）”。
  - **易错点**：忘记肥皂泡有**内外两个表面**（\(\Sigma = 8\pi r^2\)，附加压强为 \(\frac{4\gamma_0}{r}\) 而非单液滴的 \(\frac{2\gamma_0}{r}\)）。

---

## Problem 13 (2023 Final Q3): Quantum Optics (`plancks-2023-final-combined-slice-q3`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：拉比振荡演化态 \(|\psi_t\rangle\) 与激发态概率 \(P_e(t)\)**：
   - 相互作用绘景哈密顿量为 \(H_{\text{int}} = \frac{\hbar\Delta\omega}{2}\sigma_3 - \frac{\hbar\Omega_0}{2}\sigma_1 = \frac{\hbar\Omega}{2}(\vec{n}\cdot\vec{\sigma})\)，其中广义拉比频率 \(\Omega = \sqrt{\Omega_0^2 + \Delta\omega^2}\)，单位矢量 \(\vec{n} = \left(-\frac{\Omega_0}{\Omega}, 0, \frac{\Delta\omega}{\Omega}\right)\)。
   - 利用泡利算符恒等式 \((\vec{n}\cdot\vec{\sigma})^2 = \mathbb{I}\)，时间演化算符为：
     \[
     U_{\text{int}}(t) = \exp\left(-\frac{i H_{\text{int}} t}{\hbar}\right) = \cos\left(\frac{\Omega t}{2}\right)\mathbb{I} - i\sin\left(\frac{\Omega t}{2}\right)(\vec{n}\cdot\vec{\sigma})
     \]
   - 作用于初态 \(|\psi_0\rangle = |g\rangle\)（注意 \(\sigma_3|g\rangle = -|g\rangle\)，\(\sigma_1|g\rangle = |e\rangle\)）：
     \[
     |\psi_t\rangle = \left[\cos\left(\frac{\Omega t}{2}\right) + i\frac{\Delta\omega}{\Omega}\sin\left(\frac{\Omega t}{2}\right)\right]|g\rangle + i\frac{\Omega_0}{\Omega}\sin\left(\frac{\Omega t}{2}\right)|e\rangle
     \]
   - 处于激发态 \(|e\rangle\) 的概率为：
     \[
     P_e(t) = |\langle e|\psi_t\rangle|^2 = \frac{\Omega_0^2}{\Omega_0^2 + \Delta\omega^2}\sin^2\left(\frac{\sqrt{\Omega_0^2 + \Delta\omega^2}\,t}{2}\right)
     \]
2. **第 (ii) 与 (iii) 问：共振与大失谐极限讨论**：
   - **(ii) 共振（\(\Delta\omega = 0\)）**：\(\Omega = \Omega_0\)，\(P_e(t) = \sin^2\left(\frac{\Omega_0 t}{2}\right) = \frac{1}{2}(1 - \cos\Omega_0 t)\)，原子在基态与激发态之间做振幅为 1 的完全周期性翻转（拉比振荡）。
   - **(iii) 大失谐（\(\Delta\omega \gg \Omega_0\)）**：\(\Omega \approx \Delta\omega\)，\(P_e(t) \approx \left(\frac{\Omega_0}{\Delta\omega}\right)^2 \sin^2\left(\frac{\Delta\omega\,t}{2}\right) \ll 1\)，激发概率被强烈压制趋于 0，原子几乎始终停留在基态 \(|g\rangle\)。
3. **第 (iv) 问：\(\pi\) 脉冲（\(t = \pi/\Omega_0\)）下的激发概率与第一极小值**：
   - 引入无量纲失谐 \(x = \Delta\omega/\Omega_0\)，则 \(\Omega t / 2 = \frac{\pi}{2}\sqrt{1 + x^2}\)，故：
     \[
     P_e(t = \pi/\Omega_0) = \frac{1}{1 + x^2}\sin^2\left(\frac{\pi}{2}\sqrt{1 + x^2}\right)
     \]
   - 当 \(x > 0\) 时，第一个零点（极小值 \(P_e = 0\)）出现在 \(\frac{\pi}{2}\sqrt{1 + x^2} = \pi\) 处，解得：
     \[
     \sqrt{1 + x^2} = 2 \implies x = \sqrt{3}
     \]
4. **第 (v) 问：双腔拉姆齐干涉条纹（Ramsey fringes）解析证明**：
   - 记单腔 \(\pi/2\) 脉冲（\(\tau = \frac{\pi}{2\Omega_0}\)）对应的演化角为 \(\theta = \frac{\Omega\tau}{2} = \frac{\pi}{4}\sqrt{1 + x^2}\)，自由演化区（\(T = \xi\tau\)，\(H_{\text{free}} = \frac{\hbar\Delta\omega}{2}\sigma_3\)）对应的相移角为 \(\phi = \frac{\Delta\omega T}{2} = \frac{\pi}{4}\xi x\)。
   - 在 \(\{|e\rangle, |g\rangle\}\) 基底下，单腔演化矩阵为 \(U(\tau) = \begin{pmatrix} C^* & B \\ B & C \end{pmatrix}\)，其中 \(C = \cos\theta + i\frac{x}{\sqrt{1+x^2}}\sin\theta\)，\(B = \frac{i}{\sqrt{1+x^2}}\sin\theta\)；自由演化矩阵为 \(U_{\text{free}}(T) = \begin{pmatrix} e^{-i\phi} & 0 \\ 0 & e^{i\phi} \end{pmatrix}\)。
   - 经“腔1 \(\to\) 自由区 \(\to\) 腔2”演化后，末态在 \(|e\rangle\) 上的投影振幅为：
     \[
     \langle e|\psi_{\text{out}}\rangle = \langle e|U(\tau) U_{\text{free}}(T) U(\tau)|g\rangle = C^* e^{-i\phi} B + B e^{i\phi} C = 2 B \,\text{Re}\left(e^{i\phi} C\right)
     \]
   - 直接展开实部：
     \[
     \text{Re}\left(e^{i\phi} C\right) = \cos\phi\cos\theta - \frac{x}{\sqrt{1+x^2}}\sin\phi\sin\theta
     \]
   - 取模平方 \(\tilde{P}_e(x; \xi) = 4|B|^2 \left[\text{Re}(e^{i\phi}C)\right]^2\)，立即证得：
     \[
     \tilde{P}_e(x; \xi) = \underbrace{\frac{4}{1+x^2}\sin^2\left(\frac{\pi}{4}\sqrt{1+x^2}\right)}_{g(x)} \underbrace{\left[\cos\left(\frac{\pi}{4}\xi x\right)\cos\left(\frac{\pi}{4}\sqrt{1+x^2}\right) - \frac{x}{\sqrt{1+x^2}}\sin\left(\frac{\pi}{4}\xi x\right)\sin\left(\frac{\pi}{4}\sqrt{1+x^2}\right)\right]^2}_{f_\xi(x)}
     \]
5. **第 (vi) 问：\(\xi \gg 1\) 时第一零点 \(x_m\) 的 \(1/\xi\) 标度律证明**：
   - 当 \(\xi \gg 1\) 时，\(f_\xi(x)\) 随 \(\xi x\) 快速振荡，最小正零点 \(x_m \ll 1\) 由 \(f_\xi(x_m) = 0\) 决定：
     \[
     \cot\left(\frac{\pi}{4}\xi x_m\right) = \frac{x_m}{\sqrt{1+x_m^2}}\tan\left(\frac{\pi}{4}\sqrt{1+x_m^2}\right)
     \]
   - 在 \(\xi \gg 1\)、\(x_m \ll 1\) 极限下，右端 \(\approx x_m \tan\frac{\pi}{4} = x_m \to 0\)，故左端余切函数的自变量必趋于 \(\frac{\pi}{2}\)：
     \[
     \frac{\pi}{4}\xi x_m \approx \frac{\pi}{2} \implies x_m \approx \frac{2}{\xi} \propto \frac{1}{\xi}
     \]
     （若保留一阶修正，\(\cot(\frac{\pi}{4}\xi x_m) \approx \frac{\pi}{2} - \frac{\pi}{4}\xi x_m \approx x_m \implies x_m \approx \frac{2}{\xi + 4/\pi} \sim \frac{2}{\xi}\)）。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们的盲做推导与官方参考解答完全一致！特别是在第 (v) 问中，利用矩阵元的共轭对称性 \(A = C^*\) 直接合并出 \(2B\,\text{Re}(e^{i\phi}C)\)，避免了繁琐的 \(2\times 2\) 矩阵三次连乘，考场效率极高。
- **核心难点与易错点**：
  - **难点**：算符指数函数 \(\exp\left(-i\frac{\Omega t}{2}\vec{n}\cdot\vec{\sigma}\right)\) 的 \(SU(2)\) 欧拉展开，以及在第 (vi) 问超越方程中识别出 \(\xi \gg 1\) 时的主领头阶平衡 \(\frac{\pi}{4}\xi x_m \to \frac{\pi}{2}\)。
  - **易错点**：作用 \(\sigma_3|g\rangle\) 时误取正号 \(+|g\rangle\)（按题目定义 \(\sigma_3 = |e\rangle\langle e| - |g\rangle\langle g|\)，故 \(\sigma_3|g\rangle = -|g\rangle\)），导致相移符号相反。

---

## Problem 14 (2023 Final Q4): Structure of Matter (`plancks-2023-final-combined-slice-q4`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：零温自由电子气 100% 自旋极化的最大数密度 \(n_{\max}\)**：
   - 在外磁场 \(B = 8.64\text{ T}\) 中，顺磁场与逆磁场自旋态之间的塞曼能级劈裂为 \(\Delta E_Z = 2\mu_B B\)，其中玻尔磁子 \(\mu_B = \frac{e\hbar}{2m_e}\)，故 \(\Delta E_Z = \frac{e\hbar B}{m_e} \approx 1.6025 \times 10^{-22}\text{ J} \approx 1.000\text{ meV}\)。
   - 要使所有 \(N\) 个电子在基态下 100% 沿磁场方向极化（全部填入低自旋能带），单自旋极化费米球的最高占据动能（费米能 \(E_F\)）不能超过逆自旋能带的底端能量 \(\Delta E_Z = 2\mu_B B\)：
     \[
     E_F = \frac{\hbar^2 k_F^2}{2m_e} = \frac{\hbar^2}{2m_e}(6\pi^2 n)^{2/3} \le 2\mu_B B = \frac{e\hbar B}{m_e}
     \]
   - 注意两边电子质量 \(m_e\) 恰好约去！解得最大数密度：
     \[
     n_{\max} = \frac{1}{6\pi^2}\left(\frac{2m_e \cdot 2\mu_B B}{\hbar^2}\right)^{3/2} = \frac{1}{6\pi^2}\left(\frac{2eB}{\hbar}\right)^{3/2} \approx 7.18 \times 10^{22}\text{ m}^{-3}
     \]
2. **第 (ii) 问：连续模型下纳米立方体（\(L = 41.1\text{ nm}\)）内的极化电子数**：
   - 立方体体积 \(V = L^3 = (41.1 \times 10^{-9}\text{ m})^3 \approx 6.943 \times 10^{-23}\text{ m}^3\)，故：
     \[
     N_{\max} = n_{\max} V \approx 7.183 \times 10^{22} \times 6.943 \times 10^{-23} \approx 4.99 \approx 5
     \]
3. **第 (iii) 问：周期性边界条件（PBC）下的实际最大全极化电子数 \(N_{\max}^{\text{PBC}}\)**：
   - 在 PBC 下，波矢量子化为 \(\vec{k} = \frac{2\pi}{L}(n_x, n_y, n_z)\)，其中 \(n_x, n_y, n_z \in \mathbb{Z}\)。
   - 动能为 \(E(n_x, n_y, n_z) = A(n_x^2 + n_y^2 + n_z^2)\)，其中基元能量 \(A = \frac{2\pi^2\hbar^2}{m_e L^2} \approx 1.427 \times 10^{-22}\text{ J} = 890.4\,\mu\text{eV}\)。
   - 逆自旋最低态位于 \((0,0,0)\)，能量比顺自旋基态高 \(2\mu_B B = 1000.2\,\mu\text{eV}\)。由于：
     \[
     A = 890.4\,\mu\text{eV} < 2\mu_B B = 1000.2\,\mu\text{eV} < 2A = 1780.8\,\mu\text{eV}
     \]
     顺自旋电子可填满 \(n_x^2+n_y^2+n_z^2 = 0\)（简并度 1）和 \(n_x^2+n_y^2+n_z^2 = 1\)（\((\pm 1, 0, 0)\) 及其置换，简并度 6）两个壳层，故：
     \[
     N_{\max}^{\text{PBC}} = 1 + 6 = 7
     \]
4. **第 (iv) 问：零边界条件（NBC，三维无限深势阱）下的最大全极化电子数 \(N_{\max}^{\text{NBC}}\)**：
   - 在 NBC 下，驻波波函数要求 \(n_x, n_y, n_z \in \{1, 2, 3, \dots\}\)，能量为 \(E(n_x, n_y, n_z) = A'(n_x^2 + n_y^2 + n_z^2)\)，其中 \(A' = \frac{\pi^2\hbar^2}{2m_e L^2} = \frac{A}{4} \approx 222.6\,\mu\text{eV}\)。
   - 注意此时逆自旋的最低轨道是 \((1, 1, 1)\)（动能 \(3A'\)），因此顺自旋态相对于 \((1,1,1)\) 的激发动能 \(\Delta E_{\text{kin}} = A'(n_x^2 + n_y^2 + n_z^2 - 3)\) 必须小于 \(2\mu_B B \approx 4.493 A'\)！
   - 考察前几个壳层：
     - \((1, 1, 1)\)：\(n^2 = 3\)，激发能 \(0\)，简并度 \(1\)；
     - \((2, 1, 1)\) 及其置换：\(n^2 = 6\)，激发能 \(3A' = 667.8\,\mu\text{eV} < 2\mu_B B\)，简并度 \(3\)；
     - \((2, 2, 1)\) 及其置换：\(n^2 = 9\)，激发能 \(6A' = 1335.6\,\mu\text{eV} > 2\mu_B B\)。
   - 因此只能填满前两个壳层：
     \[
     N_{\max}^{\text{NBC}} = 1 + 3 = 4
     \]
5. **第 (v) 问：交换相互作用 \(H_{\text{exch}}\) 偏爱铁磁态的证明与 \(J\) 的估算**：
   - 对固定总电子数 \(N = N_\uparrow + N_\downarrow\)：
     \[
     H_{\text{exch}} = -\frac{1}{2}J\sqrt{N_\uparrow^2 + N_\downarrow^2} = -\frac{1}{2}J\sqrt{(N_\uparrow + N_\downarrow)^2 - 2N_\uparrow N_\downarrow} = -\frac{1}{2}JN\sqrt{1 - \frac{2N_\uparrow N_\downarrow}{N^2}}
     \]
     当 \(J > 0\) 时，只要 \(N_\uparrow\) 和 \(N_\downarrow\) 均非零，就有 \(H_{\text{exch}} > -\frac{1}{2}JN = H_{\text{exch}}^{\text{ferro}}\)，故交换项总是降低自旋完全极化态的能量。
   - 估算 \(J\)：两个均匀涂抹在体积 \(V = L^3\) 内的电子电荷密度为 \(\rho = -e/V\)，静电能数量级为：
     \[
     J_0 \sim \frac{e^2}{4\pi\varepsilon_0 L} \approx 5.61 \times 10^{-21}\text{ J} \approx 35.0\text{ meV}
     \]
     （若如官方解答将相对坐标积分域近似为等体积球 \(R_s = \left(\frac{3}{4\pi}\right)^{1/3}L\)，则 \(J = \frac{e^2}{4\pi\varepsilon_0 V}\int_0^{R_s} \frac{4\pi r^2}{r}\,dr = 3^{2/3}\left(\frac{\pi}{2}\right)^{1/3}\frac{e^2}{4\pi\varepsilon_0 L} \approx 1.357 \times 10^{-20}\text{ J} \approx 84.7\text{ meV}\)）。
6. **第 (vi) 问：计入交换项后的最大极化电子数 \(N_{\max}^{\text{exch}}\)**：
   - 将 1 个电子从顺自旋费米面翻转到逆自旋底端（\(N - 1\) 与 \(1\)），交换能增量为（在 \(N \gg 1\) 下）：
     \[
     \Delta E_{\text{exch}} = -\frac{1}{2}J\sqrt{(N-1)^2 + 1^2} - \left(-\frac{1}{2}JN\right) = \frac{1}{2}J\left[1 - \frac{1}{2N} + \mathcal{O}(N^{-2})\right] \approx \frac{1}{2}J
     \]
   - 这一交换能惩罚直接叠加到塞曼劈裂 \(2\mu_B B\) 上，使维持全自旋极化的临界费米能提高为：
     \[
     E_F = \frac{\hbar^2}{2m_e}(6\pi^2 n)^{2/3} = 2\mu_B B + \frac{1}{2}J \implies n_{\max}^{\text{exch}} = \frac{\big[m_e(4\mu_B B + J)\big]^{3/2}}{6\pi^2\hbar^3}
     \]
   - 代入数值：若用官方球近似 \(J \approx 84.7\text{ meV}\)，得 \(n_{\max}^{\text{exch}} \approx 2.05 \times 10^{25}\text{ m}^{-3}\)，\(N_{\max}^{\text{exch}} = n_{\max}^{\text{exch}} L^3 \approx 1423\)（若用简单标度 \(J_0 = \frac{e^2}{4\pi\varepsilon_0 L} \approx 35.0\text{ meV}\) 则得 \(N_{\max}^{\text{exch}} \approx 397\)）。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们在第 (i)–(iv) 问的数值（\(7.18 \times 10^{22}\text{ m}^{-3}\)，\(4.99\)，\(7\)，\(4\)）与官方解答分毫不差！
  - 在第 (v)(vi) 问中，我们推导出了完全一致的 \(\Delta E_{\text{exch}} \approx \frac{1}{2}J\) 和 \(n_{\max}^{\text{exch}} = \frac{[(4\mu_B B + J)m_e]^{3/2}}{6\pi^2\hbar^3}\)。值得向学生重点展示的是官方解答在第 (v) 问估算六重积分 \(\frac{1}{V^2}\int_V d^3r_1\int_V d^3r_2 \frac{1}{|\vec{r}_1 - \vec{r}_2|}\) 时采用的技巧——它将质心坐标 \(\vec{R}\) 积分设为 \(V\)，并将相对坐标 \(\vec{r} = \vec{r}_1 - \vec{r}_2\) 的积分区域近似为半径 \(R_s = (3V/4\pi)^{1/3}\) 的球，从而算出几何系数 \(3^{2/3}(\pi/2)^{1/3} \approx 2.418\)（注：实际上立方体内两点距离倒数的精确六重积分霍夫曼常数为 \(1.8823/L\)，无论取 \(1/L\)、\(1.88/L\) 还是官方的 \(2.42/L\)，在物理竞赛中均属合理的量级估算）。
- **核心难点与易错点**：
  - **难点**：区分连续态密度（Weyl 渐近公式）与纳米有限尺寸量子点中离散壳层简并度（PBC 给出 7，NBC 给出 4）的显著差异。
  - **易错点**：在第 (iv) 问 NBC（无限深势阱）中忘记最低动能态不是 0 而是零点能 \(3A'\)（对应 \((1,1,1)\)），若误用 \(A'(n_x^2+n_y^2+n_z^2) \le 2\mu_B B \approx 4.49 A'\) 则会漏掉 \(n^2 = 6\) 壳层，误得 \(N_{\max}^{\text{NBC}} = 1\)！

---

## Problem 15 (2023 Final Q5): Classical Mechanics (`plancks-2023-final-combined-slice-q5`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：球腔内纯滚动小球的拉格朗日量与单自由度证明**：
   - 小球质心在半径为 \(R - r\) 的同心球面上运动，用球坐标极角 \(\theta\)（从最低点量起）和方位角 \(\phi\) 参数化，质心速度平方为：
     \[
     v^2 = (R - r)^2\left(\dot{\theta}^2 + \sin^2\theta\,\dot{\phi}^2\right)
     \]
   - 纯滚动无滑移条件要求小球角速度大小满足 \(\omega = \frac{v}{r}\)（假设绕连线轴无自旋分量 \(\omega_n = 0\)），转动动能为 \(\frac{1}{2}I^*\omega^2 = \frac{1}{2}\beta m r^2 \left(\frac{v}{r}\right)^2 = \frac{1}{2}\beta m v^2\)。
   - 重力势能取最低点为零：\(V(\theta) = mg(R - r)(1 - \cos\theta)\)。故拉格朗日量为：
     \[
     \mathcal{L}(\theta, \dot{\theta}, \phi, \dot{\phi}) = \frac{1}{2}(1 + \beta)m(R - r)^2\left(\dot{\theta}^2 + \sin^2\theta\,\dot{\phi}^2\right) - mg(R - r)(1 - \cos\theta)
     \]
   - 由于 \(\frac{\partial \mathcal{L}}{\partial \phi} = 0\)，\(\phi\) 为循环坐标，广义动量 \(p_\phi = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = (1 + \beta)m(R - r)^2\sin^2\theta\,\dot{\phi} = \text{const}\)。
   - 初始时刻小球位于最低点 \(\theta(0) = 0\)，故 \(p_\phi(0) = 0 \implies p_\phi(t) \equiv 0\)，从而在 \(\theta \neq 0\) 处恒有 \(\dot{\phi} = 0\)，运动严格限制在同一竖直平面内（仅 1 个自由度 \(\theta\)）！
2. **第 (ii)–(v) 问：质心速度、切向加速度、法向约束力与静摩擦力**：
   - **(ii) 质心速率 \(v(\theta)\)**：由机械能守恒 \(\frac{1}{2}(1+\beta)mv^2 + mg(R-r)(1-\cos\theta) = \frac{1}{2}(1+\beta)mv_0^2\)：
     \[
     v(\theta) = \sqrt{v_0^2 - \frac{2g(R - r)(1 - \cos\theta)}{1 + \beta}}
     \]
   - **(iii) 质心切向加速度 \(a_t(\theta)\)**：对 \(v^2(\theta)\) 关于时间求导（并除以 \(2v = 2(R-r)\dot{\theta}\)），或以接触点为瞬心列力矩方程 \(mgr\sin\theta = -(I^* + mr^2)\frac{a_t}{r}\)：
     \[
     a_t(\theta) = -\frac{g\sin\theta}{1 + \beta}
     \]
   - **(iv) 球面法向支持力 \(F_{\text{constr}}(\theta)\)**：由径向牛顿第二定律 \(F_{\text{constr}}(\theta) - mg\cos\theta = \frac{mv^2(\theta)}{R - r}\)：
     \[
     F_{\text{constr}}(\theta) = \frac{m v_0^2}{R - r} + \frac{mg}{1 + \beta}\big[(3 + \beta)\cos\theta - 2\big]
     \]
   - **(v) 静摩擦力 \(F_{\text{frict}}(\theta)\)**：由切向牛顿第二定律 \(F_{\text{frict}}(\theta) - mg\sin\theta = m a_t(\theta)\)（或绕质心力矩 \(F_{\text{frict}}r = -I^*\frac{a_t}{r}\)）：
     \[
     F_{\text{frict}}(\theta) = \frac{\beta}{1 + \beta}mg\sin\theta
     \]
3. **第 (vi) 问：球对称物体的最大转动惯量系数 \(\beta_{\max}\)**：
   - 对于外半径为 \(r\)、总质量为 \(m\) 且具有球对称质量分布的刚体，任意球壳对球心的转动惯量为 \(\frac{2}{3}dm\,r'^2 \le \frac{2}{3}dm\,r^2\)。当全部质量集中于最外层薄球壳（\(r' = r\)）时取最大值：
     \[
     \beta_{\max} = \frac{2}{3}
     \]
4. **第 (vii) 问：全程保持纯滚动（完成竖直整圆周运动且不打滑）的最小初速度 \(v_0^{\min}\)**：
   - 要使小球在整周运动（\(\theta \in [0, \pi]\)）中始终不脱离且不打滑，需处处满足 \(|F_{\text{frict}}(\theta)| \le \mu_s F_{\text{constr}}(\theta)\)（由于 \(|F_{\text{frict}}| \ge 0\)，此式自动保证 \(F_{\text{constr}} \ge 0\)）：
     \[
     \frac{\beta}{1 + \beta}mg\sin\theta \le \mu_s\left[\frac{m v_0^2}{R - r} + \frac{mg}{1 + \beta}\big((3 + \beta)\cos\theta - 2\big)\right], \quad \forall \theta \in [0, \pi]
     \]
   - 整理为：
     \[
     \frac{v_0^2}{g(R - r)} \ge \frac{1}{1 + \beta}\max_{\theta \in [0, \pi]}\left[2 - (3 + \beta)\cos\theta + \frac{\beta}{\mu_s}\sin\theta\right]
     \]
   - 利用辅助角公式（或柯西不等式），\(-(3+\beta)\cos\theta + \frac{\beta}{\mu_s}\sin\theta\) 在 \(\theta \in [0, \pi]\) 内的最大值在钝角 \(\tan\theta_0 = -\frac{\beta}{\mu_s(3+\beta)}\) 处取到，其最大值为 \(\sqrt{(3+\beta)^2 + (\beta/\mu_s)^2}\)！
   - 因此最小初速度的精确解析公式为：
     \[
     v_0^{\min} = \sqrt{\frac{g(R - r)}{1 + \beta}\left[2 + \sqrt{(3 + \beta)^2 + \left(\frac{\beta}{\mu_s}\right)^2}\right]}
     \]
   - 代入 \(\beta = \frac{2}{3}\)，\(r = 0.01\text{ m}\)，\(R = 0.5\text{ m}\)，\(\mu_s = 0.9\)，\(g = 9.81\text{ m/s}^2\)：
     \[
     v_0^{\min} = \sqrt{\frac{3}{5}\times 9.81 \times 0.49 \times \left[2 + \sqrt{\left(\frac{11}{3}\right)^2 + \left(\frac{2}{2.7}\right)^2}\right]} \approx 4.07\text{ m/s}
     \]

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们的全部 7 个小问结果与官方参考解答完全一致（\(v_0^{\min} = 4.07\text{ m/s}\)）。
  - 在第 (vii) 问求极值时，官方解答通过求导 \(\tan\theta_0 = -\frac{2}{11\mu_s} = -0.202\) 先算出数值角 \(\theta_0 = 2.942\text{ rad}\) 再代回 \(f(\theta_0) = 10.10\)；而我们在盲做中直接利用三角辅助角恒等式 \(\max(A\sin\theta - B\cos\theta) = \sqrt{A^2 + B^2}\) 写出了解析闭式解 \(\sqrt{\frac{g(R-r)}{1+\beta}\left[2 + \sqrt{(3+\beta)^2 + (\beta/\mu_s)^2}\right]}\)，既直观揭示了无滑移临界条件对 \(\mu_s\) 的解析依赖，又省去了反三角函数数值查表。
- **核心难点与易错点**：
  - **难点**：在第 (vii) 问中认识到最容易发生打滑的位置**不在最高点 \(\theta = \pi\)**（最高点处 \(\sin\pi = 0\)，所需静摩擦力为零！），而是在接近最高点前的 \(\theta_0 \approx 168.6^\circ\) 处！
  - **易错点**：误把最高点不脱离条件 \(F_{\text{constr}}(\pi) = 0 \implies v_0 = \sqrt{\frac{5+\beta}{1+\beta}g(R-r)} \approx 4.04\text{ m/s}\) 当作纯滚动的充要条件，忽略了在到达最高点之前会因正压力减小而先突破最大静摩擦力发生打滑。

---

## Problem 16 (2023 Final Q6): Electromagnetism (`plancks-2023-final-combined-slice-q6`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **电路参数与边界电势设定**：
   - 同轴电缆内导体（区域 1：\(0 < r < a, 0 < z < h\)）电阻为 \(R\)，外导体圆筒（\(r = b\)）为理想导体且接地（\(\phi = 0\)）。
   - 结合题图 4a（顶部 \(z = h\) 标注 \(+V\) 为电池，底部 \(z = 0\) 为绿色负载电阻 \(R_L\)；注：若将 \(z=0\) 视为电池、\(z=h\) 视为负载，仅相当于做镜面反演 \(z \leftrightarrow h - z\)）：
     - 回路稳恒总电流 \(I = \frac{V}{R + R_L}\)。
     - 引入分压比 \(\alpha = \frac{R}{R + R_L}\)，\(\beta = \frac{R_L}{R + R_L}\)（\(\alpha + \beta = 1\)）。
     - 在 \(z = h\)（电池端），内导体电势为 \(\phi(r \le a, h) = V\)；在 \(z = 0\)（负载端），内导体电势为 \(\phi(r \le a, 0) = I R_L = \beta V\)。
2. **第 (i) 问：四个区域的电场分布与分界面电荷面密度**：
   - **区域 1（内导体，\(0 < r < a, 0 < z < h\)）**：电流沿 \(-z\) 方向均匀流动，电势沿 \(z\) 线性分布：
     \[
     \phi_1(r, z) = V\left(\beta + \alpha\frac{z}{h}\right) \implies \vec{E}_1 = -\nabla\phi_1 = -\frac{\alpha V}{h}\hat{e}_z
     \]
   - **区域 2（\(z = 0, a < r < b\)，薄圆盘负载电阻 \(R_L\)）**：径向表面电流满足拉普拉斯方程，边界条件为 \(\phi_2(a) = \beta V, \phi_2(b) = 0\)：
     \[
     \phi_2(r) = \beta V \frac{\ln(r/b)}{\ln(a/b)} \implies \vec{E}_2 = -\frac{\beta V}{\ln(a/b)}\frac{1}{r}\hat{e}_r = \frac{\beta V}{\ln(b/a)}\frac{1}{r}\hat{e}_r
     \]
   - **区域 3（\(z = h, a < r < b\)，薄圆盘电池）**：电势由题干直接给出：
     \[
     \phi_3(r) = V\frac{\ln(r/b)}{\ln(a/b)} \implies \vec{E}_3 = -\frac{V}{\ln(a/b)}\frac{1}{r}\hat{e}_r = \frac{V}{\ln(b/a)}\frac{1}{r}\hat{e}_r
     \]
   - **区域 4（\(a < r < b, 0 < z < h\)，同轴真空区）**：用分离变量法（分离常数为 0）求解 \(\nabla^2\phi_4 = 0\)，通解为 \(\phi_4(r, z) = (A + B\ln r)(C + Dz)\)。匹配 \(r=b\)（\(\phi_4=0\)）、\(r=a\)（\(\phi_4 = \phi_1\)）、\(z=0\)（\(\phi_4 = \phi_2\)）与 \(z=h\)（\(\phi_4 = \phi_3\)）四个边界条件，唯一确定：
     \[
     \phi_4(r, z) = V\left(\beta + \alpha\frac{z}{h}\right)\frac{\ln(r/b)}{\ln(a/b)}
     \]
     对其求负梯度得区域 4 的二维电场：
     \[
     \vec{E}_4 = -\frac{V}{\ln(a/b)}\left(\beta + \alpha\frac{z}{h}\right)\frac{1}{r}\hat{e}_r - \frac{\alpha V}{h\ln(a/b)}\ln\left(\frac{r}{b}\right)\hat{e}_z
     \]
   - **界面自由电荷面密度**（由高斯定理 \(\sigma = \varepsilon_0 \Delta E_n\)）：
     - 内外壁界面 \(r = a\)（1–4 界面）：\(\sigma_1(z) = \varepsilon_0 E_{4,r}(a, z) = \frac{\varepsilon_0 V}{a\ln(b/a)}\left(\beta + \alpha\frac{z}{h}\right) > 0\)；
     - 外导体内壁 \(r = b\)：\(\sigma_4(z) = -\varepsilon_0 E_{4,r}(b, z) = -\frac{\varepsilon_0 V}{b\ln(b/a)}\left(\beta + \alpha\frac{z}{h}\right) < 0\)；
     - 电池端面 \(z = h\)（4–3 界面）：\(\sigma_3(r) = \varepsilon_0 E_{4,z}(r, h) = -\frac{\varepsilon_0 \alpha V}{h\ln(b/a)}\ln\left(\frac{b}{r}\right)\)；
     - 负载端面 \(z = 0\)（4–2 界面）：\(\sigma_2(r) = -\varepsilon_0 E_{4,z}(r, 0) = +\frac{\varepsilon_0 \alpha V}{h\ln(b/a)}\ln\left(\frac{b}{r}\right)\)。
3. **第 (ii) 问：坡印廷矢量（Poynting Vector）与能流平衡分析**：
   - 由安培环路定理（内导体电流沿 \(-z\) 方向）：
     \[
     \vec{B}_1 = -\frac{\mu_0 I r}{2\pi a^2}\hat{e}_\phi \quad (0 < r < a), \qquad \vec{B}_4 = -\frac{\mu_0 I}{2\pi r}\hat{e}_\phi \quad (a < r < b)
     \]
   - 真空区域 4 的坡印廷矢量 \(\vec{S}_4 = \frac{1}{\mu_0}\vec{E}_4 \times \vec{B}_4\)：
     \[
     \vec{S}_4 = \frac{V I}{2\pi}\left[-\frac{\ln(r/b)}{\ln(a/b)}\frac{\alpha}{h r}\hat{e}_r + \left(\beta + \alpha\frac{z}{h}\right)\frac{1}{r^2\ln(a/b)}\hat{e}_z\right]
     \]
     （注意 \(\ln(a/b) < 0\)，故 \(S_{4,z} < 0\) 沿 \(-z\) 从顶部电池流向底部负载，且 \(S_{4,r} < 0\) 沿 \(-r\) 径向流入中心内导体！）。
   - **能流积分验证**：
     - 穿过顶部电池表面 \(z = h\) 流入区域 4 的总功率：\(\Phi_{\text{battery}} = \int_a^b \vec{S}_4(r, h)\cdot(-\hat{e}_z)2\pi r\,dr = V I\)（电池输出总功率）；
     - 穿过内导体表面 \(r = a\) 径向流入内导体的总功率：\(\Phi_{\text{inner}} = \int_0^h \vec{S}_4(a, z)\cdot(-\hat{e}_r)2\pi a\,dz = \alpha V I = I^2 R\)（内导体焦耳热耗散）；
     - 穿过底部负载表面 \(z = 0\) 流入负载电阻的总功率：\(\Phi_{\text{load}} = \int_a^b \vec{S}_4(r, 0)\cdot(-\hat{e}_z)2\pi r\,dr = \beta V I = I^2 R_L\)（负载焦耳热耗散）。
     三者严格满足 \(\Phi_{\text{battery}} = \Phi_{\text{inner}} + \Phi_{\text{load}}\)！
4. **第 (iii) 问：\(R = 0\) 时的电磁场动量与“隐藏动量（Hidden Momentum）”**：
   - 电磁动量密度 \(\vec{g} = \varepsilon_0 \vec{E} \times \vec{B} = \frac{1}{c^2}\vec{S}\)。对整个同轴腔体积分：
     \[
     \vec{p}_{\text{EM}} = \int_0^h dz \int_a^b 2\pi r\,dr\,\vec{g} = -\frac{V I h}{c^2}\left(\beta + \frac{\alpha}{2}\right)\hat{e}_z
     \]
     当 \(R = 0\)（\(\alpha = 0, \beta = 1\)）时：
     \[
     \vec{p}_{\text{EM}} = -\frac{V I h}{c^2}\hat{e}_z
     \]
   - **物理解释（质心能量定理与相对论隐藏动量）**：尽管宏观导线与外壳完全静止，电磁场却携带非零动量 \(-\frac{VIh}{c^2}\hat{e}_z\)。根据相对论质心定理，能量以功率 \(P = VI\) 从 \(z = h\)（电池）持续输送至 \(z = 0\)（负载），等价于质量以速率 \(\dot{m} = VI/c^2\) 沿 \(-z\) 转移；同时，内导体中处于高电势 \(+V\) 的运动载流子具有更大的相对论有效质量，产生与 \(\vec{p}_{\text{EM}}\) 大小相等、方向相反的相对论机械“隐藏动量” \(\vec{p}_{\text{mech}} = +\frac{VIh}{c^2}\hat{e}_z\)，使系统总动量保持为零。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们的盲做推导与官方解答完全一致。需注意题干文字中将 region 2 写为 \(z=0\)、region 3 写为 \(z=h\)，而官方解答遵循图 4a 将顶部 \(z=h\)（region 3）作为电池、底部 \(z=0\)（region 2）作为负载电阻；若将 \(z=0\) 作为电池、\(z=h\) 作为负载，只需令 \(\beta + \alpha\frac{z}{h} \to 1 - \alpha\frac{z}{h}\)，所有物理结论完全等价。
- **核心难点与易错点**：
  - **难点**：理解非理想导线周围的真空电场必须同时具有径向分量 \(E_r\)（维持电压传输）和轴向分量 \(E_z\)（匹配欧姆导线内部的纵向电场，使坡印廷矢量向导线内部偏折以供给焦耳热）。
  - **易错点**：误以为同轴电缆真空区的电场永远是纯径向的（只有在理想超导情况 \(R = 0 \implies \alpha = 0\) 时 \(E_z\) 才为零）。

---

## Problem 17 (2023 Final Q7): Medical Physics (`plancks-2023-final-combined-slice-q7`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：康普顿散射反冲电子动能 \(E_K(h\nu, \theta)\)**：
   - 设入射光子能量为 \(E_\gamma = h\nu\)，散射角为 \(\theta\)，散射光子能量为 \(h\nu'\)。
   - 由四维动量守恒 \((p_\gamma + p_e - p_{\gamma'})^2 = m_e^2 c^2\) 导出康普顿波长偏移公式：
     \[
     h\nu' = \frac{h\nu}{1 + \alpha(1 - \cos\theta)}, \quad \alpha \equiv \frac{h\nu}{m_e c^2}
     \]
   - 反冲电子动能为：
     \[
     E_K = h\nu - h\nu' = h\nu\,\frac{\alpha(1 - \cos\theta)}{1 + \alpha(1 - \cos\theta)}
     \]
2. **第 (ii) 问：证明大角度散射（\(\theta > \pi/2\)）光子能量上限为 \(511\text{ keV}\)**：
   - 对任意给定的 \(\theta \ge \frac{\pi}{2}\)，\(1 - \cos\theta \ge 1\)。当入射光子能量趋于无穷大（\(\alpha = \frac{h\nu}{m_e c^2} \to \infty\)）时：
     \[
     h\nu' = \frac{m_e c^2}{\frac{1}{\alpha} + (1 - \cos\theta)} < \frac{m_e c^2}{1 - \cos\theta} \le m_e c^2 = 511\text{ keV}
     \]
     （特别地，当 \(\theta = \pi/2\) 时渐近上限为 \(511\text{ keV}\)；当背散射 \(\theta = \pi\) 时渐近上限为 \(\frac{1}{2}m_e c^2 = 255.5\text{ keV}\)）。
3. **第 (iii) 问：质能吸收系数与质量衰减系数之比 \(\frac{\mu_{\text{en}}/\rho}{\mu/\rho}\)**：
   - 总截面 \(\sigma_{\text{tot}} = \sum_j \sigma_j\)，平均能量转移分数 \(f_{\text{tr}} = \frac{\mu_{\text{tr}}/\rho}{\mu/\rho} = \frac{\sum_j f_j \sigma_j}{\sum_j \sigma_j}\)。
   - 扣除次级带电粒子通过轫致辐射等辐射过程损失的份额 \(g\)，得：
     \[
     \frac{\mu_{\text{en}}/\rho}{\mu/\rho} = (1 - g)\frac{\sum_j f_j \sigma_j}{\sum_j \sigma_j}
     \]
4. **第 (iv) 与 (v) 问：铅（高 \(Z\)）中比值曲线在 \(100\text{ keV}\) 极小值与 \(>10\text{ MeV}\) 下降的物理解释**：
   - **(iv) \(100\text{ keV}\) 处的深谷（K 吸收边荧光逃逸）**：铅的 K 壳层电离能约为 \(88\text{ keV}\)。当光子能量刚超过 \(88\text{ keV}\)（约 \(90\text{–}100\text{ keV}\)）时，光电效应截面发生 K 吸收边突跃，但入射光子的大部分能量被用于克服 K 层结合能并随后以高能 K 特征 X 射线荧光的形式逃逸，真正转化为光电子动能的份额 \(f_{\text{pe}} = 1 - \frac{E_K}{h\nu}\) 跌至极小值！
   - **(v) \(>10\text{ MeV}\) 处的下降（轫致辐射损失 \(g\) 增大）**：在高 \(Z\) 材料（铅）中，当光子能量超过 \(10\text{ MeV}\) 时，由正负电子对产生和康普顿散射产生的次级高能电子/正电子在原子核库仑场中发生强烈的**轫致辐射（Bremsstrahlung）**，使辐射损失分数 \(g\) 随能量迅速增大（因辐射阻止本领 \(\propto E \cdot Z^2\)），导致 \((1 - g)\) 显著下降。
5. **第 (vi) 问：重带电粒子在物质中的能量损失（Bethe-Bloch 公式）与 Bragg 峰成因**：
   - 阻止本领遵循 Bethe-Bloch 公式：\(-\frac{dE}{dx} \propto \frac{z^2}{\beta^2} \rho \frac{Z}{A}\left[\ln\left(\frac{2m_e c^2 \beta^2 \gamma^2}{I}\right) - \beta^2 - \dots\right]\)，主要依赖于入射粒子电荷数 \(z\)、速度 \(\beta = v/c\)（近似按 \(1/\beta^2\) 反比增长）以及靶材料电子密度 \(\rho Z/A\)（与入射粒子质量 \(m\) 无关）。
   - **为何形成峰（Bragg peak）**：粒子刚射入时速度大，\(-dE/dx \propto 1/v^2\) 较小；随着深入组织减速，\(v \to 0\) 使 \(-dE/dx\) 急剧上升并在停止前达到极大值，最后因俘获电子使有效电荷 \(z_{\text{eff}} \to 0\) 而骤降为零。
   - **为何具有非零宽度**：由于每次电离碰撞的能量转移是随机过程，存在**能量歧离（Energy straggling，玻尔/朗道涨落）**以及束流初始能散，导致不同粒子的射程呈高斯分布展宽。
6. **第 (vii) 与 (viii) 问：射程标度律（Range scaling laws）与质子/碳离子射程比**：
   - 射程定义：\(R = \int_0^{E_0} \frac{dE}{-dE/dx} = M \int_0^{\beta_0} \frac{f_1(\beta)\,d\beta}{z^2 \rho (Z/A) f_2(\beta)}\)。
   - **(a) 不同粒子以相同初速度 \(\beta_0\) 穿过同一介质**：\(R \propto \frac{M}{z^2}\)（正比于粒子质量、反比于电荷平方）。
   - **(b) 同一粒子（相同初速）穿过不同介质**：近似有 \(\rho R \approx \text{const}\)（或 \(R \propto \frac{A}{\rho Z}\)）。
   - **(viii) 同速度质子（\(M_p = 1\text{ u}, z_p = 1\)）与 \(^{12}\text{C}\) 离子（\(M_{\text{C}} = 12\text{ u}, z_{\text{C}} = 6\)）的射程比**：
     \[
     \frac{R_p}{R_{^{12}\text{C}}} = \frac{M_p / z_p^2}{M_{^{12}\text{C}} / z_{^{12}\text{C}}^2} = \frac{1 / 1^2}{12 / 6^2} = \frac{36}{12} = 3
     \]
7. **第 (ix) 与 (x) 问：多重库仑散射（MCS）均方根偏转角 \(\theta_0\) 与质子/碳离子偏转比**：
   - **(ix) Highland 公式**：在小厚度 \(\Delta x \ll X_0\) 下，平面投影均方根散射角为：
     \[
     \theta_0 = \frac{13.6\text{ MeV}}{\beta c p} z \sqrt{\frac{\Delta x}{X_0}}\left[1 + 0.038\ln\left(\frac{\Delta x}{X_0}\right)\right] \propto \frac{z}{\beta c p}\sqrt{\frac{\Delta x}{X_0}}
     \]
     其中 \(X_0\) 为介质的辐射长度。
   - **(x) \(150\text{ MeV}\) 质子与 \(285\text{ MeV/u}\) 碳离子穿过 \(1\text{ m}\) 空气后的 \(\theta_0\) 之比**：
     - 对质子（\(z_p = 1, m_p \approx 938.3\text{ MeV}/c^2, E_{k,p} = 150\text{ MeV}\)）：
       相对论精确值 \((\beta c p)_p = \frac{E_{k,p}(E_{k,p} + 2m_p c^2)}{E_{k,p} + m_p c^2} \approx 279.3\text{ MeV}\)（非相对论近似为 \(2E_{k,p} = 300\text{ MeV}\)）。
     - 对 \(^{12}\text{C}\) 离子（\(z_{\text{C}} = 6\)，单核子动能 \(285\text{ MeV/u}\)，总动能 \(E_{k,\text{C}} = 12 \times 285 = 3420\text{ MeV}\)，静止能量 \(M_{\text{C}}c^2 \approx 12 \times 931.5 = 11178\text{ MeV}\)）：
       相对论精确值 \((\beta c p)_{\text{C}} = \frac{E_{k,\text{C}}(E_{k,\text{C}} + 2M_{\text{C}}c^2)}{E_{k,\text{C}} + M_{\text{C}}c^2} \approx 6038.8\text{ MeV}\)（非相对论近似为 \(2E_{k,\text{C}} = 6840\text{ MeV}\)）。
     - 因此两者的均方根散射角之比为：
       \[
       \frac{\theta_{0,p}}{\theta_{0,^{12}\text{C}}} = \frac{z_p}{z_{\text{C}}}\frac{(\beta c p)_{\text{C}}}{(\beta c p)_p} \approx \frac{1}{6} \times \frac{6038.8}{279.3} \approx 3.60 \quad \left(\text{非相对论近似为 } \frac{1}{6}\times\frac{12\times 285}{150} = 3.80\right)
       \]

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比及官方解答末尾计算失误纠正**：
  - 我们在前 9 问的公式、物理机制解释及第 (viii) 问的数值（\(R_p / R_{\text{C}} = 3\)）与官方解答完全一致。
  - **官方解答第 (x) 问式 (72) 的双重笔误提醒**：官方解答在式 (72) 中写出了 \(\frac{\theta_{0p}}{\theta_{0\,^{12}\text{C}}} = \left(\frac{z_p}{(\beta cp)_p}\right)\left(\frac{(\beta cp)_{^{12}\text{C}}}{z_{^{12}\text{C}}}\right) \sim \left(\frac{z_p}{(\beta cp)_p}\right)\left(\frac{2(\beta cp)_p}{6z_p}\right) = 3\)。这里官方作者犯了两个明显的疏忽：
    1. 忽略了 \(285\text{ MeV/u}\) 的单位是“每核子兆电子伏（\(\text{MeV/u}\)）”，\(^{12}\text{C}\) 共有 12 个核子，总动能是 \(12 \times 285 = 3420\text{ MeV}\)，因此 \((\beta cp)_{^{12}\text{C}}\) 是 \((\beta cp)_p\) 的 \(21.6\) 倍（若按非相对论是 \(22.8\) 倍），而非 \(285/150 \approx 2\) 倍！
    2. 退一步说，即便按官方自己写的 \(\frac{2}{6}\) 约分，结果也是 \(\frac{1}{3}\) 而非 \(3\)！
    正确的比值应为 \(3.60\)（相对论）或 \(3.80\)（非相对论），这也体现了碳离子重离子治癌相比质子束具有更小的横向散射展宽（\(\theta_{0,\text{C}} \approx \theta_{0,p}/3.6\)）的物理优势！
- **核心难点与易错点**：
  - **难点**：理解高 \(Z\) 材料中 K 吸收边荧光逃逸对 \(f_{\text{tr}}\) 的压低机制，以及从 Bethe-Bloch 公式积分导出同速不同粒子射程标度律 \(R \propto M/z^2\)。
  - **易错点**：混淆重离子物理中的“比能量（\(\text{MeV/u}\)，决定速度 \(\beta\)）”与“总能量（\(\text{MeV}\)，决定总动量 \(p\)）”。

---

## Problem 18 (2023 Final Q8): Astrophysics of Protoplanetary Discs (`plancks-2023-final-combined-slice-q8`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：竖直等温流体静力平衡下的密度分布 \(\rho(z)\)**：
   - 在柱坐标系 \((r, \phi, z)\) 中，到中心恒星（质量 \(M_*\)）的球半径为 \(R = \sqrt{r^2 + z^2}\)。
   - 恒星引力在竖直 \(z\) 方向的分量为 \(f_{g,z} = -\frac{G M_*}{R^2}\sin\theta = -\frac{G M_* z}{(r^2 + z^2)^{3/2}}\)。
   - 竖直方向流体静力平衡方程为 \(\frac{1}{\rho}\frac{\partial P}{\partial z} = f_{g,z}\)。代入竖直等温状态方程 \(P = c_s^2(r)\rho\)（\(c_s\) 与 \(z\) 无关）：
     \[
     \frac{1}{\rho}\frac{\partial \rho}{\partial z} = -\frac{G M_* z}{c_s^2(r^2 + z^2)^{3/2}}
     \]
   - 从中平面 \(z = 0\)（密度 \(\rho_0(r)\)，此时 \(R = r\)）积分至高度 \(z\)：
     \[
     \ln\left(\frac{\rho(r, z)}{\rho_0(r)}\right) = \frac{G M_*}{c_s^2}\left(\frac{1}{\sqrt{r^2 + z^2}} - \frac{1}{r}\right) \implies \rho(r, z) = \rho_0(r)\exp\left[\frac{G M_*}{c_s^2}\left(\frac{1}{R} - \frac{1}{r}\right)\right]
     \]
2. **第 (ii) 问：几何薄盘近似（\(H \ll r\)）与面密度 \(\Sigma\) 的关系**：
   - 当 \(|z| \ll r\) 时，将 \(\frac{1}{R} = \frac{1}{r}\left(1 + \frac{z^2}{r^2}\right)^{-1/2}\) 泰勒展开至二阶：
     \[
     \frac{1}{R} - \frac{1}{r} \approx -\frac{z^2}{2r^3}
     \]
   - 代入密度分布，得到高斯型竖直分布：
     \[
     \rho(r, z) \approx \rho_0(r)\exp\left(-\frac{G M_* z^2}{2 c_s^2 r^3}\right) = \rho_0(r)\exp\left(-\frac{z^2}{2 H^2}\right)
     \]
     其中盘的标高（Scale height）为 \(H(r) = \frac{c_s}{\Omega_K}\)，开普勒角速度为 \(\Omega_K = \sqrt{\frac{G M_*}{r^3}}\)。
   - 对 \(z \in (-\infty, +\infty)\) 高斯积分求得面密度 \(\Sigma(r)\)：
     \[
     \Sigma(r) = \int_{-\infty}^{+\infty} \rho_0(r) e^{-z^2/(2H^2)}\,dz = \sqrt{2\pi}\,\rho_0(r) H(r)
     \]
3. **第 (iii) 问：中平面（\(z = 0\)）的旋转曲线 \(v_\phi(r)\)**：
   - 在 \(z = 0\) 处，径向欧拉方程为 \(-\frac{v_\phi^2}{r} = -\frac{G M_*}{r^2} - \frac{1}{\rho_0}\frac{dP_0}{dr}\)，即：
     \[
     \frac{v_\phi^2}{r} = \frac{G M_*}{r^2} + \frac{1}{\rho_0}\frac{d(\rho_0 c_s^2)}{dr} = \frac{v_K^2}{r} + \frac{c_s^2}{r}\frac{d\ln(\rho_0 c_s^2)}{d\ln r}
     \]
     其中 \(v_K = \sqrt{\frac{G M_*}{r}} = \Omega_K r\) 为开普勒线速度。
   - 代入幂律分布 \(\rho_0(r) \propto r^{-p}\) 和 \(c_s(r) \propto r^{-q}\)（故 \(\rho_0 c_s^2 \propto r^{-(p + 2q)}\)）：
     \[
     \frac{d\ln(\rho_0 c_s^2)}{d\ln r} = -(p + 2q) \implies v_\phi(r) = v_K(r)\sqrt{1 - (p + 2q)\frac{c_s^2}{v_K^2}}
     \]
4. **第 (iv) 问：偏离开普勒旋转的相对量级与薄盘条件**：
   - 注意到 \(\frac{c_s}{v_K} = \frac{c_s}{\Omega_K r} = \frac{H}{r}\)，故：
     \[
     v_\phi(r) = v_K\sqrt{1 - (p + 2q)\left(\frac{H}{r}\right)^2} \approx v_K\left[1 - \frac{1}{2}(p + 2q)\left(\frac{H}{r}\right)^2\right]
     \]
   - 相对偏差 \(\frac{|v_\phi - v_K|}{v_K} \approx \frac{1}{2}(p + 2q)\left(\frac{H}{r}\right)^2 = \mathcal{O}\left(\frac{H^2}{r^2}\right)\)，在薄盘 \(H \ll r\) 下确实是二阶小量（亚开普勒旋转，这正是导致行星胚胎向内漂移的“逆风”机制！）。
5. **第 (v) 问：非中平面（\(z \neq 0, |z| \ll r\)）的三维旋转曲线 \(v_\phi(r, z)\) 与垂直切变**：
   - 在高度 \(z\) 处，径向引力分量为 \(-f_{g,r} = \frac{G M_* r}{(r^2 + z^2)^{3/2}} \approx \frac{v_K^2}{r}\left(1 - \frac{3z^2}{2r^2}\right)\)。
   - 径向压强梯度项（固定 \(z\) 对 \(r\) 求偏导）：
     \[
     \frac{1}{\rho}\frac{\partial P}{\partial r} = \frac{c_s^2}{r}\left[\frac{\partial \ln(\rho_0 c_s^2)}{\partial \ln r} + \frac{\partial}{\partial \ln r}\left(-\frac{z^2}{2H^2}\right)\right] = \frac{c_s^2}{r}\left[-(p + 2q) + \frac{z^2}{H^2}\frac{d\ln H}{d\ln r}\right]
     \]
   - 由于 \(H = c_s r^{3/2} (GM_*)^{-1/2} \propto r^{\frac{3}{2} - q}\)，故 \(\frac{d\ln H}{d\ln r} = \frac{3}{2} - q\)。代回径向平衡方程：
     \[
     v_\phi^2(r, z) = v_K^2\left[1 - \frac{3z^2}{2r^2} - (p + 2q)\frac{H^2}{r^2} + \left(\frac{3}{2} - q\right)\frac{z^2}{r^2}\right] = v_K^2\left[1 - \left(\frac{H}{r}\right)^2\left(p + 2q + q\frac{z^2}{H^2}\right)\right]
     \]
   - 注意 \(-\frac{3z^2}{2r^2}\) 与 \(+\frac{3z^2}{2r^2}\) **精确相消**！最终得到：
     \[
     v_\phi(r, z) = v_K\sqrt{1 - \left(\frac{H}{r}\right)^2\left(p + 2q + q\frac{z^2}{H^2}\right)}
     \]
   - 当 \(q > 0\)（温度向盘外递减）时，附加项 \(-q\frac{z^2}{r^2} < 0\)，因此高纬度（\(|z| > 0\)）处的气体比中平面气体**旋转得更慢（slower）**！

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们的盲做推导与官方参考解答在所有 5 问中完全一致！
  - 特别值得在教学中强调第 (v) 问的对消机制：利用对数导数 \(\frac{d\ln H}{d\ln r} = \frac{3}{2} - q\)，一行代数就能看清为什么引力减弱项 \(-\frac{3z^2}{2r^2}\) 会与标高张开项 \(+\frac{3z^2}{2r^2}\) 严格抵消——因为当 \(q = 0\)（全局等温）时，气体为正压流体（Barotropic fluid，\(P = P(\rho)\)），根据流体力学**泰勒-普劳德曼定理（Taylor-Proudman theorem / Poincaré-Wavre theorem）**，正压轴对称旋转流体的角速度 \(\Omega(r)\) 必然与高度 \(z\) 无关！只有当存在径向温度梯度（\(q \neq 0\)，斜压流体 Baroclinic fluid）时，才会出现随高度变化的“热成风（Thermal wind）”切变 \(-q\frac{z^2}{r^2}\)！
- **核心难点与易错点**：
  - **难点**：在第 (v) 问求 \(\frac{\partial \rho(r, z)}{\partial r}\) 时，记住标高 \(H(r) = \frac{c_s(r)}{\Omega_K(r)} \propto r^{3/2 - q}\) 本身是半径 \(r\) 的函数，不可将其视为常数。
  - **易错点**：在展開径向引力 \(f_{g,r} = -\frac{G M_* r}{(r^2 + z^2)^{3/2}}\) 时误写为 \(-\frac{G M_*}{r^2 + z^2}\)（漏乘了方向余弦 \(\cos\theta = \frac{r}{\sqrt{r^2 + z^2}}\)，导致展开系数变成 \(-1\) 而非正确的 \(-3/2\)，从而破坏了正压抵消！甚至官方解答式 (87) 文字中也写成了 \(\frac{GM_*}{R^2}\)，但右端展开式却写对了 \(1 - \frac{3}{2}\frac{z^2}{r^2}\)）。

---

## Problem 19 (2023 Final Q9): Particle Physics (`plancks-2023-final-combined-slice-q9`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (i) 问：磁星宇宙线在 1783 年与 2023 年（当前）的到达能谱及 Pierre Auger 观测事件数**：
   - 磁星 SWIFT J1818.0-1607 距离地球 \(d = 4.4\text{ kpc} = 4.4 \times 10^3 \times 3.086 \times 10^{16}\text{ m} \approx 1.358 \times 10^{20}\text{ m}\)，估算年龄为 \(240\) 年（即其诞生时发出的光子在 \(2023 - 240 = 1783\) 年到达地球！）。
   - **1783 年在地球观测到的能谱**：
     - 质子（P）和铁核（I）带电，在银河系磁场中走圆弧轨迹，路程长于直线距离 \(d\)，因此在 1783 年（与光子同时）尚未到达；
     - 唯有不带电的**中子（N）**沿直线传播（对 \(E > 10^{17}\text{ eV}\)，洛伦兹因子 \(\gamma_n > 10^8\)，速度延迟 \(\frac{d}{2c\gamma_n^2} < 10^{-4}\text{ s}\) 可完全忽略）。但中子具有有限寿命 \(\tau_n \approx 881.5\text{ s}\)（静止质量 \(m_n c^2 \approx 0.94\text{ GeV}\)），存活到达地球的概率为 \(\exp\left(-\frac{d}{\gamma_n c \tau_n}\right) = \exp\left(-\frac{m_n c d}{E \tau_n}\right)\)。因此 1783 年地球处观测到的能谱纯由中子贡献：
       \[
       \Phi_{1783}(E) = \frac{N_{0N}}{4\pi d^2}\left(\frac{E}{E_0}\right)^{-2.5} \exp\left(-\frac{m_n c d}{E \tau_n}\right) \quad (E_0 < E < E_C)
       \]
   - **现在（2023 年，滞后 \(\Delta t = 240\text{ yr} \approx 7.57 \times 10^9\text{ s}\)）Pierre Auger 天文台观测到的能量与事件数**：
     - 电荷为 \(Ze\) 的粒子在垂直于银盘的均匀磁场 \(B = 1\,\mu\text{G} = 10^{-10}\text{ T}\) 中做拉莫尔半径为 \(R_L = \frac{E}{Z e c B}\) 的圆周运动。
     - 连接源与地球的弦长为 \(d\)，圆弧长为 \(s = 2 R_L \arcsin\left(\frac{d}{2 R_L}\right)\)。利用题干提示 \(\arcsin x \approx x + \frac{x^3}{6}\)：
       \[
       \Delta s = s - d \approx 2 R_L \cdot \frac{1}{6}\left(\frac{d}{2 R_L}\right)^3 = \frac{d^3}{24 R_L^2} = c\Delta t
       \]
     - 解出此时刻恰好到达地球的粒子的拉莫尔半径：
       \[
       R_L = \sqrt{\frac{d^3}{24 c \Delta t}} \approx \sqrt{\frac{(1.358 \times 10^{20})^3}{24 \times 3 \times 10^8 \times 7.57 \times 10^9}} \approx 2.14 \times 10^{20}\text{ m} \approx 6.94\text{ kpc}
       \]
     - 对应的粒子能量 \(E = Z e c B R_L\)（单能脉冲！）：
       - **质子（\(Z = 1\)）**：\(E_P \approx 6.42 \times 10^{18}\text{ eV}\)；
       - **铁核（\(Z = 26\)）**：\(E_I = 26 E_P \approx 1.67 \times 10^{20}\text{ eV}\)（恰好低于硬截断 \(E_C = 2 \times 10^{20}\text{ eV}\)！）。
     - 在面积 \(A_{\text{Auger}} = 3000\text{ km}^2 = 3 \times 10^9\text{ m}^2\) 上接收到的事件数：
       \[
       N_P^{\text{Auger}} = \frac{A_{\text{Auger}}}{4\pi d^2} N_{0P}\left(\frac{E_P}{E_0}\right)^{-2.5} \approx 1.295 \times 10^{-32} \times 10^{40} \times (64.25)^{-2.5} \approx 3.8 \times 10^3 \text{ 个}
       \]
       \[
       N_I^{\text{Auger}} = \frac{A_{\text{Auger}}}{4\pi d^2} N_{0I}\left(\frac{E_I}{E_0}\right)^{-2.2} \approx 1.295 \times 10^{-32} \times 10^{39} \times (1670)^{-2.2} \approx 1 \text{ 个}
       \]
2. **第 (ii) 问：\(h = 10\text{ km}\) 高空 \(1\text{ TeV}\) \(K^+\) 介子的主要衰变道、次级粒子能量与存活分析**：
   - \(K^+\)（\(m_K \approx 493.7\text{ MeV}\)，\(E_K = 1\text{ TeV} \implies \gamma_K = \frac{E_K}{m_K} \approx 2025, \beta_K \approx 1\)）最主要的两个衰变道为：
     1. **轻子道 \(K^+ \to \mu^+ + \nu_\mu\)**（分支比约 \(63.5\%\)，由于手征螺旋度压低，不衰变为 \(e^+\nu_e\)）：
        - 在 \(K^+\) 静止系中，\(p^* = E_\nu^* = \frac{m_K^2 - m_\mu^2}{2m_K} \approx 235.5\text{ MeV}\)，\(E_\mu^* = \frac{m_K^2 + m_\mu^2}{2m_K} \approx 258.2\text{ MeV}\)。
        - 洛伦兹变换至地球系 \(E = \gamma_K(E^* + \beta_K p^* \cos\theta^*)\)（\(\cos\theta^* \in [-1, 1]\)）：
          - \(\nu_\mu\)：\(E_\nu \in [0, \, 2\gamma_K E_\nu^*] \approx [0, \, 954\text{ GeV}]\)（中微子稳定，直接到达地面）；
          - \(\mu^+\)：\(E_\mu \in [\gamma_K(E_\mu^* - p^*), \, \gamma_K(E_\mu^* + p^*)] \approx [46\text{ GeV}, \, 1000\text{ GeV}]\)。因 \(\mu^+\) 寿命 \(\tau_\mu = 2.2\,\mu\text{s}\)，即使取最低能量 \(46\text{ GeV}\)（\(\gamma_\mu \approx 436\)），衰变长度 \(\gamma_\mu c \tau_\mu \approx 288\text{ km} \gg 10\text{ km}\)，存活概率 \(\exp(-h/\gamma_\mu c\tau_\mu) \ge 96.6\%\)，**绝大多数 \(\mu^+\) 到达地面**（若极少数衰变，则 \(\mu^+ \to e^+ + \nu_e + \bar{\nu}_\mu\)）。
     2. **强子道 \(K^+ \to \pi^+ + \pi^0\)**（分支比约 \(20.7\%\)）：
        - 在静止系中（\(m_{\pi^+} \approx 139.6\text{ MeV}, m_{\pi^0} \approx 135.0\text{ MeV}\)），\(E_{\pi}^* \approx \frac{m_K}{2} \approx 247\text{ MeV}\)，\(p^* \approx 205\text{ MeV}\)。
        - 地球系能量范围：\(E_{\pi^0} \in [82\text{ GeV}, \, 913\text{ GeV}]\)，\(E_{\pi^+} \in [85\text{ GeV}, \, 918\text{ GeV}]\)。
        - \(\pi^0\) 通过电磁相互作用极快衰变（\(\tau_{\pi^0} = 8.5 \times 10^{-17}\text{ s}\)，\(\gamma c \tau_{\pi^0} < 0.2\text{ mm}\)），**100% 立即衰变为 \(\pi^0 \to \gamma + \gamma\)**；
        - \(\pi^+\) 通过弱相互作用衰变（\(\tau_{\pi^+} = 2.6 \times 10^{-8}\text{ s}\)），衰变长度 \(\gamma c \tau_{\pi^+} \in [4.7\text{ km}, \, 51\text{ km}]\)，存活率在 \(11\%\text{–}81\%\) 之间，**高能部分可到达地面，低能部分在空中衰变为 \(\pi^+ \to \mu^+ + \nu_\mu\)**。
3. **第 (iii) 问：赤道面内从格林尼治上空 \(h = 1000\text{ m}\) 径向入射的 \(\mu\) 子击中内罗毕（\(37^\circ\text{E}\)）所需的动量与存活率**：
   - 建立以地心为原点的赤道面直角坐标系：\((x_0, y_0) = (R_E + h, 0)\) 为 \(\mu\) 子产生点（初速度沿 \(-x\) 方向径向向心），内罗毕坐标为 \((x_N, y_N) = (R_E\cos\theta, R_E\sin\theta)\)，其中 \(R_E = 6400\text{ km}, h = 1\text{ km}, \theta = 37^\circ\)。
   - 磁场沿 \(+z\)（指向北极），洛伦兹力使粒子在赤道面内做半径为 \(R\) 的圆周运动，圆心位于 \((x_0, R) = (R_E + h, R)\)。
   - 由圆方程 \((x_N - x_0)^2 + (y_N - R)^2 = R^2\) 解得曲率半径：
     \[
     R = \frac{y_N^2 + (R_E + h - x_N)^2}{2 y_N} \approx 2142\text{ km} = 2.142 \times 10^6\text{ m}
     \]
   - 所需动量（\(B = 0.5\text{ G} = 5 \times 10^{-5}\text{ T}\)）：
     \[
     p = e B R \approx 0.3 \times B[\text{T}] \times R[\text{m}]\text{ GeV}/c \approx 32.1\text{ GeV}/c
     \]
   - 飞行的圆弧长度 \(L_{\text{eff}} = 2 R \arctan\left(\frac{y_N}{R_E + h - x_N}\right) \approx 4.185 \times 10^6\text{ m}\)。
   - 对 \(p = 32.1\text{ GeV}/c\) 的 \(\mu\) 子（\(m_\mu \approx 105.7\text{ MeV}/c^2 \implies \gamma_\mu \approx 304\)），衰变长度 \(\gamma_\mu c \tau_\mu \approx 304 \times 3 \times 10^8 \times 2.0 \times 10^{-6} \approx 1.82 \times 10^5\text{ m}\)（若取 \(\tau_\mu = 2.2\,\mu\text{s}\) 则为 \(2.01 \times 10^5\text{ m}\)），到达内罗毕的存活概率为：
     \[
     P = \exp\left(-\frac{L_{\text{eff}}}{\gamma_\mu c \tau_\mu}\right) \approx 10^{-10} \text{（几乎为 0；注：官方解答漏乘了 } 10^3 \text{ 写成 } 0.2\% \text{，详见下方对比）}
     \]

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们在第 (i)、(ii)、(iii) 问的几何模型、能量与动量数值（\(E_P = 6.42 \times 10^{18}\text{ eV}\)，\(E_I = 1.67 \times 10^{20}\text{ eV}\)，\(N_P^{\text{Auger}} \approx 3780\)，\(N_I^{\text{Auger}} = 1\)，\(p_\mu = 32.1\text{ GeV}/c\)）与官方解答完全一致！
  - **官方解答第 (iii) 问的两处明显瑕疵提醒**：
    1. *穿地几何悖论*：从 \((R_E + 1\text{ km}, 0)\) 沿 \(-x\) 方向出发、经过内罗毕 \((R_E\cos 37^\circ, R_E\sin 37^\circ)\) 的圆弧全部位于地球内部 \(r < R_E\)（地壳岩石中）！显然出题人在构造这道趣味几何题时把地球内部当成了透明真空。
    2. *存活率指数算错数量级*：弧长 \(L_{\text{eff}} \approx 4.18 \times 10^6\text{ m}\)，而 \(32.1\text{ GeV}\) \(\mu\) 子的衰减长度 \(\gamma c \tau_\mu = \frac{32100}{105.7} \times 3\times 10^8 \times 2.2\times 10^{-6} \approx 2.00 \times 10^5\text{ m}\)，因此 \(\frac{L_{\text{eff}}}{\gamma c \tau_\mu} \approx 20.9\)，真实存活率是 \(e^{-20.9} \approx 8 \times 10^{-10}\)（若用题干给的 \(\tau_\mu = 2\times 10^{-6}\text{ s}\) 则为 \(e^{-23.0} \approx 10^{-10}\)）；官方解答写出的 \(0.2\% \approx e^{-6.2}\) 是误把弧长算小了约 3.4 倍所致。
- **核心难点与易错点**：
  - **难点**：在第 (i) 问中理解“磁星年龄 240 年”是指天文学家在地球上观测到的光学年龄（即诞生光子在 1783 年到达地球，而今天 2023 年观测到的带电宇宙线相对于光子的磁场偏转路程差恰好为 \(\Delta s = c \times 240\text{ yr}\)）！
  - **易错点**：在计算圆弧弦长差 \(\Delta s = 2R_L\arcsin\left(\frac{d}{2R_L}\right) - d\) 时漏掉括号内的因子 \(1/2\)，导致 \(\Delta s\) 算成 \(\frac{d^3}{3R_L^2}\) 而非正确的 \(\frac{d^3}{24R_L^2}\)。

---

## Problem 20 (2023 Final Q10): General Relativity (`plancks-2023-final-combined-slice-q10`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **度规签名约定**：采用 \((- , + , + , +)\) 签名，\(\eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)\)，引力波微扰 \(g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}\)（\(|h_{\mu\nu}| \ll 1\)）。
2. **第 (i) 问：证明 \(s^\mu = n^\mu - \frac{1}{2}\eta^{\mu\rho}h_{\rho\lambda}n^\lambda\) 在微扰度规下为零矢量（Null vector）**：
   - 已知在闵氏背景中 \(\eta_{\mu\nu}n^\mu n^\nu = 0\)。保留至 \(\mathcal{O}(h)\) 阶：
     \[
     g_{\mu\nu} s^\mu s^\nu = (\eta_{\mu\nu} + h_{\mu\nu})\left(n^\mu - \frac{1}{2}\eta^{\mu\rho}h_{\rho\lambda}n^\lambda\right)\left(n^\nu - \frac{1}{2}\eta^{\nu\sigma}h_{\sigma\kappa}n^\kappa\right)
     \]
     \[
     = \eta_{\mu\nu}n^\mu n^\nu + h_{\mu\nu}n^\mu n^\nu - 2 \cdot \frac{1}{2}\underbrace{\eta_{\mu\nu}\eta^{\mu\rho}}_{\delta_\nu^\rho} h_{\rho\lambda}n^\lambda n^\nu + \mathcal{O}(h^2) = 0 + h_{\mu\nu}n^\mu n^\nu - h_{\nu\lambda}n^\lambda n^\nu = 0
     \]
3. **第 (ii) 与 (iii) 问：利用 TT 规范测地线方程计算引力波引起的光子频移 \(\frac{\nu(t) - \nu_0}{\nu_0}\)**：
   - 设光子由位于地球方向 \(\hat{n}\) 处的源发出（即光子沿 \(-\hat{n}\) 方向传向地球），背景四维波矢为 \(n^\mu = \nu_0(1, -\hat{n})\)，微扰后 \(s^0 = \nu\)。
   - 在横向无迹（TT）规范下，\(h_{0\mu} = 0\)，克里斯托费尔符号的 0 分量为：
     \[
     \Gamma^0_{\alpha\beta} = \frac{1}{2}\eta^{00}\left(\partial_\alpha h_{0\beta} + \partial_\beta h_{0\alpha} - \partial_0 h_{\alpha\beta}\right) = \frac{1}{2}\partial_t h_{\alpha\beta}
     \]
   - 测地线方程 \(\frac{ds^0}{d\lambda} + \Gamma^0_{\alpha\beta}s^\alpha s^\beta = 0\) 保留至 \(\mathcal{O}(h)\) 阶为：
     \[
     \frac{d\nu}{d\lambda} = -\frac{1}{2}\left(\frac{\partial h_{ij}}{\partial t}\right) \nu_0^2 \hat{n}^i \hat{n}^j
     \]
   - 对沿任意方向 \(\hat{\Omega}\) 传播的平面引力波 \(h_{ij} = h_{ij}(t - \hat{\Omega}\cdot\vec{x})\)，沿未微扰光子世界线 \(\frac{dt}{d\lambda} = \nu_0\)，\(\frac{d\vec{x}}{d\lambda} = -\nu_0\hat{n}\)，其全导数为：
     \[
     \frac{d}{d\lambda}h_{ij}(t - \hat{\Omega}\cdot\vec{x}) = \left(\frac{dt}{d\lambda} - \hat{\Omega}\cdot\frac{d\vec{x}}{d\lambda}\right)\frac{\partial h_{ij}}{\partial t} = \nu_0(1 + \hat{\Omega}\cdot\hat{n})\frac{\partial h_{ij}}{\partial t}
     \]
   - 将 \(\frac{\partial h_{ij}}{\partial t} = \frac{1}{\nu_0(1 + \hat{\Omega}\cdot\hat{n})}\frac{dh_{ij}}{d\lambda}\) 代入测地线方程：
     \[
     \frac{1}{\nu_0}\frac{d\nu}{d\lambda} = -\frac{\hat{n}^i \hat{n}^j}{2(1 + \hat{\Omega}\cdot\hat{n})}\frac{dh_{ij}}{d\lambda}
     \]
   - 从发射事件 \(p = (t_p, \vec{x}_p)\) 积分至地球接收事件 \(e = (t_e, \vec{x}_e)\)，得到著名的脉冲星计时阵列（PTA）红移公式：
     \[
     \frac{\nu(t) - \nu_0}{\nu_0} = \frac{\hat{n}^i \hat{n}^j}{2(1 + \hat{\Omega}\cdot\hat{n})}\Delta h_{ij}, \quad \Delta h_{ij} \equiv h_{ij}(t_p - \hat{\Omega}\cdot\vec{x}_p) - h_{ij}(t_e - \hat{\Omega}\cdot\vec{x}_e)
     \]
   - 特别地，当 \(\hat{\Omega} = \hat{z}\) 时，取 \(\hat{n} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)\) 且 \(h_{ij} = \begin{pmatrix} h_+ & h_\times & 0 \\ h_\times & -h_+ & 0 \\ 0 & 0 & 0 \end{pmatrix}\)：
     \[
     \frac{\nu(t) - \nu_0}{\nu_0} = \frac{\sin^2\theta}{2(1 + \cos\theta)}\big(\Delta h_+ \cos 2\phi + \Delta h_\times \sin 2\phi\big) = \frac{1}{2}(1 - \cos\theta)\big(\Delta h_+ \cos 2\phi + \Delta h_\times \sin 2\phi\big)
     \]
4. **第 (iv) 问：当 \(\hat{\Omega}\cdot\hat{n} = 1\) 时发生什么？**
   - 当 \(\hat{\Omega}\cdot\hat{n} = 1\)（即 \(\hat{\Omega} = \hat{z}\) 时 \(\theta = 0, \cos\theta = 1\)，源位于引力波传播的正前方，光子迎面穿过引力波）时，由于引力波的**横波性质**（\(h_{ij}\hat{\Omega}^j = 0\)），分子 \(\hat{n}^i\hat{n}^j\Delta h_{ij} \propto \sin^2\theta = (1 - \cos\theta)(1 + \cos\theta)\) 含有一阶零点，约去分母 \(1 + \cos\theta = 2\) 后严格等于 **0**（不产生任何频移）！
   - （注：若源与引力波同向传播 \(\hat{\Omega}\cdot\hat{n} = -1\)，即 \(\theta = \pi\)，虽然分母 \(1 + \cos\theta \to 0\)，但光子与引力波同速并行，相位差 \(\Delta h_{ij}\) 也正比于 \(1 + \cos\theta \to 0\)，频移同样有限）。
5. **第 (v) 问：多列不同方向引力波叠加的线性性**：
   - 在 \(\mathcal{O}(h)\) 线性微扰阶，克里斯托费尔符号与测地线方程关于 \(h_{\mu\nu}\) 完全是**线性的（可加的）**，因此 \(N\) 列引力波的总频移等于各列引力波单独产生频移的代数和。
6. **第 (vi) 问：修正色散关系 \(\omega(k) = c_s k\)（\(c_s \neq 1\)）下的频移表现**：
   - 此时平面引力波为 \(h_{ij}(t - \hat{\Omega}\cdot\vec{x}/c_s)\)，全导数关系变为 \(\frac{dh_{ij}}{d\lambda} = \nu_0\left(1 + \frac{\hat{\Omega}\cdot\hat{n}}{c_s}\right)\frac{\partial h_{ij}}{\partial t}\)，只需在前述所有公式中将 \(\hat{\Omega}\) 替换为 \(\frac{\hat{\Omega}}{c_s}\)：
     \[
     \frac{\nu(t) - \nu_0}{\nu_0} = \frac{\hat{n}^i \hat{n}^j}{2\left(1 + \frac{\hat{\Omega}\cdot\hat{n}}{c_s}\right)}\Delta h_{ij}
     \]
7. **第 (vii) 问：忽略引力波频率演化（Chirp）所需的最大源距离 \(D\) 估算**：
   - 要在光子从源飞往地球的传播时间 \(\Delta t = D/c\) 内忽略引力波自身的频率演化，需满足 \(\Delta t \ll \tau_{\text{chirp}} = \frac{f}{df/dt}\)，即 \(D \ll c \frac{f}{df/dt}\)。
   - **重要量纲辨析**：题干式 (90) 写为 \(\frac{df}{dt} \sim 300\left(\frac{Gm}{c^3}\right)f^{11/3}\)，漏印了四极辐射公式中无量纲化所需的指数 \(\frac{5}{3}\)！
     - **按正确的广义相对论旋进公式 \(\frac{df}{dt} \sim 300\left(\frac{Gm}{c^3}\right)^{5/3}f^{11/3}\) 计算**：
       对 \(m = 10^{11}M_\odot \approx 2 \times 10^{41}\text{ kg}\)，\(\frac{Gm}{c^3} \approx 4.93 \times 10^5\text{ s}\)，\(f = 1\text{ nHz} = 10^{-9}\text{ Hz}\)：
       \[
       \frac{df}{dt} \sim 300 \times (4.93 \times 10^5)^{5/3} \times (10^{-9})^{11/3} \approx 9.3 \times 10^{-19}\text{ Hz/s}
       \]
       特征演化时间 \(\tau_{\text{chirp}} = \frac{f}{df/dt} \approx 1.07 \times 10^9\text{ s} \approx 34\text{ yr}\)（若公式中 300 为 \(96/5 \cdot (2\pi)^{8/3} \approx 2560\) 的不同约定，则 \(\tau_{\text{chirp}} \sim 10^{10}\text{–}10^{11}\text{ s}\)，对应 \(D = c\tau_{\text{chirp}} \sim 10\text{ pc} \sim 1\text{ kpc}\) 量级）。
     - **若直接按题干式 (90) 字面公式计算**：\(\frac{df}{dt} \approx 1.48 \times 10^{-25}\text{ Hz/s}\)，则 \(D = \frac{cf}{df/dt} \approx 2.0 \times 10^{24}\text{ m} \approx 66\text{ Mpc}\)。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与官方参考解答对比**：
  - 我们在第 (i)–(vi) 问的推导与官方解答完全一致。
  - **官方解答中的两处细节辨析**：
    1. 官方解答在第 50 页推导 \(\frac{dh_{ij}}{d\lambda}\) 时笔误写成了 \(\nu\frac{\partial h_{ij}}{\partial t}(1 + \hat{\Omega}\cdot\vec{x})\)（把单位矢量 \(\hat{n}\) 误写成了位置 \(\vec{x}\)，下一行又改回了正确的 \(1 + \hat{\Omega}\cdot\hat{n}\)）；并且官方解答把光子传播方向定义为 \(\frac{d\vec{x}}{d\lambda} = -\nu\hat{n}\)，却在第 51 页把 \(\hat{n}\) 展开成了带负号的 \(-(\sin\theta\cos\phi\hat{x} + \sin\theta\sin\phi\hat{y} + \cos\theta\hat{z})\)。
    2. 在第 (vii) 问中，官方解答直接给出了 \(\Delta t = \frac{f}{df/dt} \sim 1.1\text{ kpc}/c \implies D \sim \mathcal{O}(\text{kpc})\)，这证实了原题式 (90) 确实漏印了指数 \(5/3\)（或把 \(\left(\frac{Gm}{c^3}\right)^{5/3}\) 误印成了 \(\left(\frac{Gm}{c^3}\right)^1\)）！我们在解析中同时给出了正确量纲公式与字面公式的数值，帮助竞赛生养成**先做量纲检验**的绝佳习惯。
- **核心难点与易错点**：
  - **难点**：在测地线方程积分中巧妙利用全导数代换 \(\frac{\partial h_{ij}}{\partial t} = \frac{1}{\nu_0(1 + \hat{\Omega}\cdot\hat{n})}\frac{dh_{ij}}{d\lambda}\)，将沿光子路径的积分直接化为首末两端的边界振幅差 \(\Delta h_{ij}\)（即脉冲星项 Pulsar term 与地球项 Earth term 之差）。
  - **易错点**：在第 (iv) 问中只看分母 \(1 + \cos\theta\) 而未注意分子中包含横向投影因子 \(\sin^2\theta = 1 - \cos^2\theta\)，漏看了 \(\cos\theta = 1\) 时分子为零。
