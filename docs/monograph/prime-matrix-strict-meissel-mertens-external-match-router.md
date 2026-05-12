# Prime Matrix strict Meissel-Mertens 外部匹配路由器

**状态：** `strict_meissel_mertens_external_matched_self_contained_open`

strict 外部路线下，`SelfContainedMeisselMertensConstantIntervalLedgerAt20000` 已可严格对接旧 B3 Meissel-Mertens/Dusart 外部证书：有限阶梯覆盖 `286<=x<10372`，尾段 `x>=10372` 由 reciprocal-prime Mertens 外部定理匹配，B1 口径为 `0.2614972128476428`。这只关闭外部输入并把 B3/Mertens 解析链推进到 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；自足 B1/尾段、内部 theta/低高度/contour 证明和最终行列无条件命题仍未闭合。

```text
meissel_mertens_strict_external_matched=true
meissel_mertens_interval_self_contained_closed=false
self_contained_mertens_tail_closed=false
external_b3_chain_reaches_dstructure_gate=true
dstructure_independent_acceptance_present=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. strict 外部替换

```text
SelfContainedMeisselMertensConstantIntervalLedgerAt20000
  =>
DusartMeisselMertensConstantIntervalAt20000ExternalClosed
```

## 2. Mertens 数字口径

| item | value |
| --- | ---: |
| Meissel-Mertens B1 | `0.261497212848` |
| finite step range | `[286, 10372]` |
| tail start x | `10372` |
| Dusart tail error at start | `0.001506804667` |
| external atom | `DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在早期零行反例假设链内补外部解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `StrictMeisselMertensGateActive` | `true` | `true` | strict 全局 theta 外部匹配后，当前最窄点正是 Meissel-Mertens 常数区间输入。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `StrictThetaContourAndBridgeReady` | `true` | `false` | strict 链已经外部关闭 theta contour 与有限桥，但没有关闭对应自足证明。 | ExplicitPsiThetaContourEnvelopeXGe20000StrictExternalClosedByDusart AND FiniteThetaEnvelopeBridgeStrictExternalClosedByDusartAllXPositive |
| `LegacyB3MeisselMertensExternalClosed` | `true` | `false` | 旧 B3 路由已把同一 Meissel-Mertens 常数区间原子外部替换为 Dusart 闭合原子。 | DusartMeisselMertensConstantIntervalAt20000ExternalClosed |
| `DusartReciprocalPrimeMertensExternalReady` | `true` | `false` | reciprocal-prime Mertens 外部证书提供有限阶梯、尾段匹配与 B1 常数口径。 | DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted |
| `SelfContainedMeisselMertensConstantIntervalLedgerAt20000` | `true` | `false` | 在 strict theta 前沿下接受旧 Dusart/Rosser-Schoenfeld 外部证书，可关闭该 Meissel-Mertens 外部输入。 | DusartMeisselMertensConstantIntervalAt20000ExternalClosed |
| `ExternalB3ChainReachesDStructureGate` | `true` | `false` | 外部 B3/Mertens 解析链已经推进到 DStructure/Rankin 独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `SelfContainedMeisselMertensStillOpen` | `false` | `false` | 严格自足路线仍需内联 B1 区间算术和 reciprocal-prime Mertens 尾段证明。 | SelfContainedMeisselMertensB1IntervalArithmeticLedger AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| `DStructureRankinIndependentAcceptancePresent` | `false` | `false` | 本步不是 DStructure/Rankin 独立验收，不能替代最终守门项。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosed` | `false` | `false` | 外部 Meissel-Mertens 匹配不构成行/列命题无条件闭合。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. strict 外部输入基快照

```text
ExplicitPsiThetaContourEnvelopeXGe20000StrictExternalClosedByDusart AND FiniteThetaEnvelopeBridgeStrictExternalClosedByDusartAllXPositive AND DusartMeisselMertensConstantIntervalAt20000ExternalClosed AND B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043 AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

外部路线下一守门项为 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。严格自足路线仍保留：`InternalDusartThetaEnvelopeProofLedger, CriticalLineNoZeroOn0To14FiniteLedger, CriticalStripNoOffLineZeroBelow14TuringLedger, InternalZeroFreeRegionToThetaContourEnvelopeLedger, InternalFiniteThetaEnvelopeBridgeHashLedger, SelfContainedMeisselMertensB1IntervalArithmeticLedger, SelfContainedDusartReciprocalPrimeProofAppendixXGe10372`。
