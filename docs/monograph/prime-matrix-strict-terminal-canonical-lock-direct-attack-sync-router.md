# Prime Matrix strict 终端 canonical-lock 直攻同步证书

**状态：** `strict_terminal_canonical_lock_attacked_to_mismatch_or_dls_open`

本轮直接攻 canonical-lock。结论是：canonical T1 等式成立时只给 scoped canonical 吸收，不给全局矛盾；等式不成立时，mismatch 已无静默出口，只能进入 signed source、命名回流或 clean DLS。signed lift 失败登记纪律已闭合，但出口排斥未证；clean DLS 又精确压成自足 Kuznetsov/DLS 大筛原子。direct PDEC 作用域审查仍未证明 acyclic 同集匹配。因此 canonical-lock 不是当前闭合出口，行/列命题仍未无条件闭合。

```text
canonical_lock_direct_attack_boundary_closed=true
canonical_equality_case_absorbed_scoped_only=true
mismatch_no_silent_exit_closed=true
signed_lift_failure_return_ledger_closed=true
acyclic_terminal_canonical_lock_proved=false
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 直攻压缩

攻击前：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

攻击后：

```text
(ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger) OR NamedReturnExclusion OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalSyncImported` | `true` | `false` | 上一轮已把 actual-source 反原子线压回 strict acyclic 终端三原子，首攻 canonical-lock。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `CanonicalLockAtomized` | `true` | `false` | canonical-lock 已拆成源因子嵌入、同集推前、无 noncanonical payload 三项；当前未证明。 | AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection |
| `CanonicalAdmissionTimelineGuardClosed` | `true` | `false` | canonical branch 准入必须是 pre-Cauchy T1 身份声明，不能由下游 payment/PDEC/覆盖图反推。 | AcyclicCanonicalPreCauchyCoefficientIdentityLedger |
| `PreCauchyIdentityReducedToT1Equality` | `true` | `false` | canonical RIW/Buchstab T1 公式只在 scoped canonical 分支闭合；acyclic seed 的逐点等式仍未证。 | AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock |
| `CanonicalEqualityCaseOnlyScoped` | `true` | `true` | 若 T1 等式和 branch-key lock 全成立，只进入 canonical scoped promotion；这不是全局矛盾。 | mismatch branch remains for noncanonical complement |
| `MismatchNoSilentExitClosed` | `true` | `false` | T1 mismatch 已无静默出口，只能进 signed source、命名回流或 clean DLS；但这些出口尚未排斥。 | (ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger) OR NamedReturnExclusion OR AcyclicWindowedKloostermanDLSInternalEstimate |
| `SignedLiftFailureReturnLedgerClosed` | `true` | `false` | signed lift 失败均已登记为同 formal unit 的命名出口；登记不等于排斥。 | (ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger) OR NamedReturnExclusion OR AcyclicWindowedKloostermanDLSInternalEstimate |
| `AlphaWeightDownstreamReturnsToTerminalFamily` | `true` | `false` | alpha signed 权重律继续下钻后回到 PDEC/CleanKLS 终端门、模型余量账本和 DStructure 门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `WindowedDLSReducedToKuznetsovAtom` | `true` | `false` | clean DLS 形式层已压尽，真正未证的是自足 Kuznetsov/DLS 大筛不等式。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `DirectPDECScopeAuditStillOpen` | `true` | `false` | direct same-set PDEC 协议可用，但 acyclic/noncanonical 作用域匹配未证；不能替代 canonical-lock。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `CanonicalLockCurrentAttackProved` | `false` | `false` | 本轮直攻没有证明 canonical-lock；它被吸收到 scoped canonical case 或回到 mismatch/DLS/终端门。 | (ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger) OR NamedReturnExclusion OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger) |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 终端矛盾、Kuznetsov/DLS、模型余量和 DStructure/Rankin 均未全证，不能声明行/列无条件闭合。 | ((PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新严格基

```text
((PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一首攻点：

```text
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
```

并行账本：

```text
ExplicitModelGapAndFiniteDPRCLedger
```

审稿边界：本文件关闭 canonical-lock 直攻的路由分类，不证明 Kuznetsov/DLS、PDEC/CleanKLS、模型余量或 DStructure/Rankin。
