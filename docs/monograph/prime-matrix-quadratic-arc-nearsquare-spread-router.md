# Prime Matrix 二次圆弧到近平方条带扩散路由器

**状态：** `quadratic_arc_discrepancy_compressed_to_signed_nearsquare_strip_open`

本步把二次圆弧偏差进一步压成近平方条带扩散。对 minus 侧，rho=t^2 mod d 落入 (0,t) 等价于 t^2 在某个 d 倍数上方距离小于 t；对 plus 侧，-t^2 mod d 落入 (0,t) 等价于 t^2 在某个 d 倍数下方距离小于 t。再用 P=hd+t 提升后，危险事件就是商余坐标中的有向窄条带 |h t^2-a(P-t)|<h t。因此剩余不是抽象相消，而是 Rosser 权重支撑在这些窄条带上的有符号非集中。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
arc_hit_iff_nearsquare_multiple_proved=true
nearsquare_lift_to_quotient_residue_strip_proved=true
quadratic_arc_discrepancy_compressed=true
rosser_weight_quotient_residue_support_ledger_proved=false
signed_nearsquare_strip_discrepancy_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 精确等价

令 `t=P mod d`，`P=hd+t`。对 `d>1`：

```text
minus/lower: 0 < t^2-floor(t^2/d)d < t
plus/upper:  0 < ceil(t^2/d)d-t^2 < t
lift:        P=hd+t, d=(P-t)/h, so both sides become 0<±(h t^2-a(P-t))<h t
```

圆柱斜线端点偏差等价于商余平面中的近平方窄条带穿越。

## 2. 拆分律

自足路线：

```text
RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000
  =>
(RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000)
```

允许外部分散输入：

```text
RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000
  =>
((RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000) OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| QuadraticArcDiscrepancyGateActive | `true` | `false` | 最新内部最窄点是 Rosser 权重下的二次圆弧偏差。 | RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内改写余项，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ArcHitIffNearSquareMultipleClosed | `true` | `true` | rho=±t^2 mod d 落入开弧 (0,t) 等价于 t^2 距某个 d 的倍数小于 t。 | 无剩余。 |
| NearSquareLiftToQuotientResidueStripClosed | `true` | `true` | 再写 P=hd+t，近平方事件等价于 \|h t^2-a(P-t)\|<h t 的有向窄条带。 | 无剩余。 |
| QuadraticArcCompressedToSignedNearSquareStrip | `true` | `false` | 旧二次圆弧偏差原子被压成带 Rosser 权重支撑账本的有符号近平方条带非集中。 | RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000 |
| RosserWeightQuotientResidueSupportLedgerAlpha043 | `false` | `false` | 需要把 lower weights 在 (h,t,a) 商余坐标中的支撑、符号和 well-factorable 分块登记清楚。 | RosserWeightQuotientResidueSupportLedgerAlpha043 |
| SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000 | `false` | `false` | 证明有符号 Rosser 质量不能在 \|h t^2-a(P-t)\|<h t 的窄条带上产生 0.90M 级负偏差。 | SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000 |
| ExternalWellFactorableSawtoothDispersionBoundAlpha043 | `false` | `false` | 外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。 | ExternalWellFactorableSawtoothDispersionBoundAlpha043 |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 样本验算

| P | d | side | h | t | a | rho | arc | near-square | strip | all |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 101 | 7 | minus/lower | 14 | 3 | 1 | 2 | `true` | `true` | `true` | `true` |
| 101 | 7 | plus/upper | 14 | 3 | 2 | 5 | `false` | `false` | `false` | `true` |
| 101 | 13 | minus/lower | 7 | 10 | 7 | 9 | `true` | `true` | `true` | `true` |
| 101 | 13 | plus/upper | 7 | 10 | 8 | 4 | `true` | `true` | `true` | `true` |
| 103 | 11 | minus/lower | 9 | 4 | 1 | 5 | `false` | `false` | `false` | `true` |
| 103 | 11 | plus/upper | 9 | 4 | 2 | 6 | `false` | `false` | `false` | `true` |
| 107 | 15 | minus/lower | 7 | 2 | 0 | 4 | `false` | `false` | `false` | `true` |
| 107 | 15 | plus/upper | 7 | 2 | 1 | 11 | `false` | `false` | `false` | `true` |
| 109 | 28 | minus/lower | 3 | 25 | 22 | 9 | `true` | `true` | `true` | `true` |
| 109 | 28 | plus/upper | 3 | 25 | 23 | 19 | `true` | `true` | `true` | `true` |
| 127 | 45 | minus/lower | 2 | 37 | 30 | 19 | `true` | `true` | `true` | `true` |
| 127 | 45 | plus/upper | 2 | 37 | 31 | 26 | `true` | `true` | `true` | `true` |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) AND (RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND ((RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000) OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND ((RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000) OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

先攻 `RosserWeightQuotientResidueSupportLedgerAlpha043`，把 Rosser 权重实际支撑搬到 `(h,t,a)` 条带坐标；随后攻 `SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000` 的有符号非集中。
