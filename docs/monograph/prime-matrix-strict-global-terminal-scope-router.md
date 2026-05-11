# Prime Matrix 严格全局终端门作用域校准路由器

**状态：** `strict_global_terminal_reduced_to_acyclic_terminal_family_and_high_model_gap_open`

严格全局终端门继续压缩，但必须守住作用域：GlobalPDECorSparseTerminalExclusion 可接入既有拆分，变成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve；ExplicitModelGapAndFiniteDPRCLedger 可拆成已闭合的 P<2003 有限段与仍开放的 HighSegmentModelGapAlpha043C3AnalyticLedger。可是 canonical 终端晋级闭合只限 canonical-source 形式系统，不能直接导入当前 acyclic noncanonical seed。故严格自足剩余更新为：无环 source seed、acyclic noncanonical 终端家族的 PDEC-CAP/CleanKLS 证明、高段模型余量，以及自足 DStructure/Rankin 替代包。当前仍没有无条件闭合。

```text
strict_global_terminal_scope_boundary_closed=true
canonical_terminal_promotion_not_importable_for_strict_noncanonical=true
finite_dprc_segment_closed=true
acyclic_pre_cauchy_seed_proved=false
strict_acyclic_terminal_family_proved=false
high_segment_model_gap_alpha043_c3_analytic_ledger_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND HighSegmentModelGapAlpha043C3AnalyticLedger
```

## 1. 作用域校准链

```text
GlobalPDECorSparseTerminalExclusion
  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
  -> canonical promotion closes only canonical-source branch
  -> strict acyclic noncanonical branch still needs its own terminal-family proof

ExplicitModelGapAndFiniteDPRCLedger
  -> FiniteDPRCAlpha043PBelow2003Certificate(closed)
  -> HighSegmentModelGapAlpha043C3AnalyticLedger(open)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictGlobalTerminalInputActive` | `true` | `false` | 上一层严格基含 GlobalPDECorSparseTerminalExclusion 与 ExplicitModelGapAndFiniteDPRCLedger。 | 继续拆全局终端门，并拆模型/DPRC 账本。 |
| `GlobalTerminalSplitImported` | `true` | `true` | GlobalPDECorSparseTerminalExclusion 已由既有拆分压成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。 | PDEC-CAP 或内部 CleanKLS 大筛吸收。 |
| `MaterializedFrontierExhaustedImported` | `true` | `true` | 当前已物化 PDEC 与 sparse/LocalSurvivor 前沿清零；不能继续靠局部样本消元。 | 必须处理全局家族证书，而非现成样本。 |
| `CanonicalTerminalPromotionScopeChecked` | `true` | `true` | NoFurtherCanonicalSourceTerminalPromotionGap 只在 canonical-source 形式系统内闭合。 | 不能直接关闭 acyclic noncanonical/global 终端家族。 |
| `CanonicalImportBlockedForStrictNoncanonicalSeed` | `true` | `true` | 当前严格链仍含 AcyclicPreCauchyNoncanonicalPrimitiveSourceSeed；没有证明该 seed 的终端证书全都 canonical-lock。 | 若要使用 canonical 闭合，必须新增 terminal canonical-lock theorem。 |
| `CleanKLSBottleneckScopeChecked` | `true` | `true` | Internal CleanKLS 在 canonical-source 边界内已非独立瓶颈；但 unrestricted/generic 自足 KLS 已被隔离而非证明。 | strict noncanonical 仍需 PDEC_CAP_OR_INTERNAL_CleanKLS 的同对象证明或回流。 |
| `ExplicitModelGapFiniteSplitImported` | `true` | `true` | ExplicitModelGapAndFiniteDPRCLedger 已拆分：P<2003 有限段闭合，高段解析模型余量仍开放。 | HighSegmentModelGapAlpha043C3AnalyticLedger。 |
| `StrictGlobalTerminalScopeReduced` | `true` | `true` | 严格全局终端门不能用 canonical 闭合偷渡；它被校准为 acyclic-seed 口径下的 PDEC_CAP/CleanKLS 终端证明。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。 |
| `AcyclicSeedCurrentCorpusProved` | `true` | `false` | 当前材料仍未提交无环 pre-Cauchy actual noncanonical primitive source seed。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。 |
| `StrictTerminalFamilyCurrentCorpusProved` | `true` | `false` | 当前材料没有证明 acyclic noncanonical terminal family 的 PDEC-CAP/CleanKLS 全局排斥。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。 |
| `HighSegmentModelGapCurrentCorpusProved` | `true` | `false` | P>=2003 的 S_Y(P)(1-H_Y(P))>3sqrt(S_Y(P)) 仍只有审计账本，缺解析证明。 | HighSegmentModelGapAlpha043C3AnalyticLedger。 |

## 3. 下一主攻合同

下一数学主攻点：`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily`。

必须证明：
- 对 acyclic noncanonical source 产生的全部 PDEC family 证明同一坏窗集合上的 U_CRT<L_PDEC 全局对偶证书。
- 或证明其 diffuse residual 满足内部 CleanKLS/DLS 大筛吸收并把失败回流 PDEC/SAE/ColumnCRT。
- 若要引用 canonical 终端闭合，必须证明终端证书 canonical-lock 到 RIW/Buchstab source branch。
- 同时闭合 HighSegmentModelGapAlpha043C3AnalyticLedger 的高段解析不等式。
- 继续保留自足 DStructure/Rankin 替代包。

不能作为证明使用：
- 把 NoFurtherCanonicalSourceTerminalPromotionGap 直接导入 noncanonical acyclic seed。
- 把当前物化前沿清零当作全局家族排斥。
- 把 unrestricted/generic KLS 自足版当作已证。
- 把 P<2003 有限 DPRC 闭合当作高段模型余量证明。
- 把外部 DI/BFI/KLS 作为严格自足闭合。

严格自足数学基更新为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND HighSegmentModelGapAlpha043C3AnalyticLedger AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
