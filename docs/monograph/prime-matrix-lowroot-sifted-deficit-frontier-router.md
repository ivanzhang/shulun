# Prime Matrix low-root 筛余缺口前沿证书

**状态：** `lowroot_deficit_reduced_to_short_interval_rough_residue_lower_bound_open`

`UniformLowRootSiftedResidueDeficitAfterNearRootSlots` 被进一步拆解：近根槽的来源与容量可以初等控制，真正缺口是长度 P、筛到 sqrt(kP) 的指定相位短区间 rough-residue 正下界。Mertens 密度只给启发，不能替代逐行下界；否则会把目标行命题循环写回自身。若该下界暂不能证明，必须转攻 Q1/Q2 CRT 传输的短复现/登记缺陷，或给循环外 seed/PDEC 输入。

```text
exact_deficit_identity_closed=true
near_root_slot_upper_bound_elementary=true
mertens_heuristic_not_proof=true
jacobsthal_barrier_identified=true
noncircular_short_interval_rough_residue_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 精确等价

在 `I_k={kP+a:1<=a<P}` 中，`kP+a<P^2`。因此若某个槽没有被任何
`q<=sqrt(kP+P-1)` 覆盖，它不可能是合数，只能是素数。于是：

```text
full_uncovered_slots > 0  <=>  row contains a prime.
```

这说明 low-root 缺口目标非常锋利：它不是辅助弱估计，而是行命题的核心等价形式。

## 2. 近根槽

近根槽只来自

```text
sqrt(kP) < q <= sqrt(kP+P-1).
```

每个这样的 `q` 在 row 内只给一个 residue class，容量有初等上界；它不是主要未知。
主要未知是低根覆盖后仍能保留多少 rough residue。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LowRootDeficitTargetImported | `true` | `false` | 上一层把具体零行模型压到低根筛余扣除近根槽后的统一正缺口。 | UniformLowRootSiftedResidueDeficitAfterNearRootSlots |
| ExactDeficitIdentityClosed | `true` | `true` | 对 1<=a<P，未被 q<=sqrt(kP+P-1) 覆盖的槽等价于 kP+a 为素数。 | full_uncovered_slots equals row prime slots |
| NearRootSlotUpperBoundElementary | `true` | `true` | 近根素数只在 sqrt(kP)<q<=sqrt(kP+P-1) 中出现；每个 q 只给一个 residue class，容量有初等上界。 | NearRootSemiprimeSlotCapacityUpperBound |
| RawCapacityStillIrrelevant | `true` | `true` | 低根 raw capacity 带重数大并不推出覆盖；反过来容量大也不构成矛盾。 | need sifted residue lower bound, not raw capacity |
| MertensHeuristicNotProof | `true` | `true` | Mertens 密度预测给出约 P/log(kP) 个筛余槽，但短区间逐行下界不能由平均密度替代。 | NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP |
| JacobsthalBarrierIdentified | `true` | `false` | 要无条件排除零行，需要证明长度 P 的指定相位短区间不能被低根 residue classes 与近根槽完全覆盖。 | NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP |
| Q1Q2TransportParallelStillNeeded | `true` | `false` | 若低根筛余下界无法直接给出，必须从相邻素数 Q1/Q2 的 CRT 传输中逼出短复现或登记缺陷。 | AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn |
| LowRootDeficitCurrentCorpusProved | `false` | `false` | 当前材料没有给出统一短区间 rough-residue 下界；样本正缺口不能替代证明。 | NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP |
| RowColumnUnconditionalClosureReached | `false` | `false` | 近根容量上界和精确等价已闭合，但核心 low-root 筛余下界仍未证明。 | (NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP OR AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新非循环基

```text
(NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP OR AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP
```

## 5. 诚实边界

- 本证书不把 Mertens 平均密度当作短区间逐行证明。
- 本证书不证明 row-gap 不存在；它把剩余压到短区间 rough-residue 正下界或 Q1/Q2 传输矛盾。
- 若直接证明 rough-residue 下界失败，必须从相位传输、seed cycle-cut 或 PDEC 作用域匹配破环。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json` | `6b5c87084ccd8da64c98664cffddfec39cb616129b00181d3694d998510f184f` |
| `docs/monograph/prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json` | `960a954eca848fa45c0ebb0c0086357477c058bbaf7dc4a3f966117c8c03ce21` |
| `docs/monograph/prime-matrix-strict-named-return-exclusion-compression-router.json` | `7e54f4f456a2108e28a8100a147c9491951f9367c633dd51972e908291d127c2` |
| `docs/monograph/prime-matrix-strict-stable-short-return-defect-attack-router.json` | `9ea657166a3e558e8e04b65bba186479e36d6f938b964d7fc17910f9dcb97aea` |
| `experiments/prime_matrix_lowroot_sifted_deficit_frontier_router.py` | `4b19a94eb274154bc622daca4843e9ed80da519781a9eace464679bc31cc924f` |
