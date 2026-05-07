# Triad-A1 连续 actual-payment 终端二分路由器

**状态：** `continuous_terminal_dichotomy_admission_closed_capacity_open`

连续 actual-payment 分支的终端二分已经闭合到两个外部终端义务：正 limsup 有限签名不是新出口，而是合法 column-tail PDEC 输入；全部有限签名消散不是新出口，而是 L2-flat CleanKLS/DLS 输入。剩余未闭合的是 PDEC 容量不等式和 CleanKLS 大筛估计本身。

## 1. 终端二分律

对任意无限反例塔的 canonical payment probability measures mu_i，固定有限层的 payment-signature 空间是有限的。因此要么某个有限签名有正 limsup 质量，要么每个固定有限签名质量都趋零。前者是 column-tail PDEC formal row 的合法输入；后者给出所有有限投影的 max atom 和 L2 能量趋零，即 CleanKLS/DLS admission。

```text
canonical payment measures mu_i on finite projection B_i；
either exists b in B_i with limsup mu_i(b)>0
  => positive-limsup finite signature => column-tail PDEC；
or for every fixed finite projection atom b, mu_i(b)->0
  => max atom -> 0 and L2 -> 0 on finite projections => CleanKLS/DLS admission。
```

这一步关闭的是二分逻辑，不声称已经证明 PDEC 容量或 KLS 大筛终端估计。

## 2. 汇总

- `all_actual_payment_measures_constructed=True`。
- `cap_route_count=9`。
- `positive_demand_route_count=8`。
- `route_counts={'NoTailDemandSparseOrLocalSurvivor': 1, 'PositiveLimsupPDECOrDiffuseCleanKLSDichotomy': 8}`。
- `global_max_actual_signature_share=0.0357143`。
- `global_min_effective_signature_support=28`。
- `global_min_inverse_l2_signature_support=28`。

## 3. 已闭合子命题

- `canonical actual payment measure constructed`。
- `payment_count equals low-hole demand`。
- `no third terminal route in the finite-projection dichotomy`。
- `diffuse branch supplies L2-flat admission language`。
- `positive-limsup branch supplies legal finite column-tail PDEC row input`。

## 4. 剩余终端义务

- `PDEC-CAP: prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC`。
- `KLS-EXT: prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures`。

## 5. Cap 路由

| P | demand | max sig share | eff sig support | L2 sig support | distinct sigs | route |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 0 | n/a | n/a | n/a | 0 | `NoTailDemandSparseOrLocalSurvivor` |
| 17 | 28 | 0.0357143 | 28 | 28 | 28 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 19 | 748 | 0.0254011 | 39.3684 | 112.803 | 325 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 23 | 7368 | 0.0103149 | 96.9474 | 260.521 | 748 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 29 | 22136 | 0.0122877 | 81.3824 | 330.763 | 1083 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 31 | 597416 | 0.0180444 | 55.4189 | 391.834 | 2081 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 37 | 5096664 | 0.0122645 | 81.5362 | 473.332 | 3129 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 43 | 3710420992 | 0.00316956 | 315.501 | 1539.39 | 6200 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |
| 47 | 114112801296 | 0.00598387 | 167.116 | 1342.9 | 8049 | `PositiveLimsupPDECOrDiffuseCleanKLSDichotomy` |

## 6. 读法

当前样本的 actual payment 已经高度分散；但全局证明不能依赖这些有限数值。
真正可用的是投影塔二分：集中则命名为 PDEC，完全不集中则满足 CleanKLS 的 L2-flat 输入。
所以下一步必须直接攻 `PDEC-CAP` 或 `KLS-EXT`，不能再把 actual payment 当作未定义缺口。
