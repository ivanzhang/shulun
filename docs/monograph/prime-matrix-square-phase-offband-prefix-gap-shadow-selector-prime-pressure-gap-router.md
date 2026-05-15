# Prime Matrix square-phase off-band prefix gap shadow selector prime pressure gap router

**状态：** `selector_prime_rho_hits_have_pressure_gap_open_global`

本步统计全部 344 个素数 rho 命中。当前最小 pressure gap 为 1，即每个素数 rho 命中都满足 `target_W>replay_W`；replay_W 分布为 {0: 342, 1: 2}，没有 full-shape overlap。

```text
max_p=5000
prime_rho_hit_count=344
min_pressure_gap=1
max_pressure_gap=2
pressure_gap_histogram={1: 94, 2: 250}
replay_W_histogram={0: 342, 1: 2}
full_shape_overlap_count=0
row_column_unconditional_closed=false
```

## 1. Template Pressure Gaps

| template | prime rho hits | min gap | max gap | gap histogram | replay W histogram | signed range |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| 0 | 43 | 2 | 2 | `{2: 43}` | `{0: 43}` | `-83..-1` |
| 1 | 44 | 1 | 2 | `{1: 1, 2: 43}` | `{0: 43, 1: 1}` | `-65..0` |
| 2 | 25 | 1 | 1 | `{1: 25}` | `{0: 25}` | `-82..-2` |
| 3 | 25 | 1 | 1 | `{1: 25}` | `{0: 25}` | `-82..-2` |
| 4 | 42 | 1 | 1 | `{1: 42}` | `{0: 42}` | `-60..-1` |
| 5 | 83 | 2 | 2 | `{2: 83}` | `{0: 83}` | `-83..-1` |
| 6 | 82 | 1 | 2 | `{1: 1, 2: 81}` | `{0: 81, 1: 1}` | `-78..0` |

## 2. 命题行

| name | status | statement |
| --- | --- | --- |
| `prime_rho_hit_pressure_gap_profile` | `closed_on_current_sweep` | Every prime rho hit in the sweep has target W strictly larger than replay W. |
| `ordered_shape_mismatch_not_needed_on_current_sweep` | `closed_on_current_sweep` | Current prime rho hits are already excluded at the witness pressure level before ordered-shape PDEC is needed. |
| `global_prime_pressure_gap_lower_bound` | `open` | A global proof must show prime rho hits force target_W-replay_W>=1, or route equality cases to full-shape overlap PDEC. |

## 3. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentPrimeRhoHitsHavePressureGap` | `true` | `true` | 当前全部素数 rho 命中都有至少 1 个 witness pressure 缺口。 | closed on current finite sweep |
| `CurrentFullShapeOverlapAbsent` | `true` | `true` | 当前没有 target_W=replay_W 的 full-shape overlap 例外。 | closed on current finite sweep |
| `GlobalPrimePressureGapLowerBoundProved` | `false` | `false` | 仍需全局证明素数 rho 命中必有 pressure gap。 | PrimeRhoHitWitnessPressureGapLowerBoundOrFullShapeOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成素数 rho 命中的压力缺口有限画像，不关闭全局行/列命题。 | PrimeRhoHitWitnessPressureGapLowerBoundOrFullShapeOverlapPDEC |

## 4. 下一步

- 主攻：`PrimeRhoHitWitnessPressureGapLowerBoundOrFullShapeOverlapPDEC`。
- 当前有限前沿显示所有素数 rho 命中均满足 `target_W-replay_W>=1`。
- 全局证明需要把这个 pressure gap 写成 `H,T` 的不等式；若 gap 消失，则进入 full-shape overlap PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router.py` | `77dfcd9ce965eef581172c5a41163e5846fa385914948adb23cb954ec3b326d2` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router.py` | `f0c6e92421aa66727d36b60042796ef73cadb07e7a08b378fde9c8cba2eb81cd` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json` | `31606c41cf9268aa4adf031683d22757bac054b17103da646d7eff0898717f8f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json` | `5af4d8884875aa20c002ff34f309529a409410694672939e6f9309d646fc5051` |
