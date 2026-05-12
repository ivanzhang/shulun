# Prime Matrix strict 同一显式公式口径路由器

**状态：** `same_explicit_formula_convention_reduced_to_table_algorithm_interval_hash_open`

同一显式公式口径不能由现有内部 Perron 粗链自动获得。仓库内部确实已经有 psi_0 精确公式、非平滑 Perron、零点和与平凡尾项的自洽 convention；但 Schoenfeld/Dusart epsilon 表还缺实际生成算法、区间传播规则和可复现 hash。因此本步把 convention 缺口压回表生成算法，而不是把粗链预算直接相加。

```text
internal_perron_convention_locally_closed=true
local_convention_does_not_imply_dusart_table_convention=true
same_explicit_formula_convention_closed=false
psi_vs_psi0_endpoint_jump_convention_closed=false
table_truncation_smoothing_kernel_convention_closed=false
finite_zero_tail_split_convention_closed=false
prime_power_theta_psi_transfer_same_table_convention_closed=false
interval_propagation_convention_closed=false
rounding_hash_convention_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. convention 对齐矩阵

| field | internal_status | table_match_needed | ledger |
| --- | --- | --- | --- |
| `base_function` | psi_0 exact formula closed | prove table uses psi, psi_0, or a converted endpoint convention with no hidden jump | `PsiVsPsi0EndpointJumpConventionLedger` |
| `kernel_and_truncation` | finite-T unsmoothed Perron closed for coarse B3 chain | identify the epsilon table kernel, height choice, smoothing and truncation rule | `TableTruncationSmoothingAndKernelConventionLedger` |
| `zero_split` | C=1280,C_Z=65536 zero-sum envelope closed but coarse | match finite verified-zero block and zero-free tail split used by the table | `FiniteZeroWindowAndZeroFreeTailSplitConventionLedger` |
| `prime_power_and_theta_transfer` | prime-power transfer closed for theta/Perron route | prove the same transfer direction and correction terms are used in psi epsilon table | `PrimePowerThetaPsiTransferSameTableConventionLedger` |
| `interval_propagation` | not supplied by current Perron certificates | show how b-grid or finite nodes propagate to all x in the high and middle ranges | `PsiEpsilonIntervalPropagationAndMonotonicityLedger` |
| `rounding_output` | not supplied by current Perron certificates | directed rounding and reproducible output hash for 0.00002224 and 1.00002841 | `ReproduciblePsiEpsilonTableComputationHashLedger` |

## 2. 自足替换

```text
SameExplicitFormulaConventionLedger
  =>
PsiEpsilonTableComputationAlgorithmLedger AND PsiVsPsi0EndpointJumpConventionLedger AND TableTruncationSmoothingAndKernelConventionLedger AND FiniteZeroWindowAndZeroFreeTailSplitConventionLedger AND PrimePowerThetaPsiTransferSameTableConventionLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger

PsiEpsilonTableComputationAlgorithmLedger
  =>
must specify the actual Schoenfeld/Dusart epsilon-table explicit formula before budgets can be added

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只统一假设反例链可调用的 psi 表显式公式口径，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `SameExplicitFormulaConventionGateActive` | `true` | `true` | 预算分摊证书已把下一最窄点压到同一显式公式口径。 | SameExplicitFormulaConventionLedger |
| `InternalPerronConventionLocallyClosed` | `true` | `true` | 仓库内部 B3/Perron 链已有 psi_0 精确公式、非平滑 Perron、零点和、平凡尾项与素数幂 convention。 | this is local to the coarse internal Perron route |
| `LocalConventionDoesNotImplyDusartTableConvention` | `true` | `true` | 内部 Perron convention 只说明粗链自洽；它没有给出 Schoenfeld/Dusart epsilon 表实际生成算法。 | PsiEpsilonTableComputationAlgorithmLedger |
| `PsiVsPsi0EndpointJumpConventionLedger` | `false` | `false` | 需要证明表值使用的 psi/psi_0 端点半权和跳点 convention 与内部公式可无损转换。 | PsiEpsilonTableComputationAlgorithmLedger |
| `TableTruncationSmoothingAndKernelConventionLedger` | `false` | `false` | 需要表生成器的截断高度、平滑核或非平滑核、边界避零规则和误差项定义。 | PsiEpsilonTableComputationAlgorithmLedger |
| `FiniteZeroWindowAndZeroFreeTailSplitConventionLedger` | `false` | `false` | 需要 finite verified-zero 主块与 zero-free tail 在表公式中的分界和不重复计费规则。 | PsiEpsilonTableComputationAlgorithmLedger |
| `PrimePowerThetaPsiTransferSameTableConventionLedger` | `false` | `false` | 需要素数幂、theta/psi 转换和常数项在表公式中的方向与符号。 | PsiEpsilonTableComputationAlgorithmLedger |
| `PsiEpsilonIntervalPropagationAndMonotonicityLedger` | `false` | `false` | 需要证明离散表节点如何传播到整段 x 区间，含单调性、跳点和端点。 | PsiEpsilonIntervalPropagationAndMonotonicityLedger |
| `ReproduciblePsiEpsilonTableComputationHashLedger` | `false` | `false` | 需要可复现计算 hash 与外向舍入证书，尤其要控制中段 4.46e-11 余量。 | ReproduciblePsiEpsilonTableComputationHashLedger |
| `SameExplicitFormulaConventionLedger` | `false` | `false` | 当前只能确认内部粗 Perron 公式自洽，不能确认它与 Schoenfeld/Dusart epsilon 表同口径。 | PsiEpsilonTableComputationAlgorithmLedger AND PsiVsPsi0EndpointJumpConventionLedger AND TableTruncationSmoothingAndKernelConventionLedger AND FiniteZeroWindowAndZeroFreeTailSplitConventionLedger AND PrimePowerThetaPsiTransferSameTableConventionLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `GeneratorOpenItemsAgreeWithConventionGap` | `true` | `true` | epsilon 表生成器审计中的算法、区间传播和 hash 开放项正是 convention 未闭合的来源。 | PsiEpsilonTableComputationAlgorithmLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 同一显式公式口径审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
PsiEpsilonTableComputationAlgorithmLedger
```
