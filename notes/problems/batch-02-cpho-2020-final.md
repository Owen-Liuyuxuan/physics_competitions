# CPhO 2020（第37届全国中学生物理竞赛决赛）理论试题：独立盲解、官方解答对照与深度教学拆解

本报告严格遵循两阶段协议（**Phase 1：只看原题独立盲解** $\rightarrow$ **Phase 2：对照官方参考解答与竞赛教学拆解**），涵盖第37届全国中学生物理竞赛决赛理论全部 7 道试题（`cpho-2020-final-theory-problem-slice-q1` 至 `q7`）。

---

## 第1题：`cpho-2020-final-theory-problem-slice-q1`
- **建议标题**：第37届决赛理论第1题 · 散裂中子源、查德威克中子发现与麦克斯韦动能分布
- **难度评级**：D2
- **核心物理模型**：非相对论两体弹性散射（动量矢量三角形）、序列正碰递推加速、麦克斯韦速率分布与动能分布的雅可比变换

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：两体弹性碰撞与查德威克测定中子质量**
   - 设入射中子质量为 \(m\)、初动量为 \(\vec{p}_0 = m\vec{v}_0\)，碰撞后动量为 \(\vec{p} = m\vec{v}\)；静止靶核质量为 \(m_1\)，碰撞后动量为 \(\vec{p}_1 = m_1\vec{v}_1\)，且 \(\vec{p}_1\) 与 \(\vec{p}_0\) 夹角为 \(\alpha\)。
   - 由动量守恒 \(\vec{p} = \vec{p}_0 - \vec{p}_1\) 及余弦定理消去中子末速度方向：
     \[
     m^2 v^2 = m^2 v_0^2 + m_1^2 v_1^2 - 2 m m_1 v_0 v_1 \cos\alpha
     \]
   - 由动能守恒 \(\frac{1}{2}m v_0^2 = \frac{1}{2}m v^2 + \frac{1}{2}m_1 v_1^2\) 得 \(m^2 v^2 = m^2 v_0^2 - m m_1 v_1^2\)。两式联立立即给出靶核出射速率：
     \[
     v_1 = \frac{2m}{m + m_1} v_0 \cos\alpha
     \]
   - 代回能量守恒式得中子末速率：
     \[
     v = v_0 \sqrt{1 - \frac{4 m m_1}{(m + m_1)^2} \cos^2\alpha} = \frac{\sqrt{m^2 + m_1^2 + 2 m m_1 \cos 2\alpha}}{m + m_1} v_0
     \]
   - 当 \(\alpha = 0\)（对心正碰）时，靶核速率最大：\(v_{1,\max} = \frac{2m}{m + m_1} v_0\)。
   - 代入氢核（\(m_1 = m_{\text{H}}\)，\(v_{\text{H},\max} = 3.30\times 10^7\text{ m/s}\)）与氮核（\(m_1 = 14 m_{\text{H}}\)，\(v_{\text{N},\max} = 4.70\times 10^6\text{ m/s}\)）：
     \[
     \frac{v_{\text{H},\max}}{v_{\text{N},\max}} = \frac{m + 14 m_{\text{H}}}{m + m_{\text{H}}} = \frac{33.0}{4.70} \implies m = \frac{14 v_{\text{N},\max} - v_{\text{H},\max}}{v_{\text{H},\max} - v_{\text{N},\max}} m_{\text{H}} \approx 1.16 m_{\text{H}}, \quad v_0 = \frac{m + m_{\text{H}}}{2m} v_{\text{H},\max} \approx 3.07\times 10^7\text{ m/s}
     \]

2. **第（2）问：中子束连续正碰加速氮核的递推过程**
   - 要使每次碰撞氮核速率增量最大，每次均为同向对心正碰。设第 \(i\) 次碰撞前氮核速率为 \(V_{i-1}\)，与速率为 \(v_0\) 的中子正碰后速率为 \(V_i\)。
   - 在质心系或直接由一维弹性正碰公式：
     \[
     V_i = \frac{2m v_0 + (m_{\text{N}} - m) V_{i-1}}{m_{\text{N}} + m} \implies v_0 - V_i = a (v_0 - V_{i-1}), \quad a \equiv \frac{m_{\text{N}} - m}{m_{\text{N}} + m} \approx 0.847
     \]
   - 因初态 \(V_0 = 0\)，迭代 \(n\) 次后：
     \[
     V_n = (1 - a^n) v_0
     \]
   - 令氮核动能与中子初动能近似相等：\(\frac{1}{2} m_{\text{N}} V_n^2 \approx \frac{1}{2} m v_0^2 \implies 1 - a^n \approx \sqrt{\frac{m}{m_{\text{N}}}} \approx \sqrt{\frac{1.16}{14}} \approx 0.288\)，解得 \(n = \frac{\ln(1 - 0.288)}{\ln 0.847} \approx 2.045\)，取整数 \(n = 2\)。

3. **第（3）问：最概然速率对应动能 vs 最概然动能**
   - 对麦克斯韦速率分布 \(f(v) \propto v^2 e^{-mv^2/(2k_{\text{B}}T)}\) 求极值 \(\frac{\text{d}f(v)}{\text{d}v} = 0\)，得最概然速率 \(v_p = \sqrt{\frac{2k_{\text{B}}T}{m}}\)，其对应的动能为：
     \[
     E_k(v_p) = \frac{1}{2} m v_p^2 = k_{\text{B}} T
     \]
   - 动能分布函数 \(g(E_k)\) 由概率元守恒 \(g(E_k)\text{d}E_k = f(v)\text{d}v\) 确定，利用 \(\text{d}E_k = m v \text{d}v = \sqrt{2m E_k}\text{d}v\)：
     \[
     g(E_k) = f(v) \frac{\text{d}v}{\text{d}E_k} = \frac{2}{\sqrt{\pi}} (k_{\text{B}}T)^{-3/2} E_k^{1/2} e^{-E_k/(k_{\text{B}}T)}
     \]
   - 对 \(g(E_k)\) 求极值 \(\frac{\text{d}g(E_k)}{\text{d}E_k} = 0 \implies \frac{1}{2E_k} - \frac{1}{k_{\text{B}}T} = 0\)，得最概然动能：
     \[
     E_{k,p} = \frac{1}{2} k_{\text{B}} T
     \]

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：盲解与官方参考解答完全一致。第（1）问中，官方解答给出了直角坐标分量消元（解法一）与动量矢量三角形余弦定理（解法二）两种写法，矢量三角形法显然更加紧凑；第（2）问中利用不动点变换 \(V_i - v_0 = a(V_{i-1} - v_0)\) 一步即可写出通项，比逐项展开几何级数更不易出错。
- **核心难点与易错点**：
  1. **递推方程的构建方向**：第（2）问中不是同一个中子与多个靶核碰撞（慢化），而是**同一个氮核被一束速度均为 \(v_0\) 的中子依次追尾撞击**；随着氮核速度升高，后续中子与氮核的相对速度 \(v_0 - V_{i-1}\) 递减，每次速率增量按公比 \(a = \frac{m_{\text{N}}-m}{m_{\text{N}}+m}\) 指数衰减。
  2. **概率密度函数的非线性变量代换陷阱**：第（3）问最常见的错误是认为“最概然动能就等于最概然速率对应的动能 \(k_{\text{B}}T\)”，忽略了概率密度变换时的雅可比行列式因子 \(\frac{\text{d}v}{\text{d}E_k} \propto E_k^{-1/2}\) 会把峰值位置从 \(k_{\text{B}}T\) 拉低到 \(\frac{1}{2}k_{\text{B}}T\)。

---

## 第2题：`cpho-2020-final-theory-problem-slice-q2`
- **建议标题**：第37届决赛理论第2题 · 匀强电场中双导体球靠近的无穷电像级数与场强发散
- **难度评级**：D5
- **核心物理模型**：孤立导体球电像法（镜像电荷与球心补偿电荷）、径向偶极子的电像分解、双球无穷迭代电像级数与渐近发散证明

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：孤立导体球外的点电荷电像**
   - 若导体球接地（\(\varphi = 0\)），距离球心 \(a\) 处的点电荷 \(Q\) 的镜像电荷为 \(Q'_1 = -\frac{R_0}{a}Q\)，位于球心与 \(Q\) 连线上距球心 \(x'_1 = \frac{R_0^2}{a}\) 处。
   - 若导体球为**孤立不带电导体球**，为保持总电荷为零且球面等势，球心处还需放置补偿镜像电荷 \(Q'_2 = -Q'_1 = +\frac{R_0}{a}Q\)，位置 \(x'_2 = 0\)。
2. **第（2）问：匀强外场中的感应偶极矩**
   - 匀强外场 \(\vec{E}_0\) 等效于位于 \(\mp a\)（\(a \to \infty\)）处的 \(\pm Q\)，满足 \(E_0 = 2\frac{Q}{4\pi\varepsilon_0 a^2}\)。
   - 两镜像电荷 \(Q'_\pm = \mp \frac{R_0}{a}Q\) 位于 \(\mp b = \mp \frac{R_0^2}{a}\)，球心补偿电荷恰好抵消。当 \(a \to \infty\) 时，\(b \to 0\)，两镜像电荷构成位于球心的点电偶极子：
     \[
     p' = |Q'_\pm| \cdot 2b = \frac{2 R_0^3}{a^2} Q = 4\pi\varepsilon_0 R_0^3 E_0
     \]
3. **第（3）问：径向偶极子在导体球中的镜像偶极矩**
   - 位于 \(r \mp \frac{\Delta l}{2}\) 的点电荷 \(\mp q\) 在球内产生位于 \(x'_{1,2} = \frac{R_0^2}{r \mp \Delta l / 2}\) 的镜像电荷 \(q'_{1,2} = \pm \frac{R_0}{r \mp \Delta l / 2} q\)。
   - **盲解时的关键分歧记录**：
     - 若只考虑 \(x' \approx \frac{R_0^2}{r}\) 处的局域点偶极子，其偶极矩为 \(p' = \frac{R_0^3}{r^3} q\Delta l\)；
     - 但注意 \(q'_1 + q'_2 = \frac{R_0}{r^2} q\Delta l \neq 0\)！在 \(x' = \frac{R_0^2}{r}\) 处还存在净镜像点电荷 \(q' = \frac{R_0}{r^2} q\Delta l\)，且孤立导体球球心 \(x'=0\) 处有补偿电荷 \(Q' = -q' = -\frac{R_0}{r^2} q\Delta l\)。若将球内全部四个像电荷视为一个整体求总电偶极矩，\((q', Q')\) 还会贡献 \(p'' = q' \cdot \frac{R_0^2}{r} = \frac{R_0^3}{r^3} q\Delta l\)，总偶极矩为 \(p'_{\text{总}} = \frac{2 R_0^3}{r^3} q\Delta l\)。
4. **第（4）、（5）问：双球无穷电像递推与连线中点场强发散**
   - 两球心位于 \(\pm \frac{r}{2}\)。外场 \(E_0\) 先在两球心诱导 \(p_1 = 4\pi\varepsilon_0 R_0^3 E_0\)（距各自球心 \(b_1 = 0\)，距对方球心 \(r_1 = r\)）。
   - 第 \(n\) 阶偶极子 \(p_n\)（距本球心 \(b_n\)，距对方球心 \(r_n = r - b_n\)）在对方球内 \(b_{n+1} = \frac{R_0^2}{r_n}\) 处诱导次级点偶极子 \(p_{n+1} = \left(\frac{R_0}{r_n}\right)^3 p_n\) 及次级点电荷。
   - 当 \(r \to 2R_0\) 时，由数学归纳法易得：
     \[
     b_n = \frac{n-1}{n} R_0, \quad r_n = \frac{n+1}{n} R_0, \quad p_n = \frac{1}{n^3} p_1
     \]
   - 在连线中点 \((0,0)\) 处，第 \(n\) 对偶极子到原点的距离为 \(\frac{r}{2} - b_n = R_0 - \frac{n-1}{n}R_0 = \frac{R_0}{n}\)（或对次级电荷距离 \(\frac{n+1}{2n}R_0\)），其产生的电场级数通项不趋于零（或像点偶极子贡献 \(\propto \sum \frac{p_n}{(R_0 - b_n)^3} = \sum 4E_0 \to \infty\)），故中点场强发散至无穷大。

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：
  1. **第（3）问的精确处理**：官方解答非常严谨地同时写出了两种视角：不仅求出了位于 \(b = \frac{R_0^2}{r}\) 处的局域像点偶极子 \(p' = \frac{R_0^3}{r^3} q\Delta l\)，还明确指出了净像点电荷 \(q' = \frac{R_0}{r^2} q\Delta l\) 与球心补偿电荷 \(Q' = -\frac{R_0}{r^2} q\Delta l\) 构成的附加偶极矩 \(p'' = \frac{R_0^3}{r^3} q\Delta l\)，从而给出球内像电荷系统的总偶极矩 \(p'_{\text{总}} = \frac{2 R_0^3}{r^3} q\Delta l\)。
  2. **第（4）、（5）问中的像点电荷序列**：在双球有限间距 \(r\) 下，不能把相距 \(b_n\) 的 \((q', Q')\) 合并进位于 \(b_n\) 的点偶极子，而必须将点偶极子序列 \(p_n = \left(\frac{R_0}{r_{n-1}}\right)^3 p_{n-1}\) 与点电荷序列 \(q_n^{(i)}, Q_n\) 分开递推！在第（5）问证明发散时，官方解答巧妙地证明了像点电荷在中点产生的合场强恒正，从而只需用偶极子项级数作下界放缩即可严格证出 \(E(0,0) \to \infty\)。

---

## 第3题：`cpho-2020-final-theory-problem-slice-q3`
- **建议标题**：第37届决赛理论第3题 · 二能级原子量子奥托热机与量子卡诺热机循环
- **难度评级**：D3
- **核心物理模型**：二能级统计热力学（玻尔兹曼分布）、广义功 \(\text{đ}W = p_1\text{d}E_1\) 与广义热 \(\text{đ}Q = E_1\text{d}p_1\)、量子奥托循环与量子卡诺循环

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：二能级热平衡分布**
   - 由 \(p_0 + p_1 = 1\) 及 \(p_1 / p_0 = e^{-E_1 / (k_{\text{B}}T)}\)，得：
     \[
     p_0 = \frac{1}{1 + e^{-E_1/(k_{\text{B}}T)}}, \qquad p_1 = \frac{e^{-E_1/(k_{\text{B}}T)}}{1 + e^{-E_1/(k_{\text{B}}T)}} = \frac{1}{1 + e^{E_1/(k_{\text{B}}T)}}
     \]
2. **第（2）问：量子奥托循环**
   - 题干给出 \(\text{d}\langle E\rangle = p_1 \text{d}E_1 + E_1 \text{d}p_1\)，其中 \(\text{đ}W = p_1 \text{d}E_1\)（能级间隔改变对应做功），\(\text{đ}Q = E_1 \text{d}p_1\)（占据数概率改变对应传热）。
   - 因此，量子奥托循环在 \(p_1 - E_1\) 图上是一个**矩形**：
     - **等容（不做功）过程 \(A \to B\) 和 \(C \to D\)**：能级差 \(E_1\) 保持不变（\(E_A = E_B\)，\(E_C = E_D\)），故对外做功 \(W_{AB} = W_{CD} = 0\)，传热等于内能变化：\(Q_{AB} = \Delta\langle E\rangle_{AB} = E_B(p_B - p_A) > 0\)，放热 \(|Q_{CD}| = -\Delta\langle E\rangle_{CD} = E_C(p_B - p_A)\)。
     - **绝热（无传热）过程 \(B \to C\) 和 \(D \to A\)**：激发态概率 \(p_1\) 保持不变（\(p_B = p_C\)，\(p_D = p_A\)），故 \(Q_{BC} = Q_{DA} = 0\)，内能变化 \(\Delta\langle E\rangle_{BC} = -p_B(E_B - E_C)\)，对外做功 \(W_{BC} = p_B(E_B - E_C)\)；\(\Delta\langle E\rangle_{DA} = p_A(E_B - E_C)\)，对外做功 \(W_{DA} = -p_A(E_B - E_C)\)。
   - 奥托效率为 \(\eta_{\text{Otto}} = \frac{W_{\text{net}}}{Q_{AB}} = 1 - \frac{E_C}{E_B}\)。
3. **第（3）问：量子卡诺循环与效率比较**
   - 卡诺循环由两个等温过程（\(A\to B\) 温度 \(T_h\)，\(C\to D\) 温度 \(T_l\)）和两个绝热过程（\(B\to C\) 有 \(p_B = p_C \implies \frac{E_B}{T_h} = \frac{E_C}{T_l}\)，\(D\to A\) 有 \(p_D = p_A \implies \frac{E_A}{T_h} = \frac{E_D}{T_l}\)）组成。
   - 在等温过程 \(A\to B\) 中，积分 \(Q_{AB} = \int_A^B E_1 \text{d}p_1 = E_1 p_1\big|_A^B - \int_{E_A}^{E_B} p_1 \text{d}E_1\)，得：
     \[
     Q_{AB} = \frac{E_B}{1 + e^{E_B/(k_{\text{B}}T_h)}} - \frac{E_A}{1 + e^{E_A/(k_{\text{B}}T_h)}} + k_{\text{B}} T_h \ln\frac{1 + e^{-E_B/(k_{\text{B}}T_h)}}{1 + e^{-E_A/(k_{\text{B}}T_h)}}
     \]
   - 同理 \(C\to D\) 放热 \(|Q_{CD}| = \frac{T_l}{T_h} Q_{AB}\)，故 \(\eta_{\text{Carnot}} = 1 - \frac{T_l}{T_h}\)。
   - 在奥托循环中，最高温度为 \(T_B = T_h\)，最低温度为 \(T_D = T_l\)，由绝热关系 \(\frac{E_C}{E_B} = \frac{T_C}{T_B} = \frac{T_C}{T_h}\) 及 \(T_C > T_D = T_l\)，必有 \(\eta_{\text{Otto}} = 1 - \frac{T_C}{T_h} < 1 - \frac{T_l}{T_h} = \eta_{\text{Carnot}}\)。

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：盲解与官方解答完全吻合。在计算等温过程传热 \(\int E_1 \text{d}p_1\) 时，若直接利用分部积分 \(\int E_1 \text{d}p_1 = \Delta(E_1 p_1) - \int p_1 \text{d}E_1\)（或自由能 \(F = -k_{\text{B}}T\ln Z\) 与熵 \(S = \frac{\langle E\rangle - F}{T}\)），一行即可得到结果，比官方解答先对 \(p_1(E_1)\) 求导再凑微分积分更加清爽。

---

## 第4题：`cpho-2020-final-theory-problem-slice-q4`
- **建议标题**：第37届决赛理论第4题 · 激光多普勒测速仪（LDV）：差频外差探测与干涉条纹模型
- **难度评级**：D3
- **核心物理模型**：介质中的双次多普勒效应、双光束差频外差（拍频）消去散射角依赖、干涉条纹空间调制等价模型

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：单光束散射的双次多普勒频移**
   - 流体中光速为 \(c/n\)。注意题图 4a 中 \(\theta_1\) 标在入射光逆向延长线与粒子速度 \(\vec{v}\) 之间（即粒子迎着光束运动的分量为 \(v\cos\theta_1\)），\(\theta_2\) 标在散射光传播方向与 \(\vec{v}\) 之间。
   - 粒子接收频率 \(f' = f\left(1 + \frac{nv}{c}\cos\theta_1\right)\)，再作为移动波源向 \(\theta_2\) 方向散射，观测频率：
     \[
     f'' = \frac{f'}{1 - \frac{nv}{c}\cos\theta_2} \approx f\left[1 + \frac{nv}{c}(\cos\theta_1 + \cos\theta_2)\right] \implies \Delta f = \frac{fnv}{c}(\cos\theta_1 + \cos\theta_2)
     \]
   - 代入 \(v = 1\text{ m/s}\)，\(f = 10^{14}\text{ Hz}\)，\(\Delta f \le \frac{2fnv}{c} \approx 0.7\text{ MHz} < 5\text{ MHz}\)，无法用分辨率 \(5\text{ MHz}\) 的光谱仪直接检测。
2. **第（2）问：双光束外差探测与光电流**
   - 两束相干光与水平面夹角均为 \(\alpha/2\)，散射至同一探测器（散射角 \(\theta_2\) 相同），故两束散射光的差频消去了 \(\theta_2\)：
     \[
     \Delta f_{\text{D}} = |\Delta f_1 - \Delta f_2| = \frac{fnv}{c}|\cos\theta_1 - \cos\theta'_1| = \frac{2fnv}{c}\sin\frac{\alpha}{2}\cos\beta
     \]
   - 探测器带宽 \(10^2 \sim 10^7\text{ Hz}\) 滤去了光频和频项（\(\sim 10^{14}\text{ Hz}\)）及直流常数项，输出交变光电流：
     \[
     i(t) = k E_0^2 \cos(2\pi \Delta f_{\text{D}} t + \phi_1 - \phi_2)
     \]
3. **第（3）问：相交区干涉条纹模型**
   - 介质中波长 \(\lambda = \frac{c}{nf}\)，两束夹角为 \(\alpha\) 的平行光干涉条纹平行于 \(X\) 轴，条纹间距：
     \[
     d = \frac{\lambda}{2\sin(\alpha/2)} = \frac{c}{2 n f \sin(\alpha/2)}
     \]
   - 粒子沿竖直方向（垂直条纹方向）的分速度为 \(v\cos\beta\)，穿过明暗条纹散射光脉冲的频率为：
     \[
     f_{\text{D}} = \frac{v\cos\beta}{d} = \frac{2 f n v}{c} \sin\frac{\alpha}{2} \cos\beta
     \]
     与第（2）问的多普勒拍频完全一致！

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：完全一致。本题最大的易错点在于：
  1. **图 4a 中 \(\theta_1\) 的几何定义**：图中 \(\theta_1\) 是入射光线的**来向（逆波矢方向 \(-\vec{k}_1\)）**与 \(\vec{v}\) 的夹角，因此第一级多普勒效应是 \(+\cos\theta_1\) 而非 \(-\cos\theta_1\)。
  2. **介质折射率 \(n\) 的遗漏**：在流体中条纹间距是 \(\frac{\lambda_{\text{介质}}}{2\sin(\alpha/2)} = \frac{c}{2nf\sin(\alpha/2)}\)，只有包含折射率 \(n\)，条纹模型给出的脉冲频率才与第（2）问介质中的多普勒拍频严格相等。

---

## 第5题：`cpho-2020-final-theory-problem-slice-q5`
- **建议标题**：第37届决赛理论第5题 · 磁化星际等离子体中的脉冲星信号色散、群延迟与法拉第相移
- **难度评级**：D4
- **核心物理模型**：磁化冷等离子体中圆偏振电磁波的电子回旋运动、色散关系 \(n_\pm(\omega)\)、截止频率、群速度色散延迟与双圆偏振相位差

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：圆偏振波与纵向静磁场下的电子回旋半径**
   - 电磁波电场 \(E_x = E_0\cos(kz - 2\pi ft)\)，\(E_y = E_0\cos(kz - 2\pi ft \pm \frac{\pi}{2})\) 为幅值 \(E_0\)、角频率 \(\omega = 2\pi f\) 的左/右旋圆偏振波。
   - 电子在 \(xy\) 平面内做半径 \(R_e\)、速率 \(v = 2\pi f R_e\) 的匀速圆周运动，径向洛伦兹力方程为：
     \[
     m_e (2\pi f)^2 R_e = e E_0 \pm e (2\pi f R_e) B \implies R_e = \frac{e E_0}{2\pi m_e f \left(2\pi f \mp \frac{eB}{m_e}\right)}
     \]
2. **第（2）问：色散关系与截止频率 \(f_c\)**
   - 极化强度 \(\vec{P} = -n_e e \vec{r}\) 与 \(\vec{E}\) 反向，故电位移矢量 \(\vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon_0 n^2 \vec{E}\)，给出折射率：
     \[
     n^2 = 1 - \frac{f_p^2}{f(f \mp f_B)}, \qquad f_p \equiv \frac{e}{2\pi}\sqrt{\frac{n_e}{\varepsilon_0 m_e}}, \quad f_B \equiv \frac{eB}{2\pi m_e}
     \]
   - 群速度 \(v_g = 2\pi \frac{\text{d}f}{\text{d}k} = \frac{n c}{1 + \frac{f_p^2 (f \mp f_B/2)}{f(f \mp f_B)^2}}\)。令 \(v_g = 0\)（即 \(n = 0\)），得 \(f(f \mp f_B) - f_p^2 = 0\)，取正根得截止频率：
     \[
     f_c = \sqrt{f_p^2 + \frac{f_B^2}{4}} \pm \frac{f_B}{2} = \frac{1}{2\pi}\left[\sqrt{\frac{n_e e^2}{\varepsilon_0 m_e} + \left(\frac{eB}{2m_e}\right)^2} \pm \frac{eB}{2m_e}\right]
     \]
3. **第（3）问：脉冲信号到达地球的色散延迟时间**
   - 在 \(f_p \ll f, f_B \ll f\) 下：
     \[
     \Delta t = \frac{d}{v_g} - \frac{d}{c} \approx \frac{d}{2c}\frac{f_p^2}{f^2}\left(1 \pm \frac{2f_B}{f}\right) = \frac{e^2 n_e d}{8\pi^2 \varepsilon_0 m_e c f^2}\left(1 \pm \frac{eB}{\pi m_e f}\right)
     \]
4. **第（4）问：左、右旋圆偏振波的相位差**
   - 波数 \(k_\pm = \frac{2\pi f}{c} n_\pm \approx \frac{2\pi f}{c}\left(1 - \frac{f_p^2}{2f(f \mp f_B)}\right)\)。
   - 若计入群延迟时间差与波数差（或按参考解答定义 \(\Delta\phi = (\omega t_+ - k_+ d) - (\omega t_- - k_- d)\)），得 \(\Delta\phi \approx \frac{3 e^3 n_e B d}{4\pi^2 \varepsilon_0 m_e^2 c f^2}\)（若仅算固定时刻同位置相位差 \((k_- - k_+)d\) 则为 \(\frac{e^3 n_e B d}{4\pi^2 \varepsilon_0 m_e^2 c f^2}\)）。
5. **第（5）问：电子数密度涨落引起的相位移动**
   - 由 \(n^2 = 1 - \frac{f_p^2}{f(f \mp f_B)}\) 微分得 \(\Delta n = -\frac{f_p^2}{2 n f (f \mp f_B)} \frac{\Delta n_e}{n_e}\)，故通过长度 \(a\) 区间的相移为：
     \[
     \Delta\phi = a \Delta k = \frac{2\pi f a}{c}\Delta n = -\frac{\pi f_p^2 a}{n c (f \mp f_B)} \frac{\Delta n_e}{n_e}
     \]

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：
  1. 官方解答在第（2）、（3）、（5）问中全程保留了静磁场修正项 \(f_B = \frac{eB}{2\pi m_e}\)，没有在中间步骤提前令 \(B \to 0\)。
  2. 在第（4）问中，官方解答定义两种偏振信号到达地球时的相位差为 \(\Delta\phi = (\omega t_+ - k_+ d) - (\omega t_- - k_- d)\)，把第（3）问的群延迟时间差 \(t_+ - t_-\) 也代入了相位 \(2\pi f t\)，从而得到系数为 \(3 = 2 + 1\) 的结果 \(\frac{3 e^3 n_e B d}{4\pi^2 \varepsilon_0 m_e^2 c f^2}\)。在教学中应当向学生同时讲清**同一时刻接收的单色连续波相位差 \(\Delta k \cdot d\)（法拉第旋转角对应的相位差）**与**波包中心到达时刻的载波相位差 \(\omega\Delta t - \Delta k \cdot d\)** 的物理区别。

---

## 第6题：`cpho-2020-final-theory-problem-slice-q6`
- **建议标题**：第37届决赛理论第6题 · 反质子探测、微分切伦科夫计数器与三体衰变Dalitz图
- **难度评级**：D4
- **核心物理模型**：相对论粒子反应运动学与飞行时间法（TOF）、切伦科夫辐射马赫锥与球面镜成像、三体衰变 Dalitz 图边界方程

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：反质子与 \(\pi^-\) 介子的飞行时间**
   - 入射质子总能量 \(E = 6.8\text{ GeV}\)，动量 \(P = \frac{1}{c}\sqrt{E^2 - M_p^2 c^4} = 6.735\text{ GeV}/c\)。
   - 末态 3 个质子与 1 个反质子速度近似相同，故每个粒子分得约 \(1/4\) 的总动量 \(P_{\bar{p}} = P/4 = 1.684\text{ GeV}/c\)（或分得 \(1/4\) 的实验室系总能量 \(E_{\bar{p}} = \frac{E + M_p c^2}{4} = 1.935\text{ GeV}\)）。
   - 反质子速率 \(v_{\bar{p}} = \frac{P_{\bar{p}} c^2}{\sqrt{P_{\bar{p}}^2 c^2 + M_p^2 c^4}} \approx 0.873 c\)（或 \(0.875 c\)），通过 \(l = 12\text{ m}\) 的飞行时间为：
     \[
     t_{\bar{p}} = \frac{l}{v_{\bar{p}}} \approx 45.8\text{ ns}
     \]
   - 若 \(\pi^-\) 介子与反质子动能相同（或总能量相同），\(E_\pi = E_{\bar{p}} - M_p c^2 + m_{\pi^-} c^2 \approx 1.126\text{ GeV}\)，速率 \(v_{\pi^-} = c\sqrt{1 - \frac{m_{\pi^-}^2 c^4}{E_\pi^2}} \approx 0.992 c\)，飞行时间为：
     \[
     t_{\pi^-} = \frac{l}{v_{\pi^-}} \approx 40.3\text{ ns} \quad (\text{约 } 40\text{ ns})
     \]
2. **第（2）问：切伦科夫辐射角**
   - 由惠更斯包络面几何关系：\(\cos\theta = \frac{(c/n)t}{vt} = \frac{c}{nv} \implies \theta = \arccos\frac{c}{nv}\)。
3. **第（3）问：微分切伦科夫计数器光环半径**
   - 半径为 \(R\) 的球面镜焦距为 \(f = R/2\)，焦平面上光环半径为：
     \[
     r = f\tan\theta = \frac{R}{2}\sqrt{\left(\frac{nv}{c}\right)^2 - 1}
     \]
4. **第（4）问：\(p + \bar{p} \to 3\pi^0\) 的 Dalitz 图边界**
   - 设 \(K \equiv \frac{m_{\pi^0} c^2}{Q}\)，第 \(i\) 个 \(\pi^0\) 的动能占比 \(d_i = \frac{E_{k,i}}{Q}\)，则 \(d_1 + d_2 + d_3 = 1\)，且相对论动量大小满足：
     \[
     \frac{c p_i}{Q} = \sqrt{d_i^2 + 2 K d_i}
     \]
   - 在高为 1 的等边三角形坐标系中：
     \[
     d_1 = y, \qquad d_2 = \frac{1 - y - \sqrt{3}x}{2}, \qquad d_3 = \frac{1 - y + \sqrt{3}x}{2}
     \]
   - 动量守恒 \(\vec{p}_1 + \vec{p}_2 + \vec{p}_3 = 0\) 要求 \(p_1, p_2, p_3\) 构成闭合三角形（边界对应三动量共线 \(p_i = p_j + p_k\)），即：
     \[
     \sqrt{d_i^2 + 2Kd_i} \le \sqrt{d_j^2 + 2Kd_j} + \sqrt{d_k^2 + 2Kd_k}
     \]
   - 两次平方消去根号并代入 \(d_1, d_2, d_3\) 的坐标表达式，化简得边界三次代数曲线：
     \[
     2(3K + 1)\left(y^3 - 3x^2 y\right) - (12K + 1)y^2 - 3(2K + 1)x^2 + 2(4K + 1)Ky \le 0
     \]
   - 当 \(m_{\pi^0} = 0\)（即 \(K = 0\)）时，退化为：
     \[
     \left(y - \frac{1}{2}\right)\left(y - \sqrt{3}x\right)\left(y + \sqrt{3}x\right) \le 0
     \]
     即连接外等边三角形三边中点的内接倒立等边三角形区域（\(d_1, d_2, d_3 \le \frac{1}{2}\)）。

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：
  1. 第（1）问中，官方解答同时给出了按动量均分 \(P_{\bar{p}} = P/4\)（解法一）与按总能量均分 \(E_{\bar{p}} = (E + M_p c^2)/4\)（解法二）两种处理，两者算出的 \(t_{\bar{p}}\) 均为 \(45.8\text{ ns}\)。
  2. 第（4）问 Dalitz 图消去根号化简为三次曲线的步骤是全卷代数技巧最高的一处：利用海伦公式因子 \((p_1 + p_2 + p_3)(p_1 + p_2 - p_3)(p_1 - p_2 + p_3)(-p_1 + p_2 + p_3) \ge 0\)，即 \(2(p_1^2 p_2^2 + p_2^2 p_3^2 + p_3^2 p_1^2) - (p_1^4 + p_2^4 + p_3^4) \ge 0\)，由于只含 \(p_i^2 \propto d_i^2 + 2Kd_i\)，无需开方即可一次性消去全部根号！

---

## 第7题：`cpho-2020-final-theory-problem-slice-q7`
- **建议标题**：第37届决赛理论第7题 · 悬挂式孔子欹器：偏心空腔刚体质心、“虚则欹、中则正、满则覆”与微振动
- **难度评级**：D4
- **核心物理模型**：割补法（负质量法）求偏心空腔组合体质心与转动惯量、悬挂刚体静平衡与稳定性判据、复摆微振动

### 1. Phase 1：独立盲解（只看原题）
1. **第（1）问：空欹器自由悬挂的平衡倾角**
   - 采用**割补法（实心外形减去填实的偏心镗腔）**：
     - 匀质半球体（半径 \(r\)）质心距球心距离为 \(\frac{3}{8}r\)。
     - 实心外轮廓（半径 \(R_2 = \sqrt{3}R\)，柱长 \(l = 2R\)，对称轴 \(x=0\)）：体积 \(V_{\text{实}} = \pi R_2^2 l + \frac{2}{3}\pi R_2^3 = (6 + 2\sqrt{3})\pi R^3\)，质心 \(x_{\text{C实}} = 0\)，\(z_{\text{C实}} = \frac{\pi R_2^2 l (l/2) - \frac{2}{3}\pi R_2^3 (3R_2/8)}{V_{\text{实}}} = \frac{5(3 - \sqrt{3})}{16}R\)。
     - 内部空腔（半径 \(R_1 = R\)，柱长 \(l = 2R\)，对称轴 \(x = t = \frac{3}{10}R\)）：体积 \(V_{\text{空}} = \pi R_1^2 l + \frac{2}{3}\pi R_1^3 = \frac{8}{3}\pi R^3\)，质心 \(x_{\text{C空}} = \frac{3}{10}R\)，\(z_{\text{C空}} = \frac{21}{32}R\)。
   - 空欹器总体积 \(V_{\text{欹}} = V_{\text{实}} - V_{\text{空}} = \frac{2(5 + 3\sqrt{3})}{3}\pi R^3\)，质心坐标为：
     \[
     x_{\text{C}} = -\frac{V_{\text{空}} t}{V_{\text{欹}}} = \frac{3(5 - 3\sqrt{3})}{5}R \approx -0.1177 R, \qquad z_{\text{C}} = \frac{3(3\sqrt{3} - 5)}{2}R \approx 0.2942 R
     \]
   - 悬挂点 \(Q\left(-\frac{1}{10}R, \frac{2\sqrt{3}}{11}R\right) \approx (-0.1000 R, 0.3149 R)\)。自由悬挂稳定平衡时，质心 \(C\) 位于悬挂点 \(Q\) 正下方，故 \(Z\) 轴与竖直方向夹角 \(\theta_0\) 满足：
     \[
     \tan\theta_0 = \frac{x_{\text{Q}} - x_{\text{C}}}{z_{\text{Q}} - z_{\text{C}}} = \frac{121}{25(5\sqrt{3} - 3)} \approx 0.8551 \implies \theta_0 \approx 0.7074\text{ rad} = 40.53^\circ
     \]
2. **第（2）问：绕悬挂轴的转动惯量与微振动角频率**
   - 半径 \(r\) 的匀质半球绕球心直径轴的转动惯量为 \(\frac{4}{15}\pi\rho r^5\)，由平行轴定理先移至半球质心 \(I_c = \left(\frac{4}{15} - \frac{2}{3}\cdot\frac{9}{64}\right)\pi\rho r^5 = \frac{83}{480}\pi\rho r^5\)，再移至悬挂轴 \(Q\)。
   - 将外圆柱、外半球相加并减去内圆柱、内半球绕 \(Q\) 轴的转动惯量：
     \[
     I = I_{\text{实}} - I_{\text{空}} = \frac{54635 + 11441\sqrt{3}}{6050} \pi \rho_1 R^5 \approx 12.306 \pi \rho_1 R^5
     \]
   - 质心 \(C\) 到 \(Q\) 轴的距离为 \(d = \sqrt{(x_{\text{C}} - x_{\text{Q}})^2 + (z_{\text{C}} - z_{\text{Q}})^2} = \frac{\sqrt{2(30848 - 17541\sqrt{3})}}{110} R \approx 0.02722 R\)，复摆微振动角频率为：
     \[
     \omega = \sqrt{\frac{m_{\text{欹}} g d}{I}} \approx 0.1226 \sqrt{\frac{g}{R}}
     \]
3. **第（3）问：注水至“中则正”的水深 \(h\)**
   - **关键物理洞察**：当器身正立（\(Z\) 轴竖直）时，无论水深 \(h\) 处于半球腔还是圆柱腔，水体都关于 \(Z'\) 轴对称，因此**水体的质心横坐标恒为 \(x_{\text{CS}} = t = \frac{3}{10}R\)**！
   - 要使系统总质心横坐标等于悬挂点横坐标 \(x_{\text{Ct}} = x_{\text{Q}} = -\frac{1}{10}R\)，对 \(x = x_{\text{Q}}\) 列力矩平衡：
     \[
     m_{\text{S}} (t - x_{\text{Q}}) = m_{\text{欹}} (x_{\text{Q}} - x_{\text{C}}) \implies m_{\text{S}} = \frac{7 - 3\sqrt{3}}{2}\pi \rho_2 R^3 \approx 0.9018 \pi \rho_2 R^3
     \]
   - 比较内半球腔容积对应的水质量 \(\frac{2}{3}\pi \rho_2 R^3 \approx 0.6667 \pi \rho_2 R^3 < m_{\text{S}}\)，立即断定水面已进入圆柱腔（\(h > R\)）！
   - 由 \(m_{\text{S}} = \frac{2}{3}\pi \rho_2 R^3 + \pi \rho_2 R^2 (h - R)\) 直接解得：
     \[
     h = \frac{23 - 9\sqrt{3}}{6} R \approx 1.235 R
     \]
   - 同时检验此时总质心纵坐标 \(z_{\text{Ct}} \approx 0.271 R < z_{\text{Q}} \approx 0.315 R\)，处于悬挂点下方，确为稳定正立平衡。
4. **第（4）问：“满则覆”的临界条件**
   - 当继续注水使系统总质心升高至高于悬挂点（在正立或倾斜姿态下总质心到达悬挂点之上，临界条件为系统总质心与悬挂点重合或高于悬挂点，或倾覆后质心横坐标越过 \(x_{\text{Q}}\)），稳定平衡丧失，发生倾覆（“满则覆”）。

### 2. Phase 2：对照官方参考解答与教学拆解
- **对照分析**：
  - 盲解第（3）问的思路与官方参考解答的“解法一”完全一致！
  - 官方参考解答还附上了“解法二”：如果不先利用“正立时水体质心横坐标恒为 \(x_{\text{CS}} = t\)”求出所需水体积 \(V_{\text{S}}\) 并与半球体积 \(\frac{2}{3}\pi R^3\) 比较，而是盲目先假设 \(h \le R_1\) 去对球缺做积分，就会陷入一个极其繁琐的三次方程 \(h^3 - 3Rh^2 + \dots = 0\)，费尽周折求出三个实根后才发现都不在 \((0, R)\) 内，最后还得推倒重算 \(h > R_1\)！这一对比堪称物理竞赛中**“先定性/守恒判别区间、再定量求解”**的教科书级范例。
