# Prime Matrix square-phase low-alpha semiprime phase sawtooth 路由

**状态：** `reciprocal_carry_discrepancy_reduced_to_sawtooth_sum_open`

semiprime fiber 的 carry 偏差已化为精确 sawtooth 恒等式。对 `m=qa`，有 `carry-(P-1)/m={P^2/m}-{(P^2+P-1)/m}`，同时 `carry-P/m` 只多一个 `-1/m` 校正。因此相位异常必须表现为倒数端点分数部差的低频或局部集中；样本恒等式零失败。剩余是证明这些 sawtooth 和的统一界，或登记为 reciprocal-sawtooth/PDEC。

```text
sawtooth_identity_closed=true
identity_failure_count=0
reciprocal_sawtooth_bound_proved=false
reciprocal_sawtooth_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局 sawtooth 账本

| q axes | carry | phase P/m | carry/phase | saw P sum | saw exact sum |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 43666 | 43652.759461 | 1.000303 | 13.240539 | 13.694862 |

## 2. 最热 q 轴

| record |
| --- |
| `{'q': 311, 'a_interval': [644, 11341], 'carry_count': 194, 'phase_p': 232.40238177955987, 'phase_p_minus_1': 232.4012197850813, 'signed_discrepancy_vs_p_phase': -38.402381779559875, 'signed_discrepancy_vs_exact_phase': -38.40121978508131, 'saw_p_sum': -38.40238177955994, 'saw_exact_sum': -38.40121978508086, 'identity_failure_count': 0, 'top_abs_saw_sample': {'a': 677, 'modulus': 210547, 'carry': 0, 'phase_p': 0.9499209202695835, 'saw_p': -0.9499209202695836, 'residue_left': 7120, 'residue_right': 207122}}` |

## 3. 每个 P 的总结

| P | carry | phase P/m | saw P sum | saw exact sum |
| ---: | ---: | ---: | ---: | ---: |
| 10007 | 777 | 758.466434 | 18.533566 | 18.609360 |
| 36739 | 4013 | 4038.220486 | -25.220486 | -25.110569 |
| 83561 | 10697 | 10669.116406 | 27.883594 | 28.011274 |
| 200003 | 28179 | 28186.956135 | -7.956135 | -7.815202 |

## 4. 证明边界

- 已闭合：carry 偏差与端点分数部 sawtooth 差完全等价。
- 未闭合：sawtooth 和的统一界。
- 未闭合：若 sawtooth 异常集中，对应 PDEC 的排除。
- 未闭合：occupied-b 序列的一维 Selberg 素性上界。
- 下一目标：`ReciprocalSawtoothDiscrepancyBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md` | `4d6f95b7c545e525d9ae34bc3065d11c807ef752ddefdc3186b344979c7caf78` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.json` | `41173d466644115c697765fc1c37912bb1dcc183620107f7439da7ab11b179a7` |
| `experiments/prime_matrix_square_phase_lowalpha_semiprime_phase_sawtooth_router.py` | `c09004e766306ed4890b941c170c5ae8707e255f4b1cf185962ede55787b1bc2` |
