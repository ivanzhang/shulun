# Prime Matrix inverse alignment overlap/slack 删除候选路由器

**状态：** `overlap_slack_deletion_candidate_dominates_samples_registered_map_open`

Exact-x 删除目标表暴露出一个候选机制：样本中 `overlap_debt + tau charged_slack` 全部大于等于严格余量所需删除量。这说明重叠债与 tau 桶松弛可能正是 cold-restricted 删除量的来源。当前还不能宣布闭合，因为 overlap/slack 是命中层字段，必须证明它们能被无重复、保标签地注册为 cold supply 删除单位。下一最窄点是 `RegisteredOverlapSlackToColdSupplyDeletionMap`。

```text
deletion_target_imported=true
overlap_slack_candidate_dominates_samples=true
registered_overlap_slack_deletion_map_proved=false
cold_restriction_deletion_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 候选源表

| P | X(P) | z | required | overlap | tau slack | proxy | proxy margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `168` | `3` | `3` | `3` | `1` | `4` | `1` |
| `17` | `1210` | `3` | `4` | `5` | `2` | `7` | `3` |
| `19` | `3658` | `3` | `9` | `8` | `4` | `12` | `3` |
| `23` | `58` | `3` | `11` | `11` | `5` | `16` | `5` |
| `29` | `5209` | `4` | `17` | `16` | `11` | `27` | `10` |
| `31` | `60794` | `4` | `18` | `16` | `10` | `26` | `8` |
| `37` | `73916` | `4` | `22` | `20` | `11` | `31` | `9` |
| `41` | `170880` | `4` | `25` | `23` | `16` | `39` | `14` |
| `43` | `162932` | `5` | `20` | `25` | `11` | `36` | `16` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DeletionTargetImported` | `true` | `true` | 上一层已给出 exact-x 严格余量所需删除量。 | ColdRestrictionDeletionLowerBoundAgainstExactXTable |
| `OverlapSlackCandidateDominatesSamples` | `true` | `false` | 样本中 overlap debt + tau slack 均覆盖所需删除量，但这还不是全局证明。 | RegisteredOverlapSlackToColdSupplyDeletionMap |
| `RegisteredOverlapSlackDeletionMapProved` | `false` | `false` | 仍需把 hit-level overlap/slack 无损注入 cold supply 删除单位。 | RegisteredOverlapSlackToColdSupplyDeletionMap |
| `ColdRestrictionDeletionLowerBoundProved` | `false` | `false` | 候选源足量的样本信号存在，但缺全局注册映射和无重复扣减纪律。 | RegisteredOverlapSlackToColdSupplyDeletionMap AND ColdRestrictionDeletionLowerBoundAgainstExactXTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 删除映射、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。 | RegisteredOverlapSlackToColdSupplyDeletionMap AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步

- 主攻：`RegisteredOverlapSlackToColdSupplyDeletionMap`。
- 任务：构造 overlap/slack 到 cold supply 删除单位的保标签注入，防止重复扣减。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-exact-x-budget-interface-ledger.json` | `1cdc1a5cabb6ff9043184f7e567b14622b5667f708564ef9daae04c44beb6a52` |
| `docs/monograph/prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json` | `40a659d3dd4ed96e7940302c701c89d72e93ff43930f2f2d026e62a50f6385b0` |
| `docs/monograph/prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json` | `f6f2c2c1d5bbd95e83d085f48ac5c6bb6a6250c72fc450112b6815b8313429ba` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `experiments/prime_matrix_inverse_alignment_overlap_slack_deletion_candidate_router.py` | `eda118dad1ae3249da62ec9bb12e6fea4d6aacbd0b49a85518c9e7e1ee9fd16b` |
