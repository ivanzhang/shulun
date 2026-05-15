# Prime Matrix square-phase low-alpha z=61 CRT root integral selector

**状态：** `z61_crt_phase_lock_reduced_to_unique_integral_s_root_open`

在 `span=3`、`M=57684` 的 `32` 个 CRT 根相位中，只有一个根 `r=26951` 使平方窗口公式给出整数共同乘子 `s`。虽然其中有 `9` 个根给出素数 `p=3M+r`，但只有这个整数-s 根同时给出 `a4=71s-1` 与 `a2=74s-1` 两个素数。因此 CRTPhase-PDEC 被进一步压成唯一整数源选择器问题，下一步证明全局整数源选择器容量界，或登记 RootSelector-PDEC。

```text
crt_root_integral_selector_group_count=1
all_crt_root_integral_selectors_closed=true
crt_root_integral_selector_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 根筛选摘要

| M | span | roots | prime p roots | integral s roots | full source roots | selected | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 57684 | 3 | 32 | 9 | 1 | 1 | 26951 | true |

## 2. 候选根

| residue | p | prime p | integer s | s | a4 | a2 | full source |
| ---: | ---: | --- | --- | ---: | ---: | ---: | --- |
| 1891 | 174943 | true | false | None | None | None | false |
| 3961 | 177013 | true | false | None | None | None | false |
| 8009 | 181061 | true | false | None | None | None | false |
| 11219 | 184271 | true | false | None | None | None | false |
| 11771 | 184823 | true | false | None | None | None | false |
| 24881 | 197933 | true | false | None | None | None | false |
| 26951 | 200003 | true | true | 132 | 9371 | 9767 | true |
| 34495 | 207547 | true | false | None | None | None | false |
| 46465 | 219517 | true | false | None | None | None | false |

## 3. 自足小引理

固定 `M,delta,span,q2,q4` 后，CRT 根 `r` 只给出候选 `p=span*M+r`。要回到源纤维，还必须使

```text
s=(p^2+delta+2*M*q4)/(2*M*q2*q4)
```

为整数，并且 `q2*s-1`、`2*q4*s-1` 满足素性条件。因此这一层把 CRT 相位失败对象压成有限根集上的整数源选择器。

## 4. 证明边界

- 已闭合：样本 32 个 CRT 根中唯一根通过整数-s 与双素性选择。
- 未闭合：全局整数源选择器容量界，或 RootSelector-PDEC 排斥。
- 下一目标：`CRTRootIntegralSelectorGlobalBoundOrRootSelectorPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-square-residue-phase-lock-router.json` | `68e93c45c5ae1183e7ca4b5439236cface7618e8bb23c64ab8910cb566c8a496` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_crt_root_integral_selector_router.py` | `c2ac18ae68c7ed7fb375d04dbda545ddb18f843dc05f9dab66c597045dac087c` |
