# Triad-A1 ExactWFDSourceEntropy 路由审计

**状态：** `exact_wfd_source_entropy_reduced_to_factor_support_lower_bound`

ExactWFDSourceEntropy 不需要再依赖抽象 moving-block diffuse：若精确 well-factorable 因子在每个 surviving balanced block 内有多对数以上支撑，divisor-bound 立即给出单块容量份额的任意对数小上界。当前缺口不是谱相消，而是尚未登记 exact Rosser/Iwaniec-Buchstab 因子支撑下界及 Type/Fourier 容量兼容。

## 1. 支撑下界闭合律

若 |alpha_u|,|delta_v| <= log(y)^C，且 sum|alpha_u| >= U/log(y)^C、sum|delta_v| >= V/log(y)^C，则任一 moving pair 的容量份额至多 log(y)^(4C)/(UV)。因此只要 U,V >= log(y)^B 且 B>=A+2C，就推出 ExactWFDSourceEntropy(A)。

结构推导如下：

```text
Assume |alpha_u|, |delta_v| <= L^C, L=log y.
Assume sum_u |alpha_u| >= U/L^C and sum_v |delta_v| >= V/L^C.
Then max_{u,v} |alpha_u delta_v| / (sum|alpha| sum|delta|)
  <= L^(4C)/(UV).
If U,V >= L^B and B >= A+2C, this is <= L^(-2A).
Therefore exact factor support lower bound => ExactWFDSourceEntropy(A).
```

这一步把源头熵从谱大筛问题降为精确筛权支撑问题。

## 2. 当前缺口

当前 A1/KLS ledger 有 balanced dyadic range、divisor bound、fixed-residue L2-flat，但没有逐 balanced block 的 exact factor support lower bound。所以 ExactWFDSourceEntropy 已化为一个初等筛权支撑命题，而非新的谱大筛命题。

## 3. 汇总

- `source_block_input_status=source_block_entropy_not_forced_by_formal_wfd_inputs`。
- `conditional_factor_support_implies_exact_source_entropy=True`。
- `exact_factor_support_lower_bound_present=False`。
- `current_internal_exact_wfd_source_entropy_closed=False`。
- `support_threshold_power_A_plus_2C=6.0`。
- `all_model_rows_support_bound_suffices=True`。
- `next_internal_target=ExactFactorSupportLowerBound`。
- `terminal_gap_after_router=ExactFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion`。

## 4. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `BalancedRangeSize` | WFD reduction gives U,V=C^(1/2) log^(O(1)) on balanced blocks | balanced ranges are at least log(y)^B in the clean non-edge case | range size is plausible from K1/K6, but exact lower thresholds are not recorded in A1 ledger | record explicit lower-size threshold or route small ranges back to finite PDEC/SAE | `False` |
| `DivisorBoundedFactors` | \|alpha_u\|, \|delta_v\| <= tau(uv)^C after well-factorable splitting | polylog upper bound for each factor atom | this is part of the WFD template and only costs a fixed log power | absorb into support threshold B >= A+2C | `True` |
| `ExactFactorSupportLowerBound` | not currently present as a theorem for exact Rosser/Iwaniec-Buchstab factors | sum \|alpha_u\| >= U/log^C and sum \|delta_v\| >= V/log^C on each surviving balanced block | without this, bounded factors may still be supported on one moving u and one moving v | prove squarefree/Buchstab support lower bound for exact sieve factors or route to external DI/BFI | `False` |
| `TypeFourierCapacityCompatibility` | Type-I/II and h-smoothing share the same dyadic formal unit | their Cauchy capacity does not multiply a single factor pair by an unrecorded atom | current K4 is fixed-residue L2-flat, not a moving factor-pair support theorem | state a capacity compatibility lemma or make it part of ExactFactorSupportLowerBound | `False` |
| `SupportLowerBoundImpliesEntropy` | elementary inequality max pair share <= log^(4C)/(UV) | UV >= log(y)^(2A+4C) | the implication is proved; only the exact support hypotheses remain | ExactFactorSupportLowerBound | `True` |

## 5. 阈值模型表

| k | log y | B | C | required share | support-share bound | suffices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 7 | 2 | 0.00043919 | 9.20404e-06 | `True` |
| 4 | 9.21034 | 7 | 2 | 0.000138962 | 1.63812e-06 | `True` |
| 5 | 11.5129 | 7 | 2 | 5.6919e-05 | 4.29424e-07 | `True` |
| 6 | 13.8155 | 7 | 2 | 2.74494e-05 | 1.43813e-07 | `True` |
| 7 | 16.1181 | 7 | 2 | 1.48165e-05 | 5.70319e-08 | `True` |
| 8 | 18.4207 | 7 | 2 | 8.68515e-06 | 2.55956e-08 | `True` |
| 9 | 20.7233 | 7 | 2 | 5.4221e-06 | 1.26256e-08 | `True` |

## 6. 结论

当前已证明的推进是：

```text
ExactFactorSupportLowerBound => ExactWFDSourceEntropy
=> SourceBlockEntropyNCBLK => NC-BLK.
```

但 `ExactFactorSupportLowerBound` 尚未在当前 ledger 中出现。下一步要么证明精确筛权支撑下界，
要么继续走外部 `DI/BFI original dispersion`。
