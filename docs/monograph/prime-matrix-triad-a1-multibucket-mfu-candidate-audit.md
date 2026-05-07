# Triad-A1 多桶 MFU 候选审计

**状态：** `finite_layer_mfu_candidate_rows_materialized`

当前 forced 多桶暴露矩阵均存在有限层 phase-bucket 相关候选行；这给出了 MFU-1 的候选输入，但还未证明实际支付图 Gamma 持久落在这些行上。下一步是 ActualPaymentStitching：持久则 PDEC，不持久则 CleanKLS/DLS。

## 1. 结构律

Finite-layer phase-bucket correlation is a candidate compatibility row, not a proof of actual payment. If actual payment follows a correlated row persistently, it becomes a multi-bucket formal unit and must enter PDEC. If actual payment avoids every persistent finite signature, it is DistributedPayment and enters CleanKLS/DLS.

```text
I(phase;bucket)>0
  => finite-layer correlated bucket row；
actual payment 持久跟随该 row
  => multi-bucket formal unit / PDEC；
actual payment 不持久跟随任何 finite row
  => DistributedPayment / CleanKLS-DLS。
```

## 2. 汇总

- `forced_cap_count=24`。
- `matrix_row_count=48`。
- `route_counts={'FiniteLayerMFUCandidateNeedsActualPaymentStitching': 48}`。
- `all_rows_have_finite_layer_correlation=True`。

## 3. Bucket 类型汇总

| bucket kind | rows | min MI | max MI | min normalized MI | max normalized MI | max pairs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| residue | 24 | 1.22721 | 1.26555 | 0.221783 | 0.236679 | 125486 |
| column_residue | 24 | 0.955803 | 1.24288 | 0.182715 | 0.23244 | 125486 |

## 4. Cap 明细

| P | kind | alpha | h | dir | phases | buckets | pairs | MI | normalized MI | route |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | residue | 0 | 805 | 0.25 | 1077 | 210 | 70520 | 1.26137 | 0.235897 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0 | 805 | 0.25 | 1077 | 210 | 70520 | 1.24277 | 0.232419 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0 | 1505 | 0.75 | 1081 | 210 | 70844 | 1.26137 | 0.235898 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0 | 1505 | 0.75 | 1081 | 210 | 70844 | 1.24288 | 0.23244 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.5 | 805 | 0.25 | 734 | 210 | 47690 | 1.26555 | 0.236679 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.5 | 805 | 0.25 | 734 | 210 | 47690 | 1.2428 | 0.232425 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.5 | 1505 | 0.75 | 734 | 210 | 47690 | 1.26555 | 0.236679 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.5 | 1505 | 0.75 | 734 | 210 | 47690 | 1.2428 | 0.232425 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0 | 770 | 0.5 | 1370 | 210 | 91939 | 1.23997 | 0.231896 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0 | 770 | 0.5 | 1370 | 210 | 91939 | 1.18893 | 0.222349 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0 | 1540 | 0.5 | 1370 | 210 | 91939 | 1.23997 | 0.231896 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0 | 1540 | 0.5 | 1370 | 210 | 91939 | 1.18893 | 0.222349 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.5 | 1155 | 0 | 1025 | 210 | 68790 | 1.24228 | 0.232328 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.5 | 1155 | 0 | 1025 | 154 | 68790 | 0.976839 | 0.193935 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.5 | 1155 | 0.5 | 1025 | 210 | 68790 | 1.24228 | 0.232328 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.5 | 1155 | 0.5 | 1025 | 154 | 68790 | 0.976839 | 0.193935 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.9 | 1155 | 0 | 1025 | 210 | 68790 | 1.24228 | 0.232328 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.9 | 1155 | 0 | 1025 | 154 | 68790 | 0.976839 | 0.193935 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.9 | 1155 | 0.5 | 1025 | 210 | 68790 | 1.24228 | 0.232328 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.9 | 1155 | 0.5 | 1025 | 154 | 68790 | 0.976839 | 0.193935 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.9 | 1155 | 0 | 1025 | 210 | 68790 | 1.24228 | 0.232328 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.9 | 1155 | 0 | 1025 | 154 | 68790 | 0.976839 | 0.193935 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | residue | 0.9 | 1155 | 0.5 | 1025 | 210 | 68790 | 1.24228 | 0.232328 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 43 | column_residue | 0.9 | 1155 | 0.5 | 1025 | 154 | 68790 | 0.976839 | 0.193935 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0 | 665 | 0.25 | 1150 | 253 | 94198 | 1.25046 | 0.225984 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0 | 665 | 0.25 | 1150 | 253 | 94198 | 1.22826 | 0.221973 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0 | 1645 | 0.75 | 1145 | 253 | 93819 | 1.25054 | 0.225999 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0 | 1645 | 0.75 | 1145 | 253 | 93819 | 1.22826 | 0.221973 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0 | 770 | 0.5 | 1512 | 253 | 125486 | 1.23443 | 0.223087 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0 | 770 | 0.5 | 1512 | 253 | 125486 | 1.1677 | 0.211028 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0 | 1540 | 0.5 | 1512 | 253 | 125486 | 1.23443 | 0.223087 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0 | 1540 | 0.5 | 1512 | 253 | 125486 | 1.1677 | 0.211028 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.5 | 1001 | 0.25 | 757 | 253 | 60618 | 1.25497 | 0.226799 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.5 | 1001 | 0.25 | 757 | 253 | 60618 | 1.21639 | 0.219827 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.5 | 1309 | 0.75 | 757 | 253 | 60618 | 1.25497 | 0.226799 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.5 | 1309 | 0.75 | 757 | 253 | 60618 | 1.21639 | 0.219827 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.5 | 1155 | 0 | 1133 | 253 | 94478 | 1.22721 | 0.221783 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.5 | 1155 | 0 | 1133 | 187 | 94478 | 0.955803 | 0.182715 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.5 | 1155 | 0.5 | 1133 | 253 | 94478 | 1.22721 | 0.221783 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.5 | 1155 | 0.5 | 1133 | 187 | 94478 | 0.955803 | 0.182715 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.9 | 1155 | 0 | 1133 | 253 | 94478 | 1.22721 | 0.221783 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.9 | 1155 | 0 | 1133 | 187 | 94478 | 0.955803 | 0.182715 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.9 | 1155 | 0.5 | 1133 | 253 | 94478 | 1.22721 | 0.221783 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.9 | 1155 | 0.5 | 1133 | 187 | 94478 | 0.955803 | 0.182715 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.9 | 1155 | 0 | 1133 | 253 | 94478 | 1.22721 | 0.221783 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.9 | 1155 | 0 | 1133 | 187 | 94478 | 0.955803 | 0.182715 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | residue | 0.9 | 1155 | 0.5 | 1133 | 253 | 94478 | 1.22721 | 0.221783 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |
| 47 | column_residue | 0.9 | 1155 | 0.5 | 1133 | 187 | 94478 | 0.955803 | 0.182715 | `FiniteLayerMFUCandidateNeedsActualPaymentStitching` |

## 5. 读法

这些候选行仍是 exposure 层对象。它们说明可支付图存在有限层相关结构，但不说明实际支付一定使用它。
正式闭合必须补 `ActualPaymentStitching`：

```text
若 Gamma 持久落入某个候选相关行 => MFU/PDEC；
若 Gamma 对所有候选行都不持久 => CleanKLS/DLS。
```
