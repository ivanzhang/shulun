# H4-PDEC ColumnDefect 路由合同

**状态：** `h4_pdec_column_defect_routing_contract_closed_exclusion_open`

本文承接 `h4-pdec-column-cap-source-lemma.md` 与
`h4-pdec-column-cap-coefficient-ledger.md`，专攻当前非 LHB 型出口中的
`ColumnRadius / ColumnCRT` 接口。结论是：

```text
ColumnRadiusDefect 与 ColumnCRTDefect 已有可审稿的条件路由合同；
它们仍不是已排除出口。
```

也就是说，本文闭合的是“哪些数据可构成列缺陷证书、违反列预算时如何合法回流到命名出口”，
不是证明这些出口不可能发生。

## 1. 同口径输入

固定已经过同口径拆分的坏窗类型

\[
\theta=(Q,\tau,F,\kappa,q,\mathrm{window\mbox{-}shape}).
\]

坏行写为

\[
n_c=Hq+c,\qquad 1\le c<q,
\]

第 `q` 平凡列剥离。设旧标签集合为 `\mathcal L`，通常由 `\ell<q`
的筛素数给出。若列见证输入可用，则每个活动非平凡列 `c` 配有同列素数见证

\[
\pi_c=r_cq+c
\]

和位移

\[
d_c=r_c-H.
\]

对每个坏窗点 `x=n_c` 设 `\lambda(x)` 是解释它被覆盖的旧标签。若同一点有多个可选标签，
证书必须先固定一个标签选择器；不同选择器不能混入同一个 `A g\le b` 行。

## 2. 列见证的不可零同余

**Lemma H4-PDEC-CD0（列位移零类禁止）。**
若 `\lambda(n_c)=\ell`、`\ell\mid n_c`、`\pi_c` 是同列素数见证且
`\pi_c\ne\ell`，则

\[
d_c\not\equiv0\pmod\ell .
\]

**证明。**
若 `d_c≡0 (mod ell)`，则

\[
\pi_c-n_c=d_cq\equiv0\pmod\ell .
\]

又 `\ell\mid n_c`，故 `\ell\mid \pi_c`。由于 `\pi_c` 是素数且不等于 `\ell`，
矛盾。证毕。

该引理把横向坏行覆盖标签转成纵向列位移限制，是 `ColumnCRT` 合同的唯一入口。

## 3. 相位兼容性要求

`PDEC-Dual-Cert` 的变量是

\[
g(t)=\#\{x\in S:\tau(x)=t\}.
\]

因此任何列缺陷行若要写成 `\sum_t W(t)g(t)\le B`，必须满足以下相位兼容性：

```text
对当前同口径分支中的任意两个点 x,x'，
若 tau(x)=tau(x')，则它们在该列缺陷事件中的权重相同。
```

若不满足，必须先把 `tau` 细化为

\[
\tau'(x)=(\tau(x),\mathrm{column\mbox{-}defect\ data}(x)),
\]

或改用点级计数向量。不能把依赖具体列 `c` 或具体标签选择器的事件直接乘到旧的
`g(t)` 上。

## 4. ColumnRadiusDefect 证书对象

给定半径阈值 `D_0=D_0(q,\theta)` 和列见证选择器 `\Pi`，先定义点级高半径指标

\[
{\bf 1}_D(x)
=
{\bf 1}_{|d_c|>D_0}.
\]

若该指标对 `\tau` 相位兼容，则存在 `0/1` 相位兼容权重 `W_D(t)`，使

\[
{\bf 1}_D(x)=W_D(\tau(x))\qquad(x\in S).
\]

对应线性函数为

\[
R_D(g)=\sum_t W_D(t)g(t).
\]

**定义 H4-PDEC-ColumnRadiusDefect。**
若同口径坏窗族满足

\[
R_D(g)>0,
\]

或不存在能使全部活动列满足 `|d_c|\le D_0` 的列见证选择器，则登记
`ColumnRadiusDefect(D_0,\theta,S,\Pi)`。

证书元数据必须包含：

```text
defect_id；
theta=(Q,tau,F,kappa,q,window-shape)；
D_0；
witness_selector Pi；
phase_compatible_high_radius_weights W_D(t)；
excluded_exit=ColumnRadiusDefect；
source theorem or finite certificate；
normalization of g(t)。
```

**Lemma H4-PDEC-CD1（半径路由行）。**
在已经剥离 `ColumnRadiusDefect(D_0,\theta,S,\Pi)` 的剩余分支中，可以把

\[
R_D(g)\le0
\]

作为 `ConditionalRouting` 行写入 `PDEC-Dual-Cert`。

**证明。**
若剩余分支违反该行，则 `R_D(g)>0`。按定义，这正是
`ColumnRadiusDefect`。但该出口已经在当前分支剥离，矛盾。证毕。

## 5. ColumnCRTDefect 证书对象

对每个旧标签 `\ell` 和非零位移余类 `a mod \ell`，先定义点级指标

\[
{\bf 1}_{\ell,a}(x)
=
{\bf 1}_{\lambda(x)=\ell,\ d_c\equiv a\pmod\ell}.
\]

若该指标对 `\tau` 相位兼容，则存在 `0/1` 相位兼容权重 `W_{\ell,a}(t)`，使

\[
{\bf 1}_{\ell,a}(x)=W_{\ell,a}(\tau(x))\qquad(x\in S).
\]

零余类由 CD0 禁止；若出现零余类，必须先登记为以下之一：

```text
同列见证等于标签 ell 的小例外；
标签选择器不一致；
ColumnRadiusDefect；
ColumnCRTDefect 的零类版本。
```

给定位移负载阈值 `L_D=L_D(q,\theta,\ell)`，设

\[
R_{\ell,a}(g)=\sum_t W_{\ell,a}(t)g(t).
\]

**定义 H4-PDEC-ColumnCRTDefect。**
若存在 `\ell` 与 `a\ne0 mod \ell` 使

\[
R_{\ell,a}(g)>L_D(q,\theta,\ell),
\]

或零余类事件不能由 CD0 的小例外剥离，则登记
`ColumnCRTDefect(\ell,a,L_D,\theta,S,\Pi,\lambda)`。

证书元数据必须包含：

```text
defect_id；
theta=(Q,tau,F,kappa,q,window-shape)；
label ell；
residue a mod ell；
threshold L_D(q,theta,ell)；
phase_compatible_weights W_{ell,a}(t)；
zero-class exception list；
excluded_exit=ColumnCRTDefect；
source theorem or finite certificate；
normalization of g(t)。
```

**Lemma H4-PDEC-CD2（位移余类路由行）。**
在已经剥离对应 `ColumnCRTDefect` 与零类小例外的剩余分支中，可以把

\[
R_{\ell,a}(g)\le L_D(q,\theta,\ell)
\]

作为 `ConditionalRouting` 行写入 `PDEC-Dual-Cert`。

**证明。**
若该行被违反，则由定义进入 `ColumnCRTDefect`。若违反来自零余类，则由 CD0
除小例外外直接矛盾，并按合同登记为零类 `ColumnCRTDefect`。剩余分支已经剥离这些出口，
故不可能违反。证毕。

## 6. 与 RCI/CDB 审计常数的接口

现有审计给出两个有限定位常数：

```text
prime-matrix-column-row-bridge-audit.md:
  q<=1000 的最大列见证半径为 107。

prime-matrix-rci-cdb-joint-audit.md:
  p<=1000 的紧行最大列见证半径为 81；
  紧行最大尾标签负载为 2；
  紧行最大位移余类负载为 2。
```

这些常数只允许作为有限证书或阈值候选，不能直接全局化。按本文合同，它们可进入三类行：

| 行 | 条件形式 | 当前状态 |
|---|---|---|
| `CC-FIN-RADIUS-1000` | `D_col>107 => 0` | 缺相位兼容权重 `W_D(t)` |
| `CC-FIN-TIGHT-RADIUS` | tight row 中 `D_col>81 => 0` | 已由 `h4-pdec-column-defect-weight-certificate.json` 在 `tau_fin` 下物化为空块 |
| `CC-FIN-DISPLOAD` | 位移余类负载 `>2 => 0` | 已由 `h4-pdec-column-defect-weight-certificate.json` 在 `tau_fin` 下物化为空块 |
| `CC-COND-RADIUS` | `R_D(g)>0 => ColumnRadiusDefect` | 本文给出路由合同 |
| `CC-COND-DISPLOAD` | `R_{\ell,a}(g)>L_D => ColumnCRTDefect` | 本文给出路由合同 |

`h4-pdec-column-defect-weight-certificate.json/md` 已完成两条紧行有限权重物化：

```text
tau_fin=(p,q,row)；
phase_count=835；
D_col>81 的异常块为空；
displacement residue load>2 的异常块为空。
```

因此下一步不是修改准入逻辑，而是证明或证书化全局阈值 `D_0,L_D`，并给出正式坏窗到
`tau_fin` 或全局相位的抽取映射。若兼容性失败，必须先细化 `tau`，再重新生成同口径证书。

## 7. 合成接入定理

**Theorem H4-PDEC-CD3（ColumnDefect 条件行准入）。**
设一个同口径 `PDEC-Dual-Cert` 分支已经剥离
`ColumnRadiusDefect`、`ColumnCRTDefect` 以及 CD0 的零类小例外。若给出满足本文元数据要求的
相位兼容权重 `W_D(t)`、`W_{\ell,a}(t)`、`D_0` 与 `L_D`，则 CD1 与 CD2 的所有行均可作为
`ConditionalRouting` 行进入同一坏窗计数向量 `g(t)` 的结构约束矩阵。

**证明。**
CD1 与 CD2 已分别证明每一行的违反都会进入已经剥离的命名出口。所有权重都按同一
`(Q,\tau,F,\kappa,q,\mathrm{window\mbox{-}shape})` 和同一 `g(t)` 定义，因此没有口径混合。
由 `H4-PDEC-S5`，这些行可在剩余分支中作为条件约束使用。证毕。

## 8. 审稿边界与下一硬点

本文完成：

```text
ColumnRadius/ColumnCRT 的证书对象定义；
半径与位移余类的条件路由行；
与有限审计常数 107、81、2 的准入关系；
CC-FIN-TIGHT-RADIUS 与 CC-FIN-DISPLOAD 的有限紧行权重物化；
同口径 PDEC-Dual-Cert 中的元数据要求。
```

本文没有完成：

```text
ColumnRadiusDefect 排斥；
ColumnCRTDefect 排斥；
全局阈值 D_0,L_D 的解析证明；
CC-FIN-RADIUS-1000 全行权重物化。
若旧 tau 不相位兼容，还需 tau 细化与重新归一化。
```

下一步最小硬点因此变为：

```text
优先证明正式坏窗抽取映射或全局 D_0,L_D 阈值；
同时证明集中位移余类必进入持续 endpoint/PDEC，或给出有限证书排除。
```
