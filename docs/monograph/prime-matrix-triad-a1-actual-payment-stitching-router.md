# Triad-A1 ActualPaymentStitching 路由器

**状态：** `forcedcap_multibucket_rows_routed_to_actual_payment_stitching`

ForcedCap 多桶分支的当前 48 个矩阵行已全部路由到 ActualPaymentStitching：单桶支付已排除，裸多桶 LP 已坍缩，有限层 MFU 候选行已存在；进一步加入同一 CRT fiber y 的一致完成态后，实际支付至少需要 42 个 residue 桶或 24 个 column-residue 桶，且至少约 94.47% 的支付边由唯一覆盖强制决定。ForcedGammaSignature 进一步显示 48 个有限签名行的信号均超过 ambiguous 预算：持久则进入 MFU/PDEC，不持久则进入 small-ambiguous 后继门控。当前后继层仍由 FiberDeletion 推进；若视作 NoDeletion，则 KL 形状回流 phase-residue PDEC，尚未触发 clean KLS 终端。

## 1. 路由链

```text
ExposureDominance => no single-bucket payment
MultiBucketSkeleton => vector g_b(t) materialized
ProjectionCollapse => bare multi-bucket LP gives no stronger projection
MFUCandidateAudit => finite phase-bucket correlated rows exist
FiberConsistentPayment => actual completions come from one CRT fiber y
FiberDominance => at least 42 residue buckets or 24 column-residue buckets
GammaFreedom => at most 5.53% choice-ambiguous holes; at least 94.47% forced
ForcedGammaSignature => finite signature signal exceeds ambiguous budget on all 48 rows
SmallAmbiguousCleanAdmission => current successor layers delete or return phase-residue PDEC
ActualPaymentStitching => persistent Gamma row gives MFU/PDEC; no persistent row gives CleanKLS/DLS
```

## 2. 计数链

- `skeleton_matrix_row_count=48`。
- `collapse_matrix_row_count=48`。
- `mfu_matrix_row_count=48`。
- `forced_signature_matrix_row_count=48`。
- `fiber_forced_cap_count=24`。
- `fiber_dominance_forced_cap_count=24`。
- `gamma_freedom_forced_cap_count=24`。
- `forced_signature_forced_cap_count=24`。

## 3. 签名压力

- `global_max_ambiguous_gamma_share_upper_bound=0.05528425182914454`。
- `global_min_forced_gamma_share_lower_bound=0.9447157481708555`。
- `global_min_signature_signal_minus_ambiguous_budget=0.13073320222097914`。
- `global_min_signature_signal_to_ambiguity_ratio=3.51497432278278`。

## 4. Small-Ambiguous 后继

- `current_nodeletion_triggered=False`。
- `gate_counts={'FiberDeletion': 6}`。
- `max_global_residue_normalized_kl=0.038855655443699094`。
- `max_kl_chain_abs_error=0.0`。
- `min_phase_residue_mutual_normalized_kl=0.41250010713817964`。
- `shape_route_counts={'PhaseResidueMutualPDECWitness': 6}`。
- `all_counts_match=True`。

## 5. 门控

- `single_bucket_payments_excluded=True`。
- `bare_projection_collapses=True`。
- `finite_layer_mfu_candidates_exist=True`。
- `fiber_completion_counts_match_m_vector=True`。
- `fiber_residue_bucket_lower_bound_active=True`。
- `fiber_column_residue_bucket_lower_bound_active=True`。
- `gamma_forced_share_large=True`。
- `forced_signature_or_small_ambiguous_gate_active=True`。
- `small_ambiguous_successor_routed_before_clean_terminal=True`。
- `all_current_forced_multibucket_rows_routed_to_aps=True`。

## 6. 终端二分

```text
Persistent Gamma follows finite MFU candidate
  => multi-bucket PDEC / refined TailAnchor-ColumnCRT-Cofactor row；

Gamma does not persist on any finite candidate
  => DistributedPayment / CleanKLS-DLS。
```
