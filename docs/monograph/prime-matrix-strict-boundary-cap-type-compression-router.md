# Prime Matrix strict 边界帽 formal-unit 类型压缩硬攻路由器

**状态：** `boundary_cap_type_compression_reduced_to_label_preserving_quotient_entropy_deficit_open`

`BoundaryCapFormalUnitTypeCompressionDichotomy` 继续保持原 N/T/复现骨架：早期零行给出有限无漏 formal-unit obligations，行无关 type key 与条件鸽巢骨架已闭合。新增审查结论是：已闭合的 formal-unit 哈希纪律只保证同一对象不换名、不漏账，不自动给边界帽内类型数小于 forced records 的鸽巢亏损。完整 key 重复会保留标签但未证数量压缩；粗 key 重复会丢失标签集 Q，CRT 短复现矛盾无法调用。因此真正最窄新增输入是 `BoundaryCapLabelPreservingQuotientEntropyDeficit`，并行必须保留 `BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn`。行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
row_free_type_key_definition_closed=true
pigeonhole_skeleton_conditional_closed=true
no_free_type_compression_lemma_proved=true
full_key_repeat_would_preserve_labels=true
coarse_type_repeat_loses_label_support=true
boundary_cap_forced_obligation_lower_bound_proved=false
row_free_type_upper_or_explosion_defect_proved=false
repeated_type_to_stable_same_label_return_proved=false
label_preserving_quotient_entropy_deficit_proved=false
type_drift_to_registered_defect_proved=false
boundary_cap_type_compression_dichotomy_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
BoundaryCapFormalUnitTypeCompressionDichotomy
  => NoFreeTypeCompressionLemma
  => BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect AND RepeatedBoundaryTypeToStableSameLabelReturn
  with refined nonfree gate: BoundaryCapLabelPreservingQuotientEntropyDeficit AND BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn
```

现有 formal-unit 记录与哈希闭合的是保真命名，不是压缩计数。完整 key 重复足以保持标签但没有数量亏损；粗 key 可制造重复但丢失标签保持，因此必须新增保标签商类型熵亏损或把所有标签漂移登记为已排斥缺陷。

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
| `Complete key repeat` | 完整 key 在短位移下重复。 | 标签字段保持，可接同 formal unit 短复现；但当前缺少完整 key 数量上界。 | BoundaryCapLabelPreservingQuotientEntropyDeficit |
| `Coarse key repeat` | 为了制造鸽巢重复而忽略 label_support_skeleton 或 phase/carry 字段。 | 重复不再保证同一素标签集 Q，必须证明漂移进入 PDEC/SAE/ColumnCRT。 | BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BoundaryCapTypeCompressionTargetActive` | `true` | `false` | 上一层把稳定短复现的上游强制机制压成边界帽 formal-unit 类型压缩。 | BoundaryCapFormalUnitTypeCompressionDichotomy |
| `EarlyZeroBoundaryCapPressureImported` | `true` | `true` | 早期零行假设已被 CLB、carry-shell、cofactor-depth、anchor-collar 与命名终端矩阵夹住。 | forced boundary-cap records exist only inside named contradiction matrix。 |
| `FormalUnitRecordAndHashStabilityImported` | `true` | `true` | 任意假设 witness 可生成有限无漏 formal-unit 记录，且 source/return 哈希稳定。 | 记录保真可用，但还不是类型数上界。 |
| `NoFreeTypeCompressionLemma` | `true` | `true` | formal-unit 哈希是保真命名纪律：它防止账本换口径，但不会自动让不同 witness 记录落入少数类型。 | 必须另证保标签商类型的熵亏损，或把类型增长登记为相位缺陷。 |
| `RowFreeTypeKeyDefinitionClosed` | `true` | `true` | 行无关 boundary-cap type key 的字段可定义：source family、branch、window shape、phase、anchor、carry/cofactor 与 label skeleton。 | 定义闭合，不代表类型数上界或复现推出同标签。 |
| `PigeonholeSkeletonConditionalClosed` | `true` | `true` | 若 forced obligation 数 N 大于保标签 row-free type 数 T，则同类型短复现；若 T>=N，则必须解释类型爆炸。 | BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect |
| `BoundaryCapForcedObligationLowerBoundCurrentCorpusProved` | `false` | `false` | 尚未给出边界帽中必须保留的 forced formal-unit obligations 的有效下界 N。 | BoundaryCapForcedFormalUnitObligationLowerBound |
| `RowFreeTypeUpperOrExplosionDefectCurrentCorpusProved` | `false` | `false` | 尚未证明保标签 row-free type alphabet 上界 T<N，或 T>=N 时自动产生登记相位缺陷。 | BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect |
| `FullKeyRepeatWouldPreserveLabelsButNoCountDeficit` | `true` | `true` | 若完整 canonical key 重复，source_family、phase_key、anchor/carry-shell 和标签字段同时重复，可接 CRT 短复现；但当前没有证明完整 key 的数量小于 forced records。 | BoundaryCapLabelPreservingQuotientEntropyDeficit |
| `CoarseTypeRepeatDoesNotPreserveLabelSupport` | `true` | `true` | 若为了鸽巢而忽略标签字段，重复类型不再保证同一标签集 Q 保持，CRT 的 prod(Q)\|Delta 后半段不能调用。 | BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn AND StableReturnLargeLabelSupportProductLowerBound |
| `AnchorCollarOverloadReturnSchemaImported` | `true` | `true` | 短纤维饱和、端点相位缺陷、孤立 sparse escape 与固定位移复用已有命名回流 schema。 | schema closed; terminal exclusion still open。 |
| `LabelPreservingQuotientEntropyDeficitCurrentCorpusProved` | `false` | `false` | 当前材料没有给出边界帽内保标签商类型数小于 forced records 的定量熵亏损。 | BoundaryCapLabelPreservingQuotientEntropyDeficit |
| `TypeDriftToRegisteredDefectCurrentCorpusProved` | `false` | `false` | 当前材料没有证明所有破坏标签保持的类型漂移都以同一 formal unit 权重进入 PDEC/SAE/ColumnCRT 并被排斥。 | BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn |
| `BoundaryCapFormalUnitTypeCompressionDichotomyCurrentCorpusProved` | `false` | `false` | 类型压缩本身保留原 N/T/复现骨架，同时新增审查结论：哈希保真不能替代保标签商类型熵亏损。 | BoundaryCapForcedFormalUnitObligationLowerBound AND BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect AND RepeatedBoundaryTypeToStableSameLabelReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 尚未得到反例链与真实结构链之间的终端矛盾；DStructure/Rankin 独立验收仍保留。 | BoundaryCapLabelPreservingQuotientEntropyDeficit AND BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn AND StableReturnLargeLabelSupportProductLowerBound AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步最窄硬攻点

```text
BoundaryCapLabelPreservingQuotientEntropyDeficit
```

并行必须保留：

```text
BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn
```

类型压缩若闭合后，仍需接上：

```text
StableReturnLargeLabelSupportProductLowerBound AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```
