# Prime Matrix 线性筛尾段余项缺口路由器

**状态：** `linear_sieve_tail_ten_percent_split_to_weighted_remainder_or_external_rough_open`

本步定位了 10% 主项包的真实剩余。主项常数足够，但不能用黑箱绝对余项关闭：P=100000 时主项约 4896.256004，10% 主项约 489.625600，而 |r_d|<=1 的 D≈P 余项尺度是 100000。因此真正最窄点是 Rosser-Iwaniec 权重下的 floor 余项控制；外部路线则是短区间粗数下界。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
tail_ten_percent_margin_split=true
rosser_iwaniec_weighted_floor_remainder_proved=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 缺口定位

```text
LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger
  =>
(RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)
```

## 2. 余项尺度

| item | value |
| --- | ---: |
| main at P=100000 | 4896.256004 |
| 10% main | 489.625600 |
| target S | 401 |
| allowed loss to 10% main | 4406.630403 |
| naive D=P remainder scale | 100000 |
| z at P=100000 | 141.253754 |
| z^2 at P=100000 | 19952.623150 |

这说明“主项很大”不是最后证明；最后证明必须说明 Rosser-Iwaniec 权重与 floor 余项不会发生最坏同向叠加。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TenPercentTailGateActive | `true` | `false` | 最新最窄点是尾段筛余达到线性筛模型主项 10%。 | LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内整理模型余量，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| TenPercentMainAlgebraImported | `true` | `true` | 10% 主项大于目标 401 的代数余量已由上一层闭合。 | 还需证明实际筛余达到该 10% 主项。 |
| NaiveAbsoluteRemainderCannotClose | `true` | `true` | 若只用 \|r_d\|<=1 的绝对余项，level D≈P 或 even z^2 的总损失都超过 10% 余量。 | 必须控制 Rosser 权重 floor 余项，或改用外部短区间粗数下界。 |
| TailTenPercentMarginSplit | `true` | `false` | 尾段 10% 主项包被压成二选一：内部权重余项控制，或外部短区间粗数定理。 | RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| RosserIwaniecWeightedFloorRemainderTenPercentBound | `false` | `false` | 证明 Rosser-Iwaniec 下界权重与 floor 余项配对后，总损失不超过 90% 主项。 | RosserIwaniecWeightedFloorRemainderTenPercentBound |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 引用或证明长度 P、阈值 P^0.43 的短区间 y-rough 数下界，直接给 S_Y(P)>=401。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

优先攻 `RosserIwaniecWeightedFloorRemainderTenPercentBound`：写出下界筛权重的精确 floor-sum 账本，证明加权余项总损失不超过 90% 主项；若走外部路线，则需登记一个直接适配 `x=P^2`、区间长 `P`、粗阈值 `P^0.43` 的短区间 rough-number 下界。
