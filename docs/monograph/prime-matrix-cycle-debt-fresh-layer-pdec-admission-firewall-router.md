# Prime Matrix cycle-debt fresh-layer PDEC admission firewall router

**状态：** `current_materialized_fresh_layer_pdec_frontier_closed_future_schema_or_unregistered_moving_open`

当前 cycle-debt fresh-layer PDEC/ColumnCRT 没有可保留的无名材料化实例：registered 本地投影单射排除本地材料化，广义 PDEC 边界记录当前合法 primitive 候选为零，ColumnCRT 必须先被吸收到 PDEC/SAE，new-layer schema 与二秩预算独立门也已给出准入/回流纪律。因此剩余只能是未来新增的显式 primitive fresh-layer PDEC schema，或阻断包变化形成的未登记 moving family。

```text
previous_hardpoint=MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter
registered_block_count=6
minimum_first_fresh_minus_max_window=178
minimum_remote_plus_first_fresh_log10=38.803
local_registered_materialized_pdec_closed=true
current_materialized_pdec_frontier_closed=true
pdec_family_explicit_input_boundary_closed=true
newlayer_schema_admission_closed=true
newlayer_ranktwo_budget_independent_gate_removed=true
current_corpus_materialized_fresh_layer_pdec_closed=true
future_explicit_primitive_fresh_layer_pdec_schema_submitted=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter
```

## 1. 防火墙逻辑

材料化 fresh-layer PDEC/ColumnCRT 不能作为无名口径保留。registered support 内，fresh prime 投影在窗口中单射，不能形成本地相位复用；跨窗口或远程材料化若要成为 PDEC，必须通过已经登记的 PDEC family 准入边界。

该准入边界要求同一 formal unit、固定相位映射、三物理原子以上、非二点 tautology、二秩以上且 cap-stable。若任一条件失败，事件回流 ColumnCRT/SAE/refined PDEC/sparse extractor/multiplicity，而不是成为新的终端。

## 2. registered block 审计

| block | support | audit | first fresh | fresh-window margin | local PDEC forbidden | remote+fresh log10 |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| `both_branches_plus_k14_entry_postwall` | 151 | 190 | 88609 | 88419 | `true` | 108.051 |
| `k13_branch_exclusive` | 73 | 73 | 251 | 178 | `true` | 42.832 |
| `k14_branch_exclusive` | 70 | 70 | 293 | 223 | `true` | 38.803 |
| `k14_branch_plus_entry` | 78 | 78 | 88609 | 88531 | `true` | 80.766 |
| `k14_branch_plus_entry_plus_assigned` | 78 | 107 | 88609 | 88502 | `true` | 85.053 |
| `k14_branch_plus_entry_plus_postwall` | 78 | 117 | 88609 | 88492 | `true` | 93.726 |

## 3. 未来 schema 字段

- 同一个 formal_unit_id 与一个固定 phase map
- 全部去重后至少三个物理 primitive atoms
- 不是二点 Fourier tautology 或单列 displacement
- 商去 shell/column 退化后相位秩至少为 2
- 对每个有限循环弧 localization 均 cap-stable
- 若 cap 失败，必须回流 SAE/refined PDEC/ColumnCRT/multiplicity
- 若转成 sparse/local survivor，必须提交有限 packet extractor schema
- 给出全集账本、哈希、open_obligation_count=0

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MaterializedFreshLayerBranchImported | `true` | `true` | 上一证书把裸 remote ColumnCRT 删除后，只留下材料化 fresh-layer PDEC/ColumnCRT 或未登记 moving family。 | MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter |
| RegisteredLocalFreshMaterializationForbidden | `true` | `true` | registered support 内 fresh prime 均大于窗口，且仿射投影单射；本地相位复用不能材料化为 PDEC。 | closed for registered blocks |
| CurrentMaterializedPDECFrontierClosed | `true` | `true` | 广义 PDEC 边界证书记录当前已物化合法非二点 primitive PDEC 候选为零。 | future explicit primitive schema only |
| ColumnCRTAbsorbedBeforeAdmission | `true` | `true` | PDEC family 边界规定 ColumnCRT/位移不能直接准入；必须先转成 displacement/refined PDEC 或 SAE。 | closed as unnamed ColumnCRT terminal |
| NewLayerSchemaAdmissionClosed | `true` | `true` | 若 fresh-layer PDEC 真正作为 new-layer 候选出现，其 formal-unit schema 准入层已闭合。 | rank-two cap-stable or named return |
| NewLayerRankTwoIndependentGateRemoved | `true` | `true` | new-layer 二秩预算失败不再是独立输入；它会材料化为有限弧 cap 并回流命名出口或 flat gate。 | NewLayerNoConcentrationImpliesFlatAdmission if a future schema reaches it |
| SparseFallbackSchemaBoundaryClosed | `true` | `true` | 若所谓材料化只是 sparse packet 或局部幸存者失败，则未来 sparse schema 边界已要求完整 extractor。 | future sparse schema if new |
| CurrentCorpusMaterializedFreshPDECClosed | `true` | `true` | 当前 cycle-debt 语料中没有可准入的材料化 fresh-layer PDEC/ColumnCRT；无名材料化口径被删除。 | FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter |
| FutureExplicitPrimitiveFreshLayerPDECSchemaIfNew | `false` | `false` | 未来若真新增 fresh-layer PDEC family，必须提交同 formal unit、三物理原子以上、二秩 cap-stable 的全集 schema。 | FutureExplicitPrimitiveFreshLayerPDECSchema |
| UnregisteredMovingFamilyStillOpen | `false` | `false` | 阻断包、shape、source family 或 phase map 变化仍需单独 moving-family 路由。 | UnregisteredMovingFamilyRouter |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只关闭当前语料中的无名材料化 PDEC 口径；没有证明未来 schema 不存在，也没有排斥 moving family。 | FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter |

## 5. 剩余接口

```text
FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter
```

本证书不证明未来 primitive fresh-layer PDEC schema 不存在，也不排斥未登记 moving family；它只关闭当前语料中的无名材料化 PDEC/ColumnCRT 口径。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json` | `bb3b1891e79742dbf1b00792545f5cce080d64ffbfa6520f131a0711d49083ce` |
| `data/prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json` | `07582cef6e5a7620516ace08f9477edcc3fa0ac2549c74078a965dd510e84870` |
| `docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.json` | `33273fb11ffbd8b1e4e5970d8f65f222da7c045263517e2b12f0145dff7d1bfa` |
| `docs/monograph/prime-matrix-newlayer-pdec-schema-admission-router.json` | `448ce2b5e20fa5fa6d14a1a7e4c0272d64718721b7755d1d7390f377cee04f94` |
| `docs/monograph/prime-matrix-newlayer-ranktwo-budget-ledger-router.json` | `73b82f49af3060e74bd08d8c15030b02197c1a14a63b9ddf62a81334097684a8` |
| `docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json` | `1ea554698813752d96b91df8e1f5055b68b619aaeae536ec1a6ccc1861ed3ba3` |
