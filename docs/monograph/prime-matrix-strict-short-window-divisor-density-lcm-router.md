# Prime Matrix strict 短窗口除数密度 LCM 乘子纪律路由器

**状态：** `short_window_divisor_density_reduced_to_lcm_multiplier_or_common_kernel_defect_open`

短窗口高密度除数已经进一步压成 LCM 乘子纪律。若 A={g: Y<g<=2Y, g|h} 且 |A|>=eta Y，则 L(A) 必整除同一正式频率 h。按任意顺序加入 g_t，新增乘子 mu_t=L_t/L_{t-1}=g_t/gcd(g_t,L_{t-1})。若 L(A)<=H，则 mu_t>=Lambda 的次数至多为 log H/log Lambda；剩余大量 g_t 必满足 gcd(g_t,L_{t-1})>Y/Lambda，即出现大共同核复现。因此当前硬点不再是裸除数函数估计，而是二选一：LCM 爆炸超过频率高度，或共同核复现进入 ColumnCRT/PDEC/SAE。

```text
short_window_density_materialized=true
short_window_antichain_closed=true
lcm_anchor_closed=true
incremental_multiplier_discipline_closed=true
high_multiplier_count_bound_closed=true
low_multiplier_kernel_forcing_closed=true
low_multiplier_kernel_route_registered=true
dense_lcm_after_kernel_compression_proved=false
formal_frequency_height_ceiling_matched=false
low_multiplier_common_kernel_excluded=false
short_window_divisor_density_envelope_proved=false
hot_density_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 乘子纪律

设

```text
A=A(h;Y)={g: Y<g<=2Y, g|h},  N=|A|.
```

若上一层热窗口给出 `N>=eta Y`，则所有 `g in A` 同时整除频率 `h`，因此

```text
L(A)=lcm(A) | h.
```

任选顺序 `g_1,...,g_N`，记 `L_t=lcm(g_1,...,g_t)`，则

```text
mu_t=L_t/L_{t-1}=g_t/gcd(g_t,L_{t-1}),
product_t mu_t=L(A).
```

若正式频率有高度上界 `|h|<=H`，则 `L(A)<=H`，于是对任意 `Lambda>1`：

```text
#{t: mu_t>=Lambda} <= floor(log H/log Lambda).
```

所以当 `N` 远大于该独立乘子预算时，大部分 `g_t` 必须满足

```text
gcd(g_t,L_{t-1}) > Y/Lambda.
```

这就是新的窄口：热除数密度若不能产生 LCM 爆炸，就必须产生大共同核复现。

## 2. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `short_window_antichain` | If Y<g<g'<=2Y, then g does not divide g'. | `closed` | 同一短乘法窗口中的不同除数互不整除，不能靠简单倍数链解释高密度。 |
| `lcm_anchor_divides_frequency` | For A={g: Y<g<=2Y and g\|h}, L(A)=lcm(A) divides h. | `closed` | 热除数窗口被锚定在单个频率 h 上，LCM 不能脱离频率高度预算。 |
| `incremental_multiplier_identity` | L_t/L_{t-1}=g_t/gcd(g_t,L_{t-1}), and product_t L_t/L_{t-1}=L(A). | `closed` | 每加入一个新除数，要么贡献新 LCM 乘子，要么与旧 LCM 有大共同核。 |
| `high_multiplier_count_bound` | If L(A)<=H, then #{t: mu_t>=Lambda} <= floor(log H/log Lambda). | `closed` | 频率高度上界直接限制独立新乘子数量。 |
| `low_multiplier_kernel_forcing` | If mu_t<Lambda, then gcd(g_t,L_{t-1})>Y/Lambda. | `closed` | 不能造成 LCM 爆炸的除数必须与既有除数云共享大共同核。 |
| `density_to_multiplier_pressure` | N_h(Y,2Y]>=eta Y forces either many high multipliers or many low-multiplier kernel recurrences. | `closed_dichotomy` | 短窗口线性密度不再是裸 tau 问题，而被拆成 LCM 爆炸或共同核复现。 |
| `kernel_recurrence_to_registered_defect` | Persistent low-multiplier kernel recurrences must route to ColumnCRT/PDEC; isolated ones route to SAE. | `registered_route_open` | 共同核复现已命名为下一个出口，但尚未完成排斥。 |
| `dense_lcm_after_kernel_compression` | After excluding low-multiplier kernel recurrences, dense A should force log L(A)>=c(eta,Lambda)Y. | `open_input` | 这是剩余的确定性 LCM 下界输入，不能由普通 tau(h) 粗估计替代。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链产生的低有效模/端点缺陷链条内。 | 保持 row_column_unconditional_closed=false。 |
| `ShortWindowDensityMaterialized` | `true` | `true` | 上一层已把倒数封套失败物化为 N_h(Y,2Y]>=eta Y。 | ShortWindowLCMMultiplierDisciplineForFrequencyH |
| `LCMAnchorClosed` | `true` | `true` | 该窗口全部除数的 LCM 必整除同一个正式频率 h。 | FormalFrequencyHeightCeilingForEndpointPDEC |
| `IncrementalMultiplierDisciplineClosed` | `true` | `true` | 高独立乘子数量受 log H/log Lambda 限制；其余强制大共同核。 | LowMultiplierCommonKernelColumnCRTOrPDECRoute |
| `LowMultiplierKernelRouteRegistered` | `true` | `false` | 大共同核复现应形成低商 ColumnCRT/PDEC 或孤立 SAE，但排斥未完成。 | LowMultiplierCommonKernelColumnCRTOrPDECRoute AND HotFrequencyDivisorDensityPDECorSAE |
| `DenseLCMAfterKernelCompressionProved` | `false` | `false` | 尚未证明排除共同核出口后，任意热窗口必须产生超过频率高度的 LCM 爆炸。 | DenseShortWindowLCMLowerBoundAfterKernelCompression AND FormalFrequencyHeightCeilingForEndpointPDEC |
| `ShortWindowDivisorDensityEnvelopeCurrentCorpusProved` | `false` | `false` | 尚未完成正式频率族的短窗口除数密度上界与 PDEC 下界比较。 | DenseShortWindowLCMLowerBoundAfterKernelCompression AND LowMultiplierCommonKernelColumnCRTOrPDECRoute AND WeightedPositiveEndpointPDECLowerBoundComparison |

## 4. 下一步最窄点

当前最窄点改为：

```text
LowMultiplierCommonKernelColumnCRTOrPDECRoute
```

含义：证明大量低乘子共同核复现不能在早期零行反例链中持续存在；若持续存在，必须形成低商 `ColumnCRT/PDEC`；若只孤立出现，则进入 `SAE` 并由容量账本吸收。

备用同等硬点：

```text
DenseShortWindowLCMLowerBoundAfterKernelCompression
```

并行保留：

```text
FormalFrequencyHeightCeilingForEndpointPDEC AND HotFrequencyDivisorDensityPDECorSAE AND WeightedPositiveEndpointPDECLowerBoundComparison
```

审稿边界：本步闭合的是 LCM 乘子纪律和共同核强迫，不闭合共同核排斥，也不宣称行/列命题无条件闭合。
