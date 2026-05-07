# Triad-A1 多桶投影坍缩路由器

**状态：** `bare_multibucket_lp_projection_collapse_routed`

裸多桶 LP 已全部投影坍缩：单桶支付虽已排除，但若没有 formal-unit 兼容行、列/尾条件行或实际支付图约束，多桶变量不会自动降低 U_CRT。下一步必须加入持久多桶签名兼容，或把无兼容情形路由到 CleanKLS/DLS。

## 1. 投影坍缩律

If only 0<=g_b(t)<=E_b(t), sum_b g_b(t)<=M(t), and the objective depends on G(t)=sum_b g_b(t), then the feasible projection is exactly 0<=G(t)<=M(t) whenever sum_b E_b(t)>=M(t) for every t. The current skeleton has sum_b E_b(t)=high_prime_count*M(t), so the bare multi-bucket LP gives no stronger U_CRT than the phase-mass projection.

```text
0 <= g_b(t) <= E_b(t)；
G(t)=sum_b g_b(t)；
sum_b g_b(t) <= M(t)；
sum_b E_b(t) >= M(t)
=> 0 <= G(t) <= M(t)。
```

所以仅有裸暴露上界时，多桶 LP 的 `G(t)` 投影不比普通相位质量上界更强。

## 2. 汇总

- `matrix_row_count=48`。
- `route_counts={'NeedsFormalUnitCompatibilityOrCleanKLS': 48}`。
- `all_single_bucket_payments_excluded=True`。
- `all_phase_capacity_surplus=True`。
- `all_bare_projection_collapses=True`。

## 3. 路由含义

这一步不是退回统计估计，而是排除一条无效闭合路径：

```text
单靠多桶变量数量增加
  不能推出 U_CRT^multi<L_PDEC^multi；

必须增加 formal-unit compatibility / TailAnchor / ColumnCRT / cofactor 条件行；
否则无持久兼容签名的部分进入 CleanKLS/DLS。
```

## 4. 明细

| P | kind | alpha | h | dir | phases | buckets | vars | route |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | residue | 0 | 805 | 0.25 | 1077 | 210 | 70520 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0 | 805 | 0.25 | 1077 | 210 | 70520 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0 | 1505 | 0.75 | 1081 | 210 | 70844 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0 | 1505 | 0.75 | 1081 | 210 | 70844 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.5 | 805 | 0.25 | 734 | 210 | 47690 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.5 | 805 | 0.25 | 734 | 210 | 47690 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.5 | 1505 | 0.75 | 734 | 210 | 47690 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.5 | 1505 | 0.75 | 734 | 210 | 47690 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0 | 770 | 0.5 | 1370 | 210 | 91939 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0 | 770 | 0.5 | 1370 | 210 | 91939 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0 | 1540 | 0.5 | 1370 | 210 | 91939 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0 | 1540 | 0.5 | 1370 | 210 | 91939 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.5 | 1155 | 0 | 1025 | 210 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.5 | 1155 | 0 | 1025 | 154 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.5 | 1155 | 0.5 | 1025 | 210 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.5 | 1155 | 0.5 | 1025 | 154 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.9 | 1155 | 0 | 1025 | 210 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.9 | 1155 | 0 | 1025 | 154 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.9 | 1155 | 0.5 | 1025 | 210 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.9 | 1155 | 0.5 | 1025 | 154 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.9 | 1155 | 0 | 1025 | 210 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.9 | 1155 | 0 | 1025 | 154 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | residue | 0.9 | 1155 | 0.5 | 1025 | 210 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 43 | column_residue | 0.9 | 1155 | 0.5 | 1025 | 154 | 68790 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0 | 665 | 0.25 | 1150 | 253 | 94198 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0 | 665 | 0.25 | 1150 | 253 | 94198 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0 | 1645 | 0.75 | 1145 | 253 | 93819 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0 | 1645 | 0.75 | 1145 | 253 | 93819 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0 | 770 | 0.5 | 1512 | 253 | 125486 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0 | 770 | 0.5 | 1512 | 253 | 125486 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0 | 1540 | 0.5 | 1512 | 253 | 125486 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0 | 1540 | 0.5 | 1512 | 253 | 125486 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.5 | 1001 | 0.25 | 757 | 253 | 60618 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.5 | 1001 | 0.25 | 757 | 253 | 60618 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.5 | 1309 | 0.75 | 757 | 253 | 60618 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.5 | 1309 | 0.75 | 757 | 253 | 60618 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.5 | 1155 | 0 | 1133 | 253 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.5 | 1155 | 0 | 1133 | 187 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.5 | 1155 | 0.5 | 1133 | 253 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.5 | 1155 | 0.5 | 1133 | 187 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.9 | 1155 | 0 | 1133 | 253 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.9 | 1155 | 0 | 1133 | 187 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.9 | 1155 | 0.5 | 1133 | 253 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.9 | 1155 | 0.5 | 1133 | 187 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.9 | 1155 | 0 | 1133 | 253 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.9 | 1155 | 0 | 1133 | 187 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | residue | 0.9 | 1155 | 0.5 | 1133 | 253 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
| 47 | column_residue | 0.9 | 1155 | 0.5 | 1133 | 187 | 94478 | `NeedsFormalUnitCompatibilityOrCleanKLS` |
