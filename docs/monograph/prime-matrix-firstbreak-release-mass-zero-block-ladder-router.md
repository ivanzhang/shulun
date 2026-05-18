# Prime Matrix 首破裂释放质量零行块阶梯证书

**状态：** `firstbreak_release_mass_reduced_to_zero_block_ladder_open`

释放质量放大的源头被定位到首破裂前的连续零行块。边界释放只给单位需求；若零行块长度为 L，则源侧覆盖义务总量精确为 L(P-1)。因此短块必须进入 singleton/sparse SAE，长块则必须证明覆盖质量能非循环转移为 post-break AP demand；若转移失败，失败形态进入持续覆盖历史 PDEC/ColumnCRT/SAE。

```text
contiguous_zero_block_imported=true
boundary_only_amplification_blocked=true
zero_block_cover_obligation_mass_closed=true
block_length_dichotomy_closed=true
short_zero_block_singleton_sae_proved=false
long_zero_block_mass_transfer_proved=false
release_mass_amplification_proved=false
row_column_unconditional_closed=false
```

## 1. 零行块源质量

设早期零行从 `x0` 开始，且 square-anchor 分支不接管。令 `y` 是首个非零行，
于是 `[x0,y-1]` 是连续零行块，长度

```text
L = y - x0.
```

对每个 `t in [x0,y-1]` 和每个 `1<=c<P`，零行条件给出某个 `q<P` 使

```text
q | tP+c.
```

因此源侧覆盖义务总数不是估计，而是精确为

```text
L(P-1).
```

这才是可能产生放大的实际来源；首破裂释放列非空本身只给单位需求。

## 2. 长短二分

对任意阈值 `A>=1`，零行块只有两种情况：

```text
L < A   => short zero block / singleton-sparse SAE branch,
L >= A  => long zero block cover-mass transfer or persistent PDEC branch.
```

短块没有足够行向质量自动压过 AP envelope；长块虽然有 `L(P-1)` 源质量，仍必须证明这些覆盖义务
非循环地转移成 post-break 低 carrier AP demand。若不能转移，失败不再是匿名缺口，而是持续覆盖历史、
固定相位表或 moving carrier 的 `PDEC/ColumnCRT/SAE` 出口。

## 3. 新硬点

因此

```text
FirstBreakReleaseMassAmplificationOrSingletonSAE
  -> ShortZeroBlockSingletonSAESummability
  AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC
```

其中 `LongZeroBlockCoverMassTransferToAPDemandOrPDEC` 是下一主攻：证明长零块覆盖义务必须变成
post-break AP demand，或证明转移失败必产生命名 PDEC/SAE。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ReleaseMassAmplificationImported | `true` | `false` | 上一层把 actual demand 的第一主攻压到首破裂释放质量放大或 singleton SAE。 | FirstBreakReleaseMassAmplificationOrSingletonSAE |
| ContiguousZeroBlockImported | `true` | `true` | early-to-square 分裂已给出：若 square-anchor 不接管，则有零行块 [x0,y-1] 和首破裂行 y。 | zero block [x0,y-1] |
| BoundaryOnlyAmplificationBlocked | `true` | `true` | 首破裂释放列非空只给 D_y>=1；边界释放本身不能产生 Ω(H) 需求。 | NoBoundaryOnlyReleaseAmplificationGuard |
| ZeroBlockCoverObligationMassClosed | `true` | `true` | 若零行块长度 L=y-x0，则块内每个 (t,c) 都有某 q<P 覆盖，源侧覆盖义务总数精确为 L(P-1)。 | ZeroBlockCoverObligationMassLedger |
| BlockLengthDichotomyClosed | `true` | `true` | 对任意阈值 A>=1，L<A 为短块 singleton/SAE 分支，L>=A 为长块覆盖质量转移或 PDEC 分支。 | ShortZeroBlockSingletonSAESummability OR LongZeroBlockCoverMassTransferToAPDemandOrPDEC |
| ShortBlockRoutedToSingletonSAE | `true` | `false` | 短零块没有足够行向质量自动超过 AP envelope；它必须作为 singleton/sparse SAE 或局部短块证书处理。 | ShortZeroBlockSingletonSAESummability |
| LongBlockNeedsMassTransfer | `true` | `false` | 长零块有 L(P-1) 覆盖义务，但仍需证明这些义务能非循环转移为 post-break AP demand；若转移失败，失败形态是持续覆盖历史 PDEC/ColumnCRT/SAE。 | LongZeroBlockCoverMassTransferToAPDemandOrPDEC |
| AmplificationReduced | `true` | `false` | FirstBreakReleaseMassAmplificationOrSingletonSAE 被压成短块 SAE 排斥与长块覆盖质量转移/PDEC 二项。 | ShortZeroBlockSingletonSAESummability AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC |
| AmplificationProved | `false` | `false` | 本步没有证明释放质量已经放大到超过 envelope；只定位了唯一可放大的源头是前置零行块覆盖账本。 | ShortZeroBlockSingletonSAESummability AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、短块 SAE、长块质量转移、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明释放质量已经放大到超过 AP envelope。
- 本证书只证明可能放大的源头必须是首破裂前的零行块覆盖义务，而不是边界单位释放。
- 短块 singleton/sparse SAE 与长块覆盖质量转移/PDEC 仍未排斥。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_release_mass_zero_block_ladder_router.py` | `e5581944be189edc35836ed2cb4e7da4a76c7e6c4680c08681ee7a3eaf194465` |
| `docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json` | `c6166b673207c6fdc19307de71a6fe1f5b7ed887130b6c5e7e8ad28e030bd5f2` |
| `docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json` | `54575ef141b22648dd85608f8db9144e24ef013b69df9a130147857c28840c2f` |
| `docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json` | `5bd12e6d5f2553e041f20f2b0c1b86ba145c05425b0aa89d973f7707ac4925e2` |
| `docs/monograph/prime-matrix-sparse-terminal-forced-load-lower-bound-from-early-zero-row.md` | `bbd0af50c2dab533dfbd143f2ee0c987201597c15a4881fb6ef2d4196ceaa7cd` |
| `docs/monograph/prime-matrix-bpn-bk-selberg-route.md` | `377e0c33124ac43a187c69652174aba917da18e179a0e9be2f59590e7a9c2dbf` |
| `docs/monograph/prime-matrix-bad-window-source-family-extraction-router.md` | `6230a1418722ca91ea34a35069258b84592cb193170af95df7847ec855427c3c` |
