# Prime Matrix strict 低乘子共同核分流路由器

**状态：** `low_multiplier_common_kernel_split_to_pair_difference_lock_or_fanin_defect_open`

低乘子共同核已经拆成两个不可再混淆的出口。若新增除数 g_t 的乘子 mu_t<Lambda，则 K_t=gcd(g_t,L_{t-1})>Y/Lambda。由于 L_{t-1} 由旧除数生成，K_t 必被成对共同核 gcd(g_t,g_i) 的 LCM 覆盖。于是只有两种结构：某个旧除数与 g_t 有大成对共同核，进而锁定短差值 g_t-g_i=k a；或没有单一大核，只能由多个旧除数分摊覆盖，形成多源 kernel fan-in。前者应进入低商 ColumnCRT/PDEC，后者进入 SAE/PDEC 容量账本。

```text
low_multiplier_kernel_imported=true
kernel_subcover_closed=true
pair_or_fanin_dichotomy_closed=true
large_pair_difference_lock_closed=true
large_pair_columncrt_route_registered=true
fanin_sae_pdec_route_registered=true
large_pair_columncrt_excluded=false
fanin_sae_or_pdec_excluded=false
low_multiplier_common_kernel_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 成对核覆盖

从上一层导入低乘子事件：

```text
K_t=gcd(g_t,L_{t-1}) > Y/Lambda.
```

因为 `L_{t-1}=lcm(g_1,...,g_{t-1})`，所以 `K_t` 的每个素幂都来自某个旧 `g_i`，即

```text
K_t | lcm_{i<t} gcd(g_t,g_i).
```

于是大共同核不是模糊对象：它要么集中在某个成对 gcd 上，要么由多个旧除数分摊覆盖。

## 2. 差值锁

若存在 `k=gcd(g_t,g_i)` 足够大，则因二者都在 `(Y,2Y]` 内，

```text
k | (g_t-g_i),  0<|g_t-g_i|<Y.
```

所以

```text
g_t-g_i=k a,  0<|a|<Y/k.
```

当 `k` 大时，商 `a` 很小；若这种锁定持久出现，就不是随机除数密度，而是低商列相位集中，应送入 `ColumnCRT/PDEC`。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `low_multiplier_kernel_materialization` | mu_t<Lambda implies K_t=gcd(g_t,L_{t-1})>Y/Lambda. | `imported_closed` | 由 LCM 乘子纪律继承大共同核。 |
| `kernel_subcover` | K_t divides lcm_{i<t} gcd(g_t,g_i). | `closed` | 新除数与旧 LCM 的共同核完全由它和旧除数的成对共同核覆盖。 |
| `pair_or_fanin_dichotomy` | A large K_t gives either a large pair gcd or a multi-source kernel fan-in cover. | `closed_dichotomy` | 低乘子复现被拆成单对大核与多源扇入两类，不再是无名异常。 |
| `large_pair_difference_lock` | If k\|g_t and k\|g_i with Y<g_i,g_t<=2Y, then k\|(g_t-g_i) and 0<\|g_t-g_i\|<Y. | `closed` | 单对大共同核会把短窗口差值锁到小商倍数。 |
| `large_pair_to_low_quotient_columncrt` | A persistent large-pair kernel with \|g_t-g_i\|=k a and \|a\|<Y/k enters LowQuotient ColumnCRT/PDEC. | `registered_route_open` | 若这种差值锁反复出现，它就是低商相位集中证书。 |
| `fanin_to_sae_or_pdec` | If K_t needs many previous divisors to cover, the minimal cover hypergraph is SAE unless it persists as PDEC. | `registered_route_open` | 多源扇入是可登记的结构异常，但排斥仍待证明。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的热除数窗口分支内。 | 保持 row_column_unconditional_closed=false。 |
| `LowMultiplierKernelImported` | `true` | `true` | 从 LCM 乘子纪律导入 K_t>Y/Lambda。 | LowMultiplierCommonKernelColumnCRTOrPDECRoute |
| `KernelSubcoverClosed` | `true` | `true` | 大共同核必须由成对 gcd 云覆盖。 | 无。 |
| `PairOrFanInDichotomyClosed` | `true` | `true` | 共同核出口已拆成大成对差值锁与多源扇入两类。 | LargePairKernelDifferenceColumnCRTExclusion OR MultiSourceKernelFanInSAEOrPDECExclusion |
| `LargePairDifferenceLockClosed` | `true` | `true` | 大成对共同核强制差值为共同核的小商倍数。 | LowQuotientColumnCRTOrPDECRoute |
| `LargePairColumnCRTExcluded` | `false` | `false` | 尚未证明持久差值锁不可能，或其 PDEC/ColumnCRT 证书必被排斥。 | LargePairKernelDifferenceColumnCRTExclusion |
| `FanInSAEOrPDECExcluded` | `false` | `false` | 尚未证明多源共同核扇入可全局求和吸收，或持久时被 PDEC 排斥。 | MultiSourceKernelFanInSAEOrPDECExclusion |

## 5. 下一步最窄点

```text
LargePairKernelDifferenceColumnCRTExclusion
```

备用并列硬点：

```text
MultiSourceKernelFanInSAEOrPDECExclusion
```

并行保留：

```text
LowQuotientColumnCRTOrPDECRoute AND HotFrequencyDivisorDensityPDECorSAE AND ShortWindowLCMMultiplierDisciplineForFrequencyH
```

审稿边界：本步只证明共同核可分流为成对差值锁或多源扇入；尚未排斥这两个出口。
