# Prime Matrix strict acyclic PDEC 输入物化路由器

**状态：** `acyclic_same_set_pdec_input_materialized_finite_arc_cap_bounds_open`

本步关闭 direct acyclic PDEC 的首个输入物化硬点：由普遍 formal unit 抽取、source record schema、hash stability、no-loss return 和容量乘子纪律，可在假设早期零行分支中定义同一坏窗集合 B、有限签名群 G、同一 count vector g_B 与同一质量 M。有限 LP/帽定位和终端证书压缩也关闭了 dual-cap 无第四出口。direct PDEC 的真正剩余因此压成一个原子：AcyclicFiniteArcCapMassBoundsOrNamedReturn。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
universal_formal_unit_extractor_imported=true
same_count_vector_constructed=true
acyclic_same_set_pdec_input_materialized=true
acyclic_pdec_dual_cap_localization_no_fourth_exit_proved=true
acyclic_finite_arc_cap_mass_bounds_proved=false
direct_acyclic_same_set_pdec_dual_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
```

## 1. 输入物化公式

```text
witness W -> finite formal unit records -> select direct-PDEC unit (B,G)
g_B(t) := total bad-window mass in B with signature t in G
U_CRT = U_CRT(g_B),  L_PDEC = L_PDEC(g_B),  M = sum_t g_B(t)
```

所有比较都在同一个 `g_B` 上进行。若删除、投影、quotient 或回流改变 `B/G/g_B/M`，它不能继续留在本 PDEC 输入内，必须成为命名 return。

## 2. PDEC 线更新

更新前：

```text
AcyclicSameSetPDECInputMaterializationAndMassLedger AND AcyclicPDECDualCapLocalizationAndNoFourthExit AND AcyclicFiniteArcCapMassBoundsOrNamedReturn
```

更新后：

```text
AcyclicFiniteArcCapMassBoundsOrNamedReturn
```

总终端门更新为：

```text
(AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR AcyclicFiniteArcCapMassBoundsOrNamedReturn OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AcyclicPDECInputMaterializationActive` | `true` | `false` | 上一层把 direct acyclic PDEC 的首个原子定为同集输入物化与质量账本。 | AcyclicSameSetPDECInputMaterializationAndMassLedger。 |
| `UniversalExtractorImported` | `true` | `true` | 任意假设早期零行 witness 都可产出有限、无漏、可哈希的 formal unit records。 | 把这些 records 专门读取为 PDEC count vector。 |
| `FormalUnitRecordSchemaImported` | `true` | `true` | 每个 formal unit record 含 witness、family、window、phase、branch 和 no-loss return 字段。 | 在 PDEC 分支中指定坏窗集合 B 与有限签名群 G。 |
| `BadWindowSetDefined` | `true` | `true` | 对进入 direct PDEC 的 acyclic terminal certificate，取 B 为同一 formal unit 中未命名回流的坏窗义务集合。 | 无；改变 B 的操作必须变成 return record。 |
| `FiniteSignatureGroupDefined` | `true` | `true` | 取 G 为 formal unit key 中的有限相位/签名商；hash stability 保证分割和回流不改名。 | 无；跨 G 的项必须重新登记或回流。 |
| `SameCountVectorConstructed` | `true` | `true` | 定义 g_B(t)=同一 B 内落在签名 t 的坏窗质量总和；U_CRT、L_PDEC、M 均只作用在此 g_B 上。 | 无；不同 g 的比较被禁止。 |
| `CapacityMultiplierSameSetDisciplinePreserved` | `true` | `true` | 容量乘子只登记在同一 g_B、同一 M、同一 formal unit 上；阈值迁移需命名回流。 | 无；只剩容量估计。 |
| `NoLossReturnProtectsMassLedger` | `true` | `true` | 删除、投影、quotient、重复合并若不保留 g_B，必须显式进入 PDEC/SAE/ColumnCRT/CleanKLS return。 | 无；这给出 PDEC 输入账本的同集性。 |
| `AcyclicSameSetPDECInputMaterialized` | `true` | `true` | direct acyclic PDEC 的同集输入物化闭合：B、G、g_B、M、U_CRT、L_PDEC 口径固定。 | AcyclicPDECDualCapLocalizationAndNoFourthExit。 |
| `DualCapLocalizationNoFourthExitClosed` | `true` | `true` | 有限 LP/帽定位给出 dual cap；终端证书压缩保证它只能回流 PDEC/SAE/ColumnCRT/CleanKLS，不能成为第四出口。 | 仍需证明有限弧 cap 质量上界，或执行这些命名回流。 |
| `FiniteArcCapEstimateStillOpen` | `true` | `false` | 真正剩余是对每个 acyclic formal unit、非平凡字符和有限循环弧证明 cap 质量低于阈值，或输出命名回流。 | AcyclicFiniteArcCapMassBoundsOrNamedReturn |
| `DirectAcyclicPDECCurrentCorpusProved` | `true` | `false` | direct acyclic PDEC 已越过输入物化和 dual-cap 定位，但未完成有限弧 cap 质量估计。 | AcyclicFiniteArcCapMassBoundsOrNamedReturn |

## 4. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR AcyclicFiniteArcCapMassBoundsOrNamedReturn OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 5. 下一主攻合同

主攻名：`AcyclicFiniteArcCapMassBoundsOrNamedReturn`。

必须证明：
- 固定 acyclic formal unit G 与同集 count vector g_B 后，列出所有非平凡字符 chi 与有限循环弧 I。
- 证明 g_B(chi^{-1}(I)) 低于 PDEC 帽定位阈值 (L_PDEC-alpha M)/(1-alpha)。
- 若某弧超过阈值，必须把该弧物化为 SAE、refined PDEC、ColumnCRT 或 CleanKLS return。
- 证明有限弧细化不会产生同层无限循环；升层必须进入 new-layer PDEC/CleanKLS 命名路线。

不能作为证明使用：
- 只说 dual cap 存在；dual cap 是失败证书，不是排斥证书。
- 使用 canonical-source cap 上界覆盖 acyclic/noncanonical formal unit。
- 在弧质量估计中更换 B、G、g_B 或 M。
- 把有限实验样本中没有高质量弧当作全局证明。
