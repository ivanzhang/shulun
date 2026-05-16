# Prime Matrix square-phase off-band prefix gap shadow selector H lower active one-slot epoch source router

**状态：** `active_one_slot_epoch_sources_materialized_growth_bound_open`

本步把活跃一槽 epoch 数量界压成活跃 `ell` 来源界：当前有 40 个 `(side,ell)` epoch，来自 21 个不同 `ell`，范围为 `23..109`；其中 19 个 `ell` 同时出现在正负侧。全局仍需证明活跃 `ell` 来源随尺度可控，或证明来源增长会触发 transport reset-PDEC/SAE。

```text
active_epoch_count=40
distinct_active_ell_count=21
active_ell_min=23
active_ell_max=109
both_side_ell_count=19
row_column_unconditional_closed=false
```

## 1. 活跃 ell 来源

| ell | sides | used | capacity | Rankin mass | p range |
| ---: | --- | ---: | ---: | ---: | --- |
| 23 | `['minus']` | 1 | 23 | 0.043478 | `4987..4987` |
| 29 | `['minus', 'plus']` | 4 | 58 | 0.137931 | `2687..6337` |
| 31 | `['minus', 'plus']` | 9 | 62 | 0.290323 | `2767..6569` |
| 37 | `['minus', 'plus']` | 13 | 74 | 0.351351 | `2027..9787` |
| 41 | `['minus', 'plus']` | 12 | 82 | 0.292683 | `2017..8837` |
| 43 | `['minus', 'plus']` | 14 | 86 | 0.325581 | `2137..9397` |
| 47 | `['minus', 'plus']` | 13 | 94 | 0.276596 | `2063..9473` |
| 53 | `['minus', 'plus']` | 15 | 106 | 0.283019 | `3137..6607` |
| 59 | `['minus', 'plus']` | 13 | 118 | 0.220339 | `3257..7949` |
| 61 | `['minus', 'plus']` | 21 | 122 | 0.344262 | `3187..8237` |
| 67 | `['minus', 'plus']` | 14 | 134 | 0.208955 | `3967..9127` |
| 71 | `['minus', 'plus']` | 26 | 142 | 0.366197 | `4177..9497` |
| 73 | `['minus', 'plus']` | 10 | 146 | 0.136986 | `4337..8647` |
| 79 | `['minus', 'plus']` | 21 | 158 | 0.265823 | `5197..8887` |
| 83 | `['minus', 'plus']` | 13 | 166 | 0.156627 | `5557..9787` |
| 89 | `['minus', 'plus']` | 12 | 178 | 0.134831 | `7207..9887` |
| 97 | `['minus', 'plus']` | 16 | 194 | 0.164948 | `7537..9491` |
| 101 | `['minus', 'plus']` | 17 | 202 | 0.168317 | `8387..9857` |
| 103 | `['minus', 'plus']` | 6 | 206 | 0.058252 | `8537..9461` |
| 107 | `['minus', 'plus']` | 6 | 214 | 0.056075 | `9277..9907` |
| 109 | `['minus']` | 1 | 109 | 0.009174 | `9817..9817` |

## 2. 结构判断

- 单个 epoch 容量已经闭合后，Rankin 可求和只可能来自活跃 ell 来源数的全局控制。
- 当前活跃 ell 是有限低模带，但不能把有限带直接外推为全局定理。
- 若活跃 ell 来源持续增长，必须证明它触发 residue 重复、transport reset-PDEC 或 SAE/Rankin 稀疏化。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `active_epoch_source_materialized` | `closed` | The active one-slot epochs are exactly represented by their side and least-prime-factor ell source. |
| `current_active_ell_band_finite` | `closed_on_current_sweep` | In the current sweep, all active one-slot epochs have ell in a finite low-mod band. |
| `active_ell_growth_bound_open` | `open` | A global proof must bound the number of active ell sources per scale, or show growth forces transport reset-PDEC/SAE. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ActiveEpochSourceMaterialized` | `true` | `true` | 活跃 epoch 已完全化为 `(side,ell)` 来源集合。 | closed |
| `CurrentActiveEllBandFinite` | `true` | `false` | 当前活跃 ell 落在 `23..109`，但这只是有限扫描事实。 | finite evidence only |
| `ActiveEllGrowthBoundProved` | `false` | `false` | 尚未证明活跃 ell 数量随尺度有全局可求和控制。 | ActiveEllGrowthBound |
| `TransportResetPDECExcluded` | `false` | `false` | 若活跃 ell 增长导致 residue 重复，仍需 reset-PDEC 排斥。 | TransportResetPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只定位活跃 epoch 来源，不关闭全局命题。 | ActiveEllGrowthBoundOrTransportResetPDECExclusion |

## 5. 下一步

- 主攻：`ActiveEllGrowthBoundOrTransportResetPDECExclusion`。
- 证明活跃 ell 来源增长受限，或证明增长必然产生 reset-PDEC/SAE。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_active_one_slot_epoch_source_router.py` | `48b7b694caa6cb6330ef59dda6c86caa5c2d52624c625a40e04cb5d0b5c9950f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json` | `2f86d0b8f43e35626243749be133068f651966d90c31896795c984d5801d0991` |
