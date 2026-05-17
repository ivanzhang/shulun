# Prime Matrix cycle-debt low-shell delta skeleton router

**状态：** `k13_low_shell_full_residue_exit_compressed_to_two_extra_lanes`

K=13 的低层 1..3 shell 虽然可出现全部 71 个 residue delta，但精确 MILP 显示它单独只需 6 个 delta 即可匹配。在已有 K=13 刚性核心的 7 个 delta 上，低层只需新增 0 与 66 两条 lane。于是 K=13 survivor 被压成 9-lane、全 101 demand width 的 CRT 载荷，全局 lcm 约为 10^42.095。低层 full-residue 逃逸解释被关闭，剩余是全债务九 lane CRT-load PDEC 或 residual slack-tail SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE
period_p=5680
low_shell_possible_delta_count=71
low_shell_minimum_delta_count=6
low_shell_minimum_delta_witness=[23, 35, 38, 58, 68, 70]
core_delta_count_before_low_shell=7
low_shell_new_delta_count_over_core=2
low_shell_new_deltas_over_core=[0, 66]
full_k13_delta_count_after_low_shell=9
full_k13_total_required_width=101
full_k13_global_lcm_log10=42.095
full_k13_lcm_exceeds_period=true
next_direct_attack_target=K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE
```

## 1. low-shell delta skeleton

| solution | objective | delta count | deltas |
| --- | ---: | ---: | --- |
| low shell alone | 6 | 6 | `[23, 35, 38, 58, 68, 70]` |
| extra over core | 2 | 2 new | `[0, 8, 22, 39, 54, 55, 58, 59, 66]` |

## 2. full K13 lane load

| delta | edges | width | blocker factors | log10 lane lcm |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 2 | 4 | 4 | 4.800 |
| 8 | 4 | 11 | 6 | 7.853 |
| 22 | 4 | 20 | 11 | 15.565 |
| 39 | 4 | 17 | 11 | 17.244 |
| 54 | 2 | 18 | 12 | 17.502 |
| 55 | 2 | 9 | 6 | 6.627 |
| 58 | 2 | 10 | 7 | 8.262 |
| 59 | 4 | 8 | 6 | 6.766 |
| 66 | 3 | 4 | 4 | 3.798 |

## 3. 判定

- `1..3` low shell 的 possible delta 虽为全 `0..70`，但最小匹配骨架只需 6 个 delta。
- 相对 K=13 刚性核心，low shell 只新增 delta `0,66`，总 lane 数变为 9。
- 补齐后 K=13 覆盖全部 `101` demand width，全局 CRT lcm 约 `10^42.095`。
- 因此 low-shell full-residue SAE 被压缩为九 lane 全债务 CRT-load PDEC/SAE 接口。
- 下一主攻点：`K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json` | `b575245854e1f1a72d715a468d40fd484bbb3b4f27f1a90728923966785d412f` |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json` | `13bf0789a9e12152dab8e05644476ca1cd3095af38fcb515d2a65a4ea2bfc745` |
