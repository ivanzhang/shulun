# Prime Matrix row-gap 供需/相位 cycle-cut 审计证书

**状态：** `row_gap_supply_phase_reduced_to_lowroot_deficit_or_q1q2_transport_open`

本步把具体 row-gap 反例 I_k={kP+a:1<=a<P} 无素数的想法拆成可审查的供需/相位结构。正确供给律是每个合数有素因子 q<P；但不能把供给全部限制到 q<=sqrt(kP)，因为近根带 sqrt(kP)<q<=sqrt(kP+P-1) 会产生边缘半素数槽。原始容量总和通常不短缺，真正可攻点是低根筛余槽在扣除近根 only 槽后仍有正缺口，或者 Q1/Q2 相邻素数间隙在 CRT 传输中强制同 formal unit 短复现/登记缺陷。当前材料尚未证明这两个统一输入；因此本步把具体反例压到循环外 seed cycle-cut、direct PDEC 作用域匹配或外部 prime-gap/KZ 证书。

```text
row_gap_model_pinned=true
correct_divisor_supply_law=true
low_root_only_claim_rejected=true
capacity_only_contradiction_rejected=true
crt_period_mirror_not_contradiction=true
low_root_deficit_after_near_root_slots_proved=false
q1q2_transport_defect_or_stable_short_return_proved=false
row_column_unconditional_closed=false
```

## 1. 精确 row-gap 模型

设 `I_k={kP+a:1<=a<P}` 且 `1<=k<P`。若 `I_k` 无素数，则每个 `kP+a<P^2`
都有一个素因子 `q<P`。但可证明的根界是 `q<=sqrt(kP+a)<=sqrt(kP+P-1)`，
不是统一的 `q<=sqrt(kP)`。

因此必须拆成：

```text
low-root primes:      q <= floor(sqrt(kP))
near-root primes:     floor(sqrt(kP)) < q <= floor(sqrt(kP+P-1))
zero-row obligation:  low-root slots union near-root slots covers every a=1..P-1
```

## 2. 样本供需画像

| P | k | low bound | full bound | low union | near-root only | full uncovered | low uncovered - near-root only | actual primes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 4 | 4 | 4 | 3 | 0 | 1 | 1 | 1 |
| 7 | 6 | 6 | 6 | 4 | 0 | 2 | 2 | 2 |
| 101 | 50 | 71 | 71 | 89 | 0 | 11 | 11 | 11 |
| 101 | 100 | 100 | 100 | 88 | 0 | 12 | 12 | 12 |
| 1009 | 10 | 100 | 105 | 894 | 6 | 108 | 108 | 108 |
| 1009 | 900 | 952 | 953 | 923 | 1 | 84 | 84 | 84 |
| 1009 | 1008 | 1008 | 1008 | 938 | 0 | 70 | 70 | 70 |
| 10007 | 100 | 1000 | 1005 | 9268 | 0 | 738 | 738 | 738 |
| 10007 | 9000 | 9490 | 9490 | 9442 | 0 | 564 | 564 | 564 |

表中最后两列在样本中相同，反映精确事实：`full_uncovered_slots` 正是该行内的素数槽。
要把样本现象升级为证明，必须给出统一的低根筛余正缺口定理，而不能只引用样本。

## 3. Q1/Q2 相邻素数 CRT 审查

若零行成立且 `Q1<kP`、`Q2>(k+1)P` 是夹住该区间的相邻素数，则得到一个长度超过 `P` 的真实素数间隙。
在 CRT 周期中，这只说明一个被小素数 residue classes 覆盖的块存在；镜像对称会给出镜像覆盖块，
本身不是矛盾。要变成矛盾，必须额外证明：

```text
Q1/Q2 transport forces a stable same-formal-unit same-label short return
OR every instability is a registered PDEC/SAE/ColumnCRT defect.
```

这正是当前 `Q1Q2` 传输输入，而不是已经闭合的事实。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RowGapModelPinned | `true` | `true` | 固定奇素数 P 与 1<=k<P，审查内部行 I_k={kP+a:1<=a<P} 无素数的反例模型。 | zero row means every a is covered by a prime divisor < P |
| CorrectDivisorSupplyLaw | `true` | `true` | 若 kP+a 合数且 a<P，则 kP+a<P^2，所以它有一个素因子 q<P。 | small-prime cover by q<P |
| LowRootOnlyClaimRejected | `true` | `true` | 不能只用 q<=sqrt(kP)：近根带 sqrt(kP)<q<=sqrt(kP+P-1) 可能覆盖边缘半素数槽。 | split low-root supply and near-root slots |
| ExactCoverObligation | `true` | `false` | 零行等价于所有列槽被 q<=sqrt(kP+P-1) 的 residue classes 覆盖。 | prove full_uncovered_slots cannot be zero |
| CapacityOnlyContradictionRejected | `true` | `true` | 带重数 raw capacity 通常大于 P；单纯供给总量不矛盾，必须控制重叠、相位和筛余。 | UniformLowRootSiftedResidueDeficitAfterNearRootSlots |
| LowRootDeficitAfterNearRootSlotsOpen | `true` | `false` | 真正可攻的不等式是低根筛余槽数大于近根 only 槽容量，从而留下必为素数的槽。 | UniformLowRootSiftedResidueDeficitAfterNearRootSlots |
| AdjacentQ1Q2GapLawPinned | `true` | `false` | 若 Q1<kP 与 Q2>(k+1)P 是相邻素数，则得到长度超过 P 的真实素数间隙。 | prime-gap or CRT-transport input |
| CRTPeriodMirrorNotContradiction | `true` | `true` | CRT 周期镜像只把覆盖块送到镜像覆盖块；没有同标签短复现或登记缺陷时不产生矛盾。 | AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn |
| StableShortReturnImported | `true` | `false` | 若 Q1/Q2 传输强制同 formal unit 的短同标签复现，则可用 prod(Q)\|Delta 引理；尚未证明该强制。 | AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn |
| PostSourceAdmissionMacrocycleImported | `true` | `true` | 最新 A1/PDEC/KZ 宏循环已归档；row-gap 模型必须给循环外 primitive source 或 PDEC 作用域匹配。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步给出具体 row-gap 反例的精确供需/相位拆分，但没有证明统一筛余缺口或 Q1/Q2 传输矛盾。 | (UniformLowRootSiftedResidueDeficitAfterNearRootSlots OR AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactExternalPrimeGapSqrtBarrierCertificate_FOR_ROW_GAP_ONLY) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 最新非循环基

```text
(UniformLowRootSiftedResidueDeficitAfterNearRootSlots OR AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactExternalPrimeGapSqrtBarrierCertificate_FOR_ROW_GAP_ONLY) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
UniformLowRootSiftedResidueDeficitAfterNearRootSlots
```

## 6. 诚实边界

- 本证书修正了 `q<=sqrt(kP)` 的过强供给前提。
- 本证书不证明所有 row-gap 都不可能；它把该目标压到统一低根筛余缺口或 Q1/Q2 传输矛盾。
- CRT 镜像对称不是矛盾，除非能证明同 formal unit 的短稳定复现或命名缺陷排斥。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json` | `aef259753937f9d64167d4c7478a6ab2c410d2f1f9d9474fb0e876619b517a29` |
| `docs/monograph/prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json` | `960a954eca848fa45c0ebb0c0086357477c058bbaf7dc4a3f966117c8c03ce21` |
| `docs/monograph/prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json` | `7a72bed5901b1c6b5575db7161c23108f5f4fc17e1848d75cb00b20fd1e6c993` |
| `docs/monograph/prime-matrix-strict-named-return-exclusion-compression-router.json` | `7e54f4f456a2108e28a8100a147c9491951f9367c633dd51972e908291d127c2` |
| `docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.json` | `da9326ecac2e9c560da7b933d976ff50b88d16852626afbc84e127f6d8d97b4b` |
| `docs/monograph/prime-matrix-strict-stable-short-return-defect-attack-router.json` | `9ea657166a3e558e8e04b65bba186479e36d6f938b964d7fc17910f9dcb97aea` |
| `docs/monograph/prime-matrix-strict-terminal-defect-exhaustion-router.json` | `d7b8551217e0b50d171f2eefc7ce67996eff1da16abaa3eab68c4640595c9658` |
| `experiments/prime_matrix_row_gap_supply_phase_cycle_cut_router.py` | `320fe3118eaabd7c92f874d578c657a870502a4c4373f411e4c363329bf13912` |
