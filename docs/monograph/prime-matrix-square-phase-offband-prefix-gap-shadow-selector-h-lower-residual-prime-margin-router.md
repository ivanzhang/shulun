# Prime Matrix square-phase off-band prefix gap shadow selector H lower residual prime margin router

**状态：** `residual_prime_pair_bound_reduced_to_single_equality_atom_margin_jump_open`

本步把 residual prime-pair 上界压成余量形式：`margin=Bcrit-1-residual_prime_pair_count`。当前 `P>=2001` 重放中失败数为 0，等号原子数为 1；唯一等号原子是 `P=2467`，排除等号后最小余量跳到 12。严格闭合还需证明等号原子不能持久复现，或建立全局正余量下界。

```text
max_p=10000
p0=2001
residual_prime_pair_margin_failure_count_at_p0=0
residual_prime_pair_margin_exact_count_at_p0=1
min_residual_prime_pair_margin_at_p0=0
min_margin_after_removing_exact_atoms_at_p0=12
single_equality_atom_p_values_at_p0=[2467]
row_column_unconditional_closed=false
```

## 1. 余量形式

```text
margin = Bcrit - 1 - residual_prime_pair_count
safe <=> margin >= 0
exact atom <=> margin = 0
```

## 2. side/rho 汇总

| side | rho | hits | failures | exact | min margin | p at min |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `minus` | 2 | 170 | 0 | 0 | 12 | `[5297]` |
| `minus` | 7 | 170 | 0 | 1 | 0 | `[2467]` |
| `plus` | 2 | 64 | 0 | 0 | 12 | `[2243, 3767]` |
| `plus` | 7 | 58 | 0 | 0 | 12 | `[2347]` |

## 3. 等号原子

| p | side | rho | Bcrit | Good | bound | prime pairs | margin | residual | highfactor |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | minus | 7 | 7 | 6 | 6 | 6 | 0 | 14 | 8 |

## 4. 最紧样本

| margin | p | side | rho | template | bound | prime pairs | residual | highfactor |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 2467 | minus | 7 | 6 | 6 | 6 | 14 | 8 |
| 12 | 2243 | plus | 2 | 4 | 21 | 9 | 13 | 4 |
| 12 | 2347 | plus | 7 | 2 | 17 | 5 | 11 | 6 |
| 12 | 2347 | plus | 7 | 3 | 17 | 5 | 11 | 6 |
| 12 | 3767 | plus | 2 | 4 | 28 | 16 | 22 | 6 |
| 12 | 5297 | minus | 2 | 0 | 33 | 21 | 33 | 12 |
| 12 | 5297 | minus | 2 | 5 | 33 | 21 | 33 | 12 |
| 13 | 2027 | minus | 2 | 5 | 18 | 5 | 11 | 6 |
| 13 | 2063 | plus | 2 | 4 | 21 | 8 | 11 | 3 |
| 13 | 2927 | minus | 2 | 0 | 24 | 11 | 18 | 7 |
| 13 | 2927 | minus | 2 | 5 | 24 | 11 | 18 | 7 |
| 14 | 2267 | minus | 2 | 5 | 19 | 5 | 12 | 7 |
| 15 | 2207 | minus | 2 | 0 | 22 | 7 | 12 | 5 |
| 15 | 2207 | minus | 2 | 5 | 22 | 7 | 12 | 5 |

## 5. 结构判断

- 当前有限段没有 residual prime-pair 超界。
- 唯一等号原子为 `P=2467, minus, rho=7`；排除它后最小余量为 `12`，没有 1 到 11 的近失效层。
- 这把剩余硬点压成：证明等号原子不持久，或给出全局 margin 正下界。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `residual_prime_pair_margin_form` | `closed` | The residual prime-pair safety condition is equivalent to margin=Bcrit-1-residual_prime_pair_count >=0. |
| `finite_single_equality_atom_and_margin_jump` | `closed_on_current_sweep` | On the current P>=2001 sweep there is exactly one equality atom, P=2467 minus rho=7; after removing it, the minimum margin jumps to 12. |
| `global_single_equality_atom_exclusion` | `open` | A global proof must show residual prime-pair margin remains positive away from nonpersistent equality atoms, or route equality persistence to PDEC/SAE. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ResidualPrimePairMarginFormClosed` | `true` | `true` | 真素对残余上界已改写为 margin>=0。 | closed |
| `CurrentResidualPrimeBoundHasNoFailure` | `true` | `false` | 有限重放中没有真素对残余超界。 | finite evidence only |
| `CurrentSingleEqualityAtomRegistered` | `true` | `false` | 有限重放中唯一等号原子已登记。 | finite equality atom |
| `CurrentNonEqualityMarginJumpObserved` | `true` | `false` | 排除等号原子后，有限重放最小余量跳到 12。 | finite evidence only |
| `GlobalEqualityAtomPDECExcluded` | `false` | `false` | 仍需全局排斥等号原子持久复现，或给出 margin 正下界。 | ResidualPrimePairSingleEqualityAtomOrMarginJumpPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把真素对残余上界压成单等号原子与余量跳跃。 | ResidualPrimePairSingleEqualityAtomOrMarginJumpPDEC |

## 8. 下一步

- 主攻：`ResidualPrimePairSingleEqualityAtomOrMarginJumpPDEC`。
- 具体目标：排斥 `P=2467` 型 residual-prime 等号相位持久复现，或建立全局正 margin 下界。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py` | `8cfbb81aa5e0744be24413f0f598341a52b2ab155141b751cb6f88096fe292b8` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router.py` | `e1779886fe9e8d60475b5a05ec1f99ba4a1c5a4198811c8ee0af1da6b2826ce8` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json` | `08cbcdd5cfb11a2e2fa63f1e4cf0165998cdb6490c88e516bd7dcdc03b091d5b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json` | `299142fca047a22e5c7b50dded1c01b6330bf08143b01609e2b90387b67d6330` |
