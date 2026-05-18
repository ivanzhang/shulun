# Prime Matrix stable-ladder Fourier/PDEC 证书

**状态：** `stable_actual_ladder_columncrt_reduced_to_fourier_pdec_open`

稳定实际 ladder 被写成有限乘积群 G=prod_i Z/q_iZ 上的固定点位 a。零均值函数 F_a=1_a-1/|G| 的支撑相关精确等于 ladder 超额。若超额 E_a>0，则有限群 Fourier 展开给出非平凡角色下界 max_{chi!=1}|sum chi(tau(n))|>=|G|E_a/(|G|-1)。因此 stable ladder ColumnCRT 出口被改写成显式 Fourier/PDEC 输入。

```text
stable_ladder_or_sparse_sae_imported=true
finite_group_closed=true
zero_mean_cell_function_closed=true
exact_excess_identity_closed=true
fourier_pdec_bridge_closed=true
nontrivial_character_lower_bound_closed=true
anonymous_stable_ladder_columncrt_removed=true
sparse_scale_ladder_sae_carried_forward=true
stable_ladder_fourier_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

## 1. 稳定实际 ladder 的有限群

稳定实际 ladder 给出固定素数-相位词 `((q_i,a_i))`。定义：

```text
G=prod_i Z/q_iZ,
N=|G|=prod_i q_i,
tau(n)=(n mod q_i)_i,
a=(a_i)_i.
```

这个乘积群表述不要求 `q_i` 两两不同，因此比单一 CRT 模数写法更稳健。

## 2. 零均值点位函数

令：

```text
F_a(g)=1_{g=a}-1/N.
```

则 `sum_{g in G}F_a(g)=0`，且对任意支撑 `S` 有精确超额恒等式：

```text
E_a(S)=sum_{n in S}F_a(tau(n))
      =#{n in S:tau(n)=a}-|S|/N.
```

## 3. Fourier/PDEC 桥

在有限群 `G` 上取归一化 Fourier 变换。`F_a` 的平凡角色系数为 `0`，每个非平凡角色的系数模为 `1/N`。因此：

```text
E_a(S)=sum_{chi!=1} hat F_a(chi) * S_chi,
S_chi=sum_{n in S}chi(tau(n)).
```

若 `E_a(S)>0`，则：

```text
max_{chi!=1}|S_chi| >= N*E_a(S)/(N-1).
```

这就是 stable actual ladder 的显式 Fourier/PDEC 输入。

## 4. 新硬点

```text
SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC
  -> StableActualLadderOrSparseSAEImportedLedger
  AND StableActualLadderFiniteGroupLedger
  AND StableActualLadderZeroMeanCellFunctionLedger
  AND StableActualLadderExactExcessIdentityLedger
  AND StableActualLadderFourierPDECBridgeLedger
  AND StableActualLadderNontrivialCharacterLowerBoundLedger
  AND NoAnonymousStableActualLadderColumnCRTExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap
```

剩余从稳定实际 ladder ColumnCRT 黑箱出口变成显式 Fourier/PDEC cap，或 sparse scale-ladder SAE 全局求和问题。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| StableActualLadderOrSparseSAEImported | `true` | `false` | 上一层把固定尺度词内持久漂移压成稳定实际 ladder ColumnCRT/PDEC 或 sparse scale-ladder SAE。 | SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC |
| StableActualLadderFiniteGroupClosed | `true` | `true` | 稳定实际 ladder 给出有限乘积群 G=prod_i Z/q_iZ 与固定点位 a=(a_i)。 | StableActualLadderFiniteGroupLedger |
| StableActualLadderZeroMeanCellFunctionClosed | `true` | `true` | 定义 F_a=1_{g=a}-1/\|G\|，其均值为 0；稳定 ladder 超额正是 F_a 在支撑上的相关。 | StableActualLadderZeroMeanCellFunctionLedger |
| StableActualLadderExactExcessIdentityClosed | `true` | `true` | E_a(S)=sum_{n in S}F_a(tau(n))=\|{n in S: tau(n)=a}\|-\|S\|/\|G\| 精确成立。 | StableActualLadderExactExcessIdentityLedger |
| StableActualLadderFourierPDECBridgeClosed | `true` | `true` | 有限群 Fourier 展开把 E_a(S) 写成非平凡角色和；若 E_a>0，则存在非平凡角色相关非零。 | StableActualLadderFourierPDECBridgeLedger |
| StableActualLadderNontrivialCharacterLowerBoundClosed | `true` | `true` | 若 \|G\|=N>1 且 E_a>0，则存在 chi!=1 使 \|sum_{n in S}chi(tau(n))\|>=N*E_a/(N-1)。 | StableActualLadderNontrivialCharacterLowerBoundLedger |
| NoAnonymousStableActualLadderColumnCRTExit | `true` | `true` | 稳定实际 ladder ColumnCRT 出口被改写成显式 Fourier/PDEC 输入；不再保留黑箱 ColumnCRT 口径。 | NoAnonymousStableActualLadderColumnCRTExitLedger |
| SparseScaleLadderSAECarriedForwardAfterFourierBridge | `true` | `false` | 非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。 | SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger |
| StableActualLadderFourierPDECCapStillOpen | `false` | `false` | 仍未排斥该 Fourier/PDEC 下界，也未证明 sparse scale-ladder SAE 全局可求和。 | SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需给出 stable ladder Fourier/PDEC cap，或证明 sparse scale-ladder SAE 全局可控。 | SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap |

## 6. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureImportedLedger AND StablePrefixProductSupportLedger AND FirstMovingCoordinateEffectiveWidthLedger AND LowMovingCoordinateFiniteAtomLedger AND FirstMovingCoordinateDyadicPartitionLedger AND MovingCoordinateActiveProductWidthExitLedger AND MovingCoordinateActiveCountBoundLedger AND SingleMovingCoordinatePressureLocalizationLedger AND FixedMovingCoordinateDegeneratesToColumnCRTLedger AND NoAnonymousFirstMovingCoordinatePoolLedger AND SingleMovingLPFCoordinateDriftImportedLedger AND SingleMovingCoordinateStablePrefixLedger AND SingleMovingCoordinateDyadicScaleLedger AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger AND UnboundedCoordinateScaleEscapeLedger AND PostMovingCoordinateSupportDescentLedger AND SameScaleCoordinateCycleExcludedLedger AND SparseCoordinateDriftSAERegistrationLedger AND NoAnonymousSingleCoordinateDriftLedger AND ScaleEscapingSingleCoordinateDescentImportedLedger AND ScaleEscapeIntegerSupportClockLedger AND ScaleEscapeHalvingClockDescentLedger AND FiniteDepthScaleEscapePerFiberLedger AND TerminalWidthOneFiniteAtomLedger AND ScaleLadderProductWidthColumnCRTExitLedger AND PersistentScaleLadderSignatureRegistrationLedger AND SparseScaleLadderSAERegistrationLedger AND NoCyclicScaleEscapeDescentLedger AND NoAnonymousScaleEscapeDescentLedger AND PersistentScaleLadderSignatureImportedLedger AND ScaleLadderDyadicWordPartitionLedger AND ScaleLadderProductBudgetLedger AND ScaleLadderWordEntropyFiniteCapLedger AND AggregatePersistentPressureToSingleScaleWordLedger AND FixedScaleLadderMCRTColumnCRTExitLedger AND FirstMovingScaleLadderPhaseCoordinateLedger AND SparseScaleLadderSAECarriedForwardLedger AND NoAnonymousPersistentScaleLadderSignatureLedger AND FirstMovingScaleLadderPhaseDriftImportedLedger AND FixedScaleWordSlotLedger AND FinitePrimeChoicesPerScaleSlotLedger AND FiniteResidueChoicesPerPrimeSlotLedger AND FiniteActualScaleLadderAtomSetLedger AND InfinitePigeonholeStableActualScaleLadderLedger AND NoPersistentFirstMovingScaleLadderPhaseDriftLedger AND StableActualScaleLadderMCRTColumnCRTExitLedger AND SparseScaleLadderSAECarriedForwardAfterFiniteSlotLockLedger AND NoAnonymousFirstMovingScaleLadderPhaseDriftLedger AND StableActualLadderOrSparseSAEImportedLedger AND StableActualLadderFiniteGroupLedger AND StableActualLadderZeroMeanCellFunctionLedger AND StableActualLadderExactExcessIdentityLedger AND StableActualLadderFourierPDECBridgeLedger AND StableActualLadderNontrivialCharacterLowerBoundLedger AND NoAnonymousStableActualLadderColumnCRTExitLedger AND SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger AND SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有证明 stable actual ladder Fourier/PDEC cap。
- 本证书没有证明 sparse scale-ladder SAE 全局可求和。
- 本证书只把稳定实际 ladder ColumnCRT 出口桥接为显式 Fourier/PDEC 输入。
- `SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_fourier_pdec_router.py` | `a131f2fcadb1277015fd31a84dd0b1644c61784e5a059338e5e07e900b3e52bb` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json` | `c08c4bbd6f71cbaa24984949aec981abf7f8ee615ed426378a48c7b66b7c4a4c` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json` | `8657d83b213f688fd5ee653ec0fd48d219e316838d7cce221b84f5cf8be9bbc8` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json` | `4dfe3b824d5d11788941ee4bd2a4dbe0ff7a7693e1ffd8b3fd2fa8ce50550705` |
