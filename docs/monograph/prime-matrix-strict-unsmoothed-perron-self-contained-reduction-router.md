# Prime Matrix strict 非平滑 Perron 自足剩余压缩路由器

**状态：** `unsmoothed_perron_external_closed_self_contained_reduced_to_backlund_logder_local_zero_open`

非平滑 Perron 常数层的外部条件路线已经关闭：外部 fixed-T Backlund 缩进、局部零点距离 C=288、水平加权预算 C=12000 和右边核 C=128 已合并为 Perron C=12128。但严格自足版不能导入这些外部条件；它现在被压缩为固定高度 Backlund 缩进内部证明、内部 zeta log-derivative/local zero 展开，以及由此触发的加权预算同步。最窄主攻点更新为 ClassicalBacklundZeroIndentationCostInternalProofLedger。

```text
unsmoothed_perron_external_conditional_closed=true
unsmoothed_perron_strict_self_contained_closed=false
backlund_internal_proved=false
classical_logder_internal_proved=false
local_zero_distance_self_contained_proved=false
weighted_budget_self_contained_proved=false
good_height_contract_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 条件替换边界

外部条件线：

```text
UnsmoothedChebyshevPerronExplicitFormulaConstantLedger
  =>
Psi0ZetaLogDerivativeContourShiftExternalClosedC12000 AND PerronKernelTruncationForPsi0ExternalClosedC12128
```

严格自足线：

```text
UnsmoothedChebyshevPerronExplicitFormulaConstantLedger
  =>
ClassicalBacklundZeroIndentationCostInternalProofLedger AND ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍服务统一矛盾场中的 B3/TV 输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `Psi0ExactFormulaInternalClosed` | `true` | `true` | psi_0 无截断显式公式身份已在作者侧闭合。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| `RightPerronKernelClosed` | `true` | `true` | 右边 Perron 核近似常数 C=128 已闭合。 | Psi0RightEdgePerronKernelApproximationClosedC128 |
| `ExternalFixedTIndentAndContourClosed` | `true` | `false` | 接受外部 Backlund/RVM/Titchmarsh 时，fixed-T 缩进、局部零点距离、加权水平预算和轮廓移线已条件关闭。 | Psi0ZetaLogDerivativeContourShiftExternalClosedC12000 AND PerronKernelTruncationForPsi0ExternalClosedC12128 |
| `SelfContainedFixedTIndentClosed` | `false` | `false` | 严格自足 fixed-T 缩进仍未完成；这是外部条件链不能直接转为作者侧证明的首要原因。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `SelfContainedLocalZeroDistanceClosed` | `false` | `false` | 严格自足局部零点倒距离和需自足 C_N=16、避零缩进和内部 log-derivative 展开。 | ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger AND ClassicalBacklundZeroIndentationCostInternalProofLedger AND Psi0HorizontalLocalZeroDistanceSumConstantLedger |
| `SelfContainedWeightedBudgetClosed` | `false` | `false` | 加权积分预算的算术常数已在外部条件线下闭合；自足同步仍等局部零点距离和前提。 | Psi0HorizontalWeightedIntegralBudgetLedger |
| `GoodHeightAlternativeStillOpen` | `false` | `false` | 可改走 T* 好高度平均路线，但必须重写当前 fixed-T Perron 合同，不能无声替换。 | Psi0GoodHeightTStarAveragingContourShiftLedger |
| `UnsmoothedPerronExternalConditionalClosed` | `true` | `false` | 外部条件链可关闭非平滑 Perron finite-T 层。 | PerronKernelTruncationForPsi0ExternalClosedC12128 |
| `UnsmoothedPerronStrictSelfContainedClosed` | `false` | `false` | 严格自足版尚未关闭；当前已压成 Backlund 缩进、内部 log-derivative/local zero 和加权预算同步。 | ClassicalBacklundZeroIndentationCostInternalProofLedger AND ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger |

## 3. 下一最窄点

```text
ClassicalBacklundZeroIndentationCostInternalProofLedger
```

并行保留：

```text
ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger
```

审稿边界：这一步只把自足 Perron 剩余继续压缩；没有关闭 B3 TV，也没有关闭行/列无条件命题。
