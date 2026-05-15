# Prime Matrix square-phase low-alpha z=61 PrefixGate signed balance

**状态：** `z61_prefix_gate_signed_balance_reduced_to_dyadic_lift_companion_open`

PrefixGate signed phase balance 可精确化为同权计数骨架：同一相位 `b≡0 mod 28842` 的三条命中有相同单位权重，负侧只有 quotient `1`，正侧为 quotient `2,4`，所以局部 signed weight 等于一个单位权重。正侧两条命中进一步等价于 same-p endpoint strip、shifted linear prime pair 和 square-window selector。全局剩余因此收窄为：负锚是否必有 dyadic lift companion，或 PersistentPhase/MissingLift-PDEC 是否可排斥。

```text
phase_condition=b ≡ 0 (mod 28842)
negative_quotients=[1]
positive_quotients=[2, 4]
same_unit_weight_on_phase_hits=true
signed_phase_count=1
signed_phase_weight=0.555427
positive_dyadic_lift_companion_closed_for_sample=true
prefix_gate_signed_phase_balance_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. 同权计数骨架

| quotient | sign | p | q | a | b | delta | mult | unit weight | signed |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `negative` | 36739 | 53 | 883 | 28842 | 22637 | 1 | 0.555427 | -0.555427 |
| 2 | `positive` | 200003 | 71 | 9767 | 57684 | 173579 | 1 | 0.555427 | 0.555427 |
| 4 | `positive` | 200003 | 37 | 9371 | 115368 | 527 | 1 | 0.555427 | 0.555427 |

## 2. 正侧 companion

| field | value |
| --- | --- |
| same-p | `200003` |
| endpoint span/capacity | `3 / 4` |
| carry equation | `71*9767 - 2*37*9371 = 3` |
| shifted multiplier | `132` |
| linear forms | `{'a4': '71*132-1', 'a2': '74*132-1'}` |
| square-window recovered s | `132` |

## 3. 证明边界

- 已闭合：当前 formal unit 的 PrefixGate signed balance 精确同权计数骨架。
- 已闭合：正侧两条 lift 与 shifted pair / square-window 链严格对接。
- 未闭合：dyadic lift companion 的全局必然性，或 PersistentPhase/MissingLift-PDEC 排斥。
- 下一目标：`DyadicLiftCompanionForPrefixPhaseOrPersistentPhasePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json` | `4d8a9ef2c35d9dc7d1b53d6736f8ae2ad53df2a6f41206e6f368a75d1da861b0` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json` | `ea2150eaee0eb08d7f7a3412b3d35821bac7f1901f2fa37028335cf16c9b5d0f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json` | `57d4e18eadd1bb072db598f782533b7ecefc942472cc8f26d9f0a285e97ad40e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json` | `7f3175f133abcd84096c6d522a5219f06547614f22eab2af265171e602fbbfe2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json` | `7470bdf7651a2cdc84f388e336e7c4273cbb2aa2836bb149c17330950fe3365f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_signed_balance_router.py` | `d8ac4f4ffa39d9f6a8f27161bc3a4da0a6f3bf7770c524701dff7630e8c65347` |
