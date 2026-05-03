# BPN-Defect 的 Bonferroni 截断审计

**状态：** `fifth_bonferroni_reduced_to_prime_minus_high_omega_penalty`

Bonferroni/Möbius 截断给出了可审查的边界势函数候选，低阶奇截断在小样本边界帽上给出正下界；扩展扫描显示三阶会失败，但五阶截断在 P<=199 的边界帽未发现失败，且选点扫描到 P=5003 仍为正。五阶下界有精确解释：素数数目减去至少六个小素因子的高重惩罚。因此最新硬点是证明每个边界行的素数数目严格压过高重小因子惩罚。

## 1. 截断公式

令 `N=prod_{ell<P}ell`，第 `r` 行幸存列数为

\[
S(r)=\#\{1\le c<P:((r-1)P+c,N)=1\}.
\]

对 `d|N` 定义

\[
A_d(r)=\#\{1\le c<P:d\mid (r-1)P+c\}.
\]

则

\[
S(r)=\sum_{d|N}\mu(d)A_d(r).
\]

奇阶截断 `S_1,S_3,S_5,...` 是 `S(r)` 的 Bonferroni 下界。若某个奇阶截断在所有边界行 `2<=r<=P` 上统一为正，就能证明 `BPN(P)`。

## 2. 审计总表

| P | zero count | first zero | front min row | front min exact S | front rows with positive odd bound | first positive order hist |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 4 | 169 | 10 | 1 | 12/12 | `{3: 12}` |
| 17 | 28 | 1211 | 13 | 1 | 16/16 | `{3: 15, 5: 1}` |
| 19 | 496 | 3659 | 16 | 1 | 18/18 | `{3: 18}` |
| 23 | 3456 | 59 | 15 | 2 | 22/22 | `{3: 22}` |

### 边界帽低阶奇截断扩展扫描

- max_p=199
- max_order=7
- checked_prime_count=41
- failures=`[]`
- s5_failures=`[]`
- worst_rows=`[{'p': 199, 'min_by_order': {1: -195, 3: -26, 5: 12, 7: 12}, 'min_row_by_order': {1: 27, 3: 192, 5: 180, 7: 180}, 'front_rows_with_some_positive_odd': 198, 'front_row_count': 198, 'first_row_without_positive_odd': None, 'product_counts': {1: 45, 2: 990, 3: 2864, 4: 1737, 5: 234, 6: 2, 7: 0}}, {'p': 197, 'min_by_order': {1: -190, 3: -25, 5: 15, 7: 15}, 'min_row_by_order': {1: 48, 3: 193, 5: 73, 7: 73}, 'front_rows_with_some_positive_odd': 196, 'front_row_count': 196, 'first_row_without_positive_odd': None, 'product_counts': {1: 44, 2: 946, 3: 2767, 4: 1688, 5: 230, 6: 1, 7: 0}}, {'p': 193, 'min_by_order': {1: -186, 3: -23, 5: 14, 7: 14}, 'min_row_by_order': {1: 13, 3: 122, 5: 74, 7: 74}, 'front_rows_with_some_positive_odd': 192, 'front_row_count': 192, 'first_row_without_positive_odd': None, 'product_counts': {1: 43, 2: 903, 3: 2649, 4: 1607, 5: 214, 6: 1, 7: 0}}, {'p': 191, 'min_by_order': {1: -184, 3: -25, 5: 14, 7: 14}, 'min_row_by_order': {1: 125, 3: 123, 5: 39, 7: 39}, 'front_rows_with_some_positive_odd': 190, 'front_row_count': 190, 'first_row_without_positive_odd': None, 'product_counts': {1: 42, 2: 861, 3: 2555, 4: 1560, 5: 208, 6: 1, 7: 0}}, {'p': 181, 'min_by_order': {1: -173, 3: -23, 5: 11, 7: 11}, 'min_row_by_order': {1: 90, 3: 130, 5: 130, 7: 130}, 'front_rows_with_some_positive_odd': 180, 'front_row_count': 180, 'first_row_without_positive_odd': None, 'product_counts': {1: 41, 2: 820, 3: 2338, 4: 1397, 5: 172, 6: 1, 7: 0}}, {'p': 179, 'min_by_order': {1: -170, 3: -21, 5: 12, 7: 13}, 'min_row_by_order': {1: 167, 3: 152, 5: 168, 7: 106}, 'front_rows_with_some_positive_odd': 178, 'front_row_count': 178, 'first_row_without_positive_odd': None, 'product_counts': {1: 40, 2: 780, 3: 2250, 4: 1353, 5: 166, 6: 1, 7: 0}}, {'p': 173, 'min_by_order': {1: -165, 3: -21, 5: 11, 7: 11}, 'min_row_by_order': {1: 69, 3: 136, 5: 136, 7: 136}, 'front_rows_with_some_positive_odd': 172, 'front_row_count': 172, 'first_row_without_positive_odd': None, 'product_counts': {1: 39, 2: 741, 3: 2113, 4: 1252, 5: 151, 6: 0, 7: 0}}, {'p': 167, 'min_by_order': {1: -156, 3: -18, 5: 11, 7: 11}, 'min_row_by_order': {1: 55, 3: 128, 5: 141, 7: 141}, 'front_rows_with_some_positive_odd': 166, 'front_row_count': 166, 'first_row_without_positive_odd': None, 'product_counts': {1: 38, 2: 703, 3: 1974, 4: 1150, 5: 137, 6: 0, 7: 0}}, {'p': 163, 'min_by_order': {1: -151, 3: -18, 5: 11, 7: 11}, 'min_row_by_order': {1: 75, 3: 144, 5: 116, 7: 116}, 'front_rows_with_some_positive_odd': 162, 'front_row_count': 162, 'first_row_without_positive_odd': None, 'product_counts': {1: 37, 2: 666, 3: 1868, 4: 1088, 5: 126, 6: 0, 7: 0}}, {'p': 157, 'min_by_order': {1: -146, 3: -18, 5: 11, 7: 11}, 'min_row_by_order': {1: 103, 3: 126, 5: 119, 7: 119}, 'front_rows_with_some_positive_odd': 156, 'front_row_count': 156, 'first_row_without_positive_odd': None, 'product_counts': {1: 36, 2: 630, 3: 1750, 4: 990, 5: 114, 6: 0, 7: 0}}, {'p': 151, 'min_by_order': {1: -139, 3: -17, 5: 12, 7: 12}, 'min_row_by_order': {1: 112, 3: 131, 5: 40, 7: 40}, 'front_rows_with_some_positive_odd': 150, 'front_row_count': 150, 'first_row_without_positive_odd': None, 'product_counts': {1: 35, 2: 595, 3: 1627, 4: 905, 5: 99, 6: 0, 7: 0}}, {'p': 149, 'min_by_order': {1: -135, 3: -16, 5: 11, 7: 11}, 'min_row_by_order': {1: 41, 3: 101, 5: 79, 7: 79}, 'front_rows_with_some_positive_odd': 148, 'front_row_count': 148, 'first_row_without_positive_odd': None, 'product_counts': {1: 34, 2: 561, 3: 1557, 4: 871, 5: 95, 6: 0, 7: 0}}]`

### 较大 P 的 S5 恒等式扫描

- selected_s5_omega_scan=`[{'p': 251, 'min_s5': 17, 'min_row': 175, 'prime_like_at_min': 18, 'high_omega_penalty_at_min': 1, 'failures': []}, {'p': 503, 'min_s5': 28, 'min_row': 360, 'prime_like_at_min': 29, 'high_omega_penalty_at_min': 1, 'failures': []}, {'p': 1009, 'min_s5': 49, 'min_row': 906, 'prime_like_at_min': 52, 'high_omega_penalty_at_min': 3, 'failures': []}, {'p': 2003, 'min_s5': 96, 'min_row': 1674, 'prime_like_at_min': 113, 'high_omega_penalty_at_min': 17, 'failures': []}, {'p': 5003, 'min_s5': 177, 'min_row': 4822, 'prime_like_at_min': 272, 'high_omega_penalty_at_min': 95, 'failures': []}]`


## 3. 最薄边界行画像

### P=13
- row=10, exact_survivors=1
- odd_lower_bounds=`{1: -3, 3: 1, 5: 1}`
- even_upper_bounds=`{0: 12, 2: 3, 4: 1}`
- first_zero row=169, odd_lower_bounds=`{1: -3, 3: 0, 5: 0}`

### P=17
- row=13, exact_survivors=1
- odd_lower_bounds=`{1: -6, 3: 0, 5: 1}`
- even_upper_bounds=`{0: 16, 2: 5, 4: 1, 6: 1}`
- first_zero row=1211, odd_lower_bounds=`{1: -5, 3: -1, 5: 0}`

### P=19
- row=16, exact_survivors=1
- odd_lower_bounds=`{1: -8, 3: 1, 5: 1, 7: 1}`
- even_upper_bounds=`{0: 18, 2: 4, 4: 1, 6: 1}`
- first_zero row=3659, odd_lower_bounds=`{1: -8, 3: -1, 5: 0, 7: 0}`

### P=23
- row=15, exact_survivors=2
- odd_lower_bounds=`{1: -11, 3: 1, 5: 2, 7: 2}`
- even_upper_bounds=`{0: 22, 2: 8, 4: 2, 6: 2, 8: 2}`
- first_zero row=59, odd_lower_bounds=`{1: -11, 3: 0, 5: 0, 7: 0}`

## 4. 结论

五阶 Bonferroni 截断给出一个非常窄、可证明化的硬点：

\[
S_5(r)=(P-1)-I_1(r)+I_2(r)-I_3(r)+I_4(r)-I_5(r)>0\qquad(2\le r\le P).
\]

这里 `I_j(r)` 是 j 个根基素数覆盖列交集大小的总和。奇阶 Bonferroni 给出 `S_5(r)<=S(r)`，因此若能逐项证明上式，则直接得到 `S(r)>0`，从而闭合 `BPN(P)`。

若五阶正性无法统一证明，下一步才应改写为带权筛版本：构造非负权重 `W_d`，证明

\[
\sum_{d|N}\mu(d)W_d A_d(r)>0\qquad (2\le r\le P),
\]

或证明该不等式失败时，高阶交叉集中必然触发低模 CRT 缺陷、Tail-anchor 缺陷或残洞势函数下降矛盾。

## 5. 五阶逐点恒等式

设 `omega_P(n)` 为 `n` 的不同 `<P` 素因子个数。对单个数 `n`，五阶 Bonferroni 权重为

\[
w_5(n)=\sum_{j=0}^5(-1)^j\binom{\omega_P(n)}j.
\]

由组合恒等式可得：

\[
w_5(n)=\begin{cases}
1,&\omega_P(n)=0,\\
0,&1\le \omega_P(n)\le5,\\
-\binom{\omega_P(n)-1}{5},&\omega_P(n)\ge6.
\end{cases}
\]

在边界帽 `n<P^2` 中，`omega_P(n)=0` 等价于 `n` 为素数。因此

\[
S_5(r)=\pi((r-1)P+1,rP-1)-\sum_{\substack{(r-1)P<n<rP\\ \omega_P(n)\ge6}}\binom{\omega_P(n)-1}{5}.
\]

这把 `BPN-B5` 的真实内容压缩为：每个边界行中的素数数量，严格大于含至少六个小素因子的高重合数惩罚。该形式比抽象交集和更适合下一步引入小核心乘积、短区间多因子容量和 Tail-anchor 缺陷出口。

## 6. 后续义务

- 严格证明每个边界行中 prime_like_count > high_omega_penalty。
- 将高重惩罚分解为含至少 6 个小素因子的整数计数，并用短区间多重因子上界控制。
- 充分利用边界事实 n<P^2，含至少 6 个小素因子者必须含很小的核心乘积。
- 若所有低阶奇截断均失败，证明负余量集中到低模端点缺陷或 Tail-anchor 缺陷。
- 继续保留 BPN-MCR / BPN-Phi / BPN-Defect 三接口，不宣称闭合。
