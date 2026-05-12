# Prime Matrix strict actual-source 反原子到终端家族同步证书

**状态：** `strict_actual_source_antiatom_synced_to_acyclic_terminal_family_open`

本轮把 actual-source 强化反原子继续下钻到底层接口：它经已闭合的容量乘子纪律压到 ActualNoncanonicalExactUVSupportLowerBound；ExactUV 的非递归 pair-energy 证明不能循环使用源熵目标；pair-mass 失败不是新终端，而是 moving atom；seed 存在/不存在两支又统一回到 strict acyclic 终端家族。因此当前最窄自足剩余不再是 source anti-atom 大名，而是 acyclic 终端家族三原子。三原子和 DStructure/Rankin 仍未证明，行/列命题未无条件闭合。

```text
actual_source_antiatom_to_terminal_sync_boundary_closed=true
strengthened_actual_source_antiatom_proved=false
actual_exact_uv_support_proved=false
strict_terminal_family_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同步公式

```text
AddStrengthenedActualSourceAntiAtomTheorem -> ActualNoncanonicalExactUVSupportLowerBound -> nonrecursive pair-energy guard -> seed branch fusion -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily -> (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn).
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrengthenedActualSourceAntiAtomActive` | `true` | `false` | 上一轮已确认 actual-source 强化反原子仍是新增源定理，不是已证结论。 | AddStrengthenedActualSourceAntiAtomTheorem |
| `SourceAxiomReducedToExactUVSupport` | `true` | `false` | 乘子纪律闭合后，actual-source 强化反原子的大部分成本被压到 actual noncanonical ExactUV 支撑下界。 | ActualNoncanonicalExactUVSupportLowerBound |
| `ExactUVUniqueSourceInputStillOpen` | `true` | `false` | ExactUVSupport 是当前唯一源侧终端输入，但还没有证明。 | ActualNoncanonicalExactUVSupportLowerBound |
| `ExactUVSupportSpineImported` | `true` | `false` | 新 actual-source 熵定理内部脊柱已对齐为乘子纪律加 ExactUV 支撑。 | ActualNoncanonicalExactUVSupportLowerBound |
| `NonrecursivePairEnergyGuardClosed` | `true` | `false` | 不能用源熵/ moving-atom 结论反过来证明 pair-mass；必须给独立能量界或命名回流。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `PairMassNotSeparateTerminal` | `true` | `true` | pair-mass 分散失败就是同 formal unit 的 moving atom 失败，不是第三个新终端。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `AcyclicSeedIndependentInputRemoved` | `true` | `true` | seed 存在/不存在两支均回到 acyclic terminal family，因此 seed 不再作为独立输入。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `AcyclicTerminalFamilyReducedToThreeAtoms` | `true` | `false` | 源侧下钻已经回到 strict acyclic 终端家族三原子：canonical-lock、direct PDEC、direct CleanKLS。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `DirectPDECScopeAuditOpen` | `true` | `false` | direct same-set PDEC 的协议可用，但 acyclic/noncanonical 与 canonical 同集作用域匹配未证明。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `DirectCleanDLSAtomOpen` | `true` | `false` | clean KLS/DLS 已压到窗口化 Kloosterman/DLS 内部估计，但该估计未证明。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本同步只把 actual-source 反原子线压回终端家族；没有证明三原子、ExactUV 或 DStructure/Rankin。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新最窄剩余

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

首攻点：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
```

并行保留：

```text
AcyclicWindowedKloostermanDLSInternalEstimate
```

条件外部基：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn OR FullSNonAPWFDKLSTheoremInput_OR_DIBFIPrimarySourceSpecializationProof) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只同步并压缩 actual-source 反原子线；没有证明终端三原子、ExactUV、外部谱输入或 DStructure/Rankin。
