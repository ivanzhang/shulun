# Prime Matrix square-phase off-band prefix gap shadow selector H lower active ell interval band router

**状态：** `active_ell_interval_band_closed_current_sweep_endpoint_growth_open`

当前扫描中活跃 `ell` 来源不是任意稀疏集合，而是精确等于闭区间 `23..109` 内的全部素数，共 21 个；双侧共同活跃核心为 `29..107` 内的全部素数，共 19 个。相位不对称只发生在 minus-only 端点 `[23, 109]`，plus-only 为空。因此下一步可把一般活跃来源增长界压成端点增长界，或证明端点移动触发 reset-PDEC/SAE。

```text
exact_active_prime_interval_current_sweep=true
active_band=23..109
active_band_prime_count=21
both_side_band=29..107
both_side_band_prime_count=19
endpoint_asymmetry_only_current_sweep=true
row_column_unconditional_closed=false
```

## 1. 带状结构

| object | value |
| --- | --- |
| active ell band | `23..109` |
| active prime count | `21` |
| both-side core band | `29..107` |
| both-side prime count | `19` |
| minus-only endpoints | `[23, 109]` |
| plus-only endpoints | `[]` |
| missing small prime sources below active band | `[2, 3, 5, 7, 11, 13, 17, 19]` |

## 2. 结构结论

- 当前 formal unit 内，活跃来源增长不是任意组合增长，而是素数带端点增长。
- 下端缺失小素数只有有限个，若全局活跃来源数失控，主要通道只能是上端点外推。
- 端点外推必须与 residue 重复、transport reset-PDEC 或 SAE/Rankin 稀疏化发生对接；否则仍不能闭合行/列命题。

## 3. 下一步

- 主攻：`ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`。
- 证明活跃素数带端点增长受限，或证明端点移动必然形成可排斥的 endpoint reset-PDEC/SAE。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_active_ell_interval_band_router.py` | `0a48abaf5facb0e6f036fd924fe0fef54718251541c1112b1cda2a5d8356f3a8` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json` | `2f86d0b8f43e35626243749be133068f651966d90c31896795c984d5801d0991` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json` | `f2876c431b7c4ff762deb76e26f43d974388fab22a1ee854f64fa39944ce280e` |
