# Prime Matrix self-mirror tail gap 筛缺陷证书

**状态：** `self_mirror_reduced_to_exact_sieved_tail_gap_or_weighted_rough_crt_defect_open`

self-mirror/collar 剩余被推进到真实素数 tail 与整数 tail 的精确差额。令 w(q)=min(L,q-H)ceil((P-1)/q)。整数包络 C_all 与真实 prime tail 的差额正是非素数权重 D_np，因此 G=G_int+D_np-R_named。取 z=floor(sqrt(P-1)) 后，q>z 的 z-rough 整数与素数等价，所以失败不再是抽象整数容量问题，而是加权 sqrt-rough CRT 支撑在 tail 窗口内过密，或命名 return 吃掉筛缺陷。

```text
self_mirror_imported=true
nonprime_defect_exact_closed=true
sqrt_rough_prime_tail_identity_closed=true
endpoint_parity_defect_lower_bound_closed=true
sieved_margin_functional_closed=true
sieved_positive_gap_criterion_closed=true
weighted_rough_crt_defect_excluded=false
self_mirror_sieved_gap_proved=false
row_column_unconditional_closed=false
```

## 1. prime tail 与非素数缺陷

令

```text
w(q)=min(L,q-H)ceil((P-1)/q),  H<q<P.
```

则

```text
C_all=sum_{H<q<P}w(q),
C_tail=sum_{H<q<P, q prime}w(q),
D_np=sum_{H<q<P, q not prime}w(q).
```

因此有精确恒等式

```text
C_tail=C_all-D_np.
```

这一步把整数包络中的虚假容量全部登记为真实的非素数筛缺陷。

## 2. sqrt-rough 精确身份

取

```text
z=floor(sqrt(P-1)),
W_z=prod_{ell prime, ell<=z} ell.
```

若 `z<q<P`，则

```text
q prime  <=>  gcd(q,W_z)=1.
```

所以

```text
C_tail = sum_{H<q<=z, q prime}w(q)
       + sum_{z<q<P, gcd(q,W_z)=1}w(q).
```

这把剩余硬点改成 weighted rough CRT 支撑问题。

## 3. 筛后 margin

由上一层 late collar 公式

```text
G_int=L(L-D)+min(L,y-1)-X_core.
```

加入非素数缺陷后得到真实 gap：

```text
G=G_int+D_np-R_named
 =L(L-D)+min(L,y-1)-X_core+D_np-R_named.
```

在 self-mirror 分支 `L<=D` 中，`min(L,y-1)=L`，因此

```text
G=L(L-D)+L-X_core+D_np-R_named.
```

若

```text
L(L-D)+min(L,y-1)-X_core+D_np>R_named,
```

则正 gap 已成立。

## 4. 端点与奇偶 CRT 非素数缺陷

在 `P>3` 且 `L<=D` 时，端点 `q=P-1` 是非素数并贡献权重 `L`。此外 regular saturated 区间内的偶数槽给出显式下界：

```text
D_np >= L + 2L*#{even q: max(m+1,H+L,4)<=q<=P-2}.
```

这是最小的 mod 2 CRT 缺陷；更高素模量的缺陷由 `W_z` 的 rough 支撑继续承载。

## 5. 新硬点

```text
SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC
  -> PrimeTailNonprimeDefectExactLedger
  AND SqrtRoughPrimeTailIdentityLedger
  AND EndpointParityNonprimeDefectLowerBoundLedger
  AND SievedTailGapMarginFunctionalLedger
  AND SievedPositiveGapCriterionLedger
  AND WeightedRoughTailCRTDefectOrNamedReturnPDEC
  AND SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC
```

若失败仍存在，则不是整数 tail 可饱和，而是 sqrt-rough 加权支撑过密或 `R_named` 吃掉筛缺陷。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SelfMirrorImported | `true` | `false` | 上一层把 deep-late 剩余压成自镜像 collar，或 quotient core 层/命名 return 吃掉 margin。 | SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC |
| NonprimeDefectExactClosed | `true` | `true` | 对 w(q)=min(L,q-H)ceil((P-1)/q)，有 C_tail=C_all-D_np，其中 D_np 为 H<q<P 的非素数权重总和。 | PrimeTailNonprimeDefectExactLedger |
| SqrtRoughIdentityClosed | `true` | `true` | 取 z=floor(sqrt(P-1))、W_z=prod_{ell<=z}ell。q>z 且 q<P 时，gcd(q,W_z)=1 当且仅当 q 为素数。 | SqrtRoughPrimeTailIdentityLedger |
| EndpointParityDefectClosed | `true` | `true` | 在 self-mirror 分支 L<=D 且 P>3 时，q=P-1 是非素数端点并给出权重 L；任意 q>2 的偶数 regular saturated 槽也给出二重非素数缺陷。 | EndpointParityNonprimeDefectLowerBoundLedger |
| SievedMarginFunctionalClosed | `true` | `true` | late gap 可精确改写为 G=L(L-D)+min(L,y-1)-X_core+D_np-R_named；self-mirror 时 min(L,y-1)=L。 | SievedTailGapMarginFunctionalLedger |
| SievedPositiveCriterionClosed | `true` | `true` | 若 L(L-D)+min(L,y-1)-X_core+D_np>R_named，则正 gap 已成立。 | SievedPositiveGapCriterionLedger |
| WeightedRoughCRTDefectStillOpen | `false` | `false` | 若正 gap 仍失败，则 sqrt-rough 加权 tail 必须几乎吃满整数包络；这才是新的 CRT 全局缺陷/PDEC 接口。 | WeightedRoughTailCRTDefectOrNamedReturnPDEC |
| SelfMirrorReduced | `true` | `false` | SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC 被压成素/非素数缺陷恒等式、sqrt-rough 精确素数身份、端点/奇偶 CRT 缺陷、筛后 margin 与 weighted rough PDEC。 | PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC |
| SelfMirrorSievedGapProved | `false` | `false` | 本步没有证明 D_np 总能超过 X_core 与 R_named 的消耗，只把失败形态变成加权 rough CRT 支撑过密。 | SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 weighted rough tail 的 CRT 过密、并行的 source-rank/strict 前沿和外部谱/模型输入。 | SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明 `D_np` 总能超过 `X_core` 与 `R_named` 的消耗。
- 本证书把失败形态压成 weighted sqrt-rough CRT 支撑过密或命名 return 质量过大。
- `SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_sieved_defect_router.py` | `bccacfb3f73b74d4a754496b8f5b2cbb5b47241709d6e9f5b01cb77c8ce77f80` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json` | `17ee16b69406b0f1a4f9f932ceb56af5de0ccaf634d2c7f092a15f71da8d72d2` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json` | `496714585ada926f0875418c4d1b5ce1e3d3fa6a5d5074537069120a48b594e3` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json` | `5ccd52cc7ac9212bd7479c9ea5279049be6d279f854e11a9ab4c363645575cf7` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json` | `f10a978ed4750e3994f4075cafaa86cd69d6b525916472195c25a479c13d5cbd` |
