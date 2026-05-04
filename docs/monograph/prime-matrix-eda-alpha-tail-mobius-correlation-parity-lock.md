# Möbius 二点相关到对称差奇偶锁

**状态：** `alpha_tail_mobius_correlation_parity_lock_reduction_open`

本文继续压缩 `Mobius gate` 中的二点相关项

\[
K(r)=\sum_{d\in A_r}\mu(d)\mu(d+r).
\tag{MPL-1}
\]

核心结构：在平方自由支撑上，公共素因子对 Möbius 乘积没有贡献；真正决定符号的是两边素因子支撑的
对称差奇偶。

## 1. 对称差公式

对 `d,d+r` 都 squarefree 的项，记

\[
S_1(d)=\{q:q|d\},\qquad
S_2(d)=\{q:q|d+r\}.
\tag{MPL-2}
\]

则

\[
\mu(d)\mu(d+r)
=
(-1)^{|S_1(d)|+|S_2(d)|}
=
(-1)^{|S_1(d)\triangle S_2(d)|}.
\tag{MPL-3}
\]

因为公共部分出现两次，奇偶抵消。

## 2. `q|r` 的共同锁

若 `q|r`，则

\[
q|d\quad\Longleftrightarrow\quad q|d+r.
\tag{MPL-4}
\]

所以 `q` 只能出现在公共部分或两边都不出现，不进入对称差。它会提高同符号倾向，这就是
`ShiftSmooth` 层的共同锁。

若 `q\nmid r`，则 `q` 不能同时整除 `d` 与 `d+r`；一旦出现，就必在对称差中贡献一次，
造成符号翻转。

## 3. 正相关的二分

设

\[
E(r)=\#\{d\in A_r:|S_1(d)\triangle S_2(d)|\ {\rm even}\},
\tag{MPL-5}
\]

\[
O(r)=\#\{d\in A_r:|S_1(d)\triangle S_2(d)|\ {\rm odd}\}.
\tag{MPL-6}
\]

则

\[
K(r)=E(r)-O(r).
\tag{MPL-7}
\]

若 `K(r)` 很大，只能发生：

1. **共同锁强。**  
   `r` 含有足够多小素因子，使大量局部状态被锁到公共部分；
2. **对称差奇偶偏置。**  
   在未被 `q|r` 锁住的素因子中，对称差奇偶仍显著偏偶。

第一项进入奇异因子/ColumnCRT 账本；第二项是新的 `Parity-PDEC` 对象。

## 4. 审稿边界

审计脚本：

```text
experiments/prime_matrix_alpha_tail_mobius_corr_audit.py
```

样本：

| p | block | shift | pairs | even | odd | K | avg common | avg exclusive | locked common |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 710 | 456 | 254 | 202 | 0.732394 | 4.287324 | 520 |
| 5003 | 8192 | -36 | 2416 | 1451 | 965 | 486 | 0.764073 | 4.023593 | 1846 |
| 10007 | 16384 | -900 | 5107 | 2963 | 2144 | 819 | 1.027609 | 3.652634 | 5248 |

样本说明：共同锁确实显著，但每对仍有约 `3.6--4.3` 个未锁对称差素因子。当前下一硬点不是
重新估无符号数量，而是证明这些未锁单边素因子的奇偶不能长期偏偶，除非进入 `Parity-PDEC`。

## 5. 审稿边界

已证明：

```text
K(r)>0
=> common-prime lock 或 symmetric-difference parity bias.
```

尚未证明：

```text
共同锁和奇偶偏置不能达到所需强度。
```

下一步最小硬点是给共同锁写出 `prod_{q|r}` 奇异因子上界，并把剩余对称差奇偶偏置送入
`PDEC/ColumnCRT/SAE`。
