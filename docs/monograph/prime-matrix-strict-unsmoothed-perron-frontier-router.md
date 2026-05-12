# Prime Matrix strict 非平滑 Perron 当前前沿路由器

**状态：** `unsmoothed_perron_frontier_compressed_to_zeta_logder_contour_shift_open`

非平滑 Perron 子账本已继续压缩：内部 psi_0 精确公式与右边 Perron 核近似常数已经闭合，当前真实硬点是 zeta 对数导数轮廓移线。该硬点又被压成水平边 away-from-zero 上界、局部零点距离和、加权积分预算，以及固定 T 缩进或好高度 T* 的合同选择。

```text
internal_psi0_exact_formula_closed=true
right_edge_perron_kernel_closed=true
height_selection_closed=true
zero_boundary_avoidance_closed=true
unsmoothed_perron_frontier_compressed=true
zeta_logder_contour_shift_proved=false
horizontal_logder_bound_proved=false
local_zero_distance_sum_proved=false
horizontal_weighted_integral_budget_proved=false
backlund_indentation_internal_proved=false
good_height_tstar_contract_accepted=false
unsmoothed_perron_formula_proved=false
self_contained_mertens_tail_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿表

| name | status | meaning | remaining |
| --- | --- | --- | --- |
| `internal_psi0_exact_formula` | `closed` | psi_0(x)=x-sum_rho x^rho/rho-log(2pi)-1/2 log(1-x^-2) 的无截断公式已闭合。 | 有限 T 截断余项。 |
| `right_edge_perron_kernel` | `closed` | 右边 Perron 核近似常数已闭合为 C_right=128，只支付核误差。 | Psi0ZetaLogDerivativeContourShiftBoundLedger |
| `contour_shift` | `open` | 右边竖线积分移线到零点留数时，水平边 log-derivative 与近零缩进成本仍开放。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (ClassicalBacklundZeroIndentationCostInternalProofLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger) |
| `horizontal_logder` | `open_structural_reduction` | 水平边 zeta'/zeta 已压成局部零点距离和、加权积分预算，或 whole-strip 外部显式匹配。 | self: Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger; external: ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted AND Psi0HorizontalWeightedIntegralBudgetLedger |
| `fixed_t_vs_good_height` | `choice_open` | 固定 T 需要 Backlund/缩进成本；若改用好高度 T*，必须更新当前 fixed-T 合同。 | ClassicalBacklundZeroIndentationCostInternalProofLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 该前沿只服务自足 Mertens/PNT 输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `Psi0ExactFormulaClosed` | `true` | `true` | 内部 psi_0 精确公式已闭合，不再是当前硬点。 | Finite-T truncation constants. |
| `RightEdgeKernelClosed` | `true` | `true` | Perron 右边核近似常数已闭合为 C_right=128。 | Psi0ZetaLogDerivativeContourShiftBoundLedger |
| `ContourShiftOpen` | `false` | `false` | zeta 对数导数轮廓移线尚未闭合。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (ClassicalBacklundZeroIndentationCostInternalProofLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger) |
| `HorizontalLogderOpen` | `false` | `false` | 水平边 away-from-zero 上界需要内部局部零点距离和/加权积分，或外部 whole-strip 严格匹配。 | Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger |
| `UnsmoothedPerronFrontierClosed` | `false` | `false` | 非平滑 Perron 子账本尚未闭合。 | UnsmoothedChebyshevPerronExplicitFormulaConstantLedger |

## 3. 下一最窄点

```text
Psi0HorizontalLocalZeroDistanceSumConstantLedger
```

并行保留：

```text
Psi0HorizontalWeightedIntegralBudgetLedger AND ClassicalBacklundZeroIndentationCostInternalProofLedger AND ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted AND Psi0GoodHeightTStarAveragingContourShiftLedger
```

审稿边界：本步不闭合非平滑 Perron 子账本；只关闭已证子层并给出下一个真正微硬点。
