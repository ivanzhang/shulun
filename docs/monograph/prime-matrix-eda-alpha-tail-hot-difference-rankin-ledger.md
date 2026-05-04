# 热门差值的 Rankin 账本

**状态：** `alpha_tail_hot_difference_rankin_ledger_reduction_open`

本文继续攻击跨点锚点图的热门差值分支。固定差值

\[
s=d_1-d_2\ne0
\]

能被高素锚点 `q` 复用，只可能因为

\[
q\mid s(s-r)(s+r).
\tag{HDR-1}
\]

本文只处理非共振差值

\[
s\notin\{0,r,-r\}.
\tag{HDR-1a}
\]

当 `s=0` 是对角项，已属于点负载；当 `s=±r` 时 `(HDR-1)` 中有一个因子为 `0`，任何高素数
都形式上满足同余。这是单独的共振分支，不能用 Rankin 乘积界处理。

这把“许多高素锚点同用一个差值”的可能性压成一个普通整数的大素因子计数问题。

## 1. 点态乘积界

定义

\[
\nu_R(s;r)=
\#\{q:R<q\le y,\ q\nmid r,\ q\mid s(s-r)(s+r)\}.
\tag{HDR-2}
\]

若 `nu_R(s;r)>=L`，则

\[
\prod_{j=1}^{L}p_{>R,j}
\le |s(s-r)(s+r)|,
\tag{HDR-3}
\]

其中 `p_{>R,j}` 是大于 `R` 的第 `j` 个素数。

因此只要左侧超过

\[
M_r(B)=\max_{0<|s|\le B}|s(s-r)(s+r)|,
\tag{HDR-4}
\]

就不可能有 `nu_R(s;r)>=L`。这给出完全显式的点态最大复用数。

## 2. Rankin 矩界

对任意 `rho>1`，

\[
\mathbf 1_{\nu_R(s;r)\ge L}
\le \rho^{-L}\rho^{\nu_R(s;r)}.
\tag{HDR-5}
\]

所以任意差值集合 `S` 中的高复用差值数满足

\[
\#\{s\in S:\nu_R(s;r)\ge L\}
\le
\rho^{-L}
\sum_{s\in S}\rho^{\nu_R(s;r)}.
\tag{HDR-6}
\]

而

\[
\rho^{\nu_R(s;r)}
\le
\prod_{\substack{q>R\\ q\mid s(s-r)(s+r)}}\rho.
\tag{HDR-7}
\]

这就是 Rankin/Tail 账本接口。

## 3. 热门差值二分

若跨点相关需要大量高素复用，则二分为：

1. **高复用差值存在。**  
   某个 `s` 违反点态乘积界或接近 Rankin 上界，输出 `s` 与高素因子列表作为 `ColumnCRT` 证书；
2. **低复用分散。**  
   每个 `s` 的复用数都小，跨点相关不能靠同一个差值放大；剩余只能来自低模符号边相关，
   进入 `PDEC`。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_hot_difference_audit.py
```

用法：

```text
python3 experiments/prime_matrix_alpha_tail_hot_difference_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
```

脚本输出 squarefree 支撑中的差值、可复用高素锚点数和最高压力差值。审计必须分开输出
`s=±r` 共振差值；这些不进入 `(HDR-3)`。

样本：

| p | block | shift | pairs | diff support | s=r | s=-r | hot diffs | max nonres reuse | top nonres s | top pressure |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 710 | 8074 | 362 | 362 | 7356 | 5 | -472 | 423 |
| 5003 | 8192 | -36 | 2416 | 16294 | 1686 | 1686 | 15700 | 5 | -488 | 2751 |
| 10007 | 16384 | -900 | 5107 | 30962 | 3720 | 3720 | 30120 | 6 | -1591 | 6885 |

样本显示：真正最高压力来自共振差值 `s=±r`，非共振差值最大复用只有 `3--5`。因此
Rankin 账本基本压住非共振分支，下一步必须单独攻击 `s=±r` 共振链。

## 5. 审稿边界

已证明：

```text
nonresonant hot difference branch
=> explicit large-prime factor ledger for s(s-r)(s+r).
```

尚未证明：

```text
该 ledger 的常数足以压住正式反例所需非共振跨点相关；
共振差值 s=±r 另需三点链分析。
```

下一步最小硬点是把 `(HDR-3)/(HDR-6)` 与跨点边数上界结合，给出显式 `U_hot<L_needed`；
失败则输出具体差值 `s` 和高素锚点列表。
