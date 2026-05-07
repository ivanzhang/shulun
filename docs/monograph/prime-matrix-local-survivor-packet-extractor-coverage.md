# LocalSurvivor packet extractor 覆盖审计

**状态：** `known_local_survivor_entry_extractors_covered_not_global_proof`

当前所有已知 LocalSurvivor packet 入口均有覆盖：三个机器 extractor 分别处理 Triad-A1 SparseCap、FO-PDEC 二点 SAE/Endpoint、RPZ Endpoint-SAE，聚合总账已清零物化义务；generic SAE、持久签名、升层 clean 和 descent/seam 入口均有合同回流到 PDEC/ColumnCRT/LocalSurvivor/CleanKLS。该子门只关闭已知入口覆盖，不证明未来不会出现新 sparse 入口；剩余是 NewSparseEntryAdmission。

## 1. 总裁定

```text
closed_subgate: KnownLocalSurvivorEntryExtractorsCovered
known_entry_extractor_coverage_closed: true
entry_count: 8
materialized_script_entry_count: 4
contract_entry_count: 4
missing_or_open_count: 0
```

## 2. 覆盖表

| entry | type | route | coverage | fallback |
| --- | --- | --- | --- | --- |
| TriadA1SparseCapExtractor | materialized_script_extractor | DualCap SparseCap -> LocalSurvivor or finite PDEC | covered_closed | FinitePDECAtomBeyondP or LocalSurvivorWitnessAtRowLeP |
| FOPDECTwoAtomSAEEndpointExtractor | materialized_script_extractor | physical two-point PDEC tautology -> SAE/Endpoint | covered_closed | PDEC if persistent, LocalSurvivor witness if sparse |
| RPZEndpointSAEFiniteExtractor | materialized_script_extractor | RPZ endpoint low-load candidate -> SAE finite ledger | covered_closed | Endpoint PDEC or ColumnCRT if global load appears |
| MaterializedPacketLedgerAggregator | materialized_script_extractor | known materialized packets -> combined LocalSurvivor ledger | covered_closed | Close materialized packet before global generation |
| GenericSAELocalWindowContract | contract_route_not_materialized_packet | generic sparse/single-window escape | covered_by_contract_route | packet extractor, persistent PDEC, smaller SAE, or CleanKLS/DLS |
| PersistentSignatureFallbackContract | contract_route_not_materialized_packet | same finite signature repeats in an infinite family | covered_by_contract_route | PDEC/ColumnCRT/TailAnchor/CofactorAnchor |
| LayerEscapeCleanKLSContract | contract_route_not_materialized_packet | signature layer escapes every finite packet | covered_by_contract_route | CleanKLS/DLS or explicit ExternalKLS |
| DescentSeamReturnContract | contract_route_not_materialized_packet | descent/seam route lowers to named packet | covered_by_contract_route | PDEC/LocalSurvivor/ColumnCRT packet after descent |

## 3. 证明读法

这一步把 `packet-generation` 的已知入口从口头列表变成可审计覆盖表。凡是已经物化到机器账本的入口，都必须有脚本、JSON 账本和当前闭合状态；凡是尚未物化为具体窗口的入口，必须有合同把失败回流到 PDEC、ColumnCRT、LocalSurvivor 或 CleanKLS/DLS。

因此当前不能再把已知入口本身当作开放缺口。真正剩余是：证明不存在新的未命名 sparse 入口；或者若新入口出现，必须给出同样的 extractor 和有限 packet schema。

## 4. 剩余

- `NewSparseEntryAdmission: prove no additional unnamed LocalSurvivor entry route exists`
- `PacketExtractorCompleteness for any newly admitted sparse route`
- `NonTautologicalPDEC for >=3 physical atoms or fixed-frequency constraints`
- `CleanKLS/DLS or explicit ExternalKLS for layer-escape branches`
