# Prime Matrix strict acyclic Kuznetsov/DLS 原子路由器

**状态：** `self_contained_kuznetsov_dls_atom_reduced_to_acyclic_ncblk_source_antiatom_open`

本步继续攻 `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。KZ-A 平滑、KZ-B trace formula、KZ-C Bessel 衰减、KZ-D spectral large sieve 已有内部脊柱；真正阻断是 KZ-E 的 well-factorable dispersion log-saving。既有 SC-9 前沿和 NC-BLK 核查显示，该阻断等价于证明 acyclic actual block nonconcentration/source anti-atom，或走外部 FullS-KLS-ext 条件线。因此当前最窄自足剩余更新为 `AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
kz_a_smoothing_closed=true
kz_b_trace_specialization_closed=true
kz_c_bessel_decay_closed=true
kz_d_spectral_large_sieve_closed=true
kz_e_reduced_to_ncblk_or_external=true
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
acyclic_ncblk_actual_block_nonconcentration_proved=false
acyclic_strengthened_source_antiatom_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
```

## 1. KZ 展开

```text
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
  -> KZ-A smoothing/L2 bookkeeping closed
  -> KZ-B Kuznetsov trace specialization closed
  -> KZ-C Bessel transform decay closed
  -> KZ-D spectral large sieve/pretrace chain closed
  -> KZ-E well-factorable dispersion log-saving
  -> AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
```

条件外部线：

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom OR AcceptExternalFullSKLSExtWithNoProjectionCompatibility
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `KuznetsovDLSAtomActive` | `true` | `false` | 上一层把 acyclic windowed DLS 估计压成自足 Kuznetsov/DLS 大筛原子。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `KZAClosed` | `true` | `true` | Kloosterman 模数平滑和 L2 bookkeeping 已由 H3/KZ-A 普通账本关闭。 | 无。 |
| `KZBClosed` | `true` | `true` | Kuznetsov trace formula 专门化已由 Poincare unfolding 与谱 Plancherel 内联推导。 | 无。 |
| `KZCClosed` | `true` | `true` | Bessel transform 窗口衰减已由 H3/KZ-C 账本关闭。 | 无。 |
| `KZDClosed` | `true` | `true` | 谱大筛 KZ-D 已由 pretrace/LPC/GHLC Schur 链关闭，oldform/Eisenstein 只进入多对数账本。 | 无。 |
| `KZEReducesToNCBLK` | `true` | `true` | KZ-E/well-factorable dispersion 对数节省不能由裸谱大筛给出；既有 SC-9 前沿已压到 NC-BLK 或外部 DI/BFI。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `CanonicalNCBLKAbsorptionBlockedForAcyclic` | `true` | `true` | canonical-source NC-BLK 已被同集边界吸收，但 strict acyclic/noncanonical 分支不能偷渡该吸收。 | 需证明 acyclic actual block nonconcentration 或源反原子。 |
| `GenericAntiAtomNoGoImported` | `true` | `true` | generic full-S 自足反原子在 moving-delta 模型下为假；仅靠形式 WFD/Type/Fourier 模板不能推出 NC-BLK。 | acyclic seed 必须提供更强的实际来源反原子，或接受外部 FullS-KLS-ext。 |
| `ExternalContractSeparated` | `true` | `true` | FullS-KLS-ext 或 DI/BFI/Kuznetsov 可作为外部合同线，但严格自足线需要内部来源反原子。 | AcceptExternalFullSKLSExtWithNoProjectionCompatibility 属于条件线。 |
| `SelfContainedKuznetsovDLSAtomReduced` | `true` | `false` | 自足 Kuznetsov/DLS 原子已沿 KZ-A--KZ-E 压到 acyclic NC-BLK/源反原子。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `StrictTerminalFamilyProved` | `true` | `false` | strict 终端家族仍未闭合；活动非 canonical 线卡在 acyclic NC-BLK/源反原子。 | (AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |

## 3. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。

必须证明：
- 对 acyclic clean residual 的实际系数证明同 moving-block 的最大块质量满足任意 log-power 反原子界。
- 证明该反原子来自假设早期零行链的实际 pre-Cauchy source，而不是形式 WFD 模板。
- 排除 moving-delta 单块集中模型，或说明它必回流 PDEC/SAE/ColumnCRT。
- 若使用外部 FullS-KLS-ext，必须保留条件线并证明无投影兼容。

不能作为证明使用：
- 重复 KZ-A--KZ-D 谱理论闭合。
- 把 canonical-source NC-BLK 吸收导入 acyclic/noncanonical 分支。
- 声称形式 well-factorable/Type/Fourier 模板自动给反原子。
- 把外部 FullS-KLS-ext 写成严格自足证明。
