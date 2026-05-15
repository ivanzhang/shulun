# Prime Matrix square-phase off-band prefix gap shadow selector H lower 357 residual cap router

**状态：** `lpf7_crt_quota_reduced_to_357_residual_cap_bound_open`

本步把 `lpf<=7` 配额下界改写成小筛残余 cap 上界：`cap_count-lpf7_loss <= Bcrit-1`。当前 `P>=2001` 重放中唯一残余超界仍是 `P=2467, minus, rho=7`，残余等号原子是 `P=5297, minus, rho=2` 的两条模板记录；所有 plus 侧都有正安全余量。严格闭合还需全局证明 3/5/7 小筛残余 cap 上界，或排斥 minus-side 边界/等号原子持久复现。

```text
max_p=10000
p0=2001
selected_hit_count_at_p0=462
residual_failure_count_at_p0=1
residual_exact_count_at_p0=2
max_residual_surplus_to_bound_at_p0=8
max_residual_cap_count_at_p0=65
row_column_unconditional_closed=false
```

## 1. 等价式

```text
lpf7_loss >= cap_count-Bcrit+1
<=> cap_count-lpf7_loss <= Bcrit-1
```

左侧是小因子损耗下界，右侧是经过 `3/5/7` 小筛后的 residue-cap 残余槽上界。

## 2. side/rho 汇总

| side | rho | hits | failures | exact | max residual surplus | p at max |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `minus` | 2 | 170 | 0 | 2 | 0 | `[5297]` |
| `minus` | 7 | 170 | 1 | 0 | 8 | `[2467]` |
| `plus` | 2 | 64 | 0 | 0 | -3 | `[3797]` |
| `plus` | 7 | 58 | 0 | 0 | -6 | `[2347]` |

## 3. 残余失败/等号原子

| p | side | rho | Bcrit | Good | cap | lpf7 loss | residual | bound | surplus |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | minus | 7 | 7 | 6 | 34 | 20 | 14 | 6 | 8 |
| 5297 | minus | 2 | 34 | 21 | 69 | 36 | 33 | 33 | 0 |
| 5297 | minus | 2 | 34 | 21 | 69 | 36 | 33 | 33 | 0 |

## 4. 结构判断

- 现在的主硬点不是“有多少合数”，而是 `3/5/7` 小筛后还剩多少 cap 槽。
- 当前所有硬原子都在 minus 侧；plus 侧有限重放有正余量。
- 这一步直接适配层叠筛：下一步应证明小筛残余无法高于 `Bcrit-1`，或把 minus-side 原子登记为 PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `lpf7_quota_residual_equivalence` | `closed` | The lpf<=7 quota lower bound is equivalent to small_sieve_357_residual_cap_count <= Bcrit-1. |
| `finite_residual_atoms` | `closed_on_current_sweep` | On the current P>=2001 sweep, the only residual surplus failure is P=2467 minus rho=7; residual equalities occur at P=5297 minus rho=2. |
| `global_357_residual_cap_bound` | `open` | A global proof must bound the 3/5/7-sieved residual cap slots below Bcrit, or route minus-side boundary/equality atoms to PDEC/SAE. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LPF7QuotaResidualEquivalenceClosed` | `true` | `true` | `lpf<=7` 配额已等价改写为 3/5/7 小筛残余 cap 上界。 | closed |
| `CurrentResidualFailureIsBoundary` | `true` | `false` | 有限重放中唯一残余超界是 P=2467 贴边原子。 | finite evidence only |
| `CurrentResidualEqualityAtomsRegistered` | `true` | `false` | 有限重放中残余等号原子为 P=5297 的两条模板记录。 | finite equality atoms |
| `Global357ResidualCapBoundProved` | `false` | `false` | 仍需全局证明 3/5/7 小筛残余 cap 上界，或排斥 minus-side 原子持久复现。 | SmallSieve357ResidualCapBoundOrMinusQuotaAtomPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把配额门改写成残余上界门。 | SmallSieve357ResidualCapBoundOrMinusQuotaAtomPDEC |

## 7. 下一步

- 主攻：`SmallSieve357ResidualCapBoundOrMinusQuotaAtomPDEC`。
- 具体目标：证明 `3/5/7` 小筛残余 cap 上界；若 minus-side 边界/等号原子复现，则登记为 MinusQuotaAtom-PDEC/SAE 并排斥。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router.py` | `bd8d3177dad3931beb4aa7429b727a706629f931df6a9433e5c69228ed1cd7b8` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router.py` | `92853d6dec933195048fdd082daee899a84d98d5918fccc79ea818d8def72b26` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json` | `be05022761ae720821a7023374503e9d9f95810e184ffb0cc90f2b41fc351f43` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json` | `24a8d2424b1bbda4b24f238d13f2366957de31a866968cfd63cf9ce7c339cd5b` |
