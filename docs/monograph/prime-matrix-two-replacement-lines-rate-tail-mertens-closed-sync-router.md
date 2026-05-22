# Prime Matrix 两条替代线 rate-bearing Mertens 尾段闭合同步证书

**状态：** `two_replacement_lines_rate_tail_mertens_closed_terminal_gates_open`

## 1. 结论

后续 strict rate-bearing Mertens 同步已关闭自足 Mertens 尾段，因此两条替代线不应继续把 SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 或 SelfContainedMeisselMertensConstantIntervalLedgerAt20000 作为活动硬点。最新内部承重门回到 source-root、PDEC/CleanKLS、RatePreservation 与 DStructure；外部无黑箱线仍保持 FullS theorem-match 或新 dispersion 证明边界。

```text
external_lemma_version_closed_conditionally=true
external_no_blackbox_version_closed=false
strict_self_contained_mertens_tail_proved=true
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| B3DeepSyncImported | `true` | `true` | 上一层仍把自足 B3 分支写成显式 PNT/theta 包络与 Meissel-Mertens 常数区间。 | 导入后续 rate-bearing Mertens 最新同步。 |
| DirectInternalDusartThetaPNTClosed | `true` | `true` | 直接内部 Dusart theta/PNT 包络已由 P5.1 自足同步关闭。 | DusartP51ThetaUpperFullSelfContainedLedger |
| UnsmoothedPerronClosed | `true` | `true` | 非平滑 Perron 常数层已自足闭合为 C=12128。 | UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128 |
| MeisselMertensB1Closed | `true` | `true` | Meissel-Mertens B1 常数区间已由 Euler product 区间证书自足关闭。 | SelfContainedMeisselMertensB1EulerProductIntervalClosedRadius2eMinus6At20000 |
| StrictMertensTailClosed | `true` | `true` | 有限倒数素数跳点、分部求和、theta/PNT 包络与 B1 常数区间全部导入后，strict 自足 Mertens 尾段移出活动剩余。 | closed |
| ExternalB3StillAtDStructureGate | `true` | `false` | 外部 Mertens/theta 路线也已到 DStructure/Rankin 门，但独立验收仍不是作者侧可生成证明。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| InternalBasisCondensedToTerminalGates | `true` | `false` | 删除自足 PNT/Mertens 旧硬点后，内部线最新承重门回到 source-root、PDEC/CleanKLS、Rate 与 DStructure。 | ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| DStructureStillIndependentOrSelfContainedReplacement | `true` | `false` | DStructure/Rankin 作者侧普通剩余已归零，但外部验收或完整自足替代包仍未完成。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层关闭的是 B3/Mertens 尾段解析活动缺口；没有关闭 source-root、PDEC/CleanKLS、Rate、FullS theorem-match 或 DStructure。 | not closed |

## 3. 外部线

```text
((AcceptedFullSKLSExtExternalContract) OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部引理版仍只给条件闭合；无黑箱外部版仍需同对象 FullS theorem-match、actual source capacity 新定理或新 automorphic/dispersion 证明。

## 4. 内部线

```text
((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR (GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NoFurtherCanonicalSourceTerminalPromotionGap) AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 直接主攻原子

- `ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn`
- `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet`
- `RatePreservationLedger_FOR_moving_atom_packet`
- `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage`
- `ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof`

## 6. 状态快照

| field | value |
| --- | --- |
| `previous` | `two_replacement_lines_b3_discrete_synced_to_mertens_pnt_and_dstructure_open` |
| `rate_tail` | `rate_bearing_tail_mertens_strict_self_contained_tail_closed_terminal_gates_open` |
| `direct_dusart` | `direct_internal_dusart_theta_pnt_envelope_closed_by_p51_self_contained_sync` |
| `b1` | `meissel_mertens_b1_interval_self_contained_closed` |
| `unsmoothed` | `unsmoothed_perron_strict_self_contained_closed_mertens_tail_still_open` |
| `dstructure` | `dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open` |

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json` | `76b64234307bf057c865b20478520022f755d4232dd99462a57e4bcc2d9421d2` |
| `docs/monograph/prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json` | `ad59843dbb160a980cf5fdc960021fc483103a34e2e0b6b1864e90d579a6b474` |
| `docs/monograph/prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.json` | `98aa010bfd59375efc8bc7e16839fbd63a07a9f104482dd15655c0144b03e83f` |
| `docs/monograph/prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json` | `41ecd4cfd58beb65c2ec5e1b5fdf2119ec46954e790ed0f036f92b66bfc282d4` |
| `docs/monograph/prime-matrix-strict-unsmoothed-perron-final-sync-router.json` | `2ff340b6c504622941703a1f65a02bb435c37f64dbb29d0fb664a0b7cc2fd8e8` |
| `docs/monograph/prime-matrix-two-replacement-lines-b3-deep-sync-router.json` | `388b8c3cf52ebe40371e1611f5ba1dc964e6d0e768e521c87fd54891c80cde8a` |
| `experiments/prime_matrix_two_replacement_lines_rate_tail_mertens_closed_sync_router.py` | `85a8a889a5014642897832bd9b6793deaac7c668f8130987fc98f9fcf57eda20` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `1956bdad74505e81ad5c0ca5e1570a3be4c46951e7043ef46764891635bf2547` |
