# Prime Matrix 按序推进剩余任务路由器

**状态：** `first_order_task_closed_next_self_contained_pnt_package_open`

第一顺位 B3 边界变差已在外部 Mertens 路线下由 20000 锚点预算关闭；严格自足路线没有完成无条件闭合，下一步必须内联 reciprocal-prime Mertens 尾段所需的显式 PNT 包，然后再处理最终 DStructure/Rankin 晋级包。

```text
first_order_b3_boundary_variation_completed=true
external_mertens_route_closed=true
self_contained_mertens_tail_proved=false
promotion_package_independently_accepted=false
row_column_unconditional_closed=false
next_priority=SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000
secondary_priority=SelfContainedMeisselMertensConstantIntervalLedgerAt20000
```

## 1. 本轮完成

`B3BoundaryVariationOnePercentTransferLedger` 的外部 Mertens 路线已经由 `B3Anchor20000BoundaryVariationBudgetClosedAlpha043` 关闭。旧的 `<2.865` 乘子硬证不再是必要路线；20000 锚点给出足够预算余量。

这不等于完整行/列无条件闭合，因为完全自足 Mertens 尾段和最终晋级门仍未关闭。

## 2. 顺序任务表

| order | task | status | completed | proves unconditional | next action |
| ---: | --- | --- | --- | --- | --- |
| 1 | `B3BoundaryVariationOnePercentTransferLedger` | conditional_external_mertens_route_closed | true | false | 严格自足版继续进入 SelfContainedDusartReciprocalPrimeProofAppendixXGe10372。 |
| 2 | `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372` | reduced_to_explicit_pnt_package_open | false | false | 先证明 SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000，再补 SelfContainedMeisselMertensConstantIntervalLedgerAt20000。 |
| 3 | `SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000` | open | false | false | 按子顺序推进 SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger、ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion、FiniteThetaEnvelopeBridgeBelowAnalyticThreshold。 |
| 4 | `SelfContainedMeisselMertensConstantIntervalLedgerAt20000` | open | false | false | 给出 B1 常数区间和 x=20000 基点核验，接回 reciprocal-prime Mertens 尾段。 |
| 5 | `SelfContainedDStructureTailLog4FiniteRankinProofPackage` | open_or_referee_gate | false | false | 若走外部合同版，需独立接受；若走作者自足版，需替换该独立验收门。 |
| 6 | `RowColumnUnconditionalPromotion` | blocked_by_named_inputs | false | false | 只有前述自足包全部证明，或外部合同与最终晋级门均被接受后，才能改为 true。 |

## 3. 当前最窄下一步

```text
SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000
```

具体顺序：

1. `SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger`
2. `ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion`
3. `FiniteThetaEnvelopeBridgeBelowAnalyticThreshold`
4. `SelfContainedMeisselMertensConstantIntervalLedgerAt20000`
5. `SelfContainedDStructureTailLog4FiniteRankinProofPackage` 或独立接受对应晋级门

## 4. 最新输入基

严格自足输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部 Mertens 条件输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 证据哈希

- `docs/monograph/prime-matrix-b3-signed-delay-multiplier-anchor-router.json`: `158728d20ecf491aab9376bc1f29cc0566a9218ffb292b26b5192d8bfb5a12c9`
- `docs/monograph/prime-matrix-b3-self-contained-mertens-tail-router.json`: `8a4a73bd5523f76b8eb01bd2346e9a800afa2017d693aa22eaa7c1d431e32594`
- `docs/monograph/prime-matrix-final-guard-gate-completion-verdict-router.json`: `629cb763afb5d0c3ac9d1096f0e46437e47773036244173f58a6598a7b461d0a`

