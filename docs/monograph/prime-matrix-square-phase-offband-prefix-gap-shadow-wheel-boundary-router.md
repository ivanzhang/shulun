# Prime Matrix square-phase off-band prefix gap shadow wheel boundary router

**状态：** `short_hull_prime_count_boundary_registered_open`

本步没有转换命题：wheel absorption 之后的真正剩余被精确登记为短 hull 素数计数下界。有限账本中所有 wheel gate 已关闭，最紧余量为 1；但全局证明必须说明每个固定形状 hull 含有多于互补孔袋 wheel survivors 的素数。普通 x^0.525 一个素数短区间输入不能直接闭合该门，因为这里需要 sqrt 级、且最多需要 6 个 hull 素数。

```text
record_count=11
finite_all_wheel_gates_closed=true
tight_margin_one_count=6
min_current_gate_margin=1
max_required_hull_prime_count_for_gate=6
max_depth_over_sqrt_p=2.321387
row_column_unconditional_closed=false
```

## 1. 精确边界

对每个固定孔袋模板，当前门只需要证明

```text
Prime(hull) > WheelSurvivors(complement pockets)
```

等价地，若互补孔袋有 `S` 个小轮筛幸存者，则 hull 区间至少要有 `S+1` 个素数。若该不等式失败且目标并集仍全空，反例必须进入 wheel-survivor absorption PDEC。

## 2. 最紧前沿

| P | side | hull | depth/sqrt(P) | hull primes | wheel survivors | required primes | margin |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 673 | `minus` | `619-637` | 2.081547 | 2 | 1 | 2 | 1 |
| 733 | `plus` | `675-687` | 2.142279 | 2 | 1 | 2 | 1 |
| 523 | `plus` | `485-501` | 1.661624 | 3 | 2 | 3 | 1 |
| 691 | `minus` | `649-665` | 1.597755 | 3 | 2 | 3 | 1 |
| 683 | `plus` | `639-657` | 1.683613 | 4 | 3 | 4 | 1 |
| 733 | `plus` | `675-705` | 2.142279 | 4 | 3 | 4 | 1 |
| 733 | `plus` | `681-705` | 1.920664 | 3 | 1 | 2 | 2 |
| 313 | `plus` | `273-295` | 2.260934 | 4 | 1 | 2 | 3 |
| 1129 | `plus` | `1051-1095` | 2.321387 | 7 | 4 | 5 | 3 |
| 673 | `minus` | `619-671` | 2.081547 | 8 | 5 | 6 | 3 |
| 691 | `minus` | `649-689` | 1.597755 | 6 | 2 | 3 | 4 |

## 3. 外部输入匹配审查

- 当前 hull 深度是 `O(sqrt(P))`，最大样本深度约 `2.321388*sqrt(P)`。
- 当前 gate 不是“有一个素数”即可统一闭合；最坏模板需要 `6` 个 hull 素数。
- 因此普通 Baker--Harman--Pintz 型 `x^0.525` 一个素数短区间输入不匹配本门。
- 若要外部闭合，需要 sqrt 级多素数计数输入，或直接证明这些固定穿孔并集含素数。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `wheel_gate_to_short_hull_prime_count` | `closed` | For each fixed pocket template, the wheel gate closes once the hull interval contains more primes than complement wheel survivors. |
| `finite_tight_frontier_registered` | `closed` | The finite ledger identifies all margin-one frontier records and their exact required hull prime counts. |
| `ordinary_0525_short_interval_input_mismatch` | `closed` | A one-prime x^0.525 short-interval input does not imply the required sqrt-scale multi-prime hull count. |
| `global_short_hull_prime_lower_bound` | `open` | A global proof still needs sqrt-scale prime-count lower bounds for these fixed hull/pocket shapes, or exclusion of wheel-survivor absorption PDEC. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `WheelGateBoundaryClosed` | `true` | `true` | 当前 hardpoint 已精确转写为短 hull 素数计数胜过互补 wheel survivors。 | closed |
| `FiniteFrontierRegistered` | `true` | `false` | 有限最紧样本和所需素数数已登记；这不是全局证明。 | finite evidence only |
| `ExternalBHP0525ClosesThisRoute` | `false` | `false` | BHP 型一个素数的 x^0.525 输入既长于 sqrt 尺度，也不给多素数计数。 | ShortHullPrimeLowerBoundAgainstFixedWheelPocketsOrWheelSurvivorAbsorptionPDEC |
| `GlobalShortHullPrimeLowerBoundClosed` | `false` | `false` | 仍需证明固定形状短 hull 的素数计数下界，或排斥持久吸收包。 | ShortHullPrimeLowerBoundAgainstFixedWheelPocketsOrWheelSurvivorAbsorptionPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭边界转写，不关闭行/列无条件命题。 | ShortHullPrimeLowerBoundAgainstFixedWheelPocketsOrWheelSurvivorAbsorptionPDEC |

## 6. 下一步

- 主攻：`ShortHullPrimeLowerBoundAgainstFixedWheelPocketsOrWheelSurvivorAbsorptionPDEC`。
- 自足线：对固定小 `k` 形状证明短 hull 多素数下界，或从目标 union 直接构造一个素数。
- 反例线：若下界失败，必须形成命名的 wheel-survivor absorption PDEC，并继续寻找与相位/列刚性的矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router.py` | `fb204508882e7e5d9212782370a91696e799b0630552bd9542d41a03ddbe74a7` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router.py` | `dc6cddaa6e5a472f55c1cffa87a780f992b8a8ea4fefc06370be8e565bffd5fb` |
| `data/square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json` | `a33bdf32c1ddabf0a48c0ea58ef579c8f8c3927e6eab18fb6600fc88385cec2b` |
| `data/square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json` | `5c2bd655e098a9f4cc1ce368b6dd01d7edf20a737ad9087f053a9f4db6968c0c` |
| `docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md` | `520f7c2861bd5e75087bd8e808773f51c369ab44b646f81b4ce6048f105efeba` |
| `docs/zero-row-and-prime-gap-equivalence.md` | `7f9f42d814c9eb60521c5d472f0d3212ffef814b1c66428e41fcf5eaf070981e` |
