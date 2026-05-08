# Prime Matrix 坏窗来源数据发射器路由器

**状态：** `bad_window_source_data_reduced_to_record_emitter_and_anchor_parameters`

BadWindowSourceFamilyDataExtractionLedger 已被压成确定记录发射器：每个已命名来源族都有同 formal unit 的字段来源和失败回流规则。真正还没填的是互补锚集合、D0/K/Omega、相位规则与预算参数；因此新的最窄点推进为 `ComplementAnchorSetAndD0KParameterLedger`。这一步不声称 formal corridor inventory 已有 concrete 全集，也不关闭 PDEC/SAE、Rankin 或行列无条件定理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
bad_window_source_family_record_emitter_closed=true
concrete_formal_corridor_inventory_records_available=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
BadWindowSourceFamilyDataExtractionLedger => BadWindowSourceFamilyRecordEmitterClosed AND ComplementAnchorSetAndD0KParameterLedger.
```

## 2. 发射规则

| family_id | emitter_law | required_inputs | downstream |
| --- | --- | --- | --- |
| EndpointSawtoothDirectedCRTDefect | 从 BK-DEC 端点块发射 (window_id,Q,test_function_id,tau,kappa)。 | 边界窗 I、端点 sawtooth block、低模 Q、阈值 kappa。 | PDECOrSAEUnifiedExclusionLedger |
| TailAnchorConcentration | 从饱和尾锚集合发射 (anchor a, rho_Q(a), theta, W_a, N_a)。 | 互补锚集合 A、窗口 I、D0/K、饱和阈值 theta。 | ComplementAnchorSetAndD0KParameterLedger then PDECOrSAEUnifiedExclusionLedger |
| HighOverlapFixedCoreDefect | 从重叠函数 m(d)>Omega 发射 (fixed_core d, overlap, anchor_short_window)。 | 核心尺度 D0、重叠阈值 Omega、互补锚集合 A。 | ComplementAnchorSetAndD0KParameterLedger or PDECOrSAEUnifiedExclusionLedger |
| ColoredDisjointCorridorBudgetViolation | 低重叠走廊经区间图着色，逐颜色发射 intervals/K/D0/Omega/allowed_budget。 | A、D0、K、Omega、phase_rule、allowed_budget、覆盖等式。 | ComplementAnchorSetAndD0KParameterLedger -> IntervalGraphColoringCoverageCertificateLedger -> AllowedBudgetAllocationLedger |
| SmoothCoreLowModCRTDefect | 从 failed Rankin 颜色类的 residue spike 发射 (Q,b,g(b),eta)。 | 颜色类证书、低模 Q、中心化 residue 计数、spike 阈值 eta。 | PDECOrSAEUnifiedExclusionLedger |
| SparseSingleWindowEscape | 从 sparse bad window 发射 SAE packet 字段或 lift/higher-defect 回流字段。 | window_shape、candidate set、blocker families、phase_key、formal_unit_id。 | SAE-Cert or lift to PDEC/SAE. |
| RankinConstantGapNoSpike | 从无尖峰 Rankin 失败发射 constant-gap record，不计作 PDEC/SAE 已排除。 | ledger、s、Q、allowed_budget、失败余量和细分/调参动作。 | AllowedBudgetAllocationLedger |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BadWindowSourceDataGateActive | `true` | `false` | 上一层已把当前最窄点推进到坏窗来源族数据抽取。 | BadWindowSourceFamilyDataExtractionLedger |
| FiniteTaxonomyImported | `true` | `true` | 七个来源族已经固定，数据发射器只需覆盖这些族。 | 无新来源类型剩余。 |
| SameFormalUnitEmitterAvailable | `true` | `true` | 早期零行假设给出同一 Omega=R_x formal unit 与物理原子字段。 | 禁止跨口径拼接；缺字段回流 schema。 |
| PDECExplicitBoundaryAvailable | `true` | `true` | 未来 PDEC 候选必须同 formal unit、非二点、二秩以上且 cap-stable。 | 最终 PDEC 排斥仍未无条件闭合。 |
| SparsePacketBoundaryAvailable | `true` | `true` | 未来 sparse/SAE 路线必须提交有限 packet extractor 字段。 | 全局 sparse family 排斥仍未无条件闭合。 |
| FinalExitInterfacesAvailable | `true` | `true` | 发射出的 persistent、sparse 与 Rankin 失败记录已有 PDEC/SAE/Rankin 验收接口。 | PDECOrSAEUnifiedExclusionLedger AND BatchRankinCertificatesAllPassOrReturnToPDECSAE |
| BadWindowSourceFamilyRecordEmitterClosed | `true` | `true` | 每个来源族都有确定记录发射规则；不存在需要另开类型的无名数据入口。 | BadWindowSourceFamilyRecordEmitterClosed |
| BadWindowSourceFamilyDataExtractionLedger | `true` | `true` | 数据抽取层已压成记录发射器和下一层参数账本；完整 concrete inventory 仍待下游参数填充。 | ComplementAnchorSetAndD0KParameterLedger |
| ConcreteInventoryRecordsStillDownstream | `false` | `false` | 当前没有声称已经提交全部 concrete corridor records；A/D0/K/Omega/color/budget 仍需后续账本。 | ComplementAnchorSetAndD0KParameterLedger AND IntervalGraphColoringCoverageCertificateLedger AND AllowedBudgetAllocationLedger |

## 4. 下一步

当前唯一最窄点更新为 `ComplementAnchorSetAndD0KParameterLedger`。随后才是 `IntervalGraphColoringCoverageCertificateLedger`、`AllowedBudgetAllocationLedger` 与 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

审稿边界：本步只关闭记录发射规则，不提交 concrete inventory 全集，不关闭最终无条件定理。
