# CRT 零行解集分布与边界帽审计

**状态：** `crt_solution_geometry_supports_edge_cap_reduction_not_edge_proof`

零行是列覆盖集合交的 CRT 解，镜像来自取负映射，严格成立。实验中边界帽 rows 2..P 无零行，且边界幸存者自动为素数；但中区粗合数密集不能推出边界帽非零，因为前者是数值层粗合数画像，后者是 CRT 筛层边界最小代表下界。

## 1. CRT 方程组

固定奇素数 `P`，令 `N=prod_{ell<P} ell`。第 `r` 行第 `c` 列的数为

\[
n_{r,c}=(r-1)P+c,\qquad 1\le c<P.
\]

列 `c` 被根基素数 `ell<P` 覆盖当且仅当

\[
r\equiv 1-cP^{-1}\pmod {ell}.
\]

因此零行集合是

\[
Z_P=\bigcap_{1\le c<P}\bigcup_{ell<P}\{r:r\equiv 1-cP^{-1}\pmod {ell}\}.
\]

幸存列集合是

\[
R_P(r)=\{1\le c<P:(n_{r,c},N)=1\}.
\]

取负映射给出精确镜像

\[
R_P(N-r+1)=\{P-c:c\in R_P(r)\}.
\]

所以 `r` 为零行当且仅当 `N-r+1` 为零行。

## 2. 分布审计表

| P | N | zero count | first zero | first/P | edge zeros | zero deciles | front thinnest | middle thinnest | mirror ok |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 13 | 2310 | 4 | 169 | 13.000 | 0 | `[1, 0, 0, 1, 0, 0, 1, 0, 0, 1]` | row 10, holes 1, vals `[127]` | row 1152, holes 1 | True |
| 17 | 30030 | 28 | 1211 | 71.235 | 0 | `[3, 2, 2, 4, 3, 3, 4, 2, 2, 3]` | row 13, holes 1, vals `[211]` | row 15014, holes 1 | True |
| 19 | 510510 | 496 | 3659 | 192.579 | 0 | `[61, 52, 45, 44, 46, 46, 44, 45, 52, 61]` | row 16, holes 1, vals `[293]` | row 255250, holes 1 | True |
| 23 | 9699690 | 3456 | 59 | 2.565 | 0 | `[361, 337, 344, 344, 342, 342, 344, 344, 337, 361]` | row 15, holes 2, vals `[331, 337]` | row 4849844, holes 1 | True |

## 3. 可严格使用的结论

- **镜像刚性：** 零行集合关于 `r -> N-r+1` 严格对称；这给出首端/尾端同时异常的两端帽约束。
- **边界自动素数：** 若 `2<=r<=P` 且 `c` 幸存，则 `n_{r,c}<P^2`，没有 `<P` 素因子，所以 `n_{r,c}` 必为素数。
- **边界帽等价：** 前 `P` 行无零行等价于每个 `[xP+1,xP+P-1]`, `1<=x<P`, 含素数。
- **证书最小代表：** 任意零行证书给出一个 CRT 代表；边界排除等价于证明所有完整覆盖证书的最小正代表 `>=P`。

## 4. 不能直接使用的跳步

- 中区幸存者可能是素数或 `P`-rough 合数；它们密集不是 CRT 筛层单调势能。
- 零行镜像不是短周期；它不推出零行需以 `r`、`2r` 或 `2r-1` 为复现周期。
- 因此“中区两侧光滑合数密集，所以边界无零行”目前只是启发，不是证明。

## 5. 下一步硬攻形式

要把本路线变成边界零行不存在证明，需要补充一个独立势函数：

\[
\Phi_P(R_P(r))\ge 1\quad (2\le r\le P),\qquad \Phi_P(\varnothing)=0.
\]

它必须只依赖 CRT 覆盖证书、镜像两端帽、残洞迁移和低模投影，而不能把目标结论本身放入定义。可攻版本是：若某个边界行满足 `R_P(r)=empty`，则其镜像尾端也为空；两端证书的最小标签分配合并后产生固定小模投影缺陷或残洞迁移势能为负，从而矛盾。

## 6. 零行证书样本

### P=13
- row=169 distinct_labels=5 least_label_hist=`{2: 6, 3: 2, 5: 2, 7: 1, 11: 1}`
- row=702 distinct_labels=5 least_label_hist=`{2: 6, 3: 2, 5: 2, 7: 1, 11: 1}`
- row=1609 distinct_labels=5 least_label_hist=`{2: 6, 3: 2, 5: 2, 7: 1, 11: 1}`
- row=2142 distinct_labels=5 least_label_hist=`{2: 6, 3: 2, 5: 2, 7: 1, 11: 1}`
- gap_stats=`{'min_gap': 337, 'max_gap': 907, 'small_gaps': [337]}`; avg_survivor_count_by_decile=`[2.4935, 2.4935, 2.4935, 2.4935, 2.4935, 2.4935, 2.4935, 2.4935, 2.4935, 2.4935]`

### P=17
- row=1211 distinct_labels=6 least_label_hist=`{2: 8, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1}`
- row=1638 distinct_labels=6 least_label_hist=`{2: 8, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1}`
- row=2323 distinct_labels=6 least_label_hist=`{2: 8, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1}`
- row=28820 distinct_labels=6 least_label_hist=`{2: 8, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1}`
- gap_stats=`{'min_gap': 217, 'max_gap': 2421, 'small_gaps': [217, 217, 427, 427, 427, 427, 445, 445, 655, 685, 685, 872, 872, 875, 875, 1320, 1320, 1341, 1341, 1341]}`; avg_survivor_count_by_decile=`[3.0689, 3.0689, 3.0689, 3.0689, 3.0689, 3.0689, 3.0689, 3.0689, 3.0689, 3.0689]`

### P=19
- row=3659 distinct_labels=6 least_label_hist=`{2: 9, 3: 3, 5: 2, 7: 2, 11: 1, 13: 1}`
- row=4101 distinct_labels=6 least_label_hist=`{2: 9, 3: 3, 5: 2, 7: 2, 13: 1, 17: 1}`
- row=4731 distinct_labels=6 least_label_hist=`{2: 9, 3: 3, 5: 2, 7: 2, 11: 1, 17: 1}`
- row=506852 distinct_labels=6 least_label_hist=`{2: 9, 3: 3, 5: 2, 7: 2, 11: 1, 13: 1}`
- gap_stats=`{'min_gap': 5, 'max_gap': 7317, 'small_gaps': [5, 5, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 22, 22, 22, 22, 27, 27, 27, 27]}`; avg_survivor_count_by_decile=`[3.2495, 3.2495, 3.2495, 3.2495, 3.2495, 3.2495, 3.2495, 3.2495, 3.2495, 3.2495]`

### P=23
- row=59 distinct_labels=7 least_label_hist=`{2: 11, 3: 4, 5: 2, 7: 2, 13: 1, 17: 1, 19: 1}`
- row=2612 distinct_labels=8 least_label_hist=`{2: 11, 3: 4, 5: 2, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}`
- row=5539 distinct_labels=7 least_label_hist=`{2: 11, 3: 4, 5: 2, 7: 2, 11: 1, 13: 1, 17: 1}`
- row=9699632 distinct_labels=7 least_label_hist=`{2: 11, 3: 4, 5: 2, 7: 2, 13: 1, 17: 1, 19: 1}`
- gap_stats=`{'min_gap': 20, 'max_gap': 21789, 'small_gaps': [20, 20, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 27, 27, 35, 35, 35, 35]}`; avg_survivor_count_by_decile=`[3.7625, 3.7625, 3.7625, 3.7625, 3.7625, 3.7625, 3.7625, 3.7625, 3.7625, 3.7625]`

## 7. 后续证明义务

- 将边界零行不存在表述为 CRT 覆盖证书最小代表 >=P 的下界。
- 构造独立边界势函数 Phi_P(R)，而不是依赖中区密度单调性。
- 若使用中区粗合数密集，必须证明其通过同一证书族压迫边界代表；当前尚未闭合。
