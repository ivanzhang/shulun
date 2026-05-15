# Prime Matrix square-phase off-band prefix gap shadow wheel escalation router

**状态：** `wheel17_capacity_drop_registered_global_open`

本步沿同一 hardpoint 做容量单调升级：把小轮从 13 升到 17 后，有限前沿的最大互补幸存容量从 5 降到 4，因此最大所需 hull 素数数从 6 降到 5；继续升到 19/23/29/31 在当前前沿没有进一步下降。这不是全局闭合，而是把下一硬点压成 wheel-17 固定孔袋短 hull 下界，或 prime-support collapse PDEC 排斥。

```text
baseline_wheel_bound=13
baseline_max_required_hull_prime_count=6
selected_wheel_bound=17
selected_wheel_primes=[3, 5, 7, 11, 13, 17]
selected_max_required_hull_prime_count=5
finite_capacity_drop=1
row_column_unconditional_closed=false
```

## 1. 轮筛升级表

| bound | wheel primes | max survivors | max required hull primes | min margin | tight margin-one | all finite gates closed |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 13 | `[3, 5, 7, 11, 13]` | 5 | 6 | 1 | 6 | `true` |
| 17 | `[3, 5, 7, 11, 13, 17]` | 4 | 5 | 1 | 5 | `true` |
| 19 | `[3, 5, 7, 11, 13, 17, 19]` | 4 | 5 | 1 | 5 | `true` |
| 23 | `[3, 5, 7, 11, 13, 17, 19, 23]` | 4 | 5 | 1 | 5 | `true` |
| 29 | `[3, 5, 7, 11, 13, 17, 19, 23, 29]` | 4 | 5 | 1 | 5 | `true` |
| 31 | `[3, 5, 7, 11, 13, 17, 19, 23, 29, 31]` | 4 | 5 | 1 | 5 | `true` |

## 2. wheel-17 最紧前沿

| P | side | hull | hull primes | wheel-17 survivors | required primes | margin | survivor values |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 733 | `plus` | `675-687` | 2 | 1 | 2 | 1 | `[677]` |
| 523 | `plus` | `485-501` | 3 | 2 | 3 | 1 | `[487, 491]` |
| 691 | `minus` | `649-665` | 3 | 2 | 3 | 1 | `[659, 661]` |
| 683 | `plus` | `639-657` | 4 | 3 | 4 | 1 | `[641, 643, 647]` |
| 733 | `plus` | `675-705` | 4 | 3 | 4 | 1 | `[677, 683, 691]` |
| 673 | `minus` | `619-637` | 2 | 0 | 1 | 2 | `[]` |
| 733 | `plus` | `681-705` | 3 | 1 | 2 | 2 | `[691]` |
| 313 | `plus` | `273-295` | 4 | 1 | 2 | 3 | `[277]` |
| 1129 | `plus` | `1051-1095` | 7 | 4 | 5 | 3 | `[1061, 1063, 1073, 1081]` |
| 691 | `minus` | `649-689` | 6 | 2 | 3 | 4 | `[659, 661]` |
| 673 | `minus` | `619-671` | 8 | 4 | 5 | 4 | `[631, 641, 643, 647]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `wheel_capacity_monotonicity` | `closed` | Increasing the wheel bound can only remove complement-pocket survivors and cannot weaken the gate Prime(hull)>WheelSurvivors(C). |
| `first_effective_wheel17_capacity_drop` | `finite_evidence` | On the finite residual frontier, adding 17 drops the maximum survivor requirement from 6 hull primes to 5 hull primes. |
| `post17_no_further_finite_drop` | `finite_evidence` | For tested bounds 19,23,29,31, the finite frontier does not improve beyond the wheel-17 capacity. |
| `global_wheel17_short_hull_lower_bound` | `open` | A global proof still needs short hull prime counts beating wheel-17 pocket survivors, or exclusion of prime-support collapse. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `WheelEscalationMonotonicityClosed` | `true` | `true` | 轮筛升级只会减少互补孔袋容量，因此保持同一目标命题。 | closed |
| `FiniteWheel17CapacityDropRegistered` | `true` | `false` | 有限前沿中 17 是首个把最大所需 hull 素数数从 6 降到 5 的小轮。 | finite evidence only |
| `GlobalWheel17LowerBoundClosed` | `false` | `false` | 仍需全局证明短 hull 素数数超过 wheel-17 互补幸存容量。 | ShortHullPrimeLowerBoundAgainstWheel17FixedPocketsOrPrimeSupportCollapsePDEC |
| `PrimeSupportCollapsePDECExcluded` | `false` | `false` | 若短 hull 下界失败，仍需排斥所有 hull 素数被 wheel-17 孔袋吸收的支撑塌缩。 | ShortHullPrimeLowerBoundAgainstWheel17FixedPocketsOrPrimeSupportCollapsePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压缩容量常数，不关闭全局行/列命题。 | ShortHullPrimeLowerBoundAgainstWheel17FixedPocketsOrPrimeSupportCollapsePDEC |

## 5. 下一步

- 主攻：`ShortHullPrimeLowerBoundAgainstWheel17FixedPocketsOrPrimeSupportCollapsePDEC`。
- 容量侧：证明 wheel-17 固定孔袋的短 hull 多素数下界。
- 反例侧：若失败，反例必须把所有 hull 素数压进至多 4 个 wheel-17 幸存位置，形成 prime-support collapse PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py` | `430b1d0c42dd64c5e658ff56da2ab4b92b7ad01b8821367e38d5fa3485af5600` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py` | `33a5f03674af63ed8a7d4347c0ea10ada628cb6e3cb87e046cdfaf94197ff6ef` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router.py` | `fb204508882e7e5d9212782370a91696e799b0630552bd9542d41a03ddbe74a7` |
| `data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json` | `7be890f2eef77312ef25069b38c5a0d8f2af823b92bde052f63e11f516c4c710` |
| `data/square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json` | `5c2bd655e098a9f4cc1ce368b6dd01d7edf20a737ad9087f053a9f4db6968c0c` |
| `data/square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json` | `071e8c159cba935e2e688a701c10b51d72416f2c8e4e29f1648e661d8e8c09a2` |
