# Prime Matrix square-phase off-band prefix gap shadow selector H lower lpf7 CRT quota router

**状态：** `lpf7_main_layer_reduced_to_three_small_mod_crt_quota_open`

本步把 `lpf(m)<=7` 主损耗层精确压成 `3/5/7` 三小模 CRT 配额。当前 `P>=2001` 重放中唯一失败仍是 `P=2467, minus, rho=7`；非边界最小余量为 0，等号原子是 `P=5297, minus, rho=2` 的两条模板记录。三小模总支付分别为 3层 11962、5层 4629、7层 2623。严格闭合还需证明三小模 CRT 配额全局下界，并排斥边界/等号原子持久复现。

```text
max_p=10000
p0=2001
selected_hit_count_at_p0=462
lpf7_quota_failure_count_at_p0=1
lpf7_quota_exact_count_at_p0=2
min_lpf7_quota_surplus_at_p0=-8
min_nonboundary_lpf7_quota_surplus_at_p0=0
total_lpf3_loss_at_p0=11962
total_lpf5_loss_at_p0=4629
total_lpf7_exact_loss_at_p0=2623
row_column_unconditional_closed=false
```

## 1. 三小模配额

`m=P+2(b+u)` 为奇数，因此 `lpf(m)<=7` 精确等价于 `m` 被 `3`、`5` 或 `7` 整除。按最小素因子分区后三层互不重叠。

## 2. side/rho 汇总

| side | rho | hits | failures | exact | min surplus | p at min |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `minus` | 2 | 170 | 0 | 2 | 0 | `[5297]` |
| `minus` | 7 | 170 | 1 | 0 | -8 | `[2467]` |
| `plus` | 2 | 64 | 0 | 0 | 3 | `[3797]` |
| `plus` | 7 | 58 | 0 | 0 | 6 | `[2347]` |

## 3. 失败/等号原子

| p | side | rho | Bcrit | Good | cap | required | lpf<=7 | surplus | lpf3 | lpf5 | lpf7 |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | minus | 7 | 7 | 6 | 34 | 28 | 20 | -8 | 17 | 2 | 1 |
| 5297 | minus | 2 | 34 | 21 | 69 | 36 | 36 | 0 | 26 | 8 | 2 |
| 5297 | minus | 2 | 34 | 21 | 69 | 36 | 36 | 0 | 26 | 8 | 2 |

## 4. 最紧样本

| surplus | p | side | rho | required | lpf<=7 | lpf3 | lpf5 | lpf7 | cap | Good |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| -8 | 2467 | minus | 7 | 28 | 20 | 17 | 2 | 1 | 34 | 6 |
| 0 | 5297 | minus | 2 | 36 | 36 | 26 | 8 | 2 | 69 | 21 |
| 0 | 5297 | minus | 2 | 36 | 36 | 26 | 8 | 2 | 69 | 21 |
| 1 | 4567 | minus | 7 | 34 | 35 | 20 | 13 | 2 | 70 | 20 |
| 3 | 3797 | plus | 2 | 19 | 22 | 13 | 5 | 4 | 49 | 13 |
| 3 | 5807 | minus | 2 | 42 | 45 | 24 | 12 | 9 | 82 | 17 |
| 3 | 5807 | minus | 2 | 42 | 45 | 24 | 12 | 9 | 82 | 17 |
| 3 | 8117 | minus | 2 | 56 | 59 | 41 | 11 | 7 | 106 | 24 |
| 3 | 8117 | minus | 2 | 56 | 59 | 41 | 11 | 7 | 106 | 24 |
| 4 | 2837 | minus | 2 | 24 | 28 | 18 | 7 | 3 | 44 | 5 |
| 4 | 4007 | minus | 2 | 26 | 30 | 20 | 5 | 5 | 56 | 15 |
| 4 | 7547 | minus | 2 | 62 | 66 | 31 | 22 | 13 | 108 | 19 |

## 5. 结构判断

- `3` 层是主支付层，`5/7` 是补强层；三层合计才形成当前高段的主损耗安全网。
- 非边界仍有等号原子，说明下一步不能只说“大多数有余量”，必须登记等号相位。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `lpf7_three_mod_identity` | `closed` | Because every companion m is odd, lpf(m)<=7 is exactly the disjoint least-factor partition m divisible first by 3, then 5, then 7. |
| `finite_lpf7_quota_atoms` | `closed_on_current_sweep` | On the current P>=2001 sweep, the only lpf<=7 quota failure is P=2467 minus rho=7, while exact quota equalities occur at P=5297 minus rho=2. |
| `global_lpf7_crt_quota_lower_bound` | `open` | A global proof must lower-bound the 3/5/7 CRT quota in residue-cap slots or route boundary/equality atoms to PDEC/SAE. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LPF7ThreeModIdentityClosed` | `true` | `true` | `lpf<=7` 主层已化为 `3/5/7` 三小模 CRT 配额。 | closed |
| `CurrentLPF7QuotaFailureIsBoundary` | `true` | `false` | 有限重放中唯一配额失败仍是 P=2467 贴边原子。 | finite evidence only |
| `CurrentLPF7QuotaEqualityAtomsRegistered` | `true` | `false` | 有限重放中非失败等号原子为 P=5297, minus, rho=2 的两条模板记录。 | finite equality atoms |
| `GlobalLPF7CRTQuotaLowerBoundProved` | `false` | `false` | 仍需全局证明三小模 CRT 配额下界，或排斥边界/等号原子持久复现。 | LPF7CRTQuotaLowerBoundOrBoundaryEqualityAtomPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 lpf<=7 主层压成 3/5/7 配额门。 | LPF7CRTQuotaLowerBoundOrBoundaryEqualityAtomPDEC |

## 8. 下一步

- 主攻：`LPF7CRTQuotaLowerBoundOrBoundaryEqualityAtomPDEC`。
- 具体目标：证明 `3/5/7` 小模 CRT 配额下界；若边界或等号原子复现，则登记为 BoundaryEqualityAtom-PDEC/SAE 并排斥。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router.py` | `92853d6dec933195048fdd082daee899a84d98d5918fccc79ea818d8def72b26` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router.py` | `54a77f6a45dd3ed78d6b8824e9ab23834d8884f4968bfe3f80370fe136d20661` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json` | `2dd930d9965259e874fc0c98a8de210db35bc3cd250a406db3c26859933807c5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json` | `be05022761ae720821a7023374503e9d9f95810e184ffb0cc90f2b41fc351f43` |
