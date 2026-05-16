# Prime Matrix AffineTwin endpoint-release actual-anchor replacement audit

**状态：** `current_sweep_actual_anchor_replacement_closed_global_open`

本审计继续下钻 cut-anchor ColumnCRT compression 后的逃逸：若反例链不保留当前 actual anchor `19:8`，则必须让另一个 formal pair 或未使用 target residue 成为 actual。两条路线都需要超过当前 support width 的 CRT 相位跳跃。

```text
combined_crt_modulus=899
support_width=20
actual_anchor_pair=19:8
actual_crt_residue=889
formal_replacement_candidate_count=11
min_formal_replacement_pair=19:12
min_formal_replacement_abs_crt_jump=58
min_formal_replacement_endpoint_release=70
min_formal_release_to_support_width_ratio=3.5
unused_target_replacement_candidate_count=9
unique_unused_target_pair_count=5
min_unused_target_pair=20:9
min_unused_target_abs_crt_jump=59
min_unused_target_new_side_residue_count=1
all_formal_replacement_jumps_exceed_support_width=true
all_formal_replacement_releases_exceed_support_width=true
all_unused_target_jumps_exceed_support_width=true
all_unused_targets_need_new_side_residue=true
actual_anchor_replacement_closed_current_sweep=true
```

## 1. existing formal pair replacement

| target pair | side | target residue | signed jump | abs jump | release | both endpoints |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `19:12` | `below` | 831 | -58 | 58 | 70 | `true` |
| `15:8` | `below` | 827 | -62 | 62 | 78 | `true` |
| `13:8` | `below` | 796 | -93 | 93 | 140 | `true` |
| `15:12` | `below` | 769 | -120 | 120 | 194 | `true` |
| `13:12` | `below` | 738 | -151 | 151 | 256 | `true` |
| `19:28` | `below` | 599 | -290 | 290 | 534 | `true` |
| `13:9` | `above` | 332 | 342 | 342 | 677 | `true` |
| `15:28` | `below` | 537 | -352 | 352 | 658 | `true` |
| `15:9` | `above` | 363 | 373 | 373 | 739 | `true` |
| `13:28` | `below` | 506 | -383 | 383 | 720 | `true` |
| `19:9` | `above` | 425 | 435 | 435 | 863 | `true` |

## 2. unused target replacement

| source pair | target pair | side | abs CRT jump | jump-support | new side residues |
| --- | --- | --- | ---: | ---: | ---: |
| `19:12` | `20:9` | `below` | 59 | 39 | 1 |
| `15:8` | `17:6` | `below` | 60 | 40 | 2 |
| `13:8` | `16:5` | `below` | 90 | 70 | 2 |
| `13:12` | `18:7` | `below` | 150 | 130 | 2 |
| `19:28` | `10:30` | `below` | 281 | 261 | 2 |
| `15:28` | `10:30` | `below` | 343 | 323 | 2 |
| `13:9` | `16:5` | `above` | 345 | 325 | 2 |
| `13:28` | `10:30` | `below` | 374 | 354 | 2 |
| `15:9` | `17:6` | `above` | 375 | 355 | 2 |

## 3. 显式矛盾点

保留 actual anchor 时，上一层已经压缩为固定 `P == 889 mod 899` 的单个 ColumnCRT 原子。若改由现有 formal pair 替换 actual anchor，最小 CRT 跳跃是 `58`，来自 `19:12`，已经超过 support width `20`；同时最小双端点释放为 `70`，是 support width 的 `3.5` 倍。

若改由未使用 target residue 替换 actual anchor，最小 CRT 跳跃为 `59`，来自 target `20:9`，仍超过 support width，并且至少要新增 `1` 个侧残基。两条 actual-anchor replacement 路线都不能在当前 primitive support 内完成。

## 4. 结论边界

- 本步关闭当前 sweep 的 actual-anchor replacement 吸收解释。
- 本步仍不证明全局行/列命题；剩余是把 replacement no-go 升格为全局族定理，或排斥 support-motion、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json` | `69b806c23fb4f5515cbcf1cc184229db85a44b885469676905fcd83056be0bd5` |
| `data/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json` | `2a5fc9d2433400377968f31a99049ba8d3ba6d39ad2188126c75ae24edafdc45` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
