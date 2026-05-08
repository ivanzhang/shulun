# Prime Matrix 内外两线终端归约路由器

**状态：** `dual_lane_reduced_to_source_antiatom_or_c_dependent_spectral_input_open`

内外两条线继续压窄但仍未闭合：内部线的 balanced range 已消去，支撑+容量兼容等价于 actual noncanonical source 的强化反原子；外部线的 full-S 窗口已完成，剩余是 c-dependent residue 权重的谱抵消。当前材料没有证明任一输入，也没有完成 DStructure/Rankin 独立验收。

```text
terminal_reduction_boundary_closed=true
internal_lane_closed=false
external_lane_closed=false
rankin_promotion_accepted=false
row_column_unconditional_closed=false
```

## 1. 判定表

| lane | gate | closed | proved_or_accepted | meaning | remaining |
| --- | --- | --- | --- | --- | --- |
| `joint-frontier` | `JointFrontierPinned` | `true` | `false` | 上一轮已把内外两线固定为 exact support 包或 Full-S KLS 输入。 | 分别压缩这两个包内部的真实终端。 |
| `internal` | `BalancedRangeRemoved` | `true` | `false` | full-S regime 下 U,V 多项式级大于任意固定对数阈值，balanced range 不再是硬点。 | 内部路只剩 exact factor support 与 Type/Fourier capacity compatibility。 |
| `internal` | `SupportCapacityEqualsSourceAntiAtom` | `true` | `false` | exact factor support 与容量兼容合并为最终 source capacity measure 无 moving same-(u,v) atom。 | 证明 actual noncanonical source 的强化反原子，或改走外部谱/dispersion。 |
| `external` | `FullSWindowCompleted` | `true` | `false` | S≈P 且 C≈P/log^O P，s-window 可按模 c 完成；full-S 长度本身不是终端硬点。 | 处理完成后依赖 c 的 residue 权重 B_{c,x}。 |
| `external` | `CompletedWeightSpectralAtomPinned` | `true` | `false` | 点态 Weil、L2、普通大筛和平坦 residue 捷径不足；必须有 c,h 谱/dispersion 平均抵消。 | 证明或引用 CDependentResidueWeightSpectralCancellationInput。 |
| `promotion` | `RankinPromotionStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 晋级包边界已闭合但未独立验收。 | 即使二线数学输入闭合，也还需独立晋级接受。 |

## 2. 上一层输入基

```text
(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource OR FullSNonAPWFDKLSTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 最新输入基

```text
(FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 内部线终端合同

For the final full-S non-AP WFD source capacity measure M_{u,v}, prove max_{u,v} M_{u,v}/sum M_{u,v} <= log^{-2A} for every A.

## 5. 外部线终端合同

Prove or cite spectral DI/BFI/Kuznetsov cancellation for completed Kloosterman sums with c-dependent residue weights B_{c,x}, keeping the current uncentered no-projection non-AP WFD target and arbitrary log saving.

## 6. 当前结论

本路由关闭的是两条线内部的命名松散性，不是证明缺口。完全闭合仍需要：

- 证明内部强化反原子，或证明/引用外部 c-dependent 谱抵消；
- 完成 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 独立验收。
