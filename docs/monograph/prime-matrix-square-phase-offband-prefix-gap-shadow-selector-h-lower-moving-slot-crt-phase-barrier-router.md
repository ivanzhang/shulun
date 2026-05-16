# Prime Matrix square-phase off-band prefix gap shadow selector H lower moving-slot CRT phase barrier router

**状态：** `fixed_highfactor_slot_patterns_isolated_moving_slot_family_open`

本步把 moving-slot 等号复现进一步压成固定高因子槽图样隔离门。确定性判据是：若 `lpf(m)>7` 槽给出的 CRT 模数大于这些槽共同的相位支撑宽度，则该固定高因子图样至多对应一个 P。当前 `P>=2001` 重放中隔离失败数为 0；唯一等号原子的固定图样也已隔离。但如果 `b,u` 槽随 P 移动，本步只把它登记为下一层 moving family PDEC/ColumnCRT，还不是全局无条件闭合。

```text
max_p=10000
p0=2001
selected_hit_count_at_p0=462
fixed_highfactor_slot_pattern_isolation_failure_count_at_p0=0
equality_atom_fixed_pattern_isolated=true
min_crt_minus_phase_width_at_p0=703
max_phase_width_at_p0=104
moving_slot_family_excluded=false
row_column_unconditional_closed=false
```

## 1. 判据

```text
fixed highfactor pattern isolated if:
  CRT_modulus(lpf(m)>7 slots) > common_phase_width(fixed b/u slots)
then at most one P in that fixed phase support can realize the pattern.
```

## 2. 等号原子屏障记录

| p | side | rho | margin | highfactor | distinct lpf | CRT modulus | phase width | CRT-width | isolated |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | `minus` | 7 | 0 | 8 | 5 | 2404259 | 19 | 2404240 | true |

## 3. 最紧屏障样本

| p | side | rho | template | margin | highfactor | distinct lpf | CRT modulus | phase width | CRT-width | phase support |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2467 | `minus` | 7 | 6 | 0 | 8 | 5 | 2404259 | 19 | 2404240 | `[2460,2478]` |
| 2243 | `plus` | 2 | 4 | 12 | 4 | 3 | 4199 | 17 | 4182 | `[2233,2249]` |
| 5297 | `minus` | 2 | 0 | 12 | 12 | 5 | 3541967 | 17 | 3541950 | `[5291,5307]` |
| 5297 | `minus` | 2 | 5 | 12 | 12 | 5 | 3541967 | 17 | 3541950 | `[5291,5307]` |
| 3767 | `plus` | 2 | 4 | 12 | 6 | 5 | 6079931 | 15 | 6079916 | `[3762,3776]` |
| 2347 | `plus` | 7 | 2 | 12 | 6 | 5 | 15113461 | 29 | 15113432 | `[2330,2358]` |
| 2347 | `plus` | 7 | 3 | 12 | 6 | 5 | 15113461 | 29 | 15113432 | `[2330,2358]` |
| 2063 | `plus` | 2 | 4 | 13 | 3 | 3 | 17719 | 19 | 17700 | `[2048,2066]` |
| 2027 | `minus` | 2 | 5 | 13 | 6 | 5 | 2312167 | 18 | 2312149 | `[2022,2039]` |
| 2927 | `minus` | 2 | 0 | 13 | 7 | 6 | 162216769 | 20 | 162216749 | `[2917,2936]` |
| 2927 | `minus` | 2 | 5 | 13 | 7 | 6 | 162216769 | 20 | 162216749 | `[2917,2936]` |
| 2267 | `minus` | 2 | 5 | 14 | 7 | 6 | 114801401 | 20 | 114801381 | `[2260,2279]` |
| 2647 | `minus` | 7 | 6 | 15 | 4 | 3 | 21793 | 18 | 21775 | `[2646,2663]` |
| 2207 | `minus` | 2 | 0 | 15 | 5 | 4 | 206701 | 25 | 206676 | `[2193,2217]` |
| 2207 | `minus` | 2 | 5 | 15 | 5 | 4 | 206701 | 25 | 206676 | `[2193,2217]` |
| 2687 | `minus` | 2 | 5 | 15 | 7 | 5 | 2608463 | 19 | 2608444 | `[2669,2687]` |
| 2297 | `minus` | 2 | 5 | 15 | 7 | 5 | 2687113 | 3 | 2687110 | `[2297,2299]` |
| 5407 | `minus` | 7 | 6 | 15 | 10 | 7 | 1859834119 | 10 | 1859834109 | `[5400,5409]` |
| 2837 | `minus` | 2 | 5 | 15 | 11 | 7 | 4485482287 | 10 | 4485482277 | `[2834,2843]` |
| 4007 | `minus` | 2 | 5 | 15 | 11 | 7 | 8250466367 | 4 | 8250466363 | `[4007,4010]` |

## 4. 失败形态

当前重放中没有固定高因子槽图样隔离失败。

## 5. 结构判断

- 固定高因子槽图样已经被 CRT 模数/相位宽度屏障孤立。
- 因此持久等号若存在，必须让高因子 `b,u` 槽随 `P` 移动，而不能复用同一固定图样。
- 下一层要么证明 moving-slot family 的 CRT 签名仍不可持续，要么将其作为 `MovingSlot-PDEC/ColumnCRT` 排斥对象。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_highfactor_slot_crt_phase_isolation_criterion` | `closed` | For any fixed highfactor slot pattern, if the CRT modulus from lpf(m)>7 exceeds the common phase-support width, that pattern has at most one P in the phase support. |
| `current_sweep_highfactor_patterns_isolated` | `closed_on_current_sweep` | On the current selector sweep, every highfactor absorber pattern satisfies CRT modulus > phase width; the equality atom is one isolated instance. |
| `moving_slot_family_exclusion` | `open` | A global proof must still exclude recurrence where the highfactor b/u slots themselves move with P, or route that moving family to PDEC/ColumnCRT. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedHighfactorSlotIsolationCriterionClosed` | `true` | `true` | CRT 模数大于相位宽度时，固定高因子槽图样至多命中一个 P。 | closed |
| `CurrentSweepHighfactorPatternsIsolated` | `true` | `false` | 当前重放中所有高因子图样都通过隔离门。 | finite evidence only |
| `CurrentEqualityAtomFixedPatternNonpersistent` | `true` | `true` | 唯一等号原子的固定高因子槽图样已不能复现。 | closed |
| `MovingSlotFamilyExcluded` | `false` | `false` | 槽图样随 P 移动的等号族仍未排斥。 | MovingSlotFamilyPDECOrGlobalResidualPrimeMarginJump |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步不关闭全局行/列命题，只把固定图样持久性压成移动族 PDEC。 | MovingSlotFamilyPDECOrGlobalResidualPrimeMarginJump |

## 8. 下一步

- 主攻：`MovingSlotFamilyPDECOrGlobalResidualPrimeMarginJump`。
- 具体目标：对 moving-slot family 建立统一 CRT 模数增长/相位宽度屏障，或构造正式 `MovingSlot-PDEC/ColumnCRT` 排斥证书。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router.py` | `e1a404fa0ebb30743072fd9b36905fd3a6987ada49ffa3ac1be9229afa4fb303` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py` | `8cfbb81aa5e0744be24413f0f598341a52b2ab155141b751cb6f88096fe292b8` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py` | `1e559ec00bf764d861c0ad5a4bde7c3563c27d511a9d9ba2dd46170ae16badc7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json` | `2eead30b6146d396e58ba12ed94c9edf892b3237c4dc49eb216288ae7be9134e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json` | `f2c69912fe26fc88d0f02df98c514cfa7ba407226b67de20b9b1db98ff8b3b08` |
