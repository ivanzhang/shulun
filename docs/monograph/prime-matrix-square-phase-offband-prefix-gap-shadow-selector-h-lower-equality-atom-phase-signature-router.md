# Prime Matrix square-phase off-band prefix gap shadow selector H lower equality atom phase signature router

**状态：** `exact_fixed_slot_equality_atom_nonpersistent_moving_slot_open`

本步关闭固定槽级等号原子的持久性。8 个高因子吸收槽合并为 5 个相容 CRT 条件，给出 `P ≡ 2467 (mod 2404259)`；同时 14 个固定 `b,u` 槽的相位支撑交集为 `[2460,2478]`。二者在该交集中只命中注册原子 `P=2467`。这排除了 exact fixed-slot formal unit 的复现，但移动槽/模板级等号复现仍需继续排斥。

```text
registered_p=2467
highfactor_crt=P≡2467 mod 2404259
odd_prime_physical_period=4808518
phase_intersection=[2460,2478]
phase_intersection_primes=[2467, 2473, 2477]
crt_hits_inside_phase_intersection=[2467]
exact_fixed_slot_nonpersistence_proved=true
row_column_unconditional_closed=false
```

## 1. 高因子 CRT 签名

| ell | residue | slots | compatible |
| ---: | ---: | ---: | ---: |
| 11 | 3 | 2 | true |
| 13 | 10 | 1 | true |
| 17 | 2 | 2 | true |
| 23 | 6 | 2 | true |
| 43 | 16 | 1 | true |

## 2. 固定槽相位支撑

| type | b | u | q | m | r | P lo | P hi | contains P |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `highfactor_composite` | 15 | 0 | 2437 | 2497 | 900 | 901 | 1000000000000000000000000000000 | true |
| `residual_prime_pair` | 37 | 1 | 2393 | 2543 | 690 | 1875 | 2811 | true |
| `residual_prime_pair` | 60 | 3 | 2347 | 2593 | 318 | 2161 | 2519 | true |
| `highfactor_composite` | 63 | 3 | 2341 | 2599 | 1830 | 2377 | 2771 | true |
| `residual_prime_pair` | 78 | 5 | 2311 | 2633 | 1226 | 2355 | 2589 | true |
| `residual_prime_pair` | 97 | 8 | 2273 | 2677 | 1268 | 2397 | 2546 | true |
| `residual_prime_pair` | 112 | 11 | 2243 | 2713 | 830 | 2396 | 2504 | true |
| `highfactor_composite` | 162 | 24 | 2143 | 2839 | 2112 | 2460 | 2510 | true |
| `highfactor_composite` | 184 | 32 | 2099 | 2899 | 1088 | 2446 | 2483 | true |
| `highfactor_composite` | 192 | 35 | 2083 | 2921 | 1646 | 2456 | 2490 | true |
| `highfactor_composite` | 199 | 38 | 2069 | 2941 | 1160 | 2451 | 2482 | true |
| `residual_prime_pair` | 219 | 47 | 2029 | 2999 | 1118 | 2453 | 2478 | true |
| `highfactor_composite` | 235 | 55 | 1997 | 3047 | 1230 | 2456 | 2478 | true |
| `highfactor_composite` | 237 | 56 | 1993 | 3053 | 1460 | 2459 | 2480 | true |

## 3. 真素对槽未被高因子签名自动摧毁

| b | u | q | m | q zero mod highfactor | m zero mod highfactor | nonforced |
| ---: | ---: | ---: | ---: | --- | --- | ---: |
| 37 | 1 | 2393 | 2543 | `[]` | `[]` | true |
| 60 | 3 | 2347 | 2593 | `[]` | `[]` | true |
| 78 | 5 | 2311 | 2633 | `[]` | `[]` | true |
| 97 | 8 | 2273 | 2677 | `[]` | `[]` | true |
| 112 | 11 | 2243 | 2713 | `[]` | `[]` | true |
| 219 | 47 | 2029 | 2999 | `[]` | `[]` | true |

## 4. 结构判断

- 高因子吸收槽给出的是强 CRT 锁相，不是松散统计现象。
- 固定 `b,u` 槽相位支撑极窄，和 CRT 签名相交只剩 `P=2467`。
- 因此 exact fixed-slot equality formal unit 已不能持久复现。
- 这仍不排斥移动 `b,u` 槽或同模板等号原子在高处复现；全局行/列命题仍未闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_slot_highfactor_crt_signature` | `closed` | The eight high-factor absorber slots impose five compatible congruences whose CRT representative is the registered P. |
| `fixed_bu_phase_support_is_local` | `closed` | Keeping all fourteen b/u slots in the same Euclidean cap phase forces P into the short interval [2460,2478]. |
| `exact_slot_formal_unit_nonpersistent` | `closed` | The fixed-slot equality formal unit is isolated: the CRT signature and phase support intersect only at P=2467. |
| `moving_slot_or_template_level_recurrence` | `open` | A global proof must still exclude equality recurrence with moving b/u slots or prove a global positive margin. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `HighFactorCRTSignatureClosed` | `true` | `true` | 8 个高因子吸收槽合并为 5 个相容 CRT 条件。 | closed |
| `FixedSlotPhaseSupportClosed` | `true` | `true` | 所有固定 b/u 槽共同只允许短相位区间。 | closed |
| `ExactFixedSlotFormalUnitExcludedBeyondRegisteredP` | `true` | `true` | 固定槽级等号原子不能在别的 P 上复现。 | closed |
| `MovingSlotEqualityAtomExcluded` | `false` | `false` | 移动槽/模板级等号复现仍未排斥。 | MovingSlotEqualityAtomPDECExclusionOrGlobalMarginJump |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭固定槽等号原子持久性，不关闭全局命题。 | MovingSlotEqualityAtomPDECExclusionOrGlobalMarginJump |

## 7. 下一步

- 主攻：`MovingSlotEqualityAtomPDECExclusionOrGlobalMarginJump`。
- 具体目标：把 moving-slot/template-level 等号复现也压成相位签名，或证明 residual prime margin 全局正下界。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_phase_signature_router.py` | `0f6583ab8576ef179aedf3c9ffc9b91c811edf794ce02c9f36b0b772f401aee3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json` | `8c8ff584751f4c6af83ee0c176dc5ba85e18ffe2d9e408457042f4395f786305` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json` | `2eead30b6146d396e58ba12ed94c9edf892b3237c4dc49eb216288ae7be9134e` |
