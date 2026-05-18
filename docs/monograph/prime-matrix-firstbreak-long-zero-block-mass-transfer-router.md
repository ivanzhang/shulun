# Prime Matrix 首破裂长零块覆盖质量转移证书

**状态：** `long_zero_block_mass_transfer_reduced_to_stable_history_injection_open`

长零块覆盖质量转移被压到一个更窄的非循环接口：零行块覆盖义务可按 carrier/residue history key 投影，no-loss 账本保证义务不会无名消失；若同一低 carrier 支付表稳定延续，则剩余硬点是证明其源侧质量会注入首破裂后的 AP demand；若支付表不稳定，则失败形态必须登记为 HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE。

```text
zero_block_cover_obligation_mass_imported=true
history_projection_key_defined=true
no_loss_return_accounting_imported=true
stable_table_or_named_switch_route_registered=true
history_switch_pdec_excluded=false
postbreak_ap_demand_injection_proved=false
long_zero_block_mass_transfer_proved=false
row_column_unconditional_closed=false
```

## 1. 义务域与 history key

设长零块为 `B=[x0,y-1]`，长度 `L=y-x0`。上一层已经给出源侧覆盖义务域

```text
O_B={(t,c): x0<=t<y, 1<=c<P},   |O_B|=L(P-1).
```

对任意义务 `(t,c)`，零行条件给出某个 carrier `q<P` 使

```text
q | tP+c.
```

于是可定义同一 formal unit 内的历史键

```text
kappa=(q,a),   a == c mod q,   t == -a P^{-1} mod q.
```

这正是低 carrier AP table 的单元键；但它目前只是在零块历史中的支付键，不自动给出 post-break demand。

## 2. 无损投影与切换出口

no-loss return accounting 给出守恒口径：

```text
O_B = StableSourceRecords disjoint_union NamedReturnRecords,   Lost(O_B)=empty.
```

因此长零块质量不能无名消失。它只有两种合法去向：

```text
stable low-carrier/residue table  ->  PostBreakAPDemandInjectionFromStableHistory,
history key/carrier/phase switch  ->  HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE.
```

这一步把用户强调的“反例链与真实链的相位矛盾”具体化：若相位表长期稳定，就必须兑现为首破裂后的 AP demand；
若相位表移动或换键，则它本身就是命名的历史切换异常，而不能再作为无名逃逸口。

## 3. 新硬点

因此当前硬点被压成：

```text
LongZeroBlockCoverMassTransferToAPDemandOrPDEC
  -> ZeroBlockHistoryProjectionNoLossLedger
  AND StableLowCarrierPaymentTableOrHistorySwitchPDEC
  AND PostBreakAPDemandInjectionFromStableHistory
```

其中前两段已经是账本/路由闭合口径；真正仍缺的是：稳定历史表如何在不借用 AP envelope 饱和的情况下，
给出 post-break actual demand 下界。并行还必须排斥 history switch 的 PDEC/ColumnCRT/SAE 终端。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LongZeroBlockTransferImported | `true` | `false` | 上一层把释放质量放大主攻压到长零块覆盖质量转移或 PDEC。 | LongZeroBlockCoverMassTransferToAPDemandOrPDEC |
| ZeroBlockCoverObligationMassImported | `true` | `true` | 若零行块长度为 L，则源侧覆盖义务域 O_B 的大小精确为 L(P-1)。 | O_B={(t,c): x0<=t<y, 1<=c<P} |
| CarrierResidueHistoryKeyDefined | `true` | `true` | 每个覆盖义务 q\|tP+c 都给出 history key kappa=(q,a), a=c mod q，并对应行向 AP 条件 t==-a P^{-1} mod q。 | none for key definition |
| NoLossReturnAccountingImported | `true` | `true` | 既有 no-loss 账本保证义务只能进入 SourceRecords 或 NamedReturnRecords，不允许无名消失。 | ZeroBlockHistoryProjectionNoLossLedger |
| StableTableOrNamedSwitchRouteRegistered | `true` | `false` | 长零块历史若保持同一低 carrier/residue 支付表，则进入稳定表；若 key、carrier 或相位切换，则登记为 HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE。 | StableLowCarrierPaymentTableOrHistorySwitchPDEC AND HistorySwitchPDECOrColumnCRTExclusion |
| StableHistoryPostBreakInjectionOpen | `false` | `false` | 仍未证明稳定历史表中的源侧质量必非循环注入首破裂后的 AP demand；不能从 AP envelope 饱和反推。 | PostBreakAPDemandInjectionFromStableHistory |
| HistorySwitchTerminalExcluded | `false` | `false` | 历史切换已命名为出口，但 PDEC/ColumnCRT/MovingCarrier/SAE 终端本身尚未排斥。 | HistorySwitchPDECOrColumnCRTExclusion |
| LongZeroBlockMassTransferReduced | `true` | `false` | LongZeroBlockCoverMassTransferToAPDemandOrPDEC 被压成无损投影、稳定表或命名切换、稳定历史注入三段。 | ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND PostBreakAPDemandInjectionFromStableHistory |
| LongZeroBlockMassTransferProved | `false` | `false` | 本步没有证明长零块覆盖质量已经产生 AP demand 矛盾；只关闭了无名逃逸口并暴露出稳定注入硬点。 | PostBreakAPDemandInjectionFromStableHistory AND HistorySwitchPDECOrColumnCRTExclusion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、短块 SAE、稳定历史注入、历史切换终端排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND PostBreakAPDemandInjectionFromStableHistory AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND PostBreakAPDemandInjectionFromStableHistory AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND PostBreakAPDemandInjectionFromStableHistory AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明长零块覆盖质量已经产生 AP demand 矛盾。
- 本证书只证明该质量可按 history key 无损登记：稳定则进入注入硬点，移动则进入命名切换出口。
- `PostBreakAPDemandInjectionFromStableHistory` 与 `HistorySwitchPDECOrColumnCRTExclusion` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_long_zero_block_mass_transfer_router.py` | `ee99babc0bb3f6e1f931dfb7a875edd2c831c0e13ddd65bcb66b936cc8560109` |
| `docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json` | `e5c371d3a6176d81ee48272332c77e73dab552a2aec026249f687dbd55cbe7aa` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
| `docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.md` | `b24c6b66e0c23671e7be814d2b06d405bb240da70b3930e6d37be6241e67ab37` |
| `docs/monograph/prime-matrix-strict-boundary-residual-mass-lower-bound-router.md` | `4eb51e686967950f5e071f2be818229c082d3afaf744d8caeec83f0b6099b210` |
| `docs/monograph/prime-matrix-bad-window-source-family-extraction-router.md` | `6230a1418722ca91ea34a35069258b84592cb193170af95df7847ec855427c3c` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json` | `2f378d9d29b8bf471ebc203240de29b701774395089998c1477c1af85c384d6f` |
