# Prime Matrix square-phase off-band prefix gap shadow selector phase width envelope router

**状态：** `selector_phase_width_envelope_open_global`

本步把 fixed small-k phase 宽度输入正规化为活跃端点公式。当前 11 个窗口全部由右端 b_hi 的下界约束和左端 b_lo 的上界约束夹出，精确恢复原 phase_p_width；活跃 pattern 数为 6，最大宽度为 172。这关闭了当前前沿的宽度公式层；全局仍需证明 formal-unit 族中同样的端点方向和宽度 envelope，再与标签模数下界合并推出 M>W。

```text
record_count=11
group_count=6
active_pattern_count=6
width_formula_failure_count=0
endpoint_orientation_failure_count=0
max_phase_width=172
row_column_unconditional_closed=false
```

## 1. 活跃端点公式

| idx | P | band | k | b range | width | active lower | active upper | formula ok |
| ---: | ---: | --- | ---: | --- | ---: | --- | --- | ---: |
| 0 | 733 | `minus_only_noslot` | 1 | `23..26` | 8 | `floor_lower@b=26 -> 729` | `minus_band_upper@b=23 -> 736` | `true` |
| 1 | 523 | `minus_only_noslot` | 0 | `12..15` | 96 | `floor_lower@b=15 -> 481` | `minus_band_upper@b=12 -> 576` | `true` |
| 2 | 691 | `plus_only_noslot` | 1 | `19..21` | 117 | `plus_band_lower@b=21 -> 644` | `floor_upper@b=19 -> 760` | `true` |
| 3 | 683 | `minus_only_noslot` | 0 | `14..17` | 172 | `floor_lower@b=17 -> 613` | `minus_band_upper@b=14 -> 784` | `true` |
| 4 | 733 | `minus_only_noslot` | 0 | `14..18` | 100 | `floor_lower@b=18 -> 685` | `minus_band_upper@b=14 -> 784` | `true` |
| 5 | 673 | `plus_only_noslot` | 2 | `25..27` | 28 | `plus_band_lower@b=27 -> 648` | `floor_upper@b=25 -> 675` | `true` |
| 6 | 733 | `minus_only_noslot` | 1 | `23..26` | 8 | `floor_lower@b=26 -> 729` | `minus_band_upper@b=23 -> 736` | `true` |
| 7 | 313 | `minus_only_noslot` | 1 | `15..16` | 32 | `floor_lower@b=16 -> 289` | `minus_band_upper@b=15 -> 320` | `true` |
| 8 | 1129 | `minus_only_noslot` | 1 | `29..32` | 72 | `floor_lower@b=32 -> 1089` | `minus_band_upper@b=29 -> 1160` | `true` |
| 9 | 691 | `plus_only_noslot` | 1 | `19..21` | 117 | `plus_band_lower@b=21 -> 644` | `floor_upper@b=19 -> 760` | `true` |
| 10 | 673 | `plus_only_noslot` | 2 | `25..27` | 28 | `plus_band_lower@b=27 -> 648` | `floor_upper@b=25 -> 675` | `true` |

## 2. Family Envelope

| group | records | min W | max W | patterns | orientation ok |
| --- | ---: | ---: | ---: | --- | ---: |
| `band=minus_only_noslot\|k=0\|L=4` | 2 | 96 | 172 | `['band=minus_only_noslot\|k=0\|L=4\|lo=floor_lower@b_3\|hi=minus_band_upper@b_0']` | `true` |
| `band=minus_only_noslot\|k=0\|L=5` | 1 | 100 | 100 | `['band=minus_only_noslot\|k=0\|L=5\|lo=floor_lower@b_4\|hi=minus_band_upper@b_0']` | `true` |
| `band=minus_only_noslot\|k=1\|L=2` | 1 | 32 | 32 | `['band=minus_only_noslot\|k=1\|L=2\|lo=floor_lower@b_1\|hi=minus_band_upper@b_0']` | `true` |
| `band=minus_only_noslot\|k=1\|L=4` | 3 | 8 | 72 | `['band=minus_only_noslot\|k=1\|L=4\|lo=floor_lower@b_3\|hi=minus_band_upper@b_0']` | `true` |
| `band=plus_only_noslot\|k=1\|L=3` | 2 | 117 | 117 | `['band=plus_only_noslot\|k=1\|L=3\|lo=plus_band_lower@b_2\|hi=floor_upper@b_0']` | `true` |
| `band=plus_only_noslot\|k=2\|L=3` | 2 | 28 | 28 | `['band=plus_only_noslot\|k=2\|L=3\|lo=plus_band_lower@b_2\|hi=floor_upper@b_0']` | `true` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `active_endpoint_width_formula` | `closed_on_current_frontier` | Every current fixed phase window is exactly recovered from the active b_hi lower endpoint and b_lo upper endpoint. |
| `phase_width_envelope_normal_form` | `closed` | The phase width input is reduced to explicit endpoint formulas by band/k family. |
| `global_endpoint_orientation` | `open` | A global proof must show the same active endpoint orientation holds for the formal-unit family. |
| `global_width_bound` | `open` | A global proof must combine the endpoint formula with label lower bounds to prove M>W. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteActiveEndpointFormulaClosed` | `true` | `true` | 当前 fixed phase 窗口宽度均由活跃端点公式精确恢复。 | closed on current finite frontier |
| `EndpointOrientationClosed` | `true` | `true` | 当前所有窗口均为 b_hi 给下界、b_lo 给上界。 | closed on current finite frontier |
| `GlobalEndpointOrientationProved` | `false` | `false` | 尚未证明 formal-unit 族中活跃端点方向不变。 | ActiveEndpointPhaseWidthEnvelopeAndLabelLowerBoundOrSmallModulusPDEC |
| `GlobalMGreaterThanWProved` | `false` | `false` | 仍需与标签模数下界合并推出全局 M>W。 | ActiveEndpointPhaseWidthEnvelopeAndLabelLowerBoundOrSmallModulusPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭当前宽度公式层，不关闭全局行/列命题。 | ActiveEndpointPhaseWidthEnvelopeAndLabelLowerBoundOrSmallModulusPDEC |

## 5. 下一步

- 主攻：`ActiveEndpointPhaseWidthEnvelopeAndLabelLowerBoundOrSmallModulusPDEC`。
- 直接证明目标：证明 formal-unit 族中活跃端点方向稳定，并用上述公式给出宽度 envelope。
- 随后与 cover-word 标签模数下界合并，形成全局 `M>W`。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router.py` | `d22471303dad825b366acf9418178abfbff3257f5d385771331d1666f65589bb` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router.py` | `69d98f70c0d1d4ceafebe32d35541a0f306d41c4a3ef0c34d76d5c66162b9b38` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json` | `9b74bc89311d215f67e9cd6a8c9c731cbeff3a114533eca56e8140929afcd161` |
| `data/square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json` | `d2315a905edf1d24de2158140c650b774dfacccf77d11555d20e4d8d37fbd6af` |
