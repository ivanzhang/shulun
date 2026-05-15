# Prime Matrix square-phase no-slot phase layer router

**状态：** `noslot_phase_band_reduced_to_floor_layer_bound_or_pdec_open`

本步把无槽尾素分支压成同一个二次相位的 floor-layer 问题。对 `q=P-2b` 有 `2b^2≡P^2/2 (mod q)`；写 `2b^2=kq+s` 后，plus 无槽等价于 `s<q-(P-1)/2`，minus 无槽等价于 `s>(P-1)/2`。因此每个尾素恰好落入 plus 无槽、minus 无槽、双侧有槽三类之一。若无槽分支大到威胁 `PrimeWindow`，必有某个 floor layer 承担相位端带质量。全局仍需证明层端带上界，或将持久层异常排斥为 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
phase_congruence_failure_count=0
trichotomy_failure_count=0
finite_large_noslot_branch_count=0
row_column_unconditional_closed=false
```

## 1. 相位层正规形

尾素写成 `q=P-2b`。因为

```text
2b^2 = (P-q)^2/2 == P^2/2 (mod q),
```

令 `h=(P-1)/2`，并写

```text
2b^2 = kq+s,  0<=s<q.
```

则三分法为

```text
plus no-slot  iff s < q-h
minus no-slot iff s > h
both raw       iff q-h <= s <= h.
```

因为 `q<P`，左右端带互斥。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| tail prime count | 38678 |
| plus PrimeWindow | 97145 |
| minus PrimeWindow | 97396 |
| plus no-slot | 18299 |
| minus no-slot | 15895 |
| both raw | 4484 |
| max floor layer k | 124 |

## 3. 最重层

| side | layer k | count |
| --- | ---: | ---: |
| `plus` | 0 | 3457 |
| `plus` | 1 | 1098 |
| `plus` | 2 | 819 |
| `plus` | 3 | 652 |
| `plus` | 4 | 559 |
| `plus` | 5 | 469 |
| `plus` | 6 | 449 |
| `plus` | 7 | 402 |
| `plus` | 8 | 400 |
| `plus` | 10 | 341 |
| `plus` | 9 | 340 |
| `plus` | 11 | 309 |
| `minus` | 0 | 1475 |
| `minus` | 1 | 941 |
| `minus` | 2 | 720 |
| `minus` | 3 | 609 |
| `minus` | 4 | 554 |
| `minus` | 5 | 500 |
| `minus` | 6 | 432 |
| `minus` | 7 | 380 |
| `minus` | 8 | 362 |
| `minus` | 9 | 338 |
| `minus` | 10 | 308 |
| `minus` | 11 | 296 |
| `both_raw` | 2 | 96 |
| `both_raw` | 0 | 92 |
| `both_raw` | 4 | 87 |
| `both_raw` | 3 | 83 |
| `both_raw` | 5 | 83 |
| `both_raw` | 6 | 82 |
| `both_raw` | 1 | 81 |
| `both_raw` | 8 | 78 |
| `both_raw` | 11 | 78 |
| `both_raw` | 21 | 78 |
| `both_raw` | 10 | 77 |
| `both_raw` | 7 | 76 |

## 4. 样本表

| P | tail | plus prime | plus no-slot | minus prime | minus no-slot | both raw | max k | plus large | minus large |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 1 | 3 | 1 | 3 | 0 | 0 | 0 | `false` | `false` |
| 17 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | `false` | `false` |
| 19 | 1 | 3 | 1 | 4 | 0 | 0 | 0 | `false` | `false` |
| 23 | 1 | 2 | 0 | 3 | 0 | 1 | 0 | `false` | `false` |
| 29 | 0 | 4 | 0 | 5 | 0 | 0 | 0 | `false` | `false` |
| 31 | 1 | 5 | 1 | 4 | 0 | 0 | 0 | `false` | `false` |
| 101 | 3 | 11 | 1 | 12 | 2 | 0 | 1 | `false` | `false` |
| 499 | 16 | 40 | 9 | 44 | 6 | 1 | 11 | `false` | `false` |
| 1009 | 29 | 72 | 17 | 70 | 9 | 3 | 24 | `false` | `false` |
| 2003 | 51 | 125 | 28 | 139 | 18 | 5 | 48 | `false` | `false` |
| 4999 | 118 | 300 | 58 | 289 | 46 | 14 | 124 | `false` | `false` |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `tail_phase_congruence` | `closed` | For q=P-2b, 2b^2 is congruent to P^2/2 modulo q. |
| `two_sided_noslot_trichotomy` | `closed` | Every tail prime belongs to exactly one of plus-no-slot, minus-no-slot, or both-sides-raw. |
| `floor_layer_normal_form` | `closed` | Writing 2b^2=kq+s, plus-no-slot is s<q-(P-1)/2 and minus-no-slot is s>(P-1)/2. |
| `large_noslot_branch_layer_return` | `closed` | A no-slot branch large enough to threaten PrimeWindow forces a floor layer with proportional phase-band mass. |
| `layer_band_bound_or_pdec` | `open` | A global proof still needs a bound for every floor-layer phase band, or a PDEC/SAE exclusion of persistent layers. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TailPhaseCongruenceClosed` | `true` | `true` | `2b^2 mod q` 已严格接回 `P^2/2 mod q`。 | closed |
| `TwoSidedNoSlotTrichotomyClosed` | `true` | `true` | 每个尾素恰落入 plus 无槽、minus 无槽、双侧有槽三类之一。 | closed |
| `FiniteNoLargeNoSlotBranch` | `true` | `false` | 有限扫描 P<=5000 没有无槽分支达到 PrimeWindow/2。 | finite evidence only |
| `GlobalLayerBandBound` | `false` | `false` | 仍需全局控制所有 floor layer 的二次相位端带命中。 | NoSlotFloorLayerBandBoundOrLayerPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压缩无槽分支，不关闭全局行/列命题。 | NoSlotFloorLayerBandBoundOrLayerPDEC |

## 7. 下一步

- 主攻：`NoSlotFloorLayerBandBoundOrLayerPDEC`。
- 这一步没有证明层端带全局上界；它只是把无槽异常压成固定 floor layer 的相位带异常。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-noslot-phase-layer-ledger.json` | `7b1e80c78c6aecc41f13a87dc16432245a60868efd44a3c04eafc2c22b216128` |
| `experiments/prime_matrix_square_phase_noslot_phase_layer_router.py` | `bacdd70e99b53d5e25f21d5734d72e68db41b61f6df8df3ded736d718c0648c9` |
