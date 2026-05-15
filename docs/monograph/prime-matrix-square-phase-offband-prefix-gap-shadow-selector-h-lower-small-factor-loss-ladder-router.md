# Prime Matrix square-phase off-band prefix gap shadow selector H lower small-factor loss ladder router

**状态：** `companion_composite_loss_floor_reduced_to_small_factor_loss_ladder_open`

本步把伴随合数损耗进一步分解为 least-prime-factor 小因子阶梯。当前 `P>=2001` 重放中，损耗余量为 0 的贴边行只有 1 个；`lpf(m)<=7` 只在 1 个高段行不足，而 `lpf(m)<=43` 的小因子损耗已覆盖全部行，失败数为 0。这说明当前有限障碍集中在小模 CRT 覆盖，而不是大素数尾项；但固定 43 不能当作全局定理，严格闭合仍需自足证明自适应小因子损耗下界，或排斥 large-prime companion persistence PDEC/SAE。

```text
max_p=10000
p0=2001
zero_composite_loss_surplus_count_at_p0=1
max_exact_required_lpf_cutoff_at_p0=43
failure_count_at_lpf7_at_p0=1
min_surplus_at_lpf7_at_p0=-8
failure_count_at_lpf43_at_p0=0
min_surplus_at_lpf43_at_p0=0
row_column_unconditional_closed=false
```

## 1. 阶梯判据

对每个 residue cap 合数槽，记 `lpf(m)` 为伴随 `m=P+2(b+u)` 的最小素因子。若

```text
# {cap slots with lpf(m)<=y} >= max(0, cap_count-Bcrit+1),
```

则该行的伴随合数损耗下界已经由 `<=y` 的小素因子完全支付。

## 2. 阈值汇总

| y | failure count at p0 | min surplus | failure P sample |
| ---: | ---: | ---: | --- |
| 3 | 62 | -31 | `[2027, 2297, 2467, 2477, 2557, 2647, 2837, 2927, 3307, 3607, 3617, 3767, 3797, 3803, 4007, 4177, 4327, 4567, 4597, 4657]` |
| 5 | 12 | -9 | `[2467, 3797, 4007, 4567, 5297, 5807, 7547, 8117]` |
| 7 | 1 | -8 | `[2467]` |
| 11 | 1 | -6 | `[2467]` |
| 13 | 1 | -5 | `[2467]` |
| 17 | 1 | -3 | `[2467]` |
| 19 | 1 | -3 | `[2467]` |
| 23 | 1 | -1 | `[2467]` |
| 29 | 1 | -1 | `[2467]` |
| 31 | 1 | -1 | `[2467]` |
| 37 | 1 | -1 | `[2467]` |
| 41 | 1 | -1 | `[2467]` |
| 43 | 0 | 0 | `[]` |
| 47 | 0 | 0 | `[]` |
| 53 | 0 | 0 | `[]` |
| 59 | 0 | 0 | `[]` |
| 67 | 0 | 0 | `[]` |
| 71 | 0 | 0 | `[]` |
| 83 | 0 | 0 | `[]` |
| 97 | 0 | 0 | `[]` |

## 3. P 区间账本

| P range | hits | max needed lpf | min surplus y=7 | fails y=7 | min surplus y=43 | fails y=43 | p at max cutoff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | 29 | -6 | 21 | -2 | 11 | `[863]` |
| 2001..5000 | 194 | 43 | -8 | 1 | 0 | 0 | `[2467]` |
| 5001..10000 | 268 | 7 | 0 | 0 | 11 | 0 | `[5297, 5807, 7547, 8117]` |

## 4. 最紧样本

| p | side | rho | Bcrit | Good | cap | required loss | actual loss | loss surplus | needed lpf | loss<=7 | surplus<=7 | loss<=43 | surplus<=43 |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | minus | 7 | 7 | 6 | 34 | 28 | 28 | 0 | 43 | 20 | -8 | 28 | 0 |
| 5297 | minus | 2 | 34 | 21 | 69 | 36 | 48 | 12 | 7 | 36 | 0 | 47 | 11 |
| 5297 | minus | 2 | 34 | 21 | 69 | 36 | 48 | 12 | 7 | 36 | 0 | 47 | 11 |
| 4007 | minus | 2 | 31 | 15 | 56 | 26 | 41 | 15 | 7 | 30 | 4 | 39 | 13 |
| 4567 | minus | 7 | 37 | 20 | 70 | 34 | 50 | 16 | 7 | 35 | 1 | 47 | 13 |
| 3797 | plus | 2 | 31 | 13 | 49 | 19 | 36 | 17 | 7 | 22 | 3 | 33 | 14 |
| 5807 | minus | 2 | 41 | 17 | 82 | 42 | 65 | 23 | 7 | 45 | 3 | 61 | 19 |
| 5807 | minus | 2 | 41 | 17 | 82 | 42 | 65 | 23 | 7 | 45 | 3 | 61 | 19 |
| 8117 | minus | 2 | 51 | 24 | 106 | 56 | 82 | 26 | 7 | 59 | 3 | 76 | 20 |
| 8117 | minus | 2 | 51 | 24 | 106 | 56 | 82 | 26 | 7 | 59 | 3 | 76 | 20 |
| 7547 | minus | 2 | 47 | 19 | 108 | 62 | 89 | 27 | 7 | 66 | 4 | 82 | 20 |
| 7547 | minus | 2 | 47 | 19 | 108 | 62 | 89 | 27 | 7 | 66 | 4 | 82 | 20 |

## 5. 结构判断

- 当前贴边原子唯一：`P=2467, minus, rho=7`，要求 28 个合数损耗且实际正好 28 个。
- 除该贴边原子外，`lpf(m)<=7` 的小模层已经足够支付高段损耗下界。
- 加入 `11..43` 的有限小模层后，当前高段全部通过；这给下一步 CRT 小模覆盖证明提供了最窄输入形状。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `small_factor_loss_ladder_identity` | `closed` | For any threshold y, the y-small-factor loss is the number of residue-cap slots whose companion m has least prime factor <=y. |
| `finite_lpf43_loss_floor` | `closed_on_current_sweep` | On the current P>=2001 sweep, y=43 covers the required composite-loss floor for every selector row. |
| `finite_lpf7_single_exception` | `closed_on_current_sweep` | On the current P>=2001 sweep, y=7 fails only at the exact boundary row P=2467, minus, rho=7. |
| `global_small_factor_loss_floor` | `open` | A global proof must derive an adaptive small-factor CRT loss floor, or route persistent large-prime companions to PDEC/SAE. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SmallFactorLossLadderMaterialized` | `true` | `true` | 伴随合数损耗已按 least-prime-factor 阶梯精确拆分。 | closed |
| `CurrentLPF43LossFloorClosed` | `true` | `false` | 有限重放中 lpf<=43 足以支付全部损耗下界；这不是全局证明。 | finite evidence only |
| `CurrentLPF7SingleExceptionIdentified` | `true` | `false` | lpf<=7 的唯一高段失败是贴边行 P=2467, minus, rho=7。 | finite boundary atom |
| `GlobalSmallFactorLossFloorProved` | `false` | `false` | 仍需从 CRT 小模覆盖/层叠筛推出全局小因子损耗下界。 | SelectorResidueCapSmallFactorLossFloorOrLargePrimeCompanionPersistencePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把合数损耗下界压成小因子阶梯。 | SelectorResidueCapSmallFactorLossFloorOrLargePrimeCompanionPersistencePDEC |

## 8. 下一步

- 主攻：`SelectorResidueCapSmallFactorLossFloorOrLargePrimeCompanionPersistencePDEC`。
- 具体目标：把 `lpf(m)<=y` 的小模 CRT 覆盖计数转成自足下界；若无法全局覆盖，则把大素数伴随 `m` 的持续素性登记为 PDEC/SAE。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router.py` | `54a77f6a45dd3ed78d6b8824e9ab23834d8884f4968bfe3f80370fe136d20661` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py` | `1e559ec00bf764d861c0ad5a4bde7c3563c27d511a9d9ba2dd46170ae16badc7` |
| `experiments/prime_matrix_square_phase_even_layer_interval_router.py` | `9e243ffa1743280677931b841a5227047791d4eaecbcfe3c64e6457394475e90` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json` | `bc6ca5fc07f022b8f24bc7c1b797b0f06cb8872857a5d13770ff19616f27944f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json` | `ddaceee541d8f99a44cc1cebe474ff6daf11e13d8587f84295a64cdab68af3cd` |
