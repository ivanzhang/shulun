# Prime Matrix Full-S KLS / Moving-Block 联合硬攻路由器

**状态：** `fulls_kls_movingblock_joint_attack_reduced_to_exact_support_or_new_fulls_kls_open`

本轮联合硬攻没有找到可诚实升级为无条件闭合的现有输入。内部路继续降到 actual noncanonical full-S 的精确因子支撑包；外部路继续降到必须新增或明确引用的 FullSNonAPWFDKLSTheoremInput。canonical 分支已闭合但不能再用于 noncanonical 补集；DStructure/Rankin 晋级门仍独立开放。

```text
joint_attack_boundary_closed=true
internal_lane_proved_in_current_corpus=false
external_lane_proved_or_cited_in_current_corpus=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 联合硬攻判定表

| gate | closed | blocks_final | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RefinedTwoLaneInputPinned` | `true` | `true` | 上一轮已经把数学二路压成 moving-block 内部路或 Full-S KLS 外部/新定理路。 | 继续判断二路是否能由当前材料或现有主来源推出。 |
| `CanonicalBranchRemovedFromNoncanonicalDuty` | `true` | `false` | canonical RIW/Buchstab 分支已闭合并移出；不能把它偷渡到 noncanonical full-S 补集。 | 只审查 actual noncanonical source 或外部 Full-S KLS。 |
| `InternalMovingBlockReducedToExactSupportPackage` | `true` | `true` | 内部 moving-block/SourceEntropy 路已降成精确因子支撑、balanced range 和 Type/Fourier 容量兼容包。 | 证明 actual noncanonical full-S 因子支撑包，或转外部定理。 |
| `ExactSupportNotDerivableFromK4K6` | `true` | `true` | K4 residue flatness 与 K6 dyadic bookkeeping 不能自动推出 moving factor-pair 支撑。 | 需要 factor-residue incidence 桥，或直接证明 exact factor support；canonical 支撑只服务 canonical 分支。 |
| `ExternalFullSKLSAtomPinnedButNotMatched` | `true` | `true` | 外部路已精确成 FullSNonAPWFDKLSTheoremInput；现有 DI/BFI 主来源逐项推出该对象的路线被阻断。 | 新增证明或明确引用直接覆盖当前对象的 full-S KLS/dispersion 定理。 |
| `ExternalSourceClassUsefulButInsufficient` | `true` | `true` | BFI/DI/Maynard 提供可用谱与 dispersion 技术来源，但对象仍是 AP 或一般 Kloosterman 技术类。 | 必须补变量同一化：c-dependent residue weights、未中心化、无投影、full-S、non-AP、任意对数节省。 |
| `DStructureRankinPromotionStillSeparate` | `true` | `true` | 即使数学二选一路闭合，完整行/列定理还需 DStructure/Tail-log4/finite Rankin 独立验收。 | 提交正式全集 Rankin 证书与独立接受。 |

## 2. 最新最窄输入基

```text
(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource OR FullSNonAPWFDKLSTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 内部路剩余子原子

- `FullSNonAPExactFactorSupportLowerBound`
- `FullSNonAPBalancedRangeThreshold`
- `FullSNonAPTypeFourierCapacityCompatibility`
- `FactorResidueIncidenceBridgeOrDirectExactSupport`
- `NoCanonicalBranchImportIntoNoncanonicalComplement`

## 4. 外部 Full-S KLS 输入条款

- current non-AP uncentered no-projection WFD window
- X≈P^2, C≈P/log^O(P), S≈P, 0<|h|<=P/log^O(P)
- c-dependent completed residue weights B_{c,x}
- well-factorable lambda and divisor-bounded beta/omega
- NaturalWFDScale/log^A(P) saving for every A>0
- dyadic/gcd/smoothing endpoint losses absorbed into B(A)

## 5. 外部主来源审查

| source | useful fact | current mismatch | link |
| --- | --- | --- | --- |
| `BFI-II` | well-factorable AP discrepancy / dispersion method source class | AP discrepancy target; current branch is full-S non-AP uncentered no-projection WFD | https://eudml.org/doc/164255 |
| `DI-Kloosterman` | spectral/Kuznetsov Kloosterman mean-value technology | technology backbone, not a ready-made theorem for the current c-dependent WFD weights | https://eudml.org/doc/142975 |
| `Maynard-II` | well/triply factorable AP mean-value theorem, with moduli beyond square-root ranges | AP fixed-residue theorem; does not by itself supply the non-AP no-projection WFD KLS atom | https://arxiv.org/abs/2006.07088 |
| `Maynard-I` | fixed residue AP framework using Kuznetsov/Weil/Deligne-type estimates | fixed-residue AP framework, not the current completed c-dependent residue-weight object | https://arxiv.org/abs/2006.06572 |

## 6. 当前结论

这一步继续压缩了命题边界：下一步不能再泛称“攻 KLS 或 NC-BLK”，而应精确攻下面二选一：

```text
FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource OR FullSNonAPWFDKLSTheoremInput
```

其中内部路是组合/支撑定理，外部路是新谱/dispersion 定理。二者至少一支成立后，仍需独立完成 DStructure/Rankin 晋级验收。
