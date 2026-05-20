# Prime Matrix Phi-LPF source entropy signed-survival 证书

**状态：** `phi_lpf_candidate_capacity_closed_signed_survival_open`

本步把 source-domain entropy 中的 primitive row support 下界切成两层：LPF/Phi 递推已经关闭无符号候选 row 容量，但候选 row 不是 actual signed row。要把候选容量变成源域绝对熵，仍需证明 Phi-LPF 支撑上足够多行获得非零 signed weight，并给出同一 formal unit 的 row-mass/no-heavy-row 账本。最新直接硬点因此压到 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`；行/列命题仍未无条件闭合。

```text
phi_lpf_candidate_capacity_ledger_closed=true
lpf_candidate_row_map_closed=true
candidate_capacity_audit_closed=true
candidate_rows_are_actual_signed_rows=false
nonzero_signed_row_survival_proved=false
actual_noncanonical_primitive_summand_signed_weight_expression_proved=false
same_formal_unit_row_mass_normalization_proved=false
source_domain_absolute_entropy_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

## 1. 支撑切分

切分前：

```text
PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
```

切分后：

```text
PhiLPFCandidateRowCapacityLowerBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

| atom | status | role |
| --- | --- | --- |
| `PhiLPFCandidateRowCapacityLowerBoundLedger` | `closed_unsigned` | 由 LPF 唯一 ownership 与 Phi 递推支付候选 row 容量；只说明可发射位置有多少。 |
| `NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward` | `open_signed` | 证明足够多候选 row 在同一 formal unit 中获得非零 signed weight，且没有局部因子归零或命名回流。 |
| `SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger` | `open_signed` | 在存活 signed rows 上证明总质量、单行上界、L2/no-heavy-row 与零权重回流。 |
| `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` | `open_formula` | 给出每条 actual noncanonical primitive summand 的推前前 signed coefficient 表达式。 |

## 2. Phi-LPF 候选容量样本

| N | sqrt floor | Phi-LPF candidate rows | composites | pi from Phi | pi(N) | capacity identity | actual nonzero signed rows known |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 10 | 3 | 5 | 5 | 4 | 4 | `true` | `false` |
| 30 | 5 | 19 | 19 | 10 | 10 | `true` | `false` |
| 100 | 10 | 74 | 74 | 25 | 25 | `true` | `false` |
| 997 | 31 | 828 | 828 | 168 | 168 | `true` | `false` |
| 5003 | 70 | 4332 | 4332 | 670 | 670 | `true` | `false` |
| 10000 | 100 | 8770 | 8770 | 1229 | 1229 | `true` | `false` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SourceEntropyAtomImported` | `true` | `false` | source-domain entropy 已被拆成 signed row emitter、row-mass normalization 与 primitive row support 下界。 | ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger |
| `PhiRecursiveLPFOwnershipImported` | `true` | `true` | LPF/Phi 桶恒等式已闭合：每个候选合数 row 有唯一 LPF owner，桶容量由 Phi(floor(N/p),p)-1 给出。 | PhiLPFCandidateRowCapacityLowerBoundLedger |
| `LPFCandidateRowMapImported` | `true` | `true` | LPF ownership 已支付 alpha 侧候选 row 的非后验索引，并与 unsigned skeleton 兼容。 | PhiLPFCandidateRowCapacityLowerBoundLedger |
| `CandidateCapacityAuditClosed` | `true` | `true` | 样本审计只验证 Phi-LPF 候选容量恒等式；它不是全局 signed 支撑证明。 | PhiLPFCandidateRowCapacityLowerBoundLedger |
| `CandidateRowsAreNotActualSignedRows` | `true` | `true` | 候选 row 只有 owner/capacity/geometry，没有 signed weight、local factor、orientation 或 alpha/delta side。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward |
| `SeedEmitterStillNeedsSignedLaw` | `true` | `false` | 合法 seed 分支仍需逐 primitive row 的 signed coefficient law，才能把候选 row 转成 actual signed row。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `SignedExpressionStillOpen` | `true` | `false` | 逐行 signed weight formula 的最窄点是 actual primitive summand signed expression before pushforward。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `RowSupportSplitClosed` | `true` | `false` | primitive row support 下界可分成已闭合的候选容量与仍开放的非零 signed survival。 | PhiLPFCandidateRowCapacityLowerBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward |
| `RowMassStillIndependent` | `true` | `false` | 即使 signed rows 存活，仍需同一表内 row-mass normalization/no-heavy-row 账本。 | SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| `NewPayloadBridgeConsistent` | `true` | `false` | 上一层 new-payload 桥接把首攻点压到 source-domain absolute entropy，本步给出其 LPF/Phi 支撑切分。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger |
| `PointwisePhiLPFTableStillAlternative` | `true` | `false` | 若不走 signed summand 表达式，只能提交逐点 Phi-LPF signed coefficient value table。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭无符号候选容量和 signed-survival 的边界，不证明 signed 表达式、row-mass、complete key、fixed-key multiplicity 或最终晋级门。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |

## 4. 最新保留基

```text
(ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate; parallel: CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

并行出口：

```text
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_source_entropy_signed_survival_router.py` | `456c47c2f1670aa464e3667b4507faf7a71363410508f0f3572f06f6151ceb00` |
| `docs/monograph/prime-matrix-strict-actual-source-domain-entropy-atom-router.json` | `0eaacb65ce36ad81475e8fb8806bdd90570f24939b224d6f59c38262cf2374a9` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
| `docs/monograph/prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json` | `11dc103e15a970f0c4e27a17ca32b757203b5e4fd443d6d40217854fdb5f0fe3` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json` | `fb392c7ecb2613c000b1c8696ff285c12cb91c815a08dad700e24c21fec6b66f` |
| `docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.json` | `1ab5e411f776ad878828c88627d7907ea6baf4b4be687daacee76977a993bde3` |
