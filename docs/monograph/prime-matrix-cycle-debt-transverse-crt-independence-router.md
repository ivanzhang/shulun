# Prime Matrix cycle-debt transverse CRT independence router

**状态：** `cycle_debt_crt_cover_is_transverse_to_local_period`

上一张 cycle-debt 账本中的 24 个阻断素因子全部与本地周期 5680 互素，且其全局 lcm 与该周期互素。对每个同 residue 列 P(k)=P0+5680*k，复现同一合数等待前缀时，周期平移量 K 必须同时满足 K=0 mod q 的横向 CRT 条件；合并后即 K=0 mod 337212073559813724487421695331234639247。因此该债务包不能由 5680 周期内的局部槽平移吸收，而必须升级为 transverse CRT cover PDEC，或进入真正全局 support-motion SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE
period_p=5680
period_p_factorization={"2": 4, "5": 1, "71": 1}
global_unique_blocker_factor_count=24
transverse_blocker_factor_count=24
all_blocker_factors_coprime_to_period_p=true
global_blocker_lcm=337212073559813724487421695331234639247
gcd_global_blocker_lcm_with_period_p=1
combined_period_equals_product=true
global_lcm_over_period_p_floor=59368322809826359944968608332963844
global_lcm_over_period_p_remainder=5327
global_lcm_over_period_p_log10=34.773554780024
global_lcm_over_total_wait_width_floor=3338733401582314103835858369616184547
global_lcm_over_total_wait_width_log10=36.523581741952
all_row_shift_replay_crt_consistent=true
all_row_shift_replay_classes_zero=true
all_row_lcm_exceeds_phase_support_width=true
row_lcm_exceeds_period_p_count=7
max_row_residue=67
max_row_cycle_debt=15
max_row_blocker_lcm=55140500775337593
max_row_lcm_over_period_p_floor=9707834643545
local_period_absorption_closed_current_certificate=true
next_direct_attack_target=TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE
```

## 1. transverse factor audit

| blocker factor | gcd(q,5680) | inverse of 5680 mod q | transverse unit |
| ---: | ---: | ---: | :---: |
| 3 | 1 | 1 | true |
| 7 | 1 | 5 | true |
| 11 | 1 | 3 | true |
| 13 | 1 | 12 | true |
| 17 | 1 | 9 | true |
| 19 | 1 | 18 | true |
| 23 | 1 | 22 | true |
| 29 | 1 | 7 | true |
| 31 | 1 | 9 | true |
| 37 | 1 | 2 | true |
| 41 | 1 | 28 | true |
| 43 | 1 | 11 | true |
| 47 | 1 | 20 | true |
| 59 | 1 | 48 | true |
| 61 | 1 | 35 | true |
| 67 | 1 | 58 | true |
| 73 | 1 | 26 | true |
| 79 | 1 | 69 | true |
| 83 | 1 | 30 | true |
| 97 | 1 | 9 | true |
| 101 | 1 | 80 | true |
| 113 | 1 | 49 | true |
| 167 | 1 | 84 | true |
| 257 | 1 | 89 | true |

## 2. row replay pressure

| residue | debt width | unique factors | row lcm | gcd(lcm,5680) | lcm>width | shift class |
| ---: | ---: | ---: | ---: | ---: | :---: | ---: |
| 67 | 15 | 11 | 55140500775337593 | 1 | true | 0 |
| 23 | 13 | 10 | 127082193713013 | 1 | true | 0 |
| 17 | 9 | 7 | 183222039 | 1 | true | 0 |
| 58 | 8 | 6 | 26595429 | 1 | true | 0 |
| 20 | 6 | 5 | 310947 | 1 | true | 0 |
| 15 | 7 | 5 | 278103 | 1 | true | 0 |
| 41 | 5 | 4 | 13299 | 1 | true | 0 |
| 8 | 4 | 3 | 2847 | 1 | true | 0 |
| 19 | 4 | 3 | 2451 | 1 | true | 0 |
| 43 | 3 | 3 | 2409 | 1 | true | 0 |
| 16 | 3 | 3 | 861 | 1 | true | 0 |
| 47 | 3 | 3 | 231 | 1 | true | 0 |
| 13 | 1 | 1 | 83 | 1 | true | 0 |
| 57 | 1 | 1 | 67 | 1 | true | 0 |
| 54 | 1 | 1 | 59 | 1 | true | 0 |
| 42 | 2 | 2 | 51 | 1 | true | 0 |
| 2 | 2 | 2 | 33 | 1 | true | 0 |
| 1 | 2 | 2 | 21 | 1 | true | 0 |
| 24 | 2 | 2 | 21 | 1 | true | 0 |
| 62 | 2 | 2 | 21 | 1 | true | 0 |
| 63 | 2 | 2 | 21 | 1 | true | 0 |
| 60 | 1 | 1 | 11 | 1 | true | 0 |
| 64 | 1 | 1 | 7 | 1 | true | 0 |
| 25 | 1 | 1 | 3 | 1 | true | 0 |
| 29 | 1 | 1 | 3 | 1 | true | 0 |
| 49 | 1 | 1 | 3 | 1 | true | 0 |
| 52 | 1 | 1 | 3 | 1 | true | 0 |

## 3. 判定

- `5680=2^4*5*71`，而 24 个阻断素因子均不含 `2,5,71`。
- 因为 `gcd(q,5680)=1`，每个合数等待的阻断不是周期内因子，而是周期坐标上的横向 CRT 条件。
- 对固定 residue 行，复现同一等待前缀的平移量 `K` 必须满足 `K=0 mod row_lcm`；全部 27 行合并为 `K=0 mod global_lcm`。
- 该全局横向模数与 `5680` 互素，组合周期等于两者乘积；因此 local period absorption 在当前证书内关闭。
- 本步仍不宣称行/列命题无条件闭合；剩余是排斥 transverse CRT cover PDEC，或证明 global support-motion SAE 可求和。
- 下一主攻点：`TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json` | `e2731895ab36398581674261c359b074ef71dba80c47601be4992723de15ddd8` |
