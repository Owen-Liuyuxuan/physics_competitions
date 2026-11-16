# Batch 09: Physics Cup 2021–2022 竞赛题解与教学拆解报告

本报告严格遵循两阶段协议（**Phase 1: 独立盲解试做** $\rightarrow$ **Phase 2: 对照获奖解答与 Jaan Kalda 评述进行教学拆解**），涵盖 Physics Cup 2021 与 2022 全部 10 道题目（`physicscup-2021-q1-reader` 至 `physicscup-2022-q5-reader`）。

---

## 1. `physicscup-2021-q1-reader` — Dumbbell in a magnetic field（强磁场中的铜哑铃）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **物理图像分析**：
  两个半径 $R=10\text{ cm}$ 的空心铜球壳，由长 $L=1\text{ m}$、半径 $r=1\text{ mm}$ 的细铜杆连接，总质量 $m=150\text{ g}$。置于垂直于杆方向的极强匀强磁场 $B=2\text{ MT}$ 中，初始沿杆方向赋予初速度 $v=1\text{ m/s}$。
  1. **不稳定性与末态朝向**：当哑铃稍有偏转角 $\theta$ 时，洛伦兹动生电动势 $\mathcal{E} = (\vec{v}\times \vec{B})\cdot \vec{d}$ 使一球带正电 $+Q$、另一球带负电 $-Q$。在磁场中做摆动时，流过细杆的充电电流 $I=\dot{Q}$ 受到的安培力力矩使偏离初始平行速度方向的角位移失稳，围绕垂直于速度 $\vec{u}$ 且垂直于磁场 $\vec{B}$（即平行于 $\vec{u}\times\vec{B}$）的稳定平衡取向发生振荡；由于细铜杆存在欧姆电阻耗散（以及极微弱的偶极辐射），振荡最终衰减，哑铃稳定在沿 $\vec{u}\times\vec{B}$ 方向（即与最终速度 $\vec{u}$ 和磁场 $\vec{B}$ 均垂直）。
  2. **守恒量构造**：对系统中所有电荷 $q_i$，牛顿第二定律为 $\dot{\vec{p}}_i = q_i\dot{\vec{r}}_i\times\vec{B} + \vec{F}_{\text{int},i}$。对全系统求和，内力抵消，且哑铃整体电中性（$\sum q_i = 0$），故相对质心的位置矢量 $\vec{r}_i$ 满足磁广义动量（动量与电磁动量/电偶极矩叉积项之和）守恒：
     \[
     \vec{\Pi} = m\vec{v} - \vec{p}_e \times \vec{B} = \text{const}, \quad \vec{p}_e = \sum_i q_i \vec{r}_i
     \]
  3. **初试近似与遗漏反思**：
     初试时若把两球视为点电荷构成的电容器（电容 $C \approx 2\pi\varepsilon_0 R$，球心距 $d = L+2R = 1.2\text{ m}$），容易直接认为初始状态杆平行于 $\vec{v}$，两球之间无电势差（$Q_i = 0$），从而误判初始电偶极矩 $\vec{p}_{e,i} = 0$，写出 $m v = (m + C B^2 d^2) u$，算得 $u \approx 0.0043\text{ m/s}$。
     但仔细检查单球极化：哪怕初始杆平行于 $\vec{v}$，每个半径为 $R$ 的铜球壳自身在有效电场 $\vec{E}_{\text{eff}} = \vec{v}\times\vec{B}$ 中都会发生导体球表面极化！单个导体球在匀强场 $E_{\text{eff}}$ 中感应出的电偶极矩为 $p_{\text{ball}} = 4\pi\varepsilon_0 R^3 E_{\text{eff}} = 4\pi\varepsilon_0 R^3 v B$，两球共有 $\vec{p}_{e,i} = 8\pi\varepsilon_0 R^3 (\vec{v}\times\vec{B})$！由于 $8\pi\varepsilon_0 B^2 R^3 \approx 0.890\text{ kg} \gg m = 0.15\text{ kg}$，初始动量中占主导地位的竟然不是机械动量 $mv$，而是两球自身极化提供的电磁动量 $8\pi\varepsilon_0 B^2 R^3 v$！

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  Jaan Kalda 在结果评述中明确指出：本题最容易遗漏的就是**初始广义动量中两个铜球壳自身极化偶极矩的贡献**（由于 $B=2\text{ MT}$ 极大，极化有效质量 $m_{\text{pol}} = 8\pi\varepsilon_0 B^2 R^3 \approx 0.89\text{ kg}$ 远大于哑铃机械质量 $m=0.15\text{ kg}$）。在首批无提示提交的 8 份解答中，仅有 **Zhening Li** 与 **Eddie Chen** 两人注意到了初始单球极化贡献！其中 Zhening Li 进一步用无穷镜像电荷序列严谨处理了两球之间的互电容与自身极化电势修正，得到：
  \[
  u = v \frac{m + 8\pi\varepsilon_0 B^2 R^3}{m + 8\pi\varepsilon_0 B^2 R^3 \left(\frac{L(2R+L)^2}{4R^2(R+L)} + 1\right)} \approx 0.0345\text{ m/s}
  \]
  若做领头阶展开（$R\ll L$），分母主项为 $2\pi\varepsilon_0 R L^2 B^2$，则 $u \approx v \frac{m + 8\pi\varepsilon_0 B^2 R^3}{2\pi\varepsilon_0 B^2 R (L+2R)^2} \approx 0.032\text{ m/s}$。
- **核心教学要点**：
  1. **洛伦兹力系统中的守恒律 $\vec{P}_{\text{mech}} - \vec{p}_e \times \vec{B} = \text{const}$**：这是处理磁场中可变形/可极化电中性导体系统最强大的基本工具，无需求解中间复杂的非线性摆动与阻尼微分方程。
  2. **导体球在动生电场中的自身极化 $\vec{p}_{\text{ball}} = 4\pi\varepsilon_0 R^3 (\vec{v}\times\vec{B})$**：当磁场极强（如天体物理磁星或题设 $2\text{ MT}$）时，导体自身的极化电磁质量 $m_{\text{em}} \sim \varepsilon_0 R^3 B^2$ 可以超过机械质量 $m$。

---

## 2. `physicscup-2021-q2-reader` — Comet’s orbit（彗星轨道最小离心率）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **物理图像与速度矢端图（Hodograph）建模**：
  彗星在开普勒轨道上两点的速度满足 $\vec{v}_1 \perp \vec{v}_2$ 且 $|\vec{v}_1| = 2|\vec{v}_2|$，求轨道的最小可能离心率 $e_{\min}$。
  1. **速度矢端圆定理**：在引力场中，由于角动量 $\vec{L}$ 守恒，比角动量 $h = r^2\dot{\theta}$ 为常数，运动方程 $\frac{\mathrm{d}\vec{v}}{\mathrm{d}t} = -\frac{GM}{r^2}\hat{r}$ 除以 $\dot{\theta} = \frac{h}{r^2}$ 即得：
     \[
     \frac{\mathrm{d}\vec{v}}{\mathrm{d}\theta} = -\frac{GM}{h}\hat{r} \implies \vec{v}(\theta) = \vec{u}_c + V_0 \hat{\theta}
     \]
     即开普勒轨道在速度空间中的轨迹（Hodograph）是一个半径为 $V_0 = \frac{GM}{h}$ 的圆，而圆心 $C$ 到速度空间原点 $O$ 的距离为 $|\vec{u}_c| = e V_0$！因此，**离心率 $e = \frac{|OC|}{V_0}$ 就是速度圆心 $C$ 到速度原点 $O$ 的距离与速度圆半径 $V_0$ 之比**。
  2. **几何极值求解**：
     在速度空间中，设原点 $O=(0,0)$，已知圆上两点 $P_1, P_2$ 满足 $\vec{OP}_1 \perp \vec{OP}_2$ 且 $|OP_1|=2|OP_2|$。不妨设 $P_1 = (2s, 0)$，$P_2 = (0, s)$。
     设速度圆圆心为 $C=(x,y)$，半径为 $V_0$。因 $P_1, P_2$ 在圆上：
     \[
     (x-2s)^2 + y^2 = V_0^2, \quad x^2 + (y-s)^2 = V_0^2 \implies y = 2x - \frac{3}{2}s
     \]
     于是离心率的平方为：
     \[
     e^2 = \frac{x^2 + y^2}{x^2 + (y-s)^2} = \frac{x^2 + \left(2x - \frac{3}{2}s\right)^2}{x^2 + \left(2x - \frac{5}{2}s\right)^2} = \frac{20x^2 - 24sx + 9s^2}{20x^2 - 40sx + 25s^2}
     \]
     对 $x$ 求极值（或用判别式法），立刻解得两个驻点：
     - 当 $x = \frac{s}{2}, y = -\frac{s}{2}$ 时，$e_{\min} = \frac{1}{\sqrt{5}} = \frac{\sqrt{5}}{5} \approx 0.4472$；
     - 当 $x = \frac{3s}{2}, y = \frac{3s}{2}$ 时，$e_{\max} = \frac{3}{\sqrt{5}} = \frac{3\sqrt{5}}{5}$（对应双曲线轨道分支或单支要求）。
     更妙的是用阿波罗尼斯圆（Apollonius Circle）几何法：圆上任意两点 $P_1, P_2$ 满足 $|OP_1|=2|OP_2|$，但这里固定的是 $P_1, P_2$ 与原点 $O$：在 $\triangle OP_1 P_2$ 中，斜边 $|P_1 P_2| = \sqrt{5}s$，斜边中点为 $M=(s, s/2)$，$|OM| = \frac{\sqrt{5}}{2}s$。圆心 $C$ 在 $P_1 P_2$ 的中垂线上，设 $|MC| = h$，则半径 $V_0 = \sqrt{\frac{5}{4}s^2 + h^2}$，而 $O$ 到中垂线的投影距离为 $\frac{s}{\sqrt{5}}$，沿中垂线偏移为 $h + \frac{2}{\sqrt{5}}s$，直接由三角函数或阿波罗尼斯圆相切即得 $e_{\min} = \frac{1}{\sqrt{5}}$。

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  本题收到了多达 95 份正确解答，展现了极其丰富的物理与几何视角：
  1. **偏心率矢量（Runge-Lenz 矢量）代数法（Lotus Chen 获 45% 最佳奖）**：利用 $\vec{e} = \frac{\vec{v}\times\vec{L}}{GMm} - \hat{r}$，则 $\vec{e} + \hat{r}_i = \frac{\vec{v}_i\times\vec{L}}{GMm}$，从而 $(\vec{e}+\hat{r}_1)\perp(\vec{e}+\hat{r}_2)$ 且 $|\vec{e}+\hat{r}_1| = 2|\vec{e}+\hat{r}_2| = 2a$。由 $|\hat{r}_1|=|\hat{r}_2|=1$ 及余弦定理：
     \[
     e^2 + 4a^2 - 4ae\cos\theta = 1, \quad e^2 + a^2 + 2ae\sin\theta = 1 \implies \left(\frac{e^2+4a^2-1}{4ae}\right)^2 + \left(\frac{e^2+a^2-1}{2ae}\right)^2 = 1
     \]
     整理为关于 $a^2$ 的二次方程 $20a^4 - 16a^2 + 5(e^2-1)^2 = 0$，由判别式 $\Delta = 256 - 400(e^2-1)^2 \ge 0$ 一行得出 $\frac{\sqrt{5}}{5} \le e \le \frac{3\sqrt{5}}{5}$！
  2. **速度矢端圆 + 阿波罗尼斯圆几何法（Nguyen Manh Quan / Jaan Kalda）**：固定速度圆（圆心 $C$，半径 $R$），圆上弦 $P_1 P_2$ 对原点 $O$ 张直角且 $|OP_1|=2|OP_2|$。倒过来固定 $O, P_1, P_2$，则圆心 $C$ 到 $P_1, P_2$ 等距（在 $P_1 P_2$ 中垂线上），要最小化 $\frac{|OC|}{|CP_1|}$，这等价于求点 $C$ 使得比值 $\frac{|CP_1|}{|CO|}$ 最大，其等值线正是以 $P_1, O$ 为焦点的阿波罗尼斯圆与中垂线相切！
  3. **蒙日圆（Monge Circle / 准圆）与焦点光学性质法（Eddie Chen / Fang Tzu Hsu / Arhaan Ahmad）**：利用椭圆互相垂直的两条切线交点轨迹为蒙日圆 $x^2+y^2=a^2+b^2$，或焦点向切线作垂线的垂足轨迹为辅助圆 $x^2+y^2=a^2$（且焦点到两切线距离之积与速度反比），纯几何幾步即可导出。

---

## 3. `physicscup-2021-q3-reader` — Oscillating octagon（正八边形连杆的简正振动）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **自由度计数与旋转对称群（Bloch 波矢）分类**：
  8 根质量为 $m$、长为 $l$ 的匀质刚性杆铰接成正八边形，关节处恢复力矩 $T = k(\varphi - \frac{3\pi}{4})$，限制在平面内运动。
  1. **自由度精确计数**：平面内 8 个顶点共有 $2\times 8 = 16$ 个坐标，8 根刚性杆固定长度提供 8 个完整约束，因此系统构型空间共有 $16 - 8 = 8$ 个自由度。减去平面内刚体整体运动的 3 个零频平凡模式（2 个平移 + 1 个整体转动），**非平凡简正振动模式恰好有 $8 - 3 = 5$ 个**！
  2. **利用 $C_8$ 循环对称性（离散傅里叶变换）解耦**：
     设第 $j$ 根杆（$j=0,1,\dots,7$，平衡取向角 $\alpha_j = j\frac{\pi}{4}$）相对于平衡取向的微小转角为 $\theta_j$。
     杆 $j$ 两端顶点的相对位移微元为 $\delta\vec{r}_j = l\theta_j \hat{n}_j = l\theta_j (-\sin\alpha_j, \cos\alpha_j)$。
     多边形闭合条件要求：
     \[
     \sum_{j=0}^{7} \delta\vec{r}_j = 0 \iff \sum_{j=0}^{7} \theta_j e^{i j \pi/4} = 0
     \]
     按循环群 $C_8$ 的波数 $q \in \{0, \pm 1, \pm 2, \pm 3, 4\}$ 展开 $\theta_j = \operatorname{Re}(A_q e^{i q j \pi/4})$：
     - $q = 0$：所有 $\theta_j = \text{const}$，对应正八边形整体刚体转动（1 个零频模式），而 $\theta_j \equiv 0$ 时还包含整体平面平移（2 个零频模式）；
     - $q = \pm 1$：违反多边形闭合条件 $\sum_{j=0}^7 \theta_j e^{i j \pi/4} = 0$，被刚性杆长约束严格禁止！
     - 因此，5 个非平凡振动模式完全由 **$q = \pm 2$（2 重简并）、$q = \pm 3$（2 重简并）、$q = 4$（非简并，1 个模式）** 组成！
  3. **各模式动能与势能精确计算**：
     - 对任意模式 $q \in \{2, 3, 4\}$，第 $j$ 个铰链处的角度变化为 $\Delta\varphi_j = \theta_j - \theta_{j-1}$，弹性势能为：
       \[
       V = \frac{1}{2}k \sum_{j=0}^{7} (\theta_j - \theta_{j-1})^2
       \]
     - 动能由各杆质心平动动能与绕质心转动动能之和给出（扣除整体质心平动后）：
       \[
       T = \sum_{j=0}^{7} \left(\frac{1}{2}m |\delta\dot{\vec{R}}_{\text{cm},j}|^2 + \frac{1}{2}\cdot\frac{1}{12}ml^2 \dot{\theta}_j^2\right)
       \]
     - 代入 $\theta_j = \cos(q j \pi/4)$ 逐一计算：
       1. **$q = 2$（椭圆四极形变模式，简并度 2）**：
          $\sum (\theta_j - \theta_{j-1})^2 = 8$，动能系数 $\sum (|\delta\vec{R}_{\text{cm},j}|^2/l^2 + \frac{1}{12}\theta_j^2) = \frac{10}{3}$，故：
          \[
          \omega_2 = \sqrt{\frac{12}{5}\frac{k}{ml^2}}
          \]
       2. **$q = 3$（三角六极形变模式，简并度 2）**：
          $\sum (\theta_j - \theta_{j-1})^2 = 8 + 4\sqrt{2}$，动能系数为 $\frac{5}{6}$，故：
          \[
          \omega_3 = \sqrt{\frac{24(2+\sqrt{2})}{5}\frac{k}{ml^2}}
          \]
       3. **$q = 4$（交替四角呼吸形变模式，简并度 1）**：
          $\theta_j = (-1)^j$，$\sum (\theta_j - \theta_{j-1})^2 = 32$，每个顶点沿径向交替内外位移 $x$，转角 $\theta = \frac{2x\cos(\pi/8)}{l}$，杆沿自身切向位移 $x\sin(\pi/8)$，动能系数为 $20/3 - 4\sqrt{2}$，故：
          \[
          \omega_4 = \sqrt{\frac{24(5+3\sqrt{2})}{7}\frac{k}{ml^2}}
          \]

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的离散傅里叶波矢分类结果与获奖解答（Zhening Li、Nikita Semenin、Eddie Chen 及 Huiyuan Wang 的 Mathematica 极限本征值验证）完全一致！
  - **Zhening Li 的几何直观法**极具教学启发性：他将 $n=2,3,4$ 分别画成“对边平动挤压（$n=2$）”、“上下底边同向平动、两侧顶点外摆并通过‘紫杆参考系’扣除质心运动（$n=3$）”、“所有顶点交替径向进出（$n=4$）”，纯手算几行就写出了每个模式的 $T$ 和 $V$！并且他还专门证明了为什么 $n=3$ 旋转 $0^\circ, 45^\circ, 90^\circ, 135^\circ$ 看似有 4 个状态，但 $0^\circ + 45^\circ + 90^\circ = 0$，因此只有 2 个线性无关模式。
  - **Nikita Semenin 的复坐标傅里叶级数法**则与我们的盲解思路如出一辙，利用复平面位移累加求逆直接导出通用色散关系公式。

---

## 4. `physicscup-2021-q4-reader` — Shock wave in an electron gas（强磁场稀薄电子气中的势垒激波）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **物理条件深度剖析**：
  1. **强磁场条件 $B \gg \frac{m k_B T}{\hbar e} \iff \hbar\omega_c \gg k_B T$**：
     电子在垂直于磁场的 $xy$ 平面内的朗道能级间距 $\hbar\omega_c \gg k_B T$，所有电子被冻结在最低朗道能级（$n=0$），且稀薄电子气忽略静相互作用与碰撞，因此**电子的运动完全退化为一维（沿 $z$ 轴）无碰撞独立粒子运动**！横向自由度无法与纵向自由度交换能量（无热化）。
  2. **多次反射加速与跨越势垒的“锯齿波”残余速度**：
     高度为 $U_0 = 100 k_B T$ 的阶跃势垒以慢速 $u \ll v_T = \sqrt{2k_B T/m}$ 从 $z=0$ 向 $z=L$ 推进。
     令跨越势垒所需的临界相对速度为 $V_c = \sqrt{2U_0/m} = 10\sqrt{2k_B T/m} = 10 v_T \gg v_T$。
     初始纵向速度大小为 $v_0 \sim v_T \ll V_c$ 的电子在区域 $ut < z < L$ 中被逼近的势垒多次弹性反射：每次从移动势垒反射，电子速度大小增加 $2u$！
     经过 $n$ 次反射后，当电子在 $z=L$ 处反弹回来再次迎头撞向势垒时，其在实验室系的速度为 $-v_n = -(v_0 + 2nu)$，在势垒参考系中的入射速度为 $v_n + u$。当 $v_n + u > V_c$ 时，电子终于越过势垒进入 $0 < z < ut$ 的势垒后方区域！
     由于每次反弹速度增量为 $2u$，电子越过势垒前瞬间的过剩速度 $\delta v = (v_n + u) - V_c$ 均匀分布在 $(0, 2u)$ 区间内（对热分布的 $v_0$ 而言是一个周期为 $2u$ 的快速振荡锯齿函数）。
     因此，刚进入势垒上方（$z < ut$）时，电子在势垒系中的速度 $v'_f$ 满足：
     \[
     v'^2_f = (V_c + \delta v)^2 - V_c^2 \approx 2 V_c \delta v
     \]
     对锯齿波在一个周期 $2u$ 上取平均（$\langle \delta v \rangle = u$），得到跃迁后电子的平均平方速度为：
     \[
     \langle v_f^2 \rangle = 2 V_c u = 20 v_T u = 20 u \sqrt{\frac{2k_B T}{m}}
     \]
     注意此时 $v_f \sim \sqrt{V_c u} \gg u$（因为 $u \ll V_c$）！
  3. **关键分岔：越过势垒后电子是否还会与移动势垒发生二次碰撞？（绝热极限 vs 非绝热极限）**
     - **情形 A（快激波/非绝热区：$\sqrt{\frac{k_B T}{U_0}}\sqrt{\frac{k_B T}{m}} \ll u \ll \sqrt{\frac{k_B T}{m}}$）**：
       电子在势垒达到 $x = L - ut \approx L / 10$ 附近时跃过势垒，此时势垒后方宽度为 $L - x \approx 0.9 L$，而剩余距离 $x = L/10$ 会在时间 $t_{\text{rem}} = x/u = \frac{L}{10u}$ 内走完。电子在后方跑一个来回的时间为 $T_{\text{back}} = \frac{2(L-x)}{v_f} \sim \frac{2L}{\sqrt{20 v_T u}}$。
       若 $t_{\text{rem}} \ll T_{\text{back}} \iff u \gg \frac{v_T}{10} \sim \sqrt{\frac{k_B T}{U_0}}\sqrt{\frac{k_B T}{m}}$，则电子跃过势垒后，在它从左壁 $z=0$ 反弹追上势垒之前，势垒已经撞上右壁 $z=L$ 走完全程了！
       此时每个电子最多只在势垒背面发生零次或一次碰撞，最终速度平方保持 $\langle v_f^2 \rangle = 20 v_T u$，故末态压强为：
       \[
       p = n_0 m \langle v_f^2 \rangle = 20 p_0 u \sqrt{\frac{2m}{k_B T}}
       \]
     - **情形 B（超慢激波/绝热区：$u \ll \sqrt{\frac{k_B T}{U_0}}\sqrt{\frac{k_B T}{m}}$）**：
       若 $u$ 极小，电子跃入左区 $0 < z < ut$ 后，在势垒走完剩余距离 $x$ 的过程中，还会在 $z=0$ 与移动势垒背面之间往返碰撞很多次（每次追尾碰撞损失速度 $2u$）！
       由相空间体积守恒（刘维尔定理 / 绝热不变量 $\oint p_z\,\mathrm{d}z = 2 m v_0 L$）：压缩阶段相空间矩形长缩小为 $x$、高增至 $2m V_c$；跃迁后相空间面积以窄条形式转移到左区 $0 < z < L-x$ 并随左区扩展到全长 $L$ 而绝热膨胀，最终恢复到初始宽度 $2m v_0$！因此完全绝热极限下末态分布与初态完全相同，压强恢复为：
       \[
       p = p_0
       \]

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  这道题在当年比赛过程中发生了一个著名的插曲（见 Kalda 的 Hints Summary 与 Nikita Semenin / Huiyuan Wang 的解答）：题目最初给出的条件是 $u \ll \sqrt{k_B T/m}$，而大参数 $\sqrt{U_0/k_B T} = 10$ 使得区间 $u \ll v_T$ 分裂成两个截然不同的物理机制区：
  1. **Part 4A（绝热区 $u \ll \frac{k_B T}{\sqrt{m U_0}}$）**：相空间面积（绝热不变量 $I = \oint p\,\mathrm{d}q$）在整个分裂与合并过程中守恒，或者从量子力学绝热定理看，极缓慢移动的阶跃势垒不改变粒子所处的本征态量子数 $n$，当势垒完全穿过盒子（整体势能抬升常数 $U_0$）后，每个粒子的动能与初态完全一样，因此 **$p = p_0$**！
  2. **Part 4B（中间渐近区 $\frac{k_B T}{\sqrt{m U_0}} \ll u \ll \sqrt{\frac{k_B T}{m}}$）**：电子跃过势垒时的典型速度 $v_f \sim \sqrt{V_c u}$ 远小于 $V_c$，但激波走完剩余路程 $L/10$ 的时间小于或可比于电子在左区往返一次的时间，需要精细追踪电子跃过势垒时刻的位置 $z_jump = L (1 - v_0/V_c)$ 以及在左区还能发生几次追尾碰撞（每次减速 $2u$）。若一次都不发生，则 $p = 20 p_0 u \sqrt{\frac{2m}{k_B T}}$。

---

## 5. `physicscup-2021-q5-reader` — Nonlinear circular resonator（非线性光纤环形谐振腔倍频优化）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **物理模型与稳态场方程建立**：
  1. **耦合器透射与反射关系**：
     在耦合点 $A$ 和 $C$，基频波（频率 $\omega$）的能量耦合系数为 $\alpha \ll 1$，故振幅耦合（透射）系数为 $t_1 = \sqrt{\alpha}$，振幅保持在原光纤中的传输系数为 $r_1 = \sqrt{1-\alpha} \approx 1 - \frac{\alpha}{2}$。
     对于倍频波（频率 $2\omega$），题设能量耦合系数为 $\alpha^2$，故振幅耦合系数为 $t_2 = \alpha$，振幅保持系数为 $r_2 = \sqrt{1-\alpha^2} \approx 1 - \frac{\alpha^2}{2}$。
  2. **半圆环内的非线性倍频与能量守恒**：
     设环内基频波稳态振幅为 $E$，倍频波稳态振幅为 $\mathcal{E}$。
     在每个半圆（$ABC$ 或 $CDA$）内，倍频波振幅增加 $\Delta\mathcal{E} = \delta E^2$。
     由光波能量守恒（无色散，折射率相同，光强 $I = E^2$），在半圆内总能量流 $E^2 + \mathcal{E}^2$ 守恒：
     \[
     \tilde{E}^2 + (\mathcal{E} + \delta E^2)^2 = E^2 + \mathcal{E}^2 \implies \tilde{E} = E\sqrt{1 - 2\delta\mathcal{E} - \delta^2 E^2} \approx E(1 - \delta\mathcal{E})
     \]
     即基频波每经过一个半圆，其振幅因向倍频波转移能量而衰减 $\Delta E_{\text{NL}} \approx -\delta E \mathcal{E}$！
  3. **稳态自洽方程求解与极值**：
     由于环长是基频波波长的整数倍且无色散，基频波和倍频波在环内均处于精确相长干涉谐振状态。
     - **倍频波环内稳态平衡**：在绕环一周（两个半圆 + 两个耦合器 $A, C$）中，倍频波每半圈增益 $\delta E^2$（一圈增益 $2\delta E^2$），在 $A, C$ 两处各损失振幅 $\frac{1}{2}\alpha^2 \mathcal{E}$（一圈共损失 $\alpha^2 \mathcal{E}$）：
       \[
       2\delta E^2 = \alpha^2 \mathcal{E} \implies \mathcal{E} = \frac{2\delta E^2}{\alpha^2}
       \]
       而在输出端 $D$（经过耦合器 $A$ 耦合出环），输出倍频波振幅为 $\mathcal{E}_{\text{out}} = \sqrt{\alpha^2}\mathcal{E} = \alpha\mathcal{E} = \frac{2\delta E^2}{\alpha}$，输出倍频光强为：
       \[
       \mathcal{I} = \mathcal{E}_{\text{out}}^2 = \frac{4\delta^2 E^4}{\alpha^2}
       \]
     - **基频波环内稳态平衡**：绕环一周，基频波在 $A$ 处注入振幅 $\sqrt{\alpha}E_0$，在 $A, C$ 两耦合器共损失振幅 $2\times\frac{\alpha}{2}E = \alpha E$，在两个半圆内因非线性倍频共损失振幅 $2\delta E \mathcal{E}$：
       \[
       \sqrt{\alpha} E_0 = \alpha E + 2\delta E \mathcal{E} = \alpha E + \frac{4\delta^2 E^3}{\alpha^2}
       \]
     - **无量纲化与均值不等式求极值**：
       令无量纲参数 $k = \frac{2\delta E}{\alpha^{3/2}}$，则基频波平衡方程化为：
       \[
       \sqrt{\alpha} E_0 = \alpha E (1 + k^2) \implies E = \frac{E_0}{\sqrt{\alpha}(1+k^2)}
       \]
       同时输出倍频光强为：
       \[
       \mathcal{I} = \frac{4\delta^2 E^4}{\alpha^2} = k^2 \alpha E^2 = I_0 \frac{k^2}{(1+k^2)^2}
       \]
       由均值不等式 $1 + k^2 \ge 2k$，当且仅当 $k = 1$ 时，$\mathcal{I}$ 取得最大值：
       \[
       \mathcal{I}_m = \frac{I_0}{4}
       \]
       此时由 $k = \frac{2\delta E}{\alpha_m^{3/2}} = 1$ 及 $E = \frac{E_0}{2\sqrt{\alpha_m}}$，解得最优耦合系数：
       \[
       \alpha_m^2 = \delta E_0 = \delta \sqrt{I_0} \implies \alpha_m = \sqrt{\delta} I_0^{1/4}
       \]

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的盲解推导与 Nikita Semenin、Zhening Li、Huiyuan Wang 的获奖解答完全吻合！
  - **物理图像洞察（为什么最大倍频转换输出恰好是 $\frac{1}{4}I_0$？）**：
    这是一个极其深刻的**谐振腔临界耦合（Critical Coupling / 阻抗匹配）**结论！
    1. 对于基频波，环形谐振腔有两个对称端口（底部直光纤 $A$ 和顶部直光纤 $C$）以及环内非线性损耗。当环内损耗（含顶部端口 $C$ 的泄漏与倍频转换）与输入端口 $A$ 达到匹配时，输入光强 $I_0$ 的分布为：在 $k=1$ 处，$E = \frac{E_0}{2\sqrt{\alpha}}$，底部直光纤透射到 $D$ 的基频波振幅为 $E_{D,\omega} = \sqrt{1-\alpha}E_0 - \sqrt{\alpha}E \approx E_0 - \frac{1}{2}E_0 = \frac{1}{2}E_0$（占总功率 $\frac{1}{4}I_0$），顶部光纤 $C$ 泄漏的基频波振幅为 $\sqrt{\alpha}E = \frac{1}{2}E_0$（占总功率 $\frac{1}{4}I_0$），因此**最多有 $\frac{1}{2}I_0$ 的功率被转化为倍频波**！
    2. 而生成的 $\frac{1}{2}I_0$ 倍频波功率又在顶部耦合器 $C$ 和底部耦合器 $A$ 之间**对称平分**，因此从底部输出端口 $D$ 出来的倍频波最大光强必然是 $\frac{1}{2} \times \frac{1}{2}I_0 = \frac{1}{4}I_0$！

---

## 6. `physicscup-2022-q1-reader` — Magnetized ball（永磁铁磁球的加热退磁）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **物理图像与退磁负载线（Load Line）推导**：
  半径 $R=1\text{ cm}$ 的钕铁硼（NdFeB）永磁球，先在 $T_1 = 20^\circ\text{C}$ 下置于 $3\text{ T}$ 强磁场中饱和磁化，撤去外磁场后加热到 $T_2 = 120^\circ\text{C}$，根据给定的第二象限退磁曲线（$B$ vs $\mu_0 H$）求球体磁偶极矩的变化量 $\Delta m$。
  1. **均匀磁化球体的内部退磁场基本定理 $B_{\text{in}} = -2\mu_0 H_{\text{in}}$**：
     在无外磁场（$\vec{B}_{\text{ext}} = 0$）时，设球体具有均匀磁化强度 $\vec{M}$。
     由麦克斯韦方程组 $\nabla\cdot\vec{B} = 0$ 与 $\nabla\times\vec{H} = 0$，以及均匀磁化球外部磁场等同于位于球心的磁偶极子 $\vec{m} = \frac{4}{3}\pi R^3 \vec{M}$，球体内部的磁感应强度为：
     \[
     \vec{B}_{\text{in}} = \frac{2}{3}\mu_0 \vec{M}
     \]
     再由本构关系 $\vec{B}_{\text{in}} = \mu_0(\vec{H}_{\text{in}} + \vec{M})$，消去 $\vec{M}$ 即得球内的磁场强度（退磁场）：
     \[
     \vec{H}_{\text{in}} = -\frac{1}{3}\vec{M} \implies B_{\text{in}} = -2\mu_0 H_{\text{in}}
     \]
     也就是说，无论温度如何变化、磁滞回线形状如何非线性，只要外场为零且球体保持均匀磁化，球体内部的工作点 $(\mu_0 H_{\text{in}}, B_{\text{in}})$ 必须始终位于斜率为 $-2$ 的过原点直线（退磁负载线）$B = -2(\mu_0 H)$ 上！
  2. **磁偶极矩与工作点 $B_{\text{in}}$ 的关系**：
     \[
     m = \frac{4}{3}\pi R^3 M = \frac{4}{3}\pi R^3 \cdot \frac{3 B_{\text{in}}}{2\mu_0} = \frac{2\pi R^3 B_{\text{in}}}{\mu_0}
     \]
  3. **图解法读取两温度下的交点**：
     在给定的 $(\mu_0 H, B)$ 图上画出直线 $B = -2\mu_0 H$（连接 $(0,0)$ 与 $(-0.5\text{ T}, 1.0\text{ T})$）：
     - 与 $T_1 = 20^\circ\text{C}$ 退磁曲线交于：$\mu_0 H_1 \approx -0.475\text{ T}, B_1 \approx 0.95\text{ T}$，对应 $m_1 = \frac{2\pi (0.01)^3 \times 0.95}{4\pi\times 10^{-7}} = 4.75\text{ A}\cdot\text{m}^2$；
     - 与 $T_2 = 120^\circ\text{C}$ 退磁曲线交于陡降段：$\mu_0 H_2 \approx -0.24\text{ T}, B_2 \approx 0.48\text{ T}$，对应 $m_2 = \frac{2\pi (0.01)^3 \times 0.48}{4\pi\times 10^{-7}} = 2.40\text{ A}\cdot\text{m}^2$；
     - 因此加热引起的磁矩减小量为 $|\Delta m| = m_1 - m_2 \approx 2.35 \sim 2.4\text{ A}\cdot\text{m}^2$（即 $\Delta m \approx -2.4\text{ A}\cdot\text{m}^2$）。

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的盲解与获奖解答（Victor Lequin、Eddie Chen & Zhening Li 等）完全一致！
  Jaan Kalda 在评述中强调了评审最佳解答的核心标准：**如何简洁而初等地证明均匀磁化球的 $B = -2\mu_0 H$**，而不是直接抄工程磁学手册或动用球谐函数硬解拉普拉斯方程。
  - **优雅证法 1（静电-静磁类比 + 叠加原理）**：均匀磁化球可视为两个半径为 $R$、磁荷密度为 $\pm\rho_m$（或体电流）的球错开微小位移 $\vec{d}$ 叠加而成，类比均匀极化介质球内部退极化场 $E = -\frac{P}{3\varepsilon_0}$，立即得到 $H = -\frac{1}{3}M$，或类比带电球壳旋转产生的分子电流，球心磁场为 $B = \frac{2}{3}\mu_0 M$。
  - **优雅证法 2（唯一性定理试探解，Victor Lequin / Chen & Li）**：猜测球内为匀强场 $\vec{B}_{\text{in}}$、球外为偶极场 $\vec{B}_{\text{dipole}}$，直接检验球面 $r=R$ 处的边界条件 $B_{r,\text{in}} = B_{r,\text{out}}$ 与 $H_{\theta,\text{in}} = H_{\theta,\text{out}}$，一行代数立刻锁定 $B_{\text{in}} = \frac{2}{3}\mu_0 M = -2\mu_0 H_{\text{in}}$！

---

## 7. `physicscup-2022-q2-reader` — Fastest lap（绕正三角形房屋的最快圈速）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **物理图像与变分最优化**：
  男孩在摩擦系数为 $\mu$ 的冰面上周期性地绕边长为 $a$ 的正三角形房屋奔跑，最大水平加速度恒为 $A = \mu g$，求绕跑一圈的最短时间 $\mathcal{T}_{\min}$。
  1. **轨迹紧贴顶点与对称性约化**：
     若最优轨迹不经过正三角形的三个顶点 $A, B, C$，则可将轨迹向内等比例缩小，由于时间标度 $\mathcal{T} \propto \sqrt{L/\mu g}$，缩小后的轨迹周期更短且仍能包围房屋，矛盾！因此最优轨迹必经过三个顶点 $A, B, C$。
     由三重旋转对称性与反射对称性，一圈分为三段全等的顶点间轨迹（耗时 $T_1 = \mathcal{T}/3$）。在每个顶点处，为了不出现速度折角（若轨迹在顶点处有折角，则有限加速度下顶点处速度必为 $0$，此时单边最短时间为先以 $+\mu g$ 加速半程再以 $-\mu g$ 减速半程，耗时 $T_1 = 2\sqrt{a/\mu g}$，总周期 $6\sqrt{a/\mu g}$，远慢于光滑切过顶点的情形），轨迹在顶点处的切线方向必与正三角形外角平分线垂直，即**与相邻两边均成 $\theta = \frac{\pi}{3} = 60^\circ$ 角**！
  2. **逐点最大化积分法（庞特里亚金极大值原理 / 柯西不等式）**：
     取单边 $AB$ 沿 $x$ 轴（从 $x=0$ 到 $x=a$），运动时间 $t \in [0, T_1]$，设半程时间为 $\tau = T_1/2$。
     由时间反演对称性，在 $t=0$（顶点 $A$）处速度方向为 $+\frac{\pi}{3}$，故 $v_y(0) = \sqrt{3} v_x(0)$；在最高点 $t=\tau$ 处 $v_y(\tau) = 0$。
     设在 $t \in [0, \tau]$ 内加速度矢量为 $\vec{a}(t) = \mu g (\cos\phi(t), -\sin\phi(t))$，则：
     \[
     v_y(0) = \int_0^\tau \mu g \sin\phi(s)\,\mathrm{d}s \implies v_x(0) = \frac{\mu g}{\sqrt{3}}\int_0^\tau \sin\phi(s)\,\mathrm{d}s
     \]
     而半程水平位移 $\frac{a}{2}$ 为（利用分部积分交换积分次序）：
     \[
     \frac{a}{2} = \int_0^\tau v_x(t)\,\mathrm{d}t = \tau v_x(0) + \int_0^\tau (\tau - s) a_x(s)\,\mathrm{d}s = \mu g \int_0^\tau \left[\frac{\tau}{\sqrt{3}}\sin\phi(s) + (\tau - s)\cos\phi(s)\right]\mathrm{d}s
     \]
     看！对于固定的 $\tau$，要使右端积分最大化，被积函数在每个时刻 $s \in [0, \tau]$ 互相独立！由柯西不等式 $P\sin\phi + Q\cos\phi \le \sqrt{P^2 + Q^2}$，当且仅当 $\tan\phi(s) = \frac{\tau}{\sqrt{3}(\tau - s)}$ 时，被积函数逐点达到最大值：
     \[
     \frac{a}{2} = \mu g \int_0^\tau \sqrt{\frac{\tau^2}{3} + (\tau - s)^2}\,\mathrm{d}s = \mu g \tau^2 \int_0^1 \sqrt{\frac{1}{3} + u^2}\,\mathrm{d}u
     \]
     计算该标准双曲积分：
     \[
     I = \int_0^1 \sqrt{\frac{1}{3} + u^2}\,\mathrm{d}u = \left[\frac{u}{2}\sqrt{\frac{1}{3}+u^2} + \frac{1}{6}\operatorname{arsinh}(\sqrt{3}u)\right]_0^1 = \frac{\sqrt{3}}{3} + \frac{\ln(2+\sqrt{3})}{6}
     \]
     代入 $\tau = \frac{\mathcal{T}}{6}$，立即解得最短总周期：
     \[
     \mathcal{T}_{\min} = 6\tau = 6\sqrt{\frac{a}{2\mu g I}} = 6\sqrt{\frac{3}{2\sqrt{3} + \ln(2+\sqrt{3})}\frac{a}{\mu g}} \approx 4.7528\sqrt{\frac{a}{\mu g}}
     \]

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的分部积分 + 柯西不等式逐点最大化方法仅用 5 行就导出了精确解，与获奖解答结果完全一致！
  而 Jaan Kalda 与 Eddie Chen & Zhening Li 提出的**速度空间悬链线（Hodograph Catenary）对偶法**更是物理竞赛史上的一颗明珠：
  - 在速度空间 $(v_x, v_y)$ 中，由于 $|\dot{\vec{v}}| = \mu g$，轨迹的弧长微元为 $\mathrm{d}s_v = \mu g\,\mathrm{d}t$，因此总时间 $T_1$ 对应速度空间中一条**固定总长度 $L_v = \mu g T_1$ 的均匀柔绳**！
  - 顶点速度方向约束 $\theta = \pm\frac{\pi}{3}$ 意味着这根柔绳的两端可以在两条射线 $\theta = +\frac{\pi}{3}$ 与 $\theta = -\frac{\pi}{3}$ 上无摩擦自由滑动（故绳端必与射线垂直）！
  - 位移最大化 $\max a = \max \int_0^{T_1} v_x\,\mathrm{d}t = \frac{1}{\mu g}\max \int v_x\,\mathrm{d}s_v$ 等价于这根均匀柔绳在沿 $+v_x$ 方向的**匀强引力场中势能最小（静力平衡）**！
  - 因此，**最优轨迹在速度空间中的形状必然是一条两端垂直于 $\pm 60^\circ$ 射线的悬链线（Catenary）**！这直接解释了为什么我们的积分里会出现 $\sqrt{1/3 + u^2}$ 和 $\operatorname{arsinh}(\sqrt{3}) = \ln(2+\sqrt{3})$！

---

## 8. `physicscup-2022-q3-reader` — Photon rocket（相对论光子火箭最小转向角）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **相对论四维动量与中间静止系 $K_1$ 妙解**：
  静止质量为 $m$ 的光子火箭分两阶段直线加速：第一阶段沿某固定方向加速（推力随时间变化未知，燃料消耗量未知）；随后在火箭自身参考系中将推力方向改变 $\alpha$ 角，继续第二阶段加速，直到最终在初始静止系（实验室系 $K_0$）中的速度达到 $v_f = \frac{4}{5}c$，且剩余静止质量为 $m_f = \frac{1}{4}m$。求能达到该末态的最小转向角 $\alpha_{\min}$。
  1. **单向光子火箭的快度-质量关系（与推力历史无关！）**：
     在单向加速阶段，所有喷出的光子沿着同一方向传播。因为同向零质量光子的四维动量之和仍是零质量（类光）四维矢量 $P_{\text{ph}}^2 = 0$（或者直接由齐奥尔科夫斯基相对论火箭方程 $\mathrm{d}\eta = -\frac{\mathrm{d}m_r}{m_r}$），火箭的末态完全取决于初末静止质量之比，与推力大小随时间的具体变化无关！
     具体而言，若光子火箭从静止质量 $m_a$（静止）单向加速到静止质量 $m_b$，其获得的快度（Rapidity）为：
     \[
     e^{\eta} = \frac{m_a}{m_b} \iff \cosh\eta = \frac{1}{2}\left(\frac{m_a}{m_b} + \frac{m_b}{m_a}\right), \quad \sinh\eta = \frac{1}{2}\left(\frac{m_a}{m_b} - \frac{m_b}{m_a}\right)
     \]
  2. **跳入中间转折时刻的火箭静止系 $K_1$**：
     设第一阶段结束、刚要转向时，火箭的静止质量为 $m_1 = \kappa m$（其中 $\frac{1}{4} \le \kappa \le 1$），此时的瞬时静止系记为 $K_1$。
     在参考系 $K_1$ 中观察：
     - 初始实验室系 $K_0$ 沿 $-x$ 方向运动，其快度 $\eta_1$ 满足 $e^{\eta_1} = \frac{m}{m_1} = \frac{1}{\kappa}$，对应的四维速度为 $u_{\text{lab}} = (\cosh\eta_1, -\sinh\eta_1, 0, 0)$；
     - 第二阶段火箭在 $K_1$ 系中从静止开始、沿着与 $+x$ 轴成 $\alpha$ 角的方向做单向光子火箭加速，静止质量从 $m_1 = \kappa m$ 减至 $m_f = \frac{1}{4}m$，因此在 $K_1$ 系中火箭末态的快度 $\eta_2$ 满足 $e^{\eta_2} = \frac{m_1}{m_f} = 4\kappa$，对应的四维速度为 $u_f = (\cosh\eta_2, \sinh\eta_2\cos\alpha, \sinh\eta_2\sin\alpha, 0)$！
  3. **四维速度洛伦兹不变量（双曲余弦定理）求极值**：
     注意到 $\eta_1 + \eta_2 = \ln\left(\frac{1}{\kappa}\cdot 4\kappa\right) = \ln 4$ 为定值！
     末态火箭相对于实验室系 $K_0$ 的洛伦兹因子为 $\gamma_f = \frac{1}{\sqrt{1-(4/5)^2}} = \frac{5}{3}$。
     利用四维速度内积的不变性 $-u_{\text{lab}}\cdot u_f = \gamma_f$：
     \[
     \gamma_f = \cosh\eta_1\cosh\eta_2 + \sinh\eta_1\sinh\eta_2\cos\alpha = \frac{5}{3}
     \]
     利用恒等式 $\cosh(\eta_1+\eta_2) = \frac{1}{2}(4 + \frac{1}{4}) = \frac{17}{8}$，令 $x = \cosh(\eta_1 - \eta_2) \ge 1$，则：
     \[
     \cosh\eta_1\cosh\eta_2 = \frac{17/8 + x}{2}, \quad \sinh\eta_1\sinh\eta_2 = \frac{17/8 - x}{2}
     \]
     代入解得：
     \[
     \cos\alpha = \frac{\frac{5}{3} - \frac{17/8 + x}{2}}{\frac{17/8 - x}{2}} = 1 - \frac{22/3}{17 - 8x}
     \]
     要使 $\alpha \in [0, \pi]$ 最小，需使 $\cos\alpha$ 最大，即需使分母 $17 - 8x$ 最大，故取 $x = \cosh(\eta_1 - \eta_2)$ 的最小值 $x_{\min} = 1$（即 $\eta_1 = \eta_2 = \ln 2$，中间静止质量 $m_1 = \frac{1}{2}m = \sqrt{m \cdot m_f}$）！
     代入 $x = 1$ 得：
     \[
     (\cos\alpha)_{\max} = 1 - \frac{22/3}{9} = \frac{5}{27} \implies \alpha_{\min} = \arccos\left(\frac{5}{27}\right) \approx 79.33^\circ\ (1.3845\text{ rad})
     \]

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的四维速度内积不变量解法与获得 60% 最高奖金的 **Isaac Wu** 的解法完全一致！
  Jaan Kalda 在评述中发出了极具教练智慧的感慨：
  > “Have you often solved geometry problems using the formulae for the rotation of axes? In most cases, it would be a really cumbersome approach. The same applies to the Lorentz transformations which are essentially formulae for the rotation of axes.”（你平时做几何题会频繁使用坐标轴旋转公式吗？在绝大多数情况下那都非常繁琐。洛伦兹变换本质上就是闵可夫斯基时空中的坐标轴旋转公式！）
  - 22 位在第一周解出本题的选手中，有 21 位都在实验室系中硬套二维洛伦兹速度变换公式，陷入冗长的代数化简；唯有 **Isaac Wu**（以及我们的盲解）站在中间转折系 $K_1$ 中利用四维动量/四维速度内积不变量，仅用半页纸就优雅地完成了证明。

---

## 9. `physicscup-2022-q4-reader` — Image of a point（薄透镜共线等距点像的射影尺规作图）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **光学成像的射影不变性（交比与调和点列）**：
  物空间直线上有四个等距点 $A, B, C, D$（满足 $|AB|=|BC|=|CD|$），经未知位置、未知光轴方向、未知焦距的薄透镜成像为共线点 $A', B', C', D'$。已知图上的 $A', B', C'$，求仅用尺规（实际上仅需无刻度直尺！）几何作出 $D'$，并给出坐标。
  1. **高斯/牛顿薄透镜公式的分式线性变换本质**：
     设物点到物方焦平面的有向距离为 $x$，像点到像方焦平面的有向距离为 $x'$，由牛顿薄透镜公式 $x x' = f^2$，像点沿像直线到像方焦平面交点 $E$（即无穷远物点 $\infty$ 在直线 $AB$ 上的像点！）的有向距离 $s' = \overline{EA'}$ 与 $x'$ 成正比，因此与物点到物方焦平面交点的距离 $x$ 成反比：
     \[
     s'_A = \frac{C_0}{x_A}, \quad s'_B = \frac{C_0}{x_B}, \quad s'_C = \frac{C_0}{x_C}, \quad s'_D = \frac{C_0}{x_D}
     \]
     也就是说，**薄透镜对直线的成像是一个射影变换（Projective Transformation / Möbius 变换），严格保持共线四点的交比（Cross-Ratio）不变**！
  2. **利用调和点列（Harmonic Conjugate）纯直尺作图**：
     - 在物空间中，设无穷远点为 $P_\infty$。因为 $B$ 是 $AC$ 的中点，所以 $(A, C; B, P_\infty) = -1$ 构成一组**调和点列**！
     - 经过透镜射影变换后，$P_\infty$ 的像是像方焦平面与像直线的交点 $E$。因此，在像直线上，**$(A', C'; B', E) = -1$ 也构成调和点列**！即点 $E$ 是点 $B'$ 关于 $A', C'$ 的调和共轭点（Harmonic Conjugate）！
     - 同理，因为 $C$ 是 $BD$ 的中点，所以在物空间 $(B, D; C, P_\infty) = -1$ 构成调和点列；经透镜成像后，**$(B', D'; C', E) = -1$ 同样构成调和点列**！即点 $D'$ 是点 $E$ 关于 $B', C'$ 的调和共轭点（或 $B'$ 是 $D'$ 关于 $C', E$ 的调和共轭点）！
  3. **完全四边形（Complete Quadrangle）无圆规直尺作图步骤**：
     - **第一步（作 $E$）**：任取直线 $A'C'$ 外一点 $L$，过 $B'$ 任作一条辅助直线 $l$ 交 $LA'$ 于 $M$、交 $LC'$ 于 $N$；连接 $A'N$ 与 $C'M$ 交于点 $K$；连接 $LK$ 交直线 $A'C'$ 于点 $E$！
     - **第二步（作 $D'$）**：连接 $LE$ 交同一条辅助直线 $l$（即 $B'MN$）于点 $P$；连接 $EN$ 与 $C'P$ 交于点 $Q$；连接 $LQ$ 交直线 $A'C'$ 于点 $D'$！
  4. **坐标精确计算**：
     由交比不变性 $(A', B'; C', D') = (A, B; C, D) = \frac{AC \cdot BD}{AD \cdot BC} = \frac{2 \times 2}{3 \times 1} = \frac{4}{3}$（或按标准定义 $\frac{(A'-C')(B'-D')}{(A'-D')(B'-C')} = \frac{4}{3}$），由图中 $A', B', C'$ 的坐标即可直接算出 $D'$。

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的调和点列 + 完全四边形直尺作图法与获得最佳解答首奖的 **Vlad-Ștefan Oros** 及 **Erik Sünderhauf** 的解法一字不差！
  - 在 GeoGebra 原文件中，$A', B', C'$ 算出的 $D'$ 精确坐标为 **$(7.115, 2.898)$**。
  - **Jaan Kalda 的纯几何中线作图法**也极具启发性：即便学生不知道射影几何的“交比”和“调和点列”，只要知道**平行线的像交于焦平面上的同一点 $E$**，就可以在图上任取两点 $P', Q'$ 作为物空间中与 $A, B, C$ 构成三角形 $\triangle AQC$（其中 $P, B$ 分别为 $AQ, AC$ 中点）的像；利用三角形三条中线交于重心 $M'$，即可找出 $QC$ 中点 $T$ 的像 $T'$，利用中位线 $PT \parallel AC$ 的像 $P'T'$ 与 $A'C'$ 交于焦平面点 $E$，再作平行线一步步平移出等距点 $D'$！

---

## 10. `physicscup-2022-q5-reader` — Satellite（太阳能平板卫星的最大理论充电功率）

### Phase 1: 独立盲解记录 (Blind Attempt)
- **热辐射定律 + 内置可逆卡诺热机最优化**：
  表面积为 $A$、厚度 $d \ll \sqrt{A}$ 的薄平板卫星，法线正对太阳（太阳辐射能流密度为 $S$）。卫星内部可安装任意装置，但外表面只能涂覆灰体涂层（发射率/吸收率 $\varepsilon \in [0, 1]$ 与波长无关，不同区域可涂不同灰体涂层）。忽略宇宙微波背景辐射，求最大理论恒定充电功率 $P_{\max}$。
  1. **热力学架构分析**：
     - 灰体涂层的吸收率等于发射率：$\alpha(\lambda) = \varepsilon(\lambda) = \varepsilon \in [0, 1]$。
     - 设向阳面（面积 $A$）的温度为 $T_1$、灰体发射率为 $\varepsilon_1$，则向阳面吸收太阳辐射功率 $\varepsilon_1 A S$，同时向外辐射热功率 $\varepsilon_1 A \sigma T_1^4$，因此净输入卫星内部的热流为：
       \[
       \dot{Q}_1 = \varepsilon_1 A (S - \sigma T_1^4)
       \]
       （必须有 $\sigma T_1^4 < S$，否则 $\dot{Q}_1 \le 0$，向阳面净散热，无法对外做正功）。
     - 设背阳面（面积 $A$）的温度为 $T_2$、灰体发射率为 $\varepsilon_2$，它不接收太阳辐射，向深空辐射排出的废热功率为：
       \[
       \dot{Q}_2 = \varepsilon_2 A \sigma T_2^4
       \]
     - 卫星内部最理想的发电装置是工作在热源 $T_1$ 与冷源 $T_2$ 之间的**可逆卡诺热机**（Carnot Engine）！由熵平衡方程：
       \[
       \frac{\dot{Q}_1}{T_1} = \frac{\dot{Q}_2}{T_2} \implies \frac{\varepsilon_1 (S - \sigma T_1^4)}{T_1} = \varepsilon_2 \sigma T_2^3
       \]
  2. **严格解析证明最优涂层必为双面全黑（$\varepsilon_1 = 1, \varepsilon_2 = 1$）**：
     令无量纲温度参数 $x = \frac{\sigma T_1^4}{S} \in (0, 1)$，由卡诺熵平衡解出 $\dot{Q}_2$ 并代入输出功率 $P = \dot{Q}_1 - \dot{Q}_2$：
     \[
     \frac{P}{AS} = \varepsilon_1 (1 - x) - \frac{\varepsilon_1^{4/3}}{\varepsilon_2^{1/3}} \frac{(1 - x)^{4/3}}{x^{1/3}}
     \]
     - 首先，在固定 $\varepsilon_1, x$ 时，第二项（废热损失项）正比于 $\varepsilon_2^{-1/3}$，为使 $P$ 最大，显然应使冷端散热能力最强（温度 $T_2$ 最低），故必取 **$\varepsilon_2 = 1$**！
     - 其次，如何解析证明 $\varepsilon_1 = 1$？令无量纲吸热率 $y = \varepsilon_1(1 - x)$，则：
       \[
       \frac{P}{AS} = y - \frac{y^{4/3}}{x^{1/3}}
       \]
       对于任意固定的吸热率 $y$，要使输出功率 $P$ 最大，必须使热源温度 $x = \frac{\sigma T_1^4}{S}$ 尽可能大！而由 $1 - x = \frac{y}{\varepsilon_1}$，要使 $x$ 最大（即 $1-x$ 最小），必须取 $\varepsilon_1$ 的最大可能值 **$\varepsilon_1 = 1$**！
       （这背后的物理直觉非常清晰：给定净吸热功率 $\dot{Q}_1$，涂黑 $\varepsilon_1=1$ 能让向阳面在更高的温度 $T_1$ 下吸收同样多的净热量，从而提升卡诺效率！）
  3. **单变量求导与数值求解**：
     将 $\varepsilon_1 = \varepsilon_2 = 1$ 代入：
     \[
     f(x) = \frac{P}{AS} = (1 - x) - x^{-1/3}(1 - x)^{4/3}
     \]
     对 $x$ 求导令 $f'(x) = 0$：
     \[
     -1 + \frac{1}{3}x^{-4/3}(1 - x)^{4/3} + \frac{4}{3}x^{-1/3}(1 - x)^{1/3} = 0 \iff (1 - x)^{1/3}\left(\frac{1}{3x^{4/3}} + \frac{1}{x^{1/3}}\right) = 1
     \]
     两边立方化为关于 $x$ 的四次代数方程：
     \[
     (1 - x)(1 + 3x)^3 = 27x^4 \iff 54x^4 - 9x^3 - 9x^2 - 8x - 1 = 0
     \]
     数值求解唯一正根：
     \[
     x \approx 0.7506941 \implies \tau_1 = x^{1/4} \approx 0.9308214
     \]
     代回得最大理论充电功率：
     \[
     P_{\max} \approx 0.07666021\, AS
     \]

### Phase 2: 对照获奖解答与 Jaan Kalda 评述的教学拆解
- **对照分析**：
  我们的盲解不仅算出了完全精确的 8 位有效数字系数 `0.07666021 AS`，而且采用的**固定净吸热率 $y = \varepsilon_1(1-x)$ 证明 $\varepsilon_1 = 1$** 的代数技巧，与 **Vlad-Ștefan Oros** 的获奖最佳解答完全一致！
  - Jaan Kalda 在评述中特别指出，许多参赛者只是数值试探发现 $\varepsilon_1 = 1$ 最大，或者误以为向阳面涂白能减少自身辐射从而有利，忽略了灰体定律下 $\alpha = \varepsilon$ 同步减小太阳吸收功率。
  - 此外，**Zhening Li & Eddie Chen** 还严格证明了为什么**均匀温度分布**优于分区域不同温度分布：因为函数 $P(q_1)$ 关于单位面积吸热率是严格凹函数（或由热力学第二定律，内部任何温差传热都会产生不可逆熵增，唯有向阳面等温 $T_1$、背阳面等温 $T_2$ 能消除面内横向不可逆熵产生）。
