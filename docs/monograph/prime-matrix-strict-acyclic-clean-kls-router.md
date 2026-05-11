# Prime Matrix strict acyclic clean KLS/DLS 路由器

**状态：** `direct_acyclic_clean_kls_reduced_to_windowed_dls_atom_open`

本步把 `DirectAcyclicCleanKLSDLSEstimateWithNamedReturn` 原子化。PDEC/SAE/ColumnCRT/Multiplicity 等低维缺陷已在上游剥离，所以 K1--K9 clean admission 与 L2-flat 系数账本可作为结构准入关闭；但这仍不是大筛证明。严格自足剩余压成 `AcyclicWindowedKloostermanDLSInternalEstimate`。外部 DI/BFI/Kuznetsov 可作为条件线，不能替代严格自足闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
named_defects_peeled=true
k1_k9_clean_admission_closed=true
l2_flat_coefficient_ledger_closed=true
windowed_kloosterman_template_registered=true
acyclic_windowed_kloosterman_dls_internal_estimate_proved=false
direct_acyclic_clean_kls_dls_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
```

## 1. clean KLS 收缩

```text
DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
  named low-dimensional defects already peeled
  K1--K9 admission closes structurally
  L2-flat coefficient ledger closes structurally
  remaining strict atom:
    AcyclicWindowedKloostermanDLSInternalEstimate
```

条件外部线为：

```text
AcyclicWindowedKloostermanDLSInternalEstimate OR AcceptExternalDIBFIKuznetsovNoProjectionWindowCertificate
```

严格自足线只保留：

```text
AcyclicWindowedKloostermanDLSInternalEstimate
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DirectAcyclicCleanKLSActive` | `true` | `false` | 上一层把 finite-arc 平坦剩余转为 strict acyclic clean KLS/DLS 终端。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `NamedDefectsAlreadyPeeled` | `true` | `true` | PDEC/SAE/ColumnCRT/Multiplicity/new-layer 低维缺陷已由 finite-arc 与 no-loss return 体系剥离。 | 只剩 clean residual。 |
| `K1K9AdmissionClosedByConstruction` | `true` | `true` | clean residual 的 K1--K9 准入条件成立；任一失败都按定义回流到已命名出口。 | 准入不是大筛估计。 |
| `L2FlatCoefficientLedgerClosed` | `true` | `true` | 所有固定有限投影的高原子、短窗、低相位和新增层集中已剥离，剩余给出 L2-flat 系数账本。 | 需要把系数映射到标准窗口化 Kloosterman/DLS 模板。 |
| `WindowedKloostermanTemplateRegistered` | `true` | `true` | A1 clean KLS 模板已登记：clean dyadic formal unit 映射到 m, ell, d, R, h 与平滑权重窗口。 | 提交内部大筛估计或外部证书。 |
| `CanonicalNCBLKImportBlocked` | `true` | `true` | canonical-source NC-BLK 吸收只在 canonical RIW/Buchstab 来源分支内有效，不能导入 acyclic/noncanonical clean residual。 | 必须证明 acyclic 窗口化估计或走外部条件线。 |
| `ExternalDIBFISeparated` | `true` | `true` | 外部 DI/BFI/Kuznetsov 可形成条件版本，但严格自足路线不能用外部黑箱关闭。 | AcceptExternalDIBFIKuznetsovNoProjectionWindowCertificate 只属于外部线。 |
| `DirectCleanKLSReducedToWindowedDLSAtom` | `true` | `false` | direct clean KLS/DLS 的结构准入已闭合，剩余是窗口化 Kloosterman/DLS 内部估计。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `DirectAcyclicCleanKLSDLSEstimateProved` | `true` | `false` | 当前语料尚未提交 acyclic windowed Kloosterman/DLS 自足大筛估计。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `StrictTerminalFamilyProved` | `true` | `false` | strict 终端家族仍未闭合；它现在卡在 canonical package 或 acyclic windowed DLS atom。 | (AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR AcyclicWindowedKloostermanDLSInternalEstimate |

## 3. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR AcyclicWindowedKloostermanDLSInternalEstimate) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`AcyclicWindowedKloostermanDLSInternalEstimate`。

必须证明：
- 把 acyclic clean residual 的 L2-flat 系数精确写入窗口化 Kloosterman/dispersion 双线性型。
- 给出同一 formal unit 下的模数、长度、光滑权、互素条件和坏窗质量规范化。
- 证明内部 DLS/Kuznetsov 型大筛界足以吸收 clean residual。
- 若估计失败，必须输出 point-load、short-window、low-phase 或 new-layer PDEC/SAE/ColumnCRT 命名回流。

不能作为证明使用：
- 只说 K1--K9 已通过。
- 直接引用 canonical-source NC-BLK 吸收。
- 把外部 DI/BFI/Kuznetsov 黑箱写成严格自足证明。
- 把有限数值审计当作窗口化 DLS 全局估计。
