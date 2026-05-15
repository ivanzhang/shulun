# Prime Matrix square-phase low-alpha z=61 secondary congruence selector

**状态：** `z61_integral_root_selector_reduced_to_secondary_square_congruence_open`

整数 `s` 条件不是额外的启发式筛选，而是一个更强的二级平方同余：`p^2+delta+2Mq4 ≡ 0 (mod 2Mq2q4)`。在样本的 `32` 个一级 CRT 根中，只有 `r=26951` 同时满足该二级同余；这与唯一整数 `s=132` 完全等价。因此 RootSelector-PDEC 进一步压成 SecondarySquareCongruence-PDEC，下一步证明这种二级平方同余选择的全局容量界。

```text
secondary_congruence_selector_group_count=1
all_secondary_congruence_selectors_closed=true
secondary_square_congruence_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 二级同余摘要

| M | secondary factor | secondary modulus | roots | secondary roots | selected | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 57684 | 5254 | 303071736 | 32 | 1 | 26951 | true |

## 2. 通过二级同余的根

| root residue | p | secondary residue | integral s | prime p | full source |
| ---: | ---: | ---: | --- | --- | --- |
| 1891 | 174943 | 302148792 | false | true | false |
| 3961 | 177013 | 121482504 | false | true | false |
| 8009 | 181061 | 55607376 | false | true | false |
| 11219 | 184271 | 16036152 | false | true | false |
| 11771 | 184823 | 219776040 | false | true | false |
| 24881 | 197933 | 85487688 | false | true | false |
| 26951 | 200003 | 0 | true | true | true |
| 34495 | 207547 | 43839840 | false | true | false |
| 46465 | 219517 | 3576408 | false | true | false |

## 3. 自足小引理

在一级 CRT 根条件 `p^2+delta≡0 (mod M)` 已成立时，共同乘子公式

```text
s=(p^2+delta+2*M*q4)/(2*M*q2*q4)
```

为整数，当且仅当 `p^2+delta+2*M*q4≡0 (mod 2*M*q2*q4)`。所以整数源选择器等价于在一级平方根集合上叠加一个二级平方同余。

## 4. 证明边界

- 已闭合：样本一级 CRT 根集中唯一根满足二级平方同余。
- 未闭合：全局二级平方同余容量界，或 SecondaryPhase-PDEC 排斥。
- 下一目标：`SecondarySquareCongruenceGlobalBoundOrSecondaryPhasePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-crt-root-integral-selector-router.json` | `78303772b2d0ed699a2b51d915f8053d588b2b9fc80b741c0193101325fd617a` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_secondary_congruence_selector_router.py` | `e0cd196d30200f69806ff570320c90a0800daa57faee111d5e48097398a56777` |
