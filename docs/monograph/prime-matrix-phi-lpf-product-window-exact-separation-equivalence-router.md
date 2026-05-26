# Prime Matrix Phi-LPF product-window exact separation 等价边界

**状态：** `exact_coefficient_separation_demoted_to_survivor_equivalence`
**核验日期：** `2026-05-26`

Product-window 的 exact coefficient separation 若只是说 owner measure 不等于完整非零剩余类 measure，则它与 prime survivor 非空完全等价。Fourier 形式同样如此：owner-complete defect 等于负 survivor measure，非零频率 Parseval 能量为 P*s-s^2，正性当且仅当 survivor 数 s>0。因此本层把 standalone exact separation/subunit Fourier contradiction 降级为循环门；下一步必须在 pushforward 前构造独立 signed defect，或完成带 defect 的 trace/Type-II family，或输入 C=1 sqrt 级点态素数定理，或给出非平凡 PDEC。

```text
source_firewall_imported=true
fourier_inversion_defect_identity_closed=true
exact_coefficient_separation_equivalent_to_survivor_nonempty=true
subunit_or_nonminusone_fourier_contradiction_equivalent_to_survivor_nonempty_without_independent_defect=true
standalone_exact_separation_rejected_as_noncircular_primary_gate=true
independent_signed_defect_emission_proved=false
row_column_unconditional_closed=false
```

## 1. 合同门

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OwnerCompleteDefectFourierInversionIdentity` | `true` | `true` | owner-complete defect equals negative survivor measure; Parseval energy is P*s-s^2. | identity only |
| `ExactCoefficientSeparationAsStandaloneClosure` | `true` | `false` | standalone exact separation is equivalent to survivor nonempty and cannot be used as independent proof. | IndependentSignedDefectEmissionBeforeProductWindowPushforward |
| `SubunitFourierContradictionAsStandaloneClosure` | `true` | `false` | without an independent source for the defect, Fourier non-minus-one/subunit contradiction is the same row prime statement. | IndependentSignedDefectEmissionBeforeProductWindowPushforward |
| `IndependentSignedDefectEmissionBeforeProductWindowPushforward` | `false` | `false` | 需要在 Fourier pushforward 前产生独立 signed defect，不是事后用 survivor 定义 defect。 | IndependentSignedDefectEmissionBeforeProductWindowPushforward OR NonTautologicalProductWindowPDEC |
| `ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients` | `false` | `false` | 需要把 signed defect 完成到可套用 FKMS/DI/BFI/Pascadi 类 theorem 的 coefficient/trace family。 | ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients |
| `TargetAffineRowClosureReached` | `false` | `false` | 本层只排除 exact separation 的循环用法，不证明行级正性。 | IndependentSignedDefectEmissionBeforeProductWindowPushforward OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne OR NonTautologicalProductWindowPDEC |

## 2. 有限行等价审计

| P | k | owners | survivors | energy identity | separation iff survivor | nonzero defect freqs |
| ---: | ---: | ---: | ---: | --- | --- | ---: |
| 31 | 25 | 28 | 2 | `true` | `true` | 30 |
| 101 | 73 | 93 | 7 | `true` | `true` | 100 |
| 251 | 108 | 232 | 18 | `true` | `true` | 250 |
| 499 | 362 | 469 | 29 | `true` | `true` | 498 |
| 1009 | 905 | 956 | 52 | `true` | `true` | 1008 |
| 2003 | 1256 | 1889 | 113 | `true` | `true` | 2002 |
| 5003 | 4980 | 4742 | 260 | `true` | `true` | 5002 |

## 3. 外部 trace 前沿适用性

| source | usable now | missing bridge | url |
| --- | --- | --- | --- |
| Fouvry--Kowalski--Michel--Sawin, arXiv:2511.09459, Bilinear forms with trace functions | `false` | our current defect is an owner-minus-complete coefficient on product-window residues, not yet an l-adic trace sheaf family with admissible coefficient norms | https://arxiv.org/abs/2511.09459 |
| Pascadi, arXiv:2511.08445, Non-abelian amplification and bilinear forms with Kloosterman sums | `false` | our modulus is prime P and the phase is additive product-window defect, not completed inverse-variable Kloosterman data | https://arxiv.org/abs/2511.08445 |
| Guth--Maynard and Hieu short-interval inputs | `false` | target row at x≈P^2 requires theta=1/2 with constant C<=1 | https://arxiv.org/abs/2405.20552 |

## 4. 下一手

```text
old_gate_demoted=ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC
selected_next_primary_gate=IndependentSignedDefectEmissionBeforeProductWindowPushforward
selected_parallel_trace_gate=ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
selected_parallel_distribution_gate=PointwiseSqrtPrimeInputCOne
selected_parallel_pdec_gate=NonTautologicalProductWindowPDEC
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `2339a9b21dafab0c902f9f9dbce04e0ee167b1a7a4d310583b2d162607d281fc` |
| `docs/monograph/external-theorem-index.md` | `0ea139a9dbcfc2d201ee62389dcd2ee8e3046e3c21002bebe35340fb06852609` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `6b6d1a08f2f1cd26fdcd1abd0b8ffc45df2e897a5eecfdd52fb82044223f1bbd` |
| `docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json` | `127e2a68aa49568ecc36f2ea3c2b048a396d1e3cd58ccb3bdb7dd7df9b49b8b9` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.json` | `c47579ae37b423858dfc6012233069b3bc33206cd97f1c82dd9b8551eeeb15db` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json` | `15a238a2621cc6d5585299ce86fe08bc22bb6dc205b5a346dac45f948bd89a44` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `88e33b9706410e3123154fbc60ea8f1d6bd797e47bba9a348c75aa19f4a1a5b4` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `616e8632cb24556122f7e618ba8931e820425cd0f7d2e114e25a2775ffb1c28e` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `0a59c71d7af222b71b8431d5bc821c3850ec8c6005804447172b66f1b51a81c0` |
| `experiments/prime_matrix_phi_lpf_product_window_exact_separation_equivalence_router.py` | `e57347c045dccf28b7972c2910b1a671a088ea511345f35ea8762fe9027f6cc1` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `60c852f9e24eab7e6e206d01f9e8811d3b7e84c37daf44220b1b1f04d71a6346` |
