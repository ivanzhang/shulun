# Prime Matrix strict 冷核心阈值函数表路由器

**状态：** `cold_core_threshold_function_schema_closed_summation_dominance_open`

`ColdCoreThresholdFunctionNumericTable` 的定义/函数表口径可以关闭：终端窗口端点生成器、旧 `I_W` 记号等价、规范 `C_core` 注册键和 dyadic/素数幂顺序不变性已经对齐。同时存在基准长度 cap：对任意整数窗口 `[L,R]`，`N_H([L,R])<=R-L+1`。但长度 cap 只是可复核的粗数值行，不能证明同参数求和优势；真正剩余是 `SameParameterCoreThresholdSummationDominanceTable`，即证明在实际冷历史族上 `sum_W(T_PDEC(W)-1)C_core(W)` 被需求项反超。

```text
cold_core_table_target_imported=true
endpoint_generator_and_legacy_notation_closed=true
cold_core_threshold_registry_and_order_invariance_closed=true
trivial_interval_length_cap_closed=true
cold_core_function_table_schema_closed=true
core_threshold_summation_dominance_proved=false
cold_core_threshold_numeric_table_proved=false
row_column_unconditional_closed=false
```

## 1. 长度 cap 样本

| left | right | length | sample divisor count | valid |
| --- | --- | --- | --- | --- |
| `10` | `17` | `8` | `4` | `true` |
| `31` | `42` | `12` | `6` | `true` |
| `100` | `119` | `20` | `9` | `true` |
| `511` | `545` | `35` | `12` | `true` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ColdCoreTableTargetImported` | `true` | `true` | 上一层已把冷供给数值包主攻点指向 C_core 数值表。 | ColdCoreThresholdFunctionNumericTable |
| `EndpointGeneratorAndLegacyNotationClosed` | `true` | `true` | 终端窗口端点生成器和旧 I_W 记号等价已闭合。 | ColdCoreThresholdFunctionNumericTable |
| `ColdCoreThresholdRegistryAndOrderInvarianceClosed` | `true` | `true` | C_core 已绑定为规范终端窗口对象函数，不随 dyadic/素数幂拆分顺序变化。 | ColdCoreThresholdFunctionNumericTable |
| `TrivialIntervalLengthCapClosed` | `true` | `true` | 任何冷核心窗口都有 N_H([L,R])<=R-L+1 的基准数值 cap。 | SameParameterCoreThresholdSummationDominanceTable |
| `ColdCoreFunctionTableSchemaClosed` | `true` | `true` | C_core 表的对象、键、顺序不变性和基准 cap 已闭合。 | SameParameterCoreThresholdSummationDominanceTable |
| `CoreThresholdSummationDominanceProved` | `false` | `false` | 长度 cap 过粗；尚未证明 sum_W(T_PDEC(W)-1)C_core(W) 小于需求。 | SameParameterCoreThresholdSummationDominanceTable |
| `ColdCoreThresholdNumericTableProved` | `false` | `false` | 函数表结构闭合，但缺同参数可求和优势表。 | SameParameterCoreThresholdSummationDominanceTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | SameParameterCoreThresholdSummationDominanceTable AND SameParameterPDECThresholdNumericTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步最窄点

- 主攻：`SameParameterCoreThresholdSummationDominanceTable`。
- 含义：把已规范化的 C_core 函数表变成同参数可求和优势表。
- 边界：本步不证明最终数值优势，不闭合行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json` | `c93a11c1f9f9a11728fb454eb16ead7a4cc308bdfcf2647af6dcb20d6f405602` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.json` | `d713760f063f00117cf6564c911523cf43033f612fb2d51e62a37425156f769e` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json` | `e72a9d55dd3a27c1f9d6287afd6a8debc00a0ebe241977e72e0394bc02c04abf` |
| `experiments/prime_matrix_strict_cold_core_threshold_function_table_router.py` | `e86c4ad6fb7e7a026acf5f417887f0def0f4da1594bfca75ab1ceb12c9cdbbd4` |
