# Batch 06: 泛珠三角物理奥林匹克综合试二 (PanPhO Paper 2, 2023–2026) 盲解与教学拆解全记录

本报告严格遵循两阶段协议（**Phase 1: 独立盲解** $\to$ **Phase 2: 对照官方参考解答与教学深度拆解**），涵盖 2023–2026 年泛珠三角物理奥林匹克竞赛（PanPhO）综合试二全部 8 道长题。

---

## 1. `panpho-2023-paper-2-problem-slice-q1` — 真空泡泡 (Vacuum Bubbles)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：经典相对论标量场 $\phi(t,x,y,z)$ 的 Klein-Gordon 型非线性场方程、一维拓扑孤子（畴壁 Domain Wall）、薄壁近似（Thin-wall approximation）下的三维球对称假真空衰变泡泡动力学，以及虚时间旋转（Wick 转动 $\tau = it$）下四维欧氏空间 $O(4)$ 对称瞬子（Coleman Bounce）与隧穿成核率计算（Sidney Coleman, *Phys. Rev. D* **15**, 2929 (1977)）。
- **分步独立推导**：
  - **A1 (化简畴壁方程)**：在静态 ($\partial_t \phi = 0$) 且沿 $y, z$ 方向均匀 ($\partial_y \phi = \partial_z \phi = 0$) 条件下，对称双阱势 $V(\phi) = V_D(\phi)$ 下的运动方程化简为常微分方程：
    \[
    \frac{d^2 \phi}{dx^2} = \frac{dV_D(\phi)}{d\phi}.
    \]
  - **A2 (畴壁剖面)**：方程两边同乘 $\frac{d\phi}{dx}$ 并对 $x$ 积分（等价于将 $x$ 视为时间、在反号势 $-V_D(\phi)$ 中的一维粒子机械能守恒）：
    \[
    \frac{1}{2}\left(\frac{d\phi}{dx}\right)^2 - V_D(\phi) = C.
    \]
    利用无穷远处边界条件 $x \to \pm\infty$ 时 $\phi \to \phi_\pm$、$\frac{d\phi}{dx} \to 0$ 且 $V_D(\phi_\pm) = 0$，得积分常数 $C = 0$，故：
    \[
    \frac{d\phi}{dx} = \pm\sqrt{2V_D(\phi)} \quad \text{或} \quad \left(\frac{d\phi}{dx}\right)^2 = 2V_D(\phi).
    \]
  - **A3 (畴壁张力)**：单位 $y$-$z$ 面积上的畴壁能量（表面张力 $\sigma$）为：
    \[
    \sigma = \int_{-\infty}^{+\infty} \left[\frac{1}{2}\left(\frac{d\phi}{dx}\right)^2 + V_D(\phi)\right] dx = \int_{-\infty}^{+\infty} 2V_D(\phi)\,dx = \int_{\phi_-}^{\phi_+} \sqrt{2V_D(\phi)}\,d\phi,
    \]
    从而被积函数为 $f(\phi) = \sqrt{2V_D(\phi)}$。
  - **B1 (泡泡壁静止能量)**：成核瞬间泡泡静止且半径为 $R$，薄壁近似下壁面携带的能量为球面积乘表面张力：
    \[
    E_W = 4\pi R^2 \sigma.
    \]
  - **B2 (真假真空能密差 $\epsilon$)**：微扰非对称势 $V(\phi) = V_D(\phi) + \frac{\epsilon}{\phi_+ - \phi_-}(\phi - \phi_+)$ 在假真空 $\phi_+$ 处取 $V(\phi_+) = 0$；在真真空 $\phi_-$ 附近极小值点偏移量为 $O(\epsilon)$，由于 $V'_D(\phi_-) = 0$，极小值点偏移对势能的修正为 $O(\epsilon^2)$，故在 $\epsilon$ 的领头阶下泡泡内部能密为 $V(\phi_-) \approx -\epsilon$。由成核瞬间总能量与均匀假真空相同（$E_{\text{tot}} = 0$，无辐射与耗散）：
    \[
    E_{\text{tot}} = 4\pi R^2 \sigma - \frac{4}{3}\pi R^3 \epsilon = 0 \implies \epsilon = \frac{3\sigma}{R}.
    \]
  - **B3 (成核瞬间的加速度)**：当泡泡半径由 $R$ 膨胀至 $r$ 时，静态势能为 $U_{\text{eff}}(r) = 4\pi r^2 \sigma - \frac{4}{3}\pi r^3 \epsilon$。在 $r = R$ 处（将 $\epsilon = 3\sigma/R$ 代入），径向广义力为：
    \[
    F_r = -\left.\frac{dU_{\text{eff}}}{dr}\right|_{r=R} = 4\pi R^2 \epsilon - 8\pi R \sigma = 12\pi R\sigma - 8\pi R\sigma = 4\pi R\sigma.
    \]
    在自然单位制 $c = 1$ 下，成核瞬间泡泡壁的静止质量为 $m = E_W = 4\pi R^2 \sigma$，故初始加速度为：
    \[
    a = \frac{F_r}{E_W} = \frac{4\pi R\sigma}{4\pi R^2 \sigma} = \frac{1}{R}.
    \]
  - **B4 (相对论膨胀与速度达到 $0.6$ 所需时间)**：当半径为 $r(t)$、壁速为 $v = \dot{r}$ 时，运动泡泡壁的能量（静止能量加动能）为 $E_{\text{wall}}(r) = \gamma (4\pi r^2 \sigma)$，其中 $\gamma = \frac{1}{\sqrt{1-v^2}}$。由总能量守恒 $\gamma (4\pi r^2 \sigma) = \frac{4}{3}\pi r^3 \epsilon$ 并代入 $\epsilon = \frac{3\sigma}{R}$，立得极其优美的几何关系：
    \[
    \gamma = \frac{1}{\sqrt{1 - \dot{r}^2}} = \frac{r}{R} \implies \dot{r} = \frac{\sqrt{r^2 - R^2}}{r}.
    \]
    分离变量积分（利用提示 $\frac{d\sqrt{x^2-1}}{dx} = \frac{x}{\sqrt{x^2-1}}$，其中 $x = \gamma = r/R$）：
    \[
    dt = \frac{r\,dr}{\sqrt{r^2 - R^2}} = d\sqrt{r^2 - R^2} \implies r^2 - R^2 = t^2, \quad t = R\sqrt{\gamma^2 - 1}.
    \]
    当 $v = 0.6$ 时，$\gamma = \frac{1}{\sqrt{1-0.6^2}} = \frac{5}{4}$，故：
    \[
    t = R\sqrt{\left(\frac{5}{4}\right)^2 - 1} = \frac{3}{4}R = 0.75 R.
    \]
  - **C1 (四维欧氏拉普拉斯算符径向方程)**：对四维球对称函数 $\phi(\rho)$（其中 $\rho = \sqrt{\tau^2 + x^2 + y^2 + z^2}$），四维拉普拉斯算符为 $\nabla_4^2 \phi = \frac{1}{\rho^3}\frac{d}{d\rho}\left(\rho^3 \frac{d\phi}{d\rho}\right) = \frac{d^2\phi}{d\rho^2} + \frac{3}{\rho}\frac{d\phi}{d\rho}$（或按提示代入 $\phi = \rho^2$，左边 $\partial_\tau^2\phi + \partial_x^2\phi + \partial_y^2\phi + \partial_z^2\phi = 8 = 2 + 2\rho f(\rho)$），得：
    \[
    f(\rho) = \frac{3}{\rho}.
    \]
  - **C2 (欧氏作用量径向积分)**：利用四维半径为 $\rho$ 的三维球面面积 $2\pi^2 \rho^3$，得：
    \[
    S_E = 2\pi^2 \int_0^\infty \rho^3 \left[\frac{1}{2}\left(\frac{d\phi}{d\rho}\right)^2 + V(\phi)\right] d\rho.
    \]
  - **C3 (Coleman 粒子类比定性分析)**：欧氏方程 $\frac{d^2\phi}{d\rho^2} + \frac{3}{\rho}\frac{d\phi}{d\rho} = \frac{dV}{d\phi}$ 类比为粒子坐标 $\phi$ 随有效时间 $\rho$ 的运动：
    - **C3-1**：$\frac{3}{\rho}\frac{d\phi}{d\rho}$ 移至右端为 $-\frac{3}{\rho}\frac{d\phi}{d\rho}$，始终阻碍速度 $\frac{d\phi}{d\rho}$，故为**阻力 (A)**。
    - **C3-2**：右端驱动力为 $+dV/d\phi$（在翻转势 $U_{\text{eff}} = -V(\phi)$ 中下滑），故选 **(C)**。
    - **C3-3**：为使粒子克服摩擦在 $\rho \to \infty$ 时恰好停在较低的峰值 $-V(\phi_+) = 0$，在 $\rho = 0$ 时必须从真真空峰顶 $\phi_-$ 朝 $\phi_+$ 方向偏移无穷小量出发，即 $\phi_- + |O(\delta)|$，故选 **(C)**。
    - **C3-4**：在 $\rho \to \infty$ 时场必须精确回到假真空态以保证欧氏作用量有限，即 $\phi_+$，故选 **(E)**。
  - **C4 (薄壁近似下的欧氏作用量 $S_E$)**：将积分拆分为四维球壳壁 ($\rho \approx R$) 与四维球内部 ($\rho < R$) 两部分：
    \[
    S_E = 2\pi^2 R^3 \sigma + \frac{\pi^2}{2}R^4 (-\epsilon) = 2\pi^2 R^3 \sigma - \frac{\pi^2}{2}R^4 \left(\frac{3\sigma}{R}\right) = \frac{1}{2}\pi^2 R^3 \sigma.
    \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解的所有结果与官方解答完全一致。官方解答在 B4 中特别指出，实时间双曲线轨迹 $r^2 - t^2 = R^2$ 正是四维欧氏空间球面 $\rho^2 = \tau^2 + r^2 = R^2$ 在 $\tau = it$ 解析延拓下的直接体现。
- **核心难点与易错点**：
  1. **B3 泡泡初始加速度的“表面张力内缩项”遗漏陷阱**：若学生误将泡泡壁质量 $4\pi R^2\sigma$ 当作不随半径变化的常量，只对内部体积释放的真空能 $\frac{4}{3}\pi r^3\epsilon$ 求导，会得出错误推力 $4\pi R^2\epsilon = 12\pi R\sigma$ 及错误加速度 $a = 3/R$。正确做法必须同时考虑壁面积增大消耗的表面能 $-d(4\pi r^2\sigma)/dr = -8\pi R\sigma$，净驱动力为 $4\pi R\sigma$，故 $a = 1/R$。
  2. **C3 翻转势 (Inverted Potential) 符号与边界陷阱**：Wick 转动 $\tau = it$ 使时间二阶导数变号，从而有效势变为 $-V(\phi)$，原来的势能极小值点变为山峰；且 $\rho = 0$ 处若精确位于 $\phi_-$ 则受合力为零无法滚落，必须位于偏离 $\phi_-$ 朝向 $\phi_+$ 的 $\phi_- + |O(\delta)|$ 处。

---

## 2. `panpho-2023-paper-2-problem-slice-q2` — 洛伦兹互易性 (Lorentz Reciprocity)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：静磁学洛伦兹互易定理的矢量分析证明、运动导体中动生洛伦兹力 $\sigma(\mathbf{v}\times\mathbf{B})$ 对互易性的破坏机制、相对论电磁场洛伦兹变换，以及有限电导率运动金属板上方磁偶极子的广义镜像法（混合磁偶极与电偶极镜像）与非互易品质因数 $\mathcal{R}$（J. Prat-Camps *et al.*, *Phys. Rev. Lett.* **121**, 213903 (2018)）。
- **分步独立推导**：
  - **A1 (证明静磁互易关系)**：利用恒等式 $\nabla \cdot (\mathbf{H}_1 \times \mathbf{A}_2 - \mathbf{H}_2 \times \mathbf{A}_1) = \mathbf{J}_1 \cdot \mathbf{A}_2 - \mathbf{H}_1 \cdot \mathbf{B}_2 - \mathbf{J}_2 \cdot \mathbf{A}_1 + \mathbf{H}_2 \cdot \mathbf{B}_1$。因各向同性磁导率 $\mathbf{B}_i = \mu(\mathbf{r})\mathbf{H}_i$，有 $\mathbf{H}_1 \cdot \mathbf{B}_2 = \mu \mathbf{H}_1 \cdot \mathbf{H}_2 = \mathbf{H}_2 \cdot \mathbf{B}_1$。对全空间积分并利用无穷远处边界面积分以 $O(r^{-3})$ 趋于零，得 $\int \mathbf{J}_1 \cdot \mathbf{A}_2\,dV = \int \mathbf{J}_2 \cdot \mathbf{A}_1\,dV$。代入 $\mathbf{J}_i = \nabla \times \mathbf{M}_i$ 并分部积分：
    \[
    \int \mathbf{M}_1 \cdot (\nabla \times \mathbf{A}_2)\,dV = \int \mathbf{M}_2 \cdot (\nabla \times \mathbf{A}_1)\,dV \implies \mathbf{m}_1 \cdot \mathbf{B}_2(\mathbf{r}_1) = \mathbf{m}_2 \cdot \mathbf{B}_1(\mathbf{r}_2).
    \]
  - **A2 (运动导体破坏互易性的体积分)**：当 $\nabla \times \mathbf{H}_i = \mathbf{J}_i + \sigma(\mathbf{E}_i + \mathbf{v}\times\mathbf{B}_i)$ 时，静磁情形下 $\nabla\times\mathbf{E}_i = 0$ 使 $\int \sigma(\mathbf{E}_1\cdot\mathbf{A}_2 - \mathbf{E}_2\cdot\mathbf{A}_1)\,dV = 0$，余下的动生项给出：
    \[
    \mathbf{m}_1 \cdot \mathbf{B}_2(\mathbf{r}_1) - \mathbf{m}_2 \cdot \mathbf{B}_1(\mathbf{r}_2) = \int \sigma \mathbf{v} \cdot \left[\mathbf{A}_2 \times (\nabla \times \mathbf{A}_1) - \mathbf{A}_1 \times (\nabla \times \mathbf{A}_2)\right] dV.
    \]
  - **B1 (自由空间运动参考系中的偶极磁场)**：实验室系中位于 $(0,0,z_0)$ 的偶极子 $\mathbf{m} = m_x\hat{x}$ 产生静磁场 $\mathbf{B}(x,y,z)$ 且 $\mathbf{E} = 0$。将逆洛伦兹变换 $x = \gamma(x' + vt')$, $y = y'$, $z = z'$ 代入，并由场变换 $B'_x = B_x, B'_y = \gamma B_y, B'_z = \gamma B_z$ 得：
    \[
    \mathbf{B}'(x',y',z',t') = \frac{\mu_0 m_x}{4\pi\left[\gamma^2(x'+vt')^2 + y'^2 + (z'-z_0)^2\right]^{5/2}} \begin{pmatrix} 2\gamma^2(x'+vt')^2 - y'^2 - (z'-z_0)^2 \\ 3\gamma^2(x'+vt')y' \\ 3\gamma^2(x'+vt')(z'-z_0) \end{pmatrix}.
    \]
  - **B2 & B3 (运动理想导体上的镜像法与表面场)**：在实验室系 $(0,0,-z_0)$ 处放置理想导体镜像偶极子（对 $\mathbf{m} = m_x\hat{x}$ 取镜像 $+m_x\hat{x}$；对 $\mathbf{m} = m_z\hat{z}$ 取镜像 $-m_z\hat{z}$）。在 $z = 0^+$ 表面上，实验室系中 $B_z(x,y,0^+) = 0$ 且 $\mathbf{E} = 0$；变换到随导体静止的参考系后，$B'_z(x',y',0^+,t') = \gamma B_z = 0$（且切向电场 $E'_x = E'_y = 0$），严格满足理想导体边界条件！故实验室系表面磁场分别为：
    - B2 ($\mathbf{m} = m_x\hat{x}$)：
      \[
      \mathbf{B}(x,y,0^+) = \frac{\mu_0 m_x}{2\pi(x^2+y^2+z_0^2)^{5/2}} \begin{pmatrix} 2x^2 - y^2 - z_0^2 \\ 3xy \\ 0 \end{pmatrix}.
      \]
    - B3 ($\mathbf{m} = m_z\hat{z}$)：
      \[
      \mathbf{B}(x,y,0^+) = -\frac{3\mu_0 m_z z_0}{2\pi(x^2+y^2+z_0^2)^{5/2}} \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}.
      \]
  - **B4 (运动理想导体上的互易品质因数 $\mathcal{R}$)**：由于理想导体完全排斥磁场（内部 $\mathbf{A}_i = 0$），导体运动完全不改变外部磁场分布，两类构型下均有 $B_z(\delta) = B_z(-\delta)$ 及 $B_{1z}(\delta) = B_{2x}(-\delta) = \frac{6\mu_0 m \delta z_0}{4\pi(\delta^2+4z_0^2)^{5/2}}$，故：
    \[
    \mathcal{R} = 0.
    \]
  - **C1 (广义镜像法下的表面电磁场)**：在 $(0,0,-z_0)$ 处放置镜像磁偶极子 $m_x^{(r)}\hat{x} + m_z^{(r)}\hat{z}$ 与镜像电偶极子 $p_y^{(r)}\hat{y}$。叠加实验室系场并作洛伦兹变换，在 $z=0^+$ 处（记 $R_0 = \sqrt{x^2+y^2+z_0^2}$）：
    \[
    \mathbf{B}'(0^+) = \frac{\mu_0}{4\pi R_0^5} \begin{pmatrix} 3xz_0(m_z^{(r)} - m_z) + (2x^2 - y^2 - z_0^2)m_x^{(r)} \\ 3yz_0\gamma(m_z^{(r)} - m_z + v p_y^{(r)}) + 3xy\gamma m_x^{(r)} \\ (2z_0^2 - x^2 - y^2)\gamma(m_z^{(r)} + m_z) + 3xz_0\gamma m_x^{(r)} - (2y^2 - x^2 - z_0^2)v\gamma p_y^{(r)} \end{pmatrix},
    \]
    \[
    \mathbf{E}'(0^+) = \frac{\mu_0}{4\pi R_0^5} \begin{pmatrix} 3xy c^2 p_y^{(r)} \\ (2y^2 - x^2 - z_0^2)\gamma c^2 p_y^{(r)} - v\gamma(2z_0^2 - x^2 - y^2)(m_z^{(r)} + m_z) - 3xz_0 v\gamma m_x^{(r)} \\ 3y\gamma\left[z_0 c^2 p_y^{(r)} + z_0 v(m_z^{(r)} - m_z) + x v m_x^{(r)}\right] \end{pmatrix}.
    \]
  - **C2 (求解镜像偶极矩)**：由移动参考系中趋肤层表面电流边界条件 $\mathbf{J}'_s = d\sigma\mathbf{E}'_{\parallel} = \hat{z}\times\mathbf{B}'/\mu_0$ 的主导 $y$ 分量 $B'_x(0^+) = \mu_0 d\sigma E'_y(0^+)$，利用平面 $z=0$ 上三个二次型 $(2x^2-y^2-z_0^2) + (2y^2-x^2-z_0^2) + (2z_0^2-x^2-y^2) \equiv 0$ 的线性相关性，对比 $x^2, y^2$（或 $z_0^2$）与 $xz_0$ 项系数（记无量纲参数 $\kappa = \mu_0 v\gamma\sigma d \gg 1$），解得：
    \[
    \frac{m_x^{(r)}}{m_z} = \frac{2\kappa}{1+\kappa^2} \simeq \frac{2}{\kappa}, \qquad \frac{m_z^{(r)}}{m_z} = \frac{1-\kappa^2}{1+\kappa^2} \simeq -1 + \frac{2}{\kappa^2}, \qquad \frac{p_y^{(r)}}{m_z} = -\frac{v}{c^2}\frac{2}{1+\kappa^2} \simeq -\frac{2v}{c^2\kappa^2}.
    \]
  - **C3 (有限电导率运动导体的非互易品质因数 $\mathcal{R}$)**：在 $z = z_0$ 高度处，$m_x^{(r)}$ 产生关于 $x$ 奇对称的附加磁场 $\Delta B_z(x,0,z_0) = \frac{\mu_0 m_x^{(r)}}{4\pi(x^2+4z_0^2)^{5/2}}(6xz_0)$，代入 $\mathcal{R}$ 定义得：
    \[
    \mathcal{R} \simeq -\operatorname{sign}(\delta)\frac{12|\delta/z_0|^4}{\kappa\left[(4+|\delta/z_0|^2)^{5/2} + (8-|\delta/z_0|^2)|\delta/z_0|^3\right]}.
    \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解与官方参考解答在全部推导与系数比较上完全吻合。在 C2 中，通过拉普拉斯方程谐和多项式恒等式 $(2x^2-y^2-z_0^2) + (2y^2-x^2-z_0^2) + (2z_0^2-x^2-y^2) \equiv 0$ 可以清楚解释为什么表面上看似有 $x^2, y^2, z_0^2, xz_0$ 四组空间函数，却恰好只给出 3 个线性独立方程来唯一确定 $(m_x^{(r)}, m_z^{(r)}, p_y^{(r)})$。
- **核心难点与易错点**：
  1. **为什么理想导体运动不破坏互易性（B4）？** 许多学生直觉认为只要导体运动就会破坏时间反演对称性并产生非互易信号。但理想导体（$\sigma \to \infty$）内部磁场严格为零，磁力线无法穿透导体因而不会受到运动介质的“磁流体拖拽”（对应 A2 体积分被积区域内 $\mathbf{A}_i = 0$）；只有有限电导率导体允许磁场渗透进趋肤深度 $d$，才会产生拖拽偏转偶极矩 $m_x^{(r)} \simeq \frac{2}{\kappa}m_z$。
  2. **表面电流边界条件 $\hat{z}\times\mathbf{B}' = \mu_0 \mathbf{J}'_s$ 的叉乘方向**：右手系中 $(\hat{z}\times\mathbf{B}')_y = +B'_x$，极易在安培环路积分中弄反符号导致 $m_x^{(r)}$ 差一个负号。

---

## 3. `panpho-2024-paper-2-problem-slice-q1` — 时空变介电常数 / 引力波测量中的误差估计 (TianQin Gravitational Wave Error Estimates)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **重要题干说明**：原题 PDF 切片标题栏保留了 2022 年卷二第 1 题的旧标题 `Problem 1: Spatiotemporal varying electric permittivity / 问题 1: 时空变介电常数`，但正文实际为 **天琴计划空间引力波探测中的误差估计（卫星轨道地球非球形引力摄动、太阳风自由电子等离子体相位色散误差、激光散粒噪声与衍射受限发射功率估计）**。
- **分步独立推导**：
  - **A1 (卫星圆轨道周期)**：由开普勒第三定律，在 $R = 10^8\,\text{m}$ 处：
    \[
    T = 2\pi\sqrt{\frac{R^3}{GM}} = 2\pi\sqrt{\frac{(10^8)^3}{6.67\times 10^{-11}\times 5.97\times 10^{24}}} \approx 3.15\times 10^5\,\text{s}.
    \]
  - **A2 (地球非均匀质量模型的附加加速度 $\delta\mathbf{a}$)**：设球心处质量为 $M-2m$，赤道对径点 $(\pm r\cos\theta, \pm r\sin\theta)$ 处各有一质量 $m$，卫星位于 $(R,0)$。扣除均匀球体加速度 $-\frac{GM}{R^2}\hat{x}$ 后，附加加速度分量为：
    \[
    \delta a_x = Gm\left[\frac{2}{R^2} - \frac{R - r\cos\theta}{(R^2+r^2-2Rr\cos\theta)^{3/2}} - \frac{R + r\cos\theta}{(R^2+r^2+2Rr\cos\theta)^{3/2}}\right],
    \]
    \[
    \delta a_y = Gm\left[\frac{r\sin\theta}{(R^2+r^2-2Rr\cos\theta)^{3/2}} - \frac{r\sin\theta}{(R^2+r^2+2Rr\cos\theta)^{3/2}}\right].
    \]
  - **A3 ($\delta a$ 随时间变化的周期)**：因对径点质量分布具有 $\theta \to \theta + \pi$ 对称性（$\cos\theta \leftrightarrow -\cos\theta$），$\delta a$ 关于 $\theta$ 的基本周期为 $\pi$（对应旋转 $2\pi$ 周期的一半）。考虑地球自转周期 $T_E = 86400\,\text{s}$ 与卫星公转周期 $T = 3.15\times 10^5\,\text{s}$ 同向（co-rotate）或反向（counter-rotate）两种情形：
    \[
    T_{\text{co}} = \frac{1/2}{\frac{1}{T_E} - \frac{1}{T}} \approx 5.95\times 10^4\,\text{s}, \qquad T_{\text{counter}} = \frac{1/2}{\frac{1}{T_E} + \frac{1}{T}} \approx 3.39\times 10^4\,\text{s}.
    \]
  - **A4 ($R \gg r$ 极限下的领头阶泰勒展开)**：一阶偶极项 $O(r/R)$ 因对径对称完全抵消，领头阶为二阶四极矩项 $O(r^2/R^4)$：
    \[
    \delta a_x \simeq \frac{3Gm r^2(1 - 3\cos^2\theta)}{R^4}, \qquad \delta a_y \simeq \frac{3Gm r^2\sin 2\theta}{R^4}.
    \]
  - **A5 ($\delta a$ 的典型量级估计)**：地球扁率或海陆密度差对应的非球形质量约 $m \sim (10^{-4}\text{--}10^{-3})M \sim 10^{20}\text{--}10^{21}\,\text{kg}$，代入得 $\delta a \sim 10^{-9}\text{--}10^{-7}\,\text{m/s}^2$。
  - **A6 (周期最接近 $1000\,\text{s}$ 的高阶多极分量比值)**：同向旋转时 $2\pi$ 相对转动周期为 $T_{2\pi} = 2T_{\text{co}} \approx 1.191\times 10^5\,\text{s}$。泰勒展开中 $(\cos\theta)^n$ 项包含 $\cos(n\theta)$ 谐波，周期为 $T_{2\pi}/n$。令 $T_{2\pi}/n \approx 1000\,\text{s}$ 且 $n$ 为偶数，得 $n = 120$（或 $118$）。在 $\theta = \pi/3$（$\cos\theta = 1/2$）处，二项式系数被 $(1/2)^n$ 抵消，故：
    \[
    \frac{\delta a_{1000}}{\delta a} \sim \left(\frac{r}{R}\right)^{n-2} \sim (0.0637)^{118} \sim 10^{-141}\text{ (或 }10^{-139}\text{)}.
    \]
  - **B1 & B2 (太阳风自由电子响应)**：电子加速度 $\frac{d\mathbf{v}_e}{dt} = -\frac{e\mathbf{E}}{m_e}$，电流密度变化率 $\frac{d\mathbf{J}}{dt} = -N_e e\frac{d\mathbf{v}_e}{dt} = \frac{N_e e^2}{m_e}\mathbf{E}$。
  - **B3 (激光在电子等离子体中的相速度)**：代入波动方程得色散关系 $\omega^2 = c^2 k^2 + \frac{c^2\mu_0 N_e e^2}{m_e}$，故相速度为：
    \[
    v_p = \frac{\omega}{k} \simeq c\left(1 + \frac{\mu_0 N_e e^2 c^2}{2m_e \omega^2}\right) = c\left(1 + \frac{\mu_0 N_e e^2 \lambda^2}{8\pi^2 m_e}\right).
    \]
  - **B4 (两卫星间的激光相位误差 $\delta\theta$)**：三颗卫星构成内接于半径 $R = 10^8\,\text{m}$ 圆轨道的等边三角形，星间距离为 $L = \sqrt{3}R$。自由电子引起的波数偏移 $\Delta k = k - \frac{\omega}{c} = -\frac{\mu_0 N_e e^2\lambda}{4\pi m_e}$，故相位误差为：
    \[
    \delta\theta = \Delta k \cdot \sqrt{3}R = -\frac{\sqrt{3}\mu_0 N_e e^2 \lambda R}{4\pi m_e} \approx -5.19\times 10^{-6}\,\text{rad}.
    \]
  - **C1 (散粒噪声指数)**：独立光子到达服从泊松分布，标准差 $\Delta N = \sqrt{N} = N^{1/2}$，故 $\alpha = 1/2$。
  - **C2 (最低接收功率 $P_{\text{rec}}$)**：由 $\frac{\Delta N}{N} = N^{-1/2} < 3\times 10^{-6}$ 得每秒最少光子数 $N = 1.11\times 10^{11}\,\text{s}^{-1}$，单光子能量 $E_{\text{ph}} = \frac{hc}{\lambda} = 1.87\times 10^{-19}\,\text{J}$，故：
    \[
    P_{\text{rec}} = N\frac{hc}{\lambda} \approx 2.07\times 10^{-8}\,\text{W}.
    \]
  - **C3 (最低发射功率 $P_{\text{emit}}$)**：发射端光学孔径 $D = 0.1\,\text{m}$ 产生衍射发散角 $\theta_d \sim \frac{\lambda}{D}$，传播距离 $L \sim R$（或 $\sqrt{3}R$）后光斑半径为 $w \sim \frac{\lambda L}{D} \sim 10^3\,\text{m}$，接收口径 $D$ 截获的功率比为 $\frac{P_{\text{rec}}}{P_{\text{emit}}} \sim \left(\frac{D^2}{\lambda L}\right)^2 \sim (5\text{--}9)\times 10^{-9}$，故最低发射功率为：
    \[
    P_{\text{emit}} \sim 2\text{--}7\,\text{W}.
    \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **官方文件标题错配说明与对照分析**：
  1. **官方文件标题错配考证**：2024 年综合试二原题 PDF (`panpho-2024-paper-2-problem-slice-q1`) 第 2 页顶部误印了 2022 年卷二第 1 题的标题 `Problem 1: Spatiotemporal varying electric permittivity (30 points) 问题 1: 时空变介电常数 (30 分)`；而在 2024 年官方参考解答 PDF (`panpho-2024-paper-2-solution-slice-q1`) 第 1 页中，命题组已将该标题修正为 `Problem 1: Error estimates of a gravitational wave experiment (30 points) 问题 1: 引力波测量中的误差估计 (30 分)`，且解答内容与本题干完全对应。
  2. **解答细节对照**：独立盲解的各问数值（A1 的 $3.15\times 10^5\,\text{s}$、A3 的 $3.39\times 10^4\,\text{s}$ 与 $5.95\times 10^4\,\text{s}$、A6 的 $n=120$ 与 $10^{-141}$、B4 的 $-5.19\times 10^{-6}$、C1–C3 的 $1/2, 2\times 10^{-8}\,\text{W}, \text{数瓦}$）与官方解答分毫不差。需注意官方解答在 A2 写出 $\delta a_x$ 时第一项误印为 $-\frac{G(M-2m)}{R^2}$（未减去圆轨道基态加速度 $-\frac{GM}{R^2}$，应为 $+\frac{2Gm}{R^2}$），但在 A4 进行二阶泰勒展开时已自动扣除了零阶球对称项并给出了完全正确的四极场公式。

---

## 4. `panpho-2024-paper-2-problem-slice-q2` — 度量修正的测地线与热传导 (Metric-Modified Geodesic and Heat Conduction)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：旋转对称圆锥曲面上的测地线方程与 Clairaut 守恒量（归一化角动量 $L = \rho^2\frac{d\phi}{ds}$）、圆锥展开扇形几何法与直接积分法求光线偏折角 $\gamma$；球面立体投影（Stereographic projection）共形变换保二维拉普拉斯方程不变性，以及非共心双圆边界稳态热传导的阿波罗尼斯圆（Apollonius circles）静电镜像线电荷法与分式线性共形映射法。
- **分步独立推导**：
  - **A1 (圆锥测地线微分方程)**：在柱坐标 $(\rho,\phi,z)$ 下，$ds^2 = d\rho^2 + \rho^2 d\phi^2 + dz^2$。圆锥面上 $z'(\rho) = -\cot\theta$，故 $ds^2 = (1+\cot^2\theta)d\rho^2 + \rho^2 d\phi^2 = \csc^2\theta\,d\rho^2 + \rho^2 d\phi^2$。结合归一化角动量 $L = \rho^2\frac{d\phi}{ds} \implies \frac{ds}{d\phi} = \frac{\rho^2}{L}$：
    \[
    \frac{\rho^4}{L^2} = \left(\frac{ds}{d\phi}\right)^2 = \csc^2\theta\,\rho'(\phi)^2 + \rho^2 \implies \rho'(\phi)^2 = \frac{\sin^2\theta}{L^2}\rho^2(\rho^2 - L^2).
    \]
  - **A2 (最小投影半径 $\rho_{\min}$)**：平面上入射光线距原点垂直距离（瞄准距）为 $\rho_0/2$，故守恒角动量 $|L| = \rho_0/2$。由 $\rho'(\phi)^2 \ge 0$ 得近心点最小半径：
    \[
    \rho_{\min} = |L| = \frac{\rho_0}{2} = 2.5\,\text{mm}.
    \]
  - **A3 (出射与入射光线偏折角 $\gamma$)**：光线在圆锥区域 ($\rho \le \rho_0$) 内走过的方位角的一半为：
    \[
    \phi_0 = \int_{\rho_0/2}^{\rho_0} \frac{L\,d\rho}{\sin\theta\,\rho\sqrt{\rho^2-L^2}} = \frac{1}{\sin\theta}\left.\arctan\sqrt{\frac{\rho^2}{L^2}-1}\right|_1^2 = \frac{1}{\sin\theta}\arccos\frac{|L|}{\rho_0} = \frac{\beta}{\sin\theta},
    \]
    其中 $\beta = \arccos(1/2) = \pi/3 = 60^\circ$ 为平坦圆盘情形下的半方位角。由圆锥高 $h = 5\,\text{mm}$、底面半径 $\rho_0 = 5\,\text{mm}$ 知 $\theta = \pi/4$，$\sin\theta = 1/\sqrt{2}$，故总偏折角为：
    \[
    \gamma = 2(\phi_0 - \beta) = 2\left(\frac{1}{\sin\theta} - 1\right)\beta = \frac{2\pi}{3}(\sqrt{2} - 1) \approx 49.7^\circ.
    \]
  - **B1 (立体投影下球面拉普拉斯方程变换)**：单位球面立体投影 $\rho = \frac{\sin\theta}{1+\cos\theta} = \tan\frac{\theta}{2}$ 保持方位角 $\phi$ 不变，且满足微商算子恒等式：
    \[
    \frac{d\rho}{d\theta} = \frac{1}{2\cos^2(\theta/2)} = \frac{\rho}{\sin\theta} \implies \sin\theta\,\partial_\theta = \rho\,\partial_\rho.
    \]
    代入单位球面拉普拉斯方程 $\sin\theta\,\partial_\theta(\sin\theta\,\partial_\theta T) + \partial_\phi^2 T = 0$，即得 $\rho\,\partial_\rho(\rho\,\partial_\rho T) + \partial_\phi^2 T = 0$，除以 $\rho^2$ 即证：
    \[
    \frac{1}{\rho}\partial_\rho(\rho\,\partial_\rho T) + \frac{1}{\rho^2}\partial_\phi^2 T = 0.
    \]
  - **B2 (旋转对称灯罩温度分布)**：当 $\partial_\phi T = 0$ 时，$T(\rho) = c_1\ln\rho + c_2$。代入底部 $\theta = \pi/2$ ($\rho = 1$) 处 $T = T_b$ 及顶部 $\theta = \theta_t$ ($\rho = \tan(\theta_t/2)$) 处 $T = T_t$，得：
    \[
    T(\theta) = T_b + (T_t - T_b)\frac{\ln\left(\tan\frac{\theta}{2}\right)}{\ln\left(\tan\frac{\theta_t}{2}\right)}.
    \]
  - **C1 (倾斜顶部圆孔在 $(X,Y)$ 平面的投影轨迹)**：球面圆的直径端点 $(0,0,1)$ 与 $(\sin\alpha, 0, \cos\alpha)$ 分别映射为 $(0,0)$ 与 $(\tan\frac{\alpha}{2}, 0)$。由关于 $X$ 轴对称性，映射后的圆以 $(0,0)$ 和 $(2a,0)$（其中 $a \equiv \frac{1}{2}\tan\frac{\alpha}{2}$）为直径端点，圆心为 $(\frac{1}{2}\tan\frac{\alpha}{2}, 0)$，半径为 $a = \frac{1}{2}\tan\frac{\alpha}{2}$，方程为：
    \[
    \left(X - \frac{1}{2}\tan\frac{\alpha}{2}\right)^2 + Y^2 = \frac{1}{4}\tan^2\frac{\alpha}{2}.
    \]
  - **C2 (非对称灯罩温度分布 $T(X,Y)$)**：在 $X$ 轴上放置一对相反线电荷于 $(\mu, 0)$ 与 $(\mu^{-1}, 0)$，其等势面族 $\frac{(X-\mu)^2+Y^2}{(X-\mu^{-1})^2+Y^2} = K$ 自动包含单位圆 $X^2+Y^2 = 1$（对应 $K = \mu^2$，底部边界 $T = T_b$）。要求内圆 $X^2 - 2aX + Y^2 = 0$（过原点 $(0,0)$）亦为等势面，代入 $(0,0)$ 知内圆对应 $K = \mu^4$，展开等势面方程得 $X^2 - \frac{2}{\mu + \mu^{-1}}X + Y^2 = 0$，对比 $\frac{2}{\mu + \mu^{-1}} = 2a = \tan\frac{\alpha}{2}$ 解得：
    \[
    \mu = \frac{1 + \sqrt{1 - 4a^2}}{2a} = \cot\frac{\alpha}{2} + \sqrt{\cot^2\frac{\alpha}{2} - 1}, \qquad a = \frac{1}{2}\tan\frac{\alpha}{2}.
    \]
    匹配 $T_b$（在 $(1,0)$ 处比值为 $\mu^2$）与 $T_t$（在 $(0,0)$ 处比值为 $\mu^4$），得精确解：
    \[
    T(X,Y) = \frac{T_t - T_b}{2\ln\mu}\ln\left(\frac{(X-\mu)^2 + Y^2}{(X-\mu^{-1})^2 + Y^2}\right) + 2T_b - T_t.
    \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解与官方参考解答完全一致！特别值得在教学中对比的是 C2 的求解技巧：官方解答第一法设镜像电荷位于 $X_0 \pm A$，列出 4 个关于圆心与半径的非线性方程消元求解；而我们在盲解中直接利用“外圆为单位圆 $\implies$ 两镜像点互为反演点 $x_1 x_2 = 1$（即 $\mu$ 与 $\mu^{-1}$）”以及“内圆过原点 $(0,0) \implies K = \mu^4$”，两步即可直接写出 $\mu + \mu^{-1} = \frac{1}{a} = 2\cot\frac{\alpha}{2}$，极大简化了代数运算。官方解答还提供了基于分式线性莫比乌斯变换 $w = \frac{\mu\xi - 1}{\mu - \xi}$ 将偏心圆环映射为同心圆环的第二解法。

---

## 5. `panpho-2025-paper-2-problem-slice-q1` — 高尔夫球手的噩梦 (Golfer's Nightmare)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：刚体球在竖直圆筒内壁重力场中的纯滚动（无滑滚动）非完整约束动力学、动坐标系（圆柱基矢系与随质心旋转参考系）中的欧拉动力学方程，以及科里奥利力对旋转球体产生的陀螺耦合力矩。
- **分步独立推导**：
  - **(a) & (b) (无摩擦情形)**：质心位置 $\vec{r} = (R-r)\hat{e}_\rho + z\hat{e}_z$；无摩擦时 $\phi(t) = \Omega t$，$z(t) = H - \frac{1}{2}gt^2$，$N = m(R-r)\Omega^2$。
  - **(c) (质心运动方程)**：
    \[
    m(R-r)\dot{\phi}^2 = N, \qquad m(R-r)\ddot{\phi} = F_\phi, \qquad m\ddot{z} = F_z - mg.
    \]
  - **(d) (相对质心的角速度微分方程)**：由于基矢 $\hat{e}_\rho, \hat{e}_\phi$ 以角速度 $\dot{\phi}\hat{e}_z$ 旋转，$\dot{\vec{L}} = I\dot{\vec{\omega}} = \vec{\tau}_C = r\hat{e}_\rho\times\vec{F}$ 分量式为：
    \[
    I(\dot{\omega}_\rho - \dot{\phi}\omega_\phi) = 0, \qquad I(\dot{\omega}_\phi + \dot{\phi}\omega_\rho) = -r F_z, \qquad I\dot{\omega}_z = r F_\phi.
    \]
  - **(e) (纯滚动无滑约束条件)**：接触点 $P$ 速度 $\vec{v}_P = \vec{v}_C + \vec{\omega}\times(r\hat{e}_\rho) = 0$，即：
    \[
    (R-r)\dot{\phi} + r\omega_z = 0, \qquad \dot{z} - r\omega_\phi = 0.
    \]
  - **(f) (对原点 $O$ 的总角动量 $z$ 分量守恒)**：联立 $m(R-r)\ddot{\phi} = F_\phi$、$I\dot{\omega}_z = r F_\phi$ 与 $(R-r)\ddot{\phi} + r\dot{\omega}_z = 0$，得 $(I + mr^2)\dot{\omega}_z = 0 \implies \dot{\omega}_z = 0, \ddot{\phi} = 0, F_\phi = 0$。故 $\dot{\phi} = \Omega = \text{const}$，总角动量 $z$ 分量 $L_{z/O} = m(R-r)^2\dot{\phi} + I\omega_z$ 变化率为 $0$。
  - **(g), (h), (i) (竖直方向简谐振动证明、频率与最小洞深)**：由 $\dot{\omega}_\rho = \Omega\omega_\phi = \frac{\Omega}{r}\dot{z}$ 及初态 $\omega_\rho(0) = 0, z(0) = H$，积分得 $\omega_\rho = \frac{\Omega}{r}(z - H)$。代入 $I(\dot{\omega}_\phi + \Omega\omega_\rho) = -r F_z = -rm(\ddot{z}+g)$ 及 $I = Kmr^2, \dot{\omega}_\phi = \ddot{z}/r$，整理得：
    \[
    \ddot{z} = -\frac{K}{K+1}\Omega^2\left(z - H + \frac{g}{K\Omega^2}\right).
    \]
    此即角频率为 $\Omega_z = \sqrt{\frac{K}{K+1}}\Omega$（实心球 $K = 2/5$ 时 $\Omega_z = \sqrt{\frac{2}{7}}\Omega$）、振幅为 $A = \frac{g}{K\Omega^2}$ 的简谐运动！不触底的最小洞深为 $H_m = 2A = \frac{2g}{K\Omega^2} = \frac{5g}{\Omega^2}$。
  - **(j) (最低点角速度分量与能量去向)**：在最低点 $z_{\min} = H - 2A$ 处，$\dot{z} = 0 \implies |\omega_\phi| = 0$，$|\omega_z| = \frac{R-r}{r}\Omega$；减少的重力势能 $mg(2A)$ 完全转化为绕径向轴 $\hat{e}_\rho$ 的自转能 $\frac{1}{2}I\omega_\rho^2$，得：
    \[
    |\omega_\rho| = \frac{2g}{Kr\Omega} = \frac{5g}{r\Omega}.
    \]
  - **(k1)–(k3) & (l1)–(l4) (旋转系虚拟力与科里奥利力矩解释)**：
    - 离心力、欧拉力（$\dot{\Omega}=0$）、科里奥利力对整球的合外力 $z$ 分量均为 $0$；离心力与欧拉力对球心的合力矩亦为 $0$。
    - 唯独科里奥利力对旋转球体各质元 $\vec{v}' = \vec{\omega}'\times\vec{r}'_c$ 产生非零合力矩：
      \[
      \vec{\tau}_C = -2\int dm\,\vec{r}'_c\times\left[\vec{\Omega}\times(\vec{\omega}'\times\vec{r}'_c)\right] = I(\vec{\omega}'\times\vec{\Omega}) = \frac{2}{5}mr^2(\vec{\omega}'\times\vec{\Omega}).
      \]
      当球下降积累了负向径向自转 $\omega_\rho < 0$ 时，球体上半部向 $+y'$ 运动、下半部向 $-y'$ 运动，所受科里奥利力一里一外，形成沿 $+\hat{e}_\phi$ 方向的翻转力矩，通过壁面静摩擦力耦合使球向上爬升！

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解与官方解答完全一致。在 (l3) 计算科里奥利力矩积分 $\int \rho\,dx'_c dy'_c dz'_c {z'_c}^2$ 时，官方解答采用切片圆盘积分算出 $\frac{1}{5}mr^2$；而盲解指出对任意球对称质量分布 $\int {z'_c}^2 dm = \frac{1}{3}\int {r'_c}^2 dm = \frac{1}{2}I = \frac{1}{2}Kmr^2$，无需积分即可直接得到适用于任意 $K$ 的普适公式 $\vec{\tau}_C = I(\vec{\omega}'\times\vec{\Omega})$。

---

## 6. `panpho-2025-paper-2-problem-slice-q2` — 超短电磁脉冲 (Generation of Ultrashort Electromagnetic Pulse)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：高斯超短激光脉冲的时频傅里叶变换表示、束缚电子洛伦兹阻尼振子色散模型 $\varepsilon(\omega)$、群延迟色散（GDD, $\beta_2$）引起的脉冲展宽与棱镜/光栅对腔内色散补偿，以及强场非微扰电离（Keldysh 判据）与非简谐高次谐波（HHG）阿秒脉冲产生机制。
- **分步独立推导**：
  - **A1 (高斯脉冲复数表达式与零均值约束)**：时域复数场 $a(t) = E_0 e^{-t^2/\tau_p^2} e^{i(\omega_0 t + \varphi_0)}$（实部 $E_0 e^{-t^2/\tau_p^2}\cos(\omega_0 t + \varphi_0)$）。由于包络积分有限，在 $T \to \infty$ 时时间平均值为 $\langle a(t)\rangle = \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^T a(t)\,dt = 0$。
  - **A2 (Ti:sapphire 飞秒激光参数)**：光子能量 $E_{\text{ph}} = 1.55\,\text{eV}$ 对应中心频率 $f_0 = \frac{E_{\text{ph}}}{h} \approx 3.75\times 10^{14}\,\text{Hz}$ ($\omega_0 = 2\pi f_0 \approx 2.35\times 10^{15}\,\text{rad/s}$)。半高全宽 $\text{FWHM} = 35\,\text{fs}$（若按 $t = \text{FWHM}/2$ 处振幅降至 $1/2$，则 $\tau_p = \frac{35\,\text{fs}}{2\sqrt{\ln 2}} \approx 21\,\text{fs}$；若按 $t = \text{FWHM}$ 处降至 $1/2$，则 $\tau_p = \frac{35\,\text{fs}}{\sqrt{\ln 2}} \approx 42\,\text{fs}$）。
  - **A3(1) & A3(2) (真空与色散介质中的传播)**：真空中 $E(z,t) \propto \int_{-\infty}^\infty \exp\left(-\frac{\tau_p^2(\omega-\omega_0)^2}{4}\right)e^{i(\omega t - \frac{\omega}{c}z)}\,d\omega$，满足一维波动方程 $\left(\partial_z^2 - \frac{1}{c^2}\partial_t^2\right)E = 0$。在折射率 $n(\omega)$ 的介质中传播距离 $L$ 后：
    \[
    E(L,t) \propto \int_{-\infty}^\infty \exp\left(-\frac{\tau_p^2(\omega-\omega_0)^2}{4}\right) \exp\left[i\left(\omega t - n(\omega)\frac{\omega}{c}L\right)\right] d\omega.
    \]
  - **B1 & B2 (洛伦兹振子色散模型)**：由 $m\ddot{x} + m\gamma\dot{x} + m\Omega_0^2 x = -e E_0 e^{i\omega t}$，得电子复振幅 $X_0 = \frac{-e E_0}{m(\Omega_0^2 - \omega^2 + i\gamma\omega)}$（最大位移模值为 $\frac{eE_0}{m\sqrt{(\Omega_0^2-\omega^2)^2 + \gamma^2\omega^2}}$）。极化强度 $\vec{P} = -Ne\vec{x} = \frac{Ne^2/m}{\Omega_0^2 - \omega^2 + i\gamma\omega}\vec{E}$，相对介电函数：
    \[
    \varepsilon_r(\omega) = 1 + \frac{Ne^2}{\varepsilon_0 m(\Omega_0^2 - \omega^2 + i\gamma\omega)}, \qquad n(\omega) = \sqrt{\varepsilon_r(\omega)}.
    \]
  - **C1 (二阶色散脉冲展宽公式证明)**：将 $\beta(\omega) = \beta_0 + \beta_1\omega' + \beta_2\omega'^2$（其中 $\omega' = \omega - \omega_0$）代入傅里叶积分，复高斯参数为 $a = \frac{\tau_p^2}{4} + i\beta_2 L$。由高斯积分恒等式得输出包络模方指数项为：
    \[
    \operatorname{Re}\left(\frac{(t - \beta_1 L)^2}{4a}\right) = \frac{(t - \beta_1 L)^2}{\tau_p^2 + \frac{16\beta_2^2 L^2}{\tau_p^2}} \implies \tau_{\text{out}} = \tau_p\sqrt{1 + \frac{(4\beta_2 L)^2}{\tau_p^4}}, \quad \alpha = 4.
    \]
  - **C2 (色散补偿谐振腔设计)**：在激光腔内引入棱镜对压缩器（Prism pair compressor）或衍射光栅对压缩器（Grating pair compressor），利用角色散使不同频率分量走过不同几何光程，提供反号二阶群延迟色散以抵消增益晶体的正色散。
  - **D1, D2, D3 (高次谐波与阿秒脉冲产生)**：
    - D1：一个光周期内电场赋予电子的振荡动量 $\frac{eE}{\omega}$ 需超过克服电离能 $W \approx 13.6\,\text{eV}$ 的特征动量 $\sqrt{2mW}$（即 Keldysh 参数 $\gamma_K = \frac{\omega\sqrt{2mW}}{eE} < 1$），得阈值场强 $E > \frac{\omega\sqrt{2mW}}{e} \approx 3\times 10^{10}\,\text{V/m} = 30\,\text{GV/m}$（或原子库仑场量级 $\sim 10^{11}\,\text{V/m}$）。
    - D2：在束缚势中引入非简谐高阶项 $u(x) = \alpha_1 x^2 + \alpha_2 x^3 + \dots$，运动方程 $m\ddot{x} + \alpha'_1 x = \alpha'_2 x^2 + \dots + eE_0 e^{i\omega_0 t}$ 通过非线性微扰迭代产生 $x_n \propto E_0^n e^{in\omega_0 t}$ 的高次谐波辐射。
    - D3：对于高斯包络 $E_0(t) \propto e^{-t^2/\tau_p^2}$，$n$ 阶非线性极化 $P^{(n)}(t) \propto [E_0(t)]^n e^{in\omega_0 t} = e^{-t^2/(\tau_p/\sqrt{n})^2} e^{in\omega_0 t}$ 使脉宽按 $\tau_p/\sqrt{n}$ 压缩（且多阶锁相高次谐波相干叠加进一步将脉宽压缩至阿秒量级）。

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解与官方解答在物理框架、C1 的 $\alpha = 4$、B1–B2 色散曲线、C2 棱镜/光栅压缩器以及 D1–D3 上完全一致。需特别指出官方解答在 A2 数值代入中的一个算术笔误：官方解答写下 $\tau_p = \frac{35\,\text{fs}}{\sqrt{\ln 2}} \approx 42\,\text{fs} = 4.2\times 10^{-14}\,\text{s}$ 时，将指数误写成了 $4.2\times 10^{-12}\,\text{s}$（差了两个数量级，且未除以半高全宽的因子 $2$）。在教学中指出这一笔误有助于培养学生的量纲与数量级核查习惯。

---

## 7. `panpho-2026-paper-2-problem-slice-q1` — 直流与交流导体模型 (DC and AC Conductor Models)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：直流圆柱导线内的径向磁自箍缩效应（Self-pinch）与径向霍尔静电场平衡、整体电中性条件下的电子束收缩半径 $R = a\sqrt{1-v^2/c^2}$、电子静止系 $S'$ 中“磁力消失但静电力不为零”的伽利略佯谬及其狭义相对论洛伦兹长度收缩严格消解；以及交流平板导体中的涡流趋肤效应（Skin effect）与超高频位移电流主导下的驻波过渡。
- **分步独立推导**：
  - **(a) (电流密度)**：$J(r) = e n_e(r) v$。
  - **(bi) & (bii) (导线内部磁场与电场)**：由安培环路定理与高斯定理：
    \[
    \vec{B}(r) = \frac{\mu_0 e v}{r}\left(\int_0^r n_e(r')r'\,dr'\right)\hat{\phi}, \qquad \vec{E}(r) = \frac{e}{\varepsilon_0 r}\left(\int_0^r \left[n_p - n_e(r')\right]r'\,dr'\right)\hat{r}.
    \]
  - **(c) & (d) (稳恒流动下的电子数密度分布与自箍缩半径)**：在有电子流动的区域内，每个电子所受向内的磁箍缩力 $\vec{F}_B = -evB_\phi(r)\hat{r}$ 与静电力 $\vec{F}_E = -eE_r(r)\hat{r}$ 平衡：
    \[
    \left(1 - \frac{v^2}{c^2}\right)\int_0^r n_e(r')r'\,dr' = \int_0^r n_p r'\,dr' = \frac{1}{2}n_p r^2 \implies n_e = \frac{n_p}{1 - v^2/c^2}.
    \]
    因 $n_e > n_p$，由实验室系导线单位长度总电荷中性 $\pi R^2 n_e = \pi a^2 n_p$，电子向中心收缩并充满半径为 $R = a\sqrt{1 - v^2/c^2}$ 的圆柱区：
    \[
    n_e(r) = \begin{cases} \dfrac{n_p}{1 - v^2/c^2}, & 0 \le r \le R = a\sqrt{1 - v^2/c^2}, \\ 0, & R < r \le a. \end{cases}
    \]
  - **(e) (导线表面与中心电势差)**：因电子向中心聚集、外层 $R < r \le a$ 留下净正电荷，**表面 (Surface)** 电势更高。分段积分 $E(r)$（在 $0 \le r \le R$ 内 $E(r) = \frac{e(n_p - n_e)r}{2\varepsilon_0} < 0$；在 $R < r \le a$ 内 $E(r) = \frac{en_p r}{2\varepsilon_0} - \frac{en_e R^2}{2\varepsilon_0 r}$）：
    \[
    \Delta V = -\int_0^a E(r)\,dr = \frac{e n_p a^2}{2\varepsilon_0}\ln\frac{1}{\sqrt{1 - v^2/c^2}} \approx \frac{e n_p a^2 v^2}{4\varepsilon_0 c^2}.
    \]
  - **(f), (g), (h) ($S'$ 系佯谬与相对论消解)**：
    - (f) 若不计相对论长度收缩，在随电子静止的 $S'$ 系中磁力为零，电子仅受净负电荷排斥力 $F_{\text{net}} = \frac{e^2 n_p r}{2\varepsilon_0}\frac{v^2/c^2}{1 - v^2/c^2} > 0$（向外）。
    - (g) 计及洛伦兹长度收缩后，正离子在 $S'$ 系以速度 $v$ 运动，数密度增大为 $n'_p = \gamma n_p = \frac{n_p}{\sqrt{1 - v^2/c^2}}$。
    - (h) 电子在 $S'$ 系静止、在 $S$ 系运动，故 $n_e = \gamma n'_e \implies n'_e = \frac{n_e}{\gamma} = \frac{n_p}{1-v^2/c^2}\sqrt{1-\frac{v^2}{c^2}} = \gamma n_p = n'_p$！因此在 $S'$ 系中正负电荷数密度严格相等（$E'_+ = E'_- \implies \vec{E}' = 0$），且电子静止不受磁力，合力严格为零！
  - **(i) & (j) (线性增长电流下的平板磁场与感生电场差)**：由安培环路定理得 $\vec{B}(y,t) = -\mu_0(j_0 + \alpha t)y\,\hat{x}$；由法拉第电磁感应定律 $\frac{\partial E_z}{\partial y} = -\frac{\partial B_x}{\partial t} = \mu_0\alpha y$ 积分得：
    \[
    \Delta E_z = E_z\left(\frac{D}{2}\right) - E_z\left(\frac{D}{4}\right) = \frac{3}{32}\mu_0\alpha D^2.
    \]
  - **(k), (l), (m), (n) (工频交流趋肤效应)**：
    - (k) $\frac{\sigma}{\varepsilon_0\omega} = \frac{3.77\times 10^7}{8.85\times 10^{-12}\times 2\pi\times 50} \approx 1.36\times 10^{16} \gg 1$，位移电流远小于传导电流。
    - (l) 联立 $\nabla\times\vec{E} = -\partial_t\vec{B}$ 与 $\nabla\times\vec{B} = \mu_0\sigma\vec{E}$ 得 $\frac{d^2 j(y)}{dy^2} = i\omega\mu_0\sigma\,j(y)$。
    - (m) & (n) 设 $k = \sqrt{i\omega\mu_0\sigma} = \sqrt{\frac{\omega\mu_0\sigma}{2}}(1+i)$，对称解为 $j(y) = j_0\frac{\cosh(ky)}{\cosh(kD/2)}$。在厚板极限 $D \gg \sqrt{1/(\sigma\mu_0\omega)}$ 的下表面附近：
      \[
      j(y) \simeq j_0 \exp\left[-\sqrt{\frac{\omega\mu_0\sigma}{2}}(1+i)\left(y + \frac{D}{2}\right)\right],
      \]
      \[
      J(y,t) = j_0 \exp\left[-\sqrt{\frac{\omega\mu_0\sigma}{2}}\left(y + \frac{D}{2}\right)\right]\cos\left[\sqrt{\frac{\omega\mu_0\sigma}{2}}\left(y + \frac{D}{2}\right) - \omega t\right],
      \]
      趋肤深度 $\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}} \approx 0.012\,\text{m}$。
  - **(o) (超高频位移电流主导下的驻波)**：当 $\omega\varepsilon_0 \gg \sigma$ 时，方程化为 $\frac{d^2 j(y)}{dy^2} = -\frac{\omega^2}{c^2}j(y)$，对称边界条件下形成驻波 $J(y,t) = 2A\cos\left(\frac{\omega}{c}y\right)\cos(\omega t)$，波长为 $\lambda = \frac{2\pi c}{\omega}$。

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解与官方参考解答高度一致。尤其值得在教学中强调的是 (c)–(e) 中“导线整体电中性”带来的几何收缩边界 $R = a\sqrt{1 - v^2/c^2}$：由于内部平衡要求电子密度 $n_e = \frac{n_p}{1-v^2/c^2} > n_p$，若电子总数与正离子总数相等，电子柱半径必然从 $a$ 收缩至 $R = a/\gamma$，在 $R < r \le a$ 形成一层无电子的正离子耗尽壳层，从而使表面与中心的精确电势差呈现简洁的对数形式 $\Delta V = \frac{en_p a^2}{2\varepsilon_0}\ln\gamma$（其低速展开首项恰为 $\frac{1}{4}\mu_0 e n_p v^2 a^2$）。

---

## 8. `panpho-2026-paper-2-problem-slice-q2` — 强激光与等离子体有质动力 (Intense Laser and Plasma Ponderomotive Force)

### Phase 1: 独立盲解记录 (Blind Attempt)

- **核心物理模型**：非均匀高频振荡激光场中的快慢时间尺度分离（双尺度微扰法）、电子快速抖动动能的时间平均即有质动力势 $U_p(x)$（Ponderomotive potential）、热流体压强梯度与有质动力平衡下的玻尔兹曼电子密度排空分布，以及等离子体折射率横向梯度引起的克尔型有质动力自聚焦（Self-focusing）与薄渐变折射率（GRIN）透镜焦距推导。
- **分步独立推导**：
  - **(a) (电子运动方程与有质动力势 $U_p(x)$)**：在 $\mathbf{E}(x,t) = \hat{x}E_0 e^{-x^2/L^2}\cos(\omega t)$ 中，快速振荡运动方程为 $m_e\ddot{x}_{\text{osc}} = -e E(x)\cos(\omega t)$，积分得振荡速度 $\dot{x}_{\text{osc}}(t) = -\frac{e E(x)}{m_e\omega}\sin(\omega t)$。对一个光周期求平均动能（$\langle\sin^2\omega t\rangle = 1/2$）：
    \[
    U_p(x) = \left\langle\frac{1}{2}m_e \dot{x}_{\text{osc}}^2\right\rangle = \frac{e^2 E^2(x)}{4m_e\omega^2} = \frac{e^2 E_0^2}{4m_e\omega^2}e^{-2x^2/L^2}.
    \]
  - **(b) (有质动力 $F_{p,x}(x)$ 与空间势垒图像)**：
    \[
    F_{p,x}(x) = -\frac{dU_p(x)}{dx} = \frac{e^2 E_0^2 x}{m_e\omega^2 L^2}e^{-2x^2/L^2}.
    \]
    当 $x > 0$ 时 $F_{p,x} > 0$，当 $x < 0$ 时 $F_{p,x} < 0$，即有质动力始终将电子从光强最大的中心轴线 ($x=0$) 推向两侧弱场区；$U_p(x)$ 在 $x=0$ 处形成高斯型势垒峰 $U_0 = \frac{e^2 E_0^2}{4m_e\omega^2}$。
  - **(c) (准静态热平衡电子密度分布 $n_e(x)$)**：将 $p_e = n_e k_B T_e$ 与 $F_{p,x} = -\frac{dU_p}{dx}$ 代入慢变力学平衡方程 $-\frac{\partial p_e}{\partial x} + n_e F_{p,x} = 0$：
    \[
    \frac{1}{n_e}\frac{dn_e}{dx} = -\frac{1}{k_B T_e}\frac{dU_p}{dx} \implies n_e(x) = n_0 \exp\left(-\frac{U_p(x)}{k_B T_e}\right).
    \]
  - **(d) (显式分布与电子耗尽区宽度标度)**：
    \[
    n_e(x) = n_0 \exp\left(-\frac{e^2 E_0^2}{4m_e\omega^2 k_B T_e}e^{-2x^2/L^2}\right).
    \]
    耗尽区特征宽度与光束横向宽度 $L$ 成正比；当 $U_0 = \frac{e^2 E_0^2}{4m_e\omega^2} \gg k_B T_e$ 时，由 $U_p(x_{\text{depl}}) \sim k_B T_e$ 得耗尽区半宽 $x_{\text{depl}} \sim \frac{L}{\sqrt{2}}\sqrt{\ln\left(\frac{U_0}{k_B T_e}\right)}$，随 $E_0$ 对数慢速展宽且中心耗尽深度呈指数加剧。
  - **(e) (等离子体相对介电常数、自聚焦判据与等效焦距 $f$)**：
    - (i) 忽略碰撞时自由电子极化给出冷等离子体介电函数 $\varepsilon_r(x) = 1 - \frac{\omega_p^2(x)}{\omega^2} = 1 - \frac{n_e(x)e^2}{\varepsilon_0 m_e\omega^2}$。在弱微扰 $\alpha \equiv \frac{U_p(0)}{k_B T_e} \ll 1$ 下：
      \[
      \varepsilon_r(x) \approx 1 - \frac{\omega_{p0}^2}{\omega^2} + \frac{\omega_{p0}^2}{\omega^2}\alpha e^{-2x^2/L^2} = \varepsilon_r(\infty) + \frac{\omega_{p0}^2}{\omega^2}\alpha e^{-2x^2/L^2}.
      \]
    - (ii) 由于中心处电子被排空（$n_e(0)$ 最小），而等离子体对折射率的贡献为负，故中心轴线处折射率 $n(0) = \sqrt{\varepsilon_r(0)}$ 最大、两侧折射率较小，等效于正凸透镜，激光束发生**自聚焦 (Self-focusing / Self-converging)**。
    - (iii) 对 $n(x) = \sqrt{\varepsilon_r(x)}$ 在傍轴区 $|x| \ll L$ 展开至 $x^2$ 阶：
      \[
      n(x) \approx \sqrt{\varepsilon_r(\infty)}\left(1 + \frac{1}{2}\frac{\Delta\varepsilon_r(x)}{\varepsilon_r(\infty)}\right) \approx n_{\text{eff}} - \frac{\alpha \omega_{p0}^2}{\omega^2\sqrt{\varepsilon_r(\infty)} L^2}x^2.
      \]
      穿过厚度为 $d$ 的等离子体薄层后，附加相位 $\phi(x) = k_0 n(x) d$ 的二次项与薄透镜相位因子 $\phi_{\text{lens}}(x) = -\frac{k_0 x^2}{2f}$ 对比，得等效焦距：
      \[
      f = \frac{\omega^2\sqrt{\varepsilon_r(\infty)}L^2}{2\alpha\omega_{p0}^2 d} = \frac{2\varepsilon_0 m_e^2 \omega^4 k_B T_e L^2}{n_0 e^4 E_0^2 d}\sqrt{1 - \frac{n_0 e^2}{\varepsilon_0 m_e\omega^2}}.
      \]

### Phase 2: 对照官方参考解答与教学拆解 (Comparison & Breakdown)

- **对照分析**：独立盲解与官方参考解答在全部公式、符号、耗尽宽度对数标度 $x_{\text{depl}} \sim \frac{L}{\sqrt{2}}\sqrt{\ln(U_0/k_B T_e)}$ 以及等效焦距 $f$ 的带根号背景折射率修正因子 $\sqrt{\varepsilon_r(\infty)} = \sqrt{1 - \frac{n_0 e^2}{\varepsilon_0 m_e\omega^2}}$ 上完全一致。
- **核心难点与易错点**：
  1. **为什么电子受排斥却导致激光自聚焦？** 学生常受普通电介质“高密度对应高折射率”的思维定势影响，误以为电子被排空会导致中心折射率降低而自发散。突破关键在于等离子体色散关系 $\varepsilon_r = 1 - \omega_p^2/\omega^2$ 中电子密度项带有**负号**：电子越少，折射率越接近真空值 $1$（高于周围等离子体的折射率 $<1$），从而形成中心高折射率波导。
  2. **傍轴焦距推导中的三级近似链**：需依次完成 ① 玻尔兹曼指数弱场展开 $e^{-U_p/k_B T_e} \approx 1 - U_p/k_B T_e$、② 平方根折射率一阶泰勒展开 $\sqrt{\varepsilon_r(\infty) + \Delta\varepsilon_r} \approx \sqrt{\varepsilon_r(\infty)}\left(1 + \frac{\Delta\varepsilon_r}{2\varepsilon_r(\infty)}\right)$、③ 高斯分布傍轴展开 $e^{-2x^2/L^2} \approx 1 - 2x^2/L^2$，任意一步漏掉系数 $2$ 都会导致焦距 $f$ 差 $2$ 倍。
