# Prime Matrix square-phase off-band prefix gap shadow gap cell router

**状态：** `support_collapse_reduced_to_simultaneous_gap_cell_void_open`

本步把支撑塌缩 PDEC 精确切成 gap cells：wheel-17 survivor 是允许落素数的穿孔点，其余 hull 奇候选分成若干连续 cell；支撑塌缩等价于所有这些 cells 同时 prime-void。有限账本中每个包至少有一个非空 cell，因此 all-cells-void 包数为 0；全局仍需证明每个固定小 k 包至少一个显式 cell 含素数，或排斥 simultaneous cell void PDEC。

```text
packet_count=11
gap_cell_count=29
all_cells_void_packet_count=0
min_nonvoid_cells_per_packet=1
min_escape_primes_per_packet=1
max_gap_cell_candidate_count=14
row_column_unconditional_closed=false
```

## 1. gap-cell 等价

对每个支撑塌缩包，删除 wheel-17 survivor 后，hull 中剩余奇候选自动分成若干连续 gap cells。
支撑塌缩等价于：

```text
every gap cell is prime-void
```

因此任一 gap cell 含素数，就立即排除该包。

## 2. 最紧包前沿

| P | side | hull | survivors | cells | nonvoid cells | escape primes | largest cell |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 523 | `plus` | `485-501` | `[487, 491]` | 3 | 1 | 1 | 5 |
| 683 | `plus` | `639-657` | `[641, 643, 647]` | 3 | 1 | 1 | 5 |
| 691 | `minus` | `649-665` | `[659, 661]` | 2 | 1 | 1 | 5 |
| 733 | `plus` | `675-687` | `[677]` | 2 | 1 | 1 | 5 |
| 733 | `plus` | `675-705` | `[677, 683, 691]` | 4 | 1 | 1 | 7 |
| 673 | `minus` | `619-637` | `[]` | 1 | 1 | 2 | 10 |
| 313 | `plus` | `273-295` | `[277]` | 2 | 1 | 3 | 9 |
| 733 | `plus` | `681-705` | `[691]` | 2 | 2 | 2 | 7 |
| 673 | `minus` | `619-671` | `[631, 641, 643, 647]` | 4 | 2 | 4 | 12 |
| 691 | `minus` | `649-689` | `[659, 661]` | 2 | 2 | 4 | 14 |
| 1129 | `plus` | `1051-1095` | `[1061, 1063, 1073, 1081]` | 4 | 3 | 5 | 7 |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `support_collapse_to_gap_cells` | `closed` | A support-collapse packet is exactly the simultaneous prime-void condition on all non-survivor gap cells. |
| `single_cell_prime_supply_excludes_packet` | `closed` | If any gap cell contains a prime, the corresponding support-collapse packet is impossible. |
| `finite_no_all_cells_void` | `finite_evidence` | The finite audit finds at least one non-void gap cell in every packet. |
| `global_single_gap_cell_prime_supply` | `open` | A global proof still needs a prime in at least one explicit gap cell for every fixed small-k packet, or exclusion of simultaneous cell void. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `GapCellDecompositionClosed` | `true` | `true` | 支撑塌缩已等价为所有非幸存 gap cells 同时 prime-void。 | closed |
| `SingleCellPrimeSupplyCriterionClosed` | `true` | `true` | 任一 gap cell 含素数即可排除对应塌缩包。 | closed |
| `FiniteNoAllCellsVoid` | `true` | `false` | 有限前沿中没有所有 cells 同时空的包。 | finite evidence only |
| `GlobalGapCellPrimeSupplyClosed` | `false` | `false` | 仍需全局证明每个固定小 k 包至少一个 cell 含素数。 | SingleGapCellPrimeSupplyOrSimultaneousGapCellVoidPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 PDEC 的 gap-cell 分解，不关闭全局行/列命题。 | SingleGapCellPrimeSupplyOrSimultaneousGapCellVoidPDEC |

## 5. 下一步

- 主攻：`SingleGapCellPrimeSupplyOrSimultaneousGapCellVoidPDEC`。
- 优先挑选每个包中最短且结构最稳定的非幸存 cell，证明其含素数或接入列相位矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router.py` | `b563bc3b9c01bc7f2eb8034067e5b91c17ee775f48aa01c5f4fd666ce561c23b` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py` | `69b61f3820afc3daa860fd3ac612bb78d8a3635e89aea87a2b8dafaf2bc5e273` |
| `data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json` | `221c23d9062defd07903b63b15e284ddd4f86693640f512aa6818c6abda95594` |
| `data/square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json` | `ac04a88489870922cb63f322e7515657d8762ec5fb4af58e7040c498512cedce` |
