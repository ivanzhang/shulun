# Prime Matrix square-phase low-alpha Buchstab 深度门

**状态：** `buchstab_constant_split_into_semiprime_and_deep_tail_open`

Buchstab 常数硬点已按前驱 `D_-` 的 u-因子深度分裂。若 `D_-<sqrt(P)`，则 `H=P/D_-` 满足 `H^3>P^2/D_-`，所以 H-rough 的 `u` 至多半素数；其余 `D_->=sqrt(P)` 才是真正 deep Buchstab tail。本步闭合深度门，不证明半素数常数或 deep tail 上界。

```text
u_depth_bound_checked=true
semiprime_gate_closed=true
semiprime_constant_proved=false
deep_buchstab_tail_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局 regime

| regime | hits | weighted capacity | predecessors | weighted density |
| --- | ---: | ---: | ---: | ---: |
| `deep` | 9033 | 55054 | 4660 | 0.164075 |
| `semiprime` | 12471 | 155370 | 171 | 0.080266 |

## 2. 最坏 low-alpha 块

| P | block | hits | actual u-depths | regime rows | top semiprime D_- | top deep D_- |
| ---: | --- | ---: | --- | --- | --- | --- |
| 200003 | `(31,62]` | 4540 | `{'2': 1334, '1': 3168, '3': 38}` | `{'deep': {'hits': 2535.0, 'weighted_capacity': 17381.0, 'predecessors': 1166.0, 'weighted_density': 0.14584891548242335}, 'semiprime': {'hits': 2005.0, 'weighted_capacity': 29633.0, 'predecessors': 7.0, 'weighted_density': 0.0676610535551581}}` | `{'d_minus': 37, 'hits': 362, 'capacity': 5406, 'omega_block': 1, 'weighted_capacity': 5406, 'depth_bound': 2, 'h': 5405.486486486487, 'weighted_density': 0.06696263411024787}` | `{'d_minus': 1591, 'hits': 32, 'capacity': 126, 'omega_block': 2, 'weighted_capacity': 252, 'depth_bound': 3, 'h': 125.70898805782527, 'weighted_density': 0.12698412698412698}` |

## 3. 每个 P 的总结

| P | low blocks | total hits | worst block |
| ---: | ---: | ---: | --- |
| 10007 | 2 | 412 | `(31,62]` |
| 36739 | 3 | 2040 | `(31,62]` |
| 83561 | 4 | 5659 | `(31,62]` |
| 200003 | 4 | 13393 | `(31,62]` |

## 4. 证明边界

- 已闭合：`u` 的 H-rough 因子深度上界。
- 已闭合：`D_-<sqrt(P)` 分支压为 semiprime/prime interval 常数问题。
- 未闭合：semiprime interval 常数上界。
- 未闭合：`D_->=sqrt(P)` 的 deep Buchstab tail 上界或 PDEC。
- 下一目标：`SemiprimePredecessorIntervalConstantOrDeepBuchstabTailPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.json` | `7e6448c6fbf63fa3fec79ef08077149b9157ca5e130ef5b429f67e8a6602e0d6` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json` | `68bfa3535663ae6b05870d4f28ae5dbb06e70e92e5eec2ca3e269fcf53c7914d` |
| `experiments/prime_matrix_square_phase_lowalpha_buchstab_depth_gate_router.py` | `8c1ef74f841a9e343b2dc85ac4f8145eb707fdcec8c4df8640d523ce2e854235` |
