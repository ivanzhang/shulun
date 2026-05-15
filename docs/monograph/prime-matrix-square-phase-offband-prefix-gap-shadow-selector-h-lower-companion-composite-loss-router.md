# Prime Matrix square-phase off-band prefix gap shadow selector H lower companion composite loss router

**状态：** `residue_cap_breakpoint_pressure_reduced_to_companion_composite_loss_floor_open`

本步确认 cap-only 路线不能直接闭合：高段 selector 行中 residue cap 槽数经常已经达到断点。真正剩余是伴随 `m=P+2(b+u)` 必须有足够多合数损耗。精确公式为 `GoodShell=cap_count-composite_loss`，`GoodShell<Bcrit` 等价于 `composite_loss>=max(0,cap_count-Bcrit+1)`。当前 `P>=2001` 重放中 cap 达断点行数为 399，损耗下界失败数为 0，最小损耗余量为 0；全局仍需证明这个伴随合数损耗下界，或把 prime-pair 持久过密登记并排斥为 PDEC/SAE。

```text
max_p=10000
p0=2001
prime_pair_identity_failure_count=0
cap_reaches_breakpoint_count_at_p0=399
loss_floor_failure_count_at_p0=0
min_composite_loss_surplus_to_floor_at_p0=0
max_required_composite_loss_at_p0=62
row_column_unconditional_closed=false
```

## 1. 损耗下界公式

```text
Bcrit=LowSurvivors-ceil(0.43P/logP)+1
GoodShell=residue_cap_slot_count - companion_composite_loss_count
required_loss=max(0, residue_cap_slot_count-Bcrit+1)
safe_condition=companion_composite_loss_count >= required_loss
```

因此若 cap 槽数超过断点，必须由伴随 `m` 合数槽支付差额。

## 2. P 区间账本

| P range | hits | cap reaches Bcrit | min loss surplus | max required loss | max actual loss | max cap | max prime pairs | p at min surplus |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | 90 | -2 | 20 | 26 | 33 | 10 | `[157, 173]` |
| 2001..5000 | 194 | 155 | 0 | 34 | 57 | 71 | 20 | `[2467]` |
| 5001..10000 | 268 | 244 | 12 | 62 | 112 | 127 | 35 | `[5297]` |

## 3. 最紧样本

| loss surplus | shortage | p | side | rho | Bcrit | Good | cap | loss | required loss | loss ratio | required ratio |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 2467 | minus | 7 | 7 | 6 | 34 | 28 | 28 | 0.8235294117647058 | 0.8235294117647058 |
| 12 | 13 | 2243 | plus | 2 | 22 | 9 | 29 | 20 | 8 | 0.6896551724137931 | 0.27586206896551724 |
| 12 | 13 | 2347 | plus | 7 | 18 | 5 | 30 | 25 | 13 | 0.8333333333333334 | 0.43333333333333335 |
| 12 | 13 | 2347 | plus | 7 | 18 | 5 | 30 | 25 | 13 | 0.8333333333333334 | 0.43333333333333335 |
| 12 | 13 | 3767 | plus | 2 | 29 | 16 | 53 | 37 | 25 | 0.6981132075471698 | 0.4716981132075472 |
| 12 | 13 | 5297 | minus | 2 | 34 | 21 | 69 | 48 | 36 | 0.6956521739130435 | 0.5217391304347826 |
| 12 | 13 | 5297 | minus | 2 | 34 | 21 | 69 | 48 | 36 | 0.6956521739130435 | 0.5217391304347826 |
| 13 | 14 | 2027 | minus | 2 | 19 | 5 | 31 | 26 | 13 | 0.8387096774193549 | 0.41935483870967744 |
| 13 | 14 | 2063 | plus | 2 | 22 | 8 | 27 | 19 | 6 | 0.7037037037037037 | 0.2222222222222222 |
| 13 | 14 | 2927 | minus | 2 | 25 | 11 | 44 | 33 | 20 | 0.75 | 0.45454545454545453 |
| 13 | 14 | 2927 | minus | 2 | 25 | 11 | 44 | 33 | 20 | 0.75 | 0.45454545454545453 |
| 14 | 15 | 2267 | minus | 2 | 20 | 5 | 25 | 20 | 6 | 0.8 | 0.24 |
| 15 | 16 | 2207 | minus | 2 | 23 | 7 | 28 | 21 | 6 | 0.75 | 0.21428571428571427 |
| 15 | 16 | 2207 | minus | 2 | 23 | 7 | 28 | 21 | 6 | 0.75 | 0.21428571428571427 |

## 4. 结构判断

- 余数 cap 本身不是最后矛盾点；它经常给出足够多的潜在槽。
- 真正要排斥的是这些潜在槽中伴随 `m` 也持续为素数，导致合数损耗低于必需下界。
- 最紧处损耗余量为 `0`，对应上一层断点缺口 `1`；因此下一步应攻 prime-pair 持久过密或其 PDEC 登记排斥。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `cap_prime_pair_loss_identity` | `closed` | GoodShell equals residue-cap slots minus companion-composite loss, where loss counts cap slots whose m=P+2(b+u) is composite. |
| `breakpoint_loss_floor_equivalence` | `closed` | GoodShell<Bcrit is equivalent to composite_loss >= max(0, cap_count-Bcrit+1). |
| `cap_only_route_insufficient` | `closed_on_current_sweep` | In the current sweep cap_count frequently reaches Bcrit, so the remaining pressure is the companion-composite loss floor. |
| `global_companion_composite_loss_floor` | `open` | A global proof must force enough composite companions inside residue-cap slots, or register persistent prime-pair excess as PDEC/SAE. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CompanionCompositeLossIdentityClosed` | `true` | `true` | GoodShell 精确等于 residue cap 槽数减伴随 m 合数损耗。 | closed |
| `BreakpointLossFloorEquivalenceClosed` | `true` | `false` | 有限重放中损耗下界足以守住断点；全局证明仍缺。 | finite evidence only |
| `CapOnlyEnvelopeClosed` | `false` | `false` | 只靠余数 cap 上界不能闭合，因为 cap 槽数经常超过断点。 | discard as direct closure route |
| `GlobalCompositeLossFloorProved` | `false` | `false` | 仍需全局证明伴随 m 合数损耗下界，或排斥 prime-pair 持久过密。 | SelectorResidueCapCompanionCompositeLossFloorOrPrimePairPersistencePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把余数 cap 同步压力压成伴随合数损耗下界。 | SelectorResidueCapCompanionCompositeLossFloorOrPrimePairPersistencePDEC |

## 7. 下一步

- 主攻：`SelectorResidueCapCompanionCompositeLossFloorOrPrimePairPersistencePDEC`。
- 具体目标：证明 residue cap 槽中的伴随 `m` 合数损耗达到 `max(0,cap_count-Bcrit+1)`，或把损耗不足转成 prime-pair persistence PDEC/SAE 并排斥。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py` | `1e559ec00bf764d861c0ad5a4bde7c3563c27d511a9d9ba2dd46170ae16badc7` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py` | `2b436d80485f8facf51dffb6411bff8c73d56ab36ed99bc0229b1a45911df80e` |
| `experiments/prime_matrix_square_phase_even_layer_interval_router.py` | `9e243ffa1743280677931b841a5227047791d4eaecbcfe3c64e6457394475e90` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json` | `c6d719de684899e3cbe7e153c1c5a063a07cdad9d3d9f1527e3de45e8ae579cc` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json` | `bc6ca5fc07f022b8f24bc7c1b797b0f06cb8872857a5d13770ff19616f27944f` |
