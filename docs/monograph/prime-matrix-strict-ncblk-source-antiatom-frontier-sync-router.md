# Prime Matrix strict NCBLK/source anti-atom 前沿同步证书

**状态：** `ncblk_source_antiatom_synced_to_forward_source_root_or_global_terminal_open`

本步把上一轮 pair-energy 对角剥离留下的 NCBLK/source anti-atom 与仓库已有的 actual-source seed、假设零行 seed no-go、pre-Cauchy 来源分类、moving-block 回流和 source-declaration 下游同步合并。结论是：NCBLK/source anti-atom 仍未证明，但它也不应继续作为最深主攻名。generic 反原子路线已被 moving-delta 阻断；actual 路线必须先给出不从 downstream 反推的 forward pre-Cauchy source-root packet。若该 source-root 不能正向给出，既有分类把失败推回 moving-block/global PDEC-sparse 终端；并行仍保留 direct PDEC 同集作用域与高段模型余量。行/列命题仍未无条件闭合。

```text
ncblk_proved=false
forward_source_root_packet_proved=false
global_pdec_sparse_terminal_exclusion_proved=false
high_segment_model_gap_alpha043_c3_analytic_ledger_proved=false
row_column_unconditional_closed=false
```

## 1. 同步链

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
  -> generic WFD anti-atom no-go
  -> actual route needs acyclic pre-Cauchy source seed
  -> zero-row data cannot supply signed seed
  -> independent pre-Cauchy identity taxonomy
  -> actual moving-block spread / NC-BLK
  -> moving-block/global PDEC-sparse terminal return
  -> forward source-root packet or named terminal exclusion
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestPairEnergyFrontierImported` | `true` | `false` | 上一轮 pair-energy 对角剥离后，直接主攻被钉为 NCBLK/source anti-atom。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `NCBLKDedupRouterImported` | `true` | `false` | 既有 strict NCBLK 路由已说明该标签不是新无名终端；actual 失败会标准化为 moving atom 并回全局终端。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| `GenericWFDAntiAtomNoGoPreserved` | `true` | `true` | generic WFD/formal Type/Fourier 反原子被 moving-delta 模型阻断，不能作为自足证明。 | 必须使用 actual acyclic source，或转外部谱线。 |
| `ActualSourceSupportSeedSplitImported` | `true` | `false` | ExactUV/actual-source 支撑不是单个引理；它至少需要无环 pre-Cauchy seed 与 exact-pair 分散。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExactUVPairMassDispersionOrMaxAtomBoundLedger |
| `ZeroRowCannotSupplySeed` | `true` | `true` | 早期零行反例只给 unsigned CRT 覆盖/payment 数据，不能反向生成 signed pre-Cauchy source seed。 | IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn |
| `IndependentIdentityTaxonomyClosed` | `true` | `true` | 独立 pre-Cauchy 算术来源恒等式的合法来源类已穷尽；没有隐藏第四路线。 | ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn |
| `MovingBlockReturnImported` | `true` | `true` | actual noncanonical moving-block spread 若有低维签名则进 PDEC/SAE/ColumnCRT；无签名则回早期零行终端包。 | EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock |
| `MovingAtomGlobalTerminalSyncImported` | `true` | `false` | strict moving-atom 回流已把 clean-core moving atom 接到全局 PDEC/sparse 终端与模型/DPRC 账本。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| `CommonSourcePacketStillOpen` | `true` | `false` | 若继续正向构造 source root，仍需 common declaration packet；当前语料没有该 packet。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `SourceDeclarationDownstreamSplitImported` | `true` | `false` | common packet 的下游字段已同步为 built-in signed pairing 与 ExactUV entropy/fiber 两条子线。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `NCBLKNoLongerBestNamedTarget` | `true` | `true` | 继续把 NCBLK 当作主攻名会遮蔽真正首字段；当前应攻 forward source-root packet 或命名终端排斥。 | ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn OR (GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只同步和压窄 NCBLK/source anti-atom 前沿；source-root、全局终端、PDEC scope、高段模型、Rate 与 DStructure 仍未证明。 | ((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR (GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger)) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. Forward source-root packet 字段

| field | role |
| --- | --- |
| `declaration line before Cauchy/payment` | 禁止从 payment/零行覆盖图反推 source。 |
| `primitive summand rows with branch/sign/local-factor data` | 给出实际 primitive emitter 的可审查行。 |
| `built-in signed word/coefficient pairing` | 关闭 signed payload 的首个非循环生产字段。 |
| `actual source-domain entropy and fixed exact (u,v) fiber bound` | 支撑 ExactUV 与 source anti-atom 的真实对象。 |
| `same formal-unit exact-pair no-heavy or L2 energy ledger` | 排除单 exact-pair delta 重原子。 |
| `no downstream recovery and named return partition` | 把缺字段、循环、payload 泄漏、fiber collapse 全部命名回流。 |

## 4. 最新剩余

```text
(ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR (GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger)
```

严格活动基：

```text
((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR (GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger)) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn
```

并行保留：

```text
GlobalPDECorSparseTerminalExclusion AND AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 诚实边界

- 本证书不证明 NCBLK/source anti-atom，也不证明 forward source-root packet。
- 它只把 NCBLK 名称下的现有路线同步到底：generic 路线阻断，actual 路线必须先交 source-root packet。
- 全局 PDEC/sparse 终端、direct PDEC 同集作用域、高段模型余量、RatePreservation 与 DStructure/Rankin 仍未闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_ncblk_source_antiatom_frontier_sync_router.py` | `3c587ea3c9fae927eb06cc561152d3976aa61174414eb5e8e3c380fc39fa554b` |
| `docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json` | `373321e8dd9c2aaac0e6565bada3a5273bc99fadda6345cd4a0cb54d194b7d5b` |
| `docs/monograph/prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json` | `70b20d8ddca4337179a495286b7249b4ebda9790a65cede89225306711a9cb16` |
| `docs/monograph/prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json` | `fb988aea08dcdf541574fa412e2e37254570b8ad688b010a6c0366c03c4e7270` |
| `docs/monograph/prime-matrix-strict-actual-source-support-seed-router.json` | `6c1241bb0dd29f19cec15f147b56e495c551fb7e813158491d5a52201848d982` |
| `docs/monograph/prime-matrix-hypothetical-zero-row-seed-no-go-router.json` | `ea50b980c0a9ee5208509bfa830403c1c9a047839f48ee467fc46e4ddc78fbf4` |
| `docs/monograph/prime-matrix-independent-precauchy-identity-taxonomy-router.json` | `98673babcd5fc127e58a8f5bb1bb3b78236f770b332e937674a938dfdca50534` |
| `docs/monograph/prime-matrix-counterexample-moving-block-terminal-router.json` | `9a0eb43daa02d6e29155b0b0a15b98778c0ad12c698cc75b6d3db8d689959d8d` |
| `docs/monograph/prime-matrix-strict-moving-atom-to-global-terminal-router.json` | `23ef7a5d03efcc2e2a138c6fe4a1c3930a8414837e12bdce1f933c8b42bc8c2d` |
| `docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json` | `d9e042ffccaaf050e72788abdb0a10a5776a3cb4d8a37fc949c9710a4a832f44` |
| `docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json` | `6f2a1790c735dacb3d3c3104dd6ae6469abe97a23853e073a57fb4990e4bf769` |
