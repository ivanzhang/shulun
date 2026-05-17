# Prime Matrix cycle-debt branch-replay current frontier zero router

**状态：** `cycle_debt_branch_replay_current_materialized_frontier_zero_future_schema_firewall_global_inputs_open`

cycle-debt branch-replay 的当前物化前沿已清零：fresh-layer PDEC/ColumnCRT 当前实例已关闭，FutureExplicitPrimitiveFreshLayerPDECSchema 与 unregistered moving family 均未提交具体 schema，只能作为未来准入纪律保留。该结论不证明未来 schema 永不存在，也不关闭行/列全局无条件定理；全局仍需处理最终输入防火墙后的 noncanonical 与 DStructure/Rankin 门。

```text
previous_hardpoint=FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter
current_fresh_layer_pdec_frontier_closed=true
future_explicit_primitive_fresh_layer_pdec_schema_submitted=false
unregistered_moving_family_schema_submitted=false
future_pdec_schema_admission_discipline_closed=true
future_sparse_schema_admission_discipline_closed=true
final_input_firewall_boundary_closed=true
no_hidden_terminal_remaining=true
cycle_debt_branch_replay_current_materialized_frontier_zero=true
future_explicit_schema_global_nonexistence_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;GlobalFinalInputsStillOpen
```

## 1. 当前实例与未来准入

`FutureExplicitPrimitiveFreshLayerPDECSchemaIfNew` 不是当前已出现的反例对象；它是未来新增 PDEC family 的准入纪律。同理，未登记 moving family 若没有提交 source、shape、phase 与 persistence schema，也不能作为当前终端保留。

因此在当前 cycle-debt branch-replay 语料内，活动终端实例已经清零；未来若新增对象，只能按显式 schema 重开审查。

## 2. moving-family 未来 schema 字段

- source_family_id 与 formal_unit_id
- blocker_package、shape_key、phase_map 与去重规则
- 支撑窗口、candidate set 与 exact bad-window count function
- 同签名持久性测试；若持久则回流 PDEC/ColumnCRT
- 签名漂移测试；若漂移则回流 SAE/CleanKLS/DLS 或 noncanonical final input
- 可复现实验或证明账本、哈希与 open_obligation_count=0

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FreshLayerPDECCurrentCorpusClosed | `true` | `true` | 上一证书已关闭当前 cycle-debt 语料中的无名材料化 fresh-layer PDEC/ColumnCRT。 | closed |
| FutureFreshPDECSchemaNotSubmitted | `true` | `true` | 未来 fresh-layer PDEC schema 尚未提交；它是准入纪律，不是当前已出现的数学障碍。 | future schema firewall |
| UnregisteredMovingFamilySchemaNotSubmitted | `true` | `true` | 未登记 moving family 没有提交完整 source/shape/phase/persistence schema；不能作为当前终端保留。 | future moving-family schema firewall |
| FuturePDECSchemaAdmissionDisciplineClosed | `true` | `true` | 未来 PDEC family 若新增，必须通过显式 primitive same-formal-unit schema 边界。 | reopen only with explicit schema |
| FutureSparseMovingPacketDisciplineClosed | `true` | `true` | 未来 sparse/local-survivor 型 moving packet 若新增，必须提交有限 packet extractor schema。 | reopen only with explicit extractor |
| NoHiddenTerminalBoundaryImported | `true` | `true` | 最终输入防火墙已说明当前语料无隐藏终端；未来输入只能按命名 schema 重开。 | global final inputs remain |
| CycleDebtBranchReplayCurrentFrontierZero | `true` | `true` | 在当前已物化 cycle-debt branch-replay 语料内，PDEC/ColumnCRT/future-schema/moving-family 均无活动终端实例。 | closed for current materialized branch-replay corpus |
| FutureSchemaMayReopen | `false` | `false` | 本步不证明未来 primitive fresh-layer PDEC schema 或 moving-family schema 永不存在。 | FutureExplicitPrimitivePDECSchema or FutureExplicitMovingFamilySchema if submitted |
| GlobalFinalInputsStillOpen | `false` | `false` | 行/列命题仍受全局最终输入约束，尤其 noncanonical 合法闭合模式与 DStructure/Rankin 晋级门。 | NoncanonicalFullSComplementLegalClosureMode and DStructureRankinPromotion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只清零当前 cycle-debt branch-replay 物化前沿，不关闭完整行/列无条件定理。 | CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;GlobalFinalInputsStillOpen |

## 4. 剩余接口

```text
CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;GlobalFinalInputsStillOpen
```

本证书不关闭全局行/列命题；它只说明 cycle-debt branch-replay 的当前物化前沿不再含活动终端实例。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json` | `4a7ab680dc2d9419b4973c5401d7627e0febef0686510b1e116d7d878692f695` |
| `docs/monograph/prime-matrix-final-input-firewall-boundary-router.json` | `b8db63a47643fdf9b98e860c8e81eec6de92377e87118b274f9ccf63f0008b7b` |
| `docs/monograph/prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json` | `3323fe284f3293bb2a9fb18f739c41ffb64a5bebb44b847ae97d2d6074568f3f` |
| `docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.json` | `33273fb11ffbd8b1e4e5970d8f65f222da7c045263517e2b12f0145dff7d1bfa` |
| `docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json` | `1ea554698813752d96b91df8e1f5055b68b619aaeae536ec1a6ccc1861ed3ba3` |
