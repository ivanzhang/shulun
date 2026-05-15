# Prime Matrix square-phase off-band prefix gap shadow selector tail upper pi input router

**状态：** `tail_upper_closed_on_external_pi_lane_self_contained_pi_interval_open`

尾素数项已被单独压缩：有限桥显示 `T<=0.212P/logP` 对所有 `P>=2001` 素数只有 `2753,2803` 两个 universal 例外；既有 selector 重放中 `T` 上界失败数为 0，所以这两个例外不进入当前 selector 命中。对 `P>=ceil(exp(15.0))=3269018`，外部 Dusart 型 pi 双侧界给出 `T<=0.212P/logP`。因此外部路线中尾上界门可关闭；严格自足路线仍需内化 pi 双侧区间界。

```text
p0=2001
target_t_coeff=0.212
high_p0=3269018
finite_bridge_prime_count=234552
finite_bridge_failure_p_values=[2753, 2803]
prior_selector_t_upper_failure_count_at_p0=0
external_tail_upper_closed=true
self_contained_tail_upper_closed=false
row_column_unconditional_closed=false
```

## 1. 有限桥

| range | prime count | failure count | max T coeff | p at max |
| --- | ---: | ---: | ---: | ---: |
| 2001..10000 | 926 | 2 | 0.21289976076300504 | 2753 |
| 10001..100000 | 8363 | 0 | 0.20936678921805718 | 24203 |
| 100001..1000000 | 68906 | 0 | 0.2034479000641852 | 211949 |
| 1000001..3269017 | 156357 | 0 | 0.20210232308427012 | 1197409 |

有限 universal 失败只有：

| p | T | T log(P)/P |
| ---: | ---: | ---: |
| 2753 | 74 | 0.21289976076300504 |
| 2803 | 75 | 0.21240935295660332 |

这两个失败点均小于既有 selector 重放上界 `P<=10000`，而上一系数拆分账本给出 `T_upper_failure_count_at_p0=0`，所以它们不进入 selector rho hit。

## 2. 高段 pi 输入

高段使用外部 Dusart 型模板：

```text
pi(x) <= x/log(x) * (1 + 1/log(x) + 2.51/log(x)^2)
pi(x) >= x/log(x) * (1 + 1/log(x))
```

为处理取整，使用 `floor(4P/5)>=0.799P`。于是 `P>=ceil(exp(15))` 时有：

```text
R(L)=1+1/L+2.51/L^2-0.799*L/(L-log(1/0.799))*(1+1/(L-log(1/0.799)))
R(15)=0.21179110642894328
0.212-R(15)=0.00020889357105671746
```

导数证书：

- For L>=15, R'(L)<0 for c=0.799 and upper_c2=2.51.
- 归约不等式：`Use a=-log(0.799)<0.225. It is enough to prove 0.799*L^3*(1.225L+0.225) < (L+5.02)*(L-0.225)^3.`
- 正多项式：`(67920*L^4 + 13328720*L^3 - 10357200*L^2 + 2403270*L - 182979)/3200000`
- `L=15` 处值：`14415.1175221875`。

## 3. 外部/自足边界

| input | role | self-contained |
| --- | --- | ---: |
| Dusart-type pi upper bound | high-segment upper bound for pi(P-1) | `false` |
| Dusart/Rosser-Schoenfeld-type pi lower bound | high-segment lower bound for pi(floor(4P/5)) | `false` |
| finite exact pi prefix bridge | handles P<ceil(exp(15)) and isolates two non-selector exceptions | `true` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `tail_count_exact_identity` | `closed` | T is exactly pi(P-1)-pi(floor(4P/5)). |
| `finite_tail_upper_bridge` | `closed` | For all prime P in the finite bridge, the only universal failures are P=2753 and P=2803. |
| `selector_exception_exclusion` | `closed_by_prior_selector_replay` | The two universal finite exceptions do not occur among selector rho hits in the P<=10000 replay. |
| `external_dusart_high_tail_upper` | `closed_on_external_pi_input` | Dusart-type two-sided pi bounds imply T<=0.212P/logP for P>=ceil(exp(15)). |
| `self_contained_pi_two_sided_interval_input` | `open` | A strict self-contained route still needs the pi two-sided interval ledger, unless the external Dusart input is accepted. |
| `square_window_lower_coefficient` | `open` | After the tail upper input, the remaining coefficient gate is H>=0.43P/logP, or a correlated surplus replacement. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TailUpperExternalLaneClosed` | `true` | `false` | 接受外部 Dusart 型 pi 双侧界时，T 上界门可关闭；该门不是严格自足证明。 | SquareWindowLowerCoefficientOrCorrelatedSurplusPDEC |
| `TailUpperStrictSelfContainedClosed` | `false` | `false` | 仓库当前 theta 自足包不能直接替代 pi 双侧区间界。 | SelfContainedDusartPiTwoSidedIntervalLedger |
| `FiniteExceptionsHitSelector` | `true` | `true` | 有限 universal 例外不进入 selector 命中，因此不破坏本路线。 | closed |
| `CoefficientSplitFullyClosed` | `false` | `false` | 仍需平方窗 H 下系数，或直接相关余量定理。 | SquareWindowLowerCoefficientOrCorrelatedSurplusPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭/登记尾素数上界输入，不产生最终反例矛盾。 | SquareWindowLowerCoefficientOrCorrelatedSurplusPDEC |

## 6. 下一步

- 外部路线主攻：`SquareWindowLowerCoefficientOrCorrelatedSurplusPDEC`。
- 严格自足路线补件：`SelfContainedDusartPiTwoSidedIntervalLedger`。
- 数学主线不要再转移到尾项；应直接攻 selector 平方窗下系数 `H>=0.43P/logP`，或证明相关余量 `H-2T>=cP/logP`。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router.py` | `f3edbf2be92f4f18bac9908c635ef0866b92c1be3a65d932f788f138fdfc7f1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json` | `339e3bfc87be2bf82c88e8b47ac47719e576d67bdfb06092e122d82d78ff6448` |
| `data/square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json` | `d2736d775a1d60c5e18fa8fd4598921c9030bfb03d9bc464cafcf0c7a3a6c460` |
