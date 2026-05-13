# Prime Matrix strict 旧 product-window 记号等价审查路由器

**状态：** `legacy_product_window_notation_equivalence_closed_threshold_binding_open`

`LegacyProductWindowNotationEquivalenceAudit` 可以关闭：已扫描当前相关语料，旧 `I_W/Y_W/product window ledger` 用法均为符号定义、描述性继承或计数槽位，没有发现与新端点生成器冲突的旧更新公式。因此旧窗口记号可统一解释为生成器输出。但涉及 `C_core(W)` 的阈值槽位仍未证明只依赖规范窗口尺度，最新唯一主攻点转为 `ColdCoreThresholdDyadicOrderInvarianceBindingLedger`。

```text
legacy_window_reference_count=46
no_conflicting_endpoint_formula_found=true
legacy_product_window_notation_equivalence_proved=true
cold_core_threshold_dyadic_order_invariance_proved=false
row_column_unconditional_closed=false
```

## 分类汇总

| classification | count |
|---|---:|
| `counting_slot` | 21 |
| `descriptive_inheritance` | 4 |
| `symbolic_definition` | 2 |
| `symbolic_reference` | 3 |
| `threshold_slot` | 16 |

## 旧记号命中

| file | line | classification | conflict | excerpt |
|---|---:|---|---:|---|
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 5 | `counting_slot` | `false` | 缩频终端核心除数窗口已被拆成冷预算和热异常两类。对历史词 W，令 H_W=h_0/D(W)，终端核心必须整除 H_W 并落在窗口 I_W。若 N_{H_W}(I_W)<=C_core(W)，则 Cap(W)<=C_core(W) 可直接插入 SAE 供给预算；若超过该阈值，则它是 TerminalCoreHotDivisorWindow，必须回流到 LCM  |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 31 | `counting_slot` | `false` | N_{H_W}(I_W)=#{k: k\|H_W, k in I_W}. |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 36 | `threshold_slot` | `false` | 对每个 `W` 固定阈值 `C_core(W)`： |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 39 | `counting_slot` | `false` | cold: N_{H_W}(I_W)<=C_core(W); |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 40 | `counting_slot` | `false` | hot:  N_{H_W}(I_W)> C_core(W). |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 50 | `symbolic_definition` | `false` | \| `terminal_core_window` \| Cores lie in I_W=(Y_W^-,Y_W^+] with endpoints inherited from the product window ledger. \| `closed` \| 终端核心落在明确窗口内。 \| |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 51 | `counting_slot` | `false` | \| `cold_hot_split` \| N_{H_W}(I_W)<=C_core(W) or N_{H_W}(I_W)>C_core(W). \| `closed_dichotomy` \| 单历史容量被拆成冷核心预算或热核心异常。 \| |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 52 | `threshold_slot` | `false` | \| `cold_core_insert` \| In the cold case, Cap(W)<=C_core(W) is valid in the SAE budget. \| `closed_conditional` \| 冷核心阈值可直接进入供给上界。 \| |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | 54 | `threshold_slot` | `false` | \| `budget_gap_after_cold_insert` \| After cold insertion, prove L_forced > sum_W (T_PDEC(W)-1) C_core(W). \| `open_input` \| 剩余供需比较转为冷核心阈值预算缺口。 \| |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 5 | `descriptive_inheritance` | `false` | formal-unit 稀疏历史重数已经压成缩频终端核心除数窗口计数。对历史词 W，令 D(W)=prod b_i c_i，则同一 formal unit 内该历史的终端核心 都必须整除 h_0/D(W)，并落在由窗口乘积账本给出的区间 I_W。因此 Mult_U(W)<=N_{h_0/D(W)}(I_W)。若该窗口计数过大，就回流为 TerminalCor |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 33 | `symbolic_reference` | `false` | k \| h_0/D(W),  k in I_W. |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 39 | `counting_slot` | `false` | Mult_U(W) <= N_{h_0/D(W)}(I_W). |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 46 | `threshold_slot` | `false` | 若该除数窗口热，则进入 `TerminalCoreHotDivisorWindowPDECorSAE`；若不热，则用冷核心阈值 `C_core(W)` 进入 SAE 预算。 |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 53 | `descriptive_inheritance` | `false` | \| `terminal_core_interval` \| Terminal cores k lie in an explicit interval I_W inherited from the product window ledger. \| `closed` \| 单历史容量变成缩频上的窗口除数计数。 \| |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 54 | `counting_slot` | `false` | \| `multiplicity_to_divisor_count` \| Mult_U(W) <= N_{h_0/D(W)}(I_W). \| `closed` \| 同一 formal unit 内同一历史词的重数不超过缩频终端核心除数数。 \| |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 55 | `counting_slot` | `false` | \| `hot_core_route` \| If N_{h_0/D(W)}(I_W) exceeds the cap, it is a terminal core hot divisor window and routes to PDEC/SAE. \| `registered_route_open` \| 单历史容量过大不是自由预算，而是回流到热除数/PDEC/ |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 56 | `threshold_slot` | `false` | \| `cold_core_capacity` \| If no hot core window occurs, Cap(W) is bounded by the registered cold-core threshold C_core(W). \| `closed_conditional` \| 在排除热核心出口后，单历史容量有可插入 SAE 预算的上界。 \| |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | 57 | `threshold_slot` | `false` | \| `cap_to_budget_gap` \| Insert Cap(W)<=C_core(W) into U_sparse <= sum_W (T_PDEC(W)-1)Cap(W). \| `closed_reduction` \| 单历史重数上界已接回供需预算缺口。 \| |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.md` | 20 | `counting_slot` | `false` | \| `cold_condition` \| `N_{H_W}(I_W)<=C_core(W)` \| `closed_dichotomy` \| 不满足冷条件的历史进入热核心回流。 \| |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.md` | 21 | `threshold_slot` | `false` | \| `effective_cold_supply` \| `U_np<=sum_{W in C_cold(h_0)} (T_PDEC(W)-1)C_core(W)` \| `open_bound` \| 必须对兼容冷历史树求和，而不是对全部形式历史求和。 \| |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.md` | 22 | `threshold_slot` | `false` | \| `tree_packing_goal` \| `sum_{W in C_cold(h_0)} (T_PDEC(W)-1)C_core(W) <= U0(P,z) < M#` \| `open_target` \| 这是有效剪枝闭合后应提供的数值包。 \| |
| `docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.md` | 29 | `counting_slot` | `false` | \| `ColdWindowConstraintMustBeUsed` \| `true` \| `false` \| 必须利用冷窗口 N_{H_W}(I_W)<=C_core(W)；否则无法剪掉素数幂级联。 \| `TerminalColdWindowCompatibilityAntiCascadeLemma` \| |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 71 | `symbolic_definition` | `false` | "formula": "Cores lie in I_W=(Y_W^-,Y_W^+] with endpoints inherited from the product window ledger.", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 77 | `counting_slot` | `false` | "formula": "N_{H_W}(I_W)<=C_core(W) or N_{H_W}(I_W)>C_core(W).", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 83 | `threshold_slot` | `false` | "formula": "In the cold case, Cap(W)<=C_core(W) is valid in the SAE budget.", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 95 | `threshold_slot` | `false` | "formula": "After cold insertion, prove L_forced > sum_W (T_PDEC(W)-1) C_core(W).", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 177 | `symbolic_reference` | `false` | "令 H_W=h_0/D(W)，终端核心必须整除 H_W 并落在窗口 I_W。" |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 178 | `counting_slot` | `false` | "若 N_{H_W}(I_W)<=C_core(W)，则 Cap(W)<=C_core(W) 可直接插入 SAE 供给预算；" |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 218 | `counting_slot` | `false` | "N_{H_W}(I_W)=#{k: k\|H_W, k in I_W}.", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 223 | `threshold_slot` | `false` | "对每个 `W` 固定阈值 `C_core(W)`：", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 226 | `counting_slot` | `false` | "cold: N_{H_W}(I_W)<=C_core(W);", |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | 227 | `counting_slot` | `false` | "hot:  N_{H_W}(I_W)> C_core(W).", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 71 | `descriptive_inheritance` | `false` | "formula": "Terminal cores k lie in an explicit interval I_W inherited from the product window ledger.", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 77 | `counting_slot` | `false` | "formula": "Mult_U(W) <= N_{h_0/D(W)}(I_W).", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 83 | `counting_slot` | `false` | "formula": "If N_{h_0/D(W)}(I_W) exceeds the cap, it is a terminal core hot divisor window and routes to PDEC/SAE.", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 89 | `threshold_slot` | `false` | "formula": "If no hot core window occurs, Cap(W) is bounded by the registered cold-core threshold C_core(W).", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 95 | `threshold_slot` | `false` | "formula": "Insert Cap(W)<=C_core(W) into U_sparse <= sum_W (T_PDEC(W)-1)Cap(W).", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 178 | `descriptive_inheritance` | `false` | "都必须整除 h_0/D(W)，并落在由窗口乘积账本给出的区间 I_W。" |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 179 | `counting_slot` | `false` | "因此 Mult_U(W)<=N_{h_0/D(W)}(I_W)。若该窗口计数过大，就回流为 " |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 220 | `symbolic_reference` | `false` | "k \| h_0/D(W),  k in I_W.", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 226 | `counting_slot` | `false` | "Mult_U(W) <= N_{h_0/D(W)}(I_W).", |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | 233 | `threshold_slot` | `false` | "若该除数窗口热，则进入 `TerminalCoreHotDivisorWindowPDECorSAE`；若不热，则用冷核心阈值 `C_core(W)` 进入 SAE 预算。", |
| `experiments/prime_matrix_strict_effective_cold_history_pruning_router.py` | 114 | `counting_slot` | `false` | "formula": "N_{H_W}(I_W)<=C_core(W)", |
| `experiments/prime_matrix_strict_effective_cold_history_pruning_router.py` | 120 | `threshold_slot` | `false` | "formula": "U_np<=sum_{W in C_cold(h_0)} (T_PDEC(W)-1)C_core(W)", |
| `experiments/prime_matrix_strict_effective_cold_history_pruning_router.py` | 126 | `threshold_slot` | `false` | "formula": "sum_{W in C_cold(h_0)} (T_PDEC(W)-1)C_core(W) <= U0(P,z) < M#", |
| `experiments/prime_matrix_strict_divisor_compatible_tree_packing_attack_router.py` | 161 | `counting_slot` | `false` | "必须利用冷窗口 N_{H_W}(I_W)<=C_core(W)；否则无法剪掉素数幂级联。", |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `LegacyEquivalenceTargetImported` | `true` | `false` | 上一层已把公式绑定压成旧记号等价和阈值绑定。 | `LegacyProductWindowNotationEquivalenceAudit` |
| `EndpointGeneratorAppendixImported` | `true` | `true` | 规范 product-window 端点生成器已定义并有样本账本。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `LegacyWindowReferencesFound` | `true` | `true` | 旧语料中的 I_W/Y_W/product-window/C_core 引用已扫描。 | `LegacyProductWindowNotationEquivalenceAudit` |
| `NoConflictingEndpointFormulaFound` | `true` | `true` | 未发现与新生成器冲突的旧端点更新公式。 | `LegacyProductWindowNotationEquivalenceAudit` |
| `SymbolicWindowNotationBoundToGenerator` | `true` | `true` | 旧 I_W/Y_W 作为符号窗口统一解释为生成器输出，不改变既有计数语句。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `LegacyProductWindowNotationEquivalenceProved` | `true` | `true` | 旧窗口记号等价到规范端点生成器；冲突公式不存在。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `ThresholdSlotStillOpen` | `true` | `false` | 涉及 C_core(W) 的行仍需证明阈值随 dyadic 重排不变。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `ProductWindowEndpointDyadicUpdateFormulaBindingProved` | `false` | `false` | 旧记号等价已闭合，但 C_core 阈值绑定仍未闭合。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `DyadicProductWindowEndpointCommutativityLedgerProved` | `false` | `false` | 端点部分已接回，阈值不变性未接回。 | `DyadicProductWindowEndpointCommutativityLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`ColdCoreThresholdDyadicOrderInvarianceBindingLedger`。
- 并行保留：
  - `ProductWindowEndpointDyadicUpdateFormulaBindingLedger`
  - `DyadicProductWindowEndpointCommutativityLedger`
  - `DyadicPrimePowerColdWindowCascadeExclusionLemma`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.md` | `cec86437d8db4b40bb00952fb0fcdc04e8b422a1e27ae29e270e9b46862776a1` |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.md` | `15214e6aed58ba8996c7a6ee2e3aa19716eb560309f050b0f6d0c8dde92be3a9` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | `faca65e1e870747b921a9a7641733c24a00ad1e5126d82d3f89a65f38098aa9d` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-formula-binding-router.json` | `aaf78bf3a8b79226fc17487b5e64b6bf3781fdd0d3a0e6bba26eb911e0d5af36` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | `de2224ecfcd95ee99d389df1143ac8174617eb5ddc56c134444c987018fb0ffb` |
| `experiments/prime_matrix_strict_divisor_compatible_tree_packing_attack_router.py` | `42f5ca4c0b5ed9ea4cf89aa0f1cad7609ab947b7ffb2c75a26f034c34e931f06` |
| `experiments/prime_matrix_strict_effective_cold_history_pruning_router.py` | `f205039960f2678ff0d69dcafa37a259a3c8639008d3cb370fc721c317716691` |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | `3587f2c55560e15233085d0a309d7ab67af5b3fa946f055e656bdfc81ad5d21b` |
| `experiments/prime_matrix_strict_legacy_product_window_equivalence_router.py` | `feed7dea7eb71b6f54c518e2f0191db02c1180cc4aed6911249b6d3e6df8f48c` |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | `201d1a7f8aad0195a25d222e1ee8e73b28b960a3875348ba70e52bf9bdd6f111` |
