# Prime Matrix strict canonical branch 准入时间线守门路由器

**状态：** `canonical_branch_admission_timeline_guard_closed_precauchy_identity_open`

本步直接攻击 `AcyclicSeedCanonicalBranchAdmissionBeforeCauchy`。结构结论是：canonical branch admission 是时间线门，而不是可由终端证书倒推的覆盖事实。若要走 canonical-lock，必须在 Cauchy/dispersion/terminal extraction 之前提交同一 formal unit 的 `AcyclicCanonicalPreCauchyCoefficientIdentityLedger`。现有早期零行几何、P 列锚、层叠筛、payment skeleton、PDEC/SAE 前沿和 formal-unit hash stability 都不能替代该 T1 身份账本。因此本轮关闭了准入时间线审查，但没有证明 canonical 准入，也没有得到反例链与真实链的无条件终端矛盾。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
canonical_branch_admission_timeline_guard_closed=true
timeline_admission_law_closed=true
downstream_recovery_rejected=true
acyclic_canonical_precauchy_coefficient_identity_ledger_proved=false
acyclic_seed_canonical_branch_admission_before_cauchy_proved=false
new_actual_source_entropy_theorem_proved=false
acyclic_windowed_kloosterman_dls_internal_estimate_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 时间线

| layer | name | allowed | forbidden |
| --- | --- | --- | --- |
| `T0` | CRT wheel and early-zero hypothesis | 只给位置、同余斜线、镜像和覆盖压力。 | 不能直接声明 signed canonical coefficient。 |
| `T1` | pre-Cauchy coefficient declaration | 必须在这里声明 RIW/Buchstab canonical 系数恒等式、formal unit 和 branch key。 | 不得依赖 Cauchy 选择、terminal payment、PDEC 缺陷或后验投影。 |
| `T2` | Cauchy / dispersion / Type-Fourier processing | 只处理已经登记的 T1 系数。 | 不能在处理后补造 T1 来源。 |
| `T3` | terminal extraction and payment skeleton | 可登记缺陷、same-set 推前和容量比较。 | 不能反向生成 canonical branch admission。 |
| `T4` | PDEC / SAE / ColumnCRT / CleanKLS returns | 作为命名回流或外部/内部估计分支。 | 不能冒充 pre-Cauchy canonical source。 |

## 2. 收缩公式

攻击前：

```text
AcyclicSeedCanonicalBranchAdmissionBeforeCauchy
```

攻击后：

```text
AcyclicCanonicalPreCauchyCoefficientIdentityLedger OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem OR AcyclicWindowedKloostermanDLSInternalEstimate
```

## 3. 必要 T1 账本字段

- `same formal_unit_id fixed before Cauchy/dispersion`
- `canonical RIW/Buchstab coefficient formula declared before terminal payment`
- `branch key independent of downstream PDEC/SAE/ColumnCRT outcomes`
- `weight/sign law equal to canonical source law, not merely hash-stable`
- `bad-window set and same-set pushforward consume the T1 source without changing it`

## 4. 被排除的证明模式

- 从早期零行覆盖图直接反推 signed canonical 系数
- 从 terminal certificate 或 payment skeleton 反推 pre-Cauchy source
- 用 canonical-source 已闭合结论证明当前 seed 已 canonical
- 用 formal_unit hash stability 替代测度因子与系数恒等式
- 用 actual noncanonical ExactUV/source-entropy 路线冒充 canonical branch admission

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameCounterexampleDisciplinePreserved` | `true` | `true` | 本步仍在假设早期零行存在的反例链内部工作，不用真实缺席、统计样本或 runner 输出替代证明。 | direct_unconditional_contradiction_found=false。 |
| `DirectPDECSendsBackToCanonicalLock` | `true` | `true` | direct acyclic same-set PDEC 已被作用域审计压回 canonical-lock 作用域匹配。 | AcyclicSeedCanonicalBranchAdmissionBeforeCauchy |
| `TargetIsFirstSeedEmbeddingAtom` | `true` | `false` | AcyclicSeedCanonicalSourceFiniteFactorEmbedding 的第一个必要子原子正是 pre-Cauchy canonical branch 准入。 | AcyclicSeedCanonicalBranchAdmissionBeforeCauchy |
| `TimelineAdmissionLawClosed` | `true` | `true` | canonical 准入若合法，必须在 Cauchy/dispersion/terminal extraction 前声明；下游证书只能消费该声明，不能生成该声明。 | AcyclicCanonicalPreCauchyCoefficientIdentityLedger |
| `A1CanonicalBranchScopedOnly` | `true` | `true` | A1 canonical branch 是合法子分支；但它只在对象已于 T1 声明为 RIW/Buchstab canonical source 时可用。 | 不能把 generic/noncanonical seed 静默升级为 canonical。 |
| `DownstreamRecoveryRejected` | `true` | `true` | 从早期零行覆盖图、payment skeleton、terminal certificate、有限投影或当前 PDEC 前沿反推 source 会落入来源环。 | 必须提交独立 T1 账本。 |
| `CanonicalExitFiveLedgerStillOpen` | `true` | `false` | canonical-lock 非循环出口仍缺五项 exact same-set 证书，尤其缺 pre-Cauchy coefficient identity。 | AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection |
| `CanonicalBranchAbsorptionNotGlobalContradiction` | `true` | `true` | 五项证书若成立，只给 canonical-source scoped promotion；证书不成立时 canonical-lock 不可用。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `ActualSourceSeedDoesNotProveCanonicalAdmission` | `true` | `true` | actual noncanonical seed/ExactUV 支撑属于 noncanonical 主线，不能反向证明 canonical branch admission。 | 若不提交 canonical T1 身份，只能回到 actual-source 熵或 clean DLS。 |
| `PreCauchyDeclarationLineForNoncanonicalSeparated` | `true` | `true` | noncanonical declaration line 的合法义务已另行分类；它不能填 canonical RIW/Buchstab 身份表。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。 |
| `CounterexampleTrueStructureGivesPressureNotSignedSource` | `true` | `true` | 斜线覆盖、镜像、P 列锚和层叠筛形成结构压力，但目前只给 unsigned 形状，不能直接生成 T1 signed canonical 系数。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR signed lift。 |
| `CleanDLSFallbackStillAnalyticOpen` | `true` | `false` | 若 seed 不可 canonical 准入，clean residual 的自足出口仍是窗口化 Kloosterman/DLS 内部估计。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `AcyclicSeedCanonicalBranchAdmissionCurrentCorpusProved` | `false` | `false` | 当前语料没有独立提交 T1 canonical coefficient identity ledger，因此不能证明本原子。 | AcyclicCanonicalPreCauchyCoefficientIdentityLedger OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem OR AcyclicWindowedKloostermanDLSInternalEstimate |

## 6. 下一主攻点

```text
AcyclicCanonicalPreCauchyCoefficientIdentityLedger
```

若该 T1 canonical identity 不能独立提交，canonical-lock 路线不能继续承担闭合作用；非 canonical 主线必须回到 actual-source 熵定理或 acyclic windowed DLS/CleanKLS 解析原子。
