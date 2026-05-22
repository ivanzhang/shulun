# Prime Matrix 两条替代线原子化硬包同步证书

**状态：** `two_replacement_lines_atomized_to_source_root_discrete_error_terminal_scope_open`

## 1. 结论

本层把 latest true remainder 中的内部粗包继续原子化：NC-BLK/source anti-atom 已同步到 forward pre-Cauchy source-root packet 或 global terminal/PDEC-scope；beta-sieve 的 lower weight 构造和 lower-bound 支配已经闭合，连续 B=3 主项余量也已闭合，真正剩余是 P>=100000 的离散素和统一误差；exact sawtooth 已压成二次圆弧和有符号近平方条带，失败态进入 global PDEC/sparse terminal 或 canonical terminal absorption。外部线仍保持 FullS-KLS/no-projection theorem-match 或外部合同边界。本层不宣称无条件闭合。

```text
external_lemma_version_closed_conditionally=true
external_no_blackbox_version_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LatestTrueRemainderImported | `true` | `true` | 上一层已把外部线压到 FullS-KLS/no-projection theorem-match 或 actual source capacity，把内部线压到 NC-BLK/source anti-atom 与 beta-sieve/sawtooth。 | 继续把这些粗包拆成原子。 |
| ExternalNoBlackBoxStillTheoremMatch | `true` | `false` | 外部无黑箱版仍是主来源 Full-S non-AP WFD KLS theorem-match，或 actual noncanonical source support/capacity 新定理。 | ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput |
| ExternalLemmaVersionStillConditional | `true` | `false` | 外部引理版只在接受 FullS-KLS-ext 与 DStructure/Rankin 独立验收时条件闭合；本层不把它改写成无黑箱证明。 | AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| NCBLKSyncedToForwardSourceRoot | `true` | `false` | NC-BLK/source anti-atom 不再是最佳主攻名；actual 路线必须先给出不从 downstream 反推的 pre-Cauchy source-root packet。 | ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn OR global terminal/PDEC-scope route |
| NCBLKFailureDeduplicated | `true` | `true` | generic anti-atom 被 moving-delta 阻断；actual 反原子失败等价于 exact (u,v) 大原子并回到 global PDEC/sparse terminal。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| BetaLowerWeightConstructionClosed | `true` | `true` | lower weights 的 finite word rule、符号、squarefree 支撑与 d<P 已闭合。 | BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| BetaLowerBoundDominanceClosed | `true` | `true` | Buchstab tree parity pruning 已证明显式 lower weights 逐点支配筛剩余指示函数。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| BetaMainCoefficientReduced | `true` | `false` | 99% 主系数不能由有限 checkpoint 推出，已压到连续 beta 余量与离散素和统一误差。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000 |
| B3ContinuousSurplusClosed | `true` | `true` | alpha=0.43 时 s=1/alpha 位于 2<s<3，连续线性下界筛公式给出 1% 余量。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| SawtoothCompressedToNearSquare | `true` | `false` | exact floor/sawtooth 已被压成二次圆弧，再压成有符号近平方条带非集中。 | RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000 |
| NearSquareTerminalAdmitted | `true` | `false` | 近平方条带失败没有独立第四出口，进入 global PDEC/sparse terminal 或 PDEC_CAP/CleanKLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| NearSquareCanonicalAbsorptionImported | `true` | `false` | canonical 分支中近平方终端被 NoFurtherCanonicalSourceTerminalPromotionGap 吸收；strict noncanonical 分支仍需同口径终端/PDEC/KLS。 | NoFurtherCanonicalSourceTerminalPromotionGap OR strict terminal scope proof |
| DStructureRankinGateCarried | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍需独立验收或自足替代包。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层只把最新硬包原子化；没有完成外部无黑箱 theorem-match、source-root、离散素和误差、strict 终端或 DStructure。 | not closed |

## 3. 外部线

最新外部原子化基：

```text
((AcceptedFullSKLSExtExternalContract) OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 内部线

最新内部原子化基：

```text
((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR (GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND (B3DiscretePrimeSumUniformErrorPGe100000 OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR ExternalWellFactorableSawtoothDispersionBoundAlpha043 OR NoFurtherCanonicalSourceTerminalPromotionGap) AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

直接主攻原子：

- `ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn`
- `B3DiscretePrimeSumUniformErrorPGe100000`
- `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve or strict same-set PDEC scope`
- `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 5. 状态快照

| field | value |
| --- | --- |
| `previous` | `two_replacement_lines_latest_true_remainders_synced_open` |
| `fulls_remainder` | `ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open` |
| `ncblk_frontier` | `ncblk_source_antiatom_synced_to_forward_source_root_or_global_terminal_open` |
| `ncblk_dedup` | `strict_acyclic_ncblk_source_antiatom_deduplicated_to_global_terminal_open` |
| `beta_frontier` | `beta_sieve_frontier_split_to_three_self_contained_atoms_open` |
| `beta_recursion` | `lower_weight_recursion_constructed_support_closed_dominance_open` |
| `beta_dominance` | `lower_bound_dominance_closed_main_coefficient_open` |
| `beta_main` | `main_coefficient_reduced_to_continuous_and_discrete_error_inputs_open` |
| `b3_surplus` | `continuous_beta_surplus_closed_discrete_error_open` |
| `sawtooth` | `exact_sawtooth_compressed_to_quadratic_arc_discrepancy_open` |
| `quadratic` | `quadratic_arc_discrepancy_compressed_to_signed_nearsquare_strip_open` |
| `nearsquare_admission` | `nearsquare_strip_terminal_admitted_to_global_pdec_sparse_split_open` |
| `nearsquare_absorption` | `nearsquare_terminal_absorbed_beta_sieve_frontier_open` |
| `dstructure_author` | `dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open` |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-b3-continuous-beta-sieve-surplus-router.json` | `f890f23fc5f9a4820fbe2b1153efc03e071afcc60afaf518b1934132c8f6f66d` |
| `docs/monograph/prime-matrix-beta-sieve-lower-bound-dominance-router.json` | `ba91e91d25b9525c2f27748a46bc49dfdde2dadb5b073ee78d5044f3494d6420` |
| `docs/monograph/prime-matrix-beta-sieve-lower-weight-recursion-router.json` | `f1e59ca50a7822442a2515675149c4997e7daf786139146586956469560647ae` |
| `docs/monograph/prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json` | `59c06b196474c72b206d0a4ed00f676bdb5b05ae12d2b56b4b7d9642231dfa8b` |
| `docs/monograph/prime-matrix-beta-sieve-self-contained-frontier-router.json` | `81b4ac149f20bda952b72a25bdbb02743211942a23d4be00fb70a9c212676819` |
| `docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json` | `76b64234307bf057c865b20478520022f755d4232dd99462a57e4bcc2d9421d2` |
| `docs/monograph/prime-matrix-exact-residue-sawtooth-normal-form-router.json` | `d23bf9a260cc9ae3555b0cf65dc0e083298ea2a3276fcadc018d38b9ed44424f` |
| `docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json` | `753b5bd82e01a073b1d62807aec81ef84c89f4bde4ce388d37c6d042040f5dff` |
| `docs/monograph/prime-matrix-nearsquare-canonical-terminal-absorption-router.json` | `0733e7755d853ea4be0af2810de9e45d75980eaf92faa543fb1cca57c2a52e83` |
| `docs/monograph/prime-matrix-nearsquare-strip-terminal-admission-router.json` | `5c5f292b62232ab99896e182142cb5853757032fb6a63d9af3e6f93a76819ae5` |
| `docs/monograph/prime-matrix-quadratic-arc-nearsquare-spread-router.json` | `d5aad2f36c93b6a6780d05d3b8d037fc1f387e36bf50a16039b7284c0ae5bc3d` |
| `docs/monograph/prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json` | `70b20d8ddca4337179a495286b7249b4ebda9790a65cede89225306711a9cb16` |
| `docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json` | `11d509967f5a92a50caed11e4ed4aa65a2cbaea07eaa99217c2e93391cda60d5` |
| `docs/monograph/prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json` | `d387db62f911c955d9d472a42e6f8f8b1c322d42c6103cebc9e11d7bfbd14079` |
| `experiments/prime_matrix_two_replacement_lines_atomized_hard_package_router.py` | `bee956cb9035b2cf4fda79b9b242ff7a083c6c11decedaa8fd51912c9d3c07fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `54de7d90a35db971f3a9ca287b4825895c342ba6445a2b5a5152dcb9f52f587d` |
