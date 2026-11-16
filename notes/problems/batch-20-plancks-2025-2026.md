# Batch 20: PLANCKS 2025 & 2026 International Finals 教学解析笔记

本笔记涵盖 **PLANCKS 2025 国际决赛（巴塞罗那，Q1–Q9）** 与 **PLANCKS 2026 国际决赛（埃因霍温，Q1–Q9）** 共 18 道赛题的完整两阶段盲解推演、官方解答对照及面向物理竞赛生（高中拔高与本科竞赛）的深度教学拆解。

---

## 第一部分：PLANCKS 2025 国际决赛（Q1–Q9）

### 1. 反亥姆霍兹线圈中的悬浮 (`plancks-2025-final-combined-slice-q1`)

- **物理模型**：反亥姆霍兹线圈四极磁场与小磁球磁悬浮稳定性分析
- **难度评级**：D3
- **核心标签**：`反亥姆霍兹线圈`、`四极磁场展开`、`退磁因子`、`抗磁悬浮`、`刚度张量与恩肖定理`

#### 题目拆解与求解脉络
1. **轴上磁场展开**：利用毕奥-萨伐尔定律写出位于 \(z = \pm R/2\)、电流大小同为 \(I\) 但方向相反的两共轴圆线圈在 \(z\) 轴上的磁感应强度：
   \[ B_z(0,0,z) = \frac{\mu_0 I R^2}{2}\left[\frac{1}{\left(R^2 + (z-R/2)^2\right)^{3/2}} - \frac{1}{\left(R^2 + (z+R/2)^2\right)^{3/2}}\right] \approx \frac{48\mu_0 I}{25\sqrt{5}R^2} z = B_0 \frac{2z}{R}, \]
   其中 \(B_0 \equiv \frac{24\mu_0 I}{25\sqrt{5}R}\)。
2. **近轴三维四极场重构**：由自由空间 \(\nabla \times \mathbf{B}_a = \mathbf{0}\)、\(\nabla \cdot \mathbf{B}_a = 0\) 及绕 \(z\) 轴旋转对称性，可得 \(\frac{\partial B_x}{\partial x} = \frac{\partial B_y}{\partial y} = -\frac{1}{2}\frac{\partial B_z}{\partial z} = -\frac{B_0}{R}\)，从而原点附近一阶非零磁场为标准线性四极场：
   \[ \mathbf{B}_a(\mathbf{r}) = \frac{B_0}{R}\left(-x\hat{x} - y\hat{y} + 2z\hat{z}\right). \]
3. **计入退磁场的球体磁化**：小磁球（半径 \(a \ll R\)）内部退磁场为 \(\mathbf{H}_d = -\frac{1}{3}\mathbf{M}\)，由 \(\mathbf{M} = \chi(\mathbf{H}_a + \mathbf{H}_d) = \chi\left(\frac{\mathbf{B}_a}{\mu_0} - \frac{1}{3}\mathbf{M}\right)\) 解得：
   \[ \mathbf{M} = \frac{3\chi}{\mu_0(3+\chi)}\mathbf{B}_a, \quad \mathbf{m} = \frac{4}{3}\pi a^3 \mathbf{M} = \frac{4\pi a^3}{\mu_0}\frac{\chi}{3+\chi}\mathbf{B}_a. \]
4. **磁力与刚度系数矩阵**：由 \(\mathbf{F} = (\mathbf{m}\cdot\nabla)\mathbf{B}_a = \frac{1}{2}\nabla(\mathbf{m}\cdot\mathbf{B}_a)\) 得：
   \[ \mathbf{F}(\mathbf{r}) = \frac{4\pi a^3}{3\mu_0}\left(\frac{3\chi}{3+\chi}\right)\frac{B_0^2}{R^2}(x\hat{x} + y\hat{y} + 4z\hat{z}), \quad \kappa_{\alpha\beta} = -\left.\frac{\partial F_\alpha}{\partial \beta}\right|_{\mathbf{r}=\mathbf{0}} = -\frac{4\pi a^3 B_0^2}{3\mu_0 R^2}\left(\frac{3\chi}{3+\chi}\right)\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \end{pmatrix}. \]
   - 当 \(\chi = -1\)（完全抗磁体/超导体）时，\(\frac{3\chi}{3+\chi} = -\frac{3}{2} < 0\)，三个主刚度系数全为正（且 \(z\) 方向刚度是横向的 4 倍），系统在原点处于**三维稳定悬浮状态**；
   - 当 \(\chi = +1\)（顺磁体）时，\(\frac{3\chi}{3+\chi} = +\frac{3}{4} > 0\)，主刚度系数全为负，原点为**全方向不稳定平衡点**。

#### 盲解体会与对照分析
- **盲解对照**：盲解时我采用感应偶极子在磁场中的势能 \(U(\mathbf{r}) = -\frac{1}{2}\mathbf{m}(\mathbf{r})\cdot\mathbf{B}_a(\mathbf{r})\) 求负梯度计算磁力，官方解答则直接使用 \(\mathbf{F} = (\mathbf{m}\cdot\nabla)\mathbf{B}_a\)。利用无旋场恒等式 \((\mathbf{B}_a\cdot\nabla)\mathbf{B}_a = \frac{1}{2}\nabla(B_a^2)\) 可见两者完全等价。
- **易错警示**：务必区分外磁场 \(\mathbf{H}_a = \mathbf{B}_a/\mu_0\) 与球内总磁场 \(\mathbf{H} = \mathbf{H}_a - \mathbf{M}/3\)；若漏掉退磁因子 \(1/3\)，比例系数 \(\frac{3\chi}{3+\chi}\) 会误算为 \(\chi\)，在 \(\chi = -1\) 时相差 \(3/2\) 倍。

---

### 2. 表面吸附 (`plancks-2025-final-combined-slice-q2`)

- **物理模型**：固体表面气体吸附的统计力学模型与朗缪尔等温线（Langmuir Isotherm）
- **难度评级**：D2
- **核心标签**：`微正则系综`、`正则系综`、`化学势平衡`、`朗缪尔吸附等温线`、`斯特林公式`

#### 题目拆解与求解脉络
1. **微正则系综与熵**：\(n\) 个粒子占据 \(N_S\) 个表面格点（单粒子能量 \(-\epsilon\)），\(N-n\) 个粒子占据 \(N_B\) 个体相格点（能量 0），微观状态数为：
   \[ \Omega(n) = \frac{N_B!}{(N-n)!(N_B-N+n)!}\frac{N_S!}{n!(N_S-n)!}. \]
   利用斯特林公式可得 \(S(n) = k_B \ln \Omega(n)\)。
2. **温度与吸附粒子数的关系**：由 \(E = -n\epsilon\) 及 \(\frac{1}{T} = \frac{\partial S}{\partial E} = -\frac{1}{\epsilon}\frac{\partial S}{\partial n}\) 得：
   \[ \frac{(N-n)(N_S-n)}{n(N_B-N+n)} = e^{-\epsilon/(k_B T)}. \]
   当 \(T \to \infty\) 时，\(\frac{n}{N} \to \frac{N_S}{N_S + N_B}\)（所有格点等概率占据）；当 \(T \to 0\) 时，\(n \to N_S\)，\(\frac{n}{N} \to \frac{N_S}{N}\)（表面格点完全填满以使能量最低）。
3. **正则系综与化学势平衡**：将体相与表面视为两个子系统，配分函数分别为 \(Z_B = \binom{N_B}{n_g}\) 与 \(Z_S = \binom{N_S}{n}e^{\beta n\epsilon}\)，由化学势相等 \(\mu_B = \mu_S\) 可导出完全相同的吸附状态方程。
4. **稀薄极限与朗缪尔等温线**：当 \(N_B \gg N \gg N_S\) 时，\(N-n \approx N\)，\(N_B - N + n \approx N_B\)，故：
   \[ \theta \equiv \frac{n}{N_S} = \frac{1}{1 + \frac{N_B}{N}e^{-\epsilon/(k_B T)}}. \]
   令 \(\theta = 1/2\) 得半满温度 \(T_{1/2} = \frac{\epsilon}{k_B \ln(N_B/N)}\)。结合体相理想气体方程 \(p V = p N_B V_0 = N k_B T \implies \frac{N_B}{N} = \frac{k_B T}{p V_0}\)，即得朗缪尔吸附等温线：
   \[ \theta(p) = \frac{p}{p + p_0(T)}, \quad p_0(T) = \frac{k_B T}{V_0}e^{-\epsilon/(k_B T)}. \]

#### 盲解体会与对照分析
- **系综等价性**：在热力学极限下，对总配分函数求最概然项（鞍点法）与令两个子系统的化学势相等（\(\mu_B = \mu_S\)）在数学上完全同构，后者在推广到多层吸附（BET 等温线）或混合气体竞争吸附时更具威力。

---

### 3. 第二声 (`plancks-2025-final-combined-slice-q3`)

- **物理模型**：半导体中的第二声（Second Sound）、麦克斯韦-卡塔尼奥方程与扩展不可逆热力学
- **难度评级**：D3
- **核心标签**：`第二声`、`麦克斯韦-卡塔尼奥方程`、`电报方程`、`热光栅实验`、`非平衡态熵产生`

#### 题目拆解与求解脉络
1. **弛豫极限与电报方程**：Maxwell-Cattaneo 方程 \(\tau \frac{\partial \mathbf{q}}{\partial t} + \mathbf{q} = -\kappa \nabla T\) 在慢变极限 \(t_p \gg \tau\) 下退化为傅里叶定律 \(\mathbf{q} = -\kappa\nabla T\)。联立定容能量守恒 \(C_V \frac{\partial T}{\partial t} + \nabla\cdot\mathbf{q} = 0\) 消去 \(\mathbf{q}\)，得到阻尼波动方程（电报方程）：
   \[ \tau \frac{\partial^2 T}{\partial t^2} + \frac{\partial T}{\partial t} = \frac{\kappa}{C_V}\nabla^2 T. \]
   在高频极限 \(\omega\tau \gg 1\) 下，温度以波速 \(v_{SS} = \sqrt{\frac{\kappa}{C_V\tau}} = \sqrt{\frac{\frac{1}{3}C_V c^2\tau}{C_V\tau}} = \frac{c}{\sqrt{3}} < c\) 传播，即“第二声”。
2. **热光栅实验中的阻尼驻波**：对 \(\Delta T(x,0) = A\cos(kx)\)（\(k = 2\pi/L\)），解的形式为：
   \[ \Delta T(x,t) = A e^{-t/(2\tau)}\cos(\omega_r t)\cos\left(\frac{2\pi x}{L}\right), \quad \omega_r = \frac{1}{2\tau}\sqrt{\frac{4\kappa\tau}{C_V}k^2 - 1} = \sqrt{v_{SS}^2 k^2 - \frac{1}{4\tau^2}}. \]
   要在阻尼衰减时间 \(2\tau\) 内观测到至少一次完整振荡，需满足 \(\frac{2\pi}{\omega_r} < 2\tau\)，解得空间周期上限：
   \[ L < \frac{2\pi}{\sqrt{1+4\pi^2}} v_{SS}\tau \approx v_{SS}\tau. \]
3. **逆温差传热与非平衡态熵产生**：在波动区，由于热流存在弛豫惯性 \(\tau\partial_t\mathbf{q}\)，\(\mathbf{q}\) 与 \(-\nabla T\) 存在 \(\pi/2\) 相位差，半数时间内热量从低温流向高温。在局域平衡假设下 \(\sigma_s = -\frac{\mathbf{q}\cdot\nabla T}{T^2} = \frac{q^2 + \tau\mathbf{q}\cdot\dot{\mathbf{q}}}{\kappa T^2}\) 可正可负；而引入扩展不可逆热力学（EIT）非平衡熵密度 \(s(u,\mathbf{q}) = s_{eq}(u) - \frac{\tau}{2\kappa T^2}q^2\) 后，熵产生率严格为 \(\sigma_s = \frac{q^2}{\kappa T^2} \ge 0\)，与热力学第二定律完全相容。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，我对能量守恒式作用算符 \((1 + \tau \partial_t)\) 并代入 \(\nabla\cdot(\mathbf{q} + \tau\partial_t\mathbf{q}) = -\kappa\nabla^2 T\)，直接导出电报方程，代入 \(\kappa = \frac{1}{3}C_V c^2 \tau\) 立刻得到 \(v_{SS} = c/\sqrt{3}\)。在第 3 问中，令 \(k = 2\pi/L\)，特征方程给出衰减因子 \(e^{-t/(2\tau)}\) 和振荡实频 \(\omega_r = \frac{1}{2\tau}\sqrt{4 v_{SS}^2 \tau^2 k^2 - 1}\)。要观测到至少一次完整振荡，不仅要求根号内大于零（\(L < 4\pi v_{SS}\tau\)），还需满足周期 \(T_{\text{osc}} = \frac{2\pi}{\omega_r} < 2\tau\)，解得 \(L < \frac{2\pi}{\sqrt{1+4\pi^2}} v_{SS} \tau \approx v_{SS}\tau\)。第 5 问直接用矢量恒等式 \(\nabla\cdot(\mathbf{q}/T) = \frac{1}{T}\nabla\cdot\mathbf{q} - \frac{\mathbf{q}\cdot\nabla T}{T^2}\) 即可干净利落地消去 \(\partial_t u + \nabla\cdot\mathbf{q} = 0\)。
- **Phase 2 对照参考解答**：官方解答与独立盲解高度吻合。在第 3 问关于“至少观测到一次振荡”的判据上，官方解答正是采用 \(2\pi/\omega_r < 2\tau\)（并注明取 \(4\tau\) 亦可得分），化简得到 \(L < \frac{2\pi}{\sqrt{1+4\pi^2}} v_{SS}\tau \approx v_{SS}\tau\)。在第 4 问中，官方解答给出了两种非常漂亮的物理解释：一是站在驻波角度（半个周期后原本的波谷低温区变成波峰高温区，说明热量曾逆温差汇聚），二是站在行波角度（由 \(C_V \omega T = k q\) 知 \(q\) 与 \(T\) 同相，从而与 \(\partial_x T\) 相差 \(\pi/2\) 相位，故有半数时间 \(\mathbf{q}\cdot\nabla T > 0\)）。
- **核心难点**：
  - 难点1：联立一阶偏微分方程组消元导出温度的二阶电报方程，并准确区分扩散主导区（\(\omega\tau \ll 1\)）与波动主导区（\(\omega\tau \gg 1\)）。
  - 难点2：在非平衡热力学（第 5 问）中，理解为什么局域平衡假设下 \(\sigma_s = -\frac{\mathbf{q}\cdot\nabla T}{T^2} = \frac{q^2 + \tau\mathbf{q}\cdot\dot{\mathbf{q}}}{\kappa T^2}\) 可正可负，而含热流惯性项的广义吉布斯关系 \(ds = T^{-1}du - \frac{\tau}{\kappa T^2}\mathbf{q}\cdot d\mathbf{q}\) 能完美消除不定号项。
- **高频易错点**：
  - 易错点1：在第 3 问只写出欠阻尼条件 \(4 v_{SS}^2 \tau^2 k^2 > 1\)（即 \(L < 4\pi v_{SS}\tau\)），却忽略了题干中“在达到平衡前至少能观测到一次温度振荡”（即振荡周期必须小于阻尼衰减时间 \(2\tau\)）这一更强的定量限制。
  - 易错点2：在计算 \(\nabla\cdot(\mathbf{q}/T)\) 时忘记对分母 \(T\) 求梯度，漏掉产生熵的核心项 \(\mathbf{q}\cdot\nabla(1/T) = -\frac{\mathbf{q}\cdot\nabla T}{T^2}\)。
- **教学核心结论**：傅里叶定律对应的抛物型热传导方程具有无限大信号传播速度的非物理缺陷；引入弛豫时间 \(\tau\) 的 Maxwell-Cattaneo 方程将其修正为双曲型电报方程，不仅预言了波速为 \(c/\sqrt{3}\) 的第二声，更开启了“扩展不可逆热力学（EIT）”的现代视野。

---

### 4. 关于宇宙的几个问题 (`plancks-2025-final-combined-slice-q4`)

- **物理模型**：弗里德曼宇宙学：流体状态方程、减速参数与平坦 \(\Lambda\text{CDM}\) 宇宙年龄积分
- **难度评级**：D2
- **核心标签**：`弗里德曼方程`、`宇宙学状态方程`、`减速参数`、`宇宙学常数`、`宇宙年龄精确解`

#### 题目拆解与求解脉络
1. **能量密度演化幂律**：由 \(\dot{\rho}_A = -3\frac{\dot{a}}{a}(1+w_A)\rho_A\) 积分得 \(\rho_A \propto a^{\pi_A}\)，其中 \(\pi_A = -3(1+w_A)\)。对比物质 \(\rho_M \propto a^{-3}\)、辐射 \(\rho_R \propto a^{-4}\)、宇宙学常数 \(\rho_\Lambda \propto a^0\)，得 \(w_M = 0, w_R = 1/3, w_\Lambda = -1\)。
2. **宇宙加速方程与减速参数**：对 \(\dot{a}^2 = \frac{8\pi G}{3}\rho a^2 - k\) 求时间导数并代入 \(\dot{\rho} = -3\frac{\dot{a}}{a}(\rho+P)\)，得：
   \[ \ddot{a} = -\frac{4\pi G}{3}a(\rho + 3P) \implies \alpha = -\frac{4\pi}{3}, \quad \beta = -4\pi. \]
   今日减速参数为：
   \[ q_0 = -\left.\frac{a\ddot{a}}{\dot{a}^2}\right|_0 = \frac{1}{2}\sum_A (1+3w_A)\Omega_A = \frac{1}{2}\Omega_M + \Omega_R - \Omega_\Lambda. \]
3. **平坦 \(\Lambda\text{CDM}\) 宇宙年龄**：当 \(k=0, \Omega_R=0\) 时，\(\Omega_M = 1 - \Omega_\Lambda\)，\(H(a) = H_0\sqrt{\Omega_M a^{-3} + \Omega_\Lambda}\)，故（作换元 \(x = a^{3/2}\)）：
   \[ t_0 = \frac{1}{H_0}\int_0^1 \frac{a^{1/2}da}{\sqrt{\Omega_M + \Omega_\Lambda a^3}} = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\operatorname{arsinh}\left(\sqrt{\frac{\Omega_\Lambda}{1-\Omega_\Lambda}}\right) = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\ln\left(\frac{1+\sqrt{\Omega_\Lambda}}{\sqrt{1-\Omega_\Lambda}}\right). \]

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：本题思路非常清晰直接。盲解时，第一部分直接由 \(\frac{d\ln\rho_A}{d\ln a} = -3(1+w_A)\) 读出 \(\pi_A = -3(1+w_A)\)；第二部分对 \(\dot{a}^2 = \frac{8\pi G}{3}\rho a^2 - k\) 求导，注意保留 \(\rho a^2\) 的乘积求导 \(\frac{d}{dt}(\rho a^2) = \dot{\rho}a^2 + 2\rho a\dot{a} = -a\dot{a}(\rho + 3P)\)，这样曲率常数 \(k\) 在直接求导时自动消失（甚至无需再次代回第一弗里德曼方程！），一步即得 \(\ddot{a} = -\frac{4\pi G}{3}a(\rho + 3P)\)，即 \(\alpha = -4\pi/3, \beta = -4\pi\)。第三部分代入 \(x = a^{3/2}\) 后化为标准积分 \(\frac{2}{3H_0}\int_0^1 \frac{dx}{\sqrt{1-\Omega_\Lambda + \Omega_\Lambda x^2}}\)，直接写出 \(\operatorname{arsinh}\) 或对数形式。
- **Phase 2 对照参考解答**：对比官方解答，在第 2a 问求 \(\ddot{a}\) 时，官方解答是对 \((\dot{a}/a)^2\) 求导，因此中间出现了曲率项 \(2k\dot{a}/a^3\)，需要再次代回第一弗里德曼方程才能消去 \(k\)；而我们在盲解中先乘以 \(a^2\) 写成 \(\dot{a}^2 = \frac{8\pi G}{3}\rho a^2 - k\) 再对 \(t\) 求导，常数 \(-k\) 的导数直接为 0，计算量减少一半且不易出错。其余各问结果与官方解答完全一致。
- **核心难点**：
  - 难点1：推导宇宙加速方程时高效消去曲率常数 \(k\) 与能量密度时间导数 \(\dot{\rho}\)。
  - 难点2：宇宙年龄积分 \(\int_0^1 \frac{a^{1/2}da}{\sqrt{\Omega_M + \Omega_\Lambda a^3}}\) 的换元求解，以及利用平坦宇宙条件 \(\Omega_M + \Omega_\Lambda = 1\) 消去 \(\Omega_M\)。
- **高频易错点**：
  - 易错点1：在题设单位制（\(c=1\) 或将质量密度与能量密度统称为 \(\rho\)）下，注意压力 \(P\) 与能量密度 \(\rho\) 量纲相同，切勿多乘或漏除 \(c^2\)。
  - 易错点2：做代换 \(x = a^{3/2}\) 时，微分关系 \(dx = \frac{3}{2}a^{1/2}da\) 容易漏掉因子 \(\frac{2}{3}\)。
- **教学核心结论**：将第一弗里德曼方程变形为 \(\dot{a}^2 + k = \frac{8\pi G}{3}\rho a^2\) 后再对时间求导，是瞬间导出宇宙加速方程 \(\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}(\rho + 3P)\) 的最佳技巧；由此可清晰看出：任何满足 \(w < -1/3\) 的组分（如宇宙学常数 \(w_\Lambda = -1\)）都会产生排斥性引力效应并驱动宇宙加速膨胀。

---

### 5. 黑洞阴影 (`plancks-2025-final-combined-slice-q5`)

- **物理模型**：史瓦西黑洞最内稳定圆轨道（ISCO）与事件视界望远镜（EHT）甚长基线干涉测量
- **难度评级**：D3
- **核心标签**：`史瓦西黑洞`、`有效势能`、`最内稳定圆轨道ISCO`、`甚长基线干涉VLBI`、`大气窗口与角分辨率`

#### 题目拆解与求解脉络
1. **广义相对论有效势与圆轨道**：对比牛顿有效势 \(V_{\text{eff, N}} = -\frac{GmM}{r} + \frac{L^2}{2mr^2}\)，广义相对论有效势多出强场吸引项 \(-\frac{R_s L^2}{2mr^3}\)。由圆轨道条件 \(\frac{\partial V_{\text{eff}}}{\partial r} = 0\) 可反解出角动量平方随轨道半径的变化关系：
   \[ L^2(r) = \frac{GMm^2 r^2}{r - \frac{3}{2}R_s}, \quad r_\pm(L) = \frac{L^2 \pm \sqrt{L^4 - 12 G^2 M^2 m^4 c^{-2} L^2}}{2GMm^2}. \]
   可见圆轨道仅在 \(r > \frac{3}{2}R_s\) 存在，且存在最小角动量 \(L_{\min} = \sqrt{3} m R_s c\)。
2. **轨道稳定性与 ISCO 半径**：计算二阶导数 \(\left.\frac{\partial^2 V_{\text{eff}}}{\partial r^2}\right|_{\text{orb}} = \frac{L^2}{mr^5}(r - 3R_s) = \frac{GmM}{r^3}\frac{r - 3R_s}{r - \frac{3}{2}R_s}\)。因此 \(\frac{3}{2}R_s < r < 3R_s\) 为不稳定圆轨道，\(r \ge 3R_s\) 为稳定圆轨道，最内稳定圆轨道半径为：
   \[ r_{\text{ISCO}} = 3R_s = \frac{6GM}{c^2}. \]
3. **M87* 阴影角尺寸与 EHT 毫米波基线设计**：代入 \(M = 5\times 10^9 M_\odot\)、\(D_{\text{BH}} = 16.7\text{ Mpc}\)，得 \(r_{\text{ISCO}} \approx 4.5\times 10^{13}\text{ m}\)，对应角半径 \(\theta \approx \frac{r_{\text{ISCO}}}{D_{\text{BH}}} \approx 8.6\times 10^{-11}\text{ rad}\)（角直径约 \(1.7\times 10^{-10}\text{ rad}\)）。受限于离线相关器的时间延迟精度 \(\Delta \sim 1\text{ ps}\)（要求 \(\lambda \gg c\Delta = 300\ \mu\text{m}\)）、地球最大基线 \(D \le 2R_\oplus \approx 1.27\times 10^7\text{ m}\)（要求 \(\lambda = D\theta_{\text{res}} \lesssim 1.3\text{ mm}\)）以及大气透射窗口，最佳观测波长选在 \(\lambda \approx 0.9\text{ mm}\sim 1.3\text{ mm}\)，所需望远镜基线距离约为 \(D \approx 1.0\times 10^7\text{ m}\)（约地球直径的 80%）。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，面对第 1b、1c 问求圆轨道范围与稳定性，我采用了题干提示的“反解 \(L^2(r)\) 法”：由 \(V'_{\text{eff}}(r) = 0\) 直接写出 \(L^2(r) = \frac{GMm^2 r^2}{r - 1.5 R_s}\)。由于 \(L^2 > 0\)，一眼看出圆轨道存在的充要条件是 \(r > 1.5 R_s\)！接着对 \(L^2(r)\) 求导得 \(\frac{d(L^2)}{dr} = \frac{GMm^2 r(r - 3R_s)}{(r - 1.5 R_s)^2}\)，立刻读出 \(r = 3R_s\) 对应 \(L^2\) 的极小值 \(L_{\min} = \sqrt{12}GMm/c\)，且 \(r > 3R_s\) 处 \(V''_{\text{eff}} > 0\) 稳定。第 2 问算出 \(R_s \approx 1.49\times 10^{13}\text{ m}, r_{\text{ISCO}} \approx 4.47\times 10^{13}\text{ m}\)，张角 \(\theta_{\text{ISCO}} \approx 8.6\times 10^{-11}\text{ rad}\)，结合地球直径上限选出 \(\lambda \sim 1\text{ mm}\) 的亚毫米/毫米波段。
- **Phase 2 对照参考解答**：官方解答同时展示了两种方法：一是直接解关于 \(r\) 的二次方程 \(r_\pm(L)\) 并分别讨论两个分支的值域，二是反解 \(L^2(r)\) 函数。对比可见，反解 \(L^2(r) = \frac{GMm^2 r^2}{r - \frac{3}{2}R_s}\) 的代数工作量不到前者的三分之一，且能直接建立 \(\text{sgn}(V''_{\text{eff}}) = \text{sgn}\left(\frac{dL^2}{dr}\right)\) 的几何直观。在第 2b 问中，官方解答还特别强调了离线相关器时间精度 \(\Delta \sim 1\text{ ps}\) 给出波长下限 \(\lambda \gg c\Delta = 300\ \mu\text{m}\)（排除光学与红外波段），而地球直径基线 \(D \le 2R_\oplus\) 给出波长上限 \(\lambda \lesssim 1.3\text{ mm}\)（排除长波射电），两者夹逼出唯一可行的 \(0.9\sim 1.3\text{ mm}\) 大气窗口！
- **核心难点**：
  - 难点1：利用有效势的一阶与二阶导数完整分类广义相对论圆轨道（\(r \le 1.5 R_s\) 无圆轨道，\(1.5 R_s < r < 3 R_s\) 不稳定圆轨道，\(r \ge 3 R_s\) 稳定圆轨道）。
  - 难点2：在第 2b 问中综合三重工程物理约束（1 ps 延迟同步精度决定的波长下限、地球直径决定的波长上限、大气窗口透射率）锁定毫米波段。
- **高频易错点**：
  - 易错点1：在牛顿力学中任意小角动量 \(L\) 都存在稳定圆轨道 \(r = \frac{L^2}{GMm^2}\)，但在广义相对论中由于 \(-1/r^3\) 项在短距离发散，当 \(L < \sqrt{3}mR_s c\) 时有效势不再有极值点，粒子会直接旋进掉入黑洞。
  - 易错点2：混淆 ISCO 的“角半径” \(\theta_r = r_{\text{ISCO}}/D_{\text{BH}} \approx 8.6\times 10^{-11}\text{ rad}\) 与“角直径” \(2\theta_r \approx 1.7\times 10^{-10}\text{ rad}\)，计算基线时需明确说明所用的角度定义。
- **教学核心结论**：分析单参数有效势族 \(V_{\text{eff}}(r; L)\) 的极值与稳定性时，将 \(V'_{\text{eff}}(r; L) = 0\) 改写为显函数 \(L^2 = f(r)\) 是极为强大的通用技巧：其定义域 \(f(r) > 0\) 直接给出轨道存在区间，而其单调递增区间 \(f'(r) > 0\) 直接对应稳定圆轨道区间（\(V''_{\text{eff}} > 0\)）！

---

### 6. 用恒力向上提起链条 (`plancks-2025-final-combined-slice-q6`)

- **物理模型**：恒力竖直提拉链条的变质量动力学：上升非弹性并入与下降脱离的不对称阻尼振荡
- **难度评级**：D3
- **核心标签**：`变质量动力学`、`链条运动方程`、`积分因子法`、`上升与下降不对称性`、`耗散振荡`

#### 题目拆解与求解脉络
1. **上升阶段运动方程与积分因子求解**：悬垂链条质量为 \(\lambda x\)，桌面静止链节不断被拉入运动，动量定理给出：
   \[ F - \lambda g x = \frac{d}{dt}(\lambda x \dot{x}) = \lambda \dot{x}^2 + \lambda x \ddot{x} \implies x\frac{d(v^2)}{dx} + 2v^2 = \frac{2F}{\lambda} - 2gx. \]
   乘以积分因子 \(x\) 得 \(\frac{d}{dx}(x^2 v^2) = \frac{2F}{\lambda}x - 2gx^2\)，从 \(x_0\)（\(v=0\)）积分至 \(x\) 得：
   \[ v(x) = \sqrt{\frac{F}{\lambda}\left(1 - \frac{x_0^2}{x^2}\right) - \frac{2}{3}gx_0\left(\frac{x}{x_0} - \frac{x_0^2}{x^2}\right)}. \]
2. **最大高度与平衡位置对比**：令 \(v=0\) 并消去平凡根 \(x=x_0\)，解二次方程得：
   \[ x_{\max} = \frac{\sqrt{3(3F-2gx_0\lambda)(F+2gx_0\lambda)} + 3F - 2gx_0\lambda}{4g\lambda} \xrightarrow{x_0 \ll x_{\text{eq}}} \frac{3F}{2\lambda g} = \frac{3}{2}x_{\text{eq}}. \]
   由于在 \(x < x_{\text{eq}}\) 阶段恒力 \(F\) 大于悬垂段重力，链条持续加速积累向上动能，故越过平衡位置 \(x_{\text{eq}} = F/(\lambda g)\) 后仍能继续上升至 \(\frac{3}{2}x_{\text{eq}}\)。
3. **上升阶段时间演化**：当 \(x_0 \to 0\) 时 \(v(x) = \sqrt{\frac{F}{\lambda} - \frac{2}{3}gx}\)，积分 \(t = \int_0^x \frac{dx'}{v(x')}\) 得匀减速抛物线规律：
   \[ x(t) = t\left(\sqrt{\frac{F}{\lambda}} - \frac{1}{6}gt\right). \]
4. **下降阶段运动方程与最低点**：回落时（\(\dot{x} < 0\)），链节接触桌面瞬间脱离悬垂段并由桌面支持力减速至静止，对空中部分无反冲力：
   \[ F - \lambda g x = \lambda x \ddot{x} = \frac{1}{2}\lambda x \frac{d(v^2)}{dx} \implies v(x) = -\sqrt{2g(x_{\max}-x) - \frac{2F}{\lambda}\ln\left(\frac{x_{\max}}{x}\right)}. \]
   令 \(v(x_{\min}) = 0\) 并记 \(x_{\min} = \frac{F}{\lambda g}\xi\)，由 \(\frac{3}{2} - \xi + \ln\left(\frac{2\xi}{3}\right) = 0\) 解得非平凡根 \(\xi_1 \approx 0.625\)，即 \(x_{\min} \approx 0.625\frac{F}{\lambda g}\)。此后往复经历非弹性吸积与落桌耗散，振幅逐周期衰减并收敛于 \(x_{\text{eq}} = \frac{F}{\lambda g}\)。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时我对“上升吸积”与“下降脱离”的物理边界非常警觉：上升时桌面静止链节（初速 \(u=0\)）被拉入运动系，由密歇尔斯基方程 \(m\dot{v} = F_{\text{ext}} + (u - v)\dot{m}\) 知存在附加反冲力 \(-v\dot{m} = -\lambda v^2\)，合并即 \(\frac{d}{dx}(x^2 v^2) = \frac{2F}{\lambda}x - 2gx^2\)；而下降时，链节脱离悬垂段前后的瞬时速度同为 \(v\)（\(u = v\)），减速过程由桌面支持力在系统外完成，故 \((u-v)\dot{m} = 0\)，方程直接简化为 \(\lambda x v\frac{dv}{dx} = F - \lambda g x\)。两阶段对比一气呵成。
- **Phase 2 对照参考解答**：官方解答完全印证了这一核心物理图像，且在第 2 问保留了有限初长 \(x_0\) 的二次求根公式 \(x_{\max} = \frac{\sqrt{3(3F-2gx_0\lambda)(F+2gx_0\lambda)} + 3F - 2gx_0\lambda}{4g\lambda}\)。值得向竞赛生强调的是：为什么尽管恒力 \(F\) 和重力都是保守力，链条的往复振荡却会不断衰减？原因正在于“上升段拉起静止链节”以及“下降段链节撞击桌面停止”这两个过程都是完全非弹性碰撞，每个周期都会将宏观机械能不可逆地转化为内能（热能）！
- **核心难点**：
  - 难点1：识别一阶线性微分方程 \(x\frac{d(v^2)}{dx} + 2v^2 = \frac{2F}{\lambda} - 2gx\) 的积分因子 \(x\)，将其合并为 \(\frac{d}{dx}(x^2 v^2)\)。
  - 难点2：深刻理解上升阶段与下降阶段动力学方程的不对称性：上升有 \(+\lambda\dot{x}^2\) 耗散阻力项，而下降段满足 \(\lambda x\ddot{x} = F - \lambda g x\)。
- **高频易错点**：
  - 易错点1：在上升阶段误用机械能守恒 \(Fx - \frac{1}{2}\lambda g x^2 = \frac{1}{2}(\lambda x)v^2\)（这会算得 \(v^2 = \frac{2F}{\lambda} - gx\)，比正确结果大了整整一倍，因为忽略了非弹性拉起链节损失的一半动能！）。
  - 易错点2：在下降阶段直接套用 \(\frac{d}{dt}(\lambda x\dot{x}) = F - \lambda g x\)，忘记桌面会对正在落桌的链节提供向上冲击力 \(\dot{x}\frac{d}{dt}(\lambda x)\) 以使其停下。
- **教学核心结论**：处理一切链条、绳索、火箭等变质量问题时，必须严格使用广义变质量方程 \(m\frac{dv}{dt} = \mathbf{F}_{\text{ext}} + (\mathbf{u}_{\text{rel}})\frac{dm}{dt}\)：先判断微元 \(\Delta m\) 在并入或脱离主系统瞬间的相对速度 \(\mathbf{u}_{\text{rel}} = \mathbf{u} - \mathbf{v}\) 是否为零，切勿盲目写 \(\frac{d(mv)}{dt} = F\) 或机械能守恒！

---

### 7. 恒星观测：从衍射到干涉测量 (`plancks-2025-final-combined-slice-q7`)

- **物理模型**：夫琅禾费方形孔/屏衍射、巴比涅原理与迈克耳孙恒星干涉仪（空间相干性条纹可见度）
- **难度评级**：D2
- **核心标签**：`夫琅禾费衍射`、`巴比涅原理`、`瑞利判据`、`迈克耳孙恒星干涉仪`、`条纹可见度函数`

#### 题目拆解与求解脉络
1. **方形障碍物的夫琅禾费衍射与巴比涅原理**：边长为 \(l\) 的方形孔径在距离 \(D \gg l\) 屏幕上的远场衍射光强为：
   \[ I(x,y) = I_0 \left[\frac{\sin\left(\frac{\pi l x}{\lambda_c D}\right)}{\frac{\pi l x}{\lambda_c D}}\right]^2 \left[\frac{\sin\left(\frac{\pi l y}{\lambda_c D}\right)}{\frac{\pi l y}{\lambda_c D}}\right]^2. \]
   第一极小值位于 \(\theta_{\min, x} = \theta_{\min, y} = \frac{\lambda_c}{l}\)。由巴比涅原理，不透明方形障碍物的衍射复振幅在除原点（平面波聚焦点）外与方孔等大反号，故光强分布与极小值角位置完全相同。
2. **方形孔径望远镜分辨天狼星双星**：瑞利判据给出最小分辨角 \(\theta_{\text{RP}} = \frac{\lambda}{L} = \frac{550\times 10^{-9}\text{ m}}{2.4\text{ m}} \approx 2.3\times 10^{-7}\text{ rad}\)，远小于天狼星 A 与 B 的角距离 \(\Delta\theta = 10'' \approx 4.8\times 10^{-5}\text{ rad}\)，故可清晰分辨。
3. **迈克耳孙恒星干涉仪的条纹可见度**：一维均匀恒星（直径 \(b\)，距离 \(a\)）上坐标为 \(x' \in [-b/2, b/2]\) 的发光微元在屏幕 \(x\) 处产生的双缝光强为 \(dI = \frac{2I_0}{b}\left[1 + \cos\frac{2\pi d}{\lambda}\left(\frac{x}{D} + \frac{x'}{a}\right)\right]dx'\)。对非相干扩展光源积分得：
   \[ I(x) = 2I_0\left[1 + \frac{\sin\left(\frac{\pi b d}{a\lambda}\right)}{\frac{\pi b d}{a\lambda}}\cos\left(\frac{2\pi d x}{\lambda D}\right)\right] \implies V = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = \left|\frac{\sin\left(\frac{\pi b d}{a\lambda}\right)}{\frac{\pi b d}{a\lambda}}\right|. \]
4. **参宿四（Betelgeuse）的角直径与直径**：可见度第一极小值对应 \(\frac{\pi b d}{a\lambda} = \pi\)，故角直径为：
   \[ \theta = \frac{b}{a} = \frac{\lambda}{d} = \frac{570\times 10^{-9}\text{ m}}{3.08\text{ m}} \approx 1.85\times 10^{-7}\text{ rad}, \quad b = a\theta \approx 1.6\times 10^{18}\text{ m}\times 1.85\times 10^{-7} \approx 2.96\times 10^{11}\text{ m}. \]

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解第 1 问时，我特别留意到题干问的是“不透明方形物体（opaque square object）”而非方形孔径，且询问“是否存在亮斑（Is there a bright spot?）”。严格来讲，泊松亮斑属于菲涅耳近场衍射效应；而在题设强制要求的夫琅禾费远场近似下，由巴比涅原理，障碍物衍射场等于平面波 \(\delta\) 函数减去方孔衍射场，因此对 \(x,y \neq 0\) 光强分布就是 \(I_0 \operatorname{sinc}^2\left(\frac{\pi l x}{\lambda_c D}\right)\operatorname{sinc}^2\left(\frac{\pi l y}{\lambda_c D}\right)\)，第一极小值位于 \(\theta_x = \theta_y = \lambda_c/l\)。第 3、4 问直接对扩展光源积分（空间相干性的范西特-泽尼克定理一维特例）即可。
- **Phase 2 对照参考解答**：对照官方解答，命题人正是先按边长为 \(L\)（题干记为 \(l\)）的方孔算出 \(I(x,y) \propto \operatorname{sinc}^2\left(\frac{\pi x l}{\lambda D}\right)\operatorname{sinc}^2\left(\frac{\pi y l}{\lambda D}\right)\) 并回答中心有亮斑、第一极小在 \(\lambda/l\)，随后引用巴比涅原理说明不透明方屏在原点以外振幅反号、强度分布与极小值位置不变。这种处理在竞赛评分中非常典型：既考察了标准方孔夫琅禾费积分，又考察了巴比涅原理的物理概念。
- **核心难点**：
  - 难点1：理解巴比涅原理在夫琅禾费衍射中的数学表述：互补屏的衍射场之和等于无遮挡自由传播场。
  - 难点2：在迈克耳孙恒星干涉仪中，正确写出扩展光源上偏离光轴 \(x'\) 的发光微元入射到双缝时的附加光程差 \(\Delta_1 = \frac{x' d}{a}\)，并对非相干光源做**光强积分**而非振幅积分。
- **高频易错点**：
  - 易错点1：混淆方形孔径的瑞利分辨角 \(\theta_{\text{RP}} = \frac{\lambda}{L}\) 与圆形孔径的 \(1.22\frac{\lambda}{D}\)。
  - 易错点2：将恒星上不同位置的发光点当作相干光源叠加复振幅（恒星表面不同点发光彼此独立非相干，必须先求单点产生的双缝干涉光强，再对光源坐标 \(x'\) 积分光强！）。
- **教学核心结论**：迈克耳孙恒星干涉仪是范西特-泽尼克定理（Van Cittert-Zernike Theorem）的经典体现：扩展非相干光源的空间相干度（即双缝干涉条纹可见度 \(V\)）恰好等于光源强度角分布的傅里叶变换；利用长基线 \(d\) 测可见度第一零点 \(\theta = \lambda/d\)，可用小孔径双缝突破单镜孔径限制测量恒星角直径。

---

### 8. 石墨烯纳米带 (`plancks-2025-final-combined-slice-q8`)

- **物理模型**：扶手椅型石墨烯纳米带（Armchair Graphene Nanoribbon）的紧束缚模型能带与一维态密度
- **难度评级**：D3
- **核心标签**：`石墨烯纳米带`、`紧束缚近似TBA`、`布洛赫定理`、`能隙打开机制`、`范霍夫奇点与一维态密度`

#### 题目拆解与求解脉络
1. **原胞与布洛赫波函数**：一维扶手椅型链的原胞包含 4 个碳原子（编号 \(j = 1,2,3,4\)），电子波函数为 \(\psi_k(x) = \sum_{j=1}^4 \zeta_j \psi_j^k(x)\)，其中 \(\psi_j^k(x) = \frac{1}{\sqrt{N_c}}\sum_{n=1}^{N_c} e^{ik(x+na)}\phi_j(x+na)\)。
2. **紧束缚哈密顿矩阵与本征能带**：计入原胞内跃迁 \(\gamma\)（\(1\leftrightarrow 2, 3\leftrightarrow 4\)）、\(\gamma_e\)（\(2\leftrightarrow 3\)）及跨原胞跃迁 \(\gamma_e e^{\mp ika}\)（\(1\leftrightarrow 4\)），哈密顿矩阵为：
   \[ H(k) = \begin{pmatrix} 0 & \gamma & 0 & \gamma_e e^{-ika} \\ \gamma & 0 & \gamma_e & 0 \\ 0 & \gamma_e & 0 & \gamma \\ \gamma_e e^{ika} & 0 & \gamma & 0 \end{pmatrix}. \]
   展开行列式 \(\det(H(k) - \varepsilon_k I) = 0\) 得双二次方程 \(\varepsilon_k^4 - 2(\gamma^2+\gamma_e^2)\varepsilon_k^2 + (\gamma^4 + \gamma_e^4 - 2\gamma^2\gamma_e^2\cos ka) = 0\)，解得四条能带：
   \[ \varepsilon_k = \pm\sqrt{\gamma^2 + \gamma_e^2 \pm \sqrt{2}\gamma\gamma_e\sqrt{1+\cos ka}} = \pm\sqrt{\gamma^2 + \gamma_e^2 \pm 2\gamma\gamma_e\cos\left(\frac{ka}{2}\right)}. \]
3. **\(\Gamma\) 点能隙与一维态密度（DOS）**：在 \(k=0\) 处，四条能带能量为 \(\pm(\gamma_e \pm \gamma)\)，代入 \(\gamma = -2.70\text{ eV}, \gamma_e = -3.02\text{ eV}\) 得导带底与价带顶能隙 \(E_{\text{gap}} = 2||\gamma_e| - |\gamma|| = 0.64\text{ eV}\)（若 \(\gamma = \gamma_e\) 则能隙闭合为 0）。在一维中 \(g(E) = \frac{2}{\pi}\left|\frac{dE}{dk}\right|^{-1} \propto \frac{1}{\sin(ka)}\)，故在 \(k \to 0\) 的能带极值点处态密度出现典型的一维范霍夫发散峰（\(g(E) \propto |E - E_0|^{-1/2}\)）。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，写出 \(4\times 4\) 矩阵后，如果只求第 4 问 \(\Gamma\) 点（\(k=0\)）的本征值，我发现无需展开四阶行列式，直接利用空间反演对称性（将原子序号 \((1,2,3,4)\) 翻转成 \((4,3,2,1)\) 哈密顿量不变）令本征矢满足宇称 \(\zeta_4 = \pm\zeta_1, \zeta_3 = \pm\zeta_2\)，\(4\times 4\) 矩阵立刻对角化为两个 \(2\times 2\) 矩阵 \(\begin{pmatrix} \pm\gamma_e & \gamma \\ \gamma & \pm\gamma_e \end{pmatrix}\)，心算即得四个本征值为 \(\pm\gamma_e \pm\gamma\)，能隙 \(E_{\text{gap}} = 2||\gamma_e| - |\gamma|| = 2\times(3.02 - 2.70) = 0.64\text{ eV}\)！而为了第 6 问画全布里渊区能带，再展开双二次特征方程求出完整 \(\varepsilon_k\) 即可。
- **Phase 2 对照参考解答**：官方解答直接通过拉普拉斯展开求出了任意 \(k\) 下的四阶行列式 \(\varepsilon_k^4 - 2(\gamma^2+\gamma_e^2)\varepsilon_k^2 + \gamma^4 + \gamma_e^4 - 2\gamma^2\gamma_e^2\cos(ka) = 0\)，并利用 \(2\cos^2(ka/2) = 1+\cos(ka)\) 优雅地将根号内配方为 \(\varepsilon_k = \pm\sqrt{\gamma^2 + \gamma_e^2 \pm 2\gamma\gamma_e\cos(ka/2)}\)（因此 \(k=0\) 时恰为 \(\pm\sqrt{(\gamma \pm \gamma_e)^2} = \pm(\gamma \pm \gamma_e)\)，注意官方解答代入数值时多保留了一位小数写成了 0.648 eV，准确值为 \(2\times(3.02-2.70) = 0.640\text{ eV}\)）。两种方法相得益彰：对称性降阶法适合秒杀高对称点能隙，双二次方程配方法适合求全谱色散。
- **核心难点**：
  - 难点1：准确区分原胞内跃迁（无相位因子 \(e^{\pm ika}\)）与跨原胞跃迁（带布洛赫相位因子 \(e^{\pm ika}\)），正确构建厄米矩阵 \(H(k)\)。
  - 难点2：在求解四阶本征值方程时，识别出它是关于 \(\varepsilon_k^2\) 的双二次方程，并利用倍角公式 \(\sqrt{1+\cos(ka)} = \sqrt{2}\cos(ka/2)\) 化简重根号。
- **高频易错点**：
  - 易错点1：将原胞内 \(2\leftrightarrow 3\) 的连接误加上 \(e^{\pm ika}\) 相位因子，或把 \(H_{14}\) 与 \(H_{41}\) 的共轭相位写同号（违背厄米性 \(H_{41} = H_{14}^*\)）。
  - 易错点2：画一维态密度（DOS）随能量变化图时，漏掉能带极值点（\(k=0\) 和 \(k=\pi/a\) 处群速度 \(v_g = \frac{1}{\hbar}\frac{dE}{dk} = 0\)）的一维范霍夫发散峰。
- **教学核心结论**：固体物理紧束缚模型（TBA）在竞赛中的核心套路是：1. 选定最小周期原胞（含 \(M\) 个不等价原子）；2. 写出 \(M\times M\) 动量空间矩阵 \(H_{ij}(k) = \sum_{\Delta n} t_{ij}(\Delta n)e^{ik\Delta n a}\)；3. 在高对称点（\(k=0\) 或 \(k=\pi/a\)）优先利用镜像/反演对称性将矩阵降阶对角化。

---

### 9. 量子 Grover 算法与经典碰撞 (`plancks-2025-final-combined-slice-q9`)

- **物理模型**：量子 Grover 搜索算法与一维弹性碰撞（Galperin 台球/山地列车模型）的数学同构
- **难度评级**：D3
- **核心标签**：`Grover量子搜索算法`、`SO(2)旋转算符`、`一维完全弹性碰撞`、`动能重标度空间`、`质量比量子化条件`

#### 题目拆解与求解脉络
1. **Grover 迭代算符的旋转矩阵表示**：在 \(\{|\alpha\rangle, |w\rangle\}\) 基下，\(|\psi_0\rangle = \left(\sqrt{\frac{N-1}{N}}, \frac{1}{\sqrt{N}}\right)^T = \left(\cos\frac{\theta}{2}, \sin\frac{\theta}{2}\right)^T\)，反射算符 \(K = 2|\psi_0\rangle\langle\psi_0| - I\) 与 \(U = \text{diag}(1,-1)\) 乘积为：
   \[ G(\theta) = KU = \begin{pmatrix} \frac{N-2}{N} & -\frac{2\sqrt{N-1}}{N} \\ \frac{2\sqrt{N-1}}{N} & \frac{N-2}{N} \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \quad \sin\frac{\theta}{2} = \frac{1}{\sqrt{N}}. \]
2. **精确搜索条件与渐近复杂度**：作用 \(n\) 次后 \(G^n|\psi_0\rangle = \left(\cos\left(n+\frac{1}{2}\right)\theta, \sin\left(n+\frac{1}{2}\right)\theta\right)^T\)。命中 \(|w\rangle = (0,1)^T\) 要求 \(\left(n+\frac{1}{2}\right)\theta = \frac{\pi}{2}\)，即：
   \[ N = \frac{1}{\sin^2\left(\frac{\pi}{2(2n+1)}\right)} \quad (n=1 \implies N=4), \qquad N \gg 1 \implies n \approx \frac{\pi}{4}\sqrt{N}. \]
3. **经典列车弹性碰撞的同构映射**：令 \(\xi_i = \sqrt{\frac{m_i}{M}}v_i\)（\(M = m_1+m_2, \eta = \frac{m_1}{m_2}\)），动能守恒化为 \(\xi_1^2 + \xi_2^2 = 1\)，初态（\(v_1=v_2=1\)）为 \(\vec{\xi}_0 = \left(\sqrt{\frac{\eta}{\eta+1}}, \frac{1}{\sqrt{\eta+1}}\right)^T = \left(\cos\frac{\theta}{2}, \sin\frac{\theta}{2}\right)^T\)（对应 \(N = \eta + 1\)）。车厢碰墙反号对应 \(U = \text{diag}(1,-1)\)，两车弹性碰撞对应矩阵 \(S = \begin{pmatrix} \frac{\eta-1}{\eta+1} & \frac{2\sqrt{\eta}}{\eta+1} \\ \frac{2\sqrt{\eta}}{\eta+1} & -\frac{\eta-1}{\eta+1} \end{pmatrix}\)，单轮复合变换恰为 \(SU = G(\theta)\)，其中 \(\eta = \cot^2(\theta/2)\)。
4. **“停靠-购物-接回”现象的质量比与时间**：要求经历 \(n\) 轮碰撞后车厢静止（\(\xi_2 = 0\)）且机车反向冲上山坡（\(\xi_1 = -1\)），需满足：
   \[ \left(n + \frac{1}{2}\right)\theta = \pi \implies \theta_n = \frac{2\pi}{2n+1} \implies \eta_n = \cot^2\left(\frac{\pi}{2n+1}\right). \]
   因 \(m_1 > m_2\)（\(\eta > 1\)），舍去 \(n=1\)（\(\eta_1 = 1/3\)），最小质量比取 \(n=2\)：
   \[ \eta_{\min} = \eta_2 = \cot^2\left(\frac{\pi}{5}\right) = 1 + \frac{2}{\sqrt{5}} \approx 1.894. \]
   此时机车初速为 \(v'_1 = \sqrt{\frac{1+\eta}{\eta}}\)，在斜面上往返耗时 \(T' = 2\sqrt{\frac{1+\eta}{\eta}}T = 2(\sqrt{5}-1)T \approx 2.47 T\)。机车返回谷底后以 \(\vec{\xi}^{(2)} = (1,0)^T\) 触发逆序碰撞 \((US)^2 = G(-2\theta)\)，最终两车以 \(v_1 = v_2 = -1\) 同步返回山顶。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时第 1–4 问非常顺利：一旦令 \(\cos(\theta/2) = \sqrt{\frac{N-1}{N}} = \sqrt{\frac{\eta}{\eta+1}}, \sin(\theta/2) = \frac{1}{\sqrt{N}} = \frac{1}{\sqrt{\eta+1}}\)，两个平面反射 \(U\) 与 \(K\)（或 \(S\)）的乘积在几何上必然是两反射轴夹角 \(\theta/2\) 两倍（即 \(\theta\)）的纯旋转！但在第 5 问求“使车厢静止的最小质量比 \(\eta > 1\)”时，需要特别小心终态矢量的方向：量子 Grover 算法要求旋转到 \((0, 1)^T\)（即 \((n+1/2)\theta = \pi/2\)），而经典列车问题要求**车厢静止**（\(\xi_2 = 0\)）且**机车向上退回**（\(\xi_1 = -1\)），即旋转到 \((-1, 0)^T\)！这给出 \((n+1/2)\theta = \pi \implies \frac{\theta}{2} = \frac{\pi}{2n+1}\)。当 \(n=1\) 时 \(\eta_1 = \cot^2(\pi/3) = 1/3 < 1\) 不合题意；故满足 \(\eta > 1\) 的最小解对应 \(n=2\) 次碰撞，即 \(\eta_2 = \cot^2(\pi/5) = 1 + \frac{2}{\sqrt{5}} \approx 1.894\)！
- **Phase 2 对照参考解答**：与官方解答对照，我们在第 5 问捕捉到的“终态是 \((-1,0)^T\) 而非 \((0,1)^T\)，且 \(n=1\) 给出 \(\eta=1/3 < 1\) 必须舍去、需取 \(n=2\) 得到 \(\eta = \cot^2(\pi/5) = 1 + 2/\sqrt{5}\)”这一关键转折与官方解答丝毫不差！此外在第 7 问中，当机车从山上滑回谷底（此时初态为 \((1,0)^T\)）先撞静止车厢再由车厢撞墙时，单步算符顺序反转为 \(US = (SU)^{-1} = G(-\theta)\)，经历同样的 2 轮碰撞后状态变为 \(G(-2\theta)(1,0)^T = (\cos(4\pi/5), -\sin(4\pi/5))^T = -(\cos(\pi/5), \sin(\pi/5))^T\)，即机车与车厢恰好恢复等速 \(v_1 = v_2 = -1\) 一起开回山顶！物理图像之精妙令人拍案叫绝。
- **核心难点**：
  - 难点1：理解“两个镜像反射算符 \(K\) 和 \(U\) 的乘积等于二倍夹角的旋转算符 \(G(\theta)\)”这一核心几何图像，快速写出 \(G^n|\psi_0\rangle\)。
  - 难点2：在第 5 问中准确区分 Grover 搜索目标态 \((0,1)^T\) 与列车停靠目标态 \((-1,0)^T\)，并发现 \(n=1\) 时 \(\eta = 1/3 < 1\) 违背 \(m_1 > m_2\)，从而推进到 \(n=2\) 求出 \(\cot^2(\pi/5)\)。
- **高频易错点**：
  - 易错点1：直接把第 2 问的 \(N=4 \implies \eta = 3\) 当作第 5 问的答案（\(\eta = 3\) 对应终态 \(\xi = (0,1)^T\)，即机车静止而车厢独自反弹，与题设“车厢停在站台、机车冲上山坡”恰好相反！）。
  - 易错点2：在第 6 问计算购物时间时，只算了机车上坡时间 \(\sqrt{\frac{1+\eta}{\eta}}T\)，忘了机车到达最高点后还要滑回谷底站台，总时间为往返的 2 倍。
- **教学核心结论**：将一维双物体弹性碰撞通过质量平方根重标度 \(\xi_i = \sqrt{m_i}\,v_i\) 映射为二维相空间圆上的等距反射/旋转，是解决一切多体连续碰撞计数问题（如 Galperin 台球算 \(\pi\)、费米加速模型、Grover 经典模拟）的终极利器！

---

## 第二部分：PLANCKS 2026 国际决赛（Q1–Q9）

### 10. 麦圈效应：早餐物理 (`plancks-2026-final-problem-slice-q1`)

- **物理模型**：麦圈效应（Cheerios Effect）：液面漂浮球体的毛细弯月面形变与毛细相互作用力
- **难度评级**：D3
- **核心标签**：`麦圈效应`、`表面张力与接触角`、`广义阿基米德浮力`、`修正贝塞尔函数`、`毛细吸引与排斥`

#### 题目拆解与求解脉络
1. **漂浮球体的竖直力平衡**：球体受重力 \(F_g = -\frac{4}{3}\pi R^3\rho_c g\)、广义阿基米德浮力 \(F_b = \rho_m g V_{\text{dis}}\) 以及三相接触线（半径 \(r_c = R\sin\phi_c\)）处表面张力的竖直分量 \(F_{\gamma, z} = 2\pi R\gamma\sin\phi_c \frac{h'_c}{\sqrt{1+{h'_c}^2}}\)。令 \(F_g + F_b + F_{\gamma, z} = 0\) 并引入邦德数 \(B = \frac{\rho_m g R^2}{\gamma}\) 与密度比 \(D = \frac{\rho_c}{\rho_m}\)，得：
   \[ \sin(\phi_c)\frac{h'_c}{\sqrt{1+{h'_c}^2}} = B\left(\frac{2D-1}{3} + \frac{1}{2}\cos\phi_c - \frac{1}{6}\cos^3\phi_c + \frac{h_c}{2R}\sin^2\phi_c\right). \]
2. **小形变近似与无量纲净浮重 \(\Sigma\)**：当 \(h_c \ll R, |h'_c| \ll 1\) 时，由几何关系 \(\phi_c = \pi - \theta - \arctan h'_c \approx \pi - \theta\) 得 \(\cos\phi_c \approx -\cos\theta\)，方程简化为：
   \[ \sin(\phi_c)h'_c = B\Sigma, \qquad \Sigma = \frac{2D-1}{3} - \frac{1}{2}\cos\theta + \frac{1}{6}\cos^3\theta. \]
3. **两麦圈间的毛细相互作用能与吸引力**：单颗麦圈在远处激发的液面形变为 \(h(r) = -h'_c\sin\phi_c R K_0(r/L) = -B\Sigma R K_0(r/L)\)（其中毛细长度 \(L = \sqrt{\gamma/(\rho_m g)} = R/\sqrt{B}\)）。另一颗麦圈的表观净浮重为 \(2\pi\gamma R B\Sigma\)，故相距 \(\ell\) 时的引力势能改变量与水平相互作用力为：
   \[ E(\ell) = -2\pi\gamma R^2 B^2 \Sigma^2 K_0\left(\frac{\ell}{L}\right), \qquad F(\ell) = -\frac{dE}{d\ell} = -\frac{2\pi\gamma R^2 B^2 \Sigma^2}{L}K_1\left(\frac{\ell}{L}\right) = -2\pi\gamma R B^{5/2}\Sigma^2 K_1\left(\frac{\ell}{L}\right) < 0. \]
   因 \(K_1(\ell/L) > 0\)，两麦圈恒相互吸引。
4. **麦圈与图钉的异号毛细排斥**：重图钉（\(\rho_p > \rho_m\)）使液面下凹（\(\Sigma_p > 0\)），而轻麦圈使液面上凸（\(\Sigma_c < 0\)）。麦圈趋向液面高处以降低势能，图钉趋向液面低处以降低势能，故两者相互排斥（\(E_{12} \propto -\Sigma_1\Sigma_2 K_0(\ell/L) > 0\)）。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，第 1 问的关键是看清图 1(c) 中液面斜率 \(h'_c = \left.\frac{dh}{dr}\right|_{r_c} < 0\) 的符号：当液面靠近球体向上抬升时，随 \(r\) 增大 \(h(r)\) 减小，故 \(h'_c < 0\)，此时沿液面切向朝外的表面张力 \(\gamma\) 具有**向下**的竖直分量 \(F_{\gamma,z} = 2\pi R\sin\phi_c \cdot \gamma \frac{h'_c}{\sqrt{1+{h'_c}^2}} < 0\)。将其与重力、浮力相加令为 0，移项即得题目所证公式。第 2 问由球面切线角与接触角 \(\theta\) 的几何关系 \(\phi_c \approx \pi - \theta\) 代入 \(\cos\phi_c = -\cos\theta\) 立刻得到 \(\Sigma\)。第 3、4 问直接用阿基米德净浮力与液面高度 \(h(\ell)\) 相乘即得势能与吸引力。
- **Phase 2 对照参考解答**：对照官方解答，全部推导步骤一致（顺便指出官方解答第 2 问打印时有一处微小笔误：将 \(\frac{1}{6}\cos^3\theta\) 误印为 \(\frac{1}{6}\cos^2\theta\)，以及第 4 问把 \(\frac{R^2 B^2}{L} = R B^{5/2}\) 多写了一个 \(R\) 印成 \(R^2 B^{5/2}\)，我们在教学中应给出量纲完全正确的表达式 \(F(\ell) = -\frac{2\pi\gamma R^2 B^2 \Sigma^2}{L}K_1(\ell/L) = -2\pi\gamma R B^{5/2}\Sigma^2 K_1(\ell/L)\)）。第 5 问官方解答给出的“同号毛细荷吸引、异号毛细荷排斥（\(\Sigma_1 \Sigma_2 < 0\)）”的物理图像非常精彩。
- **核心难点**：
  - 难点1：准确建立接触角 \(\theta\)、球极角 \(\phi_c\) 与液面倾角 \(\arctan h'_c\) 之间的几何关系 \(\phi_c = \pi - \theta - \arctan h'_c\)，从而在小斜率下利用 \(\cos(\pi-\theta) = -\cos\theta\) 翻转符号。
  - 难点2：理解为什么球 1 在球 2 的弯月面上移动时，其有效势能变化等于“球 1 的净浮重 \(2\pi\gamma R B\Sigma\)”乘以“球 2 在该处造成的液面抬升 \(h(\ell)\)”（类似于静电学中的点电荷在另一电荷电势中的相互作用能 \(E = q_1 \phi_2(\ell)\)）。
- **高频易错点**：
  - 易错点1：在计算表面张力竖直分量时，把接触线周长误写为大圆周长 \(2\pi R\) 而漏掉因子 \(\sin\phi_c\)。
  - 易错点2：对 \(E(\ell) = -2\pi\gamma R^2 B^2 \Sigma^2 K_0(\ell/L)\) 关于 \(\ell\) 求导时，忘记内层函数 \(\ell/L\) 求导会产生因子 \(1/L = \sqrt{\rho_m g/\gamma} = \sqrt{B}/R\)，导致力的量纲出错。
- **教学核心结论**：毛细相互作用（Cheerios effect）可以完美类比二维静电相互作用：每个漂浮物相当于一个“毛细单极荷” \(Q_i = 2\pi R_i B_i \Sigma_i\)，它在液面上激发屏蔽泊松方程（亥姆霍兹方程 \(\nabla^2 h - L^{-2}h = 0\)）的格林函数势 \(h(r) \propto -Q_i K_0(r/L)\)，两物体间的相互作用能 \(E_{12} = -2\pi\gamma Q_1 Q_2 K_0(\ell/L)\) 满足“同号相吸（两个麦圈或两个图钉）、异号相斥（麦圈与图钉）”！

---

### 11. 部分相干性与三维成像 (`plancks-2026-final-problem-slice-q2`)

- **物理模型**：光学相干断层扫描（OCT）：部分相干光迈克耳孙干涉仪、洛伦兹谱相干长度与单光子干涉
- **难度评级**：D2
- **核心标签**：`光学相干断层扫描OCT`、`一阶时间相干度`、`维纳-辛钦定理`、`条纹可见度`、`单光子自干涉`

#### 题目拆解与求解脉络
1. **单层半反界面的最大干涉可见度**：界面 \(A_1\) 功率反射率为 \(R_1 = 0.5\)，对应振幅反射系数 \(r_1 = \sqrt{0.5}\)。探测器输出功率为 \(P_D(\tau) \propto r_1^2 + 1 + 2r_1 e^{-|\tau|/\tau_c}\cos(\omega_0\tau)\)。在零延迟（\(\tau = 0\)）附近，最大条纹可见度为：
   \[ V_{\max} = \frac{P_{\max} - P_{\min}}{P_{\max} + P_{\min}} = \frac{2r_1}{1 + r_1^2} = \frac{2\sqrt{0.5}}{1 + 0.5} = \frac{2\sqrt{2}}{3} \approx 0.943. \]
2. **双层界面的 OCT 干涉图（无滤光片）**：光源中心波长 \(\lambda_0 = 1300\text{ nm}\)，谱宽 \(\Delta\lambda = 10\text{ nm}\)，相干时间 \(\tau_c = \frac{\lambda_0^2}{\pi c\Delta\lambda} \approx 0.18\text{ ps}\)，对应参考镜位移衰减半宽 \(x_c = \frac{c\tau_c}{2} = \frac{\lambda_0^2}{2\pi\Delta\lambda} \approx 26.9\ \mu\text{m}\)。由于两界面间距 \(\Delta y = 250\ \mu\text{m} \gg x_c\)，干涉图呈现中心位于 \(x=0\) 和 \(x=250\ \mu\text{m}\) 的两个完全分离的对称指数包络波包；第二个波包因往返穿过 \(A_1\)（有效振幅 \(t_1^2 r_2 = 0.5\sqrt{0.5} \approx 0.354 < r_1\)），其调制度明显低于第一个波包。
3. **窄带滤光片效应、轴向分辨率与单光子源**：插入 \(\Delta\lambda = 1\text{ nm}\) 的滤光片后，\(x_c\) 增大 10 倍至 \(269\ \mu\text{m} > \Delta y\)，导致两个干涉波包展宽并相互重叠。由此可知：要提高 OCT 轴向深度分辨率，必须采用**光谱更宽**的光源。若换用相同光谱的单光子源与单光子探测器，每个光子发生路径自干涉，累积大量光子计数后得到的干涉图与经典光场完全一致。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，第 1 问直接注意区分“功率反射率 \(R_1 = |r_1|^2 = 0.5\)”与“电场振幅反射率 \(r_1 = 1/\sqrt{2}\)”，代入双光束干涉可见度公式 \(V = \frac{2\sqrt{I_A I_B}}{I_A + I_B} = \frac{2\sqrt{0.5}}{1 + 0.5} = \frac{2\sqrt{2}}{3} \approx 0.943\)。第 2 问算出 \(x_c = \frac{\lambda_0^2}{2\pi\Delta\lambda} \approx 27\ \mu\text{m} \ll 250\ \mu\text{m}\)，同时注意第二层界面反射光需先透射过 \(A_1\)（\(T_1 = 0.5\)）、在 \(A_2\) 反射（\(R_2 = 0.5\)）、再透射回 \(A_1\)（\(T_1 = 0.5\)），故有效功率反射率为 \(0.5^3 = 0.125\)，振幅系数为 \(0.5^{3/2} = \frac{1}{2\sqrt{2}}\)，画图时第二个干涉峰包络明显低于第一个峰。第 3–5 问概念极为清晰。
- **Phase 2 对照参考解答**：官方解答的推导与我们的盲解完全吻合，且给出了清晰的数值对比图（图 1(a)(b)(c)）。特别值得注意的是官方解答在第 3 问强调的线性光学原理：为什么滤光片 \(F\) 放在探测器 \(D\) 正前方（合束之后）与放在光源正后方（分束之前）效果完全一样？因为干涉仪和滤光片都是线性时不变系统，探测器测得的总功率谱等于光源功率谱乘以干涉仪传递函数再乘以滤光片透射谱，算符顺序可交换！
- **核心难点**：
  - 难点1：准确区分功率反射率 \(R_1 = 0.5\) 与电场振幅反射率 \(r_1 = \sqrt{0.5}\)，以及第二层界面 \(A_2\) 反射回探测器的电场需经历两次 \(A_1\) 透射和一次 \(A_2\) 反射（振幅为 \(t_1^2 r_2 = 0.5\sqrt{0.5}\)）。
  - 难点2：将时间域的相干衰减因子 \(e^{-|\tau|/\tau_c}\)（其中 \(\tau = -2x/c\)）转化为空间扫描域的衰减长度 \(x_c = \frac{c\tau_c}{2} = \frac{\lambda_0^2}{2\pi\Delta\lambda}\)。
- **高频易错点**：
  - 易错点1：在第 1 问误将功率反射率 \(0.5\) 当作振幅比代入，算得错误的 \(V = \frac{2\times 0.5}{1 + 0.5^2} = 0.8\)。
  - 易错点2：直觉上误以为“相干性越好（谱线越窄）成像分辨率越高”——在 OCT 深度断层扫描中恰恰相反，它是利用“低相干干涉（白光干涉）”进行飞行时间门控定位，因此**光谱越宽、相干长度越短，轴向深度分辨率越高**！
- **教学核心结论**：迈克耳孙干涉仪输出的干涉项是光源自相关函数 \(g^{(1)}(\tau)\)，由维纳-辛钦定理（Wiener-Khinchin theorem）知它是光源功率谱的傅里叶变换：光谱宽度 \(\Delta\omega\) 越宽，时间相干包络 \(\tau_c \sim 1/\Delta\omega\) 越窄，空间深度定位精度 \(x_c = c\tau_c/2\) 就越高——这正是光学相干断层扫描（OCT）获得微米级纵向分辨率的物理精髓。

---

### 12. 木管乐器 (`plancks-2026-final-problem-slice-q3`)

- **物理模型**：木管乐器声学：声波方程、圆柱管与圆锥管驻波谐频、喇叭口阻抗匹配及声电类比（高通音孔）
- **难度评级**：D2
- **核心标签**：`木管乐器声学`、`绝热声速推导`、`圆锥管球面波`、`声学阻抗匹配`、`声电类比与音孔滤波`

#### 题目拆解与求解脉络
1. **声波方程与绝热近似判据**：联立绝热条件 \(\frac{\Delta p}{p_0} = -\gamma\frac{\Delta V}{V_0} = -\gamma\nabla\cdot\boldsymbol{\xi}\) 与牛顿第二定律 \(\rho_0\frac{\partial^2\boldsymbol{\xi}}{\partial t^2} = -\nabla p\)，消去位移 \(\boldsymbol{\xi}\) 得 \(\frac{\partial^2 p}{\partial t^2} = c^2\nabla^2 p\)，其中声速 \(c = \sqrt{\frac{\gamma p_0}{\rho_0}}\)。由于热传导项 \(|\partial_t Q| \propto |\nabla^2 T| \sim k^2\Delta T = \frac{\omega^2}{c^2}\Delta T\)，而内能变化率 \(\rho_0 C_v |\partial_t T| \sim \omega\Delta T\)，故在低频 \(\omega \ll \omega_0\) 下绝热假设极好成立。
2. **三类木管乐器的驻波本征频率**：
   - **长笛**（两端开口圆柱管，\(p(0)=p(L)=0\)）：\(p(x) \propto \sin(kx)\)，\(k_n = \frac{n\pi}{L} \implies f_n = \frac{nc}{2L}\)（\(n=1,2,3,\dots\)）；
   - **单簧管**（一端闭合一端开口圆柱管，\(p'(0)=0, p(L)=0\)）：\(p(x) \propto \cos(kx)\)，\(k_n = \frac{(2n-1)\pi}{2L} \implies f_n = \frac{(2n-1)c}{4L}\)；
   - **萨克斯管**（一端闭合一端开口圆锥管）：球对称波动解为 \(p(r,t) = \frac{A\sin(kr)}{r}\cos(\omega t+\phi)\)（在锥顶 \(r\to 0\) 处自动满足声压有限且梯度为零），由开口端 \(p(L)=0 \implies \sin(kL)=0\) 得 \(f_n = \frac{nc}{2L}\)，具备完整的偶次与奇次泛音！
3. **簧片正反馈与喇叭口阻抗匹配**：吹奏时唯有管体共振频率能形成驻波，驻波在吹口处（压力波腹）周期性张闭簧片形成正反馈锁相放大。声阻抗 \(Z = \frac{\rho c}{A}\)，无喇叭口时功率透射率为 \(T_0 = 1 - \left(\frac{Z_{\text{tube}}-Z_{\text{end}}}{Z_{\text{tube}}+Z_{\text{end}}}\right)^2 \approx \frac{4Z_{\text{end}}}{Z_{\text{tube}}}\)。加入面积翻倍（\(Z' = Z_{\text{tube}}/2\)）的喇叭口后，两次透射率乘积为：
   \[ T_{\text{bell}} = \left[1 - \left(\frac{1 - 1/2}{1 + 1/2}\right)^2\right]\cdot \frac{4 Z_{\text{end}}}{Z_{\text{tube}}/2} = \frac{8}{9}\cdot \frac{8 Z_{\text{end}}}{Z_{\text{tube}}} = \frac{64}{9}\frac{Z_{\text{end}}}{Z_{\text{tube}}} = \frac{16}{9}T_0. \]
4. **声电类比与音孔高通滤波**：管内空气质量赋予气流惯性（\(\Delta p \propto \frac{dI}{dt}\)），对应于**电感**；管壁摩擦耗散对应**电阻**；腔体可压缩性或弹性管壁对应**电容**。打开的音孔相当于并联接地小电感 \(L_h\)：低频声波被音孔短路反射（有效截断管长），高频声波因感抗 \(\omega L_h\) 很大而直接越过音孔继续向下传播，故音孔表现为**高通滤波器**。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时最令人惊艳的是第 3 问萨克斯管（圆锥管）的谐频计算：为什么一端闭合（簧片端）的圆锥管，其基频与泛音竟然和两端开口的圆柱管（长笛）一样是 \(f_n = \frac{nc}{2L}\)？利用球坐标径向拉普拉斯算符 \(\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial p}{\partial r}\right) = \frac{1}{r}\frac{\partial^2(rp)}{\partial r^2}\)，球面驻波通解为 \(p(r) = \frac{A\sin(kr) + B\cos(kr)}{r}\)。在锥顶 \(r \to 0\) 处要求声压有限（\(B=0\)），此时 \(p(r) = A\frac{\sin(kr)}{r} \approx Ak\left(1 - \frac{1}{6}k^2 r^2\right)\)，自动满足闭端边界条件 \(\left.\frac{\partial p}{\partial r}\right|_{r=0} = 0\)！而管口 \(r=L\) 处开口 \(p(L)=0 \implies \sin(kL)=0 \implies k = \frac{n\pi}{L}\)，一举解开谜题！
- **Phase 2 对照参考解答**：官方解答与我们的盲解完全一致。在第 5 问计算喇叭口辐射功率时，无喇叭口单界面透射率为 \(T_0 = 1 - \left(\frac{Z_1 - Z_{\text{end}}}{Z_1 + Z_{\text{end}}}\right)^2 = \frac{4 Z_1 Z_{\text{end}}}{(Z_1 + Z_{\text{end}})^2} \approx \frac{4 Z_{\text{end}}}{Z_1}\)；加入阻抗为 \(Z_2 = Z_1/2\) 的喇叭口后，两次透射率相乘为 \(T_{\text{bell}} = \frac{4 Z_1 (Z_1/2)}{(Z_1 + Z_1/2)^2} \cdot \frac{4 (Z_1/2) Z_{\text{end}}}{(Z_1/2 + Z_{\text{end}})^2} \approx \frac{8}{9} \cdot \frac{8 Z_{\text{end}}}{Z_1} = \frac{64}{9}\frac{Z_{\text{end}}}{Z_1} = \frac{16}{9}T_0\)（注意官方解答第 2661 行中间步骤把分子的因子 4 漏印成了 2，但最终结果 \(\frac{64}{9}\frac{Z_{\text{end}}}{Z_{\text{tube}}} = \frac{16}{9}T_0\) 完全正确）。
- **核心难点**：
  - 难点1：理解球面驻波 \(p(r) = A\frac{\sin(kr)}{r}\) 在锥顶 \(r=0\) 处既不为零（是压力波腹 \(p(0) = Ak\)）、又满足法向梯度为零（\(\left.\frac{\partial p}{\partial r}\right|_{r=0} = 0\)，速度波节），而在開口端 \(r=L\) 处由 \(\sin(kL)=0\) 给出半波长整数倍条件。
  - 难点2：在声电类比中，从牛顿第二定律 \(\Delta p \cdot A = (\rho A \ell)\frac{dv}{dt} = \rho\ell \frac{dI_V}{dt}\) 严格论证一段受限空气柱的惯性对应于**电感** \(L_{\text{ac}} = \frac{\rho\ell}{A}\)。
- **高频易错点**：
  - 易错点1：误以为所有一端闭合、一端开口的管乐器都满足 \(\lambda_n = \frac{4L}{2n-1}\)（这只对截面积恒定的圆柱管成立；圆锥管因球面波 \(1/r\) 因子，其谐频序列与开管相同！）。
  - 易错点2：在第 6 问中仅凭特征声阻抗 \(Z = \frac{\rho c}{A}\) 是实数就误判空气质量对应于电阻（行波特征阻抗为实数是因为无限长传输线的分布电感与分布电容之比 \(\sqrt{L/C}\) 为实数，而空气质量本身存储动能，对应电感！）。
- **教学核心结论**：声学传输线与电学传输线的类比（声压 \(\leftrightarrow\) 电压，体积流率 \(\leftrightarrow\) 电流，空气惯性质量 \(\leftrightarrow\) 电感，空气绝热可压缩性 \(\leftrightarrow\) 电容，喇叭口渐变扩口 \(\leftrightarrow\) 阶梯阻抗变换器）是统一理解声波反射、滤波与辐射匹配的绝佳物理框架。

---

### 13. 死亡赛车手 (`plancks-2026-final-problem-slice-q4`)

- **物理模型**：死亡赛车手避障问题：紧急直线刹车、纯转向圆周运动与后轮抱死转向复合机动的最短避障距离对比
- **难度评级**：D3
- **核心标签**：`摩擦圆与轮胎附着极限`、`自然坐标系运动方程`、`分离变量积分`、`最优避障策略`、`复合转向制动`

#### 题目拆解与求解脉络
1. **方式 1（直线急刹）**：最大制动力 \(\mu Mg\)，由动能定理 \(\frac{1}{2}Mv_0^2 = \mu Mg L_1\) 得：
   \[ L_1 = \frac{v_0^2}{2\mu g}. \]
2. **方式 2（不刹车纯圆周转向）**：摩擦力提供向心力 \(\frac{Mv_0^2}{R} = \mu Mg\)，擦墙转过 \(90^\circ\) 所需距离为：
   \[ L_2 = R = \frac{v_0^2}{\mu g} = 2L_1. \]
3. **方式 3（前轮转向 + 后轮定向制动）**：前后轮最大摩擦力各为 \(F = \frac{1}{2}\mu Mg\)。前轮不刹车，摩擦力垂直于瞬时速度 \(\mathbf{v}\)；后轮通过转向与制动配合，使摩擦力始终垂直于墙壁向外（背离墙壁，以最快减小朝向墙壁的速度分量）。设速度偏离初向的角度为 \(\alpha \in [0, \pi/2]\)，切向与法向运动方程为：
   \[ M\frac{dv}{dt} = -F\cos\alpha, \qquad Mv\frac{d\alpha}{dt} = F(1 + \sin\alpha). \]
   两式相除得 \(\frac{dv}{v} = -\frac{\cos\alpha\,d\alpha}{1+\sin\alpha}\)，积分得 \(v(\alpha) = \frac{v_0}{1+\sin\alpha}\)。当车平行于墙壁（\(\alpha = \pi/2\)）时，末速度为 \(v_f = \frac{v_0}{2}\)。利用 \(\cos\alpha\,dt = -\frac{M}{F}dv\) 积分垂直于墙方向的位移：
   \[ L_3 = \int_0^{t_f} v\cos\alpha\,dt = -\frac{M}{F}\int_{v_0}^{v_0/2} v\,dv = \frac{3M v_0^2}{8F} = \frac{3v_0^2}{4\mu g} = \frac{3}{2}L_1. \]
   综上，\(L_1 < L_3 < L_2\)，**方式 1（全力直线急刹）最为有效**（比方式 3 短 \(1/3\)，比方式 2 短 \(1/2\)）。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解第 3 问时，首先必须澄清题干中“using steering, the friction force which acts on the rear wheels, can change its direction”的物理含义：前轮不刹车（滚动导向），故前轮静摩擦力 \(\mathbf{F}_{\text{front}}\)（最大为 \(F = \frac{1}{2}\mu Mg\)）严格垂直于车轮朝向/速度方向 \(\mathbf{v}\)；而后轮既制动又配合转向，为了使车在垂直于墙方向（\(y\) 轴）获得尽可能大的反向减速度，最优控制是让后轮摩擦力 \(\mathbf{F}_{\text{rear}}\)（大小 \(F = \frac{1}{2}\mu Mg\)）始终指向**垂直于墙向外**（\(-y\) 方向）！将 \(\mathbf{F}_{\text{rear}}\) 分解到自然坐标系切向与法向，即得 \(M\dot{v} = -F\cos\alpha\) 和 \(Mv\dot{\alpha} = F(1+\sin\alpha)\)。两式直接相除得 \(\frac{dv}{v} = -\frac{d(\sin\alpha)}{1+\sin\alpha}\)，一行积分即得 \(v(\alpha) = \frac{v_0}{1+\sin\alpha}\)，再把 \(\cos\alpha\,dt = -\frac{M}{F}dv\) 代入 \(\int v\cos\alpha\,dt\) 瞬间算出 \(L_3 = \frac{3v_0^2}{4\mu g}\)。
- **Phase 2 对照参考解答**：对照官方手写解答（`page-19.jpg` 至 `page-21.jpg`），官方解答将 \(v = \dot{\alpha}R\) 代入法向方程消去 \(v\)，然后对 \(\frac{1+\sin\alpha}{\dot{\alpha}}\) 关于时间 \(t\) 和角度 \(\alpha\) 进行了整整两页繁琐的二阶导数变换才解出 \(\dot{\alpha}(\alpha)\) 和 \(v(\alpha) = \frac{v_0}{1+\sin\alpha}\)；而我们在盲解中利用 \(a_n = \frac{v^2}{R} = v\dot{\alpha}\)，直接将切向方程 \(M\frac{dv}{dt} = -F\cos\alpha\) 与法向方程 \(Mv\frac{d\alpha}{dt} = F(1+\sin\alpha)\) 相除，**仅用一行分离变量**就得到了 \(v(\alpha) = \frac{v_0}{1+\sin\alpha}\)！这一技巧在竞赛教学中极具示范价值。
- **核心难点**：
  - 难点1：正确建立第 3 问前、后轮的受力模型：前轮提供纯法向力 \(F\)，后轮提供恒定背离墙壁的力 \(F\)（其在切向投影为 \(-F\cos\alpha\)，在法向投影为 \(+F\sin\alpha\)）。
  - 难点2：在求出 \(v(\pi/2) = v_0/2\) 后，巧妙利用 \(\cos\alpha\,dt = -\frac{M}{F}dv\) 将空间积分 \(L_3 = \int v\cos\alpha\,dt\) 转化为对速度 \(v\) 的定积分 \(-\frac{M}{F}\int_{v_0}^{v_0/2} v\,dv\)，避免求解复杂的 \(x(t), y(t)\) 参数方程。
- **高频易错点**：
  - 易错点1：直觉上误以为“打方向盘绕开障碍物”比直线刹车更有效（实际上任何转向都会把一部分摩擦力或速度分量浪费在平行于墙的方向上，导致车在完全停下或转过 \(90^\circ\) 时平行于墙仍有残余动能，从而需要更大的避障距离！）。
  - 易错点2：在第 3 问误以为轨迹曲率半径 \(R\) 是常数（题干中“trajectory is still assumed to be circular”只是粗略描述转弯，实际上由 \(R(\alpha) = \frac{Mv^2(\alpha)}{F(1+\sin\alpha)} = \frac{R_0}{(1+\sin\alpha)^3}\) 可知曲率半径随 \(\alpha\) 增大而迅速减小，必须用 \(a_n = v\dot{\alpha}\) 求解！）。
- **教学核心结论**：在平面曲线运动（如导弹追踪、带阻尼抛体、赛车转向制动）中，用自然坐标系的法向加速度公式 \(a_n = v\frac{d\alpha}{dt}\) 替代 \(\frac{v^2}{R}\)，并与切向方程 \(a_t = \frac{dv}{dt}\) 相除消去 \(dt\)，是秒杀速度-偏角关系 \(v(\alpha)\) 的黄金法则！

---

### 14. 双星系统的引力波 (`plancks-2026-final-problem-slice-q5`)

- **物理模型**：双星系统引力波辐射：啁啾质量（Chirp Mass）、量纲分析法推导引力波能流与 LIGO 应变探测极限
- **难度评级**：D2
- **核心标签**：`引力波辐射功率`、`啁啾质量`、`量纲分析法`、`时空应变振幅`、`LIGO激光干涉仪`

#### 题目拆解与求解脉络
1. **开普勒定律化简与啁啾质量**：由 \(a^3\omega^2 = G(m_1+m_2)\) 及 \(\omega = \pi f_{\text{GW}}\) 消去 \(a\)，并引入啁啾质量 \(\mathcal{M} = \frac{(m_1 m_2)^{3/5}}{(m_1+m_2)^{1/5}}\)，得引力波辐射功率与距离 \(d\) 处的能流：
   \[ \dot{E}_{\text{GW}} = \frac{32}{5}\frac{G^{7/3}}{c^5}\left(\pi\mathcal{M}f_{\text{GW}}\right)^{10/3}, \qquad F_{\text{GW}} = \frac{\dot{E}_{\text{GW}}}{4\pi d^2} = \frac{8\pi^{7/3}}{5}\frac{G^{7/3}}{c^5 d^2}\left(\mathcal{M}f_{\text{GW}}\right)^{10/3}. \]
2. **弦波与引力波能流的量纲分析**：弦上机械波能量满足 \(E \propto m A^2 f^2\)。引力波在真空中传播且应变振幅 \(h = \Delta L/L\) 无量纲，设 \(F_{\text{GW}} \sim G^a c^b \langle\dot{h}^2\rangle\)，由量纲匹配 \([G^a c^b] = \text{M}\cdot\text{T}^{-1}\) 解得 \(a = -1, b = 3\)，即 \(F_{\text{GW}} \propto \frac{c^3}{G}h_0^2 f_{\text{GW}}^2\)（精确广义相对论公式为 \(F_{\text{GW}} = \frac{c^3 \omega_{\text{GW}}^2}{32\pi G}h_0^2\)）。
3. **应变振幅公式与典型天体源估算**：联立两端能流得：
   \[ h_0 = \frac{8}{\sqrt{5}}\frac{\pi^{2/3}(G\mathcal{M})^{5/3}}{c^4 d}f_{\text{GW}}^{2/3}. \]
   - **GW150914（双黑洞 \(36, 29 M_\odot\)，\(100\text{ Hz}\)，\(440\text{ Mpc}\)）**：\(\mathcal{M} \approx 28.1 M_\odot\)，\(h_0 \approx 1.5\times 10^{-21}\)；
   - **GW170817（双中子星 \(1.4, 1.3 M_\odot\)，\(100\text{ Hz}\)，\(40\text{ Mpc}\)）**：\(\mathcal{M} \approx 1.17 M_\odot\)，\(h_0 \approx 8.4\times 10^{-23}\)；
   - **双白矮星（\(0.6, 0.6 M_\odot\)，\(2\text{ mHz}\)，\(10\text{ kpc}\)）**：\(\mathcal{M} \approx 0.52 M_\odot\)，\(h_0 \approx 6.4\times 10^{-23}\)；
   - **超大质量双黑洞（\(10^6, 10^6 M_\odot\)，\(2\text{ mHz}\)，\(10\text{ Gpc}\)）**：\(\mathcal{M} = 2^{-1/5}\times 10^6 M_\odot \approx 8.71\times 10^5 M_\odot\)，\(h_0 \approx 1.6\times 10^{-17}\)（注：官方解答表格此处误将 \(\mathcal{M}\) 代作 \(92.3 M_\odot\)）。
4. **LIGO 臂长变化与探测挑战**：对 \(L_{\text{eff}} = 500\text{ km}\) 和 \(h_0 = 1.5\times 10^{-21}\)，\(\Delta L = h_0 L_{\text{eff}} \approx 7.5\times 10^{-16}\text{ m} = 0.75\text{ fm}\)（小于质子半径，约为激光波长 \(\lambda \approx 1\ \mu\text{m}\) 的 \(7\times 10^{-10}\) 倍），需综合法布里-珀罗谐振腔、百千瓦级功率循环、压缩真空态量子降噪、多级摆地震隔振及匹配滤波技术方可实现探测。

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，第 1–4 问的幂次化简和量纲分析非常顺畅：\(\mu^2 M^{4/3} = \left(\frac{m_1 m_2}{m_1+m_2}\right)^2 (m_1+m_2)^{4/3} = \frac{(m_1 m_2)^2}{(m_1+m_2)^{2/3}} = \left[\frac{(m_1 m_2)^{3/5}}{(m_1+m_2)^{1/5}}\right]^{10/3} = \mathcal{M}^{10/3}\)。需要注意在第 4、5 问中，如果仅凭量纲分析而不知道广义相对论能动张量（Isaacson 有效能动张量）中的无量纲系数 \(\frac{1}{32\pi}\)，求出的 \(h_0\) 会相差一个 \(\mathcal{O}(1)\) 的纯数字常数（如 \(4\pi^{2/3}\) 与 \(\frac{8}{\sqrt{5}}\pi^{2/3}\)）；这在竞赛中完全正常，只要指数关系 \(\frac{(G\mathcal{M})^{5/3} f_{\text{GW}}^{2/3}}{c^4 d}\) 正确即可拿满分。
- **Phase 2 对照参考解答**：对照官方解答，第 1–5 问的公式完全一致。不过我们在核对第 6 问表格数值时发现官方解答表格的第 4 行（超大质量双黑洞 \(m_1 = m_2 = 10^6 M_\odot\)）有一处明显的计算器输入笔误：等质量双星的啁啾质量为 \(\mathcal{M} = 2^{-1/5} m = 0.8706 \times 10^6 M_\odot \approx 8.71\times 10^5 M_\odot\)，代入公式可得其应变高达 \(h_0 \approx 1.6\times 10^{-17}\)（正因信号极强，它是空间引力波探测器 LISA 的黄金目标源！），而官方解答误把 \(\mathcal{M}\) 算成了 \(92.3 M_\odot\) 从而得出了 \(3.6\times 10^{-25}\)。我们在笔记中应当把正确的 \(\mathcal{M} = 8.71\times 10^5 M_\odot\) 和 \(h_0 \sim 10^{-17}\) 写清楚，同时提醒学生等质量双星啁啾质量速算公式 \(\mathcal{M} = 2^{-1/5} m \approx 0.871 m\)。
- **核心难点**：
  - 难点1：准确完成双星约化质量 \(\mu\)、总质量 \(M\) 向啁啾质量 \(\mathcal{M} = \mu^{3/5} M^{2/5}\) 的幂次合并。
  - 难点2：理解为什么引力波探测器的灵敏度随距离按 \(1/d\) 衰减而非像电磁波光度那样按 \(1/d^2\) 衰减——因为激光干涉仪直接测量的是引力波的**振幅（应变 \(h \propto F_{\text{GW}}^{1/2} \propto 1/d\)）**而非能量通量！
- **高频易错点**：
  - 易错点1：混淆轨道角频率 \(\omega_{\text{orb}}\) 与引力波频率 \(f_{\text{GW}}\) 的两倍关系：由于质量四极矩在一个轨道周期内重复两次，\(f_{\text{GW}} = 2 f_{\text{orb}} = \frac{\omega_{\text{orb}}}{\pi}\)（故 \(\omega_{\text{orb}} = \pi f_{\text{GW}}\)，而 \(\omega_{\text{GW}} = 2\pi f_{\text{GW}}\)）。
  - 易错点2：在第 6 问代入不同距离单位（\(\text{kpc}, \text{Mpc}, \text{Gpc}\)）时漏掉 \(10^3, 10^6, 10^9\) 的数量级换算。
- **教学核心结论**：记住真空引力波能流密度公式 \(F_{\text{GW}} \sim \frac{c^3}{G}\dot{h}^2\)：其中的比例系数 \(\frac{c^3}{G} \approx 4\times 10^{35}\text{ kg/s}\) 极其巨大，这意味着时空本身是“极度刚性（stiff）”的介质——即便双黑洞合并释放出数倍太阳质量的巨大能量功率，在时空结构上激起的应变涟漪 \(h\) 也只有 \(10^{-21}\) 量级！

---

### 15. 彭罗斯过程 (`plancks-2026-final-problem-slice-q6`)

- **物理模型**：旋转黑洞（Kerr 黑洞）的能层参考系拖拽与彭罗斯过程（Penrose Process）能量提取极限
- **难度评级**：D3
- **核心标签**：`克尔黑洞能层`、`参考系拖拽效应`、`彭罗斯过程`、`负能轨道`、`极端黑洞最大效率`

#### 题目拆解与求解脉络
1. **能层参考系拖拽发电（热身）**：置于能层（Ergoregion）内的圆环受时空拖拽被迫随黑洞同向旋转，通过刚性轴带动远方磁铁在线圈内旋转，产生交变磁通量并由法拉第电磁感应定律点亮灯泡；所提取的能量来自黑洞的**转动动能（角动量 \(J\)）**。
2. **转折点分裂的能量与角动量守恒**：赤道面测地线径向方程在转折点 \(r = r_0\)（\(\dot{r}=0\)）处化为关于角动量 \(L\) 的二次方程，解得：
   \[ L^{(0)} = \frac{-2aM\mu_0 + \mu_0\sqrt{2Mr_0(r_0^2+a^2-2Mr_0)}}{r_0 - 2M}, \quad L^{(1,2)} = \frac{-2aME^{(1,2)} + \sqrt{\left[{E^{(1,2)}}^2 r_0^2 + \mu_{\text{fin}}^2(2Mr_0-r_0^2)\right](r_0^2+a^2-2Mr_0)}}{r_0 - 2M}. \]
   联立 \(E^{(1)} + E^{(2)} = E^{(0)} = \mu_0\) 与 \(L^{(1)} + L^{(2)} = L^{(0)}\)，首项 \(-2aM(E^{(1)}+E^{(2)})\) 与 \(-2aM\mu_0\) 恰好抵消，约去公因子后解得：
   \[ E^{(1,2)} = \frac{\mu_0}{2}\left[1 \pm \sqrt{\frac{2M}{r_0}\left(1 - \frac{4\mu_{\text{fin}}^2}{\mu_0^2}\right)}\right]. \]
3. **负能轨道条件与极端黑洞最大效率**：要实现能量提取 \(E^{(1)} > \mu_0\)，根号项须大于 1，即分裂点必须深入能层内部：
   \[ r_0 < 2M\left(1 - \frac{4\mu_{\text{fin}}^2}{\mu_0^2}\right) < 2M, \]
   此时坠入黑洞的第 2 个粒子处于**负能态**（\(E^{(2)} = \mu_0 - E^{(1)} < 0\)）。对极端克尔黑洞（\(a = M \implies r_+ = M\)）取 \(r_0 = r_+ = M\) 及双光子衰变（\(\mu_{\text{fin}} = 0\)），得 \(E^{(1)} = \frac{1+\sqrt{2}}{2}\mu_0\)，最大能量提取效率为：
   \[ \eta_{\max} = \frac{E^{(1)} - E^{(0)}}{E^{(0)}} = \frac{\sqrt{2} - 1}{2} \approx 20.7\%. \]

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解第 3 问时，面对复杂的克尔测地线径向方程 \(\dot{r}^2 = \frac{E^2}{\mu^2} + \frac{2M}{r^3}\left(\frac{aE-L}{\mu}\right)^2 + \frac{a^2 E^2 - L^2}{\mu^2 r^2} - \frac{r^2+a^2-2Mr}{r^2} = 0\)，我注意到乘以 \(\mu^2 r^3\) 后它是关于 \((E, L, \mu)\) 的齐次二次型：\(E^2(r^3 + a^2 r + 2Ma^2) - 4MaEL - L^2(r - 2M) - \mu^2 r(r^2 + a^2 - 2Mr) = 0\)！从中解出 \(L(E, \mu) = \frac{-2MaE \pm \sqrt{\Delta(r_0)\, r_0 [E^2 r_0 + \mu^2(2M - r_0)]}}{r_0 - 2M}\)，其中 \(\Delta(r_0) = r_0^2 + a^2 - 2Mr_0\)。在 \(L^{(1)} + L^{(2)} = L^{(0)}\) 中利用 \(E^{(1)} + E^{(2)} = E^{(0)} = \mu_0\)，首项 \(-2Ma(E^{(1)}+E^{(2)})\) 与 \(-2MaE^{(0)}\) **直接完全相消**，公因子 \(\sqrt{\Delta(r_0)r_0}/(r_0-2M)\) 也直接约去！方程瞬间简化为 \(\sqrt{{E^{(1)}}^2 r_0 + \mu_{\text{fin}}^2(2M-r_0)} \pm \sqrt{{E^{(2)}}^2 r_0 + \mu_{\text{fin}}^2(2M-r_0)} = \mu_0\sqrt{2M}\)，两边平方即得所证公式！
- **Phase 2 对照参考解答**：对照官方解答，我们发现的这一“首项 \(-2MaE\) 利用能量守恒自动相消、且因子 \(\sqrt{r_0^2+a^2-2Mr_0}\) 整体约去（因此最终能量 \(E^{(1,2)}\) 竟然不显含自旋参数 \(a\)，\(a\) 仅通过视界半径 \(r_+ = M+\sqrt{M^2-a^2}\) 限制 \(r_0\) 的最小值！）”正是解开第 3 问全部代数繁难的钥匙！官方解答还提示了另一条应试捷径：由于题目已经给出了 \(E^{(1)}, E^{(2)}\) 的目标表达式，考生也可以直接将题给 \(E^{(1)}, E^{(2)}\) 代回 \(L^{(1)} + L^{(2)} = L^{(0)}\) 验证恒等式成立。
- **核心难点**：
  - 难点1：从 \(\dot{r}=0\) 的二次方程中准确解出 \(L(E, \mu)\)，并发现代入 \(E^{(1)} + E^{(2)} = E^{(0)}\) 后含黑洞自旋 \(a\) 的交叉项 \(-2MaE\) 自动抵消。
  - 难点2：深刻理解为什么只有在能层内部（赤道面 \(r_0 < 2M\)）才允许存在相对于无穷远观测者能量为负（\(E^{(2)} < 0\)）的物理粒子轨道（因为在 \(r < 2M\) 内类时杀伤矢量的模方 \(g_{tt} > 0\) 变为类空，能量 \(E = -p_t\) 可以取负值）。
- **高频易错点**：
  - 易错点1：在求解关于 \(L\) 的二次方程时未将各项通分到 \(r^3\)，或把根号内的因式分解 \((r_0^2 + a^2 - 2Mr_0)\left[E^2 r_0 + \mu^2(2M-r_0)\right]\) 算错。
  - 易错点2：误以为极端黑洞的能层外边界 \(r_{\text{erg}}\) 等于 \(M\)（赤道面上能层外边界始终是 \(r_{\text{erg}}(\pi/2) = 2M\)，而事件视界在极端自旋 \(a=M\) 时收缩至 \(r_+ = M\)，正因 \(r_+ = M < 2M\) 才使得 \(r_0 \to M\) 时比值 \(2M/r_0\) 达到最大值 2！）。
- **教学核心结论**：彭罗斯过程是广义相对论中黑洞热力学第二定律（霍金面积定理）的先声：落入视界的负能粒子（\(E^{(2)} < 0, L^{(2)} < 0\)）虽然减小了黑洞的总质量 \(M\) 和角动量 \(J\)，但黑洞的不可约质量 \(M_{\text{irr}}\)（及视界面积）反而增加；当黑洞自旋被提取殆尽（\(a \to 0, r_+ \to 2M\)）退化为史瓦西黑洞时，能层消失，能量提取即告终止。

---

### 16. 旋转的弹性绳 (`plancks-2026-final-problem-slice-q7`)

- **物理模型**：旋转弹性绳与末端质点的非均匀拉伸：拉格朗日物质坐标简谐方程 vs 欧拉空间坐标密度积分与临界角速度发散
- **难度评级**：D3
- **核心标签**：`旋转弹性绳`、`拉格朗日与欧拉坐标`、`非均匀胡克定律`、`特征值与共振发散`、`超越方程求解`

#### 题目拆解与求解脉络
1. **拉格朗日物质坐标下的微分方程（显式解法）**：选未变形时的原长坐标 \(x_0 \in [0, L_0]\) 为自变量，设旋转后径向位置为 \(r(x_0)\)。微元质量 \(dm = \frac{m}{L_0}dx_0 = \rho_0 S dx_0\)，胡克定律为 \(T(x_0) = ES\left(\frac{dr}{dx_0} - 1\right)\)。由径向力平衡 \(-dT = dm\,\omega^2 r(x_0)\) 得：
   \[ \frac{d^2 r}{dx_0^2} + k^2 r(x_0) = 0, \qquad k \equiv \omega\sqrt{\frac{\rho_0}{E}} = \omega\sqrt{\frac{m}{ESL_0}}. \]
   结合边界条件 \(r(0) = 0\) 与末端滑块平衡 \(T(L_0) = ES(r'(L_0) - 1) = M\omega^2 r(L_0)\)，解得 \(r(x_0) = C\sin(kx_0)\)，从而末端距离 \(L = r(L_0)\) 的显式表达式为：
   \[ L(\omega) = \frac{L_0\sin(kL_0)}{kL_0\cos(kL_0) - \frac{M}{m}(kL_0)^2\sin(kL_0)}. \]
   （若如官方解答采用欧拉坐标 \(x \in [0, L]\) 积分可变密度 \(\rho(x)\)，则得到与之等价的隐式方程 \(\sin(kL_0) = \left[1 + k^2 L^2\left(\frac{1}{kL} + \frac{M}{m}kL_0\right)^2\right]^{-1/2}\)。）
2. **慢速旋转极限与临界发散角速度**：当 \(\omega \to 0\)（\(kL_0 \ll 1\)）时，\(L(\omega) \approx L_0\left[1 + \frac{(M + m/3)\omega^2 L_0}{ES}\right] \to L_0\)。当分母趋于零时 \(L \to \infty\)，故临界角速度 \(\omega_{\text{cr}}\) 由下列超越方程决定：
   \[ \cot\left(\omega_{\text{cr}}L_0\sqrt{\frac{\rho_0}{E}}\right) = \frac{M}{m}\omega_{\text{cr}}L_0\sqrt{\frac{\rho_0}{E}} \iff \tan\left(\omega_{\text{cr}}L_0\sqrt{\frac{\rho_0}{E}}\right) = \frac{S\sqrt{\rho_0 E}}{M\omega_{\text{cr}}}. \]

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解本题时，我立刻意识到：如果选用变形后的空间坐标 \(x \in [0, L]\)（欧拉坐标），线密度 \(\lambda(x)\) 是未知的待求函数，方程会变成非线性微分方程；反之，如果选用**未变形时的原长坐标 \(x_0 \in [0, L_0]\)（拉格朗日物质坐标）**，每个微元的质量 \(dm = \frac{m}{L_0}dx_0\) 是严格均匀的常数！只需求解变形后位置函数 \(r(x_0)\)：由 \(\frac{dr}{dx_0} = 1 + \frac{T}{ES}\) 和 \(\frac{dT}{dx_0} = -\frac{m\omega^2}{L_0}r\)，求导一步即化为二阶线性常系数方程 \(r''(x_0) + k^2 r(x_0) = 0\)（\(k = \sqrt{\frac{m\omega^2}{ESL_0}}\)），三行代数便直接解出了显式函数 \(L(\omega) = \frac{L_0\sin(kL_0)}{kL_0\cos(kL_0) - \frac{M}{m}(kL_0)^2\sin(kL_0)}\) 及发散判据 \(\cot(kL_0) = \frac{M}{m}kL_0\)！
- **Phase 2 对照参考解答**：对照官方手写解答（`page-22.jpg` 至 `page-25.jpg`），对比效果极其震撼：官方解答选用了欧拉空间坐标 \(x \in [0, L]\)，通过引入可变密度 \(\rho(x)\) 建立非线性微分方程 \(x\,dx = A\frac{d\rho}{\rho^3(x)}\)，积分后再利用总质量守恒 \(m = S\int_0^L \rho(x)dx\) 算出反正弦积分，最终只得到了一个关于 \(L\) 的复杂隐式方程 \(\sin\left(\frac{\rho_0 L_0}{\sqrt{A}}\right) = \left[1 + \frac{1}{AL^2}\left(\frac{A}{\rho_0} + \frac{ML}{S}\right)^2\right]^{-1/2}\)！而我们的拉格朗日物质坐标法直接将其化为简谐方程，不仅给出了 \(L(\omega)\) 的显式初等函数解，而且将该隐式方程两边取余切即可证明两者 100% 等价！
- **核心难点**：
  - 难点1：区分拉格朗日坐标 \(x_0 \in [0, L_0]\) 与欧拉坐标 \(r \in [0, L]\)：在拉格朗日坐标下局部伸长率定义为 \(\varepsilon(x_0) = \frac{dr}{dx_0} - 1\)，质量微元 \(dm = \rho_0 S dx_0\) 不随拉伸而改变。
  - 难点2：在末端 \(x_0 = L_0\) 处正确写出含未知总长 \(L = r(L_0)\) 的混合边界条件 \(T(L_0) = M\omega^2 r(L_0)\)（即第一类与第二类边界条件的线性组合——Robin 边界条件）。
- **高频易错点**：
  - 易错点1：误把整根绳子当作均匀拉伸的轻弹簧处理（那只会给出 \(M=0\) 时 \(\omega_{\text{cr}} = \sqrt{ES/(mL_0)}\)，而精确连续解在 \(M=0\) 时由 \(\cos(kL_0)=0\) 给出 \(\omega_{\text{cr}} = \frac{\pi}{2}\sqrt{\frac{ES}{mL_0}}\)）。
  - 易错点2：在欧拉坐标下误写 \(dm = \frac{m}{L}dx\)（旋转时靠近转轴处张力最大、拉伸最剧烈、线密度最小，而靠近末端处张力较小、线密度较大，故欧拉线密度绝非均匀常数！）。
- **教学核心结论**：凡是涉及弹性杆、弹性绳在重力场或旋转离心场中的大变形非均匀拉伸问题，**永远优先选择未变形的原长坐标 \(x_0\)（拉格朗日坐标）作为自变量**，求解位置映射函数 \(r(x_0)\)——这能将欧拉视角下的非线性变密度微分方程直接转化为二阶常系数线性简谐/双曲方程！

---

### 17. 波函数坍缩 (`plancks-2026-final-problem-slice-q8`)

- **物理模型**：宏观机械振子的量子基态冷却、零点涨落（ZPF）与波函数坍缩模型的位移噪声功率谱（维纳-辛钦/帕塞瓦尔定理）
- **难度评级**：D2
- **核心标签**：`波函数坍缩模型CSL/DP`、`量子谐振子基态`、`零点位置涨落ZPF`、`位移噪声功率谱密度`、`帕塞瓦尔定理`

#### 题目拆解与求解脉络
1. **波函数坍缩的概念与物理机制**：波函数坍缩是指处于量子叠加态的系统约化为单一本征态的过程。潜在机制包括：(i) 哥本哈根测量坍缩（导致量子力学非决定论且测量前物理量无客观实在性）；(ii) 环境退相干（系统与环境纠缠产生表观坍缩，全局演化仍保持幺正，对应多世界诠释）；(iii) Diósi-Penrose 引力诱导坍缩（质量空间叠加导致时空度规叠加不稳定，将波函数坍缩视为连接广义相对论与量子力学的真实物理过程）；(iv) GRW/CSL 客观随机坍缩模型（引入非线性随机噪声项修改薛定谔方程，会产生反常焦耳加热）。
2. **基态冷却有效温度与零点位置涨落**：基态 \(\langle\hat{b}^\dagger\hat{b}\rangle = 0\) 能量为 \(E_0 = \frac{1}{2}\hbar\Omega_m\)，由能量均分关系 \(\frac{1}{2}k_B T = \frac{1}{2}\hbar\Omega_m\) 得有效温度 \(T = \frac{\hbar\Omega_m}{k_B}\)（若按一维谐振子两个二次型自由度 \(k_B T = \frac{1}{2}\hbar\Omega_m\) 则为 \(\frac{\hbar\Omega_m}{2k_B}\)）。由 \(\hat{x} = \sqrt{\frac{\hbar}{2m\Omega_m}}(\hat{b} + \hat{b}^\dagger)\) 计算基态位置方差：
   \[ \langle 0|\hat{x}^2|0\rangle = \frac{\hbar}{2m\Omega_m}\langle 0|(\hat{b}+\hat{b}^\dagger)^2|0\rangle = \frac{\hbar}{2m\Omega_m} \implies x_{\text{zpf}} = \sqrt{\frac{\hbar}{2m\Omega_m}}. \]
   要在位置空间分辨宏观量子叠加态，两叠加分支的空间间距必须大于 \(x_{\text{zpf}}\)。
3. **由噪声功率谱导出位移方差**：对 \(S_{xx}(\omega) = \int_{-\infty}^{+\infty} \langle x(t)x(0)\rangle e^{i\omega t}dt\) 作逆傅里叶变换并取 \(t=0\)（帕塞瓦尔定理 / 维纳-辛钦定理）：
   \[ \langle x^2\rangle = \langle x(0)x(0)\rangle = \int_{-\infty}^{+\infty} \frac{S_{xx}(\omega)}{2\pi}d\omega. \]

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时，第 1、3、4 问非常标准明确：由 \(\hat{b} + \hat{b}^\dagger = \sqrt{\frac{2m\Omega_m}{\hbar}}\hat{x}\) 立得 \(x_{\text{zpf}} = \sqrt{\frac{\hbar}{2m\Omega_m}}\)；由逆傅里叶变换 \(\langle x(t)x(0)\rangle = \int_{-\infty}^\infty S_{xx}(\omega)e^{-i\omega t}\frac{d\omega}{2\pi}\) 在 \(t=0\) 处取值即得 \(\langle x^2\rangle = \int_{-\infty}^\infty S_{xx}(\omega)\frac{d\omega}{2\pi}\)（对应实验谱图峰值下面积）。唯一需要注意措辞的是第 2 问：一维谐振子包含动能与势能两个二次型自由度，经典能量均分定理给出 \(\langle E\rangle = 2\times \frac{1}{2}k_B T = k_B T\)；若令单个自由度 \(\frac{1}{2}k_B T = \frac{1}{2}\hbar\Omega_m\) 则得 \(T = \frac{\hbar\Omega_m}{k_B}\)，若令总能量 \(k_B T = \frac{1}{2}\hbar\Omega_m\) 则得 \(T = \frac{\hbar\Omega_m}{2k_B}\)，在作答时把两种对应方式都写明最为稳妥。
- **Phase 2 对照参考解答**：对照官方解答，第 2 问官方解答写的是 \(\frac{1}{2}k_B T = \frac{1}{2}\hbar\Omega_m \implies T = \frac{\hbar\Omega_m}{k_B}\)（即将谐振子零点能与单个 \(\frac{1}{2}k_B T\) 匹配），我们在教学拆解中同时给出 \(\frac{\hbar\Omega_m}{k_B}\) 与 \(\frac{\hbar\Omega_m}{2k_B}\) 的物理说明，帮助学生在考场上做到滴水不漏。此外注意到题目式 (4) 中积分上下限印成了 \(\int_{-\infty}^\infty \to \int_\infty^{-\infty}\)，官方解答卷已将其更正为标准的 \(\int_{-\infty}^{+\infty}\)。
- **核心难点**：
  - 难点1：熟练运用玻色算符代数 \(\langle 0|(\hat{b}+\hat{b}^\dagger)^2|0\rangle = \langle 0|\hat{b}\hat{b}^\dagger|0\rangle = 1\) 严格计算基态位置涨落。
  - 难点2：理解维纳-辛钦定理（Wiener-Khinchin Theorem）在实验物理中的应用：功率谱密度 \(S_{xx}(\omega)\) 在全频域上的积分（即共振峰下的面积）直接给出时域涨落的总方差 \(\langle x^2\rangle \propto T_{\text{eff}}\)。
- **高频易错点**：
  - 易错点1：在反解 \(\hat{x}\) 时漏掉因子 \(1/2\)（由 \(\hat{b} + \hat{b}^\dagger = 2\sqrt{\frac{m\Omega_m}{2\hbar}}\hat{x} = \sqrt{\frac{2m\Omega_m}{\hbar}}\hat{x}\)，容易把根号内外的 2 弄混）。
  - 易错点2：在做逆傅里叶变换求 \(\langle x^2\rangle = \langle x(0)^2\rangle\) 时漏掉角频率积分的归一化因子 \(\frac{1}{2\pi}\)（注意 \(\frac{d\omega}{2\pi} = df\)）。
- **教学核心结论**：在量子光力学（Quantum Optomechanics）与精密测量中，谐振子的两个核心量子标尺必须烂熟于心：一是基态冷却特征温度 \(T_0 = \frac{\hbar\Omega_m}{k_B}\)，二是零点位置涨落 \(x_{\text{zpf}} = \sqrt{\frac{\hbar}{2m\Omega_m}}\)；而通过积分位移噪声谱密度 \(S_{xx}(\omega)\) 测量有效温度，则是现代低温量子实验的标准测温手段（噪声温度计）。

---

### 18. 光波导原理 (`plancks-2026-final-problem-slice-q9`)

- **物理模型**：多层包层平板光波导的几何光学导模条件、全内反射临界角与数值孔径（Numerical Aperture）
- **难度评级**：D1
- **核心标签**：`平板光波导`、`斯涅尔定律`、`全内反射临界角`、`数值孔径NA`、`多层包层有效折射率`

#### 题目拆解与求解脉络
1. **单包层波导的接收角与数值孔径**：光线从折射率 \(n_0\) 的介质以角度 \(\theta_0\) 入射端面，折射入芯层（折射率 \(n_f\)）后与轴线夹角为 \(\theta_f\)，满足 \(n_0\sin\theta_0 = n_f\sin\theta_f\)。在芯层-包层界面上的入射角为 \(\phi_f = \frac{\pi}{2} - \theta_f\)，发生全内反射要求 \(\sin\phi_f = \cos\theta_f \ge \frac{n_1}{n_f}\)，故：
   \[ \sin\theta_f = \sqrt{1 - \cos^2\theta_f} \le \frac{\sqrt{n_f^2 - n_1^2}}{n_f} \implies \text{NA} \equiv n_0\sin\theta_{\max} = \sqrt{n_f^2 - n_1^2}, \quad \theta_{\max} = \sin^{-1}\left(\frac{\sqrt{n_f^2 - n_1^2}}{n_0}\right). \]
2. **\(N\) 层包层波导的广义数值孔径**：当芯层外包覆 \(N\) 层厚包层及半无限外包层（\(k = 1, 2, \dots, N+1\)）时，导模光线需对所有包层满足全内反射条件 \(\cos\theta_f \ge \frac{n_k}{n_f}\)。最强的约束来自折射率最大的包层 \(n_{\text{clad, max}} = \max\{n_1, n_2, \dots, n_{N+1}\}\)，从而：
   \[ \theta_{\max} \approx \sin^{-1}\left(\frac{\sqrt{n_f^2 - n_{\text{clad, max}}^2}}{n_0}\right), \qquad \text{NA} \approx \sqrt{n_f^2 - n_{\text{clad, max}}^2}. \]

#### 盲解体会与对照分析
- **Phase 1 独立盲解**：盲解时第 1 问只需一分钟即可完成：注意区分“端面入射折射角 \(\theta_f\)（相对于水平波导轴线）”与“侧壁全反射入射角 \(\frac{\pi}{2}-\theta_f\)（相对于竖直界面法线）”，利用 \(\sin^2\theta_f + \cos^2\theta_f = 1\) 即可化出 \(\sqrt{n_f^2 - n_1^2}\)。第 2 问由平行多层介质界面切向波矢守恒 \(k_z = k_0 n_f\cos\theta_f = k_0 n_k \sin\phi_k\)，若光线穿透或耦合至第 \(k\) 层，要求在所有包层中均满足倏逝波条件 \(n_f\cos\theta_f \ge n_k\)（对一切 \(k=1,\dots,N+1\)），故 \(\cos\theta_f \ge \frac{\max_k n_k}{n_f} = \frac{n_{\text{clad, max}}}{n_f}\)，立得所证结论。
- **Phase 2 对照参考解答**：对照官方解答，推导完全一致。从波动光学与导波光学角度补充一点深层理解：在严格射线光学中，若第一层包层 \(n_1 < n_2\) 且厚度 \(d_1 \gg \lambda\)，全反射其实发生在 \(n_f/n_1\) 界面；但在实际波导模式理论中，任何满足 \(\beta/k_0 = n_f\cos\theta_f < n_k\) 的模式都会在第 \(k\) 层变成振荡辐射模（Leaky mode），只有当有效折射率 \(n_{\text{eff}} = n_f\cos\theta_f > \max_k n_k = n_{\text{clad, max}}\) 时，场在所有包层中才均为指数衰减的倏逝波（或严格高于所有包层基底模），从而构成真正束缚在芯层的导模（Guided mode）！用“切向传播常数 \(n_{\text{eff}} = n_f\cos\theta_f > n_{\text{clad, max}}\)”来理解第 2 问，物理逻辑比单纯的几何光学更加严密。
- **核心难点**：
  - 难点1：准确处理波导端面（垂直于轴线）与波导侧壁（平行于轴线）两个正交界面上角度的互余关系 \(\phi_{\text{wall}} = 90^\circ - \theta_f\)。
  - 难点2：从平行界面斯涅尔不变量 \(n_{\text{eff}} = n_f\cos\theta_f\) 理解为什么多层包层的严格导模束缚条件由最大包层折射率 \(n_{\text{clad, max}}\) 决定。
- **高频易错点**：
  - 易错点1：把端面折射角 \(\theta_f\) 直接当作侧壁全反射的入射角代入 \(\sin\theta_f \ge n_1/n_f\)，忘记取余角 \(\cos\theta_f \ge n_1/n_f\)。
  - 易错点2：在定义数值孔径 \(\text{NA} = n_0\sin\theta_{\max}\) 时漏写外部入射介质折射率 \(n_0\)。
- **教学核心结论**：分析任何平面层状介质或光纤波导问题时，抓住轴向有效折射率（斯涅尔不变量）\(n_{\text{eff}} = n_f\cos\theta_f = n(x)\sin\phi(x)\) 是核心关键：真正的导模必须在所有包层区域满足 \(n_{\text{eff}} > n_{\text{clad}}(x)\)，由此立刻导出 \(\text{NA} = \sqrt{n_f^2 - n_{\text{clad, max}}^2}\)。
