# Triad-A1 PDEC 质量来源路由器

**状态：** `current_dualcap_mass_sources_routed_to_btls_lfte_terminal_open`

当前 DualCap 三族都已有可追踪的 M_Q 质量来源；其 P×P 早期出口由 SparseLocalSurvivor 或全支撑 BTLS 子集继承关闭。剩余不是早期行出口，而是 PDEC/CleanKLS 等终端证书。

## 1. 结构律

A legal PDEC cap must first attach to the same formal unit C_P and inherit M_Q(t). If it is a subset of supp(M_Q) and Q>P, BTLS closes the P-row boundary exit. If a concrete atom is extracted, LFTE expands its remaining high-prime fiber locally.

```text
PDEC cap legal use:
  S subset same C_P formal unit;
  g(t)<=M_Q(t);
  cap C subset supp(M_Q);
  Q>P => BTLS checks only C cap [1,P];
  extracted atom => LFTE local fiber expansion.
```

## 2. DualCap 三族

- `dualcap_class_counts={'ForcedPersistentByDensityBarrier': 24, 'PersistentCap': 68, 'SparseCap': 16}`。
- `dualcap_route_counts={'LiftOrColumnTailOrCleanKLS': 24, 'LocalSurvivorOrExplicitPDEC': 16, 'RefinedPDECOrColumnTailRows': 68}`。
- `all_current_dualcap_mass_sources_verified=True`。
- `all_current_dualcap_pxp_exits_closed=True`。

| family | count | mass source verified | P×P exit route | P×P exit closed | remaining obligation |
| --- | ---: | --- | --- | --- | --- |
| SparseCap | 16 | `True` | `SparseLocalSurvivorOrFinitePDEC` | `True` | finite PDEC packet beyond P; no P-row exit in current sparse atoms. |
| PersistentCap | 68 | `True` | `BoundarySubsetBTLS` | `True` | ColumnTail/TailAnchor PDEC or distributed CleanKLS/DLS. |
| ForcedPersistentByDensityBarrier | 24 | `True` | `BoundarySubsetBTLS plus lift monotonicity` | `True` | next lift, column-tail rows, PDECEntropy, or CleanKLS. |

## 3. 早期出口读数

- `all_boundary_terminals_excluded=True`。
- `all_phase_le_p_have_local_survivor=True`。
- `total_phase_le_p_count=113`。
- `total_y0_completion_le_p_count=0`。
- `all_phase_mass_identities_hold=True`。
- `all_terminal_gt_p=True`。
- `total_nonzero_phase_count=5030`。
- `total_terminal_le_p_count=0`。

## 4. 剩余义务

- Prove S subset Z_LHB or an equivalent attachment for any new formal PDEC branch.
- For persistent current caps, finish ColumnTail/TailAnchor PDEC or distributed CleanKLS/DLS.
- For forced persistent caps, continue lift deletion/KL/CleanKLS routing.
- For any cap without same M_Q source, return to Multiplicity-Stitching instead of using BTLS/LFTE.

## 5. 读法

这一步没有排除全部 PDEC，也没有完成全局行命题。
它完成的是当前 DualCap 族的质量来源与早期出口接线：

```text
SparseCap     => SparseLocalSurvivor / finite PDEC beyond P；
PersistentCap => BTLS 关闭 P 行出口，终端转 ColumnTail 或 CleanKLS；
ForcedCap     => BTLS 关闭 P 行出口，升层后继续 deletion/KL/CleanKLS。
```

因此当前 PDEC 硬点已经从“是否可能在 P 行内出零行”推进为：

```text
同一 formal unit 的 PDEC 上界；
或持久支付签名的 ColumnTail/TailAnchor 排斥；
或 clean residual 的 KLS/DLS 证书。
```
