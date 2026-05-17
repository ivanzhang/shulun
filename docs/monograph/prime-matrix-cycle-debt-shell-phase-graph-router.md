# Prime Matrix cycle-debt shell phase graph router

**状态：** `tight_hall_survivors_force_non_affine_shell_phase_fragmentation`

把 K=13/14 tight-Hall 岛继续拆成 forced shell 的 bipartite phase graph。K=14 的 forced shell 乘积只有 2 个匹配，且已有 3 条强制边；K=13 的刚性核心至少需要 7 个不同 residue 相位差。两个 survivor 都没有公共单一平移相位，因此 ordinary translation support motion 被关闭。剩余只能是非仿射 shell phase fragmentation 的 PDEC，或多相位 moving-support SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13K14TightHallCRTIslandPDECOrMovingSupportSAE
survivor_shifts=[13, 14]
k13_forced_shell_matching_product=252829237248000
k14_forced_shell_matching_product=2
k13_forced_edge_count=1
k14_forced_edge_count=3
k13_single_translation_support_possible=false
k14_single_translation_support_possible=false
all_survivors_close_single_translation_support=true
k13_core_min_distinct_delta_lower_bound=7
k14_core_min_distinct_delta_lower_bound=4
next_direct_attack_target=NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE
```

## 1. shell graph summary

| K | shell | edges | matchings | forced edges | possible deltas | single translation |
| ---: | --- | ---: | ---: | ---: | ---: | :---: |
| 13 | `>=8` | 13 | 8 | 0 | 12 | false |
| 13 | `7..7` | 1 | 1 | 1 | 1 | true |
| 13 | `4..6` | 14 | 12 | 0 | 14 | false |
| 13 | `1..3` | 252 | 2633637888000 | 0 | 71 | false |
| 14 | `>=15` | 1 | 1 | 1 | 1 | true |
| 14 | `13..14` | 1 | 1 | 1 | 1 | true |
| 14 | `8..12` | 4 | 2 | 0 | 4 | false |
| 14 | `7..7` | 1 | 1 | 1 | 1 | true |

## 2. forced edges

| K | source | target | delta |
| ---: | ---: | ---: | ---: |
| 13 | 31 | 15 | 55 |
| 14 | 13 | 67 | 54 |
| 14 | 19 | 23 | 4 |
| 14 | 70 | 15 | 16 |

## 3. core phase fragmentation

| K | enumerated shells | excluded large shells | min distinct deltas | witness deltas |
| ---: | --- | --- | ---: | --- |
| 13 | `['>=8', '7..7', '4..6']` | `['1..3']` | 7 | `[8, 22, 39, 54, 55, 58, 59]` |
| 14 | `['>=15', '13..14', '8..12', '7..7']` | `[]` | 4 | `[4, 16, 28, 54]` |

## 4. 判定

- 每个 forced shell 来自 zero-slack Hall cut；shell 内不是自由容量，而是相位边图。
- 两个 survivor 的 forced shell 均无公共单一 residue 平移，因此单平移 support motion 当前关闭。
- `K=14` 高层只剩 2 个 shell 匹配，且强制 `13->67`、`19->23`、`70->15` 三条边。
- `K=13` 即便只看可枚举刚性核心，也至少需要 7 个不同相位差；低层大 shell 不会降低该下界。
- 下一主攻点：`NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json` | `50fbbec5233aaee5442ccd088c8aaa72804f87e09cf5d5895d3cf938ca602c0a` |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
