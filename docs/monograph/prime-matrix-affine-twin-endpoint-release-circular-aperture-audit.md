# Prime Matrix AffineTwin endpoint-release circular-aperture audit

**状态：** `current_sweep_circular_aperture_structured_global_open`

本审计把上一张线性壳层证书再精炼为圆周相位口径：在模 `q(q-2)` 的圆上删除最大的空弧，得到真正的最小 circular alignment arc。

```text
formal_alignment_row_count=12
combined_crt_modulus=899
support_width=20
linear_hull_width_from_previous_audit=819
largest_circular_open_gap_width=341
largest_gap_from_pair=19:8
largest_gap_to_pair=13:9
minimal_circular_alignment_arc=[3029, 3586]
minimal_circular_alignment_arc_width=558
minimal_circular_arc_width_to_modulus_ratio=0.620689655172
optimal_shifted_support_interval=[3568, 3587]
optimal_total_extension_required=539
conservative_extra_after_best_single_side_feedback=509
p_delay_open_gap_present=true
p_delay_open_gap_is_largest_gap=false
p_delay_gap_rank_by_width=3
one_sided_circular_absorption_closed_current_sweep=true
```

## 1. 圆周 gap spectrum

| from | to | from side | to side | open gap | delta |
| --- | --- | --- | --- | ---: | ---: |
| `19:8` | `13:9` | `inside` | `above` | 341 | 342 |
| `19:28` | `13:12` | `below` | `below` | 138 | 139 |
| `19:9` | `13:28` | `above` | `below` | 80 | 81 |
| `15:9` | `19:9` | `above` | `above` | 61 | 62 |
| `15:28` | `19:28` | `below` | `below` | 61 | 62 |
| `19:12` | `19:8` | `below` | `inside` | 57 | 58 |
| `13:9` | `15:9` | `above` | `above` | 30 | 31 |
| `13:28` | `15:28` | `below` | `below` | 30 | 31 |
| `13:12` | `15:12` | `below` | `below` | 30 | 31 |
| `13:8` | `15:8` | `below` | `below` | 30 | 31 |
| `15:12` | `13:8` | `below` | `below` | 26 | 27 |
| `15:8` | `19:12` | `below` | `below` | 3 | 4 |

## 2. 圆弧修正

上一张证书的 `[2304,3122]` 是当前周期线性壳层，宽度 `819`。圆周上真正的最小壳层应删除最大空弧 `19:8 -> 13:9`，其 open gap 宽度为 `341`，得到圆弧 `[3029, 3586]`，宽度 `558`。
这仍是 support width `20` 的 `27.9` 倍。即使把 support 平移到最优周期位置 `[3568, 3587]`，仍需总扩张 `539`；扣除最有利单侧 feedback horizon 后仍缺 `509`。

## 3. p-delay 子缝

`p_delay=80` 的空缝确实存在，但它不是最大圆周空弧；其宽度排名为 `3`。因此最新刚性不是“近全周期最小圆弧”，而是更精确的：最大空弧锚定在 actual packet 附近，删除它后仍留下宽度 `558` 的大圆弧，远超当前支撑和反馈地平线。

## 4. 结论边界

- 本步修正并细化上一层线性壳层：圆周最小弧已物化。
- 即使采用最优圆周切口，当前 formal-pair 系统仍不能由单侧 skew-growth 加 feedback horizon 吸收。
- 本步不关闭全局行/列命题；剩余是排斥 `CircularAperture-PDEC`，或证明持久圆弧复现进入 `ColumnCRT/PDEC`、`SAE` 或 moving-family multiplicity 出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json` | `69b806c23fb4f5515cbcf1cc184229db85a44b885469676905fcd83056be0bd5` |
