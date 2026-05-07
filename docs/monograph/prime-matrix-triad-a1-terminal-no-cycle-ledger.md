# Triad-A1 终端无循环账本

**状态：** `a1_middle_escape_closed_terminal_certificates_open`

当前账本关闭的是 A1 路线的中间逃逸和同层循环，不是三终端证书全集。后续必须在 PDEC、CleanKLS/DLS、Sparse/LocalSurvivor 三类中提交实际排斥证书。

## 1. 无循环律

固定 Q 普通 cap 持久时不能同层循环；升层后若删除不足则 HRO/TCP/TUD 强制进入 PDEC/CleanKLS，若删除持续则进入 Sparse/LocalSurvivor 或容量矛盾。

- `all_materialized_gates_pass=True`。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `terminal_no_cycle_ledger_script` | `1c908271e4cf67371e00b8b6551625674a4914f70b1be82e22af47551f57a1fe` |
| `direction_support_json` | `fbdf2704a83255fb771d044287350368d7c75b43a277b0eb8a67e8862351c571` |
| `fourier_cap_scan_json` | `fe47050ce4b60f5c5651228f7e940eb20898506149f830d86448375984b7e502` |
| `newlayer_tower_gate_json` | `c59e17f45bd93129864e54c07eb5c27a5fbb96bdd6fe1fdedcff94a7d5249597` |
| `terminal_router_json` | `eb0c2528f581dd283cd4bdfb7687fd008f4ae0cc53bfa1faa705be8c89d27d6b` |
| `tail_unit_density_json` | `5d178ad63bd0dcf03c25028af32389ae6636de0c6b1ea826b7076a1bb489c4d5` |
| `hro_1` | `69deae251f17fe9bd22a2d38e093325f608fbe4b17de0e6da98efc00ee7f33e9` |
| `hro_2` | `4c42aa7915919e83b3e2ef3e04891b282e1b9d78f80a0d80caa429888d4bba04` |
| `tcp_1` | `17e00964a8d3bfd4b75a3c9d9ba943600eb24419a9881e5a105d87c6a24797af` |
| `tcp_2` | `d08e44f727ca7b006fddcc672f1cd3066405f66e5987ce360f09642490767428` |

## 3. 门控总表

| gate | status | route |
| --- | --- | --- |
| `FixedQZeroBlockDirection` | `Closed` | 零容量块方向在 LHB 分支为空。 |
| `FixedQDensityBarrier` | `PersistentCapForcesLiftOrExtraRows` | 固定 Q 普通 Fourier cap 出现持久交集；不能在同一固定层循环，必须升层、加 column/tail 行或进 CleanKLS。 |
| `NewLayerTower` | `CurrentLayersDeleting` | 已物化升层均重新稀疏，继续累计删除势。 |
| `HoleResidueOccupancy` | `CertifiedDeletionOrNamedEscape` | 若 Occ+TI 不满则删除；若趋满只能进入 OccupancySaturation 或 TailIndependence。 |
| `TailCapacityPressure` | `CapacityDeathOrKL` | 残余洞容量/Hall 失败则死亡；容量成功则支付 Tail KL 或进入 CleanKLS。 |
| `TailUnitDensity` | `NonemptyResidualPaysKLOrCleanKLS` | 非空残余洞幸存且 u_tail 不小则支付 KL；KL 小只能进入空残余洞或 CleanKLS。 |
| `TerminalRouter` | `current_layers_all_deleting` | 当前物化层仍在删除势；删除停止时强制进入 PDEC/CleanKLS，删除发散时进入 Sparse/LocalSurvivor。 |

## 4. 关键数值

### NewLayerTower

| layer | r | class | min drop | max survival |
| --- | ---: | --- | ---: | ---: |
| Q=2310->30030 | 13 | `FiberDeletionLayer` | 3.19672 | 0.312821 |
| Q=30030->510510 | 17 | `FiberDeletionLayer` | 6.13889 | 0.162896 |

### HoleResidueOccupancy

- `max_union_bound_rate=0.34359`。
- `min_certified_deletion_lb_rate=0.65641`。

### TailCapacityPressure

- `all_consistent_with_lift_m_vector=True`。
- `all_dead_slots_hall_certified=True`。

### TailUnitDensity

- `all_unit_density_bounds_pass=True`。

## 5. 剩余终端义务

- PDEC family U_CRT<L_PDEC。
- CleanKLS/DLS admission and large-sieve certificate。
- Sparse/LocalSurvivor witness or blocker deficit。

## 6. 结论

A1 现在不能再停在固定 Q cap、升层口径、旧洞占用、Tail 容量或 Tail KL 的中间解释上。
这些门控要么已在当前层给出删除势，要么强制进入 PDEC/CleanKLS/SparseLocal 三终端。
