# Prime Matrix square-phase off-band prefix gap shadow router

**状态：** `prefix_interval_shortage_reduced_to_multi_atom_prime_void_gap_shadow_open`

本步把 `FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC` 的 prime-load 短缺继续压缩：前三 prefix atoms 中若 `W_required<=2` 且 prime-load 小于 `W_required`，则 loaded atom 个数至多为 `W_required-1`，所以在实际可用的 `N<=3` 个前缀 atom 中，至少 `N-W_required+1` 个前缀 atom 必须完全 prime-void。这样反例不再只是总量短缺，而是多个固定二次相位 q 区间同时无素数的 gap shadow。有限扫描中没有 active shadow；全局仍需排斥这个多区间 prime-void PDEC。

```text
max_p=5000
prefix_atoms=3
finite_prime_count=668
prefix_prime_load_shortage_pdec_count=0
multi_void_gap_shadow_active_count=0
row_column_unconditional_closed=false
```

## 1. 多空 atom 影子

令实际可用的前三 prefix atoms 数量为 `N<=3`。若 `W_required<=2` 且 prime-load 失败，则

```text
loaded_atom_count <= prime_load <= W_required-1
void_atom_count >= N-(W_required-1).
```

因此当 `N=3` 时，`W_required=1` 要求三个前缀 atom 全空；`W_required=2` 要求至少两个前缀 atom 全空。

## 2. 显式 PDEC 形态

每个空 atom 都是上一层已经公式化的短区间：

```text
q=P-2b,  b_lo<=b<=b_hi
k=floor(2b^2/(P-2b))
band inequality fixed
prime_count({q in this atom})=0
```

所以反例必须给出多个这样的短 q 区间同时 prime-void，而不是单个总量不等式失败。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| positive required count | 21 |
| prefix atoms | 3 |
| prefix prime-load shortage count | 0 |
| active multi-void shadow count | 0 |
| max required witnesses | 2 |
| min actual void deficit to failure | 1 |
| max actual void atom count | 2 |
| forced void atoms range | 1..3 |
| forced template candidate count range | 1..16 |

## 4. 最紧 void 边界

| P | side | W_req | N | load | void actual | void forced if fail | deficit | atoms |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 23 | `plus` | 1 | 1 | 1 | 0 | 1 | 1 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 1 | 2 | 1 | 1 | 2 | 1 | `plus_only_noslot:k0:33-35#0,both_offband_middle:k0:31-31#1` |
| 73 | `plus` | 1 | 3 | 1 | 2 | 3 | 1 | `both_offband_middle:k0:65-65#0,minus_only_noslot:k0:63-63#0,minus_only_noslot:k1:59-59#1` |
| 523 | `plus` | 1 | 3 | 1 | 2 | 3 | 1 | `both_offband_middle:k0:501-501#0,minus_only_noslot:k0:493-499#1,both_offband_middle:k1:485-485#0` |
| 683 | `plus` | 1 | 3 | 1 | 2 | 3 | 1 | `both_offband_middle:k0:657-657#0,minus_only_noslot:k0:649-655#1,both_offband_middle:k1:639-639#0` |
| 733 | `plus` | 2 | 3 | 2 | 1 | 2 | 1 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1,both_offband_middle:k2:675-675#0` |
| 271 | `minus` | 1 | 3 | 3 | 2 | 3 | 1 | `plus_only_noslot:k0:257-269#3,both_offband_middle:k0:255-255#0,plus_only_noslot:k1:245-247#0` |
| 691 | `minus` | 2 | 3 | 4 | 1 | 2 | 1 | `plus_only_noslot:k0:667-689#3,both_offband_middle:k0:665-665#0,plus_only_noslot:k1:649-653#1` |
| 43 | `minus` | 1 | 2 | 2 | 0 | 2 | 2 | `plus_only_noslot:k0:39-41#1,both_offband_middle:k0:37-37#1` |
| 47 | `minus` | 1 | 2 | 2 | 0 | 2 | 2 | `plus_only_noslot:k0:43-45#1,both_offband_middle:k0:41-41#1` |
| 113 | `plus` | 1 | 3 | 2 | 1 | 3 | 2 | `both_offband_middle:k0:103-103#1,minus_only_noslot:k0:99-101#1,minus_only_noslot:k1:95-95#0` |
| 293 | `plus` | 1 | 3 | 2 | 1 | 3 | 2 | `minus_only_noslot:k0:271-275#1,both_offband_middle:k1:265-265#0,minus_only_noslot:k1:261-263#1` |
| 421 | `plus` | 1 | 3 | 2 | 1 | 3 | 2 | `both_offband_middle:k0:401-401#1,minus_only_noslot:k0:393-399#1,both_offband_middle:k1:387-387#0` |
| 73 | `minus` | 1 | 3 | 3 | 1 | 3 | 2 | `plus_only_noslot:k0:67-71#2,both_offband_middle:k0:65-65#0,plus_only_noslot:k1:61-61#1` |
| 157 | `minus` | 1 | 3 | 3 | 1 | 3 | 2 | `plus_only_noslot:k0:147-155#2,both_offband_middle:k0:145-145#0,plus_only_noslot:k1:139-139#1` |
| 313 | `plus` | 1 | 3 | 3 | 1 | 3 | 2 | `minus_only_noslot:k0:289-295#1,minus_only_noslot:k1:281-283#2,minus_only_noslot:k2:273-275#0` |
| 419 | `minus` | 1 | 3 | 3 | 1 | 3 | 2 | `plus_only_noslot:k0:401-417#2,both_offband_middle:k0:399-399#0,plus_only_noslot:k1:387-391#1` |
| 199 | `minus` | 1 | 3 | 4 | 1 | 3 | 2 | `plus_only_noslot:k0:187-197#3,both_offband_middle:k0:185-185#0,plus_only_noslot:k1:177-179#1` |
| 487 | `plus` | 1 | 3 | 4 | 1 | 3 | 2 | `both_offband_middle:k0:465-465#0,minus_only_noslot:k0:457-463#3,minus_only_noslot:k1:445-449#1` |
| 673 | `minus` | 2 | 3 | 5 | 0 | 2 | 2 | `plus_only_noslot:k0:649-671#3,plus_only_noslot:k1:631-637#1,plus_only_noslot:k2:619-623#1` |
| 1129 | `plus` | 1 | 3 | 5 | 0 | 3 | 3 | `minus_only_noslot:k0:1083-1095#3,minus_only_noslot:k1:1065-1071#1,minus_only_noslot:k2:1051-1055#1` |

## 5. 最小 failure 模板

| P | side | W_req | N | forced void atoms | smallest candidates | templates |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 23 | `plus` | 1 | 1 | 1 | 1 | `both_offband_middle:k0:19-19(1)` |
| 37 | `minus` | 1 | 2 | 2 | 3 | `plus_only_noslot:k0:33-35+both_offband_middle:k0:31-31(3)` |
| 43 | `minus` | 1 | 2 | 2 | 3 | `plus_only_noslot:k0:39-41+both_offband_middle:k0:37-37(3)` |
| 47 | `minus` | 1 | 2 | 2 | 3 | `plus_only_noslot:k0:43-45+both_offband_middle:k0:41-41(3)` |
| 73 | `plus` | 1 | 3 | 3 | 3 | `both_offband_middle:k0:65-65+minus_only_noslot:k0:63-63+minus_only_noslot:k1:59-59(3)` |
| 113 | `plus` | 1 | 3 | 3 | 4 | `both_offband_middle:k0:103-103+minus_only_noslot:k0:99-101+minus_only_noslot:k1:95-95(4)` |
| 691 | `minus` | 2 | 3 | 2 | 4 | `plus_only_noslot:k0:667-689+both_offband_middle:k0:665-665(13); plus_only_noslot:k0:667-689+plus_only_noslot:k1:649-653(15); both_offband_middle:k0:665-665+plus_only_noslot:k1:649-653(4)` |
| 73 | `minus` | 1 | 3 | 3 | 5 | `plus_only_noslot:k0:67-71+both_offband_middle:k0:65-65+plus_only_noslot:k1:61-61(5)` |
| 733 | `plus` | 2 | 3 | 2 | 5 | `minus_only_noslot:k0:697-705+minus_only_noslot:k1:681-687(9); minus_only_noslot:k0:697-705+both_offband_middle:k2:675-675(6); minus_only_noslot:k1:681-687+both_offband_middle:k2:675-675(5)` |
| 293 | `plus` | 1 | 3 | 3 | 6 | `minus_only_noslot:k0:271-275+both_offband_middle:k1:265-265+minus_only_noslot:k1:261-263(6)` |
| 421 | `plus` | 1 | 3 | 3 | 6 | `both_offband_middle:k0:401-401+minus_only_noslot:k0:393-399+both_offband_middle:k1:387-387(6)` |
| 523 | `plus` | 1 | 3 | 3 | 6 | `both_offband_middle:k0:501-501+minus_only_noslot:k0:493-499+both_offband_middle:k1:485-485(6)` |
| 683 | `plus` | 1 | 3 | 3 | 6 | `both_offband_middle:k0:657-657+minus_only_noslot:k0:649-655+both_offband_middle:k1:639-639(6)` |
| 157 | `minus` | 1 | 3 | 3 | 7 | `plus_only_noslot:k0:147-155+both_offband_middle:k0:145-145+plus_only_noslot:k1:139-139(7)` |
| 673 | `minus` | 2 | 3 | 2 | 7 | `plus_only_noslot:k0:649-671+plus_only_noslot:k1:631-637(16); plus_only_noslot:k0:649-671+plus_only_noslot:k2:619-623(15); plus_only_noslot:k1:631-637+plus_only_noslot:k2:619-623(7)` |
| 313 | `plus` | 1 | 3 | 3 | 8 | `minus_only_noslot:k0:289-295+minus_only_noslot:k1:281-283+minus_only_noslot:k2:273-275(8)` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `prefix_load_shortage_to_multivoid_shadow` | `closed` | For N<=3 available prefix atoms and W_required<=2, prefix prime-load < W_required forces at least N-W_required+1 available prefix atoms to be prime-void. |
| `explicit_void_subset_pdec_registration` | `closed` | Each failure registers a finite set of explicit q=P-2b atom intervals that must be prime-free. |
| `finite_no_multivoid_gap_shadow` | `finite_evidence` | The finite audit finds no active multi-atom prime-void shadow up to the tested bound. |
| `global_multivoid_gap_shadow_exclusion` | `open` | A global proof still needs to exclude simultaneous prime-void in the required explicit prefix atom subsets. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PrimeLoadShortageToMultiVoidShadowClosed` | `true` | `true` | 前三 atom 若 prime-load 不足，必有多个前缀 atom 完全无素数。 | closed |
| `ExplicitVoidSubsetRegistrationClosed` | `true` | `true` | 失败已登记为若干显式 q 区间同时 prime-void 的证书族。 | closed |
| `FiniteNoMultiVoidGapShadowPDEC` | `true` | `false` | 有限扫描中未出现真实前缀 prime-load 失败。 | finite evidence only |
| `GlobalMultiVoidGapShadowExcluded` | `false` | `false` | 仍需全局排斥多个固定二次相位 q 区间同时无素数。 | FirstPrefixMultiAtomPrimeVoidGapShadowPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把短缺 PDEC 改写成多 prime-void gap shadow，不关闭全局行/列命题。 | FirstPrefixMultiAtomPrimeVoidGapShadowPDECExclusion |

## 8. 下一步

- 主攻：`FirstPrefixMultiAtomPrimeVoidGapShadowPDECExclusion`。
- 需排斥多个固定二次相位前缀 atom 同时 prime-void。
- 若不能自足排斥，则必须承认这里需要 sqrt 级短区间素数供给或同强度的新输入。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `experiments/prime_matrix_square_phase_offband_prefix_interval_formula_router.py` | `04121893b93d66564ec607141bb0e8ea81fa64743d85356a3191f800518e0430` |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `data/square-phase-offband-prefix-gap-shadow-ledger.json` | `f80e634e8dd67f202e02c0466af8df409217cc4b623b72d519612ee873fd3a74` |
