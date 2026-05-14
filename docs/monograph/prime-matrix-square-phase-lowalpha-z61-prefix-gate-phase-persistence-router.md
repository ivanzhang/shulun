# Prime Matrix square-phase low-alpha z=61 PrefixGate 相位持久性

**状态：** `z61_prefix_gate_phase_persistence_is_signed_not_absent_open`

已登记相位 `b≡0 mod 28842` 不能通过“样本中不存在”排斥：它在 `p=36739` 的负 profile 中出现一次，在 `p=200003` 的正 profile 中出现两次。因此 PrefixGate-PDEC 的下一最窄形态不是相位缺席，而是 signed phase balance：证明正 profile 中同相位贡献足以吸收负缺陷，或证明持久同相位偏斜形成可排斥的 PDEC。

```text
phase_condition=b ≡ 0 (mod 28842)
phase_hit_profile_count=2
phase_hit_total_multiplicity=3
phase_hits_by_sign={'negative': 1, 'positive': 2, 'zero': 0}
negative_phase_actual=0.555427
positive_phase_actual=1.110853
positive_over_negative_phase_actual=2.000000
prefix_gate_signed_phase_balance_proved=false
row_column_unconditional_closed=false
```

## 1. Profile 相位命中

| p | sign | linear | phase hits | phase mult | phase actual | phase share actual |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 10007 | `negative` | -1.576550 | 0 | 0 | 0.000000 | 0.000000 |
| 36739 | `negative` | -1.985602 | 1 | 1 | 0.555427 | 0.067962 |
| 83561 | `positive` | 7.257244 | 0 | 0 | 0.000000 | 0.000000 |
| 200003 | `positive` | 2.455029 | 2 | 2 | 1.110853 | 0.015055 |

## 2. 命中明细

| p | b | quotient | mult | target moduli | contribution |
| ---: | ---: | ---: | ---: | --- | ---: |
| 36739 | 28842 | 1 | 1 | `[9614, 14421]` | 0.555427 |
| 200003 | 57684 | 2 | 1 | `[9614, 14421]` | 0.555427 |
| 200003 | 115368 | 4 | 1 | `[9614, 14421]` | 0.555427 |

## 3. 证明边界

- 已闭合：PrefixGate-PDEC 相位的样本持久性与符号路由账本。
- 未闭合：signed phase balance 全局证明，或 PersistentPhase-PDEC 排斥。
- 下一目标：`PrefixGateSignedPhaseBalanceOrPersistentPhasePDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json` | `23bc56d8d9a7bb56e2dda988ad66df5d49fa7e51e00bef1f81adc6cbae146523` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_phase_persistence_router.py` | `4a75b84a1c7893d4e387963124f90ea736c282004db40d43267568146c1256c4` |
