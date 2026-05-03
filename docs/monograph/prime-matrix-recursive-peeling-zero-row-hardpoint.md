# Prime Matrix 零行递归剥离硬点

**状态：** `recursive_peeling_reduces_to_punctured_seam_windows_not_closed`

本文处理新的递归剥离设想：

```text
若 q=p_{k+1} 方阵中存在零行，
是否可反推 p=p_k 阶段在 q^2 范围内已有零行；
再递归下去，最终推出某个 CRT 周期中出现连续零行，
从而与零行镜像刚性或分布刚性矛盾？
```

结论是：该思路有一个严格可用的“层剥离恒等式”，但不能直接推出连续零行。真正递归对象不是
零行，而是带少数复活点的 `punctured zero window`。若要把它变成证明，需要新增一个
“复活点不能被缝合稳定吸收，或吸收必进入 `PDEC/TailAnchor/ColumnCRT`”的定理。

## 1. 层剥离恒等式

令 `r<p` 为相邻素数，记

\[
P_r=\prod_{\ell\le r}\ell,\qquad P_p=pP_r.
\]

设区间 `I` 在 `p`-筛下为零：

\[
\mathcal R_p(I)=\{n\in I:(n,P_p)=1,\ n>1\}=\varnothing.
\]

则在剥去顶层素数 `p` 后，`r`-筛幸存者满足精确包含

\[
\mathcal R_r(I)
\subseteq
\{n\in I:p\mid n,\ (n/p,P_r)=1\}.
\tag{RPZ-1}
\]

**证明。**
若 `n∈\mathcal R_r(I)`，则 `n` 没有不超过 `r` 的素因子。又 `\mathcal R_p(I)=\varnothing`，
所以 `n` 必有某个不超过 `p` 的素因子。由于 `r<p` 相邻，该素因子只能是 `p`。
再除去 `p` 后，若 `n/p` 有不超过 `r` 的素因子，则 `n` 也有，矛盾。证毕。

因此递归剥离不是“零行变零行”，而是：

```text
p-零窗
=> r-筛下至多若干 p-倍数复活。
```

若 `I` 的长度小于 `2p`，例如下一素数行长度 `q<2p`，则第一层复活点最多两个；若
`I` 是宽 `p` 的对齐行，则第一层复活点最多一个。

## 2. q 零行的严格反推边界

由 `prime-matrix-reverse-zero-row-dichotomy.md` 已知：若 `q=p+g`，且 `2<=s<q`
的 `q` 行是零行，则整个 `q` 行已是旧 `p`-筛零窗。令

\[
a_s=(s-1)q\bmod p.
\]

若 `a_s>=p-g`，该 `q` 行包含完整 `p` 对齐零行；若 `a_s<p-g`，它只给出跨相邻两条
`p` 行的后缀/前缀缝合零窗。审计显示 `p<=2000` 的核心区中，直接包含完整 `p`
行的比例只有约 `0.00616`，缝合支约 `0.99384`。

所以用户提出的反推路线在少数相位直接成立；主支必须处理缝合零窗和 RPZ-1 的复活点。

## 3. 为什么不能自动推出连续零行

若递归剥离要推出某个下层 `r` 网格中出现连续两条零行，至少需要三项额外事实：

1. 当前零窗长度必须覆盖两条完整 `r` 对齐行；
2. RPZ-1 产生的复活点不能落入这些完整行内；
3. 跨层缝合边界不能把零窗拆成只有后缀/前缀、没有完整对齐行的形态。

这三项都不是由“上层存在零行”自动推出。特别是第一层剥离时，`q<2p`，只可能覆盖极少数
完整 `p` 行；继续向下剥离虽然窗口相对更长，但复活点数量也累积增加。层剥离的真实状态是

\[
\mathcal R_{p_j}(I)
=
\bigsqcup_{p_j<\ell\le p_k}
\{n\in I:P^-(n)=\ell,\ (n/\ell,P_{p_j})=1\},
\]

即按最小被剥离素因子分层的复活点集合，而不是一个仍然为空的窗口。

## 4. 实验审计

新增脚本与证书：

```text
experiments/prime_matrix_recursive_peeling_zero_row_audit.py；
docs/monograph/prime-matrix-recursive-peeling-zero-row-audit.json；
docs/monograph/prime-matrix-recursive-peeling-zero-row-audit.md。
```

输入为 `prime-matrix-zero-row-crt-audit.json` 中已经发现的 `5` 个首个 `p` 对齐零行。审计结果：

```text
zero_row_records = 5；
one_step_zero_after_peeling = 2；
one_step_contains_aligned_zero_row = 1；
records_with_consecutive_zero_pair = 0。
```

逐例第一层剥离：

| p | zero row | one-step level | survivors after peeling | contained aligned zero rows |
|---:|---:|---:|---:|---|
| 13 | 169 | 11 | 1 | `[]` |
| 17 | 1211 | 13 | 0 | `[]` |
| 19 | 3659 | 17 | 1 | `[]` |
| 23 | 59 | 19 | 1 | `[]` |
| 29 | 5210 | 23 | 0 | `[6569]` |

这说明两点：

```text
1. 上层零行有时剥离后仍为空，但不保证包含完整下层对齐零行；
2. 即使包含下层对齐零行，也未自动产生连续零行。
```

因此“递归剥离自动推出连续零行并与镜像刚性矛盾”目前不能作为证明出口。

## 5. 可保留的突破方向

递归剥离仍然有价值，因为 RPZ-1 给出强容量：

```text
第一层复活点 <= 2；
宽 p 对齐行第一层复活点 <= 1；
多层复活点按最小被剥离素因子分层，具有互斥和同余稀疏性。
```

这可转化为新的硬点：

**RPZ-Puncture Rigidity.**
若 `q` 网格零行存在，则反推得到的缝合零窗在逐层剥离中只能产生低复杂度复活点集合。
若这些复活点能被继续缝合吸收，则其最小被剥离素因子层必须在低模端点、尾锚或列位移余类中
形成集中缺陷，从而进入

```text
PDEC / TailAnchor / ColumnCRT / SAE。
```

换言之，递归剥离的正确总攻链条应写为：

```text
q-grid zero row
=> old p-sieve zero seam
=> punctured recursive zero window with <=2 first-layer resurrected points
=> either survivor remains, or absorption causes named defect
=> PDEC/TailAnchor/ColumnCRT/SAE contradiction.
```

## 6. 与全局阈值的关系

这一路线也给 `ColumnRadius/ColumnCRT` 全局阈值一个更清晰的目标。与其直接证明所有列见证半径
有绝对小常数，不如证明：

```text
若递归剥离产生的 <=2 第一层复活点被完全吸收，
则吸收标签必须在某个低模/尾模位移余类上超过 L_D，
或使列见证半径超过 D_0；
于是进入 ColumnCRT 或 ColumnRadius 出口。
```

有限证书已给出 `p<=1000` 紧行样本中 `D_col<=81`、位移余类负载 `<=2`。全局化时，候选阈值不应先追求
固定 `81`，而应先证明更稳健的分支式阈值：

\[
\text{puncture absorption}
\Longrightarrow
R_{\ell,a}(g)>L_D(q)\ \text{or}\ R_D(g)>0.
\]

这把全局阈值从“每列附近必有素数”的强命题，降为“反例吸收复活点时必暴露列/CRT 缺陷”的条件命题。

## 7. 下一步最小硬点

当前最小硬点更新为：

```text
RPZ-Absorption => ColumnCRT/TailAnchor。
```

具体要证明：

1. 第一层最多两个复活点若被缝合窗口消除，则消除标签不能在所有相邻漂移窗口中分散；
2. 若分散，则某个邻近窗口保留旧筛幸存者，反例失败；
3. 若集中，则进入 `ColumnCRT` 位移余类负载或 `TailAnchor` 标签集中；
4. 若需要远距离列见证补偿，则进入 `ColumnRadius`。

该命题比“递归推出连续零行”更弱、更接近已建好的 H4-PDEC 出口账本，也更适合作为下一步全局阈值攻坚目标。
