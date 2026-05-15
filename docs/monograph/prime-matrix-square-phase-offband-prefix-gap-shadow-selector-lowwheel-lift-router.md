# Prime Matrix square-phase off-band prefix gap shadow selector lowwheel lift router

**状态：** `selector_lowwheel15_lift_split_open`

本步把 Q=15 selector 分离拆成两类来源：覆盖词 CRT 模数在 gcd(modulus,15) 上已经与 actual P 冲突的结构低轮冲突，以及覆盖词本身不冲突、但在 fixed phase 窗口内只落到非 actual mod 15 残基的相位窗口错位。当前前沿没有 Q=15 泄漏，但窗口错位词在每个包中都存在，所以不能把低轮分离直接声称为纯 CRT 标签定理；真正剩余被压成 PhaseWindowMiss lift，或 persistent Q=15 overlap 的 PDEC/ColumnCRT 证书。

```text
record_count=11
total_phase_compatible_cover_word_count=162
structural_lowwheel_conflict_word_count=113
phase_window_miss_word_count=49
q15_leakage_word_count=0
packets_requiring_phase_window_miss_lift=11
row_column_unconditional_closed=false
```

## 1. 拆分结论

当前 `Q=15` 分离不是纯标签 CRT 冲突。若覆盖词模数与 `15` 的公共因子已经排斥 actual `P`，则进入 structural conflict；否则必须依赖 fixed phase 窗口没有取到 actual `P mod 15` 的窗口错位。

## 2. 前沿记录

| idx | P | side | words | structural | window miss | q15 leak | gcd(mod,15) histogram |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 733 | `plus` | 4 | 1 | 3 | 0 | `{'1': 1, '3': 2, '5': 1}` |
| 1 | 523 | `plus` | 6 | 5 | 1 | 0 | `{'15': 4, '3': 1, '5': 1}` |
| 2 | 691 | `minus` | 35 | 24 | 11 | 0 | `{'1': 5, '15': 14, '3': 12, '5': 4}` |
| 3 | 683 | `plus` | 31 | 30 | 1 | 0 | `{'15': 14, '3': 15, '5': 2}` |
| 4 | 733 | `plus` | 5 | 3 | 2 | 0 | `{'15': 3, '3': 2}` |
| 5 | 673 | `minus` | 6 | 4 | 2 | 0 | `{'15': 1, '3': 2, '5': 3}` |
| 6 | 733 | `plus` | 4 | 1 | 3 | 0 | `{'1': 1, '3': 2, '5': 1}` |
| 7 | 313 | `plus` | 10 | 6 | 4 | 0 | `{'1': 4, '3': 4, '5': 2}` |
| 8 | 1129 | `plus` | 20 | 11 | 9 | 0 | `{'1': 2, '15': 8, '3': 7, '5': 3}` |
| 9 | 691 | `minus` | 35 | 24 | 11 | 0 | `{'1': 5, '15': 14, '3': 12, '5': 4}` |
| 10 | 673 | `minus` | 6 | 4 | 2 | 0 | `{'15': 1, '3': 2, '5': 3}` |

## 3. 窗口错位样例

| idx | P | examples |
| ---: | ---: | --- |
| 0 | 733 | `[{'labels': [3, 11, 17, 3], 'g': 3, 'res15': 4, 'values': [730]}, {'labels': [7, 19, 11, 17], 'g': 1, 'res15': 12, 'values': [732]}, {'labels': [19, 11, 17, 3], 'g': 3, 'res15': 10, 'values': [730]}]` |
| 1 | 523 | `[{'labels': [19, 11, 3, 7], 'g': 3, 'res15': 4, 'values': [499]}]` |
| 2 | 691 | `[{'labels': [7, 3, 11], 'g': 3, 'res15': 1, 'values': [724]}, {'labels': [7, 3, 19], 'g': 3, 'res15': 1, 'values': [745]}, {'labels': [7, 19, 11], 'g': 1, 'res15': 4, 'values': [724]}]` |
| 3 | 683 | `[{'labels': [11, 17, 3, 13], 'g': 3, 'res15': 5, 'values': [710]}]` |
| 4 | 733 | `[{'labels': [3, 11, 17, 3, 13], 'g': 3, 'res15': 7, 'values': [712]}, {'labels': [19, 11, 17, 3, 13], 'g': 3, 'res15': 7, 'values': [712]}]` |
| 5 | 673 | `[{'labels': [7, 3, 13], 'g': 3, 'res15': 1, 'values': [652]}, {'labels': [7, 3, 23], 'g': 3, 'res15': 4, 'values': [652]}]` |
| 6 | 733 | `[{'labels': [3, 11, 17, 3], 'g': 3, 'res15': 4, 'values': [730]}, {'labels': [7, 19, 11, 17], 'g': 1, 'res15': 12, 'values': [732]}, {'labels': [19, 11, 17, 3], 'g': 3, 'res15': 10, 'values': [730]}]` |
| 7 | 313 | `[{'labels': [7, 11], 'g': 1, 'res15': 5, 'values': [296]}, {'labels': [11, 7], 'g': 1, 'res15': 14, 'values': [305]}, {'labels': [11, 13], 'g': 1, 'res15': 4, 'values': [305]}]` |
| 8 | 1129 | `[{'labels': [3, 7, 11, 3], 'g': 3, 'res15': 7, 'values': [1096]}, {'labels': [3, 11, 7, 3], 'g': 3, 'res15': 1, 'values': [1105]}, {'labels': [3, 13, 7, 3], 'g': 3, 'res15': 4, 'values': [1126]}]` |
| 9 | 691 | `[{'labels': [7, 3, 11], 'g': 3, 'res15': 1, 'values': [724]}, {'labels': [7, 3, 19], 'g': 3, 'res15': 1, 'values': [745]}, {'labels': [7, 19, 11], 'g': 1, 'res15': 4, 'values': [724]}]` |
| 10 | 673 | `[{'labels': [7, 3, 13], 'g': 3, 'res15': 1, 'values': [652]}, {'labels': [7, 3, 23], 'g': 3, 'res15': 4, 'values': [652]}]` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `q15_finite_separator_decomposition` | `closed_on_current_frontier` | Every compatible cover word is either structurally lowwheel-conflicting or phase-window-missing modulo 15. |
| `pure_crt_label_lowwheel_lift` | `rejected` | The Q=15 separator is not explained solely by label-word CRT conflicts; window-miss words occur in every packet. |
| `phase_window_miss_lift` | `open` | The remaining lift must prove that non-conflicting cover words miss the actual selector residue inside the fixed phase window. |
| `persistent_q15_overlap_pdec` | `open` | If a non-conflicting word hits the actual residue in a persistent family, it must be routed to PDEC/ColumnCRT. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteQ15DecompositionClosed` | `true` | `true` | 当前前沿无 Q=15 窗口泄漏；每个覆盖词均被结构冲突或窗口错位解释。 | closed on current finite frontier |
| `PureCRTLowWheelLiftClosed` | `false` | `false` | 存在窗口错位词，不能声称 Q=15 分离已由覆盖词 CRT 标签自动全局推出。 | rejected |
| `PhaseWindowMissLiftProved` | `false` | `false` | 仍需对窗口错位词证明 actual selector residue 永远不落窗。 | LowWheel15PhaseWindowMissLiftOrPersistentHitPDEC |
| `PersistentQ15OverlapPDECExcluded` | `false` | `false` | 若窗口错位 lift 失败，则需对持久 Q=15 重叠提交 PDEC/ColumnCRT。 | LowWheel15PhaseWindowMissLiftOrPersistentHitPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步继续缩窄 selector 剩余，不关闭全局行/列命题。 | LowWheel15PhaseWindowMissLiftOrPersistentHitPDEC |

## 6. 下一步

- 主攻：`LowWheel15PhaseWindowMissLiftOrPersistentHitPDEC`。
- 直接证明目标：对 non-structural cover words 证明 fixed phase 窗口中的同余进程永远错开 actual `P mod 15`。
- 若窗口错位不能全局证明，则把实际重叠族登记为 persistent `Q=15` overlap 的 PDEC/ColumnCRT 证书。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router.py` | `2b16c31c7a682a0a0122634256522cbc6802789d54ae2ef1c50ced26b94db72c` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router.py` | `3b59bdbcedb0ba8195e162437885629c6bb4491edd11e3793ba93bb17723b5ae` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py` | `dc04a453b7fc1f5f5587c1ce1fc7a88ee96c30cf6e4830639fc90fdbb0ce4c06` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json` | `a9aebcbecddfdeed41fc3a33decc08ef206e6161c7e6aa7f2b30c540c8d896d0` |
| `data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json` | `494a9f0e6d8d0bb31b97efee740e1e206ee45b789d86f1c92a2c33f076b119a7` |
