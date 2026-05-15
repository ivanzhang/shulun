# Prime Matrix square-phase no-slot k0 root-window split router

**状态：** `moving_short_prime_cluster_split_into_k0_rootwindow_and_kge1_aggregate_open`

本步把 moving 短区间素数簇分裂为 `k=0` 根窗和 `k>=1` 聚合簇。plus 的 `k=0` 原子精确为 `1<=b<=B_+(P)` 且 `4B(B+1)<=P`；minus 的 `k=0` 原子精确为 `4b^2>P-1` 与 `2b(b+1)<P` 夹出的根窗。若无槽分支真正达到反例压力，则根窗簇或 `k>=1` 聚合簇至少一支承担半阈值。这仍不闭合全局；剩余是分别证明根窗素数簇和 `k>=1` 聚合簇上界，或登记并排斥相应 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
k0_formula_failure_count=0
finite_large_branch_count=0
split_logic_failure_count=0
row_column_unconditional_closed=false
```

## 1. k=0 根窗公式

plus 侧 `k=0` 时，条件化为

```text
1<=b<=B_+(P),  4B_+(P)(B_+(P)+1)<=P.
q in [P-2B_+(P), P-2].
```

minus 侧 `k=0` 时，条件化为

```text
4b^2>P-1,  2b(b+1)<P.
```

因此 `k=0` 是 P 前的根长度素数簇窗口。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| plus PrimeWindow | 97145 |
| minus PrimeWindow | 97396 |
| plus k0 load | 3457 |
| minus k0 load | 1475 |
| plus k>=1 load | 14842 |
| minus k>=1 load | 14420 |
| max plus k0 load | 11 |
| max minus k0 load | 7 |
| max plus k>=1 aggregate | 57 |
| max minus k>=1 aggregate | 52 |

## 3. 最大记录

| branch | P | PrimeWindow | load | atom/window |
| --- | ---: | ---: | ---: | --- |
| `plus k0` | 4273 | 260 | 11 | k=0, b=[1,32], q=[4209,4271] |
| `minus k0` | 4733 | 297 | 7 | k=0, b=[35,48], q=[4637,4663] |
| `plus k>=1` | 4789 | 271 | 57 | aggregate |
| `minus k>=1` | 4639 | 271 | 52 | aggregate |

## 4. 样本表

| P | plus k0 | plus k>=1 | minus k0 | minus k>=1 |
| ---: | ---: | ---: | ---: | ---: |
| 13 | 1 | 0 | 0 | 0 |
| 17 | 0 | 0 | 0 | 0 |
| 19 | 1 | 0 | 0 | 0 |
| 23 | 0 | 0 | 0 | 0 |
| 29 | 0 | 0 | 0 | 0 |
| 31 | 1 | 0 | 0 | 0 |
| 101 | 1 | 0 | 1 | 1 |
| 499 | 3 | 6 | 0 | 6 |
| 1009 | 3 | 14 | 3 | 6 |
| 2003 | 6 | 22 | 2 | 16 |
| 4999 | 11 | 47 | 3 | 43 |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `plus_k0_root_window_formula` | `closed` | The plus k=0 atom is exactly 1<=b<=B_+(P), where 4B(B+1)<=P. |
| `minus_k0_root_window_formula` | `closed` | The minus k=0 atom is exactly B_-(P)<=b<=C_-(P), with 4b^2>P-1 and 2b(b+1)<P. |
| `k0_kge1_split_dichotomy` | `closed` | A threatening no-slot branch forces either the k=0 root-window cluster or the k>=1 moving-layer aggregate to carry half the threshold. |
| `rootwindow_or_kge1_bound` | `open` | A global proof still needs bounds for the k=0 root-window prime cluster and the k>=1 aggregate, or a PDEC/SAE exclusion. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `K0RootWindowFormulaClosed` | `true` | `true` | plus/minus 的 k=0 原子已写成显式根窗。 | closed |
| `K0KGe1SplitDichotomyClosed` | `true` | `true` | 大无槽分支必进入 k=0 根窗簇或 k>=1 聚合簇。 | closed |
| `FiniteNoLargeSplitBranch` | `true` | `false` | 有限扫描 P<=5000 中没有威胁性分支。 | finite evidence only |
| `GlobalK0RootWindowPrimeClusterBound` | `false` | `false` | 仍需证明 P 前 O(sqrt(P)) 根窗中的素数簇不足以承担反例压力。 | K0RootWindowPrimeClusterBoundOrPDEC |
| `GlobalKGe1AggregateBound` | `false` | `false` | 仍需证明 k>=1 moving-layer 聚合簇不足以承担反例压力。 | KGe1MovingLayerAggregateBoundOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只分裂短区间素数簇，不关闭全局行/列命题。 | K0RootWindowPrimeClusterBoundAndKGe1MovingLayerAggregateBoundOrPDEC |

## 7. 下一步

- 主攻：`K0RootWindowPrimeClusterBoundOrPDEC`。
- 备选：`KGe1MovingLayerAggregateBoundOrPDEC`。
- 当前仍未证明全局闭合；只是把短区间簇拆成根窗簇与非零层聚合簇两个更小目标。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-noslot-k0-rootwindow-split-ledger.json` | `21ee5e1268f238bde4a68afcc64cb881720b309e9e6ade10739eefdd38409515` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
