# Prime Matrix square-phase even-layer interval router

**状态：** `square_phase_even_prime_pair_tiling_reduced_to_fixed_b_layer_intervals_open`

偶半网格素对铺砖已进一步压成固定 `b` 层的精确 `u` 区间：候选有效槽完全由 `q=P-2b`、`m=P+2(b+u)` 同为素数且 `u` 落入半列窗口区间生成，不再需要先枚举低洞。完全铺砖反例因此要求这些候选素对槽数达到低洞数 `H`；全局仍需证明候选上界低于低洞下界，或把失败登记为固定层相位 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
total_failure_count=0
candidate_upper_bound_beats_lowholes_proved=false
row_column_unconditional_closed=false
```

## 1. 固定 b 层区间

令 `H2=(P-1)/2`、`q=P-2b`。候选槽满足 `1<=s<=H2`。

plus 侧 `s=u(P-2b)-2b^2`，所以

```text
ceil((2b^2+1)/(P-2b)) <= u <= floor((2b^2+H2)/(P-2b)).
```

minus 侧 `s=2b^2-u(P-2b)`，所以

```text
ceil((2b^2-H2)/(P-2b)) <= u <= floor((2b^2-1)/(P-2b)),  u>=0.
```

再加上 `P-2b` 与 `P+2(b+u)` 同为素数，就得到全部有效半素数槽。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `fixed_b_u_interval_formula` | `closed` | For fixed b, the half-window condition 1<=s<=(P-1)/2 gives an exact integer interval for u on both signs. |
| `candidate_slots_generated_without_low_sieve` | `closed` | The effective semiprime slots are exactly the candidate pairs with q=P-2b and m=P+2(b+u) prime and u in the fixed-b interval. |
| `full_tiling_candidate_upper_bound_target` | `open` | A full tiling would require the candidate prime-pair slot count to reach the low-hole count H; proving a global upper/lower gap or PDEC return remains open. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| low survivors | 102191 | 102739 | 204930 |
| candidate slots | 5046 | 5343 | 10389 |

最小 `H-candidates` 样本：`P=3`，`sign=plus`，`H=1`，`candidates=0`。

## 4. 样本表

| P | sign | H | candidate slots | max u | max layer load | failures |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 0 | 0 | 0 | 0 |
| 13 | `minus` | 3 | 0 | 0 | 0 | 0 |
| 17 | `plus` | 1 | 0 | 0 | 0 | 0 |
| 17 | `minus` | 3 | 0 | 0 | 0 | 0 |
| 19 | `plus` | 3 | 0 | 0 | 0 | 0 |
| 19 | `minus` | 4 | 0 | 0 | 0 | 0 |
| 23 | `plus` | 3 | 1 | 1 | 1 | 0 |
| 23 | `minus` | 3 | 0 | 0 | 0 | 0 |
| 29 | `plus` | 4 | 0 | 0 | 0 | 0 |
| 29 | `minus` | 5 | 0 | 0 | 0 | 0 |
| 31 | `plus` | 5 | 0 | 0 | 0 | 0 |
| 31 | `minus` | 4 | 0 | 0 | 0 | 0 |
| 101 | `plus` | 11 | 0 | 0 | 0 | 0 |
| 101 | `minus` | 12 | 0 | 0 | 0 | 0 |
| 499 | `plus` | 42 | 2 | 4 | 1 | 0 |
| 499 | `minus` | 45 | 1 | 5 | 1 | 0 |
| 1009 | `plus` | 79 | 7 | 25 | 1 | 0 |
| 1009 | `minus` | 77 | 7 | 21 | 1 | 0 |
| 2003 | `plus` | 132 | 7 | 44 | 1 | 0 |
| 2003 | `minus` | 144 | 5 | 45 | 2 | 0 |
| 4999 | `plus` | 317 | 17 | 125 | 2 | 0 |
| 4999 | `minus` | 303 | 14 | 119 | 1 | 0 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedBLayerIntervalFormulaClosed` | `true` | `true` | 固定 b 层的 u 区间与候选槽枚举已逐项对齐。 | closed |
| `CandidateUpperBoundBeatsLowHoles` | `false` | `false` | 仍需全局证明候选素对槽数小于低洞数，或证明失败形成 PDEC/SAE。 | EvenLayerPrimePairCandidateUpperBoundBeatsLowHoles |
| `LayerPrimePairTilingPDEC` | `false` | `false` | 若候选槽可完全铺砖低洞，需要登记固定 b/u 层的相位异常。 | EvenLayerPrimePairTilingPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭层区间公式，不关闭全局行/列命题。 | EvenLayerPrimePairCandidateUpperBoundBeatsLowHoles OR EvenLayerPrimePairTilingPDECSAEReturn |

## 6. 下一步

- 主攻：`EvenLayerPrimePairCandidateUpperBoundBeatsLowHoles`。
- 备选回流：`EvenLayerPrimePairTilingPDECSAEReturn`。
- 需要证明候选素对槽数全局小于低洞数，或证明候选槽达到低洞数时固定 b/u 层产生相位异常。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-even-layer-interval-ledger.json` | `efd03b5fac377fcae05a67856534845422e78bf885e88c996d6841a86f2c96f5` |
| `experiments/prime_matrix_square_phase_even_layer_interval_router.py` | `9e243ffa1743280677931b841a5227047791d4eaecbcfe3c64e6457394475e90` |
