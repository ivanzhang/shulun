# Prime Matrix square-phase low-alpha prime-u Brun-Titchmarsh 接口

**状态：** `prime_u_branch_closed_by_external_brun_titchmarsh_constant_open_self_contained`

prime-u 分支可由外部 Brun-Titchmarsh 型短区间素数上界支付。对 `D_-=q<sqrt(P)`，区间长度 `H≈P/q`，BT 给 `prime_u(q)<=2H/logH`；相对先前模型 `H/log(P^2/q)` 的符号常数为 `2(2-alpha)/(1-alpha)`，`alpha=log q/log P<1/2` 时不超过 6。因此在接受该外部输入后，prime-u 子分支从开放硬点中剥离；自足版本仍需内联 Brun-Titchmarsh，剩余为 semiprime 单纤维相位上界与 ultra-low 复合尾项。

```text
brun_titchmarsh_external_input_registered=true
prime_u_bt_model_constant_bound_proved_from_external_input=true
prime_u_self_contained_proved=false
semiprime_single_fiber_phase_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局 BT 预算

| q axes | prime actual | model | BT budget | actual/model | actual/BT | BT/model | max symbolic factor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 8298 | 8229.927319 | 43951.639764 | 1.008271 | 0.188798 | 5.340465 | 5.997320 |

## 2. 最热 q 轴

| type | record |
| --- | --- |
| actual/model | `{'q': 263, 'alpha': 0.4916606997995414, 'h': 317.72243346007605, 'u_interval_capacity': 317, 'prime_u_capacity': 26, 'model': 18.54395843659127, 'brun_titchmarsh_budget': 110.09043475543577, 'actual_over_model': 1.4020738931713919, 'actual_over_bt': 0.2361694733766708, 'bt_over_model': 5.9367278637878815, 'symbolic_bt_factor_bound': 5.934380047364663, 'bt_model_constant_6_covers': True}` |
| BT/model | `{'q': 191, 'alpha': 0.49966478519238816, 'h': 192.35078534031413, 'u_interval_capacity': 192, 'prime_u_capacity': 8, 'model': 12.174299108276827, 'brun_titchmarsh_budget': 73.03858069814976, 'actual_over_model': 0.6571220181834628, 'actual_over_bt': 0.10953115358391212, 'bt_over_model': 5.999407444202985, 'symbolic_bt_factor_bound': 5.997320078238021, 'bt_model_constant_6_covers': True}` |

## 3. 每个 P 的总结

| P | quarter rows | prime actual | actual/model | actual/BT | BT/model |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 2 | 168 | 1.017741 | 0.182580 | 5.574207 |
| 36739 | 3 | 798 | 0.983280 | 0.180791 | 5.438760 |
| 83561 | 4 | 2141 | 1.045759 | 0.194630 | 5.373056 |
| 200003 | 4 | 5191 | 0.997124 | 0.187962 | 5.304913 |

## 4. 证明边界

- 外部闭合：接受 Brun-Titchmarsh 后，prime-u 分支有统一模型常数 `6`。
- 未自足：本文作者侧尚未内联 Brun-Titchmarsh 证明。
- 未闭合：semiprime 单 `b` 纤维相位/素性上界。
- 未闭合：ultra-low 复合尾项 Rankin/Selberg 上界或 PDEC 排除。
- 下一目标：`SemiprimeSingleFiberSelbergPhaseBoundAndUltraLowCompositeTailOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json` | `6727d8ab75e183541d62cecb47b31f87dc918e8afd51e6b21cd4736893f3129e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json` | `33dfbaed09353024edee0ccc717a184111e0611f8cb4f4ff49cf802b2f83d526` |
| `experiments/prime_matrix_square_phase_lowalpha_prime_u_brun_titchmarsh_router.py` | `f3a3e9ea9f2ecf75033ed1cda378d69a74fbe569f91611d690ab83ea410e0e82` |
