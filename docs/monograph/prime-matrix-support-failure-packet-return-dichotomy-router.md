# Prime Matrix 支撑失败 packet 回流二分路由器

**状态：** `support_failure_packet_return_dichotomy_closed_clean_core_open`

支撑失败 packet 的回流字母表已闭合：孤立、持久、列位移和漂移四类都不能成为新的隐藏终端。源侧最窄剩余进一步压成 clean-core support-failure packet 排斥。当前材料仍未证明该 clean-core packet 不存在，所以完整无条件行/列命题仍未闭合。

```text
support_failure_packet_return_dichotomy_closed=true
clean_core_packet_exclusion_proved=false
actual_final_capacity_antiatom_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SupportFailurePacketInputPinned` | `true` | `true` | 上一层已把 ExactUVSupport 失败物化为支撑失败 packet 排斥。 | 审查 packet 是否可作为新终端停留。 |
| `FiniteSparsePacketRouteClosed` | `true` | `true` | 孤立有限 packet 必须成为 LocalSurvivor/SAE 证书或显式 future sparse schema。 | 不是源侧 clean-core 微输入。 |
| `PersistentSignatureRouteClosed` | `true` | `true` | 持久有限签名必须进入显式 primitive PDEC schema。 | 未来 PDEC 需另交全集证书；不能作为隐藏支撑失败终端。 |
| `ColumnDisplacementRouteClosed` | `true` | `true` | ColumnCRT/位移/endpoint/cofactor 负载已吸收到 PDEC 或 SAE。 | 列缺陷不是第三类独立源侧终端。 |
| `DriftingBlockRouteClosed` | `true` | `true` | 所有有限签名都不持久时，只能进入 CleanKLS/DLS、exact source entropy 或外部 KLS。 | generic CleanKLS 不能偷渡为自足证明。 |
| `ReturnAlphabetComplete` | `true` | `true` | 支撑失败 packet 的非 clean-core 出口已被有限包、持久签名、列位移、漂移块和阻断逃逸覆盖。 | 只剩通过全部回流测试的 clean-core packet。 |
| `CleanCorePacketExclusionCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 clean-core support-failure packet 不存在。 | 证明 ActualNoncanonicalCleanCoreSupportFailurePacketExclusion，或直接 final capacity anti-atom。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧 clean-core 完成后仍需独立验收。 |

## 2. 回流律

任意 ActualNoncanonicalSupportFailurePacket 若不是 clean-core packet，就必须按有限孤立 packet、持久有限签名、ColumnCRT/位移、漂移 CleanKLS/DLS 或已阻断逃逸之一回流；因此它不能作为第五类终端。

## 3. 完备回流字母表

| branch | trigger | route | new terminal |
| --- | --- | --- | --- |
| `IsolatedFinitePacket` | 有限窗口内可抽取 witness 或 blocker-deficit，但签名不持久。 | LocalSurvivor/SAE packet certificate | `false` |
| `PersistentFiniteSignature` | 同一 block_key 或其有限投影签名在无穷层持久复现。 | FutureExplicitPrimitivePDECSchema | `false` |
| `ColumnOrDisplacementLoad` | 失败 packet 的负载固定位移、列半径或 endpoint/cofactor 坐标。 | ColumnCRT absorbed into displacement/endpoint/cofactor PDEC or SAE | `false` |
| `DriftingMovingBlock` | 所有有限签名都不持久，moving block 随尺度漂移。 | CleanKLS/DLS, exact source entropy, or explicit external KLS | `false` |
| `CanonicalOrGenericEscape` | 试图调用 canonical RIW/Buchstab 支撑或 generic WFD 点支撑模板。 | blocked by previous ExactUVSupport terminal audit | `false` |
| `CleanCorePacket` | 以上所有回流测试均不触发，仍有正质量 actual noncanonical 支撑失败。 | ActualNoncanonicalCleanCoreSupportFailurePacketExclusion | `true_source_microinput` |

## 4. clean-core 定义

clean-core support-failure packet 是通过所有回流测试后仍保留的正质量 actual noncanonical full-S non-AP balanced block：同 formal unit、低于 exact u/v 支撑阈值、无 canonical 导入、无有限 sparse witness、无持久 PDEC 签名、无列位移缺陷、也未进入外部或 generic CleanKLS。

## 5. 最新输入基

上一层：

```text
ActualNoncanonicalSupportFailurePacketExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

当前源侧最窄微输入：

```text
ActualNoncanonicalCleanCoreSupportFailurePacketExclusion
```

连同独立晋级门：

```text
ActualNoncanonicalCleanCoreSupportFailurePacketExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 当前结论

本步没有证明 clean-core packet 排斥；它闭合的是支撑失败 packet 的回流完备性。
下一步必须证明 `ActualNoncanonicalCleanCoreSupportFailurePacketExclusion`，或直接证明 final capacity anti-atom。
