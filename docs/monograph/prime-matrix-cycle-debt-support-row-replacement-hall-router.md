# Prime Matrix cycle-debt support-row replacement Hall router

**状态：** `support_row_replacement_hall_capacity_fails_except_k13_k14`

把 support-row replacement 写成 35 个缺失 residue 候选行对 27 个正债务需求行的 Hall 容量问题。对每个近程相位 K，候选行容量为从 K 开始最长连续 composite 段，需求为原债务长度。16 个相位中有 14 个直接违反 Hall 阈值容量，只剩 K=13,14。这两个幸存相位也必须调用 immediate-relief 行并进行大规模支撑行替换，成为新的窄 PDEC/SAE 接口。

```text
row_column_unconditional_closed=false
previous_hardpoint=FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE
period_p=5680
near_shift_limit_cycles=16
candidate_missing_residue_count=35
needed_positive_debt_row_count=27
total_demand_width=101
max_required_width=15
hall_fail_shift_count=14
hall_fail_shifts=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16]
hall_survivor_shift_count=2
hall_survivor_shifts=[13, 14]
all_but_k13_k14_fail_hall_capacity=true
k13_assigned_immediate_relief_rows=6
k14_assigned_immediate_relief_rows=8
support_row_replacement_closed_except_k13_k14_current_certificate=true
next_direct_attack_target=K13K14SupportReplacementSurvivorPDECOrGlobalSAE
```

## 1. shift Hall audit

| shift K | Hall pass | min slack | first defect | total capacity | immediate rows used | replacements |
| ---: | :---: | ---: | --- | ---: | ---: | ---: |
| 1 | false | -1 | t=1: 26-27=-1 | 96 | 0 | 0 |
| 2 | false | -1 | t=6: 5-6=-1 | 99 | 0 | 0 |
| 3 | false | -2 | t=1: 25-27=-2 | 87 | 0 | 0 |
| 4 | false | -5 | t=1: 22-27=-5 | 76 | 0 | 0 |
| 5 | false | -2 | t=6: 5-6=-1 | 104 | 0 | 0 |
| 6 | false | -2 | t=5: 6-7=-1 | 90 | 0 | 0 |
| 7 | false | -3 | t=1: 25-27=-2 | 82 | 0 | 0 |
| 8 | false | -2 | t=8: 3-4=-1 | 97 | 0 | 0 |
| 9 | false | -2 | t=1: 25-27=-2 | 98 | 0 | 0 |
| 10 | false | -2 | t=1: 25-27=-2 | 106 | 0 | 0 |
| 11 | false | -1 | t=6: 5-6=-1 | 121 | 0 | 0 |
| 12 | false | -2 | t=1: 26-27=-1 | 107 | 0 | 0 |
| 13 | true | 0 | - | 119 | 6 | 26 |
| 14 | true | 0 | - | 132 | 8 | 27 |
| 15 | false | -1 | t=6: 5-6=-1 | 120 | 0 | 0 |
| 16 | false | -2 | t=1: 25-27=-2 | 111 | 0 | 0 |

## 2. survivor assignments

Only `K=13,14` pass the Hall capacity test.  Their assignments are retained in the JSON ledger.

| shift K | total capacity | min slack | immediate rows used | replacements |
| ---: | ---: | ---: | ---: | ---: |
| 13 | 119 | 0 | 6 | 26 |
| 14 | 132 | 0 | 8 | 27 |

## 3. 判定

- 对每个阈值 `t`，Hall 条件是 `candidate rows with capacity>=t >= demand rows with debt>=t`。
- 16 个近程相位中 14 个直接违反该条件，故 support-row replacement 容量不足。
- 仅 `K=13,14` 存活；它们必须调用 immediate-relief 行并进行大规模支撑行替换。
- 本步仍不宣称行/列命题无条件闭合；它把剩余压成 `K=13,14` 两个幸存相位的 PDEC/SAE。
- 下一主攻点：`K13K14SupportReplacementSurvivorPDECOrGlobalSAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json` | `e2731895ab36398581674261c359b074ef71dba80c47601be4992723de15ddd8` |
| `data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json` | `52c01ff7e8af247a37b25f5d3266debadd3bdc4ae79ad5cc604fb920fa5d108c` |
| `data/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json` | `343ddce201b1f69189726670d132f957d7330d2724bb7c40dc9e80a9e8dd82a3` |
