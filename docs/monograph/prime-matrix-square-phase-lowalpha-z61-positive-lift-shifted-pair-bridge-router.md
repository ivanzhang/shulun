# Prime Matrix square-phase low-alpha z=61 positive lift shifted pair bridge

**状态：** `z61_positive_dyadic_lift_existence_reduced_to_shifted_square_window_open`

正向 dyadic lift 的存在性不是新的自由命题：quotient `2,4` 的两条正向 lift 与已有 same-p strip 完全同一组，并等价于 endpoint shifted-factor 中的同步移位线性素数对 `a4=71s-1`、`a2=74s-1`，其中 `s=132`。再与平方窗口证书对接后，MissingLift 的剩余被压成 shifted square-window 全局容量界，或相应 MissingLift-PDEC。

```text
positive_lift_rows_match_same_p=true
positive_lift_rows_match_shifted_pair=true
same_p_shifted_pair_bridge_closed=true
shifted_pair_square_window_bridge_closed=true
positive_lift_shifted_pair_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. 正向 lift 行

| quotient | p | q | a | b |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 200003 | 71 | 9767 | 57684 |
| 4 | 200003 | 37 | 9371 | 115368 |

## 2. Same-p endpoint strip

| p | base M | capacity | span | endpoints | carry equation |
| ---: | ---: | ---: | ---: | --- | --- |
| 200003 | 57684 | 4 | 3 | true | `71*9767 - 2*37*9371 = 3` |

## 3. Shifted pair

| p | q2 | a2 | q4 | a4 | carry | 2q4-q2 | s | forms |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 200003 | 71 | 9767 | 37 | 9371 | 3 | 3 | 132 | `{'a4': '71*132-1', 'a2': '74*132-1'}` |

## 4. Square-window 对接

| delta | residue | recovered s |
| ---: | ---: | ---: |
| 527 | 57157 | 132 |

## 5. 证明边界

- 已闭合：当前正向 dyadic lift 与 shifted pair / square-window 链严格同一对象。
- 未闭合：shifted square-window 全局容量界，或 MissingLift-PDEC 排斥。
- 下一目标：`ShiftedSquareWindowGlobalBoundOrMissingLiftPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json` | `4d8a9ef2c35d9dc7d1b53d6736f8ae2ad53df2a6f41206e6f368a75d1da861b0` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json` | `57d4e18eadd1bb072db598f782533b7ecefc942472cc8f26d9f0a285e97ad40e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json` | `7f3175f133abcd84096c6d522a5219f06547614f22eab2af265171e602fbbfe2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_shifted_pair_bridge_router.py` | `996eb5e974aee0dc2618114469fb769a35cf37cc230c8050c15718adc7804547` |
