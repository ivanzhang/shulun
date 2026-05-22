# Prime Matrix 两条替代线 RNRS/ExactUV 同步证书

**状态：** `two_lines_synced_rkslog_closed_exactuv_and_completed_kls_open`

## 1. 结论

RNRS/Rudnev 回填后，上一层两条替代线中的 RKS-log open 标记已经过期。内部自足线的最新源侧真硬点是 ExactCleanCoreFullSNonAPWFDSourceEntropy，其支撑形态为 ActualNoncanonicalExactUVSupportLowerBound，下一层需证明 CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。外部无黑箱线的标准形是 ModulusDependentCompletedFullSKLSInput 或同对象的精确主来源/新自守 dispersion 证明。外部引理版仍只是在接受外部输入和 DStructure 独立验收时条件闭合。

```text
previous_internal_rks_log_open_superseded=true
rks_log_author_side_closed=true
latest_internal_self_contained_math_input=ExactCleanCoreFullSNonAPWFDSourceEntropy
latest_internal_support_form=ActualNoncanonicalExactUVSupportLowerBound
latest_internal_layer_transfer_input=CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
latest_external_no_blackbox_input=ModulusDependentCompletedFullSKLSInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof
external_lemma_conditional_package=AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
row_column_unconditional_closed=false
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousTwoLineBoundaryImported | `true` | `true` | 上一层已把无黑箱外部线和内部自足线分开，且禁止 Phi-LPF/CRT 重命名闭合。 | sync with later RNRS and ExactUV certificates |
| RKSLogSupersededByRNRSTransfer | `true` | `true` | RKS-log/TL4-L 解析核心已由 RNRS/Rudnev 倒数能量链在作者侧回填闭合；它不再是最新内部真硬点。 | ActualNoncanonicalExactUVSupportLowerBound |
| DStructureReplacementAuthorDossierNoLongerRKSBlocked | `true` | `true` | DStructure/Tail-log4/finite Rankin 自足替代包的作者侧 RKS 阻断已移除，但这不等于独立验收事件发生。 | final promotion absorption audit or independent acceptance discipline remains |
| ExactUVSupportIsLatestInternalSourceTerminal | `true` | `false` | 内部自足数学主攻点归一为 actual noncanonical exact u/v 支撑下界，等价地为 exact clean-core source entropy。 | ActualNoncanonicalExactUVSupportLowerBound OR ExactCleanCoreFullSNonAPWFDSourceEntropy |
| CleanCoreLayerTransferStillOpen | `true` | `false` | 普通 squarefree 数量、K4/K6 incidence 和 canonical 支撑偷渡均已阻断；真正需要 clean-core exact 层承认、非零转移和 thin return。 | CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn |
| ExternalNoBlackboxNormalForm | `true` | `false` | 外部无黑箱线的标准形不是泛称 DI/BFI，而是 completed、modulus-dependent Full-S KLS 输入。 | ModulusDependentCompletedFullSKLSInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof |
| ExternalLemmaConditionalClosureStillOnlyConditional | `true` | `false` | 接受 FullS-KLS-ext/completed KLS 与 DStructure 独立验收时，外部引理版可条件闭合；当前语料库没有无条件化这些输入。 | AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层同步最新真硬点并移除过期 RKS-open 标记；未证明 ExactUV/source entropy，也未发生独立晋级验收。 | ExactCleanCoreFullSNonAPWFDSourceEntropy AND final promotion acceptance/replacement discipline |

## 3. 两条线的最新标准形

外部引理版条件闭合包：

```text
AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版：

```text
ModulusDependentCompletedFullSKLSInput OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof
```

内部自足版源侧标准形：

```text
ExactCleanCoreFullSNonAPWFDSourceEntropy
ActualNoncanonicalExactUVSupportLowerBound
CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
```

## 4. 状态快照

| field | value |
| --- | --- |
| `two_lines_status` | `two_replacement_lines_pinned_external_primary_and_internal_rkslog_open` |
| `rks_rnrs_status` | `rks_log_rnrs_transfer_author_side_closed_exact_uv_still_open` |
| `rks_promotion_status` | `rks23_energy_lane_closed_final_row_column_promotion_still_blocked_by_exact_uv_and_promotion_gate` |
| `exactuv_attack_status` | `strict_exact_uv_support_reduced_to_new_actual_source_support_theorem_open` |
| `exactuv_terminal_status` | `exact_uv_support_is_unique_source_terminal_input_open` |
| `clean_support_status` | `clean_core_support_incidence_reduced_to_exact_layer_transfer_open` |
| `clean_normal_status` | `clean_core_terminal_normal_form_closed_inputs_open` |
| `fulls_match_status` | `fulls_nonap_wfd_primary_sources_screened_exact_contract_or_new_theorem_remains` |
| `fulls_remainder_status` | `ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open` |
| `dstructure_split_status` | `dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open` |

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `587f95c1d0534fa8117328237307a17992e4d178efb7284799681b45119fb567` |
| `docs/monograph/external-theorem-index.md` | `b71e51661a0db0d8c1dc6320d6e030677f3d97625628e0f20642724dec2bae66` |
| `docs/monograph/prime-matrix-clean-core-support-incidence-attack-router.json` | `c00df78309943a83448378f4984144a74616b41bfb2c40fd8cc532e45cbff4d4` |
| `docs/monograph/prime-matrix-clean-core-terminal-normal-form-router.json` | `e2519828be8151822bd02f33c2ad506c7bf9cab7bf0dd437cd3137b334791816` |
| `docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json` | `76b64234307bf057c865b20478520022f755d4232dd99462a57e4bcc2d9421d2` |
| `docs/monograph/prime-matrix-exact-uv-support-terminal-attack-router.json` | `25a56fd099c2bd4db85c40db63b5d7555583d6f7e7a9d967e33869dcf59848b3` |
| `docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json` | `4f9aa4016fbbf8d51f98c595772ce5fae1d2c224deb27047f719305ffa1e4f01` |
| `docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json` | `753b5bd82e01a073b1d62807aec81ef84c89f4bde4ce388d37c6d042040f5dff` |
| `docs/monograph/prime-matrix-strict-exact-uv-support-attack-router.json` | `e9f89b9cc78c45934694a16a33c108347a20b70c1a9a814f34dd39c9f565a08b` |
| `docs/monograph/prime-matrix-strict-rks-log-rnrs-transfer-closure-router.json` | `3e37b25128d2be14677b360f2056475767b774515f485f8aaccf26b052d0ff95` |
| `docs/monograph/prime-matrix-strict-rks23-final-promotion-audit-router.json` | `2933cf1f48eb0e340788c16844aa1b0abda9083d1e409c0081e4ccbe59bfdc35` |
| `docs/monograph/prime-matrix-two-replacement-lines-terminal-attack-router.json` | `ffe17c6cd547ba6d6f099209d50a751bab8335786dc2aa08cec8b0c15ec0a710` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `6176dbc10925eefe25b1e05df1ce43a9d10deb8e9c75ba92afc2fad8c04df420` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `428e2970175894554f68286697488827f5caa884c01ef2aab6244240f98ea094` |
| `experiments/prime_matrix_two_replacement_lines_after_rnrs_exactuv_sync_router.py` | `d1a1b859c774ec2dfaa8a323fcc8fa40d66d63307e49988719a63b6594909983` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `480748e7977d35a2461c322ecfd604593446e88a41858106d892518ed6e19856` |
