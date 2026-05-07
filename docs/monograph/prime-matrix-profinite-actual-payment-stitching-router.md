# Prime Matrix APS 投影塔二分路由器

**状态：** `profinite_actual_payment_stitching_dichotomy_closed_terminal_estimates_open`

APS 的投影塔二分逻辑已闭合：真实支付图 `Gamma_n` 在任意无限反例塔上，要么某个有限签名正 limsup 持久，进入多桶 MFU/PDEC；要么每个固定有限签名质量趋零，进入分散 CleanKLS/DLS 输入，期间若删除势或 KL 偏斜出现则回流 PDEC。这一步关闭的是无名 APS 出口；全局 PDEC-CAP 仍需两侧终端估计。

## 1. 二分律

For the inverse tower of finite payment-signature spaces, project the real payment graph Gamma_n to every fixed finite level. Since each level is finite, either some finite atom has positive limsup mass, or every fixed atom has mass tending to zero. The first case is PersistentStitching and creates a multi-bucket formal PDEC unit. The second case is NoPersistentStitching: all finite projections have max atom and L2 energy tending to zero, so the branch is a diffuse CleanKLS/DLS input unless FiberDeletion or NoDeletion-KL has already routed it back to PDEC. This closes the APS dichotomy logic but not the terminal PDEC or KLS estimates.

```text
Gamma_n on inverse finite signature tower
  either exists finite atom R with limsup Gamma_n(R)>0
    => PersistentStitching => multi-bucket MFU/PDEC；
  or every fixed finite atom has Gamma_n(R)->0
    => NoPersistentStitching => diffuse CleanKLS/DLS input；
  with FiberDeletion / NoDeletion-KL allowed to route back to PDEC before CleanKLS.
```

## 2. 汇总

- `profinite_aps_dichotomy_closed=true`。
- `pdec_cap_same_set_global_dual_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseCleanKLS`。
- `open_final_gates=['SameSetPDECDualComparisonForPersistentMFU', 'DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `PDECCapRequestsAPS` | `true` | `false` | SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseGlobalDeletionOrSC9 | 上一层 PDEC-CAP 前沿已经把 APS 投影塔二分定位为当前门，或已越过 APS 推进到两侧终端估计。 |
| `APSContractContainsTwoWaySplit` | `true` | `false` | PersistentStitching / NoPersistentStitching | APS 合同已经写明真实支付图只能进入持久缝合或无持久缝合两路。 |
| `CurrentForcedRowsRoutedToAPS` | `true` | `false` | ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS | 当前 forced 多桶行已全部进入 APS，且有限候选行与 forced/ambiguous 门控已接线。 |
| `FiniteProjectionDichotomyAvailable` | `true` | `false` | continuous_terminal_dichotomy_admission_closed_capacity_open | 有限投影空间有限，因此正 limsup 原子或全部原子消散二分可复用到 Gamma 投影塔。 |
| `PositiveLimsupBranchRoutesToPDEC` | `true` | `false` | positive-limsup finite signature => PDEC input | 若 Gamma 在某有限签名上正 limsup 持久，则生成多桶 formal unit/refined PDEC 输入。 |
| `DiffuseBranchRoutesToCleanOrDeletionKL` | `true` | `false` | CurrentLayerFiberDeletionOrNoDeletionPhaseResiduePDEC; CleanKLSOnlyAfterFlatNoDeletion | 若固定有限签名全部消散，则进入分散支付；当前门控要求先经 FiberDeletion 或 NoDeletion-KL，平坦时才 CleanKLS。 |
| `NewFiniteAtomsDoNotCreateFourthExit` | `true` | `false` | PDEC cap no-cycle + new-layer entropy contract | 若二分过程中生成新的有限原子，它只会细化 PDEC、升层或进入 CleanKLS，不生成第四出口。 |
| `ProfiniteActualPaymentStitchingDichotomyClosed` | `true` | `false` | finite projection compactness / pigeonhole dichotomy | APS 的全局二分逻辑闭合；这只排除无名 APS 出口，不证明两侧终端估计。 |
| `SameSetPDECDualComparisonForPersistentMFU` | `false` | `true` | U_CRT^multi<L_PDEC^multi still open | 持久 Gamma 分支仍需多桶同集 PDEC 对偶容量证书。 |
| `DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL` | `false` | `true` | terminal estimates still open | 无持久 Gamma 分支仍需删除势发散、NoDeletion-KL/PDEC，或 KL 平坦 CleanKLS/DLS 大筛估计。 |

## 4. 剩余

本文件不证明 `U_CRT^multi<L_PDEC^multi`，也不证明 CleanKLS/DLS 大筛估计。它只证明 APS 不是第四出口：持久即 PDEC，消散即 CleanKLS/DLS 或删除/KL 回流 PDEC。
