# Prime Matrix strict post-antisplit alpha 到终端叶子同步前沿

**状态：** `post_antisplit_alpha_frontier_synced_to_terminal_leaf_open`

本步把 post-antisplit 后暴露出的 alpha row 首攻点继续同步到已有更深前沿：alpha/weight/rank 三腿分攻是固定点，非递归逐点表的第一字段又会经旧 joint constructor 路线回到 signed-source 固定点并进入终端叶子。因此最新严格自足活动基更新为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode`，并行仍需 ExactUV incidence、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。

```text
post_antisplit_pointwise_frontier_imported=true
alpha_and_weight_legs_return_to_terminal=true
three_leg_separate_attack_fixed_point_imported=true
nonrecursive_pointwise_field_contract_imported=true
joint_constructor_old_route_returns_to_terminal_leaf=true
current_terminal_leaf_reduced=true
noncanonical_legal_mode_proved=false
acyclic_terminal_canonical_lock_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode
parallel_direct_attack_targets=ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem, RatePreservationLedger_FOR_moving_atom_packet, DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `post-antisplit source-rank convergence` | `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | post-antisplit 后的 source-rank/no-collapse 路线已汇合到逐 primitive alpha/delta 核表。 |
| `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | 逐点核表分成 alpha 发射、权重恒等式和同表 rank/multiplicity 三腿。 |
| `AlphaRowAnchorPhaseEmissionFormulaLedger / IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger` | `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` | alpha 腿和权重恒等式腿单独下钻都会回到 PDEC/CleanKLS 终端门。 |
| `SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | rank/multiplicity 腿要求同一张 primitive source table，不能独立闭合。 |
| `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | `NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn` | 三腿分攻是固定点；必须一次性正向构造非递归逐点表。 |
| `NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn` | `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple` | 非递归逐点表的第一生产性字段是显式 joint alpha/delta constructor rule。 |
| `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple` | `signed-source fixed point -> terminal leaf firewall` | 若没有新公式工件，joint constructor 旧展开回到 signed-source 固定点，再进入终端叶子。 |
| `terminal leaf firewall` | `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode` | 当前已物化 PDEC/sparse 前沿清零后，活动终端叶子剩 canonical-lock 或 noncanonical legal mode。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PostAntiSplitPointwiseFrontierImported` | true | false | post-antisplit source-rank/no-collapse 前沿已汇合到逐 primitive alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `AlphaAndWeightLegsReturnToTerminal` | true | false | alpha row 公式腿与 signed weight/identity 腿单独攻击都会回到 PDEC/CleanKLS 终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `ThreeLegSeparateAttackFixedPointImported` | true | true | 三腿逐项攻击只会在 source table、alpha signed lift、PDEC/CleanKLS 之间循环。 | NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn |
| `NonrecursivePointwiseFieldContractImported` | true | true | 非递归逐点表字段边界已闭合；第一生产性字段是显式 joint constructor rule。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `JointConstructorOldRouteReturnsToTerminalLeaf` | true | false | 若没有新的 actual joint constructor 公式工件，旧 joint 路线回到 signed-source 固定点并进入终端叶子。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `CurrentTerminalLeafReduced` | true | false | 当前已物化 PDEC/sparse 前沿清零后，活动终端叶子只剩 canonical-lock 或 noncanonical legal mode。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `NoncanonicalLegalModeStillOpen` | true | false | noncanonical full-S 合法模式仍需实际源恒等、强化反原子或外部合同；strict 自足线未闭合。 | NoncanonicalFullSComplementLegalClosureMode |
| `ExactUVIncidenceStillParallel` | true | false | 非递归核表和终端叶子路线仍需 actual exact-UV bounded multiplicity incidence。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `DStructureGateStillOpen` | true | false | DStructure/Rankin 晋级门仍只完成边界命名，未独立接受。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | false | false | 本步只完成 post-antisplit 到终端叶子的同步；未证明 canonical-lock、noncanonical legal mode、ExactUV、RatePreservation 或 DStructure。 | row/column theorem still open |

## 3. 当前严格活动基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 结论边界

- 本文件只同步当前前沿，不证明行/列命题。
- alpha 单腿、weight 单腿、rank 单腿和旧 joint constructor 展开都不能作为非循环闭合。
- 当前必须继续攻 canonical-lock 或 noncanonical legal mode，并同时保留 ExactUV、RatePreservation、DStructure/Rankin。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_post_antisplit_alpha_terminal_leaf_sync_router.py` | `2ce99a50b00ab79c399c9f45c033715acac3543fcfd1c40d35541591d511033c` |
| `docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json` | `3359bdbe51404005aec41ec0378840a4d114c235f20354ef488e2592e3f692c7` |
| `docs/monograph/prime-matrix-strict-kernel-table-three-leg-return-sync-router.json` | `e4affac784b5c0b6339af5e70349d4c4f3d98a7a8e281677515e9f32cbb055e3` |
| `docs/monograph/prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json` | `7d40995ed78a090c3131871fde596f8f5d371891a778d697f92d9c34500cb913` |
| `docs/monograph/prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json` | `50065f545c9e86d1a58a7b96146b0c8b754ddfec187bcc15fa64c802c90f4c0e` |
| `docs/monograph/prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json` | `0fc58bc6e2dd57498614ed4535b5973daa1a78ecc086731a3e6e02a997888c75` |
| `docs/monograph/prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json` | `25a526808da942ef0d50d5725ae59e945b6152b345a31cd8e92c16130ee9c362` |
| `docs/monograph/prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json` | `3323fe284f3293bb2a9fb18f739c41ffb64a5bebb44b847ae97d2d6074568f3f` |
| `docs/monograph/prime-matrix-strict-noncanonical-legal-closure-mode-router.json` | `39c772b9e02029d14e9d400ba3651f1d51472f3d83e45740fd773e0de29e7130` |
| `docs/monograph/prime-matrix-strict-exact-uv-map-rank-incidence-router.json` | `101917e6a573efb2d6c921b2056ac92120e41f1b10ae2549f394ac0fa3d1b54c` |
| `docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.json` | `6a25a769df2b107f8a5a31e1374395d99717c4d0dd8188c969111477a648de7a` |
