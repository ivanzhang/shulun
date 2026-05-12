# Prime Matrix strict 固定商型 ColumnCRT/PDEC 路由器

**状态：** `fixed_quotient_type_reduced_to_scaled_core_descent_or_pdec_open`

固定商型出口已经从相位口号压成精确缩频递归。令 c=b+a。由于 gcd(b,c)=1，若 g=kb 与 g'=kc 都整除 h，则 lcm(g,g')=kbc 也整除 h；反过来 kbc|h 即给出同商型 pair。因此同一商型复现等价于核心 k 整除 h/(bc)。又因为合法商型有 bc>=2，所以每次固定商型递归都会把频率高度至少折半，不能形成无限循环。剩余缺口是：证明 pair 到 core 的密度/权重传递无损，或排斥跨 formal unit 的固定商型 ColumnCRT/PDEC 证书。

```text
fixed_type_scaled_frequency_identity_closed=true
core_interval_bounds_closed=true
strict_height_descent_closed=true
finite_descent_depth_closed=true
single_unit_density_to_scaled_core_closed=true
fixed_type_pdec_route_registered=true
density_transfer_without_loss_proved=false
fixed_type_pdec_excluded=false
fixed_quotient_type_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 精确缩频

固定商型 `(b,a)`，记 `c=b+a`。上一层已经保证

```text
g=kb,  g'=kc,  gcd(b,c)=1.
```

于是

```text
g|h and g'|h  <=>  lcm(g,g')=kbc | h  <=>  k | h/(bc).
```

而原短窗口 `Y<g,g'<=2Y` 给出

```text
Y/max(b,c) < k <= 2Y/min(b,c).
```

所以固定商型复现就是缩频 `h/(bc)` 的短窗口核心除数问题。

## 2. 递归不能绕圈

合法固定商型有 `b,c>=1` 且 `b!=c`，因此 `bc>=2`。每次进入同类缩频递归都满足

```text
|h/(bc)| <= |h|/2.
```

故固定商型链最长为 `floor(log_2 |h|)`。这闭合了循环风险，但不自动闭合密度传递和 PDEC 排斥。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `fixed_type_scaled_frequency_identity` | For c=b+a and gcd(b,c)=1, g=kb and g'=kc both divide h iff kbc divides h. | `closed` | 固定商型复现精确等价于核心 k 整除缩频 h/(bc)。 |
| `core_interval_bounds` | Y/max(b,c)<k<=2Y/min(b,c). | `closed` | 原短窗口中的成对除数复现转成核心 k 的有界乘法窗口。 |
| `strict_height_descent` | bc>=2, hence \|h/(bc)\|<=\|h\|/2 for every legal fixed quotient type. | `closed` | 固定商型递归不能无限原地循环；每次都至少折半频率高度。 |
| `finite_descent_depth` | Any chain of fixed quotient descents has length <= floor(log_2 \|h\|). | `closed` | 若一直不触发 PDEC/SAE，递归链也必须在有限深度终止。 |
| `persistence_to_fixed_pdec` | Persistent same (b,c) core intervals across formal units define a fixed quotient-type ColumnCRT/PDEC certificate. | `registered_route_open` | 跨 formal unit 的同型复现是命名坏窗，不可当作自由误差。 |
| `single_unit_density_to_scaled_core` | Many same-type pairs inside one formal unit give a short-window divisor-density packet for h/(bc). | `closed_reduction` | 单 formal unit 内的同型复现变成缩频核心除数密度问题。 |
| `density_transfer_without_loss` | The number and weight loss from pairs (g,g') to cores k must be bounded uniformly through descent. | `open_input` | 要闭合固定商型出口，还需证明密度阈值不会在递归中被稀释到不可用。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的固定商型大核分支内。 | 保持 row_column_unconditional_closed=false。 |
| `FixedTypeScaledFrequencyIdentityClosed` | `true` | `true` | 固定 `(b,c)` 的每个复现等价于 `k\|h/(bc)`。 | ScaledCoreDivisorDensityDescentOrFixedTypePDEC |
| `CoreIntervalBoundsClosed` | `true` | `true` | 核心 `k` 落在由 `(b,c)` 决定的有界乘法窗口中。 | 无。 |
| `StrictHeightDescentClosed` | `true` | `true` | `bc>=2`，固定商型递归每步至少折半频率高度。 | 无无限循环。 |
| `FixedTypePDECRouteRegistered` | `true` | `false` | 跨 formal unit 的同型核心窗口复现应进入固定商型 ColumnCRT/PDEC。 | FixedQuotientTypePDECColumnCertificateExclusion |
| `DensityTransferWithoutLossProved` | `false` | `false` | 尚未证明成对复现到核心窗口的密度阈值在递归中保持足够强。 | FixedQuotientDensityTransferWithoutLoss |
| `FixedQuotientTypeExcluded` | `false` | `false` | 尚未排斥固定商型 PDEC，也未闭合缩频核心密度递归的无损传递。 | FixedQuotientTypePDECColumnCertificateExclusion AND FixedQuotientDensityTransferWithoutLoss |

## 5. 下一步最窄点

```text
FixedQuotientDensityTransferWithoutLoss
```

并列需要补齐：

```text
FixedQuotientTypePDECColumnCertificateExclusion
```

并行保留：

```text
BoundedQuotientTypeSAEAbsorption AND MultiSourceKernelFanInSAEOrPDECExclusion
```

审稿边界：本步只闭合固定商型的缩频恒等式与有限下降；未闭合密度无损传递，也未排斥固定商型 PDEC。
