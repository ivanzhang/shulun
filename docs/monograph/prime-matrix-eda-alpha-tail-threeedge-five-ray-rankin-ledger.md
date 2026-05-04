# ThreeEdge 五射线热门差值 Rankin 账本

**状态：** `alpha_tail_threeedge_five_ray_rankin_ledger_reduction_open`

本文继续处理 `ThreeEdge 高尾二边同源锚点能量` 的跨点相关分支。三边锚点有三类
`0,-r,-2r`，因此同一高素数 `q` 同时锚住两个三点链点时，差值只能落在五条射线
`0,±r,±2r mod q`。非共振差值由一个五因子乘积控制；共振差值升阶为四点/五点光滑链。

## 1. 五射线复用数

固定差值

\[
s=d_1-d_2.
\tag{FRL-1}
\]

若 `q` 同时锚住 `d_1,d_2`，则存在

\[
c_1,c_2\in\{0,-r,-2r\}
\tag{FRL-2}
\]

使

\[
d_1\equiv c_1,\qquad d_2\equiv c_2\pmod q.
\tag{FRL-3}
\]

于是

\[
s=d_1-d_2\equiv c_1-c_2\in\{0,\pm r,\pm2r\}\pmod q.
\tag{FRL-4}
\]

定义非共振复用数

\[
\nu_R^{(5)}(s;r)=
\#\{q:R<q\le y,\ q\nmid r,\ q\mid s(s-r)(s+r)(s-2r)(s+2r)\}.
\tag{FRL-5}
\]

这里必须排除

\[
s\in\{0,\pm r,\pm2r\},
\tag{FRL-6}
\]

因为这些差值使 `(FRL-5)` 的某个因子为零，不能使用普通乘积界。

## 2. 点态乘积界

若 `s` 非共振且 `nu_R^{(5)}(s;r)>=L`，则

\[
\prod_{j=1}^{L}p_{>R,j}
\le
|s(s-r)(s+r)(s-2r)(s+2r)|,
\tag{FRL-7}
\]

其中 `p_{>R,j}` 是大于 `R` 的第 `j` 个素数。

若 `|s|<=B`，则右侧由

\[
M_{5,r}(B)=
\max_{0<|t|\le B}|t(t-r)(t+r)(t-2r)(t+2r)|
\tag{FRL-8}
\]

显式控制。因此只要前 `L` 个大于 `R` 的素数乘积超过 `M_{5,r}(B)`，任何非共振差值都不能有
`L` 次高素复用。

## 3. Rankin 矩界

对任意 `rho>1` 和差值集合 `S`，

\[
\#\{s\in S:\nu_R^{(5)}(s;r)\ge L\}
\le
\rho^{-L}\sum_{s\in S}\rho^{\nu_R^{(5)}(s;r)}.
\tag{FRL-9}
\]

并且

\[
\rho^{\nu_R^{(5)}(s;r)}
\le
\prod_{\substack{q>R\\
q\mid s(s-r)(s+r)(s-2r)(s+2r)}}\rho.
\tag{FRL-10}
\]

这把非共振五射线热门差值完全送入普通大素因子账本。

## 4. 共振升阶

三边尾锚的基集合已经是三点链

\[
T_r=\{d:d,d+r,d+2r\ {\rm pass}\}.
\tag{FRL-11}
\]

因此共振差值的几何含义比二点 `ShiftSmooth` 阶段更强：

1. `s=0` 是同一点，对应能量展开的点负载项。
2. `s=±r` 强制四点链

\[
d,\ d+r,\ d+2r,\ d+3r
\tag{FRL-12}
\]

全部通过。

3. `s=±2r` 强制五点链

\[
d,\ d+r,\ d+2r,\ d+3r,\ d+4r
\tag{FRL-13}
\]

全部通过。

这修正了旧二点阶段的直觉：在三边尾锚中，`s=±r` 不再只是三点链，而是四点链；`s=±2r`
是更强的五点链。

## 5. 热门差值出口

三边跨点相关若需要大量高素复用，则至少发生一项：

```text
nonresonant five-factor Rankin anomaly;
or s=0 point-load anomaly;
or s=±r four-point smooth-chain resonance;
or s=±2r five-point smooth-chain resonance;
or low-mod signed PDEC/SAE.
```

非共振分支由 `(FRL-7)--(FRL-10)` 处理。共振分支必须进入新的多点链筛包络；它们局部禁零类数从
三点链的 `1/3` 型继续升级为 `1/4` 或 `1/5` 型，因此应比当前三点共振更稀疏。

## 6. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_threeedge_five_ray_audit.py
```

样本：

| p | block | shift | chains | diff support | s=r | s=-r | s=2r | s=-2r | max reuse | top pressure |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 362 | 7864 | 189 | 189 | 101 | 101 | 6 | 200 |
| 5003 | 8192 | -36 | 1686 | 16218 | 1209 | 1209 | 916 | 916 | 8 | 2044 |
| 10007 | 16384 | -900 | 3720 | 29162 | 2860 | 2860 | 2302 | 2302 | 8 | 5910 |

样本显示：非共振最大复用仍很小；真正结构压力集中在共振 `s=±r`，其次是 `s=±2r`。这说明下一步
应严写四点/五点链的筛包络，而不是继续在普通 Rankin 账本中消耗。

## 7. 审稿边界

已证明：

```text
nonresonant five-ray hot difference
=> explicit large-prime factor ledger for
   s(s-r)(s+r)(s-2r)(s+2r).
```

尚未证明：

```text
五因子 Rankin 常数足以压住正式反例的非共振跨点相关；
s=±r,±2r 的四点/五点链共振仍需单独排斥。
```

下一步最小硬点是严写多点链局部禁零类数与 Selberg 包络，并把 `s=±r`、`s=±2r` 的压力压回
`PDEC/SAE/ColumnCRT`。
