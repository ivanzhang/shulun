# Prime Matrix concrete 锚区间枚举路由器

**状态：** `anchor_interval_formula_closed_certificate_file_open`

ConcreteAnchorIntervalEnumerationLedger 的端点公式与 source tuple 参数已闭合；当前最窄点是 `AnchorIntervalCertificateFileLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
anchor_interval_endpoint_formula_closed=true
concrete_anchor_interval_enumeration_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
ConcreteAnchorIntervalEnumerationLedger => AnchorIntervalEndpointFormulaClosed AND ConcreteSourceTupleAnchorParameterDataLedger AND AnchorIntervalCertificateFileLedger.
```

## 2. 端点公式纪律

| law | formula |
| --- | --- |
| window_membership | ad in [L,R] iff ceil(L/a)<=d<=floor(R/a)。 |
| dyadic_core_clip | d in [D0,2D0) gives left=max(D0,ceil(L/a)), right_excl=min(2D0,floor(R/a)+1)。 |
| phase_filter | phase_rule(d)=true 的点保留；identity phase 必须显式写出。 |
| same_tuple_guard | A、D0、phase_rule、window_id 必须共享同一 source_tuple_hash。 |

## 3. 证书字段

| field | meaning |
| --- | --- |
| formal_unit_id | 假设反例链中同一 formal unit 的稳定编号。 |
| source_tuple_hash | 锁定 P/range、window_id、I=[L,R]、A、D0、phase_rule。 |
| anchor_id | 互补锚 a 的稳定编号。 |
| a | 实际 anchor 值，必须来自 anchor_set_hash 对应的 A。 |
| left_d | max(D0, ceil(L/a))。 |
| right_d_exclusive | min(2D0, floor(R/a)+1)，使用半开整数区间。 |
| phase_filtered_segments | 若 phase_rule 非 identity，记录过滤后的子区间或 residue 条件。 |
| empty_interval_flag | 若 left_d>=right_d_exclusive，则显式登记空区间。 |
| endpoint_proof_hash | 端点公式和 source tuple 的可复算证明哈希。 |

## 4. 当前扫描

- ConcreteSourceTupleAnchorParameterDataLedger: `0`
- AnchorIntervalCertificateFileLedger: `0`

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ConcreteAnchorIntervalGateActive | `true` | `false` | 上一层已把最窄点推进到 concrete anchor interval 枚举。 | ConcreteAnchorIntervalEnumerationLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行反例链，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| UpstreamCoverageSchemaImported | `true` | `true` | coverage 数据已经被拆为锚区间、多重度、着色执行和覆盖等式。 | 本步只处理第一组件。 |
| ParameterDisciplineImported | `true` | `true` | A、D0、phase_rule 与 anchor_set_hash 的来源纪律已固定。 | 不能后验移动参数。 |
| AnchorIntervalEndpointFormulaClosed | `true` | `true` | 给定同一 source tuple，J_a 端点由 ceil/floor 与 [D0,2D0) 裁剪唯一确定。 | AnchorIntervalEndpointFormulaClosed |
| ConcreteSourceTupleAnchorParameterDataAvailable | `true` | `false` | 仓库尚未发现逐 formal unit 的真实 source tuple 参数数据；source tuple 参数账本闭合后该缺席不再阻塞。 | ConcreteSourceTupleAnchorParameterDataLedger |
| ConcreteSourceTupleAnchorParameterDataComplete | `true` | `false` | source tuple 数据必须完整覆盖 P/range、window_id、A、D0、phase_rule；当前由上层闭合账本给出覆盖。 | ConcreteSourceTupleAnchorParameterDataLedger |
| AnchorIntervalCertificateFilesAvailable | `false` | `false` | 仓库尚未发现按端点公式生成的 anchor interval 证书文件。 | AnchorIntervalCertificateFileLedger |
| AnchorIntervalCertificateFilesComplete | `false` | `false` | anchor interval 证书必须逐 anchor 覆盖并携带空区间记录。 | AnchorIntervalCertificateFileLedger |
| ConcreteAnchorIntervalEnumerationLedger | `false` | `false` | 端点公式与 source tuple 参数已闭合；剩余是按公式生成 anchor interval 证书文件。 | AnchorIntervalCertificateFileLedger |

## 6. 下一步

当前唯一最窄点更新为 `AnchorIntervalCertificateFileLedger`；随后才是 `LowOverlapMultiplicityTableLedger`。

审稿边界：本步吸收已闭合 source tuple 参数账本；仍不提交 anchor interval 证书文件，也不关闭行列无条件定理。
