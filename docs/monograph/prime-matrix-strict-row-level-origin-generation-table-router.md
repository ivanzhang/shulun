# Prime Matrix strict 逐行原始生成表路由器

**状态：** `row_level_origin_generation_table_reduced_to_acyclic_seed_signed_row_emitter_open`

本步继续攻击逐行 clean-core 原始生成表。结论是：表的真正生成器不是 formal-unit 容器、不是 unsigned carry-shell skeleton，也不是 source table 名称，而是一个无环 pre-Cauchy actual noncanonical source seed 自带的 signed row emitter 规则。该规则必须逐行输出 signed coefficient、sign/local factor、exact `(u,v)`、branch key，并证明推前前求和恒等式。当前材料没有该规则；若无法提交，则只能按已登记纪律回流 acyclic 终端家族。

```text
row_level_origin_generation_table_router_closed=true
acyclic_seed_signed_row_emitter_rule_proved=false
row_level_clean_core_origin_generation_table_proved=false
primitive_summand_signed_coefficient_origin_identity_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands 必须由 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity` 生成。若该 seed/emitter 不能提交，按 seed 融合与 no-go 纪律回流 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily`；不能从 unsigned skeleton 或 payment 图反推。

## 2. signed row emitter 字段

| field | meaning |
| --- | --- |
| `acyclic_source_seed` | Cauchy/dispersion 前声明的 actual noncanonical primitive source seed。 |
| `row_emitter_map` | 从 seed/source tuple 到有限 alpha/delta primitive rows 的确定性发射映射。 |
| `signed_coefficient_law` | 每条 row 的 signed coefficient 公式，含筛权、符号和 branch/local factor。 |
| `prepushforward_sum_identity` | 这些 row 在 Phi/payment 推前前求和等于 actual alpha/delta 系数。 |
| `uv_key_sync` | 每条 row 同步输出 exact `(u,v)` 和 branch key。 |
| `terminal_return_if_missing` | seed 缺失、row 缺失、零权重、符号冲突或超预算时进入命名终端家族。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RowLevelOriginTableTargetActive` | `true` | `false` | 上一层已把 primitive summand 来源恒等式压到逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `TableRequiresAcyclicSeedWithEmitter` | `true` | `true` | 逐行表不是后验枚举；必须由无环 pre-Cauchy seed 自带 signed row emitter 规则产生。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SourceLoopCutImported` | `true` | `true` | origin/formula/emitter/payment 等价环不能自证逐行表。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `ZeroRowCannotSupplySeedOrSignedRows` | `true` | `true` | 早期零行假设只给 unsigned cover/Phi 数据，不能生成 signed seed 或 signed rows。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SeedFusionDoesNotProveTable` | `true` | `true` | 全局终局中 seed 已通过存在/不存在二分并入终端门；这不等于提交了逐行生成表。 | 若继续走 signed-source 表路线，仍需 seed+emitter；若缺失则回流终端家族。 |
| `FormalUnitAndSourceTupleContainersReady` | `true` | `true` | formal unit/source tuple/anchor 参数容器可用。 | 容器不产生 signed coefficient。 |
| `UnsignedSkeletonReadyButInsufficient` | `true` | `false` | unsigned carry-shell/P列锚/layered-wheel skeleton 已能定位候选几何行。 | 缺 signed coefficient law。 |
| `SignedLiftStillPointwiseValueTableOpen` | `true` | `false` | signed lift 已压成逐 skeleton row 的 signed value table，但该表未给出。 | signed row emitter 必须输出这些值。 |
| `PointwiseWeightFormulaStillNeedsOriginRows` | `true` | `false` | 逐行 signed alpha weight 公式仍缺 primitive summand 推前前表达式。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SupportSeedIsNotRowEmitter` | `true` | `false` | actual source-support 路线给出支撑能量形式，但不生成 row emitter。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SourceTableRequiresSameRows` | `true` | `false` | actual emitter source table 也需要同一批 primitive rows，不能反过来自证 row table。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `RowLevelOriginGenerationTableCurrentCorpusProved` | `false` | `false` | 当前材料没有提交 seed 自带的 signed row emitter 和推前前求和恒等式。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |

## 4. 下一真正单点

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
