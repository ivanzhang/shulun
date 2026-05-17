# Prime Matrix cycle-debt fresh-modulus tail-sieve strict 自足同步路由器

**状态：** `fresh_modulus_tail_sieve_strict_self_contained_synced_fresh_layer_pdec_open`

本步把 branch-replay fresh-modulus 分支中旧的 strict tail-sieve 开口同步到最新解析前沿。上一桥接已把 non-PDEC 无界 fresh layers 接到 B3 避单余类粗筛对象；后续 strict Mertens/PNT+B1 证书与 B3-TV 同步证书已关闭该尾段解析出口。因此 branch-replay 的最新剩余不再是 tail-sieve stability，而是 fresh-layer PDEC/ColumnCRT 排斥。

```text
previous_hardpoint=FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure
previous_tail_object_interface_closed=true
previous_non_pdec_unbounded_fresh_layers_force_tail_rough_object=true
previous_conditional_external_tail_sieve_closed=true
previous_strict_tail_sieve_closed=false
strict_self_contained_mertens_tail_proved_latest=true
b3_tv_strict_self_contained_synchronized_latest=true
strict_self_contained_tail_sieve_closed_for_branch_replay=true
fresh_layer_pdec_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=FreshLayerPDECColumnCRTExclusion
```

## 1. 同步逻辑

上一 fresh-modulus 桥接把 non-PDEC 无界 fresh layers 转成 B3 避单余类粗筛对象，但当时 strict 路线仍把 `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372` 作为开放粗原子。后续 strict 速率尾段同步证书已经把 theta/PNT 包络与 Meissel-Mertens B1 常数区间导入，并标记 Mertens 尾段解析包已从活动剩余移出；终端预算最新同步同时确认 B3-TV 自足同步完成。

因此 branch-replay 这条分支内，tail-sieve stability 出口不再是活动剩余；剩余集中到 fresh-layer PDEC/ColumnCRT。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousFreshTailBridgeImported | `true` | `true` | 上一证书已把 non-PDEC 无界 fresh layers 接到 B3 避单余类 tail rough object。 | FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure |
| OldSelfContainedDusartAtomWasOpenInBridge | `true` | `true` | 上一桥接中 strict tail-sieve 的唯一解析粗原子仍登记为 SelfContainedDusart... | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| StrictMertensTailClosedByLatestSync | `true` | `true` | 后续 strict 速率尾段同步已导入 theta/PNT 包络与 B1 区间，Mertens 尾段解析包从活动剩余移出。 | closed |
| B3TVStrictSelfContainedSynchronized | `true` | `true` | 终端预算最新同步确认 B3-TV 的 Stieltjes 边界结构、20000 锚点预算与自足 Mertens 尾段已合并。 | closed for tail-sieve branch |
| StrictTailSieveStabilityBranchClosedForBranchReplay | `true` | `true` | 在上一桥接对象接口、B3-TV 同步和 Mertens 尾段自足闭合同时成立后，branch-replay 的 tail-sieve stability 出口移出剩余基。 | closed |
| FreshLayerPDECExitStillRequiresExclusion | `false` | `false` | 剩余反例链只能在某个 fresh layer 产生相位复用、投影碰撞、moving support 逃逸或 ColumnCRT 缺陷；该 PDEC/ColumnCRT 出口尚未排斥。 | FreshLayerPDECColumnCRTExclusion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步关闭的是 branch-replay 的 strict tail-sieve stability 出口；行/列全局还需 fresh-layer PDEC 排斥及其它全局终端门。 | FreshLayerPDECColumnCRTExclusion |

## 3. 剩余基

旧 branch-replay strict 剩余基：

```text
FreshLayerPDECColumnCRTExclusion AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372
```

新 branch-replay strict 剩余基：

```text
FreshLayerPDECColumnCRTExclusion
```

继承的全局 strict 剩余基仍为：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本同步不宣称行/列命题闭合；它只从 branch-replay 子分支中移除旧 Mertens/PNT tail-sieve 出口。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json` | `8f3ccb352887f8f95a3b670393db3993fa68495ba482d727309eca2e6cebc459` |
| `docs/monograph/prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json` | `41ecd4cfd58beb65c2ec5e1b5fdf2119ec46954e790ed0f036f92b66bfc282d4` |
| `docs/monograph/prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json` | `81ec38d8b42838b270454600184d385487f3c5453b7c4758920d3e0c8a5c22fa` |
