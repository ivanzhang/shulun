# Prime Matrix square-phase off-band prefix gap shadow selector H lower one/two-slot normal form router

**状态：** `one_two_slot_certificates_reduced_to_unique_representative_shapes_open`

本步把一槽/二槽 moving certificate 写成唯一代表正规形：`P` 是 CRT 残基在短相位支撑区间内的唯一整数代表。当前 `P>=2001` 重放中唯一代表身份失败数为 0；正规形 shape 数为 80，其中一槽 shape 40 个、二槽 shape 40 个。剩余硬点变为排斥这些唯一代表 shape 在 selector 约束下持久复现，或建立全局正 margin。

```text
max_p=10000
p0=2001
selected_hit_count_at_p0=462
unique_representative_identity_failure_count_at_p0=0
certificate_size_histogram_at_p0={'1': 399, '2': 63}
two_slot_strictly_needed_count_at_p0=63
normal_shape_count_at_p0=80
row_column_unconditional_closed=false
```

## 1. 正规形

```text
Given one/two highfactor slots S:
  P ≡ crt_residue(S) mod crt_modulus(S)
  P in I(S)=[phase_p_lo, phase_p_hi]
  |I(S)| < crt_modulus(S)
there is at most one representative P_S in I(S).
The certificate is in normal form when actual P=P_S.
```

## 2. 等号原子正规形

| p | side | rho | cert size | ell tuple | CRT modulus | phase | representative | depths |
| ---: | --- | ---: | ---: | --- | ---: | --- | --- | --- |
| 2467 | `minus` | 7 | 1 | `[43]` | 43 | `[2459,2480]` | `[2467]` | `8/13` |

## 3. 最紧正规形样本

| p | side | rho | template | margin | size | ell tuple | CRT-width | phase | depths | slots |
| ---: | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | --- | --- |
| 2467 | `minus` | 7 | 6 | 0 | 1 | `[43]` | 21 | `[2459,2480]` | `8/13` | `['237:56:43']` |
| 2347 | `plus` | 7 | 2 | 12 | 1 | `[47]` | 11 | `[2324,2359]` | `23/12` | `['180:33:47']` |
| 2347 | `plus` | 7 | 3 | 12 | 1 | `[47]` | 11 | `[2324,2359]` | `23/12` | `['180:33:47']` |
| 5297 | `minus` | 2 | 0 | 12 | 1 | `[47]` | 21 | `[5289,5314]` | `8/17` | `['470:101:47']` |
| 5297 | `minus` | 2 | 5 | 12 | 1 | `[47]` | 21 | `[5289,5314]` | `8/17` | `['470:101:47']` |
| 3767 | `plus` | 2 | 4 | 12 | 1 | `[61]` | 25 | `[3754,3789]` | `13/22` | `['290:53:61']` |
| 2243 | `plus` | 2 | 4 | 12 | 2 | `[17, 19]` | 306 | `[2233,2249]` | `10/6` | `['128:17:17', '155:25:19']` |
| 2027 | `minus` | 2 | 5 | 13 | 1 | `[37]` | 12 | `[2015,2039]` | `12/12` | `['185:41:37']` |
| 2063 | `plus` | 2 | 4 | 13 | 1 | `[47]` | 19 | `[2048,2075]` | `15/12` | `['177:37:47']` |
| 2927 | `minus` | 2 | 0 | 13 | 2 | `[37, 43]` | 1431 | `[2839,2998]` | `88/71` | `['69:3:37', '99:7:43']` |
| 2927 | `minus` | 2 | 5 | 13 | 2 | `[37, 43]` | 1431 | `[2839,2998]` | `88/71` | `['69:3:37', '99:7:43']` |
| 2267 | `minus` | 2 | 5 | 14 | 2 | `[47, 31]` | 1405 | `[2233,2284]` | `34/17` | `['102:10:47', '135:18:31']` |
| 5407 | `minus` | 7 | 6 | 15 | 1 | `[29]` | 3 | `[5384,5409]` | `23/2` | `['483:105:29']` |
| 2687 | `minus` | 2 | 5 | 15 | 1 | `[29]` | 4 | `[2669,2693]` | `18/6` | `['242:53:29']` |
| 2837 | `minus` | 2 | 5 | 15 | 1 | `[31]` | 8 | `[2832,2854]` | `5/17` | `['270:63:31']` |
| 4007 | `minus` | 2 | 5 | 15 | 1 | `[61]` | 31 | `[4007,4036]` | `0/29` | `['338:68:61']` |
| 2207 | `minus` | 2 | 0 | 15 | 2 | `[43, 23]` | 906 | `[2145,2227]` | `62/20` | `['35:1:43', '114:13:23']` |
| 2207 | `minus` | 2 | 5 | 15 | 2 | `[43, 23]` | 906 | `[2145,2227]` | `62/20` | `['35:1:43', '114:13:23']` |
| 2297 | `minus` | 2 | 5 | 15 | 2 | `[23, 43]` | 955 | `[2297,2330]` | `0/33` | `['77:5:23', '143:20:43']` |
| 2647 | `minus` | 7 | 6 | 15 | 2 | `[37, 31]` | 1117 | `[2646,2675]` | `1/28` | `['183:29:37', '205:37:31']` |
| 4567 | `minus` | 7 | 6 | 16 | 1 | `[37]` | 13 | `[4550,4573]` | `17/6` | `['417:93:37']` |
| 2137 | `minus` | 7 | 1 | 16 | 1 | `[43]` | 19 | `[2115,2138]` | `22/1` | `['198:45:43']` |
| 2137 | `minus` | 7 | 6 | 16 | 1 | `[43]` | 19 | `[2115,2138]` | `22/1` | `['198:45:43']` |
| 2557 | `plus` | 7 | 2 | 16 | 1 | `[43]` | 19 | `[2555,2578]` | `2/21` | `['237:54:43']` |

## 4. 高频正规形 shape

| shape | count | p range | min margin | min CRT-width | examples |
| --- | ---: | --- | ---: | ---: | --- |
| `size=1|side=minus|ells=71` | 31 | `4177..9257` | 25 | 14 | `[(4177, 7, ['358:74:71']), (4177, 7, ['358:74:71']), (4217, 2, ['345:67:71'])]` |
| `size=1|side=minus|ells=53` | 26 | `2377..7127` | 17 | 9 | `[(2377, 7, ['183:33:53']), (2377, 7, ['183:33:53']), (2887, 7, ['270:62:53'])]` |
| `size=1|side=minus|ells=43` | 22 | `2137..9397` | 0 | 1 | `[(2137, 7, ['198:45:43']), (2137, 7, ['198:45:43']), (2237, 2, ['165:28:43'])]` |
| `size=1|side=minus|ells=61` | 22 | `3187..8237` | 15 | 19 | `[(3187, 7, ['229:38:61']), (3187, 7, ['229:38:61']), (3677, 2, ['278:49:61'])]` |
| `size=1|side=minus|ells=59` | 18 | `3257..7877` | 17 | 21 | `[(3257, 2, ['287:61:59']), (3527, 2, ['279:52:59']), (3617, 2, ['290:55:59'])]` |
| `size=1|side=minus|ells=89` | 18 | `7297..9967` | 26 | 49 | `[(7297, 7, ['687:159:89']), (7307, 2, ['684:157:89']), (7507, 7, ['619:122:89'])]` |
| `size=1|side=minus|ells=79` | 17 | `5197..8887` | 36 | 32 | `[(5197, 7, ['435:87:79']), (5197, 7, ['435:87:79']), (5387, 2, ['369:58:79'])]` |
| `size=1|side=minus|ells=97` | 16 | `7537..8737` | 27 | 32 | `[(7537, 7, ['750:186:97']), (7537, 7, ['750:186:97']), (7547, 2, ['747:184:97'])]` |
| `size=1|side=plus|ells=79` | 16 | `5639..8887` | 36 | 20 | `[(5639, 2, ['558:138:79']), (5711, 2, ['536:124:79']), (5717, 2, ['534:123:79'])]` |
| `size=1|side=minus|ells=101` | 15 | `8387..9857` | 44 | 15 | `[(8387, 2, ['813:195:101']), (8527, 7, ['700:137:101']), (8527, 7, ['700:137:101'])]` |
| `size=1|side=minus|ells=47` | 14 | `2357..6857` | 12 | 9 | `[(2357, 2, ['177:31:47']), (2357, 2, ['177:31:47']), (3457, 7, ['300:63:47'])]` |
| `size=1|side=minus|ells=67` | 14 | `3967..9127` | 23 | 18 | `[(3967, 7, ['375:87:67']), (3967, 7, ['375:87:67']), (5507, 2, ['513:117:67'])]` |
| `size=1|side=minus|ells=83` | 14 | `5927..9787` | 37 | 30 | `[(5927, 2, ['414:67:83']), (5927, 2, ['414:67:83']), (6037, 7, ['552:123:83'])]` |
| `size=1|side=minus|ells=73` | 13 | `4337..8597` | 29 | 36 | `[(4337, 2, ['404:92:73']), (4457, 2, ['365:71:73']), (4457, 2, ['365:71:73'])]` |
| `size=1|side=minus|ells=37` | 11 | `2027..6967` | 13 | 1 | `[(2027, 2, ['185:41:37']), (2477, 2, ['189:34:37']), (3307, 7, ['298:65:37'])]` |
| `size=1|side=plus|ells=61` | 11 | `3257..5227` | 12 | 5 | `[(3257, 2, ['203:29:61']), (3347, 2, ['303:67:61']), (3767, 2, ['290:53:61'])]` |
| `size=1|side=minus|ells=41` | 10 | `2087..8837` | 17 | 2 | `[(2087, 2, ['173:34:41']), (2657, 2, ['239:52:41']), (3407, 2, ['302:65:41'])]` |
| `size=1|side=minus|ells=103` | 8 | `8537..9227` | 60 | 72 | `[(8537, 2, ['834:202:103']), (8537, 2, ['834:202:103']), (8867, 2, ['728:143:103'])]` |

## 5. 结构判断

- 一槽分支已经是单一同余残基在短区间内的唯一代表问题。
- 二槽分支中每个单槽都不足以隔离，必须依赖两个槽的 CRT 合并；这是真正的 ColumnCRT 形态。
- 下一步应对高频 shape 做持久性排斥：若同一 shape 长期复现，则进入固定模/移动模 PDEC；若 shape 漂移，则进入 SAE/Rankin 账本。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `one_two_slot_unique_representative_normal_form` | `closed` | Every one-slot/two-slot certificate is exactly a unique CRT representative inside a short phase-support interval. |
| `current_sweep_unique_representative_identity` | `closed_on_current_sweep` | On the current selector sweep, the unique representative is always the actual selector prime P. |
| `unique_representative_pdec_or_global_margin` | `open` | A global proof must show these unique representatives cannot persist under the selector chain, or route persistent shapes to ColumnCRT/PDEC. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `UniqueRepresentativeNormalFormClosed` | `true` | `true` | 一槽/二槽证书已改写为短相位区间内唯一 CRT 代表。 | closed |
| `CurrentSweepRepresentativeIdentityClosed` | `true` | `false` | 当前重放中唯一代表恒等于实际 P。 | finite evidence only |
| `TwoSlotStrictNeedIdentified` | `true` | `true` | 二槽分支中每个单槽都不足，确实需要 CRT 合并。 | closed |
| `PersistentUniqueRepresentativeShapesExcluded` | `false` | `false` | 唯一代表 shape 的持久复现尚未排斥。 | UniqueRepresentativeOneTwoSlotPDECOrGlobalResidualPrimeMarginJump |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把一槽/二槽 moving family 正规化，不关闭全局行/列命题。 | UniqueRepresentativeOneTwoSlotPDECOrGlobalResidualPrimeMarginJump |

## 8. 下一步

- 主攻：`UniqueRepresentativeOneTwoSlotPDECOrGlobalResidualPrimeMarginJump`。
- 具体目标：排斥唯一代表 shape 持久复现，或将固定 shape/移动 shape 分别接入 `ColumnCRT/PDEC` 与 `SAE/Rankin`。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py` | `235a88162fc76a089f99156ebbc167cec3c3e43c7e00c2e99addcab467b88d09` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router.py` | `731c4bc285e87e7a8f430bd4ff2ed6068717944dfea2d1ddfcc10e34bdfb12e3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json` | `65b36c6b248a45607ec514dfb648829016fe66537b6aa2ac327bd385269773f9` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-ledger.json` | `3d7546c1d5c27cf953c37e31de1eeed6d2877a0906a94c5582353f7e11a1ab5a` |
