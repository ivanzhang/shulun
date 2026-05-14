# Prime Matrix square-phase low-alpha Buchstab 模型密度路由

**状态：** `omega_weighted_density_reduced_to_buchstab_model_constant_or_spike_open`

`omega_B(D_-)` 加权密度已接到标准 Buchstab 模型账本：每个前驱的短区间长度约为 `H=P/D_-`，粗阈值也是 `H`，模型密度为 `e^{-gamma} omega(s)/log H`。本步只给出常数账本和尖峰定位，还没有证明全局常数上界或排除局部密度尖峰 PDEC。

```text
buchstab_model_ledger_materialized=true
buchstab_model_constant_bound_proved=false
local_density_spike_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 总体模型

| hits | Buchstab model | actual/model |
| ---: | ---: | ---: |
| 21504 | 15204.871417 | 1.414284 |

## 2. 最坏 low-alpha 块

| P | block | hits | model | actual/model | weighted density | top hit D_- | top model excess D_- |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 200003 | `(31,62]` | 4540 | 3330.633386 | 1.363104 | 0.096567 | `{'d_minus': 37, 'hits': 362, 'weighted_capacity': 5406, 'h': 5405.486486486487, 's': 2.4201101345184335, 'model_density': 0.03646249336546781, 'model': 197.11623913371898, 'actual_over_model': 1.8364798435223177}` | `{'d_minus': 3403, 'hits': 11, 'weighted_capacity': 58, 'h': 58.77255362915075, 's': 3.9963332206326543, 'model_density': 0.0773928597147876, 'model': 4.4887858634576805, 'actual_over_model': 2.4505512926220936}` |

## 3. 每个 P 的总结

| P | low blocks | hits | model | actual/model | worst block |
| ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 412 | 270.823465 | 1.521286 | `(31,62]` |
| 36739 | 3 | 2040 | 1464.068414 | 1.393378 | `(31,62]` |
| 83561 | 4 | 5659 | 3868.266768 | 1.462929 | `(31,62]` |
| 200003 | 4 | 13393 | 9601.712771 | 1.394855 | `(31,62]` |

## 4. 证明边界

- 已闭合：`omega_B(D_-)` 加权密度的 Buchstab 模型账本。
- 未闭合：证明模型常数上界足以支付全部 low-alpha 负载。
- 未闭合：若某前驱/尺度桶超过模型常数，需证明其触发 PDEC。
- 下一目标：`BuchstabModelConstantLedgerOrLocalDensitySpikePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-block-multiplicity-router.json` | `8d674312b227502b88a5e5c234c46f5f164a4e0cc7ac5d982c7d1f1336c61224` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json` | `b9530d634cb41da605749e7f5738f97378dd58b1570d08e2c82959d01c22bf95` |
| `experiments/prime_matrix_square_phase_lowalpha_buchstab_model_density_router.py` | `96130e4a663dca1a09f7796783bbe2a98e10147813f425705a8a72b0e885fa9a` |
