# Prime Matrix strict alpha-return bridge 到具体终端分裂同步证书

**状态：** `alpha_return_bridge_synced_to_concrete_terminal_split_open`

当前 `canonical-lock OR independent actual-source bridge` 二选一还能继续压缩。independent bridge 侧的 A1 admission 被吸收为 scoped 陈述，exact entropy 侧必须提交无环 pre-Cauchy seed 与独立 pair L2/max-atom 能量界；canonical-lock 侧则被直攻压到Kuznetsov/DLS 或 PDEC/CleanKLS+模型余量。故最新具体终端分裂为 `(AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger)`；行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
alpha_return_bridge_imported=true
independent_bridge_concrete_atoms_imported=true
a1_admission_absorbed_as_scoped_only=true
exact_entropy_reduced_to_seed_and_pair_energy=true
canonical_lock_direct_attack_imported=true
concrete_terminal_split_pinned=true
row_column_unconditional_closed=false
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn` | `canonical-lock arm OR independent actual-source arm` | 上一层只说明二选一；本轮分别下钻两条手臂。 |
| `IndependentActualSourceBridgeNotFactoredThroughAlphaReturn` | `A1CleanBranchCanonicalSourceAdmission OR ExactCleanCoreFullSNonAPWFDSourceEntropy` | actual-source 桥已具体化为 clean A1 源准入或 actual clean-core exact entropy。 |
| `A1CleanBranchCanonicalSourceAdmission` | `scoped A1 branch statement, not global contradiction` | A1 准入只能给 scoped canonical 陈述，不能单独关闭 unrestricted noncanonical 分支。 |
| `ExactCleanCoreFullSNonAPWFDSourceEntropy` | `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed` | exact entropy 若走 ExactUV 支撑路线，必须给无环 pre-Cauchy seed 和独立 pair L2/max-atom 能量界。 |
| `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary` | `(PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` | canonical-lock 直攻只给 scoped 吸收；mismatch 出口同步到 PDEC/CleanKLS+模型余量或自足 Kuznetsov/DLS。 |
| `signed source / alpha weight / pointwise routes` | `terminal-family backedge` | 这些旧路线继续下钻会回到 PDEC/CleanKLS 或 signed-source 固定点，不能当作新进展量。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AlphaReturnBridgeImported` | `true` | `false` | 上一层已把 terminal atoms 同步到 canonical-lock 或 alpha-return 前独立 actual-source 桥。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn |
| `IndependentBridgeConcreteAtomsImported` | `true` | `false` | 独立 actual-source 桥继续压成 clean A1 source admission 或 exact clean-core source entropy。 | A1CleanBranchCanonicalSourceAdmission OR ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `A1AdmissionAbsorbedAsScopedOnly` | `true` | `true` | A1 canonical source admission 只是 scoped 分支陈述，不能作为独立全局矛盾。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `ExactEntropyReducedToSeedAndPairEnergy` | `true` | `false` | exact entropy 支撑路线不能用 moving-atom/source-entropy 自身回证 pair energy。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `SourceDomainEntropySignedRowRouteStillBackedge` | `true` | `false` | source-domain entropy 的 signed row 下钻仍缺 pre-Cauchy signed coefficient law，并回到终端家族。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `ActualSourceAntiAtomSyncedBackToTerminalFamily` | `true` | `false` | 强化反原子线若继续下钻，会经 ExactUV/pair-energy/seed 回到 strict acyclic 终端家族。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `CanonicalLockDirectAttackImported` | `true` | `false` | canonical-lock 直攻没有闭合；等式真时只是 scoped 吸收，mismatch 进入 DLS/PDEC/命名回流。 | (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `KuznetsovDLSStillOpen` | `true` | `false` | clean DLS 形式层已压到自足 Kuznetsov/DLS 大筛不等式，但该不等式未证。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `PDECCleanKLSStillOpen` | `true` | `false` | PDEC/CleanKLS 标签仍需同集作用域、内部大筛和模型余量，不能当黑箱。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `CurrentConcreteTerminalSplitPinned` | `true` | `false` | 当前二选一已同步为 pair-energy seed 线、Kuznetsov/DLS 线、PDEC/CleanKLS+模型余量线三类具体硬点。 | (AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger) |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成具体终端分裂同步；尚未证明 seed+pair energy、Kuznetsov/DLS、PDEC/CleanKLS+模型余量、Rate 或 DStructure。 | ((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger)) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新具体终端分裂

```text
((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger))
```

rate-packet 口径下仍需：

```text
((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger)) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格自足高段尾项口径下为：

```text
((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger)) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

```text
IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

并行保留 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn`、自足 Kuznetsov/DLS 大筛，以及 PDEC/CleanKLS+模型余量。不能把 A1 scoped 陈述、旧 signed-source/alpha 回边、PDEC/CleanKLS 标签或 canonical-lock mismatch 登记当成闭合证明。
