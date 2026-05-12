# Prime Matrix strict Table 6.3 b=28 生成/舍入输入基审计证书

**状态：** `table63_b28_generation_rounding_reduced_to_zero_input_binding_budget_rounding_hash`

`Table63B28GeneratedUpperRounding...` 不能由现有内部粗 contour 生成：高尾粗模板距离 `2.224e-5` 表值约 `2.78e12` 倍。外部 Table 6.3 行已经可用，但作者侧自足生成必须补齐同一显式公式口径、有限零点高度端点、零点自由尾项起点、无缺口拼接、预算分摊、外向舍入和 hash。下一最窄点是把有限零点/零点自由输入绑定到同一 b=28 显式公式。

```text
external_b28_row_usable=true
b28_cap_and_p51_margin_fixed=true
coarse_internal_contour_rejected_for_b28=true
table63_b28_generation_rounding_closed=false
table63_b28_zero_input_binding_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 数值边界

| field | value |
| --- | ---: |
| `epsilon_psi_28` | `0.00002224` |
| `target_1_over_36260` | `0.000027578599007170435741864313292884721456150027578599` |
| `p51_high_tail_margin` | `0.000005338599007170435741864313292884721456150027578599` |
| `coarse_template_gap_factor_high_tail_b28` | `2779902555195.0005` |

## 2. 输入基

| basis | role | why needed |
| --- | --- | --- |
| `Table63B28SameExplicitFormulaConventionLedger` | 固定 psi/psi0、核函数、截断、素数幂和平凡零点口径 | 没有同一显式公式，finite-zero、zero-free tail 和表值 cap 不能相加比较。 |
| `Table63B28FiniteRHHeightEndpointAndZeroBlockLedger` | 给出表算法实际调用的有限 RH 高度端点和零点块证书 | Gourdon 外部来源必须转换成同一表公式的高度变量。 |
| `Table63B28ZeroFreeTailConstantsAndStartHeightLedger` | 给出零点自由区尾项常数、起点和适用区间 | Kadiri 外部常数必须进入同一表尾项预算。 |
| `Table63B28FiniteToTailNoGapNoOverlapLedger` | 证明有限零点块、尾项和截断高度无缺口、无重复扣费 | 否则同一零点区域可能漏算或双算。 |
| `Table63B28PsiEpsilonBudgetPartitionLedger` | 证明所有误差项相加小于 2.224e-5 | 表行的核心是上界生成，不是数值摘录。 |
| `Table63B28DirectedUpperRoundingAndIntervalPropagationLedger` | 证明输出 2.224E-5 是外向上舍入并覆盖整段 x>=exp(28) | 舍入方向错误会把表值从上界变成未经认证的近似。 |
| `Table63B28ReproducibleComputationHashLedger` | 给出输入、程序、版本和输出表的可复现 hash | 没有 hash 就无法区分作者侧复算与文字引用。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只审计假设反例链可调用的解析表输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `GenerationRoundingGateActive` | `true` | `true` | 上一证书把下一最窄点精确压到 b=28 表值的生成与外向舍入证书。 | Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger |
| `ExternalB28RowAlreadyUsable` | `true` | `false` | 外部路线中 b=28 表行可直接使用，且高尾拼接算术已匹配。 | external Table 6.3 accepted |
| `B28CapAndP51MarginFixed` | `true` | `true` | b=28 cap 为 2.224e-5，接入 1/36260 的数值余量固定。 | margin=0.000005338599007170435741864313292884721456150027578599 |
| `CoarseInternalContourRejectedForB28` | `true` | `true` | 现有 C=1280,C_Z=65536 内部粗 contour 距 b=28 表值约 10^12 倍，不能生成 Table 6.3。 | gap_factor=2779902555195.0005 |
| `CommonVariableInterfaceKnown` | `true` | `true` | x 区间、高度端点、零点自由阈值、显式公式、预算和 hash 六类共同变量已被分类。 | classification closed, values open |
| `ExternalFiniteRHAndZeroFreeSourcesAvailable` | `true` | `false` | Gourdon 有限零点和 Kadiri 零点自由区可作为外部来源，但尚未绑定到 b=28 表算法。 | Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger |
| `Table63B28SameExplicitFormulaConventionLedger` | `false` | `false` | 同一显式公式口径仍开放：当前内部 Perron 粗链自洽不等于 Dusart Table 6.3 的表算法口径。 | PsiVsPsi0EndpointJumpConventionLedger AND TableTruncationSmoothingAndKernelConventionLedger |
| `Table63B28ZeroInputToExplicitFormulaBindingLedger` | `false` | `false` | 还没有证明有限零点块和零点自由尾项按同一显式公式进入 b=28 表行。 | Table63B28SameExplicitFormulaConventionLedger AND Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger AND Table63B28FiniteToTailNoGapNoOverlapLedger |
| `Table63B28PsiEpsilonBudgetPartitionLedger` | `false` | `false` | 还没有可复算数值账本证明 finite-zero、zero-free tail、素数幂、平凡零点和端点误差之和小于 2.224e-5。 | Table63B28ZeroInputToExplicitFormulaBindingLedger AND PrimePowerAndTrivialZeroCorrectionBudgetLedger |
| `Table63B28DirectedUpperRoundingAndIntervalPropagationLedger` | `false` | `false` | 还缺外向上舍入和高尾区间传播日志，证明输出的 2.224E-5 是认证上界而非近似值。 | Table63B28ReproducibleComputationHashLedger |
| `Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger` | `false` | `false` | b=28 生成/舍入证书尚未作者侧闭合；当前只关闭外部表行和所需输入基定位。 | Table63B28ZeroInputToExplicitFormulaBindingLedger AND Table63B28PsiEpsilonBudgetPartitionLedger AND Table63B28DirectedUpperRoundingAndIntervalPropagationLedger AND Table63B28ReproducibleComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | b=28 表值生成审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
Table63B28ZeroInputToExplicitFormulaBindingLedger
```

