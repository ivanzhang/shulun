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

若 `a_s=0` 或 `a_s>=p-g`，该 `q` 行包含完整 `p` 对齐零行；若 `0<a_s<p-g`，它只给出跨相邻两条
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

### 3.1 行号缩放公式的精确版本

用户提出的行号 `nP_{k+1}/P_k` 是正确的高度近似，但不能直接当作下层零行号。严格形式如下。
令上层宽度为 `q`、下层宽度为 `p<q`，上层第 `s` 行区间为

\[
I_s^{(q)}=[(s-1)q+1,sq].
\]

写

\[
(s-1)q=mp+a,\qquad 0\le a<p.
\]

则 `I_s^{(q)}` 完整包含下层 `p` 对齐行，当且仅当

\[
a\ge p-(q-p).
\tag{Scale-Contain}
\]

此时被包含的完整下层行号是

\[
R=m+2=\left\lfloor{(s-1)q\over p}\right\rfloor+2.
\]

若 `(Scale-Contain)` 不成立，`I_s^{(q)}` 只给出一个跨相邻 `p` 行的缝合零窗。此时
`floor(sq/p)` 或 `ceil(sq/p)` 只是该窗口的高度定位，不是可直接调用 `Row(p)` 的对齐行。

因此严证时必须使用“区间是否完整包含下层行”的判据，不能只使用缩放行号。

### 3.2 半宽素数层的复活点

取 `h≈q/2`。上层窗口长度 `q` 确实通常大于 `2h`，所以从纯几何看它可能覆盖两条
`h` 对齐行。但剥到 `h`-筛后，原本在 `q`-筛下为零的窗口会复活所有最小素因子落在
`(h,q]` 的点。即使在 `q^2` 以内，这些点也不只包括 `q^2`：

```text
n 可以是 a*b，其中 h<a<=q，且 b>h；
若 n<=q^2，则 b<q^2/a<2q。
```

所以半宽层的复活点包括 `(h,q]` 中某个素因子乘以一个 `h`-rough 互补因子。它们可以落在
潜在的两条下层行内部，从而打断“连续零行”。

该观察修正了“每次剥离只留下一个平方双粗数”的说法：对相邻一步 `p<q` 且只看
旧 `p`-筛在 `q^2` 内的幸存者，合数例外确实只有 `q^2`；但若一次剥到约 `q/2`
的层级，合数例外变成一个半素/粗互补因子族，不再是单点。

### 3.3 `q^2` 是否落在半宽 CRT 周期内

令

\[
M(h)=\prod_{\ell\le h}\ell.
\]

若要把 `q^2` 之前的半宽层分析放入一个完整 CRT 数值周期，只需验证

\[
q^2<M(h)
\quad\Longleftrightarrow\quad
2\log q<\vartheta(h).
\tag{Period}
\]

这里 `h` 是约 `q/2` 的素数。该条件从 `h=11` 起已经非常宽松，例如
`M(11)=2310>23^2`。此后左侧只按 `log q` 增长，右侧按 `h` 级别增长。有限小例外
`h<11` 可单独检查。因此“`q^2` 落入半宽 CRT 周期”是可证明的技术条件；但它只说明
可以在同一周期内建模，不会自动推出该周期内出现连续零行。

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

进一步新增专项审计：

```text
experiments/prime_matrix_scaled_peeling_halfwidth_audit.py；
docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.json；
docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.md。
```

该审计直接检验“缩放行号”和“半宽素数连续零行”两项推断。对同一批 `5` 个首零行样本：

```text
records_with_prev_scaled_zero = 1；
records_with_two_or_more_half_zero_rows = 0；
max_half_zero_run_length = 0；
top/half_prime 范围为 2.09 到 2.71。
```

即使上层行宽已经超过半宽素数的两倍，半宽层仍没有自动出现连续零行；原因正是半宽层复活点
打断了潜在下层零行。

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

新增 `prime-matrix-rpz-absorption-defect-route.md` 与
`prime-matrix-rpz-absorption-defect-audit.md` 后，上一版硬点
`RPZ-Absorption=>ColumnCRT/TailAnchor/ColumnRadius` 已被写成可审稿的五分支路由：

```text
survivor remains
or TailAnchor load
or ColumnCRT displacement load
or ColumnRadius
or Distributed-RPZ。
```

同批 `5` 个已知首零行样本的半宽复活点总数为 `15`，所有复活点都有上层吸收标签，
但单窗最大标签负载与最大顶层列负载均为 `1`。这排除了“单窗标签集中直接给出
TailAnchor”的最短路线；真实剩余不是吸收路由，而是低负载分散吸收能否长期持续。

新增 `prime-matrix-rpz-sliding-plateau-barrier.md` 后，低负载分散态又被压缩一层：
若漂移族是连续滑动零窗平台，则同一复活源在多个窗口中重复出现。按窗口事件计数时，
这已经触发持久源 `TailAnchor`；若采用源删除账本，则所有未触发 TailAnchor 的复活源
必须压到平台边界层。

当前最小硬点更新为：

```text
RPZ-BCB（boundary-compressed barrier）。
```

具体要证明：

1. 连续滑动平台中，公共核心里的任一复活源都会以平台长度的多重度重复出现；
2. 若平台长度超过 `T_0` 而未触发 `TailAnchor`，复活源只能落在左右 `T_0` 边界层；
3. 这种边界压缩若持续，必须保留公共核心中的 `h`-筛幸存者，或进入 `SAE/PDEC/ColumnCRT`
   端点缺陷。

该命题比“递归推出连续零行”更弱，也比全局证明固定小 `D_0,L_D` 更局部：
只需排除源删除后的边界层逃逸。

新增 `prime-matrix-rpz-boundary-compressed-core-route.md` 与
`prime-matrix-rpz-bcb-core-audit.md` 后，第三项已被严写为 `BCB-Core`：
若无 TailAnchor，则平台中心

```text
J_{T0}=[L+A+T0,R+B-T0]
```

必为半宽 `h`-筛零区间。样本中该中心区间的 `11` 个幸存者全是尾锚核心源；
条件排除 TailAnchor 后，`5/5` 个中心区间干净且含完整半宽行。下一硬点因此更新为：

```text
BCB-Grid/Endpoint exclusion。
```

也就是证明正式平台的 `J_{T0}` 必含完整 `h` 对齐行，或端点缝合相位进入
`SAE/PDEC/ColumnCRT`。

新增 `prime-matrix-rpz-bcb-grid-endpoint-criterion.md` 后，这个“含完整行”问题已精确化：
对 `J=[u,v]`，令 `N=v-u+1` 与 `\delta_h(u)=(1-u) mod h`。完整包含 `h` 对齐行当且仅当
`N>=\delta_h(u)+h`；若失败，失败量就是端点 seam 缺口。样本中 `5/5` 满足该判据，
且 `4/5` 由纯长度条件自动闭合。下一硬点更新为端点相位持续失败的排斥：

```text
BCB-Endpoint persistence exclusion。
```

新增 `prime-matrix-rpz-bcb-endpoint-persistence-route.md` 与
`prime-matrix-rpz-bcb-endpoint-phase-ledger.md` 后，端点持久失败已不再是独立硬点：
低负载进入 `SAE`，高负载进入 `PDEC/ColumnCRT`。有限样本实际端点失败为 `0`，
可能失败相位只有 `2` 个。下一步需要在两条路线中择一：

```text
1. 攻 SAE/PDEC/ColumnCRT certificate closure；
2. 沿 BCB 得到的下层 h-筛零行继续做递归下降。
```

新增 `prime-matrix-rpz-dual-track-closure-route.md` 与
`prime-matrix-rpz-lower-zero-descent-audit.md` 后，两条路线已并行化：证书路线给出
`RPZ-SAE/RPZ-PDEC/RPZ-ColumnCRT` 三类接口；递归路线显示样本中的 `6` 条条件下层零行
全部下降到 `p=2` 直接矛盾，阻断节点为 `0`。当前剩余硬点更新为：

```text
LowerDescent-Grid persistence
and RPZ-SAE/PDEC/ColumnCRT certificate materialization。
```

新增 `prime-matrix-rpz-lower-descent-obstruction-ledger.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py` 后，上述剩余进一步精确：
对每个相邻下降 `p -> r`，阻断只依赖行号模 `P(r)`，并被分成 `grid_fail` 与
`puncture_block` 两类有限相位。本批实际下降节点 `20` 个、全部 `success`，实际阻断为 `0`。
因此递归剥离主线现在有两个并行最小义务：

```text
1. 证明正式反例下降路径始终落在 success 相位；
2. 若落入 grid_fail/puncture_block，则把该相位送入 RPZ-SAE/PDEC/ColumnCRT 证书接口。
```

新增 `prime-matrix-rpz-certificate-materialization-interface.md` 给出上述接口的可审稿填表格式；
它不宣称这些出口已被排除。

## 8. 相邻壳层单点下降路线更新

新增：

```text
experiments/prime_matrix_adjacent_shell_descent_ledger.py；
docs/monograph/prime-matrix-adjacent-shell-descent-ledger.md/json；
docs/monograph/prime-matrix-adjacent-shell-recursive-descent-route.md。
```

该更新把用户提出的“每次降阶只有一个新双粗点”精确化为相邻壳层单点引理：

```text
p<q 相邻；
n<q^2 且旧 p-筛幸存；
=> n 是素数；
n<=q^2 的唯一合数旧筛幸存者是 q^2。
```

因此 `q^2` 内的非第一行 `q` 零行确实先降为旧 `p`-筛零窗口，最后一行至多带 `q^2`
端点穿孔。随后写 `(s-1)q=mp+a,g=q-p`，得到无损二分：

```text
a=0 or a>=p-g  => 完整 p 对齐零行；
0<a<p-g        => seam zero window，两个 guard 长度为 a 与 p-g-a。
```

这把递归路线的实质缺口从“零行是否自动降阶”压缩为：

```text
SeamGuard-Elimination:
seam guards 不能无代价吸收 Row(p) 所需幸存者；
若持续吸收，则进入 SAE/PDEC/ColumnCRT。
```

所以旧结论仍成立：不能直接从零行推出连续下层零行。但现在有更强的正向路线：
若 `SeamGuard-Elimination` 与 `SAE/PDEC/ColumnCRT` 出口排斥闭合，则相邻壳层递归下降
会把任意 `q^2` 内零行降到 `p=2` 矛盾。
