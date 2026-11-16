# Batch 11: Physics Cup 2025–2026 竞赛题解与教学拆解记录（两阶段盲解与对照分析）

本报告严格遵循两阶段教练协议（Phase 1 独立盲解 $\to$ Phase 2 对照官方结果页评述与获奖解答进行教学拆解），涵盖 Physics Cup TalTech 2025 与 2026 全部 10 道赛题。

---

## 1. `physicscup-2025-q1-reader` — Interaction force（旋转金属球间的静电力相互作用）

### 【Phase 1：独立盲解记录】
1. **物理图像与内部场平衡**：
   位于原点的非磁性金属球（半径 $R$）绕 $x$ 轴以角速度 $\omega$ 匀速旋转，处于沿 $x$ 轴的匀强磁场 $\vec{B} = B\hat{x}$ 中。
   在金属球内部，随球共转的自由电子速度为 $\vec{v} = \vec{\omega}\times\vec{r} = \omega(-z\hat{y} + y\hat{z})$，所受洛伦兹力对应等效动生电场：
   $$\vec{v}\times\vec{B} = \omega B(y\hat{y} + z\hat{z}) = \omega B \vec{s}$$
   其中 $\vec{s} = y\hat{y} + z\hat{z}$ 为到旋转轴（$x$ 轴）的圆柱径向矢量。
   由于 $\nabla\times(\vec{v}\times\vec{B}) = 0$，球内无稳恒涡流（不消耗焦耳热），自由电荷重新分布建立静电场 $\vec{E}_{\text{in}} = -\nabla\phi_{\text{in}}$ 以抵消洛伦兹力（忽略微弱的电子离心惯性力 $m_e\omega^2\vec{s}/e$）：
   $$\vec{E}_{\text{in}} = -\omega B \vec{s} \implies \phi_{\text{in}}(x,y,z) = \frac{1}{2}\omega B(y^2 + z^2) + C = \frac{1}{2}\omega B r^2\sin^2\theta + C$$
2. **球外电四极势匹配**：
   在球面 $r=R$ 上，$\phi_{\text{in}}(R,\theta) = \frac{1}{2}\omega B R^2(1-\cos^2\theta) + C = \frac{1}{3}\omega B R^2\left[1 - P_2(\cos\theta)\right] + C$。
   球外满足拉普拉斯方程 $\nabla^2\phi_{\text{out}} = 0$，且金属球总电荷 $Q=0$（无 $1/r$ 单极项）。由唯一性定理，球外电势纯由 $l=2$ 轴对称电四极矩贡献：
   $$\phi_{\text{out}}(r,\theta) = -\frac{1}{3}\omega B \frac{R^5}{r^3} P_2(\cos\theta) = \frac{1}{6}\omega B R^5 \frac{y^2 + z^2 - 2x^2}{r^5}$$
3. **远处静止金属球的感应偶极矩与相互作用力**：
   在 $x = L \gg R$（$\theta = 0, P_2(1) = 1$）处，沿 $x$ 轴的电势与电场及梯度分别为：
   $$\phi_{\text{out}}(x,0,0) = -\frac{\omega B R^5}{3x^3}, \qquad E_x(x) = -\frac{\partial\phi_{\text{out}}}{\partial x} = -\frac{\omega B R^5}{x^4}, \qquad \frac{\partial E_x}{\partial x} = \frac{4\omega B R^5}{x^5}$$
   位于 $x=L$ 的不带电导体球在近似均匀的外场 $E_x(L)$ 中感应出电偶极矩：
   $$p_x = 4\pi\varepsilon_0 R^3 E_x(L) = -4\pi\varepsilon_0 \frac{\omega B R^8}{L^4}$$
   该感应偶极子在外场梯度中所受静电力为：
   $$F_x = p_x \left.\frac{\partial E_x}{\partial x}\right|_{x=L} = -\frac{16\pi\varepsilon_0 \omega^2 B^2 R^{13}}{L^9}$$
   负号表示两球相互吸引，力大小为 $\dfrac{16\pi\varepsilon_0 \omega^2 B^2 R^{13}}{L^9}$。

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Ethan Lu, Sim Hui Xiang 等）的对照**：
  1. **四极场的构造技巧**：Kalda 在评述中指出，绝大多数参赛者直接使用了球坐标下拉普拉斯方程的勒让德多项式展开（被 Kalda 称为“合乎逻辑但偏暴力的做法”），而获奖解通过将两个反向共线电偶极子 $\pm\vec{p}$ 平移求导 $\frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) = \frac{r^2-3x^2}{r^5}$ 直接构造出理想点四极势，并结合唯一性定理一步锁定球外电势。
  2. **题设强不等式 $R \ll \sqrt{\rho/\mu\omega}$ 的真实物理作用**：盲解时容易认为对称轴与磁场平行时不产生涡流，从而觉得趋肤深度条件 $\delta \sim \sqrt{\rho/\mu\omega} \gg R$ 是干扰项。但对照 Ethan Lu 等获奖选手的分析可知：第一，由于第二颗球感应偶极场在第一颗旋转球处会产生破坏轴对称性的微扰外场，若无 $R \ll \delta$，旋转球在非轴对称微扰场中将感生涡流与磁偶极矩；第二，这也提醒选手检验旋转带电体产生的自生磁场 $B_r/B \sim (\omega R/c)^2 \ll 1$ 与电流磁场是否可忽略。
  3. **镜像法能量求导的常见陷阱**：Sim Hui Xiang 的修正案展示了极佳的反面教材——若用点电荷对球镜像法直接求静电势能 $U$，必须把 $2\times 3$ 组镜像电荷的相互作用全部展开到 $d^4/L^9$ 阶，漏掉二阶交叉项会误得 $F \propto R^{11}/L^7$，远不如多极展开（四极场+外场感应偶极子 $F = p_x \partial_x E_x$）干净稳健。

---

## 2. `physicscup-2025-q2-reader` — Tetrahedral flock of birds（正四面体群鸟追逐问题）

### 【Phase 1：独立盲解记录】
1. **旋转反射对称性（$S_4$ 反演旋转群）降维**：
   四只鸟初始位于边长为 $a$ 的正四面体顶点，$A\to B\to C\to D\to A$ 循环追逐。
   将正四面体嵌入以原点为中心的长方体（初期为正方体）交错顶点，设 $z$ 轴连接对棱 $AC$ 中点与 $BD$ 中点。定义正交变换 $\mathcal{T}: (x,y,z) \mapsto (-y, x, -z)$（绕 $z$ 轴旋转 $90^\circ$ 再关于 $xy$ 平面反射）。
   初始时刻 $\vec{r}_B = \mathcal{T}\vec{r}_A, \vec{r}_C = \mathcal{T}\vec{r}_B, \vec{r}_D = \mathcal{T}\vec{r}_C$。由于追逐律保持该等距变换协变，任意时刻四只鸟始终构成正四面体退化而成的**正方双楔体（tetragonal disphenoid）**，其坐标满足：
   $$\vec{r}_A = (x,y,z), \quad \vec{r}_B = (-y,x,-z), \quad \vec{r}_C = (-x,-y,z), \quad \vec{r}_D = (y,-x,-z)$$
2. **圆柱坐标下的微分方程与守恒量**：
   在圆柱坐标 $(r,\phi,z)$（其中 $r = \sqrt{x^2+y^2}$）中，$\vec{r}_B - \vec{r}_A = (-y-x, x-y, -2z)$，其模长为：
   $$|\vec{r}_B - \vec{r}_A| = \sqrt{2(x^2+y^2) + 4z^2} = \sqrt{2r^2 + 4z^2}$$
   利用 $r\dot{r} = x\dot{x} + y\dot{y}$，由追逐方向单位矢量 $\frac{d\vec{r}_A}{ds} = \frac{\vec{r}_B - \vec{r}_A}{|\vec{r}_B - \vec{r}_A|}$（$s$ 为弧长）得：
   $$\frac{dr}{ds} = \frac{x(-y-x) + y(x-y)}{r\sqrt{2r^2 + 4z^2}} = \frac{-r}{\sqrt{2r^2 + 4z^2}}, \qquad \frac{dz}{ds} = \frac{-2z}{\sqrt{2r^2 + 4z^2}}$$
   两式相除消去弧长微元 $ds$：
   $$\frac{dz}{dr} = \frac{2z}{r} \implies \frac{z}{r^2} = \text{const}$$
   初始时刻 $|AC| = 2r_0 = a \implies r_0 = \frac{a}{2}$；又 $|AB| = \sqrt{2r_0^2 + 4z_0^2} = a \implies z_0 = \frac{a}{2\sqrt{2}}$。因此守恒关系为：
   $$z = \frac{\sqrt{2}}{a} r^2$$
3. **总路程积分**：
   将 $z(r)$ 代回 $\frac{ds}{dr}$：
   $$ds = -\frac{\sqrt{2r^2 + 4z^2}}{r}\,dr = -\sqrt{2 + \frac{8r^2}{a^2}}\,dr$$
   从 $r_0 = a/2$ 积分到会合点 $r = 0$：
   $$s_{\text{total}} = \int_0^{a/2} \sqrt{2 + \frac{8r^2}{a^2}}\,dr = \frac{a}{2\sqrt{2}} \int_0^1 \sqrt{1 + u^2}\,du = \frac{a}{2}\left(1 + \frac{\operatorname{arsinh}(1)}{\sqrt{2}}\right) = \frac{a}{2}\left(1 + \frac{\ln(1+\sqrt{2})}{\sqrt{2}}\right) \approx 0.811613\,a$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **三类主流解法的对比**：
  Kalda 在评述中将 111 份正确解答归纳为三类：
  1. **方法 (a)（内接长方体 / 柱坐标法，如 Bruno Machado Feltran、Ilan Mihelja & Ivan Hegedić）**：与我们盲解完全一致，利用 $S_4$ 旋转反射对称性直接将动力学约化为柱坐标 $(r,z)$，一步导出 $\frac{dz}{dr} = \frac{2z}{r}$，数学最为简明。
  2. **方法 (b)（四面体两种边长参数化，如 Eric Wang，也是官方提示路线）**：设任意时刻 $AB=BC=CD=DA=l_1$，$AC=BD=l_2$，利用邻边夹角余弦导出 $dl_1/ds$ 与 $dl_2/ds$ 的自治微分方程组。虽然完全不依赖坐标系，但计算余弦投影比外接长方体坐标略繁琐。
  3. **方法 (c)（笛卡尔坐标对称性约化，如 Capatina 等）**：将初始顶点放在 $(\pm 1, \pm 1, \pm 1)$，通过离散对称操作寻找独立时间函数 $\xi(t), \eta(t)$。这提醒学生：**四面体的对偶立方体嵌入（Cube-Tetrahedron Embedding）**是处理三维正四面体对称性问题最强大的代数工具。

---

## 3. `physicscup-2025-q3-reader` — Oscillating piston（振荡活塞下的气体费米加速加热）

### 【Phase 1：独立盲解记录】
1. **模型尺度分离与物理图像**：
   - $\lambda \gg a$：活塞振幅 $a$ 远小于分子平均自由程 $\lambda$，意味着分子在活塞振荡区（厚度 $\sim 2a$）内不会与其他分子碰撞；又因为 $v \gg u$，以速度 $v_z > u$ 撞击活塞的分子反弹后速度 $v_z' = v_z \pm 2u > u$ 远大于活塞追赶速度 $u$，故**每个入射分子在一个自由程内只与活塞发生唯一一次弹性碰撞**。
   - $H \gg \lambda \gg \frac{H^2}{vt}$：气体柱高度远大于平均自由程，整体处于流体力学导热区；热扩散特征时间 $\tau_{\text{diff}} \sim \frac{H^2}{D} \sim \frac{H^2}{\lambda v} \ll t$，说明活塞表面产生的热量能瞬间均匀传导至整个气柱，气柱温度 $T(t)$（及方均根速率 $v_{\text{rms}}(t)$）在空间上始终均匀，且遵循麦克斯韦分布。
2. **往返半周期的平均能量增益**：
   设分子入射法向速度为 $v_z > u$：
   - 活塞向下运动（迎向气体，速度 $-u$）：碰撞相对速度为 $v_z + u$，反弹后速度 $v_z' = v_z + 2u$，单次碰撞动能增量 $\Delta E_+ = \frac{1}{2}m[(v_z+2u)^2 - v_z^2] = 2mu(v_z + u)$，半周期内单位面积碰撞次数为 $\frac{T_{\text{osc}}}{2} n f(v_z)(v_z + u)$。
   - 活塞向上运动（背离气体，速度 $+u$）：碰撞相对速度为 $v_z - u$，反弹后速度 $v_z' = v_z - 2u$，单次碰撞动能增量 $\Delta E_- = -2mu(v_z - u)$，半周期内单位面积碰撞次数为 $\frac{T_{\text{osc}}}{2} n f(v_z)(v_z - u)$。
   对上、下半周期求平均，单位面积单位时间内入射速度为 $v_z$ 的分子获得的平均功率为：
   $$dP = \frac{1}{2} n f(v_z)\,dv_z \left[(v_z + u)\cdot 2mu(v_z + u) - (v_z - u)\cdot 2mu(v_z - u)\right] = 4nmu^2 v_z f(v_z)\,dv_z$$
   注意括号内 $(v_z+u)^2 - (v_z-u)^2 = 4v_z u$，即每个碰撞分子的**期望能量增益** $\langle\Delta E\rangle = \frac{1}{2}(1 + \frac{u}{v_z})\cdot 2mu(v_z+u) - \frac{1}{2}(1 - \frac{u}{v_z})\cdot 2mu(v_z-u) = 4mu^2$，**严格与分子速度 $v_z$ 无关**！
3. **温度演化与方均根速率翻倍时间**：
   对麦克斯韦分布 $f(v_z) = \sqrt{\frac{m}{2\pi k_B T}} e^{-mv_z^2/(2k_B T)}$（其中 $\frac{k_B T}{m} = \frac{1}{3}v_{\text{rms}}^2$）积分得碰撞通量：
   $$\Phi_{\text{coll}} = n \int_0^\infty v_z f(v_z)\,dv_z = n\sqrt{\frac{k_B T}{2\pi m}} = \frac{n v_{\text{rms}}}{\sqrt{6\pi}}$$
   单位面积气柱总内能为 $U = nH \cdot \frac{1}{2}m v_{\text{rms}}^2$，由能量守恒 $\frac{dU}{dt} = 4mu^2 \Phi_{\text{coll}}$：
   $$n H m v_{\text{rms}} \frac{dv_{\text{rms}}}{dt} = 4mu^2 \frac{n v_{\text{rms}}}{\sqrt{6\pi}} \implies \frac{dv_{\text{rms}}}{dt} = \sqrt{\frac{8}{3\pi}}\frac{u^2}{H} = \text{const}$$
   驚くことに，$v_{\text{rms}}(t)$ 随时间**线性增长**！从初速度 $v$ 翻倍至 $2v$ 所需时间为：
   $$t = \sqrt{\frac{3\pi}{8}}\frac{Hv}{u^2}$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **关键物理洞见与常见失分点**：
  1. **期望能量增益 $\langle\Delta E\rangle = 4mu^2$ 的速度无关性**：一等奖获得者 Siddhaarth Dharani 与我们的盲解完全一致，指出以速度 $v_z$ 飞向活塞的分子遇到下行活塞的概率为 $p_+ = \frac{1}{2} + \frac{u}{2v_z}$，遇到上行活塞的概率为 $p_- = \frac{1}{2} - \frac{u}{2v_z}$，故单次碰撞期望得能 $\langle\Delta E\rangle = p_+ \Delta E_+ + p_- \Delta E_- = 4mu^2$。其中 $2mu^2$ 来自单次碰撞的二阶项 $\frac{1}{2}m(\pm 2u)^2$，另外 $2mu^2$ 来自迎面碰撞概率高于追尾碰撞概率的多普勒通量不对称性！漏掉通量因子 $(v_z \pm u)$ 的参赛者会算出 $2mu^2$，导致最终时间差 2 倍。
  2. **热传导均匀性条件 $\lambda \gg \frac{H^2}{vt}$ 的严格论证**：Kalda 评述强调，25 份无提示正确解答中只有 9 份完整论证了热弛豫时间 $\tau_{\text{diff}} \sim \frac{H^2}{\lambda v} \ll t$（或如 Iaroslav Pozdniak 用傅里叶导热定律证明温差 $\Delta T / T \sim \frac{H^2}{\lambda v t} \ll 1$）。忽略对题给强不等式物理意义的检验是痛失最佳解答奖的主要原因。


---

## 4. `physicscup-2025-q4-reader` — Axis of a lens（理想薄透镜主光轴的纯几何尺规作图）

### 【Phase 1：独立盲解记录】
1. **中心透视（同调变换）与光心未偏折性质**：
   理想薄透镜将物平面上的圆映射为像平面上的实像椭圆。由于通过透镜光心 $O$ 的光线传播方向不发生偏折，像平面上从 $O$ 引出的任意射线与物平面上对应的射线完全重合：
   - 过光心 $O$ 作实像椭圆的两条切线 $t_1, t_2$，切点记为 $T_1', T_2'$。在物平面上，这两条射线同样与物圆相切于原像点 $T_1, T_2$。
   - 作 $\angle T_1' O T_2'$ 的角平分线 $m_O$，与椭圆交于近端 $B'$ 和远端 $A'$。由圆的对称性，物圆圆心必在角平分线 $m_O$ 上，且 $m_O$ 交物圆于近端 $A$ 与远端 $B$（注意实像成在光心 $O$ 另一侧，由薄透镜公式 $\frac{1}{r} + \frac{1}{r'} = \frac{\cos(\theta-\theta_{\text{axis}})}{f}$，物圆上离 $O$ 较近的点 $A$ 对应实像椭圆上离 $O$ 较远的点 $A'$！）。
2. **以 $O$ 为位似中心的试验圆构造与焦平面（焦点线）定位**：
   由于物圆相切于已知射线 $t_1, t_2$，任意一个同样与 $t_1, t_2$ 相切的试验圆 $\tilde{C}$ 都与真实物圆关于光心 $O$ **位似（homothetic）**！
   - 任取 $m_O$ 上一点为圆心作与 $t_1, t_2$ 相切的试验圆 $\tilde{C}$，切点为 $\tilde{T}_1, \tilde{T}_2$，与 $m_O$ 交于近点 $\tilde{A}$、远点 $\tilde{B}$（等价地，$\tilde{A}$ 即等腰三角形 $\triangle O\tilde{T}_1\tilde{T}_2$ 的内心，$\tilde{T}_1\tilde{A}$ 平分 $\angle O\tilde{T}_1\tilde{T}_2$，且 $\tilde{T}_1\tilde{B} \perp \tilde{T}_1\tilde{A}$）。
   - 物平面上的平行线在无穷远处相交，经薄透镜成像后必交于**像方焦平面与图面的交线（焦线 $f_{\text{line}}$）**。特别地，过光心 $O$ 的任意直线在像平面上的像就是其自身！
   - 过 $O$ 作 $m_O$ 的垂线 $l_0$（平行于物弦 $T_1 T_2$），则 $l_0$ 与椭圆切点弦 $T_1' T_2'$ 的交点 $F_0 = l_0 \cap T_1' T_2'$ 必在像方焦线上；
   - 过 $O$ 作平行于 $\tilde{T}_1\tilde{A}$（或 $\tilde{T}_1\tilde{B}$）的直线 $l_A$（或 $l_B$），则它与像弦 $T_1' A'$（或 $T_1' B'$）的交点 $F_A = l_A \cap T_1' A'$（或 $F_B = l_B \cap T_1' B'$）同样位于像方焦线上！
3. **主光轴作图与斜率数值**：
   连接 $F_0 F_A$ 即得像方焦线 $f_{\text{line}}$，过光心 $O$ 作 $F_0 F_A$ 的垂线即为薄透镜的主光轴：
   $$y = ax + b, \qquad a \approx 0.54627393$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Qirui He, Dhruv Shah, Alexandra Stefanova-Razumnaya）的对照**：
  1. **位似法（Homothety）与纯角平分线法的殊途同归**：Kalda 指出，31 份无提示正确解中绝大多数采用了关于光心 $O$ 的位似圆思想；而获得并列最佳解答奖的 Qirui He、Dhruv Shah 与 Alexandra Stefanova-Razumnaya 进一步注意到：在位似圆中，$\angle \tilde{A}\tilde{B}\tilde{T}_1 = \frac{\pi}{4} - \frac{\alpha}{4}$ 仅依赖于两切线夹角 $2\alpha = \angle T_1' O T_2'$，因此无需真正画出辅助圆 $\tilde{C}$，只需通过三次角平分线操作即可直接作出平行于 $AB$、$BC$ 的过 $O$ 射线，从而避免了 GeoGebra 中圆与直线交点重数带来的退化误差。
  2. **实像与虚像的对应点次序陷阱**：在确定 $m_O$ 与椭圆的两个交点 $A', B'$ 谁对应物圆近端时，必须紧扣题干中的“real image（实像）”条件——实像位于光心另一侧，物距越小则像距越大，若将 $A'$ 与 $B'$ 颠倒，会误得虚像对应的伪光轴。

---

## 5. `physicscup-2025-q5-reader` — Satellite Orbit（开普勒轨道的速度端图圆与离心率求解）

### 【Phase 1：独立盲解记录】
1. **哈密顿速度端图圆（Velocity Hodograph）定理**：
   由牛顿万有引力定律 $\frac{d\vec{v}}{dt} = -\frac{GM}{r^2}\hat{r}$ 与角动量守恒 $L = r^2\dot{\theta}$，消去时间微元 $dt$ 得：
   $$d\vec{v} = -\frac{GM}{L}\hat{r}\,d\theta \implies \vec{v}(\theta) = \vec{u}_c + R_h(-\sin\theta\,\hat{x} + \cos\theta\,\hat{y})$$
   即卫星的速度矢量末端在速度空间 $(v_x, v_y)$ 中严格描绘一个半径为 $R_h = \frac{GM}{L}$ 的圆（速度端图圆 $\Gamma$）。设速度原点 $O_v(\vec{v}=\vec{0})$ 到端图圆圆心 $C_h$ 的距离为 $d_c$，由近地点与远地点速度关系 $v_{\max} = R_h + d_c, v_{\min} = R_h - d_c$ 及 $v_{\max} r_{\min} = v_{\min} r_{\max}$ 可知，轨道的离心率即为：
   $$e = \frac{r_{\max} - r_{\min}}{r_{\max} + r_{\min}} = \frac{v_{\max} - v_{\min}}{v_{\max} + v_{\min}} = \frac{d_c}{R_h}$$
2. **速度空间中的三点定圆与圆幂定理**：
   在速度空间中，以速度原点 $O_v$ 为原点，题给三个速度矢量末端 $A, B, C$ 满足：$\vec{v}_1$ 与 $\vec{v}_3$ 反向共线（弦 $AC$ 过原点 $O_v$，长度 $AC = v_1 + v_3$），且 $\vec{v}_2 \perp \vec{v}_1$（即 $O_v B \perp AC$，高 $O_v B = v_2$）。
   - 在直角三角形 $\triangle A O_v B$ 与 $\triangle C O_v B$ 中，斜边长分别为 $AB = \sqrt{v_1^2 + v_2^2}$，$BC = \sqrt{v_2^2 + v_3^2}$。
   - 由三角形外接圆半径公式 $R_h = \frac{AB \cdot BC \cdot CA}{4 S_{\triangle ABC}}$（其中面积 $S_{\triangle ABC} = \frac{1}{2}(v_1 + v_3)v_2$）立即求得速度端图圆半径：
     $$R_h = \frac{(v_1 + v_3)\sqrt{(v_1^2 + v_2^2)(v_2^2 + v_3^2)}}{2(v_1 + v_3)v_2} = \frac{\sqrt{(v_1^2 + v_2^2)(v_2^2 + v_3^2)}}{2v_2}$$
   - 再对速度原点 $O_v$ 应用相交弦定理（圆幂定理）：
     $$R_h^2 - d_c^2 = O_v A \cdot O_v C = v_1 v_3$$
3. **离心率解析式与数值结果**：
   联立两式得轨道离心率为：
   $$e = \frac{d_c}{R_h} = \sqrt{1 - \frac{v_1 v_3}{R_h^2}} = \sqrt{1 - \frac{4 v_1 v_2^2 v_3}{(v_1^2 + v_2^2)(v_2^2 + v_3^2)}}$$
   代入 $v_1 = 1\text{ km/s}, v_2 = 2\text{ km/s}, v_3 = 3\text{ km/s}$，得 $(v_1^2+v_2^2)(v_2^2+v_3^2) = 5 \times 13 = 65$，$4v_1 v_2^2 v_3 = 48$，故：
   $$e = \sqrt{1 - \frac{48}{65}} = \sqrt{\frac{17}{65}} \approx 0.5114083$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Eric Wang, Owen Zhou）的对照**：
  1. **Type-I 标准几何路径**：我们的独立盲解（外接圆半径 $R_h = \frac{abc}{4S}$ 结合圆幂定理 $R_h^2 - d_c^2 = v_1 v_3$）与 Kalda 评述中的“命题人预设最短路径（type-I）”及 Eric Wang 的获奖解答完全一致。
  2. **Owen Zhou 的对称弦免求半径法**：Kalda 特别表扬了 Owen Zhou 的精妙替代方案——将 $B O_v$ 延长交端图圆于 $B'$，由圆幂定理 $|O_v B||O_v B'| = v_1 v_3 \implies |O_v B'| = \frac{v_1 v_3}{v_2}$，从而弦 $BB'$ 中点到 $O_v$ 的纵向偏移为 $d_y = \frac{v_2^2 - v_1 v_3}{2v_2}$，横向偏移为 $d_x = \frac{v_1 - v_3}{2}$，直接由 $d_c^2 = d_x^2 + d_y^2$ 和 $R_h^2 = d_c^2 + v_1 v_3$ 算出 $e$，与我们在盲解阶段同时给出的解析坐标法完全等价。

---

## 6. `physicscup-2026-q1-reader` — Brick between planes（双平面夹持滑块在速度空间中的双曲线轨迹与横向总位移）

### 【Phase 1：独立盲解记录】
1. **双滑动摩擦力叠加与初始加速度定标**：
   设下平面静止（速度 $\vec{0}$），上平面以恒定速度 $\vec{v} = (v, 0)$ 沿 $x$ 轴运动。滑块瞬时速度为 $\vec{u} = (u_x, u_y)$，相对两平面的滑移速度分别为 $\vec{r}_1 = \vec{u}$ 和 $\vec{r}_2 = \vec{u} - \vec{v}$，模长记为 $r_1 = |\vec{u}|, r_2 = |\vec{u} - \vec{v}|$。
   上下两平面正压力及动摩擦因数均相同，设单面摩擦加速度大小为 $\alpha = \frac{\mu N}{m}$，则动力学方程为：
   $$\frac{d\vec{u}}{dt} = -\alpha \left(\frac{\vec{r}_1}{r_1} + \frac{\vec{r}_2}{r_2}\right) = -\alpha (\hat{r}_1 + \hat{r}_2)$$
   在 $t=0$ 时，$\vec{u}(0) = (0, u_0)$，$r_1(0) = u_0$，$r_2(0) = \sqrt{v^2 + u_0^2} \equiv R$，两单位矢量夹角余弦为 $\cos\phi_0 = \frac{u_0}{R}$。由初始加速度大小 $a_0$ 可定出 $\alpha$：
   $$a_0 = \alpha\sqrt{2(1 + \cos\phi_0)} = \alpha\sqrt{\frac{2(R + u_0)}{R}} = \alpha\sqrt{\frac{2s_0}{R}} \implies \alpha = a_0\sqrt{\frac{R}{2s_0}}$$
   其中 $s_0 = R + u_0 = \sqrt{v^2 + u_0^2} + u_0$。
2. **速度空间中的守恒量（共焦双曲线轨迹）**：
   分别将运动方程向 $\hat{r}_1$ 和 $\hat{r}_2$ 方向投影：
   $$\frac{dr_1}{dt} = \hat{r}_1 \cdot \frac{d\vec{u}}{dt} = -\alpha(1 + \hat{r}_1\cdot\hat{r}_2), \qquad \frac{dr_2}{dt} = \hat{r}_2 \cdot \frac{d\vec{u}}{dt} = -\alpha(1 + \hat{r}_1\cdot\hat{r}_2)$$
   两式相减立得惊人守恒律：
   $$\frac{d}{dt}(r_2 - r_1) = 0 \implies d \equiv r_2 - r_1 = \text{const} = \sqrt{v^2 + u_0^2} - u_0 = R - u_0$$
   即滑块在速度空间 $(u_x, u_y)$ 中的轨迹是以 $(0,0)$ 和 $(v,0)$ 为焦点的**双曲线一支**！
3. **椭圆坐标参数化与横向总位移积分**：
   设 $s = r_1 + r_2$，在以 $r_1, r_2, v$ 为三边的速度三角形中，由余弦定理得 $1 + \hat{r}_1\cdot\hat{r}_2 = \frac{s^2 - v^2}{2r_1 r_2} = \frac{2(s^2 - v^2)}{s^2 - d^2}$，故：
   $$\frac{ds}{dt} = -2\alpha(1 + \hat{r}_1\cdot\hat{r}_2) = -4\alpha \frac{s^2 - v^2}{s^2 - d^2}$$
   同时，横向速度 $u_y$ 恰为该速度三角形以 $v$ 为底边的高，由海伦公式得：
   $$u_y = \frac{1}{2v}\sqrt{(s^2 - v^2)(v^2 - d^2)}$$
   当 $t \to \infty$ 时，$u_y \to 0$，滑块达到稳态速度，对应 $s \to v$。将 $dt = -\frac{s^2 - d^2}{4\alpha(s^2 - v^2)}ds$ 代入位移积分：
   $$l_y = \int_0^\infty u_y\,dt = \frac{\sqrt{v^2 - d^2}}{8\alpha v} \int_v^{s_0} \frac{s^2 - d^2}{\sqrt{s^2 - v^2}}\,ds$$
   直接积分并代入 $\sqrt{v^2 - d^2} = \sqrt{2u_0 d} = v\sqrt{2u_0 / s_0}$ 与 $\alpha = a_0\sqrt{R/(2s_0)}$，化简得解析解：
   $$l_y = \frac{1}{4a_0}\sqrt{\frac{u_0}{R}}\left[ \frac{s_0}{2}\sqrt{s_0^2 - v^2} + \left(\frac{v^2}{2} - d^2\right)\operatorname{arcosh}\left(\frac{s_0}{v}\right) \right]$$
   其中 $R = \sqrt{v^2 + u_0^2}, s_0 = R + u_0, d = R - u_0$。代入 $v = u_0 = 1\text{ m/s}, a_0 = 1\text{ m/s}^2$，得：
   $$l_y \approx 0.6631\text{ m}$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Zhuoheng Wu, Alon Hart, Muntean Rares）的对照**：
  1. **完全一致的椭圆坐标积分路径**：我们盲解导出的守恒量 $d = r_2 - r_1$、变量 $s = r_1 + r_2$、三角形高公式 $u_y = \frac{1}{2v}\sqrt{(s^2-v^2)(v^2-d^2)}$ 以及最终解析表达式与一等奖得主吴卓恒（Zhuoheng Wu）的解答逐行吻合！
  2. **几何光学与梯度流诠释**：Alon Hart 与 Jonathan Burger 进一步给出了极具启发性的物理图像——加速度 $\dot{\vec{u}} = -\alpha \nabla_{\vec{u}}(r_1 + r_2)$ 表明速度矢量在势函数 $\Phi(\vec{u}) = r_1 + r_2$（共焦椭圆族）上做最速下降梯度流；由于共焦椭圆族与共焦双曲线族 $r_2 - r_1 = \text{const}$ 处处正交，速度端图必然严格沿着单支共焦双曲线滑向两焦点连线。

---

## 7. `physicscup-2026-q2-reader` — Multi-stream gas flow（正弦速度场波破折叠焦散与多流态形成的动力学判据）

### 【Phase 1：独立盲解记录】
1. **波破时间尺度与拉格朗日柱密度守恒**：
   初始宏观速度场 $v_x(x,0) = v_0\sin(kx)$ 在压缩节点 $kx = \pi$ 附近具有最大负速度梯度 $-kv_0$。将坐标原点平移至该节点，初始速度展开为：
   $$u_0(x_0) = -v_0\sin(kx_0) \approx -kv_0 x_0 + \frac{1}{6}k^3 v_0 x_0^3$$
   在无碰撞极限下，质元轨迹为 $x(x_0, t) = x_0(1 - kv_0 t) + \frac{1}{6}k^3 x_0^3 v_0 t$，波破（折叠焦散）发生于特征时间 $t_0 = \frac{1}{kv_0}$。
   关键洞见在于：无论在 $t \approx t_0$ 时中心区域密度 $n(t)$ 被压缩放大多少倍，初始位于 $[-x_0, +x_0]$ 之间的分子在相互穿越前始终夹在两股流之间，因此单位面积上的**分子柱密度（Column Density）与光学厚度**严格守恒：
   $$N_{\text{col}} = \int_{-x(x_0)}^{x(x_0)} n(x,t)\,dx = 2n x_0 \implies P_{\text{coll}} \sim n r^2 x_0 \sim \frac{x_0}{\lambda_0}$$
   要使来自 $\pm x_0$ 的分子流能穿过焦散区而不因碰撞热化为单峰激波，必须满足无碰撞透明条件 $n r^2 x_0 \lesssim 1$（即 $x_0 \lesssim \lambda_0 \sim (nr^2)^{-1}$）。
2. **一阶线性抵消陷阱与三阶折叠焦散分布**：
   盲解初期容易直觉地认为只需在自由程 $\lambda_0$ 内的初始宏观速度差 $kv_0\lambda_0 \gtrsim v_{\text{th}} = \sqrt{k_B T/m}$。但仔细写出 $x=0$ 处在 $t = t_0 + \delta t$ 时的无碰撞分布函数 $f(0, v_x, t) = f_{\text{MB}}(v_x - u_0(-v_x t))$ 可发现：
   由于到达 $x=0$ 的分子满足 $x_0 = -v_x t$，线性速度项 $-kv_0 x_0$ 在 $t = t_0 = (kv_0)^{-1}$ 时与 $v_x$ **完全抵消**！保留到三次项得：
   $$f(0, v_x, t_0 + \delta t) \propto \exp\left[ -\frac{1}{2v_{\text{th}}^2} \left( \frac{v_x^3}{6v_0^2} - v_x \frac{\delta t}{t_0} \right)^2 \right]$$
   当 $\delta t > 0$ 时，$f(v_x)$ 在 $v_x = 0$ 及 $v_x = \pm v_0\sqrt{6\delta t/t_0}$ 处出现三个极大值，而在 $v_x = \pm v_0\sqrt{2\delta t/t_0}$ 处出现两个极小值。要使峰值至少为谷值的 2 倍，三次速度偏离项必须大于热运动速度 $v_{\text{th}}$（等价于三次折叠位移 $k^2(x_0^*)^3$ 大于热扩散位移 $v_{\text{th}} t_0 = \frac{v_{\text{th}}}{kv_0}$）：
   $$k^2 (x_0^*)^3 \sim \frac{v_{\text{th}}}{kv_0} \implies x_0^* \sim \frac{1}{k}\left(\frac{v_{\text{th}}}{v_0}\right)^{1/3}$$
3. **多流态形成判据**：
   将焦散区特征初始宽度 $x_0^*$ 代入无碰撞透明条件 $n r^2 x_0^* \lesssim 1$，立得：
   $$v_0 \gtrsim \sqrt{\frac{k_B T}{m}} \left(\frac{n r^2}{k}\right)^3 \qquad \left(\text{同时满足题设 } v_0 \gg \sqrt{\frac{k_B T}{m}}\right)$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Alon Hart, Vaibhav V, Joshua Wang）的对照**：
  1. **两种等价推导视角的印证**：
     - **拉格朗日柱密度法（Alon Hart, Vaibhav V）**：先由三次折叠位移与热扩散位移平衡 $k^2(x_0^*)^3 \sim \frac{v_{\text{th}}}{kv_0}$ 确定形成多峰所需的初始气体段宽度 $x_0^*$，再利用柱密度守恒 $N_{\text{col}} = n x_0^*$ 要求碰撞概率 $n r^2 x_0^* \lesssim 1$，完全无需追踪随时间暴涨的局域密度。
     - **欧拉弛豫时间对比法（Joshua Wang）**：在多峰刚刚形成的时刻 $\frac{\delta t}{t_0} \sim \left(\frac{v_{\text{th}}}{v_0}\right)^{2/3}$，局域速度分布宽度为 $\Delta v_x \sim v_{\text{th}}^{1/3} v_0^{2/3}$，局域密度被压缩为 $n_{\text{loc}} \sim n \left(\frac{v_0}{v_{\text{th}}}\right)^{2/3}$。因此局域碰撞弛豫时间为 $\tau_{\text{coll}} \sim (n_{\text{loc}} \Delta v_x r^2)^{-1} \sim \frac{v_{\text{th}}^{1/3}}{v_0^{4/3} n r^2}$；要求多峰形成时间 $\delta t \sim \frac{1}{kv_0}\left(\frac{v_{\text{th}}}{v_0}\right)^{2/3} \lesssim \tau_{\text{coll}}$，同样给出 $v_0 \gtrsim v_{\text{th}} \left(\frac{n r^2}{k}\right)^3$！

---

## 8. `physicscup-2026-q3-reader` — Infinite octagonal LC lattice（无限八边形自对偶 LC 晶格的纯阻输入特性）

### 【Phase 1：独立盲解记录】
1. **旋转对称性与对偶零电位节点识别**：
   将每根径向短路线收缩为四度节点后，整个无限八边形晶格具有严格的 $180^\circ$ 旋转不变性（$L \mapsto L, C \mapsto C$）与 $90^\circ$ 旋转反演性（伴随 $L \leftrightarrow C$ 互换）。
   设最内层八边形（Ring 1）上的四个二度顶点依次为 $A$（上）、$A'$（右）、$B$（下）、$B'$（左），连接 Ring 1 与 Ring 2 的四个四度节点依次为 $W_1, W_2, W_3, W_4$。当在 $A, B$ 间施加对称电压 $V_A = +V_0/2, V_B = -V_0/2$ 时，由 $180^\circ$ 反演反对称性知 $V_{B'} = -V_{A'}$；同时由 $90^\circ$ 旋转对偶性知 $A'$ 与 $B'$ 处于零电势（$V_{A'} = V_{B'} = 0$），且互阻抗 $Z_{(AB),(A'B')} = 0$。
2. **径向自相似重整化（Ring 1 $\to$ Ring 2 剥离递推）**：
   若将最内层 Ring 1 的 8 个元件剥离，剩余的从 Ring 2 向外延伸的无限网络与原网络完全同构，其中四个连接点 $(W_1, W_2, W_3, W_4)$ 在 Ring 2 上恰好扮演了 $(A, A', B, B')$ 在 Ring 1 上的完全相同角色（仅旋转 $45^\circ$ 并互换 $L \leftrightarrow C$）！
   因此，在反对称激励模式下，从 Ring 2 向外的无限网络等效于将每个节点 $W_i$ 通过拉普拉斯导纳 $Y_0(s)$ 连接到零电势参考地（其中原网络在端子 $A$ 相对零电势地的输入导纳亦为 $Y_0(s)$，即总输入阻抗 $Z_{AB}(s) = \frac{2}{Y_0(s)}$）。
3. **五步代数消元与全频段纯阻特性**：
   将 Ring 1 的 8 个元件（电容导纳 $y_C = sC$，电感导纳 $y_L = \frac{1}{sL}$）接回 $(W_1, W_2, W_3, W_4)$：
   - 对节点 $W_1$ 和 $W_4$ 列基尔霍夫电流方程（注意到 $V_{A'} = V_{B'} = 0$）：
     $$V_{W_1} = \frac{y_C}{y_L + y_C + Y_0} V_A, \qquad V_{W_4} = \frac{y_L}{y_L + y_C + Y_0} V_A$$
     （此时流入 $A'$ 的净电流 $y_L V_{W_1} + y_C V_{W_2} = y_L V_{W_1} - y_C V_{W_4} \equiv 0$ 自动满足！）
   - 从端子 $A$ 流入的总电流为：
     $$I_A = y_C(V_A - V_{W_1}) + y_L(V_A - V_{W_4}) = \frac{2 y_L y_C + (y_L + y_C)Y_0}{y_L + y_C + Y_0} V_A$$
   - 由自相似条件 $Y_0 = I_A / V_A$ 得：
     $$Y_0(y_L + y_C + Y_0) = 2 y_L y_C + (y_L + y_C)Y_0 \implies Y_0^2 = 2 y_L y_C = \frac{2C}{L}$$
   频率 $s$ 完全消去！因此等效输入阻抗恒为与频率无关的纯电阻 $Z_{AB} = \frac{2}{Y_0} = \sqrt{\frac{2L}{C}}$。在 $t=0$ 施加恒定电压 $V_0$ 后，输入电流对一切 $t > 0$ 均为常数：
   $$I(t) = V_0 \sqrt{\frac{C}{2L}}$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Alon Hart, Artyom Eryomin, Joshua Wang, Shaocong Sun）的对照**：
  1. **自相似递推法（Joshua Wang）与平面图对偶法（Alon Hart）的辉映**：我们的盲解通过剥离最内层八边形建立自相似方程 $Y_0 = \frac{2y_L y_C + (y_L+y_C)Y_0}{y_L+y_C+Y_0}$，与 Joshua Wang 的获奖解答完全一致。而一等奖得主 Alon Hart 则利用平面图对偶性：将电压源接在 $A, B$ 间且在 $A', B'$ 间叠加旋转 $90^\circ$ 的对偶激励，证明对偶网络的输入阻抗满足 $Z^* = Z / 2$，结合对偶关系 $Z Z^* = L/C$ 一步得出 $Z = \sqrt{2L/C}$。
  2. **复相序对称模分解（Artyom Eryomin, Shaocong Sun）**：通过引入相邻端子相位差为 $\pi/2$（即特征向量 $(1, i, -1, -i)$）的旋转本征模，可将四端子网络约化为单端口递推，提供了处理具有 $C_4$ 旋转对称性的多端无限网络的普适群论工具。

---

## 9. `physicscup-2026-q4-reader` — Water in a rotating container（旋转有孔薄圆盘容器中的离心不稳定性与本征模倍增时间差）

### 【Phase 1：独立盲解记录】
1. **离心不稳定性（倒立摆势能）与局域惯性抵消机制**：
   在共转参考系中，水不可压缩，各孔液面径向微位移 $x_i \ll d$ 满足体积守恒 $\sum_i x_i = 0$。由于表面张力很大且接触角为 $90^\circ$，方孔内液面保持平坦，毛细附加压强对 $x_i$ 无线性恢复力；而离心力对向外位移 $x_i$ 的水柱产生向外的广义力 $F_i = \rho \Omega^2 R d^2 x_i$（对应不稳定势能 $U = -\frac{1}{2}\rho\Omega^2 R d^2 \sum_i x_i^2$）。
   从拔去塞子（微小扰动 $\delta x_0 \lll x$）到液面位移达到宏观小量 $x$ 时，系统已演化出主导的**最快增长指数本征模** $x_i(t) \propto e^{\gamma t}$。从 $x$ 翻倍至 $2x$ 所需时间为 $T = \frac{\ln 2}{\gamma}$，故 $T^2 = \frac{(\ln 2)^2}{\gamma^2} \propto M_{\text{eff}}$。
   由于在每个小孔入口附近（尺度 $r' \sim d \ll R$）流场呈对数汇聚发散 $\propto \ln(R/d)$，单孔局域等效质量 $A_0$ 含对数发散项与孔内水柱质量 $\rho d^3$；但在求 **$T_2^2 - T_1^2$** 时，与容器大尺度几何无关的局域惯性 $A_0$ **严格相消**！同时，增长率 $\gamma \sim \Omega\sqrt{R/d} \gg \Omega$（且二维薄层中科里奥利力有势），故主腔内流场严格为二维无旋势流。
2. **圆盘边界点源的几何定理与流体动能互感矩阵**：
   位于半径为 $R$ 的圆周边界 $\vec{R}_j$ 处的二维点源 $\phi_j(\vec{r}) = -\frac{d \dot{x}_j}{\pi}\ln|\vec{r} - \vec{R}_j|$，由圆周角几何性质 $\frac{\partial}{\partial r}\ln|\vec{r}-\vec{R}_j| = \frac{1}{2R} = \text{const}$，在满足 $\sum_j \dot{x}_j = 0$ 时**自动满足圆周边界法向流速为零的边界条件**！
   由格林公式将动能化为边界积分 $K = \frac{1}{2}\rho d \oint \phi \frac{\partial\phi}{\partial n}ds = \frac{1}{2}\sum_{j,k} A_{jk}\dot{x}_j\dot{x}_k$，得孔间互感矩阵元（$j \ne k$）：
   $$A_{jk} = -\frac{\rho d^3}{\pi} \ln\frac{|\vec{R}_j - \vec{R}_k|}{R}$$
   对正六边形分布的 6 个孔（间隔 $60^\circ$）：邻孔距离 $|\Delta\vec{R}_1| = R \implies A_1 = 0$；次邻孔距离 $|\Delta\vec{R}_2| = \sqrt{3}R \implies A_2 = -\frac{\ln 3}{2\pi}\rho d^3$；对径孔距离 $|\Delta\vec{R}_3| = 2R \implies A_3 = -\frac{\ln 2}{\pi}\rho d^3$。
3. **无隔板与有隔板最快本征模及 $T_2^2 - T_1^2$ 求解**：
   循环矩阵 $A$ 的本征值为 $\lambda_m = A_0 + 2A_1\cos\frac{m\pi}{3} + 2A_2\cos\frac{2m\pi}{3} + A_3(-1)^m$（$m=1,2,3$）：
   - **无隔板情形（$T_1$）**：最小惯性本征值对应交替模 $m=3$（$x_k = (-1)^k x$）：
     $$\lambda_3 = A_0 + 2A_2 - A_3 = A_0 - \frac{\ln(3/2)}{\pi}\rho d^3$$
   - **加 12–6 点钟隔板情形（$T_2$）**：由平面镜象法，半圆腔内（1, 3, 5 点钟三孔）的流动等价于全圆腔中满足左右镜面对称（$x_{11}=x_1, x_9=x_3, x_7=x_5$）且半腔体积守恒 $x_1 + x_3 + x_5 = 0$ 的模式。在 3 点钟孔处位移非零的唯一本征模为 $(x_1, x_3, x_5) = (-1/2, 1, -1/2)x$，恰对应全圆的 $m=2$ 本征模：
     $$\lambda_2 = A_0 - A_2 + A_3 = A_0 - \frac{\ln(4/3)}{2\pi}\rho d^3$$
   因此，倍增时间平方差为：
   $$T_2^2 - T_1^2 = \frac{(\ln 2)^2 (\lambda_2 - \lambda_3)}{\rho \Omega^2 R d^2} = \frac{(\ln 2)^2 \ln(27/16)}{2\pi} \frac{d}{\Omega^2 R}$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Joshua Wang, Vinícius Ferreira Rodrigues, Siddhaarth Dharani）的对照**：
  1. **圆周点源免镜像技巧与格林积分**：我们的盲解与 Joshua Wang 的获奖解答完全一致——利用圆周上点源在其余圆周处法向导数恒为 $\frac{1}{2R}$ 这一几何性质，无需使用圆的反演镜像或无穷傅里叶级数即可直接写出精确势函数；再利用 12–6 隔板将左半圆孔恰好映射为右半圆孔的镜像点，直接复用 $6\times 6$ 循环矩阵的本征值 $\lambda_2$ 与 $\lambda_3$。
  2. **导电薄片焦耳热类比（Siddhaarth Dharani）**：Dharani 指出二维无旋流场的动能正比于均匀导电圆片在边界注入电流 $I_j \propto \dot{x}_j$ 时的焦耳热耗散功率，从而将流体惯性矩阵直接转化为多端电阻网络的阻抗矩阵。

---

## 10. `physicscup-2026-q5-reader` — Crystal Ball（水晶球内荧光染料的全反射囚禁、球差焦散环与散射光能量占比）

### 【Phase 1：独立盲解记录】
1. **弱散射与增透膜下的全反射囚禁机制**：
   微型荧光染料球紧贴水晶球（折射率 $n$，半径 $R = d/2$）后侧内表面，各向同性地向 $4\pi$ 立体角发射可见光。
   由于球面镀有理想增透膜（无部分反射）且球内杂质散射很弱（散射自由程 $\lambda_{\text{scat}} \gg d$）：
   - 任何以入射角 $\theta < \theta_{\text{crit}} = \arcsin(1/n)$ 射向球面的光线（无论向后直接射入紧贴的后壁，还是向前穿过球体射向对侧球面，由等腰三角形对称性知入射角均为 $\theta$）都会在第一次到达球面时**100% 折射穿出球外**，几乎不发生散射；
   - 任何以 $\theta > \theta_{\text{crit}}$ 发射的光线（包含向前和向后两个半球内与法线夹角 $\theta > \theta_{\text{crit}}$ 的圆锥补集）都会发生**全反射（TIR）**；由球对称介质中的克莱罗定理（冲击参数守恒），后续每次碰撞球面的入射角恒保持为 $\theta > \theta_{\text{crit}}$，光线被永久囚禁在球内，直到最终**100% 通过杂质散射离开水晶球**！
   因此，以散射光形式离开水晶球的能量占比严格等于全反射立体角占比：
   $$f_{\text{scat}} = \frac{2 \times 2\pi \cos\theta_{\text{crit}}}{4\pi} = \cos\theta_{\text{crit}} = \sqrt{1 - \frac{1}{n^2}}$$
2. **屏幕光斑的双圆结构（球差折叠焦散环与临界掠射外边界）**：
   设球心在原点，染料位于后顶点 $(-R, 0)$，屏幕位于 $z = b R$。以角度 $\theta < \theta_{\text{crit}}$ 向前发射的光线击中球面点 $(R\cos 2\theta, R\sin 2\theta)$，法线倾角为 $2\theta$，折射角为 $\phi = \arcsin(n\sin\theta)$，出射光线与 $+z$ 轴夹角为 $2\theta - \phi$，打在屏幕上的径向坐标为：
   $$\frac{r(\theta)}{R} = \sin(2\theta) + \left(b - \cos(2\theta)\right)\tan(2\theta - \phi)$$
   当 $\theta$ 从 $0$ 增大到 $\theta_{\text{crit}}$（此时 $\phi = \pi/2$）时：
   - $r(\theta)$ 先从 $0$ 增大到正的极大值 $r_1$（此处 $\frac{dr}{d\theta} = 0$，光线密集汇聚形成**明亮的内圆焦散环**！）；
   - 随后 $r(\theta)$ 减小并在某角 $\theta_0$ 处穿过 $r = 0$（整圈圆锥光线汇聚于轴上一点，形成**内圆正中心的明亮白点**！）；
   - 最后在 $\theta \to \theta_{\text{crit}}$（$\phi \to \pi/2$）时达到负向最大半径 $-r_2$（此处 $\left|\frac{dr}{d\theta}\right| \to \infty$，光强渐近衰减为零，形成**暗淡的外圆边界**！）。
3. **图像像素测量与数值反演**：
   从原图直接测量像素尺寸：比例尺直径 $d = 2R = 454\text{ px}$（即 $R = 227\text{ px}$），亮内圆半径 $r_1 \approx 66.5\text{ px}$（$r_1/R \approx 0.293 \sim 0.295$），暗外圆半径 $r_2 \approx 316.5\text{ px}$（$r_2/R \approx 1.386 \sim 1.394$）。
   联立 $\max_{\theta} \frac{r(\theta)}{R} = \frac{r_1}{R}$ 与 $\frac{|r(\theta_{\text{crit}})|}{R} = \frac{r_2}{R}$ 数值求解得：
   $$n \approx 2.17, \qquad b = \frac{z_{\text{screen}}}{R} \approx 3.71 \sim 3.73$$
   代入散射能量占比公式得：
   $$f_{\text{scat}} = \sqrt{1 - \frac{1}{n^2}} \approx 0.89 \quad (0.887)$$

### 【Phase 2：对照官方评述与获奖解答的教学拆解】
- **与 Jaan Kalda 评述及获奖解（Joshua Wang, Jonathan Burger, Alessandro D'Orazio）的对照**：
  1. **一图定乾坤的极简光线函数分析**：我们的盲解与一等奖得主 Joshua Wang（bonus 0.4 pts）的解答完全一致——通过建立单一光线落点函数 $r(\theta)$，将图像中的亮内环识别为极值焦散面 $\max r(\theta) = r_1$、将外圆边缘识别为全反射临界光线 $|r(\theta_{\text{crit}})| = r_2$，反演出 $n = 2.17$ 并得出 $f_{\text{scat}} = \sqrt{1 - 1/n^2} = 0.887 \approx 0.89$。
  2. **双向逃逸锥的立体角陷阱**：Jonathan Burger 在获奖解中特别强调了紧贴内表面的染料向前后两个半球发射时具有相同的临界角 $\theta_{\text{crit}}$（向后发射且 $\theta > \theta_{\text{crit}}$ 的光线在紧邻表面全反射后转化为向前发射的囚禁光线），若漏算后向半球的逃逸锥或误以为后向光线全部逃逸，会导致散射占比出现严重偏差。
