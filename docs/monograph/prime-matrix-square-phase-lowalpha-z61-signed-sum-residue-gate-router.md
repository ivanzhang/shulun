# Prime Matrix square-phase low-alpha z=61 signed-sum residue gate

**状态：** `z61_carry_layer_projection_reduced_to_five_term_signed_sum_residue_gate_open`

carry-layer 目标纤维可写成五项 signed-sum 的区间同余门：`S=±14421±19228±36708±382536±12540`，`cM<=S<(c+1)M`，且 `S mod 2627` 落在随 carry 平移的目标类中。当前 formal unit 中唯一命中为 `S=373055`、`c=6`、`S mod 2627=21`、符号字 `--++-`，对应 `r=26951`。因此最新硬点成为五项 signed-sum 区间同余纤维的全局界，或登记 SumResidue-PDEC。

```text
signed_sum_residue_gate_group_count=1
all_signed_sum_residue_gates_closed=true
five_term_signed_sum_interval_residue_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. Signed-Sum 摘要

| M | coefficients | selected S | selected carry | selected S mod 2627 | selected sign | combined hits | closed |
| ---: | --- | ---: | ---: | ---: | --- | --- | --- |
| 57684 | `[14421, 19228, 36708, 382536, 12540]` | 373055 | 6 | 21 | `--++-` | `['--++-:26951']` | true |

## 2. Carry 层同余门

| carry | S interval | shifted q4 targets | shifted q2 targets | shifted mod 2627 targets | q4 hits | q2 hits | combined hits |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| -9 | `[-519156,-461472)` | `[6, 7]` | `[38, 46]` | `[117, 969, 1671, 2523]` | `[]` | `[]` | `[]` |
| -8 | `[-461472,-403788)` | `[7, 8]` | `[7, 70]` | `[7, 859, 1561, 2413]` | `[]` | `[]` | `[]` |
| -7 | `[-403788,-346104)` | `[8, 9]` | `[31, 39]` | `[749, 1451, 2303, 2524]` | `[]` | `[]` | `[]` |
| -6 | `[-346104,-288420)` | `[9, 10]` | `[0, 63]` | `[639, 1341, 2193, 2414]` | `[]` | `[]` | `[]` |
| 5 | `[288420,346104)` | `[20, 21]` | `[60, 68]` | `[131, 983, 1204, 2056]` | `[]` | `[]` | `[]` |
| 6 | `[346104,403788)` | `[21, 22]` | `[21, 29]` | `[21, 873, 1094, 1946]` | `['--++-:26951']` | `['--++-:26951']` | `['--++-:26951']` |
| 7 | `[403788,461472)` | `[22, 23]` | `[53, 61]` | `[763, 984, 1836, 2538]` | `[]` | `[]` | `[]` |
| 8 | `[461472,519156)` | `[23, 24]` | `[14, 22]` | `[653, 874, 1726, 2428]` | `[]` | `[]` | `[]` |

## 3. 自足小引理

令

```text
S(sigma)=sum_i sigma_i A_i,  A=[14421,19228,36708,382536,12540].
r=S-cM, 0<=r<M.
```

则 `r mod L` 落在目标类 `T` 等价于

```text
S mod L in T+cM mod L
and cM<=S<(c+1)M.
```

因此 carry-layer 目标纤维完全转化为有限项 signed-sum 的区间同余纤维。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的五项 signed-sum 区间同余门唯一命中 `--++- / S=373055 / r=26951`。
- 未闭合：全局五项 signed-sum 区间同余纤维容量界，或 SumResidue-PDEC 排斥。
- 下一目标：`FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json` | `02ad727819419b59d9967acaff91084c2f0387eb6e6bc96881241e8506ee2ca2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json` | `6f3e6110974e79d39e0a67c305741d1d06b4b21d1c8a1a4910ebaab92e52f9df` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_signed_sum_residue_gate_router.py` | `bc938ff4dcef4483a48e3378a9a7549e68c698bbf98e1a5c8d4ce9611b56ffeb` |
