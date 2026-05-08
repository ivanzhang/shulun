# Prime Matrix B=3 边界变差乘子路由器

**状态：** `b3_boundary_variation_reduced_to_signed_multiplier_open`

B=3 边界变差的结构部分已经压实：有限小阈值素数作为精确阶梯原子保留，B=3 ordering/cap/floor/Rosser gate face 字典闭合。真正剩余不是再找一个固定常数区间，而是证明全长度 Buchstab delay kernel 的有符号传播乘子小于 2.865；一旦该乘子纪律成立，Dusart 尾段 forcing 可被 1% f(s) 预算吸收。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
b3_boundary_variation_reduced=true
b3_rosser_face_dictionary_closed=true
b3_signed_delay_kernel_multiplier_proved=false
row_column_unconditional_closed=false
```

## 1. 预算方程

| item | value |
| --- | ---: |
| alpha | 0.430000 |
| s=1/alpha | 2.325581395349 |
| f(s) | 0.431717689229 |
| 1% f(s) budget | 0.004317176892 |
| Dusart tail error at x=10372 | 0.001506804667 |
| required signed multiplier upper bound | 2.865120467574 |

也就是说，若有符号边界传播乘子 `K_B3` 满足

```text
K_B3 < 2.865
```

则 `K_B3 * 0.001506804667 < 0.004317176892 = 1% f(s)`，边界变差预算关闭。

## 2. 替换

```text
B3BoundaryVariationOnePercentTransferLedger
  =>
(B3RosserFaceDictionaryClosedAlpha043 AND B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043)
```

## 3. Face 字典

| face | equation | count for length r | role | closed |
| --- | --- | --- | --- | --- |
| ordering_faces | `u_i=u_{i+1}` | `max(r-1,0)` | 保证降序 prime word 无重复；相邻跳点碰撞只作为 Stieltjes 原子合并处理。 | `true` |
| alpha_cap | `u_1=alpha` | `1 if r>=1 else 0` | 最高素因子阈值 z=P^alpha 的移动端点。 | `true` |
| zero_floor | `u_r=0` | `1 if r>=1 else 0` | Buchstab 递归的底边；实际素数从 2 起，低阈值已由有限阶梯账本承接。 | `true` |
| b3_rosser_gate_faces | `u_1+...+u_{2m-1}+3u_{2m}=1` | `floor(r/2)` | B=3 lower word rule 的偶位门控边界。 | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BoundaryVariationGateActive | `true` | `false` | 当前 B=3 内部余项只剩边界变差传递；外部 Mertens 线下它是下一最窄点。 | B3BoundaryVariationOnePercentTransferLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内处理筛主系数误差，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FinitePrimeStepAtomsBefore10372Exact | `true` | `true` | 286<=x<10372 的素数跳点已经作为精确 Stieltjes 原子保留，不进入变差误差预算。 | 无有限低阈值误差。 |
| ExternalMertensTailAvailableForConditionalRoute | `true` | `false` | 若接受 Dusart 型外部显式 Mertens 定理，尾段一维 forcing 的最大误差为 0.001506804667。 | DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted |
| B3RosserFaceDictionaryClosed | `true` | `true` | B=3 admissible word 的 ordering/cap/floor/Rosser gate face 字典已完全列出。 | B3RosserFaceDictionaryClosedAlpha043 |
| RequiredMultiplierBudgetComputed | `true` | `true` | 1% f(s) 预算除以 Dusart 尾段最大误差，得到有符号传播乘子必须小于约 2.865。 | B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043 |
| NaiveAbsoluteFaceVariationCannotBeUsed | `true` | `true` | word 长度不固定，绝对 face 数随 r 增长；必须证明同一 Buchstab delay kernel 下的有符号乘子纪律。 | B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043 |
| BoundaryVariationReducedToSignedMultiplier | `true` | `false` | 边界变差原子被压成已闭合的 face 字典和唯一剩余的有符号 delay-kernel 乘子上界。 | (B3RosserFaceDictionaryClosedAlpha043 AND B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043) |
| B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043 | `false` | `false` | 证明 B=3 交错 Stieltjes 边界 forcing 经全长度 Buchstab 递归传播后的有效乘子 <2.865。 | B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043 |
| SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 | `false` | `false` | 若坚持完全自足路线，还必须内联证明 reciprocal-prime Mertens 尾段定理。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代本乘子证明。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372)) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

直接攻 `B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043`。这是当前 B=3 内部线的真正乘子纪律终端。
