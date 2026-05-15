# Prime Matrix square-phase k0 root-window defect router

**状态：** `k0_rootwindow_branch_reduced_to_squarewindow_root_defect_open`

本步没有换命题，而是把 `K0RootWindowPrimeClusterBoundOrPDEC` 精确压缩：若 k=0 根窗分支能承担 split 半阈值，则平方窗素数数必须满足 `PrimeWindow<=4*RootLoad`。其中 RootLoad 是 P 前显式根窗内的素数数。因此 k0 分支的全局排除等价于证明平方窗素数数始终压过该根窗负载四倍，或把持久违反者登记并排斥为 RootWindow-PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
root_load_length_envelope_failure_count=0
exact_defect_implication_failure_count=0
k0_large_branch_count=3
terminal_k0_branch_count=0
row_column_unconditional_closed=false
```

## 1. 精确压缩

设 `W_sign(P)` 为 `P^2` 正负半窗内的素数数，`R0_sign(P)` 为 `k=0` 根窗内的尾素数。split 判据中的 k0 大分支是

```text
2*R0_sign(P) >= ceil(W_sign(P)/2).
```

因此必有

```text
W_sign(P) <= 4*R0_sign(P).
```

这说明 k0 分支若真成为终端反例，只能表现为平方窗素数数相对于 P 前根窗素数数的根缺陷。

## 2. 根窗公式

plus 侧：

```text
1<=b<=B_+(P),  4B_+(P)(B_+(P)+1)<=P,
q=P-2b.
```

minus 侧：

```text
4b^2>P-1,  2b(b+1)<P,
q=P-2b.
```

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| combined PrimeWindow | 194541 |
| combined RootLoad | 4932 |
| combined no-slot load | 34194 |
| k0 large branch count | 3 |
| terminal k0 branch count | 0 |
| exact root-defect record count | 3 |
| length root-defect record count | 111 |
| max root load | 11 |
| min exact root ratio | 0.75 |
| min length root ratio | 0.25 |

## 4. 关键记录

| label | P | side | PrimeWindow | RootLoad | b interval | q interval | ratio | terminal |
| --- | ---: | --- | ---: | ---: | --- | --- | ---: | --- |
| max RootLoad | 4273 | plus | 260 | 11 | [1, 32] | [4209, 4271] | 5.909091 | `false` |
| min W/(4R0) | 13 | plus | 3 | 1 | [1, 1] | [11, 11] | 0.750000 | `false` |
| min W/(4Len) | 17 | plus | 1 | 0 | [1, 1] | [15, 15] | 0.250000 | `false` |

## 5. k0 大分支样本

| P | side | PrimeWindow | RootLoad | b interval | q interval | no-slot | terminal |
| ---: | --- | ---: | ---: | --- | --- | ---: | --- |
| 13 | plus | 3 | 1 | [1, 1] | [11, 11] | 1 | `false` |
| 19 | plus | 3 | 1 | [1, 1] | [17, 17] | 1 | `false` |
| 73 | plus | 7 | 2 | [1, 3] | [67, 71] | 3 | `false` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `k0_rootwindow_exact_load` | `closed` | The k=0 branch load is exactly the prime count in the explicit root window below P. |
| `k0_large_forces_squarewindow_root_defect` | `closed` | If the k=0 branch carries the split threshold, then PrimeWindow<=4*RootLoad. |
| `k0_terminal_branch_reduction` | `closed` | A terminal no-slot counterexample using k=0 must therefore be a square-window root-defect event. |
| `squarewindow_root_defect_exclusion` | `open` | A global proof still needs PrimeWindow>4*RootLoad, or a PDEC/SAE exclusion of persistent root-defect events. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `K0RootWindowExactLoadClosed` | `true` | `true` | k=0 根窗负载被精确写成 P 前根窗内的素数计数。 | closed |
| `K0LargeImpliesSquareWindowRootDefectClosed` | `true` | `true` | 若 k0 分支承担半阈值，则 PrimeWindow<=4*RootLoad。 | closed |
| `FiniteNoTerminalK0Branch` | `true` | `false` | 有限扫描 P<=5000 未出现终端 k0 分支。 | finite evidence only |
| `SquareWindowRootDefectExcludedGlobally` | `false` | `false` | 仍需全局证明平方窗素数数压过根窗负载四倍，或排斥持久根缺陷。 | SquareWindowRootDefectLowerBoundOrRootWindowPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭 k0 分支的必要缺陷形态，不关闭全局行/列命题。 | SquareWindowRootDefectLowerBoundOrRootWindowPDEC AND KGe1MovingLayerAggregateBoundOrPDEC |

## 8. 下一步

- 主攻：`SquareWindowRootDefectLowerBoundOrRootWindowPDEC`，即证明 `W_sign(P)>4R0_sign(P)` 或排斥持久根缺陷。
- 并行剩余：`KGe1MovingLayerAggregateBoundOrPDEC`。
- 当前仍未证明全局行/列无条件闭合；本步只关闭 k0 分支的必要缺陷形态。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py` | `9287ea0da760a470634e04dc7304b6a3df43460a5bbea96eeaac8b3a59e0be6c` |
| `data/square-phase-k0-rootwindow-defect-ledger.json` | `5ebb18020b86ff990141bea12cf29745e1d29dee888164772e0f2de8d31a3a95` |
