# Prime Matrix 正式着色走廊全集清单合约路由器

**状态：** `formal_corridor_inventory_schema_closed_data_missing`

FormalColoredCorridorInventoryLedger 的 schema 层已闭合：清单必须逐条给出坏窗族、互补锚、D0/K/Omega、同色不相交 intervals、相位规则、预算和覆盖等式。但全量 corridor records 尚未提交，因此正式 inventory 本身仍未闭合。新的最窄输入是从反例链抽取全部坏窗族与走廊来源的 `BadWindowSourceFamilyExtractionLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
formal_corridor_inventory_schema_closed=true
formal_colored_corridor_inventory_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
FormalColoredCorridorInventoryLedger => FormalColoredCorridorInventorySchemaClosed AND BadWindowSourceFamilyExtractionLedger AND ComplementAnchorSetAndD0KParameterLedger AND IntervalGraphColoringCoverageCertificateLedger AND AllowedBudgetAllocationLedger.
```

## 2. 必要字段

| field | meaning |
| --- | --- |
| family_id | 坏窗族或分支家族的稳定编号。 |
| color_id | 区间图着色后的颜色编号。 |
| P_or_P_range | 该证书覆盖的素数或素数范围。 |
| K | smooth squarefree core 的 omega 截断。 |
| D0 | 核心尺度，所有 d 走廊落在 [D0,2D0)。 |
| Omega | 低重叠阈值；高重叠分支必须回流 PDEC/SAE。 |
| anchor_set_hash | 互补锚集合 A 的可复算来源哈希。 |
| intervals | 同色两两不交的 [A_j,B_j] 整数走廊。 |
| phase_moduli | 低模相位检查模数，例如 30、210 或正式指定模数。 |
| phase_rule | sigma_K(d) 中 phase(d) 的有限判定规则。 |
| allowed_budget | 该颜色类可用预算，供 Rankin 证书验收。 |
| coverage_equation | 证明这些 intervals 正好覆盖该颜色类低重叠走廊。 |
| failure_return | Rankin 失败时回流 PDEC/SAE 或常数调参的路径。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FormalInventoryGateActive | `true` | `false` | 上一层唯一最窄点是正式着色走廊全集清单。 | FormalColoredCorridorInventoryLedger |
| DistributedCorridorSourceLawAvailable | `true` | `true` | DCS-1 已把分布式走廊饱和拆成高重叠缺陷或低重叠着色走廊。 | 无结构二分剩余。 |
| ColoredCorridorRankinLawAvailable | `true` | `true` | CCB-1 已把每个颜色类预算写成 finite Rankin 或 low-mod core CRTDefect。 | 无 Rankin 逻辑格式剩余。 |
| FinalExitContractAvailable | `true` | `true` | FXA-3 已规定 Rankin 失败必须回流 PDEC/SAE 或保留常数缺口。 | PDECOrSAEUnifiedExclusionLedger |
| InventorySchemaClosed | `true` | `true` | 正式清单字段、覆盖等式和失败回流字段已经足以定义可审稿 inventory。 | FormalColoredCorridorInventorySchemaClosed |
| InventoryDataStillMissing | `false` | `false` | 清单 schema 已闭合，但仓库仍没有正式反例链诱导出的全量 corridor records。 | BadWindowSourceFamilyExtractionLedger |
| FormalColoredCorridorInventoryLedger | `false` | `false` | FormalColoredCorridorInventoryLedger 不能由 schema 单独关闭；仍需提交全量数据和来源证明。 | BadWindowSourceFamilyExtractionLedger AND ComplementAnchorSetAndD0KParameterLedger AND IntervalGraphColoringCoverageCertificateLedger AND AllowedBudgetAllocationLedger |
| BatchRankinStillDownstream | `false` | `false` | inventory 数据齐备后，才可逐条执行 Rankin 审计并处理失败回流。 | BatchRankinCertificatesAllPassOrReturnToPDECSAE |

## 4. 下一步

当前唯一最窄点更新为 `BadWindowSourceFamilyExtractionLedger`。随后依次是 `ComplementAnchorSetAndD0KParameterLedger`、`IntervalGraphColoringCoverageCertificateLedger`、`AllowedBudgetAllocationLedger`；再之后才进入 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。
