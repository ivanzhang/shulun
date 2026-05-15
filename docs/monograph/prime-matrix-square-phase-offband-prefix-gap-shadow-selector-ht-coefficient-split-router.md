# Prime Matrix square-phase off-band prefix gap shadow selector H/T coefficient split router

**状态：** `selector_positive_density_surplus_reduced_to_coefficient_split_open_global`

本步把正密度余量输入拆成两个系数门：`H>=0.43P/logP` 与 `T<=0.212P/logP`。二者给出 `H-2T>=0.006000000000000005P/logP`；在 `P>=2001` 时足以压过 W=1 的常数项。当前有限数据支持该拆分，但全局系数证明仍未完成。

```text
max_p=10000
p0=2001
h_coeff=0.43
t_coeff=0.212
split_density_c=0.006000000000000005
prime_rho_hit_count=612
H_lower_failure_count_at_p0=0
T_upper_failure_count_at_p0=0
split_floor_closure_failure_count_at_p0=0
row_column_unconditional_closed=false
```

## 1. 系数拆分

充分条件为：

```text
H >= a P/logP
T <= b P/logP
a - 2b > 0.
```

当前登记的可攻参数是 `a=0.43,b=0.212`，因此 `a-2b=0.006`。在 `P>=2001`，该正密度项已经大于 W=1 的常数项 `1`。

## 2. P 区间系数

| P range | hits | min H coeff | max T coeff | separated surplus | p at min H | p at max T |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| 3..2000 | 150 | 0.38646464754254584 | 0.22333643526375713 | -0.06020822298496842 | `[157]` | `[277]` |
| 2001..5000 | 194 | 0.4305890165577595 | 0.2118955709759178 | 0.006797874605923904 | `[2467]` | `[3947]` |
| 5001..10000 | 268 | 0.45003229386999777 | 0.20798206915422124 | 0.03406815556155529 | `[5297]` | `[7027]` |

## 3. 最紧样本

| actual surplus coeff | template | p | side | rho | W | H | T | H coeff | T coeff | margin |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.0 | 1 | 157 | minus | 7 | 2 | 12 | 6 | 0.38646464754254584 | 0.19323232377127292 | 1 |
| 0.0 | 6 | 157 | minus | 7 | 2 | 12 | 6 | 0.38646464754254584 | 0.19323232377127292 | 1 |
| 0.008421701551102612 | 2 | 1777 | plus | 7 | 1 | 104 | 51 | 0.4379284806573347 | 0.21475338955311604 | 1 |
| 0.008421701551102612 | 3 | 1777 | plus | 7 | 1 | 104 | 51 | 0.4379284806573347 | 0.21475338955311604 | 1 |
| 0.009627284007256043 | 0 | 677 | minus | 2 | 2 | 45 | 22 | 0.4332277803265176 | 0.21180024815963078 | 2 |
| 0.009627284007256043 | 5 | 677 | minus | 2 | 2 | 45 | 22 | 0.4332277803265176 | 0.21180024815963078 | 2 |
| 0.012664382839934152 | 6 | 2467 | minus | 7 | 2 | 136 | 66 | 0.4305890165577595 | 0.20896231685891267 | 5 |
| 0.016256238208739004 | 2 | 1327 | plus | 7 | 1 | 79 | 38 | 0.42808093949679304 | 0.20591235064402702 | 2 |
| 0.016256238208739004 | 3 | 1327 | plus | 7 | 1 | 79 | 38 | 0.42808093949679304 | 0.20591235064402702 | 2 |
| 0.029787812684958337 | 4 | 173 | plus | 2 | 1 | 13 | 6 | 0.38724156490445744 | 0.17872687610974955 | 0 |
| 0.02991390221576329 | 6 | 1747 | minus | 7 | 2 | 107 | 50 | 0.4572553624409525 | 0.2136707301125946 | 8 |
| 0.032512476417477953 | 1 | 1327 | minus | 7 | 2 | 82 | 38 | 0.444337177705532 | 0.20591235064402702 | 7 |

## 4. 结构判断

- 分离系数门是比直接 `H-2T` 余量更强的输入；它更容易和外部尾素数上界、内部平方窗下界对接。
- 当前尾素数上界形状看起来可由全局显式 `pi(x)` 上界处理；真正困难仍集中在 selector 平方窗下系数。
- 若分离系数无法证明，可退回直接相关余量或低余量复现 PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `coefficient_split_sufficient_condition` | `closed` | H>=aP/logP and T<=bP/logP imply H-2T>=(a-2b)P/logP. |
| `current_split_coefficients_support_a043_b0212_after_2001` | `closed_on_current_sweep` | The finite sweep supports a=0.43 and b=0.212 after P0=2001. |
| `global_square_window_lower_and_tail_upper_coefficients` | `open` | A global proof must establish the square-window lower coefficient and tail upper coefficient, or use a correlated surplus theorem. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CoefficientSplitSufficientConditionClosed` | `true` | `true` | H 下系数与 T 上系数可推出正密度余量。 | closed |
| `CurrentCoefficientSplitHolds` | `true` | `true` | 当前有限数据支持 a=0.43,b=0.212,P0=2001。 | finite evidence only |
| `GlobalCoefficientSplitProved` | `false` | `false` | 仍需全局证明平方窗下系数与尾素数上系数。 | SquareWindowLowerCoefficientAndTailUpperCoefficientOrCorrelatedSurplusPDEC |
| `CorrelatedSurplusAlternativeProved` | `false` | `false` | 若分离系数过粗，可直接证明 H-2T 的相关正余量。 | SquareWindowLowerCoefficientAndTailUpperCoefficientOrCorrelatedSurplusPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只拆分系数输入，不关闭全局行/列命题。 | SquareWindowLowerCoefficientAndTailUpperCoefficientOrCorrelatedSurplusPDEC |

## 7. 下一步

- 主攻：`SquareWindowLowerCoefficientAndTailUpperCoefficientOrCorrelatedSurplusPDEC`。
- 优先证明 `T<=0.212P/logP` 的尾素数上界是否可由显式 `pi(x)` 上界关闭。
- 主要难点是证明 selector 平方窗 `H>=0.43P/logP`，或给出相关余量替代。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_coefficient_split_router.py` | `d495ab7dc269a058fa273693aa965991d9bf660e8541440886966d4613e24f9c` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py` | `5f53bd13fef7ac641fb9bf25f0d67d25e79d4e2d8977b667785fd6c93ded5529` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router.py` | `2cdf49886e62f706834bbbe18459e8afdb4c2c1fb653b7e9133aa54dcb52918e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json` | `458949cc7734f7b82044bd47fbda6fb60dfb870b80e6c925d3b259894b18b57b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json` | `339e3bfc87be2bf82c88e8b47ac47719e576d67bdfb06092e122d82d78ff6448` |
