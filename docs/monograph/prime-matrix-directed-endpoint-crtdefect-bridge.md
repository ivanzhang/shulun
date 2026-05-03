# Directed Endpoint CRTDefect 桥接定理

**状态：** `signed_lowmod_projection_bridge_closed_to_named_crtdefect_exit`

本文接续 `prime-matrix-signed-lowmod-bridge-hard-attack.md`。目标是完成其中已分离出的确定桥接：

```text
large endpoint sawtooth projection
=> directed CRTDefect / OSPC exit.
```

注意：本文闭合的是“进入命名出口”的桥接，不是自动排除该出口。若主链已经有对应 `CRTDefect/Tail-anchor/OSPC` 排斥定理，则可接上形成矛盾；若没有，则剩余义务就是出口排斥本身。

## 1. 低模端点原子

设

\[
I=[L,R]\cap\mathbb Z,\qquad N=R-L+1,
\]

并令 `P_T=\prod_{\ell<T}\ell`。对 `d|P_T` 定义端点原子

\[
e_d(I)=
\left\{{L-1\over d}\right\}
-
\left\{{R\over d}\right\}.
\]

由 SLM-1，

\[
D_T(I)=R_T(I)-NV_T
=\sum_{d\mid P_T}\mu(d)e_d(I).
\tag{1}
\]

## 2. Directed Endpoint CRTDefect 定义

取一个有限低模字典 `\mathfrak B_T`，其元素 `B` 是 `d|P_T` 的不交块，例如：

- 按 `d` 的 dyadic 尺度分块；
- 按最小素因子/最大素因子分块；
- 按素支撑含某小素 `r` 分块；
- 按辅助模 `r` 的非平凡 Fourier 角色分块。

定义块投影

\[
\mathcal E_B(I)=
\sum_{d\in B}\mu(d)e_d(I).
\]

**Definition DEC（有向端点 CRT 缺陷）。**
若存在 `B∈\mathfrak B_T` 使

\[
|\mathcal E_B(I)|\ge \kappa_B,
\tag{DEC}
\]

则称 `I` 触发 `Directed Endpoint CRTDefect`，记为 `DEC_T(I;\mathfrak B_T,\kappa)`。

该定义是 `CRTDefect` 的端点版：它不是说完整 CRT 周期不均衡，而是说短窗口端点在某个低模方向上产生了足以影响筛余非空/预算的有向投影。

## 3. 大缺陷到 DEC 的鸽巢桥

**Theorem DEC-1（投影桥）。**
设 `\mathfrak B_T` 为 `{d:d|P_T}` 的不交分块，并设 `\mathcal G=\bigcup_{B\in\mathfrak B_T}B`。若

\[
|D_T(I)|\ge \Delta
\]

且字典外尾项满足

\[
\left|
\sum_{\substack{d\mid P_T\\d\notin\mathcal G}}\mu(d)e_d(I)
\right|\le E_{\rm tail}<\Delta,
\tag{2}
\]

则存在 `B∈\mathfrak B_T` 使

\[
|\mathcal E_B(I)|
\ge
{\Delta-E_{\rm tail}\over |\mathfrak B_T|}.
\tag{3}
\]

因此只要取

\[
\kappa_B\le { \Delta-E_{\rm tail}\over |\mathfrak B_T|}
\]

对某个块成立，`I` 必触发 `Directed Endpoint CRTDefect`。

**证明。**
由 `(1)` 与 `(2)`，

\[
\left|
\sum_{B\in\mathfrak B_T}\mathcal E_B(I)
\right|
\ge \Delta-E_{\rm tail}.
\]

若所有 `B` 都满足

\[
|\mathcal E_B(I)|< { \Delta-E_{\rm tail}\over |\mathfrak B_T|},
\]

则三角不等式给出总和绝对值小于 `\Delta-E_tail`，矛盾。证毕。

## 4. 完整 q 行的单位旋转形式

对完整 `q` 行

\[
I_s=[(s-1)q+1,sq],
\]

端点原子为

\[
e_d(s)=
\left\{{(s-1)q\over d}\right\}
-
\left\{{sq\over d}\right\}.
\tag{4}
\]

若 `d|P_T` 且 `T\le p<q`，则 `(q,d)=1`。因此 `s\mapsto sq\bmod d` 是模 `d` 的单位旋转。

**Lemma DEC-2（旋转 Fourier 化）。**
对每个 `d|P_T`，函数 `e_d(s)` 是模 `d` 周期、均值为 `0` 的 sawtooth 差分。故任意块投影

\[
\mathcal E_B(s)=\sum_{d\in B}\mu(d)e_d(s)
\]

是模

\[
Q_B={\rm lcm}_{d\in B}d
\]

上的零均值周期函数，并有有限 Fourier 展开

\[
\mathcal E_B(s)=
\sum_{\substack{h\bmod Q_B\\h\ne0}}
\widehat{\mathcal E}_B(h)
e^{2\pi i h s/Q_B}.
\]

若 `|\mathcal E_B(s_0)|\ge\kappa_B`，则存在非零频率 `h` 使

\[
|\widehat{\mathcal E}_B(h)|
\ge {\kappa_B\over Q_B-1}.
\tag{5}
\]

**证明。**
周期性和零均值来自 `q` 在模 `d` 上可逆，完整周期内端点差分望远镜为零。有限 Fourier 展开是有限循环群上的标准展开。若所有非零 Fourier 系数都小于 `\kappa_B/(Q_B-1)`，则对任意 `s`，

\[
|\mathcal E_B(s)|
\le
\sum_{h\ne0}|\widehat{\mathcal E}_B(h)|
<\kappa_B,
\]

矛盾。证毕。

这说明 `DEC` 等价于某个低 CRT 坐标上的非零 Fourier 模式异常，是 OSPC/CRTDefect 的标准可审稿入口。

## 5. 与 OSPC 的接法

若块 `B` 是按辅助模 `r` 的残基/Fourier 角色组织，则 `(5)` 给出非零角色偏大。把同一块内的总绝对质量记为 `\mathcal A_B`，定义

\[
E_{\rm dir}(B)=
{(r-1)\sum_{\chi\ne\chi_0}|C_\chi(B)|^2\over \mathcal A_B^2}.
\]

若某个非零角色满足

\[
|C_\chi(B)|\ge \lambda_B\mathcal A_B,
\]

则

\[
E_{\rm dir}(B)\ge (r-1)\lambda_B^2.
\]

因此若

\[
(r-1)\lambda_B^2\ge 1+\delta_{\rm dir},
\]

则触发修正归一化后的 `OSPC*`。若未达到该能量阈值，但 `(DEC)` 已达到端点异常阈值，则登记为 `Directed Endpoint CRTDefect`。这给出二分：

```text
large endpoint block projection
=> OSPC*
or Directed Endpoint CRTDefect.
```

## 6. 桥接闭合结论

综合 DEC-1 与 DEC-2：

**Theorem SESE-to-Exit（SESE 到命名出口）。**
若递推坏窗口 `I` 满足：

1. `|D_T(I)|>=Delta`；
2. 所选低模字典外尾项 `<=E_tail<Delta`；
3. 字典块阈值按 `(3)` 设置；

则 `I` 必触发

```text
Directed Endpoint CRTDefect
or OSPC*.
```

若主链已有

```text
Directed Endpoint CRTDefect / OSPC*
=> Tail-anchor / CRT rigidity contradiction,
```

则该坏窗口被排除。

## 7. 剩余边界

本文完成的是：

```text
large signed low-mod endpoint defect
=> named low-mod exit.
```

仍未由本文完成的是：

```text
named low-mod exit
=> contradiction.
```

这一区分必须在审稿稿件中保留。否则会把“定义了缺陷出口”误写成“排除了缺陷出口”。

## 8. 对最终递推链的影响

相邻素数递推现在可写为：

```text
Row(p)
+ ASB/RPD unless positive DEC/OSPC*
+ Annulus-Rough unless negative DEC/OSPC*
+ Exclusion of DEC/OSPC*
=> Row(q).
```

其中前两项的桥接已经由本文和前文完成；最后一项是全局矛盾场出口排斥。若前文已有可接受的出口排斥，则递推链闭合；若没有，则唯一剩余不再是低模桥接，而是 `DEC/OSPC*` 排斥。

## 9. 出口排斥的最新压缩

后续审查见 `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md`。该文档确认一个必须保留的审稿边界：

```text
single Directed Endpoint CRTDefect
not automatically contradiction.
```

原因是低模端点场在完整 CRT 周期上零均值，但零均值只给全周期相消，不排除单个短窗口出现大锯齿端点值。真正可攻的出口排斥必须升级为二分：

```text
DEC/OSPC* bad window
=> Persistent DEC
   or Single-window Anchor Escape contradiction.
```

其中 `Persistent DEC` 给出坏行指示函数的非零 Fourier/CRT 缺陷；`Single-window Anchor Escape` 则要求证明孤立短窗口端点尖峰不能同时消灭旧核心素数与壳层旧筛幸存者。因此最终递推链应更新为：

```text
Row(p)
+ ASB/RPD unless positive DEC/OSPC*
+ Annulus-Rough unless negative DEC/OSPC*
+ PDEC-or-SAE exclusion
=> Row(q).
```

这不是终局闭合，而是把最后出口排斥压缩为一个更窄、更可审稿的硬输入。
