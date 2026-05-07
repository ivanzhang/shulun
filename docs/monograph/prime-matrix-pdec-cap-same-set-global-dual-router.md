# Prime Matrix PDEC-CAP 同集全局对偶前沿路由器

**状态：** `pdec_cap_same_set_global_dual_frontier_reduced_to_aps_not_closed`

PDEC-CAP 的当前已物化中间门全部可路由，但全局同集对偶证书仍未闭合。最窄下一步不再是固定 Q 常数优化，而是 `ProfiniteActualPaymentStitchingDichotomy`：对无限反例塔中的真实支付图 `Gamma` 证明持久缝合或无持久缝合。持久则进入多桶同集 PDEC 对偶比较 `U_CRT^multi<L_PDEC^multi`；不持久则必须由 FiberDeletion、NoDeletion-KL/PDEC 或 KL 平坦的 CleanKLS/DLS 吸收。

## 1. 前沿律

The current same-set PDEC-CAP obligation is no longer an unnamed Fourier constant search. Materialized DualCaps have same-M_Q mass sources and closed early P-row exits; current PersistentCaps route to promotion deletion or NoDeletion-KL/CleanKLS/PDEC; current ForcedCaps route to multi-bucket actual payment stitching. The next self-contained hardpoint is the profinite ActualPaymentStitching dichotomy for the real payment graph Gamma. Persistent Gamma gives a multi-bucket same-set PDEC dual comparison; nonpersistent Gamma must enter FiberDeletion/NoDeletion-KL/CleanKLS. None of these global final gates is closed here.

```text
PDEC_CAP_SameSetGlobalDualCertificate
  -> current DualCap families routed;
  -> current PersistentCap routed by promotion deletion / NoDeletion-KL;
  -> current ForcedCap routed to multi-bucket ActualPaymentStitching;
  -> remaining global gate:
       ProfiniteActualPaymentStitchingDichotomy.
```

## 2. 汇总

- `closed_current_materialized_pdec_gates=true`。
- `pdec_cap_same_set_global_dual_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=ProfiniteActualPaymentStitchingDichotomy`。
- `open_final_gates=['ProfiniteActualPaymentStitchingDichotomy', 'SameSetPDECDualComparisonForPersistentMFU', 'GlobalFiberDeletionOrNoDeletionKLCleanKLS', 'ActualPaymentStitchingContractStillOpen']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `SelfContainedBottleneckAccepted` | `true` | `false` | PDEC_CAP_SameSetGlobalDualCertificate | 上一轮已把完全自足路线压到 PDEC-CAP 同集全局对偶证书。 |
| `SameSetPDECProtocolRegistered` | `true` | `false` | Same-Set Law and U_CRT<L_PDEC protocol | PDEC 比较必须作用于同一坏窗推前计数，失败必须输出 DualCap 或缺失行。 |
| `DualCapFailureMaterialized` | `true` | `false` | {'ForcedPersistentByDensityBarrier': 24, 'PersistentCap': 68, 'SparseCap': 16} | 固定 Q 的 PDEC 对偶失败已分解为 Sparse、Persistent、Forced 三类 DualCap。 |
| `SameMassAndEarlyExitClosedForCurrentDualCaps` | `true` | `false` | mass verified; P×P exits closed | 当前 DualCap 都有同一 M_Q 质量来源，早期 P×P 出口由 Sparse/BTLS/LFTE 接线关闭。 |
| `PersistentCapsCurrentLayerRouted` | `true` | `false` | {'PromotionFiberDeletion': 68} | 当前 68 个 PersistentCap 已进入晋升删除势、NoDeletion-KL/CleanKLS 或固定签名 PDEC 路线。 |
| `ForcedCapsCurrentLayerRouted` | `true` | `false` | {'MultiBucketPDECOrDistributedCleanKLS': 24} | 当前 24 个 ForcedCap 已退出固定 Q 循环，单桶实际支付被排除，剩余进入多桶 PDEC/APS。 |
| `ActualPaymentStitchingCurrentRowsRouted` | `true` | `false` | ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS | 当前 48 个多桶矩阵行已路由到 APS：持久 Gamma 进 MFU/PDEC，不持久进分散 CleanKLS/DLS。 |
| `LHBProjectionStitchingRemoved` | `true` | `false` | pi(A_Q') subset A_Q for same C_P support | 同一 LHB 全周期完成集合口径下，升层坏项 N 为空，ProjectionStitching 不再是当前分支出口。 |
| `PDECCapNoCycleRegistered` | `true` | `false` | finite Boolean algebra refinement; new-layer entropy contract | 固定有限签名群内 PDEC cap 细化不能无限循环；升层必须进入 new-layer PDEC 或 CleanKLS。 |
| `FiniteTowerEvidenceRegistered` | `true` | `false` | ['FiberDeletionLayer', 'FiberDeletionLayer'] | 已物化两层均为 FiberDeletionLayer，但这仍只是有限塔证据，不是全局证明。 |
| `ProfiniteActualPaymentStitchingDichotomy` | `false` | `true` | APS contract open | 必须对无限反例塔中的真实支付图 Gamma 证明 PersistentStitching 或 NoPersistentStitching 二分。 |
| `SameSetPDECDualComparisonForPersistentMFU` | `false` | `true` | U_CRT^multi<L_PDEC^multi not submitted for all persistent MFU | 若 Gamma 持久缝合成多桶 formal unit，仍需提交同集多桶 PDEC 对偶容量证书。 |
| `GlobalFiberDeletionOrNoDeletionKLCleanKLS` | `false` | `true` | new-layer tower finite evidence only | 若 Gamma 不持久或升层继续推进，需证明删除势发散，或 NoDeletion-KL 回流 PDEC，或 KL 平坦进 CleanKLS/DLS。 |
| `ActualPaymentStitchingContractStillOpen` | `false` | `true` | actual_payment_stitching_contract_open | APS 合同仍是 open；不能把当前有限层 APS 路由误写成全局 PDEC-CAP 闭合。 |

## 4. 下一步

直接攻 `ProfiniteActualPaymentStitchingDichotomy`。形式化目标是：给定反例塔中的真实支付图 `Gamma_n` 与有限候选签名族 `R_{j,n}`，证明存在正 limsup 持久签名，从而进入多桶 `PDEC`；或证明每个有限签名质量趋零，从而给出分散 `CleanKLS/DLS` 输入。若升层删除势持续为正，则由 FiberDeletion 递推剥离；若删除势停止但 KL/互信息不平坦，则回流 new-layer/refined PDEC。
