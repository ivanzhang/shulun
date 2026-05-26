# Prime Matrix Phi-LPF product-window additive saving 防火墙

**状态：** `ordinary_product_window_additive_saving_rejected_as_primary_closure_gate`
**核验日期：** `2026-05-26`

Product-window 相位 e_P(hpm) 的普通非零频率节省不能作为主闭合门。若 full-cover 成立，owner product residues 正好是 F_P^*，所以每个非零频率的完整和就是 -1；任何上界 |S_h|<=B(P) 且 B(P)>=1 都不会产生矛盾。因此下一步必须改成精确系数分离、subunit Fourier contradiction、带符号缺陷的 trace/Kloosterman 桥，或点态 C=1 sqrt 素数输入。

```text
source_product_phase_imported=true
complete_nonzero_residue_fourier_fingerprint_closed=true
finite_complete_measure_identity_all_ok=true
ordinary_product_window_additive_saving_rejected_as_primary_gate=true
product_window_exact_coefficient_separation_proved=false
row_column_unconditional_closed=false
```

## 1. 合同门

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CompleteNonzeroResidueFourierFingerprint` | `true` | `true` | full-cover 时 owner residues=F_P^*，故每个非零频率 Fourier 和都等于 -1。 | identity only |
| `OrdinaryProductWindowAdditiveSavingAsPrimaryGate` | `true` | `false` | 任何只给 \|S_h\|<=B(P) 且 B(P)>=1 的普通节省都与 full-cover 完全兼容。 | ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC |
| `ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC` | `false` | `false` | 需要证明 owner product-window 测度不能等于完整非零剩余类测度，或给出 subunit Fourier 矛盾/PDEC。 | ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC OR signed defect transport |
| `ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefect` | `false` | `false` | 外部 Kloosterman/Type-II 输入只能在完成 trace family 且携带 signed defect 后使用。 | ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefect |
| `TargetAffineRowClosureReached` | `false` | `false` | 本层剪掉普通 additive saving 假出口，但不证明行级正性。 | ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefect OR PointwiseSqrtPrimeInputCOne |

## 2. 有限行 Fourier 防火墙审计

| P | k | owners | survivors | complete=-1 | ordinary bounds allow full-cover |
| ---: | ---: | ---: | ---: | --- | --- |
| 31 | 25 | 28 | 2 | `true` | `true` |
| 101 | 73 | 93 | 7 | `true` | `true` |
| 251 | 108 | 232 | 18 | `true` | `true` |
| 499 | 362 | 469 | 29 | `true` | `true` |
| 1009 | 905 | 956 | 52 | `true` | `true` |
| 2003 | 1256 | 1889 | 113 | `true` | `true` |
| 5003 | 4980 | 4742 | 260 | `true` | `true` |

## 3. 外部前沿适用性压力测试

| source | usable as closure | applicability note | url |
| --- | --- | --- | --- |
| Guth--Maynard, arXiv:2405.20552v2, New large value estimates for Dirichlet polynomials | `false` | not enough for a pointwise row of length P at x≈P^2, since x^(17/30)=P^(17/15)>P | https://arxiv.org/abs/2405.20552 |
| Le Duc Hieu, arXiv:2509.04883, APs of primes in short intervals beyond 17/30 | `false` | inherits theta>17/30; still above the required theta=1/2 scale | https://arxiv.org/abs/2509.04883 |
| Pascadi, arXiv:2511.08445, Non-abelian amplification and bilinear forms with Kloosterman sums | `false` | our modulus is prime P and current phase is additive e_P(hpm), not a completed inverse-variable Kloosterman family | https://arxiv.org/abs/2511.08445 |
| Shao--Shparlinski--Wijaya, 2025, Sums of Kloosterman sums over square-free and smooth integers | `false` | helpful only after a bridge to Kloosterman trace parameters; p-rough cofactor owner weights are not yet an admissible completed coefficient family | https://doi.org/10.1017/S0004972725100609 |

## 4. 下一手

```text
old_gate_demoted=ProductWindowBilinearAdditivePhaseSavingOrPDEC
selected_next_primary_gate=ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC
selected_parallel_trace_gate=ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefect
selected_parallel_distribution_gate=PointwiseSqrtPrimeInputCOne
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `28ce3b0607aadc806dd25c5e0ca36e48cf9c0826478b8900db0f9cca7bfa0169` |
| `docs/monograph/external-theorem-index.md` | `cc562010ef29c58669d0823bf797b5519262c9d3c70f4b4017a1053dff1a6d8c` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `d383e088a9ae8d8b32e21a7246d8aa3251b7594552c59dc02d139cab380c55cf` |
| `docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json` | `3a8f50d512a77ad9eeb8f113226fd0e1c3e33e6637b4accec90f77f381195780` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json` | `f1f62e09e90bf4af6eeee23095f8bb3e5f707d8211d3f328781bf1bce6a62a6f` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json` | `a394e6c16817f5d5e043053cc8d983738650385abb058bb01dea9e70a54e12d5` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json` | `15a238a2621cc6d5585299ce86fe08bc22bb6dc205b5a346dac45f948bd89a44` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `e9eaaba57413e2f3c70b4a1dfb88cbd3dcb2e41337b2cfc3b90731b454e88acf` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `3707999f3c5aad173af5d7b239e0a1745f4665cdcbb1fea50a0dbf2fe86f77d8` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `d408c7b49f1ebdfefea21ad4a6438555aa07c5e7ff9b4b9ab4c711a7393dc91e` |
| `experiments/prime_matrix_phi_lpf_product_window_additive_saving_firewall_router.py` | `b570f1101d55222c510a8599c9d20870304e684a381fbef91bc3e6611a59697e` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `2fc8a91088a2f4a202c328338b6c77406e9b4a010ccc592b495233483d808cf9` |
