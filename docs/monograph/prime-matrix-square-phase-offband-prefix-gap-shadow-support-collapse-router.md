# Prime Matrix square-phase off-band prefix gap shadow support collapse router

**状态：** `punctured_hull_support_collapse_pdec_registered_open`

本步把 wheel-17 失败包进一步压成穿孔 hull 素数支撑塌缩：若目标 union 全空且 wheel-17 容量门失败，则整个短 hull 中所有素数都必须落入至多 4 个指定 wheel-17 幸存位置，其他奇候选全部合数。有限账本中每个包都有至少一个逃逸素数，因此实际塌缩数为 0；全局仍需排斥这些固定小 k 穿孔短间隙模式。

```text
wheel_bound=17
record_count=11
max_wheel17_survivor_count=4
max_required_hull_prime_count=5
min_actual_escape_prime_count=1
actual_support_collapse_count=0
row_column_unconditional_closed=false
```

## 1. 塌缩包

wheel-17 下界失败并且目标 union 全空时，反例必须满足：

```text
Prime(hull) subset Wheel17Survivors(complement pockets)
```

这等价于一个穿孔短素数间隙：hull 中除少数幸存位置外全部为合数。

## 2. 塌缩前沿

| P | side | hull | survivors | escape primes | punctured composite candidates |
| ---: | --- | --- | --- | --- | ---: |
| 683 | `plus` | `639-657` | `[641, 643, 647]` | `[653]` | 7 |
| 733 | `plus` | `675-705` | `[677, 683, 691]` | `[701]` | 13 |
| 523 | `plus` | `485-501` | `[487, 491]` | `[499]` | 7 |
| 691 | `minus` | `649-665` | `[659, 661]` | `[653]` | 7 |
| 733 | `plus` | `675-687` | `[677]` | `[683]` | 6 |
| 733 | `plus` | `681-705` | `[691]` | `[683, 701]` | 12 |
| 673 | `minus` | `619-637` | `[]` | `[619, 631]` | 10 |
| 313 | `plus` | `273-295` | `[277]` | `[281, 283, 293]` | 11 |
| 673 | `minus` | `619-671` | `[631, 641, 643, 647]` | `[619, 653, 659, 661]` | 23 |
| 691 | `minus` | `649-689` | `[659, 661]` | `[653, 673, 677, 683]` | 19 |
| 1129 | `plus` | `1051-1095` | `[1061, 1063, 1073, 1081]` | `[1051, 1069, 1087, 1091, 1093]` | 19 |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `support_collapse_packet_equivalence` | `closed` | If the wheel-17 gate fails and the target union is prime-void, all hull primes must lie in the explicit wheel-17 survivor set. |
| `punctured_hull_gap_pattern_registration` | `closed` | The failure packet is a punctured prime-gap pattern: the hull is prime-free outside at most four survivor positions. |
| `finite_no_actual_support_collapse` | `finite_evidence` | The finite audit finds at least one escaping prime outside the survivor set in every packet. |
| `global_punctured_hull_gap_exclusion` | `open` | A global proof still needs to exclude these fixed small-k punctured hull gap patterns. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SupportCollapsePacketEquivalenceClosed` | `true` | `true` | wheel-17 下界失败已等价压成素数支撑塌缩包。 | closed |
| `PuncturedHullGapPatternRegistered` | `true` | `true` | 每个失败包都是固定小 k 的穿孔短素数间隙模式。 | closed |
| `FiniteNoSupportCollapse` | `true` | `false` | 有限前沿中每个包都有逃逸素数；这不是全局证明。 | finite evidence only |
| `GlobalSupportCollapseExcluded` | `false` | `false` | 仍需全局排斥这些固定形状穿孔 hull gap。 | FixedSmallKPuncturedHullPrimeGapPatternExclusionOrSupportCollapsePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成反例包结构化，不关闭全局行/列命题。 | FixedSmallKPuncturedHullPrimeGapPatternExclusionOrSupportCollapsePDEC |

## 5. 下一步

- 主攻：`FixedSmallKPuncturedHullPrimeGapPatternExclusionOrSupportCollapsePDEC`。
- 证明方向：排斥固定小 `k` 的穿孔 hull gap pattern，或把该 pattern 接入更强的列相位/平方锚矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py` | `69b61f3820afc3daa860fd3ac612bb78d8a3635e89aea87a2b8dafaf2bc5e273` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py` | `430b1d0c42dd64c5e658ff56da2ab4b92b7ad01b8821367e38d5fa3485af5600` |
| `data/square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json` | `071e8c159cba935e2e688a701c10b51d72416f2c8e4e29f1648e661d8e8c09a2` |
| `data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json` | `221c23d9062defd07903b63b15e284ddd4f86693640f512aa6818c6abda95594` |
