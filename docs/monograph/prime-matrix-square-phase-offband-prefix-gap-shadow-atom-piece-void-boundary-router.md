# Prime Matrix square-phase off-band prefix gap shadow atom-piece void boundary router

**状态：** `atom_piece_void_boundary_registered_open`

本步把 selected small-k atom-piece 的最后边界固定下来：有限前沿中 11 个 selected atom piece 全部实际非空，长度为 2..5，父 atom 最大 k=2；但裸短区间素数供给命题全局为假。因此自足闭合不能依赖“短段必有素数”，只能继续证明完整反例链约束下的 atom-piece void 与列相位/平方锚/CRT 支撑塌缩结构矛盾。

```text
record_count=11
actual_selected_atom_piece_void_count=0
candidate_count_range=2..5
b_length_range=2..5
max_parent_atom_k=2
max_depth_from_p=64
shape_family_count=6
standalone_bounded_gap_route_valid=false
row_column_unconditional_closed=false
```

## 1. 精确边界

当前剩余不能写成裸命题“每个长度 2..5 的奇数段都含素数”。正确边界是：

```text
在完整反例链已经强制 target-union void、wheel/support-collapse、gap-cell/target-segment 选择、
以及固定 small-k 相位 q=P-2b 的同一条件下，排斥 selected atom-piece void。
```

## 2. Selected atom-piece 前沿

| P | side | q atom piece | b interval | parent atom | actual primes | void? |
| ---: | --- | --- | --- | --- | --- | ---: |
| 733 | `plus` | `681-687` | `23-26` | `minus_only_noslot:k1:681-687` | `[683]` | `false` |
| 523 | `plus` | `493-499` | `12-15` | `minus_only_noslot:k0:493-499` | `[499]` | `false` |
| 691 | `minus` | `649-653` | `19-21` | `plus_only_noslot:k1:649-653` | `[653]` | `false` |
| 683 | `plus` | `649-655` | `14-17` | `minus_only_noslot:k0:649-655` | `[653]` | `false` |
| 733 | `plus` | `697-705` | `14-18` | `minus_only_noslot:k0:697-705` | `[701]` | `false` |
| 673 | `minus` | `619-623` | `25-27` | `plus_only_noslot:k2:619-623` | `[619]` | `false` |
| 733 | `plus` | `681-687` | `23-26` | `minus_only_noslot:k1:681-687` | `[683]` | `false` |
| 313 | `plus` | `281-283` | `15-16` | `minus_only_noslot:k1:281-283` | `[281, 283]` | `false` |
| 1129 | `plus` | `1065-1071` | `29-32` | `minus_only_noslot:k1:1065-1071` | `[1069]` | `false` |
| 691 | `minus` | `649-653` | `19-21` | `plus_only_noslot:k1:649-653` | `[653]` | `false` |
| 673 | `minus` | `619-623` | `25-27` | `plus_only_noslot:k2:619-623` | `[619]` | `false` |

## 3. 裸短区间路线反例

| candidate_count | q segment | odd values | all composite |
| ---: | --- | --- | ---: |
| `2` | `119-121` | `[119, 121]` | `true` |
| `3` | `119-123` | `[119, 121, 123]` | `true` |
| `4` | `115-121` | `[115, 117, 119, 121]` | `true` |
| `5` | `115-123` | `[115, 117, 119, 121, 123]` | `true` |

这些小反例只说明裸 bounded-gap 路线无效；它们不否定带完整反例链约束的条件化矛盾路线。

## 4. Shape families

| family | count |
| --- | ---: |
| `side=minus\|band=plus_only_noslot\|k=1\|cand=3\|b_len=3` | `2` |
| `side=minus\|band=plus_only_noslot\|k=2\|cand=3\|b_len=3` | `2` |
| `side=plus\|band=minus_only_noslot\|k=0\|cand=4\|b_len=4` | `2` |
| `side=plus\|band=minus_only_noslot\|k=0\|cand=5\|b_len=5` | `1` |
| `side=plus\|band=minus_only_noslot\|k=1\|cand=2\|b_len=2` | `1` |
| `side=plus\|band=minus_only_noslot\|k=1\|cand=4\|b_len=4` | `3` |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `atom_piece_void_boundary_registered` | `closed` | The newest hardpoint is exactly the exclusion of selected small-k atom-piece void under the full counterexample chain. |
| `naked_bounded_gap_route_rejected` | `closed` | The claim cannot be replaced by a standalone theorem that every odd segment of length 2..5 contains a prime. |
| `finite_atom_piece_frontier_nonvoid` | `finite_evidence` | The finite frontier has no actual selected atom-piece void, but this empirical fact is not used as a proof. |
| `counterexample_conditional_void_contradiction` | `open` | A self-contained proof still needs to derive a contradiction between atom-piece void and the preserved counterexample-chain structure. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `BoundaryRegistrationClosed` | `true` | `true` | 最新 hardpoint 已登记为 selected small-k atom-piece void 的条件化排斥问题。 | closed |
| `NakedBoundedGapInterpretationRejected` | `true` | `true` | 短 atom-piece 供给不能按裸短区间素数定理使用；长度 2..5 均有合数段反例。 | closed |
| `FiniteNoSelectedAtomPieceVoid` | `true` | `false` | 有限账本中每个 selected atom piece 实际含素数；这仍只是有限证据。 | finite evidence only |
| `CounterexampleConditionalVoidContradictionClosed` | `false` | `false` | 仍需把 atom-piece void 接入列相位、平方锚和支撑塌缩链，推出真正矛盾。 | CounterexampleConditionalSmallKAtomPieceVoidContradictionOrColumnPhasePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭错误出口并固定下一原子目标，不关闭行/列无条件命题。 | CounterexampleConditionalSmallKAtomPieceVoidContradictionOrColumnPhasePDEC |

## 7. 下一步

- 主攻：`CounterexampleConditionalSmallKAtomPieceVoidContradictionOrColumnPhasePDEC`。
- 从完整反例链出发，把 selected atom-piece void 与列相位、平方锚、CRT 支撑塌缩同时放入同一矛盾场。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router.py` | `ea4b9848cf09c980a865a80713c9fc160c74d7501912336dc90748e2096b4ff4` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router.py` | `ae2b76a0341113f4b98ac2c46598615e597e5bc25aaf23c13b77a1cdeb5ad5ab` |
| `data/square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json` | `41a1178e194c4ade02b18399ec2c5d42f55bea38a44ab9dade7106b1bbb1bc73` |
| `data/square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json` | `f5bdd68cc74988ed2cb2a115825b20cbcd8a3a172d555381d08b193137500488` |
