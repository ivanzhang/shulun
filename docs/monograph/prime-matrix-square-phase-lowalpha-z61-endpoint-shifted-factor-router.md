# Prime Matrix square-phase low-alpha z=61 endpoint shifted factor

**状态：** `z61_endpoint_spanning_pair_reduced_to_shifted_linear_prime_pair_open`

端点半素数 carry 对继续压缩：样本中 carry `3` 等于 `2q_4-q_2`，因此 `q_2a_2-2q_4a_4=3` 等价变形为 `q_2(a_2+1)=2q_4(a_4+1)`。由于 `gcd(q_2,2q_4)=1`，得到共同乘子 `s=132`，即 `a_4=71s-1`、`a_2=74s-1`。下一步的全局硬点进一步收窄为移位线性素数对容量界，或登记 ShiftedFactor-PDEC。

```text
endpoint_shifted_factor_group_count=1
all_endpoint_shifted_factor_groups_closed=true
shifted_linear_prime_pair_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 移位因子恒等式

| p | q2 | a2 | q4 | a4 | carry | 2q4-q2 | shifted identity | s | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| 200003 | 71 | 9767 | 37 | 9371 | 3 | 3 | `693528=693528` | 132 | true |

## 2. 线性素数型

| s | a4 form | a2 form | coprime(q2,2q4) |
| ---: | --- | --- | --- |
| 132 | `71*132-1` | `74*132-1` | true |

## 3. 自足小引理

若 endpoint carry 方程 `q_2a_2-2q_4a_4=c` 同时满足 `c=2q_4-q_2`，则有 `q_2(a_2+1)=2q_4(a_4+1)`。若再有 `gcd(q_2,2q_4)=1`，则存在整数 `s` 使得 `a_4=q_2s-1` 且 `a_2=2q_4s-1`。因此端点跨越半素数对被压成两个同步移位线性素数型。

## 4. 证明边界

- 已闭合：样本 endpoint pair 等价于 `s=132` 的同步移位线性素数对。
- 未闭合：全局移位线性素数对容量界，或 ShiftedFactor-PDEC 排斥。
- 下一目标：`ShiftedLinearPrimePairGlobalBoundOrShiftedFactorPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json` | `4d8a9ef2c35d9dc7d1b53d6736f8ae2ad53df2a6f41206e6f368a75d1da861b0` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_endpoint_shifted_factor_router.py` | `2f91e1c62bac4857f746cb8615ea78476e4b4c67da3decb4a9fb44618224f71b` |
