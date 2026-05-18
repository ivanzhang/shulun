# Prime Matrix strict forward source-root 终端环同步证书

**状态：** `forward_source_root_internal_route_reduced_to_terminal_cycle_open`

本步直接攻击 `ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn`。把 common packet、signed-lane 闭环、new primitive/source-rank、cycle-cut/terminal descent、antisplit ExactUV 原子化、逐点 primitive 核表、alpha row unsigned skeleton、signed-lift 回流和 anchor-collar 过载回流全部同步后，source-root 在当前语料中没有留下独立非循环证明路线。signed 路线闭环；new primitive 与 terminal descent 汇到 source-rank/no-collapse；alpha 的 unsigned 几何骨架已闭合，但 signed lift 与 overloading 都回到终端容量门。因而最新严格剩余从 source-root 改写为 direct PDEC 同集作用域，或一个不再借用 NCBLK/source-root 的非循环 Kuznetsov/DLS 证明，并仍需高段模型、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。

```text
forward_source_root_packet_proved=false
forward_source_root_independent_after_router=false
signed_lane_self_proof_eliminated=true
source_rank_paths_converged_to_pointwise_kernel=true
alpha_unsigned_skeleton_closed=true
signed_lift_branch_recycles_to_terminal_gap=true
anchor_collar_overload_return_schema_closed=true
row_column_unconditional_closed=false
```

## 1. 终端环

```text
ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn
  -> common packet downstream
  -> signed-lane cycle or ExactUV/source-rank atoms
  -> new primitive / terminal descent absorbed to source-rank
  -> pointwise primitive alpha/delta kernel table
  -> alpha row formula
  -> unsigned skeleton closed
  -> signed lift returns to terminal capacity
  -> anchor-collar overload returns to terminal capacity
  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ForwardSourceRootTargetActive` | `true` | `false` | 上一轮把 NCBLK/source anti-atom 的 actual 路线压到 forward source-root packet。 | ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn |
| `SourceDeclarationDownstreamImported` | `true` | `false` | source-root 展开后进入 common packet 下游：signed pairing 与 ExactUV entropy/fiber 两线。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `SignedLaneCycleClosed` | `true` | `true` | built-in pairing、branch trace、payload origin 与 common packet 已闭成 signed-lane 自证环。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR terminal/PDEC/external input |
| `NewPrimitiveAbsorbedToSourceRank` | `true` | `false` | new primitive 若要破环，必须携带 actual source-rank/no-collapse 包；它不是独立证明点。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `SourceEntropyCycleGuardImported` | `true` | `true` | source-domain entropy 下钻后进入 seed coordinate-source cycle，不能自证。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR terminal descent |
| `CycleCutTerminalDescentUnified` | `true` | `false` | cycle-cut、terminal descent 与 PDEC 内部线被统一到 joint declaration line 或条件终端输入。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `AntiSplitTraceExactUVAtomized` | `true` | `false` | 反分裂 built-in pairing 又回到 signed trace cycle；ExactUV 被拆成 signed row law、complete key 与 fixed-key multiplicity。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `SourceRankConvergesToPointwiseKernel` | `true` | `false` | new primitive、terminal descent、source entropy 与 key/fiber 线汇到同 formal-unit 逐点 primitive alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `PointwiseKernelSplitImported` | `true` | `false` | 逐点核表已拆成 alpha row 发射、独立权重恒等式、同表 rank/multiplicity 三腿。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `AlphaUnsignedSkeletonClosed` | `true` | `true` | source tuple、carry-shell、P 列距离和 layered-wheel 已给出 unsigned row skeleton。 | signed coefficient lift and overload return remain |
| `SignedLiftReturnsToTerminalGap` | `true` | `false` | signed lift 经 signed weight law 与 independent identity taxonomy 回到 moving-block/NCBLK，再回终端容量门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND HighSegmentModelGapAlpha043C3AnalyticLedger |
| `AnchorCollarOverloadReturnSchemaClosed` | `true` | `true` | anchor-collar 过载没有专属第四出口，只能进入 PDEC/SAE/ColumnCRT/LocalSurvivor/CleanKLS 终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND HighSegmentModelGapAlpha043C3AnalyticLedger |
| `ForwardSourceRootSubsumedByTerminalCycle` | `true` | `true` | 当前语料中的 source-root 内部路线全部回到 signed/source-rank/alpha 终端环；source-root 不再是独立主攻名。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND HighSegmentModelGapAlpha043C3AnalyticLedger |
| `TerminalSplitStillOpen` | `true` | `false` | PDEC/CleanKLS 终端已二分为 direct PDEC scope 或 clean Kuznetsov/DLS；两臂仍未证明。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `CleanKLSArmWouldCycleIfUsingNCBLKSourceRoot` | `true` | `true` | CleanKLS/KZ-DLS 既有自足路线压到 NCBLK；若再用 source-root 线闭合，就回到本环。 | NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只封住 source-root 自足回环；direct PDEC scope、非循环 KZ/DLS、高段模型、Rate 与 DStructure 仍未证明。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新剩余

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse) AND HighSegmentModelGapAlpha043C3AnalyticLedger
```

严格活动基：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

并行保留：

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 诚实边界

- 本证书不证明 source-root packet，也不证明终端 PDEC/CleanKLS。
- 它只说明当前内部 source-root 证明路线会回到终端容量环，不能作为非循环闭合。
- CleanKLS/KZ-DLS 若再经 NCBLK/source-root 闭合就是同一环；需要非循环 KZ/DLS 证明或 direct PDEC scope。
- 高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_forward_source_root_terminal_cycle_sync_router.py` | `720723160fa1029e9c2fe42eaa69b811f2299300dcf5bfbf09658a636ac8915f` |
| `docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json` | `11d509967f5a92a50caed11e4ed4aa65a2cbaea07eaa99217c2e93391cda60d5` |
| `docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json` | `6f2a1790c735dacb3d3c3104dd6ae6469abe97a23853e073a57fb4990e4bf769` |
| `docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json` | `17e1966e5e4dad0a168abc867d451291be4991c999f28bfbaf494d5875447bf1` |
| `docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json` | `3194b1509c245cd42f607bbab6b96a1e17420454c3ae40245fb859985d38a601` |
| `docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json` | `266319a61ccd56e74c500a1ab1e4f8ed3b977473de37b0c5647607bae3621b2a` |
| `docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json` | `aff83d09d39ccc932dbe3b23c954102c820d2b45ae72f7c9d50442e8a8c94dcd` |
| `docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json` | `72261ef1a6ba980a674636e9ec70064a59d827009b4fde0ae7acf06801c9d90e` |
| `docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json` | `8e147c15b7a2b06ea52c356a9571416ca0eabda9c6323d88df4aea94b7578064` |
| `docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json` | `3359bdbe51404005aec41ec0378840a4d114c235f20354ef488e2592e3f692c7` |
| `docs/monograph/prime-matrix-strict-pointwise-primitive-kernel-table-router.json` | `adb8a9e1e05a33dff6a5f5d1dd03cf2a86b8420d49be536c1ddffa77185afae1` |
| `docs/monograph/prime-matrix-strict-alpha-row-anchor-phase-formula-router.json` | `1da61d631c11df13e21c840516701954072e915d348b1ab4fd6bfb2fd3a0c6d8` |
| `docs/monograph/prime-matrix-strict-alpha-row-unsigned-skeleton-router.json` | `98f6fa7be381de7d3170bc0abf7e37bde6b1f87351c3ad4bc2c2d4ce62e71c87` |
| `docs/monograph/prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json` | `82df6d5ef928a1b15165e10e9237d5638702117c57e9a51ae00d0a8c4b7a9824` |
| `docs/monograph/prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json` | `bf22b3307b4e383ab103ae8fe55cd22a86dea4fd33a3ccc239cb2a5a4724d1f7` |
| `docs/monograph/prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json` | `e14fbe40cc8deea93426e43cb5f76ad32d7866365eb23af2de1150715498bd22` |
| `docs/monograph/prime-matrix-strict-alpha-anchor-collar-overload-return-router.json` | `b600b8c5cfef63321ee08c0fb80504e63d5ac808b3a60b494ff71d518a783d89` |
| `docs/monograph/prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json` | `9c97ae816a9b8840e743496fabd791c8792c136a547c0990010f31ea0a80f19d` |
| `docs/monograph/prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json` | `fb988aea08dcdf541574fa412e2e37254570b8ad688b010a6c0366c03c4e7270` |
