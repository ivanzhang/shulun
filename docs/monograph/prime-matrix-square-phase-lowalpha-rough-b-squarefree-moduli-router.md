# Prime Matrix square-phase low-alpha rough-b squarefree 低模账本

**状态：** `rough_b_squarefree_lowmod_divisibility_ledger_materialized_selberg_remainder_open`

Selberg 上筛需要 squarefree 模数 `d` 的整除余项，而不仅是单素数零类。本账本对 prime-a 生成的 b 多重序列统计所有 squarefree `2<=d<=D` 的 `d|b` 计数，并与随机维数一期望 `N/d` 比较。样本中相对误差阈值内无越界行；若某个 d 持续越界，它就是更强的 Squarefree-LowMod-RoughB-PDEC。当前仍未证明统一 squarefree 余项界。

```text
squarefree_lowmod_ledger_materialized=true
sample_relative_error_within_limit=true
selberg_squarefree_remainder_bound_proved=false
squarefree_lowmod_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 总览

| D limit | values | squarefree d | rel limit | flagged | worst z row | worst relative row |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1000 | 43666 | 607 | 0.350000 | 0 | `{'d': 863, 'value_count': 43666, 'actual_divisible': 70, 'expected_divisible': 50.59791425260718, 'actual_over_expected': 1.3834562359730684, 'absolute_error': 19.402085747392817, 'relative_error_to_count': 0.0004443293580220954, 'zscore': 2.729190665396867}` | `{'d': 17, 'value_count': 43666, 'actual_divisible': 2488, 'expected_divisible': 2568.5882352941176, 'actual_over_expected': 0.9686254751980946, 'absolute_error': -80.58823529411757, 'relative_error_to_count': 0.0018455602824650201, 'zscore': -1.6390374267121366}` |

## 2. 最大 z-score 行

| d | actual | expected | actual/expected | rel error | zscore |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 863 | 70 | 50.597914 | 1.383456 | 0.000444 | 2.729191 |
| 731 | 40 | 59.734610 | 0.669629 | 0.000452 | -2.555129 |
| 654 | 87 | 66.767584 | 1.303028 | 0.000463 | 2.477977 |
| 914 | 31 | 47.774617 | 0.648880 | 0.000384 | -2.428241 |
| 214 | 170 | 204.046729 | 0.833142 | 0.000780 | -2.389063 |
| 498 | 110 | 87.682731 | 1.254523 | 0.000511 | 2.385726 |
| 258 | 139 | 169.248062 | 0.821280 | 0.000693 | -2.329587 |
| 327 | 160 | 133.535168 | 1.198186 | 0.000606 | 2.293699 |
| 861 | 67 | 50.715447 | 1.321097 | 0.000373 | 2.288011 |
| 535 | 61 | 81.618692 | 0.747378 | 0.000472 | -2.284402 |
| 871 | 66 | 50.133180 | 1.316493 | 0.000363 | 2.242212 |
| 401 | 132 | 108.892768 | 1.212202 | 0.000529 | 2.217127 |
| 253 | 144 | 172.592885 | 0.834333 | 0.000655 | -2.180753 |
| 469 | 114 | 93.104478 | 1.224431 | 0.000479 | 2.167861 |
| 614 | 53 | 71.117264 | 0.745248 | 0.000415 | -2.150102 |
| 939 | 61 | 46.502662 | 1.311753 | 0.000332 | 2.127065 |

## 3. 证明边界

- 已物化：`d<=D` 的 squarefree 整除余项账本。
- 已闭合：任何越界 `d` 都可直接命名为 Squarefree-LowMod-RoughB-PDEC。
- 未闭合：对所有必要 Selberg level 的 squarefree 余项给出统一上界。
- 未闭合：排斥持久 squarefree 低模 PDEC/SAE。
- 下一目标：`SquarefreeLowModDivisibilitySelbergRemainderBoundOrPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json` | `74d26984ec6cb02e19f3f3d51f798d965b34bc9650451ab73d1bbb5fba081e3a` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.json` | `39fc08499336004b0fbf42702c1cd0d96377dd784ced4cc906fec059b9789c46` |
| `experiments/prime_matrix_square_phase_lowalpha_rough_b_squarefree_moduli_router.py` | `bc8d73e1280598d9e9451d58b0c1074ed78ca180910374c1e2a68850101c8760` |
