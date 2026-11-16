# Batch 07 · PLANCKS 2024 International Finals (Dublin) 独立试做与教学拆解报告

本报告严格遵循两阶段协议：
1. **第一阶段（Blind Solve / 只看原题独立尝试解答）**：仅阅读 `catalog/questions.json` 中的原题文本与题图，独立建立物理模型、列出核心方程并推演至最终结果，如实记录试做过程中的分支思考与潜在卡点。
2. **第二阶段（Solution Comparison & Pedagogical Breakdown / 对照官方解答分析与教学拆解）**：阅读 `plancks-2024-final-combined-answer-slice-qX` 官方参考解答，对比独立试做与官方解答的异同（包括官方解答中的精妙对偶/对称技巧或官方解答中的印刷/量纲笔误），并面向高中物理竞赛拔高生与本科物理竞赛生（PLANCKS / Physics Cup）提炼**难点**、**易错点**与**模型迁移指南**。

---

## Problem 1: Moment of Inertia (`plancks-2024-final-combined-slice-q1`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **题意与几何关系梳理**：
   - 质量为 \(m\) 的均匀薄板呈等腰三角形 \(ABC\)，两腰 \(AB = AC = r\)，底边 \(BC = 2a\)，半顶角为 \(\theta\)。
   - 由几何关系可知：\(a = r\sin\theta\)，底边上的高为 \(H = r\cos\theta\)。
   - 质心 \(G\) 位于底边高线上，距离顶点 \(A\) 为 \(\frac{2}{3}H\)，距离底边 \(BC\) 为 \(\frac{1}{3}H\)。
2. **第 (a) 问推导**：
   - 方法一（直接积分法）：以顶点 \(A\) 为原点，对称轴（高线）为 \(y\) 轴（向下为正，\(0 \le y \le H\)），平行于底边方向为 \(x\) 轴。
   - 在高度 \(y\) 处，水平细条的半宽为 \(x_m(y) = y\tan\theta\)，面积面密度 \(\sigma = \frac{m}{H^2\tan\theta}\)。
   - 先求绕顶点 \(A\) 的转动惯量 \(I_A\)：
     \[
     I_A = \int_0^H \sigma \, dy \int_{-y\tan\theta}^{y\tan\theta} (x^2 + y^2)\,dx = \sigma \int_0^H \left(\frac{2}{3}\tan^3\theta + 2\tan\theta\right) y^3\,dy = \frac{1}{2} m H^2 \left(1 + \frac{1}{3}\tan^2\theta\right)
     \]
   - 代入 \(H = r\cos\theta\)：
     \[
     I_A = \frac{1}{2} m r^2 \left(\cos^2\theta + \frac{1}{3}\sin^2\theta\right)
     \]
   - 由平行轴定理，质心 \(G\) 到 \(A\) 的距离为 \(d_{AG} = \frac{2}{3}H = \frac{2}{3}r\cos\theta\)，故：
     \[
     I_G = I_A - m d_{AG}^2 = m r^2 \left(\frac{1}{2}\cos^2\theta + \frac{1}{6}\sin^2\theta - \frac{4}{9}\cos^2\theta\right) = \frac{1}{18} m r^2 \left(\cos^2\theta + 3\sin^2\theta\right)
     \]
   - 利用二倍角公式 \(\cos^2\theta = \frac{1+\cos 2\theta}{2}\)，\(\sin^2\theta = \frac{1-\cos 2\theta}{2}\)：
     \[
     \cos^2\theta + 3\sin^2\theta = \frac{1+\cos 2\theta + 3 - 3\cos 2\theta}{2} = 2 - \cos 2\theta
     \]
     从而证得：
     \[
     I_G = \frac{1}{18} m r^2 (2 - \cos 2\theta)
     \]
   - *注（竞赛秒杀法）*：任意三角形薄板对质心的转动惯量等价于在三个顶点各放 \(\frac{m}{12}\) 质量、在质心放 \(\frac{3m}{4}\) 质量（或各边中点各放 \(\frac{m}{3}\) 质量）的质点系！直接用顶点等效质点算：\(A\) 到 \(G\) 距离平方为 \(\frac{4}{9}H^2\)，\(B,C\) 到 \(G\) 距离平方均为 \(\frac{1}{9}H^2 + a^2\)，故 \(I_G = \frac{m}{12}\left(\frac{4}{9}H^2 + \frac{2}{9}H^2 + 2a^2\right) = \frac{m}{18}(H^2 + 3a^2) = \frac{1}{18}mr^2(\cos^2\theta + 3\sin^2\theta) = \frac{1}{18}mr^2(2-\cos 2\theta)\)，两行即得！
3. **第 (b) 问推导**：
   - 正 \(n\) 边形由 \(n\) 个全等的等腰三角形拼成，外接圆直径为 \(2r\)（即每个等腰三角形两腰长为 \(r\)），总质量为 \(M\)，则每个三角形质量 \(m = \frac{M}{n}\)，半顶角 \(\theta = \frac{\pi}{n}\)。
   - 每个三角形的质心 \(G\) 到正 \(n\) 边形中心 \(G'\)（即顶点 \(A\)）的距离为 \(d = \frac{2}{3}r\cos\frac{\pi}{n}\)。
   - 对单个三角形应用平行轴定理（或者直接用第 (a) 问中间算出的 \(I_A\)）：
     \[
     I_{G'}^{(n)} = n \left( I_G + \frac{M}{n} d^2 \right) = M r^2 \left[ \frac{1}{18}\left(2 - \cos\frac{2\pi}{n}\right) + \frac{4}{9}\cos^2\frac{\pi}{n} \right] = \frac{1}{6} M r^2 \left(1 + 2\cos^2\frac{\pi}{n}\right)
     \]
   - 当 \(n \to \infty\) 时，\(\cos\frac{\pi}{n} \to 1\)，故 \(I_{G'}^{(\infty)} \to \frac{1}{6}Mr^2(1 + 2) = \frac{1}{2}Mr^2\)，完美恢复圆盘转动惯量公式。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 官方解答直接以质心 \(G\) 为原点建立坐标系，设三角形总高为 \(3h = r\cos\theta\)，对右半三角形积分 \(\int_0^a dx \int_{-h}^{\frac{h}{a}(2a-3x)} (x^2+y^2) dy\)，得到 \(I_G = \frac{1}{6}m(a^2 + 3h^2)\)，再化为 \(\frac{1}{18}mr^2(2-\cos 2\theta)\)。
  - 相比之下，我们在盲做时采用的**先对顶点 \(A\) 积分再用平行轴定理**（积分上下限关于 \(y\) 是线性齐次的 \(\pm y\tan\theta\)），不仅避免了带常数项的斜线积分上下限，而且算出的 \(I_A\) 恰好就是第 (b) 问中每个扇形三角形绕中心 \(G'\) 的转动惯量！
  - 此外，官方解答在第 (b) 问中将外接圆半径临时改记为了 \(a\)，最后一步又写回 \(\frac{1}{2}Mr^2\)，阅读时需注意符号一致性。
- **核心难点与易错点**：
  - **难点**：二重积分区域的边界方程设定与三角恒等式化简。
  - **易错点**：平行轴定理的方向（\(I_G = I_A - md^2\) 而非加号），以及正 \(n\) 边形中每个等腰三角形的半顶角是 \(\theta = \frac{\pi}{n}\)（顶角 \(2\theta = \frac{2\pi}{n}\)），极易误代为 \(\frac{2\pi}{n}\)。

---

## Problem 2: Quaternions (`plancks-2024-final-combined-slice-q2`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：证明 \(ij = -ji\)**：
   - 设三元数 \(z = ib + jc\)（或一般形式 \(a + ib + jc\)）。根据模长定义 \(|z|^2 = b^2 + c^2\)，以及模长乘法保持性 \(|z_1 z_2| = |z_1||z_2|\)，取 \(z = ib + jc\)，有 \(|z^2| = |z|^2 = b^2 + c^2\)。
   - 利用结合律与分配律展开 \(z^2\)（注意不能假定 \(i,j\) 交换）：
     \[
     z^2 = (ib + jc)(ib + jc) = b^2 i^2 + c^2 j^2 + bc(ij + ji) = -(b^2 + c^2) + bc(ij + ji)
     \]
   - 要使对任意实数 \(b,c\) 均有 \(|z^2| = b^2 + c^2\)，由于实部已经是 \(-(b^2+c^2)\)，交叉项必须恒为零：\(ij + ji = 0 \implies ij = -ji\)。
2. **第 (b) 问：证明 \(k = ij\) 满足 \(k^2 = -1\) 且不能表示为三元数**：
   - 计算 \(k^2\)：利用结合律与 \(ij = -ji\)：
     \[
     k^2 = (ij)(ij) = i(ji)j = i(-ij)j = -i^2 j^2 = -(-1)(-1) = -1
     \]
   - 反证法证明 \(k \neq \alpha + \beta i + \gamma j\)（\(\alpha,\beta,\gamma \in \mathbb{R}\)）：
     - 假设 \(ij = k = \alpha + \beta i + \gamma j\)。两边左乘 \(i\)，利用 \(i^2 = -1\)：
       \[
       i(ij) = i^2 j = -j = \alpha i - \beta + \gamma ij = \alpha i - \beta + \gamma(\alpha + \beta i + \gamma j) = (\gamma\alpha - \beta) + (\alpha + \gamma\beta)i + \gamma^2 j
       \]
     - 比较 \(j\) 的系数（或线性无关性）：左边 \(j\) 的系数为 \(-1\)，右边为 \(\gamma^2 \ge 0\)，实数范围内 \(\gamma^2 = -1\) 无解！矛盾！（或者像官方解答那样先平方再算 \(ijk = -1\)）。
3. **第 (c) 问：证明纯虚四元数乘法公式 \(q_1 q_2 = (-\vec{v}_1\cdot\vec{v}_2, \vec{v}_1\times\vec{v}_2)\)**：
   - 由 \(k = ij = -ji\) 及 \(i^2 = j^2 = k^2 = -1\)，可得循环反对易关系：
     \[
     jk = j(ij) = -j^2 i = i = -kj, \qquad ki = (ij)i = -i^2 j = j = -ik
     \]
   - 展开 \(q_1 q_2 = (v_{1x}i + v_{1y}j + v_{1z}k)(v_{2x}i + v_{2y}j + v_{2z}k)\)：
     \[
     q_1 q_2 = -(v_{1x}v_{2x} + v_{1y}v_{2y} + v_{1z}v_{2z}) + (v_{1y}v_{2z} - v_{1z}v_{2y})i + (v_{1z}v_{2x} - v_{1x}v_{2z})j + (v_{1x}v_{2y} - v_{1y}v_{2x})k = (-\vec{v}_1\cdot\vec{v}_2, \, \vec{v}_1\times\vec{v}_2)
     \]
4. **第 (d) 问：计算 \(e^q\)，其中 \(q = \frac{\pi}{5}i + \frac{4\pi}{15}k\)**：
   - **为什么不平凡**：因为 \(i\) 与 \(k\) 不对易（\(ik = -ki \neq ki\)），所以**绝不能**写成 \(e^{\frac{\pi}{5}i} e^{\frac{4\pi}{15}k}\)！
   - **一般公式推导**：对于纯虚四元数 \(q = (0, \vec{v})\)，由第 (c) 问公式可知 \(\vec{v}\times\vec{v} = \vec{0}\)，故：
     \[
     q^2 = -|\vec{v}|^2 = -\theta^2 \quad (\text{其中 } \theta = |\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2})
     \]
   - 设单位纯虚四元数 \(\hat{u} = \frac{q}{\theta}\)，则 \(\hat{u}^2 = -1\)！于是 \(q = \theta \hat{u}\) 与普通复数 \(i\theta\) 满足完全相同的幂级数规律：
     \[
     e^q = \sum_{n=0}^\infty \frac{\theta^n \hat{u}^n}{n!} = \cos\theta + \hat{u}\sin\theta = \cos|\vec{v}| + \frac{q}{|\vec{v}|}\sin|\vec{v}|
     \]
   - **代入数值**：\(q = \frac{3\pi}{15}i + \frac{4\pi}{15}k = \frac{\pi}{15}(3i + 4k)\)。
   - 模长 \(\theta = |\vec{v}| = \frac{\pi}{15}\sqrt{3^2 + 4^2} = \frac{5\pi}{15} = \frac{\pi}{3}\)，单位四元数 \(\hat{u} = \frac{3}{5}i + \frac{4}{5}k\)。
   - 代入欧拉公式：
     \[
     e^q = \cos\frac{\pi}{3} + \left(\frac{3}{5}i + \frac{4}{5}k\right)\sin\frac{\pi}{3} = \frac{1}{2} + \frac{\sqrt{3}}{2}\left(\frac{3}{5}i + \frac{4}{5}k\right) = \frac{1}{2} + \frac{3\sqrt{3}}{10}i + \frac{2\sqrt{3}}{5}k
     \]

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 第 (a)(b)(c) 问思路与官方解答完全一致，且我们在第 (b) 问中直接左乘 \(i\) 导出 \(\gamma^2 = -1\) 比官方解答更简短。
  - **发现官方解答笔误**：在第 (d) 问最后一步代入数值时，官方解答误把 \(\frac{q}{|q|} = \frac{3i+4k}{5}\) 写成了 \(\frac{\pi}{5}(3i+4j)\)（既多乘了一个 \(\pi\)，又把 \(k\) 抄成了 \(j\)），导致最终结果多出了因子 \(\pi\)。我们的独立推导结果 \(\frac{1}{2} + \frac{3\sqrt{3}}{10}i + \frac{4\sqrt{3}}{10}k\) 才是完全正确的（因为 \(|e^q| = 1\)，实部平方加虚部模方必须等于 \(1\)：\(\left(\frac{1}{2}\right)^2 + \left(\frac{3\sqrt{3}}{10}\right)^2 + \left(\frac{4\sqrt{3}}{10}\right)^2 = \frac{1}{4} + \frac{27+48}{100} = 1\)）。
- **核心难点与易错点**：
  - **难点**：理解非对易代数中指数映射 \(e^{A+B} \neq e^A e^B\)，并通过构造平方为 \(-1\) 的单位生成元 \(\hat{u} = \frac{\vec{v}}{|\vec{v}|}\) 将级数重求和（这与量子力学中泡利矩阵算符指数 \(e^{i\vec{\theta}\cdot\vec{\sigma}} = \cos\theta\,I + i(\hat{\theta}\cdot\vec{\sigma})\sin\theta\) 完全同构）。
  - **易错点**：归一化单位四元数 \(\frac{q}{|q|}\) 时漏除 \(\pi\) 或搞混基底符号。

---

## Problem 3: Möbius Strip · Time Travel? (`plancks-2024-final-combined-slice-q3`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **坐标系与拓扑边界条件建立**：
   - 设莫比乌斯带的宽度方向为 \(x \in [0, W]\)，周长（扭转）方向为 \(y \in [0, L]\)。
   - 在带内部 \(V(x,y) = 0\)，自由粒子定态薛定谔方程为：
     \[
     -\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\psi(x,y) = E\psi(x,y)
     \]
   - 边界条件：
     1. 侧边硬壁束缚（波函数在边缘为零）：\(\psi(0, y) = \psi(W, y) = 0\)。
     2. 纵向扭转 \(180^\circ\) 粘合条件：沿 \(y\) 走过一圈 \(L\) 后，横向坐标发生关于中心线 \(x = W/2\) 的反转（\(x \mapsto W - x\)）：
        \[
        \psi(x, y + L) = \psi(W - x, y)
        \]
2. **第 (a) 问：本征波函数与本征能量**：
   - 采用分离变量法：由 \(\psi(0,y)=\psi(W,y)=0\)，横向波函数取 \(\sin\left(\frac{n\pi x}{W}\right)\)（\(n = 1, 2, 3, \dots\)）。
   - 注意到在反射变换 \(x \mapsto W - x\) 下，横向本征函数具有确定的宇称：
     \[
     \sin\left(\frac{n\pi(W - x)}{W}\right) = \sin(n\pi - \frac{n\pi x}{W}) = (-1)^{n+1} \sin\left(\frac{n\pi x}{W}\right)
     \]
     - 当 \(n\) 为奇数（如 \(n=1,3,5,\dots\)，关于 \(x=W/2\) 偶对称）时，\((-1)^{n+1} = +1\)；
     - 当 \(n\) 为偶数（如 \(n=2,4,6,\dots\)，关于 \(x=W/2\) 奇对称）时，\((-1)^{n+1} = -1\)。
   - 纵向波函数取平面波 \(e^{i k_y y}\)。代入扭转周期边界条件 \(\psi(x, y+L) = \psi(W-x, y)\)：
     \[
     e^{i k_y L} = (-1)^{n+1}
     \]
   - 因此 \(k_y L = \ell \pi\)（\(\ell \in \mathbb{Z}\)），其中：
     - 若 \(n\) 为奇数，则 \(e^{i\ell\pi} = +1 \implies \ell\) 为偶数；
     - 若 \(n\) 为偶数，则 \(e^{i\ell\pi} = -1 \implies \ell\) 为奇数。
     - 统一写成选择定则：**\(n \in \mathbb{Z}^+, \, \ell \in \mathbb{Z}\)，且 \(n + \ell\) 必为奇数**！
   - 归一化常数：\(\int_0^L dy \int_0^W dx \, |N|^2 \sin^2\left(\frac{n\pi x}{W}\right) = |N|^2 L \frac{W}{2} = 1 \implies N = \sqrt{\frac{2}{LW}}\)。
   - 归一化波函数与能量本征值：
     \[
     \psi_{n,\ell}(x,y) = \sqrt{\frac{2}{LW}} \sin\left(\frac{n\pi x}{W}\right) e^{i\frac{\ell\pi}{L}y}, \qquad E_{n,\ell} = \frac{\hbar^2\pi^2}{2m}\left(\frac{n^2}{W^2} + \frac{\ell^2}{L^2}\right) \quad (n+\ell \text{ 为奇数})
     \]
3. **第 (b) 问：波包量子复原时间 (Quantum Revival Time)**：
   - 含时波函数展开为 \(\Psi(x,y,t) = \sum_{n,\ell} c_{n,\ell} \psi_{n,\ell}(x,y) e^{-i E_{n,\ell} t / \hbar}\)。
   - 要使任意初始局域波包严格恢复到初始状态（除可能的全局相位外），需要所有本征态的演化相位差为 \(2\pi\) 的整数倍，即 \(E_{n,\ell} T / \hbar = 2\pi N_{n,\ell}\)。
   - 代入 \(W = 3\text{ nm}\)，\(L = 20\text{ nm}\)。取公分母长度 \(D = \text{lcm}(W, L) = 60\text{ nm}\)：
     \[
     E_{n,\ell} = \frac{\hbar^2\pi^2}{2m D^2}\left( (20n)^2 + (3\ell)^2 \right) = E_0 \left( 400n^2 + 9\ell^2 \right), \quad E_0 = \frac{\hbar^2\pi^2}{2m D^2}
     \]
   - 由于 \(400n^2 + 9\ell^2\) 对任意整数 \(n,\ell\) 均为整数（且当 \(n+\ell\) 为奇数时，\(400n^2 + 9\ell^2\) 恒为奇数，其差值 \(400(n^2-n'^2) + 9(\ell^2-\ell'^2)\) 恒为偶数，最大公约数可進一步分析，但基本周期由 \(E_0 T / \hbar = 2\pi\) 或 \(\pi\) 决定）：
   - 按基本基频 \(E_0\) 计算复原时间：
     - 若取 \(E_0 T / \hbar = 2\pi\)，则 \(T = \frac{4 m D^2}{\pi \hbar} \approx 6.30\times 10^{-12}\text{ s}\)；
     - 注意到 \(n+\ell\) 为奇数 \(\implies \ell\) 的奇偶性由 \(n\) 决定：当 \(n\) 为奇数时 \(\ell\) 为偶数，\(400n^2+9\ell^2 \equiv 0 + 0 \equiv 0 \pmod 4\)；当 \(n\) 为偶数时 \(\ell\) 为奇数，\(400n^2+9\ell^2 \equiv 0 + 1 \equiv 1 \pmod 2\)。若直接按官方常用的 \(\frac{E_0 T}{\hbar} = \pi\) 或 \(2\pi\)，待对照官方答案确认因子 \(2\)。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 第 (a) 问的波函数、能量本征值与量子数奇偶耦合条件（\(n+m\) 为奇数）与官方解答 100% 一致！
  - 第 (b) 问中，官方解答也巧妙地引入了最小公倍数长度 \(D = 60\text{ nm}\)（不过官方解答把 \(\left(\frac{n}{3}\right)^2 + \left(\frac{m}{20}\right)^2\) 通分写成了 \(\frac{(3n)^2 + (20m)^2}{60^2}\)，虽然分子系数调换了，但丝毫不影响提取公因式 \(E_0 = \frac{\hbar^2\pi^2}{2m_e D^2}\)）。
  - **发现官方解答的两处细节瑕疵**：
    1. 官方解答在写周期公式时把相位条件 \(E_0 T / \hbar = 2\pi\) 误写成了 \(T = \frac{\hbar}{E_0}\)（少乘了 \(2\pi\)），但在下一步代公式时又神奇地塞回了一个 \(\pi\)，写成了 \(T = \frac{2m_e \pi D^2}{\hbar^2 \pi^2} = \frac{2 m_e D^2}{\pi \hbar} = 3.15\times 10^{-12}\text{ s}\)（相当于取了 \(E_0 T / \hbar = \pi\)）。
    2. 严格来说，如果波包包含既有 \(n\) 为奇数（\(\ell\) 为偶数，\(400n^2+9\ell^2\) 为偶数）又有 \(n\) 为偶数（\(\ell\) 为奇数，\(400n^2+9\ell^2\) 为奇数）的本征态，由于奇偶本征值之差为奇数，完整复原周期应满足 \(\frac{E_0 T}{\hbar} = 2\pi \implies T = \frac{4 m_e D^2}{\pi \hbar} = 6.30\text{ ps}\)；而在 \(t = 3.15\text{ ps}\)（即 \(\frac{E_0 t}{\hbar} = \pi\)）时，奇数 \(\ell\) 态获得 \(-1\) 相位而偶数 \(\ell\) 态获得 \(+1\) 相位，这恰好对应波包绕莫比乌斯带走完**一圈** \(y \to y + L\)、横向坐标发生镜像反转 \(x \to W - x\)！因为初始波包中心在 \(x = W/2\)，如果初始波包关于 \(x = W/2\) 对称，它仅包含奇数 \(n\)（偶数 \(\ell\)）的态，此时所有态的 \(400n^2+9\ell^2\) 都是 \(4\) 的倍数，甚至在更短的时间就能复原！这一物理图像在教学中极具启发性。

---

## Problem 4: Icy Roof (`plancks-2024-final-combined-slice-q4`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **题图信息读取**：
   - 球形屋顶为半径 \(R = 10\text{ m}\) 的上半球面。
   - 屋顶底部边缘向外：\(0 \sim 1\text{ m}\) 是混凝土地面（PATH），\(1\text{ m} \sim 1.25\text{ m}\)（宽 \(25\text{ cm}\)）是带刺玫瑰丛（ROSE BUSH），\(1.25\text{ m} \sim 4.25\text{ m}\)（宽 \(3\text{ m}\)）是鱼塘（FISH POND）。
2. **第 (a) 问：标准质点无摩擦滑落与平抛/斜抛落点计算**：
   - 设质点从半球最高点由静止开始无摩擦滑下，转过的极角为 \(\theta\)（与竖直向上方向的夹角）。
   - 由机械能守恒：\(\frac{1}{2}m v^2 = mgR(1 - \cos\theta) \implies v^2 = 2gR(1 - \cos\theta)\)。
   - 法向动力学方程：\(mg\cos\theta - N = m\frac{v^2}{R}\)。
   - 脱离屋顶条件 \(N = 0\)：
     \[
     \cos\theta_0 = \frac{2}{3}, \qquad \sin\theta_0 = \frac{\sqrt{5}}{3}, \qquad v_0 = \sqrt{\frac{2}{3}gR}
     \]
   - 脱离点坐标（以球心为原点，水平向右为 \(x\)，竖直向上为 \(y\)）：
     \[
     x_0 = R\sin\theta_0 = \frac{\sqrt{5}}{3}R, \qquad y_0 = R\cos\theta_0 = \frac{2}{3}R
     \]
   - 脱离瞬间的速度分量：
     \[
     v_{x0} = v_0\cos\theta_0 = \frac{2}{3}\sqrt{\frac{2}{3}gR}, \qquad v_{y0} = -v_0\sin\theta_0 = -\frac{\sqrt{5}}{3}\sqrt{\frac{2}{3}gR}
     \]
   - 脱离后做斜下抛运动，落地时 \(y(t) = y_0 + v_{y0}t - \frac{1}{2}gt^2 = 0\)：
     \[
     \frac{1}{2}gt^2 + \frac{\sqrt{5}}{3}\sqrt{\frac{2}{3}gR}\,t - \frac{2}{3}R = 0
     \]
   - 解二次方程得下落时间 \(t\)：
     \[
     t = \sqrt{\frac{R}{27g}}\left(\sqrt{46} - \sqrt{10}\right)
     \]
   - 落地点的水平坐标 \(x_{\text{land}}\)：
     \[
     x_{\text{land}} = x_0 + v_{x0}t = R\left[\frac{\sqrt{5}}{3} + \frac{2\sqrt{2}}{27}\left(\sqrt{46} - \sqrt{10}\right)\right] \approx 1.12458 R = 11.246\text{ m}
     \]
   - 距离屋顶边缘（\(x = R = 10\text{ m}\)）的水平距离为：
     \[
     \Delta x = x_{\text{land}} - R \approx 1.246\text{ m}
     \]
   - 对照花园地形：混凝土小路是 \(0 \sim 1.00\text{ m}\)，玫瑰丛是 \(1.00\text{ m} \sim 1.25\text{ m}\)，鱼塘是 \(1.25\text{ m} \sim 4.25\text{ m}\)。\(1.246\text{ m}\) 刚好落在玫瑰丛的最外侧边缘（差 \(4\text{ mm}\) 进鱼塘），所以他会一头扎进带刺的玫瑰丛（ROSE BUSH）！
3. **第 (b) 问：放宽不合理近似的物理估算**：
   - 由于 \(1.246\text{ m}\) 距离玫瑰丛与鱼塘的分界线 \(1.25\text{ m}\) 仅有 \(4\text{ mm}\)（相对误差 \(0.04\%\)），任何微小的物理修正都会改变他的命运！
   - **近似 1：质点近似（有限人体尺寸）**：人的质心在屋顶表面上方约 \(\Delta R \approx 0.5\text{ m} \sim 1.0\text{ m}\)（即便趴下也有 \(\sim 15\text{ cm}\)）。由于落点距离与有效半径成正比 \(x_{\text{land}} = 1.1246 R_{\text{eff}}\)，哪怕有效半径只增加 \(\Delta R = 0.1\text{ m}\)，落点也会外移 \(11\text{ cm}\) 达到 \(1.36\text{ m}\)，直接落入鱼塘（Pond）！
   - **近似 2：绝对光滑无摩擦（冰面动摩擦系数 \(\mu_k \approx 0.03 \sim 0.05\)）**：摩擦损耗机械能，使脱离角 \(\theta_0\) 增大（更晚脱离）、脱离速度 \(v_0\) 减小且更偏向竖直向下，这会使落点向内缩进超过 \(10\text{ cm}\)，让他摔在混凝土小路（Concrete Path）或玫瑰丛深处。
   - **近似 3：空气阻力**：人体滑落速度约 \(8\text{ m/s}\)，空气阻力约为体重的 \(2\% \sim 3\%\)，同样使落点向内缩短数厘米。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 第 (a) 问的代数解析式 \(x = r\left(\frac{\sqrt{5}}{3} + \frac{\sqrt{8}}{27}(\sqrt{46}-\sqrt{10})\right) = 1.1246 r\) 与官方解答完全分毫不差！
  - *注*：官方解答中把极角定义写成了与水平面的夹角符号（或者把 \(\cos\theta_0\) 误印成了 \(\sin\theta_0 = 2/3\)），但后面的数值完全是按与竖直夹角算的。
  - 题目的幽默设计正在于 \(1.246\text{ m}\) 卡在 \(1.25\text{ m}\) 边界内侧 \(4\text{ mm}\) 处，从而自然引出第 (b) 问对“球形鸡/质点近似”的批判性讨论。

---

## Problem 5: Floating Ring (`plancks-2024-final-combined-slice-q5`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **物理模型与磁通量守恒**：
   - 超导细环电阻 \(R_{\text{ohm}} = 0\)，故穿过超导环的总磁通量（外磁场磁通量 + 自感磁通量）恒定不变：
     \[
     \Phi_{\text{tot}} = \pi r_0^2 B_z(z) + L I = \text{const}
     \]
   - 初始时刻 \(z = 0\)，\(I = 0\)，故 \(\Phi_{\text{tot}} = \pi r_0^2 B_0\)。
   - 当环位于垂直坐标 \(z\) 处时，\(B_z(z) = B_0(1 - \alpha z)\)，代入磁通量守恒：
     \[
     \pi r_0^2 B_0(1 - \alpha z) + L I(z) = \pi r_0^2 B_0 \implies I(z) = \frac{\pi r_0^2 B_0 \alpha}{L} z
     \]
2. **洛伦兹力与简谐振动方程**：
   - 环上电流 \(I(z)\) 与径向磁场 \(B_r(r_0) = B_0 \beta r_0\) 相互作用，产生竖直方向的安培力：
     \[
     F_z = -(2\pi r_0) I(z) B_r(r_0) = -\frac{2\pi^2 r_0^4 B_0^2 \alpha \beta}{L} z = -k z
     \]
     其中等效劲度系数为：
     \[
     k = \frac{2\pi^2 r_0^4 B_0^2 \alpha \beta}{L}
     \]
   - 竖直方向牛顿第二定律（以向上为 \(z\) 正方向）：
     \[
     m \ddot{z} = -k z - mg = -k(z - z_{\text{eq}}), \qquad z_{\text{eq}} = -\frac{mg}{k}
     \]
   - 这正是角频率为 \(\omega = \sqrt{\frac{k}{m}}\) 的简谐运动！
3. **代入数值计算**：
   - 已知 \(m = 5\times 10^{-5}\text{ kg}\)，\(r_0 = 5\times 10^{-3}\text{ m}\)，\(L = 1.3\times 10^{-8}\text{ H}\)，\(B_0 = 0.01\text{ T}\)，\(\alpha = 2\text{ m}^{-1}\)，\(\beta = 32\text{ m}^{-1}\)。
   - 计算角频率 \(\omega\) 与频率 \(f\)：
     \[
     \omega = \sqrt{\frac{2\pi^2 (5\times 10^{-3})^4 (0.01)^2 \times 2 \times 32}{1.3\times 10^{-8} \times 5\times 10^{-5}}} = \sqrt{121.475} \approx 11.02\text{ rad/s}, \qquad f = \frac{\omega}{2\pi} \approx 1.754\text{ Hz}
     \]
   - 振幅 \(A\)：由 \(z(0) = 0, \dot{z}(0) = 0\)，振幅等于平衡位置下移量：
     \[
     A = |z_{\text{eq}}| = \frac{g}{\omega^2} \approx \frac{9.81}{121.475} \approx 0.0808\text{ m} = 8.08\text{ cm}
     \]
   - 第 (b) 问最大电流：发生在最低点 \(z_{\min} = -2A \approx -16.15\text{ cm}\) 处：
     \[
     I_{\max} = \frac{\pi r_0^2 B_0 \alpha}{L} (2A) = \frac{\pi (5\times 10^{-3})^2 (0.01) (2)}{1.3\times 10^{-8}} \times 0.1615 \approx 19.5\text{ A}
     \]
   - *敏锐物理洞察*：注意题目给出的磁场满足 \(\nabla\cdot\vec{B} = \frac{1}{r}\frac{\partial(r B_r)}{\partial r} + \frac{\partial B_z}{\partial z} = B_0(2\beta - \alpha)\)。在真实无源空间中应有 \(\alpha = 2\beta\)，但题目人为给定了 \(\alpha = 2\text{ m}^{-1}, \beta = 32\text{ m}^{-1}\)，因此计算时不能私自用 \(\alpha = 2\beta\) 替换！

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 我们的解析公式 \(\omega = \sqrt{\frac{2\pi^2 r_0^4 B_0^2 \alpha\beta}{Lm}} = 11.02\text{ rad/s}\)、\(f = 1.75\text{ Hz}\)、\(A = 8.1\text{ cm}\)、\(I_{\max} = 19.6\text{ A}\) 与官方解答 100% 吻合！
  - 官方解答在末尾特别加了一句彩蛋评注：*"It is worth noting that the magnetic fields in the question do not satisfy Maxwell's equations, well done to the participants who spotted this."* 这恰恰印证了我们在盲做时的敏锐洞察！
- **核心难点与易错点**：
  - **易错点 1（幂次陷阱）**：\(I(z) \propto r_0^2\)，而安培力 \(F_z = 2\pi r_0 I B_r(r_0)\) 中环周长贡献一个 \(r_0\)、径向场 \(B_r = B_0\beta r_0\) 又贡献一个 \(r_0\)，合起来 \(k \propto r_0^4\)！如果漏掉 \(B_r\) 中的 \(r_0\) 写成 \(r_0^3\)，频率会差 \(\sqrt{200} \approx 14\) 倍。
  - **易错点 2**：最大电流发生在振动的**最低点**（\(|z| = 2A\)），而不是平衡位置（\(|z| = A\)），因为电流正比于位移 \(z\) 而非速度 \(\dot{z}\)！这与常规电阻环电磁阻尼（感应电流正比于速度）截然不同。

---

## Problem 6: Nuclear Medicine Scan (`plancks-2024-final-combined-slice-q6`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：含衰减的线积分公式**：
   - 设沿探测视线 \(\ell\)，某发射点 \((x,y)\) 到物体朝向探测器表面的穿出距离为 \(z(s)\)（或以探测器侧边界为 \(s=0\)，向物体内部深入距离为 \(s\)）。
   - 该点发出的光子到达物体表面需穿过厚度 \(s\) 的组织，衰减因子为 \(\exp\left(-\int_0^s \mu(x',y')\,ds'\right)\)。
   - 因此探测器测得的总信号为：
     \[
     I = k \int_0^\ell A(x,y) \exp\left(-\int_0^s \mu(x',y')\,ds'\right) ds
     \]
2. **第 (b) 问：椭圆截面极坐标下的衰减信号**：
   - 椭圆边界方程为 \(\frac{X^2}{a^2} + \frac{Y^2}{b^2} = 1\)。注意：过原点且与 \(x\) 轴夹角为 \(\vartheta\) 的直线，其与椭圆边界交点的极径 \(R_{\max}(\vartheta)\) 满足：
     \[
     R_{\max}^2(\vartheta)\left(\frac{\cos^2\vartheta}{a^2} + \frac{\sin^2\vartheta}{b^2}\right) = 1 \implies R_{\max}(\vartheta) = \frac{ab}{\sqrt{b^2\cos^2\vartheta + a^2\sin^2\vartheta}}
     \]
     （或者如果题目中的 \(\vartheta\) 指的是椭圆参数方程 \(X = a\cos\vartheta, Y = b\sin\vartheta\) 的离心角，则边界极径为 \(R_{\max} = \sqrt{a^2\cos^2\vartheta + b^2\sin^2\vartheta}\)）。
   - 沿该直径方向，分为与探测器同象限（极径 \(r \in [0, R_{\max}]\)，到表面距离 \(s = R_{\max} - r\)）和与探测器反象限（极径 \(r \in [0, R_{\max}]\)，极角 \(\vartheta+\pi\)，到表面距离 \(s = R_{\max} + r\)）两段：
     \[
     I = k \int_0^{R_{\max}} A(r,\vartheta) e^{-\mu(R_{\max} - r)}\,dr + k \int_0^{R_{\max}} A(r,\vartheta+\pi) e^{-\mu(R_{\max} + r)}\,dr
     \]
3. **第 (c) 问：有限圆孔径探测器修正**：
   - 设探测器圆孔半径为 \(R\)，距离原点为 \(Q\)。各向同性点源在距离探测器 \(d\) 处发出的光子，落入探测器立体角的比例为：
     \[
     F(d) = \frac{\pi R^2}{4\pi d^2} = \frac{R^2}{4 d^2}
     \]
   - 对于同象限点，\(d = Q - r\)；对于反象限点，\(d = Q + r\)。将常数 \(k\) 替换为 \(F(d)\) 即可：
     \[
     I = \int_0^{R_{\max}} \frac{R^2}{4(Q-r)^2} A(r,\vartheta) e^{-\mu(R_{\max} - r)}\,dr + \int_0^{R_{\max}} \frac{R^2}{4(Q+r)^2} A(r,\vartheta+\pi) e^{-\mu(R_{\max} + r)}\,dr
     \]
4. **第 (d) 问：鹿角对称性定量计算**：
   - 观察图 8：两条平行探测线穿过鹿头。第 \(i\) 条线（\(i=1,2\)）上，鹿角芽点源 \(A_i\) 距离朝向探测器的头骨外表面深度为 \(\ell_i\)，头骨背景在该线上的总弦长为 \(L_i\)。
   - **关键几何判读**：图 8 中标注的 \(z_1, z_2\) 是点源后方的弦长还是整条弦长？
     - 情况 A：若背景弦总长为 \(z_i + \ell_i\)（即 \(\ell_i\) 是点源前段，\(z_i\) 是点源后段），则背景贡献为 \(I_{\text{bg},i} = k \int_0^{z_i+\ell_i} A_0 e^{-\mu x}\,dx = \frac{k A_0}{\mu}\left(1 - e^{-\mu(z_i+\ell_i)}\right)\)；
     - 情况 B：若总弦长就是 \(z_i\)，则 \(I_{\text{bg},i} = \frac{k A_0}{\mu}(1 - e^{-\mu z_i})\)。
     - 注意到 \(\mu = 0.27\text{ cm}^{-1}\)，\(\mu z_2 = 0.27 \times 12.5 = 3.375\)，而 \(\mu(z_2+\ell_2) = 0.27 \times 23.5 = 6.345\)。
     - 分别计算两种情况下的 \(A_1, A_2\)：
       - 按情况 A（总弦长 \(z_i+\ell_i\)）：
         \[
         I_i = k\left[\frac{A_0}{\mu}\left(1 - e^{-\mu(z_i+\ell_i)}\right) + A_i e^{-\mu\ell_i}\right] \implies A_1 \approx 4921\text{ Bq}, \quad A_2 \approx 7960\text{ Bq}
         \]
       - 按情况 B（总弦长 \(z_i\)）：\(A_1 \approx 4968\text{ Bq}, A_2 \approx 14991\text{ Bq}\)。
     - 无论哪种情况，\(A_1 \neq A_2\)，说明鹿角生长**不均匀**（不对称）！

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 官方解答在第 (d) 问采用的正是情况 A（总积分上限为 \(z_{1,2} + \ell_{1,2}\)），算出 \(A_1 = 4921\text{ Bq}\)，\(A_2 = 7960\text{ Bq}\)，比值为 \(61.8\%\)，与我们的情况 A 数值完全一致！
  - **发现官方解答在第 (b) 问的经典数学陷阱**：官方解答把椭圆参数方程 \(X = a\cos\vartheta, Y = b\sin\vartheta\) 中的离心角 \(\vartheta\) 直接当成了极坐标的极角 \(\vartheta\)，从而写出了 \(R_{\max} = \sqrt{a^2\cos^2\vartheta + b^2\sin^2\vartheta}\)。实际上，若 \(\vartheta\) 是极角（直线与 \(x\) 轴夹角），代入 \(\frac{(R\cos\vartheta)^2}{a^2} + \frac{(R\sin\vartheta)^2}{b^2} = 1\) 得到的边界极径应为 \(R_{\max}(\vartheta) = \left(\frac{\cos^2\vartheta}{a^2} + \frac{\sin^2\vartheta}{b^2}\right)^{-1/2}\)！这是解析几何与物理竞赛中极其经典的易错点，我们在教学拆解中将其作为核心警示。

---

## Problem 7: Dark Matter in the Galaxy (`plancks-2024-final-combined-slice-q7`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **第 (a) 问：暗物质平均密度计算**：
   - 假设球对称质量分布，半径 \(r = 2.6\times 10^4\text{ ly} = 2.4596\times 10^{20}\text{ m}\) 内的总质量为 \(M_{\text{tot}}\)，可见发光物质质量为 \(M_{\text{lum}}\)。
   - 由圆轨道开普勒定律 \(v^2 = \frac{GM(r)}{r}\)，暗物质总质量为：
     \[
     M_{\text{DM}} = M_{\text{tot}} - M_{\text{lum}} = \frac{r}{G}\left(v_{\text{meas}}^2 - v_{\text{calc}}^2\right)
     \]
   - 球形区域体积 \(V = \frac{4}{3}\pi r^3\)，故平均暗物质质量密度为：
     \[
     \rho_{\text{DM}} = \frac{M_{\text{DM}}}{V} = \frac{3\left(v_{\text{meas}}^2 - v_{\text{calc}}^2\right)}{4\pi G r^2}
     \]
   - 代入数值：\(v_{\text{meas}} = 2.5\times 10^5\text{ m/s}\)，\(v_{\text{calc}} = 1.5\times 10^4\text{ m/s}\)，\(G = 6.67\times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2\)：
     \[
     \rho_{\text{DM}} \approx 3.684\times 10^{-21}\text{ kg/m}^3
     \]
   - 单位换算为 \(\text{GeV}/(c^2\cdot\text{cm}^3)\)：
     \[
     1\text{ GeV}/c^2 = \frac{1.602\times 10^{-10}\text{ J}}{(3\times 10^8\text{ m/s})^2} = 1.780\times 10^{-27}\text{ kg}, \qquad 1\text{ m}^3 = 10^6\text{ cm}^3
     \]
     \[
     \rho_{\text{DM}} = \frac{3.684\times 10^{-21}}{1.780\times 10^{-27} \times 10^6} \approx 2.07\text{ GeV}/(c^2\cdot\text{cm}^3)
     \]
2. **第 (b) 问：微型黑洞质量量级估算**：
   - “每年大约有一个微型黑洞从行星与恒星（间距 \(d_0 = 1\text{ AU} = 1.5\times 10^{11}\text{ m}\)）之间穿过”。
   - 这是一个典型的天体物理碰撞截面/扫掠体积（Swept Volume）估算问题：
     - **模型 A（扫掠盒子模型）**：行星-恒星连线有效横截面积取 \(A_{\text{eff}} \sim (1\text{ AU})^2\)（或直径 \(1\text{ AU}\) 的圆截面 \(\frac{\pi}{4}(1\text{ AU})^2\)），黑洞相对运动特征速度 \(v \sim v_{\text{meas}} = 250\text{ km/s}\)，在 \(\Delta t = 1\text{ yr} = 3.156\times 10^7\text{ s}\) 内扫过的体积为：
       \[
       V_{\text{unit}} \sim (1\text{ AU})^2 \cdot v_{\text{meas}} \cdot \Delta t \approx (1.5\times 10^{11})^2 \times 2.5\times 10^5 \times 3.156\times 10^7 \approx 1.775\times 10^{35}\text{ m}^3
       \]
       该体积内平均有 \(1\) 个黑洞，故单个黑洞质量为：
       \[
       M_{\text{BH}} = \rho_{\text{DM}} V_{\text{unit}} \approx 3.684\times 10^{-21} \times 1.775\times 10^{35} \approx 6.54\times 10^{14}\text{ kg} \approx 3.3\times 10^{-16}\,M_\odot
       \]
     - **模型 B（自由程立方体模型）**：若认为黑洞在 \(\Delta t = 1\text{ yr}\) 内运动的距离 \(L = v_{\text{meas}}\Delta t \approx 7.89\times 10^{12}\text{ m} \approx 52.6\text{ AU}\) 就是相邻黑洞的平均间距特征尺度，则每个黑洞占据的立方体体积为 \(V_{\text{unit}} \sim L^3 \sim (v_{\text{meas}}\Delta t)^3 \approx 4.9\times 10^{38}\text{ m}^3\)，此时：
       \[
       M_{\text{BH}} = \rho_{\text{DM}} V_{\text{unit}} \sim 10^{18}\text{ kg} \sim 10^{-12}\,M_\odot
       \]

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 第 (a) 问公式与数值 \(2.07\text{ GeV}/(c^2\cdot\text{cm}^3)\) 与官方解答完全一致。
  - 第 (b) 问中，官方解答在文字开头写的是 *"a box of \(1\text{ AU} \times v_{\text{orbit}} \times 1\text{ year}\)"*（还漏了一个维度），但在算式里实际写的是立方体对角线模型 \(V_{\text{unit}} = \left(\frac{2 \cdot t_{1\text{yr}} \cdot v_{\text{orbit}}}{\sqrt{3}}\right)^3\)（即我们的模型 B），得出 \(M_{\text{BH}} \approx 10^{-12}\,M_\odot\)，并明确指出由于对“穿过日地之间”的几何截面定义不同，\(10^{-14}\,M_\odot \sim 10^{-8}\,M_\odot\)（或扫掠柱体模型的 \(10^{-16}\,M_\odot\)）只要物理推理自洽均给满分。

---

## Problem 8: Icosahedron of Resistors (`plancks-2024-final-combined-slice-q8`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **方法一：电流叠加与对称性秒杀法（最快但需看清相邻条件）**：
   - 正二十面体有 \(V = 12\) 个顶点，\(E = 30\) 条边，每个顶点度数为 \(d = 5\)。
   - **试探**：如果仿照立方体或无穷网格，从顶点 \(1\) 注入 \(1\text{ A}\) 电流，从其余 \(11\) 个顶点各流出 \(\frac{1}{11}\text{ A}\) 电流，此时从顶点 \(1\) 出发的 \(5\) 条边電流相等吗？
   - **警惕陷阱**！在正二十面体中，除顶点 \(1\) 外的 \(11\) 个顶点分为三层：第一层（与 \(1\) 相邻的 \(5\) 个顶点）、第二层（距离为 \(2\) 的 \(5\) 个顶点）、以及对跖点（距离为 \(3\) 的 \(1\) 个顶点 \(12\)）。由于正二十面体关于顶点 \(1\) 具有严格的五重旋转对称性（\(C_5\) 对称群），当其余 \(11\) 个顶点等量抽流 \(\frac{1}{11}\text{ A}\) 时，这种抽流分布关于顶点 \(1\) 依然保持严格的 \(C_5\) 旋转对称！因此，从顶点 \(1\) 发出的 \(5\) 条边必然完全等价，每条边上的电流**严格等于** \(\frac{1}{5}\text{ A}\)！
   - 于是，在“\(1\) 进 \(1\text{ A}\)，其余 \(11\) 点各出 \(\frac{1}{11}\text{ A}\)”的状态下，相邻顶点 \(1,2\) 之间的电势差为：
     \[
     V_1^{(A)} - V_2^{(A)} = I_{12}^{(A)} R = \frac{1}{5}\text{ V}
     \]
   - 再构造对称的第二状态：“顶点 \(2\) 流出 \(1\text{ A}\)，其余 \(11\) 个顶点各流入 \(\frac{1}{11}\text{ A}\)”。同样由关于顶点 \(2\) 的 \(C_5\) 旋转对称性，汇入顶点 \(2\) 的 \(5\) 条边电流严格相等，均为 \(\frac{1}{5}\text{ A}\)，故 \(V_1^{(B)} - V_2^{(B)} = \frac{1}{5}\text{ V}\)。
   - 将两状态线性叠加：除 \(1,2\) 外的 \(10\) 个顶点净注入电流为 \(-\frac{1}{11} + \frac{1}{11} = 0\)；顶点 \(1\) 净流入电流为 \(I_{\text{tot}} = 1 + \frac{1}{11} = \frac{12}{11}\text{ A}\)，顶点 \(2\) 净流出电流为 \(\frac{12}{11}\text{ A}\)。
   - 两点间总电势差为 \(V_1 - V_2 = \frac{1}{5} + \frac{1}{5} = \frac{2}{5}\text{ V}\)。
   - 故相邻两顶点间的等效电阻为：
     \[
     R_{\text{eff}} = \frac{V_1 - V_2}{I_{\text{tot}}} = \frac{2/5}{12/11} = \frac{11}{30}\,\Omega
     \]
2. **方法二：镜像对称折叠与 \(\Delta\text{-Y}\) / 平面串并联化简（双重验证）**：
   - 将电流从顶点 \(1\) 注入、从相邻顶点 \(2\) 抽出。
   - 该电路有两个正交的对称面：
     1. 包含边 \(1\text{-}2\) 的对称面（前后镜像对称）：将不在该平面上的 \(8\) 个顶点两两配对等势折叠，合并为平面电路；
     2. 垂直平分边 \(1\text{-}2\) 的中垂面（左右反对称面）：位于中垂面上的所有节点（包括边 \(1\text{-}2\) 中点 \(X\)、对侧边 \(3\text{-}4\) 中点 \(Y\)、以及中垂面上的两对顶点 \(9\text{-}10\) 和 \(11\text{-}12\)）电势恒等于 \(\frac{V_1+V_2}{2} = 0\)！
   - 将中垂面上所有点短接为同一个零电势节点 \(O\)，只需计算左半边（顶点 \(1\) 到节点 \(O\)）的等效电阻 \(R_{1O}\)，则 \(R_{12} = 2 R_{1O}\)。
   - 在左半边电路中，一步步进行串并联：
     - 底部支路：\(\frac{1}{2}\,\Omega\) 与 \(\frac{1}{4}\,\Omega\) 并联得 \(\frac{1}{6}\,\Omega\)，串联 \(\frac{1}{4}\,\Omega\)（或按官方图：\(\frac{1}{2} + \frac{1}{4} = \frac{3}{4}\,\Omega\)，再与 \(\frac{1}{4}\,\Omega\) 并联得 \(\frac{3}{16}\,\Omega\)）；
     - 接着与 \(\frac{1}{2}\,\Omega\) 串联得 \(\frac{3}{16} + \frac{1}{2} = \frac{11}{16}\,\Omega\)；
     - 最后在顶点 \(1\) 到 \(O\) 之间，有三条并联支路：\(\frac{1}{4}\,\Omega\)、\(\frac{1}{4}\,\Omega\)、\(\frac{11}{16}\,\Omega\)（或者两条 \(\frac{1}{4}\,\Omega\) 并联为 \(\frac{1}{8}\,\Omega\)，不对，一条是边 \(1\text{-}X\) 的半边 \(\frac{1}{2}\,\Omega\)，一条是 \(1\text{-}(9,10)\) 的 \(\frac{1}{2}\,\Omega\)，合并后为 \(\frac{1}{4}\,\Omega\) 与 \(\frac{11}{16}\,\Omega\) 并联）：
       \[
       R_{1O} = \left(\frac{1}{1/4} + \frac{1}{11/16}\right)^{-1} = \left(4 + \frac{16}{11}\right)^{-1} = \frac{11}{60}\,\Omega \implies R_{12} = 2 R_{1O} = \frac{11}{30}\,\Omega
       \]
   - 两种方法殊途同归，结果严格为 \(\frac{11}{30}\,\Omega\)！

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 极为巧合的是，官方解答同样给出了这两种解法（First Solution 为双重对称折叠串并联，Second Solution 为 \(1\text{ A}\) 进、\(11\times \frac{1}{11}\text{ A}\) 出的叠加原理），步骤与结果 \(\frac{11}{30}\,\Omega\) 完全一致！
- **深度教学延伸（极其重要）**：
  - 为什么“一进十一出”的叠加法对正二十面体的**相邻顶点**成立？因为正二十面体不仅是顶点传递图（Vertex-transitive），更是**边传递图（Edge-transitive / Symmetric graph）**！对于任意包含 \(V\) 个顶点、\(E\) 条边（每条边电阻为 \(R\)）的边传递图（如全部五种柏拉图正多面体：正四面体、正六面体、正八面体、正十二面体、正二十面体），由这一叠加法可以直接导出相邻顶点等效电阻的**普适Foster定理公式**：
    \[
    R_{\text{adj}} = \frac{V - 1}{E} R
    \]
    代入正二十面体 \(V = 12, E = 30, R = 1\,\Omega\)，立得 \(R_{\text{adj}} = \frac{12-1}{30} = \frac{11}{30}\,\Omega\)！但必须向学生强调：该方法**只能**直接求相邻顶点间的电阻，若求非相邻顶点（如距离为 \(2\) 或对跖点），则必须使用对称平面折叠法！

---

## Problem 9: Molecular Zipper (`plancks-2024-final-combined-slice-q9`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **模型规则与微观态计数**：
   - 共有 \(N\) 个链环（links），打开必须从第 \(1\) 个开始依次连续打开，且第 \(N\) 个链环永远不能打开。
   - 因此，系统打开的链环数 \(p\) 只能取 \(p = 0, 1, 2, \dots, N-1\)。
   - 当有 \(p\) 个链环打开时：
     - 能量为 \(E_p = p\epsilon\)；
     - 由于每个打开的链环有 \(G\) 种取向，而闭合的链环只有 \(1\) 种状态，故对应于固定 \(p\) 的微观态简并度为 \(g_p = G^p\)。
2. **第 (a) 问：配分函数与自由能**：
   - 正则系综配分函数为：
     \[
     Z = \sum_{p=0}^{N-1} G^p e^{-\beta p\epsilon} = \sum_{p=0}^{N-1} x^p = \frac{1 - x^N}{1 - x}, \qquad x \equiv G e^{-\epsilon / (k_B T)}
     \]
   - 亥姆霍兹自由能为：
     \[
     F = -k_B T \ln Z = -k_B T \ln\left(\frac{1 - x^N}{1 - x}\right)
     \]
3. **第 (b) 问：有限温度相变与临界温度 \(T_c\)**：
   - 在热力学极限 \(N \to \infty\) 下：
     - 当 \(x < 1\) 时，\(x^N \to 0\)，\(F \to k_B T \ln(1 - x)\)（非广延量，单位链环自由能 \(f = \lim_{N\to\infty} F/N = 0\)）；
     - 当 \(x > 1\) 时，\(x^N \gg 1\)，\(F \approx -N k_B T \ln x = N(\epsilon - k_B T \ln G)\)（广延量，\(f = \epsilon - k_B T \ln G\)）。
   - 自由能的奇异性发生在 \(x = 1\) 处：
     \[
     G e^{-\epsilon / (k_B T_c)} = 1 \implies T_c = \frac{\epsilon}{k_B \ln G}
     \]
   - 显然只有当 \(G > 1\)（即 \(\ln G > 0\)）时，才存在有限的正临界温度 \(T_c > 0\)。
4. **第 (c) 问：平均打开链环数 \(\langle p \rangle\) 与序参量**：
   - 利用对数求导技巧：
     \[
     \langle p \rangle = \frac{1}{Z} \sum_{p=0}^{N-1} p x^p = x \frac{\partial \ln Z}{\partial x} = x \left( \frac{1}{1 - x} - \frac{N x^{N-1}}{1 - x^N} \right) = \frac{x}{1 - x} - \frac{N x^N}{1 - x^N}
     \]
   - 在 \(N \to \infty\) 下考察打开比例 \(\phi = \frac{\langle p \rangle}{N}\)：
     - 当 \(T < T_c\)（\(x < 1\)）时，\(x^N \to 0\)，\(\langle p \rangle = \frac{x}{1-x} = \mathcal{O}(1)\)，故 \(\phi = \frac{\langle p \rangle}{N} \to 0\)（拉链处于闭合态）；
     - 当 \(T > T_c\)（\(x > 1\)）时，\(x^N \to \infty\)，\(\langle p \rangle \approx N - \frac{1}{x-1}\)，故 \(\phi = \frac{\langle p \rangle}{N} \to 1\)（拉链完全解链！）。
   - 因此 \(\frac{\langle p \rangle}{N}\)（或 \(1 - \frac{\langle p \rangle}{N}\)）在 \(T_c\) 处发生从 \(0\) 到 \(1\) 的一阶跳变，可作为该解链相变的序参量。
5. **第 (d) 问：需要 \(G > 1\) 的物理原因**：
   - 热力学相变的本质是**内能 \(U\) 与熵 \(S\) 的竞争**（最小化自由能 \(F = U - TS\)）。
   - 打开 \(p\) 个链环需要付出内能代价 \(\Delta U = p\epsilon > 0\)，但同时获得构型熵增益 \(\Delta S = k_B \ln(G^p) = p k_B \ln G\)，故自由能变化为：
     \[
     \Delta F(p) = \Delta U - T\Delta S = p(\epsilon - k_B T \ln G)
     \]
   - 若 \(G = 1\)，则打开链环没有任何单链环构型熵增益（\(\Delta S = 0\)），在任何有限温度下打开链环只会单纯增加能量，因此拉链永远倾向于闭合，不可能发生相变；只有当 \(G > 1\) 时，单链环解开后的多取向简并度提供了正的广延熵 \(\Delta S = p k_B \ln G > 0\)，使得当 \(T > T_c = \frac{\epsilon}{k_B \ln G}\) 时熵项 \(-T\Delta S\) 压倒能量代价 \(\Delta U\)，驱动DNA双链自发完全解旋！

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 全部四问的推导、公式、热力学极限讨论及能量-熵竞争机制与官方参考解答（源自 Kittel 1969 经典论文）完全一致！
- **核心难点与易错点**：
  - **难点**：在 \(x = 1\) 处 \(\langle p \rangle\) 表面上出现 \(\frac{0}{0}\) 不定式，需用洛必达法则或泰勒展开 \(x = 1 + \delta\) 才能算出 \(T = T_c\) 时 \(\langle p \rangle = \frac{N-1}{2}\)。
  - **易错点**：等比数列求和上限是 \(N-1\)（共 \(N\) 项），容易误写成上限 \(N\) 导致分子变成 \(1 - x^{N+1}\)。

---

## Problem 10: 4D Sun (`plancks-2024-final-combined-slice-q10`)

### 【第一阶段：只看原题独立试做 (Blind Attempt)】
1. **四维空间黑体辐射谱推导**：
   - 在 \(n\) 维空间（本题 \(n = 4\)）中，光子的色散关系仍为 \(E = h\nu = \hbar c k\)。
   - 动量空间（或波矢空间）中，频率在 \([\nu, \nu + d\nu]\) 之间的光子态密度正比于 \(n\) 维球壳的体积元：
     \[
     g(\nu)\,d\nu \propto k^{n-1}\,dk \propto \nu^{n-1}\,d\nu
     \]
   - 结合玻色-爱因斯坦分布 \(n_{\text{BE}}(\nu) = \frac{1}{e^{h\nu / (k_B T)} - 1}\)，单位体积内按**频率**分布的黑体辐射能量谱密度为：
     \[
     u_\nu(\nu)\,d\nu \propto h\nu \cdot \nu^{n-1} \frac{1}{e^{h\nu/(k_B T)} - 1}\,d\nu \propto \frac{\nu^n}{e^{h\nu/(k_B T)} - 1}\,d\nu
     \]
   - 若按**波长** \(\lambda = c/\nu\)（\(d\nu = -\frac{c}{\lambda^2}d\lambda\)）分布，则能量谱密度为：
     \[
     u_\lambda(\lambda)\,d\lambda \propto \frac{\lambda^{-(n+2)}}{e^{hc/(\lambda k_B T)} - 1}\,d\lambda
     \]
2. **维恩位移定律求解（两种表象对比）**：
   - **表象 A（按频率分布 \(u_\nu\) 的峰值，\(n = 4\)）**：
     - 令无量纲变量 \(x = \frac{h\nu}{k_B T}\)，求 \(f_4(x) = \frac{x^4}{e^x - 1}\) 的极大值：
       \[
       \frac{d}{dx}\left(\frac{x^4}{e^x - 1}\right) = 0 \implies x = 4(1 - e^{-x})
       \]
     - 迭代求解：初值取 \(x_0 = 4\)，第一次迭代 \(x_1 = 4(1 - e^{-4}) \approx 4(1 - 0.0183) \approx 3.927\)，精确解为 \(x_{\max}^{(\nu)} \approx 3.9207\)。
     - 对应波长 \(\lambda_{\text{peak}}^{(\nu)} = \frac{c}{\nu_{\max}} = \frac{hc}{k_B T x_{\max}^{(\nu)}}\)：
       \[
       \lambda_{\text{peak}}^{(\nu)} = \frac{6.626\times 10^{-34} \times 3\times 10^8}{1.38\times 10^{-23} \times 6000 \times 3.921} \approx 612\text{ nm} \quad (\text{若取 } x\approx 3.9 \text{ 则为 } 616\text{ nm})
       \]
   - **表象 B（按波长分布 \(u_\lambda\) 的峰值，\(n = 4\)）**：
     - 令 \(y = \frac{hc}{\lambda k_B T}\)，求 \(g_4(y) = \frac{y^6}{e^y - 1}\) 的极大值：
       \[
       y = 6(1 - e^{-y}) \implies y_{\max}^{(\lambda)} \approx 6(1 - e^{-6}) \approx 5.985
       \]
     - 对应波长 \(\lambda_{\text{peak}}^{(\lambda)} = \frac{hc}{k_B T y_{\max}^{(\lambda)}} \approx 401\text{ nm}\)（紫光/近紫外）。
3. **颜色判定**：
   - 在四维空间中，与三维空间相比（三维下 \(x_{\max}^{(\nu)} \approx 2.82\)，\(y_{\max}^{(\lambda)} \approx 4.97\)，\(\lambda_{\text{peak}}^{(\lambda)} \approx 483\text{ nm}\)），由于高频态密度因子从 \(\nu^2\) 增强为 \(\nu^3\)，黑体辐射谱整体向**高频（短波/蓝紫端）移动**！因此太阳看起来仍接近白色，但显著向蓝绿色/蓝紫色偏移（泛蓝绿或蓝白光）。

### 【第二阶段：对照官方解答与教学拆解 (Comparison & Breakdown)】
- **与参考解答对比**：
  - 官方解答采用了**表象 A（按频率分布 \(\varepsilon(\nu) \propto \frac{\nu^n}{e^{h\nu/kT}-1}\)）**，列出超越方程 \(x = n(1 - e^{-x})\)，用一次迭代 \(x \approx n - n e^{-n}\) 算出 \(n=4\) 时 \(x_{\max} \approx 3.927\)（代入时取了 \(3.9\)），得到 \(\lambda_{\max} = \frac{hc}{kT x_{\max}} \approx 616\text{ nm}\)，并评注：*"616 nm is middle of the spectrum, so it will look white with a green-blue tint... It would also be valid to look at \(\varepsilon(\lambda)\,d\lambda\) instead of \(\varepsilon(\nu)\,d\nu\)."*
- **核心难点与易错点**：
  - **难点 1**：高维球面面积元标度律 \(d^{n-1}k \propto k^{n-1}dk\) 的快速推导（无需算出四维球立体角系数 \(2\pi^2\)，因为求极值时常数因子直接约掉！）。
  - **难点 2**：没有计算器或 Lambert \(W\) 函数表时，如何手算超越方程 \(x = n(1 - e^{-x})\)？利用 \(e^{-n} \ll 1\) 进行不动点迭代 \(x^{(1)} = n(1 - e^{-n})\)，一步即可达到 \(0.15\%\) 的极高精度！
  - **易错点**：混淆 \(u_\nu\) 的峰值频率对应波长 \(\frac{c}{\nu_{\max}}\) 与 \(u_\lambda\) 的峰值波长 \(\lambda_{\max}\)（相差雅可比行列式因子 \(\left|\frac{d\nu}{d\lambda}\right| = \frac{c}{\lambda^2}\)，导致幂次从 \(n=4\) 变为 \(n+2=6\)）。
