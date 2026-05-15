# Prime Matrix square-phase low-alpha z=61 negative support isolation

**状态：** `z61_target_cell_negative_multihit_support_isolated_to_one_absorbed_mixed_group_open`

目标格多命中 residue 的负支撑在样本中高度隔离：没有 negative-only 组，也没有 mixed-unabsorbed 组；唯一含负支撑的 mixed 组正是 `[9614,14421]`，并已由两条正记录吸收。其余 20 个多命中组全部 positive-only。下一步应证明负多命中支撑只能进入已吸收 mixed 组，或登记 NegativeOnlyResidue-PDEC。

```text
positive_only_group_count=20
negative_only_group_count=0
mixed_absorbed_group_count=1
mixed_unabsorbed_group_count=0
negative_multihit_atom_count=1
positive_multihit_atom_count=30
negative_multihit_support_isolated_in_sample=true
row_column_unconditional_closed=false
```

## 1. 混合组

| hit moduli | signed count | pos | neg | signed weight | absorbed |
| --- | ---: | ---: | ---: | ---: | --- |
| `[9614, 14421]` | 1 | 2 | 1 | 0.555427 | true |

## 2. 负多命中原子

| p | b | hit moduli | signed weight |
| ---: | ---: | --- | ---: |
| 36739 | 28842 | `[9614, 14421]` | -0.555427 |

## 3. 证明边界

- 已闭合：样本目标格中负多命中支撑只进入一个已吸收 mixed 组。
- 未闭合：全局负支撑隔离证明，或 NegativeOnlyResidue-PDEC 排斥。
- 下一目标：`NegativeMultiHitSupportIsolationProofOrNegativeOnlyResiduePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.json` | `e2e75e89e828926e310e956a9dbdebacae9bd752a86c67dc4d99415075f7438a` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_negative_support_isolation_router.py` | `f9ff1e706f5bd43bd03087d039d4da64a75bc9ba8a4e3f3b83dab6645751e169` |
