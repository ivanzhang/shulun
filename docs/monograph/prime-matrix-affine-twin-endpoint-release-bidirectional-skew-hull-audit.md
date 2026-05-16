# Prime Matrix AffineTwin endpoint-release bidirectional skew-hull audit

**状态：** `current_sweep_bidirectional_skew_hull_structured_global_open`

本审计把最新 slack 原子放回局部逆元对齐框架：每个 formal pair 给出一个关于 `P` 的 CRT 类，支撑窗口若要同时吸收这些类，就必须覆盖它们的最小相位壳层。

```text
local pair alignment: P = generator_residue (mod q-2)
                      P = shifted_fill_residue (mod q)
hull = smallest current-period interval containing all nearest representatives
```

```text
formal_alignment_row_count=12
empty_alignment_row_count=11
combined_crt_modulus=899
support_interval=[2669, 2688]
support_width=20
alignment_hull_interval=[2304, 3122]
alignment_hull_width=819
left_extension_required=365
right_extension_required=434
left_extra_skew_after_feedback_horizon=335
right_extra_skew_after_feedback_horizon=409
bidirectional_extra_skew_after_shared_hull=744
hull_width_to_modulus_ratio=0.911012235818
modulus_minus_hull_width=80
affine_p_delay=80
hull_complement_equals_affine_p_delay=true
one_sided_skew_growth_absorption_closed_current_sweep=true
```

## 1. 局部对齐表

| pair | side | representative | distance | surplus | actual | CRT residue |
| --- | --- | ---: | ---: | ---: | --- | ---: |
| `13:8` | `below` | 2594 | 75 | 45 | false | 796 |
| `13:9` | `above` | 3029 | 341 | 316 | false | 332 |
| `13:12` | `below` | 2536 | 133 | 103 | false | 738 |
| `13:28` | `below` | 2304 | 365 | 335 | false | 506 |
| `15:8` | `below` | 2625 | 44 | 14 | false | 827 |
| `15:9` | `above` | 3060 | 372 | 347 | false | 363 |
| `15:12` | `below` | 2567 | 102 | 72 | false | 769 |
| `15:28` | `below` | 2335 | 334 | 304 | false | 537 |
| `19:8` | `inside` | 2687 | 0 | 0 | true | 889 |
| `19:9` | `above` | 3122 | 434 | 409 | false | 425 |
| `19:12` | `below` | 2629 | 40 | 10 | false | 831 |
| `19:28` | `below` | 2397 | 272 | 242 | false | 599 |

## 2. 壳层刚性

全部 formal pair 的最近代表落在 `[2304, 3122]`，宽度 `819`。当前支撑只有 `20`，若靠单一支撑窗口同时吸收所有 formal pair，左侧必须扩张 `365`，右侧必须扩张 `434`。
扣除当前 feedback horizon 后，左侧仍缺 `335`，右侧仍缺 `409`。因此一侧移动或纯 skew 翻向不能解释当前 formal-pair 全集。
更刚性的读数是：`modulus - hull_width = 80`，正好等于 affine p-delay `80`。也就是说，若反例链要把所有 formal pair 同时塞回一个支撑壳层，它几乎占满整个 `q(q-2)` 周期，只留下 p-delay 大小的互补缝。

## 3. 与逆元最小对齐解 x 的关系

旧的逆元最小对齐路线把 `xP+r` 的小素因子覆盖写成 `x` 的 CRT 覆盖问题。本审计使用同一思想，但变量换成当前 AffineTwin 局部相位 `P`：每个 generator/fill residue pair 给出一个 `P mod q(q-2)` 的精确类。最近代表、支撑距离和最小壳层就是该局部系统的最小对齐证书。
这一步没有证明全局 `min x>P`，而是把当前反例链/真实链的显式冲突压成双向壳层：反例链需要近全周期壳层，真实链只有宽度 `20` 的 primitive 支撑和有限 feedback horizon。

## 4. 结论边界

- 当前 `12` 个 formal pair 的局部 CRT 对齐壳层已精确物化。
- 壳层同时向 below 和 above 两侧超出 feedback horizon，所以单侧 skew-growth 吸收关闭。
- 本步不关闭全局行/列命题；剩余是排斥 `BidirectionalSkewHull-PDEC`，或证明持久壳层复现进入 `ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-crt-window-gap-ledger.json` | `4822729687dfb1818e8d917ca278f2eeda8d167825456f1dc1dd0456e142f71f` |
| `data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json` | `358cda290d4be012472c7dfa81064972e016ff88972093e8af5855ba0eb524a9` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json` | `09be6a101dd2775a057577a1ef960270dbd88b03dd5e5cec4d1bddec67eb1acf` |
