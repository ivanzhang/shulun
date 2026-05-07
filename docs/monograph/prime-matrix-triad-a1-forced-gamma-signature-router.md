# Triad-A1 Forced Gamma 签名路由器

**状态：** `forced_gamma_signature_pressure_materialized`

ForcedCap 的 Gamma 自由度已压到小预算后，48 个有限层 phase-bucket 签名行全部满足 `signature_signal > ambiguous_budget`。因此下一步不再是寻找新的 exposure 统计，而是证明实际 Gamma 若持久命中这些签名则进入 PDEC；若不持久，则小 ambiguous 分散残余进入 CleanKLS/DLS。

## 1. 结构律

写 Gamma=Gamma_forced union Gamma_amb，且 Gamma_amb 的质量至多为 aD。任何超过 a 预算的持久有限签名都不能纯由选择自由解释，其持久部分必须来自 forced fiber 主体，于是路由到 MFU/PDEC。若没有有限签名在 a 预算以上持久，则剩余责任是小自由度、多桶、分散的，准入 CleanKLS/DLS。

```text
Gamma = Gamma_forced union Gamma_amb；
|Gamma_amb| <= aD；
persistent finite signature mass > aD
  => 不能只由 ambiguous choice 解释，必须含 forced fiber 主体，进入 MFU/PDEC；
no persistent finite signature above aD
  => 小 ambiguous 多桶分散，进入 CleanKLS/DLS。
```

## 2. 汇总

- `forced_cap_count=24`。
- `signature_matrix_row_count=48`。
- `missing_key_count=0`。
- `route_counts={'ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission': 48}`。
- `all_rows_routed_to_forced_signature_or_small_ambiguous_clean=True`。
- `global_max_ambiguous_gamma_share_upper_bound=0.0552843`。
- `global_min_forced_gamma_share_lower_bound=0.944716`。
- `global_min_signature_signal_minus_ambiguous_budget=0.130733`。
- `global_min_signature_signal_to_ambiguity_ratio=3.51497`。
- `global_min_ambiguous_escape_bucket_lower_bound=2`。

## 3. Bucket 类型汇总

| bucket kind | rows | min signal | max ambiguous | min margin | min ratio | min fiber buckets |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| column_residue | 24 | 0.182715 | 0.0552843 | 0.130733 | 3.51497 | 24 |
| residue | 24 | 0.221783 | 0.0552843 | 0.169801 | 4.08794 | 42 |

## 4. 行明细

| P | alpha | h | dir | kind | signal | ambiguous | margin | ratio | fiber buckets | route |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 0 | 805 | 0.25 | residue | 0.235897 | 0.0417363 | 0.194161 | 5.65208 | 55 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 805 | 0.25 | column_residue | 0.232419 | 0.0417363 | 0.190682 | 5.56874 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 1505 | 0.75 | residue | 0.235898 | 0.0417441 | 0.194154 | 5.65106 | 55 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 1505 | 0.75 | column_residue | 0.23244 | 0.0417441 | 0.190696 | 5.56821 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 805 | 0.25 | residue | 0.236679 | 0.0420589 | 0.19462 | 5.62732 | 52 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 805 | 0.25 | column_residue | 0.232425 | 0.0420589 | 0.190366 | 5.52618 | 42 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 1505 | 0.75 | residue | 0.236679 | 0.0420589 | 0.19462 | 5.62732 | 52 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 1505 | 0.75 | column_residue | 0.232425 | 0.0420589 | 0.190366 | 5.52618 | 42 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 770 | 0.5 | residue | 0.231896 | 0.0397255 | 0.19217 | 5.83746 | 53 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 770 | 0.5 | column_residue | 0.222349 | 0.0397255 | 0.182624 | 5.59715 | 37 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 1540 | 0.5 | residue | 0.231896 | 0.0397255 | 0.19217 | 5.83746 | 53 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0 | 1540 | 0.5 | column_residue | 0.222349 | 0.0397255 | 0.182624 | 5.59715 | 37 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 1155 | 0 | residue | 0.232328 | 0.0394953 | 0.192833 | 5.88242 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 1155 | 0 | column_residue | 0.193935 | 0.0394953 | 0.154439 | 4.91031 | 39 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 1155 | 0.5 | residue | 0.232328 | 0.0394953 | 0.192833 | 5.88242 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.5 | 1155 | 0.5 | column_residue | 0.193935 | 0.0394953 | 0.154439 | 4.91031 | 39 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0 | residue | 0.232328 | 0.0394953 | 0.192833 | 5.88242 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0 | column_residue | 0.193935 | 0.0394953 | 0.154439 | 4.91031 | 39 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0.5 | residue | 0.232328 | 0.0394953 | 0.192833 | 5.88242 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0.5 | column_residue | 0.193935 | 0.0394953 | 0.154439 | 4.91031 | 39 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0 | residue | 0.232328 | 0.0394953 | 0.192833 | 5.88242 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0 | column_residue | 0.193935 | 0.0394953 | 0.154439 | 4.91031 | 39 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0.5 | residue | 0.232328 | 0.0394953 | 0.192833 | 5.88242 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 43 | 0.9 | 1155 | 0.5 | column_residue | 0.193935 | 0.0394953 | 0.154439 | 4.91031 | 39 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 665 | 0.25 | residue | 0.225984 | 0.0552063 | 0.170778 | 4.09345 | 46 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 665 | 0.25 | column_residue | 0.221973 | 0.0552063 | 0.166767 | 4.02079 | 33 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 1645 | 0.75 | residue | 0.225999 | 0.0552843 | 0.170715 | 4.08794 | 45 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 1645 | 0.75 | column_residue | 0.221973 | 0.0552843 | 0.166689 | 4.01512 | 33 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 770 | 0.5 | residue | 0.223087 | 0.0522676 | 0.17082 | 4.26817 | 42 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 770 | 0.5 | column_residue | 0.211028 | 0.0522676 | 0.158761 | 4.03745 | 30 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 1540 | 0.5 | residue | 0.223087 | 0.0522676 | 0.17082 | 4.26817 | 42 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0 | 1540 | 0.5 | column_residue | 0.211028 | 0.0522676 | 0.158761 | 4.03745 | 30 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1001 | 0.25 | residue | 0.226799 | 0.0545949 | 0.172204 | 4.15422 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1001 | 0.25 | column_residue | 0.219827 | 0.0545949 | 0.165232 | 4.02652 | 24 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1309 | 0.75 | residue | 0.226799 | 0.0545949 | 0.172204 | 4.15422 | 48 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1309 | 0.75 | column_residue | 0.219827 | 0.0545949 | 0.165232 | 4.02652 | 24 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1155 | 0 | residue | 0.221783 | 0.0519819 | 0.169801 | 4.26654 | 43 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1155 | 0 | column_residue | 0.182715 | 0.0519819 | 0.130733 | 3.51497 | 34 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1155 | 0.5 | residue | 0.221783 | 0.0519819 | 0.169801 | 4.26654 | 43 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.5 | 1155 | 0.5 | column_residue | 0.182715 | 0.0519819 | 0.130733 | 3.51497 | 34 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0 | residue | 0.221783 | 0.0519819 | 0.169801 | 4.26654 | 43 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0 | column_residue | 0.182715 | 0.0519819 | 0.130733 | 3.51497 | 34 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0.5 | residue | 0.221783 | 0.0519819 | 0.169801 | 4.26654 | 43 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0.5 | column_residue | 0.182715 | 0.0519819 | 0.130733 | 3.51497 | 34 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0 | residue | 0.221783 | 0.0519819 | 0.169801 | 4.26654 | 43 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0 | column_residue | 0.182715 | 0.0519819 | 0.130733 | 3.51497 | 34 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0.5 | residue | 0.221783 | 0.0519819 | 0.169801 | 4.26654 | 43 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
| 47 | 0.9 | 1155 | 0.5 | column_residue | 0.182715 | 0.0519819 | 0.130733 | 3.51497 | 34 | `ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission` |
