# NewSparseEntryAdmission 审计

**状态：** `no_additional_unnamed_local_survivor_entry_route_not_global_proof`

无名 sparse 入口在当前合同体系中已经没有独立位置：短窗、endpoint、Bohr-cap、tail/cofactor、descent/seam 都被命名到 SAE/LocalSurvivor/PDEC/ColumnCRT；同签名持久复现不是 sparse，而是 PDEC/ColumnCRT/TailAnchor/CofactorAnchor；层级逃逸不是 sparse，而是 CleanKLS/DLS admission。结合已知 extractor 覆盖，当前剩余不再是 NewSparseEntryAdmission，而是未来若新增显式 sparse 路线时必须提交 extractor schema。

## 1. 总裁定

```text
closed_subgate: NoAdditionalUnnamedLocalSurvivorEntryRoute
known_extractors_closed: true
no_additional_unnamed_local_survivor_entry_route: true
admission_source_count: 8
missing_admission_count: 0
```

## 2. 准入表

| source | class | verdict | target route |
| --- | --- | --- | --- |
| ShortWindowOrEndpointSparse | Sparse | admitted_named_route | LocalSurvivor packet extractor or SAE-Cert |
| PDECDualSparseCap | SparseFromPDECDualFailure | admitted_named_route | LocalSurvivor packet or refined PDEC |
| EndpointSeamSparse | EndpointSeam | admitted_named_route | Endpoint PDEC, ColumnCRT, or SAE packet |
| BohrCapSparse | BohrCap | admitted_named_route | SAE packet or persistent PDEC/ColumnCRT |
| ColumnTailCofactorSparse | ColumnTailCofactor | admitted_named_route | Tail/Cofactor PDEC or SAE packet |
| DescentSeamSparse | DescentSeam | admitted_named_route | named PDEC/LocalSurvivor/ColumnCRT packet |
| PersistentSignatureNotSparse | Persistent | admitted_named_route | PDEC/ColumnCRT/TailAnchor/CofactorAnchor |
| LayerEscapeNotSparse | Flat | admitted_named_route | CleanKLS/DLS or ExternalKLS |

## 3. 证明读法

这一步只处理“是否还有未命名的新 LocalSurvivor 入口”。答案是：在当前合同体系内没有。所有能产生孤立窗口的来源都已命名到 SAE/LocalSurvivor/PDEC/ColumnCRT；所有不能保持孤立的来源都转成持久签名或 clean 平坦分支。

因此下一步若有人提出新的 sparse 路线，它必须作为显式新入口提交，并附带同样的 packet extractor、字段 schema、fallback 规则和机器账本；否则它不是合法终端。

## 4. 剩余

- `PacketExtractorCompleteness for any future explicitly admitted sparse route`
- `NonTautologicalPDEC for >=3 physical atoms or fixed-frequency constraints`
- `CleanKLS/DLS or explicit ExternalKLS for layer-escape branches`
- `D-structure/Tail-log4/Rankin referee inputs for final theorem promotion`
