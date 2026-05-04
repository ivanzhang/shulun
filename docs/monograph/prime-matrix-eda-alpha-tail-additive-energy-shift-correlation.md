# 加法能量异常到位移光滑相关

**状态：** `alpha_tail_additive_energy_shift_correlation_reduction_open`

本文继续压缩 `Bohr-cap=>additive energy` 分支。加法能量不是终点；它等价于低素平方自由集合在
许多位移 `r` 上同时出现 `d` 与 `d+r`。这把硬点变成一族位移双光滑相关不等式。

## 1. 差值相关

令

\[
D\subset(B,2B]
\tag{ASC-1}
\]

为固定符号的低素 squarefree 集合。定义

\[
C_D(r)=\#\{d\in D:d+r\in D\}.
\tag{ASC-2}
\]

则

\[
E_+(D)=\sum_r C_D(r)^2.
\tag{ASC-3}
\]

这是加法能量的精确定义展开。

## 2. 热门位移推出

若

\[
E_+(D)\ge E_0,
\tag{ASC-4}
\]

则至少发生一项：

1. **单热门位移。**

\[
\max_{r\ne0}C_D(r)\ge \Lambda;
\tag{ASC-5}
\]

2. **分散位移能量。**

\[
\sum_{\substack{r\ne0\\ C_D(r)<\Lambda}}C_D(r)^2
\ge E_0-|D|^2-\Lambda^2.
\tag{ASC-6}
\]

这里 `r=0` 的对角贡献为 `|D|^2`。这是纯粹的阈值二分。

## 3. 单热门位移的双光滑相关

固定 `r`。`C_D(r)` 计数的是

\[
d,\ d+r\in(B,2B],
\tag{ASC-7}
\]

且二者都满足：

1. squarefree；
2. 所有素因子 `<=y=floor(0.9p)`；
3. Möbius 符号相同。

因此若 `(ASC-5)` 过大，就得到位移双光滑相关异常：

```text
ShiftSmooth(r):
区间 (B,2B] 内过多 n 使 n 与 n+r 同为 y-smooth squarefree 且同符号。
```

对任意素数 `ell|r`，若 `ell<=y`，则 `n` 与 `n+r` 可同时避开 `ell` 的零类约束退化为一次筛；
若 `ell\nmid r`，二者同时非零需要避开两个剩余类。这正是用户指出的“二禁降一禁”结构在
加法能量层的对应物。

## 4. 分散位移能量出口

若没有单个热门位移，则 `(ASC-6)` 表示许多位移同时有中等强度的双光滑相关。把这些位移按
`gcd(r,M_y)` 与大小 dyadic 分组，必有一组产生固定奇异因子账本异常：

```text
Distributed ShiftSmooth:
许多同 gcd 类型的 r 上，ShiftSmooth(r) 总量超过二禁/一禁筛模型。
```

持续出现时进入 `PDEC/ColumnCRT`；孤立出现时进入 `SAE`。

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_additive_energy_audit.py
```

用法：

```text
python3 experiments/prime_matrix_alpha_tail_additive_energy_audit.py --selected '997:4096:-,5003:8192:-' --format table
```

它输出 `D` 的大小、差值支撑、加法能量、相对区间随机模型的比值与最热门非零位移。

样本：

| p | block | sign | d count | diff support | energy | energy/model | max diff | max count |
|---:|---:|:---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | - | 697 | 8083 | 45140885 | 1.540872 | -36 | 249 |
| 5003 | 8192 | - | 1645 | 16355 | 679085497 | 1.510286 | -36 | 641 |
| 10007 | 16384 | - | 3338 | 32731 | 5730623078 | 1.508103 | -900 | 1278 |

这些样本显示能量没有爆炸，但确有稳定的热门位移。下一步应优先证明 `ShiftSmooth(r)` 的
二禁/一禁筛上界，而不是继续抽象处理总能量。

## 6. 审稿边界

已证明：

```text
AdditiveEnergy anomaly
=> Single ShiftSmooth hotspot 或 Distributed ShiftSmooth anomaly.
```

尚未证明：

```text
ShiftSmooth hotspot / distributed anomaly 不可能。
```

下一步最小硬点是对 `ShiftSmooth(r)` 写出利用 `q|r` 时二禁降一禁的筛上界，并把失败路由到
`PDEC/ColumnCRT/SAE`。
