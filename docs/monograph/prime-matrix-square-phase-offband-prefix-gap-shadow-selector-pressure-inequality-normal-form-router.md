# Prime Matrix square-phase off-band prefix gap shadow selector pressure inequality normal form router

**状态：** `selector_prime_pressure_gap_reduced_to_ht_inequality_open_global`

本步把素数 rho 命中的 pressure gap 正规化为 H,T 不等式：`target_W-replay_W>=1` 当且仅当 `2T-H<=2W-3`，等价于 `H-2T>=3-2W`。当前 344 个素数 rho 命中全部满足该不等式；最小正规形 slack 为 0，边界 slack=0 的命中数为 1。

```text
max_p=5000
prime_rho_hit_count=344
ht_inequality_failure_count=0
min_normal_form_slack=0
max_normal_form_slack=84
boundary_slack_zero_count=1
normal_form_slack_histogram={0: 1, 1: 6, 2: 4, 3: 4, 4: 6, 5: 5, 6: 3, 7: 5, 8: 10, 9: 4, 10: 6, 11: 11, 12: 4, 13: 5, 14: 1, 15: 12, 16: 7, 18: 7, 19: 1, 20: 5, 21: 3, 22: 4, 23: 3, 24: 9, 25: 6, 26: 11, 27: 8, 29: 5, 30: 13, 31: 7, 32: 9, 33: 6, 34: 12, 35: 9, 36: 4, 37: 3, 38: 7, 39: 6, 40: 4, 41: 7, 42: 7, 43: 7, 44: 7, 45: 4, 46: 1, 47: 8, 48: 7, 49: 4, 50: 1, 51: 3, 52: 7, 53: 3, 54: 3, 55: 1, 56: 2, 57: 7, 58: 2, 59: 3, 60: 3, 62: 2, 63: 4, 65: 3, 66: 2, 67: 1, 71: 1, 74: 1, 79: 3, 81: 2, 84: 2}
row_column_unconditional_closed=false
```

## 1. 等价正规形

令 `D=2T-H`，并记目标 shape 需要 `W` 个 off-band witness。回放需要

```text
replay_W=max(0,floor(D/2)+1).
```

因此 `target_W-replay_W>=1` 等价于

```text
2T-H <= 2W-3,
H-2T >= 3-2W.
```

## 2. Template Summary

| template | hits | W | min slack | max slack | slack histogram | boundary | H-2T range |
| ---: | ---: | --- | ---: | ---: | --- | ---: | --- |
| 0 | 43 | `[2]` | 2 | 84 | `{2: 1, 4: 1, 8: 2, 10: 2, 12: 2, 15: 2, 16: 2, 18: 1, 22: 1, 23: 1, 24: 1, 27: 2, 30: 1, 31: 1, 32: 1, 34: 4, 35: 1, 36: 1, 37: 1, 38: 1, 40: 1, 42: 1, 47: 1, 48: 1, 52: 1, 53: 1, 56: 1, 57: 2, 59: 1, 60: 1, 62: 1, 79: 1, 84: 1}` | 0 | `1..83` |
| 1 | 44 | `[2]` | 1 | 66 | `{1: 1, 3: 1, 5: 2, 7: 1, 8: 1, 9: 1, 11: 2, 13: 2, 15: 1, 24: 1, 25: 1, 26: 2, 29: 2, 30: 3, 31: 1, 32: 1, 33: 1, 35: 1, 36: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 2, 44: 2, 47: 1, 49: 1, 51: 1, 52: 1, 54: 1, 58: 1, 63: 2, 66: 1}` | 0 | `0..65` |
| 2 | 25 | `[1]` | 1 | 81 | `{1: 2, 2: 1, 3: 1, 11: 1, 15: 1, 18: 1, 20: 1, 24: 1, 25: 1, 26: 1, 27: 1, 30: 1, 33: 1, 34: 1, 35: 1, 38: 1, 39: 1, 41: 1, 44: 1, 45: 1, 52: 1, 57: 1, 65: 1, 81: 1}` | 0 | `2..82` |
| 3 | 25 | `[1]` | 1 | 81 | `{1: 2, 2: 1, 3: 1, 11: 1, 15: 1, 18: 1, 20: 1, 24: 1, 25: 1, 26: 1, 27: 1, 30: 1, 33: 1, 34: 1, 35: 1, 38: 1, 39: 1, 41: 1, 44: 1, 45: 1, 52: 1, 57: 1, 65: 1, 81: 1}` | 0 | `2..82` |
| 4 | 42 | `[1]` | 0 | 59 | `{0: 1, 4: 3, 6: 1, 7: 1, 8: 1, 10: 2, 14: 1, 15: 1, 16: 1, 18: 1, 20: 1, 21: 1, 22: 1, 24: 2, 25: 1, 26: 2, 27: 2, 30: 1, 31: 2, 32: 2, 34: 1, 41: 1, 42: 2, 43: 2, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 55: 1, 59: 1}` | 1 | `1..60` |
| 5 | 83 | `[2]` | 2 | 84 | `{2: 1, 4: 2, 6: 1, 7: 1, 8: 3, 9: 1, 10: 2, 11: 2, 12: 2, 13: 1, 15: 4, 16: 2, 18: 3, 19: 1, 20: 1, 22: 2, 23: 2, 24: 1, 26: 3, 27: 2, 30: 1, 31: 2, 32: 2, 33: 1, 34: 5, 35: 2, 36: 1, 37: 2, 38: 1, 40: 1, 41: 2, 42: 2, 43: 1, 44: 1, 45: 1, 47: 2, 48: 3, 52: 2, 53: 1, 54: 1, 56: 1, 57: 2, 59: 1, 60: 1, 62: 1, 65: 1, 67: 1, 71: 1, 74: 1, 79: 1, 84: 1}` | 0 | `1..83` |
| 6 | 82 | `[2]` | 1 | 79 | `{1: 1, 3: 1, 5: 3, 6: 1, 7: 2, 8: 3, 9: 2, 11: 5, 13: 2, 15: 2, 16: 2, 20: 1, 21: 2, 24: 2, 25: 2, 26: 2, 29: 3, 30: 5, 31: 1, 32: 3, 33: 2, 35: 3, 36: 1, 38: 2, 39: 3, 40: 1, 41: 1, 42: 1, 43: 2, 44: 2, 47: 3, 48: 2, 49: 2, 51: 2, 52: 1, 53: 1, 54: 1, 57: 1, 58: 1, 60: 1, 63: 2, 66: 1, 79: 1}` | 0 | `0..78` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `pressure_gap_ht_equivalence` | `closed` | For target W>=1, target_W-replay_W>=1 is equivalent to 2T-H<=2W-3, or H-2T>=3-2W. |
| `current_prime_rho_hits_satisfy_ht_normal_form` | `closed_on_current_sweep` | Every current prime rho hit satisfies the H,T normal-form inequality. |
| `global_ht_inequality_for_prime_rho_hits` | `open` | A global proof must derive 2T-H<=2W-3 for prime rho hits, or route equality failure to full-shape overlap PDEC. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PressureGapHTEquivalenceClosed` | `true` | `true` | `target_W-replay_W>=1` 已等价为 `2T-H<=2W-3`。 | closed |
| `CurrentHTInequalityHolds` | `true` | `true` | 当前全部素数 rho 命中满足 H,T 正规形不等式。 | closed on current finite sweep |
| `GlobalHTInequalityProved` | `false` | `false` | 仍需全局证明 prime rho hit 强制该 H,T 不等式。 | PrimeRhoHitHTInequalityLowerBoundOrFullShapeOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 pressure gap 的 H,T 正规形，不关闭全局行/列命题。 | PrimeRhoHitHTInequalityLowerBoundOrFullShapeOverlapPDEC |

## 5. 下一步

- 主攻：`PrimeRhoHitHTInequalityLowerBoundOrFullShapeOverlapPDEC`。
- 已关闭 pressure gap 到 H,T 不等式的代数等价。
- 真正剩余是全局证明 prime rho hit 强制 `2T-H<=2W-3`；边界 slack=0 是最窄例外层。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router.py` | `f2874e8671ae937ef5f7e162e1dbc50d88f6c1eeee7be431531e86d47201fe90` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router.py` | `77dfcd9ce965eef581172c5a41163e5846fa385914948adb23cb954ec3b326d2` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json` | `5af4d8884875aa20c002ff34f309529a409410694672939e6f9309d646fc5051` |
| `data/square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json` | `ee751ab5d4a528200b4e7328cb72f02be31e6bc5895d8e0bf85bbb302978eb2a` |
