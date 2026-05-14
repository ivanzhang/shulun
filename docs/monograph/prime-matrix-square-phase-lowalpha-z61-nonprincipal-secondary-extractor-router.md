# Prime Matrix square-phase low-alpha z=61 非主正相位抽取

**状态：** `z61_residual_reduced_to_nonprincipal_secondary_extractor_open`

两处残量可以更自然地由非主正相位信用支付。`mid<=4` 由两个 `--++` 单元覆盖；`unbalanced<=8` 可由 4 个非主正相位单元覆盖，且不必依赖上一层的 `--++` 选中模板。因此下一硬点压成 unbalanced 四个非主正相位单元的相位不变量，或输出 Extractor-PDEC。

```text
principal_positive_p=83561
nonprincipal_secondary_identity_closed=true
sample_nonprincipal_cells_cover_all_residuals=true
unbalanced_cover_cell_count=4
unbalanced_cover_sign_words=-++-,-+--,+-++,+-+-
nonprincipal_extractor_phase_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. bucket 非主正相位覆盖

| bucket | residual need | total secondary | cover cells | cover credit | surplus |
| --- | ---: | ---: | ---: | ---: | ---: |
| `mid<=4` | 0.042281 | 0.081573 | 2 | 0.051506 | 0.009225 |
| `unbalanced<=8` | 0.037200 | 0.053785 | 4 | 0.041886 | 0.004687 |

## 2. 选中覆盖单元

| bucket | omega | shell | signs | secondary credit | cumulative | pairs | profile vector |
| --- | ---: | --- | --- | ---: | ---: | --- | --- |
| `mid<=4` | 3 | `(2D,4D]` | `--++` | 0.028278 | 0.028278 | `200003->10007:0.005070, 200003->36739:0.023208` | `10007:-1.749411, 36739:-8.007256, 83561:6.150322, 200003:8.708046` |
| `mid<=4` | 4 | `(D,2D]` | `--++` | 0.023228 | 0.051506 | `200003->10007:0.001143, 200003->36739:0.022085` | `10007:-0.315393, 36739:-6.095123, 83561:2.683332, 200003:7.355355` |
| `unbalanced<=8` | 3 | `(2D,4D]` | `-++-` | 0.015200 | 0.015200 | `36739->10007:0.003708, 36739->200003:0.011492` | `10007:-2.193242, 36739:2.714492, 83561:6.893740, 200003:-6.796502` |
| `unbalanced<=8` | 5 | `(4D,8D]` | `-+--` | 0.011886 | 0.027086 | `36739->10007:0.000401, 36739->83561:0.002752, 36739->200003:0.008732` | `10007:-0.184853, 36739:1.985946, 83561:-1.267369, 200003:-4.021515` |
| `unbalanced<=8` | 5 | `(2D,4D]` | `+-++` | 0.008140 | 0.035226 | `10007->36739:0.000883, 200003->36739:0.007257` | `10007:0.226569, 36739:-2.537867, 83561:1.807935, 200003:1.861220` |
| `unbalanced<=8` | 3 | `(D,2D]` | `+-+-` | 0.006661 | 0.041886 | `10007->36739:0.002926, 10007->200003:0.003734` | `10007:1.112897, 36739:-8.361086, 83561:4.022690, 200003:-10.668508` |

## 3. 模板信用

| bucket | sign word | secondary credit |
| --- | --- | ---: |
| `mid<=4` | `--++` | 0.063136 |
| `mid<=4` | `-++-` | 0.009902 |
| `mid<=4` | `-+++` | 0.003599 |
| `mid<=4` | `+++-` | 0.002716 |
| `mid<=4` | `-+--` | 0.001399 |
| `mid<=4` | `+-+-` | 0.000822 |
| `unbalanced<=8` | `-++-` | 0.015200 |
| `unbalanced<=8` | `--++` | 0.011898 |
| `unbalanced<=8` | `-+--` | 0.011886 |
| `unbalanced<=8` | `+-++` | 0.008140 |
| `unbalanced<=8` | `+-+-` | 0.006661 |

## 4. 证明边界

- 已闭合：非主正相位信用与上一层 secondary credit 精确一致。
- 已压缩：`unbalanced<=8` 由 4 个非主正相位单元覆盖。
- 未闭合：证明这 4 个单元的相位不变量，或登记 Extractor-PDEC。
- 下一目标：`UnbalancedFourNonprincipalCellsPhaseInvariantOrExtractorPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json` | `3a969b773dd2ef0f972e6d2a2ada55824c255fc1c06044360394add4c67f35a0` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json` | `a39098dbe0a99b79259bc828641a2de7c7e6596bea21ea553e44f2088f9a9770` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json` | `f37d1d58c9c03c95badb956c102919ebd6a69db811139157393a1123f0a52d1b` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_nonprincipal_secondary_extractor_router.py` | `be52479f7f8596728451ea02c73fb8b68ad18490472dfa8f1db4576820b79f06` |
