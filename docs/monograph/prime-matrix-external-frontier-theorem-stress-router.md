# Prime Matrix 外部前沿定理压力测试证书

**状态：** `external_frontier_theorems_imported_side_bounds_closed_main_target_open`

## 1. 结论

外部前沿定理已经能给出真实副产品：Baker-Harman-Pintz 2001 禁止长度约 P^0.05 以上的连续空行串；若 Runbo Li 2025 预印本被接受，可把指数改进到 P^0.04。Xylouris/Meng 的 Linnik 型结果保证列方向最终出现素数，但高度仍为 P^5 或 P^4.5 量级，不能进入 P^2 方阵；Li-Zhang-Cai 的 P2 almost-prime 结果进入 P^2，却正好是错误奇偶对象。故所有有帮助的外部定理都已定位为 side bounds/parity diagnostics；目标命题仍需要 theta<=1/2 的点态短区间定理、Linnik<=2 的同窗口常数版本、theta=1/2 二阶矩到行格点的转移，或真正非线性破奇偶构造。

```text
target_short_interval_theta=0.5
best_published_pointwise_short_interval_theta=0.525
best_frontier_preprint_pointwise_short_interval_theta=0.52
best_published_empty_row_run_exponent_bound=0.050000000000000044
best_frontier_preprint_empty_row_run_exponent_bound=0.040000000000000036
target_linnik_exponent=2.0
best_general_linnik_exponent_recorded=5.0
best_special_prime_modulus_compatible_linnik_exponent_recorded=4.5
least_almost_prime_ap_exponent_inside_square=1.8345
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 2. 外部定理压力表

| theorem | status | payload | transformed payload | helps | closes target | obstruction |
| --- | --- | --- | --- | --- | --- | --- |
| Baker-Harman-Pintz 2001 prime gaps | `published_external` | Every large interval of length x^0.525 contains a prime. | For x~P^2 this forbids prime-free row runs longer than P^0.05 up to constants. | Closes a genuine side theorem: no asymptotically long consecutive empty-row block of exponent >0.05. | `false` | Target row theorem needs theta<=1/2, i.e. empty-run exponent <0. |
| Runbo Li 2025 Harman-sieve computation | `frontier_preprint_external` | Claims every large interval of length x^0.52 contains a prime. | If accepted, this improves the empty-row run exponent bound from 0.05 to 0.04. | Best known-looking pointwise short-interval candidate located in this audit. | `false` | Still has theta=0.52>1/2 and is preprint status; it does not give one prime in each P-long row. |
| Guth-Maynard 2024/2026 zero-density consequence | `arxiv_external` | Uniform short-interval PNT at exponents theta>17/30. | For x~P^2 this gives row windows of size P^(17/15+o(1)), weaker than BHP/Li for pointwise row closure. | Important for zero-density and exceptional-set technology, but not the pointwise row gate. | `false` | 17/30>1/2; pointwise length is still too long. |
| Gafni-Tao 2025 exceptional short intervals | `arxiv_external` | Relates zero-density estimates to exceptional sets; records all-x theta>17/30 and almost-all theta>2/15 context. | Almost-all x control does not imply control on the rigid lattice endpoints kP or P^2-row blocks. | Useful for density-style side bounds and for checking that row-grid control is the missing interface. | `false` | Needs lattice/grid transfer from continuous exceptional measure to every P-spaced row endpoint. |
| Xylouris 2011 Linnik exponent 5.2 | `published_external` | Least prime in a reduced residue class mod q is O(q^5.2). | For q=P this gives a column prime by height P^5.2, far beyond the P^2 square. | Confirms the AP route is real but much too weak for P x P column closure. | `false` | Column theorem needs Linnik exponent <=2 with compatible constants/window. |
| Xylouris 2018 Linnik exponent <5 | `published_external_nonenglish` | Improves the general Linnik exponent below 5. | For q=P this is still height P^(5-o(1)), not P^2. | Best general published direction found for least prime AP, still not target-compatible. | `false` | Exponent gap remains nearly 3. |
| Meng 2001 bounded-cubic-part AP exponent 4.5 | `published_external_special_moduli` | For moduli with bounded cubic part, least AP prime is O(q^4.5). | Prime modulus P is structurally compatible with bounded cubic part, but P^4.5 is still outside the P^2 square. | Stronger special-modulus AP side theorem; gives no column closure. | `false` | Exponent gap 2.5 above the needed L<=2 threshold. |
| Li-Zhang-Cai 2021 least P2 almost-prime in AP | `arxiv_external_wrong_object` | Least at-most-two-prime-factor number in a reduced residue class is O(q^1.8345). | For q=P this enters the P^2 square, but it is an almost-prime, not a prime. | Sharp parity-barrier diagnostic: the AP sieve reaches the square for P2, not for primes. | `false` | Wrong parity object; cannot replace column prime existence. |

## 3. 真实副产品

已由已发表外部定理登记的副产品：

```text
BHPNoLongEmptyRowRunExponent005
XylourisLinnikColumnPrimeByHeightP5Plus
MengPrimeModulusColumnPrimeByHeightP45
```

预印本/错误奇偶对象诊断：

```text
LeastP2AlmostPrimeInEachColumnInsideP2Square
Li052NoLongEmptyRowRunExponent004_if_accepted
```

## 4. 仍需的新突破

```text
PointwiseShortIntervalPrimeTheoremThetaLeHalf OR LinnikExponentLeTwoWithSquareWindowConstants OR GridTransferredShortIntervalSecondMomentAtThetaHalf OR NonlinearParityBreakingActualSourceConstructor
```

## 5. 来源链接

| theorem | source |
| --- | --- |
| Baker-Harman-Pintz 2001 prime gaps | <https://doi.org/10.1112/plms/83.3.532> |
| Runbo Li 2025 Harman-sieve computation | <https://arxiv.org/abs/2308.04458> |
| Guth-Maynard 2024/2026 zero-density consequence | <https://arxiv.org/abs/2405.20552> |
| Gafni-Tao 2025 exceptional short intervals | <https://arxiv.org/abs/2505.24017> |
| Xylouris 2011 Linnik exponent 5.2 | <https://arxiv.org/abs/0906.2749> |
| Xylouris 2018 Linnik exponent <5 | <https://www.mathnet.ru/eng/cheb681> |
| Meng 2001 bounded-cubic-part AP exponent 4.5 | <https://xbna.pku.edu.cn/EN/Y2001/V37/I1/20> |
| Li-Zhang-Cai 2021 least P2 almost-prime in AP | <https://arxiv.org/abs/2103.13360> |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `294f967aeddee1b1c6e019ea61cfd2fe559ba20f9ae7217a0547dd0dc3fa38c3` |
| `docs/monograph/external-theorem-index.md` | `90302c76df1b04dada3e1f85d3a0ff5bbba9363a9d8cce418eb59ed3671db597` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `472b2c1abb88232e553081fe3759a4ee7a6c17b9af3e26aa02f73f3d7018c715` |
| `docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.json` | `e8a6967386568175e8d4b06d7b0abd5123934ecc89ac8cb094f154d8bf076290` |
| `experiments/prime_matrix_external_frontier_theorem_stress_router.py` | `7a0fd0f40663df793d7f88cede9eae199167ea3f8051b7998973f3af4be058d2` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `9d41b790ad1098b4c730483f5d17557d4a8da70748f358285ba16b0708f5aac0` |
