# Prime Matrix square-phase off-band prefix gap shadow selector H lower equality atom PDEC router

**状态：** `residual_prime_single_equality_atom_registered_as_pdec_open`

本步把唯一 residual-prime 等号原子登记为 formal-unit PDEC 候选。该原子为 `P=2467, minus, rho=7`，cap 分区为 low357=20、highfactor=8、prime_pairs=6；其中 residual prime pairs 恰等于 `Bcrit-1`，所以 margin=0。这仍不是全局闭合；下一步必须排斥该等号相位持久复现，或证明全局正 margin。

```text
unit_id=residual-prime-equality|p=2467|side=minus|rho=7|template=6|Bcrit=7|margin=0
equality_atom_count=1
low357_composite_count=20
highfactor_absorber_count=8
residual_prime_pair_count=6
total_cap_count=34
partition_identity_closed=false
row_column_unconditional_closed=false
```

## 1. Formal Unit

```json
{
  "Bcrit": 7,
  "bound": 6,
  "margin": 0,
  "p": 2467,
  "rho": 7,
  "side": "minus",
  "template_index": 6,
  "unit_id": "residual-prime-equality|p=2467|side=minus|rho=7|template=6|Bcrit=7|margin=0"
}
```

## 2. 真素对槽

| b | u | q | m | s | r | m mod 3 | m mod 5 | m mod 7 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 37 | 1 | 2393 | 2543 | 345 | 690 | 2 | 3 | 2 |
| 60 | 3 | 2347 | 2593 | 159 | 318 | 1 | 3 | 3 |
| 78 | 5 | 2311 | 2633 | 613 | 1226 | 2 | 3 | 1 |
| 97 | 8 | 2273 | 2677 | 634 | 1268 | 1 | 2 | 3 |
| 112 | 11 | 2243 | 2713 | 415 | 830 | 1 | 3 | 4 |
| 219 | 47 | 2029 | 2999 | 559 | 1118 | 2 | 4 | 3 |

## 3. 高因子吸收槽

| b | u | q | m | lpf(m) | s | r |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15 | 0 | 2437 | 2497 | 11 | 450 | 900 |
| 63 | 3 | 2341 | 2599 | 23 | 915 | 1830 |
| 162 | 24 | 2143 | 2839 | 17 | 1056 | 2112 |
| 184 | 32 | 2099 | 2899 | 13 | 544 | 1088 |
| 192 | 35 | 2083 | 2921 | 23 | 823 | 1646 |
| 199 | 38 | 2069 | 2941 | 17 | 580 | 1160 |
| 235 | 55 | 1997 | 3047 | 11 | 615 | 1230 |
| 237 | 56 | 1993 | 3053 | 43 | 730 | 1460 |

## 4. 结构判断

- 等号原子要求 6 个 residual prime-pair 槽全部保留，任何一个转为合数都会产生正 margin。
- 同一原子还需要 8 个高因子吸收槽精确吸收 357 残余超界；这是一个高度刚性的相位配置。
- 下一步要证明这种 formal unit 不能在高处持久复现，或给出全局 margin 正下界。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `single_equality_atom_formal_unit_registered` | `closed` | The unique current equality atom is registered as a formal unit with side, rho, template, cap partition, prime-pair slots, and absorber slots. |
| `equality_atom_partition_identity` | `closed` | For the equality atom, cap=low357 composites + highfactor composites + residual prime pairs, and residual prime pairs equal Bcrit-1. |
| `global_equality_atom_nonpersistence` | `open` | A global proof must exclude persistent recurrence of this formal equality pattern or prove a positive residual-prime margin away from it. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `EqualityAtomPDECRegistrationClosed` | `true` | `true` | 唯一等号原子已登记为 formal-unit PDEC 候选。 | closed |
| `EqualityAtomPartitionIdentityClosed` | `false` | `true` | 等号原子的 cap 分区与 margin=0 身份闭合。 | closed |
| `EqualityAtomPDECExcluded` | `false` | `false` | 仍需排斥该等号 formal unit 的持久复现。 | ResidualPrimeEqualityAtomPDECExclusionOrGlobalMarginJump |
| `GlobalMarginJumpProved` | `false` | `false` | 仍需证明全局正 margin 或 12 跳跃余量。 | ResidualPrimeEqualityAtomPDECExclusionOrGlobalMarginJump |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只登记等号原子，不关闭全局命题。 | ResidualPrimeEqualityAtomPDECExclusionOrGlobalMarginJump |

## 7. 下一步

- 主攻：`ResidualPrimeEqualityAtomPDECExclusionOrGlobalMarginJump`。
- 具体目标：排斥该 equality formal unit 的持久复现，或证明 residual prime margin 全局正下界。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_pdec_router.py` | `2ef7c1f621c75ed1481abf97c7e6b1e8b9095b0ed34390432e656e705b1e5e75` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py` | `1e559ec00bf764d861c0ad5a4bde7c3563c27d511a9d9ba2dd46170ae16badc7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json` | `299142fca047a22e5c7b50dded1c01b6330bf08143b01609e2b90387b67d6330` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json` | `631a87ae9131deabfaadb40928de4a26de1b647a7b7d7accd35093ef6d5bb7ae` |
