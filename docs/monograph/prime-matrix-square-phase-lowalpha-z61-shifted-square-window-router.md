# Prime Matrix square-phase low-alpha z=61 shifted square window

**状态：** `z61_shifted_linear_prime_pair_reduced_to_square_window_congruence_open`

同步移位线性素数对继续和短条带端点联立：`N_low=2q_4(q_2s-1)`、`N_high=q_2(2q_4s-1)`，且 `p^2=M*N_low-delta`。样本中 `M=57684`、`delta=527`，`p^2≡-527 (mod 57684)`，并且 `delta+M*span <= p-1 < delta+M*(span+1)`，所以 `s` 被平方窗口公式唯一恢复为 `132`。下一步硬点变为这种平方同余端点窗口的全局容量界，或登记 SquareWindow-PDEC。

```text
shifted_square_window_group_count=1
all_shifted_square_window_groups_closed=true
shifted_square_window_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 平方窗口

| p | M | q2 | q4 | s | N low | N high | span | delta | residue | s recovered | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 200003 | 57684 | 71 | 37 | 132 | 693454 | 693457 | 3 | 527 | 57157 | 132 | true |

## 2. 端点窗口不等式

| delta_high | p-1 | next threshold | low floor | high floor | endpoint span |
| ---: | ---: | ---: | --- | --- | --- |
| 173579 | 200002 | 231263 | true | true | true |

## 3. 自足小引理

设 `M=2B`，端点移位对给出 `a_4=q_2s-1`、`a_2=2q_4s-1`。则归一条带端点为

```text
N_low=2q_4(q_2s-1),
N_high=q_2(2q_4s-1),
N_high-N_low=2q_4-q_2.
```

若 `p^2=M*N_low-delta` 且 `delta+M*(N_high-N_low) <= p-1 < delta+M*(N_high-N_low+1)`，则这两个归一半素数正好跨越 `p^2` 后长度 `p` 的端点窗口。同时 `s=(p^2+delta+2Mq_4)/(2Mq_2q_4)`，所以平方窗口会唯一锁定共同乘子。

## 4. 证明边界

- 已闭合：样本移位线性素数对等价于一个平方同余端点窗口。
- 未闭合：全局平方窗口容量界，或 SquareWindow-PDEC 排斥。
- 下一目标：`ShiftedSquareWindowGlobalBoundOrSquareWindowPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json` | `57d4e18eadd1bb072db598f782533b7ecefc942472cc8f26d9f0a285e97ad40e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_router.py` | `1ac8ee363bcba2b1a9994f9cb798d5974b5f6d531679fe8cd006c84a45921e9b` |
