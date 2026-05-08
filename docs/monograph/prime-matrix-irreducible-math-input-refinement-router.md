# Prime Matrix 不可约数学输入精化路由器

**状态：** `irreducible_math_input_refined_to_full_s_kls_or_moving_block_open`

终局数学输入边界可再精化一层：内部路仍是 actual moving-block spread；外部路不是已经逐项匹配的现有 DI/BFI/Kuznetsov 推论，而是必须新增、证明或明确引用的 FullSNonAPWFDKLSTheoremInput。再加上 DStructure/Rankin 独立验收未完成，当前材料仍不能声明完整行/列无条件定理。

```text
refinement_boundary_closed=true
all_required_inputs_proved_or_accepted=false
existing_primary_dibfi_match_rejected=true
ap_source_lift_rejected=true
internal_moving_block_proof_found_in_current_corpus=false
new_full_s_kls_theorem_proved_or_cited_in_current_corpus=false
independent_promotion_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 精化判定表

| gate | closed | proved_or_accepted | meaning | refinement |
| --- | --- | --- | --- | --- |
| `PreviousIrreducibleBasisPinned` | `true` | `false` | 上一轮已把数学输入压成 moving-block spread 或精确外部 DIBFI/Kuznetsov。 | 继续审查外部标签是否真能由现有 DI/BFI 主来源逐项匹配。 |
| `InternalLaneIsActualMovingBlockSpread` | `true` | `false` | 内部路不是 fixed-projection diffuse，而是 actual full-S non-AP WFD 系数的 moving same-(u,v) 块扩散。 | 保留为 MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients。 |
| `ExistingPrimaryDIBFISourceMatchRejected` | `true` | `false` | 现有 BFI AP 定理和 DI/Maynard J-scale 不能推出当前 full-S non-AP KLS-ext。 | 外部路不能再写成已经匹配的现有 DI/BFI/Kuznetsov 推论。 |
| `APSourceLiftRejected` | `true` | `false` | non-AP WFD 补集不能无损回提为 AP-source discrepancy。 | 外部路剩余不能借 APSourceLift 逃回 BFI AP 定理。 |
| `FullSNonAPWFDKLSAtomPinned` | `true` | `false` | 新增 full-S 定理输入已被精确定义为当前 non-AP、未中心化、无投影 WFD 窗口的 KLS/dispersion 估计。 | 把 PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem 精化为 FullSNonAPWFDKLSTheoremInput。 |
| `IndependentPromotionStillRequired` | `true` | `false` | DStructure/Tail-log4/finite Rankin 晋级包边界已闭合，但尚未独立接受。 | 完整行/列无条件定理仍需独立晋级验收。 |

## 2. 精化后的输入基

上一轮输入：

```text
MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem
```

精化后输入：

```text
(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients OR FullSNonAPWFDKLSTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 当前结论

这一步关闭的是命名精度缺口，不是证明缺口。
`FullSNonAPWFDKLSTheoremInput` 仍需新增自足证明或独立外部定理引用；
`MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients` 仍未由当前材料推出；
`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 仍需独立验收。
