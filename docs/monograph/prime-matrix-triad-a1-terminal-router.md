# Triad-A1 终端证书路由器

**状态：** `terminal_routes_materialized_not_terminal_certificates`

当前已物化层全部路由为 LiftFiberDeletion，尚未产生可提交的 PDEC 或 CleanKLS 实例。这不是停顿：它说明当前分支仍在删除势账本中推进；未来若删除停止，路由器会强制转入三终端证书。

## 1. 路由律

FiberDeletion 行继续累计删除势；NoDeletion+KL 偏斜进入 PDEC；NoDeletion+低 KL 进入 CleanKLS；口径缺失回到 formal unit/Stitching。

```text
FiberDeletion              => ContinueLiftOrSparse；
NoDeletionKLPDEC           => Triad-A PDEC；
NoDeletionCleanKLSCandidate=> Triad-C CleanKLS；
NoDeletionMixedKL          => refine cap / next layer, then A or C；
MissingKLInput             => formal unit/Stitching gap。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `terminal_router_script` | `b9dbc76d793e6570a1b85ac8e059999ec9c916d990c6de205894c8b329a67d08` |
| `nodeletion_kl_gate_json` | `5cbfa7c96f19c0ab178eb0810492383509edc23daf205f7a3f823986ecff755f` |
| `infinite_tower_budget_json` | `5d31543f88f0dcac735a61dff0d26d836d0ad038dda7895c109674279bc79082` |
| `newlayer_tower_gate_json` | `c59e17f45bd93129864e54c07eb5c27a5fbb96bdd6fe1fdedcff94a7d5249597` |

## 3. 总计

- `current_terminal_claim=current_layers_all_deleting`。
- `route_counts={'LiftFiberDeletion': 6}`。
- `triad_counts={'ContinueLiftOrSparse': 6}`。

## 4. 明细

| layer | P | gate | route | triad | survival | drop | path survival | path D | obligation |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 17 | `FiberDeletion` | `LiftFiberDeletion` | `ContinueLiftOrSparse` | 0.0769231 | 13 | 0.0769231 | 2.56495 | 继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。 |
| Q=2310->30030 | 19 | `FiberDeletion` | `LiftFiberDeletion` | `ContinueLiftOrSparse` | 0.202198 | 4.94565 | 0.016031 | 4.13323 | 继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。 |
| Q=2310->30030 | 23 | `FiberDeletion` | `LiftFiberDeletion` | `ContinueLiftOrSparse` | 0.310345 | 3.22222 | 0.0505539 | 2.98472 | 继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。 |
| Q=2310->30030 | 29 | `FiberDeletion` | `LiftFiberDeletion` | `ContinueLiftOrSparse` | 0.312821 | 3.19672 | 0.312821 | 1.16213 | 继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。 |
| Q=30030->510510 | 19 | `FiberDeletion` | `LiftFiberDeletion` | `ContinueLiftOrSparse` | 0.0792839 | 12.6129 | 0.016031 | 4.13323 | 继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。 |
| Q=30030->510510 | 23 | `FiberDeletion` | `LiftFiberDeletion` | `ContinueLiftOrSparse` | 0.162896 | 6.13889 | 0.0505539 | 2.98472 | 继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。 |

## 5. 当前边界

当前路由没有给出最终证明，因为 `LiftFiberDeletion` 仍需无限塔删除势发散或后续 NoDeletion 分支证书。
但它关闭了一个重要漏洞：新增层结果不会散落为临时解释，必须进入同一个终端三证书接口。
