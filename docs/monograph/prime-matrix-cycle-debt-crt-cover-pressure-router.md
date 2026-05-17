# Prime Matrix cycle-debt CRT cover pressure router

**状态：** `cycle_debt_requires_large_crt_cover_pressure`

27 个正周期债务 residue 的合数等待可写成周期坐标 k 上的 CRT 阻断覆盖。所有阻断最小素因子合并后共有 24 个不同素因子，整体 lcm 为 337212073559813724487421695331234639247，远大于本地 P 周期 5680。最大压力行是 residue=67：15 个等待周期由 11 个不同阻断素因子覆盖，单行 lcm 为 55140500775337593。因此周期债务若作为全局族复现，必须携带大 CRT 相位包，而不能被视为局部自由 support motion。

```text
row_column_unconditional_closed=false
previous_hardpoint=OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE
ell=71
period_p=5680
positive_cycle_debt_residue_count=27
total_composite_waits=101
global_unique_blocker_factor_count=24
global_blocker_lcm=337212073559813724487421695331234639247
global_blocker_product_log10=38.527903115735
max_row_residue=67
max_row_cycle_debt=15
max_row_blocker_lcm=55140500775337593
crt_cover_modulus_exceeds_local_period=true
next_direct_attack_target=CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE
```

## 1. pressure rows

| residue | debt | unique factors | blocker lcm | first prime P |
| ---: | ---: | ---: | ---: | ---: |
| 67 | 15 | 11 | 55140500775337593 | 98047 |
| 23 | 13 | 10 | 127082193713013 | 86927 |
| 17 | 9 | 7 | 183222039 | 66047 |
| 58 | 8 | 6 | 26595429 | 58207 |
| 20 | 6 | 5 | 310947 | 45247 |
| 15 | 7 | 5 | 278103 | 53407 |
| 41 | 5 | 4 | 13299 | 41647 |
| 8 | 4 | 3 | 2847 | 37567 |
| 19 | 4 | 3 | 2451 | 33247 |
| 43 | 3 | 3 | 2409 | 31567 |
| 16 | 3 | 3 | 861 | 31327 |
| 47 | 3 | 3 | 231 | 28447 |
| 13 | 1 | 1 | 83 | 18047 |
| 57 | 1 | 1 | 67 | 17807 |
| 54 | 1 | 1 | 59 | 15887 |
| 42 | 2 | 2 | 51 | 25247 |
| 2 | 2 | 2 | 33 | 22367 |
| 1 | 2 | 2 | 21 | 21727 |
| 24 | 2 | 2 | 21 | 25087 |
| 62 | 2 | 2 | 21 | 26687 |
| 63 | 2 | 2 | 21 | 21647 |
| 60 | 1 | 1 | 11 | 19727 |
| 64 | 1 | 1 | 7 | 16607 |
| 25 | 1 | 1 | 3 | 20047 |
| 29 | 1 | 1 | 3 | 16927 |
| 49 | 1 | 1 | 3 | 18367 |
| 52 | 1 | 1 | 3 | 20287 |

## 2. 判定

- 每个合数等待都是周期坐标 `k` 上的一个 CRT 阻断类。
- 27 个正债务 residue 合并后需要 `24` 个不同阻断素因子。
- 全局阻断 lcm 远大于本地 `P` 周期 `5680`，所以复现该债务需要大 CRT 相位包。
- 本步不排斥所有大 CRT 包；它把剩余命名为 cycle-debt CRT cover PDEC 或全局 support-motion SAE。
- 下一主攻点：`CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json` | `d3d3ef44e7f59396feb07cbbc0baddda7b986c1fcdee64f403bae838d7e5284b` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
| `data/prime-matrix-one-period-relief-deficit-ledger.json` | `9769e5804e151090153adcf1fe08dcfcf65270ae3229e1a2ff2eefc6676dd753` |
