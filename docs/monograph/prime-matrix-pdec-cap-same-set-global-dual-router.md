# Prime Matrix PDEC-CAP 同集全局对偶前沿路由器

**状态：** `pdec_cap_same_set_global_dual_frontier_reduced_to_terminal_estimates_not_closed`

PDEC-CAP 的当前已物化中间门全部可路由，APS 投影塔二分也已闭合；diffuse 分支又被压到固定壳低模 PDEC/ColumnCRT 持久偏斜或自足 SC-9。新增持久有限签名统一路由后，持久 MFU 与固定壳低模持久不再是两个平行硬点。但全局同集对偶证书仍未闭合。最新最窄剩余是：统一的 `PersistentFiniteSignaturePDECColumnCRT` 终端排斥，或无持久多壳平坦分支的 `SelfContainedKuznetsovLSAtomSC9`。

## 1. 前沿律

The current same-set PDEC-CAP obligation is no longer an unnamed Fourier constant search. Materialized DualCaps have same-M_Q mass sources and closed early P-row exits; current PersistentCaps route to promotion deletion or NoDeletion-KL/CleanKLS/PDEC; current ForcedCaps route to multi-bucket actual payment stitching. The profinite ActualPaymentStitching dichotomy for the real payment graph Gamma is now closed as a routing law. Persistent Gamma gives a finite-signature formal unit; nonpersistent Gamma must enter FiberDeletion/NoDeletion-KL/CleanKLS. The diffuse terminal split is now routed further to fixed-shell low-mod PDEC/ColumnCRT persistence or the self-contained Kuznetsov-LS atom SC-9. The persistent-signature unification router identifies persistent MFU and fixed-shell low-mod persistence as the same finite-signature formal-unit grammar. The remaining global final gates are the unified PersistentFiniteSignaturePDECColumnCRT terminal and the separate flat SC-9 atom, not an unnamed APS/diffuse exit.

```text
PDEC_CAP_SameSetGlobalDualCertificate
  -> current DualCap families routed;
  -> current PersistentCap routed by promotion deletion / NoDeletion-KL;
  -> current ForcedCap routed to multi-bucket ActualPaymentStitching;
  -> APS profinite dichotomy routed;
  -> persistent MFU and fixed-shell persistence unified;
  -> remaining terminal estimates:
       PersistentFiniteSignaturePDECColumnCRT or SC-9.
```

## 2. 汇总

- `closed_current_materialized_pdec_gates=true`。
- `pdec_cap_same_set_global_dual_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9`。
- `open_final_gates=['PersistentFiniteSignaturePDECColumnCRT', 'SelfContainedKuznetsovLSAtomSC9']`。

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
| `DiffuseTerminalSplitRouted` | `true` | `false` | FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9 | 不持久 Gamma 分支已合成为删除势/NoDeletion-KL/CleanKLS 的终端分裂，无名 diffuse 出口关闭。 |
| `PersistentMFUAndFixedShellUnified` | `true` | `false` | PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9 | 持久 Gamma 的 MFU 分支与不持久 Gamma 内部冒出的固定壳低模持久分支，已经统一为同 formal unit 的有限签名 PDEC/ColumnCRT 证书对象。 |
| `ActualPaymentStitchingContractSupersededByProfiniteDichotomy` | `true` | `false` | contract open text superseded by profinite APS router | 原 APS 合同中的二分缺口已由投影塔二分路由器闭合；它不再是独立终端阻塞。 |
| `PersistentFiniteSignaturePDECColumnCRT` | `false` | `true` | terminal U_CRT<L_PDEC or displacement PDEC exclusion not submitted | 所有持久有限签名 formal unit 仍需提交同集 PDEC/ColumnCRT 对偶容量排斥证书。 |
| `SelfContainedKuznetsovLSAtomSC9` | `false` | `true` | flat multishell clean atom remains open | 无持久有限签名且多壳完全平坦时，完全自足版仍需证明 SC-9 谱大筛原子。 |

## 4. 下一步

下一步直接攻两侧终端估计：统一持久有限签名 formal unit 的 `PersistentFiniteSignaturePDECColumnCRT` 对偶容量证书；以及无持久、多壳平坦时的自足 `SelfContainedKuznetsovLSAtomSC9`。
