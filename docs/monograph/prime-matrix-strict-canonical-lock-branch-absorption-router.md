# Prime Matrix strict canonical-lock 分支吸收路由器

**状态：** `strict_canonical_lock_absorbed_as_scoped_canonical_branch_active_noncanonical_source_entropy_open`

本步把 canonical-lock 从活动非 canonical 主线中吸收掉：五项 exact same-set 证书成立时，它只是 canonical-source 范围内的条件晋级 case；证书缺失时则不能调用 canonical-lock。因此 canonical-lock 不再是独立非循环出口，真正活动的 noncanonical 剩余目标只剩原 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
canonical_lock_branch_absorption_closed=true
canonical_exact_certificate_branch_discharged_conditionally=true
canonical_lock_standalone_global_contradiction=false
global_unrestricted_terminal_family_exclusion_closed=false
acyclic_terminal_canonical_lock_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 主线压缩

吸收前：

```text
AcyclicCanonicalExactSameSetPromotionCertificate OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

吸收后，活动 noncanonical 主线为：

```text
NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactSameSetCanonicalCertificateBranchPinned` | `true` | `false` | 上一层已把 canonical-lock 精炼成五项 exact same-set canonical 晋级证书。 | AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection |
| `CanonicalTerminalPromotionImportedWithScope` | `true` | `true` | canonical RIW/Buchstab source 分支内，终端晋级已闭合；但该闭合不覆盖 unrestricted/global noncanonical 分支。 | scope=canonical-source branch only。 |
| `CertificatePresentBranchDischargedConditionally` | `true` | `true` | 若五项证书实际提交，则对象已在同一 formal unit 和同一坏窗集合下进入 canonical 分支，按 scoped canonical promotion 处理。 | 不再作为活动 noncanonical 终端。 |
| `CertificateAbsentBranchCannotUseCanonicalLock` | `true` | `true` | 若五项证书任一项缺失，则 finite factor 或 same-set pushforward 定义失败，canonical-lock 不能被调用。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `A1AdmissionAbsorptionConsistent` | `true` | `true` | 这与 A1 source-admission 分支吸收一致：canonical 分支陈述不作为 global contradiction，只作为 scoped case。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `DirectTerminalFallbackStillRejected` | `true` | `true` | 证书缺失时不能改走 direct PDEC/direct CleanKLS 标签链，因为该链已被证明回流。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `ActiveNoncanonicalTerminalReducedToSourceEntropy` | `true` | `false` | 吸收 canonical scoped case 后，活动 noncanonical 主线只剩原 actual-source 熵定理。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本步只是分支吸收，不证明 source entropy，也不关闭 DStructure/Rankin 或最终行/列命题。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem AND remaining promotion gates。 |

## 3. 结构结论

canonical-lock 的 exact same-set 证书若存在，只把该 case 送入 canonical-source scoped promotion；若证书不存在，canonical-lock 不可用。因 direct PDEC/CleanKLS 已回流，活动 noncanonical 主线被压成唯一目标 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。这不是行/列命题无条件闭合。

## 4. 下一主攻点

```text
NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```
