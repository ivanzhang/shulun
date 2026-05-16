# Prime Matrix square-phase off-band prefix gap shadow selector H lower minimal subcertificate router

**状态：** `moving_slot_family_reduced_to_one_or_two_slot_subcertificates_open`

本步把 moving-slot family 的固定图样隔离进一步压成最小子证书。当前 `P>=2001` 重放中，所有 462 条 selector 行都存在大小不超过 2 的隔离子证书；其中单槽 399 条、双槽 63 条。唯一等号原子有单槽证书。这把剩余硬点降为一槽/二槽 moving certificate 的持久性排斥，仍不是全局无条件闭合。

```text
max_p=10000
p0=2001
selected_hit_count_at_p0=462
subcertificate_failure_count_at_p0=0
minimal_certificate_size_histogram_at_p0={'1': 399, '2': 63}
max_minimal_certificate_size_at_p0=2
min_subcertificate_margin_at_p0=1
equality_atom_minimal_certificate_size=1
row_column_unconditional_closed=false
```

## 1. 子证书判据

```text
A highfactor subset S is an isolation subcertificate if:
  CRT_modulus(S) > common_phase_width(S).
Then fixed S can occur for at most one P in its phase support.
```

## 2. 等号原子子证书

| p | side | rho | margin | cert size | CRT modulus | phase width | CRT-width | slots |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2467 | `minus` | 7 | 0 | 1 | 43 | 22 | 21 | `[(237, 56, 43)]` |

## 3. 最紧子证书样本

| p | side | rho | template | margin | cert size | CRT modulus | phase width | CRT-width | slots |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2467 | `minus` | 7 | 6 | 0 | 1 | 43 | 22 | 21 | `[(237, 56, 43)]` |
| 2347 | `plus` | 7 | 2 | 12 | 1 | 47 | 36 | 11 | `[(180, 33, 47)]` |
| 2347 | `plus` | 7 | 3 | 12 | 1 | 47 | 36 | 11 | `[(180, 33, 47)]` |
| 5297 | `minus` | 2 | 0 | 12 | 1 | 47 | 26 | 21 | `[(470, 101, 47)]` |
| 5297 | `minus` | 2 | 5 | 12 | 1 | 47 | 26 | 21 | `[(470, 101, 47)]` |
| 3767 | `plus` | 2 | 4 | 12 | 1 | 61 | 36 | 25 | `[(290, 53, 61)]` |
| 2243 | `plus` | 2 | 4 | 12 | 2 | 323 | 17 | 306 | `[(128, 17, 17), (155, 25, 19)]` |
| 2027 | `minus` | 2 | 5 | 13 | 1 | 37 | 25 | 12 | `[(185, 41, 37)]` |
| 2063 | `plus` | 2 | 4 | 13 | 1 | 47 | 28 | 19 | `[(177, 37, 47)]` |
| 2927 | `minus` | 2 | 0 | 13 | 2 | 1591 | 160 | 1431 | `[(69, 3, 37), (99, 7, 43)]` |
| 2927 | `minus` | 2 | 5 | 13 | 2 | 1591 | 160 | 1431 | `[(69, 3, 37), (99, 7, 43)]` |
| 2267 | `minus` | 2 | 5 | 14 | 2 | 1457 | 52 | 1405 | `[(102, 10, 47), (135, 18, 31)]` |
| 5407 | `minus` | 7 | 6 | 15 | 1 | 29 | 26 | 3 | `[(483, 105, 29)]` |
| 2687 | `minus` | 2 | 5 | 15 | 1 | 29 | 25 | 4 | `[(242, 53, 29)]` |
| 2837 | `minus` | 2 | 5 | 15 | 1 | 31 | 23 | 8 | `[(270, 63, 31)]` |
| 4007 | `minus` | 2 | 5 | 15 | 1 | 61 | 30 | 31 | `[(338, 68, 61)]` |
| 2207 | `minus` | 2 | 0 | 15 | 2 | 989 | 83 | 906 | `[(35, 1, 43), (114, 13, 23)]` |
| 2207 | `minus` | 2 | 5 | 15 | 2 | 989 | 83 | 906 | `[(35, 1, 43), (114, 13, 23)]` |
| 2297 | `minus` | 2 | 5 | 15 | 2 | 989 | 34 | 955 | `[(77, 5, 23), (143, 20, 43)]` |
| 2647 | `minus` | 7 | 6 | 15 | 2 | 1147 | 30 | 1117 | `[(183, 29, 37), (205, 37, 31)]` |
| 4567 | `minus` | 7 | 6 | 16 | 1 | 37 | 24 | 13 | `[(417, 93, 37)]` |
| 2137 | `minus` | 7 | 1 | 16 | 1 | 43 | 24 | 19 | `[(198, 45, 43)]` |
| 2137 | `minus` | 7 | 6 | 16 | 1 | 43 | 24 | 19 | `[(198, 45, 43)]` |
| 2557 | `plus` | 7 | 2 | 16 | 1 | 43 | 24 | 19 | `[(237, 54, 43)]` |

## 4. 失败形态

当前重放中没有大小不超过设定阈值的子证书失败。

## 5. 结构判断

- 大多数行甚至由单个高因子槽隔离；剩余少数只需两个槽。
- 因此 moving-slot family 的真正硬点已降到一槽/二槽证书的持久性，而不是多槽组合复杂性。
- 下一步要分别处理单槽移动和双槽移动：单槽是 `ell > phase_width` 的一维相位锁，双槽是两个相位区间交叠加 CRT 乘子锁。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `subcertificate_isolation_criterion` | `closed` | Any subset of highfactor slots whose CRT modulus exceeds its common phase-support width isolates that fixed subset pattern. |
| `current_sweep_one_or_two_slot_subcertificates` | `closed_on_current_sweep` | On the current selector sweep, every highfactor-isolated row has a one-slot or two-slot isolation subcertificate. |
| `one_or_two_slot_moving_family_exclusion` | `open` | A global proof must exclude persistent one-slot/two-slot moving certificates or route them to ColumnCRT/PDEC. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SubcertificateIsolationCriterionClosed` | `true` | `true` | 任意子集 CRT 模数超过相位宽度即可隔离固定子图样。 | closed |
| `CurrentSweepCoveredBySizeAtMostTwo` | `true` | `false` | 当前重放全部由一槽/二槽子证书覆盖。 | finite evidence only |
| `EqualityAtomOneSlotSubcertificateClosed` | `true` | `true` | 唯一等号原子有单槽隔离证书，因此固定等号图样更强地孤立。 | closed |
| `OneOrTwoSlotMovingFamilyExcluded` | `false` | `false` | 一槽/二槽 moving certificate 的持久族尚未排斥。 | OneOrTwoSlotMovingCertificatePDECOrGlobalResidualPrimeMarginJump |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压缩 moving family 的证书阶数，不关闭全局行/列命题。 | OneOrTwoSlotMovingCertificatePDECOrGlobalResidualPrimeMarginJump |

## 8. 下一步

- 主攻：`OneOrTwoSlotMovingCertificatePDECOrGlobalResidualPrimeMarginJump`。
- 具体目标：证明一槽/二槽 moving certificate 不能持久复现，或把其接入正式 `ColumnCRT/PDEC` 排斥证书。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router.py` | `731c4bc285e87e7a8f430bd4ff2ed6068717944dfea2d1ddfcc10e34bdfb12e3` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router.py` | `e1a404fa0ebb30743072fd9b36905fd3a6987ada49ffa3ac1be9229afa4fb303` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py` | `8cfbb81aa5e0744be24413f0f598341a52b2ab155141b751cb6f88096fe292b8` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json` | `f2c69912fe26fc88d0f02df98c514cfa7ba407226b67de20b9b1db98ff8b3b08` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json` | `65b36c6b248a45607ec514dfb648829016fe66537b6aa2ac327bd385269773f9` |
