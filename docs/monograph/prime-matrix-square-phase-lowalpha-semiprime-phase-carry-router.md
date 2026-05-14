# Prime Matrix square-phase low-alpha semiprime 相位 carry 路由

**状态：** `semiprime_fiber_phase_reduced_to_reciprocal_carry_discrepancy_open`

semiprime 单纤维的非空事件已精确改写成 reciprocal carry：`b` 区间非空当且仅当 `floor((P^2+P-1)/(qa))-floor(P^2/(qa))=1`，等价于余数阈值 `(P^2 mod qa)+P-1>=qa`。因此相位非空过密不再是抽象统计现象，而是倒数 floor-carry 的 sawtooth 偏差。样本公式零失败；剩余是证明 carry_count 相对 phase_mass 的统一偏差界，或把失败登记为 reciprocal-carry/PDEC。

```text
carry_formula_closed=true
fractional_threshold_identity_closed=true
reciprocal_carry_discrepancy_bound_proved=false
reciprocal_carry_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局 carry 账本

| q axes | phase mass | carry count | carry/phase | signed discrepancy |
| ---: | ---: | ---: | ---: | ---: |
| 171 | 43652.759461 | 43666 | 1.000303 | 13.240539 |

## 2. 最热 q 轴

| type | record |
| --- | --- |
| positive discrepancy | `{'q': 173, 'h': 1156.086705202312, 'a_interval': [1157, 15205], 'phase_mass': 355.5208527694025, 'carry_count': 385, 'carry_over_phase': 1.0829181945333548, 'signed_discrepancy': 29.479147230597505, 'absolute_discrepancy_sum': 459.2557415232906, 'formula_failure_count': 0, 'carry_value_failure_count': 0, 'top_carry_sample': {'a': 1163, 'b_interval': [198815, 198815], 'width': 0.9940556364594257, 'residue': 22023, 'modulus': 201199}}` |
| carry/phase | `{'q': 73, 'h': 137.08219178082192, 'a_interval': [138, 1171], 'phase_mass': 47.791289800447515, 'carry_count': 57, 'carry_over_phase': 1.1926859525659057, 'signed_discrepancy': 9.208710199552485, 'absolute_discrepancy_sum': 57.38698247059022, 'formula_failure_count': 0, 'carry_value_failure_count': 0, 'top_carry_sample': {'a': 139, 'b_interval': [9869, 9869], 'width': 0.9862028185670642, 'residue': 9453, 'modulus': 10147}}` |

## 3. 每个 P 的总结

| P | carry count | phase mass | carry/phase | signed discrepancy |
| ---: | ---: | ---: | ---: | ---: |
| 10007 | 777 | 758.466434 | 1.024436 | 18.533566 |
| 36739 | 4013 | 4038.220486 | 0.993755 | -25.220486 |
| 83561 | 10697 | 10669.116406 | 1.002613 | 27.883594 |
| 200003 | 28179 | 28186.956135 | 0.999718 | -7.956135 |

## 4. 证明边界

- 已闭合：纤维非空与 reciprocal carry/fractional-threshold 完全等价。
- 未闭合：carry_count 相对 phase_mass 的统一偏差界。
- 未闭合：若 carry 偏差持续过大，对应 reciprocal-carry/PDEC 的排除。
- 未闭合：非空纤维上的素性密度上界。
- 下一目标：`ReciprocalCarryDiscrepancyBoundForSemiprimeFibersOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.json` | `1543e8024672a1bd3afa5e41611c42418553241740fc69accf21f8de233af990` |
| `docs/monograph/prime-matrix-square-phase-reciprocal-floor-congruence-ledger.json` | `3f5419e1fb07546e1b4607cc47187620a3ef95672e564b414db4ae80426a260b` |
| `experiments/prime_matrix_square_phase_lowalpha_semiprime_phase_carry_router.py` | `914503dd603c9c205e362b3844195966af2d6c41e9831528e645cc3a951da71a` |
