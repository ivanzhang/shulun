# Prime Matrix inverse alignment overlap/slack 注册删除映射审计

**状态：** `direct_suffix_deletion_map_closed_residual_weight_compression_open`

本步把 `RegisteredOverlapSlackToColdSupplyDeletionMap` 下钻到单个 raw suffix 命中单位。结论是：可无歧义注册的删除单位不是 `overlap_debt + tau_slack` 的相加量，而是`raw_suffix_capacity-|R_{x,z}|`，即所有未被残洞 tau 选中的后缀命中单位。`tau_slack` 与未出现后缀容量都包含在这个直接后缀删除集中；全局 `overlap_debt` 含有小素层内部重叠，不能整体注入 raw suffix cold 删除单位。因此原相加候选不能闭合。所需删除量精确分解为直接后缀冗余删除加 `floor(|R_{x,z}|-M#)+1`，下一最窄点是`ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger`。

```text
registered_direct_suffix_overlap_deletion_map_closed=true
tau_slack_injection_into_direct_suffix_deletion_closed=true
overlap_plus_tau_additive_map_rejected_under_current_labels=true
deletion_target_decomposition_closed=true
registered_overlap_slack_deletion_map_proved=false
row_column_unconditional_closed=false
```

## 1. 单位审计表

| P | X(P) | z | raw | R | direct del | tau slack | unappeared | overlap total | additive proxy | required | residual compression |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `168` | `3` | `5` | `4` | `1` | `1` | `0` | `3` | `4` | `3` | `2` |
| `17` | `1210` | `3` | `7` | `5` | `2` | `2` | `0` | `5` | `7` | `4` | `2` |
| `19` | `3658` | `3` | `11` | `6` | `5` | `4` | `1` | `8` | `12` | `9` | `4` |
| `23` | `58` | `3` | `14` | `7` | `7` | `5` | `2` | `11` | `16` | `11` | `4` |
| `29` | `5209` | `4` | `20` | `9` | `11` | `11` | `0` | `16` | `27` | `17` | `6` |
| `31` | `60794` | `4` | `21` | `10` | `11` | `10` | `1` | `16` | `26` | `18` | `7` |
| `37` | `73916` | `4` | `26` | `12` | `14` | `11` | `3` | `20` | `31` | `22` | `8` |
| `41` | `170880` | `4` | `30` | `13` | `17` | `16` | `1` | `23` | `39` | `25` | `8` |
| `43` | `162932` | `5` | `24` | `11` | `13` | `11` | `2` | `25` | `36` | `20` | `7` |

解释：`direct del=raw-R` 是可直接注册的后缀冗余删除单位；`residual compression=floor(R-M#)+1` 是仍需证明的已分配残洞 atom 权重压缩量。

## 2. 已闭合/未闭合命题

| name | status | statement |
| --- | --- | --- |
| `suffix_unit_partition` | `closed` | U_suf is the disjoint union of assigned tau units and direct suffix deletion units. |
| `tau_slack_registration` | `closed` | charged tau slack and unappeared suffix capacity are subsets of direct suffix deletion units. |
| `overlap_plus_tau_additive_injection` | `rejected_under_current_labels` | global overlap_debt + charged tau slack is not a disjoint injection into raw suffix deletion units. |
| `deletion_target_decomposition` | `closed` | required deletion = direct suffix deletion + floor(\|R_xz\|-M#)+1 in the audited exact-x rows. |
| `residual_assigned_atom_compression` | `open` | the remaining task is to compress assigned residual atoms from unit weight to reciprocal/M# weight, or route the excess to named returns. |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousOverlapSlackCandidateImported` | `true` | `true` | 上一层候选表已读入并逐行复核。 | RegisteredOverlapSlackToColdSupplyDeletionMap |
| `DirectSuffixOverlapDeletionMapClosed` | `true` | `true` | raw suffix 命中单位可精确分成 tau 已分配单位与可删除后缀冗余单位。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger |
| `TauSlackInjectionClosed` | `true` | `true` | tau charged slack 不是新增独立供给；它已包含在 direct suffix deletion 中。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger |
| `OverlapSlackAdditiveMapRejected` | `true` | `true` | 样本级单位账本显示 overlap_debt + tau_slack 超过可注册的不重叠 raw suffix 删除单位，不能按原候选相加。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger |
| `DeletionTargetDecompositionClosed` | `true` | `true` | 所需删除量已精确拆成后缀冗余删除与残洞已分配 atom 的 reciprocal 权重压缩。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger |
| `RegisteredOverlapSlackDeletionMapProved` | `false` | `false` | 原 `overlap_debt + tau_slack` 映射不能闭合；必须改攻残洞已分配 atom 的权重纪律或命名回流。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步

- 主攻：`ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger`。
- 具体任务：证明已分配残洞 atom 不能以单位权继续留在非持久 cold supply；它必须按 `M#=sum n_q/mu_q` 的 reciprocal 权重压缩，或触发固定历史、ColumnCRT、热核心、PDEC/SAE 等命名回流。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-exact-x-budget-interface-ledger.json` | `1cdc1a5cabb6ff9043184f7e567b14622b5667f708564ef9daae04c44beb6a52` |
| `data/inverse-alignment-exact-zero-row-charge-profile-ledger.json` | `c7cabc90437430aee6614b0428662fe0ce67a1eac9a3ee263b5560ef06481db3` |
| `docs/monograph/prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json` | `40a659d3dd4ed96e7940302c701c89d72e93ff43930f2f2d026e62a50f6385b0` |
| `docs/monograph/prime-matrix-inverse-alignment-overlap-slack-deletion-candidate-router.json` | `4f5ec057437d1badedb4c3df988fc5729c15518d5f325108024387f1fb338174` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json` | `52bd322127d85f72df347da33b5ccc71b6ef2c023539db38244793e6d8d3448c` |
| `experiments/prime_matrix_inverse_alignment_overlap_slack_deletion_map_router.py` | `0571a1f3c60cf0263289673ffbf1183aba47058990e4a14450aab8ca485b4914` |
