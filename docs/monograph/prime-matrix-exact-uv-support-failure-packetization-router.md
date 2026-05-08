# Prime Matrix ExactUVSupport 失败包化路由器

**状态：** `exact_uv_support_failure_packetized_packet_exclusion_open`

最后源侧输入被进一步包化：不再把 `ActualNoncanonicalExactUVSupportLowerBound` 当作抽象正下界，而是等价改写为排斥所有 actual noncanonical 支撑失败 packet。这关闭了“支撑失败仍可无名停留”的边界，但当前材料仍未证明 packet 全部不存在或必回流，所以完整无条件行/列命题仍未闭合。

```text
failure_packetization_closed=true
exact_uv_support_proved=false
actual_support_failure_packet_exclusion_proved=false
actual_final_capacity_antiatom_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactSupportTerminalPinned` | `true` | `true` | 上一层已把唯一源侧微输入固定为 ActualNoncanonicalExactUVSupportLowerBound。 | 只能攻击该输入本身，不能回到已排除伪路线。 |
| `RegisteredCapacityAttached` | `true` | `true` | 所有 Type/Fourier/fiber 成本已经登记为同一 formal unit 的 log-power 乘子。 | 支撑失败不能再解释为账外乘子问题。 |
| `FailureEquivalencePacketized` | `true` | `true` | ExactUVSupport 失败等价于存在一个正质量 actual noncanonical clean block，其 exact u/v 支撑乘积低于登记阈值。 | 必须排斥这些 packet，或证明它们回流到已命名出口。 |
| `CanonicalAndGenericEscapeBlocked` | `true` | `true` | canonical RIW/Buchstab 支撑链和 generic WFD 点支撑模型都不能替代该 packet 排斥。 | packet 必须在 actual noncanonical 补集内处理。 |
| `SparseSchemaInterfaceReady` | `true` | `true` | 未来 sparse 路线已经有显式 packet extractor schema 准入规则。 | Actual support-failure packet 是一个新增 source class，仍需证明排斥或提交全集证书。 |
| `NoHiddenSupportFailure` | `true` | `true` | 支撑失败不能继续作为抽象硬点存在；它必须物化为带字段、阈值、回流测试和哈希的 packet。 | 当前材料还没有排斥所有这种 packet。 |
| `ActualSupportFailurePacketExclusionCurrentCorpusProved` | `false` | `false` | 当前材料没有证明所有 actual noncanonical 支撑失败 packet 都不存在或必回流。 | 证明 ActualNoncanonicalSupportFailurePacketExclusion，或给直接 final capacity anti-atom。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧 packet 排斥完成后仍需独立验收。 |

## 2. 等价改写

在已固定 actual noncanonical clean block、exact u/v 支撑定义和 registered multiplier 阈值后，ActualNoncanonicalExactUVSupportLowerBound 等价于不存在正质量 ActualNoncanonicalSupportFailurePacket。

上一层源输入：

```text
ActualNoncanonicalExactUVSupportLowerBound
```

包化后的等价输入：

```text
ActualNoncanonicalSupportFailurePacketExclusion
```

连同独立晋级门，最新完全自足输入基写成：

```text
ActualNoncanonicalSupportFailurePacketExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 支撑失败 packet 准入字段

| field | meaning | why needed |
| --- | --- | --- |
| `source_class` | 固定为 actual noncanonical full-S non-AP balanced source。 | 防止 canonical 支撑链或 generic WFD 模板偷渡。 |
| `formal_unit_id` | 与 registered multiplier discipline 的同一 formal unit 对齐。 | 防止账外 Type/Fourier/fiber 乘子重入。 |
| `block_key` | 记录 P、窗口、dyadic U,V、phase_key、path/tail 标签。 | 使 moving block 不再是无名变量。 |
| `exact_u_support/exact_v_support` | 列出或证明精确 u、v 支撑集合及其绝对权重非零性。 | ExactUVSupport 失败正是这些集合乘积低于阈值。 |
| `support_threshold` | 登记 L^(2A+4C+E) 或更强阈值。 | 与 final M_{u,v} 反原子不等式直接相连。 |
| `registered_capacity_profile` | 给出 packet 内 M_{u,v}、总质量、最大 pair 质量和 log-power 乘子。 | 区分 raw support 失败和最终容量反原子失败。 |
| `return_tests` | 逐项测试 canonical、PDEC、SAE/LocalSurvivor、ColumnCRT、CleanKLS/DLS、外部 KLS。 | 若不能直接排斥 packet，必须回流到已命名出口。 |
| `reproducible_certificate` | 脚本、JSON 字段、范围、哈希和 open_obligation_count。 | 使未来新增 sparse 支撑失败路线不能作为隐藏终端。 |

## 4. 阈值样本

| k | log y | required power | required pair support | failure packet condition |
| ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 17.0 | 185664143359702 | `S_u*S_v < L^17` |
| 4 | 9.21034 | 17.0 | 24699408928878996 | `S_u*S_v < L^17` |
| 5 | 11.5129 | 17.0 | 1096874099498946944 | `S_u*S_v < L^17` |
| 6 | 13.8155 | 17.0 | 24335370598442758144 | `S_u*S_v < L^17` |
| 7 | 16.1181 | 17.0 | 334451684862452432896 | `S_u*S_v < L^17` |
| 8 | 18.4207 | 17.0 | 3237400927126027763712 | `S_u*S_v < L^17` |
| 9 | 20.7233 | 17.0 | 23976697736727197908992 | `S_u*S_v < L^17` |

## 5. 当前结论

若 ExactUVSupport 失败，则失败不再是无名硬点：它必须给出一个 finite sparse packet，携带 source_class、formal_unit_id、block_key、exact u/v 支撑、阈值、容量剖面、回流测试和可复现证书。若不能给出这样的 packet，则支撑失败命题无准入。

本步没有证明 `ActualNoncanonicalSupportFailurePacketExclusion`；它闭合的是准入和等价边界。
要完成源侧自足闭合，下一步必须证明所有这种 packet 不存在、或必回流到 PDEC/SAE/ColumnCRT/CleanKLS/外部 KLS，或直接证明 final capacity anti-atom。
