# Batch 12: 泛珠三角物理奥林匹克综合试二 (PanPhO Paper 2, 2019–2020) 盲解与教学拆解全记录

本报告严格遵循两阶段协议（**Phase 1: 独立盲解** $\to$ **Phase 2: 对照官方参考解答与教学深度拆解**），涵盖 2019–2020 年泛珠三角物理奥林匹克竞赛（PanPhO）综合试二全部 4 道长题：
- `panpho-2019-paper-2-problem-slice-q1`（引力波 Gravitational Waves）
- `panpho-2019-paper-2-problem-slice-q2`（同步现象 Synchronization）
- `panpho-2020-paper-2-problem-slice-q1`（引力常数的精密测量 Precision Measurement of $G$）
- `panpho-2020-paper-2-problem-slice-q2`（不同维度的物理 Physics in Various Dimensions）

---

## 1. `panpho-2019-paper-2-problem-slice-q1` — 引力波 (Gravitational Waves)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：双脉冲星圆轨道牛顿引力动力学与四极引力辐射功率量纲分析、绝热轨道衰减并合时间积分、双探测器（LIGO L1/H1）平面波到达时间差（ToA）圆锥定位、引力波能流平方反比衰减，以及局域洛伦兹系（牛顿潮汐力等效模型）下弹簧连接双质点的受迫振动与共振响应。
- **分步独立推导**：
  - **A1 (双脉冲星轨道周期 $T_B$)**：两颗质量均为 $M$、半径均为 $r$ 的脉冲星绕质心在半径为 $R$ 的圆轨道上运动（注意题图虚线标注 $R$ 为每个星体到质心的轨道半径，故两星间距为 $2R$）。由牛顿第二定律：
    \[
    \frac{G_N M^2}{(2R)^2} = M \omega^2 R = M \left(\frac{2\pi}{T_B}\right)^2 R \implies v = \sqrt{\frac{G_N M}{4R}}, \quad T_B = \frac{2\pi R}{v} = 4\pi \sqrt{\frac{R^3}{G_N M}}.
    \]
  - **A2 (引力波辐射频率 $f_{GW}$)**：引力波由质量分布的四极矩变化激发。由于两颗脉冲星质量相等，每经过半个轨道周期 $T_B/2$，两星互换位置，空间质量分布完全恢复初态，故引力波周期为 $T_{GW} = T_B / 2$，频率为：
    \[
    f_{GW} = \frac{2}{T_B} = \frac{1}{2\pi}\sqrt{\frac{G_N M}{R^3}}.
    \]
  - **A3 (引力辐射功率量纲指数 $\alpha, \beta, \gamma$)**：已知 $P = \frac{2}{5c^5} G_N^\alpha M^\beta R^\gamma$。各物理量量纲为 $[P] = \mathrm{M L^2 T^{-3}}$，$[c^{-5}] = \mathrm{L^{-5} T^5}$，$[G_N] = \mathrm{M^{-1} L^3 T^{-2}}$，$[M] = \mathrm{M}$，$[R] = \mathrm{L}$。对比量纲指数：
    \[
    \begin{cases}
    \mathrm{M}: & 1 = -\alpha + \beta, \\
    \mathrm{L}: & 2 = -5 + 3\alpha + \gamma, \\
    \mathrm{T}: & -3 = 5 - 2\alpha,
    \end{cases}
    \implies \alpha = 4, \quad \beta = 5, \quad \gamma = -5.
    \]
  - **A4 (脉冲星碰撞时间 $T_C$)**：双星系统总动能 $E_k = 2 \times \frac{1}{2} M v^2 = \frac{G_N M^2}{4R}$，引力势能 $E_p = -\frac{G_N M^2}{2R}$，总机械能为：
    \[
    E = E_k + E_p = -\frac{G_N M^2}{4R}.
    \]
    由能量守恒 $\frac{dE}{dt} = -P$：
    \[
    \frac{G_N M^2}{4R^2}\frac{dR}{dt} = -\frac{2}{5c^5}\frac{G_N^4 M^5}{R^5} \implies R^3 \frac{dR}{dt} = -\frac{8 G_N^3 M^3}{5 c^5}.
    \]
    两星表面接触发生碰撞时，星体中心距为 $2r$，即末态轨道半径为 $R_{\text{min}} = r$。从初态 $R$ 积分至末态 $r$ 得：
    \[
    T_C = \frac{5 c^5}{32 G_N^3 M^3}\left(R^4 - r^4\right) = \frac{5 c^5}{8(-\gamma - 1)} G_N^{1-\alpha} M^{2-\beta} \left(R^{-\gamma-1} - r^{-\gamma-1}\right).
    \]
  - **A5 (广义相对论势能修正对周期的影响)**：附加势能修正 $\Delta V_{GR} = -\frac{C}{R^2}$（$C > 0$）提供额外的径向吸引力 $-\frac{\partial \Delta V_{GR}}{\partial R} = -\frac{2C}{R^3} < 0$。在相同的 $M, R$ 下，向心引力增强要求更大的轨道线速度 $v$，因此双星系统的周期 $T_B$ **减小（Decrease）**。
  - **B1 (自由检验粒子最大响应方向)**：引力波源位于 $-y$ 方向，波沿 $+y$ 轴传播。由于引力波是横波，空间距离振荡发生在垂直于传播方向的 $x$-$z$ 平面内。选项 A–D 均在 $x$-$y$ 平面内，其中完全垂直于 $y$ 轴的是沿 $x$ 轴方向，故选 **A**。
  - **B2 (LIGO 双台站时间差定位)**：信号先后到达 L1 与 H1 的时间差 $\Delta t = 0.007\text{ s}$，对应波程差 $\Delta l = c\Delta t = 3.00\times 10^8 \times 0.007 = 2.1\times 10^3\text{ km}$。两探测器间距 $d = 3\times 10^3\text{ km}$，因波源距离远大于 $d$，可视为平面波入射，波源方向与 L1-H1 连线夹角 $\theta$ 满足：
    \[
    \cos\theta = \frac{c\Delta t}{d} = \frac{2.1\times 10^3\text{ km}}{3\times 10^3\text{ km}} = 0.7 \implies \theta = \arccos(0.7) \approx 0.795\text{ rad} \approx 45.6^\circ.
    \]
    由于双探测器关于连线具有轴对称性，波源在三维空间中的可能方向构成一个以 L1-H1 连线（$y$ 轴）为轴、偏向 L1（$-y$）一侧、半顶角为 $45.6^\circ$ 的**圆锥面（Cone）**。
  - **B3 (穿过地球的引力波总能量 $E_R$)**：双黑洞并合损失质量 $\Delta M = (36 + 29 - 62)M_\odot = 3 M_\odot$，释放总引力波能量：
    \[
    E_{\text{tot}} = \Delta M c^2 = 3 \times 1.99\times 10^{30}\text{ kg} \times (3.00\times 10^8\text{ m/s})^2 \approx 5.373 \times 10^{47}\text{ J}.
    \]
    在距离 $D = 10^{22}\text{ km} = 10^{25}\text{ m}$ 处，地球截面 $\pi r_E^2$（$r_E = 6.37\times 10^6\text{ m}$）接收的能量比例为 $\frac{\pi r_E^2}{4\pi D^2} \approx 1.014 \times 10^{-37}$，故穿过地球的能量为：
    \[
    E_R = E_{\text{tot}} \frac{r_E^2}{4 D^2} \approx 5.45 \times 10^{10}\text{ J}.
    \]
  - **B4 (到达地球时的引力波振幅 $A$)**：球面波能流密度与距离平方成反比（$\propto 1/r^2$），而引力波能量密度正比于振幅平方（$\propto A^2$），故振幅与距离成反比 $A \propto 1/r$。由 $r_0 = 1000\text{ km}$ 处 $A_0 \simeq 0.01$ 得地球处振幅：
    \[
    A = A_0 \frac{r_0}{D} = 0.01 \times \frac{10^3\text{ km}}{10^{22}\text{ km}} = 10^{-21}.
    \]
  - **B5 (退行速度的多普勒测量)**：只有**元素的发射光谱或吸收光谱（B）**具有已知的实验室固有特征频率，通过比对观测频率与固有频率即可直接测定多普勒红移与退行速度；同步辐射谱与带电粒子能量分布连续且依赖天体未知参数，引力波频率则与质量存在简并。故选 **B**。
  - **C1–C3 (引力波潮汐力与弹簧振子受迫响应)**：
    - 设两粒子对称位于 $x = \pm x_p(t)$，无引力波时平衡位置为 $x = \pm r/2$。当 $k = 0$（自由粒子）时，两粒子间距在 $r(1-A)$ 与 $r(1+A)$ 间振荡，即右侧粒子运动学方程为 $x^{(0)}(t) = \frac{r}{2} - \frac{Ar}{2}\sin(\omega_{GW} t)$。
    - 代入牛顿第二定律 $m\ddot{x}^{(0)} = F_0 \sin(\omega_{GW} t)$，定出引力波对右侧粒子的等效周期作用力幅值为：
      \[
      F_0 = \frac{1}{2} m \omega_{GW}^2 A r \quad (\text{左侧粒子受力为 } -F_0\sin(\omega_{GW}t)).
      \]
    - 加上原长为 $r$、劲度系数为 $k$ 的轻弹簧后，由对称性，弹簧中点静止，右侧半根弹簧的等效劲度系数为 $2k$。右侧粒子位移偏移量 $\xi(t) = x(t) - r/2$ 满足受迫振动方程：
      \[
      m\ddot{\xi} + 2k\xi = F_0 \sin(\omega_{GW} t) = \frac{1}{2} m \omega_{GW}^2 A r \sin(\omega_{GW} t).
      \]
    - 最小动能稳态特解为 $\xi(t) = \frac{r A'}{2}\sin(\omega_{GW} t)$，代入得精确响应振幅：
      \[
      A' = \frac{A \omega_{GW}^2}{\left|\frac{2k}{m} - \omega_{GW}^2\right|}.
      \]
    - **C1 ($k \gg m\omega_{GW}^2$)**：低频准静态极限下，惯性项可忽略，弹簧伸长直接平衡引力波潮汐力 $2k\xi_{\max} \simeq F_0$，得：
      \[
      A' \simeq \frac{m\omega_{GW}^2}{2k} A.
      \]
    - **C2 ($k \ll m\omega_{GW}^2$)**：高频弱耦合极限下，对 $k$ 展开至一阶线性项（或用微扰法 $x = x^{(0)} + x^{(1)}$）：
      \[
      A' = \frac{A}{1 - \frac{2k}{m\omega_{GW}^2}} \simeq A\left(1 + \frac{2k}{m\omega_{GW}^2}\right).
      \]
    - **C3 ($k = m\omega_{GW}^2 / 2$)**：此时弹簧-双质点系统的固有角频率 $\omega_0 = \sqrt{2k/m} = \omega_{GW}$ 与引力波驱动频率相等，发生**共振（Resonance）**，两粒子间距做周期性振荡且振荡幅度随时间不断增大（线性增长）。
  - **C4 (地球玩具模型单周期吸收能量数量级估算)**：
    - 平衡时两质点相距 $r = 6000\text{ km} = 6\times 10^6\text{ m}$，弹簧原长 $r_0 = 7000\text{ km}$，压缩量 $\Delta r = 1000\text{ km} = 10^6\text{ m}$。由自引力与弹簧弹力平衡：
      \[
      k\Delta r = \frac{G_N m^2}{r^2} \implies k = \frac{6.67\times 10^{-11}\times (3\times 10^{24})^2}{(6\times 10^6)^2 \times 10^6} \approx 1.67\times 10^{19}\text{ kg/s}^2.
      \]
    - 对比 $m\omega_{GW}^2 = 3\times 10^{24} \times (2\pi \times 100)^2 \approx 1.18\times 10^{30}\text{ kg/s}^2 \gg k$，地球处于 **C2 ($k \ll m\omega_{GW}^2$)** 极限，地球尺度变化幅值约为 $\delta r \simeq rA = 6\times 10^{-15}\text{ m}$。
    - 等效驱动力幅值为 $F_0 = \frac{1}{2}m\omega_{GW}^2 Ar \approx 3.55\times 10^{15}\text{ N}$。若按驱动力在特征位移 $\delta r$ 上所做功的量级估算：$W \sim F_0 \delta r \sim 21\text{ J}$。
  - **C5 (地球质量黑洞吸收的引力波能量)**：
    - 在牛顿力学中，黑洞半径由逃逸速度等于光速定出：
      \[
      v_{\text{esc}} = \sqrt{\frac{2 G_N M_E}{r_{BH}}} = c \implies r_{BH} = \frac{2 G_N M_E}{c^2} \approx 8.85\times 10^{-3}\text{ m}.
      \]
    - 由于到达黑洞视界内的引力波全部被吸收无法逃逸，由几何截面之比（相对 B3 中地球接收能量 $E_R \approx 5.45\times 10^{10}\text{ J}$）：
      \[
      E_{BH} = E_R \left(\frac{r_{BH}}{r_E}\right)^2 \approx 5.45\times 10^{10}\text{ J} \times \left(\frac{0.00885}{6.37\times 10^6}\right)^2 \approx 1.05\times 10^{-7}\text{ J}.
      \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：
  1. **A1–A5 与 B1–B5**：盲解结果与官方参考解答完全一致。需要注意在 B3 的大数指数运算中，$\frac{r_E^2}{4D^2} = \frac{(6370\text{ km})^2}{4\times (10^{22}\text{ km})^2} = 1.014\times 10^{-37}$，乘以 $E_{\text{tot}} = 5.37\times 10^{47}\text{ J}$ 得 $5.45\times 10^{10}\text{ J}$，切勿在 $\text{km}$ 与 $\text{m}$ 换算时出现 10 的幂次笔误。
  2. **C1–C2 的两种解法对比**：官方解答给出了“半弹簧对称法”（取右侧半根弹簧，劲度系数为 $2k$，并在 C2 中展示了一阶微扰迭代 $x = x^{(0)} + x^{(1)}$）以及“双质点 $2\times 2$ 矩阵求逆法”。我们在盲解中直接写出相对位移（或半弹簧）的二阶常系数受迫振动方程并求稳态解 $A' = \frac{A}{1 - 2k/(m\omega_{GW}^2)}$，一次推导即可同时涵盖 C1（大 $k$ 展开）、C2（小 $k$ 泰勒展开）与 C3（分母为零的共振判据），在考场上最为迅捷。
  3. **C4 地球吸收能量估算的物理图像辨析**：官方解答采用 $W \sim F_0 \delta r = \frac{1}{2}m\omega_{GW}^2 A^2 r^2 \approx 21\text{ J}$，其物理假设是引力波在拉伸地球的四分之一周期内做功 $F_0 \delta r$（转化成质点动能与势能），随后在回弹过程中这部分能量通过地球内部耗散机制转化为热能；若无耗散或仅计入弹簧弹性势能改变量 $\Delta E_p \sim \frac{1}{2}k(\delta r)^2 \sim 10^{-9}\text{ J}$，数值会小得多。因此答题时必须写出 $F_0 = \frac{1}{2}m\omega_{GW}^2 Ar$ 与 $\delta r = rA$ 的分步给分点（各 0.5 分）。
- **核心难点与易错点**：
  1. **A1/A4 双星间距 $2R$ 与轨道半径 $R$ 的混淆**：题干与插图明确定义 $R$ 为圆轨道半径（两星间距为 $2R$），若误将万有引力分母写成 $R^2$ 而非 $(2R)^2$，会导致 A1 周期漏掉因子 2，且 A4 引力势能写成 $-G_N M^2/R$ 造成系数连锁错误。
  2. **C1/C2 串联半弹簧的劲度系数加倍（$2k$ 而非 $k$）**：整根弹簧原长为 $r$、劲度系数为 $k$，当两粒子各自向外移动 $x_0$ 时，弹簧总伸长量为 $2x_0$，每个粒子受到的弹力为 $2kx_0$。若忘记因子 2，会导致 C1 得到 $\frac{m\omega_{GW}^2}{k}A$、C2 得到 $A(1 + \frac{k}{m\omega_{GW}^2})$，且与 C3 题干给出的共振条件 $k = m\omega_{GW}^2/2$ 产生矛盾（实际上 C3 的题干条件本身就是校核 C1/C2 系数 2 的“天然提示”！）。

---

## 2. `panpho-2019-paper-2-problem-slice-q2` — 同步现象 (Synchronization)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：
  - **Part A (惠更斯双摆钟同步模型，Oliveira & Melo, *Sci. Rep.* 2015)**：受恒定干摩擦阻尼 $mLb\,\text{sign}(\dot{q})$ 与定点能量注入（擒纵机构每次在 $q = -b/\omega^2, \dot{q}>0$ 处注入固定动能 $\frac{1}{2}mL^2 h^2$）的单摆极限环振荡，以及双摆通过脉冲耦合实现同相/反相同步的庞加莱映射（Poincaré map）。
  - **Part B (交流电网的二阶 Kuramoto 同步模型，Dörfler et al., *PNAS* 2013)**：电感输电线有功功率传输公式 $\bar{P}_{12} = \frac{V^2}{2\omega L}\sin(\theta_1 - \theta_2)$、发电机/电动机转子相位动力学方程（Swing equation）及其与圆环弹簧耦合振子网络的精确力学类比。
- **分步独立推导**：
  - **A1 (干摩擦单摆小角度运动方程)**：切向牛顿第二定律为 $mL\ddot{q} = -mg\sin q - mLb\,\text{sign}(\dot{q})$，小角度下 $\sin q \simeq q$，引入 $\omega = \sqrt{g/L}$ 得：
    \[
    \ddot{q} = -\omega^2 q - b\,\text{sign}(\dot{q}).
    \]
  - **A2 (分段平移简谐运动求解完整周期)**：
    - **(a) 第一个四分之一周期（$0 \le t \le \frac{\pi}{2\omega}$，$\dot{q} > 0$）**：方程化为 $\ddot{q} = -\omega^2\left(q + \frac{b}{\omega^2}\right)$，是以 $q = -\frac{b}{\omega^2}$ 为平衡中心的简谐运动！由于初态 $t=0$ 恰在该平衡中心 $q(0) = -\frac{b}{\omega^2}$ 且 $\dot{q}(0) = u_n$，立得：
      \[
      q(t) = -\frac{b}{\omega^2} + \frac{u_n}{\omega}\sin(\omega t), \qquad \dot{q}(t) = u_n\cos(\omega t).
      \]
    - **(b) 第二、三个四分之一周期（$\frac{\pi}{2\omega} \le t \le \frac{3\pi}{2\omega}$，$\dot{q} < 0$）**：在右侧最高点 $t = \frac{\pi}{2\omega}$ 处 $q\left(\frac{2\pi}{4\omega}\right) = \frac{u_n}{\omega} - \frac{b}{\omega^2}$、$\dot{q} = 0$。此后 $\dot{q} < 0$，方程变为 $\ddot{q} = -\omega^2\left(q - \frac{b}{\omega^2}\right)$，平衡中心跳变至 $+\frac{b}{\omega^2}$，振幅减小为 $\left(\frac{u_n}{\omega} - \frac{b}{\omega^2}\right) - \frac{b}{\omega^2} = \frac{u_n}{\omega} - \frac{2b}{\omega^2}$：
      \[
      q(t) = \frac{b}{\omega^2} + \left(\frac{u_n}{\omega} - \frac{2b}{\omega^2}\right)\sin(\omega t), \qquad \dot{q}(t) = \left(u_n - \frac{2b}{\omega}\right)\cos(\omega t).
      \]
    - **(c) 第四个四分之一周期（$\frac{3\pi}{2\omega} \le t \le \frac{2\pi}{\omega}$，$\dot{q} > 0$）**：在左侧最高点 $t = \frac{3\pi}{2\omega}$ 处 $q\left(\frac{3\pi}{2\omega}\right) = -\frac{u_n}{\omega} + \frac{3b}{\omega^2}$、$\dot{q} = 0$。此后 $\dot{q} > 0$，平衡中心跳回 $-\frac{b}{\omega^2}$，振幅进一步衰减为 $\frac{u_n}{\omega} - \frac{4b}{\omega^2}$：
      \[
      q(t) = -\frac{b}{\omega^2} + \left(\frac{u_n}{\omega} - \frac{4b}{\omega^2}\right)\sin(\omega t), \qquad \dot{q}(t) = \left(u_n - \frac{4b}{\omega}\right)\cos(\omega t).
      \]
  - **A3 ($u_{n+1}$ 与 $u_n$ 的递推关系)**：第 $n$ 个周期结束（$t = \frac{2\pi}{\omega}^-$）到达踢动点 $q = -\frac{b}{\omega^2}$ 时，角速度为 $\dot{q}_- = u_n - \frac{4b}{\omega}$。注入动能 $\frac{1}{2}mL^2 h^2$ 后：
    \[
    \frac{1}{2}mL^2 u_{n+1}^2 = \frac{1}{2}mL^2\left(u_n - \frac{4b}{\omega}\right)^2 + \frac{1}{2}mL^2 h^2 \implies u_{n+1} = \sqrt{\left(u_n - \frac{4b}{\omega}\right)^2 + h^2}.
    \]
  - **A4 (多次踢动后的稳态极限环角速度 $u_\infty$)**：令 $u_{n+1} = u_n = u$，平方展开消去 $u^2$ 得：
    \[
    0 = -\frac{8b}{\omega}u + \frac{16b^2}{\omega^2} + h^2 \implies u = \frac{h^2\omega}{8b} + \frac{2b}{\omega}.
    \]
  - **A5 (第一象限受角冲量 $mL^2\alpha$ 后的相位偏移)**：
    - 在 $t_0 \in \left(0, \frac{\pi}{2\omega}\right)$ 受到角冲量 $mL^2\alpha$，角速度瞬时增加 $\Delta\dot{q} = \alpha$。由线性叠加原理，对于 $t \in \left(t_0, t_1\right)$：
      \[
      q(t) = -\frac{b}{\omega^2} + \frac{u_n}{\omega}\sin(\omega t) + \frac{\alpha}{\omega}\sin\left[\omega(t - t_0)\right], \qquad \dot{q}(t) = u_n\cos(\omega t) + \alpha\cos\left[\omega(t - t_0)\right].
      \]
    - **(a) 摩擦力第一次变号时刻 $t_1$**：令 $\omega t_1 = \frac{\pi}{2} + \varepsilon$，由 $\dot{q}(t_1) = 0$ 展开至 $O(\alpha)$ 得 $-u_n\varepsilon + \alpha\sin(\omega t_0) = 0 \implies \varepsilon = \frac{\alpha\sin(\omega t_0)}{u_n}$，故：
      \[
      t_1 = \frac{\pi}{2\omega} + \frac{\alpha\sin(\omega t_0)}{\omega u_n}.
      \]
    - **(b) 摩擦力第二次变号时刻 $t_2$ 与 (c) 第 $(n+1)$ 次踢动时刻 $t_3$**：利用简谐运动的等时性——从右转折点 $\dot{q}(t_1)=0$ 到左转折点 $\dot{q}(t_2)=0$ 恰经历围绕 $+\frac{b}{\omega^2}$ 的半个简谐周期 $\frac{\pi}{\omega}$；从左转折点 $\dot{q}(t_2)=0$ 到第四象限平衡中心 $q(t_3) = -\frac{b}{\omega^2}$ 恰经历四分之一个简谐周期 $\frac{\pi}{2\omega}$（与振幅微扰无关！）。因此：
      \[
      t_2 = \frac{3\pi}{2\omega} + \frac{\alpha\sin(\omega t_0)}{\omega u_n}, \qquad t_3 = \frac{2\pi}{\omega} + \frac{\alpha\sin(\omega t_0)}{\omega u_n}.
      \]
  - **A6 (第四象限受角冲量 $mL^2\alpha$ 后的踢动时刻)**：
    - 当 $t_0 \in \left(\frac{3\pi}{2\omega}, \frac{2\pi}{\omega}\right)$ 时，冲击前第四象限角速度幅值为 $u_n - \frac{4b}{\omega}$。受冲量后：
      \[
      q(t) = -\frac{b}{\omega^2} + \left(\frac{u_n}{\omega} - \frac{4b}{\omega^2}\right)\sin(\omega t) + \frac{\alpha}{\omega}\sin\left[\omega(t - t_0)\right].
      \]
    - 令 $\omega t_3 = 2\pi + \delta$，由 $q(t_3) = -\frac{b}{\omega^2}$ 展开至 $O(\alpha)$ 得 $\left(u_n - \frac{4b}{\omega}\right)\delta - \alpha\sin(\omega t_0) = 0$（注意 $\sin(\omega t_0) < 0$，故 $\delta < 0$，冲击使摆提前到达踢动点！），得：
      \[
      t_3 = \frac{2\pi}{\omega} + \frac{\alpha\sin(\omega t_0)}{\omega\left(u_n - \frac{4b}{\omega}\right)}.
      \]
  - **A7 (双摆相位滞后 $\phi_n$ 的演化映射)**：
    - 设单摆 1 在 $t = 0$ 开始第 $n$ 个周期，单摆 2 滞后相位 $\phi_n \in [0, \pi/2)$，即单摆 2 在 $t_0 = \frac{\phi_n}{\omega}$ 到达 $q_2 = -\frac{b}{\omega^2}$ 并向单摆 1 发送正冲量 $\alpha$。
    - 此时单摆 1 处于第 1 象限（相位 $\omega t_0 = \phi_n$），由 A5 知单摆 1 的下一次踢动时刻推迟至：
      \[
      t_1 = \frac{2\pi}{\omega} + \frac{\alpha\sin\phi_n}{\omega u_n}.
      \]
    - 在 $t = t_1$ 时刻，单摆 1 到达 $q_1 = -\frac{b}{\omega^2}$ 并向单摆 2 发送正冲量 $\alpha$。此时单摆 2 距离其上次踢动已过去时间 $t_1 - \frac{\phi_n}{\omega} \simeq \frac{2\pi - \phi_n}{\omega}$，处于第 4 象限！由 A6 知单摆 2 的下一次踢动时刻提前至：
      \[
      t_2 = \frac{\phi_n}{\omega} + \frac{2\pi}{\omega} + \frac{\alpha\sin(2\pi - \phi_n)}{\omega\left(u_n - \frac{4b}{\omega}\right)} = \frac{2\pi + \phi_n}{\omega} - \frac{\alpha\sin\phi_n}{\omega\left(u_n - \frac{4b}{\omega}\right)}.
      \]
    - 因此第 $n+1$ 周期开始时两摆的相位差为：
      \[
      \phi_{n+1} = \omega(t_2 - t_1) = \phi_n - \alpha\left(\frac{1}{u_n - \frac{4b}{\omega}} + \frac{1}{u_n}\right)\sin\phi_n.
      \]
  - **A8 (小相移下衰减 10 倍所需的周期数 $N$)**：当 $\phi_n \ll 1$ 时，$\sin\phi_n \simeq \phi_n$，每周期按公比 $1 - \alpha\left[\left(u_n - \frac{4b}{\omega}\right)^{-1} + u_n^{-1}\right]$ 指数衰减，减小 10 倍所需周期数为：
    \[
    N \simeq \frac{\ln 10}{\alpha\left[\left(u_n - \frac{4b}{\omega}\right)^{-1} + u_n^{-1}\right]}.
    \]
  - **B1 (电感传输线平均有功功率)**：由 $L\frac{dI_{12}}{dt} = V_1(t) - V_2(t) = V[\cos(\omega t + \theta_1) - \cos(\omega t + \theta_2)]$ 积分得 $I_{12}(t) = \frac{V}{\omega L}[\sin(\omega t + \theta_1) - \sin(\omega t + \theta_2)] + I_{12}(0)$。节点 1 向节点 2 传输的瞬时功率 $P_{12}(t) = V_1(t)I_{12}(t)$ 对时间取周期平均：
    \[
    \bar{P}_{12} = \langle V\cos(\omega t + \theta_1) I_{12}(t)\rangle = \frac{V^2}{2\omega L}\sin(\theta_1 - \theta_2).
    \]
  - **B2 (电网节点相位 $\theta_j(t)$ 的动力学方程)**：节点 $j$ 转子动能为 $E_{\text{rot}, j} = \frac{1}{2}I(\omega + \dot{\theta}_j)^2$，功率平衡方程为 $\frac{d}{dt}\left[\frac{1}{2}I(\omega + \dot{\theta}_j)^2\right] = P_j - \frac{1}{2}\kappa(\omega + \dot{\theta}_j)^2 - \sum_{k\neq j}\frac{V^2}{2\omega L}\sin(\theta_j - \theta_k)$。在 $|\dot{\theta}_j| \ll \omega$ 下保留一阶项并除以 $\omega$ 得：
    \[
    I\frac{d^2\theta_j}{dt^2} = \frac{P_j}{\omega} - \frac{1}{2}\kappa\omega - \kappa\frac{d\theta_j}{dt} + \frac{V^2}{2\omega^2 L}\sum_{k\neq j}\sin(\theta_k - \theta_j).
    \]
  - **B3 (圆环耦合振子网络动力学方程与电网类比表)**：半径为 $R$ 的圆环上粒子 $j$ 与 $k$ 间弦长为 $2R\sin\frac{|\theta_k - \theta_j|}{2}$，弹簧拉力 $2kR\sin\frac{\theta_k - \theta_j}{2}$ 沿圆环切向的分量为 $2kR\sin\frac{\theta_k - \theta_j}{2}\cos\frac{\theta_k - \theta_j}{2} = kR\sin(\theta_k - \theta_j)$。乘以半径 $R$ 写出角动量定理（力矩方程，$I = mR^2$）：
    \[
    I\frac{d^2\theta_j}{dt^2} = R F_j - R^2 b\frac{d\theta_j}{dt} + \sum_{k\neq j} k R^2 \sin(\theta_k - \theta_j).
    \]
    对应关系表：
    - 转动惯量项：$I\frac{d^2\theta_j}{dt^2} \longleftrightarrow I\frac{d^2\theta_j}{dt^2}$
    - 阻尼力矩项：$R^2 b\frac{d\theta_j}{dt} \longleftrightarrow \kappa\frac{d\theta_j}{dt}$
    - 外力矩项：$R F_j \longleftrightarrow \frac{P_j}{\omega} - \frac{1}{2}\kappa\omega$
    - 耦合恢复力矩项：$k R^2\sin(\theta_k - \theta_j) \longleftrightarrow \frac{V^2}{2\omega^2 L}\sin(\theta_k - \theta_j)$
  - **B4 (稳态下发电机与功耗设备间的相位差)**：忽略摩擦（$\kappa = 0$），每个功耗节点功率 $P_c = -P$，每个发电机节点功率 $P_g = \frac{N_c}{N_g}P$。稳态时所有发电机同相 $\theta_g$、所有功耗节点同相 $\theta_c$，对功耗节点列稳态平衡方程：
    \[
    -\frac{P}{\omega} + N_g \frac{V^2}{2\omega^2 L}\sin(\theta_g - \theta_c) = 0 \implies \theta_g - \theta_c = \arcsin\left(\frac{2\omega L P}{N_g V^2}\right).
    \]
  - **B5 (维持电网同步的最少发电机数量)**：由 $|\sin(\theta_g - \theta_c)| \le 1$ 得：
    \[
    \frac{2\omega L P}{N_g V^2} \le 1 \implies N_{g,\min} = \left\lceil \frac{2\omega L P}{V^2} \right\rceil \quad \left(\text{或 }\frac{2\omega L P}{V^2}\right).
    \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：盲解的所有结果与官方解答完全一致。在 A5(b) 和 A5(c) 中，官方解答详细计算了冲量对第二、三、四象限振幅的 $O(\alpha\cos\omega t_0)$ 修正，然后再求解速度过零点与位移过 $-\frac{b}{\omega^2}$ 点；而我们在盲解中指出的**分段简谐运动等时性**（从转折点到转折点必为 $\pi/\omega$，从转折点到平衡中心 $-\frac{b}{\omega^2}$ 必为 $\pi/(2\omega)$，与振幅无关）直接一步看穿了为什么 A5 的三个时刻偏移量完全相同！
- **核心难点与易错点**：
  1. **为什么双摆同向冲量 $\alpha > 0$ 会导致同相同步？**：在第一象限受正冲量使摆幅增大从而**推迟**到达最高点（$\Delta t_1 = +\frac{\alpha\sin\phi_n}{\omega u_n} > 0$），而在第四象限受正冲量使摆更快冲向平衡点从而**提前**完成周期（$\Delta t_2 = -\frac{\alpha\sin\phi_n}{\omega(u_n - 4b/\omega)} < 0$），两者符号相反，在相减 $\phi_{n+1} = \omega(t_2 - t_1)$ 时同向叠加使相位差缩小！干摩擦 $b > 0$ 使得第四象限速度更小（$u_n - 4b/\omega < u_n$），进一步放大了第四象限的相位响应灵敏度。
  2. **B3 表格的量纲一致性（力方程 vs 力矩方程）**：官方答题纸表格表头明确写的是“转动惯量 Moment of inertia”、“阻尼力矩 Damping torque”、“外力扭矩 Torque due to external force”，因此必须将切向牛顿第二定律两边同乘半径 $R$ 化为力矩形式（如 $R^2 b \dot{\theta}_j$ 和 $k R^2 \sin(\theta_k - \theta_j)$），切勿直接填切向力而漏掉因子 $R$ 或 $R^2$。

---

## 3. `panpho-2020-paper-2-problem-slice-q1` — 引力常数的精密测量 (Precision Measurement of the Gravitational Constant $G$)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：Parks & Faller 激光干涉双单摆测 $G$ 实验（*PRL* **105**, 110801 (2010)）——有限长均匀细线引力场积分、高斯引力通量定理、四质量源（外侧/内侧对称构型）水平引力分量矢量合成、独立测量不确定度传递公式、单摆水平微位移静力平衡 $\Delta g_x = \omega^2\Delta x$，以及法布里-珀罗（Fabry-Pérot）光学谐振腔的自由光谱区（FSR）、腔损耗与拍频位移传感。
- **分步独立推导**：
  - **A1 (地球表面引力场强)**：忽略地球自转，地球表面引力场强为：
    \[
    g = \frac{GM}{R^2}.
    \]
  - **A2 (有限长细线在 $P$ 点的引力场 $X$ 分量)**：细线总质量 $M$、高度 $h$，线密度 $\lambda = M/h$，沿 $Z$ 轴分布于 $z \in [-z_0, h - z_0]$，点 $P$ 位于 $(r, 0)$。微元 $dz$ 在 $P$ 点产生的水平引力场（指向细线，取大小为正）：
    \[
    g_x = \int_{-z_0}^{h-z_0} \frac{G(M/h)\,dz}{r^2 + z^2}\frac{r}{\sqrt{r^2 + z^2}} = \frac{GMr}{h}\int_{-z_0}^{h-z_0}\frac{dz}{(z^2 + r^2)^{3/2}}.
    \]
    利用题目给定的积分公式 $\int\frac{dx}{(x^2+a^2)^{3/2}} = \frac{x}{a^2\sqrt{x^2+a^2}} + C$ 得：
    \[
    g_x = \frac{GM}{hr}\left[\frac{h - z_0}{\sqrt{(h - z_0)^2 + r^2}} + \frac{z_0}{\sqrt{z_0^2 + r^2}}\right].
    \]
  - **A3 (近线极限 $r \to 0$ 下的引力场)**：当 $r \ll z_0, h-z_0$ 时，方括号内两项均趋于 1，故：
    \[
    g_x \simeq \frac{2GM}{hr}.
    \]
  - **A4 (高斯定理验证 A3)**：对点质量 $M$，穿过半径为 $r$ 球面的引力场总通量为 $\Phi = \frac{GM}{r^2}(4\pi r^2) = 4\pi GM$。取包络细线的一段同轴小圆柱面（半径 $r$、高 $\Delta z$），内部包含质量 $\Delta m = \frac{M}{h}\Delta z$，由高斯定理 $\Phi_{\text{cyl}} = g_x (2\pi r \Delta z) = 4\pi G \frac{M}{h}\Delta z$，即得 $g_x = \frac{2GM}{hr}$。
  - **A5 (内侧位置时摆锤 A 处的水平引力场)**：
    - 摆锤 A 位于 $(-d/2, 0) = (-0.17\text{ m}, 0)$，内侧四个质量源轴线位于 $(\pm a_2/2, \pm b/2) = (\pm 0.083\text{ m}, \pm 0.131\text{ m})$，全部位于摆锤 A 右侧（$+x$ 方向）。
    - 左侧一对内源到 A 的距离与方向余弦：
      \[
      r_{\text{left}} = \sqrt{\left(\frac{d - a_2}{2}\right)^2 + \left(\frac{b}{2}\right)^2} = \sqrt{0.087^2 + 0.131^2} \approx \sqrt{0.02473}\text{ m} \approx 0.1573\text{ m}, \quad \cos\theta_{\text{left}} = \frac{0.087}{r_{\text{left}}} \approx 0.5532.
      \]
    - 右侧一对内源到 A 的距离与方向余弦：
      \[
      r_{\text{right}} = \sqrt{\left(\frac{d + a_2}{2}\right)^2 + \left(\frac{b}{2}\right)^2} = \sqrt{0.253^2 + 0.131^2} \approx \sqrt{0.08117}\text{ m} \approx 0.2849\text{ m}, \quad \cos\theta_{\text{right}} = \frac{0.253}{r_{\text{right}}} \approx 0.8880.
      \]
    - 代入 $G = 6.67\times 10^{-11}\text{ N}\cdot\text{kg}^{-2}\text{m}^2$，$M = 119.1\text{ kg}$，$h = 0.312\text{ m}$，$z_0 = 0.002\text{ m}$，得向右总场强：
      \[
      g_{\text{in}} = g_{\text{left}} + g_{\text{right}} \approx 1.6204\times 10^{-7} + 1.1798\times 10^{-7} = 2.8002\times 10^{-7}\text{ m/s}^2.
      \]
  - **A6 (外侧位置时摆锤 A 处的水平引力场)**：
    - 外侧四个质量源轴线位于 $(\pm a_1/2, \pm b/2) = (\pm 0.284\text{ m}, \pm 0.131\text{ m})$，其中左对源在 A 左侧（向左拉 A），右对源在 A 右侧（向右拉 A）：
      \[
      r_{\text{left}} = \sqrt{(0.284 - 0.17)^2 + 0.131^2} = \sqrt{0.03016}\text{ m} \approx 0.1737\text{ m}, \quad \cos\theta_{\text{left}} = \frac{0.114}{r_{\text{left}}} \approx 0.6565,
      \]
      \[
      r_{\text{right}} = \sqrt{(0.284 + 0.17)^2 + 0.131^2} = \sqrt{0.2233}\text{ m} \approx 0.4725\text{ m}, \quad \cos\theta_{\text{right}} = \frac{0.454}{r_{\text{right}}} \approx 0.9608.
      \]
    - 左对源产生向左场强 $g_{\text{left}} \approx 1.7016\times 10^{-7}\text{ m/s}^2$，右对源产生向右场强 $g_{\text{right}} \approx 5.7237\times 10^{-8}\text{ m/s}^2$，净水平场强（向左）为：
      \[
      g_{\text{out}} = g_{\text{left}} - g_{\text{right}} \approx 1.1292\times 10^{-7}\text{ m/s}^2 \quad (\text{或向右 }-1.1292\times 10^{-7}\text{ m/s}^2).
      \]
  - **A7 (质量源从外侧移到内侧时摆锤 A 处水平引力场变化量 $\Delta g_x$)**：由于内侧场强向右、外侧场强向左，总变化量为两者绝对值之和：
    \[
    \Delta g_x = 2.8002\times 10^{-7} + 1.1292\times 10^{-7} = 3.9294\times 10^{-7}\text{ m/s}^2.
    \]
  - **A8 (A3 表达式 $g_x = \frac{2GM}{hr}$ 的相对不确定度)**：由独立误差传递公式：
    \[
    \frac{\sigma_{g_x}}{g_x} = \sqrt{\left(\frac{\sigma_M}{M}\right)^2 + \left(\frac{\sigma_h}{h}\right)^2 + \left(\frac{\sigma_r}{r}\right)^2} = \sqrt{(0.6\times 10^{-5})^2 + (1.4\times 10^{-5})^2 + (1.4\times 10^{-5})^2} = \sqrt{4.28}\times 10^{-5} \approx 2.07\times 10^{-5}.
    \]
  - **B1 ($\Delta g_x$ 与单摆微位移 $\Delta x$、固有角频率 $\omega$ 的关系)**：单摆小角度水平恢复力满足 $m\Delta g_x = m g \tan\theta \simeq m g \frac{\Delta x}{l} = m\omega^2\Delta x$，故：
    \[
    \Delta g_x = \omega^2 \Delta x.
    \]
  - **B2 (利用 A7 计算摆锤位移变化量)**：单摆垂向距离 $l = 0.738\text{ m}$，$g = 9.8\text{ m/s}^2$。单个摆锤水平偏移量为：
    \[
    \Delta x = l\frac{\Delta g_x}{g} = 0.738 \times \frac{3.9294\times 10^{-7}}{9.8} \approx 29.59\text{ nm} \quad (\text{两摆锤间距变化量为 }2\Delta x \approx 59.18\text{ nm}).
    \]
  - **B3 (两摆锤频率平均值及其不确定度)**：已知 $f_1 = (0.589\,8171 \pm 0.000\,0023)\text{ Hz}$，$f_2 = (0.589\,7069 \pm 0.000\,0013)\text{ Hz}$。
    - 平均值：$\bar{f} = \frac{1}{2}(f_1 + f_2) = 0.589\,7620\text{ Hz}$。
    - 标准差：$\sigma_{\bar{f}} = \frac{1}{2}\sqrt{\sigma_{f_1}^2 + \sigma_{f_2}^2} \approx 1.321\times 10^{-6}\text{ Hz}$；按题目 Remark 定义的相对不确定度为：
      \[
      \frac{\sigma_{\bar{f}}}{\bar{f}} = \frac{\sqrt{\frac{1}{4}(2.3\times 10^{-6})^2 + \frac{1}{4}(1.3\times 10^{-6})^2}}{0.589\,7620} \approx 2.24\times 10^{-6}.
      \]
  - **B4 (达到 $10^{-7}$ 周期相对精度所需测量的周期数 $n$)**：单摆周期 $T = 1/\bar{f} \approx 1.6956\text{ s}$。测量 $n$ 个周期的总时间绝对误差为 $\sigma_t = 10^{-5}\text{ s}$，单周期相对误差为 $\frac{\sigma_t}{nT} = 10^{-7}$，解得：
    \[
    n = \frac{10^{-5}}{10^{-7}\times 1.6956} \approx 59.
    \]
  - **B5 (法布里-珀罗腔相邻纵模的频率间隔与波长间隔)**：腔长 $L = d = 0.34\text{ m}$，驻波相邻纵模频率差（自由光谱区 FSR）与波长差分别为：
    \[
    \Delta f = \frac{c}{2L} = \frac{3.00\times 10^8}{2\times 0.34} \approx 4.41\times 10^8\text{ Hz} = 441\text{ MHz},
    \]
    \[
    \Delta\lambda = \frac{\lambda^2}{c}\Delta f = \frac{(633\times 10^{-9})^2}{2\times 0.34} \approx 5.89\times 10^{-13}\text{ m} = 5.89\times 10^{-4}\text{ nm}.
    \]
  - **B6 (每次透射的能量损失比例估算)**：谱线宽度 $\delta f \approx 100\text{ kHz}$，无输入时驻波相位扩散 $2\pi$（或能量衰减特征时间）为 $\tau = \frac{1}{2\pi \delta f}$，而光在两镜间单程传播时间为 $\Delta t = \frac{L}{c}$，故每次透射损失能量比例约为：
    \[
    \eta \simeq \frac{L/c}{1/(2\pi\delta f)} = \frac{2\pi L \delta f}{c} = \frac{2\pi \times 0.34 \times 10^5}{3.00\times 10^8} \approx 7.1\times 10^{-4} \quad (\text{若不计 }2\pi\text{ 因子则为 }1.1\times 10^{-4}).
    \]
  - **B7 (腔长改变 $\delta L = 1\text{ nm}$ 对应的腔频变化 $\delta f$)**：由 $f = n\frac{c}{2L}$ 两边取微分：
    \[
    \delta f = -f\frac{\delta L}{L} = -\frac{c}{\lambda}\frac{\delta L}{L} = -\frac{3.00\times 10^8}{633\times 10^{-9}}\times \frac{1.0\times 10^{-9}}{0.34} \approx -1.3939\text{ MHz}.
    \]
  - **B8 (由 $125\text{ MHz}$ 拍频改变量计算两摆锤间距改变量)**：
    \[
    \Delta x_{\text{sep}} = \frac{125\text{ MHz}}{1.3939\text{ MHz/nm}} \approx 89.68\text{ nm}.
    \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：
  1. **盲解纠错亮点（B7 数量级心算校核）**：在初看 B7 时，由於激光频率 $f = c/\lambda \approx 4.74\times 10^{14}\text{ Hz}$ 极大，心算时极易把 $\frac{10^{-9}}{633\times 10^{-9}}$ 约分后的 $\frac{3\times 10^8}{633\times 0.34} = \frac{300\times 10^6}{215.22} = 1.3939\times 10^6\text{ Hz}$ 误写成 $\text{GHz}$。对照 B8 中实验测得的拍频变化 $125\text{ MHz}$ 与 B2 中估算的数十纳米级位移，立即可知灵敏度必为 $1.3939\text{ MHz/nm}$，从而在 B8 得到极其合理的 $89.68\text{ nm}$！这充分体现了跨小题物理量级自洽检验的重要性。
  2. **B2 中英文题干表述差异提示**：B2 英文题干写的是“change in the separation of the pendulum bobs”（两摆锤间距变化 $2\Delta x \approx 59.18\text{ nm}$），而中文题干写的是“摆锤位置的变化量”（单摆锤位移 $\Delta x \approx 29.59\text{ nm}$）。官方参考解答按单摆锤 $\Delta x = 29.5912\text{ nm}$ 给分，因此竞赛答题时同时写出单摆锤位移 $\Delta x = 29.59\text{ nm}$ 和双摆锤间距变化 $2\Delta x = 59.18\text{ nm}$ 是最稳妥的满分策略。
  3. **A6 镜像打印笔误说明**：官方解答第 7 页在写 A6 的 $r_{\text{right}}^2 = (0.284 + 0.17)^2 + 0.131^2$ 时，中间步骤误印成了 $0.02233\text{ m}^2$（多了一个零，正确值为 $0.2233\text{ m}^2$），但其随后的 $\cos\theta_{\text{right}} = 0.9608$ 与最终结果 $1.1292\times 10^{-7}\text{ m/s}^2$ 均是按正确的 $0.2233\text{ m}^2$ 算出的。
- **核心难点与易错点**：
  1. **A5/A6 四源水平引力场的方向投影与正负号**：必须先计算每个细线源在三维空间中到摆锤 A 的水平面径向距离 $r = \sqrt{\Delta x^2 + (b/2)^2}$，代入 A2 公式算出沿连线方向的场强 $g(r)$，再乘以水平投影余弦 $\cos\theta = \Delta x / r$！很多学生漏乘 $\cos\theta$，或者把 $r$ 误代为 $\Delta x$。此外，内侧位置四源全在 A 右侧（同向相加），外侧位置左源在 A 左、右源在 A 右（反向相减），从而 A7 的总变化量 $\Delta g_x$ 是 A5 与 A6 大小**相加**而非相减！
  2. **题目自定义“不确定度（Uncertainty）”的特殊约定**：题干第 6 页 Remark 明确规定本题中物理量 $f$ 的“误差/不确定度”特指**相对标准差** $\sqrt{\sigma_f^2 / f^2} = \sigma_f / f$（无量纲），因此 A8、B3、B4 均需按相对不确定度计算。

---

## 4. `panpho-2020-paper-2-problem-slice-q2` — 不同维度的物理 (Physics in Various Dimensions)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：
  - **Part A & C ($n$ 维与二维牛顿引力及有效势分析)**：$n$ 维高斯通量定律导出引力 $F = -GMm/r^{n-1}$ 与有效势 $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + V(r)$，分析 $n=4$（共形临界维数）、$n>4$（势垒不稳定性）与 $n=2$（对数势全域束缚）的轨道拓扑。
  - **Part B (Kaluza-Klein 紧致化“降维打击”)**：四维空间将第四维紧致化为周长 $C$ 的小圆环 $S^1$，导出有效三维引力常数 $G_3 = \frac{\pi}{2C}G_4$、相对论 Kaluza-Klein 有效质量 $m_{\text{eff}} = \sqrt{m^2 + p_4^2/c^2}$ 及降维瞬间的机械能跃变。
  - **Part D (2+1 维广义相对论圆锥时空与宇宙弦观测效应)**：点质量 $M$ 产生局部平坦但具有亏损角 $\delta$ 的圆锥几何（等价于三维空间中的宇宙弦 Cosmic String），通过“剪开扇形展平法”研究双像引力透镜（D1）、尾迹相向碰撞（D2）与介质运动下的二维声学多普勒效应（D3–D4）。
- **分步独立推导**：
  - **A1 ($n$ 维牛顿引力与势能幂指数)**：由高斯定律 $(F/m)\cdot A_{n-1}r^{n-1} = -A_{n-1}GM$ 得 $F = -GMmr^{1-n}$；积分得势能 $V(r) = \frac{GMm}{2-n}r^{2-n}$。故：
    \[
    \alpha = 1 - n, \qquad \beta = 2 - n.
    \]
  - **A2 ($n$ 维开普勒第二定律角动量指数)**：有心力场中运动平面固定，平面极坐标下角动量守恒 $L = mr^2\dot{\varphi}$，故：
    \[
    \lambda = 2.
    \]
  - **A3 (径向速度 $\dot{r}$)**：由机械能守恒 $E = \frac{1}{2}m\dot{r}^2 + \frac{L^2}{2mr^2} - \frac{GMm}{(n-2)r^{n-2}}$ 解得：
    \[
    \dot{r} = \pm\sqrt{\frac{2E}{m} + \frac{2GM}{(n-2)r^{n-2}} - \frac{L^2}{m^2 r^2}}.
    \]
  - **A4 (圆轨道的代数条件)**：圆轨道要求 $\dot{r} = 0$ 且 $\ddot{r} = 0$（向心力平衡）：
    \[
    \begin{cases}
    \dfrac{2E}{m} + \dfrac{2GM}{(n-2)r^{n-2}} - \dfrac{L^2}{m^2 r^2} = 0, \\[8pt]
    \dfrac{GM}{r^{n-1}} - \dfrac{L^2}{m^2 r^3} = 0.
    \end{cases}
    \]
  - **A5 ($n=4$ 时的轨道可能性)**：当 $n=4$ 时，圆轨道条件给出 $L^2 = GMm^2$ 且 $E = 0$。此时对于任意半径 $r$，根号内表达式 $\frac{2E}{m} + \frac{GM - L^2/m^2}{r^2} \equiv 0$ 恒成立，即对所有 $r$ 均有 $\dot{r} = 0$（随遇平衡圆轨道）。因此（1）形成椭圆轨道、（2）逃逸至 $r\to\infty$、（3）坠入 $r\to 0$ **全部不可能（All impossible）**。
  - **A6 ($n>4$ 时的轨道可能性与 $r$ 范围)**：
    - 当 $n>4$ 时，圆轨道条件意味着 $E > 0$。令 $x = 1/r^2$，要求 $\dot{r}^2 \ge 0$ 即 $\frac{2GM}{n-2}x^{(n-2)/2} \ge \frac{L^2}{m^2}x - \frac{2E}{m}$。
    - 由於左端幂函数（幂次 $\frac{n-2}{2} > 1$）是严格下凸函数，右端是直线，方程 $\frac{2E}{m} + \frac{2GM}{(n-2)r^{n-2}} - \frac{L^2}{m^2 r^2} = 0$ 最多有两个正根 $r_1 \le r_2$（在 $r_1 < r < r_2$ 区间内 $\dot{r}^2 < 0$ 为禁区；在严格圆轨道参数下两根重合 $r_1 = r_2 = r_0$）：
      - **(1) 形成椭圆轨道**：**不可能（Impossible）**（有效势只有极大值没有极小值势阱）。
      - **(2) 运动到 $r \to \infty$**：**可能（Possible）**，条件为 $r > r_2$（若在 $x=1/r^2$ 坐标下看则是较小根一侧，物理上对应大于外转折点半径 $r > r_2$ 的散射区）。
      - **(3) 运动到 $r \to 0$**：**可能（Possible）**，条件为 $0 < r < r_1$（小于内转折点半径的坍缩区）。
  - **B1 (四维与有效三维引力常数的关系)**：在 $r \gg C$ 处取高斯面为三维球面 $S^2(r)$ 与第四维小圆环 $S^1(C)$ 的直积柱面，其三维“超面积”为 $4\pi r^2 C$。由四维高斯定律（$A_3 = 2\pi^2$）：
    \[
    \left(\frac{F}{m}\right) 4\pi r^2 C = -2\pi^2 G_4 M \implies F = -\frac{\pi G_4 M m}{2 C r^2}.
    \]
    与三维牛顿引力 $F = -\frac{G_3 M m}{r^2}$ 对比，得：
    \[
    G_4 = \frac{2C}{\pi} G_3.
    \]
  - **B2 (降维后的三维有效质量 $m_{\text{eff}}$)**：将四维质能关系 $E^2 = (p_1^2 + p_2^2 + p_3^2 + p_4^2)c^2 + m^2 c^4$ 改写为三维形式 $E^2 = |\mathbf{p}_{\text{3D}}|^2 c^2 + m_{\text{eff}}^2 c^4$，得：
    \[
    m_{\text{eff}} = \sqrt{m^2 + \frac{p_4^2}{c^2}}.
    \]
  - **B3 (降维打击后行星的三维有效总能量)**：打击前在四维圆轨道上有 $\frac{L^2}{m r^3} = \frac{G_4 M m}{r^3} \implies E_K = \frac{L^2}{2mr^2} = \frac{G_4 M m}{2r^2} = \frac{C G_3 M m}{\pi r^2}$。打击方向垂直于轨道平面（$p_4 = 0 \implies m_{\text{eff}} = m$），动量与动能不变，而势能突变为三维引力势能 $-\frac{G_3 M m}{r}$。故三维有效总能量为：
    \[
    E_{\text{3D}} = -\frac{G_3 M m}{r} + \frac{C G_3 M m}{\pi r^2} \simeq -\frac{G_3 M m}{r} \quad (\text{因 }r \gg C).
    \]
  - **C1 (二维牛顿引力与势能)**：$n=2$ 时 $A_1 = 2\pi$，由高斯定律得：
    \[
    F = -\frac{GMm}{r}, \qquad V(r) = GMm\ln\left(\frac{r}{r_0}\right) \text{ 或 } GMm\ln r.
    \]
  - **C2 (二维圆轨道的代数条件)**：
    \[
    \begin{cases}
    \dfrac{2E}{m} - 2GM(\ln r + \text{const}) - \dfrac{L^2}{m^2 r^2} = 0, \\[8pt]
    \dfrac{GMm}{r} = \dfrac{L^2}{mr^3}.
    \end{cases}
    \]
  - **C3 (二维轨道的有界性讨论)**：
    - 由于 $r \to \infty$ 时对数势 $GMm\ln r \to +\infty$（势阱无穷深），且 $r \to 0$ 时离心势垒 $\frac{L^2}{2mr^2} \to +\infty$（圆轨道存在意味着 $L \neq 0$），因此任何有限能量 $E$ 下：
      - **(2) 运动到 $r \to \infty$**：**不可能（Impossible）**。
      - **(3) 运动到 $r \to 0$**：**不可能（Impossible）**。
      - **(1) 在有界区间 $0 < r_1 \le r \le r_2 < \infty$ 内运动**：一般情况下**可能（Possible）**；但若参数严格固定在圆轨道能量最小值处使得方程 $\frac{2E}{m} - 2GM(\ln r + \text{const}) - \frac{L^2}{m^2 r^2} = 0$ 的两根重合（$r_1 = r_2$），则不存在满足严格不等号 $r_1 < r_2$ 的非退化区间。
  - **D1 (圆锥时空双像条件与双像夹角)**：
    - 在展平的扇形（圆心角 $2\pi - \delta$）上，光线为不穿过顶点 M 的直线（弦）。从 P 到观测者 O 的两条绕行路径对 M 张角分别为 $\theta$ 与 $\tilde{\theta} = 2\pi - \delta - \theta$。
    - 两条弦均存在（不穿过顶点 M）当且仅当两个圆心角均小于 $\pi$：
      \[
      \begin{cases}
      0 < \theta < \pi, \\
      0 < 2\pi - \delta - \theta < \pi,
      \end{cases}
      \implies \pi - \delta < \theta < \pi.
      \]
    - 在两个等腰三角形 $\triangle\text{MPO}$ 中，两虚线与 MO 连线的夹角分别为 $\alpha_1 = \frac{\pi - \theta}{2}$ 和 $\alpha_2 = \frac{\pi - \tilde{\theta}}{2}$，故双像间的夹角为：
      \[
      \alpha_1 + \alpha_2 = \frac{2\pi - (\theta + \tilde{\theta})}{2} = \frac{\delta}{2}.
      \]
  - **D2 (观测者 P 与 Q 相遇时间 $t_m$)**：
    - 转换到以质点 M 为静止参考系的展平平面，并将亏损角 $\delta$ 的剪口置于 M 运动方向的后方（即朝向 PQ 的一侧剪去半角为 $\delta/2$ 的对称楔形）。
    - 在该平面上，P 与 Q 沿平行于对称轴的水平直线以速率 $v$ 向 M 运动，直至同时撞上剪口的两条粘合边（与对称轴夹角为 $\delta/2$，距 M 的垂直距离为 $d$，水平距离为 $d\cot\frac{\delta}{2}$）。故总位移为 $s + d\cot\frac{\delta}{2}$，相遇时间为：
      \[
      t_m = \frac{s + d\cot(\delta/2)}{v}.
      \]
  - **D3 (相遇前 Q 听到的声波频率 $f_r$)**：
    - 在 M（及声波介质）静止系中，把粘合边两侧的平面拼合展开：P 与 Q 沿夹角为 $\delta$ 的两条汇合直线以速率 $v$ 冲向交点（相遇点 A）。
    - 设在时刻 $t$，P、Q 距相遇点 A 的距离为 $L(t) = v(t_m - t)$。P 在时刻 $t_e$ 发射的声波在时刻 $t_r$ 被 Q 接收，在三角形 $\triangle\text{APQ}$ 中由余弦定理：
      \[
      L^2(t_e) + L^2(t_r) - 2L(t_e)L(t_r)\cos\delta = c_s^2(t_r - t_e)^2 = \frac{c_s^2}{v^2}\left[L(t_e) - L(t_r)\right]^2.
      \]
    - 设比值 $\kappa = \frac{L(t_e)}{L(t_r)} = \frac{t_m - t_e}{t_m - t_r} > 1$，整理得：
      \[
      \frac{\kappa^2 + 1 - 2\kappa\cos\delta}{(\kappa - 1)^2} = \frac{c_s^2}{v^2} \iff \frac{\kappa + \kappa^{-1} - 2\cos\delta}{\kappa + \kappa^{-1} - 2} = \frac{c_s^2}{v^2} \iff \frac{\kappa + \kappa^{-1}}{2} = \frac{c_s^2 - v^2\cos\delta}{c_s^2 - v^2} = \frac{13}{12}.
      \]
    - 解得 $\kappa = \frac{3}{2}$（舍去 $<1$ 的根 $\frac{2}{3}$），故 $L(t_e) = \frac{3}{2}L(t_r)$，接收频率为：
      \[
      f_r = \frac{\delta t_e}{\delta t_r} f = \frac{\delta L(t_e)}{\delta L(t_r)} f = \frac{3}{2} f.
      \]
  - **D4 (Q 开始听到频率 $f_r$ 的起始时刻 $t$)**：
    - 要使声波经历亏损角折叠后的此多普勒频移，连接发射点 B（$AB = L(t_e) = \frac{3}{2}L(t_r)$）与接收点 C（$AC = L(t_r)$）的声线必须穿过粘合线 AD 上位于 M 左侧（即点 A 与点 M 之间）的线段！
    - 临界情形为声线 BC 恰好经过质点 M（即点 D 与 M 重合，$AD = d\csc\frac{\delta}{2}$，且 AD 平分 $\angle\text{BAC} = \delta$）。
    - 利用面积割补法：$S_{\triangle\text{ABC}} = S_{\triangle\text{ABD}} + S_{\triangle\text{ACD}}$：
      \[
      \frac{1}{2}\left(\frac{3}{2}L(t_r)\right) L(t_r)\sin\delta = \frac{1}{2}\left(\frac{3}{2}L(t_r)\right)\left(d\csc\frac{\delta}{2}\right)\sin\frac{\delta}{2} + \frac{1}{2}L(t_r)\left(d\csc\frac{\delta}{2}\right)\sin\frac{\delta}{2}.
      \]
    - 化简得 $\frac{3}{4}L(t_r)\sin\delta = \frac{5}{4}d \implies L(t_r) = \frac{5d}{3\sin\delta}$。代入 $L(t_r) = v(t_m - t)$ 得起始时刻：
      \[
      t = t_m - \frac{L(t_r)}{v} = \frac{s + d\cot(\delta/2)}{v} - \frac{5d}{3v\sin\delta}.
      \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：
  1. **D3 与 D4 的几何化简高度吻合**：我们在盲解中通过自相似比例因子 $\kappa = \frac{t_m - t_e}{t_m - t_r} = \frac{L(t_e)}{L(t_r)}$ 将二维非共线多普勒效应直接转化为余弦定理二次方程 $\frac{1}{2}(\kappa + \kappa^{-1}) = \frac{13}{12} \implies \kappa = \frac{3}{2}$，与官方解答的“Alternative approach（波周期数守恒法）”完全一致，省去了对隐函数求微商的繁琐代数！在 D4 中，面积法 $S_{\triangle\text{ABC}} = S_{\triangle\text{ABD}} + S_{\triangle\text{ACD}}$ 仅用两行就解出了角平分线截距 $L(t_r) = \frac{5d}{3\sin\delta}$，远比辅助线余弦定理法直观。
  2. **A6 中 $r$ 与 $x = 1/r^2$ 的坐标方向辨析**：官方解答第 17 页在引入 $x = 1/r^2$ 作图时，将横轴左根记为 $r_1$、右根记为 $r_2$，但忘了 $x = 1/r^2$ 与 $r$ 是**反序**的（小 $x$ 对应大 $r \to \infty$，大 $x$ 对应小 $r \to 0$），因此官方解答文字中写的“(2) $r < r_1$，(3) $r > r_2$”实际上是针对变量 $x$ 的方向写的；若按半径 $r$ 排序（$0 < r_1 \le r_2 < \infty$），逃逸至 $r \to \infty$ 对应大半径区 $r > r_2$，坠入 $r \to 0$ 对应小半径区 $r < r_1$。我们在教学中需特别为学生澄清这一反演映射细节。
- **核心难点与易错点**：
  1. **B1 高维高斯定律中的单位球面积系数 $A_{n-1}$**：题干特意定义了 $n$ 维高斯通量为 $-A_{n-1}GM$（使得球对称下 $A_{n-1}$ 恰好约消）。但在 B1 降维打击中，四维空间的高斯面不再是三维球面 $S^3$（面积 $2\pi^2 r^3$），而是柱面 $S^2(r) \times S^1(C)$（面积 $4\pi r^2 C$），此时左端为 $4\pi r^2 C$、右端为 $-2\pi^2 G_4 M$，系数不再相等！若不理解高斯定律的几何面积本质，就会漏掉 $\frac{2}{\pi}$ 因子。
  2. **D3 声波介质参考系陷阱**：题目明确指出“声波的传播介质跟随质点 M 运动（即与 M 相对静止）”。若学生误把相遇点 A（或实验室系）当作介质静止系，直接套用一维多普勒公式 $f_r = \frac{c_s + v\sin(\delta/2)}{c_s - v\sin(\delta/2)}f$，则会因为忽略了介质沿角平分线方向的迎面漂移速度 $v\cos(\delta/2)$ 而扣掉一半分数（最多得 2/4 分）。
