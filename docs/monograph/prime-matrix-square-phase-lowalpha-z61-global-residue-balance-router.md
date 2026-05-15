# Prime Matrix square-phase low-alpha z=61 global residue balance

**状态：** `z61_target_cell_multihit_residue_groups_all_locally_absorbed_global_proof_open`

同一目标格内全部多命中 residue 组已做有符号吸收审计：样本中 `21` 个 hit-moduli 组全部局部吸收，未吸收组数为 `0`。这说明当前 Residue-PDEC 不是孤立侥幸，而是嵌入更大的目标格多命中正吸收结构；但这仍是样本目标格证书，下一步要把该吸收规则提升为全局证明，或登记真正未吸收的 Residue-PDEC。

```text
multi_hit_atom_count=31
multi_hit_group_count=21
total_signed_count=29
total_signed_weight=15.379530
unabsorbed_group_count=0
sample_target_cell_multihit_balance_closed=true
global_residue_signed_count_balance_proved=false
row_column_unconditional_closed=false
```

## 1. Profile 符号

| p | sign | linear | nonzero | max weight value |
| ---: | --- | ---: | ---: | ---: |
| 10007 | `negative` | -1.576550 | 2 | 9982 |
| 36739 | `negative` | -1.985602 | 31 | 28842 |
| 83561 | `positive` | 7.257244 | 125 | 57190 |
| 200003 | `positive` | 2.455029 | 264 | 66010 |

## 2. 多命中组

| hit moduli | signed count | pos | neg | signed weight | absorbed |
| --- | ---: | ---: | ---: | ---: | --- |
| `[8170, 11438]` | 1 | 1 | 0 | 0.768923 | true |
| `[8398, 12597]` | 1 | 1 | 0 | 0.579520 | true |
| `[8547, 14245]` | 1 | 1 | 0 | 0.559866 | true |
| `[8602, 12903]` | 1 | 1 | 0 | 0.582595 | true |
| `[8930, 12502]` | 1 | 1 | 0 | 0.581037 | true |
| `[8930, 13395]` | 1 | 1 | 0 | 0.746077 | true |
| `[9338, 14674]` | 1 | 1 | 0 | 0.517263 | true |
| `[9435, 10545]` | 1 | 1 | 0 | 0.362282 | true |
| `[9614, 14421]` | 1 | 2 | 1 | 0.555427 | true |
| `[9842, 14763]` | 1 | 1 | 0 | 0.530361 | true |
| `[9890, 13846]` | 1 | 1 | 0 | 0.696605 | true |
| `[10101, 13209]` | 1 | 1 | 0 | 0.531598 | true |
| `[10166, 15249]` | 1 | 1 | 0 | 0.345414 | true |
| `[10455, 11685]` | 1 | 1 | 0 | 0.548670 | true |
| `[10545, 14763]` | 1 | 1 | 0 | 0.335662 | true |
| `[8151, 13585]` | 2 | 2 | 0 | 1.165583 | true |
| `[8806, 13209]` | 2 | 2 | 0 | 1.116652 | true |
| `[9010, 13515]` | 2 | 2 | 0 | 1.044214 | true |
| `[9430, 13202]` | 2 | 2 | 0 | 1.428190 | true |
| `[10070, 15105]` | 2 | 2 | 0 | 0.992061 | true |
| `[9758, 14637]` | 4 | 4 | 0 | 1.391531 | true |

## 3. 证明边界

- 已闭合：当前样本目标格内所有多命中 residue 组均无未吸收净负组。
- 未闭合：把该 signed count balance 提升为全局证明，或排斥未吸收 Residue-PDEC。
- 下一目标：`LiftTargetCellMultiHitBalanceToGlobalOrUnabsorbedResiduePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.json` | `896298959563e296b581030dadfd3ff34d172c1a45b7af3867237a209040a279` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_global_residue_balance_router.py` | `613c9822f0b53516fbe8c8ec28b610261fca85c7345af96fbdc29fd1fa12299f` |
