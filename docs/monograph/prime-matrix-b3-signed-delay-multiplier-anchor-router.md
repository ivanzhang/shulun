# Prime Matrix B=3 有符号 delay 乘子锚点提升路由器

**状态：** `b3_boundary_variation_conditional_closed_self_contained_mertens_tail_open`

旧的 10372 锚点要求乘子 <2.865，过窄。把精确有限阶梯段提升到 x<20000 后，Dusart 尾段误差降为 0.001294124698；在 alpha=0.43、2<s<3 中，Buchstab delay kernel 的 BV 乘子由分部积分给出 <=4e^gamma/s=3.063444559。乘积 0.003964479265 小于 1% f(s)=0.004317176892，因此外部 Mertens 定理版的 B=3 边界变差和 99% 主系数包关闭。完全自足版仍只剩 Mertens 尾段定理内联证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
b3_signed_delay_multiplier_anchor_route_closed=true
b3_boundary_variation_one_percent_conditional_closed=true
beta_sieve_main_coefficient_99pct_conditional_closed=true
old_literal_multiplier_lt2865_proved=false
self_contained_mertens_tail_proved=false
row_column_unconditional_closed=false
```

## 1. 锚点提升

旧充分条件：

```text
B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043
  =>
B3Anchor20000BoundaryVariationBudgetClosedAlpha043
```

实际结构闭合包：

```text
B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043
  =>
(B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND B3TwoToThreeDelayKernelBVMultiplierLE3064Alpha043)
```

| item | value |
| --- | ---: |
| old anchor x | 10372 |
| promoted anchor x | 20000 |
| promoted segment primes | 990 |
| first promoted prime | 10391 |
| last promoted prime | 19997 |
| promoted reciprocal mass | 0.067655410327 |
| P threshold where P^alpha reaches promoted anchor | 10055307096 |

## 2. Delay 乘子账本

| item | value |
| --- | ---: |
| alpha | 0.430000 |
| s=1/alpha | 2.325581395349 |
| 2<s<3 | true |
| f(s) | 0.431717689229 |
| 1% f(s) budget | 0.004317176892 |
| Dusart tail error at promoted anchor | 0.001294124698 |
| BV multiplier bound | 3.063444558943 |
| forced error bound | 0.003964479265 |
| budget slack | 0.000352697627 |

2<s<3 中

```text
f(s)=s^{-1} int_1^{s-1} 2e^gamma/t dt.
```

对 Stieltjes forcing 使用分部积分，`phi(t)=2e^gamma/t` 单调递减，所以

```text
(|phi(1)|+|phi(s-1)|+TV(phi))/s = 4e^gamma/s.
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SignedDelayMultiplierGateActive | `true` | `false` | 上一层唯一 B=3 内部硬点是有符号 delay-kernel 乘子纪律。 | B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内处理筛主系数误差，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FaceDictionaryAvailable | `true` | `true` | 上一层已经列出 B=3 ordering/cap/floor/Rosser gate face 字典。 | 无 face 字典剩余。 |
| FiniteAnchorPromotion10372To20000Closed | `true` | `true` | 把 10372<=x<20000 的素数跳点也精确保留，从而降低无限尾段 Mertens forcing。 | B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 |
| TwoToThreeDelayKernelFormulaClosed | `true` | `true` | alpha=0.43 给 s=2.325581，处于 2<s<3；lower sieve 只用 phi(t)=2e^gamma/t 的一层 delay kernel。 | B3TwoToThreeDelayKernelBVMultiplierLE3064Alpha043 |
| DelayKernelBVMultiplierBoundClosed | `true` | `true` | Stieltjes 分部积分给 BV 乘子 <=4e^gamma/s=3.063444558943。 | B3TwoToThreeDelayKernelBVMultiplierLE3064Alpha043 |
| PromotedAnchorOnePercentBudgetClosed | `true` | `true` | 锚点 20000 处 Dusart 尾误差乘以 BV 乘子仍小于 1% f(s)。 | B3Anchor20000BoundaryVariationBudgetClosedAlpha043 |
| OldMultiplierAtomBypassedByAnchorPromotion | `true` | `false` | 旧的 10372 锚点 <2.865 充分条件不再硬证；改由 20000 锚点的更优预算直接关闭父级边界变差。 | B3Anchor20000BoundaryVariationBudgetClosedAlpha043 |
| SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 | `false` | `false` | 若坚持完全自足路线，还必须内联证明 reciprocal-prime Mertens 尾段定理。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代本乘子证明。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372)) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

外部 Mertens 定理版的 B=3 beta-sieve 主系数包已关闭，晋级看 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足版仍先攻 `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372`。
