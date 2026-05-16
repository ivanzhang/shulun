# Prime Matrix square-phase off-band prefix gap shadow selector H lower transport-cell iteration-drift router

**状态：** `transport_cell_chained_persistence_closed_nonchained_open`

本步证明 transport cell 的链式迭代深度恒等式：若同一 cell 连续复现，左右相位深度分别按 `-lo_defect` 与 `+hi_defect` 线性漂移。当前 12 个 cell 全部存在前向收缩边，因此从观测起点出发都只能有限次连续复现；最长前向寿命为 8 次转移，观测到一次后最多还能追加 7 次。剩余硬点缩成非连续 transport 复现的 PDEC/ColumnCRT，或 singleton residue 的 SAE/Rankin 可求和。

```text
transport_cell_count=12
depth_iteration_identity_failure_count=0
exact_phase_translate_count=0
forward_finite_lifetime_count=12
max_forward_transition_count=8
max_forward_additional_after_observed=7
immediate_terminal_after_observed_count=8
row_column_unconditional_closed=false
```

## 1. 迭代恒等式

```text
If the same transport cell is repeated n times:
  left_depth(n)  = left_depth(0)  - n * lo_defect
  right_depth(n) = right_depth(0) + n * hi_defect
validity requires both depths to stay nonnegative.
```

## 2. 有限寿命记录

| ell | residue | side | p values | defect | start depth | next depth | forward max | additional | contracting edges |
| ---: | ---: | --- | --- | --- | --- | --- | ---: | ---: | --- |
| 43 | 16 | `minus` | `[2467, 2897]` | `1/1` | `[8, 13]` | `[7, 14]` | 8 | 7 | `['left']` |
| 43 | 20 | `plus` | `[2557, 3847]` | `-14/-7` | `[2, 21]` | `[16, 14]` | 3 | 2 | `['right']` |
| 53 | 45 | `minus` | `[2377, 5557]` | `15/-1` | `[17, 18]` | `[2, 17]` | 1 | 0 | `['left', 'right']` |
| 43 | 37 | `minus` | `[2617, 6917]` | `15/-5` | `[28, 13]` | `[13, 8]` | 1 | 0 | `['left', 'right']` |
| 53 | 25 | `minus` | `[2887, 7127]` | `12/16` | `[18, 4]` | `[6, 20]` | 1 | 0 | `['left']` |
| 53 | 31 | `minus` | `[3847, 5437]` | `9/7` | `[10, 13]` | `[1, 20]` | 1 | 0 | `['left']` |
| 37 | 14 | `minus` | `[3307, 5527]` | `-10/-8` | `[3, 21]` | `[13, 13]` | 2 | 1 | `['right']` |
| 59 | 42 | `minus` | `[5647, 7417]` | `30/28` | `[33, 2]` | `[3, 30]` | 1 | 0 | `['left']` |
| 89 | 88 | `minus` | `[7297, 9967]` | `-3/-2` | `[9, 13]` | `[12, 11]` | 6 | 5 | `['right']` |
| 29 | 24 | `minus` | `[6317, 7187]` | `5/6` | `[6, 14]` | `[1, 20]` | 1 | 0 | `['left']` |
| 79 | 39 | `plus` | `[7307, 8887]` | `-18/-21` | `[0, 24]` | `[18, 3]` | 1 | 0 | `['right']` |
| 103 | 64 | `plus` | `[8819, 9437]` | `-23/-10` | `[0, 19]` | `[23, 9]` | 1 | 0 | `['right']` |

## 3. 结构判断

- 当前 12 个 transport cell 都不是 exact translate。
- 每个 cell 都有前向收缩边，因此不能沿同一 cell 无限连续复现。
- 这仍未排除非连续复现；非连续情形必须继续用 ColumnCRT/PDEC 或 SAE/Rankin 处理。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `transport_cell_depth_iteration_identity` | `closed` | Under repeated use of the same transport cell, phase depths evolve by D_L(n)=D_L(0)-n*lo_defect and D_R(n)=D_R(0)+n*hi_defect. |
| `current_transport_cell_forward_chain_nonpersistence` | `closed_on_current_sweep` | Every current transport cell has a forward contracting edge, hence only finitely many chained repeats are possible from the observed start. |
| `nonchained_transport_or_singleton_sae_open` | `open` | A global proof must still exclude non-chained transport recurrences or prove singleton-residue SAE/Rankin summability. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `DepthIterationIdentityClosed` | `true` | `true` | 同一 transport cell 迭代时左右深度按边界缺陷线性更新。 | closed |
| `CurrentForwardChainNonPersistenceClosed` | `true` | `false` | 当前 12 个 cell 全部有前向有限寿命；最长只能连续走 8 次。 | finite evidence only |
| `ExactTranslateEscapeAbsentCurrentSweep` | `true` | `false` | 当前没有零缺陷 exact translate 逃逸口。 | finite evidence only |
| `NonChainedTransportExcluded` | `false` | `false` | 非连续复现仍可能存在，需要 ColumnCRT/PDEC 或 SAE 处理。 | NonChainedTransportCellPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭 chained transport 通道，不关闭全局命题。 | NonChainedTransportCellPDECOrSingletonResidueSAESummability |

## 6. 下一步

- 主攻：`NonChainedTransportCellPDECOrSingletonResidueSAESummability`。
- 对非连续 transport 复现建立 ColumnCRT/PDEC 上界。
- 对 singleton residue packet 建立 SAE/Rankin 可求和账本。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_transport_cell_iteration_drift_router.py` | `e8f2f9a8598f1a67c925e792011cf14ad86f1c9d1c5013ba1ba0ff8b799d278c` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json` | `7a6af4c73819b3e86322f0b0e40032dc0e98a3f114eab5b163284c85e2b6f23b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json` | `45e0a3f337d03dbc6317776e3350aa75a018d155062b6ce4c24fd8b65bbca692` |
