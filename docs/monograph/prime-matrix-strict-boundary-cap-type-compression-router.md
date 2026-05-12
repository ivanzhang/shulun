# Prime Matrix strict 边界帽 formal-unit 类型压缩路由器

**状态：** `boundary_cap_type_compression_reduced_to_forced_count_type_bound_repeated_label_open`

`BoundaryCapFormalUnitTypeCompressionDichotomy` 继续下钻后，真正能形成明显矛盾的统一场已经固定：早期零行给出有限无漏 formal-unit obligations；把每个 obligation 投影到不含绝对行号的 boundary type。若强制实例数 `N` 大于类型数 `T`，鸽巢给出短复现；若类型数不被压缩，则类型增长必须登记为相位缺陷。当前已闭合的是 type key 定义和条件鸽巢骨架；未闭合的是 `N` 的有效下界、`T` 的上界或类型爆炸回流、以及重复 type 是否确实保持同一素标签集。行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
row_free_type_key_definition_closed=true
pigeonhole_skeleton_conditional_closed=true
boundary_cap_forced_obligation_lower_bound_proved=false
row_free_type_upper_or_explosion_defect_proved=false
repeated_type_to_stable_same_label_return_proved=false
boundary_cap_formal_unit_type_compression_dichotomy_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 类型压缩骨架

拆分前：

```text
BoundaryCapFormalUnitTypeCompressionDichotomy
```

拆分后：

```text
BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect AND RepeatedBoundaryTypeToStableSameLabelReturn
```

条件矛盾流水线：

```text
EarlyZeroRowWithinP
  ->
UniversalFormalUnitExtractor gives finite no-loss formal-unit records
  ->
Boundary row-free type map pi is defined
  ->
N_forced > T_type gives repeated type within boundary cap
  ->
Repeated type -> stable same-label return
  ->
Label product lower bound gives prod(Q)>|Delta|
  ->
CRT short recurrence lemma gives contradiction
```

## 2. 行无关 type key

| field | role |
| --- | --- |
| `source_family_id` | 锁定 Endpoint/TailAnchor/HighOverlap/ColoredCorridor/SmoothCore/Sparse/RankinConstant 等有限来源族。 |
| `branch_type` | 区分 physical、phase_defect、carry_cofactor、return、quotient/reuse 等分支。 |
| `window_shape` | 只保留边界帽相对形状，不包含绝对行号；否则无法形成短复现。 |
| `D0,K,Omega` | 继承核心尺度、截断与重叠阈值；无参数时写 canonical null。 |
| `phase_key` | 相位、residue、anchor、fixed-core 或 identity；漂移必须登记为 phase defect。 |
| `anchor_set_hash` | 由同一 formal unit 的 payload 复算 A；不得后验换锚。 |
| `carry_cofactor_signature` | 记录 carry-shell、cofactor-depth、anchor-collar 需要保持的行无关壳签名。 |
| `label_support_skeleton` | 记录要在短复现中保持的素标签骨架；若漂移则进入缺陷分支。 |

## 3. 压缩二分

| case | meaning | consequence | remaining |
| --- | --- | --- | --- |
| `T<N` | 边界帽 forced obligations 数 N 大于行无关类型数 T。 | 鸽巢给出两个不同边界行/位置共享同一类型，位移 Delta 小于边界帽高度。 | RepeatedBoundaryTypeToStableSameLabelReturn |
| `T>=N` | 类型数没有被压缩，反例链必须在边界帽中持续产生新 phase/anchor/carry/label 类型。 | 这不是自由增长；按 no-loss return 必须登记为 phase defect 或新 layer payload。 | BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect |
| `Repeated type` | 同一行无关 type key 在短位移下复现。 | 若 type key 足够完整，得到同 formal unit 同标签短复现；再接标签乘积下界和 CRT 矛盾。 | RepeatedBoundaryTypeToStableSameLabelReturn AND StableReturnLargeLabelSupportProductLowerBound |
| `Drifting type` | 为避免复现而改变 phase_key、anchor_set_hash、carry/cofactor 或 label skeleton。 | 漂移必须作为已登记坏窗/位移/相位缺陷进入 PDEC/SAE/ColumnCRT。 | SignatureDriftToRegisteredPhaseDefectTheorem |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BoundaryTypeCompressionInputActive` | `true` | `false` | 上一层已把首要硬点固定为边界帽 formal-unit 类型压缩。 | BoundaryCapFormalUnitTypeCompressionDichotomy |
| `UniversalFormalUnitExtractorImported` | `true` | `true` | 任意早期零行 witness 可产出有限、无漏、可哈希的 formal unit records。 | 这只给有限记录，不给类型数量上界。 |
| `PartitionAndAssignmentImported` | `true` | `true` | 义务域 O(w) 已被有限 key-fibers 覆盖，且每个 key 归入有限 source family 或命名 return。 | 仍需边界帽上的计数压缩。 |
| `NoLossAndHashStabilityImported` | `true` | `true` | 未闭合对象不会丢失，formal_unit/source_tuple/hash 在回流下稳定。 | 稳定命名不等于类型数足够小。 |
| `AnchorAndSourceTupleFieldsImported` | `true` | `true` | A、D0/K/Omega、phase_rule、anchor_set_hash 可由同一 formal unit payload 复算。 | 需要将这些字段投影成行无关 type key 并计数。 |
| `EarlyZeroRigidityPressureImported` | `true` | `true` | 早期零行已被 CLB、carry-shell、cofactor-depth、anchor-collar 与终端无第四出口约束。 | AnchorCollarPrimeFiberCapacityBoundOrPDECReturn |
| `RowFreeTypeKeyDefinitionClosed` | `true` | `true` | 可定义不含绝对行号的 boundary-cap type key；重复才有可能推出短复现。 | 定义闭合，不代表类型数上界或复现推出同标签。 |
| `PigeonholeSkeletonConditionalClosed` | `true` | `true` | 若 forced obligation 数 N 大于 row-free type 数 T，则同类型短复现；若 T>=N，则必须解释类型爆炸。 | BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect |
| `PhaseScanImportedAsHeuristicSupportOnly` | `true` | `true` | 大标签乘积超过 P 支持 CRT 后半段，但实验不能证明类型压缩。 | 仍需正式 N/T 不等式。 |
| `BoundaryCapForcedObligationLowerBoundCurrentCorpusProved` | `false` | `false` | 尚未给出边界帽中必须保留的 forced formal-unit obligations 的有效下界 N。 | BoundaryCapForcedFormalUnitObligationLowerBound |
| `RowFreeTypeUpperOrExplosionDefectCurrentCorpusProved` | `false` | `false` | 尚未证明 row-free type alphabet 上界 T<N，或 T>=N 时自动产生登记相位缺陷。 | BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect |
| `RepeatedTypeToStableReturnCurrentCorpusProved` | `false` | `false` | 尚未证明重复 type key 足以保持同一素标签集 Q 并得到同 formal unit 的同标签短复现。 | RepeatedBoundaryTypeToStableSameLabelReturn |
| `BoundaryCapTypeCompressionCurrentCorpusProved` | `false` | `false` | 类型压缩只完成了定义与条件鸽巢骨架，核心 N/T/重复到标签 三项仍未证明。 | BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect AND RepeatedBoundaryTypeToStableSameLabelReturn |

## 5. 下一主攻点

```text
BoundaryCapForcedFormalUnitObligationLowerBound
```

并行硬点：

```text
BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect AND RepeatedBoundaryTypeToStableSameLabelReturn
```

完整剩余链：

```text
(BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect AND RepeatedBoundaryTypeToStableSameLabelReturn) AND StableReturnLargeLabelSupportProductLowerBound AND SignatureDriftToRegisteredPhaseDefectTheorem
```
