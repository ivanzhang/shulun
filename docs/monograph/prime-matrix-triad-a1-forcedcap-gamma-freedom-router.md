# Triad-A1 ForcedCap Gamma 自由度路由器

**状态：** `forcedcap_gamma_freedom_bounded_by_fiber_redundancy`

ForcedCap 的实际支付图 Gamma 已被 fiber 冗余强约束：当前最多约 5.53% 的洞有选择自由，至少约 94.47% 的支付边在每个完成态中被唯一覆盖强制决定。

## 1. 结构律

For each completion-hole pair let k>=1 be the number of high-prime cover edges. Only k>=2 pairs are choice-ambiguous. Since sum(k-1)=cover_incidence-demand, the ambiguous share is at most cover_over_demand-1, and the forced share is at least 2-cover_over_demand.

```text
D = completion-hole demand；
C = fiber-consistent cover incidence = sum k；
ambiguous_pairs <= C-D；
ambiguous_share <= C/D - 1；
forced_share >= 2 - C/D。
```

这一步不需要枚举实际支付选择；它只用同一 fiber 完成态的冗余覆盖数给出 Gamma 自由度上界。

## 2. 汇总

- `forced_cap_count=24`。
- `all_completion_counts_match_m_vector=True`。
- `global_max_ambiguous_gamma_share_upper_bound=0.0552843`。
- `global_min_forced_gamma_share_lower_bound=0.944716`。

## 3. Cap 明细

| P | alpha | h | dir | cover/demand | ambiguous upper | forced lower | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 0 | 805 | 0.25 | 1.04174 | 0.0417363 | 0.958264 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0 | 1505 | 0.75 | 1.04174 | 0.0417441 | 0.958256 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.5 | 805 | 0.25 | 1.04206 | 0.0420589 | 0.957941 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.5 | 1505 | 0.75 | 1.04206 | 0.0420589 | 0.957941 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0 | 770 | 0.5 | 1.03973 | 0.0397255 | 0.960275 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0 | 1540 | 0.5 | 1.03973 | 0.0397255 | 0.960275 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.5 | 1155 | 0 | 1.0395 | 0.0394953 | 0.960505 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.5 | 1155 | 0.5 | 1.0395 | 0.0394953 | 0.960505 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 1.0395 | 0.0394953 | 0.960505 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 1.0395 | 0.0394953 | 0.960505 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 1.0395 | 0.0394953 | 0.960505 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 1.0395 | 0.0394953 | 0.960505 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0 | 665 | 0.25 | 1.05521 | 0.0552063 | 0.944794 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0 | 1645 | 0.75 | 1.05528 | 0.0552843 | 0.944716 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0 | 770 | 0.5 | 1.05227 | 0.0522676 | 0.947732 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0 | 1540 | 0.5 | 1.05227 | 0.0522676 | 0.947732 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.5 | 1001 | 0.25 | 1.05459 | 0.0545949 | 0.945405 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.5 | 1309 | 0.75 | 1.05459 | 0.0545949 | 0.945405 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.5 | 1155 | 0 | 1.05198 | 0.0519819 | 0.948018 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.5 | 1155 | 0.5 | 1.05198 | 0.0519819 | 0.948018 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 1.05198 | 0.0519819 | 0.948018 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 1.05198 | 0.0519819 | 0.948018 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 1.05198 | 0.0519819 | 0.948018 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 1.05198 | 0.0519819 | 0.948018 | `GammaMostlyForcedMFUOrSmallAmbiguousCleanKLS` |
