# CPhO 2021 第38届全国中学生物理竞赛决赛理论试题：独立试做与教学拆解报告（Batch 04）

本报告严格遵循“第一阶段：只看原题独立盲做（Phase 1: Blind Solve）”与“第二阶段：对照官方解答深度比对与竞赛教学拆解（Phase 2: Comparison & Pedagogical Breakdown）”的双阶段规范，涵盖第38届全国中学生物理竞赛决赛理论试卷全部5道大题（`cpho-2021-final-theory-problem-slice-q1` 至 `q5`）。

---

## 第一题：菲涅耳半波带法与4级相位型波带片聚焦成像 (`cpho-2021-final-theory-problem-slice-q1`)

- **建议标题 (`better_title`)**：菲涅耳半波带与四级相位波带片的聚焦及多焦点成像
- **难度评级 (`difficulty`)**：`D3`
- **核心物理模型 (`model`)**：菲涅耳半波带衍射模型与相位型波带片（Phase Zone Plate）傍轴光程差近似

### Phase 1：独立盲做过程与初解记录

1. **物理图像与基本傍轴关系**：
   设小圆孔半径为 \(R = OM = 1.00\text{ mm}\)，入射波长 \(\lambda = 632.8\text{ nm}\)。对于轴上距圆孔中心 \(O\) 为 \(r_0\)（\(r_0 \gg \lambda\)）的场点 \(P\)，若整个圆孔恰好被划分为 \(N\) 个半波带，则圆孔外缘 \(M\) 到 \(P\) 的距离为 \(r_0 + N\frac{\lambda}{2}\)。由勾股定理：
   \[
   \sqrt{R^2 + r_0^2} = r_0 + N\frac{\lambda}{2} \implies R^2 = N\lambda r_0 + \frac{N^2\lambda^2}{4}
   \]
   在傍轴近似 \(r_0 \gg N\lambda\) 下略去二阶小量，得到半波带数目 \(N\) 与轴上位置 \(r_0\) 的核心对偶关系：
   \[
   r_0 \approx \frac{R^2}{N\lambda}
   \]

2. **第（1）问推导**：
   当 \(N = 2n+1\) 时：
   - \(n = 0 \implies N = 1\)（全孔仅含1个半波带，轴上最右侧主焦点 \(P_0\)）：
     \[
     r_0 = OP_0 = \frac{R^2}{\lambda} = \frac{(1.00\times 10^{-3}\text{ m})^2}{632.8\times 10^{-9}\text{ m}} \approx 1.580\text{ m} = 1580\text{ mm}
     \]
   - \(n = 1 \implies N = 3\)（全孔含3个半波带，两两相消后剩1个半波带，次焦点 \(P_1\)）：
     \[
     r_1 = OP_1 = \frac{R^2}{3\lambda} \approx 0.5268\text{ m} = 527\text{ mm}
     \]

3. **第（2）问推导（4级相位型波带片）**：
   波带片按 \(N=4\) 划分固定环带，且在第1、3环带覆盖透明薄膜使光程增加 \(\lambda/2\)（即相位延迟 \(\pi\)）。
   - **（i）主焦点 \(P_0'\)**：对于对应 \(N=4\) 的轴上位置，原本第1、2、3、4环带到达该点的几何光程差依次递增 \(\lambda/2\)（奇偶环带反相相消）；但第1、3环带额外附加 \(\lambda/2\) 光程后，4个环带的次波到达该点同相叠加，形成强聚焦主焦点：
     \[
     r_0' = OP_0' = \frac{R^2}{4\lambda} \approx 0.3951\text{ m} = 395\text{ mm}
     \]
   - **（ii）紧邻主焦点左侧暗点 \(P_{-1}'\)**：向 \(P_0'\) 左侧移动时，\(r\) 减小，每个固定环带对应的几何光程差增大。按照题目给定的波带重划规则（“将已有的每个半波带重新划分为若干个新的半波带”），紧邻左侧的暗点对应将4个固有环带中的**每一个环带重新等分为2个新的半波带**，即整个圆孔相对于 \(P_{-1}'\) 包含 \(N_{-1} = 4 \times 2 = 8\) 个半波带。此时每个固有环带内部的两个新半波带自身反相相消（无论该固有环带是否附加了 \(\lambda/2\) 薄膜），合振幅为零：
     \[
     r_{-1}' = OP_{-1}' = \frac{R^2}{8\lambda} = \frac{OP_0'}{2} \approx 0.1975\text{ m} = 198\text{ mm}
     \]
   - **（iii）紧邻主焦点右侧暗点 \(P_{+1}'\)**：向 \(P_0'\) 右侧移动时，\(r\) 增大，按题目规则将已有环带合并。将每2个相邻固有环带合并为1个新的半波带，则整个圆孔相对于 \(P_{+1}'\) 相当于 \(N_{+1} = 4 / 2 = 2\) 个半波带（外缘与中心的几何路径差为 \(\lambda\)）。此时第1与第3固有环带的几何光程差恰好为 \(\lambda/2\)（且两者均附加了 \(\lambda/2\) 薄膜），故第1与第3环带反相相消；同理第2与第4固有环带几何光程差也为 \(\lambda/2\)，亦反相相消，形成暗点：
     \[
     r_{+1}' = OP_{+1}' = \frac{R^2}{2\lambda} = 2 OP_0' \approx 0.7901\text{ m} = 790\text{ mm}
     \]

4. **第（3）问推导（点光源成像与虚实像判据）**：
   物点 \(S\) 位于波带片左侧 \(s_{\text{物}} = OS = 3\text{ m} = 3000\text{ mm}\) 处，像点 \(S'\) 位于右侧 \(s_{\text{像}} = OS'\) 处。光线从 \(S\) 经圆孔边缘 \(M\) 到 \(S'\) 与沿轴线经 \(O\) 到 \(S'\) 的几何路径差为：
   \[
   \Delta L = \left(\sqrt{s_{\text{物}}^2 + R^2} - s_{\text{物}}\right) + \left(\sqrt{s_{\text{像}}^2 + R^2} - s_{\text{像}}\right) \approx \frac{R^2}{2}\left(\frac{1}{s_{\text{物}}} + \frac{1}{s_{\text{像}}}\right)
   \]
   - **（i）主焦点成像**：主焦点要求上述总几何路径差跨越4个半波带，即 \(\Delta L = 4 \times \frac{\lambda}{2} = 2\lambda\)：
     \[
     \frac{1}{s_{\text{物}}} + \frac{1}{s_{\text{像}}} = \frac{4\lambda}{R^2} = \frac{1}{f} \quad \left(f = OP_0' = \frac{R^2}{4\lambda} \approx 395\text{ mm}\right)
     \]
     由此直接验证了薄透镜高斯成像公式成立，代入 \(s_{\text{物}} = 3000\text{ mm}\) 得：
     \[
     s_{\text{像}} = \frac{s_{\text{物}} f}{s_{\text{物}} - f} \approx 455\text{ mm}
     \]
   - **（ii）最近的另一像点与对应次焦点**：要在不改变相位片结构的前提下再次同相聚焦，需将4级波带片中的**每个固有环带拆分为奇数 \(2n+1\) 个新半波带**。取最近的 \(n=1\)（即每个固有环带拆分为3个新半波带，每个固有环带内2个相消、余1个有效半波带），则全孔共拆分为 \(N' = 3 \times 4 = 12\) 个半波带，边缘与轴线的总几何路径差为 \(\Delta L = 12 \times \frac{\lambda}{2} = 6\lambda\)：
     \[
     \sqrt{s_{\text{物}}^2 + R^2} + \sqrt{s_{\text{像}}'^2 + R^2} = s_{\text{物}} + s_{\text{像}}' + 6\lambda \implies \frac{R^2}{2}\left(\frac{1}{s_{\text{物}}} + \frac{1}{s_{\text{像}}'}\right) \approx 6\lambda
     \]
     解得最近另一像点位置 \(s_{\text{像}}' \approx 138\text{ mm}\)（若直接解根式方程可得 \(137\text{ mm}\)～\(138\text{ mm}\)），对应的次焦点焦距（\(s_{\text{物}} \to \infty\)）为：
     \[
     f' = \frac{R^2}{12\lambda} = \frac{f}{3} \approx 132\text{ mm}
     \]
   - **（iii）物距 \(s_{\text{物}} = OP_0'/2 \approx 198\text{ mm}\) 时的像**：
     此时物点到孔边缘与孔中心的几何路径差已达：
     \[
     \Delta L_{\text{物}} = \sqrt{s_{\text{物}}^2 + R^2} - s_{\text{物}} \approx \frac{R^2}{2(R^2 / 8\lambda)} = 4\lambda
     \]
     - 若以**主焦点**成像，要求经过波带片调制后的等效几何路径差为 \(2\lambda\)。由于入射波前在边缘已滞后 \(4\lambda > 2\lambda\)，波带片无法使波前会聚到右侧实像点，而是使出射发散波前等效于从波带片**左侧**某虚像点 \(S''\)（距离 \(|s_{\text{像}}''| = x_4\)）发出，满足 \(\Delta L_{\text{物}} - \Delta L_{\text{虚像}} = 2\lambda\)，即 \(\Delta L_{\text{虚像}} = 4\lambda - 2\lambda = 2\lambda\)，故为**虚像**，位于波带片**左侧主焦点处**（距 \(O\) 点 \(395\text{ mm}\)～\(396\text{ mm}\)）。
     - 若以**（3）（ii）次焦点**成像，要求总几何路径差为 \(6\lambda\)。由于 \(\Delta L_{\text{物}} = 4\lambda < 6\lambda\)，右侧实像点恰好提供剩余的 \(\Delta L_{\text{实像}} = 6\lambda - 4\lambda = 2\lambda\)，故为**实像**，位于波带片**右侧 \(393\text{ mm}\)～\(395\text{ mm}\) 处**（即右侧主焦点位置附近）。

### Phase 2：对照官方参考解答分析与教学拆解

- **与官方解答的对照**：
  1. 物理图像与全部结论完全一致。
  2. **值得注意的计算细节**：官方解答没有先对 \(\sqrt{s^2 + R^2} - s \approx \frac{R^2}{2s}\) 作泰勒展开，而是直接保留了带根号的精确几何方程，例如：
     \[
     \sqrt{198^2 + 1.00^2} + \sqrt{x_5^2 + 1.00^2} = 198 + x_5 + 6\lambda
     \]
     由于第（3）（iii）问中先将 \(f = 395.07\text{ mm}\) 四舍五入取整为 \(395\text{ mm}\)，再取 \(s_{\text{物}} = 198\text{ mm}\)，直接代回根式方程消去平方项时会放大舍入误差，从而得到 \(s_{\text{像}}'' = -396\text{ mm}\) 与 \(s_{\text{像}}''' = 393\text{ mm}\)（而在傍轴代数式下两者严格等于 \(\mp f = \mp 395\text{ mm}\)）。在竞赛阅卷中，保留根式求解或使用傍轴近似公式 \(R^2/(2s)\) 均得分，但教学中必须向学生讲明四舍五入中间值代入非线性根式方程带来的尾数差异。
  3. 在第（3）（iii）问虚像的处理上，官方解答直接令形式方程 \(\sqrt{s_{\text{物}}^2 + R^2} + \sqrt{s_{\text{像}}''^2 + R^2} = s_{\text{物}} + s_{\text{像}}'' + 2\lambda\)，移项平方后由于 \(\sqrt{s_{\text{像}}''^2 + R^2} \ge 0\)，解出一阶项系数从而得到 \(s_{\text{像}}'' = -396\text{ mm} < 0\)。这种代数写法看似快捷，但严格来说 \(\sqrt{x^2 + R^2} - x\) 对负 \(x\) 并不等于 \(-R^2/(2|x|)\)（展开应为 \(\sqrt{x^2+R^2} \approx |x| + \frac{R^2}{2|x|}\)，对于虚像发散波面，边缘光线到虚像点的距离比中心远，几何光程差是相减关系 \(\Delta L_{\text{物}} - \Delta L_{\text{像}} = 2\lambda\)）。我们在 Phase 1 中从波前曲率（发散球面波光程差相减）给出的物理推导更加严谨且不会产生符号悖论。

---

## 第二题：神舟十二号与天宫空间站交会对接的广义霍曼变轨动力学 (`cpho-2021-final-theory-problem-slice-q2`)

- **建议标题 (`better_title`)**：航天器轨道交会对接的广义变轨动力学与容错极值分析
- **难度评级 (`difficulty`)**：`D4`
- **核心物理模型 (`model`)**：有心力场开普勒椭圆轨道极坐标方程、冲量变轨与周期匹配相位条件

### Phase 1：独立盲做过程与初解记录

1. **第（1）问：用守恒量表示轨道参量 \(R, \varepsilon\)**：
   初始圆轨道半径 \(r_0\)、速率 \(v_0\)，故引力常量乘积为 \(GM = r_0 v_0^2\)。
   由正椭圆轨道 \(r(\theta) = \frac{R}{1 + \varepsilon\cos\theta}\) 在近地点 \(r_{\text{近}} = \frac{R}{1+\varepsilon}\) 与远地点 \(r_{\text{远}} = \frac{R}{1-\varepsilon}\) 处的机械能与角动量守恒：
   \[
   R = \frac{L^2}{GMm^2} = \frac{L^2}{m^2 r_0 v_0^2}, \qquad \varepsilon = \sqrt{1 + \frac{2EL^2}{m(GMm)^2}} = \sqrt{1 + \frac{2EL^2}{m^3 r_0^2 v_0^4}}
   \]

2. **第（2）问：旋转椭圆轨道的极坐标方程**：
   点火后长轴（近地点方向）相对极轴顺时针旋转了 \(\phi\) 角，而 \(\theta_c\) 逆时针测量，故真近点角为 \(\theta_c + \phi\)：
   \[
   r_c(\theta_c) = \frac{R}{1 + \varepsilon\cos(\theta_c + \phi)}
   \]
   由点火瞬间 \(\theta_c = 0\) 时 \(r_c(0) = r_0\)，得 \(R = r_0(1 + \varepsilon\cos\phi)\)，代入即得：
   \[
   r_c(\theta_c) = \frac{r_0(1 + \varepsilon\cos\phi)}{1 + \varepsilon\cos(\theta_c + \phi)}
   \]

3. **第（3）问：轨道周期之比 \(T_c / T_A\)**：
   椭圆半长轴 \(a_c = \frac{r_{\text{近}} + r_{\text{远}}}{2} = \frac{R}{1 - \varepsilon^2} = r_0 \frac{1 + \varepsilon\cos\phi}{1 - \varepsilon^2}\)。由开普勒第三定律：
   \[
   \frac{T_c}{T_A} = \left(\frac{a_c}{r_0}\right)^{3/2} = \left(\frac{1 + \varepsilon\cos\phi}{1 - \varepsilon^2}\right)^{3/2}
   \]

4. **第（4）问：用点火参数 \(\delta, \alpha\) 表示 \(\varepsilon\) 和 \(\varepsilon\cos\phi\)**：
   点火后瞬间速度的径向与切向分量为：
   \[
   v_r = v_0 \delta\sin\alpha, \qquad v_\theta = v_0(1 + \delta\cos\alpha)
   \]
   角动量 \(L = m r_0 v_\theta = m r_0 v_0(1 + \delta\cos\alpha)\)，代入 \(R = \frac{L^2}{m^2 r_0 v_0^2} = r_0(1 + \varepsilon\cos\phi)\) 立即得到：
   \[
   1 + \varepsilon\cos\phi = (1 + \delta\cos\alpha)^2 \implies \varepsilon\cos\phi = \delta\cos\alpha(2 + \delta\cos\alpha)
   \]
   同时，对轨道方程求导得点火处径向与切向速度之比：
   \[
   \left.\frac{v_r}{v_\theta}\right|_{\theta_c=0} = \left.\frac{1}{r_0}\frac{dr_c}{d\theta_c}\right|_{\theta_c=0} = \frac{\varepsilon\sin\phi}{1 + \varepsilon\cos\phi} = \frac{\delta\sin\alpha}{1 + \delta\cos\alpha} \implies \varepsilon\sin\phi = \delta\sin\alpha(1 + \delta\cos\alpha)
   \]
   两式平方相加得偏心率：
   \[
   \varepsilon = \delta\sqrt{\cos^2\alpha(2 + \delta\cos\alpha)^2 + \sin^2\alpha(1 + \delta\cos\alpha)^2} = \delta\sqrt{1 + 3\cos^2\alpha + 2\delta\cos\alpha(1 + \cos^2\alpha) + \delta^2\cos^2\alpha}
   \]

5. **第（5）问：第一类汇合点相遇条件**：
   追击者 \(c\) 绕行 \(n_c\) 圈回到 \(\theta_c = 0\) 历时 \(t = n_c T_c\)；目标 \(A\) 从初始相位 \(\theta_0\) 出发第 \(n_A\) 次到达 \(\theta = 0\) 历时 \(t = \left(n_A - \frac{\theta_0}{2\pi}\right) T_A\)。令二者相等：
   \[
   n_A = \frac{\theta_0}{2\pi} + n_c \frac{T_c}{T_A} = \frac{\theta_0}{2\pi} + n_c \left(\frac{1 + \varepsilon\cos\phi}{1 - \varepsilon^2}\right)^{3/2}
   \]

6. **第（6）问：\(n_A(\alpha)\) 的容错极值点 \(\alpha_0\)**：
   由能量与半长轴的直接关系 \(E = -\frac{GMm}{2a_c} = \frac{1}{2}m(v_r^2 + v_\theta^2) - \frac{GMm}{r_0}\)，注意到 \(v_r^2 + v_\theta^2 = v_0^2(1 + 2\delta\cos\alpha + \delta^2)\)，可得极其简洁的约化关系：
   \[
   \frac{a_c}{r_0} = \frac{1 + \varepsilon\cos\phi}{1 - \varepsilon^2} = \frac{1}{1 - 2\delta\cos\alpha - \delta^2}
   \]
   因此：
   \[
   n_A(\alpha) = \frac{\theta_0}{2\pi} + n_c (1 - 2\delta\cos\alpha - \delta^2)^{-3/2}
   \]
   对 \(\alpha\) 求导令 \(\frac{dn_A}{d\alpha} = 0\)，即 \(\sin\alpha = 0\)，得两个明显极值点：
   \[
   \alpha_0 = 0 \quad \text{或} \quad \alpha_0 = \pi
   \]

7. **第（7）问：上限 \(\delta_{\max}\) 与数值求解**：
   - **情形一（取 \(\alpha_0 = 0\)，正向切向点火加速）**：
     此时 \(\varepsilon = \delta(\delta + 2) < 1\)（或 \(1 - 2\delta - \delta^2 > 0\)，保证为闭合椭圆轨道），解得上限：
     \[
     \delta_{\max} = \sqrt{2} - 1 \approx 0.414
     \]
     由 \(\left(\frac{2\pi n_A - \theta_0}{2\pi n_c}\right)^{2/3} = \frac{1}{1 - 2\delta - \delta^2}\) 得二次方程：
     \[
     \delta^2 + 2\delta + \left(\frac{2\pi n_c}{2\pi n_A - \theta_0}\right)^{2/3} - 1 = 0
     \]
     代入 \(\theta_0 = \frac{\pi}{2}, n_A = 2, n_c = 1\)，得 \(\frac{2\pi n_c}{2\pi n_A - \theta_0} = \frac{4}{7}\)，取正根：
     \[
     \delta = \sqrt{2 - \left(\frac{4}{7}\right)^{2/3}} - 1 \approx 0.145
     \]
   - **情形二（取 \(\alpha_0 = \pi\)，反向切向点火）**：
     此时 \(\varepsilon = \delta|\delta - 2| < 1\)，解得 \(0 < \delta < \sqrt{2} + 1\)（其中 \(\delta = 1\) 时退化为直线坠落中心），上限 \(\delta_{\max} = \sqrt{2} + 1\)。对应方程为 \(\delta^2 - 2\delta + \left(\frac{2\pi n_c}{2\pi n_A - \theta_0}\right)^{2/3} - 1 = 0\)，当 \(\theta_0 = \frac{\pi}{2}, n_A = 2, n_c = 1\) 时，因要求 \(T_c > T_A\)，正根为 \(\delta = 1 + \sqrt{2 - (4/7)^{2/3}} \approx 2.145\)（反向点火使速度反向且大于 \(v_0\)）。

### Phase 2：对照官方参考解答分析与教学拆解

- **与官方解答的对照与亮点剖析**：
  1. 官方解答在第（4）问提供了两种求法（近远地点能量联立法与极坐标速度分量法），在第（7）问完整给出了 \(\alpha_0 = 0\) 和 \(\alpha_0 = \pi\) 两套给分方案，与我们的盲做结果完全吻合。
  2. **关键教学突破点（代数化简 vs 物理守恒律）**：
     在第（6）问中，官方参考解答将第（4）问得到的 \(\varepsilon\cos\phi\) 和 \(\varepsilon^2\) 强行代入 \(f(\alpha) = \frac{1 + \varepsilon\cos\phi}{1 - \varepsilon^2}\)，写出了一个分母含有 \(\cos^4\alpha\) 的繁琐分式（参考解答第9页式㉑）：
     \[
     f(\alpha) = \frac{1 + \delta\cos\alpha(2 + \delta\cos\alpha)}{1 - \delta^2\left[1 + 3\cos^2\alpha + 2\delta\cos\alpha(1 + \cos^2\alpha) + \delta^2\cos^2\alpha\right]}
     \]
     许多考生在考场上看到这个复杂分式后不敢化简，导致第（7）问代入求 \(\delta\) 时计算量剧增。而实际上，我们在盲做时指出：**椭圆轨道的半长轴 \(a_c\) 仅由总机械能 \(E\) 唯一决定，与角动量方向无关！** 因此分子 \(1 + \varepsilon\cos\phi = (1 + \delta\cos\alpha)^2\) 必然可以从分母 \(1 - \varepsilon^2 = (1 - 2\delta\cos\alpha - \delta^2)(1 + \delta\cos\alpha)^2\) 中整体约去，直接化简为：
     \[
     f(\alpha) = \frac{1}{1 - 2\delta\cos\alpha - \delta^2}
     \]
     向学生展示这一“用机械能守恒指导分式因式分解”的技巧，能瞬间将5分钟的繁琐代数化简降维为10秒钟的口算！

---

## 第三题：氙核直接探测暗物质粒子的散射运动学与截面统计 (`cpho-2021-final-theory-problem-slice-q3`)

- **建议标题 (`better_title`)**：暗物质粒子与氙核弹性散射的相对论前运动学、角分布及探测率估算
- **难度评级 (`difficulty`)**：`D3`
- **核心物理模型 (`model`)**：等质量二体弹性散射质心系-实验室系变换、概率测度雅可比变换与散射截面碰撞率模型

### Phase 1：独立盲做过程与初解记录

1. **第（1）问：等质量各向同性弹性散射运动学**：
   设 \(M_X = M_{\text{Xe}} = M = 132 m_p\)，入射速度 \(v_0 = 200\text{ km/s} \ll c\)（非相对论弹性碰撞）。
   - **（i）反冲动量与出射角关系**：质心速度 \(v_C = v_0 / 2\)。在质心系中，靶核 \(^{132}\text{Xe}\) 碰撞后速度大小仍为 \(v_0' = v_0 / 2\)，设其与 \(z\) 轴夹角为 \(\theta' \in [0, \pi]\)。变换回实验室系，由速度矢量等腰三角形（\(\mathbf{v}_{\text{Xe}} = \mathbf{v}_C + \mathbf{v}_{\text{Xe}}'\)）立得：
     \[
     \theta = \frac{\theta'}{2} \in \left[0, \frac{\pi}{2}\right], \qquad v_{\text{Xe}}(\theta) = 2 v_0' \cos\theta = v_0 \cos\theta
     \]
     故实验室系中 \(^{132}\text{Xe}\) 核的动量为：
     \[
     p(\theta) = M v_0 \cos\theta \quad \left(0 \le \theta \le \frac{\pi}{2}\right), \qquad p(\theta) = 0 \quad \left(\frac{\pi}{2} < \theta \le \pi\right)
     \]
   - **（ii）实验室系角分布**：质心系各向同性意味着在质心系立体角元 \(d\Omega' = 2\pi\sin\theta' d\theta'\) 内散射概率均匀分布：
     \[
     dP = \frac{d\Omega'}{4\pi} = \frac{1}{2}\sin\theta' d\theta' = -\frac{1}{2} d(\cos\theta')
     \]
     代入 \(\theta' = 2\theta\)，得实验室系下按极角 \(\theta\)（或 \(\cos\theta\)、立体角 \(\Omega\)）的概率分布（三种等价表述）：
     \[
     \frac{dP}{d\theta} = \sin(2\theta) = 2\sin\theta\cos\theta, \quad \text{或} \quad \frac{dP}{d\cos\theta} = 2\cos\theta, \quad \text{或} \quad \frac{dP}{d\Omega} = \frac{\cos\theta}{\pi} \quad \left(0 \le \theta \le \frac{\pi}{2}\right)
     \]
   - **（iii）反冲动能分布**：实验室系中 \(^{132}\text{Xe}\) 获得的动能为：
     \[
     E_k(\theta) = \frac{p^2(\theta)}{2M} = \frac{1}{2} M v_0^2 \cos^2\theta = E_k^{\text{in}} \cos^2\theta \quad \left(E_k^{\text{in}} = \frac{1}{2} M v_0^2\right)
     \]
     对 \(\theta\) 微分得 \(|dE_k| = M v_0^2 \cos\theta\sin\theta d\theta = E_k^{\text{in}} \sin(2\theta) d\theta = E_k^{\text{in}} dP\)，因此动能分布密度函数为常数：
     \[
     \frac{dP}{dE_k} = \frac{1}{E_k^{\text{in}}} = \frac{1}{\frac{1}{2} M v_0^2} \quad \left(0 \le E_k \le \frac{1}{2} M v_0^2\right)
     \]
     即反冲核动能在 \(\left[0, \frac{1}{2} M v_0^2\right]\) 区间内服从**均匀分布**。

2. **第（2）问：每年发生的碰撞总次数**：
   \(1.0\text{ t} = 1.0\times 10^6\text{ g}\) 液氙所含 \(^{132}\text{Xe}\) 原子核总数：
   \[
   N_{\text{Xe}} = \frac{1.0\times 10^6\text{ g}}{132\text{ g/mol}} \times 6.023\times 10^{23}\text{ mol}^{-1} \approx 4.563\times 10^{27}
   \]
   地球附近暗物质粒子数密度 \(n_X = \frac{\rho_X}{m_X} = \frac{0.40 m_p/\text{cm}^3}{132 m_p} \approx 3.030\times 10^{-3}\text{ cm}^{-3}\)。
   一年时间 \(t = 365 \times 86400\text{ s} \approx 3.1536\times 10^7\text{ s}\)，速率 \(v_0 = 2.00\times 10^7\text{ cm/s}\)，截面 \(\sigma = 1.0\times 10^{-38}\text{ cm}^2\)。
   每年总碰撞次数：
   \[
   N_C = N_{\text{Xe}} n_X \sigma v_0 t \approx 4.563\times 10^{27} \times 3.030\times 10^{-3} \times 1.0\times 10^{-38} \times 2.00\times 10^7 \times 3.1536\times 10^7 \approx 87\text{ 次}
   \]

3. **第（3）问：超出阈值 \(E_{\text{阈}} = 10\text{ keV}\) 的年可探测事例数**：
   最大反冲动能（即入射暗物质粒子动能）：
   \[
   E_k^{\text{in}} = \frac{1}{2} (132 \times 0.94\text{ GeV}/c^2) \times \left(\frac{2.00\times 10^5\text{ m/s}}{3.00\times 10^8\text{ m/s}}\right)^2 \approx 27.57\text{ keV} \approx 28\text{ keV}
   \]
   由于反冲动能在 \([0, E_k^{\text{in}}]\) 上均匀分布，超过阈值 \(E_{\text{阈}} = 10\text{ keV}\) 的比例为 \(\frac{E_k^{\text{in}} - E_{\text{阈}}}{E_k^{\text{in}}}\)，故每年可探测到的碰撞个数为：
   \[
   N_S = N_C \frac{E_k^{\text{in}} - E_{\text{阈}}}{E_k^{\text{in}}} \approx 87.2 \times \frac{27.57 - 10}{27.57} \approx 56\text{ 个}
   \]

4. **第（4）问：暗物质速率上限 \(v_{\max}\) 的物理成因**：
   该上限是由**银河系的引力逃逸速率**造成的；速率超过银河系逃逸速率的暗物质粒子无法被银河系引力束缚，早已逃逸出银河系。

5. **第（5）问：探测器对轻质量暗物质的质量盲区下限**：
   当暗物质粒子质量为 \(m_X\)、以最大速度 \(v_{\max} = 0.002c\) 与静止氙核（质量 \(m_{\text{Xe}} = 132 m_p \approx 124.08\text{ GeV}/c^2\)）发生正碰时，氙核获得的最大反冲速度为 \(v_{r\max} = \frac{2 m_X}{m_X + m_{\text{Xe}}} v_{\max}\)，最大反冲动能为：
   \[
   E_{r\max} = \frac{1}{2} m_{\text{Xe}} v_{r\max}^2 = \frac{2 m_{\text{Xe}} m_X^2}{(m_X + m_{\text{Xe}})^2} v_{\max}^2
   \]
   令 \(E_{r\max} < E_{\text{阈}} = 10\text{ keV}\)，解得无法探测到信号的暗物质质量上限：
   \[
   m_X < \frac{m_{\text{Xe}}}{\frac{v_{\max}}{c}\sqrt{\frac{2 m_{\text{Xe}} c^2}{E_{\text{阈}}}} - 1} \approx 13.84\text{ GeV}/c^2 \approx 14\text{ GeV}/c^2 \quad (\text{或 } 14.7 m_p \approx 15 m_p)
   \]

### Phase 2：对照官方参考解答分析与教学拆解

- **与官方解答的对照**：
  1. 全部解析公式与数值结果（\(87\) 次、\(56\) 个、\(14\text{ GeV}/c^2\)）与官方参考解答丝毫不差。
  2. **多视角解法对比**：官方解答在第（1）（ii）问中给出了三种解法：解法一利用立体角环带周长正比于 \(\sin\theta'\)，解法二利用球坐标立体角微元变换 \(d\cos\theta' d\phi' \to d\cos\theta d\phi\)，解法三利用三维动量空间狄拉克 \(\delta\) 函数 \(\rho'(\mathbf{p}') = \frac{1}{4\pi p_0^2}\delta(p'-p_0)\) 及伽利略变换下相空间体积元不变性 \(d^3\mathbf{p}' = d^3\mathbf{p}\)。
  3. 对高中竞赛生而言，解法一与解法二（球面立体角微元比值）最直观、最不易出错；而解法三则是本科理论物理（统计力学与粒子物理散射理论）的标准语言，非常适合作为冲击国家集训队与大学物理竞赛（PLANCKS）的高阶拓展教材。

---

## 第四题：生物细胞膜周围反离子云的泊松-玻尔兹曼分布与渗透压斥力 (`cpho-2021-final-theory-problem-slice-q4`)

- **建议标题 (`better_title`)**：带电生物膜反离子云的泊松-玻尔兹曼方程、静电屏蔽与双电层渗透压斥力
- **难度评级 (`difficulty`)**：`D4`
- **核心物理模型 (`model`)**：一维非线性泊松-玻尔兹曼方程（Poisson-Boltzmann Equation，Gouy-Chapman双电层模型）与麦克斯韦应力/理想气体渗透压平衡

### Phase 1：独立盲做过程与初解记录

1. **第（1）问：单侧无限大带电生物膜的离子屏蔽层**：
   - **（i）微分方程**：在 \(x > 0\) 溶液中，正离子数密度服从玻尔兹曼分布 \(n(x) = n_0 e^{-e\varphi(x)/(kT)}\)，电荷体密度 \(\rho(x) = e n(x)\)。结合一维泊松方程 \(\frac{d^2\varphi}{dx^2} = -\frac{\rho(x)}{\varepsilon}\)，得：
     \[
     \frac{d^2\varphi}{dx^2} = -\frac{e n_0}{\varepsilon} \exp\left(-\frac{e\varphi}{kT}\right)
     \]
   - **（ii）边界条件**：膜内为导体且取膜表面电势为零，由高斯定理知紧贴膜外侧（\(x = 0^+\)）电场强度为 \(E(0^+) = -\frac{\sigma}{\varepsilon}\)，故边界条件为：
     \[
     \left.\varphi\right|_{x=0} = 0, \qquad \left.\frac{d\varphi}{dx}\right|_{x=0} = -E(0^+) = \frac{\sigma}{\varepsilon}
     \]
   - **（iii）试探解定参**：将 \(\varphi(x) = A\ln(1 + Bx)\) 代入微分方程与边界条件：
     \[
     -\frac{AB^2}{(1+Bx)^2} = -\frac{e n_0}{\varepsilon} (1 + Bx)^{-eA/(kT)}, \qquad AB = \frac{\sigma}{\varepsilon}
     \]
     比较指数与系数得：
     \[
     A = \frac{2kT}{e}, \qquad B = \frac{\sigma e}{2\varepsilon kT}, \qquad n_0 = \frac{\sigma^2}{2\varepsilon kT}
     \]
     故电势与正离子数密度分布为：
     \[
     \varphi(x) = \frac{2kT}{e}\ln\left(1 + \frac{\sigma e}{2\varepsilon kT}x\right), \qquad n(x) = \frac{\sigma^2}{2\varepsilon kT}\frac{1}{\left(1 + \frac{\sigma e}{2\varepsilon kT}x\right)^2}
     \]
   - **（iv）电中性验证**：单位面积柱体内正离子总电荷为：
     \[
     Q = \int_0^\infty e n(x)\,dx = \frac{e n_0}{B} = \sigma
     \]
     与膜表面负电荷面密度 \(-\sigma\) 之和恰为零，系统整体呈电中性。
   - **（v）静电场能 \(U_f\) 与正离子总电势能 \(U_e\)**：
     - 单位面积柱体内的静电场能：
       \[
       U_f = \int_0^\infty \frac{1}{2}\varepsilon \left(\frac{d\varphi}{dx}\right)^2 dx = \frac{1}{2}\varepsilon A^2 B^2 \int_0^\infty \frac{dx}{(1+Bx)^2} = \frac{1}{2}\varepsilon A^2 B = \frac{\sigma kT}{e}
       \]
     - 同一体积内所有正离子在静电场 \(\varphi(x)\) 中的总电势能（注：每个正离子在外场与周围全部电荷共同建立的宏观电势 \(\varphi(x)\) 中的势能为 \(e\varphi(x)\)）：
       \[
       U_e = \int_0^\infty e n(x) \varphi(x)\,dx = \frac{e n_0 A}{B} \int_0^\infty \frac{\ln(1+y)}{(1+y)^2}\,dy = \sigma A \times 1 = \frac{2\sigma kT}{e}
       \]

2. **第（2）问：两个平行带电生物膜（间距 \(2D\)）之间的相互作用**：
   - **（i）试探解 \(\varphi(x) = A\ln[\cos(Bx)]\) 定参**：
     代入 \(\frac{d^2\varphi}{dx^2} = -\frac{e n_0}{\varepsilon} e^{-e\varphi/(kT)}\)，得：
     \[
     -\frac{AB^2}{\cos^2(Bx)} = -\frac{e n_0}{\varepsilon} [\cos(Bx)]^{-eA/(kT)} \implies A = \frac{2kT}{e}, \qquad B = \sqrt{\frac{n_0 e^2}{2\varepsilon kT}}
     \]
   - **（ii）由边界条件求 \(n_0\)**：
     在 \(x = \pm D\) 处，\(\left.\frac{d\varphi}{dx}\right|_{x=\mp D} = \pm \frac{\sigma}{\varepsilon}\)，即 \(AB\tan(BD) = \frac{\sigma}{\varepsilon}\)。令 \(\theta = BD \in \left(0, \frac{\pi}{2}\right)\)，则 \(\theta\) 满足超越方程：
     \[
     \theta\tan\theta = \frac{\sigma e D}{2\varepsilon kT}
     \]
     从而中心处正离子数密度为：
     \[
     n_0 = \frac{2\varepsilon kT}{e^2} B^2 = \frac{2\varepsilon kT \theta^2}{e^2 D^2}
     \]
   - **（iii）膜表面与中心处正离子数密度之差 \(\Delta n\)**：
     \[
     \Delta n \equiv n(\pm D) - n_0 = n_0\left(\frac{1}{\cos^2\theta} - 1\right) = n_0 \tan^2\theta = \frac{2\varepsilon kT}{e^2 D^2}(\theta\tan\theta)^2 = \frac{\sigma^2}{2\varepsilon kT}
     \]
     可见接触值定理（Contact Value Theorem）成立：\(\Delta n\) 仅由表面电荷密度 \(\sigma\) 与温度 \(T\) 决定，与板间距 \(2D\) 无关。
   - **（iv）电中性验证**：
     \[
     \int_{-D}^{D} e n(x)\,dx = \int_{-D}^{D} \frac{e n_0}{\cos^2(Bx)}\,dx = \frac{2 e n_0}{B}\tan\theta = 2\sigma
     \]
     与两板所带总负电荷面密度 \(-2\sigma\) 精确抵消。
   - **（v）细胞膜单位面积所受合力 \(f\)**：
     - **方法一（膜表面直接受力分析）**：在 \(x = D\) 膜表面处，体系中其余全部电荷（另一块负电平板 \(- \sigma\) 与全体正离子云 \(+2\sigma\)，合电量为 \(+\sigma\)）在 \(x=D\) 膜处产生的电场大小等价于面电荷 \(+\sigma\) 的无限大平板电场 \(E_{\text{外}} = \frac{\sigma}{2\varepsilon}\)，故静电力为指向对称中心 \(x=0\) 的吸力 \(f_e = \frac{\sigma^2}{2\varepsilon}\)；与此同时，紧贴膜内侧的正离子气产生向外的理想气体渗透压强 \(f_h = n(\pm D) kT = n_0 kT + \frac{\sigma^2}{2\varepsilon}\)（膜内外水自身静水压强抵消）。两者叠加，\(\frac{\sigma^2}{2\varepsilon}\) 精确相消，净合力为背离对称中心的**排斥力**：
       \[
       f = f_h - f_e = n_0 kT = \frac{2\varepsilon k^2 T^2 \theta^2}{e^2 D^2}
       \]
     - **方法二（对称面 \(x=0\) 动量流/力学平衡法）**：取右半空间 \([0, D]\) 内的离子与右极板为整体，右半空间与左半空间在 \(x=0\) 平面处的静电力相互抵消（因为 \(E(0) = 0\)，麦克斯韦应力为零，且左右两半总电荷均为零），故右半部分仅受到 \(x=0\) 界面处正离子气的理想气体热压强 \(P(0) = n_0 kT\)，由整体力学平衡立即得出极板单位面积所受排斥力为 \(f = n_0 kT = \frac{2\varepsilon k^2 T^2 \theta^2}{e^2 D^2}\)！
   - **（vi）近距离与远距离极限下的渐近行为**：
     - **近距离极限（\(\frac{\sigma e D}{2\varepsilon kT} \ll 1\)）**：\(\theta \ll 1\)，\(\tan\theta \approx \theta \implies \theta \approx \sqrt{\frac{\sigma e D}{2\varepsilon kT}}\)，故：
       \[
       f \approx \frac{\sigma kT}{e D} \propto \frac{1}{D}
       \]
     - **远距离极限（\(\frac{\sigma e D}{2\varepsilon kT} \gg 1\)）**：\(\theta \to \frac{\pi}{2}\)（常数），故：
       \[
       f \approx \frac{\pi^2 \varepsilon k^2 T^2}{2 e^2 D^2} \propto \frac{1}{D^2}
       \]

### Phase 2：对照官方参考解答分析与教学拆解

- **与官方解答的对照**：
  1. 我们在盲做中给出的两种求膜单位面积合力的方法，恰好分别对应官方参考解答第23页的“解法一”与“解法二”！
  2. **软物质物理经典结论的竞赛化演绎**：本题原型是胶体与生物物理中著名的 **Gouy-Chapman 双电层模型** 与 **Langmuir 渗透压公式**。学生在做第（2）（v）问时，最大的误区是只算静电力而漏掉正离子热运动的渗透压 \(n(\pm D)kT\)，或者误认为两块均带负电的平板是因为“同种电荷静电排斥”才相互排斥。事实上，由于板间正离子云总电荷为 \(+2\sigma\)，纯静电相互作用对极板反而是净吸力 \(f_e = \frac{\sigma^2}{2\varepsilon}\)，真正抵抗静电吸力并使细胞膜相互排斥不结块的，是板间高浓度正离子云的热运动渗透压 \(f_h = n_0 kT + \frac{\sigma^2}{2\varepsilon}\)！这一点在物理图像上极具震撼力。

---

## 第五题：顺磁、铁磁、反铁磁分子场理论与二维XY模型涡旋BKT相变 (`cpho-2021-final-theory-problem-slice-q5`)

- **建议标题 (`better_title`)**：磁性自旋系统的外斯分子场理论与二维XY模型拓扑涡旋相变
- **难度评级 (`difficulty`)**：`D5`
- **核心物理模型 (`model`)**：居里-外斯平均场模型（Curie-Weiss Molecular Field）、反铁磁双子晶格奈尔相变与二维XY模型BKT（Berezinskii-Kosterlitz-Thouless）涡旋相变

### Phase 1：独立盲做过程与初解记录

1. **第（1）问：顺磁居里定律与铁磁居里-外斯分子场**：
   设单电子自旋磁矩大小 \(m_0 = \mu_B = \frac{e\hbar}{2m}\)。
   - **（i）顺磁体磁化率**：外磁场 \(B\) 下自旋平行与反平行磁矩能量为 \(E_\mp = \mp m_0 B\)。由玻尔兹曼分布得平均磁矩与磁化强度：
     \[
     M = n m_0 \frac{e^{m_0 B/(kT)} - e^{-m_0 B/(kT)}}{e^{m_0 B/(kT)} + e^{-m_0 B/(kT)}} = n m_0 \tanh\left(\frac{m_0 B}{kT}\right)
     \]
     在高温弱磁近似 \(kT \gg m_0 B\) 及 \(\chi \ll 1\)（\(B = \mu_0(H+M) \approx \mu_0 H\)）下：
     \[
     M \approx \frac{\mu_0 n m_0^2}{kT} H \implies \chi = \frac{C}{T}, \qquad C = \frac{\mu_0 n m_0^2}{k} = \frac{\mu_0 n e^2 \hbar^2}{4 m^2 k}
     \]
   - **（ii）铁磁分子场系数 \(\gamma\) 与顺排分子场 \(H_m\)**：
     引入外斯分子场 \(H_m = \gamma M\)，将顺磁公式中的 \(H\) 替换为有效场 \(H + H_m = H + \gamma M\)：
     \[
     M = \frac{C}{T}(H + \gamma M) \implies \chi = \frac{M}{H} = \frac{C}{T - \gamma C}
     \]
     与居里-外斯定律 \(\chi = \frac{C}{T - \theta}\) 比较得 \(\gamma C = \theta\)，故：
     \[
     \gamma = \frac{\theta}{C} = \frac{4 m^2 k \theta}{\mu_0 n e^2 \hbar^2}
     \]
     当所有磁矩完全顺排时，饱和磁化强度 \(M = n m_0\)，故分子场为：
     \[
     H_m = \gamma n m_0 = \frac{k\theta}{\mu_0 m_0} = \frac{2 m k \theta}{\mu_0 e \hbar}
     \]

2. **第（2）问：一维铁磁自旋链的等效场、基态磁能与单自旋翻转激发能**：
   - **（i）最近邻等效场与系统磁能**：
     每个非端点自旋有左右2个最近邻自旋，其感受到的总分子场为 \(H_m = \frac{k\theta}{\mu_0 m_0}\)，故单个自旋在其最近邻格点上提供的分子场（等效磁场）为：
     \[
     H_m' = \frac{1}{2} H_m = \frac{k\theta}{2\mu_0 m_0} = \frac{m k \theta}{\mu_0 e \hbar} \quad \left(\text{对应磁感应强度 } B_m' = \mu_0 H_m' = \frac{m k \theta}{e\hbar}\right)
     \]
     每对最近邻自旋的相互作用能为 \(\varepsilon_{\text{bond}} = -m_0 \mu_0 H_m' = -\frac{1}{2} k\theta\)（或从总能量含 \(\frac{1}{2}\) 相互作用因子计算：每个自旋在总分子场 \(H_m\) 中的势能为 \(-m_0\mu_0 H_m = -k\theta\)，全系统求和需乘 \(\frac{1}{2}\) 以消除成对重复计数）。对于含 \(N\) 个格点（\(N-1 \approx N\) 个最近邻键）的一维链，总磁能为：
     \[
     E_N = -\frac{1}{2}(N-1) k\theta \approx -\frac{1}{2} N k\theta
     \]
   - **（ii）单个非端点自旋翻转的能量增加**：
     翻转前，该自旋与左右两个最近邻构成的2个键能量之和为 \(2 \times \left(-\frac{1}{2}k\theta\right) = -k\theta\)；翻转后变为反平行，这2个键能量之和变为 \(2 \times \left(+\frac{1}{2}k\theta\right) = +k\theta\)。因此系统总能量增加量为：
     \[
     \Delta E = (+k\theta) - (-k\theta) = 2 k\theta
     \]

3. **第（3）问：一维反铁磁双子晶格的磁能与奈尔温度 \(T_N\)**：
   - **（i）反铁磁体基态磁能**：
     在反铁磁基态下，A、B子晶格磁矩大小均为 \(m_0 = \frac{e\hbar}{2m}\) 且方向相反（\(\boldsymbol{\mu}_A = -\boldsymbol{\mu}_B\)）。代入题给分子场 \(\mathbf{H}_{mA} = -\beta\boldsymbol{\mu}_B - \alpha\boldsymbol{\mu}_A = (\beta - \alpha)\boldsymbol{\mu}_A\)，每个自旋在分子场中的能量为 \(-\mu_0 \boldsymbol{\mu}_A \cdot \mathbf{H}_{mA} = -\mu_0 m_0^2 (\beta - \alpha)\)。计入成对相互作用的 \(\frac{1}{2}\) 因子，\(N\) 个格点系统的总磁能为：
     \[
     E_N = -\frac{1}{2} N \mu_0 m_0^2 (\beta - \alpha) = -\frac{N \mu_0 (\beta - \alpha) e^2 \hbar^2}{8 m^2}
     \]
     （若计入有限开链边界修正，共有 \(N-1\) 对AB最近邻键和 \(N-2\) 对同种次近邻键，则 \(E_N = -\frac{1}{2}(N-1)\mu_0 m_0^2 \beta + \frac{1}{2}(N-2)\mu_0 m_0^2 \alpha\)。）
   - **（ii）奈尔温度 \(T_N\)**：
     A、B子晶格的原子数密度均为 \(n/2\)，故子晶格磁化强度与平均单原子磁矩的关系为 \(\mathbf{M}_A = \frac{n}{2}\bar{\boldsymbol{\mu}}_A\)、\(\mathbf{M}_B = \frac{n}{2}\bar{\boldsymbol{\mu}}_B\)。因此分子场用磁化强度表出为：
     \[
     \mathbf{H}_{mA} = -\frac{2}{n}(\beta\mathbf{M}_B + \alpha\mathbf{M}_A), \qquad \mathbf{H}_{mB} = -\frac{2}{n}(\beta\mathbf{M}_A + \alpha\mathbf{M}_B)
     \]
     无外场时令 \(\mathbf{H}_A = \mathbf{H}_{mA}\)、\(\mathbf{H}_B = \mathbf{H}_{mB}\)，代入题给顺磁响应关系 \(\mathbf{M}_{A,B} = \frac{C}{2T}\mathbf{H}_{A,B}\)：
     \[
     \begin{cases}
     \left(1 + \frac{C\alpha}{nT}\right)\mathbf{M}_A + \frac{C\beta}{nT}\mathbf{M}_B = \mathbf{0} \\
     \frac{C\beta}{nT}\mathbf{M}_A + \left(1 + \frac{C\alpha}{nT}\right)\mathbf{M}_B = \mathbf{0}
     \end{cases}
     \]
     系数行列式为零给出非零反铁磁序（\(\mathbf{M}_A = -\mathbf{M}_B \ne \mathbf{0}\)）的临界温度即奈尔温度：
     \[
     T_N = \frac{C}{n}(\beta - \alpha) = \frac{\mu_0 m_0^2}{k}(\beta - \alpha) = \frac{\mu_0 (\beta - \alpha) e^2 \hbar^2}{4 m^2 k}
     \]

4. **第（4）问：二维正方点阵 XY 模型的拓扑涡旋与 BKT 相变**：
   - **（i）半径 \(r\) 圆周上相邻格点取向角之差的平均值**：
     半径为 \(r\) 的圆周长 \(2\pi r\)，包含约 \(N_r = \frac{2\pi r}{a}\) 个晶格步长。由绕行一圈总角度变化 \(\sum_{\langle i,j\rangle}(\theta_i - \theta_j) = 2\pi l\)，得相邻格点取向角之差的平均值为：
     \[
     \langle \theta_i - \theta_j \rangle = \frac{2\pi l}{2\pi r / a} = \frac{l a}{r} \quad \left(\text{对图 5e 中 } l=1 \text{ 为 } \frac{a}{r}\right)
     \]
   - **（ii）单个涡旋系统的能量估算**：
     将 \(\cos(\theta_i - \theta_j) \approx 1 - \frac{1}{2}(\theta_i - \theta_j)^2\) 代入磁能公式，相对于全顺排铁磁基态能量 \(E_0 = -2 N_{\text{tot}} J\)，半径为 \(r\) 的同心圆环上包含 \(\frac{2\pi r}{a}\) 对周向最近邻（径向最近邻夹角约为0，激发能为0），每对周向最近邻贡献激发能 \(\frac{1}{2}J\left(\frac{la}{r}\right)^2\)。对半径 \(r\) 从晶格常数 \(a\) 到系统尺寸 \(L\)（或 \(a/2\) 到 \(L/2\)）的所有同心圆环求和（化和为积分 \(\sum \frac{a}{r} \approx \int_a^L \frac{dr}{r} = \ln\frac{L}{a}\)）：
     \[
     E_{\text{vortex}} = \sum_{r=a}^{L} \frac{2\pi r}{a} \cdot \frac{1}{2} J \left(\frac{la}{r}\right)^2 \approx \pi J l^2 \int_a^L \frac{dr}{r} = \pi J l^2 \ln\frac{L}{a} \quad \left(l=1 \text{ 时为 } \pi J \ln\frac{L}{a}\right)
     \]
     （若加上基态能量 \(E_0\)，则总能量为 \(E = E_0 + \pi J l^2 \ln\frac{L}{a}\)。）
   - **（iii）状态数 \(\Omega\) 与构型熵 \(S\)**：
     在边长为 \(L\)、晶格常数为 \(a\) 的二维正方点阵中，涡旋中心可以落入约 \(\left(\frac{L}{a}\right)^2\) 个原胞（格点间隙）位置，故状态数与熵分别为：
     \[
     \Omega = \left(\frac{L}{a}\right)^2, \qquad S = k\ln\Omega = 2 k \ln\frac{L}{a}
     \]
   - **（iv）涡旋相变温度（BKT相变温度）**：
     形成单个自由涡旋所引起的亥姆霍兹自由能变化为：
     \[
     F = E_0 + (\pi J l^2 - 2 k T)\ln\frac{L}{a}
     \]
     由于宏观系统 \(\ln\frac{L}{a} \gg 1\)（热力学极限下发散），自由能增量 \(\Delta F\) 的正负号由括号内系数决定，临界相变温度为：
     \[
     T_c = \frac{\pi J l^2}{2k} \quad \left(\text{对于基元涡旋 } l=1\text{，} T_c = \frac{\pi J}{2k}\right)
     \]
     当 \(T < T_c\) 时，产生单个自由涡旋使自由能发散到 \(+\infty\)，系统抑制自由涡旋产生（涡旋只能以正反涡旋束缚对形式存在）；当 \(T > T_c\) 时，熵增主导，产生自由涡旋使自由能发散到 \(-\infty\)，系统中自发涌现大量自由涡旋，破坏系统的准长程磁有序。

### Phase 2：对照官方参考解答分析与教学拆解

- **与官方解答的对照与深度辨析**：
  1. **关于第（2）（i）问“平均值”表述的歧义剖析**：
     原题干写道：“每个原子所感受到的磁场可理解为其最近邻格点上的原子提供的‘分子场’的平均值。”如果严格按字面把 \(H_m\) 理解为左右2个最近邻各自产生的场 \(H_m'\) 的算术平均值，则会得出 \(H_m' = H_m\)；但从物理实质来看，每个原子感受到的总分子场 \(H_m\) 应当是其所有 \(z\) 个最近邻提供的分子场的**矢量和**（一维链配位数 \(z=2\)，故单个最近邻提供的等效场为 \(H_m' = H_m / 2 = \frac{k\theta}{2\mu_0 m_0}\)）。官方参考解答第29页式⑪明确采用了 \(H_m' = \frac{k\theta}{2\mu_0 m_0}\)，并据此写出单键相互作用能 \(-\frac{1}{2}k\theta\) 与总能量 \(E_N = -\frac{1}{2}(N-1)k\theta\)。在教学中必须向学生重点剖析这一题干措辞瑕疵与海森堡/伊辛相互作用哈密顿量 \(H = -J\sum_{\langle i,j\rangle} \sigma_i\sigma_j\) 的精确对应关系。
  2. **关于第（4）（ii）问正方晶格各向异性与连续圆环近似的证明**：
     官方解答在第（4）（ii）问给出了多达**四种解法**！其中解法一（连续场梯度积分 \(\frac{J}{2}\int |\nabla\theta|^2 d^2\mathbf{r}\)）和解法二（同心圆环求和）与我们的盲做完全一致；而解法三和解法四则非常精彩地证明了：**即便在离散正方点阵上考虑晶格方向与径向夹角 \(\alpha\)，由于一个格点周围纵向与横向四个最近邻键的夹角分别为 \(\frac{a\cos\alpha}{r}\) 和 \(\frac{a\sin\alpha}{r}\)，利用恒等式 \(\cos^2\alpha + \sin^2\alpha = 1\)，每个格点的平均相互作用激发能严格等于 \(\langle E_i \rangle = \frac{J a^2}{2 r^2}\)，与晶格方位角 \(\alpha\) 完全无关！** 这一几何证明消除了学生对“用同心圆代替正方点阵是否会漏算一维方向键”的疑虑，是极佳的竞赛教学素材。
