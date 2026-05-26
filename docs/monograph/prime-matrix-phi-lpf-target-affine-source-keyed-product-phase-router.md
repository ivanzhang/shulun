# Prime Matrix Phi-LPF target-affine source-keyed product phase 路由

**状态：** `source_keyed_owner_phase_emission_closed_to_product_window_phase`
**核验日期：** `2026-05-26`

Source-keyed owner phase 的代数发射式已经闭合：每个 LPF owner 元素 n=pm=kP+r 都满足 r≡pm mod P，因此 offset Fourier phase 可无损改写为 source-keyed product-window phase e_P(hpm)。这是真推进，因为抽象 source key 已变成显式 (p,m) product phase；但它仍只是恒等式。full-cover 时该 product residue 集会成为 F_P^* 的排列，非零频率和等于 -1。要非循环突破，下一步必须证明 ProductWindowBilinearAdditivePhaseSaving/PDEC，或把这个双曲 product-window 完成到外部 trace/Kloosterman/Type-II 可接受的系数族，或输入 C=1 sqrt 级点态素数定理。

```text
target_affine_source_keyed_product_phase_synced=true
source_keyed_owner_phase_emission_formula_closed=true
finite_product_phase_identity_all_ok=true
product_window_bilinear_additive_phase_saving_proved=false
product_window_to_completed_kloosterman_bridge_proved=false
row_column_unconditional_closed=false
```

## 1. 合同门

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SourceKeyedProductWindowPhaseEmissionIdentity` | `true` | `true` | 对每个 owner key n=pm=kP+r，offset phase e_P(hr) 精确等于 product phase e_P(hpm)。 | identity only |
| `FullCoverProductPhaseEquation` | `true` | `false` | 若 full cover 成立，则 owner product residues 是 F_P^* 的排列，所有非零频率和为 -1。 | ProductWindowBilinearAdditivePhaseSavingOrPDEC |
| `ProductWindowBilinearAdditivePhaseSavingOrPDEC` | `false` | `false` | 需要证明目标 product-window rough-owner 集不可能模拟全体非零 residue，或给出符号节省。 | ProductWindowBilinearAdditivePhaseSavingOrPDEC OR named PDEC/SAE/LocalSurvivor |
| `ProductWindowToCompletedKloostermanOrTraceBridge` | `false` | `false` | 当前相位是 e_P(hpm) 与双曲窗口；不是已完成的 inverse-variable Kloosterman family。 | ProductWindowToCompletedKloostermanOrTraceBridge |
| `LPFOwnerRoughCofactorWeightsToTypeIICoefficients` | `false` | `false` | p-rough cofactor weights 还没有转成外部 Type-II theorem 可接受的 well-factorable 系数。 | LPFOwnerRoughCofactorWeightsToTypeIICoefficients |
| `TargetAffineRowClosureReached` | `false` | `false` | 本层关闭 source-keyed emission identity，但不证明行级正性。 | ProductWindowBilinearAdditivePhaseSavingOrPDEC OR ProductWindowToCompletedKloostermanOrTraceBridge OR PointwiseSqrtPrimeInputCOne |

## 2. 有限行 product phase 审计

| P | k | owner keys | survivors | identity | rough | window | max phase error |
| ---: | ---: | ---: | ---: | --- | --- | --- | ---: |
| 31 | 25 | 28 | 2 | `true` | `true` | `true` | 0.0 |
| 101 | 73 | 93 | 7 | `true` | `true` | `true` | 0.0 |
| 251 | 108 | 232 | 18 | `true` | `true` | `true` | 0.0 |
| 499 | 362 | 469 | 29 | `true` | `true` | `true` | 0.0 |
| 1009 | 905 | 956 | 52 | `true` | `true` | `true` | 0.0 |
| 2003 | 1256 | 1889 | 113 | `true` | `true` | `true` | 0.0 |
| 5003 | 4980 | 4742 | 260 | `true` | `true` | `true` | 0.0 |

## 3. 下一手

```text
selected_next_primary_gate=ProductWindowBilinearAdditivePhaseSavingOrPDEC
selected_parallel_trace_gate=ProductWindowToCompletedKloostermanOrTraceBridge
selected_parallel_typeii_gate=LPFOwnerRoughCofactorWeightsToTypeIICoefficients
selected_parallel_distribution_gate=PointwiseSqrtPrimeInputCOne
```

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `bb5f6c2c0394dc15be36f0b06139b1137f360621fce599f29a11a50264d1fbfc` |
| `docs/monograph/external-theorem-index.md` | `8f6f6c542b3aaf42beaac4f001b26edecac66ff177d64e6447a42f78d74d7731` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `bb30c0650ea80fb537b0aa401f48d57ef4e9e4bb0a7b33571fee287c16760109` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json` | `f1f62e09e90bf4af6eeee23095f8bb3e5f707d8211d3f328781bf1bce6a62a6f` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json` | `a394e6c16817f5d5e043053cc8d983738650385abb058bb01dea9e70a54e12d5` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json` | `68d92a76de9afa0228d9e9dae12de19bb4b8189e69397c66c7d967ce4b915b0e` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `19e44c42b1e43a77d5ab8d518f2d2f0de51544be4e174251df37ccadbc31ab25` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `9c0d5623e85fef7fe004caff27f6f00f68af083d6d51527414bbb5d2457f69b7` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `97fe483cf602d3f1d68d59f7241970440fd0aef1c3fd0be19d4ca1be7256d036` |
| `experiments/prime_matrix_phi_lpf_target_affine_source_keyed_product_phase_router.py` | `054bd7ec21a5691e4565df90c6986c123d85752b7868904c5124f57278c963f8` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `233bff8d8bec71f508b95e0ca83676664453f2e4c9b0893f1fda545f2289dc33` |
