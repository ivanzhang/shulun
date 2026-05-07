# Triad-A1 PersistentCap 终端路由器

**状态：** `current_persistent_caps_routed_to_promotion_deletion_or_terminal_triad`

当前 68 个 PersistentCap 已从早期出口和 top-prime 独立终端中退出：它们有同一 M_Q 质量来源，P×P 出口由 BTLS 关闭，top-prime 支付全部晋升为 Q=2310->30030 的正删除势。剩余是删除势塔是否发散，或停止后进入 NoDeletion-KL/CleanKLS/PDEC。

## 1. 路由链

```text
AttachedMass => g(t)<=M_Q(t)
BTLS => no P-row boundary exit
ColumnTail payment => fixed signature PDEC or distributed CleanKLS
TopPrime=next prime => promote Q to rQ
PromotionFiberDeletion => deletion potential ledger
If deletion potential stops accumulating => NoDeletion-KL / CleanKLS / PDEC
```

## 2. 计数一致性

- `mass_source_persistent_count=68`。
- `payment_persistent_count=68`。
- `promotion_cap_count=68`。
- `deletion_cap_count=68`。
- `all_counts_match=True`。

## 3. 门控结果

- `mass_source_verified=True`。
- `pxp_exit_closed_by_btls=True`。
- `payment_intersections_recomputed=True`。
- `payment_phase_m_counts_match=True`。
- `top_prime_is_next_high_prime=True`。
- `promotion_all_fiber_deletion=True`。
- `promotion_deletion_potential_positive=True`。
- `all_current_persistent_caps_routed=True`。

## 4. 当前层指标

- `global_min_deletion_potential_current_layer=0.8800788718999966`。
- `global_max_survival_current_layer=0.4147501982553529`。
- `promotion_class_counts={'PromotionFiberDeletion': 68}`。
- `payment_route_counts={'ColumnTailPigeonholeRowOrDistributedCleanKLS': 68}`。
- `unique_phase_signature_count=1915`。

## 5. 剩余义务

- 证明沿正式无限反例族的晋升删除势发散，或抽出 NoDeletion 层。
- NoDeletion 层若 KL 偏斜持久，提交 new-layer/profinite PDEC。
- NoDeletion 层若 KL 可求和，提交 CleanKLS/DLS admission。
- 若固定 residue/column 签名持久，提交 TailAnchor/ColumnCRT PDEC。

## 6. 读法

这一步没有证明删除势在所有后继层必发散，也没有排除全部 PDEC/CleanKLS。
它关闭的是当前 PersistentCap 的三个中间逃逸：

```text
早期 P×P 出口      => BTLS 关闭；
固定 Q 同层循环     => TopPrime 晋升；
top-prime 独立终端  => PromotionFiberDeletion 删除势账本。
```

因此 PersistentCap 的全局剩余硬点已经变成：

```text
删除势塔发散；
或 NoDeletion-KL / CleanKLS；
或固定 residue/column PDEC。
```
