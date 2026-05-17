# Prime Matrix cycle-debt fresh support-motion 全局路由器

**状态：** `registered_support_motion_escape_closed_remote_columncrt_or_unregistered_moving_open`

registered branch-replay 的 support-motion escape 已被同步关闭：本地 fresh-layer 投影碰撞已排除，同一阻断包本地非零支撑漂移又被 support-gap lcm 屏障排除；若 registered block 仍在全局无限复现，只能提升为远程 P-space ColumnCRT 类。剩余为 RemotePspaceColumnCRT 排斥或未登记 moving family 路由。

```text
previous_hardpoint=FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion
period_p=5680
registered_block_count=6
local_fresh_layer_projection_collision_excluded=true
registered_local_support_motion_excluded=true
persistent_registered_replay_routes_to_columncrt_pdec=true
isolated_registered_atoms_cannot_form_global_escape=true
registered_support_motion_escape_closed=true
minimum_cycle_log10_margin_over_support_width=30.737
minimum_p_space_columncrt_modulus_log10=36.337
remote_pspace_columncrt_excluded=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

## 1. 同步引理

registered fresh-layer 剩余包含三种表面形态：本地投影碰撞、本地支撑漂移、远程复现。本地投影碰撞已由 fresh-layer 单射引理排除；本地支撑漂移已由同一阻断包的 `lcm(B)` 复现屏障排除。因此若 registered block 仍在全局反例链中无限复现，它不再是本地支撑运动，而必须是固定 P-space ColumnCRT 类。

若阻断包改变，则它不属于 registered support-motion escape，而是未登记 moving family，需要新的 PDEC/SAE/ColumnCRT 路由。

## 2. block 读数

| block | support | audit | log10 cycle replay | log10 P-space CRT | local motion closed |
| --- | ---: | ---: | ---: | ---: | --- |
| `k13_branch_exclusive` | 73 | 73 | 36.678 | 40.432 | `true` |
| `k14_branch_exclusive` | 70 | 70 | 32.582 | 36.337 | `true` |
| `k14_branch_plus_entry` | 78 | 78 | 72.064 | 75.819 | `true` |
| `k14_branch_plus_entry_plus_assigned` | 78 | 107 | 76.351 | 80.105 | `true` |
| `k14_branch_plus_entry_plus_postwall` | 78 | 117 | 85.024 | 88.778 | `true` |
| `both_branches_plus_k14_entry_postwall` | 151 | 190 | 99.349 | 103.103 | `true` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FreshLocalCollisionAlreadyExcluded | `true` | `true` | 上一证书已排除 registered fresh layer 在本地 primitive support 内的投影碰撞。 | closed |
| RegisteredLocalSupportMotionExcluded | `true` | `true` | support-gap replay lemma 已证明同一阻断包本地非零复现周期至少为 lcm(B)，且远超支撑宽度。 | closed for registered blocks |
| PersistentRegisteredRemoteReplayRoutesToPspaceColumnCRT | `true` | `true` | 全局二分已证明若某个 registered block 无限复现，则提升为固定 P-space ColumnCRT 类。 | RemotePspaceColumnCRTExclusion |
| IsolatedRegisteredAtomsNotGlobalEscape | `true` | `true` | 若没有 registered block 无限复现，则登记原子只是有限项，不能构成全局结构逃逸。 | closed as global escape |
| NewBlockerPackageRoutesToMovingFamily | `true` | `false` | 若阻断包改变，则不再是 registered support motion，而是未登记 moving family，须另建 PDEC/SAE/ColumnCRT 路由。 | UnregisteredMovingFamilyRouter |
| RegisteredSupportMotionEscapeClosed | `true` | `true` | 本地碰撞和本地支撑漂移均已排除；registered 无限复现只能是远程 P-space ColumnCRT。 | closed except remote ColumnCRT |
| RemoteColumnCRTOrUnregisteredMovingFamilyStillOpen | `false` | `false` | 剩余不是本地支撑运动，而是远程 P-space ColumnCRT 排斥或未登记 moving family 的新路由。 | RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只关闭 registered support-motion escape，不排斥远程 ColumnCRT 或未登记 moving-family。 | RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter |

## 4. 剩余接口

```text
RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

本证书不排斥远程 P-space ColumnCRT，也不排斥未登记 moving family；它只删除 registered support-motion escape 这个本地出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json` | `07582cef6e5a7620516ace08f9477edcc3fa0ac2549c74078a965dd510e84870` |
| `data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json` | `5c2b502fbc787652b7d07f25d4886746cb64500f280b0128d131869f6b769105` |
| `data/prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json` | `b25a9e5083355f5495156d61b9cf924af55843966d0efe0b7492075cdd811bc4` |
