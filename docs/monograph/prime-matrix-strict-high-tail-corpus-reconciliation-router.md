# Prime Matrix 严格高段尾项语料校准路由器

**状态：** `strict_high_tail_reconciled_to_mertens_tail_and_strict_terminal_family_open`

本步把 strict 高段尾项与已经完成的 beta/B3/sawtooth 语料重新对齐。lower weights 构造、逐点支配、连续主项、Stieltjes 表示和 B=3 delay 乘子账本可导入；exact sawtooth 失败态也不再是独立第三输入，而是并入 strict acyclic noncanonical 终端家族。严格自足高段剩余因此压成 Mertens/PNT 内联证明；若接受外部 Dusart/Rosser-Schoenfeld 输入，高段解析线可移出活动缺口。完整行/列命题仍未无条件闭合。

```text
strict_high_tail_corpus_reconciliation_closed=true
lower_weight_construction_and_dominance_imported=true
continuous_and_stieltjes_layers_imported=true
b3_boundary_variation_anchor20000_imported=true
self_contained_mertens_tail_proved=false
exact_sawtooth_independent_input_removed=true
strict_terminal_family_proved=false
row_column_unconditional_closed=false
strict_self_contained_high_tail_gap_after_router=SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000
```

## 1. 校准前后

校准前 strict 高段尾项写成：

```text
SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound
```

导入现有语料后，严格自足高段尾项剩余压成：

```text
SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000
```

同时 exact sawtooth 失败态收费到 strict 终端家族，而不是用 canonical 吸收偷渡。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictHighTailCorpusReconciliationActive` | `true` | `false` | 上一层 strict 高段尾项仍把 beta 构造、99% 主系数和 exact sawtooth 写成三个并列开放输入。 | 导入已经完成的 beta/B3/sawtooth 语料，并重新校准严格作用域。 |
| `LowerWeightConstructionAndDominanceImported` | `true` | `true` | B=3 lower word rule、有限递归、支撑、符号、level 与逐点 lower-bound 支配均已由内部组合证明关闭。 | 不再把 SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix 作为未拆黑箱。 |
| `ContinuousAndStieltjesLayersImported` | `true` | `true` | 连续 f(1/0.43) 余量与 prime-word Stieltjes 精确表示已闭合，离散误差集中到 B=3 边界余项。 | B3 交错边界余项的一维 Mertens 尾段。 |
| `BoundaryVariationAnchor20000Imported` | `true` | `true` | 10372 到 20000 的有限锚点提升、face 字典和 delay-kernel BV 乘子账本已闭合。 | 若不用外部 Dusart/Rosser-Schoenfeld，则仍需自足证明 reciprocal-prime Mertens 尾段。 |
| `ExternalMertensHighTailRouteAvailable` | `true` | `false` | 接受 Dusart/Rosser-Schoenfeld 型外部显式 Mertens/theta 输入时，B3 高段解析链可接到 DStructure/Rankin 门。 | 这是外部条件接入，不是严格自足内联证明。 |
| `SelfContainedMertensTailStillOpen` | `true` | `false` | 完全自足版必须内联显式 PNT 机器：x>=20000 的 theta/psi 包络和 Meissel-Mertens 常数区间。 | SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `ExactSawtoothNormalFormImported` | `true` | `true` | Exact floor/sawtooth 已精确化为二次圆弧，再化为近平方条带 formal unit。 | 条带失败态是否形成可排除的全局终端家族。 |
| `NearSquareTerminalAdmittedToStrictTerminalFamily` | `true` | `false` | 近平方条带失败会生成同一 formal unit 的 PDEC/SAE 证书；在 strict noncanonical 口径中只能并入已开放的 acyclic terminal-family 门，不能用 canonical 吸收偷渡。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。 |
| `ExactSawtoothIndependentInputRemovedByCharging` | `true` | `false` | Exact sawtooth 不再作为第三个高段独立输入保留；其失败态被收费到 strict 全局终端门。 | strict 终端门本身仍未证明。 |
| `StrictHighTailSelfContainedCurrentCorpusProved` | `true` | `false` | 旧三项已经重新压缩，但严格自足高段尾项还缺 Mertens/PNT 内联证明。 | SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 即便高段外部解析线可用，完整行/列命题仍受 acyclic seed、strict PDEC/CleanKLS 与 DStructure/Rankin 替代门限制。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基更新为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若接受外部 Mertens/theta 显式定理，高段解析缺口可移出，剩：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`SelfContainedMertensTail_OR_AcyclicTerminalFamily`。

- 高段严格自足优先：`SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000`。
- 全局 strict 优先：`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily`。

不能作为证明使用：
- 把 canonical-source 的 NoFurtherCanonicalSourceTerminalPromotionGap 直接导入 acyclic noncanonical 分支。
- 把 Dusart/Rosser-Schoenfeld 外部 Mertens 定理冒充为仓库内自足证明。
- 把 finite checkpoint 余量外推成 P>=100000 全尾段证明。
- 把 exact sawtooth 标准形本身当作负损失界。
- 把 DStructure/Rankin 独立验收门改写为已证自足替代包。
