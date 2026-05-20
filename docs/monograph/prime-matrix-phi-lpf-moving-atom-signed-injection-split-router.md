# Prime Matrix Phi-LPF moving-atom signed-injection split 证书

**状态：** `phi_lpf_moving_atom_signed_injection_split_to_pointwise_table_open`

本步继续拆解 `LPFMovingAtomSignedPreimageMassInjectionLedger`。上一层已经把 moving atom 的无符号前像固定到 LPF-owned source buckets；因此 signed 注入本身没有新的计数自由度。若逐点推前前 same-(u,v) signed sum identity 已给出，则大原子到某一正/负 sign-lane 的半质量抽取是有限线性代数。当前真正缺口是正向提交逐点 Phi-LPF signed value table 或完整 bucket signed law，并配合同一 formal unit 的 signed survival 与 row-mass/no-heavy-row 账本。最新直接主攻同步为 `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`；行/列命题仍未无条件闭合。

```text
lpf_preimage_partition_imported=true
signed_injection_has_no_unsigned_remainder=true
half_mass_sign_lane_extraction_finite_algebra_closed=true
prepushforward_same_uv_identity_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
signed_survival_and_row_mass_proved=false
signed_injection_ledger_current_corpus_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

## 1. 有限 sign-lane 抽取

若某个 final same-(u,v) atom 满足 `|sum_{e in F} w_e| >= T`，则在已知逐点推前前恒等式的条件下，
正 lane 或负 lane 至少一个承担 `>= T/2` 的绝对质量。该步不需要新的筛计数；缺失的是 `w_e` 的逐点来源表。

## 2. 同步链

| from | to | meaning |
| --- | --- | --- |
| `LPFMovingAtomSignedPreimageMassInjectionLedger` | `PhiLPFMovingAtomPrepushforwardSameUVSignedSumIdentity AND LPFMovingAtomHalfMassSignLaneExtractionLemma` | signed 注入由逐点推前前恒等式加有限 sign-lane 半质量抽取组成。 |
| `PhiLPFMovingAtomPrepushforwardSameUVSignedSumIdentity` | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PhiLPFBucketSignedCoefficientLawBeforePushforward` | same-(u,v) 推前前恒等式必须由逐点 signed 表或完整 bucket signed law 正向给出。 |
| `LPFMovingAtomHalfMassSignLaneExtractionLemma` | `closed finite algebra after identity` | 一旦恒等式给出，\|sum w_e\| 大迫使某一 sign-lane 至少承担一半绝对质量。 |
| `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PhiLPFBucketSignedCoefficientLawBeforePushforward` | `NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger` | signed 值表还必须配合同 formal unit 非零存活、总质量和 no-heavy-row/L2。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LPFPreimagePartitionImported | `true` | `true` | 上一层已删除无主/prime-row 前像，moving atom 若存在必须有 LPF-owned source-bucket 前像。 | LPFMovingAtomSignedPreimageMassInjectionLedger |
| SignedInjectionHasNoUnsignedRemainder | `true` | `true` | signed 注入不再包含新的计数问题；无符号桶容量已支付，剩余全是 signed value、prepushforward identity 与质量归一化字段。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| HalfMassSignLaneExtractionFiniteAlgebra | `true` | `true` | 若 exact prepushforward same-(u,v) signed sum identity 已给出，\|sum w_e\|>=T 立即推出正/负某一 sign-lane 的绝对质量至少 T/2。 | PhiLPFMovingAtomPrepushforwardSameUVSignedSumIdentity |
| PrepushforwardSameUVIdentityCurrentCorpusProved | `false` | `false` | 当前语料没有给出每个 LPF bucket signed coefficient 到 final same-(u,v) atom 的逐点推前前恒等式。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PhiLPFBucketSignedCoefficientLawBeforePushforward |
| PointwiseSignedValueTableStillOpen | `true` | `false` | 逐点 Phi-LPF signed 表仍是直接非循环替代；沿现有来源链展开会回到 signed-source 固定点。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| SignedSurvivalAndRowMassStillOpen | `true` | `false` | 即使逐点表存在，还需证明足够多非零 signed rows、同 formal unit 总质量和 no-heavy-row/L2。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| OriginTableSyncImportedButNotProof | `true` | `false` | signed-survival/origin-table 同步说明该缺口会回到 primitive summand signed expression，而不是自动闭合。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| RatePacketStillParallel | `true` | `false` | 若 signed 注入走终端包路线，仍需 PDEC/CleanKLS 速率包、高段模型余量和 RatePreservation。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet |
| SignedInjectionLedgerCurrentCorpusProved | `false` | `false` | 本层只把 signed 注入拆成逐点表/推前恒等式、半质量 sign-lane 和 row-mass；没有排斥 moving atom。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不是三目标命题无条件闭合。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. strict 基

```text
(PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 最新保留基

```text
((PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PhiLPFBucketSignedCoefficientLawBeforePushforward OR ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet)
```

下一直接主攻：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

并行主攻：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
HighSegmentModelGapAlpha043C3AnalyticLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_moving_atom_signed_injection_split_router.py` | `da178e1daf29235c9fbf8d35729d52d7150fedc41fa2b4c676670e6edc9ddcee` |
| `docs/monograph/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json` | `1ece66b081f2c9870f908717c2a97ba5e897c363694c789c69519782a821dbeb` |
| `docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json` | `65fb8bbd578b7dcc32c930fc86e8ea9b803d59b4d5773c589c44cfec90027e58` |
| `docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.json` | `073edf36be5e26306930db964a9a7920916efc6af78c1fb034a4a34f804189f7` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json` | `2a1b6082621d0c9d8ddd1acfa69d12f9c3f3a38cebe422ba3d14b196661b5a30` |
| `docs/monograph/prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json` | `f5135c99d7f964b3c5b29b81681512083ff8bcaca431ff71fda3f2606fa81b9a` |
