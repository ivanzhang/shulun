# Prime Matrix square-phase low-alpha z=61 secondary quotient gate

**状态：** `z61_secondary_square_congruence_reduced_to_quotient_residue_gate_open`

二级平方同余可消去大模数 `M`：由一级条件 `p^2+delta=M*K`，二级条件等价于 `K+2q4≡0 (mod 2q2q4)`。样本中 `2q2q4=5254`，而在 32 个一级 CRT 根上，`mod 37` 门和 `mod 71` 门各自已经单独唯一选中 `r=26951`。因此最新硬点压成 quotient-residue gate 的全局容量界，或登记 QuotientGate-PDEC。

```text
secondary_quotient_gate_group_count=1
all_secondary_quotient_gates_closed=true
quotient_residue_gate_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 商余数门摘要

| M | delta | gate modulus | target residue | roots | full gate roots | selected | q4 unique | q2 unique |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 57684 | 527 | 5254 | 5180 | 32 | 1 | 26951 | true | true |

## 2. 因子门

| factor modulus | pass count | pass residues | uniquely selected |
| ---: | ---: | --- | --- |
| 2 | 32 | `[1891, 3961, 5653, 7457, 7723, 8009, 11219, 11771, 17071, 17623, 20833, 21119, 21385, 23189, 24881, 26951, 30733, 32803, 34495, 36299, 36565, 36851, 40061, 40613, 45913, 46465, 49675, 49961, 50227, 52031, 53723, 55793]` | false |
| 37 | 1 | `[26951]` | true |
| 71 | 1 | `[26951]` | true |
| 74 | 1 | `[26951]` | true |
| 142 | 1 | `[26951]` | true |
| 2627 | 1 | `[26951]` | true |
| 5254 | 1 | `[26951]` | true |

## 3. 素数候选的 K 余数

| root | p | K | K+2q4 mod 5254 | prime p | full source |
| ---: | ---: | ---: | ---: | --- | --- |
| 1891 | 174943 | 530564 | 5238 | true | false |
| 3961 | 177013 | 543194 | 2106 | true | false |
| 8009 | 181061 | 568322 | 964 | true | false |
| 11219 | 184271 | 588652 | 278 | true | false |
| 11771 | 184823 | 592184 | 3810 | true | false |
| 24881 | 197933 | 679174 | 1482 | true | false |
| 26951 | 200003 | 693454 | 0 | true | true |
| 34495 | 207547 | 746754 | 760 | true | false |
| 46465 | 219517 | 835374 | 62 | true | false |

## 4. 自足小引理

一级平方同余给出 `p^2+delta=M*K`。于是

```text
p^2+delta+2*M*q4 ≡ 0 (mod 2*M*q2*q4)
```

等价于 `K+2*q4≡0 (mod 2*q2*q4)`。因此二级平方同余可降为一级根集合上的小模商余数门。

## 5. 证明边界

- 已闭合：样本二级同余等价于 quotient `K` 的小模余数门，且 q2/q4 因子门各自唯一选中同一根。
- 未闭合：全局 quotient-residue gate 容量界，或 QuotientGate-PDEC 排斥。
- 下一目标：`QuotientResidueGateGlobalBoundOrQuotientGatePDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json` | `470a79443beba230550a0ecdb6607b9aeedbee15221fe893d7c798783db6388d` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_secondary_quotient_gate_router.py` | `da470c112de8485cf671d150343bb747c84a3662e18ed80fc37e8e72c09faad6` |
