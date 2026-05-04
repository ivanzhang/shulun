# 多点小素平方自由删除账本

**状态：** `alpha_tail_square_deletion_ledger_reduction_open`

上一层得到

\[
E_m=\Delta_m^{\rm rough}-D_m^{\rm sq}.
\tag{SDL-1}
\]

因此要证明 `C=1`，核心可转为证明小素平方自由删除量 `D_m^{sq}` 足以覆盖粗筛端点盈余。
本文把 `D_m^{sq}` 写成有限平方剩余类并给出 Bonferroni/重叠证书。

## 1. 平方删除事件

在粗筛幸存集 `R_{m,r}` 上，对素数 `a<=y` 与位置 `0<=j<m` 定义事件

\[
\mathcal E_{a,j}=\{d\in R_{m,r}:a^2\mid d+jr\}.
\tag{SDL-2}
\]

平方自由删除量为

\[
D_m^{\rm sq}
=
\left|\bigcup_{\substack{a\le y\\0\le j<m}}\mathcal E_{a,j}\right|.
\tag{SDL-3}
\]

每个事件是模 `a^2` 的一个剩余类；若 `a\nmid r` 且 `a^2>m`，不同 `j` 通常给 distinct 类。

## 2. Bonferroni 下界

令

\[
S_1=\sum_{a,j}|\mathcal E_{a,j}|,
\tag{SDL-4}
\]

\[
S_2=\sum_{(a,j)<(b,k)}|\mathcal E_{a,j}\cap\mathcal E_{b,k}|.
\tag{SDL-5}
\]

则

\[
D_m^{\rm sq}\ge S_1-S_2.
\tag{SDL-6}
\]

若 `S_1-S_2` 已大于 `\Delta_m^{rough}`，则 `E_m<=0` 立即成立。

另有一个在重叠强时更稳的下界。令

\[
H_{\max}=\max_{d\in R_{m,r}}\#\{(a,j):a^2\mid d+jr\}.
\tag{SDL-7}
\]

则

\[
D_m^{\rm sq}\ge {S_1\over H_{\max}}.
\tag{SDL-8}
\]

因为 `S_1` 是所有被删除点的命中重数总和，而每个被删除点贡献至多 `H_max`。
若 `S_1/H_max` 已大于 `\Delta_m^{rough}`，同样得到 `E_m<=0`。若失败，则必须出现平方类总质量低或
单点平方命中重数异常高。

## 3. 失败二分

若平方删除不足，即

\[
D_m^{\rm sq}<\Delta_m^{\rm rough},
\tag{SDL-9}
\]

则至少发生一项：

1. **平方类总质量不足。**  
   `S_1` 小于粗筛模型给出的预期，进入小模平方类 `PDEC`。
2. **平方类重叠过强。**  
   `S_2` 过大或 `H_max` 过大，说明许多粗筛幸存点同时落入多个平方类，进入 square-overlap
   `ColumnCRT/Rankin`。
3. **粗筛盈余过强。**  
   `\Delta_m^{rough}` 本身过大，回到粗筛端点 `PDEC/SAE`。

所以 `D_m^{sq}` 不足不是新黑箱；它只能来自平方类低模失衡或平方类重叠拥塞。

## 4. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_square_deletion_audit.py
```

样本：

| p | block | shift | m | rough | deleted | S1 | S2 | S1-S2 | max hits | S1/Hmax |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 1186 | 997 | 4363 | 9075 | -4712 | 10 | 436.300000 |
| 997 | 4096 | -36 | 5 | 995 | 894 | 5013 | 13922 | -8909 | 12 | 417.750000 |
| 5003 | 8192 | -36 | 4 | 4577 | 3368 | 13405 | 25459 | -12054 | 10 | 1340.500000 |
| 5003 | 8192 | -36 | 5 | 4261 | 3345 | 16504 | 41380 | -24876 | 12 | 1375.333333 |
| 10007 | 16384 | -900 | 4 | 8518 | 5658 | 23726 | 46601 | -22875 | 12 | 1977.166667 |
| 10007 | 16384 | -900 | 5 | 7629 | 5327 | 27575 | 71211 | -43636 | 15 | 1838.333333 |

样本说明：二阶 Bonferroni 因平方类重叠强而为负；但 `S1/Hmax` 在所有正粗筛盈余样本中都超过
`rough_surplus`。下一步应把 `H_max` 的理论上界显式化。

## 5. 审稿边界

已证明：

```text
squarefree deletion D_sq is a finite union of q^2 residue classes;
D_sq >= S1-S2;
D_sq >= S1/Hmax;
D_sq insufficient => square-mass PDEC or square-overlap congestion or rough PDEC.
```

尚未证明：

```text
S1/Hmax 总是足以覆盖 rough_endpoint_surplus；
或三个失败出口全部可排斥。
```

下一步最小硬点是对 `S1` 给粗筛条件下的下界，并对 `H_max` 给乘积/CRT 重叠上界。
