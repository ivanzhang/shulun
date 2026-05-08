# Prime Matrix noncanonical full-S 补集输入合同路由器

**状态：** `noncanonical_complement_input_contract_pinned_global_unconditional_still_open`

Noncanonical full-S 补集的必要输入合同已经固定；当前材料不能自足闭合完整全局行/列命题。下一步不是继续攻击 generic WFD 模板，而是证明实际源恒等、实际源强化反原子，或提交外部/量化 DI/BFI。

## 1. 合同律

After the canonical RIW/Buchstab branch is subtracted, the remaining full-S problem is not a generic WFD self-contained lemma: that template is refuted by the moving-delta model. The remaining noncanonical complement can only be closed by proving actual source identity, proving a strengthened anti-atom for the actual source, or by taking the quantified no-projection DI/BFI route. Final row-column promotion still separately requires the D-structure/Rankin acceptance gate.

```text
contract_boundary_closed=true
canonical_branch_removed_from_remainder=true
generic_wfd_template_available=false
noncanonical_complement_closed_by_current_corpus=false
row_column_unconditional_closed=false
```

## 2. 必要输入族

- Actual source identity with canonical RIW/Buchstab source
- Strengthened anti-atom for the actual noncanonical full-S source
- External or newly proved quantified no-projection DI/BFI route
- Independent D-structure/Tail-log4/finite Rankin promotion

## 3. 审查表

| gate | verdict | closed | evidence | consequence | required input |
| --- | --- | --- | --- | --- | --- |
| `CanonicalBranchSubtracted` | `closed` | `true` | actual-source provenance + source-lock + final theorem boundary | canonical 分支不再属于全局剩余。 | none inside canonical branch |
| `GenericWFDSelfContainedTemplate` | `refuted_not_available` | `true` | ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput | 不能把 unrestricted generic WFD 当作可补局部引理继续使用。 | replace by actual-source theorem or external DI/BFI |
| `OldActualFullSSourceBridge` | `superseded` | `true` | actual-source bridge global reconciliation | 旧宽阻断门应改写成 noncanonical 补集输入合同。 | NoncanonicalFullSComplementAntiAtomOrExternalDIBFI |
| `SourceIdentityOption` | `open_input` | `false` | taxonomy.actual_source_bridge_theorem_closed=false | 若能证明实际 full-S non-AP 源等于 canonical RIW/Buchstab 源，则补集回流已闭合边界。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab |
| `StrengthenedAntiAtomOption` | `open_input` | `false` | terminal gap includes ProveActualSourceStrengthenedAntiAtom | 若不能证明源恒等，必须直接证明实际 noncanonical 源的强化反原子。 | FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `ExternalDIBFIOption` | `open_external_or_new_proof` | `false` | DIBFIQuantifiedNoProjectionWindowCertificate remains in global blockers | 外部/generic 路线需要无投影未中心化 dispersion 恒等式和量化窗口代入。 | NoProjectionUncenteredDispersionIdentity + QuantifiedDIBFIWindowSubstitution |
| `DStructureFinalPromotion` | `referee_block` | `false` | DStructureTailLog4FiniteRankinPromotion remains in global blockers | 即便补集输入完成，完整行/列无条件晋级仍需 D-structure/Rankin 独立接受。 | DStructureTailLog4FiniteRankinIndependentAcceptance |
| `NoHiddenFourthRoute` | `contract_closed` | `true` | taxonomy routes: canonical, refuted generic, external, actual-source | 当前材料下没有第四条可自足偷渡路线。 | choose source identity, strengthened anti-atom, or external DI/BFI |

## 4. 判定

该路由器闭合的是“必要输入边界”：canonical 分支已扣除，generic WFD 模板不可用，noncanonical 补集必须由实际源恒等、实际源强化反原子或外部/量化 DI/BFI 处理。它不证明这些输入本身，也不把完整行/列无条件命题升级为已证定理。
