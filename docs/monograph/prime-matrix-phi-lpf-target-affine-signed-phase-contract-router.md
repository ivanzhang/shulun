# Prime Matrix Phi-LPF target-affine signed phase contract 路由

**状态：** `target_affine_signed_phase_reduced_to_source_keyed_phase_or_sqrt_input`
**核验日期：** `2026-05-26`

target-affine signed phase 的第一层相位恒等式已经闭合：row Fourier defect 精确等于 prime survivor Fourier transform。但这只是等价检测；给出正下界仍等价于证明行内有素数。只使用 owner residue phase 会回到 prime-gap 等价式，直接使用 Lambda/Mobius 又变成 theta/psi 行输入。非循环突破必须正向构造 source-keyed owner phase emission formula，或把 owner fibers 完成到可用 trace/Kloosterman family，或输入真正 C=1 sqrt-scale 点态素数定理。

```text
target_affine_signed_phase_contract_synced=true
row_fourier_defect_identity_closed=true
row_fourier_positive_lower_bound_proved=false
source_keyed_owner_phase_emission_formula_proved=false
completed_trace_kloosterman_family_from_owner_fibers_proved=false
row_column_unconditional_closed=false
```

## 1. 合同门

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TargetAffineRowFourierDefectIdentity` | `true` | `true` | 对任意 h mod P，row indicator = owner composite indicator + prime survivor indicator。 | identity only |
| `RowFourierDefectPositiveLowerBound` | `true` | `false` | 非零 Fourier 能量等价检测 survivor；但给正下界仍等价于证明行内有素数。 | PointwiseSqrtPrimeInputCOne |
| `OwnerResiduePhaseOnlyPayload` | `true` | `false` | 只给 a_p=-kP mod p 或 offset Fourier 相位会回到 full-cover/prime-gap 等价式。 | SourceKeyedOwnerPhaseEmissionFormula |
| `LambdaMobiusRowPayload` | `true` | `false` | 若直接使用 Lambda 或 Mobius-Von-Mangoldt 行权重，就是 theta/psi 行输入，不是 LPF 内生证明。 | PointwiseSqrtPrimeInputCOne |
| `SourceKeyedOwnerPhaseEmissionFormula` | `false` | `false` | 必须正向给出依赖 owner key、source key、orientation、ExactUV 的相位发射公式。 | SourceKeyedOwnerPhaseEmissionFormula OR named PDEC/SAE/LocalSurvivor |
| `CompletedTraceKloostermanFamilyFromOwnerFibers` | `false` | `false` | 必须把 owner fibers 完成到真正 bilinear/trilinear trace 或 Kloosterman family。 | CompletedTraceKloostermanFamilyFromOwnerFibers |
| `ExternalKloostermanTraceInputsAdmissibleNow` | `true` | `false` | FKMS/MQW/Pascadi/Wright 等输入是候选，但当前对象还没有完成成它们需要的系数族。 | SourceKeyedOwnerPhaseEmissionFormula AND CompletedTraceKloostermanFamilyFromOwnerFibers |
| `TargetAffineSignedPhasePayloadProved` | `false` | `false` | 本步只固定 signed phase 的最小合同，不证明全局行级不等式。 | SourceKeyedOwnerPhaseEmissionFormula OR PointwiseSqrtPrimeInputCOne OR CompletedTraceKloostermanFamilyFromOwnerFibers |

## 2. 有限行 phase 审计

| P | k | primes | owner total | cover | max nonzero Fourier | parseval error |
| ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 31 | 25 | 2 | 28 | `true` | 1.989738647 | 0.0 |
| 101 | 73 | 7 | 93 | `true` | 5.247613004 | 0.0 |
| 251 | 108 | 18 | 232 | `true` | 12.812437924 | 0.0 |
| 499 | 362 | 29 | 469 | `true` | 18.484986504 | 0.0 |
| 1009 | 905 | 52 | 956 | `true` | 34.104549083 | 1e-09 |
| 2003 | 1256 | 113 | 1889 | `true` | 73.765790315 | 2e-09 |
| 5003 | 4980 | 260 | 4742 | `true` | 170.940382297 | 3.8e-08 |

## 3. 外部 trace/Kloosterman 输入接入口

| input | directly admissible now | usable after | source |
| --- | --- | --- | --- |
| Fouvry-Kowalski-Michel-Sawin bilinear trace functions | `false` | ell-adic trace family with monodromy/conductor data is constructed | https://arxiv.org/abs/2511.09459 |
| Milicevic-Qin-Wu bilinear Kloosterman sums | `false` | owner fibers become a two-variable Kloosterman sum modulo moving q | https://arxiv.org/abs/2511.07550 |
| Pascadi non-abelian amplification / composite Type-II | `false` | well-factorable composite-modulus Type-II coefficients are exposed | https://arxiv.org/abs/2511.08445 |
| Wright trilinear Kloosterman fractions | `false` | terminal payload becomes a trilinear convolution with equidistributed beta sequence | https://arxiv.org/abs/2604.25177 |

```text
selected_next_primary_gate=SourceKeyedOwnerPhaseEmissionFormula
selected_parallel_distribution_gate=PointwiseSqrtPrimeInputCOne
selected_parallel_trace_gate=CompletedTraceKloostermanFamilyFromOwnerFibers
selected_direct_table_gate=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `643f5cad187c396b5c1daba4fb6f6fdd027e8b1251fe74fe4f48caf1fe1b335a` |
| `docs/monograph/external-theorem-index.md` | `faf9970243ff90d4f8b9c5c1d8496a614a1c429e9f2b0cf8b162138d0c3b6f1d` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `0b395898191eb4e9f504e6617d0e30b5ca37d87851c4239b0cda89738abc032e` |
| `docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json` | `3a52ce41b6380ad6b884271d246183005d023c29eb162d745a54f668acb16120` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json` | `f1f62e09e90bf4af6eeee23095f8bb3e5f707d8211d3f328781bf1bce6a62a6f` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json` | `68d92a76de9afa0228d9e9dae12de19bb4b8189e69397c66c7d967ce4b915b0e` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `61bfc836860afe0da01eee3163b4b6d5be035bb75209b4de415ba61366ce0605` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `4b7665eef5896ba574ba635eb8e67c4d78481854f72a41b7d037f503e4a161fb` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `13a9ffb81186ec126ac6d2743937ed5edca284bd0ac20e545f52fc6c7c9d2d3d` |
| `experiments/prime_matrix_phi_lpf_target_affine_signed_phase_contract_router.py` | `74fc1e2050042fff6a4f7ce0a357e3359c37001eec3c1747f629400845010d69` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `8fa3c4ca62a9254f3d9d20980e93d5dd08816f88366c670ea14f1c27e5272145` |
