# Prime Matrix square-phase k>=1 aggregate pressure router

**状态：** `kge1_aggregate_branch_reduced_to_squarewindow_pressure_defect_open`

本步把 `KGe1MovingLayerAggregateBoundOrPDEC` 精确压成压力缺陷：若 k>=1 聚合分支承担 split 半阈值，则必有 `PrimeWindow<=4*KGe1Load`。`KGe1Load` 仍是显式 moving-layer 原子上的素数负载，并受 b 轴无槽支撑点数控制。有限审计只出现一个压力样本且不是终端 no-slot 分支；全局仍需排斥持久聚合压力缺陷。

```text
max_p=5000
finite_prime_count=668
support_envelope_failure_count=0
pressure_implication_failure_count=0
kge1_pressure_branch_count=1
terminal_kge1_branch_count=0
row_column_unconditional_closed=false
```

## 1. 精确压缩

设 `K1_sign(P)` 为所有 `k>=1` moving-layer 原子上的 prime-load 聚合。若该分支承担 split 半阈值，则

```text
2*K1_sign(P) >= ceil(PrimeWindow_sign(P)/2),
```

从而必有

```text
PrimeWindow_sign(P) <= 4*K1_sign(P).
```

因此 k>=1 分支的终端反例必须是平方窗素数数相对 moving-layer 聚合负载过小的压力缺陷。

## 2. 支撑包络

`K1_sign(P)` 只计入满足 k>=1 无槽二次相位不等式且 `q=P-2b` 为素数的 b；因此

```text
K1_sign(P) <= #{b: k(b)>=1 and b lies in the sign no-slot support}.
```

这个包络无条件正确，但单靠它仍不足以全局闭合，需要更细的素数负载界或 PDEC 排斥。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| combined PrimeWindow | 194541 |
| combined KGe1Load | 29262 |
| combined support b count | 116282 |
| support envelope failures | 0 |
| pressure implication failures | 0 |
| k>=1 pressure branch count | 1 |
| terminal k>=1 branch count | 0 |
| min margin vs 4KGe1 | -4 |
| min margin vs support | -524 |
| max KGe1Load | 57 |
| max support density in tail b | 0.421505376344086 |

## 4. 关键记录

| label | P | side | PrimeWindow | KGe1 | support | no-slot | margin vs 4K | terminal |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| worst vs 4KGe1 | 523 | plus | 36 | 10 | 18 | 13 | -4 | `false` |
| worst vs support | 4877 | plus | 276 | 48 | 200 | 53 | 84 | `false` |
| max KGe1 | 4789 | plus | 271 | 57 | 194 | 65 | 43 | `false` |
| max support density | 4651 | plus | 264 | 42 | 196 | 50 | 96 | `false` |

## 5. 压力样本

| P | side | PrimeWindow | KGe1 | K0 | no-slot | support | terminal |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 523 | plus | 36 | 10 | 3 | 13 | 18 | `false` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `kge1_aggregate_exact_load` | `closed` | The k>=1 branch load is exactly the aggregate prime-load over all nonzero moving layers. |
| `kge1_load_support_envelope` | `closed` | The k>=1 prime-load is bounded by its explicit b-axis no-slot support count. |
| `kge1_pressure_forces_squarewindow_defect` | `closed` | If the k>=1 branch carries the split threshold, then PrimeWindow<=4*KGe1Load. |
| `kge1_pressure_defect_exclusion` | `open` | A global proof still needs PrimeWindow>4*KGe1Load, or a MovingLayer-PDEC exclusion of persistent aggregate pressure. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `KGe1AggregateLoadClosed` | `true` | `true` | k>=1 聚合负载由上一层 moving layer 原子精确给出。 | closed |
| `KGe1SupportEnvelopeClosed` | `true` | `true` | k>=1 prime-load 不超过显式 b 支撑点数。 | closed |
| `KGe1PressureImpliesSquareWindowDefectClosed` | `true` | `true` | 若 k>=1 分支承担半阈值，则 PrimeWindow<=4*KGe1Load。 | closed |
| `FiniteNoTerminalKGe1Branch` | `true` | `false` | 有限扫描 P<=5000 未出现终端 k>=1 分支。 | finite evidence only |
| `KGe1AggregatePressureDefectExcludedGlobally` | `false` | `false` | 仍需证明平方窗素数数压过 k>=1 聚合负载四倍，或排斥持久 moving-layer 聚合压力缺陷。 | KGe1AggregatePressureDefectOrMovingLayerPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 k>=1 分支压成压力缺陷，不关闭全局行/列命题。 | PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC AND KGe1AggregatePressureDefectOrMovingLayerPDEC |

## 8. 下一步

- 主攻：`KGe1AggregatePressureDefectOrMovingLayerPDEC`。
- 与 k0 分支并行，最终还需 `PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC` 或更精细的平方窗/聚合负载比较。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_kge1_aggregate_pressure_router.py` | `c558428051e1c6e60d51944ac249c6646f7b06e8ef453f7e8ef2abaeb2000d2e` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `data/square-phase-kge1-aggregate-pressure-ledger.json` | `ed24820d474b1c6792808feb64cbdbfa5f870c60b3e2cf8c952a3f19723e6824` |
