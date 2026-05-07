# Triad-A1 连续方向弧 Box-Dual 审计

**状态：** `continuous_direction_arc_box_dual_materialized_not_closed`

连续方向弧 box-dual 已物化：当前合法 box 行不能给出 U_CRT<L_PDEC。它把 ContinuousDirectionArcDual 缺口转成具体的 persistent continuous DualCap 输入。

## 1. 结构律

在仅有 0<=g(t)<=M(t) 的同集容量行下，固定 h 与方向 zeta 的最优解会取满 Re(e^{i zeta}e(ht))>0 的全部相位。因此连续方向弧上界可由半平面支持函数精确计算。若该上界仍大，失败对象就是连续方向 DualCap，必须加入 column/tail/cofactor 行或转 CleanKLS。

```text
U_box(h,zeta)=sum_t M(t) max(0, Re(e^{i zeta}e(ht)))；
U_box(h)=max_zeta U_box(h,zeta)。
```

这是当前合法 box 行的精确连续方向弧上界，不是离散方向采样。

## 2. 汇总

- `Q=2310`。
- `route_counts={'PersistentContinuousDualCapNeedsColumnTailOrCleanKLS': 8, 'SparseContinuousDualCapToLocalSurvivor': 1}`。
- `global_max_box_dual_value_over_total_m=0.998391`。
- `global_min_best_cap_phase_count=4`。

## 3. P 级最强连续弧

| P | total M | nonzero phases | best h | zeta | U_box/M | cap mass share | cap phases | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 4 | 4 | 377 | 0.418398 | 0.998391 | 1 | 4 | `SparseContinuousDualCapToLocalSurvivor` |
| 17 | 28 | 28 | 1309 | 0.716667 | 0.920824 | 1 | 28 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 19 | 496 | 140 | 847 | 0.318866 | 0.875267 | 0.987903 | 137 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 23 | 3456 | 232 | 1045 | 0.272541 | 0.871343 | 0.923611 | 188 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 29 | 6416 | 150 | 1595 | 0.655463 | 0.849387 | 0.981297 | 145 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 31 | 150056 | 596 | 1085 | 0.764017 | 0.807475 | 0.907874 | 400 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 37 | 984644 | 810 | 1015 | 0.279846 | 0.848953 | 0.944427 | 549 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 43 | 591088736 | 2050 | 805 | 0.324739 | 0.730057 | 0.88754 | 1094 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |
| 47 | 17276029248 | 2266 | 665 | 0.357868 | 0.70571 | 0.862747 | 1142 | `PersistentContinuousDualCapNeedsColumnTailOrCleanKLS` |

## 4. 读法

如果目标是证明 `U_CRT<L_PDEC`，当前 box 行已经不够：连续方向上仍有 persistent cap。
因此下一步不应继续增加方向采样密度，而应补入同集合法的结构行：

```text
column/displacement compatibility；
tail/cofactor nonreuse；
actual Gamma forced-signature constraints；
或 flat residual CleanKLS/DLS。
```
