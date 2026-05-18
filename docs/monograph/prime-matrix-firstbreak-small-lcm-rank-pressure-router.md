# Prime Matrix 首破裂 small-LCM rank-pressure 压缩证书

**状态：** `firstbreak_small_lcm_reduced_to_low_carrier_or_rank_deficit_open`

首破裂 small-LCM 分支已被压成 rank-pressure 三分：固定 carrier 标签集满足 L=prod Lambda<=H=P-y，故任意阈值 B 以上的独立 carrier 数最多为 floor(log H/log B)，特别是两个大于 sqrt(H) 的 carrier 不可能同处一个 fixed small-LCM formal unit。因此小 LCM 若要承担反例压力，必须由低 carrier 固定 residue 复用、非持久稀疏 SAE，或高 carrier 低秩容量缺口来解释。

```text
distinct_prime_product_law_closed=true
small_lcm_rank_pressure_closed=true
two_large_carrier_sqrt_barrier_closed=true
small_lcm_branch_excluded=false
row_column_unconditional_closed=false
```

## 1. Rank-pressure 引理

在首破裂 fixed small-LCM 分支中，必须有 `H=P-y>=1`；若 `y=P`，则没有后续非零复现步长，
该分支直接回到 square-anchor/SAE 边界。活动 carrier 标签集 `Lambda` 由互异素数构成，且

```text
L = lcm(Lambda) = product_{q in Lambda} q <= H = P-y.
```

对任意阈值 `B>1`，若 `Lambda_>B={q in Lambda:q>B}`，则

```text
B^|Lambda_>B| < product_{q in Lambda_>B} q <= L <= H,
```

所以

```text
|Lambda_>B| <= floor(log H / log B).
```

取 `B=sqrt(H)` 得到最尖锐的局部结论：两个 `q>sqrt(H)` 的 carrier 不可能同时出现在同一个 fixed small-LCM formal unit 中。

## 2. 三分出口

小 LCM 分支因此不再是宽口径 ColumnCRT 标签，而被分成：

```text
SmallLCMColumnCRTPDECExclusion
  -> LowCarrierFixedResidueColumnCRTPDECExclusion
  AND LowCarrierNonpersistentSparseSAESummability
  AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE
```

- 低 carrier 固定 residue：若 `q<=B` 的低 carrier 持久承担压力，同一 `q/residue` 在 `H` 内反复出现，进入 ColumnCRT/PDEC。
- 低 carrier 非持久：若固定 residue 不持久，则不能形成稳定支付链，只能进入 sparse SAE/LocalSurvivor。
- 高 carrier 低秩：排除低 carrier 后，高 carrier 独立秩被 `log H/log B` 控制；若仍要覆盖反例压力，必须证明低秩容量不足或退化为 singleton SAE。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SmallLCMBranchImported | `true` | `false` | 上一层把首破裂终端拆成 small-LCM、nonreplay sparse SAE、moving-carrier 三项。 | SmallLCMColumnCRTPDECExclusion |
| PositiveReplayWidthGuardClosed | `true` | `true` | fixed small-LCM replay 只有在 H=P-y>=1 时才有非零步长；若 y=P，则没有后续复现行，回到 square-anchor/SAE 边界。 | H>=1 for this branch |
| DistinctPrimeProductLawClosed | `true` | `true` | 首破裂固定 carrier 标签是互异素数时，L=lcm(Lambda)=prod_{q in Lambda} q。 | none for formula |
| SmallLCMRankPressureClosed | `true` | `true` | 小 LCM 分支满足 prod Lambda=L<=H=P-y；因此任意阈值 B 下，q>B 的 carrier 数至多 floor(log H/log B)。 | rank_{>B} <= floor(log H/log B) |
| TwoLargeCarrierSqrtBarrierClosed | `true` | `true` | 特别地，两个 q>sqrt(H) 的 carrier 不能同时出现在同一固定 small-LCM formal unit 中。 | HighCarrierRankDeficitCapacityBoundOrSingletonSAE |
| ShortWindowLCMDisciplineImported | `true` | `true` | 仓库已有 LCM 乘子纪律：不能制造 LCM 爆炸的高密度对象必须产生共同核/固定 residue 复现。 | LowCarrierFixedResidueColumnCRTPDECExclusion |
| LowCarrierFixedResidueRouteRegistered | `true` | `true` | 若小 LCM 压力由 q<=B 的低 carrier 承担，则同一 q/residue 在 H 内反复出现；持久时是 ColumnCRT/PDEC。 | LowCarrierFixedResidueColumnCRTPDECExclusion |
| LowCarrierNonpersistentSparseRouteRegistered | `true` | `true` | 若低 carrier 不持久复用固定 residue，则不能形成稳定支付链，只能作为 sparse SAE/LocalSurvivor 计费。 | LowCarrierNonpersistentSparseSAESummability |
| HighCarrierRankDeficitRouteRegistered | `true` | `false` | 排除低 carrier 后，高 carrier rank 被 log H/log B 控制；若仍要覆盖反例压力，必须证明低秩容量不足或退化为 singleton SAE。 | HighCarrierRankDeficitCapacityBoundOrSingletonSAE |
| SmallLCMBranchReduced | `true` | `false` | 抽象 SmallLCMColumnCRTPDECExclusion 被压成低 carrier 固定 residue、低 carrier 稀疏 SAE、高 carrier rank deficit 三项。 | LowCarrierFixedResidueColumnCRTPDECExclusion AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE |
| SmallLCMBranchExcluded | `false` | `false` | 本步没有排斥三项终端，只关闭了 small-LCM 的 rank-pressure 结构。 | LowCarrierFixedResidueColumnCRTPDECExclusion AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、小 LCM 三项、nonreplay SAE、moving carrier 与并行 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND LowCarrierFixedResidueColumnCRTPDECExclusion AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 4. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND LowCarrierFixedResidueColumnCRTPDECExclusion AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND LowCarrierFixedResidueColumnCRTPDECExclusion AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 诚实边界

- 本证书不证明 small-LCM 分支不存在。
- 本证书只证明小 LCM 强制 carrier rank 受限，并把持续压力压入低 carrier 复用、稀疏 SAE 或高 carrier 低秩容量缺口。
- 三个终端排斥仍未完成，行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_small_lcm_rank_pressure_router.py` | `0546345213fdcce70b092b52e2b55299b5a6dbcc97e6cef788dad6b50cabc8f1` |
| `docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json` | `5bd12e6d5f2553e041f20f2b0c1b86ba145c05425b0aa89d973f7707ac4925e2` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md` | `6b1498eb0c46eb3302ed336a68c479b7f4f7bbff0b7b971d5b3fc05346d1707d` |
| `docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md` | `9974e8d739fa510a9fdd417a658dacb308326aad48a646cf3f9c361d3d295079` |
| `docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json` | `b38bc33611a384f5d925c2005c5e9df9cff5fee0af0b8bc5da4acc8bff88b681` |
| `docs/monograph/prime-matrix-early-zero-terminal-schema-reconciliation-router.json` | `a998f03b4bbb260f47b9b9978b1ff22995ff800329fc75f6faa48bb10a4d14e8` |
