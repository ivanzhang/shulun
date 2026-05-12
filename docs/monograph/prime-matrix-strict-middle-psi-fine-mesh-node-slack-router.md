# Prime Matrix strict 中段 psi 细网格节点余量/hash 守门器

**状态：** `fine_mesh_node_contract_closed_sparse_anchors_rejected_node_data_hash_open`

细网格节点余量/hash 的边界现在清楚了：需要覆盖 646258 个百万网格起始节点。Dusart Table 6.2 的稀疏点值虽然强，但在最坏短区间增量传播下只能从每个锚点推出个位数百万网格的安全余量，无法跨越十万级点间缺口。因此节点表或等价可复算 psi 算法/hash 是不可省略输入。

```text
mesh_definition_endpoint_closed=true
sparse_dusart_anchors_cannot_replace_fine_mesh=true
node_table_schema_contract_closed=true
machine_readable_node_table_present=false
middle_psi_fine_mesh_node_slack_floor_hash_closed=false
certified_short_interval_psi_increment_upper_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 网格合同

```text
x_left=8.000000000000000e+11
x_right=1.446257064291475e+12
mesh_h=1.000000000000000e+06
target_ratio=1.000028410000000e+00
required_node_slack_floor=3.073386854526510e+06
start_node_rule=x_i=x_left+i*h for 0<=i<ceil((x_right-x_left)/h), final interval clipped at x_right
mesh_id_sha256=7f24359883a054c7ee18ac1c95a12be33282577cb64836c59ae3759abd442294
start_node_count=6.462580000000000e+05
first_start_node=8.000000000000000e+11
last_start_node=1.446257000000000e+12
final_interval_length=6.429147509765625e+04
regular_endpoint_overshoot=9.357085249023438e+05
required_record_fields=['i', 'x_i', 'psi_upper_or_exact', 'target_ratio_x_i_minus_psi_lower_slack', 'slack_ge_required_floor', 'computation_method', 'directed_rounding_mode', 'source_or_chunk_hash']
```

## 2. 稀疏锚点传播审计

| anchor_x | slack | slack/floor | certified_start_nodes | gap_to_next | uncovered |
| ---: | ---: | ---: | ---: | ---: | ---: |
| `8.000000000000000e+11` | `2.269002072546387e+07` | `7.382741515942197e+00` | `7` | `100000` | `99993` |
| `9.000000000000000e+11` | `2.579176812402344e+07` | `8.391969297987041e+00` | `8` | `100000` | `99992` |
| `1.000000000000000e+12` | `2.836986323474121e+07` | `9.230814270243213e+00` | `9` | `446258` | `446249` |

## 3. 自足替换

```text
MiddlePsiFineMeshNodeSlackFloorAndHashLedger
  =>
DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger AND NodeSlackFloorAuditLedger AND MeshCompletenessAndIndexHashLedger AND MiddlePsiUpperDirectedRoundingLedger

DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger
  =>
machine-readable psi node table or reproducible exact psi computation over the certified mesh

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只补中段解析输入证书，不用真实零行缺席来替代假设反例链。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `MiddlePsiFineMeshNodeSlackGateActive` | `true` | `true` | 短区间增量账本已把百万网格路线的主要缺口压成节点余量和 hash。 | MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `MeshDefinitionAndEndpointLedger` | `true` | `true` | 百万网格端点、起始节点数、最后截断区间和记录字段已经固定。 | none |
| `RequiredNodeSlackFloorImported` | `true` | `true` | 从短区间增量账本继承每个起始节点至少约 3.073386e6 的绝对余量门槛。 | node table must certify every start node above this floor |
| `SparseDusartAnchorsCannotReplaceFineMesh` | `true` | `true` | Table 6.2 的 8e11、9e11、1e12 稀疏锚点在最坏增量传播下只能覆盖个位数百万网格，不能跨越十万级缺口。 | DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger |
| `NodeTableSchemaContractClosed` | `true` | `true` | 节点表必须逐行给出 i、x_i、psi 上界或精确值、余量、舍入模式和分块 hash。 | MeshCompletenessAndIndexHashLedger |
| `MachineReadableNodeTablePresent` | `false` | `false` | 仓库当前未发现覆盖 646258 个起始节点的机器可读 psi 节点表。 | DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger |
| `DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger` | `false` | `false` | 需要 Deléglise-Rivat 数据或等价可复算算法输出，并绑定版本、端点、舍入和 hash。 | external data archive or internal exact psi computation certificate |
| `NodeSlackFloorAuditLedger` | `false` | `false` | 需要逐节点检查 target*x_i-psi(x_i) >= required_node_slack_floor。 | requires machine-readable node table |
| `MeshCompletenessAndIndexHashLedger` | `false` | `false` | 需要证明索引 0..646257 无缺行、无重复、端点截断一致，并给出整体 hash。 | requires canonical table serialization |
| `MiddlePsiUpperDirectedRoundingLedger` | `false` | `false` | 需要外向舍入规则，防止浮点/十进制表值把 4.46e-11 级拼接余量吃掉。 | directed rounding proof |
| `MiddlePsiFineMeshNodeSlackFloorAndHashLedger` | `false` | `false` | 本步关闭了网格合同和稀疏锚点失败审计，但没有节点数据/hash，故节点余量守门仍开放。 | DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger AND NodeSlackFloorAuditLedger AND MeshCompletenessAndIndexHashLedger AND MiddlePsiUpperDirectedRoundingLedger |
| `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger` | `false` | `false` | 即使节点余量未来闭合，短区间总包仍还要 BT 输入和素数幂修正。 | BrunTitchmarshShortIntervalPrimeCountUpperLedger AND PrimePowerShortIntervalCorrectionLedger AND MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 细网格节点合同不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger
```
