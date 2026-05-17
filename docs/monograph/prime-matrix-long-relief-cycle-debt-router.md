# Prime Matrix long relief cycle debt router

**状态：** `long_relief_requires_explicit_ell_cycle_phase_debt`

long-relief 并非简单远端等待，而是固定 ell=71 周期上的显式相位债务：35 个缺失 residue 中只有 8 个在 reset 后第一次相位命中即为素数，其余 27 个必须跨后续周期；总周期债务为 101，恰好等于 full-horizon 中的 101 个合数形式命中。最大债务来自 residue=67，需要等待 15 个完整 71 周期才到 P=98047。

```text
row_column_unconditional_closed=false
previous_hardpoint=AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE
ell=71
period_p=5680
missing_nonzero_count=35
zero_cycle_relief_count=8
positive_cycle_debt_residue_count=27
total_cycle_debt=101
total_composite_wait_count=101
matches_full_horizon_composite_missing_count=true
max_cycle_debt=15
max_cycle_debt_residue=67
max_cycle_debt_p_delay=85200
periods_touched_until_full_relief=16
next_direct_attack_target=LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability
```

## 1. cycle-debt rows

| residue | first formal P | first prime P | cycle debt | composite waits |
| ---: | ---: | ---: | ---: | ---: |
| 67 | 12847 | 98047 | 15 | 15 |
| 23 | 13087 | 86927 | 13 | 13 |
| 17 | 14927 | 66047 | 9 | 9 |
| 58 | 12767 | 58207 | 8 | 8 |
| 15 | 13647 | 53407 | 7 | 7 |
| 20 | 11167 | 45247 | 6 | 6 |
| 41 | 13247 | 41647 | 5 | 5 |
| 8 | 14847 | 37567 | 4 | 4 |
| 19 | 10527 | 33247 | 4 | 4 |
| 16 | 14287 | 31327 | 3 | 3 |
| 43 | 14527 | 31567 | 3 | 3 |
| 47 | 11407 | 28447 | 3 | 3 |
| 1 | 10367 | 21727 | 2 | 2 |
| 2 | 11007 | 22367 | 2 | 2 |
| 24 | 13727 | 25087 | 2 | 2 |
| 42 | 13887 | 25247 | 2 | 2 |
| 62 | 15327 | 26687 | 2 | 2 |
| 63 | 10287 | 21647 | 2 | 2 |
| 13 | 12367 | 18047 | 1 | 1 |
| 25 | 14367 | 20047 | 1 | 1 |
| 29 | 11247 | 16927 | 1 | 1 |
| 49 | 12687 | 18367 | 1 | 1 |
| 52 | 14607 | 20287 | 1 | 1 |
| 54 | 10207 | 15887 | 1 | 1 |
| 57 | 12127 | 17807 | 1 | 1 |
| 60 | 14047 | 19727 | 1 | 1 |
| 64 | 10927 | 16607 | 1 | 1 |
| 6 | 13567 | 13567 | 0 | 0 |
| 14 | 13007 | 13007 | 0 | 0 |
| 30 | 11887 | 11887 | 0 | 0 |
| 31 | 12527 | 12527 | 0 | 0 |
| 33 | 13807 | 13807 | 0 | 0 |
| 50 | 13327 | 13327 | 0 | 0 |
| 68 | 13487 | 13487 | 0 | 0 |
| 70 | 14767 | 14767 | 0 | 0 |

## 2. 判定

- 每个 cycle debt 都是一整段 `71` 同 residue 周期的素数锚等待。
- `total_cycle_debt=101` 与 full-horizon 账本中的合数形式命中数完全相等。
- 最大单点债务是 `residue=67`，从首次形式命中到真实素数锚相差 `85200`。
- 因此 long-relief 分支必须解释长期相位等待，而不是只解释 endpoint 外延。
- 下一主攻点：`LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json` | `d3d3ef44e7f59396feb07cbbc0baddda7b986c1fcdee64f403bae838d7e5284b` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
| `data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json` | `52c01ff7e8af247a37b25f5d3266debadd3bdc4ae79ad5cc604fb920fa5d108c` |
