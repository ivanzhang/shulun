# Prime Matrix 外部前沿定理压力测试证书

**状态：** `external_frontier_theorems_imported_side_bounds_closed_main_target_open`
**外部源核验日期：** `2026-05-23`

## 1. 结论

外部前沿定理已经能给出真实副产品：Baker-Harman-Pintz 2001 禁止长度约 P^0.05 以上的连续空行串；若 Runbo Li 2025 预印本被接受，可把指数改进到 P^0.04。Xylouris/Meng 的 Linnik 型结果保证列方向最终出现素数，但高度仍为 P^5 或 P^4.5 量级，不能进入 P^2 方阵；Li-Zhang-Cai 的 P2 almost-prime 结果进入 P^2，却正好是错误奇偶对象。Guth--Maynard v2 与 Le Duc Hieu v2 在 theta>17/30 短区间内给出点态 PNT/等差数列结构，但换算到行尺度仍需要 P^(2/15+o(1)) 个行厚度。故所有有帮助的外部定理都已定位为 side bounds/parity diagnostics；目标命题仍需要 theta<=1/2 的点态短区间定理、Linnik<=2 的同窗口常数版本、theta=1/2 二阶矩到行格点的转移，或真正非线性破奇偶构造。

```text
target_short_interval_theta=0.5
best_published_pointwise_short_interval_theta=0.525
best_frontier_preprint_pointwise_short_interval_theta=0.52
best_arxiv_uniform_structural_theta=17/30
best_published_empty_row_run_exponent_bound=0.05+epsilon
best_frontier_preprint_empty_row_run_exponent_bound=0.04+epsilon_if_accepted
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
| Le Duc Hieu 2025 prime APs in short intervals | `arxiv_external_structural_stress` | For theta>17/30, every sufficiently long interval [x,x+x^theta] contains many k-term APs of primes. | At x~P^2 the interval length remains P^(17/15+o(1)); it certifies rich prime structure only after thickening each row by P^(2/15+o(1)) rows. | Rules out the hope that adding Green-Tao/transference structure at the 17/30 scale alone closes the P-row theorem. | `false` | The row window is still wider than one P-row; structural abundance does not imply a prime in each individual row. |
| Xylouris 2011 Linnik exponent 5.2 | `published_external` | Least prime in a reduced residue class mod q is O(q^5.2). | For q=P this gives a column prime by height P^5.2, far beyond the P^2 square. | Confirms the AP route is real but much too weak for P x P column closure. | `false` | Column theorem needs Linnik exponent <=2 with compatible constants/window. |
| Xylouris 2018 Linnik exponent <5 | `published_external_nonenglish` | Improves the general Linnik exponent below 5. | For q=P this is still height P^(5-o(1)), not P^2. | Best general published direction found for least prime AP, still not target-compatible. | `false` | Exponent gap remains nearly 3. |
| Meng 2001 bounded-cubic-part AP exponent 4.5 | `published_external_special_moduli` | For moduli with bounded cubic part, least AP prime is O(q^4.5). | Prime modulus P is structurally compatible with bounded cubic part, but P^4.5 is still outside the P^2 square. | Stronger special-modulus AP side theorem; gives no column closure. | `false` | Exponent gap 2.5 above the needed L<=2 threshold. |
| Li-Zhang-Cai 2021 least P2 almost-prime in AP | `arxiv_external_wrong_object` | Least at-most-two-prime-factor number in a reduced residue class is O(q^1.8345). | For q=P this enters the P^2 square, but it is an almost-prime, not a prime. | Sharp parity-barrier diagnostic: the AP sieve reaches the square for P2, not for primes. | `false` | Wrong parity object; cannot replace column prime existence. |

## 3. 转换门槛引理

```text
pointwise_short_interval_to_row_run=A pointwise theorem giving a prime in every interval of length x^theta at x~P^2 only gives no empty row-run longer than P^(2theta-1+o(1)); every-row closure requires theta<=1/2.
linnik_to_square_column=A least-prime-in-AP theorem p(a mod P) << P^L enters the P^2 square only if L<=2 with compatible constants and reduced residue classes.
almost_all_exceptional_to_lattice=Almost-all x short-interval PNT does not control the rigid lattice of P-spaced row starts without an additional grid-transfer or second-moment input.
```

## 4. 真实副产品

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
HieuPrimeAPsTheta17over30_structural_abundance_no_row_closure
```

## 5. 仍需的新突破

```text
PointwiseShortIntervalPrimeTheoremThetaLeHalf OR LinnikExponentLeTwoWithSquareWindowConstants OR GridTransferredShortIntervalSecondMomentAtThetaHalf OR NonlinearParityBreakingActualSourceConstructor
```

## 6. 来源版本快照

| name | version | date | audited payload | source |
| --- | --- | --- | --- | --- |
| Baker-Harman-Pintz 2001 | `published` | 2001-10-22 online / 2001-11 issue | Published pointwise prime in [x, x+x^0.525] for large x. | <https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2> |
| Runbo Li short intervals | `arXiv:2308.04458v8` | 2025-10-16 | Preprint claims primes in [x-x^0.52, x] for all sufficiently large x. | <https://arxiv.org/abs/2308.04458> |
| Guth-Maynard large values | `arXiv:2405.20552v2` | 2026-04-07 | Zero-density estimate and short-interval prime asymptotics at length x^(17/30+o(1)). | <https://arxiv.org/abs/2405.20552> |
| Gafni-Tao exceptional intervals | `arXiv:2505.24017v1` | 2025-05-29 | Exceptional-set interface: all x for theta>17/30 and almost all x for theta>2/15 are not row-grid pointwise closure. | <https://arxiv.org/abs/2505.24017> |
| Le Duc Hieu short-interval prime APs | `arXiv:2509.04883v2` | 2025-09-24 | Many k-term prime APs in every interval [x,x+x^theta] for theta>17/30; structurally stronger but length gate unchanged. | <https://arxiv.org/abs/2509.04883> |
| Li-Zhang-Cai least P2 almost-prime in AP | `arXiv:2103.13360v2` | 2021-07-19 | P2(a,q) << q^1.8345, inside P^2 after q=P but wrong parity object. | <https://arxiv.org/abs/2103.13360> |
| Xylouris Linnik constant | `Acta Arith. 150 (2011)` | 2011 | Least AP prime exponent L=5.2; later <5 records remain far above the needed L<=2 gate. | <https://arxiv.org/abs/0906.2749> |

## 7. 来源链接

| theorem | source |
| --- | --- |
| Baker-Harman-Pintz 2001 prime gaps | <https://doi.org/10.1112/plms/83.3.532> |
| Runbo Li 2025 Harman-sieve computation | <https://arxiv.org/abs/2308.04458> |
| Guth-Maynard 2024/2026 zero-density consequence | <https://arxiv.org/abs/2405.20552> |
| Gafni-Tao 2025 exceptional short intervals | <https://arxiv.org/abs/2505.24017> |
| Le Duc Hieu 2025 prime APs in short intervals | <https://arxiv.org/abs/2509.04883> |
| Xylouris 2011 Linnik exponent 5.2 | <https://arxiv.org/abs/0906.2749> |
| Xylouris 2018 Linnik exponent <5 | <https://www.mathnet.ru/eng/cheb681> |
| Meng 2001 bounded-cubic-part AP exponent 4.5 | <https://xbna.pku.edu.cn/EN/Y2001/V37/I1/20> |
| Li-Zhang-Cai 2021 least P2 almost-prime in AP | <https://arxiv.org/abs/2103.13360> |

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `58f9cfb013fdce3073a5b301f691856e562af7d54d480a6af53c73490bd1f46b` |
| `docs/monograph/external-theorem-index.md` | `7298c290ecf47a60f92065ca32e98522c6ff2bb8eb9ef6d9e4f58d48adcd1eb2` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `05a00d919dccd89898c09dbdd48a89950c59a32ffc28354ad8420674759321ff` |
| `docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.json` | `e8a6967386568175e8d4b06d7b0abd5123934ecc89ac8cb094f154d8bf076290` |
| `experiments/prime_matrix_external_frontier_theorem_stress_router.py` | `f0942d19a1ad12167ca30b9969e8419e7fbdac87258de4357bac35e9ddb2d4c7` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `c3922727f38323266346e20689bed851ee9314b7129b89a42e56cc45763fc59b` |
