# Prime Matrix inverse alignment 最小 x 相位扫描路由器

**状态：** `inverse_alignment_min_x_phase_scan_closed_for_requested_P_uniform_bound_open`

用户提出的轮序 gcd 方程组在素因子可选意义下与 `q|xP+r` 完全等价；对请求的 P=13,17,19,23,29,31，最小对齐解分别为 168、1210、3658、58、5209、60794，全部大于 P。早期窗口 `1<=x<=P` 中，多数 x 已由 cutoff 容量缺口排除；少数例外表现为 raw capacity 足够但后缀相位没有命中残洞的 pure phase defect；扩展到 P<=101 时，纯相位例外只出现在 (17,12) 与 (23,14)；并且从 P>=29 起，第二大素数 cutoff 后只剩最大尾素数时已经有严格容量缺口。因此最窄可攻全局输入不是再求样本，而是证明统一的“容量缺口或登记相位缺陷”下界。

```text
wheel_gcd_equivalence_checked=true
all_requested_minimal_x_gt_P=true
uniform_lower_bound_inequality_proved=false
row_column_unconditional_closed=false
```

## 1. 等价式

对任意素数 `q<P`：

```text
q | xP+r
<=> x == -r*P^{-1} (mod q)
<=> q | (P-q)x+r
<=> gcd((P-q)x+r, q)=q.
```

因此用户的 `gcd(kx+r,P-k)` 轮序系统是等价的；其中 `k=P-q` 给出模数正好为 `q` 的规范见证。`gcd(x,r)>1` 是有效但冗余的快捷项。

## 2. 最小对齐解

| P | primes q<P | minimal x | one-indexed row | x/P | overlap debt | first-factor histogram |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `13` | `[2, 3, 5, 7, 11]` | `168` | `169` | `12.923076923077` | `3` | `{2: 6, 3: 2, 5: 2, 7: 1, 11: 1}` |
| `17` | `[2, 3, 5, 7, 11, 13]` | `1210` | `1211` | `71.176470588235` | `5` | `{2: 8, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1}` |
| `19` | `[2, 3, 5, 7, 11, 13, 17]` | `3658` | `3659` | `192.526315789474` | `8` | `{2: 9, 3: 3, 5: 2, 7: 2, 11: 1, 13: 1}` |
| `23` | `[2, 3, 5, 7, 11, 13, 17, 19]` | `58` | `59` | `2.521739130435` | `11` | `{2: 11, 3: 4, 5: 2, 7: 2, 13: 1, 17: 1, 19: 1}` |
| `29` | `[2, 3, 5, 7, 11, 13, 17, 19, 23]` | `5209` | `5210` | `179.620689655172` | `16` | `{2: 14, 3: 5, 5: 2, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}` |
| `31` | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]` | `60794` | `60795` | `1961.096774193548` | `16` | `{2: 15, 3: 5, 5: 2, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1}` |

## 3. 相位向量

| P | phase vector rho_q/mu_q |
| --- | --- |
| `13` | `[(2, 0, 6), (3, 0, 4), (5, 1, 3), (7, 0, 1), (11, 5, 1)]` |
| `17` | `[(2, 0, 8), (3, 1, 6), (5, 0, 3), (7, 3, 2), (11, 0, 1), (13, 9, 1)]` |
| `19` | `[(2, 0, 9), (3, 2, 6), (5, 3, 4), (7, 1, 3), (11, 7, 2), (13, 9, 1), (17, 11, 1)]` |
| `23` | `[(2, 0, 11), (3, 1, 8), (5, 1, 5), (7, 3, 3), (11, 8, 2), (13, 5, 2), (17, 9, 1), (19, 15, 1)]` |
| `29` | `[(2, 1, 14), (3, 1, 10), (5, 4, 5), (7, 6, 4), (11, 2, 3), (13, 12, 2), (17, 1, 2), (19, 8, 2), (23, 3, 2)]` |
| `31` | `[(2, 0, 15), (3, 1, 10), (5, 1, 6), (7, 3, 4), (11, 5, 3), (13, 9, 2), (17, 6, 2), (19, 15, 1), (23, 6, 2), (29, 9, 1)]` |

## 4. 早期窗口排斥模式

| P | checked | capacity deficit x-count | pure phase defect x-count | weakest raw capacity margin | final-tail gap | phase-only witnesses |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `13` | `1<=x<=13` | `13` | `0` | `1` | `1` | `[]` |
| `17` | `1<=x<=17` | `16` | `1` | `0` | `0` | `[{'x': 12, 'uncovered_columns': [7], 'best_capacity_cut': {'cutoff': 11, 'residual_size': 1, 'suffix_raw_capacity': 1, 'suffix_effective_hits_inside_residual': 0, 'capacity_gap_residual_minus_raw': 0, 'effective_gap_residual_minus_hits': 1, 'uncovered_columns': [7]}}]` |
| `19` | `1<=x<=19` | `19` | `0` | `1` | `1` | `[]` |
| `23` | `1<=x<=23` | `22` | `1` | `0` | `0` | `[{'x': 14, 'uncovered_columns': [9, 15], 'best_capacity_cut': {'cutoff': 17, 'residual_size': 2, 'suffix_raw_capacity': 2, 'suffix_effective_hits_inside_residual': 0, 'capacity_gap_residual_minus_raw': 0, 'effective_gap_residual_minus_hits': 2, 'uncovered_columns': [9, 15]}}]` |
| `29` | `1<=x<=29` | `29` | `0` | `1` | `1` | `[]` |
| `31` | `1<=x<=31` | `31` | `0` | `1` | `1` | `[]` |

## 5. 扩展容量探针

扩展扫描范围：素数 `13<=P<=101`。

| P | capacity deficit x-count | pure phase defect x-count | weakest raw margin | final-tail cutoff/tail | final-tail min gap | phase-only witnesses |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| `13` | `13` | `0` | `1` | `7/11` | `1` | `[]` |
| `17` | `16` | `1` | `0` | `11/13` | `0` | `[{'x': 12, 'uncovered_columns': [7], 'best_capacity_cut': {'cutoff': 11, 'residual_size': 1, 'suffix_raw_capacity': 1, 'suffix_effective_hits_inside_residual': 0, 'capacity_gap_residual_minus_raw': 0, 'effective_gap_residual_minus_hits': 1, 'uncovered_columns': [7]}}]` |
| `19` | `19` | `0` | `1` | `13/17` | `1` | `[]` |
| `23` | `22` | `1` | `0` | `17/19` | `0` | `[{'x': 14, 'uncovered_columns': [9, 15], 'best_capacity_cut': {'cutoff': 17, 'residual_size': 2, 'suffix_raw_capacity': 2, 'suffix_effective_hits_inside_residual': 0, 'capacity_gap_residual_minus_raw': 0, 'effective_gap_residual_minus_hits': 2, 'uncovered_columns': [9, 15]}}]` |
| `29` | `29` | `0` | `1` | `19/23` | `1` | `[]` |
| `31` | `31` | `0` | `1` | `23/29` | `1` | `[]` |
| `37` | `37` | `0` | `1` | `29/31` | `1` | `[]` |
| `41` | `41` | `0` | `2` | `31/37` | `2` | `[]` |
| `43` | `43` | `0` | `2` | `37/41` | `2` | `[]` |
| `47` | `47` | `0` | `2` | `41/43` | `2` | `[]` |
| `53` | `53` | `0` | `3` | `43/47` | `3` | `[]` |
| `59` | `59` | `0` | `2` | `47/53` | `2` | `[]` |
| `61` | `61` | `0` | `4` | `53/59` | `4` | `[]` |
| `67` | `67` | `0` | `3` | `59/61` | `3` | `[]` |
| `71` | `71` | `0` | `5` | `61/67` | `5` | `[]` |
| `73` | `73` | `0` | `4` | `67/71` | `4` | `[]` |
| `79` | `79` | `0` | `4` | `71/73` | `4` | `[]` |
| `83` | `83` | `0` | `5` | `73/79` | `5` | `[]` |
| `89` | `89` | `0` | `6` | `79/83` | `6` | `[]` |
| `97` | `97` | `0` | `5` | `83/89` | `5` | `[]` |
| `101` | `101` | `0` | `6` | `89/97` | `6` | `[]` |

## 6. 下界控制目标

令 `R_z(x)` 为未被 `q<=z` 覆盖的残洞列，`A_q(x)` 为 `q` 的相位列集，
`C_z(x)=sum_{q>z} |A_q(x)|`，`E_z(x)=|R_z(x) cap union_{q>z} A_q(x)|`。

零行必要条件是：

```text
|R_z(x)| <= E_z(x) <= C_z(x).
```

所以若能对所有 `1<=x<=P` 找到一个 cutoff `z` 使

```text
|R_z(x)| > C_z(x)   或   C_z(x)>=|R_z(x)| 但 |R_z(x)|>E_z(x),
```

就得到 `X(P)>P`。本次样本显示：容量缺口已经排除绝大多数早期行；扩展探针中 `P>=29` 未出现纯相位例外。更强的是，`P>=29` 时取 `z` 为第二大素数 `<P`，只留下最大尾素数，已经出现严格容量缺口。这提示可优先证明 final-tail 容量缺口不等式；若小 P 或等号态出现，则接入 PDEC/SAE/ColumnCRT 登记缺陷线。

## 7. 判定边界

| name | status | statement |
| --- | --- | --- |
| `wheel_gcd_equivalence` | `closed` | q\|xP+r iff x==-r*P^{-1} mod q iff gcd((P-q)x+r,q)=q; hence the k-wheel gcd system is equivalent when prime divisibility, not only a fixed k, is allowed. |
| `minimal_alignment_scan` | `closed_for_requested_P` | For P=13,17,19,23,29,31 the least x satisfying every column is computed by exact divisibility, then replayed by the wheel gcd equations. |
| `capacity_deficit_cut` | `closed_as_necessary_inequality` | For cutoff z, zero row requires \|R_z(x)\| <= C_z(x)=sum_{q>z} mu_q(x); if \|R_z\|>C_z then x cannot be a zero row. |
| `effective_phase_defect_cut` | `closed_as_exact_obstruction` | Even when raw capacity is enough, zero row still requires R_z(x) subset union_{q>z} A_q(x); failure is the exact phase-defect residue obstruction. |
| `final_tail_cut_probe` | `diagnostic_strong_candidate` | For tested P>=29, taking z as the second largest prime below P leaves only the largest tail prime and already gives \|R_z(x)\|>mu_tail(x) for every 1<=x<=P. |
| `uniform_lower_bound_gap` | `open` | A global proof of X(P)>P still needs a non-tautological lower bound forcing capacity deficit, with only exceptional equality cases routed as registered phase defects. |

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-exact-x-budget-interface-ledger.json` | `1cdc1a5cabb6ff9043184f7e567b14622b5667f708564ef9daae04c44beb6a52` |
| `data/inverse-alignment-min-x-phase-scan-ledger.json` | `ece15abdb5fd5bf50a50e66217cd6472bd1f627b57feea2b19e92ab162fe6f98` |
| `docs/monograph/prime-matrix-inverse-alignment-exact-x-budget-interface-router.json` | `9d8332f7813532faf0efab89112cc12b2ce6b2756b7330fff2471e37c36bc5fe` |
| `docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json` | `ff08e13fd2dbbd7dbbdaf7a1648fc8f339cd2e52eec84a5ba3a0df7873c05d9c` |
| `docs/monograph/prime-matrix-zero-row-minrep-route-review.md` | `cff5609900bcfaa796b6b586c44458727b9807f2f1afd2210e52360dbe5bef26` |
| `experiments/prime_matrix_inverse_alignment_min_x_phase_scan_router.py` | `1fa7e7f808422ec78dcba91605538bce981bd428d640c976d1de0b14086178b7` |
