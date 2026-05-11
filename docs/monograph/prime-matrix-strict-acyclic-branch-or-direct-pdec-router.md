# Prime Matrix strict acyclic canonical/direct-PDEC 二选一路由器

**状态：** `canonical_admission_open_direct_acyclic_pdec_selected_and_atomized`

本步把二选一硬点做成严格分叉：canonical 路线只有在 seed 因子图、同集推前、无 payload 残留全部证明后才可导入；当前语料没有证明这些前提。因此 strict acyclic/noncanonical 活动分支优先转入 DirectAcyclicSameSetPDECCapDualCertificate。该证书又被压成三项：先物化同一坏窗集合上的 PDEC 输入和质量账本；再证明 dual-cap 定位无第四出口；最后证明有限循环弧 cap 质量上界或命名回流。命题仍未无条件闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
canonical_branch_conditional_implication_pinned=true
acyclic_seed_canonical_branch_admission_proved=false
acyclic_seed_finite_factor_map_weight_identity_proved=false
direct_acyclic_same_set_pdec_selected=true
acyclic_same_set_pdec_input_materialized=false
direct_acyclic_same_set_pdec_dual_proved=false
direct_acyclic_clean_kls_dls_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
```

## 1. 二选一分叉

canonical 条件包：

```text
AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection
```

direct PDEC 原子化前：

```text
DirectAcyclicSameSetPDECCapDualCertificate
```

direct PDEC 原子化后：

```text
AcyclicSameSetPDECInputMaterializationAndMassLedger AND AcyclicPDECDualCapLocalizationAndNoFourthExit AND AcyclicFiniteArcCapMassBoundsOrNamedReturn
```

总终端门更新为：

```text
(AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR (AcyclicSameSetPDECInputMaterializationAndMassLedger AND AcyclicPDECDualCapLocalizationAndNoFourthExit AND AcyclicFiniteArcCapMassBoundsOrNamedReturn) OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TwoLaneGateActive` | `true` | `false` | 上一层留下二选一：证明 canonical-lock 的 seed 准入包，或转 direct acyclic same-set PDEC。 | canonical package OR DirectAcyclicSameSetPDECCapDualCertificate。 |
| `CanonicalBranchConditionalImplicationPinned` | `true` | `true` | 若 seed 因子图、同集推前和无 payload 残留全部成立，则可条件导入 canonical-source 终端闭合。 | 该项只是条件蕴含，不证明前提。 |
| `CanonicalAdmissionCurrentCorpusStillOpen` | `true` | `false` | 当前材料未证明 acyclic seed 在 pre-Cauchy 层就是 canonical RIW/Buchstab source branch。 | AcyclicSeedCanonicalBranchAdmissionBeforeCauchy。 |
| `CanonicalFactorMapCurrentCorpusStillOpen` | `true` | `false` | 当前材料未提交 pi_* mu_c = mu_a 的同测度有限因子图。 | AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity。 |
| `NoPayloadProjectionCurrentCorpusStillOpen` | `true` | `false` | 当前材料未证明 noncanonical payload 在 canonical 投影后无残留。 | AcyclicSeedNoSourceReplacementOrPayloadCreation AND NoNoncanonicalPayloadSurvivesCanonicalProjection。 |
| `DirectPDECSelectedAsLiveStrictBranch` | `true` | `true` | 在不偷渡 canonical 前提的 strict acyclic/noncanonical 分支中，下一主攻口必须是 direct same-set PDEC 或 direct CleanKLS；优先攻 PDEC。 | DirectAcyclicSameSetPDECCapDualCertificate |
| `RegisteredCapacityMultiplierImported` | `true` | `true` | 容量乘子纪律已在严格二线终局过滤中登记，direct PDEC 必须使用同一阈值和同一坏窗口径。 | 仍需物化 acyclic PDEC 输入。 |
| `SameSetPDECProtocolImportedWithScope` | `true` | `true` | PDEC 比较的形式协议是同一坏窗计数向量上计算 U_CRT 与 L_PDEC；若失败必须输出 dual cap。 | 该协议不自动证明 acyclic 终端家族满足输入物化和 cap 上界。 |
| `AcyclicPDECInputMaterializationPinned` | `true` | `false` | 必须从 acyclic terminal certificate 生成同一 formal unit、同一坏窗集合、同一质量 M 的 PDEC count vector。 | AcyclicSameSetPDECInputMaterializationAndMassLedger。 |
| `DualCapLocalizationPinned` | `true` | `false` | 若 acyclic PDEC 不等式失败，必须定位到有限方向帽 dual cap，并证明它只能命名回流而不能作为第四出口。 | AcyclicPDECDualCapLocalizationAndNoFourthExit。 |
| `FiniteArcMassBoundsPinned` | `true` | `false` | direct acyclic PDEC 的真正估计硬点是所有有限循环弧 cap 质量上界，或输出 PDEC/SAE/ColumnCRT/CleanKLS 命名回流。 | AcyclicFiniteArcCapMassBoundsOrNamedReturn。 |
| `DirectAcyclicPDECCurrentCorpusProved` | `true` | `false` | 当前材料闭合了 canonical-source PDEC 边界，但没有闭合 acyclic/noncanonical 同集 PDEC 证书。 | AcyclicSameSetPDECInputMaterializationAndMassLedger AND AcyclicPDECDualCapLocalizationAndNoFourthExit AND AcyclicFiniteArcCapMassBoundsOrNamedReturn |

## 3. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR (AcyclicSameSetPDECInputMaterializationAndMassLedger AND AcyclicPDECDualCapLocalizationAndNoFourthExit AND AcyclicFiniteArcCapMassBoundsOrNamedReturn) OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`AcyclicSameSetPDECInputMaterializationAndMassLedger`。

必须证明：
- 从假设早期零行反例链的 acyclic terminal certificate 中定义唯一坏窗集合 B 和有限 formal unit G。
- 构造同一 count vector g_B(t)，使 U_CRT、L_PDEC、M、capacity multiplier 全部作用在同一个 g_B 上。
- 证明删除、投影、回流、quotient 不改变坏窗集合口径；改变则必须命名为 PDEC/SAE/ColumnCRT/CleanKLS return。
- 若 U_CRT >= L_PDEC，则输出有限方向帽 dual cap，并进入 finite-arc cap mass bounds 或命名回流。

不能作为证明使用：
- 把 canonical-source PDEC-CAP 闭合直接用于 acyclic/noncanonical 分支。
- 把 source 哈希稳定当成同集 count vector 物化。
- 在 U_CRT 与 L_PDEC 中使用不同坏窗集合或不同推前质量。
- 把 dual cap 的存在当成矛盾；必须继续证明 cap 上界或命名回流。
