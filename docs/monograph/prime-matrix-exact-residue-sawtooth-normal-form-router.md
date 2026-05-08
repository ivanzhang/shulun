# Prime Matrix 精确残基 sawtooth 二次圆弧标准形路由器

**状态：** `exact_sawtooth_compressed_to_quadratic_arc_discrepancy_open`

本步把精确 floor 余项压成二次圆弧偏差。对每个 d>1，floor 误差完全由 t=P mod d 与 rho=±t^2 mod d 决定：A_d-P/d=1_{0<rho<t}-t/d。因此剩余不再是抽象 floor 控制，而是 Rosser 权重下的二次相位圆弧非集中命题；内部几何路线可写成近平方除数扩散，外部路线可写成 well-factorable sawtooth dispersion。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
exact_floor_to_quadratic_arc_identity_proved=true
endpoint_d1_loss_registered=true
sawtooth_atom_compressed=true
rosser_weighted_quadratic_arc_discrepancy_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 精确标准形

```text
1<=k<P
A_1=P-1, A_1-P=-1
t_d=P mod d, rho_d^±=±t_d^2 mod d in {1,...,d-1}
A_d^±=floor(P/d)+1_{0<rho_d^±<t_d}
A_d^±-P/d=1_{0<rho_d^±<t_d}-t_d/d
```

推导要点：对 d>1，P 与 d 互素，所以 rho_d^± 非零。写 P=floor(P/d)d+t_d，在 1<=k<P 中同余 k=rho 的点数就是 floor(P/d) 加上该残基是否落在开弧 (0,t_d) 内。

## 2. 容量匹配

| item | value |
| --- | ---: |
| model main at P=100000 | 4896.256004 |
| target S | 401 |
| target/main | 0.081899 |
| conservative main fraction | 0.990000 |
| sawtooth loss budget | 0.900000 main |
| residual after 99%-90% | 440.663040 |
| d=1 endpoint loss | 1 |
| residual after endpoint loss | 439.663040 |

## 3. 拆分律

内部标准形：

```text
ExactResidueWeightedFloorSawtoothTenPercentBound
  =>
RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000
```

允许外部分散输入：

```text
ExactResidueWeightedFloorSawtoothTenPercentBound
  =>
(RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExactSawtoothGateActive | `true` | `false` | 若标准 beta-sieve 权重包被接受，下一硬点就是精确加权 floor/sawtooth 余项。 | ExactResidueWeightedFloorSawtoothTenPercentBound |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条里整理余项标准形，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FloorToQuadraticArcIdentityClosed | `true` | `true` | 对 d>1，令 t=P mod d、rho=±t^2 mod d，则 A_d=floor(P/d)+1_{0<rho<t}。 | 无剩余。 |
| EndpointD1LossRegistered | `true` | `true` | 因区间为 1<=k<P，d=1 给 A_1-P=-1；该单点损失已从容量中扣除。 | 无剩余。 |
| NinetyNineMainVsNinetySawtoothCapacityClosed | `true` | `true` | 若权重主系数保守达到 99% 模型主项，sawtooth 损失不超过 90% 主项且扣除 d=1 后仍超过目标 401。 | 无剩余。 |
| SawtoothAtomCompressedToQuadraticArcDiscrepancy | `true` | `false` | 旧 sawtooth 原子被压成 Rosser 权重下的二次圆弧偏差界。 | RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 |
| RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 | `false` | `false` | 证明 sum lambda_d^-(1_{0<±(P mod d)^2 mod d<P mod d}-(P mod d)/d) >= -0.90 M(P)。 | RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 |
| WellFactorableNearSquareDivisorSpreadBoundAlpha043 | `false` | `false` | 等价几何形式是 t^2 与 d 的近端余数/近平方除数扩散；这是内部结构路线。 | WellFactorableNearSquareDivisorSpreadBoundAlpha043 |
| ExternalWellFactorableSawtoothDispersionBoundAlpha043 | `false` | `false` | 外部解析路线是 well-factorable 权重下的 sawtooth/分散估计。 | ExternalWellFactorableSawtoothDispersionBoundAlpha043 |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 短区间 rough-number 下界仍可绕过内部 sawtooth 分析。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 样本验算

| P | d | sign | t | rho | direct | formula | holds |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 101 | 7 | minus | 3 | 2 | 15 | 15 | `true` |
| 101 | 7 | plus | 3 | 5 | 14 | 14 | `true` |
| 101 | 13 | minus | 10 | 9 | 8 | 8 | `true` |
| 101 | 13 | plus | 10 | 4 | 8 | 8 | `true` |
| 103 | 11 | minus | 4 | 5 | 9 | 9 | `true` |
| 103 | 11 | plus | 4 | 6 | 9 | 9 | `true` |
| 107 | 15 | minus | 2 | 4 | 7 | 7 | `true` |
| 107 | 15 | plus | 2 | 11 | 7 | 7 | `true` |

## 6. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) AND RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000 OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 下一步

直接攻 `RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000`。内部几何支路是 `WellFactorableNearSquareDivisorSpreadBoundAlpha043`；外部解析支路是 `ExternalWellFactorableSawtoothDispersionBoundAlpha043`。
