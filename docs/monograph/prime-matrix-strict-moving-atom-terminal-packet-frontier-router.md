# Prime Matrix strict moving-atom 终端 packet 前沿路由器

**状态：** `moving_atom_exclusion_reduced_to_rate_bearing_terminal_packet_and_dprc_open`

本步继续攻击当前推荐原子 `ActualNoncanonicalCleanCoreMovingAtomExclusion`。已有材料给出两个事实：第一，moving atom 可标准化为 exact entropy，但当前 ExactUV/pair-mass 内部脊柱会回到源熵目标，不能作为非递归证明；第二，直接 moving-block 路线把 actual same-`(u,v)` 大原子送入全局 PDEC/sparse/ColumnCRT/SAE 终端或有限 DPRC/模型余量账本。因此当前真正可攻的非循环形式不是“再证明 pair-mass 分散”，而是：

```text
RateBearingMovingAtomTerminalPacketExclusionWithExplicitDPRC
```

即对每个超过阈值的 clean-core moving same-`(u,v)` 大原子 packet，证明它要么产生已排斥的低维终端证书，要么在有限 DPRC/模型余量账本中失败；并且该推出带 log-power 速率，不只是定性二分。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
moving_atom_target_active=true
exact_entropy_pairmass_route_recursive=true
direct_moving_block_terminal_route_active=true
rate_bearing_terminal_packet_exclusion_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
actual_noncanonical_clean_core_moving_atom_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 路线分解

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
  <=> ExactCleanCoreFullSNonAPWFDSourceEntropy
  but ExactUV/pair-mass spine is recursive in current corpus

ActualNoncanonicalCleanCoreMovingAtomExclusion
  -> Rate-bearing actual same-(u,v) moving block packet
  -> PDEC / SAE-LocalSurvivor / ColumnCRT / sparse terminal
     OR ExplicitModelGapAndFiniteDPRCLedger
```

所以本轮保留第二条直接 moving-block 线，禁止把第一条 pair-mass 递归脊柱当证明。

## 2. 终端 packet 字段

| field | meaning |
| --- | --- |
| `formal_unit_id` | 与 early-zero 假设、source tuple、registered multiplier、terminal ledger 同单位 |
| `moving_pair_key` | moving same-`(u,v)` 的 exact key，含 phase、branch、dyadic/truncation 和 sign refinement |
| `mass_threshold` | `M_b >= M / log^K` 的速率型大原子阈值 |
| `low_dim_signature_tests` | PDEC、ColumnCRT、SAE/LocalSurvivor、sparse packet 的有限签名测试 |
| `no_signature_case` | 无低维签名时必须进入 L2-flat / DPRC / model-gap 账本 |
| `return_exclusion` | 每个 return tag 必须已排斥或进入明确外部合同，不能只是命名 |
| `rate_preservation` | 从 moving atom 到终端 packet 的每步损失仍保留所需 log-power |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MovingAtomTargetActive` | `true` | `false` | 当前推荐主攻原子是 actual noncanonical clean-core moving atom 排斥。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `ExactEntropyNormalFormImported` | `true` | `true` | moving atom 等价于 exact entropy / max atom 标准形。 | 不能直接证明时需其他路线 |
| `PairMassEntropyRouteRecursive` | `true` | `true` | 当前 ExactUV/pair-mass/rate-bearing/terminal/canonical 脊柱回到源熵目标。 | 不可作为证明 |
| `DirectMovingBlockTerminalRouteImported` | `true` | `true` | moving same-`(u,v)` 大原子若存在，应进入低维终端或 DPRC/model-gap。 | 需带速率排斥 |
| `CurrentMaterializedFutureSchemaDisciplineImported` | `true` | `true` | 当前 PDEC/sparse 前沿无物化义务；未来新增必须提交显式 schema。 | 仍需排斥实际由 packet 物化的终端 |
| `RateBearingRequirementPinned` | `true` | `true` | 目标需要任意固定 A 的 log-power 速率，定性投影二分不足。 | RateBearingMovingAtomTerminalPacketExclusionWithExplicitDPRC |
| `DPRCCompatibilityRemovedButLedgerOpen` | `true` | `false` | DPRC 兼容门已删除，但 ExplicitModelGapAndFiniteDPRCLedger 本身仍开放。 | ExplicitModelGapAndFiniteDPRCLedger |
| `GlobalTerminalExclusionCurrentCorpusProved` | `false` | `false` | 当前材料没有全局排斥 packet 物化后的 PDEC/SAE/ColumnCRT/sparse 终端。 | GlobalPDECorSparseTerminalExclusion_FOR_rate_bearing_packet |
| `RateBearingTerminalPacketExclusionCurrentCorpusProved` | `false` | `false` | 当前没有带速率证明每个 moving atom packet 都被排斥。 | RateBearingMovingAtomTerminalPacketExclusionWithExplicitDPRC |
| `MovingAtomExclusionCurrentCorpusProved` | `false` | `false` | moving atom 排斥仍未闭合。 | terminal packet exclusion + DPRC |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本步只压缩 moving atom 硬点，未产生终端矛盾。 | moving atom terminal packet + DStructure/Rankin |

## 4. 下一真正单点

```text
RateBearingMovingAtomTerminalPacketExclusionWithExplicitDPRC
```

展开为：

```text
MovingAtomToLowDimSignatureOrNoSignatureDPRCLemma
AND GlobalPDECorSparseTerminalExclusion_FOR_rate_bearing_packet
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger
AND NoPairMassEntropyCircularity
```

## 5. 结论

`ActualNoncanonicalCleanCoreMovingAtomExclusion` 没有被证明；但当前真正可攻的非循环形式已经更窄：排斥带 log-power 阈值的 moving same-`(u,v)` 终端 packet，并补齐有限 DPRC/模型余量账本。继续走 ExactUV/pair-mass 只会回到源熵固定点，不能作为闭合证明。
