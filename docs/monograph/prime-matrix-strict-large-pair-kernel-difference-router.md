# Prime Matrix strict 大成对共同核差值锁路由器

**状态：** `large_pair_kernel_difference_reduced_to_finite_quotient_type_pdec_or_sae_open`

大成对共同核差值锁进一步压成有限商字母表。对一对短窗口除数 g,g'，取精确核 k=gcd(g,g')，写 g=kb、g'=k(b+a)，则 gcd(b,b+a)=1。若该核属于低乘子分支的阈值 k>Y/Lambda，因为 g,g' 都在 (Y,2Y]，必有 1<=b,b+a<2Lambda 且 0<|a|<Lambda。故所有这类异常只落在 O(Lambda^2) 个商型 (b,a) 中。持久同型复现应形成固定商型 ColumnCRT/PDEC；非持久同型则进入有限字母表 SAE 容量账本。

```text
exact_pair_gcd_normal_form_closed=true
bounded_quotient_gap_closed=true
finite_quotient_alphabet_closed=true
fixed_type_pdec_route_registered=true
bounded_type_sae_route_registered=true
fixed_type_pdec_excluded=false
bounded_type_sae_absorbed=false
large_pair_kernel_difference_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 有限商字母表

对大成对核事件，取精确共同核

```text
k=gcd(g,g'),  g=kb,  g'=k(b+a),  gcd(b,b+a)=1.
```

若 `k>Y/Lambda` 且 `Y<g,g'<=2Y`，则

```text
1<=b,b+a<2Lambda,  0<|a|<Lambda.
```

因此所有商型 `(b,a)` 至多为 `O(Lambda^2)` 个。这个压缩是结构性的：它不依赖真实样本缺席，也不使用统计逼近。

## 2. 出口

同一 `(b,a)` 反复出现时，变量只剩共同核 `k` 的相位移动，形成固定商型 `ColumnCRT/PDEC`。若所有 `(b,a)` 都不持久，则有限字母表给出可求和的 `SAE` 账本入口。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `exact_pair_gcd_normal_form` | For k=gcd(g,g'), write g=kb, g'=k(b+a), with gcd(b,b+a)=1. | `closed` | 成对共同核可规范化为精确核乘互素商对。 |
| `bounded_quotient_gap` | If Y<g,g'<=2Y and k>Y/Lambda, then 1<=b,b+a<2Lambda and 0<\|a\|<Lambda. | `closed` | 大核差值锁把商变量压进有限字母表。 |
| `finite_quotient_alphabet` | #{(b,a): 1<=b,b+a<2Lambda, a!=0, gcd(b,b+a)=1} <= 8 Lambda^2. | `closed` | 大成对核异常不能产生无限新类型，只能在 O(Lambda^2) 个商型中移动。 |
| `fixed_type_persistence_route` | Repeated same (b,a) locks force a fixed quotient-type ColumnCRT/PDEC certificate. | `registered_route_open` | 同一商型复现时，相位自由度只剩核心 k，进入固定类型 CRT 证书。 |
| `bounded_type_sae_route` | If no quotient type persists beyond its threshold, total large-pair locks are SAE-countable. | `registered_route_open` | 不持久的有限字母表异常应由 SAE 容量账本吸收。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的低乘子共同核分支内。 | 保持 row_column_unconditional_closed=false。 |
| `ExactPairGCDNormalFormClosed` | `true` | `true` | 大成对核可写成精确核 k 与互素商对 b,b+a。 | 无。 |
| `FiniteQuotientAlphabetClosed` | `true` | `true` | 若 k>Y/Lambda，则商型数量至多 O(Lambda^2)。 | FiniteQuotientAlphabetForLargePairKernelLocks |
| `FixedTypePDECRouteRegistered` | `true` | `false` | 同一商型持久复现应进入固定商型 ColumnCRT/PDEC。 | FixedQuotientTypeColumnCRTOrPDECExclusion |
| `BoundedTypeSAERouteRegistered` | `true` | `false` | 商型不持久时应按有限字母表 SAE 计数吸收。 | BoundedQuotientTypeSAEAbsorption |
| `LargePairKernelDifferenceExcluded` | `false` | `false` | 尚未排斥固定商型 PDEC，也未完成不持久商型 SAE 总量账本。 | FixedQuotientTypeColumnCRTOrPDECExclusion AND BoundedQuotientTypeSAEAbsorption |

## 5. 下一步最窄点

```text
FixedQuotientTypeColumnCRTOrPDECExclusion
```

并列需要补齐：

```text
BoundedQuotientTypeSAEAbsorption
```

并行保留：

```text
LargePairKernelDifferenceColumnCRTExclusion AND MultiSourceKernelFanInSAEOrPDECExclusion
```

审稿边界：本步闭合有限商型压缩，不闭合固定商型 PDEC 排斥，也不闭合 SAE 总量账本。
