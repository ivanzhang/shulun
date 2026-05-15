# Prime Matrix square-phase off-band prefix gap shadow wheel absorption router

**状态：** `complement_absorption_reduced_to_wheel_survivor_capacity_open`

本步用小轮筛 `[3, 5, 7, 11, 13]` 压缩互补孔袋吸收容量。互补孔袋中的素数必然属于小轮筛幸存者；若 hull 素数数超过这些幸存者数量，目标并集必含素数。有限账本中 11 个 count-gate 残余全部被 wheel capacity gate 关闭；全局仍需证明相同不等式或排斥持久 wheel-survivor absorption PDEC。

```text
wheel_bound=13
wheel_primes=[3, 5, 7, 11, 13]
source_residual_count=11
wheel_capacity_closed_count=11
wheel_survivor_absorption_pdec_count=0
row_column_unconditional_closed=false
```

## 1. 轮筛容量门

互补孔袋吸收全部 hull 素数时，互补孔袋内的每个素数都必须通过小轮筛。因此

```text
Prime(complement pockets) <= WheelSurvivors(complement pockets)
```

若 `Prime(hull)>WheelSurvivors(C)`，互补孔袋无法吸收全部 hull 素数，目标并集必含素数。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| source residual count | 11 |
| wheel capacity closed | 11 |
| wheel-survivor absorption PDEC | 0 |
| min wheel capacity margin | 1 |
| max complement wheel survivors | 5 |
| max complement primes | 4 |

## 3. 轮筛容量边界

| P | side | hull | hull primes | raw C cand | C primes | wheel survivors | margin | survivor values |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 683 | `plus` | `639-657` | 4 | 4 | 3 | 3 | 1 | `[641, 643, 647]` |
| 733 | `plus` | `675-705` | 4 | 10 | 3 | 3 | 1 | `[677, 683, 691]` |
| 523 | `plus` | `485-501` | 3 | 3 | 2 | 2 | 1 | `[487, 491]` |
| 691 | `minus` | `649-665` | 3 | 5 | 2 | 2 | 1 | `[659, 661]` |
| 673 | `minus` | `619-637` | 2 | 3 | 0 | 1 | 1 | `[629]` |
| 733 | `plus` | `675-687` | 2 | 2 | 1 | 1 | 1 | `[677]` |
| 733 | `plus` | `681-705` | 3 | 4 | 1 | 1 | 2 | `[691]` |
| 673 | `minus` | `619-671` | 8 | 12 | 4 | 5 | 3 | `[629, 631, 641, 643, 647]` |
| 1129 | `plus` | `1051-1095` | 7 | 9 | 2 | 4 | 3 | `[1061, 1063, 1073, 1081]` |
| 313 | `plus` | `273-295` | 4 | 4 | 1 | 1 | 3 | `[277]` |
| 691 | `minus` | `649-689` | 6 | 6 | 2 | 2 | 4 | `[659, 661]` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `complement_prime_capacity_leq_wheel_survivors` | `closed` | Complement-pocket primes are bounded by survivors of the odd wheel with primes <= 13. |
| `hull_count_beats_wheel_capacity_gate` | `closed` | If hull_prime_count is larger than complement wheel survivors, the target union must contain a prime. |
| `finite_no_wheel_survivor_absorption` | `finite_evidence` | The finite audit finds no residual wheel-survivor absorption after the chosen wheel. |
| `global_wheel_survivor_absorption_exclusion` | `open` | A global proof still needs hull prime lower bounds beating wheel survivor capacity, or exclusion of persistent wheel-survivor absorption. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ComplementWheelCapacityGateClosed` | `true` | `true` | 互补孔袋吸收容量已从候选数降到小轮筛幸存数。 | closed |
| `FiniteNoWheelSurvivorAbsorptionPDEC` | `true` | `false` | 有限样本中小轮筛容量门关闭所有残余。 | finite evidence only |
| `GlobalWheelCapacityClosed` | `false` | `false` | 仍需全局证明 hull 素数下界超过互补轮筛容量，或排斥持久吸收。 | HullPrimeCountBeatsComplementWheelCapacityOrWheelSurvivorAbsorptionPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成容量压缩，不关闭全局行/列命题。 | HullPrimeCountBeatsComplementWheelCapacityOrWheelSurvivorAbsorptionPDEC |

## 6. 下一步

- 主攻：`HullPrimeCountBeatsComplementWheelCapacityOrWheelSurvivorAbsorptionPDEC`。
- 需全局证明短 hull 的素数下界超过互补孔袋的小轮筛幸存容量。
- 若失败，反例必须表现为互补孔袋的小轮筛幸存者吸收全部 hull 素数。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router.py` | `dc6cddaa6e5a472f55c1cffa87a780f992b8a8ea4fefc06370be8e565bffd5fb` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py` | `33a5f03674af63ed8a7d4347c0ea10ada628cb6e3cb87e046cdfaf94197ff6ef` |
| `data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json` | `7be890f2eef77312ef25069b38c5a0d8f2af823b92bde052f63e11f516c4c710` |
| `data/square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json` | `a33bdf32c1ddabf0a48c0ea58ef579c8f8c3927e6eab18fb6600fc88385cec2b` |
