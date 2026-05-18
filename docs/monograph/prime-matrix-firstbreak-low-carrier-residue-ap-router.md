# Prime Matrix 首破裂低 carrier fixed-residue AP 骨架证书

**状态：** `firstbreak_low_carrier_fixed_residue_reduced_to_ap_table_pdec_open`

低 carrier 固定 residue 分支已被压成行向 AP 骨架：对固定 q 和列 residue a，覆盖相位强制行 t 落在唯一同余类 t≡-aP^{-1} mod q；因此在 H=P-y 的剩余行宽内，每个 residue cell 至多命中 ceil(H/q) 行。持续超出或正密度承担压力只能成为低维 residue table PDEC/ColumnCRT；非持久 cell 进入 sparse SAE。

```text
residue_to_row_ap_formula_closed=true
single_residue_ap_envelope_closed=true
low_carrier_residue_table_finite_closed=true
ap_envelope_capacity_comparison_proved=false
low_carrier_fixed_residue_excluded=false
row_column_unconditional_closed=false
```

## 1. AP 骨架引理

首破裂后行区间记为 `I_y={y,...,P-1}`，长度 `H=P-y`。对低 carrier 素数 `q<P` 和固定列 residue `a mod q`，覆盖条件为

```text
tP+c == 0 mod q,   c == a mod q.
```

因此

```text
tP == -a mod q.
```

由于 `(P,q)=1`，得到唯一行同余类

```text
t == -a P^{-1} mod q.
```

所以同一 `(q,a)` residue cell 在 `I_y` 中最多命中

```text
ceil(H/q)
```

个行位置。固定阈值 `B` 后，所有 `q<=B` 的低 carrier cell 数至多 `sum_{q<=B} q`，于是低 carrier fixed-residue 压力是一个低维 AP table 问题。

## 2. 三分出口

低 carrier fixed-residue 出口更新为：

```text
LowCarrierFixedResidueColumnCRTPDECExclusion
  -> LowCarrierResidueAPEnvelopeCapacityComparison
  AND DenseLowCarrierResidueTablePDECExclusion
  AND SparseLowCarrierResidueCellSAESummability
```

- AP envelope 容量比较：证明反例所需低 carrier 压力超过 AP table 可供给，或证明未超过时仍不足以支付零行。
- 稠密 residue table PDEC：若某些低维 cell 持久承担正密度压力或超出 envelope，则进入同 formal unit 的 ColumnCRT/PDEC。
- 稀疏 cell SAE：若 cell 不持久，只能作为 sparse SAE/LocalSurvivor 计费。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LowCarrierFixedResidueImported | `true` | `false` | 上一层把 small-LCM 的首个出口压到低 carrier 固定 residue 的 ColumnCRT/PDEC 排斥。 | LowCarrierFixedResidueColumnCRTPDECExclusion |
| ResidueToRowAPFormulaClosed | `true` | `true` | 固定 q 与列 residue a 时，覆盖条件 c≡a mod q 等价于行 t≡-a P^{-1} mod q。 | none for formula |
| SingleResidueAPEnvelopeClosed | `true` | `true` | 在 I_y={y,...,P-1}、H=P-y 中，同一 (q,a) residue cell 的行命中数至多 ceil(H/q)。 | cell_load <= ceil(H/q) |
| LowCarrierResidueTableFiniteClosed | `true` | `true` | 固定阈值 B 后，q<=B 的低 carrier residue cells 总数至多 sum_{q<=B} q，是低维有限表。 | finite low-carrier residue table |
| LowEffectiveModColumnCRTImport | `true` | `true` | 仓库已有低有效模路由：共同因子/低商模异常若持久，必须登记为 PDEC/ColumnCRT。 | DenseLowCarrierResidueTablePDECExclusion |
| PersistentResidueTableIsPDEC | `true` | `true` | 若某些低 carrier residue cells 持续超出 AP envelope 或承担正密度压力，它们构成同 formal unit 的低维 residue table PDEC。 | DenseLowCarrierResidueTablePDECExclusion |
| NonpersistentResidueCellsAreSparseSAE | `true` | `true` | 若低 carrier residue cells 不持久复现，则它们不能形成支付链，只能进入 sparse SAE/LocalSurvivor。 | SparseLowCarrierResidueCellSAESummability |
| APEnvelopeCapacityComparisonOpen | `false` | `false` | 尚未证明反例链所需低 carrier 压力必超过 AP envelope，或证明低于 envelope 时仍不足以支付零行。 | LowCarrierResidueAPEnvelopeCapacityComparison |
| LowCarrierFixedResidueReduced | `true` | `false` | 抽象低 carrier fixed-residue 出口被压成 AP envelope 容量比较、稠密 residue table PDEC、稀疏 cell SAE 三项。 | LowCarrierResidueAPEnvelopeCapacityComparison AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability |
| LowCarrierFixedResidueExcluded | `false` | `false` | 本步只给出 AP 骨架和命名分流，尚未排斥三项终端。 | LowCarrierResidueAPEnvelopeCapacityComparison AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、低 carrier 三项、其余 first-break 出口与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND LowCarrierResidueAPEnvelopeCapacityComparison AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 4. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND LowCarrierResidueAPEnvelopeCapacityComparison AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND LowCarrierResidueAPEnvelopeCapacityComparison AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 诚实边界

- 本证书不证明低 carrier fixed-residue 分支不存在。
- 本证书只把该分支压成 AP table 容量比较、稠密 residue table PDEC 与稀疏 cell SAE。
- 行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_low_carrier_residue_ap_router.py` | `30bbc15f97364d13c03955f015eab2430d394277f8497769d07bc23586ca924c` |
| `docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json` | `747ab2d8f1f4569ed1bd9e00f868e26f33a7a22c8310e0776580ee8ad571dad9` |
| `docs/monograph/prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json` | `ef556e92601ac57086ad79bb993ec476c0e2bb3de06277d50e450136cfa59c72` |
| `docs/monograph/prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json` | `9eef33defabab6ff2bddfd3627b5034984171d98db34e55d04cecee3b4d15f56` |
| `docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md` | `6b1498eb0c46eb3302ed336a68c479b7f4f7bbff0b7b971d5b3fc05346d1707d` |
| `docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json` | `b38bc33611a384f5d925c2005c5e9df9cff5fee0af0b8bc5da4acc8bff88b681` |
