# Prime Matrix 短区间 rough-residue 屏障路由证书

**状态：** `direct_rough_residue_route_classified_as_row_gap_strength_open`

`NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP` 被审查为平方根长度短区间素数存在性的同义屏障：扣除近根槽后的 rough-residue 正缺口为正，当且仅当对应 row 内已有素数。因此它不能作为自足非循环证明的内部黑箱；若不用外部短区间素数间隙输入，当前路线必须转到 Q1/Q2 CRT 传输缺陷、seed cycle-cut 或 same-set PDEC 作用域匹配。

```text
full_root_rough_equals_prime_in_row=true
near_root_subtraction_keeps_equivalence=true
mertens_average_insufficient=true
periodwide_jacobsthal_shortcut_rejected=true
noncircular_internal_use_rejected=true
noncircular_short_interval_rough_residue_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 精确屏障

令 `I_k={kP+a:1<=a<P}` 且 `1<=k<P`。对每个槽 `n=kP+a`，有

```text
n <= kP+P-1 < P^2.
```

若 `n` 是合数，则存在素因子 `q<=sqrt(n)<=sqrt(kP+P-1)`。反过来，若没有
这样的素因子覆盖该槽，则 `n` 只能是素数。因此

```text
#{a in [1,P-1] : kP+a is uncovered by all q<=sqrt(kP+P-1)} > 0
iff
I_k contains a prime.
```

这说明当前 rough-residue 下界已经不是松弛辅助量，而是行命题在筛语言中的精确版本。

## 2. 近根扣除

上一层的 low-root 表达式把 `q<=sqrt(kP)` 的覆盖和

```text
sqrt(kP)<q<=sqrt(kP+P-1)
```

的近根 only 槽分开。若记 `L` 为 low-root 未覆盖槽数，`N` 为近根 only 槽数，则

```text
full_root_uncovered = L - N.
```

所以要证明 `L-N>0`，仍然正是证明该行存在素数。近根容量上界是正确但不足的：核心不是容量，而是指定相位短区间逐点不能全覆盖。

## 3. 非循环判定

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RoughResidueTargetImported | `true` | `false` | 上一层把 low-root 缺口压到长度 P、筛到 sqrt(kP) 并扣除近根槽后的指定相位 rough-residue 正下界。 | NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP |
| FullRootRoughEqualsPrimeInRow | `true` | `true` | 在 k<P 且 1<=a<P 时，kP+a<P^2；若未被任何 q<=sqrt(kP+P-1) 覆盖，则 kP+a 只能是素数。 | full-root uncovered slot iff row prime slot |
| NearRootSubtractionKeepsEquivalence | `true` | `true` | low-root 未覆盖槽扣除近根 only 槽后的正缺口，正是 full-root 未覆盖槽正性，因此等价于该行有素数。 | low_uncovered_minus_near_root_only > 0 iff row contains a prime |
| MertensAverageInsufficient | `true` | `true` | Mertens 或 beta-sieve 平均密度只能给期望量；不能排除某个指定 CRT 相位长度 P 短区间被完全覆盖。 | pointwise short-interval lower bound still missing |
| PeriodWideJacobsthalShortcutRejected | `true` | `true` | 已有 primorial/Jacobsthal 审计显示全周期最长低筛覆盖块可超过 P；不能用周期全局最长块上界关闭特殊相位。 | must use special phase or transport/PDEC, not global Jacobsthal bound |
| DirectRoughLowerBoundIsRowGapStrength | `true` | `false` | 若无条件证明该 rough-residue 正下界，就已证明每个 I_k=(kP,kP+P) 有素数；这不是辅助引理，而是行命题本身的平方根长度素数间隙形态。 | ExactExternalSqrtLengthPrimeGapInput_FOR_ROW_GAP_ONLY |
| NonCircularInternalUseRejected | `true` | `true` | 在自足证明内把该下界当作已证输入会循环使用目标命题；只能登记为外部强输入或转攻非循环相位传输/seed/PDEC。 | AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步关闭 direct rough-residue 首攻的循环性审查，但没有给出全局无条件证明。 | (AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新内部非循环基

```text
(AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若接受外部平方根长度短区间素数间隙输入，可写为：

```text
(ExactExternalSqrtLengthPrimeGapInput_FOR_ROW_GAP_ONLY OR (AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate)) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

但该外部输入在本文中未被证明，也不能冒充自足闭合。

## 5. 下一直接主攻

```text
AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
```

并行保留：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

## 6. 诚实边界

- 本证书不证明 row-gap 不存在。
- 本证书不把 Mertens、平均 beta-sieve 密度、或有限样本当作逐行短区间证明。
- 本证书只删除一个循环首攻点：`NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP` 若直接使用，就是目标命题本身。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_short_interval_rough_residue_barrier_router.py` | `8891209fc94a8ae6c205f3bc1507f45df7eef9018cabd01ba96f125d89d08cf7` |
| `docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json` | `80ae10c28cd1700bb3e5fb1280198a2332468800f9ea8e306dd8d699a22716f6` |
| `docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json` | `6b5c87084ccd8da64c98664cffddfec39cb616129b00181d3694d998510f184f` |
| `docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json` | `ff08e13fd2dbbd7dbbdaf7a1648fc8f339cd2e52eec84a5ba3a0df7873c05d9c` |
| `docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.json` | `35ae489251780714fd8168bb39108b636a4882d967acd642f4c24a6a046fbcfb` |
| `docs/monograph/prime-matrix-square-phase-jacobsthal-special-phase-router.json` | `fa548f93b15f6961478bb8ecff06afab73694bea5daaec2aeefb741e4a4d34a3` |
