# Prime Matrix square-phase off-band prefix atom supply router

**状态：** `loaded_atom_multiplicity_reduced_to_first_prefix_supply_open`

本步把 loaded off-band atom 重数下界压成早期前缀供给门：按 b 从小到大，也就是 q 从接近 P 向下排列 off-band atoms；若前 3 个 atoms 中的 loaded atom 个数至少为 `W_required`，且 `W_required<=2`，则上一层重数门闭合。有限扫描显示所有正阈值点在前 3 个 off-band atoms 内已经获得足够 loaded atoms，并且 prime-load 也足够；全局仍需证明这个早期前缀非空供给，或排斥 PrefixVoidPDEC。

```text
max_p=5000
prefix_atoms=3
finite_prime_count=668
required_gt_two_pdec_count=0
prefix_loaded_count_shortage_pdec_count=0
prefix_prime_load_shortage_pdec_count=0
row_column_unconditional_closed=false
```

## 1. 前缀供给门

按自然顺序排列 off-band atoms：`b` 从小到大，也就是 `q=P-2b` 从接近 `P` 向下移动。

若前缀满足

```text
loaded_atom_count(first prefix) >= W_required
W_required <= 2,
```

则上一层 loaded atom 重数门闭合。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| positive required count | 21 |
| prefix atoms | 3 |
| required > 2 PDEC count | 0 |
| prefix loaded shortage count | 0 |
| prefix prime-load shortage count | 0 |
| tail envelope defect count | 21 |
| max required witnesses | 2 |
| max needed prefix for loaded count | 3 |
| max needed prefix for prime load | 3 |
| min prefix loaded surplus | 0 |
| min prefix prime-load surplus | 0 |
| min exact pressure margin | 1 |

## 3. 前缀深度边界

| P | side | D=2T-H | W_req | needed prefix | prefix loaded | prefix load | prefix atoms |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 691 | `minus` | 3 | 2 | 3 | 2 | 4 | `plus_only_noslot:k0:667-689#3,both_offband_middle:k0:665-665#0,plus_only_noslot:k1:649-653#1` |
| 73 | `plus` | 1 | 1 | 3 | 1 | 1 | `both_offband_middle:k0:65-65#0,minus_only_noslot:k0:63-63#0,minus_only_noslot:k1:59-59#1` |
| 673 | `minus` | 3 | 2 | 2 | 3 | 5 | `plus_only_noslot:k0:649-671#3,plus_only_noslot:k1:631-637#1,plus_only_noslot:k2:619-623#1` |
| 487 | `plus` | 0 | 1 | 2 | 2 | 4 | `both_offband_middle:k0:465-465#0,minus_only_noslot:k0:457-463#3,minus_only_noslot:k1:445-449#1` |
| 733 | `plus` | 2 | 2 | 2 | 2 | 2 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1,both_offband_middle:k2:675-675#0` |
| 683 | `plus` | 0 | 1 | 2 | 1 | 1 | `both_offband_middle:k0:657-657#0,minus_only_noslot:k0:649-655#1,both_offband_middle:k1:639-639#0` |
| 523 | `plus` | 0 | 1 | 2 | 1 | 1 | `both_offband_middle:k0:501-501#0,minus_only_noslot:k0:493-499#1,both_offband_middle:k1:485-485#0` |
| 37 | `minus` | 0 | 1 | 2 | 1 | 1 | `plus_only_noslot:k0:33-35#0,both_offband_middle:k0:31-31#1` |
| 1129 | `plus` | 0 | 1 | 1 | 3 | 5 | `minus_only_noslot:k0:1083-1095#3,minus_only_noslot:k1:1065-1071#1,minus_only_noslot:k2:1051-1055#1` |
| 421 | `plus` | 0 | 1 | 1 | 2 | 2 | `both_offband_middle:k0:401-401#1,minus_only_noslot:k0:393-399#1,both_offband_middle:k1:387-387#0` |
| 419 | `minus` | 0 | 1 | 1 | 2 | 3 | `plus_only_noslot:k0:401-417#2,both_offband_middle:k0:399-399#0,plus_only_noslot:k1:387-391#1` |
| 313 | `plus` | 1 | 1 | 1 | 2 | 3 | `minus_only_noslot:k0:289-295#1,minus_only_noslot:k1:281-283#2,minus_only_noslot:k2:273-275#0` |
| 293 | `plus` | 0 | 1 | 1 | 2 | 2 | `minus_only_noslot:k0:271-275#1,both_offband_middle:k1:265-265#0,minus_only_noslot:k1:261-263#1` |
| 199 | `minus` | 0 | 1 | 1 | 2 | 4 | `plus_only_noslot:k0:187-197#3,both_offband_middle:k0:185-185#0,plus_only_noslot:k1:177-179#1` |
| 157 | `minus` | 0 | 1 | 1 | 2 | 3 | `plus_only_noslot:k0:147-155#2,both_offband_middle:k0:145-145#0,plus_only_noslot:k1:139-139#1` |
| 113 | `plus` | 1 | 1 | 1 | 2 | 2 | `both_offband_middle:k0:103-103#1,minus_only_noslot:k0:99-101#1,minus_only_noslot:k1:95-95#0` |
| 73 | `minus` | 0 | 1 | 1 | 2 | 3 | `plus_only_noslot:k0:67-71#2,both_offband_middle:k0:65-65#0,plus_only_noslot:k1:61-61#1` |
| 47 | `minus` | 1 | 1 | 1 | 2 | 2 | `plus_only_noslot:k0:43-45#1,both_offband_middle:k0:41-41#1` |
| 43 | `minus` | 0 | 1 | 1 | 2 | 2 | `plus_only_noslot:k0:39-41#1,both_offband_middle:k0:37-37#1` |
| 271 | `minus` | 0 | 1 | 1 | 1 | 3 | `plus_only_noslot:k0:257-269#3,both_offband_middle:k0:255-255#0,plus_only_noslot:k1:245-247#0` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `prefix_loaded_atom_supply_gate` | `closed` | If the first 3 off-band atoms contain at least W_required loaded atoms and W_required<=2, then the side closes. |
| `finite_first_prefix_loaded_supply` | `finite_evidence` | The finite audit finds that the first 3 off-band atoms already supply enough loaded atoms for every positive-required side. |
| `finite_first_prefix_prime_load_supply` | `finite_evidence` | The finite audit also finds enough prime load inside the first 3 off-band atoms. |
| `prefix_void_pdec_registration` | `closed` | A failure of the prefix supply gate is registered as PrefixVoidPDEC over explicit early q-interval atoms. |
| `global_prefix_loaded_supply` | `open` | A global proof still needs loaded atom supply in the first 3 off-band atoms, or PrefixVoidPDEC exclusion. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PrefixLoadedAtomSupplyGateClosed` | `true` | `true` | 早期前缀 loaded atom 重数达标即可推出上一层重数门。 | closed |
| `FiniteNoPrefixLoadedShortagePDEC` | `true` | `false` | 有限扫描中早期前缀没有 loaded atom 重数短缺。 | finite evidence only |
| `FiniteNoPrefixPrimeLoadShortagePDEC` | `true` | `false` | 有限扫描中早期前缀 prime-load 也没有短缺。 | finite evidence only |
| `GlobalPrefixSupplyClosed` | `false` | `false` | 仍需全局证明早期 off-band atom 前缀供给，或排斥 PrefixVoidPDEC。 | FirstThreeOffBandAtomLoadedMultiplicityOrPrefixVoidPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 loaded atom 重数硬点压成早期前缀供给，不关闭全局行/列命题。 | FirstThreeOffBandAtomLoadedMultiplicityOrPrefixVoidPDEC |

## 6. 下一步

- 主攻：`FirstThreeOffBandAtomLoadedMultiplicityOrPrefixVoidPDEC`。
- 需证明正阈值处前 3 个 off-band atoms 已有足够 loaded atoms。
- 若失败，则反例必须表现为显式早期 q 区间前缀 prime void。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_atom_supply_router.py` | `33417272aa7d1e270c90c0bb2fa86c67dbd622a7fee93ac61be632a61abd7a45` |
| `experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py` | `35fef62e68c422f78266fc5866a18e5024d1cde1565e8e5aedcf3bfe34fff3cb` |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `data/square-phase-offband-prefix-atom-supply-ledger.json` | `4a2f5df25400a9b2a7b3d8763d0ac7c865db6a6e97464a15baf8168671806e33` |
