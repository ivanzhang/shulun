# Prime Matrix square-phase low-alpha z=61 terminal sign forcing

**状态：** `z61_dominant_peel_reduced_to_terminal_sign_forcing_open`

dominant peel 后的三项终端门也可完全剥离：`14421` 正号分支有区间候选但无同余命中，负号分支保留；`19228` 正号分支区间空，负号分支保留；最后 `12540` 只有负号同时满足区间和同余。因此当前 formal unit 的终端三项被强制为 `---`，与上游 `382536,36708` 的正号合成剥离坐标 `++---`。

```text
terminal_sign_forcing_group_count=1
all_terminal_sign_forcings_closed=true
terminal_sign_forcing_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 终端摘要

| M | coefficients | interval | targets | forced terminal sign | full peel-order sign | closed |
| ---: | --- | --- | --- | --- | --- | --- |
| 57684 | `[14421, 19228, 12540]` | `[-73140,-15456)` | `[395, 1097, 1949, 2170]` | `---` | `++---` | true |

## 2. 剥离 14421

| sign | rest interval | rest targets | interval candidates | target candidates | hits |
| --- | --- | --- | ---: | ---: | --- |
| `+` | `[-87561,-29877)` | `[663, 884, 1736, 2438]` | 1 | 0 | `[]` |
| `-` | `[-58719,-1035)` | `[608, 829, 1681, 2383]` | 2 | 1 | `[{'sign_word': '--', 'signed_sum': -31768, 'sum_mod': 2383, 'in_interval': True, 'target_hit': True, 'full_hit': True}]` |

## 3. 剥离 19228

| sign | rest interval | rest targets | interval candidates | target candidates | hits |
| --- | --- | --- | ---: | ---: | --- |
| `+` | `[-77947,-20263)` | `[842, 1544, 2396, 2617]` | 0 | 0 | `[]` |
| `-` | `[-39491,18193)` | `[595, 1447, 1668, 2520]` | 2 | 1 | `[{'sign_word': '-', 'signed_sum': -12540, 'sum_mod': 595, 'in_interval': True, 'target_hit': True, 'full_hit': True}]` |

## 4. 最后一项 12540

| sign | signed sum | mod 2627 | in interval | target hit | full hit |
| --- | ---: | ---: | --- | --- | --- |
| `+` | 12540 | 2032 | true | false | false |
| `-` | -12540 | 595 | true | true | true |

## 5. 自足小引理

终端三项仍使用同一个剥离恒等式：固定首项符号后，区间和目标同余同时平移。
若某分支没有区间候选，则为 interval-empty；若有区间候选但没有目标命中，则为 residue-empty。当前终端唯一幸存路径是

```text
14421 -> -, 19228 -> -, 12540 -> -.
```

## 6. 证明边界

- 已闭合：当前 z=61 formal unit 的终端三项符号被区间和同余共同强制为全负。
- 未闭合：全局终端符号强制机制，或 Terminal-PDEC 排斥。
- 下一目标：`TerminalSignForcingGlobalBoundOrTerminalPDEC`。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json` | `bd408eb36e3b1a42cb0b24c07eff5dcbbc55684c54633cc1cb2ee90eb8952756` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_terminal_sign_forcing_router.py` | `52c49cae67d3c0127d37ddd252abf975406c38c1056f45d10db0baafcfaf0f5a` |
