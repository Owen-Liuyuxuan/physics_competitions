# PLANCKS 2019 中文辅助译文

## plancks-2019-final-problem-slice-q1 | 单层与多层吸附

气体分子吸附到固体表面，是表面物理中的重要问题。假设：(1) 表面有有限个相同的吸附位点；(2) 已吸附分子之间不相互作用；(3) 吸附可逆。原图给出单层吸附（Langmuir 等温线）和多层吸附（BET 等温线）的过程，$p$ 为吸附质的分压。

先考虑只能形成单层的情形。空位点数为 $N_0$，占据位点数为 $N_1$；吸附和脱附速率常数分别为 $k_a,k_d$，平衡常数 $K=k_a/k_d$。吸附速率 $r_a=k_apN_0$，脱附速率 $r_d=k_dN_1$。

(a，2 分) 假设达到平衡，推导覆盖度 $\Theta=N_{\rm ad}/N_{\rm sites}$ 关于 $K,p$ 的表达式。这里 $N_{\rm ad}$ 是被吸附质占据的位点数，$N_{\rm sites}$ 是总位点数。

(b，2 分) 高压、低压极限下 $\Theta$ 分别如何？一半位点被占据时的特征分压 $p_{1/2}$ 是多少？

现在允许多层吸附。$N_i$ 表示恰有 $i$ 个吸附分子叠置的位点数。除前述假设外，再假设：(4) 气体分子只与最上层相互作用；(5) 相互作用只有吸附质—表面及吸附质—吸附质两种。后一种过程的速率常数为 $k'_a,k'_d$，令 $K'=k'_a/k'_d$，$c=K/K'$，$z=K'p$。

(c，2 分) 用递推论证将 $N_i$ 表成 $N_0$ 的函数，特别证明 $i>1$ 时 $N_i=c(K'p)^iN_0=cz^iN_0$。

(d，2 分) 多层情形中，吸附分子总数和表面位点总数分别为 $N_{\rm ad}=\sum_{i=1}^{\infty}iN_i$、$N_{\rm sites}=\sum_{i=0}^{\infty}N_i$。求两者及覆盖度 $\Theta=N_{\rm ad}/N_{\rm sites}$ 的表达式。

(e，2 分) 解释 $K'$ 和 $z$ 的物理意义。多层模型称为 BET 等温线，源自 Brunauer、Emmett、Teller 1938 年的工作。

## plancks-2019-final-problem-slice-q2 | 分束器与光子的量子统计

单个光子不能在线性分束器中简单分成两半；量子力学给出它从不同端口出射的概率。这种最简单的光学装置已能揭示光子的量子统计，也能帮助理解单光子的 Mach–Zehnder 干涉。

练习 1：经典分束器。无损耗分束器有输入复振幅 $E_1,E_2$，输出 $E_3=RE_1+TE_2$、$E_4=TE_1+RE_2$。$R,T$ 是针对场振幅而非强度定义的反射、透射系数。能量守恒要求 $|E_1|^2+|E_2|^2=|E_3|^2+|E_4|^2$。

(a，1 分) 仅有一个输入（$|E_2|=0$）时，证明 $|R|^2+|T|^2=1$。(b，1 分) 两输入相等 $E_1=E_2=E$ 时，证明 $RT^*+TR^*=0$。(原卷再次标为 b，1 分) 证明透射分量与反射分量之间因此有额外的 $\pi/2$ 相位差。

练习 2：用狄拉克符号描述量子分束器。源 A、B 向两个输入模式发射光子，探测器 C、D 对应输出模式。用 $|x\rangle_j$ 表示第 $j$ 个光子所在模式。例如 A 中 $n$ 个光子的态为 $|a\rangle_1\cdots|a\rangle_n$；$|a\rangle_1|b\rangle_2$ 与 $|b\rangle_1|a\rangle_2$ 不同。无损耗 50/50 分束器的变换是
$$|a\rangle\longrightarrow (|c\rangle+i|d\rangle)/\sqrt2,\qquad |b\rangle\longrightarrow(i|c\rangle+|d\rangle)/\sqrt2.$$

(a，2 分) 分别求输入 $|a\rangle$ 和 $|a\rangle_1|a\rangle_2$ 的输出态。单光子在 C、D 被探测到的概率各是多少？双光子都在 C、都在 D、以及 C 和 D 各一个的概率分别是多少？

(b，2 分) 每个输入端口各有一个光子。分别考虑可区分光子 $|a\rangle_1|b\rangle_2$、不可区分玻色光子 $(|a\rangle_1|b\rangle_2+|b\rangle_1|a\rangle_2)/\sqrt2$，以及假想“费米光子”的反对称叠加 $(|a\rangle_1|b\rangle_2-|b\rangle_1|a\rangle_2)/\sqrt2$。求各自输出态及都在 C、都在 D、各一个的概率。

练习 3：Hong–Ou–Mandel 实验。1987 年的实验使两个光子从不同端口入射，并改变源 A 到分束器的距离，调节相对到达时间。原图横轴是该位移；略大于 $300\,\mu\mathrm m$ 时两光子同时到达。符合计数指 C、D 同时各探测到一个光子；在一定延迟窗口内出现明显凹陷，称为 HOM 凹陷。

(a，1 分) 对照练习 1(b)、2(b)，符合计数凹陷说明光子具有怎样的量子统计？(b，1 分) 现代实验可用同一个单光子源，让第一个光子经长光纤延迟后与第二个相遇，再扫描延迟。什么决定凹陷的时间（或距离）宽度？凹陷深度能告诉我们什么？(c，1 分) 如何将 HOM 凹陷与“光子是无相互作用粒子”的说法协调起来？

## plancks-2019-final-problem-slice-q3 | 自由基对的自旋化学

一个自由基对包含两个未配对电子自旋，其中一个电子通过超精细相互作用张量 $\hat A$ 与自旋为 $1/2$ 的原子核耦合。体系处于外磁场 $\mathbf B$ 中。电子对可处于单重态 S 或三重态 T。忽略偶极—偶极及交换相互作用，哈密顿量为
$$\hat H=\mu_Bg\,\mathbf B\cdot\mathbf S_1+\mu_Bg\,\mathbf B\cdot\mathbf S_2+\mu_B\mathbf S_1\cdot\hat A\cdot\mathbf I.$$
其中 $\mathbf I$ 为核自旋算符，$\mathbf S_{1,2}$ 为电子自旋算符。

Q1（1 分）：总自旋的可能取值是什么？Q2（3 分）：写出描述自由基对的全部 8 个总自旋本征基函数 $\psi_i$。Q3（2 分）：给出自由基对单重态与三重态之间允许发生跃迁的条件。

Q4（1 分）：若各向异性超精细张量仅 $A_{zz}=16\,\mathrm G$ 非零，外磁场强度为 $0.5\,\mathrm G$，数值检查上述条件是否满足。Q5（3 分）：若自由基对初始制备于单重态，估算其转变成某个三重态所需的特征时间。

## plancks-2019-final-problem-slice-q4 | 相对论轨道

经典力学中行星绕太阳的轨道是椭圆。考虑狭义相对论效应后，轨道成为旋转椭圆：
$$\frac1r=\frac1{r_0}\{1+\varepsilon\cos[\alpha(\theta-\theta_0)]\},$$
其中 $\alpha=1$ 对应经典结果。

（1 分）证明低速下，质量 $m$ 的物体的相对论动能可近似为 $-mc^2/\gamma$（允许相差一个常量）。

（1 分）利用上一问写出太阳—行星体系的相对论拉格朗日量。

（5 分）推导上述轨道方程，用轨道的基本守恒量（能量、角动量等）表示 $\alpha,r_0$。

（3 分）水星轨道平均半径为 $58\times10^6\,\mathrm{km}$，周期为 88 天。计算一世纪内近日点（距太阳最近的轨道点）的角坐标变化。

## plancks-2019-final-problem-slice-q5 | 橡胶的熵弹性

橡胶由许多彼此交联的长链聚合物构成。分子链的构象数随伸长变化，因此产生熵弹性。以下用随机游走和仿射形变模型研究这一现象；模型示意、原卷中的概率分布及符号定义可对照原图。

练习 1：单条聚合物。将聚合物视为 $N$ 个长度为 $b$ 的步长所组成的随机游走，一端在原点，另一端 $\mathbf R=(x,y,z)$ 的概率密度为 $P(x,y,z;N)=[3/(2\pi Nb^2)]^{3/2}\exp[-3(x^2+y^2+z^2)/(2Nb^2)]$。（1，1 分）推导一维和三维的均方伸长，即 $\langle x^2\rangle$ 和 $\langle R^2\rangle=\langle x^2+y^2+z^2\rangle$。（2，1 分）计算平均空间尺度（均方根端到端距离），并与聚合物轮廓长度 $L=bN$ 比较；后者是可拉伸的最大长度。聚异戊二烯（合成橡胶）的典型参数为 $N=20000,b=8\,\text{Å}$。

在原子力显微镜实验中，链的一端固定于基底，另一端连接悬臂，因此可控制 $\mathbf R$ 并测量链的力 $\mathbf F(\mathbf R)$。宏观态由 $\mathbf R$ 确定，微观态数 $\Omega(\mathbf R)\propto P(x,y,z)$。（3，1 分）忽略内能 $U$ 及与 $\mathbf R$ 无关的项，推导 Helmholtz 自由能 $A(\mathbf R)$，证明力是熵性的，且
$$\mathbf F(\mathbf R)=-\frac{3k_BT}{Nb^2}\mathbf R.$$

练习 2：形变自由能密度。假设网络在未形变状态交联，每条网链均有 $N_s$ 步，初始端到端矢量按高斯分布 $P(x,y,z;N_s)$ 取样。形变后每条链的端点发生均匀仿射变换 $(x,y,z)\mapsto(\lambda_xx,\lambda_yy,\lambda_zz)$，内部单体仍可自由运动。橡胶不可压缩，沿 $x$ 拉伸时 $\lambda_x=\lambda,\lambda_y=\lambda_z=\lambda^{-1/2}$。

（1，1 分）求形变后的平均端到端距离平方 $\langle\lambda_x^2x^2+\lambda_y^2y^2+\lambda_z^2z^2\rangle$。提示：平均仍按交联时的未形变分布进行。（2，1 分）求单条网链平均自由能并证明相对未形变状态的自由能密度为
$$\Delta a(\lambda)=\rho_s[\langle A(\lambda)\rangle-\langle A(1)\rangle]=\frac{\rho_sk_BT}{2}(\lambda^2+2\lambda^{-1}-3).$$
其中 $\rho_s$ 为网链数密度，剪切模量定义为 $G=\rho_sk_BT$。（3，1 分）求 $\rho_s$ 和 $G$。聚异戊二烯密度 $0.830\,\mathrm{g/cm^3}$，每步摩尔质量 $M_0=113\,\mathrm{g/mol}$，每条网链 $N_s=44$ 步，温度取室温。

练习 3：橡皮筋的力—伸长关系。维持长度 $L_x(\lambda)=L_{x1}\lambda$ 所需外力为 $F(\lambda)=d[V\Delta a(\lambda)]/dL_x(\lambda)$，$V$ 为体积；外力与橡胶自身作用力反向。

（1，1 分）未形变尺寸为 $10\,\mathrm{cm}\times0.3\,\mathrm{cm}\times0.3\,\mathrm{cm}$，画出 $F$ 对 $L_x$ 的示意曲线。用上一问的 $G$，或估计 $G=0.5\,\mathrm{MPa}$。（2，1 分）分别求小形变和大形变极限的近似关系。小应变定义为 $\lambda=1+\epsilon,\epsilon\ll1$。（3，1 分）末端悬挂 $1\,\mathrm{kg}$，求平衡长度（按大形变极限）。若用打火机火焰瞬时将其加热到 $500\,\mathrm K$，新的平衡长度是多少？（4，1 分）链不能伸得超过其轮廓长度。仍取大形变极限，以均方根端到端距离等于网链轮廓长度的 50% 为断裂判据，估算临界伸长比 $\lambda_c$。

剪切模量与温度成正比，体现橡胶弹性的熵性。这与大多数材料不同，是 Gough 在 1802 年观察、后来由 Joule 研究的 Joule–Gough 效应。

## plancks-2019-final-problem-slice-q6 | 二维 XY 模型的拓扑相变

2016 年诺贝尔物理学奖表彰了 Kosterlitz、Thouless 和 Haldane 对拓扑物态与拓扑相变的研究。具有连续对称性的低温有序体系，例如铁磁体、向列液晶、量子液体和超导体，可出现点状或线状拓扑缺陷。这里研究二维铁磁体的 $O(2)$ 对称 XY 模型：
$$H=-\frac J2\sum_{\langle ij\rangle}\mathbf S_i\cdot\mathbf S_j,\qquad \mathbf S_i=(\cos\theta_i,\sin\theta_i),\quad J>0.$$

问题 1（2 分）：证明低温时可用原卷式 (3) 的连续模型近似，其角度梯度能为 $\frac K2\int_A d^2x\,\partial_\mu\theta\,\partial_\mu\theta$，并含与构型无关的常数项。$\mu=1,2$，$A$ 为面积，$z$ 为晶格配位数，$K=Jc/2$，$c$ 是与晶格有关、量级为 1 的几何因子，短距离截断 $a$ 为晶格间距。常数项的原卷记号见原图。

问题 2（2 分）：证明低温下能量最有利的角场满足二维 Laplace 方程 $\nabla^2\theta=0$。常数场显然是解。由于自旋的周期性，任意闭合曲线 $C$ 上应有 $\oint_Cd\theta=2\pi q$，$q\in\mathbb Z$。若 $q=0$，场可在曲线内部正规；若 $q\ne0$，内部至少存在一个奇点。$q$ 称为拓扑指数或缺陷强度，具有可加性。

设所有环绕原点的路径具有相同 $q$，用极坐标 $\mathbf x=r(\cos\varphi,\sin\varphi)$；梯度和 Laplace 算符的极坐标表达式见原图。问题 3（1 分）：证明 $\theta(x_1,x_2)=\theta_0+q\varphi=\theta_0+q\tan^{-1}(x_2/x_1)$ 在除原点外的平面满足场方程和上述环路条件。图 2 给出 $\theta_0=0,q=-1,1,2$ 的纹理。问题 4（1 分）：求图 3 两个缺陷的强度。

问题 5（1 分）：计算强度 $q$ 的单缺陷自能，证明 $H=\pi q^2K\ln(R/a)$，其中 $\pi R^2=A$；说明为何 $|q|=1$ 的缺陷占主导。多个缺陷的角场及强度可叠加，图 4 给出示例。

缺陷不被束缚在特定格点，可以移动。问题 6（1 分）：求单缺陷的平移熵。考虑一对强度 $+1,-1$ 的缺陷，总拓扑强度为零，可相互湮灭，也可自发产生；每个的产生能量取上述自能。问题 7（2 分）：求这对缺陷的自由能以及缺陷对能自发产生的临界温度。Kosterlitz 和 Thouless 指出，超过此温度后缺陷大量产生使体系完全无序，并产生无限阶相变。附加思考（0 分）：无限阶相变是什么意思？

## plancks-2019-final-problem-slice-q7 | Higgs 机制

电磁等长程力由无质量规范玻色子传递；弱力等短程力由有质量规范玻色子传递，强度随距离指数衰减。相比 Coulomb 势，Yukawa 势为 $V^{\rm Yuk}(r)=e^{-cMr/\hbar}/(4\pi r)$，其中 $M$ 是传递粒子的质量；它是原点点源对应的标量 Klein–Gordon 方程解。Higgs 机制可在不破坏底层规范对称性的情况下引入规范玻色子质量。

以超导体作类比：进入超导体的磁场指数衰减，即 Meissner–Ochsenfeld 效应。超导电流密度与磁场的 London 方程为 $\nabla\times\mathbf j_s=-(2e)^2n_c\mathbf B/(m_cc^2)$；$n_c=n_e/2$ 为 Cooper 对数密度，$m_c=2m_e$，$n_e$ 为参与超导的电子数密度。这里保留原卷的单位约定和 $c$ 因子，具体公式以原图为准。

(a，2 分) 静态条件 $\partial\mathbf E/\partial t=0$ 下，用 SI 制 Maxwell 方程推导 $\nabla^2\mathbf B=\mu_0e^2n_e\mathbf B/(m_ec^2)=\mathbf B/\lambda^2$，其中 $\lambda$ 为穿透深度。(b，2 分) 设 $\mathbf B=B(x)\mathbf e_z$，求满足 $x\to\infty$ 时磁场消失的解。(c，1 分) 比较 Yukawa 势与所得磁场解，猜测 $\lambda$ 与 $M$ 的关系。

(d，3 分) 在 Coulomb 规范 $\nabla\cdot\mathbf A=0$ 下，由 $\mathbf B=\nabla\times\mathbf A$ 证明 $-\nabla^2\mathbf A=\mu_0\mathbf j_s$。再利用前面结果，选择适当规范并明确写出它，证明有质量矢量场满足原卷式 (13) 的静态 Proca 方程。原卷还说明：含时情况下，可从非齐次波动方程出发，以相同论证得到式 (15) 的 Proca 方程，对应光子获得质量。相关算符及单位系数请对照原图。

(e，2 分) Higgs 机制假定存在真空场，像超导体抑制电磁长程作用那样，使弱相互作用指数衰减，W、Z 玻色子因此有“有效”质量。在自然单位 $\hbar=c=\mu_0=1$ 下，$\mathbf j=-g^2v^2\mathbf A$，$g$ 为耦合强度，$v$ 是势 $V=\mu^2\phi^2+\lambda\phi^4$（$\lambda>0$）的最低点/真空值，$\phi$ 为 Higgs 场。要有非零 $v$，$\mu^2$ 应满足什么条件？测得的规范玻色子质量是什么？可使用前面关联质量图像与表面电流图像的关系。

## plancks-2019-final-problem-slice-q8 | 黑洞照片

本题探讨事件视界望远镜 EHT 合作组刚公布的 M87* 黑洞图像（见原图，2019 年）。

1（2 分）：仅用牛顿力学及光速是普适速度上限这一信息，推导黑洞半径，不使用狭义或广义相对论。与广义相对论在 Schwarzschild 径向坐标中的正确结果 $r_S=2GM/c^2$ 比较。取 $G\approx7\times10^{-11}\,\mathrm{Nm^2/kg^2},c\approx3\times10^8\,\mathrm{m/s}$。为什么牛顿估算也能大致正确？提示：考虑量纲。

2（3 分）：黑洞的“阴影”源于事件视界内的光被捕获；无自转黑洞的视界位于 $r=r_S$。致密天体作为引力透镜会使光偏折，据此解释阴影周围明亮光环的存在。解释中应考虑视界是零超曲面，即光线可保持恒定径向坐标的表面。

3（3 分）：估算分辨 M87* 阴影和光环所需的望远镜尺度。先用第 1 问及质量 $M\approx6\times10^9M_\odot$（$M_\odot\approx2\times10^{30}\,\mathrm{kg}$）估算阴影尺度；距离 $d\approx5\times10^{22}\,\mathrm m$，EHT 观测波长 $\lambda\approx1\,\mathrm{mm}$，口径 $L$ 的角分辨率约为 $\lambda/L$。结合 EHT 实际由南极、南美、北美和欧洲的多座望远镜组成，讨论结果。

4（2 分）：黑洞阴影观测使我们能在“强场区”检验广义相对论。提出量化引力强弱的方法，并与已有大量相对论检验的太阳系比较。可取太阳半径 $r_\odot\approx7\times10^8\,\mathrm m$。

## plancks-2019-final-problem-slice-q9 | 各向异性固体中的电子运动

材料的能量色散为 $\varepsilon(\mathbf k)=\hbar^2[(k_x^2+k_y^2)/m^*+k_z^2/(2m^*)]$，其中 $m^*,2m^*$ 是有效质量，$\mathbf k$ 为电子波矢。考虑位于 Fermi 面上 $\mathbf k_0=(k_x^0,k_y^0,k_z^0)$ 的电子。

(a，1 分) 求电子速度 $\mathbf v=\hbar^{-1}\nabla_{\mathbf k}\varepsilon$。

(b，2 分) 加电场 $\mathbf E=(E,0,0)$，求电子加速度的方向和大小。(c，2 分) 将电场改为 $\mathbf E=(E/\sqrt2,0,E/\sqrt2)$，重新求加速度方向和大小。

(d，3 分) 撤去电场，改加磁场 $\mathbf B=(B,0,0)$，证明波矢分量满足原卷所给的耦合演化关系（$k_x$ 不变，$k_y,k_z$ 互相耦合），确定其中 $\omega_1,\omega_2$。原卷该行导数排印需对照原图，不在译文中擅自修订。

(e，2 分) 由 (d) 证明电子在垂直于 $\mathbf B$ 的平面内振荡，并求振荡频率。

## plancks-2019-final-problem-slice-q10 | 结冰前沿

研究湖水结冰时冰层厚度随时间的变化。冰层导出凝固潜热的速率决定冰层增长速度。首先假设湖在深度方向占据 $0\le x<\infty$，表面位于 $x=0$；水温为凝固温度 $T_m$，冰内温度分布为线性，表面温度恒为 $T_0$，时刻 $t$ 的凝固前沿位于 $X(t)$。

(a，2 分) 求液—固相变释放潜热的速率。(b，2 分) 用热传导定律求通过冰层的热流率。(c，3 分) 进而证明 $X(t)=\sqrt{2Kt}$，并求常数 $K$。

更精确的解析解为 $X(t)=2\lambda\sqrt{\alpha t}$，其中 $\alpha=k/(\rho c)$，$\lambda$ 满足
$$\lambda e^{\lambda^2}\operatorname{erf}(\lambda)=\frac{c(T_m-T_0)}{L\sqrt\pi},\qquad\operatorname{erf}(x)=\frac2{\sqrt\pi}\int_0^xe^{-u^2}du.$$

(d，2 分) 用一阶近似求 $\lambda^2$，证明也得到 (c) 的近似式。(e，1 分) 这个结冰模型若用作熔融钢凝固的第一近似，是否合适？

参数为热导率 $k$、熔化比潜热 $L$、密度 $\rho$、比热 $c$。SI 制数值：冰的 $T_m=273,\rho=900,L=3.3\times10^5,c=2100,k=2.2$；钢的 $T_m=1650,\rho=7900,L=2.7\times10^5,c=450,k=40$。
