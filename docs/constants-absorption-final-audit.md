# 常数吸收最终核对表

本表核对 `docs/explicit-p0-constants.structured-conservative.json` 中的保守常数如何吸收 A/B、C、D 与 EXT 定理包中的损失。机器抽取证书见 `docs/explicit-p0-structured-conservative-result.json`。

## 1. 主阈值口径

- 理论阈值证书：`log_P0_upper=3.5`。
- 有限验证证书：`P<=floor(exp(5))=148` 全部通过。
- 因为 `exp(3.5)<exp(5)`，理论段与有限验证段重叠覆盖全部奇素数。

## 2. Tail-log4 吸收

| 项 | 常数 | 需求 | 余量 |
| --- | ---: | ---: | ---: |
| `tail_error_power` | 4 | `>A_star=2` | 2 |
| `K_sieve_log_saving` | 128 | RKS 总损失 `<=74` | `>=54` |
| `C_vaughan_blocks` | 10 | 固定分块损失 | 已计入 74 |
| `C_rect_variation` | 10 | 矩形变差损失 | 已计入 74 |
| `C_divisor_coeff` | 10 | 除数系数损失 | 已计入 74 |

结论：Tail-log4 的 `P/log^4P` 尾误差强于主链只需的 `P/log^2P` 级吸收；RKS 对数节省账本仍有至少 54 个对数幂余量。

## 3. D 组结构吸收

| 项 | 常数 | 用途 | 核对 |
| --- | ---: | --- | --- |
| `C_OMR_layer` | 16 | 层蛋糕/阈值层损失 | 被 `A_OMR_log=8` 覆盖 |
| `C_OMR_model` | 16 | 一阶圆周模型常数 | 只影响绝对常数 |
| `C_OMR_projection` | 16 | 投影增量选择损失 | 被 `A_OMR_log=8` 覆盖 |
| `C_CGTP` | 16 | martingale 能量账本 | 被 `A_CGTP_log=8` 与 `epsilon_OMR_power=64` 覆盖 |
| `C_LSMP` | 16 | 小质量 packing/coarea | 被 `A_LSMP_log=8` 覆盖 |
| `C_collision_span` | 16 | FCT span 计数 | 被 `A_collision_span_log=8` 覆盖 |

D 组显式对数指数合计按最终主链采用保守值

`A_OMR_log + A_CGTP_log + A_LSMP_log + A_collision_span_log = 32 < K_sieve_log_saving=128`。

因此 D 组结构损失不会吃尽 Tail-log4/RKS 的主对数余量。

## 4. Weil/完成法吸收

| 项 | 常数 | 用途 |
| --- | ---: | --- |
| `C_weil_completion` | 11664 | 完成法、Kloosterman 完整和、短侧 Weil 吸收的绝对常数包 |
| `A_weil_completion_log` | 4 | 不完全和完成法 `logP` 损失 |

`A_weil_completion_log=4` 已小于 RKS 余量 54，也小于结构总余量 128 的安全预算。绝对常数只影响抽取器中的阈值位置，不改变对数幂不等式方向。

## 5. 小 `logP` 直接证书区

- `use_direct_c_zone_certificate=true`。
- `C_zone_direct_logP=5`。

该开关表示 `logP<=5` 由有限验证证书覆盖；理论抽取给 `logP>3.5`，所以两段存在重叠区 `[3.5,5]`，无缝覆盖。

## 6. 机器复核命令

最终审稿包应保留以下命令作为可复现实验：

`python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --max-log 100 --step 0.1`

期望输出：`log_P0_upper=3.5`。

`python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json`

期望输出：`ok=true`，`odd_prime_count=33`。

## 7. 常数结论

在 `EXT-*` 外部定理按引用表成立、A/B/C/D 附录接口采用当前常数包时，所有对数损失均被 `K_sieve_log_saving=128` 和 `epsilon_OMR_power=64` 保守吸收；抽取器复现 `log_P0_upper=3.5`，有限验证覆盖到 `exp(5)`，因此常数层面闭合。
