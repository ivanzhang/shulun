# Prime Matrix 两条替代线终端硬攻证书

**状态：** `two_replacement_lines_pinned_external_primary_and_internal_rkslog_open`

## 1. 总结

两条替代线已经压到可核查终端：无黑箱外部线必须逐项证明 exact full-S non-AP WFD KLS 定理，或写出新的自守/dispersion 证明；内部自足线必须同时证明 FineSignedSourcePackage 与 Tail-log4/RKS-log 倒数 Kloosterman 固定对数节省。外部引理版只在接受 FullS-KLS-ext 和 DStructure/Rankin 独立验收时条件闭合；当前语料库仍未无条件闭合。

```text
external lemma conditional package:
AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance

no-blackbox external remainder:
ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof

internal self-contained remainder:
FineSignedSourcePackage AND SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving

row_column_unconditional_closed=false
```

## 2. 无黑箱外部主来源线

精确定理目标：

```text
For every fixed A>0 and prime P large enough, prove the full-S non-AP WFD Kloosterman-large-sieve estimate for W_full(C,S,H) with C≈P/log^O(P), S≈P, H<=P/log^O(P), well-factorable lambda_c, divisor-bounded beta_s, smooth omega_h, c-dependent completed residue weights, no AP-source lift, no centering/projection loss, and saving NaturalWFDScale/log^A(P).
```

| source | object | weights | window | moduli range | smoothing/projection | saving | constants | match | blocking gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BFI1986_Theorem10 | AP discrepancy for primes/arithmetic functions in residue classes | well-factorable modulus weights match only after AP-source formulation | large-moduli AP average, not full-S non-AP reciprocal window | strong AP range; object still AP | requires AP discrepancy and main-term subtraction | log-power AP saving is available inside its hypotheses | sufficient for AP branch only | `false` | APSourceLift is rejected for the current uncentered no-projection non-AP WFD object |
| DI_Kuznetsov_spectral_large_sieve | post-completion Kloosterman spectral average | given coefficient vectors, not actual source emitter | phase/modulus/frequency template is close | spectral level can cover KLS-style averages after completion | completion/projection must already be justified | large-sieve saving exists for matched completed forms | not yet transferred to arbitrary log^A full-S target | `false` | c-dependent completed residue weights and no-projection de-completion are not a ready-made corollary |
| Maynard2020_and_2023_large_moduli_AP | AP distribution with well/triply-well-factorable weights | very strong AP well-factorable weights | AP moduli beyond square-root barrier, not every sqrt row window | improves AP level of distribution | AP-source and residue-class framework | AP mean-value saving | does not provide full-S non-AP KLS conclusion | `false` | conclusion type remains AP distribution, not uncentered non-AP full-S WFD KLS |
| Friedlander_Iwaniec_parity_sensitive_model | special polynomial/parity-breaking sieve technology | conceptual Type-II/parity-sensitive guidance | not the current CRT row top band | not a theorem for the current W_full | not applicable as a direct projection | not a ready estimate for W_full | technology-class only | `false` | model inspiration, not a theorem-match for full-S non-AP WFD |
| NewAutomorphicDispersionProof | exact W_full full-S non-AP WFD target | must handle c-dependent completed residue weights | must cover C≈P/log^O(P), S≈P, H<=P/log^O(P) | prime-matrix top band P^2/sqrt-scale | must preserve no hidden projection and de-completion errors | must prove NaturalWFDScale/log^A(P) for every fixed A | must survive downstream log-loss ledger | `true` | not proved yet; this is the exact new theorem to write |

新自守/dispersion 证明必须补齐：

| task | closed | detail |
| --- | --- | --- |
| CompletionWithoutProjectionLoss | `false` | 把 actual full-S non-AP 对象完成到 Kloosterman 相位，同时证明中心化/投影误差不吞掉目标 log saving。 |
| CDependentWeightSpectralLargeSieve | `false` | 证明 c-dependent completed residue weights 的 Kuznetsov/谱大筛平均抵消，而不是套用固定系数模板。 |
| WellFactorableModulusTransferNonAP | `false` | 保持 well-factorable 模权，但不退回 APSourceLift 或 AP discrepancy。 |
| DecompletionAndEndpointErrorBudget | `false` | 把完成型估计回传到原始 uncentered full-S 窗口，保存所有端点、粗糙截断和 CRT 误差。 |
| ArbitraryLogSavingConstants | `false` | 给出任意固定 A 的 log^{-A} 节省，并记录足以穿过后续 loss ledger 的常数强度。 |

## 3. 内部自足线

DStructure/Rankin 自足替代包的最窄解析原子：

```text
SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving
```

精确定理目标：

```text
For prime modulus P and dyadic reciprocal variables m,n with divisor-bounded Vaughan/RKS coefficients and |I||J|>=P/log^A(P), prove a BG/RKS-type bilinear or multilinear reciprocal Kloosterman fixed log-saving for e_P(xi/(mn)), strong enough to leave the prior log^-44 budget after RKS losses; equivalently supply the log^-118 block used by the ledger.
```

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FineSignedSourcePackage | `false` | `false` | 内部自足版仍需同一 formal unit 的 pre-Cauchy signed emitter 与 Phi-LPF signed tables。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| DStructureFormalShell | `true` | `true` | D/AB Structured-EHPD 壳、有限验证和 Rankin pass-or-return 已可作为作者侧证据包处理。 | analytic TL4-L/RKS-log core |
| SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving | `false` | `false` | DStructure/Rankin 自足替代包的真正解析硬点已压到 BG/RKS-log 倒数 Kloosterman 固定对数节省。 | SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| BakerSingleFrequencyShortcut | `true` | `false` | Baker 单频率素变量估计对象不同，不能替代 coherent d/frequency average。 | prove averaged reciprocal Kloosterman theorem, not just pointwise prime-variable bound |
| InternalSelfContainedRowColumnClosure | `false` | `false` | 内部自足版必须同时关闭 source signed package 与 RKS-log/TL4-L 固定节省；当前没有无条件闭合。 | FineSignedSourcePackage AND SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving |

FineSignedSourcePackage 展开：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

## 4. 状态快照

| field | value |
| --- | --- |
| `dual_closure_status` | `dual_closure_split_external_conditional_closed_internal_self_contained_open` |
| `theorem_match_status` | `fulls_nonap_wfd_primary_sources_screened_exact_contract_or_new_theorem_remains` |
| `true_remainder_status` | `ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open` |
| `dstructure_split_status` | `dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open` |
| `rks_compressed_status` | `self_contained_replacement_package_compressed_to_rks_log_reciprocal_kloosterman_core` |
| `rks_hardpoint_status` | `self_contained_replacement_package_reduced_to_tail_log4_rks_log_hardpoint` |
| `strict_mainline_status` | `strict_mainline_frontier_synced_open_not_unconditionally_closed` |

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `3b33d11d81030641c6ed3db3b28a4238c16d8c2c0bcb8681ca181fde1f59d1c3` |
| `docs/monograph/external-theorem-index.md` | `e7b7ae2ddad7bb8fea47a2d73d7a4b94cd9b802a66b7b5a9f672087bf7cedf18` |
| `docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json` | `76b64234307bf057c865b20478520022f755d4232dd99462a57e4bcc2d9421d2` |
| `docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.json` | `6a25a769df2b107f8a5a31e1374395d99717c4d0dd8188c969111477a648de7a` |
| `docs/monograph/prime-matrix-dual-closure-external-internal-hardpoint-router.json` | `5095631438e220314abc03c41253a9fafd7e5a8f239d5ae414fc99f02e7e8034` |
| `docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json` | `4f9aa4016fbbf8d51f98c595772ce5fae1d2c224deb27047f719305ffa1e4f01` |
| `docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json` | `753b5bd82e01a073b1d62807aec81ef84c89f4bde4ce388d37c6d042040f5dff` |
| `docs/monograph/prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.json` | `10f6be174685f161f994d54befcb38711ddbf19fccc2482331a90ceb256e1097` |
| `docs/monograph/prime-matrix-strict-mainline-self-contained-frontier-router.json` | `37ea060dc254202c9af7688083a52d1b51f1909fa8fdfb6a4238fdf07364eb39` |
| `docs/monograph/prime-matrix-strict-self-contained-replacement-package-hardpoint-router.json` | `30d6ca23c9e10b65784dd3b81cf5b7b1c7073e825e4e9283779c04d13952146b` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `8f949e9316b555a4a70c6490f97c350b733af6b5cc6725e6e1c15b34c5030613` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `3fc6a7b503db4887155acdb5ea3c280589b5fb40d0eff6d2937c17b1a11aedc4` |
| `experiments/prime_matrix_two_replacement_lines_terminal_attack_router.py` | `b49b3ec7da30b15a65970bf97dcf014f59d610f9a877af8267a0515fd22edb66` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `f279dd1de03f5c3f31d00849383e1bc5a96f8e6e6dde628acf65ffd505e9b94e` |
