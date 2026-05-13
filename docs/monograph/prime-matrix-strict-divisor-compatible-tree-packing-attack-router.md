# Prime Matrix strict 除数兼容冷历史树打包界攻坚路由器

**状态：** `divisor_compatible_tree_packing_requires_cold_window_prefix_branching_open`

`DivisorCompatibleColdHistoryTreePackingBound` 不能只靠 `D(W)|h_0` 闭合。素数幂频率给出结构性阻塞：若 `h_0=2^a`，有序乘积分组本身就可产生约 `2^(a-1)` 条形式历史；即使把因子限制为 2 和 4，数量也按 Fibonacci(a) 增长，约为 `P^0.694`，仍大于 `alpha=0.43` 的需求阶。因此树打包界必须使用冷窗口约束和前缀分叉回流：过多分叉必须触发热核心、固定历史或 LCM 共同核。

```text
divisor_compatibility_alone_rejected_as_sufficient=true
prime_power_cascade_case_closed=false
cold_history_prefix_branching_hot_or_fixed_return_proved=false
divisor_compatible_cold_history_tree_packing_bound_proved=false
row_column_unconditional_closed=false
```

## 阻塞模型

| model | history_count_lower_shape | p_exponent_if_2a_about_p | demand_exponent_alpha | beats_alpha_043 | meaning |
|---|---|---:|---:|---:|---|
| `all powers of 2 as grouped factors` | `2^(a-1) for h_0=2^a` | 1.000000 | 0.430000 | `true` | 若冷条件不进一步剪枝，仅靠 D(W)\|h_0 无法阻止有序分组爆炸。 |
| `factors restricted to 2 and 4` | `Fibonacci(a)` | 0.694242 | 0.430000 | `true` | 即使只允许两种小乘子，增长阶约 P^0.694，也大于需求阶 P^0.43。 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `TreePackingTargetImported` | `true` | `false` | 上一层已把有效剪枝压成除数兼容冷历史树打包界。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `DivisorCompatibilityInterfaceImported` | `true` | `true` | D(W)\|h_0 与 H_W=h_0/D(W) 的接口已闭合。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `DivisorCompatibilityAloneRejected` | `true` | `true` | 素数幂频率模型显示仅靠 D(W)\|h_0 仍可产生过大的有序历史树。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma` |
| `ColdWindowConstraintMustBeUsed` | `true` | `false` | 必须利用冷窗口 N_{H_W}(I_W)<=C_core(W)；否则无法剪掉素数幂级联。 | `TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `PrefixBranchingReturnRoutesRegistered` | `true` | `false` | 过多同前缀分叉若不是冷兼容，必须回流热核心、固定历史或 LCM 共同核。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma` |
| `PrimePowerCascadeCaseClosed` | `false` | `false` | 尚未排斥最危险的小乘子/素数幂级联冷窗口。 | `PrimePowerCascadeColdWindowExclusionOrCapacityTable` |
| `DivisorCompatibleColdHistoryTreePackingBoundProved` | `false` | `false` | 树打包界必须同时使用冷窗口反级联和前缀分叉回流；当前未证明。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma AND PrimePowerCascadeColdWindowExclusionOrCapacityTable AND TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `ColdSupplyNumericEnvelopeProved` | `false` | `false` | 树打包界之外，仍需 C_core 与 T_PDEC 同参数数值表。 | `DivisorCompatibleColdHistoryTreePackingBound AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`ColdHistoryPrefixBranchingHotOrFixedReturnLemma`。
- 并行保留：
  - `PrimePowerCascadeColdWindowExclusionOrCapacityTable`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `DenseLCMOrLowMultiplierCommonKernelReturn`
  - `ColdCoreThresholdFunctionNumericTable`
  - `SameParameterPDECThresholdNumericTable`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.json` | `72d7aeeb5a09864efcb9cd729d4d5331b1adfb780ec33b3a1ae29dfe6e67431b` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json` | `2604e2de93bc17bbe7678dddccf958b8a747714286d2c1ab8d5734246be78733` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `experiments/prime_matrix_strict_divisor_compatible_tree_packing_attack_router.py` | `42f5ca4c0b5ed9ea4cf89aa0f1cad7609ab947b7ffb2c75a26f034c34e931f06` |
