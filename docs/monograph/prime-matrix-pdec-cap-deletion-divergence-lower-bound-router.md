# Prime Matrix PDEC-CAP 删除发散下界路由器

**状态：** `deletion_divergence_lower_bound_reduced_to_occupancy_saturation`

全局删除势发散下界继续压窄：HRO 引理证明若删除势不发散，就必须出现 `OccupancySaturation` 或 `TailIndependence`。后者已由 NoDeletion-KL/CleanKLS 路由吸收；因此删除侧真正剩余是排斥占用饱和，或把占用饱和送入 PDEC/ColumnCRT。

## 1. 路由律

HRO gives S_t subset Occ_t union TI_t. If the deletion potential does not diverge, then on a positive subsequence the average Occ/r + TI/r must tend to one. The TI branch is precisely promoted-prime non-necessity and is already routed to NoDeletion-KL/PDEC or CleanKLS/SC9. Therefore the deletion-divergence lower-bound problem is reduced to excluding OccupancySaturation: near-full old-hole residue occupancy must imply a lower-level capacity contradiction, PDEC, or ColumnCRT.

```text
HRO: S_t subset Occ_t union TI_t;
if sum D_n does not diverge
  => average Occ/r + TI/r -> 1 on a positive subsequence;
TI/r -> 1
  => NoDeletion-KL/PDEC or CleanKLS/SC9;
therefore deletion-side remaining hardpoint
  => OccupancySaturationPDECOrColumnCRT.
```

## 2. 汇总

- `deletion_divergence_lower_bound_reduced=true`。
- `global_deletion_divergence_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_deletion_hardpoint=OccupancySaturationPDECOrColumnCRT`。
- `open_final_gates=['OccupancySaturationPDECOrColumnCRT']`。
- `hro_summary={'row_count': 6, 'min_certified_deletion_lb_rate': 0.6564102564102564, 'max_union_bound_rate': 0.3435897435897436, 'max_occupied_rate': 0.30256410256410254, 'max_tail_independent_rate': 0.08753315649867374, 'all_nonempty_survival_bounded_by_union': True, 'all_certified_deletion_positive': True}`。
- `deletion_summary={'row_count': 6, 'min_deletion_rate': 0.6871794871794872, 'min_deletion_potential': 1.1621256943904354, 'max_survival_rate': 0.3128205128205128, 'all_deletion_positive': True}`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `DeletionDivergenceHardpointActive` | `true` | `false` | GlobalDeletionPotentialDivergenceLowerBound | 上一层已把删除侧压到全局删除势发散下界。 |
| `PromotedPrimeEssentialityMaterialized` | `true` | `false` | {'row_count': 6, 'min_deletion_rate': 0.6871794871794872, 'min_deletion_potential': 1.1621256943904354, 'max_survival_rate': 0.3128205128205128, 'all_deletion_positive': True} | 当前物化层中 promoted prime 的必要性删除势为正；删除不是统计噪声。 |
| `HROBarrierRegistered` | `true` | `false` | S_t subset Occ_t union TI_t | HRO 引理给出幸存 fiber 只能来自旧洞 residue 占用或 Tail 独立完成。 |
| `CurrentHROLayersDelete` | `true` | `false` | {'row_count': 6, 'min_certified_deletion_lb_rate': 0.6564102564102564, 'max_union_bound_rate': 0.3435897435897436, 'max_occupied_rate': 0.30256410256410254, 'max_tail_independent_rate': 0.08753315649867374, 'all_nonempty_survival_bounded_by_union': True, 'all_certified_deletion_positive': True} | 当前 HRO 物化层中 union bound 严格控制幸存率，且认证删除下界均为正。 |
| `DivergenceFailureForcesSaturationOrTailIndependence` | `true` | `false` | if sum D_n finite, Occ/r + TI/r -> 1 on a positive subsequence | 若删除势不可发散，则 HRO 迫使占用近满或 Tail 独立近满，没有第三种删除逃逸。 |
| `TailIndependenceRoutedToNoDeletionKLClean` | `true` | `false` | CleanKLSDLSLargeSieveOrExternalKLSInput | Tail 独立近满就是 promoted prime 非必要，已进入 NoDeletion-KL/PDEC 或 CleanKLS/SC9 分支。 |
| `DeletionDivergenceLowerBoundReduced` | `true` | `false` | only OccupancySaturation remains on deletion side | 删除发散下界已压到 OccupancySaturation 排斥；TailIndependence 已回流 NoDeletion/CleanKLS。 |
| `OccupancySaturationPDECOrColumnCRT` | `false` | `true` | near-full old-hole residues not globally excluded | 仍需证明 \|Occ_t\|/r -> 1 的占用饱和会触发低层容量矛盾、PDEC 或 ColumnCRT。 |

## 4. 剩余

`OccupancySaturationPDECOrColumnCRT` 尚未证明。下一步应证明旧洞 residue 近满占用不能在无限塔中保持：要么低层洞密度过大形成容量矛盾，要么相位偏斜持久形成 PDEC，要么列位移结构形成 ColumnCRT。
