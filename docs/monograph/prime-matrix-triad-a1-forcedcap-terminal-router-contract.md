# Triad-A1 ForcedCap 终端路由合同

**状态：** `forcedcap_terminal_router_contract_reduces_to_lift_or_terminal_triad`

本文处理 `ForcedPersistentByDensityBarrier`。这类 cap 的本质不是“强证书”，而是固定 `Q` 层的密度屏障：
当 `supp(M_Q)` 太稠时，普通正密度 Fourier cap 必然持久，不能再指望同一固定层闭合。正确动作是升层、
加 column-tail 行，或进入 CleanKLS。

## 1. 路由链

```text
ForcedPersistentByDensityBarrier
=> AttachedMass: g(t)<=M_Q(t)
=> BTLS: P×P 边界出口关闭
=> DensityBarrier: fixed-Q same-cap closure impossible
=> lift Q to Q'=rQ
=> ColumnTailExposure: tail 支付暴露物化
=> ExposureDominance: 单 residue / 单 column-residue 实际支付排除
=> multi-bucket PDEC / next persistent / NoDeletion-KL / CleanKLS
```

这条链关闭的是固定 `Q` 同层循环。它不声称 forced cap 已排除。

## 2. 当前机器路由

对应审计：

```text
experiments/prime_matrix_triad_a1_forcedcap_terminal_router.py
docs/monograph/prime-matrix-triad-a1-forcedcap-terminal-router.md/json
```

当前读数：

```text
mass_source_forced_count=24；
forced_lift_cap_count=24；
forced_exposure_cap_count=24；
forced_dominance_cap_count=24；
all_counts_match=True；
all_current_forced_caps_routed=True。
```

门控全真：

```text
mass_source_verified=True；
pxp_exit_closed_by_btls=True；
boundary_terminals_excluded=True；
boundary_phase_le_p_has_local_survivor=True；
old_intersections_recomputed=True；
all_forced_lifts_persistent=True；
columntail_exposure_materialized=True；
single_residue_actual_payment_excluded=True；
single_column_residue_actual_payment_excluded=True。
```

## 3. 结构意义

当前 `24` 个 forced cap 满足：

```text
1. 有同一 M_Q 质量来源；
2. 前 P 行出口由 BTLS 关闭；
3. 旧层交集已重算一致；
4. lift 到 Q'=30030 后仍为持久支撑；
5. column-tail 暴露签名已物化；
6. 单 residue 与单 column-residue 实际支付已由暴露支配排除。
```

所以它们已经不是早期零行风险，也不能继续在固定 `Q=2310` 同层循环。剩余义务是：

```text
多桶实际支付签名升级为持久 formal unit，或证明实际支付分散；
multi-bucket TailAnchor / ColumnCRT / refined PDEC；
next-lift 删除势或 NoDeletion-KL；
CleanKLS/DLS。
```

## 4. 闭合边界

本文完成：

```text
当前 forced cap 的早期出口关闭；
固定 Q 密度屏障同层循环关闭；
forced cap 的 column-tail 暴露输入物化；
forced cap 的单桶实际支付排除；
forced cap 的下一步路由归一化。
```

本文未完成：

```text
forced cap 的 multi-bucket actual-payment PDEC 排斥；
后继 lift 删除势发散；
NoDeletion-KL / CleanKLS 证书全集。
```

因此它推进的是 forced 分支的无循环归约，不是最终无条件证明。
