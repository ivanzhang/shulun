# Prime Matrix PDEC-CAP 占位饱和核路由器

**状态：** `occupancy_saturation_reduced_to_dense_old_hole_kernel`

`OccupancySaturation` 已被严格压缩：稀疏旧洞情形由 HRO 注入界直接排除；若占位仍近满，则必须存在近满 promoted residue 的旧洞选择核。因此下一硬点不再是宽口径占位饱和，而是 `DenseOldHoleKernelCapacityPDECOrColumnCRT`。

## 1. 核路由律

HRO already gives |Occ_t| <= min(|H_Q(t)|, r). Hence near-full occupancy |Occ_t|/r -> 1 is impossible in every sparse old-hole regime |H_Q(t)| <= (1-eta)r, and more generally unless the old holes occupy (1-o(1))r distinct promoted-prime residues. In the remaining case one can choose a selector c_b in H_Q(t) for (1-o(1))r residues b, satisfying ((t+bQ-1)P+c_b)=0 mod r while c_b avoids every low-prime forbidden class mod q|Q. Thus the true hardpoint is not generic occupancy saturation, but a dense old-hole selector kernel; it must be discharged by a low-level capacity contradiction, persistent phase-residue PDEC, or ColumnCRT displacement rigidity.

```text
HRO injection:
  |Occ_t| <= min(|H_Q(t)|, r).

Therefore:
  |H_Q(t)| <= (1-eta)r
    => |Occ_t|/r <= 1-eta
    => no OccupancySaturation.

If OccupancySaturation persists:
  exists B_t subset Z/rZ with |B_t|=(1-o(1))r;
  for each b in B_t choose c_b in H_Q(t);
  ((t+bQ-1)P+c_b)=0 mod r;
  c_b avoids every low-prime forbidden class mod q|Q.

Remaining target:
  DenseOldHoleKernelCapacityPDECOrColumnCRT.
```

## 2. 汇总

- `occupancy_saturation_reduced_to_dense_kernel=true`。
- `occupancy_saturation_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_occupancy_hardpoint=DenseOldHoleKernelCapacityPDECOrColumnCRT`。
- `open_final_gates=['DenseOldHoleKernelCapacityPDECOrColumnCRT']`。
- `hro_saturation_summary={'row_count': 6, 'max_phase_occupied_ratio': 0.3076923076923077, 'max_avg_occupied_ratio': 0.30256410256410254, 'max_union_bound_rate': 0.3435897435897436, 'min_saturation_gap': 0.6923076923076923, 'max_old_hole_count': 5, 'min_promoted_prime': 13, 'max_promoted_prime': 17, 'dense_phase_count_at_0_9': 0, 'current_layers_far_from_occupancy_saturation': True}`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `OccupancyHardpointActive` | `true` | `false` | OccupancySaturationPDECOrColumnCRT | 上一层已把删除侧真正剩余压到 HRO 占位饱和出口。 |
| `HROInjectionBoundRegistered` | `true` | `false` | \|Occ_t\| <= min(\|H_Q(t)\|, r) | 每个旧洞列在 promoted prime residue 上最多贡献一个占位；占位近满必须先有旧洞 residue 近满。 |
| `SparseOldHoleCaseExcluded` | `true` | `false` | if \|H_Q(t)\| <= (1-eta)r then \|Occ_t\|/r <= 1-eta | 只要旧洞数或旧洞 residue 数有固定缺口，占位饱和不可能发生，HRO 自动给出删除缺口。 |
| `NearFullOccupancyForcesSelectorKernel` | `true` | `false` | exists B_t with \|B_t\|=(1-o(1))r and c_b in H_Q(t) | 占位饱和等价于存在近满 residue 选择核：对几乎每个 promoted residue，可选一个旧洞列同时避开全部低层素因子同余禁类。 |
| `CurrentAuditsFarFromSaturation` | `true` | `false` | {'row_count': 6, 'max_phase_occupied_ratio': 0.3076923076923077, 'max_avg_occupied_ratio': 0.30256410256410254, 'max_union_bound_rate': 0.3435897435897436, 'min_saturation_gap': 0.6923076923076923, 'max_old_hole_count': 5, 'min_promoted_prime': 13, 'max_promoted_prime': 17, 'dense_phase_count_at_0_9': 0, 'current_layers_far_from_occupancy_saturation': True} | 当前物化层的最大相位占位率远低于 1；这是 sanity check，不是全局证明。 |
| `DenseOldHoleKernelCapacityPDECOrColumnCRT` | `false` | `true` | near-full selector kernel not globally excluded | 剩余硬点已经从一般占位饱和压成稠密旧洞选择核：需证明它触发低层容量矛盾、PDEC 相位偏斜或 ColumnCRT 列位移刚性。 |

## 4. 剩余

`DenseOldHoleKernelCapacityPDECOrColumnCRT` 尚未排除。下一步应直接研究近满选择核的三种互斥出路：低层轮筛容量过载、相位-residue 分布持久偏斜形成 PDEC、或选择列随 promoted residue 呈固定列位移结构形成 ColumnCRT。
