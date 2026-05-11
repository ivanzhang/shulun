# Prime Matrix strict actual moving-block/NC-BLK 对接路由器

**状态：** `strict_actual_moving_block_reduced_to_global_terminal_modelgap_open`

`ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` 在 strict 链中已不能作为独立无名出口保留：有低维签名时进入 PDEC/SAE/ColumnCRT/sparse 终端，无低维签名时进入早期零行L2-flat/终端包；后者已调和为 `GlobalPDECorSparseTerminalExclusion`，再由全局拆分压到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`。moving-block 专属 DPRC 兼容门可删除，但 `ExplicitModelGapAndFiniteDPRCLedger` 仍是独立账本。因此当前最窄剩余不是 moving-block 本身，而是全局终端容量/内部大筛门与模型余量账本；直接矛盾仍未达到，行/列命题不能宣称无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
counterexample_assumption_only=true
strict_actual_moving_block_router_closed=true
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
new_actual_source_entropy_theorem_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_after_router=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

## 1. 反例链压缩

```text
Assume EarlyZeroRowWithinP
ActualNoncanonicalMovingBlockSpreadNCBLK cannot remain unnamed
registered low-dimensional signature -> PDEC/SAE/ColumnCRT/sparse terminal
no registered signature -> pure L2-flat/early-zero terminal package
early-zero terminal schema -> GlobalPDECorSparseTerminalExclusion
global terminal split -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
DPRC compatibility gate removed, ExplicitModelGapAndFiniteDPRCLedger remains
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictActualMovingBlockInputActive` | `true` | `false` | 上一层 strict 恒等式分类已把最窄点压成 actual noncanonical moving-block/NC-BLK。 | ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只在 Assume EarlyZeroRowWithinP 的假设链条中传递，不用真实零行缺席作证。 | 所有输出必须是反例链内的命名终端、模型账本或打开输入。 |
| `MovingBlockTerminalReductionImported` | `true` | `true` | actual same-(u,v) moving block 有登记低维签名则进 PDEC/SAE/ColumnCRT；无签名则进 L2-flat/早期零行终端包。 | EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock。 |
| `EarlyZeroTerminalSchemaReconciledImported` | `true` | `true` | 抽象 EarlyZeroTerminalExclusionPackage 已与 anchor、cofactor、early-band、DLS 回流 schema 调和。 | GlobalPDECorSparseTerminalExclusion。 |
| `DPRCCompatibilityGateRemovedImported` | `true` | `true` | moving-block 替换没有引入新的 DPRC 口径；兼容性门可删除，但模型账本自身仍保留。 | ExplicitModelGapAndFiniteDPRCLedger |
| `GlobalTerminalSplitImported` | `true` | `true` | GlobalPDECorSparseTerminalExclusion 已与全局终端家族拆分对齐。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `CurrentMaterializedTerminalFrontierExhausted` | `true` | `true` | 当前已物化 PDEC 与 sparse/LocalSurvivor 前沿清零；future schema 只是准入纪律。 | 这不是未来全局 family 不存在的证明。 |
| `StrictActualMovingBlockNoUnnamedExit` | `true` | `true` | strict moving-block/NC-BLK 不能再作为独立无名出口停留。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `DirectContradictionNotYetReached` | `true` | `false` | 早期零行反例链已被挤压到命名终端与模型账本，但尚未推出足以闭合命题的直接矛盾。 | 需证明终端容量/内部大筛，或证明模型余量账本。 |
| `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` | `false` | `false` | 仍未证明全局 PDEC-CAP 容量证书或内部 CleanKLS/DLS 大筛吸收。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `ExplicitModelGapAndFiniteDPRCLedger` | `false` | `false` | P<2003 有限 DPRC 与 P>=2003 模型余量账本仍需正式证明。 | ExplicitModelGapAndFiniteDPRCLedger |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终独立晋级验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 直接矛盾缺口

若要把早期零行反例链与真实结构链变成直接矛盾，需要再证明：反例强制的终端对象落入可排斥的全局 PDEC-CAP / internal CleanKLS 大筛容量门，并同时支付 ExplicitModelGapAndFiniteDPRCLedger。当前材料只证明无名出口不存在，没有证明这些终端门本身。

## 4. 下一主攻点

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

连同独立晋级门：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```
