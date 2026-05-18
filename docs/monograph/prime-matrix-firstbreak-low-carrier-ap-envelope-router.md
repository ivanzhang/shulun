# Prime Matrix 首破裂低 carrier AP exact-envelope 证书

**状态：** `firstbreak_low_carrier_ap_exact_envelope_closed_demand_gap_open`

低 carrier AP envelope 已被精确化：任意 residue table T 的行发生量为 U_T(I)=sum_{(q,a) in T} N_{q,a}(I)，其中 N_{q,a}(I)<=ceil(H/q)；更尖锐地，固定 q 时 sum_a N_{q,a}(I)=H。因此容量比较的形式上界已闭合，真正剩余是证明反例链的 actual row-incidence demand 超过该 envelope，或把接近 envelope 的稠密低维 table 登记并排斥为 PDEC。

```text
cell_count_formula_closed=true
single_cell_sharp_bound_closed=true
all_residues_exact_mass_closed=true
selected_table_envelope_closed=true
ap_capacity_comparison_proved=false
row_column_unconditional_closed=false
```

## 1. Exact envelope

首破裂后行区间 `I_y` 长度为 `H=P-y`。对低 carrier residue table

```text
T subset {(q,a): q<=B, a mod q},
```

定义行发生量

```text
U_T(I_y)=sum_{(q,a) in T} #{t in I_y: t == -a P^{-1} mod q}.
```

单个 cell 满足

```text
#{t in I_y: t == -a P^{-1} mod q} <= ceil(H/q).
```

更尖锐的是，固定 `q` 时所有 residue cell 精确分割行区间：

```text
sum_{a mod q} #{t in I_y: t == -a P^{-1} mod q} = H.
```

因为每个行 `t` 对模 `q` 只选择一个 residue `a=-tP mod q`。所以任意 table 的安全 envelope 为

```text
U_T(I_y) <= sum_{(q,a) in T} ceil(H/q),
U_T(I_y) <= H * |{q: exists a with (q,a) in T}|.
```

## 2. 剩余真实容量接口

AP envelope 只是形式可供给上界。要把它升级为矛盾，还需要同一 formal unit 下的 actual 需求下界：

```text
ActualLowCarrierRowIncidenceDemandLowerBound
```

并证明该需求超过 exact envelope；若某个低维 table 接近 envelope，则它必须是稠密 residue table PDEC，而不是普通误差。

因此本硬点更新为：

```text
LowCarrierResidueAPEnvelopeCapacityComparison
  -> ActualLowCarrierRowIncidenceDemandLowerBound
  AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| APEnvelopeCapacityImported | `true` | `false` | 上一层把低 carrier fixed-residue 出口压到 AP envelope 容量比较。 | LowCarrierResidueAPEnvelopeCapacityComparison |
| CellCountFormulaClosed | `true` | `true` | 对任意 table T，U_T(I)=sum_{(q,a) in T} #{t in I:t≡-aP^{-1} mod q}。 | LowCarrierAPExactEnvelopeLedger |
| SingleCellSharpBoundClosed | `true` | `true` | 单个 (q,a) cell 的行发生数不超过 floor((H+q-1)/q)=ceil(H/q)。 | N_{q,a}(I)<=ceil(H/q) |
| AllResiduesExactMassClosed | `true` | `true` | 固定 q 时，所有 a mod q 的 cell 在 I_y 中的发生数精确求和为 H；每一行只选择一个 residue。 | sum_a N_{q,a}(I)=H |
| SelectedTableEnvelopeClosed | `true` | `true` | 任意选定低 carrier table T 的 envelope 为 U_T<=sum_{(q,a) in T} ceil(H/q)，且 U_T<=H*\|Q(T)\|。 | LowCarrierAPExactEnvelopeLedger |
| FormalEnvelopeNotActualDemandGuard | `true` | `true` | AP envelope 只是可供给上界；要形成矛盾还必须证明反例链强制的 actual row-incidence demand 超过该上界。 | ActualLowCarrierRowIncidenceDemandLowerBound |
| DenseTablePDECRouteRegistered | `true` | `true` | 若 table T 为了接近 envelope 必须在许多低 carrier residue 上持久占位，则它是同 formal unit 的稠密 residue table PDEC。 | DenseLowCarrierResidueTablePDECExclusion |
| SparseTableSAERouteRegistered | `true` | `true` | 若 T 稀疏或不持久，AP envelope 发生只进入 sparse cell SAE/LocalSurvivor，不形成稳定反例支付链。 | SparseLowCarrierResidueCellSAESummability |
| APCapacityComparisonReduced | `true` | `false` | 容量比较被拆成 exact envelope ledger、actual demand 下界、以及 envelope strict gap 或 dense-table PDEC。 | ActualLowCarrierRowIncidenceDemandLowerBound AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC |
| APCapacityComparisonProved | `false` | `false` | 本步不证明 actual demand 下界，也不排斥 dense table PDEC；只关闭 envelope 公式。 | ActualLowCarrierRowIncidenceDemandLowerBound AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、AP demand/gap、PDEC/SAE 终端与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ActualLowCarrierRowIncidenceDemandLowerBound AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 4. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ActualLowCarrierRowIncidenceDemandLowerBound AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ActualLowCarrierRowIncidenceDemandLowerBound AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 诚实边界

- 本证书不证明低 carrier AP 分支不存在。
- 本证书只关闭 AP table 的 exact envelope 公式。
- actual demand 下界、strict gap 和 dense-table PDEC 排斥仍未完成。
- 行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_low_carrier_ap_envelope_router.py` | `18de7a8692e0a1b94699f2a46c802bd442c0455e1b4751640de2b36bbf93e0c3` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.json` | `03248e0defb00a2419e713cb229d804f725d8c44e86a277d51a613abb5d6b94c` |
| `docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md` | `6b1498eb0c46eb3302ed336a68c479b7f4f7bbff0b7b971d5b3fc05346d1707d` |
| `docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md` | `9974e8d739fa510a9fdd417a658dacb308326aad48a646cf3f9c361d3d295079` |
| `docs/monograph/prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json` | `ef556e92601ac57086ad79bb993ec476c0e2bb3de06277d50e450136cfa59c72` |
| `docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json` | `b38bc33611a384f5d925c2005c5e9df9cff5fee0af0b8bc5da4acc8bff88b681` |
