# Prime Matrix strict PDEC same-set 作用域分支饱和前沿

**状态：** `pdec_scope_branch_saturated_internal_noncycle_exit_reduced_to_new_joint_formula_open`

`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` 已按当前内部材料攻到边界：direct PDEC 需要 canonical-lock 同口径，canonical-lock 只 scoped，CleanKLS/DLS 又回到终端家族，终端家族三手臂已饱和。因此 PDEC 手臂仍是可接受的新 scope 证书或外部 DIBFI 输入，但在当前 strict 自足内部语料中不再提供独立非循环出口。剩余真正内部破环点压成`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`，并继续保留模型余量、RatePreservation、DStructure/Rankin 独立验收门。

```text
pdec_scope_branch_attacked=true
pdec_scope_branch_saturated_in_current_internal_corpus=true
pdec_scope_proved=false
canonical_lock_proved=false
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
strict_acyclic_terminal_family_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestFrontierContainsPDECScope` | `true` | `false` | seed-cycle-cut 饱和后，strict 自足线只剩 PDEC same-set 作用域匹配或新 joint 公式。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `DirectPDECScopeAuditClosed` | `true` | `false` | direct PDEC 已完成同集协议审计，但 canonical-source 同集结果只能 scoped 使用。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `PDECRequiresCanonicalLockOrExternalDIBFI` | `true` | `false` | PDEC 作用域匹配不能无条件导入；内部需 canonical lock，外部需 DIBFI，fallback 是 windowed DLS。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicWindowedKloostermanDLSInternalEstimate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| `CanonicalLockAttackedButScoped` | `true` | `false` | canonical equality case 只给 scoped canonical promotion，不给 acyclic noncanonical 全局矛盾。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `CleanKLSDLSTerminalReturn` | `true` | `false` | CleanKLS/DLS 形式层已攻到底，但 KZ-E/NC-BLK 回到 acyclic 终端家族而非终端矛盾。 | AcyclicNoncanonicalTerminalFamily |
| `TerminalFamilyAlreadySaturated` | `true` | `false` | 终端家族三手臂已同步：canonical scoped，direct PDEC open，CleanKLS returns terminal。 | Nonrecursive/PDEC/NewJoint fixed frontier. |
| `PDECScopeNotIndependentNonrecursiveExit` | `true` | `false` | PDEC 手臂仍可作为外部或新 scope 证书输入，但在当前内部语料中不是已证非循环出口。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NewExplicitJointFormulaStillAbsent` | `true` | `false` | 剩余内部破环只能提交新的显式 joint alpha/delta 构造公式，否则仍回到 signed-source 固定点。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |

## 2. 最新严格内部非循环基

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件 PDEC/外部保留线：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```
