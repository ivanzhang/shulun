# Prime Matrix actual-source bridge 全局调和路由器

**状态：** `actual_source_bridge_absorbed_for_canonical_branch_global_complement_open`

Actual-source bridge 已在 canonical 分支内闭合；旧阻断门 `ActualFullSSourceBridge` 应被替换为更精确的 `NoncanonicalFullSComplementAntiAtomOrExternalDIBFI`。这缩窄了完整全局版剩余，但不闭合完整行/列无条件定理。

## 1. 调和律

The actual-source bridge has been closed only after restricting the theorem to the canonical RIW/Buchstab source branch. This absorbs the bridge inside the canonical self-contained theorem, but it does not close the noncanonical full-S complement. The former broad blocker ActualFullSSourceBridge should therefore be replaced by the sharper noncanonical complement obligation: strengthened anti-atom or external DI/BFI.

```text
actual_source_bridge_closed_for_canonical_branch=true
actual_source_bridge_closes_global_unrestricted=false
old_blocker_superseded=ActualFullSSourceBridge
updated_global_blocking_gates:
  - UnrestrictedGenericWFD
  - NoncanonicalFullSComplementAntiAtomOrExternalDIBFI
  - FullSNonAPStrengthenedSourceAntiAtom
  - DIBFIQuantifiedNoProjectionWindowCertificate
  - DStructureTailLog4FiniteRankinPromotion
```

## 2. 审查表

| gate | closed | evidence | meaning | global remainder |
| --- | --- | --- | --- | --- |
| `CanonicalActualSourceProvenanceClosed` | `true` | NoFurtherActualSourceProvenanceGap | canonical no-black-box 分支的 pre-Cauchy lambda_c 已声明为 RIW/Buchstab 决策树系数。 | 不覆盖 noncanonical/generic 补集。 |
| `SourceLockBranchSplitClosed` | `true` | A1CleanBranchCanonicalSourceAdmissionOrExternalDIBFIOriginalDispersion | source lock 已严格二分：canonical 分支内部闭合，noncanonical 分支外部化或回流。 | global unrestricted 仍必须处理 noncanonical 补集。 |
| `CanonicalSourceTheoremAlreadyClosed` | `true` | NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap | actual-source bridge 对 canonical-source 自足定理已经不再是开门。 | 不能升级为完整行/列无条件定理。 |
| `OldActualFullSSourceBridgeBlockerSuperseded` | `true` | ActualFullSSourceBridge in previous obstruction list | 旧阻断名应被更精确地替换为 noncanonical full-S 补集问题。 | FullSNonAPStrengthenedSourceAntiAtom_OR_ExternalDIBFI |
| `UnrestrictedGenericStillNotClosed` | `true` | ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput | unrestricted generic 自足版仍被 moving-delta 反证，不能由 canonical 来源账本偷渡闭合。 | 必须新增强化反原子或外部 DI/BFI 证书。 |

## 3. 下一步

继续完整全局化时，不应再攻击 canonical actual-source bridge；它已经在自足边界内闭合。真正剩余是 noncanonical full-S 补集：证明强化 source anti-atom，或完成外部 DI/BFI 无投影量化证书。
