# Prime Matrix square-phase low-alpha z=61 dyadic same-p strip carry

**状态：** `z61_positive_dyadic_lifts_reduced_to_endpoint_spanning_same_p_strip_open`

两个正 dyadic lift 共用同一个 `p` 后，可归一到同一个 quotient-2 短条带。在样本中该条带只有 `4` 个整数槽，`2q_4a_4` 占最低槽，`q_2a_2` 占最高槽；等价半素数 carry 方程为 `71*9767 - 2*37*9371 = 3`。因此 dyadic 正吸收器进一步压成端点跨越的短条带半素数对问题，下一步证明这种 endpoint-spanning pair 的全局容量界，或登记 EndpointPair-PDEC。

```text
positive_same_p_group_count=1
max_slot_capacity=4
all_positive_same_p_groups_closed=true
all_positive_same_p_groups_endpoint_spanning=true
endpoint_spanning_semiprime_pair_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 同 p 短条带

| p | B | base modulus | slots | capacity | normalized values | span | carry equation | endpoints |
| ---: | ---: | ---: | --- | ---: | --- | ---: | --- | --- |
| 200003 | 28842 | 57684 | `[693454,693457]` | 4 | `[693457, 693454]` | 3 | `71*9767 - 2*37*9371 = 3` | true |

## 2. 源纤维归一化

| quotient | q | a | n=qa | normalized n | delta |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 71 | 9767 | 693457 | 693457 | 173579 |
| 4 | 37 | 9371 | 346727 | 693454 | 527 |

## 3. 自足小引理

设同一 `p,B` 下有 quotient `2` 与 `4` 两条短残基源纤维。令 `n_2=q_2a_2`，`n_4=q_4a_4`。二者归一到同一条带：

```text
p^2 < 2B*n_2 <= p^2+p-1,
p^2 < 2B*(2n_4) <= p^2+p-1.
```

因此 `n_2` 与 `2n_4` 必须落在同一个长度约 `p/(2B)` 的整数槽集合中。样本里该集合只有 4 个槽，二者占据两端，所以正吸收器的存在等价于一个端点跨越半素数对。

## 4. 证明边界

- 已闭合：样本内正 dyadic lift 对被压成同 p 短条带端点跨越半素数 carry 方程。
- 未闭合：全局端点跨越半素数对容量界，或 EndpointPair-PDEC 排斥。
- 下一目标：`EndpointSpanningSemiprimePairGlobalBoundOrEndpointPairPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json` | `ea2150eaee0eb08d7f7a3412b3d35821bac7f1901f2fa37028335cf16c9b5d0f` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_same_p_strip_carry_router.py` | `506548705dbd1070dce2cbca95f3b8dd345794df54772ebea28d33979e70da38` |
