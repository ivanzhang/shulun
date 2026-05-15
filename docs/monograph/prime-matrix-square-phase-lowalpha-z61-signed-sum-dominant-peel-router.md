# Prime Matrix square-phase low-alpha z=61 signed-sum dominant peel

**状态：** `z61_five_term_signed_sum_reduced_to_dominant_peel_open`

五项 signed-sum 门可按主系数剥离：先剥离 `382536`，负号分支被区间直接排除，正号分支把问题降到四项和 `[-36432,21252)` 与模 `2627` 目标 `[325,1027,1879,2100]`。再剥离 `36708`，负号分支无同余命中，正号分支降到三项全负 `---`，和为 `-46189`。合并得到唯一全符号 `++---` 在剥离坐标中，对应原坐标 `--++-` 与 `r=26951`。

```text
dominant_peel_group_count=1
all_dominant_peels_closed=true
dominant_peel_signed_sum_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 剥离摘要

| M | source coefficients | source interval | source targets | dominant | second | terminal coefficients | terminal hits | closed |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |
| 57684 | `[14421, 19228, 36708, 382536, 12540]` | `[346104,403788)` | `[21, 873, 1094, 1946]` | 382536 | 36708 | `[14421, 19228, 12540]` | `[{'sign_word': '---', 'signed_sum': -46189, 'sum_mod': 1097}]` | true |

## 2. 主系数分支

| peeled | sign | rest interval | rest targets | interval candidates | hits |
| ---: | --- | --- | --- | ---: | --- |
| 382536 | `+` | `[-36432,21252)` | `[325, 1027, 1879, 2100]` | 7 | `[{'sign_word': '--+-', 'signed_sum': -9481, 'sum_mod': 1027}]` |
| 382536 | `-` | `[728640,786324)` | `[88, 940, 1642, 2494]` | 0 | `[]` |

## 3. 第二系数分支

| peeled | sign | rest interval | rest targets | interval candidates | hits |
| ---: | --- | --- | --- | ---: | --- |
| 36708 | `+` | `[-73140,-15456)` | `[395, 1097, 1949, 2170]` | 3 | `[{'sign_word': '---', 'signed_sum': -46189, 'sum_mod': 1097}]` |
| 36708 | `-` | `[276,57960)` | `[255, 957, 1809, 2030]` | 4 | `[]` |

## 4. 自足小引理

若 `S=epsilon A+U` 且目标为 `I=[L,H)` 与 `S mod Q in T`，则固定 `epsilon` 后等价于

```text
U in [L-epsilon*A, H-epsilon*A),
U mod Q in T-epsilon*A.
```

因此可逐个剥离主系数，并把不可能分支登记为区间空分支或同余空分支。

## 5. 证明边界

- 已闭合：当前 z=61 formal unit 的五项 signed-sum 门经两次主系数剥离后只剩三项全负终端命中。
- 未闭合：把这种主系数剥离机制提升为全局 signed-sum 容量界，或排斥 Peel-PDEC。
- 下一目标：`DominantPeelSignedSumGlobalBoundOrPeelPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json` | `000bb6e26dec4b78c4215118876df470f40659f120db560c9bee5cf6a80fd0c7` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_signed_sum_dominant_peel_router.py` | `83ec936e19a52179c43a701e75d9aaafd62cb20e1301f5486325b753b2c7b8c0` |
