# Triad-A1 ForcedCap Fiber 支配路由器

**状态：** `forcedcap_actual_payment_dominated_by_fiber_consistent_incidence`

加入同一 fiber y 的一致性后，ForcedCap 的单 residue 与单 column-residue 支付被更强地排除；当前实际支付至少需要 42 个 residue bucket 或 24 个 column-residue bucket。

## 1. 结构律

Actual payment edges are a subset of the cover edges induced by fiber-consistent completions. Therefore ActualPayment(bucket)<=FiberConsistentCover(bucket), and every cap needs at least ceil(D/max_bucket_fiber_cover) buckets.

```text
ActualPayment(bucket) <= FiberConsistentCover(bucket)；
D_C <= sum ActualPayment(bucket)；
bucket_count >= ceil(D_C / max FiberConsistentCover)。
```

## 2. 汇总

- `forced_cap_count=24`。
- `route_counts={'FiberDominatedMultiBucketPDECOrCleanKLS': 24}`。
- `all_single_residue_payment_excluded_by_fiber=True`。
- `all_single_column_residue_payment_excluded_by_fiber=True`。
- `global_min_actual_residue_buckets_by_fiber=42`。
- `global_min_actual_column_residue_buckets_by_fiber=24`。
- `global_max_residue_fiber_cover_share=0.0240372`。
- `global_max_column_residue_fiber_cover_share=0.0433302`。

## 3. Cap 明细

| P | alpha | h | dir | D | min residue buckets | min colres buckets | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 0 | 805 | 0.25 | 3681774070 | 55 | 48 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0 | 1505 | 0.75 | 3680568532 | 55 | 48 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.5 | 805 | 0.25 | 2927527528 | 52 | 42 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.5 | 1505 | 0.75 | 2927527528 | 52 | 42 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0 | 770 | 0.5 | 2767127028 | 53 | 37 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0 | 1540 | 0.5 | 2767127028 | 53 | 37 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.5 | 1155 | 0 | 2122220360 | 48 | 39 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.5 | 1155 | 0.5 | 2122220360 | 48 | 39 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 2122220360 | 48 | 39 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 2122220360 | 48 | 39 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 2122220360 | 48 | 39 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 2122220360 | 48 | 39 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0 | 665 | 0.25 | 109225010520 | 46 | 33 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0 | 1645 | 0.75 | 108692179512 | 45 | 33 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0 | 770 | 0.5 | 96599086824 | 42 | 30 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0 | 1540 | 0.5 | 96599086824 | 42 | 30 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.5 | 1001 | 0.25 | 79296544896 | 48 | 24 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.5 | 1309 | 0.75 | 79296544896 | 48 | 24 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.5 | 1155 | 0 | 67088446560 | 43 | 34 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.5 | 1155 | 0.5 | 67088446560 | 43 | 34 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 67088446560 | 43 | 34 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 67088446560 | 43 | 34 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 67088446560 | 43 | 34 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 67088446560 | 43 | 34 | `FiberDominatedMultiBucketPDECOrCleanKLS` |
