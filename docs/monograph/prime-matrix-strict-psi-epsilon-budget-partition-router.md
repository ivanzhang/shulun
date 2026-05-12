# Prime Matrix strict psi epsilon 预算分摊路由器

**状态：** `psi_epsilon_budget_caps_fixed_component_partition_open`

psi epsilon 预算分摊的上限已经固定：高尾表值 cap 为 2.224e-5，中段表值 cap 为 2.841e-5，但中段接入 theta(x)-x<x/36260 后只剩约 4.46e-11 的未分配余量。因此不能再用粗 contour 或未登记舍入误差含混通过；必须先固定同一显式公式口径，再逐项给出 finite-zero 主块、zero-free tail、修正项和舍入 hash 的数值账本。

```text
budget_caps_arithmetic_fixed=true
middle_splice_tiny_slack_guard_closed=true
current_coarse_contour_rejected_for_budget=true
psi_epsilon_budget_partition_closed=false
same_explicit_formula_convention_closed=false
finite_verified_zero_main_block_budget_closed=false
zero_free_tail_numerical_budget_closed=false
directed_rounding_budget_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 预算上限

| site | cap_type | cap | derived_theta_slack | consequence |
| --- | --- | --- | --- | --- |
| high tail x>=e^28 | psi table relative cap | `2.224000000000000000e-5` | `5.338599007170435742e-6` | finite-zero + zero-free-tail + corrections + rounding must fit below eps_psi(28) |
| middle strip 8e11<=x<=e^28 | psi table relative cap | `2.841000000000000000e-5` | `4.457340209326913989e-11` | after psi-theta gap, unbudgeted error must be < middle theta slack |
| middle theta splice | unallocated splice slack | `4.457340209326913989e-11` | `4.457340209326913989e-11` | this is only about 4.46e-11, so no hidden rounding or convention error is tolerable |

## 2. 粗模板失败倍数

```text
high_tail_b28=2.779902555195e+12
middle_left_8e11=2.093733314265e+12
```

## 3. 自足替换

```text
PsiEpsilonBudgetPartitionLedger
  =>
SameExplicitFormulaConventionLedger AND FiniteVerifiedZeroMainBlockNumericalBudgetLedger AND ZeroFreeTailNumericalBudgetLedger AND PrimePowerAndTrivialZeroCorrectionBudgetLedger AND DirectedRoundingAndIntervalPropagationBudgetLedger AND TableGeneratorHashInterfaceLedger

SameExplicitFormulaConventionLedger
  =>
must be closed before numerical component budgets can be added

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审查假设反例链可调用的 psi 表预算，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `PsiEpsilonBudgetPartitionGateActive` | `true` | `true` | 有限零点到尾项桥接证书已把下一最窄点压到 psi epsilon 预算分摊。 | PsiEpsilonBudgetPartitionLedger |
| `BudgetCapsArithmeticFixed` | `true` | `true` | 高尾 cap、中段 cap 与中段 theta 拼接余量已被精确固定，不能再用模糊常数吸收误差。 | budget caps fixed, component bounds still open |
| `MiddleSpliceTinySlackGuard` | `true` | `true` | 中段 theta 拼接余量约 4.46e-11；任何未登记舍入、尾项或公式差异都会破坏拼接。 | SameExplicitFormulaConventionLedger AND DirectedRoundingAndIntervalPropagationBudgetLedger |
| `CurrentCoarseContourRejectedForBudget` | `true` | `true` | 既有 C=1280,C_Z=65536 模板失败：高尾约 2.780e+12 倍，中段约 2.094e+12 倍。 | FiniteVerifiedZeroMainBlockNumericalBudgetLedger AND ZeroFreeTailNumericalBudgetLedger |
| `SameExplicitFormulaConventionLedger` | `false` | `false` | 预算分摊前必须先固定同一显式公式、截断、平滑、prime-power 与 zero-free tail 口径。 | without this, component budgets are not comparable |
| `FiniteVerifiedZeroMainBlockNumericalBudgetLedger` | `false` | `false` | 需要有限 verified-zero 主块在 e^28 与 8e11 两个端点及区间传播中的数值上界。 | FiniteRHHeightEndpointLedger |
| `ZeroFreeTailNumericalBudgetLedger` | `false` | `false` | 需要零点自由尾项在同一表公式中的数值上界，并证明不与 finite-zero 主块重复扣费。 | ZeroFreeTailStartHeightLedger |
| `PrimePowerAndTrivialZeroCorrectionBudgetLedger` | `false` | `false` | 需要素数幂、平凡零点和端点修正在 psi 表口径下的剩余预算。 | SameExplicitFormulaConventionLedger |
| `DirectedRoundingAndIntervalPropagationBudgetLedger` | `false` | `false` | 需要外向舍入和区间传播误差严格小于中段极薄余量。 | TableGeneratorHashInterfaceLedger |
| `PsiEpsilonBudgetPartitionLedger` | `false` | `false` | 当前只固定预算上限和失败模板；尚未给出各组件相加小于 cap 的可复算账本。 | SameExplicitFormulaConventionLedger AND FiniteVerifiedZeroMainBlockNumericalBudgetLedger AND ZeroFreeTailNumericalBudgetLedger AND PrimePowerAndTrivialZeroCorrectionBudgetLedger AND DirectedRoundingAndIntervalPropagationBudgetLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | psi epsilon 预算分摊不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
SameExplicitFormulaConventionLedger
```
