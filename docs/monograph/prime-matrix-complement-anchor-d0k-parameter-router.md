# Prime Matrix 互补锚与 D0/K/Omega 参数纪律路由器

**状态：** `complement_anchor_d0k_parameter_discipline_closed_coloring_open`

ComplementAnchorSetAndD0KParameterLedger 的参数纪律已闭合：互补锚集合 A、D0、K、Omega、phase_rule 与 anchor_set_hash 都必须由同一 source tuple 可复算地产生，不能为 Rankin 预算后验调参。剩余不再是参数来源，而是提交区间图着色、同色不相交 intervals 与覆盖等式，即 `IntervalGraphColoringCoverageCertificateLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
complement_anchor_d0k_parameter_discipline_closed=true
formal_colored_corridor_inventory_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
ComplementAnchorSetAndD0KParameterLedger => ComplementAnchorSetAndD0KParameterDisciplineClosed AND IntervalGraphColoringCoverageCertificateLedger.
```

## 2. 参数纪律

| field | discipline | forbidden |
| --- | --- | --- |
| D0 | 由 TailCore/CoreK bucket 的 dyadic core scale 固定，使用半开区间 [D0,2D0)。 | 不能为通过 Rankin 预算而后验移动 dyadic 边界。 |
| K | 由 source record 的 omega 截断固定，sigma_K(d) 使用 omega(d)<=K。 | 不能在同一颜色类内混用多个 K，除非拆成不同 records。 |
| Omega | 由 DCS 高/低重叠二分固定；m(d)>Omega 立即回流 high-overlap defect。 | 不能把高重叠点留在 low-overlap colored corridor 中。 |
| anchor_set_hash | 对规范化 source tuple 与排序后的互补锚集合 A 取哈希，作为可复算来源标识。 | 不能只给口头 anchor set；必须能由 I、D0、A0、phase_rule 复算。 |
| phase_rule | phase(d) 是 source record 携带的有限谓词；若无相位过滤则显式写 identity。 | 不能在 Rankin 失败后临时追加相位过滤来降低计数。 |
| corridor_domain | 每个 a 生成 J_a={d:D0<=d<2D0, ad in I}；低重叠仅保留 m(d)<=Omega 部分。 | 不能把不属于同一 D0/K/Omega tuple 的走廊合并进同一颜色证书。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ComplementAnchorParameterGateActive | `true` | `false` | 上一层已把最窄点推进到互补锚、D0/K/Omega 参数账本。 | ComplementAnchorSetAndD0KParameterLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的证书参数，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FormalInventoryFieldsPinned | `true` | `true` | 正式 inventory 已要求 K、D0、Omega、anchor_set_hash、phase_rule 与 coverage_equation。 | 字段格式无剩余。 |
| TailCoreDyadicSourcePinsD0K | `true` | `true` | TailCoreBucket 已把核心 d 放入唯一 dyadic D0 桶，并固定 omega 截断 K。 | D0/K 不能后验调参。 |
| DCSOverlapThresholdPinsOmega | `true` | `true` | DCS 用 Omega 把高重叠点送回缺陷，低重叠点才允许进入着色走廊。 | Omega 不能用于隐藏高重叠。 |
| CCBPhaseRuleAndRankinObjectPinned | `true` | `true` | CCB 的 sigma_K(d) 明确携带 phase(d)，Rankin 证书对象随该 tuple 固定。 | 预算分配留给下一层。 |
| ComplementAnchorSetAndD0KParameterDisciplineClosed | `true` | `true` | A、D0、K、Omega、phase_rule 与 hash 的来源纪律已固定，不能再后验选择参数。 | ComplementAnchorSetAndD0KParameterDisciplineClosed |
| ComplementAnchorSetAndD0KParameterLedger | `true` | `true` | 参数账本闭合为 canonical tuple 纪律；下一步应提交区间图着色与覆盖等式。 | IntervalGraphColoringCoverageCertificateLedger |
| ConcreteColoringStillDownstream | `false` | `false` | 同色 intervals、覆盖等式和颜色数证书仍未提交。 | IntervalGraphColoringCoverageCertificateLedger |

## 4. 下一步

当前唯一最窄点更新为 `IntervalGraphColoringCoverageCertificateLedger`。随后才是 `AllowedBudgetAllocationLedger` 与 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

审稿边界：本步只固定参数来源纪律，不提交 coloring/budget/Rankin concrete 证书全集。
