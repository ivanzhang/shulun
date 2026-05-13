# Prime Matrix strict 父支撑数值 envelope 路由器

**状态：** `parent_support_envelope_reduced_to_dilated_parent_window_cold_table_open`

`ParentScaledChildUnionSupportNumericEnvelope` 的几何核心可以关闭：若父窗口为 `[L,R]`，子乘子为 `g`，外向生成器给出子窗口 `[floor(L/g),ceil(R/g)]`，投回父尺度后为 `[g floor(L/g),g ceil(R/g)]`。每个这样的区间都包含 `[L,R]`，所以所有兄弟投影窗口的并集不是复杂多段集合，而是单个扩张父窗口 `[L_*,R_*]`；左右扩张宽度都小于最大子乘子。于是父投影支撑被 `N_{H_U}([L_*,R_*])` 控制，可接入规范 `C_core^*` 冷核心表。但要得到数值 envelope，还必须证明该扩张父窗口冷，或排斥热核心/PDEC/SAE 回流；因此行/列命题仍未无条件闭合。

```text
parent_support_target_imported=true
sibling_projection_identity_imported=true
scaled_child_union_single_interval_geometry_proved=true
collar_width_lt_max_child_proved=true
projected_support_to_dilated_parent_window_proved=true
parent_dilated_window_cold_core_table_proved=false
parent_dilated_window_hot_return_excluded=false
parent_scaled_child_union_support_numeric_envelope_proved=false
row_column_unconditional_closed=false
```

## 几何引理

| lemma | statement | effect |
|---|---|---|
| `scaled child interval contains parent interval` | `g*floor(L/g)<=L<=R<=g*ceil(R/g)` | 所有兄弟投影窗口都覆盖同一个父窗口。 |
| `single collar interval` | `union_g [g floor(L/g),g ceil(R/g)] = [L_*,R_*]` | scaled-child union 不是多段并集，而是单个 collar 扩张。 |
| `collar width` | `0<=L-L_*<g_max and 0<=R_*-R<g_max` | 边界外扩只由最大子乘子控制。 |
| `parent divisor support` | `pi(F_U) subset {d:d\|H_U, d in [L_*,R_*]}` | 父支撑数值界可接入规范冷核心窗口表。 |
| `cold or hot parent window` | `N_{H_U}([L_*,R_*])<=C_core^*(parent key) or hot return` | 若父扩张窗口不冷，失败必须命名为热核心/PDEC/SAE。 |

## 有限几何核验

| parent window | children | union interval | g_max | left collar | right collar | single interval | collar bound |
|---|---|---|---:|---:|---:|---:|---:|
| `[20, 180]` | `[2, 3, 5, 6]` | `[18, 180]` | 6 | 2 | 0 | `true` | `true` |
| `[30, 240]` | `[2, 3, 4, 5, 7]` | `[28, 245]` | 7 | 2 | 5 | `true` | `true` |
| `[50, 420]` | `[3, 4, 5, 6, 7, 9]` | `[45, 423]` | 9 | 5 | 3 | `true` | `true` |
| `[60, 720]` | `[4, 5, 6, 7, 8, 9, 10]` | `[54, 721]` | 10 | 6 | 1 | `true` | `true` |
| `[401, 4001]` | `[11, 13, 17, 19, 23]` | `[390, 4012]` | 23 | 11 | 11 | `true` | `true` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `ParentSupportTargetImported` | `true` | `true` | 上一层已把 sibling numeric envelope 压成父投影支撑。 | `ParentScaledChildUnionSupportNumericEnvelope` |
| `ScaledChildUnionSingleIntervalProved` | `true` | `true` | 同一父窗口外向缩放回来的兄弟投影并集是单个 collar 扩张区间。 | `ParentSiblingDilatedWindowColdCoreThresholdTable` |
| `CollarWidthBoundProved` | `true` | `true` | 左右 collar 宽度均小于最大子乘子。 | `ParentSiblingDilatedWindowColdCoreThresholdTable` |
| `ProjectedSupportToDilatedWindowProved` | `true` | `true` | 父投影支撑被单个扩张父窗口上的除数计数控制。 | `ParentSiblingDilatedWindowColdCoreThresholdTable` |
| `ConditionalColdCoreInsertionClosed` | `true` | `false` | 若扩张父窗口冷，则支撑项可由 C_core^* 表控制。 | `ColdCoreThresholdFunctionNumericTable` |
| `ParentDilatedWindowHotReturnExcluded` | `false` | `false` | 若扩张父窗口热，仍需排斥热核心/PDEC/SAE 回流。 | `ParentSiblingDilatedWindowHotCorePDECorSAEExclusion` |
| `ParentSupportNumericEnvelopeProved` | `false` | `false` | 几何压缩已闭合，但冷核心数值表或热回流排斥尚未完成。 | `ParentSiblingDilatedWindowColdCoreThresholdTable AND ParentSiblingDilatedWindowHotCorePDECorSAEExclusion` |
| `SiblingColdCoreThresholdNumericEnvelopeProved` | `false` | `false` | 父支撑数值界、overlap 和 PDEC 阈值仍未全部闭合。 | `ParentSiblingDilatedWindowColdCoreThresholdTable AND SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion AND SameParameterPDECThresholdNumericTable` |
| `TerminalColdWindowAntiCascadeProved` | `false` | `false` | 反级联仍需父扩张窗口数值表和热/固定历史排斥。 | `SiblingColdCoreThresholdNumericEnvelopeTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | `ParentSiblingDilatedWindowColdCoreThresholdTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`ParentSiblingDilatedWindowColdCoreThresholdTable`。
- 并行保留：
  - `ParentSiblingDilatedWindowHotCorePDECorSAEExclusion`
  - `SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion`
  - `ColdCoreThresholdFunctionNumericTable`
  - `SameParameterPDECThresholdNumericTable`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `experiments/prime_matrix_strict_parent_support_numeric_envelope_router.py` | `e652d018b52e02c7f1c265977731e8a532f63bdabd19d21bfac7466ef62de16b` |
| `docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json` | `52bd322127d85f72df347da33b5ccc71b6ef2c023539db38244793e6d8d3448c` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json` | `c93a11c1f9f9a11728fb454eb16ead7a4cc308bdfcf2647af6dcb20d6f405602` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
