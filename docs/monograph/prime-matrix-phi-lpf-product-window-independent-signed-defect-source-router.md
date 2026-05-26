# Prime Matrix Phi-LPF product-window independent signed defect 来源账本

**状态：** `independent_signed_defect_rebased_to_phi_lpf_bucket_signed_law`
**核验日期：** `2026-05-26`

Product-window 的独立 signed defect 不能来自 survivor 后验定义，也不能由无符号 LPF/Phi support、owner 分桶、rough cofactor split 或 product phase identity 自动产生。若不输入点态 sqrt 素数定理或非平凡 PDEC，则它等价于提交一个真正的 Phi-LPF bucket signed coefficient law：在 pushforward 前对每个 `(p,m)` 给出 signed coefficient、local factor、orientation/source key 与 prepushforward sum identity。因此最新主攻从抽象 IndependentSignedDefectEmission 精确 rebased 到 PhiLPFBucketSignedCoefficientLawBeforePushforward，并行替代为逐点 signed table、rough-cofactor signed transport 或带 signed defect 的 completed trace/Type-II bridge。

```text
product_window_exact_equivalence_imported=true
survivor_defined_defect_rejected_as_circular=true
unsigned_lpf_phi_support_cannot_emit_independent_signed_defect=true
independent_signed_defect_source_equivalent_to_phi_lpf_bucket_signed_law=true
completed_trace_bridge_requires_signed_defect_first=true
row_column_unconditional_closed=false
```

## 1. 必要 payload 字段

| field | meaning |
| --- | --- |
| `owner_key` | 产品窗口中的 LPF owner key `(p,m)`，满足 `pm=kP+r` 且 `m` 为 `p`-rough。 |
| `signed_coefficient` | 在读取 survivor 前正向给出的系数 `a_{p,m}`；不能由 `1_S` 或 `1_O-1_*` 后验定义。 |
| `local_factor` | 与 LPF/Phi 递推、rough cofactor 乘法、截断端点兼容的局部因子。 |
| `orientation_and_branch` | sign/orientation、alpha-delta side、branch key 的传输规则。 |
| `source_identity` | pre-Cauchy/source-domain 的同 formal unit 求和恒等式，不经过 payment skeleton 反推。 |
| `pushforward_identity` | 推前到 product-window row phase 后给出目标 signed defect 的等式。 |
| `admissible_norms` | 若走 trace/Type-II 路线，需要系数范数、导子、factorability、区间范围可被外部 theorem 接受。 |
| `return_tag` | 若字段缺失、冲突、后验依赖或退化为 survivor 等价式，必须进入 PDEC/SAE/terminal 命名回流。 |

## 2. 来源门状态

| source | closed | proved | status | reason | remaining |
| --- | --- | --- | --- | --- | --- |
| survivor-defined defect | `true` | `false` | rejected as circular | exact-equivalence 证书已证明 owner-complete defect = -survivor measure。 | `IndependentSignedDefectEmissionBeforeProductWindowPushforward` |
| unsigned LPF/Phi support and capacity | `true` | `false` | cannot emit sign | support stripping 只关闭无符号支撑/容量；signed coefficient、local factor、orientation 未给出。 | `PhiLPFBucketSignedCoefficientLawBeforePushforward` |
| row-origin fixed-point table | `true` | `false` | fixed-point self-certification rejected | row-origin/bucket-law 同步把 hardpoint 接回 bucket signed law。 | `PhiLPFBucketSignedCoefficientLawBeforePushforward` |
| rough cofactor transport | `true` | `false` | formal split closed, signed multiplier open | bucket transport 已闭合 cofactor split，但没有 `a_p(qm)` 的 signed transport law。 | `(PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward) AND PhiLPFBucketPrepushforwardSignedSumIdentity` |
| pointwise Phi-LPF signed table | `false` | `false` | sufficient but not submitted | 逐点表若给出可直接作为独立 defect 来源；当前语料标记为 open。 | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` |
| constructor bucket transport stack | `true` | `false` | rebase imported, side gates still open | bucket stack 需要 edge multiplier/source 三原子、signed survival、row-mass/no-heavy-row 等合取门。 | `((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |
| completed trace / Type-II bridge | `false` | `false` | requires signed coefficients first | 没有 independent signed coefficients 时，外部 trace/Kloosterman theorem 无对象可作用。 | `ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients` |
| non-tautological product-window PDEC | `false` | `false` | parallel escape, not materialized | 必须不是两点 Fourier tautology 或 survivor 等价式；需要同 formal unit 缺陷能量阈值。 | `NonTautologicalProductWindowPDEC` |
| pointwise sqrt prime input | `false` | `false` | external distribution route | 若能输入 `C=1` sqrt 级点态素数定理，可绕过 signed defect；当前未有。 | `PointwiseSqrtPrimeInputCOne` |

## 3. 有限行 sign ambiguity 审计

| P | k | owner keys | survivors | sign-shadow bits | log10 sign-shadow | unsigned determines signed defect |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 25 | 28 | 2 | 28 | 8.42884 | `false` |
| 101 | 73 | 93 | 7 | 93 | 27.99579 | `false` |
| 251 | 108 | 232 | 18 | 232 | 69.838959 | `false` |
| 499 | 362 | 469 | 29 | 469 | 141.183068 | `false` |
| 1009 | 905 | 956 | 52 | 956 | 287.784676 | `false` |
| 2003 | 1256 | 1889 | 113 | 1889 | 568.645662 | `false` |
| 5003 | 4980 | 4742 | 260 | 4742 | 1427.484239 | `false` |

## 4. 外部 theorem 对象条件

| input | usable now | needed project object | current status | url |
| --- | --- | --- | --- | --- |
| Fouvry--Kowalski--Michel--Sawin trace-function bilinear forms | `false` | l-adic trace family plus admissible coefficient norms from signed defect coefficients | no independent signed coefficient table, so not directly usable | https://arxiv.org/abs/2511.09459 |
| Pascadi / DI-BFI / Kloosterman Type-II route | `false` | completed inverse-variable Kloosterman family with factorable signed coefficients | current product phase is additive and defect coefficients are not emitted before pushforward | https://arxiv.org/abs/2511.08445 |
| Pointwise short-interval prime route | `false` | theta((kP,(k+1)P))>0 at x≈P^2, length P, constant C<=1 | known frontier remains above the exact sqrt row scale or average-type | https://arxiv.org/abs/2405.20552 |

## 5. 下一手

```text
old_gate_rebased=IndependentSignedDefectEmissionBeforeProductWindowPushforward
selected_next_primary_gate=PhiLPFBucketSignedCoefficientLawBeforePushforward
selected_parallel_pointwise_gate=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
selected_parallel_transport_gate=PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward
selected_parallel_trace_gate=ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
selected_parallel_pdec_gate=NonTautologicalProductWindowPDEC
selected_parallel_distribution_gate=PointwiseSqrtPrimeInputCOne
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `e305b1b8ef7c54b57e78c79dd4d86c43f5250c8afe0080ab2090f83f1596bcb2` |
| `docs/monograph/external-theorem-index.md` | `210c28a742889ffeacd0e7f783586aeb61786b0f361607994040e10c629f650e` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `157b507b0f7401491c2510d1b3ea383dc852001587d3687de65e20820f5ec1ea` |
| `docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json` | `8f696d3cb025e8d98790530763d5b87717c945b57c310f6d16f4c49711c8fdcb` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.json` | `7657156a4bb570c3760b4f3588f0cc97d74f3ba2be64b4c9de604e428c02bade` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.json` | `45350f4ae7118c3a246ebede5e8c0f108b8b149949fc142f6b86fdd38ebd0123` |
| `docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json` | `127e2a68aa49568ecc36f2ea3c2b048a396d1e3cd58ccb3bdb7dd7df9b49b8b9` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.json` | `b43385be1930cc180946c5db0028ed1f8bc4da881080b7b62ac127ccb9a940db` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json` | `15a238a2621cc6d5585299ce86fe08bc22bb6dc205b5a346dac45f948bd89a44` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `e9b93da6eb46ca350cef15a36d90fb8a627645e7f88a61fcccc003a43c4940ec` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `2376257b7caf9dbfa9b4b20fa645ec34023810f7df4bdd17bf5a66002b67bc92` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `8c29dea47c58e159b2a1725eb8dec12addb4dfe7ce1f25da573bfe40861a6e2e` |
| `experiments/prime_matrix_phi_lpf_product_window_independent_signed_defect_source_router.py` | `2503e96990159dcea2b9e87645e763e7862c91cdb0a63eb684e156364c034af8` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `21dbb3603993ac78a8d3e586d403160df213e5f752fc2fdd2a3d74f99651b463` |
