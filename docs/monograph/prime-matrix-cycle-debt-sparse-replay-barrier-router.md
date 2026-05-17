# Prime Matrix cycle-debt sparse replay barrier router

**状态：** `exact_transverse_crt_replay_is_sparse_or_moving_pdec`

横向 CRT cover 若保持同一阻断图 exact replay，则完整 debt word 的下一次复现必须相隔 337212073559813724487421695331234639247 个 residue 周期，即 P 距离 1915364577819741955088555229481412750922960。而当前 full-relief 可见跨度只有 1102/71 个周期，向上取整为 16。因此任意短于 global_lcm 的局部/中程 support-motion 窗口至多包含一份完整复本；exact 分支是稀疏 SAE 型。若反例链需要高频复现，就不能保持同一 CRT cover，而必须移动阻断素因子或相位类，进入 moving transverse cover PDEC。

```text
row_column_unconditional_closed=false
previous_hardpoint=TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE
period_p=5680
ell=71
global_exact_replay_cycle_modulus=337212073559813724487421695331234639247
global_exact_replay_p_gap=1915364577819741955088555229481412750922960
global_exact_replay_density_log10=-38.527903115735
max_cycle_debt_support_width=15
total_composite_wait_width=101
full_relief_step_gap_after_reset=1102
full_relief_cycle_span=1102/71
full_relief_cycle_span_ceiling=16
global_dead_gap_cycles_after_debt_word=337212073559813724487421695331234639232
global_modulus_over_max_debt_width_floor=22480804903987581632494779688748975949
global_modulus_over_total_wait_width_floor=3338733401582314103835858369616184547
global_modulus_over_full_cycle_span_ceiling_floor=21075754597488357780463855958202164952
global_p_gap_over_full_relief_p_gap_floor=21726004739334641051367459499562304343
single_full_debt_copy_per_full_relief_horizon=true
rows_with_replay_modulus_exceeding_own_debt=27
rows_with_replay_modulus_exceeding_total_waits=12
rows_with_single_copy_in_full_horizon=21
exact_replay_branch_is_sae_sparse_current_certificate=true
non_sparse_persistence_forces_moving_blocker_map=true
next_direct_attack_target=SparseReplaySAEOrMovingTransverseCoverPDEC
```

## 1. row replay audit

| residue | debt | replay modulus | dead gap cycles | replay P gap | single in full horizon |
| ---: | ---: | ---: | ---: | ---: | :---: |
| 67 | 15 | 55140500775337593 | 55140500775337578 | 313198044403917528240 | true |
| 23 | 13 | 127082193713013 | 127082193713000 | 721826860289913840 | true |
| 17 | 9 | 183222039 | 183222030 | 1040701181520 | true |
| 58 | 8 | 26595429 | 26595421 | 151062036720 | true |
| 20 | 6 | 310947 | 310941 | 1766178960 | true |
| 15 | 7 | 278103 | 278096 | 1579625040 | true |
| 41 | 5 | 13299 | 13294 | 75538320 | true |
| 8 | 4 | 2847 | 2843 | 16170960 | true |
| 19 | 4 | 2451 | 2447 | 13921680 | true |
| 43 | 3 | 2409 | 2406 | 13683120 | true |
| 16 | 3 | 861 | 858 | 4890480 | true |
| 47 | 3 | 231 | 228 | 1312080 | true |
| 13 | 1 | 83 | 82 | 471440 | true |
| 57 | 1 | 67 | 66 | 380560 | true |
| 54 | 1 | 59 | 58 | 335120 | true |
| 42 | 2 | 51 | 49 | 289680 | true |
| 2 | 2 | 33 | 31 | 187440 | true |
| 1 | 2 | 21 | 19 | 119280 | true |
| 24 | 2 | 21 | 19 | 119280 | true |
| 62 | 2 | 21 | 19 | 119280 | true |
| 63 | 2 | 21 | 19 | 119280 | true |
| 60 | 1 | 11 | 10 | 62480 | false |
| 64 | 1 | 7 | 6 | 39760 | false |
| 25 | 1 | 3 | 2 | 17040 | false |
| 29 | 1 | 3 | 2 | 17040 | false |
| 49 | 1 | 3 | 2 | 17040 | false |
| 52 | 1 | 3 | 2 | 17040 | false |

## 2. 判定

- exact replay 保持同一阻断图时，完整 debt word 的平移量必须是全局横向 lcm 的倍数。
- 当前 full-relief horizon 只有 `ceil(1102/71)=16` 个 residue 周期；完整复现间距远超该窗口。
- 因此 exact 分支只能作为孤立稀疏复本计入 SAE；它不能提供高频容量补偿。
- 若反例链要求在短窗口或正密度中持续复现，就必须改变阻断素因子、阻断相位或行组合，形成 moving transverse cover PDEC。
- 本步仍不宣称行/列命题无条件闭合；它把剩余压成 sparse SAE 与 moving-cover PDEC 的二分。
- 下一主攻点：`SparseReplaySAEOrMovingTransverseCoverPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-transverse-crt-independence-ledger.json` | `f8fa7ddd7e2c0c3388c086e85ffd5ae3db449c27102a47ad1bb0ebe0292f4de9` |
| `data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json` | `e2731895ab36398581674261c359b074ef71dba80c47601be4992723de15ddd8` |
| `data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json` | `52c01ff7e8af247a37b25f5d3266debadd3bdc4ae79ad5cc604fb920fa5d108c` |
