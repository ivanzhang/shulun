# Prime Matrix square-phase off-band prefix gap shadow selector H lower persistence frontier partition router

**状态：** `persistence_frontier_partition_closed_global_exclusion_open`

本步把唯一代表前沿做成完整分区：324 个物理事件中，24 个来自 12 个固定残基 transport-cell 对，剩余 300 个都是 singleton residue packet，没有第三类未登记持久性。因此最新硬点只剩两门：排斥 transport-cell 全局持久复现，或证明 singleton residue 的 SAE/Rankin 可求和。

```text
physical_record_count=324
transport_cell_physical_record_count=24
singleton_residue_physical_record_count=300
unclassified_physical_record_count=0
partition_identity_closed=true
row_column_unconditional_closed=false
```

## 1. 前沿分区

| class | packets | physical records | global status |
| --- | ---: | ---: | --- |
| `transport_cell_pairs` | 12 | 24 | `open_transport_cell_pdec_or_columncrt` |
| `singleton_residue_packets` | 300 | 300 | `open_singleton_residue_sae_rankin` |

## 2. 结构判断

- 固定残基复现已经全部收缩到 12 个 transport cell 对。
- 非固定残基部分全部是 singleton residue packet；当前没有额外 persistence 类别。
- 全局证明仍需关闭 transport-cell 持久性或 singleton-residue SAE/Rankin。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `frontier_partition_identity` | `closed` | Physical unique-representative events split into recurrent fixed-residue transport-cell records and singleton residue packets. |
| `current_sweep_no_unclassified_persistence` | `closed_on_current_sweep` | On the current sweep every physical event is accounted for by either a transport cell pair or a singleton residue packet. |
| `global_transport_or_singleton_sae_open` | `open` | A global proof must exclude transport-cell persistence or prove singleton-residue SAE/Rankin summability. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FrontierPartitionIdentityClosed` | `true` | `true` | 324 个物理事件被 24 个 transport-cell 事件与 300 个 singleton residue 事件精确分割。 | closed |
| `NoUnclassifiedPersistenceCurrentSweep` | `true` | `false` | 当前扫描没有第三类未登记持久性。 | finite evidence only |
| `TransportCellPersistenceExcluded` | `false` | `false` | 12 个互异 transport cell 仍需全局非持久证明。 | TransportCellPDEC/ColumnCRT |
| `SingletonResidueSAESummabilityProved` | `false` | `false` | 300 个 singleton residue packet 仍需 SAE/Rankin 可求和输入。 | SingletonResidueSAE/Rankin |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步完成前沿分区，不关闭全局行/列命题。 | TransportCellNonPersistenceOrSingletonResidueSAESummability |

## 5. 下一步

- 主攻：`TransportCellNonPersistenceOrSingletonResidueSAESummability`。
- 优先尝试 transport-cell 全局非持久证明；若失败，登记明确 ColumnCRT/PDEC。
- 同步准备 singleton-residue SAE/Rankin 可求和账本。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_persistence_frontier_partition_router.py` | `878b2206a4530bc18ac529f01dde2a968bcf9cdd475636c8cb25ae8e591b3271` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json` | `d1e5ac2f12b542edc86559cbbb8b75f862f1ee02df351a024bc302a4af01427b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json` | `7a6af4c73819b3e86322f0b0e40032dc0e98a3f114eab5b163284c85e2b6f23b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json` | `1f61cb91bbabc3fdccfee381045187a294f0483a73834491189b8d636e585745` |
