# Triad-A1 ForcedCap 暴露支配路由器

**状态：** `forcedcap_actual_payment_dominated_by_exposure`

ForcedCap 的实际 column-tail 支付受暴露账本支配；当前全部 24 个 forced cap 都排除了单 residue 与单 column-residue 承担全部需求。剩余只能是多桶持久 PDEC 或分散 CleanKLS/DLS。

## 1. 结构律

Actual payment in a bucket is bounded above by its exposure. Therefore a cap with demand D and max bucket exposure E must use at least ceil(D/E) buckets, unless it routes to a persistent multi-bucket PDEC formal unit.

```text
actual_payment(bucket) <= exposure(bucket)；
D_C <= sum actual_payment(bucket)；
therefore bucket_count >= ceil(D_C / max_exposure)。
```

这不是固定常数判据；每个 cap 使用自己的 `D_C/max_exposure` 动态下界。

## 2. 汇总

- `forced_cap_count=24`。
- `route_counts={'MultiBucketPDECOrDistributedCleanKLS': 24}`。
- `all_single_residue_actual_payment_excluded=True`。
- `all_single_column_residue_actual_payment_excluded=True`。
- `global_min_actual_residue_buckets_by_exposure=11`。
- `global_min_actual_column_residue_buckets_by_exposure=9`。
- `global_max_residue_exposure_share=0.0959528`。
- `global_max_column_residue_exposure_share=0.118157`。

## 3. P 级汇总

| P | caps | min actual residue buckets | min actual colres buckets | max residue exposure share | max colres exposure share |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | 12 | 11 | 10 | 0.0914834 | 0.101366 |
| 47 | 12 | 11 | 9 | 0.0959528 | 0.118157 |

## 4. Cap 明细

| P | alpha | h | dir | D | min residue buckets | min colres buckets | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 0 | 805 | 0.25 | 3681774070 | 13 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0 | 1505 | 0.75 | 3680568532 | 13 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.5 | 805 | 0.25 | 2927527528 | 12 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.5 | 1505 | 0.75 | 2927527528 | 12 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0 | 770 | 0.5 | 2767127028 | 12 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0 | 1540 | 0.5 | 2767127028 | 12 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.5 | 1155 | 0 | 2122220360 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.5 | 1155 | 0.5 | 2122220360 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 2122220360 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 2122220360 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 2122220360 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 2122220360 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0 | 665 | 0.25 | 109225010520 | 11 | 11 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0 | 1645 | 0.75 | 108692179512 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0 | 770 | 0.5 | 96599086824 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0 | 1540 | 0.5 | 96599086824 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1001 | 0.25 | 79296544896 | 11 | 9 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1309 | 0.75 | 79296544896 | 11 | 9 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1155 | 0 | 67088446560 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1155 | 0.5 | 67088446560 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 67088446560 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 67088446560 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 67088446560 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 67088446560 | 11 | 10 | `MultiBucketPDECOrDistributedCleanKLS` |

## 5. 读法

这一步把 `暴露签名` 升级成实际支付的上界约束。
若某个实际支付签名持久承担需求，它必须是一组多桶 formal unit，而不是单 residue/单 column-residue。
若没有这样的持久多桶集合，则 forced cap 的支付只能分散，进入 CleanKLS/DLS。
