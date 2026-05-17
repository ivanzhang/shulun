# Prime Matrix one-period relief deficit router

**状态：** `one_period_relief_capacity_deficit_materialized`

reset 后第一个完整 ell=71 周期已经让 35 个缺失非零 residue 全部形式命中一次，但只有 8 个命中为实际素数 relief；其余 27 个全部是合数形式命中，恰好对应正周期债务 residue 数。同时该周期还有 10 个 repeat prime anchor。因此一个 reset-local 周期存在明确 relief 容量缺口，必须进入后续周期债务。

```text
row_column_unconditional_closed=false
previous_hardpoint=LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability
ell=71
period_p=5680
period_step_range=90..160
period_p_range=9887..15487
period_is_complete_residue_cycle=true
missing_nonzero_required=35
formal_missing_hit_count=35
actual_relief_count_in_one_period=8
composite_missing_count_in_one_period=27
repeat_prime_anchor_count_in_one_period=10
relief_deficit_after_one_period=27
next_direct_attack_target=OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE
```

## 1. actual relief rows in one period

| step | P | residue |
| ---: | ---: | ---: |
| 115 | 11887 | 30 |
| 123 | 12527 | 31 |
| 129 | 13007 | 14 |
| 133 | 13327 | 50 |
| 135 | 13487 | 68 |
| 136 | 13567 | 6 |
| 139 | 13807 | 33 |
| 151 | 14767 | 70 |

## 2. 判定

- 一个完整 residue 周期内，形式上 35 个缺失非零 residue 全部出现。
- 实际素数 relief 只有 `8` 个，因此一周期后仍缺 `27` 个。
- `27` 个合数形式命中正好是上一张 cycle-debt 证书中的正周期债务 residue。
- 同周期还有 `10` 个 repeat prime-anchor，继续增加 reset/旧容量压力。
- 下一主攻点：`OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json` | `d3d3ef44e7f59396feb07cbbc0baddda7b986c1fcdee64f403bae838d7e5284b` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
| `data/prime-matrix-long-relief-cycle-debt-ledger.json` | `9c56e1cb9d3dd20d0115634b9a53a2d9f1b4b42bef8a20dd633a52dda505b090` |
