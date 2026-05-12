# Prime Matrix strict 非平滑 Perron 自足最终同步路由器

**状态：** `unsmoothed_perron_strict_self_contained_closed_mertens_tail_still_open`

`UnsmoothedChebyshevPerronExplicitFormulaConstantLedger` 已完成 strict 自足同步：先前压缩出的四个开放原子已经逐项闭合，右边 Perron 核 C=128 与水平边 C=12000 合成为 finite-T Perron 常数 C=12128。这只关闭非平滑 Perron 常数层；自足 Mertens 尾段、B3 TV 和行/列无条件命题仍未闭合。

```text
psi0_zeta_logder_contour_shift_self_contained_closed=true
perron_kernel_truncation_self_contained_closed=true
unsmoothed_perron_strict_self_contained_closed=true
self_contained_mertens_tail_closed=false
b3_tv_strict_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
C_perron_total=12128.000000000000
```

## 1. 自足替换

```text
Psi0ZetaLogDerivativeContourShiftBoundLedger
  => Psi0ZetaLogDerivativeContourShiftSelfContainedClosedC12000

PerronKernelTruncationConstantForPsi0Ledger
  => PerronKernelTruncationForPsi0SelfContainedClosedC12128

UnsmoothedChebyshevPerronExplicitFormulaConstantLedger
  => UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128

```

## 2. 常数聚合

| component | constant | atom | meaning |
| --- | ---: | --- | --- |
| right edge Perron kernel | `128.000000000000` | Psi0RightEdgePerronKernelApproximationClosedC128 | psi_0 与右边截断竖线积分之间的核误差。 |
| horizontal contour package | `12000.000000000000` | Psi0ZetaLogDerivativeContourShiftSelfContainedClosedC12000 | fixed-T 缩进、水平边 log-derivative 与留数左边界合成的水平预算。 |
| finite-T Perron reserve | `12128.000000000000` | PerronKernelTruncationForPsi0SelfContainedClosedC12128 | 只关闭 finite-T Perron 截断层，不包含零点和/PNT 数值预算。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只关闭假设反例链所需解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `StrictReductionFourAtomsReplaced` | `true` | `true` | Backlund 缩进、logder 展开、局部倒距离和加权预算四个 strict 原子均已完成自足替换。 | Backlund AND logder AND local-zero-distance AND weighted-budget |
| `ExactPsi0FormulaInternalClosed` | `true` | `true` | 内部 psi_0 无截断显式公式身份已闭合，可作为 finite-T 截断起点。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| `HeightAndBoundaryConventionClosed` | `true` | `true` | 避零高度选择与边界重数极限已在 Perron 四微账本中闭合。 | Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger |
| `ResidueAndLeftEdgeAvailable` | `true` | `true` | 留数清单与左边界衰减已由内部 psi_0 精确公式链吸收。 | Psi0ContourResidueAndLeftEdgeClosed |
| `RightEdgePerronKernelClosed` | `true` | `true` | 右边 Perron 核近似常数已给出 C=128。 | Psi0RightEdgePerronKernelApproximationClosedC128 |
| `HorizontalContourShiftSelfContainedClosed` | `true` | `true` | fixed-T 缩进和水平边 logder 包均自足后，zeta 对数导数轮廓移线包自足闭合。 | Psi0ZetaLogDerivativeContourShiftSelfContainedClosedC12000 |
| `PerronKernelTruncationConstantForPsi0Ledger` | `true` | `true` | 右边核 C=128 与水平边 C=12000 合成，finite-T Perron 截断层自足闭合为 C=12128。 | PerronKernelTruncationForPsi0SelfContainedClosedC12128 |
| `UnsmoothedPerronStrictSelfContainedClosed` | `true` | `true` | strict Perron 压缩账本四个开放原子全部替换后，非平滑 Perron 常数层自足闭合。 | UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128 |
| `SelfContainedMertensTailStillOpen` | `false` | `false` | Perron 常数层闭合不等于 Mertens 尾段闭合；零点和、theta@20000、低高度和 B1 区间仍独立。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger AND FiniteLowHeightZeroCheckLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步不产生早期零行反例链与真实结构链的终端矛盾；全局行/列命题仍未闭合。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger
```

也就是进入零点自由区零点和预算；这仍属于 B3/Mertens 尾段内部，不是全局行列终端矛盾。
