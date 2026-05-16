# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin epoch-pair multiplicity router

**状态：** `affine_twin_epoch_pair_sparse_eta_gate_passes_current_sweep_global_open`

本步把 AffineTwin epoch-pair multiplicity 压成 eta 稀疏门：取 `eta=1/40`，当前候选 `q` 的乘法占用上界逐项低于 eta，且总占用也低于 eta。当前最大占用为 0.013348164627，总占用为 0.023577117629，总 eta 余量为 0.001422882371。若全局出现 eta 门失败，失败行已被命名为 HighDensityEpochPair-PDEC/ColumnCRT；否则进入 sparse SAE 账本。

```text
eta=1/40
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
candidate_product_mass_upper_sum=0.023577117629
candidate_total_eta_slack=0.001422882371
max_occupancy_upper_ratio=0.013348164627
high_density_epoch_pair_count=0
current_sparse_acceptance_closed=true
row_column_unconditional_closed=false
```

## 1. eta 稀疏门

| q | used upper | capacity | occupancy | eta slack numerator | realized | high density |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 12 | 899 | 0.013348165 | 419 | `true` | `false` |
| 43 | 16 | 1763 | 0.009075440 | 1123 | `false` | `false` |
| 103 | 12 | 10403 | 0.001153513 | 9923 | `false` | `false` |

## 2. 出口

- 当前扫描没有 HighDensityEpochPair 行。
- 若后续或全局族出现 `occupancy>eta`，该 `q` 直接成为固定/移动模 ColumnCRT-PDEC 证书对象。
- 若始终满足 sparse gate，则进入 sparse SAE 质量账本；全局仍需证明该质量可求和并足以吸收反例链。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `current_affine_twin_epoch_pair_sparse_acceptance` | `closed_current_sweep` | For eta=1/40, every current candidate affine-twin epoch-pair has product occupancy below eta, and the total candidate product occupancy is also below eta. |
| `high_density_epoch_pair_pdec_trigger` | `closed_routing` | If an affine-twin epoch-pair violates the eta sparse gate, the offending q gives a named HighDensityEpochPair-PDEC/ColumnCRT certificate. |
| `global_sparse_sae_bound` | `open` | A global proof must show the sparse gate persists with summable SAE mass, or exclude the high-density epoch-pair PDEC family. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentEpochPairSparseEtaGateClosed` | `true` | `false` | 当前候选 twin epoch-pair 全部低于 eta=1/40。 | finite evidence only |
| `CurrentTotalCandidateMassBelowEta` | `true` | `false` | 当前候选乘法占用总质量也低于 eta=1/40。 | finite evidence only |
| `HighDensityEpochPairPDECRouted` | `true` | `true` | 若 eta 门失败，失败行已命名为 HighDensityEpochPair-PDEC/ColumnCRT。 | exclusion still separate |
| `GlobalSparseSAEBoundProved` | `false` | `false` | 仍需证明全局稀疏 SAE 质量可求和并足以吸收反例链。 | AffineTwinSparseSAEGlobalBoundOrHighDensityEpochPairPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成当前候选稀疏验收与高密度出口命名，不关闭全局行/列命题。 | AffineTwinSparseSAEGlobalBoundOrHighDensityEpochPairPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinSparseSAEGlobalBoundOrHighDensityEpochPairPDECExclusion`。
- 具体目标：证明 sparse SAE 的全局求和吸收，或排斥 HighDensityEpochPair-PDEC/ColumnCRT。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_epoch_pair_multiplicity_router.py` | `cadb393015006e2c3b7126fb7677607f23328ad1f3d42198729d0cb78d088288` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json` | `8323447f703d339a1ff63e35f0dcaff4d697b295ea79241f67c23d2ecd5c00d3` |
