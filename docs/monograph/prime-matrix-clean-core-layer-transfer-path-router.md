# Prime Matrix clean-core 层转移路径分割路由器

**状态：** `clean_core_layer_transfer_reduced_to_path_partition_open`

最新真正剩余继续缩小为 clean-core actual 系数的路径分割账本：证明其有 polylog 多条互斥路径、同路径非零/无抵消，并把薄块或路径失败回流到命名出口。当前材料尚未证明该账本。

```text
clean_core_layer_transfer_path_boundary_closed=true
clean_core_path_partition_proved=false
clean_core_exact_layer_transfer_proved=false
external_completed_kls_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorLayerTransferInputPinned` | `true` | `false` | 上一层已把支撑关联压成 clean-core exact 层承认、非零转移与薄块回流。 | 继续拆解层承认到底需要哪类系数结构。 |
| `LayerTransferReducesToSelectorRetention` | `true` | `false` | 层承认和非零转移可由 selector 保留率加 clean return 合同推出。 | 为 actual clean-core 系数给出 selector/path 账本。 |
| `SelectorRetentionReducesToFinitePathSignatures` | `true` | `false` | 若 raw support 被 polylog 多个 exact 路径签名分割，则最大签名保留 log-power 支撑。 | 证明 clean-core actual 路径分割、无抵消和失败回流。 |
| `CanonicalDecisionTreeTemplateAvailable` | `true` | `false` | canonical RIW/Buchstab 递归可展开为有限互斥决策树。 | 这只是模板，仍需 actual clean-core 系数来源或独立路径公式。 |
| `FormalWFDSourceRejected` | `true` | `true` | 仅有 well-factorable 性质不能推出 source entropy 或路径支撑。 | clean-core 不能用 generic WFD 形式假设冒充路径账本。 |
| `CanonicalProvenanceClosedButScoped` | `true` | `true` | canonical 来源账本已闭合，但只覆盖 canonical 分支，不覆盖 noncanonical clean-core。 | clean-core 要么证明自己的实际系数路径分割，要么转外部/回流。 |
| `CleanCorePathPartitionCurrentCorpusProved` | `false` | `false` | 当前材料没有给出 actual clean-core 系数的有限路径分割、同路径非零和薄块回流合同。 | 证明 CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn。 |
| `ExternalCompletedKLSStillOpen` | `true` | `false` | 外部替代仍是 modulus-dependent completed Full-S KLS。 | 证明或独立接受该 completed KLS 输入。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 路径分割律

若 actual clean-core 系数能被分割为 polylog 多个互斥 exact 路径签名，且每条路径同号或非零，则 pigeonhole 给出 selector retention；再结合 raw Buchstab support 与 thin/rejected return，即可推出 clean-core exact layer transfer。

## 3. 作用域律

canonical RIW/Buchstab 决策树和来源账本已经闭合，但只在 canonical-source 分支内有效。clean-core noncanonical 残余不能导入该来源；它必须给出自己的 actual coefficient path partition，或走 completed KLS/命名回流。

## 4. 最新输入基

条件输入基：

```text
(CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn OR ModulusDependentCompletedFullSKLSInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

`CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn` 要求：

- actual clean-core `alpha/delta` 系数在同一 formal unit 中有 exact 路径签名分割；
- 路径签名数量为 polylog，足以用 pigeonhole 保留 log-power 支撑；
- 同路径贡献非零且无抵消，或进一步细分直到互斥；
- thin、路径超预算、抵消或来源失败必须回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部 KLS。

## 5. 保留率模型

| k | log y | raw support | path count | retained support | required support | suffices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 15728.4 | 47.7171 | 329.618 | 329.618 | `True` |
| 4 | 9.21034 | 66279.4 | 84.8304 | 781.317 | 781.317 | `True` |
| 5 | 11.5129 | 202269 | 132.547 | 1526.01 | 1526.01 | `True` |
| 6 | 13.8155 | 503309 | 190.868 | 2636.94 | 2636.94 | `True` |
| 7 | 16.1181 | 1.08785e+06 | 259.793 | 4187.37 | 4187.37 | `True` |
| 8 | 18.4207 | 2.12094e+06 | 339.321 | 6250.53 | 6250.53 | `True` |
| 9 | 20.7233 | 3.822e+06 | 429.454 | 8899.68 | 8899.68 | `True` |

## 6. 当前结论

本步没有证明 clean-core 路径分割账本；它把层承认/非零转移硬点压成了一个可审稿的
actual coefficient path-partition 合同，并明确 canonical 决策树不能跨分支偷渡。
