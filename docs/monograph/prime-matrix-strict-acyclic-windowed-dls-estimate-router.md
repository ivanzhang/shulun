# Prime Matrix strict acyclic windowed DLS 估计路由器

**状态：** `acyclic_windowed_dls_reduced_to_self_contained_kuznetsov_large_sieve_atom_open`

本步继续攻 `AcyclicWindowedKloostermanDLSInternalEstimate`。形式层已压尽：acyclic clean residual 的对象、窗口化双线性型、相位/可逆变量、L2 系数范数和失败回流字母表均可由现有账本关闭。剩下的不是变量命名或 clean 准入，而是一个真正解析原子：`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。外部 DI/BFI/Kuznetsov 只能作为条件线，仍需精确专门化与无投影兼容。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
acyclic_windowed_bilinear_normal_form_closed=true
phase_invertible_variable_ledger_closed=true
coefficient_norm_ledger_closed=true
failure_return_alphabet_closed=true
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
acyclic_windowed_kloosterman_dls_internal_estimate_proved=false
direct_acyclic_clean_kls_dls_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

严格自足线：

```text
AcyclicWindowedKloostermanDLSInternalEstimate
  -> clean residual object fixed
  -> windowed bilinear normal form
  -> phase/invertible-variable ledger
  -> coefficient norm ledger
  -> SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
```

条件外部线：

```text
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR (ExactExternalKLSSpecialization AND UncenteredNoProjectionCompatibilityForAcyclicCleanBlock)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WindowedDLSInternalEstimateActive` | `true` | `false` | 上一层把 strict acyclic clean KLS/DLS 压成窗口化 Kloosterman/DLS 内部估计。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `CleanResidualObjectFixed` | `true` | `true` | 同一 formal unit 中的 PDEC/SAE/ColumnCRT/new-layer 低维缺陷已剥离，只剩 L2-flat clean residual。 | 无；对象已固定。 |
| `BilinearNormalFormClosed` | `true` | `true` | clean residual 可写入窗口化 Kloosterman/dispersion 双线性型，变量为 m, ell, d, R, h 与平滑 W。 | 大筛不等式本身。 |
| `PhaseAndInvertibleVariableLedgerClosed` | `true` | `true` | CRT 相位、可逆变量、gcd/unit 层和非零 Fourier 频率已经由 A1 clean KLS 模板登记。 | 内部谱估计。 |
| `CoefficientNormLedgerClosed` | `true` | `true` | L2-flat 系数、dyadic 分块、平滑导数损失和 polylog 预算均在 clean admission/模板账本内登记。 | 证明这些范数输入下的 KLS/DLS log-saving。 |
| `FailureReturnAlphabetClosed` | `true` | `true` | 若失败来自 point-load、short-window、low-phase、new-layer 或列/壳集中，已经命名回流。 | 纯谱大筛不等式无法再靠命名回流删除。 |
| `ExternalLineSeparated` | `true` | `true` | 外部 DI/BFI/Kuznetsov 线需要精确专门化和无投影兼容；它可给条件闭合，不给严格自足闭合。 | ExactExternalKLSSpecialization AND UncenteredNoProjectionCompatibilityForAcyclicCleanBlock。 |
| `InternalKuznetsovDLSInequalityAtomPinned` | `true` | `false` | 真正自足剩余是证明 acyclic clean blocks 的窗口化 Kuznetsov/DLS 大筛不等式。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `AcyclicWindowedDLSInternalEstimateProved` | `true` | `false` | 当前语料没有提交该自足谱大筛证明。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `StrictTerminalFamilyProved` | `true` | `false` | strict 终端家族仍未闭合；活动非 canonical 线卡在自足 Kuznetsov/DLS 不等式。 | (AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |

## 3. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。

必须证明：
- 对所有 acyclic clean dyadic blocks 给出统一窗口化 Kloosterman/DLS 双线性型上界。
- 上界必须只依赖 L2 范数、模数窗口、频率窗口、平滑导数损失和 polylog 预算。
- 所得节省必须足以吸收 strict 终端门中剩余 clean residual 质量。
- 若试图使用外部 DI/BFI/Kuznetsov，必须另证精确专门化和无投影兼容，并标记为条件线。

不能作为证明使用：
- 重复 K1--K9 clean admission 或 L2-flat 账本。
- 只给 DI/BFI 变量表而不证明 J-scale/谱大筛上界。
- 把外部定理当成严格自足证明。
- 把有限数值审计或低维回流字母表当成纯谱不等式。
