# Prime Matrix square-phase low-alpha z=61 positive lift root selector bridge

**状态：** `z61_positive_lift_square_window_reduced_to_unique_root_selector_open`

MissingLift 的 square-window 剩余可继续压到 CRT root integral selector：在 `M=57684, delta=527, span=3` 的 32 个 CRT 根中，只有 `r=26951` 给出整数 `s=132`，并同时给出两个素数源 `a4=9371,a2=9767`。因此正向 lift 存在性在当前 formal unit 中等价于唯一 full-source 根选择；全局剩余是证明这类根选择器容量界，或登记 MissingLift-PDEC。

```text
crt_root_count=32
prime_p_candidate_count=9
integral_s_candidate_count=1
full_source_candidate_count=1
selected_is_unique_integral_s_root=true
selected_is_unique_full_source_root=true
positive_lift_root_selector_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. Selector data

| M | delta | span | q2 | q4 | roots | prime p | integral s | full source |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 57684 | 527 | 3 | 71 | 37 | 32 | 9 | 1 | 1 |

## 2. Unique selected root

| residue | p | s | a4 | a2 | p prime | a4 prime | a2 prime |
| ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 26951 | 200003 | 132 | 9371 | 9767 | true | true | true |

## 3. 证明边界

- 已闭合：当前 positive lift square-window 与唯一 full-source CRT 根严格同一对象。
- 未闭合：全局 CRT root integral selector 容量界，或 MissingLift-PDEC 排斥。
- 下一目标：`CRTRootIntegralSelectorGlobalBoundOrMissingLiftPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-crt-root-integral-selector-router.json` | `78303772b2d0ed699a2b51d915f8053d588b2b9fc80b741c0193101325fd617a` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json` | `25c354e6440e1f1f9a945cf96f54b86c1f854f20fdd804c109c4685d06596772` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_root_selector_bridge_router.py` | `d9b0d9193a6628fecdb5d77ead216d600505e5a037341543267758f1b548b6fe` |
