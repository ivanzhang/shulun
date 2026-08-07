# MFAC 半素数三项 dispatch 审计

**状态：** `global_semiprime_triad_reconstructed_actual_dispatch_open`
**核验日期：** `2026-08-07`

```text
global_triad_reconstructed=true
actual_dispatch_present=false
canonical_zero_sum_collapse=false
earliest_missing_field=origin_selector
next_positive_gate=OffDiagonalSemiprimeTriadActualDispatchBeforePushforward
mathematical_nonexistence_proved=false
rh_proved=false
row_column_unconditional_closed=false
```

当前语料未提交从半素数三项 global payload 到 actual primitive row 的前向 dispatch。
当前 triad 缺少 `row_key`，因此不能把未分派的零和 payload 误报为 canonical collapse。
这不表示数学上不可能存在 dispatch，也不证明 signed transport、`ψ` 平滑误差、零点排除、行/列命题或 RH。

## 三项

| divisor | cofactor | global payload | missing fields |
| ---: | ---: | ---: | --- |
| 2 | 3 | 0.69314718056 | `pre_cauchy, independent_of_downstream, origin_selector, actual_emitter_registered, row_key, orientation, local_factor, prepushforward_identity` |
| 3 | 2 | 1.09861228867 | `pre_cauchy, independent_of_downstream, origin_selector, actual_emitter_registered, row_key, orientation, local_factor, prepushforward_identity` |
| 6 | 1 | -1.79175946923 | `pre_cauchy, independent_of_downstream, origin_selector, actual_emitter_registered, row_key, orientation, local_factor, prepushforward_identity` |

## 正向门

必须在 pre-Cauchy 层为三项提交 actual record、row dispatch、orientation、local factor 与 prepushforward identity；仅有 D/E global transport 不能替代该门。
