# Prime Matrix PDEC-CAP 同集全局对偶前沿路由器

**状态：** `pdec_cap_same_set_global_dual_frontier_reduced_to_terminal_estimates_not_closed`

PDEC-CAP 的当前已物化中间门全部可路由，APS 投影塔二分也已闭合；diffuse 分支又被压到 DenseOldHoleKernel/Capacity/PDEC/ColumnCRT 或自足 SC-9。但全局同集对偶证书仍未闭合。最新最窄剩余是：持久 `Gamma` 的多桶同集 PDEC 对偶比较 `U_CRT^multi<L_PDEC^multi`，以及不持久 `Gamma` 的 `DenseOldHoleKernelCapacityPDECOrColumnCRT` 或 `SelfContainedKuznetsovLSAtomSC9`。

## 1. 前沿律

The current same-set PDEC-CAP obligation is no longer an unnamed Fourier constant search. Materialized DualCaps have same-M_Q mass sources and closed early P-row exits; current PersistentCaps route to promotion deletion or NoDeletion-KL/CleanKLS/PDEC; current ForcedCaps route to multi-bucket actual payment stitching. The profinite ActualPaymentStitching dichotomy for the real payment graph Gamma is now closed as a routing law. Persistent Gamma gives a multi-bucket same-set PDEC dual comparison; nonpersistent Gamma must enter FiberDeletion/NoDeletion-KL/CleanKLS. The diffuse terminal split is now routed further to DenseOldHoleKernel/Capacity/PDEC/ColumnCRT or the self-contained Kuznetsov-LS atom SC-9. The remaining global final gates are the persistent same-set PDEC dual comparison and the narrowed diffuse terminal estimates, not an unnamed APS exit.

```text
PDEC_CAP_SameSetGlobalDualCertificate
  -> current DualCap families routed;
  -> current PersistentCap routed by promotion deletion / NoDeletion-KL;
  -> current ForcedCap routed to multi-bucket ActualPaymentStitching;
  -> APS profinite dichotomy routed;
  -> remaining terminal estimates:
       persistent MFU PDEC or diffuse DenseOldHoleKernel / SC-9.
```

## 2. 汇总

- `closed_current_materialized_pdec_gates=true`。
- `pdec_cap_same_set_global_dual_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=SameSetPDECDualComparisonForPersistentMFU_OR_DenseOldHoleKernelOrSC9`。
- `open_final_gates=['SameSetPDECDualComparisonForPersistentMFU', 'DiffuseDenseOldHoleKernelOrSelfContainedSC9']`。

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
| `ProfiniteActualPaymentStitchingDichotomy` | `true` | `false` | finite projection compactness / pigeonhole dichotomy | 真实支付图 Gamma 的 PersistentStitching / NoPersistentStitching 二分逻辑已闭合到两侧终端估计。 |
| `SameSetPDECDualComparisonForPersistentMFU` | `false` | `true` | U_CRT^multi<L_PDEC^multi not submitted for all persistent MFU | 若 Gamma 持久缝合成多桶 formal unit，仍需提交同集多桶 PDEC 对偶容量证书。 |
| `DiffuseTerminalSplitRouted` | `true` | `false` | DenseOldHoleKernelCapacityPDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9 | 不持久 Gamma 分支已合成为删除势/NoDeletion-KL/CleanKLS 的终端分裂，无名 diffuse 出口关闭。 |
| `DiffuseDenseOldHoleKernelOrSelfContainedSC9` | `false` | `true` | ['DenseOldHoleKernelCapacityPDECOrColumnCRT', 'SelfContainedKuznetsovLSAtomSC9'] | 不持久 Gamma 分支剩余自足义务：稠密旧洞选择核触发容量/PDEC/ColumnCRT，或 KL 平坦 clean 残余的 SC-9 谱大筛原子。 |
| `ActualPaymentStitchingContractSupersededByProfiniteDichotomy` | `true` | `false` | contract open text superseded by profinite APS router | 原 APS 合同中的二分缺口已由投影塔二分路由器闭合；它不再是独立终端阻塞。 |

## 4. 下一步

下一步直接攻两侧终端估计：持久 `Gamma` 分支的多桶同集 PDEC 对偶容量证书 `U_CRT^multi<L_PDEC^multi`；以及无持久 `Gamma` 分支中的稠密旧洞选择核容量/PDEC/ColumnCRT 或自足 `SelfContainedKuznetsovLSAtomSC9`。
