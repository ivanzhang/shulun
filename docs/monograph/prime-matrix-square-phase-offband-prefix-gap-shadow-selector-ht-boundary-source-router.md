# Prime Matrix square-phase off-band prefix gap shadow selector H/T boundary source router

**状态：** `selector_prime_rho_ht_boundary_source_isolated_open_global`

本步把 prime rho hit 的 H/T 硬点拆成 W 专属整数下界：W=1 需要 `H-2T>=1`，W=2 需要 `H-2T>=-1`。当前 344 个命中没有 W 专属下界失败；slack<=1 的临界行只有 7 个，slack=0 的真正边界只有 1 个。

```text
max_p=5000
prime_rho_hit_count=344
global_ht_inequality_failure_count=0
w_specific_bound_failure_count=0
critical_slack_le_1_count=7
boundary_slack_zero_count=1
critical_p_values=[157, 173, 1777]
critical_template_indices=[1, 2, 3, 4, 6]
w2_stronger_nonnegative_failure_count=0
row_column_unconditional_closed=false
```

## 1. W 专属整数下界

`H/T` 正规形为 `H-2T>=3-2W`。当前模板只出现 `W=1` 与 `W=2`，因此硬点被拆成：

```text
W=1: H-2T >= 1
W=2: H-2T >= -1
```

| W | hits | required lower bound | min H-2T | max H-2T | failures | equality | p at min |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 92 | 1 | 1 | 82 | 0 | 1 | `[173]` |
| 2 | 252 | -1 | 0 | 83 | 0 | 0 | `[157]` |

## 2. slack<=1 临界行

| template | p | side | rho | W | H | T | H-2T | bound | excess | slack | prefix atoms |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 157 | minus | 7 | 2 | 12 | 6 | 0 | -1 | 1 | 1 | `plus_only_noslot:k0[147,155]:2,both_offband_middle:k0[145,145]:0,plus_only_noslot:k1[139,139]:1` |
| 2 | 157 | plus | 7 | 1 | 14 | 6 | 2 | 1 | 1 | 1 | `both_offband_middle:k0[145,145]:0,minus_only_noslot:k0[141,143]:0,both_offband_middle:k1[137,137]:1` |
| 2 | 1777 | plus | 7 | 1 | 104 | 51 | 2 | 1 | 1 | 1 | `both_offband_middle:k0[1735,1735]:0,minus_only_noslot:k0[1719,1733]:3,both_offband_middle:k1[1705,1705]:0` |
| 3 | 157 | plus | 7 | 1 | 14 | 6 | 2 | 1 | 1 | 1 | `both_offband_middle:k0[145,145]:0,minus_only_noslot:k0[141,143]:0,both_offband_middle:k1[137,137]:1` |
| 3 | 1777 | plus | 7 | 1 | 104 | 51 | 2 | 1 | 1 | 1 | `both_offband_middle:k0[1735,1735]:0,minus_only_noslot:k0[1719,1733]:3,both_offband_middle:k1[1705,1705]:0` |
| 4 | 173 | plus | 2 | 1 | 13 | 6 | 1 | 1 | 0 | 0 | `minus_only_noslot:k0[157,159]:1,minus_only_noslot:k1[149,151]:2,minus_only_noslot:k2[145,145]:0` |
| 6 | 157 | minus | 7 | 2 | 12 | 6 | 0 | -1 | 1 | 1 | `plus_only_noslot:k0[147,155]:2,both_offband_middle:k0[145,145]:0,plus_only_noslot:k1[139,139]:1` |

## 3. 结构判断

- `W=1` 的目标下界是正余量 `H>=2T+1`；当前唯一 slack=0 边界是 `p=173, side=plus, rho=2, template=4`。
- `W=2` 的目标下界只需 `H>=2T-1`；当前有限前沿实际更强，全部满足 `H>=2T`。
- 因此下一步不应回到泛泛短区间素数命题，而应证明 W 专属的 H/T 来源不等式，或把反复出现的边界相位登记为 PDEC/ColumnCRT。
- 当前仍未证明全局行/列无条件闭合。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `w_specific_ht_integer_bounds` | `closed` | The normal form is split into W=1: H-2T>=1 and W=2: H-2T>=-1. |
| `current_w_specific_bounds_hold` | `closed_on_current_sweep` | Every current prime rho hit satisfies its W-specific H/T bound. |
| `critical_boundary_source_isolated` | `closed_on_current_sweep` | All slack<=1 rows are explicitly expanded to square-window prime offsets, tail primes, and prefix atoms. |
| `global_w_specific_ht_source_inequality` | `open` | A global proof must derive the W-specific H/T source inequality, or route recurrent boundary failure to PDEC. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `WSpecificIntegerNormalFormClosed` | `true` | `true` | `2T-H<=2W-3` 已拆成 W=1 与 W=2 的整数下界。 | closed |
| `CurrentWSpecificBoundsHold` | `true` | `true` | 当前全部 prime rho hit 满足 W 专属 H/T 下界。 | closed on current finite sweep |
| `CriticalBoundaryRowsIsolated` | `true` | `true` | slack<=1 的临界对象已全部展开为具体窗口与 atom 来源。 | closed on current finite sweep |
| `GlobalWSpecificHTSourceInequalityProved` | `false` | `false` | 仍需全局证明 W 专属 H/T 来源不等式，或把边界复现登记为 PDEC。 | WSpecificHTSourceInequalityOrBoundaryRecurrencePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只隔离 H/T 边界来源，不关闭全局行/列命题。 | WSpecificHTSourceInequalityOrBoundaryRecurrencePDEC |

## 6. 下一步

- 主攻：`WSpecificHTSourceInequalityOrBoundaryRecurrencePDEC`。
- 证明目标：从 selector 相位、低轮 residue、平方窗与尾素数供给的共同约束推出 W 专属 H/T 来源不等式。
- 若出现低余量长期复现，则把它转为边界复现 PDEC/ColumnCRT，而不是把有限验证当作证明。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router.py` | `2bceab09fed0b827d59f89c9773ff04445231ad8a632d28c345858d49382b9c3` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router.py` | `f2874e8671ae937ef5f7e162e1dbc50d88f6c1eeee7be431531e86d47201fe90` |
| `data/square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json` | `ee751ab5d4a528200b4e7328cb72f02be31e6bc5895d8e0bf85bbb302978eb2a` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json` | `289702f6150d001371716152f404434422d303fd31397394119cdcad90d596d3` |
