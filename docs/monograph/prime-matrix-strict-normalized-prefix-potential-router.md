# Prime Matrix strict 归一化 prefix 残洞势路由器

**状态：** `normalized_prefix_potential_reduced_to_rough_count_type_threshold_finite_check_open`

`NormalizedPrefixResidualPotentialLowerBound` 已被压成确定的筛余问题：容量纪律给出 M#_{x,z}>=|R_{x,z}|/ceil(P/z)。因此只要在某个非循环 prefix 窗口 z<=P^(1/2-eps) 证明统一粗筛余下界 |R_{x,z}|>=c P/log z，就得到 M#>=c z/log z。剩余是三件事：证明或引用显式低界筛、给出 formal-unit 类型阈值账本、并补有限小 P 证书；之后仍要做标签到类型的抗塌缩。

```text
multiplier_to_rough_count_reduction_closed=true
noncircular_prefix_cutoff_window_identified=true
uniform_prefix_rough_count_lower_bound_proved=false
formal_unit_type_threshold_ledger_proved=false
finite_small_p_boundary_prefix_certificate_proved=false
normalized_prefix_residual_potential_lower_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 势下界公式

容量纪律已给出

```text
M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)},
mu_{tau_z(c)}<=ceil(P/z),
so M#_{x,z}>=|R_{x,z}|/ceil(P/z).
```

若能在 `z<=P^(1/2-eps)` 上用低界筛证明 `|R_{x,z}|>=c_eps P/log z`，则得到

```text
M#_{x,z}>=c_eps z/log z.
```

这条路径绕开了自然 cutoff `z=x` 的短素数屏障，但引入了显式筛常数、类型阈值和有限段证书。

## 2. 压缩表

| reduction | formula | status |
| --- | --- | --- |
| `multiplier_to_rough_count` | M#_{x,z} >= \|R_{x,z}\| / ceil(P/z). | `closed` |
| `classical_sieve_window` | For z<=P^(1/2-eps), a lower-bound sieve would give \|R_{x,z}\| >= c_eps P/log z after finite constants. | `external_or_internal_input_open` |
| `normalized_growth` | Combining the two gives M#_{x,z} >= c_eps z/log z. | `conditional_on_rough_count` |
| `type_threshold_comparison` | Need c_eps z/log z > T_formal(P,z) on the same row-free type alphabet. | `open` |
| `finite_small_p` | Explicit constants leave a finite P range that must be certified separately. | `open` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NormalizedPotentialInputActive` | `true` | `false` | 上一层已把容量乘子纪律后的直接硬点定为 M# 归一化势下界。 | NormalizedPrefixResidualPotentialLowerBound |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍只在早期零行假设下研究 prefix 残洞势，不使用真实缺席数据。 | 保持 row_column_unconditional_closed=false。 |
| `MultiplierToRoughCountReductionClosed` | `true` | `true` | 由 mu_q<=ceil(P/z) 得 M#>=\|R_{x,z}\|/ceil(P/z)，把归一化势压到 prefix 粗筛余数量。 | 需要 \|R_{x,z}\| 下界。 |
| `NoncircularCutoffWindowIdentified` | `true` | `true` | 若取 z<=P^(1/2-eps)，筛的 level 可保持在窗口长度 P 内，避免自然 cutoff x~P 的短素数屏障。 | 需要显式低界筛常数或内部化证明。 |
| `UniformPrefixRoughCountCurrentCorpusProved` | `false` | `false` | 当前语料尚未逐行证明 \|R_{x,z}\|>=c P/log z；这可作为经典低界筛外部输入或内部化目标。 | UniformPrefixRoughCountLowerBound |
| `FormalUnitTypeThresholdLedgerCurrentCorpusProved` | `false` | `false` | 尚未给出同一 row-free type alphabet 的阈值 T_formal(P,z)，所以还不能比较 M# 与类型数。 | FormalUnitTypeThresholdLedger |
| `FiniteSmallPBoundaryPrefixCurrentCorpusProved` | `false` | `false` | 即使采用显式筛常数，也会留下有限小 P 段；该证书尚未物化。 | FiniteSmallPBoundaryPrefixCertificate |
| `NormalizedPrefixPotentialCurrentCorpusProved` | `false` | `false` | M# 势的内部公式已闭合，但全局下界、阈值比较和有限段证书仍未完成。 | UniformPrefixRoughCountLowerBound AND FormalUnitTypeThresholdLedger AND FiniteSmallPBoundaryPrefixCertificate |
| `StillNeedsAntiCollapseAfterPotential` | `false` | `false` | 即便 M# 足够大，仍需证明不同标签支撑不在 row-free type/quotient 中塌缩。 | PrefixLabelSupportToRowFreeTypeAntiCollapse |

## 4. 下一最窄点

```text
UniformPrefixRoughCountLowerBound
```

并行保留：

```text
FormalUnitTypeThresholdLedger AND FiniteSmallPBoundaryPrefixCertificate AND PrefixLabelSupportToRowFreeTypeAntiCollapse
```

审稿边界：本步只把 M# 势压成显式筛余下界与阈值比较；尚未提供低界筛证明或有限段证书。
