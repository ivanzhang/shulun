# Prime Matrix square-phase root-defect input boundary router

**状态：** `k0_rootdefect_reduced_to_prime_square_endpoint_count_or_pdec_open`

`k=0` 根缺陷现在有精确输入边界：根窗本身可无条件压到 `RootLoad<=sqrt(P)/2`，所以若能证明平方窗素数数 `PrimeWindow>2sqrt(P)`，则自动得到 `PrimeWindow>4*RootLoad` 并排除 k0 分支。但这个平方窗计数输入正处在 `X=P^2` 的 `X^(1/2)` 短区间尺度，通用 `X^0.525` 定理不能给出它；因此当前自足路线仍需证明该特殊素数平方端点计数，或将失败登记并排斥为 RootWindow-PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
root_sqrt_envelope_failure_count=0
exact_root_defect_record_count=3
gt_2sqrt_input_failure_count=251
terminal_k0_branch_count=0
row_column_unconditional_closed=false
```

## 1. 无条件可证部分

根窗长度给出

```text
RootLoad_sign(P) <= root window length <= sqrt(P)/2.
```

因此

```text
4*RootLoad_sign(P) <= 2*sqrt(P).
```

所以以下输入足以关闭 k0 根缺陷：

```text
PrimeWindow_sign(P) > 2*sqrt(P).
```

## 2. 输入边界

| item | value |
| --- | --- |
| sufficient input | For every odd prime P and each sign, PrimeWindow_sign(P)>2*sqrt(P). |
| why sufficient | R0_sign(P)<=sqrt(P)/2, hence 4*R0_sign(P)<=2*sqrt(P). |
| generic short interval gap | Baker-Harman-Pintz X^0.525 gives P^1.05 at X=P^2, not length P. |
| self-contained closure claimed | `false` |

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| combined PrimeWindow | 194541 |
| combined RootLoad | 4932 |
| root sqrt envelope failures | 0 |
| exact root-defect records | 3 |
| >2sqrt input failures | 251 |
| terminal k0 branch count | 0 |
| min margin vs 4RootLoad | -1 |
| min margin vs >2sqrt threshold | -15 |
| max RootLoad | 11 |

## 4. 关键记录

| label | P | side | PrimeWindow | RootLoad | 4RootLoad | >2sqrt threshold | margin vs 4R | margin vs threshold | terminal |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| worst vs 4RootLoad | 13 | plus | 3 | 1 | 4 | 8 | -1 | -5 | `false` |
| worst vs >2sqrt | 137 | plus | 9 | 2 | 8 | 24 | 1 | -15 | `false` |
| max RootLoad | 4273 | plus | 260 | 11 | 44 | 131 | 216 | 129 | `false` |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `rootload_sqrt_envelope` | `closed` | For both signs, the k=0 root-window load satisfies R0_sign(P)<=sqrt(P)/2. |
| `primewindow_gt_2sqrt_closes_k0` | `closed` | If PrimeWindow_sign(P)>2sqrt(P), then PrimeWindow_sign(P)>4R0_sign(P), so the k0 root-defect branch is excluded. |
| `external_0525_not_enough` | `closed_as_boundary` | A generic X^0.525 short-interval theorem gives length P^1.05 at X=P^2 and does not supply the needed length P count. |
| `prime_square_endpoint_count_input` | `open` | A global self-contained closure still needs PrimeWindow_sign(P)>2sqrt(P), or a RootWindow-PDEC exclusion. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RootLoadSqrtEnvelopeClosed` | `true` | `true` | 根窗长度给出 R0<=sqrt(P)/2，因此 4R0<=2sqrt(P)。 | closed |
| `CountGt2SqrtWouldCloseK0Closed` | `true` | `true` | 若平方窗素数数大于 2sqrt(P)，则必然压过 4R0。 | closed |
| `FiniteExactRootDefectOnlySmallNonterminal` | `true` | `false` | 有限扫描 P<=5000 中精确根缺陷只出现在小样本，且没有终端 k0 分支。 | finite evidence only |
| `GenericBHP0525InputSufficient` | `false` | `false` | 通用 X^0.525 短区间输入在 X=P^2 后长于目标窗口，不能关闭本门。 | theta<=1/2 on prime-square endpoints |
| `PrimeSquareEndpointCountGt2SqrtPProved` | `false` | `false` | 当前仓库尚未证明每个素数 P 的 P^2 正负长度 P 窗口中有超过 2sqrt(P) 个素数。 | PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 k0 根缺陷的外部/内部输入边界定清，不关闭全局行/列命题。 | PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC AND KGe1MovingLayerAggregateBoundOrPDEC |

## 7. 下一步

- 主攻：`PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC`。
- 这不是普通 `X^0.525` 短区间输入能给出的结论；若不引入外部新定理，必须继续从 square-phase 覆盖失败中抽取 RootWindow-PDEC/SAE。
- 并行保留：`KGe1MovingLayerAggregateBoundOrPDEC`。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_rootdefect_input_boundary_router.py` | `db1535cfe475c022adef39695891887e06e620dc0f09e4d2ec95b5b3d6a8f928` |
| `experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py` | `9287ea0da760a470634e04dc7304b6a3df43460a5bbea96eeaac8b3a59e0be6c` |
| `data/square-phase-rootdefect-input-boundary-ledger.json` | `6e6aa0d0ec33bffa02b07974c25ab32cda9554d2bc03963a0a69b5fe5cce0ec2` |
