# Prime Matrix 坏窗来源族抽取路由器

**状态：** `bad_window_source_family_taxonomy_closed_data_missing`

BadWindowSourceFamilyExtractionLedger 的 taxonomy 层已闭合：假设早期零行反例诱导的端点、尾锚、高重叠核心、低重叠着色走廊、smooth-core 低模尖峰、sparse 单窗逃逸以及 Rankin 无尖峰常数缺口，都已经落入有限命名来源族。但仓库尚未提交逐 formal unit 的全量来源记录，因此完整来源族抽取账本仍未闭合。新的唯一最窄点是 `BadWindowSourceFamilyDataExtractionLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
bad_window_source_family_taxonomy_closed=true
bad_window_source_family_extraction_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
BadWindowSourceFamilyExtractionLedger => BadWindowSourceFamilyTaxonomyClosed AND BadWindowSourceFamilyDataExtractionLedger.
```

## 2. 来源族表

| family_id | trigger | formal_payload | route | inventory_role |
| --- | --- | --- | --- | --- |
| EndpointSawtoothDirectedCRTDefect | BK-DEC 端点 sawtooth 块投影超过预算。 | 低模 Q、非零端点测试函数 F、坏窗相位 tau(x)。 | persistent -> PDEC-Cert; sparse -> SAE-endpoint。 | 登记 endpoint bad-window family；不生成 corridor intervals。 |
| TailAnchorConcentration | 同一互补锚 a 的走廊承担过大 TailCoreBucket 质量。 | anchor a、低模相位 rho_Q(a)、饱和阈值 theta、窗口 I。 | single-anchor -> SAE-anchor; persistent phase -> PDEC/Directed CRTDefect。 | 登记 tail-anchor bad-window family；若转入分布式则继续生成 corridor 源。 |
| HighOverlapFixedCoreDefect | 分布式走廊中固定核心 d 被过多互补锚复用。 | fixed core d、overlap m(d)>Omega、锚短窗 [L/d,R/d]。 | Tail-anchor 或 low-mod CRTDefect，再并入 PDEC/SAE。 | 登记 high-overlap return；不能伪装成低重叠 colored corridor。 |
| ColoredDisjointCorridorBudgetViolation | 低重叠走廊经区间图着色后，某颜色类核心筛预算超标。 | color_id、intervals、K、D0、Omega、phase_rule、allowed_budget。 | Rankin pass -> closed; Rankin fail -> low-mod core spike or constant ledger。 | 正式 corridor inventory 的主体记录来源。 |
| SmoothCoreLowModCRTDefect | Rankin/模型预算失败伴随 smooth-core residue spike。 | 低模 Q、residue b、中心化计数 g(b)、core 测试函数。 | persistent -> PDEC-Cert; isolated -> SAE-core。 | 登记 failed Rankin 颜色类的 PDEC/SAE 回流原因。 |
| SparseSingleWindowEscape | 统一低模缺陷的坏窗集合非空但低于 persistent 阈值 beta。 | single window I、survivor/lift/higher-defect 三选一证书。 | SAE-Cert；若 lift 或 higher-defect 成立则回流 PDEC/SAE 主接口。 | 登记 sparse bad window 的有限 SAE 义务。 |
| RankinConstantGapNoSpike | Rankin 颜色类超预算，但没有可登记的 low-mod spike。 | 失败颜色类、s、Q、ledger、allowed_budget、细分或调参说明。 | 不是坏窗证书；保留为常数/参数账本未闭合。 | 必须显式失败回流，不能被计作 PDEC/SAE 已排除。 |

## 3. 下一步数据字段

| field | meaning |
| --- | --- |
| source_family_id | 必须属于本路由器列出的有限来源族。 |
| formal_unit_id | 同一反例链中的 formal unit 编号，禁止跨口径拼接。 |
| P_or_P_range | 该记录适用的素数或素数范围。 |
| window_id | 坏窗、边界帽、走廊或颜色类的稳定编号。 |
| low_modulus_Q | 触发低模缺陷时使用的模数；无则写 null 并说明。 |
| phase_key | 相位、residue、anchor 或 fixed-core 键。 |
| test_function_id | endpoint/core/tail-anchor 对应的有限测试函数编号。 |
| branch_type | persistent、sparse、rankin_pass、rankin_fail 或 constant_gap。 |
| corridor_payload | 若为 colored corridor，必须给 intervals/K/D0/Omega/color_id。 |
| failure_return | PDEC、SAE、Rankin、constant-gap 或 downstream anchor/color/budget。 |
| source_hash | 可复算来源文件或证书哈希。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BadWindowSourceFamilyGateActive | `true` | `false` | 上一层正式 corridor inventory 已把当前最窄点设为坏窗来源族抽取。 | BadWindowSourceFamilyExtractionLedger |
| EndpointSourceFamilyRegistered | `true` | `true` | BK 端点 sawtooth 超预算已命名为 Directed Endpoint CRTDefect，并进入 PDEC/SAE。 | 无 endpoint 来源族命名剩余。 |
| TailAnchorAndHighOverlapFamiliesRegistered | `true` | `true` | TailCore 分支已拆成尾锚、分布式走廊；尾锚持续化后进入 SAE 或 PDEC。 | 无 tail-anchor 来源族命名剩余。 |
| DistributedCorridorFamiliesRegistered | `true` | `true` | 分布式走廊饱和已拆成高重叠固定核心或低重叠着色走廊预算。 | 无 distributed corridor 来源族命名剩余。 |
| RankinAndLowModFamiliesRegistered | `true` | `true` | 着色走廊预算失败要么是 finite Rankin 账本缺口，要么是 low-mod core CRTDefect。 | 无 core/Rankin 来源族命名剩余。 |
| PersistentSparseInterfaceRegistered | `true` | `true` | 任意命名低模缺陷已统一为 persistent PDEC 或 sparse SAE 验收接口。 | 最终 PDEC/SAE 证书仍未全集提交。 |
| PDECUpperConstraintInputsNamed | `true` | `true` | PDEC 上界需使用 mirror、column、tail-anchor、core-overlap 与 Rankin-routing 五类约束。 | 仍需逐实例数据和对偶证书。 |
| BadWindowSourceFamilyTaxonomyClosed | `true` | `true` | 所有坏窗/走廊来源已经落入有限命名族；不存在新的无名来源类型。 | BadWindowSourceFamilyTaxonomyClosed |
| BadWindowSourceFamilyDataAvailable | `false` | `false` | 扫描仓库是否已有正式反例链诱导的全量坏窗来源族记录；当前未发现。 | BadWindowSourceFamilyDataExtractionLedger |
| BadWindowSourceFamilyExtractionLedger | `false` | `false` | 来源族 taxonomy 已闭合，但抽取 ledger 本身必须提交逐记录数据后才能关闭。 | BadWindowSourceFamilyDataExtractionLedger |

## 5. 审稿边界

当前唯一最窄点更新为 `BadWindowSourceFamilyDataExtractionLedger`。只有提交全量来源记录后，才可进入 `ComplementAnchorSetAndD0KParameterLedger`、`IntervalGraphColoringCoverageCertificateLedger`、`AllowedBudgetAllocationLedger` 与 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

这一步没有关闭 PDEC-Cert、SAE-Cert、DStructure/Rankin 独立验收门，也没有关闭行列无条件定理。
