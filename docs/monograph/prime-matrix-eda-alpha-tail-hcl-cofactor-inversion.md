# HCL 高核心负载的互补因子反演

**状态：** `alpha_tail_hcl_cofactor_inversion_reduction_open`

本文继续压缩 `HDL-CoreLoad`。核心观察：当高 dyadic 块满足 `d>p-1` 时，每个高低素核心
`d|p^2+k` 都强制产生一个小互补因子

\[
m={p^2+k\over d}<p+2.
\]

因此高核心异常不是自由的高维覆盖；它必须投影到一条很短的低互补因子带上。

## 1. 互补因子反演

固定

\[
H=p-1,\qquad y=\lfloor0.9p\rfloor,\qquad n_k=p^2+k.
\tag{CFI-1}
\]

令 `I=(B,2B]` 且 `B>H`。对 `1<=k<=H` 定义

\[
\mathcal M_I^\pm(k)=
\left\{
m:\;
m\mid n_k,\;
{n_k\over m}\in I,\;
{n_k\over m}\mid G_y(k),\;
\mu\!\left({n_k\over m}\right)=\pm1
\right\}.
\tag{CFI-2}
\]

则有精确恒等式

\[
C_I^\pm(k)=|\mathcal M_I^\pm(k)|.
\tag{CFI-3}
\]

**证明。**  
`C_I^\pm(k)` 计数的是 `d in I`、`d|G_y(k)`、`mu(d)=pm1` 的 squarefree 除数。
令 `m=n_k/d`，得到 `(CFI-2)` 中的互补因子。反过来，任意 `(CFI-2)` 中的 `m` 给出
`d=n_k/m`，且满足 `d in I`、`d|G_y(k)`、`mu(d)=pm1`。二者互逆。证毕。

## 2. 互补因子带

由 `d in (B,2B]` 得

\[
{p^2+1\over 2B}<m<{p^2+H\over B}.
\tag{CFI-4}
\]

特别地，若 `B>H`，则

\[
m<{p^2+p-1\over p-1}=p+2+{1\over p-1}.
\tag{CFI-5}
\]

所以所有高块 core 命中都被压到 `m<=p+2` 的低互补因子带；当 `B=\lambda p` 时，互补因子尺度约为
`p/lambda`。

## 3. CofactorLoad 恒等式

定义互补因子负载

\[
L_I^\pm(m)=
\#\{1\le k\le H:m\in\mathcal M_I^\pm(k)\}.
\tag{CFI-6}
\]

由 `(CFI-3)` 得

\[
\sum_{k=1}^H C_I^\pm(k)=\sum_m L_I^\pm(m).
\tag{CFI-7}
\]

因此 `HCL-8` 的奇核心过剩等价于

\[
\sum_m L_I^-(m)\ge H R_I^-+{\tau\over2}.
\tag{CFI-8}
\]

`HCL-7` 的偶核心亏损则等价于正符号互补因子负载低于 harmonic 模型。

## 4. 单个互补因子的容量

固定 `m`。若 `m in \mathcal M_I^\pm(k)`，则

\[
p^2+k\equiv0\pmod m.
\tag{CFI-9}
\]

所以 `k` 属于模 `m` 的一个固定剩余类，进而

\[
L_I^\pm(m)\le 1+\left\lfloor {H\over m}\right\rfloor.
\tag{CFI-10}
\]

此外还必须满足 `d=(p^2+k)/m in I`，这是对同一剩余类的短截断；因此 `(CFI-10)` 是保守上界。

## 5. 新的二分出口

由 `(CFI-8)` 与 `(CFI-10)`，奇核心过剩必须进入以下二分之一。

1. **Cofactor-anchor。**  
   存在小互补因子 `m` 使 `L_I^-(m)` 接近上界 `1+floor(H/m)`；这等价于同一低模剩余类
   在短截断内高密度命中，进入 `ColumnCRT/PDEC`。
2. **Distributed-cofactor load。**  
   过剩分散在许多 `m` 上。由于每个 `m` 的命中被 `(CFI-10)` 限制，这会产生大规模
   互补因子带覆盖预算，进入 `Distributed-CoreLoad`。

偶核心亏损不需要再经过 cofactor anchor；它本身已经是正符号端点命中系统性不足，直接保留为
`PDEC` 出口。

## 6. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_cofactor_audit.py
```

用法：

```text
python3 experiments/prime_matrix_alpha_tail_cofactor_audit.py --selected 997:4096,5003:8192 --format table
```

该脚本对每个 `p:B` 输出正负符号命中相对 harmonic 模型的差、最大列负载、最大互补因子负载与
支撑规模。它用于定位反例若存在时必须触发的 cofactor-anchor 或 distributed-cofactor 出口；
有限样本不作为全局证明输入。

样本摘要：

| p | block | high | plus gap | minus gap | max minus column | max minus m | minus column support | minus m support |
|---:|---:|:---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | true | -15.565296 | 2.698051 | 4 | 5 | 90 | 85 |
| 5003 | 8192 | true | 1.706891 | 15.047993 | 7 | 3 | 492 | 623 |
| 10007 | 16384 | true | -17.086838 | 62.797308 | 10 | 3 | 1050 | 1273 |

这组审计显示：在这些高块样本中，奇核心过剩主要表现为 `minus m support` 很大、单个互补因子
负载很低。这支持下一步优先攻击 `Distributed-cofactor load`，而不是先假设存在大 cofactor-anchor。

## 7. 审稿边界

已证明：

```text
高块 HCL 异常
=> 低互补因子带上的 CofactorLoad 异常。
```

尚未证明：

```text
Cofactor-anchor 或 Distributed-cofactor load 不可能。
```

下一步最小硬点是把 `(CFI-10)` 与互补因子带长度结合，给出显式容量不等式；失败时产生
`ColumnCRT/PDEC/SAE` 证书。
