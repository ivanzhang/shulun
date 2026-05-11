# Prime Matrix strict 反例链/真实结构链循环切断路由器

**状态：** `counterexample_true_structure_direct_contradiction_reduced_to_noncyclic_cut_inputs_open`

本步没有换命题，而是专门审查“早期零行反例链”与“真实结构刚性链”之间能否直接撞出矛盾。结论是：真正可立即产生矛盾的核心引理已经明确，即同一 formal unit 的同标签短复现会强制 `prod(Q)|Delta`，从而与 `0<|Delta|<prod(Q)` 矛盾；但当前尚未证明早期零行必强制这种短稳定复现，也尚未证明不稳定时必生成已排斥的 PDEC/SAE/ColumnCRT 相位缺陷。另一方面，pair-mass、direct PDEC/CleanKLS、canonical-lock 下游反推 source 都已识别为循环或作用域不匹配。故当前最窄非循环切口是 `StableShortSameLabelRecurrenceOrRegisteredPhaseDefect`，并列备用为 exact same-set canonical 晋级证书或完全独立的 actual-source 熵证明。行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
counterexample_assumption_only=true
short_same_label_recurrence_contradiction_lemma_proved=true
early_zero_forces_stable_short_return_or_defect_proved=false
terminal_recurrence_loop_cut=true
pair_mass_entropy_loop_cut=true
acyclic_canonical_exact_same_set_promotion_certificate_proved=false
independent_exact_pair_l2_or_max_atom_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 可立即闭合的短复现矛盾引理

设固定 P、行参数 n、列坐标 c 和同一 formal unit 的标签证书。若对素标签集 Q 中每个 q<P，同一列标签在行位移 Delta 后仍由同一个 q 解释，则 x_{n+Delta,c}-x_{n,c}=Delta*P 同时被 q 整除。因 gcd(P,q)=1，得 q|Delta。所以 prod(Q)|Delta。若 0<|Delta|<prod(Q)，则同标签短复现不可能。因此，一旦早期零行反例能强制同 formal unit 的短稳定复现，或在不稳定处强制登记相位缺陷，就会给出真正直接矛盾或进入可审查 PDEC/SAE/ColumnCRT 出口。

直接矛盾公式：

```text
EarlyZeroRowWithinP AND StableSameFormalUnitSameLabelReturn(Delta,Q) AND 0<|Delta|<prod(Q) => contradiction, because prod(Q)|Delta.
```

不稳定分支仍需证明：

```text
EarlyZeroRowWithinP AND NOT StableSameFormalUnitSameLabelReturn => RegisteredPhaseDefect(PDEC/SAE/ColumnCRT) is still open and must be proved.
```

## 2. 矛盾候选审查

| candidate | true structure | counterexample pressure | why not contradiction yet | needed cut |
| --- | --- | --- | --- | --- |
| `CRTMirrorVsEarlyRow` | 非平凡零行在完整 CRT 周期内关于中心镜像成对。 | 假设存在 P 行以内早期零行，镜像会给出同相位的远端伴随对象。 | 镜像把早期行送到周期远端，不自动给同一 formal unit 的短复现。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect |
| `PColumnLayeredWheelClamp` | P 列锚、圆柱斜线和层叠轮筛把候选覆盖压到固定相位字母表。 | 早期零行反例必须同时服从 carry-shell、anchor-collar 和 layered-wheel。 | 这些约束目前仍是 unsigned 支撑形状，不能直接产生 signed pre-Cauchy 源。 | AlphaFormulaSignedCoefficientLiftLedger OR AlphaSignedLiftFailureNamedReturnLedger |
| `SameLabelShortRecurrence` | 行位移 Delta 后，同列值对每个 q<P 的变化是 Delta*P，且 P 在 mod q 下可逆。 | 若同一 formal unit 的同标签覆盖证书短复现，则每个保持的素标签 q 都强制 q \| Delta。 | 短复现引理本身已闭合；未证的是早期零行一定强制这种稳定短复现或相位缺陷。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect |
| `CurrentPDECSparseFrontierZero` | 当前已物化 PDEC 与 sparse/LocalSurvivor 前沿为零。 | 反例链若不稳定，必须投射成低维相位缺陷或 sparse packet。 | 当前前沿为零只是当前语料实例清零，不是未来全局 family 不存在证明。 | TerminalLeafExclusionForAcyclicNoncanonicalFamily |
| `CanonicalSourceClosure` | canonical RIW/Buchstab 分支已有来源闭合和终端晋级材料。 | 若反例链实际是 canonical 同集推前，则可调用 canonical 范围闭合。 | 尚未提交 exact same-set promotion：pre-Cauchy 准入、有限因子图、同集推前、无 payload 残留。 | AcyclicCanonicalExactSameSetPromotionCertificate |
| `PairMassDispersion` | Cauchy/支撑能量引理可从独立 pair L2 或最大 pair 原子界推出支撑下界。 | 反例链若集中在 moving same-(u,v) 大原子，会与源熵反原子目标正面相撞。 | 当前没有不依赖源熵目标自身的独立 pair L2/max-atom 界。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |

## 3. 循环切断表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameTheoremAndCounterexampleDiscipline` | `true` | `true` | 本步只在假设 EarlyZeroRowWithinP 的反例链中工作，不用真实缺席或样本统计替代证明。 | 所有输出必须是反例链内的命名矛盾、命名回流或打开输入。 |
| `ActualMovingBlockUnnamedExitRemoved` | `true` | `true` | actual moving-block/NC-BLK 不能再作为独立无名出口。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `UnsignedGeometryAmplifierImported` | `true` | `true` | 早期零行反例已被 carry-shell、anchor-collar、P 列锚和 layered-wheel 放入同一真实结构压力场。 | AlphaFormulaSourceTupleToCarryShellVariableBindingLedger AND AlphaFormulaCarryShellCongruenceRowFormulaLedger AND AlphaFormulaPhaseWheelCompatibilityLedger AND AlphaFormulaSignedCoefficientLiftLedger AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger |
| `SignedSourceExtractionStillOpen` | `true` | `false` | 真实几何压力仍不能反推出 signed pre-Cauchy alpha source；signed lift 是活动缺口。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger |
| `ShortSameLabelRecurrenceContradictionLemma` | `true` | `true` | 若同一 formal unit 的同标签证书以 0<\|Delta\|<prod(Q) 短复现，且保持标签集 Q，则 q\|Delta 对全部 q in Q，矛盾。 | 必须证明早期零行强制短稳定同标签复现，或不稳定时强制登记相位缺陷。 |
| `EarlyZeroForcesStableShortReturnOrDefect` | `false` | `false` | 当前材料尚未证明早期零行反例一定产生同 formal unit 的短稳定复现，或产生可排斥 PDEC/SAE/ColumnCRT 相位缺陷。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect |
| `PairMassEntropyLoopCut` | `true` | `true` | pair-mass 分散不能用 moving-atom/source-entropy 目标自身证明，否则是回流。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `IndependentPairEnergyStillOpen` | `true` | `false` | 独立 pair 能量界已压成 rate-bearing 大 pair packet 排斥，但该排斥再走终端标签会回流。 | RateBearingLargePairAtomPacketExclusion |
| `DirectTerminalRouteRecurrenceCut` | `true` | `true` | direct PDEC/CleanKLS 终端标签链已识别为回到 canonical-lock 或原 actual-source 熵目标的循环。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `CanonicalLockReducedToExactSameSetCertificate` | `true` | `false` | canonical-lock 已压成 exact same-set 晋级证书；任一子账本缺失时不能调用 canonical 分支闭合。 | AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection |
| `TerminalDescentNotLeafExclusion` | `true` | `false` | 终端无隐藏循环下降 schema 已闭合，但叶子排斥没有证明；不能把下降当作最终矛盾。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `CurrentLeafZeroNotGlobalNonexistence` | `true` | `true` | 当前 PDEC/sparse 前沿为零只清理当前实例；未来 schema 是准入纪律，不是全局不存在定理。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `ActualSourceBridgeStillConcreteOpen` | `true` | `false` | actual-source 桥已具体化为 source admission 或 moving atom 排斥，但两者均未证明。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `DirectVisibleContradictionCurrentCorpusProved` | `false` | `false` | 反例链与真实结构链之间尚未得到无条件直接矛盾；当前得到的是最小非循环切口。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR AcyclicCanonicalExactSameSetPromotionCertificate OR NonrecursiveIndependentProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |

## 4. 当前非循环切口

```text
StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR AcyclicCanonicalExactSameSetPromotionCertificate OR NonrecursiveIndependentProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

首选下一硬攻点：

```text
StableShortSameLabelRecurrenceOrRegisteredPhaseDefect
```

备用硬攻点：

```text
AcyclicCanonicalPreCauchyCoefficientIdentityLedger OR IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

独立晋级门仍保留：

```text
SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
