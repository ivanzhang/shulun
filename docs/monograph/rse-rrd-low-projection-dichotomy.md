# RRD-low 低模投影与 OSPC 二分

**状态：** `normalized_ospc_formula_and_low_projection_bridge`

本报告继续处理 `RRD-low`。关键结论是：先修正 `OSPC` 的能量归一化，再把 `Pi_{<=Z}` 定义成低模字典的正交投影；这样 `RRD-low` 可以严格二分为“小则吸收，大则进入 OSPC/CRTDefect”。

## 1. OSPC 归一化修正

旧文档中的 OSPC 写法右侧额外除以 `r-1`，该尺度过弱：均匀分布也会自动满足，从而不能作为“有向集中”的判据。

应使用与实验脚本 `complex_energy` 一致的归一化：

\[
E_{\rm dir}(q,r)=
{(r-1)\sum_{a\in(\mathbb Z/r\mathbb Z)^\times}|C_a(q,r)|^2
\over
\mathcal A(q,r)^2}.
\]

这里 `A(q,r)` 是同一批项在分残基前的总绝对质量，即脚本中的 `total_abs`。使用 `A(q,r)` 而不是 `sum_a |C_a|` 可以把残基内相消也计入反集中效果，并与旧扫描的 `complex_energy` 完全一致。

修正后的有向小素集中定义为

\[
E_{\rm dir}(q,r)\ge 1+\delta_{\rm dir}.
\tag{OSPC*}
\]

在该规范下，均匀同相分布给 `E_dir=1`，单个残基类集中给 `E_dir=r-1`。这才是后续低模出口需要的尺度。

旧辅助模扫描在该尺度下的最大值为：

- `max complex_energy=0.004424`。
- `maxAbs/uniform=1.293232`。

这说明旧样本没有显示强 OSPC；也再次确认普通 support concentration 不足，必须使用有向能量判据。

## 2. 低模投影的正式对象

在 dyadic 层 `m~M` 上取 Hilbert 空间

\[
\mathcal H_M=L^2([M,2M),\mu_M),
\]

其中 `mu_M` 是归一化计数测度。令

\[
a(m)=1_{P^-(m)>Y}-\rho_M.
\]

选择低模字典 `D_Z`，由以下原子张成：

- `q<=Z` 的小模周期原子；
- Buchstab 分解的低层因子原子；
- 辅助模 `r` 上的有向残基块原子，对应 `C_a(q,r)`。

定义

\[
\Pi_{\le Z}:\mathcal H_M\to {\rm span}(D_Z)
\]

为正交投影；若字典非正交，则用 Gram 矩阵的外向区间逆来定义可审查投影。分解为

\[
a=a_{\rm low}+a_{\rm perp},\qquad
a_{\rm low}=\Pi_{\le Z}a.
\]

## 3. Hilbert 二分引理

令 `W` 为已经同权归一化的 RSE 临界测试函数，即上一节中由

\[
{|\omega_\ell|\over h}\cdot {hH\over \ell M}\big/{H\over M}
={|\omega_\ell|\over \ell}
\]

归一到 `V_omega=sum |omega_l|/l` 的测试函数。

则

\[
\mathcal E_{\rm low}=\langle \Pi_{\le Z}a,W\rangle
=\langle a,\Pi_{\le Z}W\rangle.
\]

由正交投影和 Cauchy--Bessel，得到严格二分：

```text
若 |E_low| <= 0.006，则 RRD-low 被账本吸收；
若 |E_low| > 0.006，则某个低模块 B(q,r) 的投影贡献超过块预算。
```

后一种块预算违例就是修正后 `OSPC*` 或直接 `CRTDefect` 的候选入口。

## 4. 当前预算接法

- `RRD-low <= 0.006`：由小情形吸收，或由大情形转交 OSPC/CRTDefect。
- `RRD-perp <= 0.012`：低模正交后再用 Buchstab/CRT 均衡估计。
- `RRD-conversion <= 0.002`：端点和振幅线性化误差。

## 5. 下一步审稿义务

- 把 OSPC 公式统一改为 E_dir(q,r)>=1+delta_dir。
- 在正文中定义 D_Z、Gram 矩阵和 Pi_{<=Z}。
- 证明低模块预算违例推出修正后的 OSPC 或直接 CRTDefect。
- 证明 a_perp 的同权测试范数 <=0.012。

本轮完成的是 `RRD-low` 的正确数学接口：修正 OSPC 尺度，并把低模大贡献严格定位到有限低模块。尚未完成的是低模块违例到 `CRTDefect` 的逐项定量证明，以及 `RRD-perp<=0.012`。
