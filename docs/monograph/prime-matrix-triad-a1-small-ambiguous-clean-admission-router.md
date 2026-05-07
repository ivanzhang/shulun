# Triad-A1 Small-Ambiguous CleanKLS 准入路由器

**状态：** `small_ambiguous_branch_routed_before_clean_terminal`

当前 APS small-ambiguous 分支尚未触发 clean 终端：已物化升层仍全部处于 FiberDeletion；同时 KL 形状账本显示，若把这些层视作 NoDeletion，偏斜也会以 phase-residue mutual PDEC witness 回流。

## 1. 结构律

small-ambiguous 分支不能直接调用 CleanKLS。若新增层仍有 fiber deletion，则继续由删除势推进；若删除停止但 KL 或 phase-residue 互信息持久偏大，则回流 new-layer/refined PDEC；只有 deletion 停止且 KL/互信息同时趋平，才成为真正 CleanKLS/DLS 输入。

```text
small ambiguous residual
  => FiberDeletion 继续推进；
  or NoDeletion + KL/MI 偏斜 => refined/new-layer PDEC；
  or NoDeletion + KL/MI flat => CleanKLS/DLS。
```

## 2. 门控

- `small_ambiguous_gate_active=True`。
- `current_layers_delete_before_clean=True`。
- `kl_chain_identity_exact=True`。
- `if_nodeletion_then_phase_residue_pdec_witness=True`。
- `no_clean_shape_currently_visible=True`。
- `all_current_small_ambiguous_routed=True`。

## 3. Small-Ambiguous 汇总

- `global_max_ambiguous_gamma_share_upper_bound=0.0552843`。
- `global_min_signature_signal_minus_ambiguous_budget=0.130733`。
- `global_min_signature_signal_to_ambiguity_ratio=3.51497`。

## 4. NoDeletion/KL 汇总

- `gate_counts={'FiberDeletion': 6}`。
- `shape_route_counts={'PhaseResidueMutualPDECWitness': 6}`。
- `current_nodeletion_triggered=False`。
- `max_global_residue_normalized_kl=0.0388557`。
- `min_phase_residue_mutual_normalized_kl=0.4125`。
- `max_kl_chain_abs_error=0`。

## 5. 当前结论

当前层没有 clean KLS 终端输入。真正剩余证明义务是：若未来升层删除势停止，
必须证明 KL/互信息平坦并提交 CleanKLS/DLS 证书；若不平坦，则自动回流 PDEC。
