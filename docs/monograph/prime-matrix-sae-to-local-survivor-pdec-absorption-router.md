# Prime Matrix SAE 到 LocalSurvivor/PDEC 吸收路由器

**状态：** `sae_independent_terminal_absorbed_current_contract_remainder_pdec_plus_future_schema`

SAE 独立终端已吸收到 LocalSurvivor packet 证书、PDEC 持久签名回流和 CleanKLS/DLS 层级逃逸接口。第一包当前不再有独立 SAE 终端；剩余核心是广义 PDEC 证书族，以及未来若新增显式 sparse 路线时必须同时提交 extractor schema。

## 1. 吸收律

SAE 不是独立终端族。任意 sparse/single-window escape 必须先输出有限 LocalSurvivor packet，并给出 witness 或 blocker-deficit 数据；否则若有限签名持久复现，就变成 PDEC/ColumnCRT/TailAnchor/CofactorAnchor；若签名层级逃逸，就进入 CleanKLS/DLS admission。当前已物化 LocalSurvivor 包已经耗尽，所有已知 sparse 入口都有命名 extractor 或 fallback 路由。因此未来若出现新的 sparse 路线，它是显式 schema 义务，不是隐藏的第三终端。

```text
sae_independent_terminal_removed=true
terminal_package_fully_proved=false
row_column_unconditional_closed=false
```

## 2. 审查表

| gate | closed | evidence | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalTwoFamilyRemainderBeforeSAE` | `true` | ColumnCRT absorption router | 上一轮已经把第一包压成 SAE 与广义 PDEC 两族。 | decide whether SAE is genuinely independent |
| `SAELocalReduction` | `true` | prime-matrix-sae-local-certificate-reduction | 孤窗逃逸只能给 LocalSurvivor packet，或因持久/阻塞集中回流 PDEC、下降或 clean。 | fill finite packet or route persistent signature |
| `MaterializedLocalSurvivorPacketsExhausted` | `true` | local survivor materialized packet ledger | 当前已物化的 LocalSurvivor/SAE 包没有开放局部义务。 | not a proof for future unaudited sparse packets |
| `KnownEntryExtractorsCovered` | `true` | local survivor packet extractor coverage | 已知 LocalSurvivor 入口均有脚本或合同 extractor。 | new explicit sparse route must bring its own schema |
| `NoAdditionalUnnamedSparseEntry` | `true` | new sparse entry admission audit | 当前合同体系内没有额外无名 sparse/LocalSurvivor 入口。 | future new route is an explicit new input, not hidden terminal |
| `PacketGenerationDichotomy` | `true` | local survivor packet generation contract | 无法抽取为有限 packet 时，同签名持久化进入 PDEC，层级逃逸进入 CleanKLS/DLS。 | PDEC exclusion or noncanonical/external clean input |
| `PersistentSparseFallbackAdmitted` | `true` | persistent terminal admission router | 持久 sparse fallback 不能停在 SAE，必须通过 primitive/non-tautological PDEC 准入边界。 | primitive/non-tautological PDEC family |

## 3. SAE 吸收后的第一包剩余

- PDEC family：包含 endpoint / displacement / cofactor / primitive / non-tautological 证书
- FutureExplicitSparsePacketExtractorSchema：若未来新增真正 sparse 路线，必须同步提交 extractor schema

## 4. 判定

`SAE` 的正确边界不是“所有未来孤窗已直接证明不存在”，而是：它不能作为独立终端。一旦孤窗可以抽取为有限 packet，就必须给出 LocalSurvivor witness 或覆盖亏损；一旦同一有限签名持久复现，就回流 PDEC/ColumnCRT/TailAnchor/CofactorAnchor；一旦签名层级逃逸，就进入 CleanKLS/DLS 或外部输入包。当前已物化 packet 和已知入口已经清零，所以第一包的结构剩余压到广义 PDEC 证书族和未来显式 sparse schema 义务。
