# Triad-A1 ForcedCap 终端路由器

**状态：** `current_forced_caps_routed_to_lift_or_terminal_triad`

当前 24 个 ForcedPersistentByDensityBarrier cap 已关闭 P×P 早期出口，并从固定 Q 同层循环中退出。一层 lift 后仍为持久支撑，所以它们没有被本层删除势完全吸收；其 column-tail 暴露签名已物化，且单 residue 与单 column-residue 实际支付已被暴露支配排除；剩余义务是 multi-bucket PDEC、next-lift 删除/KL 门控或 CleanKLS。

## 1. 路由链

```text
DensityBarrier => fixed-Q ordinary cap cannot close by same layer
AttachedMass => g(t)<=M_Q(t)
BTLS => no P-row boundary exit
Lift Q=2310 to Q'=30030
LiftPersistentNeedsColumnTailOrNextLift => no same-Q cycle
ColumnTailExposure => fixed-signature PDEC candidate or distributed CleanKLS
ExposureDominance => no single residue or single column-residue payment
Next route => multi-bucket PDEC / next lift deletion-KL / CleanKLS
```

## 2. 计数一致性

- `mass_source_forced_count=24`。
- `forced_lift_cap_count=24`。
- `forced_exposure_cap_count=24`。
- `forced_dominance_cap_count=24`。
- `all_counts_match=True`。

## 3. 门控结果

- `mass_source_verified=True`。
- `pxp_exit_closed_by_btls=True`。
- `boundary_terminals_excluded=True`。
- `boundary_phase_le_p_has_local_survivor=True`。
- `old_intersections_recomputed=True`。
- `all_forced_lifts_persistent=True`。
- `columntail_exposure_materialized=True`。
- `single_residue_actual_payment_excluded=True`。
- `single_column_residue_actual_payment_excluded=True`。
- `all_current_forced_caps_routed=True`。

## 4. 当前层指标

- `lift_class_counts={'LiftPersistentNeedsColumnTailOrNextLift': 24}`。
- `q_source=2310`。
- `target_q=30030`。
- `support_profile_count=2`。
- `total_phase_le_p_count=113`。
- `total_y0_completion_le_p_count=0`。
- `exposure_route_counts={'ForcedColumnTailExposurePDECOrDistributedCleanKLS': 24}`。
- `dominance_route_counts={'MultiBucketPDECOrDistributedCleanKLS': 24}`。
- `global_min_actual_residue_buckets_by_exposure=11`。
- `global_min_actual_column_residue_buckets_by_exposure=9`。
- `p_level_effective_exposure_support=[{'cap_count': 12, 'max_column_residue_exposure_share': 0.10136636329320674, 'max_residue_exposure_share': 0.09148341880953399, 'min_effective_column_residue_exposure_support': 9.86520545387877, 'min_effective_prime_exposure_support': 1.0, 'min_effective_residue_exposure_support': 10.930942601543707, 'p': 43}, {'cap_count': 12, 'max_column_residue_exposure_share': 0.11815744804881946, 'max_residue_exposure_share': 0.09595282805196387, 'min_effective_column_residue_exposure_support': 8.463283665256776, 'min_effective_prime_exposure_support': 1.0, 'min_effective_residue_exposure_support': 10.421787666940297, 'p': 47}]`。

## 5. 剩余义务

- 把多桶实际支付签名升级为持久 formal unit，或证明实际支付分散。
- 对持久多桶实际支付签名提交 TailAnchor / ColumnCRT / refined PDEC 行。
- 执行下一层 lift，并按 FiberDeletion / NoDeletion-KL / CleanKLS 路由。
- 若 lift 后出现稀疏子帽，接入 LocalSurvivor / LFTE。
- 若 lift 后仍持久且平坦，提交 CleanKLS/DLS admission。

## 6. 读法

这一步没有排除 ForcedCap。它关闭的是两个中间逃逸：

```text
P×P 早期出口  => BTLS 关闭；
固定 Q 同层循环 => DensityBarrier 强制 lift。
```

和 PersistentCap 不同，当前 forced cap 的一层 lift 仍为持久支撑。
所以它们的下一硬点不是当前层删除势，而是：

```text
column-tail PDEC；
multi-bucket actual-payment PDEC；
next-lift 删除/KL；
或 CleanKLS/DLS。
```
