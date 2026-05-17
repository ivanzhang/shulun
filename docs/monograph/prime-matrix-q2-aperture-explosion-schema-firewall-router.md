# Q2 aperture-explosion schema-firewall 同步路由

**状态：** `q2_aperture_explosion_current_schema_firewall_not_global_proof`

Q2 fresh-layer tail-mass 之后，受控孔径已进入 SAE；剩余的孔径爆炸若要成为真实反例链，必须材料化为支撑运动、阻断包变化或 fresh-layer PDEC 的显式 schema。当前 registered support-motion、材料化 fresh-layer PDEC 与 branch-replay 物化前沿均已有防火墙同步；因此当前无名 aperture-explosion 终端不可保留。未来若提交显式 schema，需要按防火墙重开。

```text
previous_hardpoint=ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;GlobalFinalInputsStillOpen
controlled_fresh_tail_imported=true
registered_support_motion_imported_closed=true
current_materialized_fresh_pdec_imported_closed=true
current_branch_replay_frontier_zero_imported=true
future_explicit_aperture_explosion_schema_submitted=false
unnamed_aperture_explosion_terminal_allowed=false
row_column_unconditional_closed=false
next_direct_attack_target=Q2ApertureExplosionCurrentSchemaFirewall;GlobalFinalInputsStillOpen
```

## 1. 同步逻辑

受控孔径 fresh-tail 已被压入 `SAE`。剩余若声称孔径增长能追赶 fresh modulus，
它就必须说明哪个支撑、阻断包、相位映射或 fresh-layer PDEC 在持久复现。
这类对象不能无名保留：registered support-motion、当前材料化 fresh-layer PDEC 与 current frontier zero
已经给出准入防火墙。

## 2. 样本路由

| P | x0 | Q2 | initial width | controlled route | explosion route |
| ---: | ---: | ---: | ---: | --- | --- |
| 13 | 168 | 2203 | 25 | `SAE` | `explicit moving-family/PDEC schema firewall` |
| 17 | 1210 | 20593 | 31 | `SAE` | `explicit moving-family/PDEC schema firewall` |
| 19 | 3658 | 69539 | 41 | `SAE` | `explicit moving-family/PDEC schema firewall` |
| 23 | 58 | 1361 | 35 | `SAE` | `explicit moving-family/PDEC schema firewall` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ControlledFreshTailImported | `true` | `true` | 上一证书已把受控孔径、无 PDEC 的 fresh-tail 压入 SAE。 | aperture explosion or PDEC only |
| ApertureExplosionMeansSchemaChange | `true` | `true` | 若 log W_j 反复追赶 log M_j，则局部端点替换模型失效；必须给出支撑运动、阻断包变化或 fresh-layer PDEC schema。 | explicit schema firewall |
| RegisteredSupportMotionImportedClosed | `true` | `true` | 已有 registered support-motion 全局路由排除了本地支撑漂移；持久 registered replay 只能提升为远程 ColumnCRT/PDEC。 | RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter |
| CurrentMaterializedFreshPDECImportedClosed | `true` | `true` | 已有 fresh-layer PDEC admission firewall 关闭当前语料中的无名材料化 PDEC/ColumnCRT。 | FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter |
| CurrentBranchReplayFrontierZeroImported | `true` | `true` | 已有 current-frontier-zero 证书说明当前 branch-replay 语料内没有活动终端实例。 | CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;GlobalFinalInputsStillOpen |
| FutureExplicitSchemaReopenOnly | `true` | `true` | 未来若出现 Q2 aperture-explosion/moving-family/PDEC 候选，必须提交 source、shape、phase、persistence 与哈希账本；不能作为无名终端保留。 | future explicit schema if new |
| GlobalRowColumnUnconditionalClosureReached | `false` | `false` | 本步只同步当前语料的 schema 防火墙；没有证明未来 schema 不存在，也没有关闭全局最终输入。 | Q2ApertureExplosionCurrentSchemaFirewall;GlobalFinalInputsStillOpen |

## 4. 最新剩余

```text
Q2ApertureExplosionCurrentSchemaFirewall;GlobalFinalInputsStillOpen
```

本证书只是当前语料的 schema 防火墙同步；它不证明未来显式 aperture-explosion/moving-family schema 不存在，
也不构成行/列命题的全局无条件证明。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json` | `314cf3aae30e4a5565e4c9e157703622c7fb9fdb630bb09c43ca723879832b43` |
| `docs/monograph/prime-matrix-cycle-debt-fresh-support-motion-global-router.json` | `eab025e80b600786d209394402a8e64114b4b8f8a847a53eb07f0da5747c7662` |
| `docs/monograph/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.json` | `4a7ab680dc2d9419b4973c5401d7627e0febef0686510b1e116d7d878692f695` |
| `docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json` | `fb6ba535d8c13abd69c7238539049a64161b6e1e19595fc403a0394b7a56029a` |
