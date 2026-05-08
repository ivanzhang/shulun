# Prime Matrix B=3 显式素数倒数 Mertens 包络路由器

**状态：** `explicit_reciprocal_mertens_external_closed_self_contained_tail_proof_open`

显式素数倒数 Mertens 包络被压到最窄边界：286<=x<10372 是有限阶梯账本，x>=10372 可由 Dusart 型外部定理关闭；但完全自足路线仍缺少该外部定理的内联证明。因此外部定理版下一点转为 B=3 边界变差传递，自足版下一点则是 reciprocal-prime Mertens 尾段证明附录。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
explicit_prime_reciprocal_mertens_external_closed=true
explicit_prime_reciprocal_mertens_self_contained_proved=false
finite_prime_step_ledger_286_to_10371_closed=true
dusart_tail_parameter_match_closed=true
row_column_unconditional_closed=false
```

## 1. 拆分律

完全自足路线：

```text
ExplicitPrimeReciprocalMertensEnvelopeXGe286
  =>
(B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372)
```

外部定理路线：

```text
ExplicitPrimeReciprocalMertensEnvelopeXGe286
  =>
DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted
```

Dusart/Rosser-Schoenfeld type reciprocal-prime Mertens estimates close the x>=10372 tail as an external theorem. A fully self-contained proof would have to reproduce that explicit PNT/Mertens machinery inside this project.

## 2. 有限阶梯账本

| item | value |
| --- | ---: |
| low x | 286 |
| high x exclusive | 10372 |
| primes in segment | 1211 |
| first prime in segment | 293 |
| last prime in segment | 10369 |
| reciprocal mass in segment | 0.477836381628 |
| prefix mass below high x | 2.487278820844 |
| P threshold where P^alpha reaches 10372 | 2183811432 |
| worst finite B1 audit x | 286 |
| worst finite B1 audit error | 0.015229745650 |

该有限表不是用实验外推无限尾段；它只是把小阈值素数跳点作为精确 Stieltjes 原子保留。

## 3. Dusart 尾段匹配

| item | value |
| --- | ---: |
| tail start x | 10372 |
| log tail start | 9.246865146659 |
| Dusart error at tail start | 0.001506804667 |
| error decreases for tail | true |
| self-contained proof in repo | false |

外部来源：Dusart, *Estimates of some functions over primes without R.H.*, arXiv:1002.0442。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExplicitPrimeReciprocalMertensGateActive | `true` | `false` | 上一层最新最窄点是 x>=286 的显式素数倒数 Mertens 包络。 | ExplicitPrimeReciprocalMertensEnvelopeXGe286 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条内的筛主系数误差，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| PreviousLowHighSplitAvailable | `true` | `true` | prime-harmonic 包络已拆成低素数有限账本与高阈值显式 Mertens 包络。 | 无上游拆分剩余。 |
| FinitePrimeStepLedger286To10371Closed | `true` | `true` | 286<=x<10372 只含有限个素数跳点，作为精确阶梯测度保留，不消耗渐近误差。 | B3FinitePrimeReciprocalStepLedger286To10371PGe100000 |
| DusartTailParameterMatchXGe10372Closed | `true` | `false` | x>=10372 与 Dusart reciprocal-prime 显式 Mertens 定理的有效区间匹配；这是外部定理匹配，不是仓库内证明。 | DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted |
| ExternalRouteForExplicitMertensEnvelopeClosed | `true` | `false` | 若接受 Dusart/Rosser-Schoenfeld 型外部显式定理，ExplicitPrimeReciprocalMertensEnvelopeXGe286 可关闭。 | DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted |
| SelfContainedTailProofStillOpen | `false` | `false` | 完全自足路线仍必须内联证明 x>=10372 的 reciprocal-prime Mertens 显式误差。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| B3BoundaryVariationOnePercentTransferLedger | `false` | `false` | Mertens 包络关闭后，还需证明 B=3 admissible 区域的边界变差传递小于 1% f(s)。 | B3BoundaryVariationOnePercentTransferLedger |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代整个 B=3 边界包。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372)) AND B3BoundaryVariationOnePercentTransferLedger) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND B3BoundaryVariationOnePercentTransferLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND B3BoundaryVariationOnePercentTransferLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

完全自足路线先攻 `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372`；若接受外部显式 Mertens 定理，则下一点直接转为 `B3BoundaryVariationOnePercentTransferLedger`。
