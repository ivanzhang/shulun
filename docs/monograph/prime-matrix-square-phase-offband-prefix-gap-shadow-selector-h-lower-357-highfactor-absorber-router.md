# Prime Matrix square-phase off-band prefix gap shadow selector H lower 357 highfactor absorber router

**状态：** `357_residual_cap_overflow_reduced_to_highfactor_absorber_open`

本步把 `3/5/7` 小筛残余拆成真素对残余与 `lpf>7` 高因子合数吸收项。当前 `P>=2001` 重放中，正残余超界行数为 1，高因子吸收失败数为 0；真素对残余上界失败数为 0。唯一正超界原子 `P=2467` 的超界量 8 被 8 个 `lpf>7` 合数槽精确吸收，因此残余超界本身不是最终矛盾；严格闭合仍需全局证明真素对残余上界，或排斥高因子吸收/素对持久相位。

```text
max_p=10000
p0=2001
positive_residual_surplus_count_at_p0=1
positive_surplus_absorber_failure_count_at_p0=0
residual_prime_pair_bound_failure_count_at_p0=0
residual_prime_pair_exact_count_at_p0=1
max_positive_residual_surplus_at_p0=8
row_column_unconditional_closed=false
```

## 1. 吸收分解

```text
357_residual_cap = residual_prime_pairs + highfactor_composite_absorbers
highfactor_composite_absorbers = #{cap slots with lpf(m)>7 and m composite}
```

残余 cap 超界只说明小筛后剩余槽多；只有其中的真素对槽超过 `Bcrit-1` 才会冲击 H 下界。

## 2. 原子表

| p | side | rho | Bcrit | residual | bound | residual surplus | prime pairs | prime surplus | highfactor | absorber surplus |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | minus | 7 | 7 | 14 | 6 | 8 | 6 | 0 | 8 | 0 |
| 5297 | minus | 2 | 34 | 33 | 33 | 0 | 21 | -12 | 12 | 12 |
| 5297 | minus | 2 | 34 | 33 | 33 | 0 | 21 | -12 | 12 | 12 |

## 3. 高因子吸收 lpf 直方图

```json
{
  "2467:minus:rho7:tpl6": {
    "11": 2,
    "13": 1,
    "17": 2,
    "23": 2,
    "43": 1
  },
  "5297:minus:rho2:tpl0": {
    "11": 5,
    "17": 2,
    "31": 1
  },
  "5297:minus:rho2:tpl5": {
    "11": 5,
    "17": 2,
    "31": 1
  }
}
```

## 4. 结构判断

- `P=2467` 的残余超界量是 8，刚好由 8 个 `lpf>7` 合数槽吸收；真素对数等于上界。
- `P=5297` 的残余等号行有 12 个高因子吸收槽，因此真素对数低于上界 12。
- 下一步应直接攻真素对残余上界，或把高因子吸收/素对共存相位登记为 PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `residual_prime_absorber_split` | `closed` | The 3/5/7 residual cap splits exactly into residual prime-pair slots plus lpf>7 high-factor composite absorber slots. |
| `finite_highfactor_absorbs_positive_residual_surplus` | `closed_on_current_sweep` | On the current P>=2001 sweep, every positive 357 residual surplus is covered by lpf>7 high-factor composite absorbers. |
| `global_residual_prime_pair_bound_or_absorber_pdec` | `open` | A global proof must bound residual prime pairs by Bcrit-1, or prove/pdec-exclude high-factor absorber persistence whenever residual cap overflows. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ResidualPrimeAbsorberSplitClosed` | `true` | `true` | 357 残余已精确分解为真素对槽与 lpf>7 高因子合数吸收槽。 | closed |
| `CurrentHighFactorAbsorbsPositiveSurplus` | `true` | `false` | 有限重放中所有正残余超界都由高因子合数吸收。 | finite evidence only |
| `CurrentResidualPrimePairBoundClosed` | `true` | `false` | 有限重放中真素对残余未超过上界；全局证明仍缺。 | finite evidence only |
| `GlobalResidualPrimePairBoundOrAbsorberPDECProved` | `false` | `false` | 仍需全局证明真素对残余上界，或排斥高因子吸收持久相位。 | ResidualPrimePairBoundOrHighFactorAbsorberPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 357 残余超界压成高因子吸收门。 | ResidualPrimePairBoundOrHighFactorAbsorberPDEC |

## 7. 下一步

- 主攻：`ResidualPrimePairBoundOrHighFactorAbsorberPDEC`。
- 具体目标：证明 residual prime-pair count `<=Bcrit-1`，或证明/排斥高因子吸收与真素对持久共存 PDEC。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router.py` | `e1779886fe9e8d60475b5a05ec1f99ba4a1c5a4198811c8ee0af1da6b2826ce8` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router.py` | `bd8d3177dad3931beb4aa7429b727a706629f931df6a9433e5c69228ed1cd7b8` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py` | `1e559ec00bf764d861c0ad5a4bde7c3563c27d511a9d9ba2dd46170ae16badc7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json` | `24a8d2424b1bbda4b24f238d13f2366957de31a866968cfd63cf9ce7c339cd5b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json` | `08cbcdd5cfb11a2e2fa63f1e4cf0165998cdb6490c88e516bd7dcdc03b091d5b` |
