# Prime Matrix cycle-debt fresh-cover prime-obstacle router

**状态：** `same_support_fresh_cover_hits_actual_prime_obstacles`

在保持同一 27 个正债务 residue 支撑行的前提下，任一近程平移窗口 K=1..16 都含有真实素数障碍。每个平移窗口有 101 个待覆盖槽，最少也有 17 个素数障碍（K=5），K=16 的全 fresh 窗口仍有 27 个素数障碍。故 fresh moving cover 不能在同一支撑行上重建全合数词；它必须删除实际素数障碍成为 PDEC，或替换支撑行并进入 support-row replacement SAE/PDEC。

```text
row_column_unconditional_closed=false
previous_hardpoint=FreshMovingCoverPDECOrGlobalSupportMotionSAE
period_p=5680
near_shift_limit_cycles=16
positive_cycle_debt_residue_count=27
total_cycle_debt_mass_per_shift=101
tested_shift_count=16
total_tested_same_support_slots=1616
total_prime_obstacles_all_near_shifts=364
total_new_prime_obstacles_all_near_shifts=263
prime_obstacle_density_all_near_shifts=364/1616
all_near_shift_same_support_windows_have_prime_obstacles=true
min_prime_obstacle_count_per_shift=17
min_prime_obstacle_shift=5
min_prime_obstacle_rows_per_shift=12
max_prime_obstacle_count_per_shift=28
max_prime_obstacle_shift=14
shift_1_prime_obstacle_count=27
shift_near_limit_prime_obstacle_count=27
shift_near_limit_new_prime_obstacle_count=27
same_support_fresh_cover_closed_current_certificate=true
support_row_replacement_or_prime_obstacle_pdec_required=true
next_direct_attack_target=FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE
```

## 1. shift obstacle audit

| shift K | prime obstacles | exit primes | new primes | composite slots | rows hit |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 27 | 27 | 0 | 74 | 27 |
| 2 | 20 | 18 | 2 | 81 | 18 |
| 3 | 18 | 12 | 6 | 83 | 17 |
| 4 | 22 | 9 | 13 | 79 | 19 |
| 5 | 17 | 7 | 10 | 84 | 12 |
| 6 | 20 | 6 | 14 | 81 | 14 |
| 7 | 24 | 5 | 19 | 77 | 17 |
| 8 | 22 | 4 | 18 | 79 | 14 |
| 9 | 24 | 3 | 21 | 77 | 16 |
| 10 | 24 | 2 | 22 | 77 | 16 |
| 11 | 20 | 2 | 18 | 81 | 13 |
| 12 | 20 | 2 | 18 | 81 | 13 |
| 13 | 27 | 2 | 25 | 74 | 16 |
| 14 | 28 | 1 | 27 | 73 | 15 |
| 15 | 24 | 1 | 23 | 77 | 13 |
| 16 | 27 | 0 | 27 | 74 | 15 |

## 2. 判定

- 对每个 `K=1..16`，同一 27 行支撑的 fresh window 都含有 actual prime obstacles。
- 最轻窗口仍有 17 个素数障碍；全 fresh 的 `K=16` 窗口有 27 个素数障碍，且全是新素数障碍。
- 因此 same-support fresh cover 已被真实链打断；要继续复现必须删除实际素数障碍，或更换支撑行。
- 本步仍不宣称行/列命题无条件闭合；它把剩余压成 prime-obstacle PDEC 或 support-row replacement SAE/PDEC。
- 下一主攻点：`FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json` | `e2731895ab36398581674261c359b074ef71dba80c47601be4992723de15ddd8` |
| `data/prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json` | `6a8d4fa34bda675b325d10b0f43eef870f2ee24dd62bcbaff25e05433a672c08` |
