# Prime Matrix strict B3 长度 P 余项总变差预算路由器

**状态：** `b3_remainder_tv_reduced_to_signed_stieltjes_boundary_conditional_external_closed_self_contained_mertens_tail_open`

B3 长度 P 余项总变差缺口已经从裸 `sum |lambda_d^-|` 压缩到有符号 Stieltjes 边界预算。关键结构刚性是：CRT 余项不是可任意同号叠加的误差云；Rosser lower weights 展开为 B3 prime words 后，所有余项都落在 ordering/cap/floor/Rosser gate 的边界面上，并由 prime-harmonic 阶梯测度的 Mertens 尾段经 Buchstab delay kernel 传播。接受外部显式 Mertens/Dusart 尾段时，20000 锚点的 B3 边界变差预算已可关闭；严格自足线仍缺该 Mertens 尾段的内联证明。

```text
naive_absolute_tv_rejected=true
crt_remainder_boundary_functional_reduction_closed=true
prime_word_stieltjes_ledger_imported=true
alternating_boundary_remainder_reduction_imported=true
anchor20000_boundary_variation_budget_imported=true
b3_tv_budget_conditional_external_closed=true
b3_tv_budget_strict_self_contained_proved=false
self_contained_mertens_tail_proved=false
b3_remainder_total_variation_budget_proved=false
unified_terminal_budget_strict_inequality_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 结构压缩

裸 CRT 估计只给出

```text
|R_{x,z}| >= (P-1)W^- - sum_d |lambda_d^-|.
```

但这不是可闭合的最优结构。B3 Rosser 权重应展开为 prime words；此时长度 P 余项是

```text
signed Stieltjes boundary remainder on B3 admissible faces.
```

因此当前 TV 项的真实替换是

```text
B3RemainderTotalVariationBudgetForLengthP
  =>
B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger
  =>
B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043
```

其中 `ANCHOR` 在接受外部显式 Mertens/Dusart 尾段时已由 20000 锚点闭合；严格自足线仍需内联 Mertens 尾段证明。

## 2. 压缩表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `raw_absolute_tv_rejected` | sum_d \|lambda_d^-\| is not the usable B3 remainder budget. | `discipline_closed` | 裸绝对值会丢失 Rosser word 交错与边界面结构，不能作为自足闭合路径。 |
| `crt_remainder_as_boundary_functional` | A_d(x)-(P-1)/d is an endpoint/face functional after expanding lambda_d^- into prime words. | `closed_reduction` | 长度 P 的 CRT 余项不是自由符号云，而由 Stieltjes 阶梯测度边界控制。 |
| `prime_word_stieltjes_import` | B3 prime-word sums equal iterated Stieltjes integrals over the B3 admissible polytope. | `imported_closed` | 离散 prime-word 和到 Stieltjes 对象是精确重写，无解析误差。 |
| `alternating_boundary_split` | B3AlternatingBoundaryRemainderOnePercentLedger => B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger. | `imported_reduction` | 真正余项是 prime-harmonic/Mertens 一维包络经 B3 边界变差传播。 |
| `anchor20000_conditional_budget` | K_B3 <= 4e^gamma/s = 3.063444558943 and tail error <=0.001294124698. | `conditional_external_closed` | 若接受外部 Mertens/Dusart 尾段，锚点 20000 后边界变差小于 1% f(s)。 |
| `self_contained_tail_boundary` | Strict self-contained closure still needs SelfContainedDusartReciprocalPrimeProofAppendixXGe10372. | `open_self_contained_input` | 完全自足版缺的是素数倒数 Mertens 尾段内联证明，不是新的零行几何命题。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只服务早期零行反例链中的 prefix 粗筛余输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `NaiveAbsoluteTVBlocked` | `true` | `true` | 不能把 `sum \|lambda_d^-\|` 当作最终预算；必须保留 Rosser 交错和 B3 面结构。 | Use signed Stieltjes boundary budget. |
| `SignedBoundaryReductionClosed` | `true` | `true` | 长度 P 余项被压成 B3 prime-word Stieltjes 边界余项，而非自由 CRT 误差云。 | B3AlternatingBoundaryRemainderOnePercentLedger |
| `ConditionalExternalB3TVClosed` | `true` | `false` | 接受外部显式 Mertens/Dusart 尾段时，已有 20000 锚点和 delay-kernel BV 乘子可关闭 B3 TV。 | External Mertens/Dusart acceptance, not strict self-contained proof. |
| `StrictSelfContainedB3TVProved` | `false` | `false` | 严格自足版仍需内联证明 prime-harmonic Mertens 尾段包络。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| `UnifiedTerminalBudgetUpdated` | `true` | `false` | 统一预算方程的 TV 项现在有条件外部闭合和严格自足剩余边界。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND FiniteBoundaryPrefixRoughCountCertificate AND downstream terminal/cold-supply inputs |
| `DirectUnconditionalContradictionReached` | `false` | `false` | B3 TV 的压缩尚未触发统一终端预算严格不等式。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate AND terminal/cold-supply inputs |

## 4. 下一最窄点

```text
SelfContainedDusartReciprocalPrimeProofAppendixXGe10372
```

并行保留：

```text
FiniteBoundaryPrefixRoughCountCertificate AND B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND ColdCoreNonpersistentSupplyUpperBound
```

审稿边界：本步不声明 strict 自足 B3 TV 已闭合；它只把裸 TV 缺口压成有符号 Stieltjes 边界预算，并登记外部条件闭合与自足 Mertens 尾段剩余。
