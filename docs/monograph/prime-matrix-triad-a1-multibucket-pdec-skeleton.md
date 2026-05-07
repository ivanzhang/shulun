# Triad-A1 多桶 PDEC 骨架审计

**状态：** `forcedcap_multibucket_vector_lp_skeleton_materialized`

ForcedCap 的 residue 与 column-residue 多桶向量 LP 骨架已物化；当前每个骨架都复核了旧暴露账本、相位暴露恒等式与单桶排除。下一步可以直接生成 U_CRT^multi/L_PDEC^multi 对偶证书或输出可路由失败。

## 1. 结构律

Multi-bucket PDEC must use variables g_b(t) with bounds 0<=g_b(t)<=E_b(t), sum_b g_b(t)<=M(t), and one total payment row. A failure of U_CRT^multi<L_PDEC^multi must route to SingleBucketReturn, CorrelatedBucketBlock, ColumnTailMissingRow, or DiffuseExtremizer.

```text
g_b(t) >= 0；
g_b(t) <= E_b(t)；
sum_b g_b(t) <= M(t)；
sum_t sum_b g_b(t) = |Gamma_S|。
```

这里不使用固定常数；每个 cap 的桶数下界由自己的 `D/max_b E_b` 给出。

## 2. 汇总

- `forced_cap_count=24`。
- `matrix_row_count=48`。
- `bucket_kinds=['residue', 'column_residue']`。
- `all_existing_exposure_references_match=True`。
- `all_phase_exposure_identities_hold=True`。
- `all_single_bucket_payments_excluded=True`。

## 3. Bucket 类型汇总

| bucket kind | rows | min buckets | max exposure share | min effective support | max variables |
| --- | ---: | ---: | ---: | ---: | ---: |
| residue | 24 | 11 | 0.0959528 | 2.60155 | 125486 |
| column_residue | 24 | 9 | 0.118157 | 2.06339 | 125486 |

## 4. Cap/桶骨架明细

| P | kind | alpha | h | dir | phases | buckets | vars | D | min buckets | max share | eff support | route |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | residue | 0 | 805 | 0.25 | 1077 | 210 | 70520 | 3681774070 | 13 | 0.082822 | 2.82458 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0 | 805 | 0.25 | 1077 | 210 | 70520 | 3681774070 | 11 | 0.0927079 | 2.73303 | `MultiBucketVectorLPReady` |
| 43 | residue | 0 | 1505 | 0.75 | 1081 | 210 | 70844 | 3680568532 | 13 | 0.0828344 | 2.82461 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0 | 1505 | 0.75 | 1081 | 210 | 70844 | 3680568532 | 11 | 0.0929628 | 2.73348 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.5 | 805 | 0.25 | 734 | 210 | 47690 | 2927527528 | 12 | 0.087153 | 2.80794 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.5 | 805 | 0.25 | 734 | 210 | 47690 | 2927527528 | 11 | 0.0953805 | 2.69727 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.5 | 1505 | 0.75 | 734 | 210 | 47690 | 2927527528 | 12 | 0.087153 | 2.80794 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.5 | 1505 | 0.75 | 734 | 210 | 47690 | 2927527528 | 11 | 0.0953805 | 2.69727 | `MultiBucketVectorLPReady` |
| 43 | residue | 0 | 770 | 0.5 | 1370 | 210 | 91939 | 2767127028 | 12 | 0.0887159 | 2.82048 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0 | 770 | 0.5 | 1370 | 210 | 91939 | 2767127028 | 11 | 0.0998313 | 2.61149 | `MultiBucketVectorLPReady` |
| 43 | residue | 0 | 1540 | 0.5 | 1370 | 210 | 91939 | 2767127028 | 12 | 0.0887159 | 2.82048 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0 | 1540 | 0.5 | 1370 | 210 | 91939 | 2767127028 | 11 | 0.0998313 | 2.61149 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.5 | 1155 | 0 | 1025 | 210 | 68790 | 2122220360 | 11 | 0.0914834 | 2.80609 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.5 | 1155 | 0 | 1025 | 154 | 68790 | 2122220360 | 10 | 0.101366 | 2.24067 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.5 | 1155 | 0.5 | 1025 | 210 | 68790 | 2122220360 | 11 | 0.0914834 | 2.80609 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.5 | 1155 | 0.5 | 1025 | 154 | 68790 | 2122220360 | 10 | 0.101366 | 2.24067 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.9 | 1155 | 0 | 1025 | 210 | 68790 | 2122220360 | 11 | 0.0914834 | 2.80609 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.9 | 1155 | 0 | 1025 | 154 | 68790 | 2122220360 | 10 | 0.101366 | 2.24067 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.9 | 1155 | 0.5 | 1025 | 210 | 68790 | 2122220360 | 11 | 0.0914834 | 2.80609 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.9 | 1155 | 0.5 | 1025 | 154 | 68790 | 2122220360 | 10 | 0.101366 | 2.24067 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.9 | 1155 | 0 | 1025 | 210 | 68790 | 2122220360 | 11 | 0.0914834 | 2.80609 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.9 | 1155 | 0 | 1025 | 154 | 68790 | 2122220360 | 10 | 0.101366 | 2.24067 | `MultiBucketVectorLPReady` |
| 43 | residue | 0.9 | 1155 | 0.5 | 1025 | 210 | 68790 | 2122220360 | 11 | 0.0914834 | 2.80609 | `MultiBucketVectorLPReady` |
| 43 | column_residue | 0.9 | 1155 | 0.5 | 1025 | 154 | 68790 | 2122220360 | 10 | 0.101366 | 2.24067 | `MultiBucketVectorLPReady` |
| 47 | residue | 0 | 665 | 0.25 | 1150 | 253 | 94198 | 109225010520 | 11 | 0.0949491 | 2.63004 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0 | 665 | 0.25 | 1150 | 253 | 94198 | 109225010520 | 11 | 0.0997327 | 2.53304 | `MultiBucketVectorLPReady` |
| 47 | residue | 0 | 1645 | 0.75 | 1145 | 253 | 93819 | 108692179512 | 11 | 0.09516 | 2.62952 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0 | 1645 | 0.75 | 1145 | 253 | 93819 | 108692179512 | 10 | 0.10002 | 2.53229 | `MultiBucketVectorLPReady` |
| 47 | residue | 0 | 770 | 0.5 | 1512 | 253 | 125486 | 96599086824 | 11 | 0.0959528 | 2.62719 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0 | 770 | 0.5 | 1512 | 253 | 125486 | 96599086824 | 10 | 0.107084 | 2.4138 | `MultiBucketVectorLPReady` |
| 47 | residue | 0 | 1540 | 0.5 | 1512 | 253 | 125486 | 96599086824 | 11 | 0.0959528 | 2.62719 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0 | 1540 | 0.5 | 1512 | 253 | 125486 | 96599086824 | 10 | 0.107084 | 2.4138 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.5 | 1001 | 0.25 | 757 | 253 | 60618 | 79296544896 | 11 | 0.0923769 | 2.60155 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.5 | 1001 | 0.25 | 757 | 253 | 60618 | 79296544896 | 9 | 0.118157 | 2.44438 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.5 | 1309 | 0.75 | 757 | 253 | 60618 | 79296544896 | 11 | 0.0923769 | 2.60155 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.5 | 1309 | 0.75 | 757 | 253 | 60618 | 79296544896 | 9 | 0.118157 | 2.44438 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.5 | 1155 | 0 | 1133 | 253 | 94478 | 67088446560 | 11 | 0.094961 | 2.61129 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.5 | 1155 | 0 | 1133 | 187 | 94478 | 67088446560 | 10 | 0.100214 | 2.06339 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.5 | 1155 | 0.5 | 1133 | 253 | 94478 | 67088446560 | 11 | 0.094961 | 2.61129 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.5 | 1155 | 0.5 | 1133 | 187 | 94478 | 67088446560 | 10 | 0.100214 | 2.06339 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.9 | 1155 | 0 | 1133 | 253 | 94478 | 67088446560 | 11 | 0.094961 | 2.61129 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.9 | 1155 | 0 | 1133 | 187 | 94478 | 67088446560 | 10 | 0.100214 | 2.06339 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.9 | 1155 | 0.5 | 1133 | 253 | 94478 | 67088446560 | 11 | 0.094961 | 2.61129 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.9 | 1155 | 0.5 | 1133 | 187 | 94478 | 67088446560 | 10 | 0.100214 | 2.06339 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.9 | 1155 | 0 | 1133 | 253 | 94478 | 67088446560 | 11 | 0.094961 | 2.61129 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.9 | 1155 | 0 | 1133 | 187 | 94478 | 67088446560 | 10 | 0.100214 | 2.06339 | `MultiBucketVectorLPReady` |
| 47 | residue | 0.9 | 1155 | 0.5 | 1133 | 253 | 94478 | 67088446560 | 11 | 0.094961 | 2.61129 | `MultiBucketVectorLPReady` |
| 47 | column_residue | 0.9 | 1155 | 0.5 | 1133 | 187 | 94478 | 67088446560 | 10 | 0.100214 | 2.06339 | `MultiBucketVectorLPReady` |

## 5. 失败路由

后续若 `U_CRT^multi<L_PDEC^multi` 失败，失败对象必须输出：

```text
SingleBucketReturn      => 与已排除的单桶支付冲突，或回到单桶 PDEC；
CorrelatedBucketBlock   => 细化为更小 multi-bucket formal unit；
ColumnTailMissingRow    => 补 TailAnchor / ColumnCRT / cofactor 条件行；
DiffuseExtremizer       => CleanKLS/DLS。
```

因此多桶 PDEC 不再是模糊出口，而是一个可继续递归剥离的向量 LP/对偶入口。
