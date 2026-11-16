# Batch 17: PLANCKS 2019 Final & 2020 Final 物理竞赛深度精讲笔记

本分册涵盖 **PLANCKS 2019 Odense Final（第 1–10 题）** 与 **PLANCKS 2020 London Final（第 1–9 题）** 共 19 道决赛真题的严格两阶段解析（第一阶段：只读原题独立盲解；第二阶段：对照官方解答或跨路径交叉核验与竞赛教学拆解）。

---

## Part I: PLANCKS 2019 Final (Odense)

> **说明**：PLANCKS 2019 官方仅公开了原题卷 PDF，题库未收录官方解答卷。因此在第二阶段中，我们对每一问均采用**多视角独立推导（如巨正则系综配分函数法、生成算符法、角动量耦合代数法、拉格朗日-比奈方程多路径对消、量纲与极限情形核验）**进行严格自洽性校核。

---

### 1. Mono- and Multilayer Adsorption (`plancks-2019-final-problem-slice-q1`)

- **物理模型**：气固表面单层吸附（Langmuir 等温线）与多层吸附（BET 等温线）的动力学细致平衡与无穷级数求和模型
- **难度评级**：D2
- **教学标签**：`表面物理`、`Langmuir吸附`、`BET多层吸附`、`细致平衡原理`、`幂级数求和`

#### 第一阶段：只看原题的独立盲解

1. **(a) 单层吸附平衡覆盖度 \(\Theta\)**：
   在单层吸附模型中，表面仅存在空位点（数目 \(N_0\)）与单层占据位点（数目 \(N_1\)），总位点数 \(N_{\text{sites}} = N_0 + N_1\)，已吸附分子数 \(N_{\text{ad}} = N_1\)。
   达到热力学动态平衡时，吸附速率 \(r_a\) 与脱附速率 \(r_d\) 相等：
   \[
   r_a = r_d \implies k_a p N_0 = k_d N_1 \implies N_1 = \frac{k_a}{k_d} p N_0 = K p N_0.
   \]
   因此单层表面覆盖度为：
   \[
   \Theta = \frac{N_{\text{ad}}}{N_{\text{sites}}} = \frac{N_1}{N_0 + N_1} = \frac{K p N_0}{N_0(1 + Kp)} = \frac{Kp}{1 + Kp}.
   \]

2. **(b) 高低压极限与半覆盖特征压强 \(p_{1/2}\)**：
   - **低压极限（\(p \to 0\)，即 \(Kp \ll 1\)）**：\(\Theta \approx Kp\)，覆盖度与分压成正比（亨利定律区，表面空位充足）。
   - **高压极限（\(p \to \infty\)，即 \(Kp \gg 1\)）**：\(\Theta \to 1\)，所有表面位点均被单层铺满，达到单层饱和吸附。
   - **半覆盖压强 \(p_{1/2}\)**：令 \(\Theta(p_{1/2}) = \frac{1}{2}\)，得：
     \[
     \frac{K p_{1/2}}{1 + K p_{1/2}} = \frac{1}{2} \implies K p_{1/2} = 1 \implies p_{1/2} = \frac{1}{K} = \frac{k_d}{k_a}.
     \]

3. **(c) 多层吸附的递推关系与 \(N_i\) 表达式**：
   设 \(N_i\) 为恰好吸附了 \(i\) 层分子的表面位点数。在动态平衡下，利用各相邻层之间的**细致平衡（Detailed Balance）**：
   - 第 \(0\) 层与第 \(1\) 层之间（吸附质-基底表面相互作用，速率常数 \(k_a, k_d\)）：
     \[
     k_a p N_0 = k_d N_1 \implies N_1 = K p N_0 = c K' p N_0 = c z N_0,
     \]
     其中 \(c = K/K'\)，\(z = K' p\)。
   - 第 \(i-1\) 层与第 \(i\) 层之间（\(i \ge 2\)，吸附质-吸附质相互作用，速率常数 \(k'_a, k'_d\)，平衡常数 \(K' = k'_a/k'_d\)）：
     \[
     k'_a p N_{i-1} = k'_d N_i \implies N_i = K' p N_{i-1} = z N_{i-1}.
     \]
   由数学归纳法，对任意 \(i \ge 1\) 递推可得：
   \[
   N_i = z^{i-1} N_1 = z^{i-1}(c z N_0) = c z^i N_0 = c (K' p)^i N_0.
   \]

4. **(d) 多层吸附的 \(N_{\text{ad}}\)、\(N_{\text{sites}}\) 与覆盖度 \(\Theta\)**：
   为使无穷多层求和收敛，需满足 \(0 \le z = K'p < 1\)。
   - 总表面位点数 \(N_{\text{sites}}\)：
     \[
     N_{\text{sites}} = \sum_{i=0}^\infty N_i = N_0 + \sum_{i=1}^\infty c z^i N_0 = N_0 \left(1 + \frac{cz}{1 - z}\right) = N_0 \frac{1 + (c - 1)z}{1 - z}.
     \]
   - 吸附分子总数 \(N_{\text{ad}}\)：
     \[
     N_{\text{ad}} = \sum_{i=1}^\infty i N_i = c N_0 \sum_{i=1}^\infty i z^i = c N_0 z \frac{d}{dz}\left(\sum_{i=0}^\infty z^i\right) = c N_0 z \frac{d}{dz}\left(\frac{1}{1 - z}\right) = \frac{c z N_0}{(1 - z)^2}.
     \]
   - 多层吸附表观覆盖度 \(\Theta\)（即 BET 等温线方程）：
     \[
     \Theta = \frac{N_{\text{ad}}}{N_{\text{sites}}} = \frac{\frac{c z N_0}{(1 - z)^2}}{\frac{1 + (c - 1)z}{1 - z} N_0} = \frac{cz}{(1 - z)\bigl[1 + (c - 1)z\bigr]}.
     \]

5. **(e) \(K'\) 与 \(z\) 的物理意义**：
   当 \(z \to 1^-\)（即 \(p \to 1/K'\)）时，\(\Theta \to \infty\)，意味着吸附层厚度趋于无穷大，气相分子在表面发生宏观**体相液化（凝聚）**。由于在温度 \(T\) 下纯液体与其饱和蒸气处于相平衡（凝聚速率 \(k'_a p_0\) 等于蒸发速率 \(k'_d\)），故 \(p_0 = \frac{k'_d}{k'_a} = \frac{1}{K'}\) 正是该温度下吸附质纯液体的**饱和蒸气压**！
   - \(K' = \frac{1}{p_0}\)：体相液化/凝聚过程的平衡常数（饱和蒸气压的倒数）。
   - \(z = K' p = \frac{p}{p_0}\)：气体的**相对压强（Relative Pressure，或相对于饱和蒸气压的活度/饱和度）**。

#### 第二阶段：交叉核验与教学拆解

- **巨正则系综（统计力学）独立核验**：
  每个表面位点可视为一个独立的巨正则子系统，若吸附 \(i\) 个分子（\(i \ge 1\)），第 1 层结合能为 \(\varepsilon_1\)，后续各层凝聚能均为 \(\varepsilon_L\)（体相液化热），化学势为 \(\mu = k_B T \ln(p/p_{\text{ref}})\)。则单个位点的巨正则配分函数为：
  \[
  \Xi_1 = 1 + e^{\beta(\mu + \varepsilon_1)} \sum_{i=1}^\infty e^{(i-1)\beta(\mu + \varepsilon_L)} = 1 + \sum_{i=1}^\infty c z^i = \frac{1 + (c-1)z}{1 - z},
  \]
  其中 \(z = e^{\beta(\mu + \varepsilon_L)} = p/p_0\)，\(c = e^{\beta(\varepsilon_1 - \varepsilon_L)}\)。位点平均吸附分子数 \(\Theta = z \frac{\partial \ln \Xi_1}{\partial z} = \frac{cz}{(1-z)[1+(c-1)z]}\)，且当 \(c \to \infty\) 或截断至 \(i=1\) 时严格退化为 Langmuir 公式 \(\Theta = \frac{cz}{1+cz} = \frac{Kp}{1+Kp}\)，两套推导完美吻合。
- **核心难点与易错点**：
  1. **细致平衡 vs 总通量平衡**：在推导 (c) 时，若列出第 \(i\) 层的净变化率 \(\frac{dN_i}{dt} = (k'_a p N_{i-1} - k'_d N_i) - (k'_a p N_i - k'_d N_{i+1}) = 0\)，需要从 \(i=0\) 开始逐层递推消除括号项，等价于相邻两层直接满足细致平衡 \(k'_a p N_{i-1} = k'_d N_i\)。
  2. **\(N_{\text{sites}}\) 求和漏掉 \(N_0\)**：计算 \(N_{\text{sites}} = \sum_{i=0}^\infty N_i\) 时，务必注意 \(i=0\) 项是 \(N_0\)（不乘因子 \(c\)），而 \(i \ge 1\) 项才含有因子 \(c\)；若误写成 \(c N_0 \sum_{i=0}^\infty z^i\)，则当 \(c \ne 1\) 时结果错误。

---

### 2. Quantum Optics (`plancks-2019-final-problem-slice-q2`)

- **物理模型**：无损分束器（Beamsplitter）的幺正相位约束与双光子 Hong-Ou-Mandel (HOM) 量子干涉效应
- **难度评级**：D2
- **教学标签**：`量子光学`、`分束器幺正性`、`Hong-Ou-Mandel干涉`、`玻色子聚束`、`全同粒子统计`

#### 第一阶段：只看原题的独立盲解

1. **Exercise 1：经典无损分束器**
   - **(a) 单端口输入能量守恒**：
     令 \(E_2 = 0\)，则 \(E_3 = R E_1\)，\(E_4 = T E_1\)。代入能量守恒 \(|E_1|^2 + |E_2|^2 = |E_3|^2 + |E_4|^2\)：
     \[
     |E_1|^2 = |R E_1|^2 + |T E_1|^2 = \bigl(|R|^2 + |T|^2\bigr)|E_1|^2 \implies |R|^2 + |T|^2 = 1.
     \]
   - **(b1) 双端口等幅输入条件**：
     令 \(E_1 = E_2 = E \ne 0\)，则 \(E_3 = (R+T)E\)，\(E_4 = (T+R)E\)。由能量守恒：
     \[
     |E|^2 + |E|^2 = |R+T|^2 |E|^2 + |T+R|^2 |E|^2 \implies 2 = 2\bigl(|R|^2 + |T|^2 + R T^* + T R^*\bigr).
     \]
     将 \(|R|^2 + |T|^2 = 1\) 代入，立即得到：
     \[
     R T^* + T R^* = 0.
     \]
   - **(b2) 反射与透射分量的 \(\pi/2\) 相位差**：
     将复系数写为极坐标形式 \(R = |R|e^{i\phi_R}\)，\(T = |T|e^{i\phi_T}\)，代入 \(R T^* + T R^* = 0\)：
     \[
     |R||T|\left(e^{i(\phi_R - \phi_T)} + e^{-i(\phi_R - \phi_T)}\right) = 2|R||T|\cos(\phi_R - \phi_T) = 0.
     \]
     对于非平凡分束器（\(|R| \ne 0, |T| \ne 0\)），必有 \(\cos(\phi_R - \phi_T) = 0\)，即：
     \[
     \Delta\phi = \phi_R - \phi_T = \pm \frac{\pi}{2} \pmod{2\pi}.
     \]
     这证明了对称无损分束器的反射光与透射光之间存在 \(\pi/2\) 的相对相移（对应乘子 \(\pm i\)）。

2. **Exercise 2：狄拉克符号下的量子分束器**
   给定 50/50 分束器演化规则：
   \[
   |a\rangle \xrightarrow{\text{BS}} \frac{1}{\sqrt{2}}\bigl(|c\rangle + i|d\rangle\bigr), \qquad |b\rangle \xrightarrow{\text{BS}} \frac{1}{\sqrt{2}}\bigl(i|c\rangle + |d\rangle\bigr).
   \]
   - **(a)(a) 单光子输入 \(|\psi_{\text{in}}\rangle = |a\rangle\)**：
     输出态为 \(|\psi_{\text{out}}\rangle = \frac{1}{\sqrt{2}}(|c\rangle + i|d\rangle)\)。
     在探测器 C 测得的概率 \(P(C) = \left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}\)；在探测器 D 测得的概率 \(P(D) = \left|\frac{i}{\sqrt{2}}\right|^2 = \frac{1}{2}\)。
   - **(a)(b) 同模式双光子输入 \(|\psi_{\text{in}}\rangle = |a\rangle_1 |a\rangle_2\)**：
     输出态为：
     \[
     |\psi_{\text{out}}\rangle = \frac{1}{2}\bigl(|c\rangle_1 + i|d\rangle_1\bigr)\bigl(|c\rangle_2 + i|d\rangle_2\bigr) = \frac{1}{2}\Bigl(|c\rangle_1|c\rangle_2 + i|c\rangle_1|d\rangle_2 + i|d\rangle_1|c\rangle_2 - |d\rangle_1|d\rangle_2\Bigr).
     \]
     检测概率分别为：
     - 两个光子均在 C：\(P(2C) = |1/2|^2 = \frac{1}{4}\)；
     - 两个光子均在 D：\(P(2D) = |-1/2|^2 = \frac{1}{4}\)；
     - C、D 各测得一个光子（符合计数）：\(P(1C, 1D) = |i/2|^2 + |i/2|^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}\)。
   - **(b)(a) 两个可区分光子输入 \(|\psi_{\text{in}}\rangle = |a\rangle_1 |b\rangle_2\)**：
     输出态为：
     \[
     |\psi_{\text{out}}\rangle = \frac{1}{2}\bigl(|c\rangle_1 + i|d\rangle_1\bigr)\bigl(i|c\rangle_2 + |d\rangle_2\bigr) = \frac{1}{2}\Bigl(i|c\rangle_1|c\rangle_2 + |c\rangle_1|d\rangle_2 - |d\rangle_1|c\rangle_2 + i|d\rangle_1|d\rangle_2\Bigr).
     \]
     由于光子 1 和光子 2 可区分，正交基矢 \(|c\rangle_1|d\rangle_2\) 与 \(|d\rangle_1|c\rangle_2\) 对应不同的物理末态，概率直接相加而不发生振幅相消：
     \[
     P(2C) = \frac{1}{4}, \qquad P(2D) = \frac{1}{4}, \qquad P(1C, 1D) = \left|\frac{1}{2}\right|^2 + \left|-\frac{1}{2}\right|^2 = \frac{1}{2}.
     \]
   - **(b)(b) 两个不可区分的玻色子光子 \(|\psi_{\text{in}}\rangle = \frac{1}{\sqrt{2}}\bigl(|a\rangle_1|b\rangle_2 + |b\rangle_1|a\rangle_2\bigr)\)**：
     输出态为：
     \[
     \begin{aligned}
     |\psi_{\text{out}}\rangle &= \frac{1}{2\sqrt{2}}\Bigl[\bigl(i|c\rangle_1|c\rangle_2 + |c\rangle_1|d\rangle_2 - |d\rangle_1|c\rangle_2 + i|d\rangle_1|d\rangle_2\bigr) + \bigl(i|c\rangle_1|c\rangle_2 - |c\rangle_1|d\rangle_2 + |d\rangle_1|c\rangle_2 + i|d\rangle_1|d\rangle_2\bigr)\Bigr] \\
     &= \frac{i}{\sqrt{2}}\bigl(|c\rangle_1|c\rangle_2 + |d\rangle_1|d\rangle_2\bigr).
     \end{aligned}
     \]
     交叉项完美相消！检测概率为：
     \[
     P(2C) = \frac{1}{2}, \qquad P(2D) = \frac{1}{2}, \qquad P(1C, 1D) = 0 \quad (\text{玻色子聚束 / HOM 零符合！}).
     \]
   - **(b)(c) 两个假想“费米子型光子”反对称态 \(|\psi_{\text{in}}\rangle = \frac{1}{\sqrt{2}}\bigl(|a\rangle_1|b\rangle_2 - |b\rangle_1|a\rangle_2\bigr)\)**：
     输出态为：
     \[
     |\psi_{\text{out}}\rangle = \frac{1}{2\sqrt{2}}\Bigl[2|c\rangle_1|d\rangle_2 - 2|d\rangle_1|c\rangle_2\Bigr] = \frac{1}{\sqrt{2}}\bigl(|c\rangle_1|d\rangle_2 - |d\rangle_1|c\rangle_2\bigr).
     \]
     同探测器项相消，检测概率为：
     \[
     P(2C) = 0, \qquad P(2D) = 0, \qquad P(1C, 1D) = \frac{1}{2} + \frac{1}{2} = 1 \quad (\text{费米子反聚束！}).
     \]

3. **Exercise 3：Hong-Ou-Mandel (HOM) 实验分析**
   - **(a) 量子统计性质判据**：
     实验观测到零延迟处符合计数率出现深谷（HOM dip，趋近于 0），与 Exercise 2(b) 中不可区分玻色子的预测 \(P(1C, 1D) = 0\) 完全一致（而可区分粒子为 \(1/2\)，费米子为 \(1\)，经典波干涉由 Exercise 1 知依赖相对相位且强度关联满足 \(P_{\text{coinc}} \ge 1/4\)）。这直接证实了光子服从**玻色-爱因斯坦统计（对称波函数）**。
   - **(b) HOM 深谷的宽度与深度**：
     - **宽度（Width）**：由单光子波包的**相干时间 \(\tau_c\)**（或相干长度 \(l_c = c\tau_c \sim c/\Delta\nu\)，即光子波包的空间长度/光谱带宽的倒数）决定。只有当两光子的到达时间差 \(|\Delta t| \lesssim \tau_c\) 时，它们的波包在分束器上发生时空重叠，无法通过到达时间加以区分。
     - **深度（Depth / Visibility）**：反映了单光子源发射光子的**不可区分度（Indistinguishability）**与**单光子纯度**。若两个光子在偏振、频率、空间模式、到达时间上完全不可区分，且无多光子噪声，符合计数率在谷底降为 0（可见度 \(100\%\)）；若存在部分可区分性，谷底深度将变浅。
   - **(c) 为什么无相互作用的光子会产生 HOM 干涉谷？**
     HOM 效应并非源于光子之间的直接力场相互作用（光子在真空中确实无相互作用），而是源于全同玻色子多粒子态的**量子路径相消干涉**：产生“C、D 各探测到一个光子”共有两条不可区分的双光子量子路径——“两光子均透射”（振幅 \(T \times T = \frac{1}{\sqrt{2}}\times\frac{1}{\sqrt{2}} = +\frac{1}{2}\)）与“两光子均反射”（振幅 \(R \times R = \frac{i}{\sqrt{2}}\times\frac{i}{\sqrt{2}} = -\frac{1}{2}\)）。由于全同玻色子交换对称性，这两条路径的末态完全相同，概率幅相加 \(\frac{1}{2} + \left(-\frac{1}{2}\right) = 0\)，从而导致符合计数概率严格为零。

#### 第二阶段：交叉核验与教学拆解

- **二次量子化产生算符法（Fock 态）核验**：
  用玻色产生算符 \(\hat{a}^\dagger, \hat{b}^\dagger\) 表示分束器变换：\(\hat{a}^\dagger \to \frac{1}{\sqrt{2}}(\hat{c}^\dagger + i\hat{d}^\dagger)\)，\(\hat{b}^\dagger \to \frac{1}{\sqrt{2}}(i\hat{c}^\dagger + \hat{d}^\dagger)\)。
  双光子输入态 \(|1_a, 1_b\rangle = \hat{a}^\dagger \hat{b}^\dagger |0\rangle\) 演化为：
  \[
  \frac{1}{2}(\hat{c}^\dagger + i\hat{d}^\dagger)(i\hat{c}^\dagger + \hat{d}^\dagger)|0\rangle = \frac{1}{2}\Bigl(i(\hat{c}^\dagger)^2 + \hat{c}^\dagger\hat{d}^\dagger - \hat{d}^\dagger\hat{c}^\dagger + i(\hat{d}^\dagger)^2\Bigr)|0\rangle.
  \]
  利用玻色对易关系 \([\hat{c}^\dagger, \hat{d}^\dagger] = 0\)，中间两项直接抵消，得到 \(\frac{i}{\sqrt{2}}\bigl(|2_c, 0_d\rangle + |0_c, 2_d\rangle\rangle\)（注意 \(|2_c\rangle = \frac{1}{\sqrt{2}}(\hat{c}^\dagger)^2|0\rangle\)），快速验证了 \(P(2C) = P(2D) = 1/2, P(1C, 1D) = 0\)。
- **核心难点与易错点**：
  1. **可区分与不可区分态的概率计算规则**：在 (b)(a) 中，\(|c\rangle_1|d\rangle_2\) 与 \(|d\rangle_1|c\rangle_2\) 虽都对应“C 和 D 各响一次”，但因为光子 1、2 可区分（例如颜色或到达时间不同），原则上可通过测量知道哪一个光子去了 C，因此必须**先取模平方再相加**：\(|1/2|^2 + |-1/2|^2 = 1/2\)；而在 (b)(b) 中，对称化输入态使得 \(|c\rangle_1|d\rangle_2\) 本身的系数为 \(\frac{1 - 1}{2\sqrt{2}} = 0\)，在振幅层面即已抵消。

---

### 3. Radical Pair Spin Chemistry (`plancks-2019-final-problem-slice-q3`)

- **物理模型**：外磁场与超精细相互作用下的自由基对（双电子+单核自旋系统）单重态-三重态量子相干转换
- **难度评级**：D3
- **教学标签**：`自旋化学`、`角动量耦合`、`超精细相互作用`、`单重态-三重态转换`、`拉比振荡`

#### 第一阶段：只看原题的独立盲解

系统包含两个未配对电子自旋 \(\vec{S}_1, \vec{S}_2\)（\(S_1 = S_2 = 1/2\)）与一个核自旋 \(\vec{I}\)（\(I = 1/2\)），哈密顿量为：
\[
\hat{H} = \mu_B g(\vec{B}\cdot\vec{S}_1) + \mu_B g(\vec{B}\cdot\vec{S}_2) + \mu_B(\vec{S}_1 \cdot \hat{A} \cdot \vec{I}).
\]

1. **(Q1) 总自旋的可能取值**：
   - **双电子自由基对总自旋 \(\vec{S} = \vec{S}_1 + \vec{S}_2\)**：由 \(\frac{1}{2} \otimes \frac{1}{2} = 0 \oplus 1\)，电子总自旋量子数可取 **\(S = 0\)（单重态 Singlet）** 或 **\(S = 1\)（三重态 Triplet）**。
   - **三自旋系统总自旋 \(\vec{F} = \vec{S}_1 + \vec{S}_2 + \vec{I} = \vec{S} + \vec{I}\)**：再与核自旋 \(I = 1/2\) 耦合，由 \((0 \oplus 1) \otimes \frac{1}{2} = \frac{1}{2} \oplus \left(\frac{1}{2} \oplus \frac{3}{2}\right)\)，三自旋系统总自旋量子数可取 **\(F = \frac{1}{2}\)（两组二重态，共 4 个态）** 和 **\(F = \frac{3}{2}\)（一组四重态，共 4 个态）**。

2. **(Q2) 描述自由基对量子态的 8 个完备正交归一基波函数 \(\psi_i\) (\(i=1,\dots,8\))**：
   记单电子自旋本征态为 \(|\uparrow\rangle, |\downarrow\rangle\)（对应 \(m_s = \pm 1/2\)），核自旋本征态为 \(|\Uparrow\rangle, |\Downarrow\rangle\)（对应 \(m_I = \pm 1/2\)）。
   - **表示一：电子总自旋 \((S, M_S)\) 与核自旋 \((I, M_I)\) 耦合基（自旋化学标准工作基）**：
     - 电子单重态（\(S = 0, M_S = 0\)）：
       \[
       \psi_1 = |S, \Uparrow\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\bigr)|\Uparrow\rangle, \qquad
       \psi_2 = |S, \Downarrow\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\bigr)|\Downarrow\rangle.
       \]
     - 电子三重态（\(S = 1, M_S = +1, 0, -1\)）：
       \[
       \begin{aligned}
       \psi_3 &= |T_+, \Uparrow\rangle = |\uparrow\uparrow\rangle|\Uparrow\rangle, &
       \psi_4 &= |T_+, \Downarrow\rangle = |\uparrow\uparrow\rangle|\Downarrow\rangle, \\
       \psi_5 &= |T_0, \Uparrow\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle\bigr)|\Uparrow\rangle, &
       \psi_6 &= |T_0, \Downarrow\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle\bigr)|\Downarrow\rangle, \\
       \psi_7 &= |T_-, \Uparrow\rangle = |\downarrow\downarrow\rangle|\Uparrow\rangle, &
       \psi_8 &= |T_-, \Downarrow\rangle = |\downarrow\downarrow\rangle|\Downarrow\rangle.
       \end{aligned}
       \]
   - **表示二：三自旋总角动量 \(|F, M_F; S\rangle\) 共同本征基**：
     - \(S = 0, F = 1/2\) 二重态（2 个态）：\(\tilde{\psi}_{1,2} = |S, \Uparrow\rangle, |S, \Downarrow\rangle\)；
     - \(S = 1, F = 3/2\) 四重态（4 个态）：
       \[
       \begin{aligned}
       \left|\frac{3}{2}, +\frac{3}{2}; 1\right\rangle &= |T_+, \Uparrow\rangle, &
       \left|\frac{3}{2}, +\frac{1}{2}; 1\right\rangle &= \sqrt{\frac{1}{3}}|T_+, \Downarrow\rangle + \sqrt{\frac{2}{3}}|T_0, \Uparrow\rangle, \\
       \left|\frac{3}{2}, -\frac{1}{2}; 1\right\rangle &= \sqrt{\frac{2}{3}}|T_0, \Downarrow\rangle + \sqrt{\frac{1}{3}}|T_-, \Uparrow\rangle, &
       \left|\frac{3}{2}, -\frac{3}{2}; 1\right\rangle &= |T_-, \Downarrow\rangle;
       \end{aligned}
       \]
     - \(S = 1, F = 1/2\) 二重态（2 个态）：
       \[
       \left|\frac{1}{2}, +\frac{1}{2}; 1\right\rangle = \sqrt{\frac{2}{3}}|T_+, \Downarrow\rangle - \sqrt{\frac{1}{3}}|T_0, \Uparrow\rangle, \qquad
       \left|\frac{1}{2}, -\frac{1}{2}; 1\right\rangle = \sqrt{\frac{1}{3}}|T_0, \Downarrow\rangle - \sqrt{\frac{2}{3}}|T_-, \Uparrow\rangle.
       \]

3. **(Q3) 单重态与三重态之间发生跃迁（\(S \leftrightarrow T\) 转换）的条件**：
   - **对称性破缺（非对角耦合矩阵元非零）**：哈密顿量必须不与电子总自旋平方算符 \(\hat{S}^2\) 对易，即 \([\hat{H}, \hat{S}^2] \ne 0\)，等价于存在非零耦合元 \(\langle T_m, m'_I | \hat{H} | S, m_I \rangle \ne 0\)。外磁场塞曼项 \(\mu_B g \vec{B}\cdot(\vec{S}_1 + \vec{S}_2) = \mu_B g \vec{B}\cdot\vec{S}\) 关于两电子完全对称，满足 \([\vec{B}\cdot\vec{S}, \hat{S}^2] = 0\)，不能单独引起 \(S \leftrightarrow T\) 跃迁；只有两个电子感受到不同的局部磁场——即此处仅电子 1 存在非零超精细耦合 \(\hat{A} \ne 0\)——才能混合单重态与三重态。
   - **能级近简并条件（能量匹配条件）**：为使量子相干转换高效发生，单重态与目标三重态之间的塞曼能级劈裂 \(\Delta E_Z \sim \mu_B g B\) 不能远大于超精细耦合非对角元 \(|V_{\text{hfi}}| \sim \mu_B |\hat{A}|\)（即要求外磁场处于弱场/中场区 \(g B \lesssim |\hat{A}|\)，或者跃迁发生在不受外场塞曼移动影响的简并子空间 \(|S\rangle \leftrightarrow |T_0\rangle\) 内）。

4. **(Q4) 数值检验（\(A_{zz} = 16\text{ G}\) 为唯一非零分量，\(B = 0.5\text{ G}\)）**：
   - 超精细相互作用项为 \(\hat{H}_{\text{hfi}} = \mu_B A_{zz} S_{1z} I_z\)（注：在自旋化学与磁共振文献中，以高斯 G 为单位给出的超精细张量 \(A_{zz}\) 通常定义为等效磁场，有时在公式中写为 \(g\mu_B A_{zz} S_{1z} I_z\)，此处按题干式 (1) 保留 \(\mu_B\) 或包含 \(g \approx 2\) 均不影响量级判断）。
   - 注意到 \(S_{1z} = \frac{1}{2}(S_{1z} + S_{2z}) + \frac{1}{2}(S_{1z} - S_{2z})\)，作用在电子单重态上有：
     \[
     S_{1z}|S\rangle = \frac{1}{\sqrt{2}}\left(\frac{1}{2}|\uparrow\downarrow\rangle - \left(-\frac{1}{2}\right)|\downarrow\uparrow\rangle\right) = \frac{1}{2}|T_0\rangle.
     \]
     因此非对角耦合元为：
     \[
     V = \langle T_0, m_I | \hat{H}_{\text{hfi}} | S, m_I \rangle = \mu_B A_{zz} m_I \langle T_0 | S_{1z} | S \rangle = \pm \frac{1}{4}\mu_B A_{zz} \ne 0 \quad (\text{若含 } g \text{ 则为 } \pm \frac{1}{4}g\mu_B A_{zz}).
     \]
   - 同时，特征超精细场强 \(A_{zz} = 16\text{ G}\) 远大于外磁场 \(B = 0.5\text{ G}\)（\(A_{zz} \gg B\)）：若 \(\vec{B} \parallel \hat{z}\)，则 \(|S, m_I\rangle\) 与 \(|T_0, m_I\rangle\) 塞曼能完全简并（\(\Delta E = 0\)）；即便 \(\vec{B} \perp \hat{z}\)，塞曼劈裂 \(\sim 0.5\text{ G}\) 也远小于 \(A_{zz} = 16\text{ G}\)。故 **\(S \leftrightarrow T\) 转换条件完全满足！**

5. **(Q5) 单重态转换为三重态的特征时间 \(\tau\) 估算**：
   在近简并二能级子空间 \(\{|S, m_I\rangle, |T_0, m_I\rangle\}\)（\(m_I = \pm 1/2\)）中，有效哈密顿矩阵为：
   \[
   H_{\text{eff}} = \begin{pmatrix} 0 & V \\ V & 0 \end{pmatrix}, \qquad |V| = \frac{1}{4}\mu_B A_{zz} \quad \left(\text{或含电子 } g\approx 2 \text{ 因子时 } |V| = \frac{1}{4}g\mu_B A_{zz}\right).
   \]
   初态制备在 \(|\Psi(0)\rangle = |S, m_I\rangle\) 时，体系在 \(|S, m_I\rangle\) 与 \(|T_0, m_I\rangle\) 之间发生拉比振荡（Rabi oscillation）：
   \[
   |\Psi(t)\rangle = \cos\left(\frac{|V|t}{\hbar}\right)|S, m_I\rangle - i\sin\left(\frac{|V|t}{\hbar}\right)|T_0, m_I\rangle, \qquad P_{S \to T_0}(t) = \sin^2\left(\frac{|V|t}{\hbar}\right).
   \]
   首次完全转换为三重态 \(|T_0\rangle\)（\(P_{S\to T_0} = 1\)）所需相位为 \(\frac{|V|\tau}{\hbar} = \frac{\pi}{2}\)，故特征转换时间为：
   \[
   \tau = \frac{\pi \hbar}{2 |V|} = \frac{2\pi \hbar}{\mu_B A_{zz}} \quad \left(\text{若含 } g \text{ 因子则为 } \tau = \frac{2\pi \hbar}{g \mu_B A_{zz}}\right).
   \]
   代入物理常数 \(\hbar = 1.055 \times 10^{-34}\text{ J}\cdot\text{s}\)，\(\mu_B = 9.274 \times 10^{-24}\text{ J/T}\)，\(A_{zz} = 16\text{ G} = 1.6 \times 10^{-3}\text{ T}\)：
   - 按题干式 (1) 字面系数（不含 \(g\)）：
     \[
     \tau = \frac{2\pi \times 1.055 \times 10^{-34}}{9.274 \times 10^{-24} \times 1.6 \times 10^{-3}} \approx 4.47 \times 10^{-8}\text{ s} \approx 45\text{ ns}.
     \]
   - 按自旋化学标准定义（\(A_{zz}\) 以高斯为单位对应 \(g\mu_B A_{zz}\)，\(g \approx 2\)）：
     \[
     \tau = \frac{2\pi \hbar}{g\mu_B A_{zz}} \approx 2.23 \times 10^{-8}\text{ s} \approx 22\text{ ns} \quad \left(\text{若取 } \tau \sim \frac{\hbar}{|V|} \text{ 量级则为 } 7\text{--}14\text{ ns}\right).
     \]

#### 第二阶段：交叉核验与教学拆解

- **算符海森堡演化交叉核验**：
  定义差自旋算符 \(\Delta\vec{S} = \vec{S}_1 - \vec{S}_2\)，注意到 \(S_z |S\rangle = 0\)，而 \(\Delta S_z |S\rangle = |T_0\rangle\)，\(\Delta S_z |T_0\rangle = |S\rangle\)。在 \(\vec{B} = B\hat{z}\) 下，电子 1 的总有效磁场为 \(B_{1,\text{eff}} = B + \frac{1}{g} A_{zz} m_I\)，电子 2 的总有效磁场为 \(B_{2,\text{eff}} = B\)。两电子自旋进动角频率差为 \(\Delta\omega = \frac{\mu_B A_{zz} |m_I|}{\hbar} = \frac{\mu_B A_{zz}}{2\hbar}\)。当两电子自旋相对相位演过 \(\Delta\phi = \Delta\omega \cdot \tau = \pi\) 时，反对称单重态 \(\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)\) 恰好翻转成对称三重态 \(\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)\)，所需时间 \(\tau = \frac{\pi}{\Delta\omega} = \frac{2\pi\hbar}{\mu_B A_{zz}}\)，与二能级拉比振荡公式一字不差！
- **核心难点与易错点**：
  1. **漏掉自旋算符的 \(\frac{1}{2}\) 因子**：电子与核自旋算符均为 \(\hat{S}_z = \frac{1}{2}\sigma_z\)，\(\hat{I}_z = \frac{1}{2}\sigma_{Iz}\)（在 \(\hbar = 1\) 单位制下本征值为 \(\pm 1/2\)），因此 \(\langle T_0, \Uparrow | S_{1z} I_z | S, \Uparrow \rangle = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}\)。许多学生误用泡利矩阵本征值 \(\pm 1\)，导致时间算错 4 倍。

---

### 4. Relativistic Orbit (`plancks-2019-final-problem-slice-q4`)

- **物理模型**：狭义相对论修正下的开普勒行星轨道进动与水星近日点进动计算
- **难度评级**：D3
- **教学标签**：`狭义相对论力学`、`相对论拉格朗日量`、`Binet方程`、`轨道进动`、`水星近日点进动`

#### 第一阶段：只看原题的独立盲解

1. **第 1 问（1 分）：小速度极限下 \(-mc^2/\gamma\) 与动能的近似关系**：
   相对论洛伦兹因子为 \(\gamma = \left(1 - \frac{v^2}{c^2}\right)^{-1/2}\)。当 \(v \ll c\) 时，对 \(-\frac{mc^2}{\gamma}\) 作泰勒展开：
   \[
   -\frac{mc^2}{\gamma} = -mc^2\sqrt{1 - \frac{v^2}{c^2}} = -mc^2\left(1 - \frac{v^2}{2c^2} - \frac{v^4}{8c^4} + \mathcal{O}\left(\frac{v^6}{c^6}\right)\right) = -mc^2 + \frac{1}{2}mv^2 + \frac{1}{8}m\frac{v^4}{c^2} + \cdots
   \]
   略去常数静能项 \(-mc^2\) 后，在低速极限下其主导项恰为经典动能 \(\frac{1}{2}mv^2\)！
   （注：从最小作用量原理看，自由相对论粒子的作用量为 \(S = -mc^2 \int d\tau = \int \left(-\frac{mc^2}{\gamma}\right)dt\)，因此 \(-\frac{mc^2}{\gamma}\) 正是生成精确相对论动量 \(\vec{p} = \frac{\partial \mathcal{L}}{\partial \vec{v}} = \gamma m \vec{v}\) 的正确拉格朗日动能项。）

2. **第 2 问（1 分）：太阳-行星系统的相对论拉格朗日量**：
   在平面极坐标 \((r, \theta)\) 中，\(v^2 = \dot{r}^2 + r^2\dot{\theta}^2\)，引力势能 \(V(r) = -\frac{GMm}{r}\)，故相对论拉格朗日量为：
   \[
   \mathcal{L}(r, \dot{r}, \dot{\theta}) = -\frac{mc^2}{\gamma} - V(r) = -mc^2\sqrt{1 - \frac{\dot{r}^2 + r^2\dot{\theta}^2}{c^2}} + \frac{GMm}{r}.
   \]

3. **第 3 问（5 分）：推导相对论轨道方程并求 \(\alpha\) 与 \(r_0\)**：
   - **守恒量分析**：
     由于 \(\theta\) 为循环坐标，正则角动量 \(L\) 守恒：
     \[
     L = \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = \gamma m r^2 \dot{\theta} = \text{const}.
     \]
     由于 \(\mathcal{L}\) 不显含时间 \(t\)，系统总能量（哈密顿量）\(E\) 守恒：
     \[
     E = \dot{r}\frac{\partial \mathcal{L}}{\partial \dot{r}} + \dot{\theta}\frac{\partial \mathcal{L}}{\partial \dot{\theta}} - \mathcal{L} = \gamma m(\dot{r}^2 + r^2\dot{\theta}^2) + \frac{mc^2}{\gamma} - \frac{GMm}{r} = \gamma mc^2 - \frac{GMm}{r} = \text{const}.
     \]
   - **相对论比奈（Binet）轨道方程推导**：
     作変数代换 \(u = \frac{1}{r}\)。由角动量守恒 \(\gamma \dot{\theta} = \frac{L}{mr^2} = \frac{L}{m}u^2\)，对径向速度作链式求导：
     \[
     \gamma \dot{r} = \gamma \frac{dr}{d\theta}\dot{\theta} = -\frac{1}{u^2}\frac{du}{d\theta}\left(\frac{L}{m}u^2\right) = -\frac{L}{m}\frac{du}{d\theta}.
     \]
     利用恒等式 \(\gamma^2 c^2 - \gamma^2(\dot{r}^2 + r^2\dot{\theta}^2) = c^2\)，将 \(\gamma mc^2 = E + GMmu\) 代入：
     \[
     \left(\frac{E + GMmu}{mc}\right)^2 - c^2\left(\frac{L}{m}\right)^2 \left[\left(\frac{du}{d\theta}\right)^2 + u^2\right] = m^2 c^4 / m^2 c^2 = c^2.
     \]
     展开整理得：
     \[
     \left(\frac{du}{d\theta}\right)^2 + \left(1 - \frac{G^2 M^2 m^2}{L^2 c^2}\right) u^2 - \frac{2 G M m^2 E}{L^2 c^2} u = \frac{E^2 - m^2 c^4}{L^2 c^2}.
     \]
     对 \(\theta\) 求导并约去公因子 \(2\frac{du}{d\theta}\)，得到线性常系数二阶微分方程：
     \[
     \frac{d^2 u}{d\theta^2} + \left(1 - \frac{G^2 M^2 m^2}{L^2 c^2}\right) u = \frac{G M m^2 E}{L^2 c^2}.
     \]
     令无量纲进动参数 \(\alpha\) 与半通径 \(r_0\) 分别为：
     \[
     \alpha = \sqrt{1 - \left(\frac{G M m}{L c}\right)^2}, \qquad r_0 = \frac{\alpha^2 L^2 c^2}{G M m^2 E} = \frac{L^2 c^2 - G^2 M^2 m^2}{G M m^2 E} \quad \left(\text{非相对论极限下 } E \approx mc^2, \alpha \to 1 \implies r_0 \to \frac{L^2}{GMm^2}\right),
     \]
     则微分方程化为 \(\frac{d^2 u}{d\theta^2} + \alpha^2 u = \frac{\alpha^2}{r_0}\)，其通解即为旋转椭圆方程：
     \[
     \frac{1}{r} = \frac{1}{r_0}\Bigl\{1 + \varepsilon\cos\bigl[\alpha(\theta - \theta_0)\bigr]\Bigr\}.
     \]

4. **第 4 问（3 分）：水星每世纪近日点进动角计算**：
   - **单圈进动角公式**：
     相邻两次经过近日点满足 \(\alpha \Delta\theta = 2\pi\)。由于 \(\frac{GMm}{Lc} \ll 1\)，有：
     \[
     \alpha = \sqrt{1 - \left(\frac{GMm}{Lc}\right)^2} \approx 1 - \frac{1}{2}\left(\frac{GMm}{Lc}\right)^2 \implies \Delta\theta = \frac{2\pi}{\alpha} \approx 2\pi\left[1 + \frac{1}{2}\left(\frac{GMm}{Lc}\right)^2\right].
     \]
     故每公转一周，近日点角坐标移动量为：
     \[
     \delta\theta_{\text{rev}} = \Delta\theta - 2\pi \approx \pi \left(\frac{GMm}{Lc}\right)^2.
     \]
   - **利用轨道半径 \(a\) 与周期 \(T\) 消去 \(GM\) 和 \(L\)**：
     对近似圆轨道（平均轨道半径 \(a = 58 \times 10^6\text{ km} = 5.8 \times 10^{10}\text{ m}\)，公转周期 \(T = 88\text{ days} = 88 \times 86400\text{ s} = 7.6032 \times 10^6\text{ s}\)），轨道线速度为 \(v = \frac{2\pi a}{T}\)。由牛顿向心力公式 \(\frac{GM}{a^2} = \frac{v^2}{a} \implies GM = a v^2\)，且角动量 \(L \approx m v a\)，故：
     \[
     \frac{GMm}{Lc} \approx \frac{(a v^2) m}{(m v a) c} = \frac{v}{c} = \frac{2\pi a}{c T}.
     \]
   - **代入数值计算**：
     \[
     v = \frac{2\pi \times 5.8 \times 10^{10}\text{ m}}{7.6032 \times 10^6\text{ s}} \approx 4.793 \times 10^4\text{ m/s}, \qquad \frac{v}{c} = \frac{4.793 \times 10^4}{3.00 \times 10^8} \approx 1.598 \times 10^{-4}.
     \]
     单圈进动角为：
     \[
     \delta\theta_{\text{rev}} \approx \pi \left(\frac{v}{c}\right)^2 \approx \pi \times (1.598 \times 10^{-4})^2 \approx 8.02 \times 10^{-8}\text{ rad} \approx 0.0165''.
     \]
     一世纪（\(100\text{ years} = 36525\text{ days}\)）内水星公转圈数 \(N_{\text{orb}} = \frac{36525}{88} \approx 415.06\) 圈，总进动角为：
     \[
     \Delta\theta_{\text{century}} = N_{\text{orb}} \delta\theta_{\text{rev}} \approx 415.06 \times 8.02 \times 10^{-8}\text{ rad} \approx 3.33 \times 10^{-5}\text{ rad} \approx 1.91 \times 10^{-3}\text{ deg} \approx 6.87''\text{ (角秒)}.
     \]

#### 第二阶段：交叉核验与教学拆解

- **物理背景与广义相对论对比核验**：
  狭义相对论（仅考虑相对论质量随速度变化导致的有效势修正 \(-\frac{G^2 M^2 m}{2 c^2 r^2}\)）给出的单圈近日点进动为 \(\delta\theta_{\text{SR}} = \frac{\pi GM}{a(1-e^2)c^2} \approx \pi (v/c)^2 \approx 6.9''/\text{世纪}\)。而在爱因斯坦广义相对论（Schwarzschild 度规）中，测地线方程给出的有效修正势为 \(-\frac{GM L^2}{m c^2 r^3}\)，其进动角为 \(\delta\theta_{\text{GR}} = \frac{6\pi GM}{a(1-e^2)c^2} = 6\,\delta\theta_{\text{SR}} \approx 43''/\text{世纪}\)！狭义相对论效应恰好占广义相对论总进动量的 \(1/6\)，这是理论物理史上极为著名的经典结论。
- **核心难点与易错点**：
  1. **拉格朗日量与哈密顿量的混淆**：切忌把拉格朗日量写成 \(\mathcal{L}_{\text{wrong}} = (\gamma - 1)mc^2 - V(r)\)！因为 \(\frac{\partial}{\partial v}\bigl[(\gamma - 1)mc^2\bigr] = \gamma^3 mv \ne \gamma mv\)。题目第 1 问专门引导考生证明 \(-\frac{mc^2}{\gamma} \approx -mc^2 + \frac{1}{2}mv^2\)，正是为了给出正确的相对论拉格朗日函数 \(\mathcal{L} = -\frac{mc^2}{\gamma} - V\)。
  2. **题干未给太阳质量 \(M_\odot\) 与引力常数 \(G\) 时的代数消元**：第 4 问只给了水星轨道半径 \(a\) 和周期 \(T\)，许多学生试图背诵 \(G\) 和 \(M_\odot\)，实际上直接利用开普勒第三定律 \(\frac{GM}{a v} = v\) 即可将无量纲参数 \(\frac{GMm}{Lc}\) 一步化简为 \(\frac{v}{c} = \frac{2\pi a}{cT}\)。

---

### 5. Polymers and Rubber (`plancks-2019-final-problem-slice-q5`)

- **物理模型**：高分子链三维随机游走模型、熵弹性（Entropic Elasticity）、仿射网络形变自由能与 Joule-Gough 热缩效应
- **难度评级**：D2
- **教学标签**：`统计物理`、`高分子随机游走`、`橡胶熵弹性`、`仿射形变模型`、`Joule-Gough效应`

#### 第一阶段：只看原题的独立盲解

1. **Exercise 1：拉伸单根高分子链**
   给定末端距概率分布：
   \[
   P(x, y, z; N) = \left(\frac{3}{2\pi N b^2}\right)^{3/2} \exp\left(-\frac{3(x^2 + y^2 + z^2)}{2Nb^2}\right).
   \]
   - **1. 一维与三维均方末端距**：
     \(P(x,y,z;N)\) 是三个独立同分布正态随机变量的乘积，每个分量均值 \(\langle x \rangle = 0\)，方差 \(\sigma^2 = \frac{Nb^2}{3}\)。故：
     \[
     \langle x^2 \rangle = \frac{N b^2}{3}, \qquad \langle R^2 \rangle = \langle x^2 + y^2 + z^2 \rangle = 3\langle x^2 \rangle = N b^2.
     \]
   - **2. 均方根空间尺寸与轮廓长度对比**：
     均方根末端距 \(R_{\text{rms}} = \sqrt{\langle R^2 \rangle} = \sqrt{N}\,b\)，完全拉直的轮廓长度 \(L = N b\)，比值 \(\frac{R_{\text{rms}}}{L} = \frac{1}{\sqrt{N}} \ll 1\)（高分子自然状态下呈高度卷曲的线团状）。
     代入聚异戊二烯典型参数 \(N = 20000\)，\(b = 8\text{ \AA} = 0.8\text{ nm}\)：
     \[
     R_{\text{rms}} = 0.8\text{ nm} \times \sqrt{20000} \approx 113.1\text{ nm}, \qquad L = 0.8\text{ nm} \times 20000 = 16000\text{ nm} = 16\text{ }\mu\text{m}.
     \]
   - **3. 亥姆霍兹自由能 \(A(\mathbf{R})\) 与熵弹性恢复力 \(\mathbf{F}(\mathbf{R})\)**：
     微观态数 \(\Omega(\mathbf{R}) \propto P(x,y,z;N)\)，构象熵为：
     \[
     S(\mathbf{R}) = k_B \ln \Omega(\mathbf{R}) = -\frac{3 k_B}{2 N b^2}\mathbf{R}^2 + S_0.
     \]
     忽略内能 \(U\) 与常数项，亥姆霍兹自由能为：
     \[
     A(\mathbf{R}) = -T S(\mathbf{R}) = \frac{3 k_B T}{2 N b^2}\mathbf{R}^2 = \frac{3 k_B T}{2 N b^2}(x^2 + y^2 + z^2).
     \]
     高分子链对悬臂梁施加的力为自由能的负梯度：
     \[
     \mathbf{F}(\mathbf{R}) = -\nabla_{\mathbf{R}} A(\mathbf{R}) = -\frac{3 k_B T}{N b^2}\mathbf{R}.
     \]
     这表明单根理想高分子链等效于劲度系数 \(k_{\text{eff}} = \frac{3 k_B T}{N b^2} \propto T\) 的胡克弹簧，其恢复力完全源于构象熵的减少（熵弹性）。

2. **Exercise 2：交联橡胶网络的形变自由能密度**
   - **1. 形变后单根链段的均方末端距**：
     交联在未形变态完成，初始坐标 \((x,y,z)\) 服从 \(P(x,y,z;N_s)\)，满足 \(\langle x^2 \rangle = \langle y^2 \rangle = \langle z^2 \rangle = \frac{N_s b^2}{3}\)。
     在不可压缩单轴拉伸 \(\lambda_x = \lambda\)，\(\lambda_y = \lambda_z = \lambda^{-1/2}\) 下：
     \[
     \langle R_{\text{def}}^2 \rangle = \langle \lambda_x^2 x^2 + \lambda_y^2 y^2 + \lambda_z^2 z^2 \rangle = \lambda^2 \langle x^2 \rangle + \lambda^{-1}\langle y^2 \rangle + \lambda^{-1}\langle z^2 \rangle = \frac{N_s b^2}{3}\left(\lambda^2 + 2\lambda^{-1}\right).
     \]
   - **2. 单链平均自由能与单位体积自由能密度变化 \(\Delta a(\lambda)\)**：
     将 \(\langle R_{\text{def}}^2 \rangle\) 代入 Exercise 1 的自由能公式（\(N \to N_s\)）：
     \[
     \langle A(\lambda) \rangle = \frac{3 k_B T}{2 N_s b^2}\langle R_{\text{def}}^2 \rangle = \frac{k_B T}{2}\left(\lambda^2 + 2\lambda^{-1}\right).
     \]
     未形变态（\(\lambda = 1\)）时 \(\langle A(1) \rangle = \frac{3}{2}k_B T\)。乘以网络链段数密度 \(\rho_s\)，得到自由能密度变化：
     \[
     \Delta a(\lambda) \equiv \rho_s\bigl(\langle A(\lambda) \rangle - \langle A(1) \rangle\bigr) = \frac{\rho_s k_B T}{2}\left(\lambda^2 + 2\lambda^{-1} - 3\right) = \frac{G}{2}\left(\lambda^2 + 2\lambda^{-1} - 3\right),
     \]
     其中剪切模量 \(G = \rho_s k_B T\)。
   - **3. 链段数密度 \(\rho_s\) 与剪切模量 \(G\) 的数值计算**：
     给定体密度 \(\rho = 0.830\text{ g/cm}^3 = 830\text{ kg/m}^3\)，单步摩尔质量 \(M_0 = 113\text{ g/mol} = 0.113\text{ kg/mol}\)，每条链段步数 \(N_s = 44\)，室温取 \(T = 298\text{ K}\)（或 \(300\text{ K}\)）：
     - 链段数密度：
       \[
       \rho_s = \frac{\rho N_A}{N_s M_0} = \frac{830 \times 6.022 \times 10^{23}}{44 \times 0.113} \approx 1.005 \times 10^{26}\text{ m}^{-3}.
       \]
     - 剪切模量：
       \[
       G = \rho_s k_B T = \frac{\rho R T}{N_s M_0} \approx \frac{830 \times 8.314 \times 298}{44 \times 0.113} \approx 4.14 \times 10^5\text{ Pa} = 0.414\text{ MPa} \quad (T=300\text{ K 时为 } 0.416\text{ MPa}).
       \]

3. **Exercise 3：橡皮筋的力-伸长关系与热力学行为**
   - **1. 力-伸长关系表达式与曲线特征**：
     橡皮筋初始尺寸 \(L_{x1} = 10\text{ cm} = 0.10\text{ m}\)，初始截面积 \(A_0 = L_{y1} L_{z1} = 0.3\text{ cm} \times 0.3\text{ cm} = 9.0 \times 10^{-6}\text{ m}^2\)，体积 \(V = A_0 L_{x1}\) 保持不变。由 \(L_x(\lambda) = L_{x1}\lambda\)，外加拉力为：
     \[
     F(\lambda) = \frac{d\bigl(V \Delta a(\lambda)\bigr)}{d L_x(\lambda)} = \frac{V}{L_{x1}}\frac{d\Delta a(\lambda)}{d\lambda} = A_0 G \left(\lambda - \frac{1}{\lambda^2}\right) = A_0 G \left[\frac{L_x}{L_{x1}} - \left(\frac{L_{x1}}{L_x}\right)^2\right].
     \]
     图像特征：当 \(L_x = L_{x1}\)（\(\lambda = 1\)）时 \(F = 0\)；在 \(L_x\) 略大于 \(L_{x1}\) 时斜率较陡（初始斜率 \(3A_0 G / L_{x1}\)），随后斜率逐渐减小并在大拉伸区趋于渐近直线 \(F \approx \frac{A_0 G}{L_{x1}} L_x\)。
   - **2. 小形变与大形变极限近似**：
     - **小形变极限（\(\lambda = 1 + \epsilon, \epsilon \ll 1\)）**：
       \[
       \lambda - \lambda^{-2} = (1 + \epsilon) - (1 - 2\epsilon + 3\epsilon^2 - \cdots) \approx 3\epsilon \implies F \approx 3 A_0 G \epsilon = 3 A_0 G \frac{L_x - L_{x1}}{L_{x1}}.
       \]
       （注：由此可见不可压缩橡胶的杨氏模量 \(E = 3G\)，对应泊松比 \(\nu = 0.5\)。）
     - **大形变极限（\(\lambda \gg 1\)）**：
       忽略 \(\lambda^{-2}\) 项，得线性渐近关系：
       \[
       F(\lambda) \approx A_0 G \lambda = A_0 \rho_s k_B T \frac{L_x}{L_{x1}}.
       \]
   - **3. 悬挂 \(m = 1\text{ kg}\) 重物的平衡长度及加热至 \(T = 500\text{ K}\) 后的反常收缩**：
     外力 \(F = mg = 1\text{ kg} \times 9.81\text{ m/s}^2 = 9.81\text{ N}\)。在大形变近似 \(F \approx A_0 G \frac{L_x}{L_{x1}}\) 下：
     \[
     L_x(T) \approx \frac{m g L_{x1}}{A_0 G(T)} = \frac{m g L_{x1}}{A_0 \rho_s k_B T} \propto \frac{1}{T}.
     \]
     - **室温下（\(T_1 = 298\text{ K}\)）**：
       - 若用 Exercise 2 算出的 \(G = 0.414\text{ MPa}\)（\(A_0 G = 3.726\text{ N}\)）：\(\lambda = \frac{9.81}{3.726} \approx 2.63 \implies L_x \approx 26.3\text{ cm}\)（若解精确三次方程 \(\lambda - \lambda^{-2} = 2.63\)，则 \(\lambda \approx 2.76, L_x \approx 27.6\text{ cm}\)）。
       - 若用题干备用估计值 \(G = 0.5\text{ MPa}\)（\(A_0 G = 4.50\text{ N}\)）：\(\lambda = \frac{9.81}{4.50} \approx 2.18 \implies L_x \approx 21.8\text{ cm}\)。
     - **瞬间加热至 \(T_2 = 500\text{ K}\) 后**：
       由于 \(G \propto T\)，升温使熵弹性模量增大，橡皮筋发生**热缩（Joule-Gough 效应）**：
       \[
       L_x(500\text{ K}) = L_x(T_1)\frac{T_1}{T_2} \approx \begin{cases} 26.3\text{ cm} \times \frac{298}{500} \approx 15.7\text{ cm} & (\text{采用 } G = 0.414\text{ MPa}), \\ 21.8\text{ cm} \times \frac{300}{500} \approx 13.1\text{ cm} & (\text{采用 } G = 0.5\text{ MPa}). \end{cases}
       \]
   - **4. 断裂伸长比 \(\lambda_c\) 估算**：
     在大形变极限（\(\lambda \gg 1\)）下，形变链段的均方根末端距为：
     \[
     R_{\text{rms}}(\lambda) = \sqrt{\langle R_{\text{def}}^2 \rangle} = \sqrt{\frac{N_s b^2}{3}\left(\lambda^2 + \frac{2}{\lambda}\right)} \approx b\sqrt{\frac{N_s}{3}}\,\lambda.
     \]
     链段的最大轮廓长度为 \(L_{\text{strand}} = N_s b\)。令 \(R_{\text{rms}}(\lambda_c) = 0.5 L_{\text{strand}} = 0.5 N_s b\)：
     \[
     b\sqrt{\frac{N_s}{3}}\,\lambda_c = 0.5 N_s b \implies \lambda_c = 0.5\sqrt{3 N_s}.
     \]
     代入 \(N_s = 44\)：
     \[
     \lambda_c = 0.5\sqrt{3 \times 44} = 0.5\sqrt{132} \approx 5.74 \quad (\text{对应断裂长度 } L_{x,c} \approx 57.4\text{ cm}).
     \]

#### 第二阶段：交叉核验与教学拆解

- **连续介质力学与热力学麦克斯韦关系核验**：
  1. 在小应变下，不可压缩各向同性弹性体的泊松比 \(\nu = 1/2\)，杨氏模量 \(E = 2G(1 + \nu) = 3G\)，与我们在 Exercise 3.2 中由 \(\lambda - \lambda^{-2} \approx 3\epsilon\) 导出的比例系数 \(3\) 完全吻合。
  2. 由热力学基本方程 \(dA = -S dT + F dL_x\)，麦克斯韦关系给出 \(\left(\frac{\partial S}{\partial L_x}\right)_T = -\left(\frac{\partial F}{\partial T}\right)_{L_x}\)。因为拉伸高分子链使其构象数减少，\(\left(\frac{\partial S}{\partial L_x}\right)_T < 0\)，故定长升温时张力必然增大 \(\left(\frac{\partial F}{\partial T}\right)_{L_x} > 0\)，定张力升温时长度必然缩短！
- **核心难点与易错点**：
  1. **对 \(L_x(\lambda)\) 求导与对 \(\lambda\) 求导的转换**：\(F(\lambda) = \frac{d(V \Delta a)}{d L_x}\)，注意 \(V = A_0 L_{x1}\) 在不可压缩形变中是常数，且 \(d L_x = L_{x1} d\lambda\)，故 \(\frac{V}{L_{x1}} = A_0\)（即未形变时的初始横截面积，对应的应力 \(F/A_0\) 称为工程应力 / 名义应力）。

---

### 6. Topological Defects (`plancks-2019-final-problem-slice-q6`)

- **物理模型**：二维 XY 铁磁模型的连续极限、涡旋拓扑缺陷（Vortex）能量-熵竞争与 Kosterlitz-Thouless (BKT) 无限阶相变
- **难度评级**：D3
- **教学标签**：`统计物理`、`二维XY模型`、`拓扑缺陷`、`涡旋环绕数`、`Kosterlitz-Thouless相变`

#### 第一阶段：只看原题的独立盲解

1. **Problem 1（2 分）：低温连续场近似**：
   二维晶格上的 O(2) 铁磁 XY 模型哈密顿量为：
   \[
   H = -\frac{J}{2}\sum_{\langle ij \rangle}\vec{S}_i \cdot \vec{S}_j = -\frac{J}{2}\sum_{\langle ij \rangle}\cos(\theta_i - \theta_j),
   \]
   其中 \(\vec{S}_i = (\cos\theta_i, \sin\theta_i)\)。在低温下，相邻格点自旋夹角变化平缓，\(|\theta_i - \theta_j| \ll 1\)，作泰勒展开：
   \[
   \cos(\theta_i - \theta_j) \simeq 1 - \frac{1}{2}(\theta_i - \theta_j)^2 \simeq 1 - \frac{1}{2}\bigl[(\vec{x}_j - \vec{x}_i)\cdot\vec{\nabla}\theta(\vec{x}_i)\bigr]^2.
   \]
   设每个格点有 \(z\) 个最近邻，晶格常数为 \(a\)。对全晶格 \(N\) 个格点求和：
   - 常数项给出基态能量项（相差符号约定）：\(-\frac{Jz}{2}N\)（题干式 (3) 将常数项记作 \(\frac{Kz}{2}N\)，不影响场导数变分）；
   - 梯度项对最近邻方向求和 \(\sum_{\delta} \delta_\mu \delta_\nu = c a^2 \delta_{\mu\nu}\)，并将离散格点求和转化为面积分 \(\sum_i a^2 \to \int_A d^2x\)，得到连续场哈密顿量：
     \[
     H \simeq \text{const} + \frac{K}{2}\int_A d^2x\,\partial_\mu \theta(\vec{x})\partial_\mu \theta(\vec{x}), \qquad K = \frac{J}{2}c.
     \]

2. **Problem 2（2 分）：能量极小构型的拉普拉斯方程**：
   对连续哈密顿量泛函 \(H[\theta]\) 关于角度场 \(\theta(\vec{x}) \to \theta(\vec{x}) + \delta\theta(\vec{x})\) 求一阶变分并分部积分：
   \[
   \delta H = K\int_A d^2x\,\partial_\mu\theta\,\partial_\mu(\delta\theta) = -K\int_A d^2x\,\bigl(\partial_\mu\partial_\mu\theta(\vec{x})\bigr)\delta\theta(\vec{x}) + \text{边界项} = 0.
   \]
   由变分基本引理，低温下能量最优的场构型满足二维拉普拉斯方程（调和场方程）：
   \[
   \partial_\mu\partial_\mu\theta(\vec{x}) = \vec{\nabla}^2\theta(\vec{x}) = 0.
   \]

3. **Problem 3（1 分）：验证单涡旋解 \(\theta(x_1, x_2) = \theta_0 + q\varphi(x_1, x_2) = \theta_0 + q\tan^{-1}(x_2/x_1)\)**：
   - 在除去原点 \((0,0)\) 的平面极坐标 \((r, \varphi)\) 中，\(\theta(r, \varphi) = \theta_0 + q\varphi\) 与径向坐标 \(r\) 无关（\(\frac{\partial\theta}{\partial r} = 0\)），且关于 \(\varphi\) 为线性函数（\(\frac{\partial\theta}{\partial\varphi} = q\)，\(\frac{\partial^2\theta}{\partial\varphi^2} = 0\)）。代入极坐标拉普拉斯算符：
     \[
     \vec{\nabla}^2\theta = \frac{\partial^2\theta}{\partial r^2} + \frac{1}{r}\frac{\partial\theta}{\partial r} + \frac{1}{r^2}\frac{\partial^2\theta}{\partial\varphi^2} = 0 \quad (\forall r > 0),
     \]
     满足式 (4)。
   - 沿绕原点逆时针一周的闭合曲线 \(C\) 积分：
     \[
     \oint_C d\theta = \int_0^{2\pi} \frac{\partial\theta}{\partial\varphi}d\varphi = \int_0^{2\pi} q\,d\varphi = 2\pi q, \qquad q \in \mathbb{Z},
     \]
     满足拓扑量子化条件式 (5)。

4. **Problem 4（1 分）：读取 Figure 3 中两个点缺陷的拓扑强度 \(q\)**：
   观察原卷第 13 页 Figure 3 的自旋矢量场纹理：
   - **方法一（沿绕原点的逆时针圆周追踪自旋旋转角）**：
     - **左图**：在 \(+x\) 轴（\(\varphi=0\)）自旋指向右（\(\theta=0\)）；随方位角 \(\varphi\) 逆时针增加到 \(\pi/2\)（\(+y\) 轴），自旋顺时针旋转了 \(180^\circ\) 指向左（\(\theta = -\pi\)）；绕原点逆时针一整圈（\(\Delta\varphi = 2\pi\)），自旋顺时针旋转了 \(2\) 圈（\(\Delta\theta = -4\pi\)），故拓扑强度为 **\(q = -2\)**。
     - **右图**：在 \(+x\) 轴（\(\varphi=0\)）自旋指向右（\(\theta=0\)）；在 \(\varphi=\pi/4\) 指向左下（\(\theta = -3\pi/4\)）；在 \(+y\) 轴（\(\varphi=\pi/2\)）指向上（\(\theta = -3\pi/2\)）；绕原点逆时针一整圈，自旋顺时针旋转了 \(3\) 圈（\(\Delta\theta = -6\pi\)），故拓扑强度为 **\(q = -3\)**。
   - **方法二（鞍点双曲扇区/径向分界线计数法）**：
     对于 \(\theta = q\varphi\)，自旋沿径向（\(\theta = \varphi \pmod\pi\)）的直线条数为 \(N_{\text{sep}} = 2|1 - q|\)。Figure 2 中 \(q = -1\) 有 \(2|1 - (-1)| = 4\) 个双曲扇区；Figure 3 左图有 \(6\) 个双曲扇区，由 \(2(1 - q) = 6 \implies q = -2\)；Figure 3 右图有 \(8\) 个双曲扇区，由 \(2(1 - q) = 8 \implies q = -3\)。

5. **Problem 5（1 分）：计算强度为 \(q\) 的缺陷自能并解释为何 \(|q|=1\) 占主导**：
   由 \(\vec{\nabla}\theta = \frac{1}{r}\frac{\partial\theta}{\partial\varphi}\vec{e}_\varphi = \frac{q}{r}\vec{e}_\varphi\)，有 \((\vec{\nabla}\theta)^2 = \frac{q^2}{r^2}\)。在红外截断 \(R\)（系统尺寸）与紫外截断 \(a\)（晶格常数/涡旋核半径）之间积分：
   \[
   E_q = \frac{K}{2}\int_a^R r\,dr \int_0^{2\pi} d\varphi\,\frac{q^2}{r^2} = \pi q^2 K \int_a^R \frac{dr}{r} = \pi q^2 K \ln\left(\frac{R}{a}\right).
   \]
   由于自能正比于 \(q^2\) 且宏观系统中 \(\ln(R/a) \gg 1\)，一个高阶缺陷（\(|q| \ge 2\)）的能量 \(\pi q^2 K \ln(R/a)\) 严格大于 \(|q|\) 个独立单位缺陷的能量之和 \(|q|\pi K \ln(R/a)\)（因 \(q^2 > |q|\) 对一切 \(|q| \ge 2\) 成立）。因此高阶涡旋在能量上不稳定，会自发分裂为单位涡旋 \(|q|=1\)，且其热激发玻尔兹曼权重 \(\exp(-E_q/k_B T) = (R/a)^{-\pi K q^2 / k_B T}\) 随 \(q^2\) 指数衰减，故系统中由 \(|q| = 1\) 缺陷主导。

6. **Problem 6（1 分）：单个缺陷的平动熵（构型熵）**：
   面积为 \(A = \pi R^2\) 的二维晶格中共有约 \(\Omega_1 \simeq \frac{\pi R^2}{\pi a^2} = \left(\frac{R}{a}\right)^2\) 个可供放置涡旋核心的格点/晶胞位置。故单个缺陷的平动熵为：
   \[
   S_1 = k_B \ln \Omega_1 = k_B \ln\left[\left(\frac{R}{a}\right)^2\right] = 2 k_B \ln\left(\frac{R}{a}\right).
   \]

7. **Problem 7（2 分）：正反涡旋对的自由能与自发产生临界温度 \(T_{\text{KT}}\)**：
   按题干模型，产生一对拓扑荷为 \(+1\) 和 \(-1\) 的独立缺陷，每个缺陷的能量代价为 \(E_1 = \pi K \ln(R/a)\)，总能量为 \(E_{\text{pair}} = 2 E_1 = 2\pi K \ln(R/a)\)；两个缺陷可在晶格中自由独立移动，总构型熵为 \(S_{\text{pair}} = 2 S_1 = 4 k_B \ln(R/a)\)。
   因此涡旋对的亥姆霍兹自由能为：
   \[
   F_{\text{pair}} = E_{\text{pair}} - T S_{\text{pair}} = 2\bigl(\pi K - 2 k_B T\bigr)\ln\left(\frac{R}{a}\right) \quad \left(\text{每个缺陷的自由能为 } F_1 = (\pi K - 2k_B T)\ln\frac{R}{a}\right).
   \]
   当 \(F_{\text{pair}} < 0\) 时，产生自由涡旋对使系统自由能降低，缺陷对将自发大量增殖。临界温度（Kosterlitz-Thouless 温度）由 \(\pi K - 2 k_B T_{\text{KT}} = 0\) 给出：
   \[
   T_{\text{KT}} = \frac{\pi K}{2 k_B}.
   \]

8. **附加思考题（0 分）：什么是“无限阶相变（Infinite-order phase transition）”？**
   在 Ehrenfest 相变分类中，若自由能对温度（或外场）的第 \(n\) 阶导数发生不连续跳变或发散，而前 \(n-1\) 阶导数均连续，则称为 \(n\) 阶相变。在 BKT 相变中，关联长度在 \(T \to T_{\text{KT}}^+\) 时按 \(\xi \propto \exp\bigl(b/\sqrt{T - T_{\text{KT}}}\bigr)\) 呈指数发散，自由能奇异部分为 \(F_{\text{sing}} \propto \xi^{-2} \propto \exp\bigl(-2b/\sqrt{T - T_{\text{KT}}}\bigr)\)。该函数在 \(T = T_{\text{KT}}\) 处具有**本性奇点（Essential Singularity）**：自由能对温度的**任意有限阶导数** \(\frac{\partial^n F}{\partial T^n}\) 在相变点处全部连续（因而没有任何潜热或热容跳变），但自由能本身是非解析的，故称为“无限阶相变”。

#### 第二阶段：交叉核验与教学拆解

- **束缚涡旋对相互作用能与重整化群图像核验**：
  在真实无穷大平面中，单个孤立涡旋的总拓扑荷非零，无法单独从无缺陷基态激发，必须成对激发 \((+1, -1)\)。相距为 \(r\) 的正反涡旋对在远场相互屏蔽，其相互作用能为 \(E_{\text{int}}(r) \simeq 2\pi K \ln(r/a)\)。在二维平面内，当质心固定时，相对坐标 \(\vec{r}\) 在尺度 \(r\) 附近的构型熵也是 \(S_{\text{rel}}(r) \simeq 2k_B \ln(r/a)\)，计算涡旋对的平均平方间距 \(\langle r^2 \rangle \propto \int_a^\infty r\,dr\,r^2 e^{-2\pi K \ln(r/a) / k_B T} = \int_a^\infty dr\,r^{3 - 2\pi K / k_B T}\)，该积分在 \(3 - \frac{2\pi K}{k_B T} = -1 \implies T_{\text{KT}} = \frac{\pi K}{2k_B}\) 处发散（即涡旋对解绑 unbinding）！两种截然不同的统计推导给出了完全相同的 \(T_{\text{KT}} = \frac{\pi K}{2k_B}\)。
- **核心难点与易错点**：
  1. **矢量场拓扑荷 \(q\) 的快速判别**：在看图识 \(q\)（Problem 4）时，最稳妥的方法是画一个绕原点逆时针的小圆，观察箭头方向随圆周角 \(\varphi\) 是逆时针转（\(q > 0\)）还是顺时针转（\(q < 0\)），或者直接数径向分界线（Separatrices）的条数 \(N_{\text{sep}} = 2|1-q|\)。

---

### 7. Higgs Mechanism (`plancks-2019-final-problem-slice-q7`)

- **物理模型**：超导伦敦穿透深度（Meissner 效应）、有质量矢量玻色子 Proca 方程与阿贝尔希格斯机制（自发对称性破缺）
- **难度评级**：D2
- **教学标签**：`超导电性`、`London方程`、`Meissner效应`、`Proca方程`、`Higgs机制`

#### 第一阶段：只看原题的独立盲解

1. **(a)（2 分）由麦克斯韦方程组与伦敦方程推导磁场屏蔽方程 (11)**：
   在静磁情形（\(\frac{\partial\vec{E}}{\partial t} = 0\)）下，安培环路定理与磁场高斯定理为：
   \[
   \nabla \times \vec{B} = \mu_0 \vec{j}_s, \qquad \nabla \cdot \vec{B} = 0.
   \]
   对安培定律两边取旋度，利用矢量恒等式 \(\nabla \times (\nabla \times \vec{B}) = \nabla(\nabla\cdot\vec{B}) - \nabla^2\vec{B} = -\nabla^2\vec{B}\)：
   \[
   -\nabla^2\vec{B} = \mu_0 (\nabla \times \vec{j}_s).
   \]
   代入题干给定的伦敦方程 (9) \(\nabla \times \vec{j}_s = -\frac{(2e)^2 n_c}{m_c c^2}\vec{B}\)，以及库珀对数密度 \(n_c = \frac{1}{2}n_e\)、质量 \(m_c = 2m_e\)：
   \[
   -\nabla^2\vec{B} = -\mu_0 \frac{4e^2 (n_e/2)}{(2m_e) c^2}\vec{B} = -\frac{\mu_0 e^2 n_e}{m_e c^2}\vec{B} \implies \nabla^2\vec{B} = \frac{\mu_0 e^2 n_e}{m_e c^2}\vec{B} = \frac{1}{\lambda^2}\vec{B},
   \]
   其中穿透深度 \(\lambda = \sqrt{\frac{m_e c^2}{\mu_0 e^2 n_e}}\)（注：此处严格遵循题干式 (9) 與式 (11) 的符号约定）。

2. **(b)（2 分）一维半无限超导体中的磁场分布 \(\vec{B} = B(x)\vec{e}_z\)**：
   将 \(\vec{B}(x) = B(x)\vec{e}_z\) 代入 \(\nabla^2\vec{B} = \frac{1}{\lambda^2}\vec{B}\)，得常微分方程：
   \[
   \frac{d^2 B(x)}{dx^2} = \frac{1}{\lambda^2}B(x) \implies B(x) = B_0 e^{-x/\lambda} + C e^{+x/\lambda}.
   \]
   由无穷远处边界条件 \(\lim_{x\to\infty} B(x) = 0\)，必有 \(C = 0\)。故超导体内磁场呈指数衰减（迈斯纳效应）：
   \[
   \vec{B}(x) = B_0 e^{-x/\lambda}\vec{e}_z.
   \]

3. **(c)（1 分）对比汤川势（Yukawa Potential）猜测穿透深度 \(\lambda\) 与玻色子质量 \(M\) 的关系**：
   对比汤川势 \(V^{\text{Yuk}}(r) = \frac{e^{-\frac{cM}{\hbar}r}}{4\pi r}\) 中的指数衰减因子 \(e^{-\frac{cM}{\hbar}r}\) 与超导磁场解 \(e^{-x/\lambda}\)，两者的特征衰减长度直接对应（即玻色子的约化康普顿波长）：
   \[
   \frac{1}{\lambda} \sim \frac{c M}{\hbar} \implies \lambda = \frac{\hbar}{M c} \quad \left(\text{或结合式 (13) 含 }\mu_0\text{ 的约定写为 }\frac{1}{\lambda^2} = \mu_0\left(\frac{c}{\hbar}M\right)^2\right).
   \]

4. **(d)（3 分）库仑规范下矢势方程与非含时 Proca 方程推导**：
   - 将 \(\vec{B} = \nabla \times \vec{A}\) 代入静磁安培定律 \(\nabla \times \vec{B} = \mu_0 \vec{j}_s\)：
     \[
     \nabla \times (\nabla \times \vec{A}) = \nabla(\nabla\cdot\vec{A}) - \nabla^2\vec{A} = \mu_0 \vec{j}_s.
     \]
     采用**库仑规范（Coulomb gauge）\(\nabla\cdot\vec{A} = 0\)**，立得式 (12)：
     \[
     -\nabla^2\vec{A} = \mu_0 \vec{j}_s.
     \]
   - 再将 \(\vec{B} = \nabla \times \vec{A}\) 代入伦敦方程 (9)：
     \[
     \nabla \times \vec{j}_s = -\frac{e^2 n_e}{m_e c^2}(\nabla \times \vec{A}) \implies \nabla \times \left(\vec{j}_s + \frac{e^2 n_e}{m_e c^2}\vec{A}\right) = 0.
     \]
     这表明括号内的矢量场是无旋场，可写为标量函数梯度 \(\nabla\chi\)。进一步指定**伦敦规范（London gauge）**：在保持 \(\nabla\cdot\vec{A} = 0\) 的同时要求规范函数使 \(\chi = 0\)（且在超导体深处 \(\vec{A}\to 0, \vec{j}_s\to 0\)，法向分量匹配边界），从而直接有第一伦敦方程：
     \[
     \vec{j}_s = -\frac{e^2 n_e}{m_e c^2}\vec{A}.
     \]
     将其代入式 (12) \(-\nabla^2\vec{A} = \mu_0 \vec{j}_s\)，并代入 \(\frac{\mu_0 e^2 n_e}{m_e c^2} = \frac{1}{\lambda^2} = \mu_0\left(\frac{c}{\hbar}M\right)^2\)，即得非含时 Proca 方程 (13)：
     \[
     \left(-\nabla^2 + \mu_0\left(\frac{c}{\hbar}M\right)^2\right)\vec{A} = 0.
     \]

5. **(e)（2 分）希格斯势真空期望值 \(v\) 的存在条件与规范玻色子质量 \(M\)**：
   给定希格斯势 \(V(\phi) = \mu^2\phi^2 + \lambda\phi^4\)（\(\lambda > 0\)）。求极值点：
   \[
   \frac{dV}{d\phi} = 2\phi\bigl(\mu^2 + 2\lambda\phi^2\bigr) = 0.
   \]
   - **非零真空期望值 \(v \ne 0\) 存在的条件**：由于 \(\lambda > 0\)，若 \(\mu^2 \ge 0\)，则唯一实根为 \(\phi = 0\)；要使方程存在非零实根 \(v \ne 0\)（且 \(\frac{d^2 V}{d\phi^2}\big|_{\phi=v} = -4\mu^2 > 0\) 为极小值点），必须满足：
     \[
     \mu^2 < 0,
     \]
     此时真空极小值位于：
     \[
     v^2 = -\frac{\mu^2}{2\lambda} > 0 \implies v = \pm\sqrt{-\frac{\mu^2}{2\lambda}}.
     \]
   - **规范玻色子的测量质量 \(M\)**：在自然单位制（\(\hbar = c = \mu_0 = 1\)）下，将真空流 \(\vec{j} = -g^2 v^2 \vec{A}\)（式 16）代入波动方程 (14) \(\left(\frac{\partial^2}{\partial t^2} - \nabla^2\right)\vec{A} = \vec{j}\)，得到：
     \[
     \left(\frac{\partial^2}{\partial t^2} - \nabla^2 + g^2 v^2\right)\vec{A} = 0.
     \]
     与自然单位制下的 Proca 方程 (15) \(\left(\frac{\partial^2}{\partial t^2} - \nabla^2 + M^2\right)\vec{A} = 0\) 对比系数，立得规范玻色子的质量为：
     \[
     M = g|v| = g\sqrt{-\frac{\mu^2}{2\lambda}}.
     \]

#### 第二阶段：交叉核验与教学拆解

- **规范协变导数拉格朗日量核验**：
  在粒子物理阿贝尔 Higgs 模型（即相对论 Ginzburg-Landau 模型）中，标量场动能项为 \(\mathcal{L}_{\text{kin}} = |D_\mu \phi|^2 = |(\partial_\mu - i g A_\mu)\phi|^2\)。当 \(\phi\) 在真空态凝聚到 \(v = \sqrt{-\mu^2/(2\lambda)}\) 时，\(\mathcal{L}_{\text{kin}}\) 中出现 \(\frac{1}{2}(2 g^2 v^2) A_\mu A^\mu\)（或实标量规范归一化下的 \(g^2 v^2 A^2 / 2\)），其欧拉-拉格朗日方程给出四维流 \(j^\mu = -g^2 v^2 A^\mu\)，对应规范玻色子质量 \(M = g|v|\)，与题干通过超导伦敦流类比导出的结果完全一致。
- **核心难点与易错点**：
  1. **题干混合单位制的识别**：注意题干式 (9) 在 SI 制下多写了一个 CGS 制的 \(1/c^2\) 因子，并在式 (13) 和 (15) 中给质量项乘了 \(\mu_0\)。在竞赛答题中，切勿擅自删改题目给定方程中的常数因子，而应严格按题干给定的方程 (9)、(11)、(13)、(15) 进行代数变形。

---

### 8. Black Hole Picture (`plancks-2019-final-problem-slice-q8`)

- **物理模型**：黑洞史瓦西半径的牛顿逃逸速度导出、引力透镜光子球（光环与阴影）、事件视界望远镜（EHT）VLBI 衍射极限分辨率与强场引力判据
- **难度评级**：D2
- **教学标签**：`天体物理`、`广义相对论`、`史瓦西黑洞`、`事件视界望远镜(EHT)`、`量纲分析`

#### 第一阶段：只看原题的独立盲解

1. **第 1 问（2 分）：用牛顿力学与光速极限导出黑洞半径，并用量纲分析解释**：
   - **牛顿逃逸速度推导（Michell-Laplace 暗星模型）**：
     在牛顿引力场中，质量为 \(m\) 的粒子从半径 \(R\) 处以速度 \(v\) 径向发射，其机械能为 \(E = \frac{1}{2}mv^2 - \frac{GMm}{R}\)。粒子刚好能逃逸至无穷远（\(E = 0\)）所需的逃逸速度为 \(v_{\text{esc}} = \sqrt{\frac{2GM}{R}}\)。
     结合“光速 \(c\) 是宇宙速度上限”，令逃逸速度等于光速 \(v_{\text{esc}} = c\)，解得黑洞半径：
     \[
     \frac{1}{2}mc^2 = \frac{GMm}{R} \implies R = \frac{2GM}{c^2}.
     \]
   - **与广义相对论结果对比及量纲分析论证**：
     该结果与广义相对论史瓦西半径 \(r_S = \frac{2GM}{c^2}\) 在形式上**完全相同**！
     为什么纯牛顿力学（把光当成以速度 \(c\) 运动的经典质点，且忽略时空弯曲）能给出正确的特征尺度？
     **量纲分析（Dimensional Analysis）解释**：对于不带电、不旋转的球对称黑洞，决定其视界尺度的物理量仅有三个——黑洞质量 \(M\)（量纲 \([M]\)）、牛顿引力常数 \(G\)（量纲 \([L^3 M^{-1} T^{-2}]\)）与光速 \(c\)（量纲 \([L T^{-1}]\)）。将这三个量组合出长度量纲 \([L]\) 的**唯一幂次组合**就是：
     \[
     R \propto \frac{G M}{c^2}.
     \]
     因此，任何包含引力常数 \(G\) 与光速极限 \(c\) 的理论，给出的黑洞半径必然正比于 \(\frac{GM}{c^2}\)，差别最多只是一个 \(\mathcal{O}(1)\) 的无量纲常数（在史瓦西径向坐标定义下该常数恰好也是 \(2\)）。

2. **第 2 问（3 分）：基于引力透镜效应与零超曲面性质解释黑洞“阴影（Shadow）”与“光环（Light Ring）”**：
   - **黑洞阴影（Shadow）**：在 \(r = r_S\) 处的事件视界是一个**零超曲面（Null Hypersurface）**，即即便向外径向发射的光线在 \(r = r_S\) 处也只能停留在恒定半径 \(r = r_S\) 上，任何进入 \(r < r_S\) 的光线都将不可逆地落向中心奇点。不仅如此，在 \(r_S\) 外部到光子球半径 \(r_{\text{ph}} = \frac{3}{2}r_S\) 之间，任何指向内侧（或碰撞参数小于临界值 \(b_c = \frac{3\sqrt{3}}{2}r_S \approx 2.6\,r_S\)）的光线也会被强引力弯曲并最终坠入视界，导致远方观测者在视线中心看到一片没有光线逃出的暗区，即“黑洞阴影”。
   - **明亮光环（Light Ring）**：大质量致密天体具有极强的**引力透镜效应（Gravitational Lensing）**，使经过其附近的光线发生剧烈偏折。既然在 \(r = r_S\)（视界）处向外发射的光线停留在原地，而在无穷远处光线沿直线传播，根据连续性，在视界外侧必然存在一个临界球面——**光子球层（Photon Sphere，史瓦西黑洞位于 \(r_{\text{ph}} = \frac{3}{2}r_S\)）**，在此处引力弯曲恰使切向光子做恒定半径 \(r = r_{\text{ph}}\) 的不稳定圆周运动！来自周围炙热吸积盘或背景的辐射一旦以接近临界碰撞参数 \(b \approx b_c\) 掠过光子球层，光线会在逃向地球观测者之前绕黑洞旋转一圈乃至多圈。多圈轨道叠加大大增加了视线穿过发光等离子体的光学路径长度，将来自各个方向的辐射聚焦在阴影边缘，形成极其明亮的“光环”。

3. **第 3 问（3 分）：估算 M87* 阴影尺寸与所需望远镜口径 \(L\)，并讨论 EHT 的地球级干涉阵列**：
   - **第一步：估算 M87* 的史瓦西半径（阴影特征尺寸）**：
     给定 \(M = 6 \cdot 10^9 M_\odot \approx 6 \cdot 10^9 \times 2 \cdot 10^{30}\text{ kg} = 1.2 \cdot 10^{40}\text{ kg}\)，\(G \approx 7 \cdot 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2\)，\(c \approx 3 \cdot 10^8\text{ m/s}\)：
     \[
     r_S = \frac{2GM}{c^2} \approx \frac{2 \times 7 \cdot 10^{-11} \times 1.2 \cdot 10^{40}}{(3 \cdot 10^8)^2} \approx 1.87 \cdot 10^{13}\text{ m} \approx 2 \cdot 10^{13}\text{ m}.
     \]
     （注：黑洞阴影直径约为 \(D_{\text{shadow}} = 2 b_c = 3\sqrt{3} r_S \approx 5.2 r_S \approx 9.7 \cdot 10^{13}\text{ m} \approx 10^{14}\text{ m}\)；数量级估算取 \(r_S\)、\(2r_S\) 或 \(5r_S\) 均可。）
   - **第二步：计算对地球的张角 \(\theta\) 与所需望远镜尺寸 \(L\)**：
     M87* 距离地球 \(d \approx 5 \cdot 10^{22}\text{ m}\)，阴影对应的角尺度为：
     \[
     \theta \sim \frac{r_S}{d} \approx \frac{1.87 \cdot 10^{13}\text{ m}}{5 \cdot 10^{22}\text{ m}} \approx 3.7 \cdot 10^{-10}\text{ rad} \quad \left(\text{若用直径 } 2r_S\text{--}5.2r_S\text{ 则为 } 7.5 \cdot 10^{-10}\text{--}1.9 \cdot 10^{-9}\text{ rad} \approx 15\text{--}40\text{ }\mu\text{as}\right).
     \]
     观测波长 \(\lambda \approx 1\text{ mm} = 10^{-3}\text{ m}\)，由衍射极限分辨率 \(\frac{\lambda}{L} \lesssim \theta\) 得所需望远镜口径：
     \[
     L \gtrsim \frac{\lambda}{\theta} \approx \frac{10^{-3}\text{ m}}{3.7 \cdot 10^{-10}} \approx 2.7 \cdot 10^6\text{ m} = 2700\text{ km} \quad \left(\text{要清晰分辨光环结构需 } L \sim 3 \cdot 10^6\text{--}10^7\text{ m，即数千至上万公里！}\right).
     \]
   - **第三步：结合 EHT 全球望远镜阵列进行讨论**：
     在工程上建造一个直径数千乃至上万公里的单口径射电望远镜是完全不可能的。为此，EHT 合作组采用了**甚长基线干涉测量技术（VLBI）**：将分布在南极、南美洲（智利 ALMA）、北美洲和欧洲的多台毫米波射电望远镜通过原子钟精确同步，利用地球自转进行综合孔径成像。这样一来，望远镜阵列的等效口径 \(L\) 不再受限于单个抛物面天线的直径，而是等于洲际望远镜之间的最大基线长度——即**地球直径（\(D_{\text{Earth}} \approx 1.27 \cdot 10^7\text{ m} \approx 1.3 \cdot 10^4\text{ km}\)）**，其角分辨率达到 \(\frac{\lambda}{D_{\text{Earth}}} \approx 8 \cdot 10^{-11}\text{ rad} \approx 16\text{ }\mu\text{as}\)，刚好达到分辨 M87* 阴影与光环所需的尺度！

4. **第 4 问（2 分）：定量刻画“强场引力区（Strong-field regime）”并与太阳系引力场对比**：
   - **无量纲引力场强度参数 \(\epsilon\)**：
     可以用无量纲化的牛顿引力势（即天体史瓦西半径与特征半径 \(R\) 之比，也称致密性参数 Compactness Parameter）来定量衡量引力场的强弱：
     \[
     \epsilon(R) \equiv \frac{r_S}{R} = \frac{2GM}{c^2 R} = \frac{2|\Phi_N(R)|}{c^2}.
     \]
   - **M87* 视界附近 vs 太阳表面的定量对比**：
     - 在黑洞视界与光子球附近（\(R \sim r_S\)）：
       \[
       \epsilon_{\text{M87*}} \sim \frac{r_S}{r_S} = 1,
       \]
       广义相对论的所有高阶非线性效应与领头阶同量级，处于极端的**强场引力区**。
     - 在太阳系中引力最强的太阳表面（\(M_\odot \approx 2 \cdot 10^{30}\text{ kg} \implies r_{S,\odot} = \frac{2GM_\odot}{c^2} \approx 3.0 \cdot 10^3\text{ m}\)，太阳半径 \(r_\odot \approx 7 \cdot 10^8\text{ m}\)）：
       \[
       \epsilon_\odot = \frac{r_{S,\odot}}{r_\odot} \approx \frac{3.0 \cdot 10^3\text{ m}}{7 \cdot 10^8\text{ m}} \approx 4.3 \cdot 10^{-6} \ll 1.
       \]
       （若在水星轨道 \(a \approx 5.8 \cdot 10^{10}\text{ m}\) 处，更只有 \(\epsilon_{\text{Mercury}} \approx 5 \cdot 10^{-8}\)。）
     因此，黑洞视界附近的无量纲引力场强度比太阳表面强约 **\(2.3 \times 10^5\) 倍**（比水星轨道强约 \(2 \times 10^7\) 倍），使得 EHT 对黑洞阴影的观测成为人类对广义相对论强场区的直接检验。

#### 第二阶段：交叉核验与教学拆解

- **史瓦西度规有效势精确核验**：
  在史瓦西度规 \(ds^2 = -\left(1 - \frac{r_S}{r}\right)c^2 dt^2 + \left(1 - \frac{r_S}{r}\right)^{-1}dr^2 + r^2 d\Omega^2\) 中，零测地线（光子轨道）径向方程为 \(\left(\frac{dr}{d\lambda}\right)^2 + V_{\text{eff}}(r) = \frac{1}{b^2}\)，其中有效势 \(V_{\text{eff}}(r) = \frac{1}{r^2}\left(1 - \frac{r_S}{r}\right)\)。求极值得 \(\frac{dV_{\text{eff}}}{dr} = 0 \implies r_{\text{ph}} = \frac{3}{2}r_S\)，极大值 \(V_{\text{eff}}(r_{\text{ph}}) = \frac{4}{27 r_S^2}\)，故临界碰撞参数（即远方观测者看到的阴影半径）为 \(b_c = \frac{3\sqrt{3}}{2}r_S \approx 2.60\,r_S\)，阴影直径为 \(3\sqrt{3}r_S \approx 5.20\,r_S\)。这为第 2、3 问的物理图像提供了严格的数学支撑。
- **核心难点与易错点**：
  1. **引力势强度 \(\epsilon = \frac{2GM}{c^2 R}\) 与潮汐力/曲率 \(\mathcal{R} \sim \frac{GM}{c^2 R^3}\) 的区分**：超大质量黑洞在视界处的潮汐力 \(\sim \frac{c^2}{r_S^2}\) 反而很小，因此衡量偏离闵可夫斯基平直时空的后牛顿展开参数是无量纲引力势 \(\epsilon = \frac{2GM}{c^2 R}\)。

---

### 9. Solid State Physics (`plancks-2019-final-problem-slice-q9`)

- **物理模型**：各向异性有效质量费米面电子的半经典波包动力学与回旋共振（Cyclotron Resonance）
- **难度评级**：D2
- **教学标签**：`固体物理`、`有效质量张量`、`半经典电子动力学`、`回旋共振频率`、`费米面`

#### 第一阶段：只看原题的独立盲解

给定电子色散关系：
\[
\varepsilon(\mathbf{k}) = \hbar^2\left(\frac{k_x^2 + k_y^2}{m^*} + \frac{k_z^2}{2m^*}\right).
\]

1. **(a)（1 分）点 \(\mathbf{k}_0 = (k_x^0, k_y^0, k_z^0)\) 处的电子群速度矢量 \(\mathbf{v} = \frac{1}{\hbar}\nabla_{\mathbf{k}}\varepsilon(\mathbf{k})\)**：
   对 \(\varepsilon(\mathbf{k})\) 求各分量偏导：
   \[
   v_x = \frac{1}{\hbar}\frac{\partial\varepsilon}{\partial k_x} = \frac{2\hbar k_x^0}{m^*}, \qquad
   v_y = \frac{1}{\hbar}\frac{\partial\varepsilon}{\partial k_y} = \frac{2\hbar k_y^0}{m^*}, \qquad
   v_z = \frac{1}{\hbar}\frac{\partial\varepsilon}{\partial k_z} = \frac{\hbar k_z^0}{m^*}.
   \]
   故速度矢量为：
   \[
   \mathbf{v}(\mathbf{k}_0) = \frac{\hbar}{m^*}\left(2k_x^0,\, 2k_y^0,\, k_z^0\right).
   \]

2. **(b)（2 分）外加电场 \(\mathbf{E} = (E, 0, 0)\) 时电子加速度的方向与大小**：
   电子带电荷 \(q = -e\)（\(e > 0\)），半经典运动方程为 \(\hbar\frac{d\mathbf{k}}{dt} = -e\mathbf{E} = (-eE, 0, 0)\)。
   对群速度 \(\mathbf{v} = \frac{\hbar}{m^*}(2k_x, 2k_y, k_z)\) 求时间导数：
   \[
   \mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{\hbar}{m^*}\left(2\frac{dk_x}{dt},\, 2\frac{dk_y}{dt},\, \frac{dk_z}{dt}\right) = \left(-\frac{2eE}{m^*},\, 0,\, 0\right).
   \]
   - **方向**：沿 \(-x\) 轴方向 \(( -1, 0, 0 )\)（与电场 \(\mathbf{E}\) 反向）；
   - **大小**：\(|\mathbf{a}| = \frac{2e|E|}{m^*}\)。

3. **(c)（2 分）外加电场改为 \(\mathbf{E} = \left(\frac{E}{\sqrt{2}}, 0, \frac{E}{\sqrt{2}}\right)\) 时的加速度方向与大小**：
   由 \(\hbar\frac{d\mathbf{k}}{dt} = -e\mathbf{E} = \left(-\frac{eE}{\sqrt{2}},\, 0,\, -\frac{eE}{\sqrt{2}}\right)\)，代入 \(\mathbf{a} = \frac{d\mathbf{v}}{dt}\)：
   \[
   \mathbf{a} = \frac{1}{m^*}\left(2\hbar\frac{dk_x}{dt},\, 2\hbar\frac{dk_y}{dt},\, \hbar\frac{dk_z}{dt}\right) = -\frac{eE}{\sqrt{2}m^*}\left(2,\, 0,\, 1\right).
   \]
   - **大小**：
     \[
     |\mathbf{a}| = \frac{e|E|}{\sqrt{2}m^*}\sqrt{2^2 + 0^2 + 1^2} = \sqrt{\frac{5}{2}}\,\frac{e|E|}{m^*}.
     \]
   - **方向**：沿单位矢量 \(\hat{\mathbf{a}} = -\frac{1}{\sqrt{5}}(2, 0, 1)\) 方向（在 \(xz\) 平面内，与 \(-x\) 轴夹角为 \(\arctan(1/2) \approx 26.6^\circ\)，由于有效质量各向异性，加速度方向不再与外电场 \(\mathbf{E}\) 共线！）。

4. **(d)（3 分）撤去电场并施加磁场 \(\mathbf{B} = (B, 0, 0)\) 时的波矢演化方程及 \(\omega_1, \omega_2\)**：
   在纯磁场中，电子的半经典洛伦兹力方程为：
   \[
   \hbar\frac{d\mathbf{k}}{dt} = -e(\mathbf{v} \times \mathbf{B}).
   \]
   计算叉乘 \(\mathbf{v} \times \mathbf{B}\)（其中 \(\mathbf{B} = B\hat{\mathbf{x}}\)）：
   \[
   \mathbf{v} \times \mathbf{B} = \left(\frac{2\hbar k_x}{m^*}\hat{\mathbf{x}} + \frac{2\hbar k_y}{m^*}\hat{\mathbf{y}} + \frac{\hbar k_z}{m^*}\hat{\mathbf{z}}\right) \times (B\hat{\mathbf{x}}) = \frac{\hbar B}{m^*}\left(0,\, k_z,\, -2k_y\right).
   \]
   代入 \(\hbar\frac{d\mathbf{k}}{dt} = -e(\mathbf{v} \times \mathbf{B})\) 并约去 \(\hbar\)，得到分量微分方程组：
   \[
   \frac{dk_x}{dt} = 0, \qquad \frac{dk_y}{dt} = -\frac{eB}{m^*}k_z = -\omega_1 k_z, \qquad \frac{dk_z}{dt} = \frac{2eB}{m^*}k_y = \omega_2 k_y
   \]
   （注：题干印刷式将右端变量 \(k_z, k_y\) 误印成了 \(dk_z, dk_y\)，其物理意义显然为线性耦合系数 \(k_z, k_y\)）。因此：
   \[
   \omega_1 = \frac{eB}{m^*}, \qquad \omega_2 = \frac{2eB}{m^*}.
   \]

5. **(e)（2 分）证明电子在垂直于 \(\mathbf{B}\) 的平面内振荡并求振荡频率**：
   - 由 \(\frac{dk_x}{dt} = 0\) 知 \(k_x(t) = k_x^0 = \text{const}\)，故沿磁场 \(\mathbf{B}\)（\(x\) 轴）方向电子做匀速运动（若 \(k_x^0 = 0\) 则静止）。
   - 对 \(\frac{dk_y}{dt} = -\omega_1 k_z\) 两边关于时间 \(t\) 求导，并将 \(\frac{dk_z}{dt} = \omega_2 k_y\) 代入：
     \[
     \frac{d^2 k_y}{dt^2} = -\omega_1 \frac{dk_z}{dt} = -\omega_1 \omega_2 k_y \implies \frac{d^2 k_y}{dt^2} + \omega_c^2 k_y = 0,
     \]
     同理对 \(k_z\) 有 \(\frac{d^2 k_z}{dt^2} + \omega_c^2 k_z = 0\)。
   - 由于实空间速度分量 \(v_y = \frac{d y}{dt} = \frac{2\hbar}{m^*}k_y\)、\(v_z = \frac{d z}{dt} = \frac{\hbar}{m^*}k_z\) 与 \(k_y, k_z\) 成正比，电子在垂直于磁场 \(\mathbf{B}\) 的 \(yz\) 平面内做简谐振荡（椭圆回旋运动），其回旋角频率为：
     \[
     \omega_c = \sqrt{\omega_1 \omega_2} = \sqrt{\left(\frac{eB}{m^*}\right)\left(\frac{2eB}{m^*}\right)} = \frac{\sqrt{2}\,eB}{m^*},
     \]
     对应的振荡频率（线频率）为：
     \[
     f_c = \frac{\omega_c}{2\pi} = \frac{\sqrt{2}\,eB}{2\pi m^*}.
     \]

#### 第二阶段：交叉核验与教学拆解

- **Shockley 回旋有效质量公式独立核验**：
  在固体物理中，磁场沿任意方向（此处沿 \(x\) 轴）时，电子在垂直于磁场的 \(yz\) 平面内的回旋有效质量为 \(m_c = \sqrt{m_{yy} m_{zz}}\)，其中有效质量张量逆矩阵定义为 \((M^{-1})_{ij} = \frac{1}{\hbar^2}\frac{\partial^2 \varepsilon}{\partial k_i \partial k_j}\)。
  对本题色散关系 \(\varepsilon(\mathbf{k}) = \hbar^2\left(\frac{k_x^2 + k_y^2}{m^*} + \frac{k_z^2}{2m^*}\right)\) 求二阶偏导：
  \[
  m_{xx} = m_{yy} = \left(\frac{1}{\hbar^2}\frac{\partial^2\varepsilon}{\partial k_y^2}\right)^{-1} = \frac{m^*}{2}, \qquad m_{zz} = \left(\frac{1}{\hbar^2}\frac{\partial^2\varepsilon}{\partial k_z^2}\right)^{-1} = m^*.
  \]
  因此回旋有效质量为 \(m_c = \sqrt{m_{yy} m_{zz}} = \sqrt{\frac{m^*}{2}\cdot m^*} = \frac{m^*}{\sqrt{2}}\)，回旋角频率为：
  \[
  \omega_c = \frac{eB}{m_c} = \frac{\sqrt{2}\,eB}{m^*},
  \]
  与耦合微分方程解法完全一致！
- **核心难点与易错点**：
  1. **注意题干色散关系中 \(k_x^2 + k_y^2\) 项没有分母 \(2\)**：标准教科书常写 \(\frac{\hbar^2 k^2}{2m^*}\)，而本题故意写成 \(\frac{\hbar^2(k_x^2 + k_y^2)}{m^*} + \frac{\hbar^2 k_z^2}{2m^*}\)。求导时 \(\frac{\partial}{\partial k_x}(k_x^2) = 2k_x\) 会带来因子 \(2\)，千万不要凭习惯漏掉这个 \(2\)！

---

### 10. Freezing Front (`plancks-2019-final-problem-slice-q10`)

- **物理模型**：湖水结冰前沿推进的准稳态热传导模型（Stefan 问题）与熔融钢铁凝固适用性判据
- **难度评级**：D2
- **教学标签**：`热传导`、`Stefan问题`、`相变潜热`、`误差函数展开`、`量纲与无量纲数(Stefan数)`

#### 第一阶段：只看原题的独立盲解

1. **(a)（2 分）液-固相变潜热释放速率**：
   设湖面横截面积为 \(A\)（或取单位面积 \(A = 1\)）。在 \(dt\) 时间内，位于 \(x = X(t)\) 处的结冰前沿向下推进 \(dX\)，结冰的水质量为 \(dm = \rho A dX\)。
   因此单位面积上相变潜热的释放速率（热流密度）为：
   \[
   q_L = \frac{1}{A}\frac{dQ_L}{dt} = \rho L \frac{dX}{dt} \quad \left(\text{对面积 } A \text{ 为 } \frac{dQ_L}{dt} = \rho A L \frac{dX}{dt}\right).
   \]

2. **(b)（2 分）通过冰层的热传导速率**：
   在 \(0 \le x \le X(t)\) 的冰层内，温度分布呈线性，从表面 \(x = 0\) 处的恒定低温 \(T_0\) 线性增加到结冰前沿 \(x = X(t)\) 处的冰点温度 \(T_m\)（\(T_m > T_0\)），故温度梯度为：
   \[
   \frac{\partial T}{\partial x} = \frac{T_m - T_0}{X(t)}.
   \]
   由傅里叶热传导定律，单位面积通过冰层向外传导的热流速率为：
   \[
   q_c = \frac{1}{A}\frac{dQ_c}{dt} = k\frac{T_m - T_0}{X(t)} \quad \left(\text{对面积 } A \text{ 为 } \frac{dQ_c}{dt} = k A \frac{T_m - T_0}{X(t)}\right).
   \]

3. **(c)（3 分）导出结冰前沿位置 \(X(t) = \sqrt{2Kt}\) 及常数 \(K\) 的表达式**：
   结冰前沿释放的潜热必须全部通过冰层传导散失，令 (a) 与 (b) 相等：
   \[
   \rho L \frac{dX}{dt} = k\frac{T_m - T_0}{X(t)} \implies X\frac{dX}{dt} = \frac{k(T_m - T_0)}{\rho L}.
   \]
   结合初始条件 \(X(0) = 0\) 对时间 \(t\) 积分：
   \[
   \int_0^{X(t)} X\,dX = \int_0^t \frac{k(T_m - T_0)}{\rho L}\,dt' \implies \frac{1}{2}X^2(t) = K t \implies X(t) = \sqrt{2 K t},
   \]
   其中常数 \(K\) 为：
   \[
   K = \frac{k(T_m - T_0)}{\rho L}.
   \]

4. **(d)（2 分）对精确解析解超越方程作一阶近似并还原式 (18)**：
   给定精确解 \(X(t) = 2\lambda\sqrt{\alpha t}\)（其中热扩散率 \(\alpha = \frac{k}{\rho c}\)），且 \(\lambda\) 满足超越方程：
   \[
   \lambda e^{\lambda^2}\operatorname{erf}(\lambda) = \frac{c(T_m - T_0)}{L\sqrt{\pi}}, \qquad \operatorname{erf}(\lambda) = \frac{2}{\sqrt{\pi}}\int_0^\lambda e^{-u^2}du.
   \]
   当 \(\lambda \ll 1\) 时，作一阶泰勒近似：
   \[
   e^{\lambda^2} = 1 + \lambda^2 + \cdots \approx 1, \qquad \operatorname{erf}(\lambda) = \frac{2}{\sqrt{\pi}}\left(\lambda - \frac{\lambda^3}{3} + \cdots\right) \approx \frac{2\lambda}{\sqrt{\pi}}.
   \]
   代入超越方程左端保留最低阶（\(\mathcal{O}(\lambda^2)\)）：
   \[
   \lambda \cdot 1 \cdot \left(\frac{2\lambda}{\sqrt{\pi}}\right) = \frac{2\lambda^2}{\sqrt{\pi}} \approx \frac{c(T_m - T_0)}{L\sqrt{\pi}} \implies \lambda^2 \approx \frac{c(T_m - T_0)}{2L}.
   \]
   将 \(\lambda = \sqrt{\frac{c(T_m - T_0)}{2L}}\) 与 \(\alpha = \frac{k}{\rho c}\) 代入 \(X(t) = 2\lambda\sqrt{\alpha t}\)：
   \[
   X(t) = \sqrt{4\lambda^2 \alpha t} \approx \sqrt{4\left[\frac{c(T_m - T_0)}{2L}\right]\left(\frac{k}{\rho c}\right)t} = \sqrt{2\frac{k(T_m - T_0)}{\rho L}t} = \sqrt{2Kt},
   \]
   完美还原了式 (18)！

5. **(e)（1 分）该准稳态线性模型对熔融钢铁（Molten Steel）凝固问题的适用性评估**：
   - **判据分析**：第 (d) 问的一阶近似（即忽略固体层内部降温显热、假设固体层内温度呈线性分布）成立的前提是 \(\lambda^2 \approx \frac{c(T_m - T_0)}{2L} \ll 1\)（无量纲 **Stefan 数** \(\text{Ste} = \frac{c(T_m - T_0)}{L} \ll 1\)，即冷却固体所需的显热远小于相变潜热）。
   - **湖水结冰 vs 钢水凝固的数值对比**：
     - **湖水结冰（Ice）**：\(T_m = 273\text{ K}\)，冬季气温通常仅比冰点低 \(\Delta T = T_m - T_0 \sim 5\text{--}20\text{ K}\)。由题表数据 \(c = 2100\text{ J/(kg}\cdot\text{K)}\)，\(L = 3.3 \cdot 10^5\text{ J/kg}\)，得：
       \[
       \lambda_{\text{ice}}^2 \approx \frac{2100 \times 10}{2 \times 3.3 \cdot 10^5} \approx 0.032 \ll 1,
       \]
       小量近似极好，线性温度分布模型非常适用。
     - **熔融钢铁凝固（Steel）**：熔点高达 \(T_m = 1650\text{ K}\)，若浇铸在室温模具（\(T_0 \approx 300\text{ K}\)）中，温差高达 \(T_m - T_0 \approx 1350\text{ K}\)。由题表数据 \(c = 450\text{ J/(kg}\cdot\text{K)}\)，\(L = 2.7 \cdot 10^5\text{ J/kg}\)，得：
       \[
       \frac{c(T_m - T_0)}{2L} \approx \frac{450 \times 1350}{2 \times 2.7 \cdot 10^5} \approx 1.125 > 1 \quad (\text{Ste}_{\text{steel}} \approx 2.25 \not\ll 1)！
       \]
       此时凝固后的钢壳从 \(1650\text{ K}\) 冷却到 \(300\text{ K}\) 释放的显热 \(c\Delta T \approx 6.1 \cdot 10^5\text{ J/kg}\) 甚至超过了潜热 \(L = 2.7 \cdot 10^5\text{ J/kg}\) 的两倍！\(\lambda \ll 1\) 近似完全失效（线性模型会高估凝固速度），且实际铸造中模具表面温度 \(T_0\) 也会随大量热流注入而显著升高。因此，除非控制环境温度 \(T_0\) 极其接近钢的熔点 \(T_m\)，否则该线性模型作为熔融钢铁凝固的第一近似**并不恰当（需要求解完整的含热容超越方程）**。

#### 第二阶段：交叉核验与教学拆解

- **精确超越方程数值解对比核验**：
  对于钢水凝固（\(\text{Ste} = 2.25\)），精确超越方程为 \(\lambda e^{\lambda^2}\operatorname{erf}(\lambda) = \frac{2.25}{\sqrt{\pi}} \approx 1.269\)。数值求解得精确根为 \(\lambda_{\text{exact}} \approx 0.805\)（\(\lambda_{\text{exact}}^2 \approx 0.648\)），而一阶近似给出 \(\lambda_{\text{approx}}^2 = 1.125\)（\(\lambda_{\text{approx}} \approx 1.061\)），相对误差超过 \(30\%\)！相反，对 \(\Delta T = 10\text{ K}\) 的湖水结冰，\(\lambda_{\text{exact}} \approx 0.177\)，\(\lambda_{\text{approx}} \approx 0.178\)，相对误差不足 \(1\%\)。
- **核心难点与易错点**：
  1. **误差函数 \(\operatorname{erf}(\lambda)\) 的定义与低阶展开**：注意被积函数在 \(u \to 0\) 时 \(e^{-u^2} \approx 1\)，故 \(\int_0^\lambda e^{-u^2}du \approx \lambda\)，千千万万不可漏掉积分前面的归一化系数 \(\frac{2}{\sqrt{\pi}}\)！

---

## Part II: PLANCKS 2020 Final (London)

---

### 11. A Snow Plough Problem (`plancks-2020-final-problem-slice-q1`)

- **物理模型**：恒定降雪率与恒定排雪体积速率下的扫雪车变质量/变厚度运动微分方程模型（Agnew 经典扫雪机微分方程）
- **难度评级**：D1
- **教学标签**：`经典力学`、`常微分方程建模`、`扫雪车问题`、`对数积分`、`黄金分割比`

#### 第一阶段：只看原题的独立盲解

1. **合理的物理假设（Assumptions）**：
   - 降雪从 \(t = -T\)（即早上 06:00 前 \(T\) 小时）开始，且单位面积降雪速率 \(R_S\)（单位 \(\text{m/s}\)）随时间和空间保持恒定，积雪不融化、不被风吹散；
   - 扫雪车从 \(t = 0\)（06:00 am）自 \(x(0) = 0\) 出发沿笔直公路单向行驶，其除雪速率（单位时间清除的积雪体积）\(R_P\)（单位 \(\text{m}^3/\text{s}\)）保持恒定；
   - 铲刀宽度 \(w\) 恒定，且铲刀高度大于积雪厚度 \(h(t)\)，所经之处积雪被完全推除。

2. **(i) \(w, h, R_P, \Delta x, \Delta t\) 之间的关系**：
   在极短时间 \(\Delta t\) 内，扫雪车前进距离 \(\Delta x\)，铲除的积雪体积为 \(\Delta V = w h(t) \Delta x\)。由于扫雪车除雪体积速率恒为 \(R_P\)，故在 \(\Delta t\) 时间内清除的体积满足：
   \[
   w h \Delta x = R_P \Delta t.
   \]

3. **(ii) \(h, R_S, t, T\) 之间的关系**：
   到时刻 \(t\) 为止，雪已经持续下了 \(t + T\) 的时间，故路面积雪厚度（高度）为：
   \[
   h(t) = R_S (t + T).
   \]

4. **求解开始下雪的时间**：
   将 \(h(t) = R_S(t + T)\) 代入 \(w h \Delta x = R_P \Delta t\) 并取极限 \(\Delta t \to 0\)，得到运动微分方程：
   \[
   \frac{dx}{dt} = \frac{R_P}{w R_S}\frac{1}{t + T} = \frac{\alpha}{t + T}, \qquad \alpha \equiv \frac{R_P}{w R_S}.
   \]
   结合初始条件 \(x(0) = 0\) 对时间 \(t\) 积分：
   \[
   x(t) = \int_0^t \frac{\alpha}{t' + T}dt' = \alpha \ln\left(\frac{t + T}{T}\right) = \alpha \ln\left(1 + \frac{t}{T}\right).
   \]
   以小时（\(\text{hr}\)）为时间单位（因 \(t/T\) 无量纲，方程形式对任意时间单位均成立）：
   - 第一小时（\(t \in [0, 1]\)）走过的路程：
     \[
     d_1 = x(1) - x(0) = \alpha \ln\left(\frac{1 + T}{T}\right).
     \]
   - 第二小时（\(t \in [1, 2]\)）走过的路程：
     \[
     d_2 = x(2) - x(1) = \alpha \ln\left(\frac{2 + T}{1 + T}\right).
     \]
   由题意 \(d_2 = \frac{1}{2}d_1\)（等价于前两小时总路程 \(x(2) = d_1 + d_2 = \frac{3}{2}d_1\)）：
   \[
   \ln\left(\frac{2 + T}{1 + T}\right) = \frac{1}{2}\ln\left(\frac{1 + T}{T}\right) \implies \left(\frac{2 + T}{1 + T}\right)^2 = \frac{1 + T}{T}.
   \]
   交叉相乘化简：
   \[
   T(T^2 + 4T + 4) = (T + 1)^3 = T^3 + 3T^2 + 3T + 1 \implies T^2 + T - 1 = 0.
   \]
   取正根（\(T > 0\)）：
   \[
   T = \frac{\sqrt{5} - 1}{2}\text{ hours} \approx 0.618034\text{ hours} = 37\text{ min } 4.9\text{ s} \approx 37\text{ min } 5\text{ s}.
   \]
   从 \(06:00:00\) 往前推 \(37\text{ min } 5\text{ s}\)，得开始下雪的时刻为 **\(05:22:55\text{ am}\)（约 \(05:23\text{ am}\))**。

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q1`）对比**：
  1. **完全一致的核心结果**：我们的微分方程 \(\frac{dx}{dt} = \frac{\alpha}{t+T}\)、积分位移 \(x(t) = \alpha\ln(1 + t/T)\)、黄金分割比 \(T = \frac{\sqrt{5}-1}{2}\text{ hr} \approx 37\text{ min } 5\text{ s}\) 以及下雪时间 \(05:22:55\) 与官方解答完全一致！
  2. **官方解答中的两处笔误指正**：
     - 在官方解答第 2 页式 (2) 中，作者误将 \(h = R_S(t+T)\) 多印了 \(wx\) 写成了 \(h = R_S(t+T)wx\)，但紧接着下一行代入时又自动消去了 \(wx\) 写成正确的 \(R_S(t+T)w\Delta x = R_P\Delta t\)；
     - 在官方解答第 3 页化简 \(\left(1 + \frac{2}{T}\right)^2 = \left(1 + \frac{1}{T}\right)^3\) 时，中间代数方程误印成了 \(T^2 - T - 1 = 0\)，但紧接着求根公式却写成了 \(T = \frac{-1 + \sqrt{5}}{2}\)（这恰是正确方程 \(T^2 + T - 1 = 0\) 的正根！）。我们的盲解推导彻底避免了这两处笔误。
- **核心难点与易错点**：
  1. **时间单位的无量纲不变性**：无须把 \(1\text{ hr}\) 换算成 \(3600\text{ s}\)，因为对数宗量 \(1 + t/T\) 是时间之比，直接令 \(t = 1, 2\) 解出以小时为单位的 \(T\) 最简洁。
  2. **“第二小时路程”与“两小时末总路程”的区分**：第二小时的路程是 \(\Delta x_{1\to 2} = x(2) - x(1)\)，对应 \(x(2) = \frac{3}{2}x(1)\)，切忌误列成 \(x(2) = \frac{1}{2}x(1)\)。

---

### 12. Dotty Dinosaur (`plancks-2020-final-problem-slice-q2`)

- **物理模型**：赠券收集问题（Coupon Collector's Problem）——离散马尔可夫链与几何分布期望可加性模型
- **难度评级**：D1
- **教学标签**：`概率统计`、`赠券收集问题`、`几何分布`、`马尔可夫链递推`、`调和级数`

#### 第一阶段：只看原题的独立盲解

设当前恐龙身上已经收集了 \(k\) 种不同颜色的圆点（\(k \in \{0, 1, 2, 3, 4, 5\}\)）。
- 掷一次均匀六面色子，掷出尚未收集到的新颜色的概率为：
  \[
  p_k = \frac{6 - k}{6}.
  \]
- 从拥有 \(k\) 种颜色到首次获得第 \(k+1\) 种颜色所需的投掷次数 \(n_k\) 服从成功概率为 \(p_k\) 的**几何分布（Geometric Distribution）**：
  \[
  P(n_k = m) = (1 - p_k)^{m-1} p_k \quad (m = 1, 2, 3, \dots).
  \]
- 几何分布随机变量的数学期望为：
  \[
  \langle n_k \rangle = \sum_{m=1}^\infty m (1 - p_k)^{m-1} p_k = \frac{1}{p_k} = \frac{6}{6 - k}.
  \]
- 总投掷次数 \(N_{\text{throws}} = \sum_{k=0}^5 n_k\)。由数学期望的线性可加性，集齐全部 6 种颜色所需的平均投掷次数为：
  \[
  \langle N_{\text{throws}} \rangle = \sum_{k=0}^5 \langle n_k \rangle = \frac{6}{6} + \frac{6}{5} + \frac{6}{4} + \frac{6}{3} + \frac{6}{2} + \frac{6}{1} = 6\left(1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\right) = 6 \times \frac{49}{20} = \frac{147}{10} = 14.7.
  \]

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q2`）对比**：
  - 官方解答采用**全期望公式（一阶马尔可夫状态向后递推法）**：设 \(e_k\) 为已集齐 \(k\) 种颜色后还需投掷的平均次数（边界条件 \(e_6 = 0\)），由下一步转移概率列出线性递推关系：
    \[
    e_k = 1 + \frac{6 - k}{6}e_{k+1} + \frac{k}{6}e_k \implies \frac{6 - k}{6}e_k = 1 + \frac{6 - k}{6}e_{k+1} \implies e_k - e_{k+1} = \frac{6}{6 - k}.
    \]
    累加即得 \(e_0 = \sum_{k=0}^5 \frac{6}{6-k} = 14.7\)，并在末尾指出当种类数 \(N \gg 1\) 时渐近行为 \(E_N = N H_N \sim N \ln N\)。
  - 我们在盲解中使用的“阶段等待时间几何分布分解”与官方的“条件期望递推方程”互为对偶（\(n_k\) 的期望恰为 \(e_k - e_{k+1}\)），两种方法结合讲解能让竞赛生彻底掌握随机过程求期望的核心技巧。
- **核心难点与易错点**：
  1. **状态拆分的独立性**：将整个随机过程按“已收集的不同颜色数 \(k\)”切分为 6 个无记忆阶段 \(0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 6\)，每个阶段都是独立同分布的伯努利试验，从而避开了复杂的无穷步转移矩阵求逆。

---

### 13. Einstein's Story (`plancks-2020-final-problem-slice-q3`)

- **物理模型**：光子钟（Light Clock）思想实验、伽利略绝对时间假设与狭义相对论光速不变原理的时间膨胀推导
- **难度评级**：D1
- **教学标签**：`狭义相对论`、`光子钟思想实验`、`光速不变原理`、`时间膨胀`、`洛伦兹因子`

#### 第一阶段：只看原题的独立盲解

逐一填写题干红框标注的 10 个空缺（编号 1 至 10）：

1. **红框 1（Equation 1）**：在各自静止的实验室参考系中，光脉冲垂直往返高度 \(H\) 的总路程为 \(2H\)，飞行时间为 \(T\)，故光速表达式为：
   \[
   C = \frac{2H}{T}. \qquad \text{(1)}
   \]
2. **红框 2（几何光路草图）**：画出对称的折线（等腰三角形）光路图——光脉冲从左下起点 \(A\) 沿斜向上直线传播至顶部中央平面镜反射，再沿斜向下直线返回右下终点 \(B\)，标注垂直高度 \(H\) 与底部水平位移 \(AB\)。
3. **红框 3**：在另一艘邮轮观测者测得的往返时间 \(T'\) 内，两船以相对速度 \(V\) 运动，相对水平位移 \(AB\) 为：
   \[
   V T'.
   \]
4. **红框 4**：由勾股定理，上升段和下降段斜边长均为 \(\sqrt{H^2 + \left(\frac{VT'}{2}\right)^2}\)，故光脉冲走过的总路程 \(D\) 为：
   \[
   D = 2\sqrt{H^2 + \left(\frac{V T'}{2}\right)^2} = \sqrt{4H^2 + V^2 T'^2}.
   \]
5. **红框 5**：因此，另一艘船上的实验者测得的光速 \(C'\) 定义为路程除以时间：
   \[
   \frac{D}{T'}.
   \]
6. **红框 6（Equation 2）**：将 \(D\) 代入 \(C' = \frac{D}{T'}\)，得：
   \[
   C' = \frac{2\sqrt{H^2 + \left(\frac{V T'}{2}\right)^2}}{T'} = \sqrt{\frac{4H^2}{T'^2} + V^2}. \qquad \text{(2)}
   \]
7. **红框 7（Equation 3）**：若按经典牛顿绝对时间观假设 \(T = T'\)，将式 (1) \(\frac{2H}{T} = C\) 代入式 (2)，得：
   \[
   C' = \sqrt{C^2 + V^2}. \qquad \text{(3)}
   \]
8. **红框 8**：根据爱因斯坦 1905 年狭义相对论的光速不变原理，两个惯性系测得的光速必然相等，即 \(C = \mathbf{C'}\)。
9. **红框 9**：两位实验者转而采纳爱因斯坦的假设：
   \[
   C = C'.
   \]
10. **红框 10（Equation 4）**：令 \(C = C'\) 并联立式 (1)（\(2H = C T\)）与式 (2)（\(C^2 T'^2 = 4H^2 + V^2 T'^2 = C^2 T^2 + V^2 T'^2\)），解出运动时钟的时间膨胀公式：
    \[
    T' = \frac{T}{\sqrt{1 - \frac{V^2}{C^2}}}. \qquad \text{(4)}
    \]

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q3`）对比**：
  我们盲解给出的 10 个编号答案（公式与草图）与官方标准答案第 4 页的 `Numbered Answers` 列表完全吻合！
- **核心难点与易错点**：
  1. **固有时 \(T\) 与坐标时 \(T'\) 的物理区分**：在光钟静止系中，发光与接收发生在**同一空间地点**，故 \(T\) 是**固有时（Proper Time）**；而在相对运动的观测者看来，发光点 \(A\) 与接收点 \(B\) 位于不同空间位置，所测得的 \(T' = \gamma T > T\) 是膨胀后的坐标时（“运动的钟变慢”）。

---

### 14. Time of Flight (`plancks-2020-final-problem-slice-q4`)

- **物理模型**：半导体瞬态飞行时间法（Transient ToF）测量载流子迁移率、双对数拐点判读与缺陷陷阱色散输运
- **难度评级**：D2
- **教学标签**：`半导体物理`、`载流子迁移率`、`飞行时间法(ToF)`、`误差传递`、`陷阱态与色散输运`

#### 第一阶段：只看原题的独立盲解

1. **(a)（2 分）从图 2（双对数光电流-时间图）确定渡越时间 \(t_{\text{tr}}\) 的位置及理由**：
   - **位置**：位于双对数曲线中前段平缓区（近似平台/缓降直线）与后段陡降区（快速幂律衰减直线）相交的**拐点（"Knee" / Inflection point，对应横坐标约 \(t_{\text{tr}} \approx 2.5\text{ }\mu\text{s}\)）**。
   - **理由**：脉冲激光在入射电极附近产生薄层载流子包后，载流子包在恒定外加电场驱动下以近似恒定的漂移速度穿过样品体区，此时光电流维持在较高的近恒定平台值；当载流子包的主体（前锋）到达对侧电极（Al）并被收集抽出时，体内可移动载流子数目骤减，导致光电流在 \(t = t_{\text{tr}}\) 处发生急剧转折下降。

2. **(b)（2 分）由图 3 计算载流子迁移率 \(\mu\) 及其不确定度**：
   由迁移率公式 \(\mu = \frac{d^2}{V t_{\text{tr}}}\)，得线性关系：
   \[
   t_{\text{tr}}^{-1} = \frac{\mu}{d^2} V = m V, \qquad \mu = m d^2,
   \]
   其中 \(m\) 为图 3（\(t_{\text{tr}}^{-1}\) 对外加偏压 \(V\)）拟合直线的斜率。
   - 从图 3 读取斜率 \(m\)：拟合直线经过 \((V_1, y_1) \approx (5\text{ V}, 0.35)\) 与 \((V_2, y_2) \approx (30\text{ V}, 3.22)\)，图面数值斜率为：
     \[
     m_{\text{num}} = \frac{\Delta y}{\Delta V} \approx \frac{3.22 - 0.35}{30 - 5} \approx 0.115\text{ V}^{-1} \quad (\text{若过原点附近取斜率约为 } 0.105\text{--}0.116\text{ V}^{-1}).
     \]
   - 注意图 3 纵轴单位标注为 \(t_{\text{Transit}}^{-1}\ (10^{-5}\text{ s}^{-1})\)：
     - **物理实际单位（\(t_{\text{tr}} \sim \mu\text{s} \implies t_{\text{tr}}^{-1} \sim 10^5\text{ s}^{-1}\)，纵轴标题中的 \(10^{-5}\) 表示坐标数值 \(= t_{\text{tr}}^{-1} \times 10^{-5}\text{ s}\)）**：
       此时 \(m \approx 1.15 \times 10^4\text{ V}^{-1}\text{s}^{-1}\)，样品厚度 \(d = 1.33 \pm 0.07\text{ }\mu\text{m} = (1.33 \pm 0.07)\times 10^{-4}\text{ cm}\)，\(d^2 = 1.769 \times 10^{-8}\text{ cm}^2 = 1.769 \times 10^{-12}\text{ m}^2\)：
       \[
       \mu = m d^2 \approx 1.15 \times 10^4 \times 1.769 \times 10^{-8}\text{ cm}^2\text{V}^{-1}\text{s}^{-1} \approx (2.0 \pm 0.2) \times 10^{-4}\text{ cm}^2\text{V}^{-1}\text{s}^{-1} = (2.0 \pm 0.2) \times 10^{-8}\text{ m}^2\text{V}^{-1}\text{s}^{-1},
       \]
       其中相对误差主要由厚度平方决定：\(\frac{\Delta\mu}{\mu} \approx 2\frac{\Delta d}{d} = 2\times\frac{0.07}{1.33} \approx 10.5\%\)。
     - （注：若在计算时漏将 \(d = 1.33\text{ }\mu\text{m}\) 换算为 \(\text{cm}\) 而直接用 \(1.33^2 \approx 1.77\) 乘以 \(1.15 \times 10^4\)，则会得到数值 \((2.05 \pm 0.14) \times 10^4\)——我们在第二阶段将会看到这正是官方参考答案所犯的单位换算笔误！）

3. **(c)（2 分）所测载流子的种类及相反电荷载流子的去向**：
   - **所测载流子**：由图 1 可见，外加电场 \(\vec{E}\) 方向从左（ITO 透明电极，正极）指向右（Al 电极，负极），而光生载流子包顺着电场 \(\vec{E}\) 的方向向 Al 电极漂移；同时图 3 横轴外加偏压为正值，说明测得的是带正电的**空穴（Holes）**（注：初期光激发首先形成束缚电子-空穴对即**激子 Exciton**，随后在外加电场下解离）。
   - **相反电荷（电子）的去向**：带负电的**电子（Electrons）**逆着电场 \(\vec{E}\) 方向运动，由于激光在紧贴入射端 ITO 电极处激发，电子诞生后立即被近旁的 ITO 正电极吸收抽取。

4. **(d)（1 分）体内载流子陷阱（Trap）的物理实例**：
   半导体体内的化学杂质原子（掺杂剂/氧或水分子污染）、晶格结构缺陷（空位、位错、晶界、悬挂键）或有机半导体中位于导带底（LUMO）下方/价带顶（HOMO）上方的局域态能级（电子陷阱或空穴陷阱）。

5. **(e)（2 分）陷阱捕获对载流子包及图 2 曲线的影响**：
   - **对载流子包的影响**：部分载流子在渡越途中被陷阱随机捕获并延迟释放，导致原本紧凑同步运动的载流子包发生严重的**空间展宽与弥散（Dispersive transport）**，不再作为一个整体同时到达对侧电极，且复合损耗增加。
   - **对图 2 的影响**：由于载流子到达电极的时间高度分散，图 2 中原本清晰的平台与陡降之间的**拐点（Knee）将被抹平/模糊化**，整体曲线向下弯曲且拖出更长的慢衰减尾。

6. **(f)（1 分）不加外置偏压（\(V = 0\)）时图 2 的形态及原因**：
   由于两侧电极材料不同（ITO 功函数约 \(4.7\text{ eV}\)，Al 功函数约 \(4.1\text{ eV}\)），器件内部天然存在由电极功函数差引起的**内建电场（Built-in potential / bias）**！因此即使外加偏压为零，内建电场仍会驱动光生载流子定向漂移穿过样品，图 2 **依然会呈现出具有清晰渡越时间拐点（Knee）的相似曲线形状**，只是由于有效驱动电压较小，光电流幅值会降低且渡越时间变长。（若假设理想对称无内建电场，则只剩扩散与复合，无漂移渡越拐点。）

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q4`）对比**：
  1. **(a)、(c)、(d)、(e)、(f) 完全吻合**：特别是第 (f) 问，许多学生会以为“不加外电压就没有电流”，而官方解答明确指出：“由于 ITO 与 Al 两种电极材料的功函数不同，存在内建偏压（built-in bias），因此图 2 仍能看到清晰的渡越时间且曲线形状不变，只是电流幅值减小”！
  2. **官方解答第 (b) 问的单位换算笔误剖析**：
     官方解答写有：\(\mu = m d^2 = 2.05 \pm 0.14 \times 10^4\text{ cm}^2\text{V}^{-1}\text{s}^{-1}\)。复盘其算式可以发现：出题人读取斜率 \(m \approx 1.156 \times 10^4\text{ V}^{-1}\text{s}^{-1}\)，然后直接乘以了 \(d^2 = 1.33^2 = 1.7689\)（即 \(1.156 \times 10^4 \times 1.769 = 2.05 \times 10^4\)），忘记把 \(d = 1.33\text{ }\mu\text{m}\) 换算成 \(1.33 \times 10^{-4}\text{ cm}\)（平方后相差 \(10^{-8}\) 倍）！好在官方评分标准特别注明了“Only the order of magnitude matters... If there are no units or error do not award a mark”。在我们的讲义中同时给出正确的物理量级 \(2.05 \times 10^{-4}\text{ cm}^2\text{V}^{-1}\text{s}^{-1}\) 与未换算微米的数值，能帮助学生养成严谨的单位核查习惯。
- **核心难点与易错点**：
  1. **双对数图（Log-Log Plot）在色散输运中的物理意义**：在非晶或有机半导体（Scher-Montroll 理论）中，电流在 \(t < t_{\text{tr}}\) 时满足 \(I(t) \propto t^{-(1-\alpha)}\)，在 \(t > t_{\text{tr}}\) 时满足 \(I(t) \propto t^{-(1+\alpha)}\)。在线性坐标下很难看清转折点，但取双对数后两段幂律变成斜率分别为 \(-(1-\alpha)\) 与 \(-(1+\alpha)\) 的两条直线，交点即为渡越时间 \(t_{\text{tr}}\)！
  2. **异质电极器件的内建电场**：ITO/有机层/Al 结构本质上是一个肖特基/MIM 二极管，零外偏压下功函数差 \(\Delta W / e \sim 0.6\text{ V}\) 依然维持着非零内建电场。

---

### 15. Phonon-assisted Charge Transport in 2D (`plancks-2020-final-problem-slice-q5`)

- **物理模型**：二维晶格声子辅助电荷隧穿的费米黄金定则（Fermi's Golden Rule）与无穷二维电阻网络（方格与蜂窝晶格）叠加定理模型
- **难度评级**：D3
- **教学标签**：`固体物理`、`费米黄金定则`、`二维态密度`、`声子辅助跃迁`、`无穷电阻网络`

#### 第一阶段：只看原题的独立盲解

1. **(a)（5 分）利用费米黄金定则计算相邻格点 A、B 间的跃迁电阻 \(R\)**：
   系统哈密顿量为：
   \[
   H = \frac{qU}{2}\bigl(|A\rangle\langle A| - |B\rangle\langle B|\bigr) + \hbar v \sum_{\vec{k}} |\vec{k}| n_{\vec{k}} + g\sum_{\vec{k}}\left(c_{\vec{k}}^\dagger |B\rangle\langle A| + c_{\vec{k}}|A\rangle\langle B|\right).
   \]
   - **初末态与跃迁矩阵元**：
     初态电荷在格点 A 且声子库为空（零温），即 \(|\psi_i\rangle = |A, 0\rangle\)，初态能量 \(E_i = +\frac{qU}{2}\)；
     末态电荷跃迁至格点 B 同时发射一个波矢为 \(\vec{k}\) 的声子，即 \(|\psi_f(\vec{k})\rangle = |B, 1_{\vec{k}}\rangle\)，末态能量 \(E_f(\vec{k}) = -\frac{qU}{2} + \hbar v k\)（其中 \(k = |\vec{k}|\)）。
     微扰哈密顿量 \(H_{\text{int}} = g\sum_{\vec{k}}\left(c_{\vec{k}}^\dagger |B\rangle\langle A| + c_{\vec{k}}|A\rangle\langle B|\right)\) 的跃迁矩阵元为：
     \[
     \langle B, 1_{\vec{k}} | H_{\text{int}} | A, 0 \rangle = g.
     \]
   - **二维声子态密度（DOS）与费米黄金定则**：
     由费米黄金定则，从 A 到 B 的总跃迁速率为：
     \[
     \Gamma_{A\to B} = \frac{2\pi}{\hbar}\sum_{\vec{k}}\bigl|\langle B, 1_{\vec{k}} | H_{\text{int}} | A, 0 \rangle\bigr|^2 \delta(E_f(\vec{k}) - E_i) = \frac{2\pi}{\hbar} g^2 \rho(\epsilon = qU),
     \]
     其中二维声子态密度 \(\rho(\epsilon)\) 由面积为 \(S\) 的二维晶体玻恩-冯·卡门周期边界条件（或硬壁边界条件）给出：
     \[
     \sum_{\vec{k}} \longrightarrow \frac{S}{(2\pi)^2}\int_0^\infty 2\pi k\,dk = \frac{S}{2\pi}\int_0^\infty k\,dk.
     \]
     由于声子色散关系为 \(\epsilon = \hbar v k\)（\(dk = \frac{d\epsilon}{\hbar v}\)），能量态密度为：
     \[
     \rho(\epsilon) = \frac{S}{2\pi} k \frac{dk}{d\epsilon} = \frac{S \epsilon}{2\pi \hbar^2 v^2}.
     \]
     代入 \(\epsilon = qU\)，得跃迁速率：
     \[
     \Gamma_{A\to B} = \frac{2\pi}{\hbar} g^2 \left(\frac{S q U}{2\pi \hbar^2 v^2}\right) = \frac{g^2 S q U}{\hbar^3 v^2}.
     \]
   - **电流与单键电阻 \(R\)**：
     由于声子库初始为空，逆向过程（吸收声子从 B 到 A）速率为零，故净电流为：
     \[
     I = q \Gamma_{A\to B} = \frac{q^2 g^2 S}{\hbar^3 v^2} U.
     \]
     由欧姆定律 \(R = \frac{U}{I}\)，得相邻两格点间的单键电阻为：
     \[
     R = \frac{\hbar^3 v^2}{q^2 g^2 S}.
     \]

2. **(b)（3 分）无穷大二维正方晶格（Square Lattice）相邻格点 A、B 间的等效电阻 \(R_{AB}\)**：
   当样品面积远大于原胞面积且边界电流为零时，系统等效为无穷大二维正方网格，每条边均为阻值 \(R\) 的电阻。利用**线性叠加原理与晶格旋转对称性**：
   - **情形 I**：从节点 A 注入电流 \(I\)，并在无穷远处均匀流出。由正方晶格节点的四重旋转对称性（配位数 \(z = 4\)），从 A 出发的 4 条相邻边各分得电流 \(\frac{I}{4}\)，因此边 \(AB\) 上从 A 流向 B 的电流为 \(I_1 = \frac{I}{4}\)。
   - **情形 II**：从无穷远处均匀流入电流 \(I\)，并从节点 B 抽出电流 \(I\)。由对称性，汇入节点 B 的 4 条相邻边各承载电流 \(\frac{I}{4}\)，因此边 \(AB\) 上从 A 流向 B 的电流也为 \(I_2 = \frac{I}{4}\)。
   - **叠加**：将情形 I 与情形 II 叠加，无穷远处净电流抵消为零，此时总电流 \(I\) 从 A 注入并从 B 流出，而直接流经边 \(AB\) 电阻 \(R\) 的电流为：
     \[
     I_{AB} = I_1 + I_2 = \frac{I}{4} + \frac{I}{4} = \frac{I}{2}.
     \]
     于是 A、B 两点间的电势差为 \(U_{AB} = I_{AB} R = \frac{1}{2} I R\)，等效电阻为：
     \[
     R_{AB}^{\text{square}} = \frac{U_{AB}}{I} = \frac{R}{2} = \frac{\hbar^3 v^2}{2 q^2 g^2 S}.
     \]

3. **(c)（2 分）六角蜂窝晶格（Honeycomb Lattice）相邻格点间的等效电阻**：
   在蜂窝晶格（图 4）中，每个格点有 \(z = 3\) 条等价的最近邻键（互成 \(120^\circ\) 三重旋转对称）。
   重复上述叠加定理分析：单独向 A 注入电流 \(I\) 时，沿键 \(AB\) 流出的电流为 \(\frac{I}{3}\)；单独从 B 抽出电流 \(I\) 时，沿键 \(AB\) 流入 B 的电流也为 \(\frac{I}{3}\)。叠加后流经键 \(AB\) 电阻 \(R\) 的电流为：
   \[
   I_{AB} = \frac{I}{3} + \frac{I}{3} = \frac{2}{3}I.
   \]
   因此蜂窝晶格相邻格点间的等效电阻为：
   \[
   R_{AB}^{\text{honeycomb}} = \frac{U_{AB}}{I} = \frac{2}{3}R = \frac{2 \hbar^3 v^2}{3 q^2 g^2 S}.
   \]
   （推广：对任意配位数为 \(z\)、每条边等价的无穷晶格，相邻节点等效电阻恒为 \(R_{AB} = \frac{2}{z}R\)！）

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q5`）对比**：
  对照官方手写解答扫描页（`page-14.jpg`），我们的推导与官方解答在每一处细节上都 100% 重合：
  - 第 (a) 问中，官方解答采用硬壁边界条件 \(k_{x,y} = \frac{\pi}{L_{x,y}}n\) 在第一象限（\(\frac{1}{4}\) 圆环面积 \(\frac{2\pi k\,dk}{4}\)）计算态密度，得到 \(\rho(k)dk = \frac{S k\,dk}{2\pi}\)，与我们采用的周期性边界条件（全圆环面积 \(2\pi k\,dk\) 除以 \(\frac{(2\pi)^2}{L_x L_y}\)）给出的态密度 \(\rho(\epsilon) = \frac{\epsilon S}{2\pi (\hbar v)^2}\) 完全相同；
  - 第 (b)、(c) 问中，官方解答还将除 \(AB\) 外的其余无穷网格等效为一个并联电阻 \(R'\)，由基尔霍夫电压定律 \(R' (I - I_{AB}) - R I_{AB} = 0\) 算出方格网 \(R' = R\)、蜂窝网 \(R' = 2R\)，再并联得 \(R/2\) 与 \(2R/3\)。直接用 \(U_{AB} = I_{AB} R\) 甚至连 \(R'\) 都不必引入，一步即得结果。
- **核心难点与易错点**：
  1. **为什么欧姆定律 \(I \propto U\) 在此量子跃迁模型中成立？** 这是因为二维线性声子色散 \(\epsilon = \hbar v k\) 的态密度恰巧正比于能量一次方 \(\rho(\epsilon) \propto \epsilon\)！当跃迁释放的能量 \(\epsilon = qU\) 时，可用声子末态数目正比于电压 \(U\)，从而使黄金定则跃迁率 \(\Gamma \propto \rho(qU) \propto U\)，自然导出线性欧姆电阻！（若在三维晶格中，声子态密度 \(\rho_{\text{3D}}(\epsilon) \propto \epsilon^2\)，则零温下 \(I \propto U^2\)，将呈现非线性伏安特性！）
  2. **蜂窝晶格非复式布拉伐格子但键对称性仍成立**：虽然蜂窝晶格包含两个子晶格 A 和 B（非简单布拉伐格子），但由于点群对称性保证了每个顶点引出的 3 条键完全等价，叠加定理与三等分电流依然严格适用。

---

### 16. Newcomen's Beam Engine (`plancks-2020-final-problem-slice-q6`)

- **物理模型**：纽科门大气式梁式蒸汽机（Newcomen Atmospheric Engine）的力矩平衡、流体静力载荷与单循环抽水体积模型
- **难度评级**：D2
- **教学标签**：`热机与流体力学`、`纽科门蒸汽机`、`大气压强做功`、`流体静力学平衡`、`工程物理建模`

#### 第一阶段：只看原题的独立盲解

1. **核心物理模型与假设列表（Assumptions）**：
   - **冷凝真空假设**：冷水喷雾注入汽缸 C 后，水蒸气完全冷凝，汽缸内形成接近理想的真空（\(P_{\text{cyl}} \approx 0\)），而喷入的冷水体积可忽略不计；
   - **准静态/匀速运动与无摩擦假设**：横梁 B 关于中点对称铰接（左右力臂相等），忽略汽缸 C、抽水管 T 内的活塞滑动摩擦以及水流经单向阀 \(V_1, V_2\) 的粘滞阻力；
   - **液体不可压缩与管路充满假设**：水不可压缩（密度 \(\rho_w = 1000\text{ kg/m}^3\)），经过初始几次循环充水（priming）后，抽水管 T 内已完全充满水，单向阀 \(V_1, V_2\) 开闭瞬时且无泄漏。

2. **动力学可行性检验（Force / Torque Balance Check）**：
   为什么题目除了给出抽水管直径 \(d = 0.3\text{ m}\) 和冲程 \(\text{Str} = 2\text{ m}\) 外，还给出了蒸汽缸直径 \(D = 0.8\text{ m}\)、大气压 \(P_{\text{atm}} = 0.1\text{ MPa}\)、矿井深度 \(H = 50\text{ m}\) 和抽水杆超重 \(\text{ExMass} = 1200\text{ kg}\)？因为必须首先检验**大气压驱动力是否足以克服水柱重力和抽水杆超重**！
   - **工作冲程（PR 上升、P 下降）**：
     - 右侧蒸汽缸绿色活塞 P 受到的大气向下推力：
       \[
       F_{\text{atm}} = P_{\text{atm}} \left(\frac{\pi}{4}D^2\right) = 1.0 \times 10^5\text{ Pa} \times \frac{\pi}{4}(0.8\text{ m})^2 \approx 50,265\text{ N}.
       \]
     - 左侧红色抽水活塞在集水坑液面以下深度 \(h\)（\(0 \le h \le \text{Str}\)）处向上运动时，阀门 \(V_2\) 关闭、\(V_1\) 打开。活塞上方水柱高 \(H + h\)，对活塞顶面施加向下压力 \(\rho_w g (H + h) A_T\)；同时集水坑水体对活塞底面施加向上浮力/静水压力 \(\rho_w g h A_T\)。两者相抵后，水柱对活塞的净向下负载力恒为（与深度 \(h\) 无关！）：
       \[
       F_{\text{water}} = \rho_w g H \left(\frac{\pi}{4}d^2\right) = 1000 \times 9.81 \times 50 \times \frac{\pi}{4}(0.3)^2 \approx 34,671\text{ N}.
       \]
       （若不扣除底部集水坑静水托力、按总长 \(H + \text{Str} = 52\text{ m}\) 计算，水柱重量为 \(36,058\text{ N}\)。）
     - 加上左侧抽水杆 PR 相对右侧活塞杆 P 的超重负载：
       \[
       W_{\text{ex}} = \text{ExMass} \cdot g = 1200 \times 9.81 = 11,772\text{ N}.
       \]
     - 左侧总向下负载力为：
       \[
       F_{\text{left}} = F_{\text{water}} + W_{\text{ex}} = 34,671 + 11,772 = 46,443\text{ N} \quad (\text{若计 } H+\text{Str}\text{ 则为 } 47,830\text{ N}).
       \]
     - 对比左右两侧力：
       \[
       F_{\text{atm}} \approx 50,265\text{ N} > F_{\text{left}} \approx 46,443\text{ N}\ (47,830\text{ N})！
       \]
       右侧大气推力大于左侧总负载，横梁顺时针转动，成功拉起抽水杆与水柱！
   - **复位冲程（PR 下降、P 上升）**：
     打开蒸汽阀 S 放入常压蒸汽后，汽缸 C 内外压强均为 \(P_{\text{atm}}\)，绿色活塞净气压为零；此时阀门 \(V_1\) 关闭、\(V_2\) 打开，左侧抽水杆依靠其超重 \(W_{\text{ex}} = 11,772\text{ N} > 0\) 自动克服浮力与阻力下沉到底部，完成循环！

3. **单循环抽水体积计算**：
   在单次工作冲程中，直径 \(d = 0.3\text{ m}\) 的抽水活塞上升一个冲程 \(\text{Str} = 2\text{ m}\)，从管顶溢出的水体积等于活塞扫过的圆柱体积：
   \[
   V_{\text{cycle}} = A_T \times \text{Str} = \frac{\pi}{4}d^2 \times \text{Str} = \frac{\pi}{4}(0.3\text{ m})^2 \times 2\text{ m} = 0.045\pi\text{ m}^3 \approx 0.1414\text{ m}^3 \approx 141\text{ L}.
   \]

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q6`）对比**：
  官方解答的评分细则（共 10 分）印证了我们在盲解中的判断：
  - 若考生只写出 \(V = \text{Str} \times \frac{\pi}{4}d^2 = 0.141\text{ m}^3\)，仅能得 1 分（结果分）！
  - 其余 9 分全部奖励给对蒸汽机工作循环的物理力学分析：计算右侧大气压向下推力 \(50,265\text{ N}\)（1 分）、计算左侧水柱加超重负载 \(47,830\text{ N}\)（1 分）、指出两力不平衡产生力矩使横梁加速/稳态转动（2 分）、证明活塞在集水坑液面下深度 \(h\) 变化时上下静水压力抵消使净水柱负载 \(\rho_w g H A\) 保持恒定（1 分）、分析复位冲程靠超重下沉（1 分）以及列出无摩擦、喷水量可忽略等合理假设（3 分）。
- **核心难点与易错点**：
  1. **开放式工程建模题的得分策略**：在 PLANCKS 等英国风格物理竞赛中，当题干给出了看似“多余”的参数（如 \(D, P_{\text{atm}}, H, \text{ExMass}\)）并提示“your answer will depend upon the assumptions that you make”时，绝不能只代一个几何体积公式了事，必须用给定的力学参数完成整个工作循环的**力平衡/能量自洽性论证**！
  2. **水下活塞的阿基米德浮力抵消**：当抽水活塞位于集水坑水面以下深度 \(h\) 时，活塞底面受到的压强为 \(P_{\text{atm}} + \rho_w g h\)，顶面受到的压强为 \(P_{\text{atm}} + \rho_w g (H + h)\)，压差恒为 \(\Delta P = \rho_w g H\)，与活塞在冲程中的瞬时位置 \(h\) 无关。

---

### 17. 1888 (`plancks-2020-final-problem-slice-q7`)

- **物理模型**：1888 年悉尼大学大一物理数学试卷十问（天体轨道、阿基米德浮力、气体实验定律、水银气压计、雷电与避雷针、蒸汽机、电解、磁化、照相机光谱响应与含参高斯积分）
- **难度评级**：D2
- **教学标签**：`经典物理综合`、`阿基米德原理`、`气体定律与热机`、`电磁学基础`、`含参高斯积分`

#### 第一阶段：只看原题的独立盲解

1. **(a)（1 分）为什么月球不会掉到地球上？**
   月球时刻受到指向地球中心的万有引力并处于持续向地球“自由下落”的状态；但月球同时具有很大的切向轨道速度（\(v \approx 1.0\text{ km/s}\)），地球引力恰好提供其做近圆周运动所需的向心力 \(\frac{GM_E m}{r^2} = \frac{mv^2}{r}\)，使其下落轨迹的曲率半径等于轨道半径，从而永远绕地球公转而不会撞击地面。

2. **(b)（1 分）阿基米德排水体积实验及其在测定比重（Specific Gravity）中的应用**：
   - **著名实验**：为检验叙拉古国王希罗（Hiero）的王冠是否为纯金，阿基米德将王冠与等质量的纯金分别浸入装满水的容器中，通过测量溢出水的体积发现王冠排开水的体积更大（密度更小，掺了银），从而创立了**阿基米德原理**——浸在流体中的物体受到向上的浮力，其大小等于物体所排开流体的重力 \(F_b = \rho_{\text{fluid}} g V\)。
   - **测定比重的方法**：先在空气中称出物体的重力 \(W_{\text{air}} = \rho_{\text{body}} g V\)，再将其完全浸没在纯水中称得视重 \(W_{\text{water}} = W_{\text{air}} - F_b\)。两次读数之差即为同体积水的重力 \(F_b = \rho_{\text{water}} g V = W_{\text{air}} - W_{\text{water}}\)，故物体的比重（相对密度）为：
     \[
     \text{SG} = \frac{\rho_{\text{body}}}{\rho_{\text{water}}} = \frac{W_{\text{air}}}{W_{\text{air}} - W_{\text{water}}}.
     \]

3. **(c)（1 分）密闭空气升温与等温加压的物理效应**：
   - **(i) 升高密闭容器内一定体积空气的温度（定容过程）**：根据查理定律/盖-吕萨克定律（\(P \propto T\)），气体分子的平均平动动能 \(\frac{3}{2}k_B T\) 增大，分子热运动速率增大，单位时间内撞击器壁的频率和单次碰撞动量传递均增加，导致容器内**气体压强随绝对温度成正比升高**（若容器可自由膨胀保持定压，则体积随绝对温度成正比增大 \(V \propto T\)）。
   - **(ii) 保持温度恒定而增大压强（等温过程）**：根据波义耳定律（Boyle's Law，\(PV = \text{const}\)），温度不变时分子平均动能不变，增大外加压强会使**气体体积与压强成反比缩小**（\(V \propto 1/P\)），气体数密度与质量密度同比例增大。

4. **(d)（1 分）如何制作气压计（Barometer）及其测量对象**：
   - **制作步骤（托里拆利水银气压计）**：取一根长约 \(1\text{ m}\)（约 36 英寸）、一端封闭的玻璃管，灌满纯水银并排尽所有气泡；堵住管口将其倒置插入盛有水银的敞口水银槽中，在液面下松开管口，管内水银柱自然下降至距槽内液面约 \(760\text{ mm}\) 高处，管顶留出托里拆利真空区，在管壁附上刻度尺即成。
   - **测量对象**：测量当地的**大气压强**（\(P_{\text{atm}} = \rho_{\text{Hg}} g h\)，也可据此推算海拔高度与天气变化）。

5. **(e)（1 分）雷电现象的解释与避雷针的作用**：
   - **雷电成因**：积雨云中剧烈的上升暖湿气流与下沉冰晶/霰粒碰撞摩擦，发生电荷分离（通常云层上部积聚正电荷，下部积聚负电荷），并在地面感应出正电荷。当云地之间或云层之间的电场强度超过空气的介电击穿场强（或由相对论逃逸电子雪崩激发导电通道）时，发生剧烈的火花放电，伴随强光（闪电）与通道空气急剧受热膨胀产生的冲击波（雷鸣）。
   - **避雷针的作用**：安装在建筑物顶端的金属杆通过粗导线与大地相连，在雷击发生时提供一条**极低电阻的安全泄流通道**，将巨大的雷电流直接导入大地（同时尖端放电也有助于局部中和电荷），从而保护建筑物免受雷击焚毁或结构损坏。

6. **(f)（1 分）普通往复式蒸汽机的工作部件与运行原理图解**：
   - **核心部件**：锅炉（Boiler）、进汽室与滑阀（Slide valve）、汽缸（Cylinder）、活塞与活塞杆（Piston & rod）、十字头与连杆（Crosshead & connecting rod）、曲柄（Crank）、飞轮（Flywheel）及冷凝器/排汽口。
   - **工作原理**：锅炉产生的高压水蒸气经滑阀交替进入汽缸活塞的左、右两侧，推动活塞做往复直线运动（同时另一侧的乏汽通过滑阀排入大气或冷凝器）；滑阀由曲轴上的偏心轮联动控制自动换向，连杆与曲柄机构将活塞的往复运动转化为飞轮的连续旋转机械功。

7. **(g)（1 分）电解（Electrolysis）的定义、实例与能量转化**：
   - **定义**：将直流电通过电解质溶液或熔融电解质，在正负电极上引发氧化还原反应从而使化合物分解的过程。
   - **简单实例**：电解水（\(2\text{H}_2\text{O} \xrightarrow{\text{通电}} 2\text{H}_2\uparrow + \text{O}_2\uparrow\)，阴极 \(\text{H}^+\) 得电子还原生成氢气，阳极 \(\text{OH}^-\)/水失电子氧化生成氧气；或电解硫酸铜溶液、熔融氯化钠）。
   - **系统能量状态变化**：外部电源输入的**电能**一部分转化为分解产物的**化学能（化学势能）**，另一部分因电解液内阻产生焦耳热而转化为系统的**热能（内能）**。

8. **(h)（1 分）什么是磁铁？如何制作磁铁？**
   - **定义**：磁铁是内部磁畴（原子磁矩）取向一致、能在周围空间产生磁场并吸引铁、钴、镍等铁磁性物质的物体，具有南（S）北（N）两极。
   - **制作方法**：① **电磁感应磁化法**：将硬钢棒放入通有强直流电的螺线管线圈内部，强磁场使钢棒内部磁畴定向排列，断电后保留剩磁成为永磁体（或保留通电线圈绕软铁芯直接构成电磁铁）；② **永磁体单向摩擦法**：用一块现成的永磁体磁极沿同一方向反复摩擦钢针/钢棒。

9. **(i)（1 分）普通照相机的结构原理及煤气灯（Gaslight）下拍照通常失败的原因**：
   - **相机原理**：由不透光暗箱、前端凸透镜（镜头）、光圈、快门以及位于焦平面处的感光干版/胶片组成。远处物体发出的光经凸透镜折射后，在感光底片上形成倒立、缩小的实像，使底片上的卤化银（如 \(\text{AgBr}\)）发生光化学还原记录潜影。
   - **煤气灯下拍照失败的原因**：19 世纪末的早期卤化银感光干版仅对高频、短波长的**蓝紫光和紫外光（Actinic rays，光化学活性射线）**敏感，而对红黄光几乎不感光（尚未普及全色感光乳剂）；同时煤气灯火焰温度低（约 \(1500\text{--}2000\text{ K}\)），发光强度弱且光谱绝大部分集中在长波长的**红外、红光与黄光区**，蓝紫光成分极少，导致底片无法在合理曝光时间内有效感光。

10. **(j)（1 分）证明含参高斯积分 \(\int_0^\infty e^{-a^2 x^2}\cos(2bx)\,dx = \frac{\sqrt{\pi}}{2a}e^{-b^2/a^2}\)**：
    - **证法一（含参变量积分求导法 / 费曼技巧，完全符合 1888 年经典微积分风格）**：
      记 \(I(b) = \int_0^\infty e^{-a^2 x^2}\cos(2bx)\,dx\)。对参数 \(b\) 求导并用分部积分：
      \[
      \begin{aligned}
      \frac{dI}{db} &= \int_0^\infty (-2x)e^{-a^2 x^2}\sin(2bx)\,dx = \int_0^\infty \frac{\sin(2bx)}{a^2}\,d\left(e^{-a^2 x^2}\right) \\
      &= \left[\frac{e^{-a^2 x^2}\sin(2bx)}{a^2}\right]_0^\infty - \frac{2b}{a^2}\int_0^\infty e^{-a^2 x^2}\cos(2bx)\,dx = -\frac{2b}{a^2}I(b).
      \end{aligned}
      \]
      分离变量求解一阶常微分方程 \(\frac{dI}{I} = -\frac{2b}{a^2}db\)：
      \[
      I(b) = I(0) e^{-b^2/a^2}.
      \]
      利用标准高斯积分初值 \(I(0) = \int_0^\infty e^{-a^2 x^2}dx = \frac{\sqrt{\pi}}{2a}\)，立得：
      \[
      \int_0^\infty e^{-a^2 x^2}\cos(2bx)\,dx = \frac{\sqrt{\pi}}{2a}e^{-b^2/a^2}.
      \]
    - **证法二（欧拉公式配方法）**：
      利用被积函数偶对称性与 \(\cos(2bx) = \operatorname{Re}\left(e^{2ibx}\right)\)：
      \[
      I(b) = \frac{1}{2}\int_{-\infty}^\infty e^{-a^2 x^2 + 2ibx}dx = \frac{1}{2}e^{-b^2/a^2}\int_{-\infty}^\infty e^{-a^2\left(x - \frac{ib}{a^2}\right)^2}dx = \frac{\sqrt{\pi}}{2a}e^{-b^2/a^2}.
      \]

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q7`）对比**：
  官方解答特别说明“既接受 1888 年时代的解释，也接受现代物理解释”。我们的十问解答完整覆盖了官方评分要点，而且在第 (j) 问中，官方解答采用的是把 \(\cos(2bx)\) 展开成幂级数逐项用伽马函数积分或用分部积分的方法，我们给出的“对参数 \(b\) 求导化为一阶 ODE”和“复指数配方法”比级数展开法快得多！
- **核心难点与易错点**：
  1. **避雷针的常见误区**：官方解答第 (e) 问特别注明“Award no marks for any references to the rod attracting the lightning to it”——避雷针的作用是当雷击发生时提供低阻抗对地泄流通道（以及尖端放电中和电荷），切勿写成“把远处的闪电吸引过来”。
  2. **第 (j) 问积分上下限是 \([0, \infty)\) 而非 \((-\infty, \infty)\)**：注意单侧高斯积分结果带有因子 \(\frac{1}{2}\)，即 \(\frac{\sqrt{\pi}}{2a}e^{-b^2/a^2}\)。

---

### 18. Dominoes and Pendulums (`plancks-2020-final-problem-slice-q8`)

- **物理模型**：长方体骨牌倾倒的重力势能垒（亚稳态局部极小值）与大振幅单摆周期发散的连续性拓扑论证
- **难度评级**：D1
- **教学标签**：`经典力学`、`重力势能垒`、`亚稳态与稳定性`、`非线性单摆`、`连续性论证`

#### 第一阶段：只看原题的独立盲解

1. **(a)（6 分）为什么竖直放置的多米诺骨牌（\(d < l\)）不会自发倒下以达到最低能量状态？**
   - **质心运动轨迹与势能函数 \(U(\theta)\)**：
     骨牌宽 \(2d\)、高 \(2l\)（\(d < l\)）。在图 5(a) 竖直状态（旋转角 \(\theta = 0\)）下，右下角位于原点 \((0,0)\)，质心位于 \((-d, l)\)，质心高度为 \(y(0) = l\)；在图 5(b) 平躺状态（\(\theta = \pi/2\)）下，质心位于 \((l, d)\)，高度为 \(y(\pi/2) = d < l\)。
     当骨牌绕右下角支点 \((0,0)\) 顺时针转过角度 \(\theta \in [0, \pi/2]\) 时，质心到原点的距离恒为对角线之半 \(r = \sqrt{l^2 + d^2}\)，质心坐标 \((x(\theta), y(\theta))\) 由旋转变换给出：
     \[
     \begin{pmatrix} x(\theta) \\ y(\theta) \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} -d \\ l \end{pmatrix} = \begin{pmatrix} -d\cos\theta + l\sin\theta \\ d\sin\theta + l\cos\theta \end{pmatrix}.
     \]
     因此重力势能 \(U(\theta) = m g y(\theta)\) 随倾角 \(\theta\) 的变化为：
     \[
     U(\theta) = mg\bigl(l\cos\theta + d\sin\theta\bigr) = mg\sqrt{l^2 + d^2}\sin(\theta + \varphi), \qquad \varphi = \arctan\left(\frac{l}{d}\right) > \frac{\pi}{4}.
     \]
   - **势能垒（Potential Energy Barrier）与局部稳定性分析**：
     对 \(y(\theta)\) 求导：
     \[
     \frac{dy}{d\theta} = d\cos\theta - l\sin\theta, \qquad \left.\frac{dy}{d\theta}\right|_{\theta = 0^+} = d > 0！
     \]
     在小角度微扰下，\(y(\theta) \approx l + d\theta - \frac{1}{2}l\theta^2\)，质心高度首先随 \(\theta\) 增大而**上升**，直到临界倾角 \(\theta_m = \arctan(d/l)\)（此时质心恰好运动到支点 \((0,0)\) 的正上方）达到势能极大值：
     \[
     U_{\max} = mg\sqrt{l^2 + d^2} > U(0) = mgl.
     \]
     这说明图 5(a) 的竖直状态处于一个**局部势能极小值（亚稳态 Metastable State）**，与图 5(b) 的全局势能极小值 \(U(\pi/2) = mgd\) 之间隔着一个高度为：
     \[
     \Delta U = mg\left(\sqrt{l^2 + d^2} - l\right) > 0
     \]
     的**势能垒**（或从力矩角度看：当 \(\theta < \arctan(d/l)\) 时，重力作用线落在支点 \((0,0)\) 左侧，产生逆时针恢复力矩使骨牌回到竖直位置）。在没有外部能量注入越过该势能垒之前，骨牌无法自发倾倒。

2. **(b)（4 分）基于连续性证明单摆周期 \(T(\theta_0)\) 随初始振幅 \(\theta_0\) 增大而增加**：
   - 考察刚性轻杆单摆从静止释放（\(\theta(0) = \theta_0, \dot{\theta}(0) = 0\)）的运动方程 \(\frac{d^2\theta}{dt^2} + \frac{g}{l}\sin\theta = 0\)。
   - 当初始释放角取极限值 \(\theta_0 = \pi\)（即摆球竖直倒立在最高点）时，\(\sin\pi = 0\)，切向恢复力为零，摆球处于**不稳定平衡点**。若无外界扰动，从 \(\theta_0 = \pi\) 静止释放的摆球将永远停留在最高点，意味着完成一次往复摆动的周期趋于无穷大：
     \[
     \lim_{\theta_0 \to \pi^-} T(\theta_0) = \infty.
     \]
   - 而在小角度极限 \(\theta_0 \to 0^+\) 下，周期收敛于有限常数 \(T(0) = 2\pi\sqrt{\frac{l}{g}}\)。
   - 由于运动微分方程中的恢复力项 \(\sin\theta\) 在 \(\theta_0 \in (0, \pi)\) 上光滑连续，周期函数 \(T(\theta_0)\) 是关于初始振幅 \(\theta_0\) 的连续函数（且在 \((0, \pi)\) 内处处有 \(\sin\theta < \theta\)，真实角加速度恒小于简谐近似值）。一个在 \(\theta_0 \to 0\) 时为有限值 \(2\pi\sqrt{l/g}\)、在 \(\theta_0 \to \pi\) 时连续发散至 \(+\infty\) 的单调光滑函数，必然随初始振幅 \(\theta_0\) 的增大而增大！

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q8`）对比**：
  我们的解答与官方解答完全一致！在第 (a) 问中，我们同样使用了二维旋转矩阵导出 \(y(\theta) = d\sin\theta + l\cos\theta = \sqrt{l^2+d^2}\sin(\theta+\varphi)\)、小角度展开 \(y \approx l + d\theta - l\theta^2/2\) 以及极值角 \(\theta_m = \arctan(d/l)\)；在第 (b) 问中，官方解答正是利用最高点 \(\theta_0 = \pi\) 为不稳定平衡点、周期 \(T(\pi) = \infty\) 结合连续性给出证明。
- **核心难点与易错点**：
  1. **注意题干第 (a) 问的坐标笔误**：题干文字将图 5(a) 的质心坐标误印成了 \((-d, -l)\)，而图 5(a) 中清楚标明质心在第二象限 \((-d, l)\)（官方解答第 2 页也按 \((-d, l)\) 计算）。答题时顺手指出题干文字中的负号笔误并以图 5(a) 的 \((-d, l)\) 为准，能展现极佳的物理素养。
  2. **第 (b) 问切勿陷入椭圆积分展开**：题目明确要求“Present a simple argument based on continuity”，若花大量时间推导第一类完全椭圆积分 \(T(\theta_0) = 4\sqrt{l/g}K(\sin\frac{\theta_0}{2}) \approx 2\pi\sqrt{l/g}(1 + \frac{1}{16}\theta_0^2 + \cdots)\) 虽然正确，但不如直接指出 \(\theta_0 \to \pi\) 时 \(T \to \infty\) 的拓扑连续性论证简洁直观。

---

### 19. Buried Room (`plancks-2020-final-problem-slice-q9`)

- **物理模型**：地心空腔内的牛顿球壳定理（万有引力势恒定）、非惯性系离心力与日月潮汐力数量级评估模型
- **难度评级**：D2
- **教学标签**：`万有引力`、`牛顿球壳定理`、`引力势积分`、`非惯性系与潮汐力`、`开放式物理估算`

#### 第一阶段：只看原题的独立盲解

**结论**：你会**漂浮（Float）**在房间中（处于微重力/失重状态），而不会像在地面上那样稳稳站在某一面墙上。

以下从基本物理原理、假设条件与多因素数量级估算给出完整论证：

1. **基本假设（Assumptions）**：
   - 房间具有足够的结构强度与隔热、密封生命维持系统，使人（设质量 \(m \approx 80\text{--}100\text{ kg}\)，可视为质点）能在地心的高温高压环境下正常生存；
   - 地球一阶近似为球对称天体（半径 \(R_E \approx 6.37 \times 10^6\text{ m}\)，密度 \(\rho(r')\) 仅依赖于距地心的距离 \(r'\)，或简化为均匀密度 \(\bar{\rho} \approx 5.5 \times 10^3\text{ kg/m}^3\)），房间近似为位于地心、半径 \(a \sim 5\text{ m}\) 的球形或正方体空腔。

2. **地球自身引力的严格证明——牛顿球壳定理（Newton's Shell Theorem）**：
   考虑内半径为 \(a\)、外半径为 \(b = R_E\) 的球对称厚球壳，在空腔内部任意一点 \(P\)（距地心距离 \(R < a\)）产生的引力势 \(\Phi(R)\)。
   采用球坐标系 \((r', \theta, \varphi)\)，将 \(z\) 轴取在 \(\vec{R}\) 方向。质量微元 \(dm = \rho(r') r'^2 \sin\theta\,dr'\,d\theta\,d\varphi\) 到点 \(P\) 的距离为 \(r = \sqrt{r'^2 + R^2 - 2r'R\cos\theta}\)。
   对 \(\theta\) 微分得 \(r\,dr = r' R \sin\theta\,d\theta\)，当 \(\theta\) 从 \(0\) 变到 \(\pi\) 时，因为 \(R < a \le r'\)，距离 \(r\) 从 \(r_{\min} = r' - R\) 变到 \(r_{\max} = r' + R\)。
   因此空腔内任一点 \(P\) 的引力势为：
   \[
   \Phi(R) = -2\pi G \int_a^b \rho(r') r'^2 dr' \int_0^\pi \frac{\sin\theta\,d\theta}{r} = -\frac{2\pi G}{R}\int_a^b \rho(r') r'\,dr' \int_{r'-R}^{r'+R} dr = -4\pi G \int_a^b \rho(r') r'\,dr' = \text{const}！
   \]
   若密度 \(\rho\) 恒定，则 \(\Phi(R) = -2\pi G \rho (b^2 - a^2) = \text{const}\)。
   由于引力势 \(\Phi\) 在空腔内部处处为常数（与位置 \(R\) 完全无关），引力场强为：
   \[
   \vec{g}_{\text{Earth}}(\vec{R}) = -\vec{\nabla}\Phi = \vec{0} \quad (\forall R < a)！
   \]
   （注：也可以使用高斯引力通量定理 \(\oint \vec{g}\cdot d\vec{A} = -4\pi G M_{\text{enc}} = 0\) 一步证得 \(\vec{g} = \vec{0}\)。）

3. **高阶微扰与次要物理效应的数量级评估**：
   - **正方体空腔形状修正（偏离球对称）**：
     \(10\text{ m} \times 10\text{ m} \times 10\text{ m}\) 的正方体空腔与内切球之间的八个角落质量缺失（或房间墙壁建材质量）产生的残余引力场量级至多为 \(\Delta g_{\text{cube}} \sim G \rho_c L \sim 6.67\times 10^{-11} \times 1.3\times 10^4 \times 10 \sim 10^{-5}\text{ m/s}^2 \sim 10^{-6}\,g_0\)，微乎其微。
   - **地球内部横向密度不均匀性**：
     若地球地幔/地核某侧存在高密度异常体，会产生微弱的净引力指向密度较高的一侧，但量级同样远小于地面重力。
   - **地球自转离心力**：
     地球自转角速度 \(\omega \approx 7.29 \times 10^{-5}\text{ rad/s}\)，在房间内离自转轴最大距离 \(r_\perp \le 5\sqrt{2}\text{ m} \approx 7\text{ m}\) 处，离心加速度为：
     \[
     a_{\text{cent}} = \omega^2 r_\perp \lesssim (7.29 \times 10^{-5})^2 \times 7 \approx 3.7 \times 10^{-8}\text{ m/s}^2 \approx 4 \times 10^{-9}\,g_0,
     \]
     完全无法让人“站立”。
   - **太阳与月球的引力及潮汐效应**：
     虽然太阳在地心处的引力场强为 \(g_{\text{Sun}} = \frac{GM_\odot}{d_{\text{ES}}^2} \approx 5.9 \times 10^{-3}\text{ m/s}^2\)，月球引力场强为 \(g_{\text{Moon}} \approx 3.3 \times 10^{-5}\text{ m/s}^2\)，但因为**整个地球（连同地心房间）都在绕日、绕地月质心做自由落体轨道运动**，在随地球平动的非惯性系中，天体在地心处的均匀引力被轨道惯性力精确抵消！人在房间里感受到的只是跨越 \(r \sim 5\text{ m}\) 的**潮汐加速度**：
     \[
     a_{\text{tidal}} \sim \frac{2 G M_{\text{Moon}} r}{d_{\text{EM}}^3} \sim 10^{-12}\text{ m/s}^2,
     \]
     即使不考虑自由落体抵消而直接计算太阳/月球引力（如官方评分标准中也给分的简化视角），其大小也远小于地面重力且方向随地球自转不断改变。
   - **房间内多个人之间的相互万有引力与空气浮力**：
     若房间内有两个质量 \(m = 100\text{ kg}\) 的人相距 \(1\text{ m}\)，彼此引力仅为 \(F = \frac{Gm^2}{d^2} \approx 6.7 \times 10^{-7}\text{ N}\)。而在微重力下，人轻轻蹬墙或呼吸气流的速度（\(\sim \text{m/s}\)）远大于任何残余微重力场的逃逸速度（\(\sqrt{2\Delta g L} \lesssim 1\text{ cm/s}\)），因此人必然在房间内自由漂浮！

#### 第二阶段：对照官方解答与教学拆解

- **与官方解答（`plancks-2020-final-solution-slice-q9`）对比**：
  官方解答是一份长达 6 页的开放式评分指南，将 10 分拆分为五大板块：
  1. **地球内部引力分析（1–6 分）**：定性说明对称抵消并画图得 2–3 分；用薄球壳力积分（式 1–9）或厚球壳引力势积分 \(\Phi = -2\pi\rho G(b^2 - a^2) = \text{const}\)（式 10–14）严格证明空腔内 \(\vec{g} = -\nabla\Phi = \vec{0}\) 可拿满 5–6 分！我们的盲解不仅给出了厚球壳引力势积分的完整推导，还推广到了任意径向密度分布 \(\rho(r')\)。
  2. **太阳系其他天体（太阳、月球）的影响（1–2 分）**：用万有引力定律讨论太阳和月球的影响。
  3. **房间的几何与物理性质（1 分）**：讨论正方体与球形近似、墙壁引力、高温高压防护等。
  4. **人的假设与多体引力（1 分）**：将人视为 \(\sim 80\text{--}100\text{ kg}\) 质点、房间内两人之间的引力等。
  5. **其他合理的物理效应（1–2 分）**：如地球内部密度不均匀、地球自转效应、空气浮力等。
- **核心难点与易错点**：
  1. **“仅在地心一点 \(r=0\) 处引力为零” vs “在整个空腔 \(r < a\) 内处处引力为零”**：许多学生以为只有站在房间正中心 \((0,0,0)\) 才不受地球引力，一旦偏离中心靠近墙壁（例如 \(r = 4\text{ m}\)）就会受到地球引力。实际上由牛顿球壳定理，由于 \(r < a\) 内部已经被挖空，外部整个地球（\(a \le r' \le R_E\)）在球形空腔内的**每一个点**产生的合引力都严格为零！
  2. **球壳引力势积分上下限的符号处理**：在积分 \(\int_{|r'-R|}^{r'+R} dr\) 中，对于空腔内部点有 \(R < a \le r'\)，故 \(|r' - R| = r' - R\)，积分结果为 \(2R\)，恰与分母上的 \(R\) 约去，使引力势 \(\Phi\) 成为与 \(R\) 无关的常数；而在实心球外部（\(R > b \ge r'\)），\(|r' - R| = R - r'\)，积分结果为 \(2r'\)，从而保留了 \(1/R\) 依赖关系。
