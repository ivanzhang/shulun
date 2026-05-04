# TailParity 的首个高素因子锚点展开

**状态：** `alpha_tail_tailparity_first_anchor_reduction_open`

本文处理 `Parity-PDEC` 分解后的高尾项

\[
\sum_{d\in A_r}\Psi_{R,r}(d)(\Theta_{R,y,r}(d)-1).
\tag{TPA-1}
\]

核心结论：高尾奇偶偏置不是黑箱；它可精确展开为“首个未锁高素因子”的单边锚点和。

## 1. 有序高素因子

令

\[
R<q_1<q_2<\cdots<q_s\le y
\tag{TPA-2}
\]

为高尾素数。写

\[
\theta_j(d)=\psi_{q_j,r}(d).
\tag{TPA-3}
\]

则

\[
\Theta_{R,y,r}(d)=\prod_{j=1}^s\theta_j(d).
\tag{TPA-4}
\]

## 2. Telescoping 恒等式

有精确恒等式

\[
\Theta_{R,y,r}(d)-1
=
\sum_{j=1}^s
(\theta_j(d)-1)\prod_{i<j}\theta_i(d).
\tag{TPA-5}
\]

**证明。**  
令 `P_j=prod_{i<=j}theta_i`，`P_0=1`。则
`P_s-1=sum_j(P_j-P_{j-1})=sum_j(theta_j-1)P_{j-1}`。证毕。

## 3. 首个高素因子锚点

若 `q_j|r`，则 `theta_j(d)=1`，不贡献。若 `q_j∤r`，则

\[
\theta_j(d)-1=
\begin{cases}
-2,& d\equiv0\ {\rm or}\ -r\pmod {q_j},\\
0,& \text{otherwise}.
\end{cases}
\tag{TPA-6}
\]

因此高尾项精确等于

\[
-2\sum_{\substack{R<q\le y\\ q\nmid r}}
\sum_{\substack{d\in A_r\\ d\equiv0\ {\rm or}\ -r\pmod q}}
\Psi_{R,r}(d)\prod_{R<\ell<q}\psi_{\ell,r}(d).
\tag{TPA-7}
\]

这就是首个高素因子锚点展开：每个贡献都绑定到一个未锁高素数 `q` 的单边零类。

## 4. 大 TailParity 的二分

若 `(TPA-1)` 的绝对值达到 `T_0`，则至少发生一项：

1. **高素锚点集中。**  
   存在 `q`，其单边零类贡献达到 `T_0 / N_tail` 量级，其中 `N_tail=pi(y)-pi(R)-#{q|r}`；
2. **分散高尾能量。**  
   许多 `q` 的锚点贡献同号累积，形成 tail-anchor 能量异常。

第一项进入 `ColumnCRT/SAE`；第二项进入 `TailParity-Rankin/PDEC`。

## 5. 当前最小硬点

`TailParity` 已被压成：

```text
未锁高素数 q 的单边零类锚点贡献
```

下一步需要证明这些锚点不能同号累积到所需尺度；失败时必须输出具体 `q`、剩余类
`0` 或 `-r mod q`、以及低模符号函数上的 `ColumnCRT/PDEC/SAE` 证书。

## 6. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailparity_anchor_audit.py
```

用法：

```text
python3 experiments/prime_matrix_alpha_tail_tailparity_anchor_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
```

脚本逐项核验 `(TPA-5)` 的 telescoping 恒等式，并输出总高尾贡献与绝对值最大的高素锚点。

样本：

| p | block | shift | R | pairs | tail | top q | top value |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 31 | 710 | 82 | 37 | 42 |
| 5003 | 8192 | -36 | 31 | 2416 | 402 | 61 | 70 |
| 10007 | 16384 | -900 | 31 | 5107 | 680 | 73 | 130 |

样本显示：高尾贡献不是单个 `q` 完全承担，而是多个高素锚点同号累积。下一步应攻击
`distributed tail-anchor energy`，或证明这些锚点贡献在低模符号下必须相互抵消。
