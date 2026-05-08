# Prime Matrix B=3 自足 Mertens 尾段证明边界路由器

**状态：** `self_contained_mertens_tail_reduced_to_explicit_pnt_package_open`

完全自足 Mertens 尾段没有从当前几何或 B=3 筛结构自动闭合；它等价于把显式 PNT 机器内联：零点自由区/显式 theta 误差、B1 常数区间，以及分部求和转移。仓库已有平滑显式公式起点和分部求和形式，但缺少零点自由区与 B1 区间证明。因此外部 Dusart 版已经推进到 DStructure，完全自足版的唯一真正剩余是显式 PNT 包。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
self_contained_mertens_tail_reduced=true
self_contained_mertens_tail_proved=false
external_mertens_route_closed=true
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
SelfContainedDusartReciprocalPrimeProofAppendixXGe10372
  =>
(B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000)
```

## 2. 来源审查

| item | value |
| --- | --- |
| smooth_explicit_formula_appendix_present | `true` |
| zero_free_region_proof_present | `false` |
| explicit_theta_envelope_present_in_appendix | `false` |
| partial_summation_transfer_formal | `true` |
| meissel_mertens_constant_interval_present | `false` |
| tail_20000_self_contained_proved | `false` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SelfContainedMertensTailGateActive | `true` | `false` | 完全自足路线的唯一剩余是把 Dusart reciprocal-prime Mertens 定理内联证明。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条内的筛主系数解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FinitePromotionTo20000Reusable | `true` | `true` | 上一层已经把 10372<=x<20000 提升为有限精确阶梯账本；自足尾段只需从 x>=20000 开始。 | B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 |
| SmoothExplicitFormulaAppendixPresent | `true` | `true` | 仓库已有平滑 Chebyshev 显式公式附录，可作为 PNT 型证明链的起点。 | 还不能推出显式零点自由区或 Dusart 常数。 |
| PartialSummationTransferClosed | `true` | `true` | 一旦给出显式 theta/psi 误差和常数区间，素数倒数和由 Stieltjes 分部求和形式推出。 | PrimeReciprocalPartialSummationFromThetaEnvelopeClosed |
| ExplicitZeroFreeThetaEnvelopeMissing | `false` | `false` | 当前附录没有 de la Vallee Poussin/Korobov-Vinogradov 型零点自由区与显式 theta 误差证明。 | SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 |
| MeisselMertensConstantIntervalMissing | `false` | `false` | 当前仓库没有自足给出 B1 常数区间并与 x=20000 基点核验对接。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| SelfContainedMertensTailReducedToPNTPackage | `true` | `false` | 旧 Dusart 原子被压成有限锚点、分部求和、显式零点自由 theta 包、B1 常数区间四项。 | (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) |
| SelfContainedPrimeReciprocalMertensTailXGe20000 | `false` | `false` | 等价的简写：从 x>=20000 开始给出自足 reciprocal-prime Mertens 尾段误差。 | SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted | `true` | `false` | 若接受 Dusart 外部定理，本分支已经由上一层条件路线关闭。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是外部 Mertens 版最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

自足版先攻 `SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000`，随后补 `SelfContainedMeisselMertensConstantIntervalLedgerAt20000`。
 外部 Mertens 版则继续晋级 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
