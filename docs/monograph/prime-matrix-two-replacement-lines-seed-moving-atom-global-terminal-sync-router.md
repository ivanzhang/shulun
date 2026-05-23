# Prime Matrix 两条替代线 seed/moving-atom/global-terminal 同步证书

**状态：** `two_replacement_lines_seed_moving_atom_global_terminal_synced_open`

## 1. 结论

ExactUV/source 非循环前沿的 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ActualNoncanonicalCleanCoreMovingAtomExclusion` 已与 strict moving-atom/global-terminal 证书同步：moving atom 排斥不再是孤立硬点；若 seed 下仍存在 clean-core moving atom，它必须进入 GlobalPDECorSparseTerminalExclusion 并支付 ExplicitModelGapAndFiniteDPRCLedger。 因而最新内部活动基变为 AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger；严格自足版还保留 RatePreservationLedger_FOR_moving_atom_packet 与 SelfContainedDStructureTailLog4FiniteRankinReplacementPackage。 ExactUV/pair-mass 支线不能作为独立闭合证明，因为它下游压到 rate-bearing large-pair packet 或回到全局终端。外部引理版仍只是条件闭合，目标命题仍未无条件闭合。

```text
moving_atom_isolated_hardpoint_removed=true
acyclic_seed_current_corpus_proved=false
moving_atom_exclusion_current_corpus_proved=false
global_pdec_sparse_terminal_exclusion_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
rate_preservation_ledger_proved=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExactUVSourceFrontierImported | `true` | `true` | 上一层已把 ExactUV/source 三标签归一为无环源种子加 clean-core moving atom 排斥。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ActualNoncanonicalCleanCoreMovingAtomExclusion |
| MovingAtomToGlobalTerminalImported | `true` | `true` | strict moving-atom 证书说明：若 seed 下仍有 clean-core moving atom，则它必须进入全局 PDEC/sparse 终端并支付模型/DPRC 账本。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| MovingAtomNoLongerIsolatedHardpoint | `true` | `true` | moving atom 排斥不再作为孤立最终硬点；它被非循环接到 global terminal packet。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| AcyclicSeedStillOpen | `true` | `false` | 无环 pre-Cauchy noncanonical primitive source seed 尚未由当前材料证明。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn |
| GlobalPDECSparseTerminalStillOpen | `true` | `false` | 当前语料尚未全局排斥 persistent PDEC、ColumnCRT、SAE/LocalSurvivor 或 sparse terminal 家族。 | GlobalPDECorSparseTerminalExclusion |
| ExplicitModelGapDPRCStillOpen | `true` | `false` | 模型余量与有限 DPRC 账本仍是独立未闭合账本。 | ExplicitModelGapAndFiniteDPRCLedger |
| RatePreservationCarried | `true` | `false` | moving atom packet 仍需 log-power 速率保持；定性投影二分不能替代。 | RatePreservationLedger_FOR_moving_atom_packet |
| PairMassRouteNotIndependentProof | `true` | `true` | ExactUV/pair-mass 支线不能独立闭合 source entropy；它下游压到 rate-bearing large-pair packet 或回到全局终端。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND RateBearingLargePairAtomPacketExclusion |
| GlobalTerminalBoundaryImported | `true` | `true` | 当前已物化局部 PDEC/LocalSurvivor/NC-BLK 前沿耗尽；剩余是全局终端家族排斥，不是局部样本补丁。 | GlobalTerminalFamilyExclusion |
| GlobalTerminalSplitImported | `true` | `true` | 全局终端家族已拆成 PDEC-CAP 或内部 CleanKLS 大筛；最终晋级还保留 DStructure/Rankin 门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| AcyclicTerminalSaturationImported | `true` | `false` | 继续展开 strict acyclic terminal family 会饱和为非递归构造/同集 PDEC 作用域/新 joint 公式三臂，而非闭合证明。 | (NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| HighTailNoLongerActiveButSelfContainedPackageCarried | `true` | `false` | 高段解析常数可被外部 Mertens/Dusart 移出活动硬点；严格自足仍需保留 zeta/Mertens 包时不得伪称终稿。 | self-contained high-tail package only if refusing external explicit estimates |
| ExternalNoBlackboxFrontierCarried | `true` | `false` | 无黑箱外部版仍需同对象 Full-S theorem-match、actual source capacity 或 completed residue dispersion。 | (ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof OR CDependentResidueWeightSpectralCancellationInput OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| ExternalLemmaOnlyConditional | `true` | `false` | 外部引理版仍只在接受 FullS-KLS-ext 与 DStructure 独立验收时条件闭合；这不是完全无条件证明。 | AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| InternalSelfContainedVersionClosed | `false` | `false` | 本层只同步并移位真硬点；未证明 seed、global terminal、DPRC/model、Rate 或自足 DStructure。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |
| RowColumnUnconditionalClosed | `false` | `false` | 没有把 moving atom 接回 global terminal 或外部条件接受写成目标命题无条件闭合。 | not closed |

## 3. 最新两线边界

上一层内部源侧基：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ActualNoncanonicalCleanCoreMovingAtomExclusion
```

moving atom 接回全局终端后的内部活动基：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger
```

严格自足版保留为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若继续展开终端家族，当前饱和基为：

```text
(NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部引理条件版：

```text
AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof OR CDependentResidueWeightSpectralCancellationInput OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 非循环纪律

本证书只允许从 ExactUV/source 非循环前沿正向导入 strict moving-atom/global-terminal 归约。 它删除的是 moving atom 作为孤立出口的地位，不删除无环源种子、全局终端排斥、模型/DPRC、Rate 或 DStructure 门。 ExactUV/pair-mass 支线若要继续使用，必须提供独立 pair energy 或 large-pair packet 排斥，不能回证 source entropy。

## 5. 状态快照

| field | value |
| --- | --- |
| `exactuv_source_status` | `two_replacement_lines_exactuv_source_frontier_reduced_to_seed_and_moving_atom_open` |
| `moving_atom_global_status` | `strict_moving_atom_reduced_to_global_terminal_and_model_dprc_open` |
| `moving_atom_packet_status` | `moving_atom_exclusion_reduced_to_rate_bearing_terminal_packet_and_dprc_open` |
| `pair_energy_status` | `strict_independent_pair_energy_reduced_to_rate_bearing_large_pair_packet_exclusion_open` |
| `global_boundary_status` | `materialized_frontier_exhausted_terminal_family_exclusion_open` |
| `global_split_status` | `global_terminal_family_exclusion_reduced_not_closed` |
| `acyclic_terminal_saturation_status` | `strict_acyclic_terminal_family_saturated_to_nonrecursive_breaker_open` |
| `high_tail_reconciliation_status` | `strict_high_tail_reconciled_to_mertens_tail_and_strict_terminal_family_open` |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `b9f70b7be4de87428053946aca2bcc85e7d768ff350474cec238fb98bc8ab3f9` |
| `docs/monograph/external-theorem-index.md` | `ab1e78cc903b6e7575379335ef76e20080aa0a6cc6ec2f10e186ddec5a2a0d7c` |
| `docs/monograph/prime-matrix-global-terminal-family-boundary-router.json` | `44274d6f4fb05f658d7ca8a6b8123032efdad658273b003969d8af871f286aad` |
| `docs/monograph/prime-matrix-global-terminal-family-exclusion-split-router.json` | `f9a5e6a0583a20578b3a98952382fe6a149b6c46ad57591974e4268bd8d9a03b` |
| `docs/monograph/prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json` | `ee2c23863dfa524a59dfb34333d45cef28f4e606a258cd4d7a02f2904455277c` |
| `docs/monograph/prime-matrix-strict-high-tail-corpus-reconciliation-router.json` | `6e09be944654bce653382054981fae9662c824384d1397b629ec50f6e553422c` |
| `docs/monograph/prime-matrix-strict-independent-pair-energy-attack-router.json` | `b587d4d2665daeb0158f0c429f52b98ec6461e1e33d6d6a1b4b60af76dd88f74` |
| `docs/monograph/prime-matrix-strict-moving-atom-terminal-packet-frontier-router.json` | `fa8f1b0bc5b769aa5932c04ed4915144912213e46b163a1202ca2a5d5fe86ac7` |
| `docs/monograph/prime-matrix-strict-moving-atom-to-global-terminal-router.json` | `23ef7a5d03efcc2e2a138c6fe4a1c3930a8414837e12bdce1f933c8b42bc8c2d` |
| `docs/monograph/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.json` | `8c6f3c4ea4ead438ec4efa1fb4894608c50dd67e33b46807aa3872d5a4c2f4d5` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `d2681fe217a0a59ccad9ddd1f899a1170697f2c886dc2325d6e55a113abca5ef` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `4e4a61c297fc36a37920bbd0653f505aa46bf2f46c0cd6f9943aa7cc854d3b4e` |
| `experiments/prime_matrix_two_replacement_lines_seed_moving_atom_global_terminal_sync_router.py` | `0128b51022d753c95136964742dce257c23ad487d6876a62d25c18af5d374209` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `1769ae69dd075b1d9c92d3d0acf3ff9ced0b272da854d3c00e15eb89707c302b` |
