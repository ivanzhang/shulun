# Triad-A1 PersistentCap 终端路由合同

**状态：** `persistentcap_terminal_router_contract_reduces_to_deletion_or_terminal_triad`

本文把 `PersistentCap` 从一个 PDEC 中间标签压成确定的递归路由。核心结论不是“PersistentCap 已全部排除”，而是：
当前 PersistentCap 不能再作为早期零行出口、固定 `Q` 同层循环或 top-prime 独立终端。它只能进入删除势塔、
`NoDeletion-KL/CleanKLS`，或固定 residue/column 的 PDEC。

## 1. 路由链

```text
PersistentCap
=> AttachedMass: g(t)<=M_Q(t)
=> BTLS: P×P 边界出口关闭
=> ColumnTail payment equation
=> fixed residue/column signature PDEC
   or top-prime persists
   or distributed CleanKLS
=> top-prime=next high prime 时 promote Q to rQ
=> PromotionFiberDeletion / NoDeletion-KL / CleanKLS / PDEC
```

这条链的作用是消掉中间逃逸：每一步要么下降为删除势，要么进入三终端证书。

## 2. 当前机器路由

对应审计：

```text
experiments/prime_matrix_triad_a1_persistentcap_terminal_router.py
docs/monograph/prime-matrix-triad-a1-persistentcap-terminal-router.md/json
```

当前读数：

```text
mass_source_persistent_count=68；
payment_persistent_count=68；
promotion_cap_count=68；
deletion_cap_count=68；
all_counts_match=True；
all_current_persistent_caps_routed=True。
```

门控全真：

```text
mass_source_verified=True；
pxp_exit_closed_by_btls=True；
payment_intersections_recomputed=True；
payment_phase_m_counts_match=True；
top_prime_is_next_high_prime=True；
promotion_all_fiber_deletion=True；
promotion_deletion_potential_positive=True。
```

## 3. 结构意义

当前 `68` 个 PersistentCap 已经满足：

```text
1. 有同一 M_Q 质量来源；
2. 前 P 行出口由 BTLS 关闭；
3. column-tail 支付方程已物化；
4. top-prime 支付全部是下一新增素数；
5. 晋升到 Q'=30030 后全部产生正删除势。
```

所以这些 cap 不再承担“P 行以内零行”的风险；它们现在承担的是递归塔风险：

```text
若后续每层都有正删除势且 sum D_n 发散：
  支撑密度趋零，回到 Sparse/LocalSurvivor/容量矛盾；

若 sum D_n 可求和：
  a_n->1，进入 NoDeletion-KL；

若 NoDeletion 有偏斜：
  new-layer/profinite PDEC；

若 NoDeletion 平坦：
  CleanKLS/DLS；

若固定 residue/column 签名持久：
  TailAnchor/ColumnCRT PDEC。
```

## 4. 闭合边界

本文完成：

```text
当前 PersistentCap 的中间路由闭合；
top-prime 持久支付被递归晋升吸收；
当前层正删除势账本接入。
```

本文未完成：

```text
任意后继层删除势发散定理；
NoDeletion-KL/PDEC 证书全集；
CleanKLS/DLS 大筛证书；
TailAnchor/ColumnCRT PDEC 排斥。
```

因此它推进的是全局闭合链的结构归约，而不是最终无条件行命题证明。
