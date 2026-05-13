# Prime Matrix strict primitive product Rankin 失败回流包路由器

**状态：** `primitive_rankin_failure_packet_schema_closed_actual_payload_and_clean_residual_open`

`PrimitiveProductRankinFailureReturnPacketLedger` 的当前可闭合部分是回流包字母表、哈希身份与诊断失败 stub：Rankin 失败块若不是热窗口、共同核、PDEC/SAE、固定历史或 carrier-lcm return，就不能留下第六类无名出口，只能成为 clean primitive 分散失败残项。因此本步把硬点压缩为：为 actual 失败行给出 payload，并证明 clean primitive 失败必有更优 sigma 通过 P^0.18 或导出矛盾。全体实际失败包和行/列无条件闭合仍未完成。

```text
primitive_product_rankin_failure_return_packet_schema_closed=true
primitive_product_rankin_failure_return_packet_ledger_closed=false
all_actual_rankin_failure_rows_packeted=false
clean_primitive_dispersion_rankin_failure_excluded_or_sigma_pass_proved=false
row_column_unconditional_closed=false
```

## 1. 失败回流包字母表

| packet_type | trigger | route | status |
| --- | --- | --- | --- |
| `hot_density_return` | 失败块在短乘法窗口或 sibling family 中显示局部密度过载。 | TerminalCoreHotDivisorWindowPDECorSAE / DLSShortWindowSAEBoundOrNamedReturn | named_return_open |
| `common_kernel_return` | 失败块共享低乘子核、固定商型、重复 gcd 或兄弟重叠键。 | CommonKernelReturnCycleDescentOrPDECLedger | free_cycle_excluded_named_exits_open |
| `pdec_sae_return` | 失败块携带 low-mod spike、相位缺陷、ColumnCRT、point-load 或局部幸存 packet。 | PDEC/SAE/ColumnCRT named terminal family | named_return_open |
| `fixed_history_return` | 同 formal unit 下有限历史、商型或 packet 签名持久复现。 | FixedTypeHistoryPDECExclusion / persistent terminal family | persistent_terminal_open |
| `carrier_lcm_return` | no-return guard 被 source-defect、valuation-overflow 或 carrier-lcm 兼容缺陷破坏。 | CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption | budget_or_persistent_terminal_open |

## 2. 非合法终端残项

| residual | definition | forced_next | meaning |
| --- | --- | --- | --- |
| `clean_primitive_failure` | 五类命名回流均不触发，但 Rankin bound 仍大于 P^0.18。 | CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass | 它不能作为第六类无名出口；必须证明存在更优 sigma 通过预算，或推出 clean primitive 分散失败不可能。 |
| `actual_payload_missing` | 失败行只有诊断样本或 schema，没有 actual source_tuple/block witness。 | ActualPrimitiveProductRankinFailurePacketPayloadTable | 只能生成 packet stub；不能把诊断样本升级为全体证明。 |

## 3. 回流包纪律

| law | formula | meaning |
| --- | --- | --- |
| `failed_row_totality` | verdict=return_required -> one named packet or one clean residual witness | 失败行不能静默留在 primitive dispersion。 |
| `packet_hash_stability` | packet_id=H(source_tuple_hash,block_id,sigma,rankin_ratio,packet_type,payload_hash) | 同一 formal unit 下回流身份稳定，不允许后验换包。 |
| `diagnostic_stub_boundary` | diagnostic_only=true -> packet_stub, not actual proof row | 样表只证明字段必要性，不证明全体失败已命名。 |
| `clean_residual_not_terminal` | no named trigger -> CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass | 无触发的 clean primitive 失败是下一证明原子，不是闭合结论。 |
| `counterexample_branch_guard` | Assume EarlyZeroRowWithinP only; empirical absence not used | 仍在反例链内部推导，不调用真实零行缺席。 |

## 4. 诊断失败 stub

| sample_row_id | Y | h0 | sigma | rankin_overbudget_ratio | packet_status |
| --- | ---: | ---: | ---: | ---: | --- |
| sample-1 | 16 | 2310 | 0.1 | 3.935239 | diagnostic_stub_requires_actual_trigger_payload |
| sample-2 | 64 | 2310 | 0.1 | 3.982899 | diagnostic_stub_requires_actual_trigger_payload |
| sample-3 | 64 | 4320 | 0.1 | 6.167526 | diagnostic_stub_requires_actual_trigger_payload |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FailureReturnTargetImported` | `true` | `true` | 上一层 no-return P^0.18 pass/return 已把当前点推进到失败回流包账本。 | PrimitiveProductRankinFailureReturnPacketLedger |
| `P018PassReturnSchemaImported` | `true` | `true` | 每个 no-return dyadic 块已经强制二分为 Rankin pass 或 return_required。 | NoReturnPrimitiveProductRankinP018PassOrFailureReturnTable |
| `ReturnAlphabetForPrimitiveRankinFailureClosed` | `true` | `true` | 热窗口、共同核、PDEC/SAE、固定历史与 carrier-lcm 五类回流覆盖所有非 clean primitive 失败触发。 | PrimitiveProductRankinFailureReturnPacketSchema |
| `PacketHashAndNoPosthocDisciplineClosed` | `true` | `true` | 失败包必须绑定 source tuple、block、sigma、overbudget ratio 与 payload hash。 | canonical packet identity |
| `DiagnosticFailRowsMaterializedAsStubs` | `true` | `true` | 诊断样表中的失败行已变成 packet stub，说明缺包字段不能忽略。 | diagnostic only |
| `ActualAllFailRowsHaveNamedPackets` | `false` | `false` | 尚未给出全体 actual P^0.18 失败行的 payload 与触发分类。 | ActualPrimitiveProductRankinFailurePacketPayloadTable |
| `CleanPrimitiveResidualExcludedOrSigmaPass` | `false` | `false` | 若五类回流均不触发，仍需证明 clean primitive 分散失败会被某个 sigma 压回 P^0.18，或推出矛盾。 | CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass |
| `PrimitiveProductRankinFailureReturnPacketLedgerClosed` | `false` | `false` | 本步关闭 schema/字母表/哈希纪律，但未证明全体实际失败行都已命名或 clean residual 被排除。 | ActualPrimitiveProductRankinFailurePacketPayloadTable AND CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass AND CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一步最窄点

- 主攻：`CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass`。
- 并行保留：`ActualPrimitiveProductRankinFailurePacketPayloadTable`、`PerBlockRankinSigmaSelectionTable`、carrier-lcm return、非持久预算、持久终端族与 DStructure/Rankin 独立验收门。
- 边界：本步不声明全体 actual 失败行已 packeted，也不声明行/列命题无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/primitive-product-rankin-p018-sample-table.json` | `6ee83fd827a289762f17da0e458cc1fb7fcfbe64b862d7b1fef635133f06e551` |
| `docs/monograph/prime-matrix-early-band-local-survivor-return-schema-router.json` | `2d73378013a2c7cbf4c2551ed2393cb1a5d350e73f2fe571f3b0d6d12c1f098d` |
| `docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json` | `a2d4e9a4d5d5f8d377571fc39d9c94e1ddb97d2afae30ef9e4c9e18296677307` |
| `docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.json` | `1dc6e98d6eb37c2571d0c3bdff385f66069b8812c6c1a9c8b97860b37cfc6f95` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json` | `81c12e6ee229ba4dc21688529dc6818e7c9569e2051c3b6617c288169a547cd9` |
| `docs/monograph/prime-matrix-support-failure-packet-return-dichotomy-router.json` | `9c0b1a6aa36b240b6a9cd9772bde88e6e3319e083b90c738573fc28f9a8a5fa7` |
| `experiments/prime_matrix_strict_primitive_product_rankin_failure_return_packet_router.py` | `9d88401ce616674f2d331fd0a807ec6f4643c98323269c795d5e684cb2af16ab` |
