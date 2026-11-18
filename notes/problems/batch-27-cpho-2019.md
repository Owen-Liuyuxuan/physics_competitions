# Batch 27: 第36届全国中学生物理竞赛复赛与决赛理论试题（CPhO 2019）独立盲解与教学拆解

> **说明**：本笔记严格执行两阶段教练协议：
> - **Phase 1（独立盲解）**：仅查看 `derived/questions/cpho-2019-*-problem-slice-q*/page-*.jpg` 原题图像与附图，独立构建物理模型、完成全步骤推导，并作量纲、极限与数值校核；
> - **Phase 2（对照拆解）**：随后逐页核对 `cpho-2019-*-solution-slice-q*/page-*.jpg` 官方参考解答，对比思路优劣、勘正官方笔误与物理漏洞（如复赛第2题碰撞假设 \(v_0 \ge 0\) 漏掉反转滑行区间与式(24)分母 \(l^3\) 量纲笔误、复赛第5题解法三展开系数 \(n_0/n\) 笔误、复赛第6题中间过早修约 \(0.980c\) 导致 \(4.52\%\to 4.59\%\) 偏移、决赛第2题“界面总电荷”与“自由电荷”辨析、决赛第6题金星凌日基线取弧长 \(1900\text{ km}\) 而非垂直投影弦长 \(1614\text{ km}\) 及核心氢占比 \(0.71\) 漏乘等），并提炼面向高中竞赛生与本科普物学生的核心难点与迁移方法。

---

# 复赛理论试题（Semifinal Theory）

## 1. 第36届复赛理论第1题 · 三脚圆凳茶杯的最低质心最佳高度与脚力变化 (`cpho-2019-semifinal-theory-problem-slice-q1`)

- **难度评级**：`D2`
- **物理模型**：变质量液体容器质心极值模型与空间平行力系三点静力平衡模型
- **教学标签**：`质心极值问题`、`最稳水位条件`、`三脚架静力平衡`、`力矩平衡法`、`微扰安全边界`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **茶水中最佳高度 \(h\) 的确定**
   以圆凳凳面（茶杯底面所在平面）为高度零点 \(z = 0\)，竖直向上为 \(z\) 轴。
   - 茶杯总质量为 \(m\)，其中杯底质量 \(m_{\text{底}} = \frac{m}{5}\)（厚度可忽略，质心位于 \(z = 0\)），均匀圆柱形薄壁杯壁质量 \(m_{\text{壁}} = \frac{4}{5}m\)（高为 \(H\)，质心位于 \(z = \frac{H}{2}\)）。故空茶杯的质心高度为：
     \[
     z_{\text{空}} = \frac{\frac{m}{5}\cdot 0 + \frac{4m}{5}\cdot \frac{H}{2}}{m} = \frac{2}{5}H.
     \]
   - 设杯中茶水高度为 \(h\)（\(0 \le h \le H\)），记 \(\lambda = \rho \pi r^2\) 为单位高度茶水的质量，则茶水质量 \(m_{\text{水}} = \lambda h\)，其质心位于 \(z_{\text{水}} = \frac{h}{2}\)。
   - “杯+水”整体的质心高度 \(z_G(h)\) 为：
     \[
     z_G(h) = \frac{\frac{2}{5}mH + \frac{1}{2}\lambda h^2}{m + \lambda h}.
     \]
   - 物理趋势分析：随着 \(h\) 从 \(0\) 开始增加，由于水面低于整体质心，加注茶水会使整体质心不断**降低**（在 \(0 < h < h^*\) 区间内，茶水越多反而越稳定）；当 \(h\) 增大到使水面恰好与当前整体质心等高时，\(z_G(h)\) 达到最小值；此后继续加水，整体质心将重新升高，稳定性变差。题中要求“所盛茶水尽可能多并保持足够稳定”，即对应整体质心最低（稳定性极值点）时的高度 \(h^*\)。
   - 求极值（令 \(\frac{\mathrm{d}z_G}{\mathrm{d}h} = 0\)，或等价利用物理结论 \(z_G(h^*) = h^*\)）：
     \[
     \frac{\mathrm{d}z_G}{\mathrm{d}h} = \frac{\lambda h(m + \lambda h) - \lambda\left(\frac{2}{5}mH + \frac{1}{2}\lambda h^2\right)}{(m + \lambda h)^2} = \frac{\lambda\left(\frac{1}{2}\lambda h^2 + m h - \frac{2}{5}mH\right)}{(m + \lambda h)^2} = 0.
     \]
     解方程 \(\frac{1}{2}\lambda h^2 + mh - \frac{2}{5}mH = 0\)，舍去负根得：
     \[
     h^* = \frac{-m + \sqrt{m^2 + \frac{4}{5}m\lambda H}}{\lambda} = \frac{m}{\rho\pi r^2}\left(\sqrt{1 + \frac{4\rho\pi r^2 H}{5m}} - 1\right).
     \]
     （校验：① 验证 \(h^* = z_G(h^*) < \frac{2}{5}H < H\)，茶水绝不会溢出；② 当杯极轻 \(m \to 0\) 时，展开根号得 \(h^* \to \sqrt{\frac{4mH}{5\rho\pi r^2}} \to 0\)；③ 量纲上 \(m/(\rho\pi r^2)\) 为长度，\(\rho r^2 H / m\) 无量纲，完全自洽。）

2. **滑移到内切 \(D\) 点后各凳脚支持力的改变量**
   当茶水高度为 \(h^*\) 时，“杯+水”总质量 \(M_t\) 恰好化简为：
   \[
   M_t = m + \rho\pi r^2 h^* = m\sqrt{1 + \frac{4\rho\pi r^2 H}{5m}} = \sqrt{m^2 + \frac{4}{5}m\rho\pi r^2 H}.
   \]
   - 几何关系：设等边三角形 \(ABC\) 的中心（即圆心 \(O\) 在底板上的投影）为 \(O'\)。三角形高为 \(\frac{\sqrt{3}}{2}a\)，故 \(O'B = \frac{a}{\sqrt{3}}\)，\(O'\) 到边 \(AC\) 的距离 \(d_{AC} = \frac{a}{2\sqrt{3}}\)。
   - 由题图 b 可见，\(OD \perp AC\) 且 \(D\) 点位于从 \(O\) 指向边 \(AC\) 一侧（远离 \(B\) 点）。茶杯底面圆心从 \(O\) 移动到与圆凳内切于 \(D\) 点的新位置 \(O_c\)，水平位移大小为 \(d = R - r\)，方向垂直 \(AC\) 指向边 \(AC\)。
   - 因为茶杯质量远小于凳子质量（\(M_t \ll M_{\text{凳}}\)），各凳脚支持力均保持大于零，无翻倒脱离地面的情况；又因为凳面及凸缘均均匀，凳子自身重力与滑移前原始重力在差分中完全消去。
   - 建立水平坐标：取 \(O'\) 为原点，\(x\) 轴从 \(O'\) 垂直指向 \(AC\)，\(y\) 轴平行于 \(\overrightarrow{CA}\)。则 \(B\left(-\frac{a}{\sqrt{3}}, 0\right)\)，\(A, C\) 横坐标均为 \(+\frac{a}{2\sqrt{3}}\)、纵坐标对称（\(\pm \frac{a}{2}\)）。
   - 设各脚支持力改变量为 \(\Delta N_A, \Delta N_B, \Delta N_C\)（向上为正）。列写增量平衡方程：
     - 竖直合力平衡增量：\(\Delta N_A + \Delta N_B + \Delta N_C = 0\)；
     - 绕 \(x\) 轴力矩平衡增量（对称性）：\(\Delta N_A = \Delta N_C \implies \Delta N_B = -2\Delta N_A\)；
     - 绕 \(y\) 轴力矩平衡增量（向下重力 \(M_t g\) 从 \(x=0\) 移至 \(x = R-r\)）：
       \[
       x_A \Delta N_A + x_C \Delta N_C + x_B \Delta N_B = M_t g (R - r).
       \]
       代入坐标与 \(\Delta N_C = \Delta N_A, \Delta N_B = -2\Delta N_A\)：
       \[
       \left(\frac{a}{2\sqrt{3}} + \frac{a}{2\sqrt{3}} + \frac{2a}{\sqrt{3}}\right)\Delta N_A = \sqrt{3}\,a\,\Delta N_A = M_t g(R - r).
       \]
   - 解得各凳脚支持力相对于滑移前的改变：
     \[
     \Delta N_A = \Delta N_C = \frac{(R - r)g}{\sqrt{3}\,a}\sqrt{m^2 + \frac{4}{5}m\rho\pi r^2 H} \quad (\text{增大}),
     \]
     \[
     \Delta N_B = -\frac{2(R - r)g}{\sqrt{3}\,a}\sqrt{m^2 + \frac{4}{5}m\rho\pi r^2 H} \quad (\text{减小}).
     \]
     （检验：直接以 \(AC\) 边为转轴列力矩方程，\(B\) 到 \(AC\) 距离为 \(\frac{\sqrt{3}}{2}a\)，重心向 \(AC\) 移动 \(R-r\)，立即得 \(\Delta N_B \cdot \frac{\sqrt{3}}{2}a = -M_t g(R-r)\)，与上式完全一致！）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（2）问的全部公式和表述与官方参考解答（`page-1.jpg`–`page-3.jpg`）完全一致！官方在第（1）问中除微积分求导法外，还给出了一个极为漂亮的**均值不等式解法（另一解法）**：把 \(y_{\text{CM}}\) 配凑成 \(\frac{\frac{2mH}{5} + \frac{m^2}{2\lambda}}{m+\lambda h} + \frac{m+\lambda h}{2\lambda} - \frac{m}{\lambda}\)，再对前两项直接应用 \(a + b \ge 2\sqrt{ab}\) 避开求导。在第（2）问中，官方也同时列出了绕中心轴和绕 \(AC\) 边为转轴的两种解法，并在式(12)明确给出了保证 \(N_B > 0\) 不翻倒的凳质量下限条件 \(M > \frac{2\sqrt{3}(R-r)-a}{a}M_t\)，对应题干“茶杯质量远小于凳子质量”的铺垫。
- **核心难点与典型易错点**：
  - 难点1：领悟“茶水尽可能多且保持足够稳定”在物理建模上对应于质心曲线先降后升的最低点 \(z_G = (z_G)_{\min}\)（等价于水面高度恰好追上整体质心高度 \(h^* = z_G(h^*)\)）。
  - 难点2：根据图 b 准确判断 \(D\) 点的方位（\(OD \perp AC\) 且偏向 \(AC\) 边而非 \(B\) 点），并正确给出圆心位移 \(d = R - r\)。
  - 易错点1：算空杯质心时误将杯高 \(H/2\) 直接当成空杯质心，忽略了杯底占 \(m/5\)、杯壁占 \(4m/5\) 的加权比例。
  - 易错点2：求支持力变化时错把 \(R\) 当作移动距离（漏减去杯半径 \(r\)），或者算错 \(O'\) 到 \(AC\) 边与到 \(B\) 点的距离比（\(1:2\)）。
- **教练总结与迁移建议**：对于“向容器注水使整体质心最低”一类极值问题，记住“新增微元质量 \(\mathrm{d}m\) 恰好位于当前总质心高度时，质心达到极低值”这一通用结论（\(h^* = z_G(h^*)\)）可直接秒杀验证；而三点支承刚体的载荷变化问题，采用“增量力矩平衡 + 选边 \(AC\) 为转轴”能彻底消去凳子自身重力和冗余未知量。

---

## 2. 第36届复赛理论第2题 · 农用平板车把手落地碰撞与滚滑制动多过程 (`cpho-2019-semifinal-theory-problem-slice-q2`)

- **难度评级**：`D4`
- **物理模型**：刚体定轴摆落 + 双接触点多体约束碰撞（动量-冲量与角动量耦合） + 滚滑过渡及纯滚动摩擦制动动力学
- **教学标签**：`刚体碰撞与动量定理`、`摩擦反向与自锁判定`、`又滑又滚到纯滚动`、`瞬时锁死解锁机制`、`多过程分段力学`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **碰撞前瞬间把手的转动角速度 \(\omega_0\)**
   设向右（把手前端）为 \(+x\)，竖直向上为 \(+y\)，逆时针转动为正方向。车轮半径 \(r\)，两车轮质量各为 \(m\)（本题第(1)问中车轮被卡住不能平动，光滑车轴对车轮无力矩，故车轮静止）。
   - 平板长 \(l\)、质量 \(2m\)、质心在车轴 \(O\) 处，绕轴转动惯量：
     \[
     I_{\text{板}} = \frac{1}{12}(2m)l^2 = \frac{1}{6}ml^2.
     \]
   - 两把手各长 \(2l\)、质量 \(m\)，前端与平板对齐（即在轴前 \(+\frac{l}{2}\) 处，末端在轴后 \(-\frac{3}{2}l\) 处），故每根把手质心在轴后 \(r_h = \frac{l}{2}\) 处。两把手绕轴转动惯量：
     \[
     I_{\text{把}} = 2\left[\frac{1}{12}m(2l)^2 + m\left(\frac{l}{2}\right)^2\right] = 2\left(\frac{1}{3} + \frac{1}{4}\right)ml^2 = \frac{7}{6}ml^2.
     \]
   - 转动部分（平板+两把手，总质量 \(4m\)）总转动惯量 \(I_0 = \frac{1}{6}ml^2 + \frac{7}{6}ml^2 = \frac{4}{3}ml^2\)。
   - 把手末端 \(P\) 距轴 \(O\) 长度为 \(\frac{3}{2}l\)，碰撞地面时车轴高 \(r\)，故把手与水平地面夹角 \(\theta\) 满足：
     \[
     \sin\theta = \frac{2r}{3l}, \qquad \cos\theta = \frac{\sqrt{9l^2 - 4r^2}}{3l}.
     \]
   - 机械能守恒：平板质心高度不变；两把手质心在水平释放时与轴等高，碰撞时下降 \(\Delta h = \frac{l}{2}\sin\theta = \frac{r}{3}\)。故：
     \[
     \frac{1}{2}I_0 \omega_0^2 = 2mg\cdot\frac{r}{3} \implies \frac{2}{3}ml^2\omega_0^2 = \frac{2}{3}mgr \implies \omega_0 = \frac{\sqrt{gr}}{l}.
     \]

2. **碰撞过程分析及车轮从开始运动直至静止车轴移动的距离 \(s\)**
   - **碰撞前瞬间系统动量与角动量**：
     轮子静止，平板质心在 \(O\) 处速度为零，两把手质心位于 \(O\) 的相对位置 \(\left(-\frac{l}{2}\cos\theta, -\frac{r}{3}\right)\)，绕 \(O\) 逆时针转动（\(\omega_0 > 0\)），故碰前全车（总质量 \(6m\)）动量为：
     \[
     P_{x0} = 2m\left(\omega_0 \frac{r}{3}\right) = \frac{2}{3}mr\omega_0 > 0, \qquad P_{y0} = 2m\left(-\omega_0 \frac{l}{2}\cos\theta\right) = -ml\cos\theta\,\omega_0 < 0,
     \]
     把手末端 \(P\) 的水平速度 \(v_{Px}(0^-) = +\omega_0 r > 0\)，车轮与地面接触点 \(W\) 的初速度 \(v_{Wx}(0^-) = 0\)。
   - **锁死与碰撞动力学分析**：
     碰前瞬间车轮与轴锁死、碰后瞬间解锁，碰撞时间 \(\Delta t\) 较短但不为零（忽略重力冲量，几何位形不变）。由于碰后把手末端竖直不反弹且车轮不离地，碰后系统角速度 \(\omega_f = 0\)（车轮角速度亦为 \(0\)），整体仅剩水平速度 \(V\)。
     关键几何约束：一旦车轮与轴锁死，整个系统成为一个刚体，而把手末端 \(P\) 与车轮底部 \(W\) 均在地面 \(y=0\)（距轴 \(O\) 竖直距离均为 \(-r\)），因此刚体上这两个接触点具有**完全相同的瞬时水平速度**：
     \[
     v_{Px}(t) = v_{Wx}(t) = v_O(t) + \omega(t) r \equiv v_x(t).
     \]
     记地面总法向冲量为 \(J_N = J_{NP} + J_{Nw}\)，总水平摩擦冲量为 \(J_f = J_{fP} + J_{fw}\)。由于竖直动量从 \(-ml\cos\theta\,\omega_0\) 变为 \(0\)，总法向冲量必为：
     \[
     J_N = J_{NP} + J_{Nw} = m l \cos\theta\,\omega_0.
     \]
     （注：锁死与碰撞期间保持 \(N_w \ge 0\) 的条件：以 \(P\) 点为固定参照点，锁死前后全程 \(L_{P,0} = -\frac{1}{6}ml^2\omega_0\)，\(L_{P,f} = -\frac{16}{3}mr V\)，得 \(\frac{3}{2}l\cos\theta\,J_{Nw} = \frac{1}{6}ml^2\omega_0 - \frac{16}{3}mrV\)，若锁死先于撞地完成则撞地阶段需 \(\frac{1}{6}l^2 - \frac{70}{27}r^2 + \frac{8}{9}\mu r l\cos\theta \ge 0\)，即轮半径远小于车长。）
     设滑动过程中保持 \(v_x(t) > 0\)，此时两接触点同时受向左滑动摩擦力 \(f = -\mu(N_P + N_w)\)。对 \(v_x = v_O + \omega r\) 求导得：
     \[
     6m\dot{v}_O + \frac{2}{3}mr\dot{\omega} = -\mu(N_P + N_w) = \mu m l \cos\theta\,\dot{\omega} \implies \dot{v}_x = \left(\frac{\mu l \cos\theta}{6} + \frac{8}{9}r\right)\dot{\omega} < 0,
     \]
     可见 \(v_x(t)\) 单调递减。根据 \(\mu\) 的大小，严格存在三个物理区间：
     - **情形 A（小摩擦，\(\mu < \tan\theta = \frac{2r}{3l\cos\theta} = \frac{2r}{\sqrt{9l^2 - 4r^2}}\)）**：
       整个碰撞过程中 \(v_x(t)\) 始终为正，总摩擦冲量 \(J_f = -\mu J_N = -\mu ml\cos\theta\,\omega_0\)。由水平动量定理：
       \[
       6m V - \frac{2}{3}mr\omega_0 = -\mu ml\cos\theta\,\omega_0 \implies V = \frac{2r - 3\mu l\cos\theta}{18}\omega_0 = \frac{\sqrt{gr}}{6}(\sin\theta - \mu\cos\theta) > 0.
       \]
     - **情形 B（强摩擦，\(\mu \ge \frac{16r}{3l\cos\theta} = \frac{8}{3}\tan\theta\)）**：
       \(v_x(t)\) 在 \(\omega^* = \frac{\mu l\cos\theta - \frac{2}{3}r}{\mu l\cos\theta + \frac{16}{3}r}\omega_0 > 0\) 处降为零（此时 \(v_O^* = -\omega^* r < 0\)）。此后随 \(\omega\) 继续减小，所需维持 \(v_x=0\) 的静摩擦 \(f_s = -\frac{16}{3}mr\dot{\omega} \le \mu(N_P + N_w)\)，故静摩擦锁住接触点直至 \(\omega = 0\)，碰后 \(V = 0, s = 0\)。
     - **情形 C（中等摩擦，\(\tan\theta \le \mu < \frac{8}{3}\tan\theta\)）**：
       \(v_x(t)\) 在 \(\omega^*\) 处降为零后，最大静摩擦不足以维持 \(v_x = 0\)，接触点将**反向向左滑动**（\(v_x < 0\)），摩擦力反向向右（\(+\mu(N_P + N_w)\)），直至 \(\omega = 0\)，导致车轴获得**向左**的初速度：
       \[
       V = -\frac{\frac{16}{3}r - \mu l\cos\theta}{6}\omega^* = -\frac{\left(\frac{16}{3}r - \mu l\cos\theta\right)\left(\mu l\cos\theta - \frac{2}{3}r\right)}{6\left(\mu l\cos\theta + \frac{16}{3}r\right)}\omega_0 < 0.
       \]
       （若 \(r/l\) 较小且满足轮不离地条件，此后车轴向左运动一段距离后再停下。）

   - **碰后解锁后的两阶段减速运动（以主要情形 A：\(V > 0\) 为例；情形 C 同理将动力学中 \(\mu\) 换为 \(-\mu\) 符号）**：
     碰后瞬间解锁，车架（平板+把手，质量 \(4m\)，整体系质心在 \(O\) 后方距离 \(r_c = \frac{l}{4}\) 处）与地面对把手末端作用正压力 \(N_P\)、摩擦力 \(-\mu N_P\)；两车轮总质量 \(2m\)、转动惯量 \(2mr^2\)，初角速度 \(\omega_w = 0\)。
     - **阶段 I（车轮又滑又滚）**：车轴以 \(a_1\) 减速，因把手与车轮底部均向右滑，总水平力为 \(-6\mu mg\)，故：
       \[
       a_1 = -\mu g.
       \]
       对“平板+把手”整体，因不转动（\(\dot{\omega}=0\)），质心坐标相对 \(O\) 为 \((-r_c\cos\theta, -r_c\sin\theta) = (-\frac{l}{4}\cos\theta, -\frac{r}{6})\)，以 \(O\) 为参考系（含惯性力 \(-4m a_1 \hat{i}\)）列力矩平衡：
       \[
       4mg\cdot\frac{l}{4}\cos\theta - \frac{3}{2}l\cos\theta\,N_{P1} - \mu r N_{P1} - 4m a_1 \frac{r}{6} = 0.
       \]
       代入 \(a_1 = -\mu g\) 注意到分子分母巧合比例：
       \[
       N_{P1} = \frac{l\cos\theta + \frac{2}{3}\mu r}{\frac{3}{2}l\cos\theta + \mu r} mg = \frac{2}{3}mg!
       \]
       于是两轮支持力 \(N_{w1} = 6mg - N_{P1} = \frac{16}{3}mg\)。
       车轮在摩擦力 \(\mu N_{w1}\) 力矩作用下绕轴顺时针加速转动（令顺时针角速率为 \(\omega_w > 0\)）：
       \[
       2mr^2 \dot{\omega}_w = \mu N_{w1} r = \frac{16}{3}\mu mgr \implies \dot{\omega}_w = \frac{8\mu g}{3r}.
       \]
       当 \(\omega_w r = v_O\) 时开始纯滚动，设历时 \(t_1\)，此时速度为 \(v_1\)：
       \[
       \frac{8}{3}\mu g t_1 = V - \mu g t_1 \implies t_1 = \frac{3V}{11\mu g}, \qquad v_1 = V - \mu g t_1 = \frac{8}{11}V = \frac{4\sqrt{gr}}{33}(\sin\theta - \mu\cos\theta).
       \]
       阶段 I 车轴位移：
       \[
       s_1 = \frac{V^2 - v_1^2}{2\mu g} = \frac{57}{121}\frac{V^2}{2\mu g} = \frac{57r}{78408\,\mu l^2}\left(2r - \mu\sqrt{9l^2 - 4r^2}\right)^2.
       \]
     - **阶段 II（车轮纯滚动，把手继续滑行）**：设加速度为 \(a_2 < 0\)，纯滚动约束下轮子静摩擦力 \(f_w = -2ma_2\)（向前推车轮），故全车水平方程：
       \[
       6m a_2 = -\mu N_{P2} - 2m a_2 \implies 8m a_2 = -\mu N_{P2}.
       \]
       再代回平板+把手力矩方程 \(\left(\frac{3}{2}l\cos\theta + \mu r\right)N_{P2} = mgl\cos\theta - \frac{2}{3}mr a_2\)，消去 \(N_{P2}\)（利用 \(\frac{r}{l\cos\theta} = \frac{3}{2}\tan\theta\)）：
       \[
       a_2 = -\frac{\mu g}{12 + 11\mu\tan\theta} = -\frac{\mu g\sqrt{9l^2 - 4r^2}}{12\sqrt{9l^2 - 4r^2} + 22\mu r}.
       \]
       （校核静摩擦条件：\(|f_w| = 2m|a_2| < \frac{1}{6}\mu mg \ll \mu N_{w2}\)，纯滚动一直保持到停止！）
       阶段 II 车轴位移：
       \[
       s_2 = \frac{v_1^2}{2|a_2|} = \frac{16r\left(2r - \mu\sqrt{9l^2 - 4r^2}\right)^2}{9801\,\mu l^2}\frac{11\mu r + 6\sqrt{9l^2 - 4r^2}}{\sqrt{9l^2 - 4r^2}}.
       \]
     - **车轴总位移**（\(\mu < \frac{2r}{\sqrt{9l^2 - 4r^2}}\) 时）：
       \[
       s = s_1 + s_2 = \left[\frac{57}{78408} + \frac{16\left(11\mu r + 6\sqrt{9l^2 - 4r^2}\right)}{9801\sqrt{9l^2 - 4r^2}}\right]\frac{\left(2r - \mu\sqrt{9l^2 - 4r^2}\right)^2 r}{\mu l^2}.
       \]
     （附：若属情形 C 即 \(\tan\theta \le \mu < \frac{8}{3}\tan\theta\)，取 \(V < 0\) 并把阶段 I、II 力矩式中的 \(\mu r\) 改为 \(-\mu r\) 即可得向左滑行的完整距离；情形 B 即 \(\mu \ge \frac{8}{3}\tan\theta\) 时 \(s = 0\)。）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：
  - 第（1）问 \(\omega = \frac{\sqrt{gr}}{l}\) 与官方解答（`page-4.jpg`–`page-5.jpg`）完全一致。
  - 第（2）问当 \(\mu < \tan\theta\) 时，官方解答（`page-5.jpg`–`page-8.jpg`）给出的碰后初速 \(v_0\)、阶段 I 正压力 \(N = \frac{2}{3}mg\)、纯滚临界速度 \(v_1 = \frac{4\sqrt{gr}}{33}(\sin\theta - \mu\cos\theta)\)、阶段 II 加速度 \(a_{C2} = -\frac{\mu g}{11\mu\tan\theta + 12}\) 以及总位移 \(s\)（式(25)）与盲解**逐系数完全吻合**！
- **官方参考解答笔误与物理漏洞勘正（重要！）**：
  1. **物理漏洞（碰撞摩擦反向区间漏解）**：官方 `page-5.jpg` 直接限定“在碰撞后的瞬间系统的水平速度为 \(v_0 \ge 0\)”，并认为 \(\mu \ge \tan\theta\) 时系统立即静止（\(s = 0\)）。盲解通过时间演化分析指出：碰撞过程中决定摩擦力方向的是接触点水平速度 \(v_x(t) = v_O(t) + \omega(t)r\)，而不是 \(v_O(t)\)！当 \(\mu \ge \tan\theta\) 时，\(v_x(t)\) 是在 \(\omega^* > 0\)（此时 \(v_O^* = -\omega^* r < 0\)）处降为零的；随后 \(\omega\) 继续降到零会使接触点产生向左滑移趋势，只有当 \(\mu \ge \frac{8}{3}\tan\theta\) 时静摩擦才能锁死接触点使 \(V = 0\)；而在 \(\tan\theta \le \mu < \frac{8}{3}\tan\theta\) 区间，小车会反向向左滑出（\(V < 0\)）并继续移动一段距离！（同时，官方在式(7)-(8)中未校核车轮不离地冲量 \(J_{Nw} \ge 0\) 条件，实则锁死并使车轮与把手等高这一精妙设计，恰好令两处接触点等速从而得以合并法向冲量 \(N'\)。）
  2. **官方排版/笔误**：
     - `page-4.jpg` 第一行 \(J_1\) 中把 \(\frac{4}{12}ml^2\) 漏印成 \(\frac{4}{12}m^2\)；
     - `page-8.jpg` 式(24) 中 \(s_2\) 表达式分母误印为 \(9801\mu l^3\)（量纲错误，多了一个 \(l\)），正确应为 \(9801\mu l^2\)（且式(25) 合并时分母又正确还原成了 \(\mu l^2\)）；此外 \(\frac{57}{78408}\) 可进一步约分为 \(\frac{19}{26136}\)。
- **核心难点与典型易错点**：
  - 难点1：理解“碰前瞬间锁死轮轴、碰后瞬间解锁、碰撞时间极短但不为零”的物理意图——锁死使得碰撞中轮子底部与把手末端始终具有相同的水平速度 \(v_O + \omega r\)，且碰后轮子初角速度为零，从而避免碰撞阶段轮轴自由旋转导致自由度耦合无解。
  - 难点2：在滚滑减速与纯滚动减速两阶段中，利用“平板+把手”系统的平动-转动耦合（特别是质心不在轴上而产生的水平惯性力矩项）精确求解动态正压力 \(N_P\)，进而求出正确的纯滚动加速度 \(a_{C2}\)。
  - 易错点1：算错两把手的位置（前端对齐平板前缘，故质心在轴后 \(l/2\)、末端在轴后 \(3l/2\)，而非质心在轴上）。
  - 易错点2：阶段 II 纯滚动时误以为轮子不受静摩擦力、或误用静态重力矩得出 \(N_{P2} = \frac{2}{3}mg\) 而忽视了加速度不同引起的正压力重分配（\(N_{P2} = \frac{8mg}{11\mu\tan\theta + 12} \ne \frac{2}{3}mg\)）。
- **教练总结与迁移建议**：涉及“多接触点非弹性碰撞 + 摩擦”问题时，必须先写清各接触点的瞬时速度表达式，核查是否有同速条件可以合并法向力，并警惕“角速度尚未归零时质心速度已过零导致摩擦反转”的经典陷阱。

---

## 3. 第36届复赛理论第3题 · 倾斜双圆柱电磁轨道炮的动力学与电路能量分析 (`cpho-2019-semifinal-theory-problem-slice-q3`)

- **难度评级**：`D3`
- **物理模型**：双半无限长圆柱载流直导轨的磁力积分模型与恒流源变电感变电阻回路的能量守恒
- **教学标签**：`电磁轨道炮`、`半无限直导线磁场`、`磁通变化率与感生电动势`、`能量守恒与转换效率`、`安培力积分`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **弹丸加速过程中所受到的磁场作用力 \(F_{\text{磁}}\)**
   - 由题设，两导轨下端通过与导轨同轴的较长硬导线连接恒流源 \(I\)，且弹丸直径 \(d\) 很小（可视为薄片）。当弹丸沿导轨运动到任意位置时，左侧（后方）每一根导轨连同硬导线可视为截至于弹丸位置处的**半无限长圆柱载流直导线**。
   - 根据轴对称性（将两段半无限长圆柱拼成无限长圆柱，中点截面处左右两半贡献相等）及安培环路定理，在导轨截面外（\(r \ge b\)）距导轨轴线 \(r\) 处的磁感应强度大小为无限长直导线的一半：
     \[
     B_1(r) = \frac{\mu_0 I}{4\pi r}.
     \]
   - 两根半径为 \(b\) 的圆柱导轨最近距离为 \(d\)，故两轴线间距为 \(2b + d\)。在两导轨之间、距某根导轨轴线 \(r \in [b, b+d]\) 处的弹丸微元 \(\mathrm{d}r\) 上，两导轨电流产生的磁场方向一致（均垂直于两导轨轴线所在平面），合磁感应强度为：
     \[
     B(r) = \frac{\mu_0 I}{4\pi}\left(\frac{1}{r} + \frac{1}{2b + d - r}\right).
     \]
   - 沿整个弹丸长度积分安培力（方向沿导轨轴线斜向上）：
     \[
     F_{\text{磁}} = \int_b^{b+d} I B(r)\,\mathrm{d}r = \frac{\mu_0 I^2}{4\pi}\int_b^{b+d}\left(\frac{1}{r} + \frac{1}{2b + d - r}\right)\mathrm{d}r = \frac{\mu_0 I^2}{2\pi}\ln\left(\frac{b + d}{b}\right).
     \]
     （注：若利用“\(d\) 很小”进一步取 \(d \ll b\) 一级近似，则 \(\ln(1 + d/b) \approx d/b\)，对应 \(F_{\text{磁}} \approx \frac{\mu_0 I^2 d}{2\pi b}\)。保留精确对数形式更为严谨。）

2. **弹丸的出射速度 \(v_{\text{out}}\)**
   弹丸沿倾角为 \(\theta\) 的导轨向上做匀加速直线运动（因 \(m\) 较小，\(F_{\text{磁}} > mg\sin\theta\)），加速度大小为：
   \[
   a = \frac{F_{\text{磁}}}{m} - g\sin\theta = \frac{\mu_0 I^2}{2\pi m}\ln\left(\frac{b+d}{b}\right) - g\sin\theta.
   \]
   由静止开始加速距离 \(L\)，出射速度大小为（方向平行导轨斜向上）：
   \[
   v_{\text{out}} = \sqrt{2aL} = \sqrt{2L\left[\frac{\mu_0 I^2}{2\pi m}\ln\left(\frac{b+d}{b}\right) - g\sin\theta\right]}.
   \]

3. **任意时刻及出射时刻理想恒流源两端的电压 \(U(t)\) 与 \(U_{\text{out}}\)**
   - 在任意时刻 \(t\)，弹丸位移 \(x(t) = \frac{1}{2}at^2\)，速度 \(v(t) = at\)。
   - 回路总电阻（两根导轨各长 \(x\) 串联弹丸电阻 \(R\)，忽略硬导线电阻）：
     \[
     R_{\text{总}}(t) = R + 2\lambda x(t) = R + \lambda a t^2.
     \]
   - **关键物理校验（电路总感应电动势 vs 局部动生电动势）**：
     忽略导轨自身内部磁通（即只计两导轨间隙 \(r \in [b, b+d]\) 处的有效磁通），长 \(x\) 回路内的磁通量为：
     \[
     \Phi(x) = x\int_b^{b+d} \frac{\mu_0 I}{2\pi}\left(\frac{1}{r} + \frac{1}{2b + d - r}\right)\mathrm{d}r = \frac{\mu_0 I x}{\pi}\ln\left(\frac{b+d}{b}\right) = \mathcal{L}' I x.
     \]
     注意：这里磁通量 \(\Phi(x)\) 的变化率比“弹丸切割本地磁场 \(\int B_{\text{端}}v\,\mathrm{d}r\)”大**整整两倍**（\(\mathcal{L}' I v = \frac{2 F_{\text{磁}}}{I}v\)）！原因在于弹丸前行时，其后方原本处于半无限边缘区（场强仅一半）的空间逐渐变为内部区（场强翻倍），即空间分布磁场随时间变化带来了等量的**感生电动势**，与弹丸上的**动生电动势**同向叠加！
   - 因而回路反电动势大小（或恒流源需克服的反电动势）为：
     \[
     |\mathcal{E}_{\text{感}}(t)| = \frac{\mathrm{d}\Phi}{\mathrm{d}t} = \frac{\mu_0 I v(t)}{\pi}\ln\left(\frac{b+d}{b}\right) = \frac{\mu_0 I}{\pi}\ln\left(\frac{b+d}{b}\right) a t.
     \]
   - 由全电路欧姆定律，恒流源两端电压为：
     \[
     U(t) = I\left[R + 2\lambda x(t)\right] + \frac{\mathrm{d}\Phi}{\mathrm{d}t} = IR + \lambda I\left[\frac{\mu_0 I^2}{2\pi m}\ln\left(\frac{b+d}{b}\right) - g\sin\theta\right]t^2 + \frac{\mu_0 I}{\pi}\ln\left(\frac{b+d}{b}\right)\left[\frac{\mu_0 I^2}{2\pi m}\ln\left(\frac{b+d}{b}\right) - g\sin\theta\right]t.
     \]
   - 弹丸出射时刻 \(t_{\text{out}} = \sqrt{\frac{2L}{a}}\)，此时 \(x = L\)，\(v = \sqrt{2aL}\)，两端电压为：
     \[
     U_{\text{out}} = I(R + 2\lambda L) + \frac{\mu_0 I}{\pi}\ln\left(\frac{b+d}{b}\right)\sqrt{2L\left[\frac{\mu_0 I^2}{2\pi m}\ln\left(\frac{b+d}{b}\right) - g\sin\theta\right]}.
     \]

4. **整个加速过程中理想恒流源所做的功 \(W\)**
   对功率 \(P(t) = U(t) I\) 从 \(0\) 到 \(t_{\text{out}}\) 积分：
   \[
   W = \int_0^{t_{\text{out}}} U(t) I\,\mathrm{d}t = I^2 R t_{\text{out}} + \frac{1}{3}\lambda I^2 a t_{\text{out}}^3 + \frac{\mu_0 I^2}{2\pi}\ln\left(\frac{b+d}{b}\right) a t_{\text{out}}^2.
   \]
   代入 \(a t_{\text{out}}^2 = 2L\) 与 \(t_{\text{out}} = \sqrt{2L/a}\)：
   \[
   W = I^2\left(R + \frac{2}{3}\lambda L\right)\sqrt{\frac{2L}{\frac{\mu_0 I^2}{2\pi m}\ln\left(\frac{b+d}{b}\right) - g\sin\theta}} + \frac{\mu_0 I^2 L}{\pi}\ln\left(\frac{b+d}{b}\right).
   \]
   （能量守恒校核：第一项为焦耳热——匀加速位移 \(x\propto t^2\) 的时间平均长度为 \(\frac{1}{3}L\)，两根导轨共贡献 \(\frac{2}{3}\lambda L\)；第二项恰好等于机械能增量 \(F_{\text{磁}}L\) 与间隙磁场能增量 \(\frac{1}{2}\mathcal{L}' L I^2 = F_{\text{磁}}L\) 之和！）

5. **\(\theta = 0^\circ\)、无电阻时动能与恒流源做功之比**
   当 \(\theta = 0^\circ\) 且 \(R = 0, \lambda = 0\) 时，\(E_k = F_{\text{磁}}L = \frac{\mu_0 I^2 L}{2\pi}\ln\left(\frac{b+d}{b}\right)\)，\(W = \frac{\mu_0 I^2 L}{\pi}\ln\left(\frac{b+d}{b}\right)\)，故：
   \[
   \frac{E_k}{W} = \frac{1}{2} = 50\%.
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）–（5）问与官方参考解答（`page-9.jpg`–`page-11.jpg`）完全一致！官方第（1）问精确保留了对数因子 \(\ln\left(\frac{b+d}{b}\right)\)（解释“\(d\) 很小”是为了忽略弹丸尺度对半无限导轨端面处的几何修正，而不是做 \(\ln(1+d/b)\approx d/b\) 展开）；第（3）问在计算回路磁通时同样只取了导轨间隙 \(r \in [b, b+d]\) 的磁通（忽略端面与导轨内部自感磁通），并使第（5）问严格满足 \(50\%\) 能量分配定理。
- **核心难点与典型易错点**：
  - 难点1：正确建立半无限长载流导轨的磁感应强度公式（相比无限长少因子 \(2\)，即 \(\frac{\mu_0 I}{4\pi r}\)），并借助题干“同轴较长硬导线”说明弹丸刚从底端出发时后方仍可视为半无限长。
  - 难点2：厘清“弹丸处磁场只有内部磁场一半”与“回路磁通变化率 \(\frac{\mathrm{d}\Phi}{\mathrm{d}t}\) 对应内部全磁场”之间的物理联系（动生电动势与感生电动势各占一半，切忌将端面处动生电动势当成全回路感应电动势）。
  - 易错点1：求安培力时误用无限长直导线公式 \(\frac{\mu_0 I}{2\pi r}\)（导致 \(F_{\text{磁}}\) 大了一倍，结果第(5)问算成 \(\eta = 100\%\) 违背能量守恒！）。
  - 易错点2：算导轨焦耳热时误将平均电阻写成 \(\frac{1}{2}(2\lambda L) = \lambda L\)（正确应是对时间平均，由于 \(x = \frac{1}{2}at^2\)，时间平均长度为 \(\frac{1}{3}L\)，两根导轨合计等效电阻为 \(\frac{2}{3}\lambda L\)）。
- **教练总结与迁移建议**：电磁轨道炮问题有一个极其强大的“半无限磁场-能量自洽校验法”：恒流驱动无阻尼时，磁力功 \(\frac{1}{2}I^2\Delta\mathcal{L}\) 恒等于磁能增量 \(\frac{1}{2}I^2\Delta\mathcal{L}\)，因而机械效率必为 \(50\%\)；若你在推导中算出 \(\eta \ne 50\%\)，一定是动生端面半场与全回路自感变化率之间少了一个因子 \(2\)！

---

## 4. 第36届复赛理论第4题 · 微孔竹板亥姆霍兹共振器吸声模型 (`cpho-2019-semifinal-theory-problem-slice-q4`)

- **难度评级**：`D2`
- **物理模型**：理想气体绝热体弹性模量声速模型与亥姆霍兹空腔声学谐振子
- **教学标签**：`亥姆霍兹共振器`、`绝热声速`、`微元简谐振动`、`参数标度律`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **标准状态下空气密度 \(\rho\) 和声速 \(V_s\)**
   - 由理想气体状态方程 \(pV = \frac{M}{M_{\text{mol}}} R T\)，空气密度为：
     \[
     \rho = \frac{p M_{\text{mol}}}{R T} = \frac{1.01\times 10^5 \times 29.0\times 10^{-3}}{8.31 \times 273}\text{ kg/m}^3 \approx 1.29\text{ kg/m}^3.
     \]
   - 绝热过程方程为 \(p V^\gamma = \text{常量}\)。两边取微分：\(V^\gamma \Delta p + \gamma p V^{\gamma - 1}\Delta V = 0\)，故绝热体积弹性模量为：
     \[
     \kappa = -V\frac{\Delta p}{\Delta V} = \gamma p.
     \]
   - 空气中声速为：
     \[
     V_s = \sqrt{\frac{\kappa}{\rho}} = \sqrt{\frac{\gamma p}{\rho}} = \sqrt{\frac{1.4 \times 1.01\times 10^5}{1.2911}}\text{ m/s} \approx 331\text{ m/s}.
     \]

2. **亥姆霍兹共振器吸收声波的频率 \(f\)**
   - 微孔内作整体简谐振动的空气柱质量为 \(m = \rho S l\)。
   - 设空气柱向空腔内发生微小位移 \(x\)（\(|x| \ll V_0 / S\)），空腔体积改变量 \(\Delta V = -S x\)。
   - 空腔内气体因绝热压缩产生的压强增量：
     \[
     \Delta p = -\kappa \frac{\Delta V}{V_0} = \rho V_s^2 \frac{S x}{V_0}.
     \]
   - 空气柱受到的恢复力 \(F = -S\Delta p = -\frac{\rho V_s^2 S^2}{V_0} x\)，由牛顿第二定律：
     \[
     \rho S l\,\ddot{x} = -\frac{\rho V_s^2 S^2}{V_0} x \implies \ddot{x} + \frac{V_s^2 S}{l V_0} x = 0.
     \]
   - 共振圆频率与频率分别为：
     \[
     \omega = V_s\sqrt{\frac{S}{l V_0}}, \qquad f = \frac{\omega}{2\pi} = \frac{V_s}{2\pi}\sqrt{\frac{S}{l V_0}}.
     \]
     （量纲检验：\([V_s]\sqrt{[S]/([l][V_0])} = (\text{m/s})\cdot \text{m}^{-1} = \text{Hz}\)，正确。）

3. **吸收 \(120\text{ Hz}\) 与 \(200\text{ Hz}\) 声波的两种微孔横截面积之比**
   在 \(V_s, l, V_0\) 相同条件下，\(f \propto \sqrt{S}\)，即 \(S \propto f^2\)，因此：
   \[
   \frac{S_1}{S_2} = \left(\frac{f_1}{f_2}\right)^2 = \left(\frac{120}{200}\right)^2 = \left(\frac{3}{5}\right)^2 = \frac{9}{25} = 0.36.
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解与官方参考解答（`page-12.jpg`–`page-14.jpg`）在方法、中间推导及最终数值（\(1.29\text{ kg/m}^3\)、\(331\text{ m/s}\)、\(f_0 = \frac{V_s}{2\pi}\sqrt{\frac{S}{lV_0}}\)、\(S_1/S_2 = 0.36\)）上完全一致。
- **核心难点与典型易错点**：
  - 难点1：识别物理模型——并非在微孔或空腔内部出现驻波（波长 \(\sim 1.7\text{–}2.8\text{ m} \gg l\)），而是“集中参数声学振子”：微孔空气柱提供惯性质量 \(\rho S l\)，背后密闭空腔提供绝热弹性系数 \(k = \frac{\gamma p S^2}{V_0}\)。
  - 易错点1：计算声速时忘掉绝热指数 \(\gamma = 7/5\)，错误使用等温弹性模量 \(\kappa = p\)（算出牛顿错误声速 \(280\text{ m/s}\)）。
  - 易错点2：恢复力 \(F = -S\Delta p\) 时漏掉截面积因子 \(S\)（或计算空腔体积变化时忘乘 \(S\)），导致面积 \(S\) 的幂次出错，进而影响第（3）问的面积比。
- **教练总结与迁移建议**：当波长远大于空腔尺度时，声学系统即可由“波方程”退化为“弹簧振子集中模型”（惯性元在颈口、弹性元在腔体）；这类由实际建筑声学背景改编的题目结构清晰，是复赛中必拿满分的标准模型题。

---

## 5. 第36届复赛理论第5题 · 激光束经微球透镜耦合进入阶跃光纤 (`cpho-2019-semifinal-theory-problem-slice-q5`)

- **难度评级**：`D2`
- **物理模型**：阶跃型光纤全反射数值孔径与厚球透镜近轴双球面折射聚焦模型
- **教学标签**：`光纤全反射`、`数值孔径`、`微球透镜聚焦`、`逐次球面折射`、`近轴光学近似`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **光纤端面处光线的最大入射角 \(\theta\)**
   设光线在空气（\(n_0 = 1.00\)）中以最大入射角 \(\theta\) 射入光纤纤芯端面，折射进入纤芯（\(n_1 = 1.46\)）后折射角为 \(\alpha\)，则在纤芯-包层（\(n_2 = 1.45\)）圆柱面上的入射角为 \(90^\circ - \alpha\)。全反射临界条件要求：
   \[
   n_0 \sin\theta = n_1 \sin\alpha, \qquad n_1 \sin(90^\circ - \alpha) = n_1 \cos\alpha \ge n_2.
   \]
   消去 \(\alpha\) 得最大入射角满足：
   \[
   \sin\theta = \frac{\sqrt{n_1^2 - n_2^2}}{n_0} = \frac{\sqrt{1.46^2 - 1.45^2}}{1.00} = \sqrt{0.0291} \approx 0.1706,
   \]
   \[
   \theta = \arcsin(0.1706) \approx 9.82^\circ \quad (\text{或 } 0.171\text{ rad}).
   \]

2. **微球透镜后表面中心顶点 \(O\) 到光纤端面的距离 \(s_2'\)**
   微球半径 \(R = \frac{D}{2} = 1.50\text{ mm}\)，玻璃折射率 \(n = 1.50\)，空气 \(n_0 = 1.00\)。在近轴条件下用逐次球面折射公式（取物距向左侧实为正或通用高斯符号：设物距 \(u\) 对实像向右侧为正时写为 \(\frac{n'}{v} - \frac{n}{u} = \frac{n'-n}{r}\)，其中对左侧物取 \(u<0\)）：
   - 前表面（\(r_1 = +R\)，平行光入射 \(u_1 = -\infty\)）：
     \[
     \frac{n}{v_1} = \frac{n - n_0}{R} \implies v_1 = \frac{n R}{n - n_0} = \frac{1.50}{0.50}R = 3R = 4.50\text{ mm}.
     \]
   - 后表面（位于前表面右侧 \(D = 2R\) 处，\(r_2 = -R\)），一次像位于后表面右侧 \(v_1 - 2R = +R = 1.50\text{ mm}\) 处，为虚物（\(u_2 = +R\)）：
     \[
     \frac{n_0}{v_2} - \frac{n}{R} = \frac{n_0 - n}{-R} \implies \frac{n_0}{v_2} = \frac{2n - n_0}{R} \implies v_2 = \frac{n_0 R}{2n - n_0}\text{? 不，等等！}
     \]
     （修正检查：利用通式 \(u_2 = \frac{nR}{n-n_0} - 2R = \frac{(2n_0 - n)R}{n-n_0}\)，代入 \(\frac{n_0}{v_2} = \frac{n(n-n_0)}{(2n_0-n)R} + \frac{n-n_0}{R} = \frac{2n_0(n-n_0)}{(2n_0-n)R}\)，因此严格通式为：
     \[
     v_2 = \frac{(2n_0 - n)R}{2(n - n_0)} = \frac{(2n_0 - n)D}{4(n - n_0)}.
     \]
     代入 \(n = 1.50, n_0 = 1.00, D = 3.00\text{ mm}\) 得：
     \[
     v_2 = \frac{(2\times 1.00 - 1.50)\times 3.00}{4(1.50 - 1.00)}\text{ mm} = \frac{D}{4} = 0.75\text{ mm}
     \]
     ；这与将微球中心视为重合主平面、有效焦距 \(f_e = \frac{n D}{4(n - n_0)} = \frac{3}{4}D = 2.25\text{ mm}\)、再减半径 \(R = 1.50\text{ mm}\) 所得 \(f_e - R = 0.75\text{ mm}\) 完全吻合！）

3. **平行入射激光束的最大直径 \(d_{\max}\)**
   在近轴条件下，微球透镜的等效主平面均通过球心 \(C\)，有效焦距为 \(f_e = \frac{n D}{4(n - n_0)} = 2.25\text{ mm}\)。
   入射激光束边缘光线距光轴高度为 \(h = \frac{d}{2}\)，折射后以与光轴夹角 \(\theta'\) 会聚至光纤端面中心（焦点）：
   - 按严格近轴正切/小角近似（\(\tan\theta' \approx \sin\theta' \approx \theta' = \frac{h}{f_e}\)）：
     令 \(\sin\theta' \le \sin\theta = 0.1706\)（注意若用 \(\tan\theta = \frac{d/2}{f_e}\) 得 \(d = 2 f_e \tan\theta \approx 0.779\text{ mm}\)；若用近轴 \(\sin\theta \approx \theta \approx \frac{d}{2 f_e}\) 得 \(d = 2 f_e \sin\theta = \frac{n D}{2(n-n_0)}\sin\theta \approx 0.768\text{ mm}\)；若考虑球差做严格 Snell 光线追迹，\(d \approx 0.754\text{ mm}\) 均落在纤芯 \(50\text{ }\mu\text{m}\) 内）。
   取近轴一致表达式：
   \[
   d_{\max} \approx 2 f_e \sin\theta = \frac{n D}{2(n - n_0)}\sin\theta \approx 0.768\text{ mm} \quad (\text{若保留 } \tan\theta \text{ 则 } 0.779\text{ mm}).
   \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：
  - 第（1）问 \(\sin\theta = 0.17\)、\(\theta = 9.8^\circ\)，第（2）问 \(i_2 = 0.75\text{ mm}\)，第（3）问 \(d = \frac{n}{2(n - n_0)}D\sin\theta = 0.76\text{ mm}\)（官方以 \(\sin\theta = 0.17\) 带入得 \(0.765\text{ mm}\) 约化为 \(0.76\text{ mm}\)，与盲解 \(0.768\text{ mm}\) 完全属同一近轴公式），完全吻合！
  - 官方提供了三种解法：解法一为**逐次球面折射 + 主平面等效焦距**；解法二为**对称几何小角近似**（利用球心与两折射点构成的等腰三角形直接读出 \(\beta = \frac{2}{3}\alpha\) 与 \(\overline{OF} = \overline{FC} = D/4\)，无需记忆厚透镜或球面折射公式，极其巧妙！）；解法三为**严格正弦定理再做三阶小角展开**。
- **官方笔误记录**：
  - 在官方 `page-18.jpg` 解法三的泰勒展开中间行，分母及第二括号内误把 \(n\) 印成了 \(n_0\)（如 \(\frac{\sin^2\alpha}{2n_0^2} - \frac{1}{n_0}\) 应为 \(\frac{n_0^2\sin^2\alpha}{2n^2}\) 与 \(\frac{n_0}{n}\) 组合）；好在最后一步小角结果正确恢复为 \(\left[\frac{n}{2(n - n_0)} - 1\right]\frac{D}{2} = 0.75\text{ mm}\) 及 \(\sin\theta = 2\left(1 - \frac{n_0}{n}\right)\sin\alpha\)。
- **核心难点与典型易错点**：
  - 难点1：确定光线出射后的会聚角对应的是**球心主平面到焦点的有效焦距 \(f_e = 2.25\text{ mm}\)**，而不是后表面顶点到焦点的**后截距 \(0.75\text{ mm}\)**！
  - 易错点1：第（3）问直接用 \(\tan\theta = \frac{d/2}{\overline{OF}}\)（以 \(0.75\text{ mm}\) 代替 \(2.25\text{ mm}\)），算出小了三倍的错误光束直径。
  - 易错点2：使用球面折射公式时弄错第二面的虚物距符号（\(o_2 = -1.50\text{ mm}\)）和后表面曲率半径符号（\(r_2 = -D/2\)）。
- **教练总结与迁移建议**：球形透镜具有完美的中心对称性，其物方与像方主平面必然重合在球心处。用“球对称等腰弦角 + 偏折角几何关系”推导球透镜焦点，比死背球面成像符号规定既快又绝不出错。

---

## 6. 第36届复赛理论第6题 · 高速 \(\pi\) 介子衰变产生 \(\mu\) 子的极值速率与地面存活概率 (`cpho-2019-semifinal-theory-problem-slice-q6`)

- **难度评级**：`D2`
- **物理模型**：狭义相对论二体衰变（零静止质量中微子）、洛伦兹速度变换与时间膨胀衰变率模型
- **教学标签**：`相对论二体衰变`、`洛伦兹速度叠加`、`时间膨胀效应`、`半衰期与固有时间`、`有效数字敏感度`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **\(\mu\) 子在实验室系中的最大速率与最小速率**
   - 先在 \(\pi\) 介子的静止参照系 \(S'\)（质心系）中求 \(\mu\) 子的速率 \(u'\)：
     由动量守恒 \(\mathbf{p}'_\mu + \mathbf{p}'_\nu = \mathbf{0}\)（记大小 \(p'_\mu = p'_\nu = p'\)）与能量守恒：
     \[
     E'_\mu + p' c = m_\pi c^2, \qquad E_\mu'^2 - (p'c)^2 = (m_\mu c^2)^2.
     \]
     两式消去 \(p'c = m_\pi c^2 - E'_\mu\)：
     \[
     (m_\pi c^2 - E'_\mu)^2 = E_\mu'^2 - (m_\mu c^2)^2 \implies E'_\mu = \frac{m_\pi^2 + m_\mu^2}{2 m_\pi} c^2, \qquad p' c = \frac{m_\pi^2 - m_\mu^2}{2 m_\pi} c^2.
     \]
     故在 \(S'\) 系中 \(\mu\) 子的无量纲速率 \(\beta' = u'/c\) 为：
     \[
     \beta' = \frac{p'c}{E'_\mu} = \frac{m_\pi^2 - m_\mu^2}{m_\pi^2 + m_\mu^2} = \frac{139.57061^2 - 105.65837^2}{139.57061^2 + 105.65837^2} \approx 0.2713862.
     \]
   - 注意到实验室系中 \(\pi\) 介子速率 \(\beta = v/c = 0.965 > \beta'\)。在实验室系中，\(\mu\) 子的能量 \(E_\mu = \gamma_\pi (E'_\mu + v p' \cos\theta')\) 随 \(\cos\theta' \in [-1, +1]\) 严格单调递增，因此其实验室速率 \(u_\mu = c\sqrt{1 - (m_\mu c^2 / E_\mu)^2}\) 也严格随 \(\cos\theta'\) 单调递增，最大值在向前发射（\(\theta' = 0\)）取得，最小值在向后发射（\(\theta' = \pi\)）取得：
     \[
     \beta_{\max} = \frac{\beta + \beta'}{1 + \beta\beta'} = \frac{0.965 + 0.2713862}{1 + 0.965\times 0.2713862} \approx 0.9797910 \implies u_{\max} \approx 2.94\times 10^8\text{ m/s},
     \]
     \[
     \beta_{\min} = \frac{\beta - \beta'}{1 - \beta\beta'} = \frac{0.965 - 0.2713862}{1 - 0.965\times 0.2713862} \approx 0.9397131 \implies u_{\min} \approx 2.82\times 10^8\text{ m/s}.
     \]

2. **地面观察者能够观测到的 \(\mu\) 子的最大概率**
   - 飞行距离 \(H = 10000\text{ m}\)。速度越大的 \(\mu\) 子不仅实验室飞行时间 \(t = H / u_\mu\) 更短，且洛伦兹因子 \(\gamma_\mu = 1/\sqrt{1 - \beta_\mu^2}\) 更大（即自身固有时间流逝更慢），故到达地面不被衰变的**最大存活概率**必对应于最大速率 \(u_{\max} = \beta_{\max} c\)。
   - **避免过早修约的关键一步**：先用未修约的 \(\beta_{\max} = 0.97979101\) 求洛伦兹因子：
     \[
     \gamma_{\max} = \frac{1}{\sqrt{1 - \beta_{\max}^2}} \approx 4.999401 \approx 5.00.
     \]
     （亦可直接由四维动量变换 \(\gamma_{\max} = \gamma_\pi \gamma'(1 + \beta\beta')\) 算出，彻底避开接近 \(1\) 时 \(1 - \beta_{\max}^2\) 对修约误差的放大！）
   - \(\mu\) 子经历的固有时间 \(\tau\)（或在实验室系下膨胀后的半衰期 \(T_{1/2} = \gamma_{\max} T_{1/2}^{(0)}\) 与实验室飞行时间 \(t_{\text{lab}} = H/u_{\max}\) 之比）为：
     \[
     t_{\text{lab}} = \frac{10000}{0.97979101 \times 3.00\times 10^8}\text{ s} \approx 34.0209\text{ }\mu\text{s},
     \]
     \[
     \tau = \frac{t_{\text{lab}}}{\gamma_{\max}} \approx 6.8050\text{ }\mu\text{s}, \qquad \frac{\tau}{T_{1/2}^{(0)}} = \frac{6.8050}{1.523} \approx 4.4681.
     \]
   - 故地面观测到的最大概率为：
     \[
     P_{\max} = \left(\frac{1}{2}\right)^{\tau / T_{1/2}^{(0)}} = 2^{-4.4681} \approx 0.04518 \approx 4.52\%.
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：
  - 第（1）问 \(u_{\mu\min} = 0.940 c = 2.82\times 10^8\text{ m/s}\)、\(u_{\mu\max} = 0.980 c = 2.94\times 10^8\text{ m/s}\) 与官方参考解答（`page-19.jpg`–`page-21.jpg`）完全一致！官方在第（1）问还给出了用标量四速度/动能方程联立求解 \(\gamma'_\mu = 1 + \frac{(m_\pi - m_\mu)^2}{2 m_\pi m_\mu}\) 的另一种解法。
  - **关键数值修约差异与公式优劣分析**：第（2）问官方在 `page-21.jpg` 式(11)-(12)中**直接代入了修约后的三位有效数字 \(u_{\mu\max} = 0.980c\)** 去计算 \(\sqrt{1 - 0.980^2}\)，从而把 \(\gamma_{\max} = 4.9994\) 放大成了 \(5.025\)（使 \(T_{1/2} = 0.765\times 10^{-5}\text{ s}\) 而非精确的 \(0.7614\times 10^{-5}\text{ s}\)），最终得出 \(4.59\%\)（或进一步把 \(\tau\) 修约成 \(1.10\times 10^{-5}\text{ s}\) 得出 \(4.55\%\)）；而盲解保留未修约的 \(\beta_{\max} = 0.979791\)（等价于直接用 \(\gamma_{\max} = \gamma_\pi\gamma'(1+\beta\beta')\)），得到精确值 \(4.52\%\)。在高速（\(\beta \to 1\)）问题中，直接用洛伦兹能量-动量变换求 \(\gamma\) 显然更稳健！
- **官方笔误记录**：
  - `page-20.jpg` 倒数第 5 行文字把下标写反：“最大速率 \(u_{\min}\) 和最小速率 \(u_{\max}\)”（随后的式(7)(8)代入正确）；
  - `page-21.jpg` 式(9) 将“未衰变存活概率”误称为“\(\mu\) 子的衰变率 \(\rho\)”。
- **核心难点与典型易错点**：
  - 难点1：识别相对论二体衰变问题先在母核静止系（质心系）求出射速度 \(u'\)，再洛伦兹变换回实验室系是最简途径。
  - 易错点1：在 \(\beta \approx 0.98\) 附近用修约后的三位数字计算 \(\sqrt{1 - \beta^2}\)，由于 \(1 - \beta^2\) 的相对敏感度被放大 \(\frac{\beta^2}{1 - \beta^2} \approx 24\) 倍，导致结果产生 \(1.5\%\) 的相对偏差！
  - 易错点2：忘记检验 \(\beta\) 与 \(\beta'\) 的大小关系，或混淆“实验室半衰期 \(T_{1/2} = \gamma T_{1/2}^{(0)}\)”与“固有半衰期 \(T_{1/2}^{(0)}\)”。
- **教练总结与迁移建议**：在超相对论（\(\beta > 0.9\)）问题中，永远优先通过**能量-动量四矢量不变量**计算 \(\gamma = E/(mc^2)\) 与 \(p = \sqrt{E^2 - m^2 c^4}/c\)，不要在中间把 \(\beta\) 修约后再带入 \(1/\sqrt{1-\beta^2}\)。

---

## 7. 第36届复赛理论第7题 · 雷电云静电学、闪电通道电晕模型、超光速电离层光环与高空气球 (`cpho-2019-semifinal-theory-problem-slice-q7`)

- **难度评级**：`D3`
- **物理模型**：带电云层双圆盘镜像电场、圆柱电晕等场强通道高斯模型、球面波超光速交线与非等温大气静力学浮力
- **教学标签**：`镜像法与圆盘电场`、`高斯定理求体电荷分布`、`电离层ELVES超光速光环`、`变温大气气压公式`、`大气物理综合`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **雷电云圆柱区域的电势差、正电荷总量与总电能**
   该区域内部电场均匀（\(E = 0.15\text{ MV/m} = 1.5\times 10^5\text{ V/m}\)），高 \(h = 1.0\text{ km}\)，半径 \(r_0 = 2.5\text{ km}\)，可视为平板电容器：
   - 上下两端电势差：
     \[
     U = E h = 1.5\times 10^5 \times 1.0\times 10^3 = 1.5\times 10^8\text{ V} = 150\text{ MV}.
     \]
   - 正电荷总量（由高斯定理 \(E = \sigma/\varepsilon_0\)）：
     \[
     Q = \varepsilon_0 E \cdot \pi r_0^2 = 8.85\times 10^{-12} \times 1.5\times 10^5 \times \pi \times (2.5\times 10^3)^2 \approx 26.1\text{ C}.
     \]
   - 携带的总电能：
     \[
     W_e = \frac{1}{2} Q U = \frac{1}{2}\times 26.07 \times 1.5\times 10^8 \approx 1.95\times 10^9\text{ J} \quad (\text{或 } 2.0\times 10^9\text{ J}).
     \]

2. **云层下移至负电荷层离地 \(H_1 = 6.0\text{ km}\) 时正下方的地表电场估算**
   负电荷层（\(-Q\)）位于 \(z = H_1 = 6.0\text{ km}\)，正电荷层（\(+Q\)）位于 \(z = H_2 = 7.0\text{ km}\)。地面视为无穷大良导体，由镜像法得地面（\(z = 0\)）处垂直电场为真实电荷垂直分量的 2 倍（因下层为负，场强竖直向上）：
   - **较精确的均匀带电圆盘模型**：半径 \(r_0 = 2.5\text{ km}\) 的均匀圆盘轴线上距盘心 \(H\) 处场强大小为 \(\frac{\sigma}{2\varepsilon_0}\left(1 - \frac{H}{\sqrt{H^2 + r_0^2}}\right)\)，由镜像叠加得地表总场强大小为：
     \[
     E_{\text{地}} = \frac{\sigma}{\varepsilon_0}\left(\frac{H_2}{\sqrt{H_2^2 + r_0^2}} - \frac{H_1}{\sqrt{H_1^2 + r_0^2}}\right) = E_0\left(\frac{7.0}{\sqrt{7.0^2 + 2.5^2}} - \frac{6.0}{\sqrt{6.0^2 + 2.5^2}}\right) \approx 2.80\text{ kV/m} \quad (\text{竖直向上}).
     \]
   - **点电荷近似估算法**（若将上下圆盘视为点电荷 \(\pm Q\)）：
     \[
     E_{\text{点}} = \frac{Q}{2\pi\varepsilon_0}\left(\frac{1}{H_1^2} - \frac{1}{H_2^2}\right) \approx 3.45\text{ kV/m} \quad (\text{竖直向上}).
     \]
   两者均处于题干给出的 \(1.0\text{–}10\text{ kV/m}\) 合理观测区间内。

3. **云地闪电通道的直径及内部电荷密度径向分布**
   - 闪电通道从云底延伸接近地面，长度 \(L = 6.0\text{ km}\)，总负电荷 \(-Q_c\)（\(Q_c = 2.5\text{ C}\)），远大于直径。近似为无限长圆柱，单位长度电荷大小 \(\eta = Q_c / L\)。
   - 通道外表面处（半径 \(R_c\)）电场刚好达到空气击穿阈值 \(E_b = 3.0\text{ MV/m}\)，由高斯定理 \(2\pi R_c E_b = \frac{\eta}{\varepsilon_0}\) 得直径：
     \[
     D_c = 2 R_c = \frac{Q_c}{\pi \varepsilon_0 L E_b} = \frac{2.5}{\pi \times 8.85\times 10^{-12}\times 6.0\times 10^3 \times 3.0\times 10^6} \approx 5.0\text{ m}.
     \]
   - 在通道内部（中心细路径外 \(r_{\text{core}} < r \le R_c\)），场强大小恒定等于击穿场强（且指向径向内侧 \(\mathbf{E} = -E_b \hat{r}\)，因带负电）。对半径 \(r\)、长 \(L\) 的同轴圆柱高斯面应用高斯定理（中心细路径带电量忽略）：
     \[
     -E_b \cdot 2\pi r L = \frac{1}{\varepsilon_0}\int_0^r \rho(r')\,2\pi r' L\,\mathrm{d}r' \implies \int_0^r r'\rho(r')\,\mathrm{d}r' = -\varepsilon_0 E_b r.
     \]
     两边对 \(r\) 求导得电荷密度径向分布（带负号表示负电荷）：
     \[
     \rho(r) = -\frac{\varepsilon_0 E_b}{r} \qquad (r_{\text{core}} < r \le R_c).
     \]
     （验证：\(\int_0^{R_c} \rho(r) 2\pi r L\,\mathrm{d}r = -2\pi\varepsilon_0 E_b L R_c = -Q_c\)，完全自洽。）

4. **电离层底部光环产生与扩展示意图及 \(r = 100\text{ km}\) 时的径向扩张速度**
   - 物理过程：通道底部波源发出无线电波以光速 \(c\) 球面传播；因 \(30\text{ kHz} \ll 20\text{ MHz}\)（电离层截止频率），电磁波不能深入电离层，而是在 \(H = 80\text{ km}\) 的电离层底面激发等离子体瞬间发光。球面波前 \(R = ct\) 与水平平面 \(z = H\) 的交线即是以正上方为圆心的光环，半径满足：
     \[
     r(t) = \sqrt{c^2 t^2 - H^2} \quad \left(t \ge \frac{H}{c}\right).
     \]
   - 对时间 \(t\) 求导（或利用斜交投影几何 \(v = c/\cos\theta\)），得光环扩张径向速度：
     \[
     v_r = \frac{\mathrm{d}r}{\mathrm{d}t} = \frac{c^2 t}{\sqrt{c^2 t^2 - H^2}} = c\frac{\sqrt{r^2 + H^2}}{r} = c\sqrt{1 + \left(\frac{H}{r}\right)^2}.
     \]
   - 代入 \(H = 80\text{ km}\)、\(r = 100\text{ km}\)：
     \[
     v_r = c\sqrt{1 + 0.8^2} = c\sqrt{1.64} \approx 1.281 c \approx 3.84\times 10^8\text{ m/s}.
     \]
     （物理意义说明：此速度超过光速 \(c\)，但它属于球面波前扫过静止平面的几何交点“剪刀效应”相速度，并不传递超光速的横向物理信号，不违背狭义相对论。）

5. **高空 \(12\text{ km}\) 悬浮氦气球的体积 \(V\)**
   - 设温度递减率 \(\alpha = 5.0\times 10^{-3}\text{ K/m}\)，\(T(z) = T_0 - \alpha z\)，在 \(z = 12\text{ km}\) 处 \(T_1 = 290 - 5.0\times 12 = 230\text{ K}\)。
   - 由流体静力学平衡 \(\mathrm{d}p = -\rho_{\text{空气}} g\,\mathrm{d}z = -\frac{p M}{R T(z)} g\,\mathrm{d}z\) 分离变量积分：
     \[
     \int_{p_0}^{p_1} \frac{\mathrm{d}p}{p} = -\frac{M g}{R}\int_0^z \frac{\mathrm{d}z'}{T_0 - \alpha z'} \implies p_1 = p_0\left(\frac{T_1}{T_0}\right)^{\frac{M g}{\alpha R}},
     \]
     指数 \(\frac{M g}{\alpha R} = \frac{0.029 \times 9.8}{0.005 \times 8.31} \approx 6.8400\)。
   - 该高度处空气密度：
     \[
     \rho_1 = \frac{p_1 M}{R T_1} = \frac{p_0 M}{R T_0}\left(\frac{T_1}{T_0}\right)^{\frac{Mg}{\alpha R} - 1} = 1.2173\times\left(\frac{230}{290}\right)^{5.8400} \approx 0.3139\text{ kg/m}^3.
     \]
   - 悬浮力平衡 \(\rho_1 V g = (m_{\text{载}} + \rho_{\text{He}} V) g\)：
     \[
     V = \frac{m_{\text{载}}}{\rho_1 - \rho_{\text{He}}} = \frac{50}{0.3139 - 0.18}\text{ m}^3 \approx 373\text{ m}^3 \quad (\text{或按 } \rho_1 \approx 0.31\text{ kg/m}^3 \text{ 算为 } 385\text{ m}^3).
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：
  - 盲解与官方参考解答（`page-23.jpg`–`page-27.jpg`）全面吻合！官方第（2）问同样同时列出了点电荷粗算（\(3.5\text{ kV/m}\)）与均匀圆盘积分法（\(2.8\text{ kV/m}\)）；第（4）问给出了微元法 \(v = c/\cos\theta\) 与解析求导法 \(\mathrm{d}r/\mathrm{d}t\) 两种途径；第（5）问在将 \(\rho_1\) 中间修约为 \(0.31\text{ kg/m}^3\) 后得出 \(V_0 = 3.8\times 10^2\text{ m}^3\)（不修约为 \(3.73\times 10^2\text{ m}^3\)）。
  - 细微符号注记：第（3）问官方写 \(\rho(r) = \varepsilon_0 E_{\text{击穿}} r^{-1}\)，实际上因通道带负电荷，严格电荷体密度应带负号 \(\rho(r) = -\frac{\varepsilon_0 E_b}{r}\)（若只谈电荷密度大小则与官方一致）。
- **核心难点与典型易错点**：
  - 难点1：第（2）问当圆盘半径 \(r_0 = 2.5\text{ km}\) 与离地高度 \(6.0\text{ km}\) 处于同一量级时，点电荷近似会带来约 \(24\%\) 的偏高误差，采用精确圆盘公式结合镜像法（总场强直接由题给 \(E_0 = \sigma/\varepsilon_0\) 表达）既省算力又精确。
  - 难点2：第（3）问由“已知内部电场恒定反推电荷分布”的逆向高斯定理应用，须在柱对称高斯积分后对 \(r\) 求导（而非误以为电荷均匀分布）。
  - 易错点1：第（2）问使用镜像法时忘记地面是导体、镜像电荷产生等大垂直贡献，漏掉因子 \(2\)。
  - 易错点2：第（5）问错误套用等温气压公式 \(p = p_0 e^{-Mgz/(RT_0)}\) 代替线性变温大气积分，或忘记计算空气密度时分母用的温度是 \(T_1 = 230\text{ K}\) 而非 \(T_0 = 290\text{ K}\)。
- **教练总结与迁移建议**：本题把大气电学（雷暴云、电晕通道）、电离层光学（超光速相速度剪刀效应）与线性变温大气静力学有机串联，非常考验在真实物理情景中**抓主干近似、核查量级合理性**的综合能力。

---

# 决赛理论试题（Final Theory）

## 8. 第36届决赛理论第1题 · 缺损辐条车轮在地面纯滚动的角加速度与接触力 (`cpho-2019-final-theory-problem-slice-q1`)

- **难度评级**：`D3`
- **物理模型**：非对称质心刚体平面纯滚动动力学与瞬时转动中心微扰求导
- **教学标签**：`非对称刚体纯滚动`、`瞬时转动中心`、`能量守恒求导法`、`复杂分数精确运算`、`质心加速度分解`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **几何与惯量基础参数**
   轮盘内半径 \(R_1 = \frac{4}{5}R_0\)，外半径 \(R_0\)，质量 \(M = 8m\)；两根均匀辐条各长 \(R_1\)，质量各为 \(m\)，夹角 \(120^\circ\)，总质量 \(M_{\text{总}} = 8m + 2m = 10m\)。
   - 轮子绕中心轴 \(O\) 的转动惯量：
     \[
     I_{\text{盘}} = \frac{1}{2}M(R_0^2 + R_1^2) = 4m\left(1 + \frac{16}{25}\right)R_0^2 = \frac{164}{25}mR_0^2,
     \]
     \[
     I_{\text{辐}} = 2\cdot\frac{1}{3}mR_1^2 = \frac{2}{3}m\cdot\frac{16}{25}R_0^2 = \frac{32}{75}mR_0^2,
     \]
     \[
     I_O = \frac{492 + 32}{75}mR_0^2 = \frac{524}{75}mR_0^2.
     \]
   - 总质心 \(C\) 的位置：两辐条夹角 \(120^\circ\)，各自质心距 \(O\) 为 \(\frac{R_1}{2} = \frac{2}{5}R_0\)，向角平分线投影得辐条整体质心距 \(O\) 为 \(\frac{2}{5}R_0\cos 60^\circ = \frac{1}{5}R_0\)。故总质心 \(C\) 位于角平分线上、距 \(O\) 的距离为：
     \[
     d = OC = \frac{2m\cdot \frac{1}{5}R_0}{10m} = \frac{1}{25}R_0.
     \]
   - 轮子绕总质心 \(C\) 的转动惯量（由平行轴定理）：
     \[
     I_C = I_O - M_{\text{总}} d^2 = \left(\frac{524}{75} - \frac{10}{625}\right)mR_0^2 = \frac{2614}{375}mR_0^2.
     \]

2. **瞬时转轴能量法导出任意角位置 \(\theta\) 的 \(\omega(\theta)\) 与 \(\alpha(\theta)\)**
   设轮子向左侧纯滚动（逆时针转动 \(\theta\) 角，\(\theta = 0\) 时 \(OC\) 水平向左）。在任意转角 \(\theta\) 处，由余弦定理得质心 \(C\) 到地面接触点（瞬时速度中心 \(P\)）的距离平方：
   \[
   PC^2 = R_0^2 + d^2 - 2R_0 d\cos\left(\frac{\pi}{2} - \theta\right) = R_0^2 + d^2 - 2R_0 d\sin\theta.
   \]
   故绕瞬时转动中心 \(P\) 的瞬时转动惯量为：
   \[
   I_P(\theta) = I_C + M_{\text{总}} PC^2 = I_O + M_{\text{总}} R_0^2 - 2 M_{\text{总}} R_0 d\sin\theta.
   \]
   其中 \(I_O + M_{\text{总}} R_0^2 = \left(\frac{524}{75} + 10\right)mR_0^2 = \frac{1274}{75}mR_0^2\)，\(M_{\text{总}} d = \frac{2}{5}mR_0\)。
   - **第（1）问：刚释放时（\(\theta = 0, \omega = 0\)）**：
     瞬时接触点 \(P\) 无向心加速度（\(\omega^2 R_0 = 0\)），可直接对 \(P\) 列能量守恒再求导或直接列转动定理：
     \[
     I_P(0)\alpha_1 = M_{\text{总}} g d \implies \alpha_1 = \frac{\frac{2}{5}m g R_0}{\frac{1274}{75}mR_0^2} = \frac{30}{1274}\frac{g}{R_0} = \frac{15}{637}\frac{g}{R_0} \quad (\text{逆时针}).
     \]
   - **第（2）问：辐条 \(OB\) 首次转到竖直位置（\(\theta = 30^\circ\)）**：
     初始时 \(OB\) 在水平向左下方 \(60^\circ\)（即距竖直向下偏左 \(30^\circ\)），故轮子逆时针滚过 \(\theta = 30^\circ\) 时 \(OB\) 首次竖直向下（\(\sin\theta = \frac{1}{2}, \cos\theta = \frac{\sqrt{3}}{2}\)）。
     - 此时 \(I_P(30^\circ) = \left(\frac{1274}{75} - \frac{2}{5}\right)mR_0^2 = \frac{1244}{75}mR_0^2\)。
     - 由机械能守恒 \(\frac{1}{2}I_P(\theta)\omega^2 = M_{\text{总}} g d\sin\theta\) 得：
       \[
       \omega^2 = \frac{2\cdot\frac{2}{5}m g R_0 \cdot \frac{1}{2}}{\frac{1244}{75}mR_0^2} = \frac{30}{1244}\frac{g}{R_0} = \frac{15}{622}\frac{g}{R_0}.
       \]
     - 将机械能守恒式对时间 \(t\) 求导并消去 \(\omega\)：
       \[
       I_P(\theta)\alpha - M_{\text{总}} R_0 d\cos\theta\,\omega^2 = M_{\text{总}} g d\cos\theta \implies \alpha = \frac{M_{\text{总}} d\cos\theta\,(g + R_0\omega^2)}{I_P(\theta)}.
       \]
       代入 \(\theta = 30^\circ\) 与 \(\omega^2 = \frac{15}{622}\frac{g}{R_0}\)：
       \[
       \alpha = \frac{\frac{2}{5}mR_0\cdot\frac{\sqrt{3}}{2}\cdot\frac{637}{622}g}{\frac{1244}{75}mR_0^2} = \frac{15\times 637\sqrt{3}}{622\times 1244}\frac{g}{R_0} = \frac{9555\sqrt{3}}{773768}\frac{g}{R_0} \quad (\text{逆时针}).
       \]
     - 求地面对轮子的摩擦力 \(f\)（取向右为 \(+x\)）与支持力 \(N\)（向上为 \(+y\)）：
       写出质心坐标 \(x_C = -R_0\theta - d\cos\theta\)，\(y_C = R_0 - d\sin\theta\)，二次求导得质心加速度：
       \[
       a_{Cx} = (-R_0 + d\sin\theta)\alpha + d\cos\theta\,\omega^2, \qquad a_{Cy} = -d\cos\theta\,\alpha + d\sin\theta\,\omega^2.
       \]
       代入 \(M_{\text{总}} = 10m\)、\(d = \frac{1}{25}R_0\)、\(\sin 30^\circ = \frac{1}{2}\)、\(\cos 30^\circ = \frac{\sqrt{3}}{2}\)：
       \[
       f = M_{\text{总}} a_{Cx} = -\frac{89907\sqrt{3}}{773768}mg \quad (\text{负号表示水平向左}),
       \]
       \[
       N = M_{\text{总}}(g + a_{Cy}) = \frac{7735679}{773768}mg \quad (\text{竖直向上}).
       \]
       （交叉验证：用质心转动定理 \(I_C\alpha = N d\cos\theta + f(R_0 - d\sin\theta)\) 代入检验，两边分数均精确等于 \(\frac{832559\sqrt{3}}{9672100}mgR_0\)，零误差！）

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解的所有过程与最终庞大分数的分子分母（\(\frac{15}{637}\frac{g}{R_0}\)、\(\frac{9555\sqrt{3}}{773768}\frac{g}{R_0}\)、\(\frac{89907\sqrt{3}}{773768}mg\)、\(\frac{7735679}{773768}mg\)）与官方参考解答（`page-1.jpg`–`page-3.jpg`）**一字不差地精确一致**！官方最后同样利用质心转动定理 \(J_C\alpha = F_N x_C\cos\theta - F_f(R_0 - x_C\sin\theta)\) 作为独立核验手段。
- **官方排版笔误记录**：
  - `page-1.jpg` 式(2) 分子打印有误，把计算质心坐标写成了 `((M'+m)*0 + (-m)*(-R_1/2))/M'`（实为仅两辐条各自贡献合成出 \(m R_1 / (2M')\)）；
  - `page-2.jpg` 式(4) 漏印 `M'` 的撇号成了 `M`，另“加速度 \(a_P\)”误印成希腊字母 \(\alpha_P\)。
- **核心难点与典型易错点**：
  - 难点1：识别纯滚动瞬时转动中心 \(P\) 并非惯性系定点，当 \(\omega \ne 0\) 时 \(P\) 点有竖直向上的向心加速度 \(a_P = \omega^2 R_0\)，不可直接套用 \(\tau_P = I_P \alpha\)（必须改用“对机械能守恒式关于 \(t\) 求导”，或者在 \(P\) 系中添加向心惯性力 \(-M_{\text{总}}\omega^2 R_0\hat{j}\) 的力矩，正好对应 \(+M_{\text{总}} R_0 d\cos\theta\,\omega^2\) 项！）。
  - 易错点1：把两辐条质心合距离算成 \(\frac{1}{2}R_1\)（忘记因夹角 \(120^\circ\) 要乘 \(\cos 60^\circ = \frac{1}{2}\)）。
  - 易错点2：直接将静止释放时 \(\theta = 0\) 成立的 \(\tau_P = I_P \alpha\) 照搬到第（2）问 \(\theta = 30^\circ\) 处，漏掉了非惯性修正项 \(M_{\text{总}} R_0 d\cos\theta\,\omega^2\)（算丢约 \(2.4\%\)，分数大错）。
- **教练总结与迁移建议**：在刚体平面纯滚动动力学中，“写清 \(I_P(\theta)\) 后对机械能守恒求全导数求 \(\alpha(\theta)\)，再通过质心坐标二阶导数反推支反力 \(N, f\)，最后用 \(I_C\alpha = \tau_C\) 做逆向校验”是一套几乎百战百胜、完全避开瞬时轴非惯性系陷阱的黄金流程。

---

## 9. 第36届决赛理论第2题 · 双层耗损电介质半圆柱壳稳态场、界面电荷与双指数弛豫 (`cpho-2019-final-theory-problem-slice-q2`)

- **难度评级**：`D3`
- **物理模型**：漏电介质稳恒电流-静电场耦合模型与双 \(RC\) 串联似稳弛豫回路
- **教学标签**：`耗损电介质`、`电流连续性边界条件`、`界面总电荷与自由电荷`、`柱壳电容与电阻`、`似稳双指数衰减`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **介质内电场强度与电势分布**
   忽略边缘效应，电场线沿角向圆弧分布。设左、右两金属膜（\(\varphi = 0\) 与 \(\varphi = \pi\)）电势分别为 \(V(0) = V_0\) 与 \(V(\pi) = 0\)（方向沿 \(+\hat{\varphi}\)）。
   - 在稳恒状态下，半径 \(r\) 处各介质内电流连续 \(\nabla\cdot\mathbf{J} = 0\)，即两区域角向场强 \(E_1(r), E_2(r)\) 各自不随 \(\varphi\) 变化，且沿任意半圆弧长积分电压之和为 \(V_0\)：
     \[
     \sigma_1 E_1(r) = \sigma_2 E_2(r), \qquad E_1(r) r\theta_0 + E_2(r) r(\pi - \theta_0) = V_0.
     \]
   - 解得电场强度大小（沿 \(+\hat{\varphi}\) 方向）：
     \[
     E_1(r) = \frac{\sigma_2 V_0}{\left[\sigma_2 \theta_0 + \sigma_1(\pi - \theta_0)\right]r}, \qquad E_2(r) = \frac{\sigma_1 V_0}{\left[\sigma_2 \theta_0 + \sigma_1(\pi - \theta_0)\right]r}.
     \]
   - 电势分布 \(V(\varphi)\)（仅依赖 \(\varphi\)）：
     \[
     V(\varphi) = \begin{cases}
     V_0\left[1 - \dfrac{\sigma_2\varphi}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)}\right], & 0 \le \varphi < \theta_0, \\
     V_0\dfrac{\sigma_1(\pi - \varphi)}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)}, & \theta_0 < \varphi \le \pi.
     \end{cases}
     \]

2. **\(\varphi = \theta_0\) 界面处的电荷**
   （注意区分“自由电荷”与“含极化束缚电荷在内的净总电荷”！）
   - **界面净总电荷 \(Q_{\text{净}}\)（自由+束缚电荷，由 \(\mathbf{E}\) 的高斯定理 \(\sigma_{\text{净}} = \varepsilon_0(E_2 - E_1)\) 积分）**：
     \[
     Q_{\text{净}} = \int_a^b \varepsilon_0\left[E_2(r) - E_1(r)\right] l\,\mathrm{d}r = \frac{\varepsilon_0(\sigma_1 - \sigma_2) l \ln(b/a)}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)} V_0.
     \]
   - **界面自由电荷 \(Q_f\)（由 \(\mathbf{D}\) 的高斯定理 \(\sigma_f = \varepsilon_0(\varepsilon_{r2}E_2 - \varepsilon_{r1}E_1)\) 积分，对应等效电路中间节点自由电量）**：
     \[
     Q_f = \int_a^b \varepsilon_0\left[\varepsilon_{r2}E_2(r) - \varepsilon_{r1}E_1(r)\right] l\,\mathrm{d}r = \frac{\varepsilon_0(\varepsilon_{r2}\sigma_1 - \varepsilon_{r1}\sigma_2) l \ln(b/a)}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)} V_0.
     \]
   （若端电压反向即 \(V(0)=0, V(\pi)=V_0\)，则上述电荷与场强均取相反号。）

3. **两介质区域的电阻和电容**
   将半圆柱壳沿径向剖分成无数并联的薄同轴圆弧壳（半径 \(r\)、厚度 \(\mathrm{d}r\)、轴长 \(l\)、弧张角 \(\Delta\varphi\)）。各壳层间等势面重合，彼此并联：
   - 电阻：\(\mathrm{d}G = \sigma\frac{l\,\mathrm{d}r}{r\,\Delta\varphi} \implies G = \frac{\sigma l}{\Delta\varphi}\ln\frac{b}{a}\)，故：
     \[
     R_1 = \frac{\theta_0}{\sigma_1 l \ln(b/a)}, \qquad R_2 = \frac{\pi - \theta_0}{\sigma_2 l \ln(b/a)}.
     \]
   - 电容：\(\mathrm{d}C = \varepsilon_0\varepsilon_r\frac{l\,\mathrm{d}r}{r\,\Delta\varphi} \implies C = \frac{\varepsilon_0\varepsilon_r l}{\Delta\varphi}\ln\frac{b}{a}\)，故：
     \[
     C_1 = \frac{\varepsilon_0\varepsilon_{r1} l \ln(b/a)}{\theta_0}, \qquad C_2 = \frac{\varepsilon_0\varepsilon_{r2} l \ln(b/a)}{\pi - \theta_0}.
     \]
   （几何无关恒等式校验：\(R_1 C_1 = \frac{\varepsilon_0\varepsilon_{r1}}{\sigma_1}\)，\(R_2 C_2 = \frac{\varepsilon_0\varepsilon_{r2}}{\sigma_2}\)。）

4. **\(t = 0\) 断开电源后的等效电路及端电压 \(V(t)\)**
   - 等效电路为 \((R_1 \parallel C_1)\) 与 \((R_2 \parallel C_2)\) 串联。
   - 当 \(t = 0\) 断开外部电源后，外部断路电流为零，两个并联 \(RC\) 支路之间无外部净电流交换，因此两回路各自独立通过内部漏电阻放电！由全电流连续性 \(C_i \frac{\mathrm{d}V_i}{\mathrm{d}t} + \frac{V_i}{R_i} = 0\)（\(i=1,2\)），时间常数分别为：
     \[
     \tau_1 = R_1 C_1 = \frac{\varepsilon_0\varepsilon_{r1}}{\sigma_1}, \qquad \tau_2 = R_2 C_2 = \frac{\varepsilon_0\varepsilon_{r2}}{\sigma_2}.
     \]
   - 断开瞬间电容电压不能突变，初值由稳恒分压给出：
     \[
     V_1(0) = \frac{\sigma_2\theta_0}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)}V_0, \qquad V_2(0) = \frac{\sigma_1(\pi - \theta_0)}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)}V_0.
     \]
   - 故两金属膜间电压随时间呈**双指数衰减**：
     \[
     V(t) = V_1(t) + V_2(t) = V_0\frac{\sigma_2\theta_0\, e^{-\frac{\sigma_1}{\varepsilon_0\varepsilon_{r1}}t} + \sigma_1(\pi - \theta_0)\, e^{-\frac{\sigma_2}{\varepsilon_0\varepsilon_{r2}}t}}{\sigma_2\theta_0 + \sigma_1(\pi - \theta_0)} \quad (t \ge 0).
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（3）、（4）问的全部解析式和物理逻辑与官方参考解答（`page-4.jpg`–`page-6.jpg`）完全一致！
- **第（2）问“总电荷”定义辨析与官方笔误记录**：
  - 在第（2）问中，官方参考解答（`page-4.jpg`–`page-5.jpg` 式(7)-(8)）使用 \(\sigma_e = \varepsilon_0(E_2 - E_1)\) 计算的是**包含束缚极化电荷在内的净总电荷** \(Q_{\text{净}} = \frac{\varepsilon_0(\sigma_1/\sigma_2 - 1)l\ln(b/a)}{\theta_0 + \frac{\sigma_1}{\sigma_2}(\pi - \theta_0)}V_0\)。需提醒竞赛生：若题目指“界面累积自由电荷”（即漏电界面上 \(D_{2n} - D_{1n}\) 形成的自由面电荷，也是第(4)问等效电路节点电量 \(Q_2 - Q_1\)），则应带入 \(\varepsilon_{r1}, \varepsilon_{r2}\)；在考场上遇到“总电荷”一词时，先明确写出自由电荷、束缚电荷与净总电荷三者关系再给出答案最为稳妥。
  - 官方细微笔误：`page-5.jpg` 式(17)分母印成了 `1/G`（应为 `1/G_1`），`page-6.jpg` 式(20)-(24) 把 \(\varepsilon_{r1}\) 简写/误印成了 \(\varepsilon_1\)（但随后恢复正常）。
- **核心难点与典型易错点**：
  - 难点1：断开外电源后，识别串联的两个 \(R_i \parallel C_i\) 支路因为外电路开路而**完全退耦**（不能把它们合成一个总电阻和一个总电容去做单指数衰减！只有当 \(\frac{\varepsilon_{r1}}{\sigma_1} = \frac{\varepsilon_{r2}}{\sigma_2}\) 时才退化为单指数；一般情形下随时间流逝界面自由电荷还会自我重排甚至变号！）。
  - 易错点1：稳恒态确定边界条件时误用纯静电极化条件 \(D_1 = D_2\) 而非稳恒电流连续性 \(J_1 = J_2\)（即 \(\sigma_1 E_1 = \sigma_2 E_2\)）。
  - 易错点2：计算半圆柱体电容或电阻时，把沿角向串联的薄壳误当成沿径向串联而错积分 \(\int r\,\mathrm{d}r\)。
- **教练总结与迁移建议**：耗损电介质（leaky dielectric）的标准解题三步曲是：① 稳恒直流看 \(\sigma\)（\(J_n\) 连续定出电场和分压）；② 瞬态初始瞬间看 \(\varepsilon\)（电容电压不突变）；③ 似稳演化阶段画出 \(R_i \parallel C_i\) 等效网络列节点电流方程。理解为什么两支路外接断开后变成各自放电，能彻底打通电磁学场论与电路似稳理论的壁垒。

---

## 10. 第36届决赛理论第3题 · 超导重力仪磁悬浮原理、地下湖引力微扰与电容交流电桥 (`cpho-2019-final-theory-problem-slice-q3`)

- **难度评级**：`D3`
- **物理模型**：球体空穴引力叠加模型、准亥姆霍兹线圈超导磁通守恒悬浮模型及双电容交流反馈微平衡
- **教学标签**：`超导磁悬浮`、`磁通量守恒`、`非均匀磁场安培力`、`双电容静电反馈`、`地球重力异常`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **球形地下湖引起的正上方地表重力加速度微小变化 \(\Delta g\)**
   由均匀地球表面重力加速度 \(g_0 = \frac{4}{3}\pi G \rho_E R_E\)，得地球平均密度：
   \[
   \rho_E = \frac{3 g_0}{4\pi G R_E} = \frac{3\times 9.80}{4\pi\times 6.67\times 10^{-11}\times 6.37\times 10^6} \approx 5.506\times 10^3\text{ kg/m}^3.
   \]
   将地下湖视作在均匀地球上叠加一个密度为 \(\Delta\rho = \rho_w - \rho_E\)、半径 \(r_L = 10\text{ km}\)、球心深度 \(h = 15\text{ km}\) 的均匀球体。由牛顿壳层定理，正上方地表处的重力加速度变化（减小量）大小为：
   \[
   \Delta g = \frac{4\pi G r_L^3 (\rho_E - \rho_w)}{3 h^2} = \frac{4\pi\times 6.67\times 10^{-11}\times (10^4)^3\times (5506.5 - 1000)}{3\times (1.5\times 10^4)^2} \approx 5.60\times 10^{-3}\text{ m/s}^2.
   \]

2. **准亥姆霍兹超导重力仪的磁场参数、感应电流与重力加速度**
   - **i) \(B_0\) 和 \(\beta\) 的表达式**：
     下线圈（\(z = 0\)，\(N\) 匝）与上线圈（\(z = R\)，\(\alpha N\) 匝）均通电流 \(i_0\)、半径均为 \(R\)。轴线上 \(z\) 处总磁场：
     \[
     B_z(z) = \frac{\mu_0 N i_0 R^2}{2}\left[\frac{1}{(z^2 + R^2)^{3/2}} + \frac{\alpha}{\left[(z - R)^2 + R^2\right]^{3/2}}\right].
     \]
     在 \(z = R\) 处，\(B_0 = B_z(R)\)：
     \[
     B_0 = \frac{\mu_0 N i_0}{2R}\left(\alpha + \frac{1}{2\sqrt{2}}\right) = \frac{\sqrt{2}\mu_0 N i_0}{8R}(2\sqrt{2}\alpha + 1).
     \]
     在 \(z = R\) 处对 \(z\) 求导（上线圈在此对称中心处导数为零）：
     \[
     \left.\frac{\mathrm{d}B_z}{\mathrm{d}z}\right|_{z=R} = \frac{\mu_0 N i_0 R^2}{2}\cdot\left(-\frac{3R}{(2R^2)^{5/2}}\right) = -\frac{3\mu_0 N i_0}{8\sqrt{2}R^2} = -B_0\beta,
     \]
     故径向梯度系数：
     \[
     \beta = \frac{3}{2R(2\sqrt{2}\alpha + 1)}.
     \]
   - **ii) 超导细环平衡处感应电流 \(I_0\)**：
     由于超导细环电阻为零，全过程中总磁通量守恒；初始（\(i = 0, I = 0\)）磁通 \(\Phi = 0\)。在 \(z = R\) 平衡位置，因 \(D \ll 2R\)，外磁场穿过环面的磁通约为 \(B_0\cdot\frac{\pi D^2}{4}\)。由 \(\Phi_{\text{总}} = B_0\frac{\pi D^2}{4} + L I_0 = 0\) 得：
     \[
     I_0 = -\frac{\pi D^2 B_0}{4 L} = -\frac{\pi D^2 \mu_0 N i_0}{8 R L}\left(\alpha + \frac{1}{2\sqrt{2}}\right) \quad (\text{负号表示与 } i_0 \text{ 反向}).
     \]
   - **iii) 重力加速度 \(g_0\) 的表达式**：
     在 \(z = R\) 处，环周上径向磁场 \(B_r = \frac{1}{2}\beta B_0 \left(\frac{D}{2}\right) = \frac{1}{4}\beta B_0 D\)（向外）。反向电流 \(|I_0|\) 在 \(B_r\) 中受向上的安培力 \(F_z = |I_0| B_r \cdot \pi D\)，平衡重力 \(m g_0\)：
     \[
     m g_0 = \frac{\pi D^2 B_0}{4 L}\cdot \frac{\beta B_0 D}{4}\cdot \pi D = \frac{\pi^2 D^4 \beta B_0^2}{16 L},
     \]
     代入 \(B_0\) 与 \(\beta\) 得：
     \[
     g_0 = \frac{3\pi^2 D^4 \mu_0^2 N^2 i_0^2}{1024 m L R^3}(2\sqrt{2}\alpha + 1) = \frac{3\pi^2 D^4 \mu_0^2 N^2 i_0^2}{256\sqrt{2} m L R^3}\left(\alpha + \frac{1}{2\sqrt{2}}\right).
     \]
     （用虚功原理对 \(U = \frac{\Phi_{\text{ext}}^2}{2L}\) 求负导数 \(F_z = -\frac{\mathrm{d}U}{\mathrm{d}z}\) 所得公式完全相同！）

3. **交流电桥平衡测微重力变化 \(\Delta g\) 与 \(\Delta V\) 的关系**
   由于电桥两侧电感 \(L_0\) 和电容 \(C_0\) 完全对称，电桥重新平衡意味着 \(C_1 = C_2\)，即超导“平板”必须被静电力拉回**精确的原平衡位置 \(z = R\)**（上下两极板间距均为 \(x = d/2\)）。
   - 因为超导平板回到 \(z = R\) 位置，磁悬浮力保持 \(F_{\text{磁}}(R) = mg\) 不变。
   - 原本 \(V_1 = V_2 = V_C\) 时上下静电吸引力相消；调整为 \(V_1 = V_C + \Delta V\)、\(V_2 = V_C - \Delta V\) 后，电容平行板吸引力 \(F_e = \frac{\varepsilon_0 A V^2}{2(d/2)^2} = \frac{2\varepsilon_0 A V^2}{d^2}\)，故净向上的静电力为：
     \[
     \Delta F_e = \frac{2\varepsilon_0 A}{d^2}\left[(V_C + \Delta V)^2 - (V_C - \Delta V)^2\right] = \frac{8\varepsilon_0 A V_C}{d^2}\Delta V.
     \]
   - 平衡新增重力 \(m\Delta g = \Delta F_e\)，得精确线性关系：
     \[
     \Delta g = \frac{8\varepsilon_0 A V_C}{m d^2}\Delta V.
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（2）、（3）问全部推导和最终代数/数值表达式与官方参考解答（`page-8.jpg`–`page-10.jpg`）**100% 精确一致**！
- **官方排版小瑕疵**：`page-9.jpg` 中第（2）ii) 问之前多处引用了错位的公式编号（如“由(17)式得”实指式(10)(14)，“由题给条件和(19)(20)式得”实指式(10)(11)(15)），不影响实际代数结果。
- **核心难点与典型易错点**：
  - 难点1：抓住第（3）问“电桥零点反馈”的核心——电桥再平衡意味着电容间隙恢复对称（\(x = d/2\)），从而磁场力保持原值 \(mg\)，使 \(\Delta g\) 与 \(\Delta V\) 严格成正比，且平方项 \((\Delta V)^2\) 精确抵消！
  - 易错点1：计算平行板电容器吸引力时错用 \(F = Q E = \frac{\varepsilon_0 A V^2}{x^2}\)（忘记电容器极板所处平均场强只有 \(\frac{1}{2}E\) 而多出因子 \(2\)），以及把半间距 \(x = d/2\) 错当成 \(d\)（结果整体差 4 倍或 8 倍）。
  - 易错点2：求导 \(B_z(z)\) 在 \(z = R\) 的梯度时对 \((R + (z-R)^2)^{-3/2}\) 误用一阶展开，其实上线圈在 \(z = R\) 处一阶导数为零。
- **教练总结与迁移建议**：本题把真实的地球物理前端仪器——超导重力仪（Superconducting Gravimeter）分解为引力异常、超导抗磁悬浮、差分电容电桥闭环反馈三大物理模块，展示了物理测量中“力平衡回零（Null-balance）消除非线性漂移”的经典思想。

---

## 11. 第36届决赛理论第4题 · 汽车涡轮增压与中冷器热力学过程 (`cpho-2019-final-theory-problem-slice-q4`)

- **难度评级**：`D2`
- **物理模型**：理想气体准静态绝热压缩、等压冷却及开口/闭口等效气团做功与熵变模型
- **教学标签**：`绝热压缩`、`等压过程熵变`、`涡轮增压与中冷器`、`功与热量辨析`、`气体状态方程`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **经过涡轮增压器与中间冷却器后气缸内空气质量 \(m_1\) 及功率倍数**
   - 进气终态压强 \(p_1 = 1.45\times 10^5\text{ Pa}\)，温度恢复至 \(T_0 = 15^\circ\text{C} = 288.15\text{ K}\)（或 \(288\text{ K}\)），气缸容积 \(V_0 = 4.00\times 10^{-4}\text{ m}^3\)。
   - 气缸内空气质量：
     \[
     m_1 = \frac{p_1 V_0 M}{R T_0} = \frac{1.45\times 10^5 \times 4.00\times 10^{-4} \times 29.0\times 10^{-3}}{8.31 \times 288.15} \approx 0.7024\text{ g} \quad (\text{取 } 288\text{ K 为 } 0.7028\text{ g}).
     \]
   - 未经增压和冷却时气缸质量 \(m_0 = \frac{p_0 V_0 M}{R T_0} \approx 0.4893\text{ g}\)。因功率与进入空气质量成正比，输出功率增加到原来的倍数为：
     \[
     \frac{P_1}{P_0} = \frac{m_1}{m_0} = \frac{p_1}{p_0} = \frac{1.45}{1.01} \approx 1.44 \quad (\text{精准值 } 1.436).
     \]

2. **无中间冷却器时的空气质量 \(m_2\) 及功率倍数**
   - 仅经涡轮增压器绝热压缩（\(\gamma = 7/5\)）后，温度升至：
     \[
     T_1 = T_0 \left(\frac{p_1}{p_0}\right)^{\frac{\gamma - 1}{\gamma}} = 288.15\times\left(\frac{1.45}{1.01}\right)^{2/7} \approx 319.5\text{ K}.
     \]
   - 由绝热密度比 \(\rho_1 / \rho_0 = (p_1 / p_0)^{1/\gamma}\)，充满容积 \(V_0\) 的空气质量为：
     \[
     m_2 = m_0 \left(\frac{p_1}{p_0}\right)^{5/7} = 0.4893\times\left(\frac{1.45}{1.01}\right)^{5/7} \approx 0.6335\text{ g}.
     \]
   - 输出功率增加到原来的倍数为：
     \[
     \frac{P_2}{P_0} = \left(\frac{p_1}{p_0}\right)^{5/7} \approx 1.295 \approx 1.30.
     \]

3. **外界对进入气缸的气团所做的功及两过程中的熵变**
   取第（1）问中最终充满气缸的固定气团（质量 \(m_1\)，摩尔数 \(n_1 = \frac{p_1 V_0}{R T_0} \approx 0.02422\text{ mol}\)）为研究对象，其经历两段过程：\((p_0, T_0) \xrightarrow{\text{绝热}} (p_1, T_1) \xrightarrow{\text{等压}} (p_1, T_0)\)。
   - **外界所做的功 \(W\)**：
     - 过程1（绝热压缩）：
       \[
       W_1 = \Delta U_1 = n_1 C_V (T_1 - T_0) = \frac{p_1 V_0}{\gamma - 1}\left[\left(\frac{p_1}{p_0}\right)^{\frac{\gamma - 1}{\gamma}} - 1\right] \approx 15.78\text{ J}.
       \]
     - 过程2（等压降温压缩，体积从 \(V_1 = V_0\frac{T_1}{T_0}\) 缩至 \(V_0\)）：
       \[
       W_2 = -p_1 (V_0 - V_1) = n_1 R (T_1 - T_0) = p_1 V_0\left[\left(\frac{p_1}{p_0}\right)^{\frac{\gamma - 1}{\gamma}} - 1\right] \approx 6.31\text{ J}.
       \]
     - 外界对气体所做的总功：
       \[
       W = W_1 + W_2 = \frac{\gamma}{\gamma - 1} p_1 V_0\left[\left(\frac{p_1}{p_0}\right)^{\frac{\gamma - 1}{\gamma}} - 1\right] = n_1 C_p (T_1 - T_0) \approx 22.1\text{ J}.
       \]
     （附注：在定常流动模型中，涡轮增压器轴功为 \(\Delta H_1 = n_1 C_p(T_1 - T_0)\)，中冷器轴功为零，且初末温度均为 \(T_0\) 故进出口流动功 \(p_0 V_i - p_1 V_0 = 0\)，两者数值完全等同！）
   - **两过程中的熵变**：
     - 过程1（准静态绝热）：\(\Delta S_1 = 0\)。
     - 过程2（等压冷却）：
       \[
       \Delta S_2 = n_1 C_p \ln\left(\frac{T_0}{T_1}\right) = -n_1 R \ln\left(\frac{p_1}{p_0}\right) = -\frac{p_1 V_0}{T_0}\ln\left(\frac{p_1}{p_0}\right) \approx -0.0728\text{ J/K}.
       \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）、（2）、（3）问的方法与数值结论（\(0.703\text{ g}\)、\(1.43\text{–}1.44\)、\(0.632\text{–}0.634\text{ g}\)、\(1.30\)、\(W = 22.1\text{ J}\)、\(\Delta S_1 = 0\)、\(\Delta S_2 = -0.0728\text{ J/K}\)）与官方参考解答（`page-11.jpg`–`page-13.jpg`）完全一致！官方第（3）问同样通过跟踪进入气缸的固定气团计算 \(W = W_1 + W_2\)，并在计算 \(\Delta S_2\) 时还展示了用“连接初末态的一条等温路径”直接得出 \(-n_1 R\ln(p_1/p_0)\) 的巧法。
- **官方细微数值不一致**：官方在 `page-11.jpg` 式(3) 取 \(T_0 = 288.15\text{ K}\) 算出 \(\rho_0 = 1.22\text{ kg/m}^3\)，导致第（1）、（2）问 \(m_1'/m_0\) 取整误差产生 \(1.43\)（精确为 \(1.44\)）；到第（3）问 `page-13.jpg` 式(17) 与 (19) 中又取 \(T_0 = 288.00\text{ K}\)，另 `page-12.jpg` 另一种解法中间过程出现了 `p_1^{(1-\gamma)/\gamma}` 误印成 `p_1^{1-\gamma}/\gamma` 的排版笔误。
- **核心难点与典型易错点**：
  - 易错点1：第（3）问忘记计入气体在中间冷却器**等压降温体积缩小**过程中外界对气体做的功 \(W_2 = n_1 R(T_1 - T_0) = 6.32\text{ J}\)，只算了绝热功 \(W_1 = 15.78\text{ J}\)。
  - 易错点2：第（2）问直接利用 \(m \propto p\) 计算，忘记了绝热压缩伴随升温导致密度仅按 \(p^{1/\gamma}\) 增长。
  - 易错点3：算 \(\Delta S_2\) 时误用定容比热容 \(C_V\) 代替定压比热容 \(C_p\)（少乘了 \(\gamma = 7/5\)）。
- **教练总结与迁移建议**：在绝热+等压组合题中，由于总功等于 \(\Delta H = n C_p \Delta T\) 且总熵变可直接取等温替代路径 \(\Delta S = -n R\ln(p_1/p_0)\)，利用这两条状态函数结论做秒杀验算，能够极好地防止过程量积分出错。

---

## 12. 第36届决赛理论第5题 · 诺奖光镊装置的光学聚焦、光力模型与热力学捕获概率 (`cpho-2019-final-theory-problem-slice-q5`)

- **难度评级**：`D3`
- **物理模型**：激光扩束艾里斑衍射极限、多层平行平板傍轴不变量聚焦、介质中光动量辐射压与麦克斯韦速率分布捕获阈值
- **教学标签**：`光镊原理`、`艾里斑与扩束`、`平面界面傍轴聚焦`、`介质中光子动量`、`麦克斯韦分布积分`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **不加扩束镜时空气中聚焦光斑直径 \(d_1\)**
   激光束截面直径 \(D_1 = 1.5\text{ mm}\) 经焦距 \(f = 4.0\text{ mm}\) 聚焦物镜聚焦，受圆孔衍射艾里斑第一暗环限制，光斑直径为：
   \[
   d_{o1} = 2\times 1.22\frac{\lambda f}{D_1} = \frac{2.44 \times 632.8\times 10^{-9} \times 4.0\times 10^{-3}}{1.5\times 10^{-3}}\text{ m} \approx 4.12\text{ }\mu\text{m}.
   \]

2. **伽利略扩束镜两透镜间距 \(L\) 及扩束后光束直径 \(D_2\)**
   凹透镜（\(f_1 = -6.3\text{ mm}\)）与凸透镜（\(f_2 = +25.2\text{ mm}\)）组成共焦扩束系统，平行光出射要求焦点重合：
   \[
   L = f_1 + f_2 = -6.3 + 25.2 = 18.9\text{ mm},
   \]
   扩束后直径按相似三角形放大：
   \[
   D_2 = \left|\frac{f_2}{f_1}\right| D_1 = \frac{25.2}{6.3}\times 1.5\text{ mm} = 6.0\text{ mm}.
   \]

3. **傍轴近似下水中聚焦光斑到玻璃内表面的距离 \(h\) 及水中光斑直径 \(d_{o2}\)**
   - **聚焦深度 \(h\)**：物镜在空气中本应聚焦在距离 \(f = 4.0\text{ mm}\) 处，即距玻璃外表面 \(f - a = 2.0\text{ mm}\)。光线先以虚像物距进入厚 \(d = 1.0\text{ mm}\)、折射率 \(n_g = 1.46\) 的底面玻璃，再进入 \(n_w = 1.33\) 的蒸馏水。跟踪傍轴边缘光线斜率（\(n_a\theta_a = n_g\theta_g = n_w\theta_w\)）：
     - 空气-玻璃外表面处高度 \(y_1 = (f - a)\theta_a\)；
     - 穿过厚度 \(d\) 玻璃后，内表面处高度 \(y_2 = y_1 - d\theta_g = \left(f - a - \frac{n_a}{n_g}d\right)\theta_a\)；
     - 射入水中后以角度 \(\theta_w = \frac{n_a}{n_w}\theta_a\) 会聚，故聚焦光斑到池底内表面的距离为：
       \[
       h = \frac{y_2}{\theta_w} = \frac{n_w}{n_a}\left(f - a - \frac{n_a}{n_g}d\right) = 1.33\times\left(4.0 - 2.0 - \frac{1.0}{1.46}\right)\text{ mm} \approx 1.75\text{ mm}.
       \]
   - **关键物理校验（水中光斑直径）**：
     在水中，激光波长缩短为 \(\lambda_w = \frac{\lambda}{n_w}\)，但与此同时由于平界面折射，会聚半角也缩小为 \(\theta_w = \frac{n_a}{n_w}\theta_a = \frac{D_2}{2 n_w f}\)（即数值孔径 \(\text{NA} = n_w \theta_w = n_a \theta_a = \frac{D_2}{2f}\) 保持不变！）。因此水中衍射艾里斑直径为：
     \[
     d_{o2} = \frac{1.22 \lambda_w}{\theta_w} = \frac{1.22(\lambda / n_w)}{D_2 / (2 n_w f)} = \frac{2.44 \lambda f}{D_2} \approx 1.03\text{ }\mu\text{m}!
     \]
     （即平面介质界面的纵向缩放效应精确抵消了波长变短效应，光斑大小不因水层或玻璃层而缩小，严格等于空气中扩束后的 \(1.03\text{ }\mu\text{m}\)！）

4. **双光束模型中小球所受光力 \((F_x, F_y)\) 及与重力之比**
   - **物理核心**：小球浸没在折射率为 \(n_w = 1.33\) 的蒸馏水中，水中光子波长为 \(\lambda_w = \lambda / n_w\)，故单位时间内功率为 \(p\) 的光束在水中携带的动量流（即光力尺度）为 \(\frac{n_w p}{c}\)（Minkowski 光动量）。
   - 入射总动量流：\(\dot{\mathbf{P}}_{\text{入}} = \frac{n_w(p_1 + p_2)}{c}\hat{i}\)。
   - 出射总动量流（见图 b，\(L_1\) 上偏 \(15^\circ\)、\(L_2\) 下偏 \(15^\circ\)）：
     \[
     \dot{\mathbf{P}}_{\text{出}} = \frac{n_w}{c}\left[(p_1 + p_2)\cos 15^\circ\,\hat{i} + (p_1 - p_2)\sin 15^\circ\,\hat{j}\right].
     \]
   - 由动量定理 \(\mathbf{F} = \dot{\mathbf{P}}_{\text{入}} - \dot{\mathbf{P}}_{\text{出}}\)，得小球受力（\(p_1 = 1.0\text{ mW}, p_2 = 2.0\text{ mW}\)）：
     \[
     F_x = \frac{n_w (p_1 + p_2)}{c}(1 - \cos 15^\circ) = \frac{1.33\times 3.0\times 10^{-3}}{3.00\times 10^8}(1 - \cos 15^\circ) \approx 4.53\times 10^{-13}\text{ N},
     \]
     \[
     F_y = \frac{n_w (p_2 - p_1)}{c}\sin 15^\circ = \frac{1.33\times 1.0\times 10^{-3}}{3.00\times 10^8}\sin 15^\circ \approx 1.15\times 10^{-12}\text{ N} \quad (\text{沿 }+y\text{ 指向强光侧!}).
     \]
   - 小球重力 \(G_b = \rho_b \cdot \frac{4}{3}\pi \left(\frac{D_b}{2}\right)^3 g = 1.0\times 10^3\times \frac{4}{3}\pi (1.0\times 10^{-6})^3\times 9.80 \approx 4.105\times 10^{-14}\text{ N}\)。
   - 与重力之比：
     \[
     \frac{F_x}{G_b} \approx 11.0, \qquad \frac{F_y}{G_b} \approx 28.0.
     \]

5. **\(T = 300\text{ K}\) 时水中聚苯乙烯小球的方均根速率 \(v_{\text{rms}}\)**
   由能量均分定理 \(\frac{1}{2}m_b v_{\text{rms}}^2 = \frac{3}{2}k_B T\)（\(m_b \approx 4.189\times 10^{-15}\text{ kg}\)）：
   \[
   v_{\text{rms}} = \sqrt{\frac{3 k_B T}{m_b}} = \sqrt{\frac{3 \times 1.38\times 10^{-23}\times 300}{4.189\times 10^{-15}}} \approx 1.72\times 10^{-3}\text{ m/s}.
   \]

6. **能被光势阱捕获的小球最大速率 \(v_{\max}\)**
   势阱中心 \(r = 0\) 处势能最低为 \(U_{\min} = -U_0\)（\(U_0 = 0.078\text{ eV} = 1.250\times 10^{-20}\text{ J}\)），逸出势阱边界后 \(U = 0\)。逃逸临界条件为总机械能 \(\frac{1}{2}m_b v_{\max}^2 - U_0 = 0\)：
   \[
   v_{\max} = \sqrt{\frac{2 U_0}{m_b}} = \sqrt{\frac{2\times 0.078\times 1.602\times 10^{-19}}{4.189\times 10^{-15}}} \approx 2.44\times 10^{-3}\text{ m/s}.
   \]

7. **质量分别为 \(m\) 和 \(2m\) 的小球被光势阱捕获的概率大小比较**
   对定域势阱 \(U_0\)，小球被捕获的条件是动能 \(\frac{1}{2}m v^2 \le U_0\)，即 \(v \le v_{\max}(m) = \sqrt{\frac{2 U_0}{m}}\)。作无量纲能量变量代换 \(x = \sqrt{\frac{m}{2k_B T}} v\)，则捕获概率为：
   \[
   P(m) = \int_0^{\sqrt{\frac{2U_0}{m}}} 4\pi\left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-\frac{mv^2}{2k_B T}}\,\mathrm{d}v = \frac{4}{\sqrt{\pi}}\int_0^{\sqrt{\frac{U_0}{k_B T}}} x^2 e^{-x^2}\,\mathrm{d}x.
   \]
   可见积分限与被积函数均已完全消去质量 \(m\)，仅取决于势阱深与热能之比 \(U_0/(k_B T)\)。故在相同势阱深度 \(U_0\) 下，**质量为 \(m\) 与 \(2m\) 的小球被捕获的概率完全相等**：\(P_m = P_{2m}\)。

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第（1）–（7）问与官方参考解答（`page-15.jpg`–`page-18.jpg`）全面吻合！特别值得称道的是第（3）问水中艾里斑直径 \(n_w\) 精确消去的证明（官方同样从垂直放大率 \(V_1 = V_2 = 1\) 与折射角变换双方面证明了这一点）、以及第（4）问官方明确采用水中光动量 \(p = \frac{p n_w \Delta t}{c}\)（得到 \(10.9\) 与 \(28.0\)，其中 \(10.9\) 系把 \(4.53\times 10^{-13}\) 修约成 \(0.45\times 10^{-12}\) 再除 \(4.11\times 10^{-14}\) 产生的小差异）。
- **官方排版笔误记录**：
  - `page-15.jpg` 式(1) 公式分母误印成 `R_1`（带数却代入 `D_1 = 1.50 mm`），式(3) 亦将直径写成 `R_2`；
  - `page-16.jpg` 式(7) 第一行把 `i_2 =` 误印成 `i_1 =`；
  - `page-17.jpg` 式(27)（且缺式(26)编号）把 `U(r)` 势阱中心最小值误印成 `-U_0(1 - y^2/4)_{y=0}`。
- **核心难点与典型易错点**：
  - 难点1：理解平面介质界面折射不改变衍射极限光斑大小（即数值孔径 \(\text{NA} = n\sin\theta\) 守恒与 \(\lambda_w = \lambda/n_w\) 共同保证 \(d_{o2} = d_{o1}/4 = 1.03\text{ }\mu\text{m}\)）。
  - 难点2：正确计入浸没介质折射率 \(n_w\) 对水中光束动量流的放大因子（\(F \propto n_w P / c\)）。
  - 易错点1：第（3）问误以为水中波长缩短为 \(\lambda / n_w\) 而物镜焦距不变，从而多除以一个 \(n_w\) 算出 \(0.77\text{ }\mu\text{m}\)。
  - 易错点2：第（7）问看到 \(v_{\max} = \sqrt{2U_0/m}\) 随 \(m\) 增大而减小，便凭直觉猜“质量越大逃逸速度越小所以越难捕获”，忽略了热平衡下大质量小球的最概然速率 \(v_p = \sqrt{2k_B T/m}\) 按完全相同的比例 \(1/\sqrt{m}\) 缩小！
- **教练总结与迁移建议**：光学实验建模题往往“入口宽、步步递进”。只要紧扣**数值孔径守恒**、**水中动量 \(n_w E / c\)** 和**热力学动能分布与质量无关**这三条硬核心原理，看似庞杂的现代诺奖实验题（光镊）即可迎刃而解。

---

## 13. 第36届决赛理论第6题 · 从《周髀算经》与金星凌日到太阳质子-质子聚变全模型 (`cpho-2019-final-theory-problem-slice-q6`)

- **难度评级**：`D4`
- **物理模型**：天体视差几何（金星凌日）、黑体辐射、恒星核聚变 pp 链产能动力学与辐射失质量轨道绝热演化
- **教学标签**：`金星凌日测日地距`、`核聚变pp链`、`反应率对数图估温`、`辐射失质量角动量守恒`、`天体物理综合建模`
- **适用层次**：高中竞赛 (复赛/决赛) · 兼顾本科普通物理

### Phase 1：独立盲解记录（只看原题）

1. **《周髀算经》竹竿测太阳视角**
   - i) 由小角几何相似得 \(\Phi = \frac{D}{S_{\text{日地}}} = \frac{d}{L}\)。
   - ii) 减误办法：前端加小孔或半透光遮挡/目镜准直片消除人眼炫光与瞳孔尺寸影响；投影成像在屏上测量代替人眼直视；多次测量取平均并选择太阳高度角较高时观测以减少大气折射畸变。
   - iii) \(d = 1\text{ 寸}\)，\(L = 8\text{ 尺} = 80\text{ 寸} \implies \Phi = \frac{1}{80} = 0.0125\text{ rad}\)。

2. **金星凌日测太阳视角与日地距离**
   - i) 由开普勒第三定律，\(r_{\text{VE}} = \frac{S_{\text{日金}}}{S_{\text{日地}}} = \left(\frac{T_{\text{金}}}{T_{\text{地}}}\right)^{2/3} = \left(\frac{224.701}{365.256}\right)^{2/3} \approx 0.7233\)。
   - ii) 如图 a，金星中心进入与离开日面的时刻分别为两次外切/内切的中间时刻：\(t_{\text{入}} = \frac{6:10:10 + 6:27:51}{2} = 6:19:00.5\)，\(t_{\text{出}} = \frac{12:31:57 + 12:49:31}{2} = 12:40:44\)，故中心扫过日面弦长 \(D_p\) 历时 \(t_{\text{凌}} = 6\text{ h }21\text{ m }43.5\text{ s} = 0.26509\text{ d}\)。
     在随日地连线共转的参考系中，金星以会合角速度 \(\omega_{\text{syn}} = 2\pi\left(\frac{1}{T_{\text{金}}} - \frac{1}{T_{\text{地}}}\right)\) 运动，垂直扫过线位移为 \(S_{\text{日金}}\omega_{\text{syn}} t_{\text{凌}}\)。将其从地金距离 \((S_{\text{日地}} - S_{\text{日金}})\) 投影至日地距离 \(S_{\text{日地}}\) 处的日面弦长 \(D_p\)，得：
     \[
     \frac{D_p}{S_{\text{日地}}} = \frac{r_{\text{VE}}}{1 - r_{\text{VE}}} 2\pi\left(\frac{1}{T_{\text{金}}} - \frac{1}{T_{\text{地}}}\right) t_{\text{凌}} \approx 7.458\times 10^{-3} \quad \left(\approx \frac{1}{134}\right).
     \]
     由弦心距 \(h_p = \frac{5}{16}D\) 及几何关系 \(D_p = \sqrt{D^2 - 4h_p^2} = \frac{\sqrt{39}}{8}D\)，得太阳视角：
     \[
     \Phi = \frac{D}{S_{\text{日地}}} = \frac{8}{\sqrt{39}}\frac{D_p}{S_{\text{日地}}} \approx 9.55\times 10^{-3}\text{ rad} \quad \left(\approx \frac{1}{105}\right).
     \]
   - iii) 设地面两观察者 \(P, P'\) 在垂直观测方向投影间距为 \(H\)。通过金星（距日 \(r_{\text{VE}} S_{\text{日地}}\)、距地 \((1-r_{\text{VE}})S_{\text{日地}}\)）在日面上形成两条同侧平行弦 \(AB, A'B'\)，其弦心距之差为 \(\Delta h = h_{p'} - h_p = \frac{r_{\text{VE}}}{1 - r_{\text{VE}}} H\)。记日面等效相对角速度 \(\omega_{\text{app}} = \frac{2\pi r_{\text{VE}}}{1 - r_{\text{VE}}}\left(\frac{1}{T_{\text{金}}} - \frac{1}{T_{\text{地}}}\right)\)，则 \(D_p = S_{\text{日地}}\omega_{\text{app}} t_p\)、\(D_{p'} = S_{\text{日地}}\omega_{\text{app}} t_{p'}\)，代入 \(\Delta h = \frac{1}{2}\sqrt{D^2 - D_{p'}^2} - \frac{1}{2}\sqrt{D^2 - D_p^2}\) 解得：
     \[
     S_{\text{日地}} = \frac{2 r_{\text{VE}} H}{(1 - r_{\text{VE}})\left[\sqrt{\Phi^2 - (\omega_{\text{app}} t_{p'})^2} - \sqrt{\Phi^2 - (\omega_{\text{app}} t_p)^2}\right]}.
     \]
   - iv) 忽略自转与地轴倾角时，同一经度北京（\(39.5^\circ\)）与香港（\(22.5^\circ\)）在垂直观测方向投影间距：
     \[
     H = R_E(\sin 39.5^\circ - \sin 22.5^\circ) = 6370\times(\sin 39.5^\circ - \sin 22.5^\circ) \approx 1614\text{ km}.
     \]
     代入 \(t_p = 6:21:57\)、\(t_{p'} = 6:19:31\) 及第 ii) 问数据，得：
     \[
     S_{\text{日地}} \approx 1.43\times 10^8\text{ km} \quad (\text{若不取投影而用弧长 } 1890\text{ km 则为 } 1.67\times 10^8\text{ km}).
     \]

3. **太阳能量输出与表面温度**
   - i) 地球截获太阳辐射功率：\(P_E = I \cdot \pi R_E^2 = 1.37\times 10^3 \times \pi \times (6.37\times 10^6)^2 \approx 1.75\times 10^{17}\text{ W}\)。
   - ii) 人类年耗能 \(E_{\text{人}} = 7.0\times 10^9\times 3000\times 4\times 3.6\times 10^6 \approx 3.024\times 10^{20}\text{ J}\)，平均功率 \(P_{\text{人}} \approx 9.58\times 10^{12}\text{ W}\)，占比 \(\frac{P_{\text{人}}}{P_E} \approx 5.5\times 10^{-5}\)（约 \(1 : 1.8\times 10^4\)）。
   - iii) 太阳总光度：\(L_\odot = I \cdot 4\pi S_{\text{日地}}^2 = 1.37\times 10^3\times 4\pi\times (1.5\times 10^{11})^2 \approx 3.87\times 10^{26}\text{ W}\)。
   - iv) 斯特藩-玻尔兹曼定律 \(L_\odot = \pi D^2 \sigma T_s^4\)：
     \[
     T_s = \left(\frac{3.874\times 10^{26}}{\pi\times (1.4\times 10^9)^2 \times 5.67\times 10^{-8}}\right)^{1/4} \approx 5.77\times 10^3\text{ K}.
     \]

4. **太阳质量、平均密度与化学产能极限寿命**
   - i) 由开普勒定律 \(M_\odot = \frac{4\pi^2 S_{\text{日地}}^3}{G T_{\text{地}}^2} \approx 2.01\times 10^{30}\text{ kg}\)，平均密度 \(\bar{\rho}_\odot = \frac{6 M_\odot}{\pi D^3} \approx 1.40\times 10^3\text{ kg/m}^3\)。
   - ii) 按上题给定标准煤发电等效值 \(q = 4\text{ kWh/kg} = 1.44\times 10^7\text{ J/kg}\)（或标准煤热值 \(2.93\times 10^7\text{ J/kg}\)），全太阳煤燃烧仅能维持 \(\tau_{\text{煤}} = \frac{M_\odot q}{L_\odot} \approx 2.36\times 10^3\text{ 年}\)（按热值约为 \(4.8\times 10^3\text{ 年}\)）。与存在 \(50\text{ 亿年}\) 对比，产能效率至少须是化学反应的 \(2.1\times 10^6\) 倍（或 \(\sim 1.0\times 10^6\) 倍）。

5. **氢核聚变 pp 链分析**
   将核反应组合为 \(2\text{(a)} + 2\text{(b)} + \text{(c)}\)，加上两个正电子与等离子体中两个电子湮灭成光子：净反应为 \(4p + 2e^- \to {}^4\text{He} + 2\nu_e + \gamma\)。忽略中微子带走能量，每消耗 \(4\) 个质子释放总能量：
   \[
   \Delta E_{\text{循环}} = (4m_p + 2m_e - m_{{}^4\text{He}})c^2 = (4\times 938.3 + 2\times 0.51 - 3727.5)\text{ MeV} = 26.72\text{ MeV} = 4.281\times 10^{-12}\text{ J}.
   \]
   - i) 每消耗 1 个质子放能 \(\Delta E_p = 6.68\text{ MeV} = 1.070\times 10^{-12}\text{ J}\)，单位时间消耗质子数：
     \[
     \dot{N}_p = \frac{L_\odot}{\Delta E_p} \approx 3.62\times 10^{38}\text{ s}^{-1}.
     \]
   - ii) 太阳总质子数 \(N_p = \frac{0.71 M_\odot}{m_p} \approx 8.53\times 10^{56}\)，最多还可维持时间：
     \[
     t_{\max} = \frac{N_p}{\dot{N}_p} \approx 2.36\times 10^{18}\text{ s} \approx 7.46\times 10^{10}\text{ 年},
     \]
     单位时间单个质子的 \(p\text{-}p\) 反应概率：
     \[
     P_{pp} = \frac{\dot{N}_p}{N_p} \approx 4.25\times 10^{-19}\text{ s}^{-1}.
     \]
   - iii) 每净消耗 4 个质子（发生 2 次 (a) 反应）产生 2 个中微子，故地球处中微子通量：
     \[
     \Phi_\nu = \frac{\dot{N}_p / 2}{4\pi S_{\text{日地}}^2} \approx 6.40\times 10^{14}\text{ m}^{-2}\cdot\text{s}^{-1}.
     \]
   - iv) 单位时间质量亏损：\(\frac{\mathrm{d}M_\odot}{\mathrm{d}t} = \frac{L_\odot}{c^2} \approx 4.30\times 10^9\text{ kg/s}\)（合 \(1.36\times 10^{17}\text{ kg/年}\)）。

6. **太阳核心区域温度下限估算**
   核心半径 \(R_{\text{核}} = \frac{1}{4}R_\odot\)，体积 \(V_{\text{核}} = \frac{1}{64}V_\odot\)。由 \(R(T) = P / n_p\) 且 \(R(T)\) 随 \(T\) 单调递增，温度下限对应核心密度取理论最大上限（假设太阳总氢质量全部聚在核心内）：
   \[
   n_{p,\max} = \frac{N_p}{V_{\text{核}}} = 64 \bar{n}_p \approx 3.80\times 10^{25}\text{ cm}^{-3}, \qquad R(T) \ge \frac{P_{pp}}{n_{p,\max}} \approx 1.12\times 10^{-44}\text{ cm}^3/\text{s}.
   \]
   查图 c 中 `p+p` 点划线（瓶颈步反应），\(R \sim 10^{-44}\text{ cm}^3/\text{s}\) 恰好对应温度下限：
   \[
   T_{\min} \approx 1.0\times 10^7\text{ K}.
   \]

7. **单个中微子最大能量与辐射能计算最大相对误差**
   中微子仅在步 (a) \(p + p \to D + e^+ + \nu_e\) 中产生，质量亏损（含 \(e^+\) 静能扣除，因正电子湮灭在其后发生）为：
   \[
   Q_a = (2m_p - m_D - m_e)c^2 = (2\times 938.3 - 1875.6 - 0.51)\text{ MeV} = 0.49\text{ MeV}.
   \]
   当反冲的 \(D\) 与 \(e^+\) 共速且动能近似为零（\(\frac{p_\nu^2}{2m_D} \approx 6\times 10^{-5}\text{ MeV} \ll Q_a\)）时，单个中微子带走最大能量 \(E_{\nu,\max} \approx 0.49\text{ MeV}\)。每个循环发射 2 个中微子，故忽略中微子带走能量造成的最大相对误差为：
   \[
   \delta_{\max} = \frac{2 E_{\nu,\max}}{\Delta E_{\text{循环}}} = \frac{0.98}{26.72} \approx 3.7\%.
   \]

8. **一亿年辐射失质量及地球公转周期变化**
   - i) \(\Delta M = \frac{L_\odot}{c^2}\Delta t = 4.304\times 10^9 \times (10^8\times 365.256\times 86400) \approx 1.36\times 10^{25}\text{ kg}\)。
   - ii) 太阳辐射各向同性且缓变，地球相对太阳的角动量守恒：\(L_E = m_E \sqrt{G M_\odot r} = \text{常量} \implies r \propto M_\odot^{-1}\)（轨道半径微增）。代入开普勒第三定律 \(T \propto r^{3/2} M_\odot^{-1/2} \propto M_\odot^{-2}\)（或直接 \(L_E = m_E \frac{2\pi r^2}{T} \implies T \propto r^2 \propto M_\odot^{-2}\)）。取微扰得：
     \[
     \frac{\Delta T}{T_{\text{地}}} = 2\frac{\Delta M}{M_\odot} \approx 1.35\times 10^{-5} \implies \Delta T \approx 4.27\times 10^2\text{ s}.
     \]

### Phase 2：对照参考解答与教学拆解

- **与参考解答对比**：盲解第 1)–8) 全部物理模型、关键推导（含角动量守恒导出 \(T \propto M_\odot^{-2}\) 而不是固定 \(r\) 的常见错误）与数值量级与官方参考解答（`page-22.jpg`–`page-27.jpg`）**高度一致**！
- **官方解答亮点、修约偏差与笔误梳理（重要！）**：
  1. **第 2) iv) 问基线投影 \(H\) 的计算差异**：题目 iii) 明确要求“直线距离（在垂直于观测方向上的投影）为 \(H\)”，盲解据此取赤道面垂直投影弦长 \(H = R_E(\sin 39.5^\circ - \sin 22.5^\circ) = 1614\text{ km}\) 得 \(S_{\text{日地}} = 1.43\times 10^8\text{ km}\)；而官方 `page-23.jpg` 式(11) 却直接把两地纬度差对应的**地表弧长** \(\frac{17^\circ}{180^\circ}\pi R_E = 1900\text{ km}\) 当成了 \(H\)，得到 \(1.6\times 10^8\text{ km}\)。此外官方在 `page-23.jpg` 列出北京 `6:10:00` 与 `12:31:57` 时实际是直接相减得到 `6:21:57`（而非先取内外切均值）。
  2. **第 5) i) 问正电子湮灭表达式**：官方 `page-25.jpg` 式(20) 把 4 个质子变成氦核及 2 个正电子湮灭的净质能差写为 \((4M_p - M_{{}^4\text{He}} - 2m_e + 4m_e)c^2\)（括号内先扣 2 个正电子生成再加回 2 对正负电子湮灭共 4 个 \(m_e\)），结果同为 \(26.7\text{ MeV}\)。
  3. **第 6) 问核反应率下限小失误**：官方 `page-26.jpg` 式(26) 计算核心区质子数密度上限 \(n_{p,\max}\) 时忘了乘氢质量占比 \(0.71\)（算出全核子密度 \(5.4\times 10^{25}\text{ cm}^{-3}\) 而非质子密度 \(3.8\times 10^{25}\text{ cm}^{-3}\)），同时把分子上的 \(P_{pp}\) 误写成了 \(2.9\times 10^{-19}\text{ s}^{-1}\)（实为第 5)ii)问的 \(4.2\times 10^{-19}\text{ s}^{-1}\)）；幸好在对数图 `图 c` 中 \(5.4\times 10^{-45}\) 与 \(1.1\times 10^{-44}\) 均对应垂直陡升区的 \(T \approx 1.0\times 10^7\text{ K}\)。
  4. **其他排版痕迹**：`page-24.jpg` 与 `page-27.jpg` 存在红色修订残留公式；`page-22.jpg` 式(5) 把两地观察视角写成了 \(\frac{D_p}{S_{\text{日金}}} = \frac{D_p}{S_{\text{日地}}} + \dots\)（与 \(D_p\) 符号混用，实指日面弦在金星距离处张角与在地球距离处张角之差等于会合角位移）。
- **核心难点与典型易错点**：
  - 难点1：第 2) 问理解金星凌日中的**双重几何投影**——公转角速度差需乘金日/地金距离比 \(\frac{r_{\text{VE}}}{1 - r_{\text{VE}}}\)，且视差基线也按同比例投影到日面弦心距之差。
  - 难点2：第 6) 问读懂为何用“核心全包总质量”去求温度**下限**（反比关系 \(R(T) = P/n\) 下，\(n\) 取最大上限才给出 \(R(T)\) 最小下限，从而确定门槛温度）。
  - 难点3：第 8) 问识别辐射失质量引起的**轨道半径与周期耦合绝热变化**（\(L = \sqrt{GMr}\) 守恒 \(\implies T \propto M^{-2}\)，变分因子为 \(2\) 而非 \(\frac{1}{2}\)！）。
  - 易错点1：第 5) 问算核聚变能量时，题给为**裸核质量**，切忌再按原子质量套公式而漏掉 \(2 m_e c^2 = 1.02\text{ MeV}\) 的正负电子湮灭光子能量；另外易弄错“每消耗 4 个质子产生 2 个中微子”。
  - 易错点2：第 7) 问错把中微子能量减去正电子湮灭能量或直接算成 \(1.51\text{ MeV}\)（正电子湮灭发生在反应 (a) 之后，中微子早已逃逸，故其最大能量仅由反应 (a) 本身 Q 值 \(0.49\text{ MeV}\) 决定）。
- **教练总结与迁移建议**：这道压轴题堪称太阳物理的百科全书——从古代几何测角、天体测量视差法、黑体辐射、核聚变网络瓶颈、中微子能谱到天体力学绝热不变量一气呵成。做这类长题时，务必保持“每问结束即时校验数量级与天体常识（如 \(1.5\times 10^8\text{ km}, 5800\text{ K}, 10^7\text{ K}, 6.5\times 10^{10}\text{ cm}^{-2}\text{s}^{-1}\)）”，就能在复杂链条中立于不败之地。
