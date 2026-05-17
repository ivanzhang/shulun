# Prime Matrix cycle-debt remote ColumnCRT feedback router

**状态：** `bare_remote_pspace_columncrt_terminal_closed_materialized_fresh_layer_pdec_or_unregistered_moving_open`

remote P-space ColumnCRT 不能再作为裸固定周期终端保留：孤立有限原子已由 exact runner 吸收，固定有限 CRT 类已由 fresh-modulus escalation 证明为非终端，且 non-PDEC 无界 fresh layers 已由 tail-sieve strict 同步关闭。因此剩余必须是某个新素数层已经材料化的 PDEC/ColumnCRT，或阻断包改变后的未登记 moving family。

```text
previous_hardpoint=RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter
registered_remote_block_count=6
minimum_remote_pspace_columncrt_modulus_log10=36.337
maximum_remote_pspace_columncrt_modulus_log10=103.103
minimum_first_fresh_log10_gain=2.400
minimum_sample_fresh_log10_gain=19.435
registered_finite_atoms_absorbed=true
fixed_finite_remote_crt_not_terminal=true
non_pdec_fresh_tail_sieve_closed=true
bare_remote_pspace_columncrt_terminal_closed=true
materialized_fresh_layer_pdec_columncrt_excluded=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

## 1. 反馈闭合逻辑

上一接口中的 `RemotePspaceColumnCRT` 有两种含义必须分开：

- 如果它只是裸固定远程周期类，则它已经落回旧 `BranchReplayColumnCRTPDECExclusion` 链；有限原子、固定有限 CRT 终端和 non-PDEC tail-sieve 出口均已被已有证书吸收。
- 如果它在某个新素数层真实产生相位复用、投影碰撞或载荷集中，则它不再是裸远程周期类，而是材料化的 fresh-layer PDEC/ColumnCRT。

因此当前接口不应继续写成宽泛的 remote ColumnCRT，而应改写为材料化 fresh-layer PDEC/ColumnCRT 或未登记 moving family。

## 2. remote blocks

| block | support | audit | log10 P-space CRT | +first fresh | +sample fresh |
| --- | ---: | ---: | ---: | ---: | ---: |
| `k13_branch_exclusive` | 73 | 73 | 40.432 | 42.832 | 59.867 |
| `k14_branch_exclusive` | 70 | 70 | 36.337 | 38.803 | 56.368 |
| `k14_branch_plus_entry` | 78 | 78 | 75.819 | 80.766 | 115.400 |
| `k14_branch_plus_entry_plus_assigned` | 78 | 107 | 80.105 | 85.053 | 119.687 |
| `k14_branch_plus_entry_plus_postwall` | 78 | 117 | 88.778 | 93.726 | 128.360 |
| `both_branches_plus_k14_entry_postwall` | 151 | 190 | 103.103 | 108.051 | 142.685 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RemotePspaceColumnCRTImported | `true` | `true` | 上一证书已证明 registered block 若无限复现，只能提升为远程 P-space ColumnCRT/PDEC 类。 | remote registered P-space ColumnCRT |
| RegisteredFiniteAtomsAlreadyAbsorbed | `true` | `true` | post-100000 exact runner 已关闭当前登记有限原子分支；孤立远程原子不能作为全局逃逸。 | closed for registered finite atoms |
| FixedFiniteRemoteCRTNotTerminal | `true` | `true` | fresh-modulus escalation 证书已证明固定有限 CRT replay 类不是无限反例链的终端稳定结构。 | unbounded fresh modulus or PDEC |
| NonPDECFreshTailSieveClosed | `true` | `true` | 若无 fresh-layer PDEC/ColumnCRT，则无界 fresh layers 已接入 B3 tail-sieve 对象并由 strict 同步关闭。 | closed unless fresh-layer PDEC materializes |
| LocalSupportMotionAlreadyClosed | `true` | `true` | 本地投影碰撞和本地 support-motion 逃逸均已关闭；剩余不再是本地漂移。 | closed |
| BareRemotePspaceColumnCRTTerminalClosed | `true` | `true` | 远程 P-space ColumnCRT 若只是裸固定周期类，则被有限原子、固定有限 CRT 非终端和 non-PDEC tail-sieve 闭合链吸收。 | materialized fresh-layer PDEC/ColumnCRT or unregistered moving family |
| MaterializedFreshLayerPDECColumnCRTStillOpen | `false` | `false` | 若远程类在某个新素数层实际产生相位复用/碰撞/PDEC 载荷，本证书尚未排斥该材料化 PDEC/ColumnCRT。 | MaterializedFreshLayerPDECColumnCRTExclusion |
| UnregisteredMovingFamilyStillOpen | `false` | `false` | 若阻断包、shape 或来源签名改变，则它不是 registered remote ColumnCRT，而是未登记 moving family。 | UnregisteredMovingFamilyRouter |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步关闭裸远程周期终端解释，但不排斥材料化 fresh-layer PDEC 或未登记 moving family。 | MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter |

## 4. 剩余接口

```text
MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

本证书不排斥材料化 fresh-layer PDEC/ColumnCRT，也不排斥未登记 moving family；它只把裸 remote P-space ColumnCRT 终端解释从剩余接口中删除。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json` | `eab025e80b600786d209394402a8e64114b4b8f8a847a53eb07f0da5747c7662` |
| `data/prime-matrix-cycle-debt-post100000-tail-atom-exact-ledger.json` | `97b0a494818031721eb7076903f70ede95727b387828197def9d14efeb9a50e9` |
| `data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json` | `bfc13d727a480ee6bb358d5f01a826b5e14b0a2bdef7dd8961c4f58c5ba116d9` |
| `data/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json` | `99d31e9d86f0802049d5640413f3913f393f76bf62dcccab82f844ce2ff91cb4` |
