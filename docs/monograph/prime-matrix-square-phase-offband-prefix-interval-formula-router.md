# Prime Matrix square-phase off-band prefix interval formula router

**状态：** `first_prefix_supply_reduced_to_explicit_q_interval_prime_shortage_open`

本步把前三 off-band atom 的 loaded 重数口径精炼为真正需要的容量口径：当 `W_required<=2` 时，前 3 个 atoms 的总 prime-load 达到 `W_required` 就足以推出 top-two atom 负载达标。每个前缀 atom 又被写成显式 `q=P-2b` 区间、固定 `k=floor(2b^2/(P-2b))` 和一个二次 band 不等式。因此若前缀失败，反例必须表现为最多 3 个早期 q 区间的素数供给短缺。有限扫描未发现该短缺；全局仍需证明这些短 q 区间必有足够素数，或排斥对应 PDEC。

```text
max_p=5000
prefix_atoms=3
finite_prime_count=668
formula_identity_failure_count=0
required_gt_two_pdec_count=0
prefix_prime_load_shortage_pdec_count=0
prefix_top_two_load_shortage_pdec_count=0
row_column_unconditional_closed=false
```

## 1. 容量口径精炼

上一层的 loaded atom 个数是足够条件，但真正接入双 atom 门的是前缀 prime-load 容量。若

```text
W_required <= 2
sum prime_load(first prefix atoms) >= W_required,
```

则两个最大前缀 atom 的 prime-load 之和也至少为 `W_required`，因此双 atom 容量门闭合。

## 2. 显式区间公式

尾素写成 `q=P-2b`。每个前缀 atom 由固定 `k` 与固定 band 给出：

```text
k(P-2b) <= 2b^2 < (k+1)(P-2b)
base = 2b^2-k(P-2b)
plus_only_noslot:  base < (P-4b+1)/2
minus_only_noslot: base > (P-1)/2
both_offband:      (P-4b+1)/2 <= base <= (P-1)/2
```

所以前缀失败不再是抽象 atom 失败，而是显式短 q 区间中的素数个数不足。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| positive required count | 21 |
| prefix atoms | 3 |
| formula identity failures | 0 |
| required > 2 PDEC count | 0 |
| prefix prime-load shortage count | 0 |
| prefix top-two shortage count | 0 |
| prefix capacity failure count | 0 |
| tail envelope defect count | 21 |
| max required witnesses | 2 |
| min prefix prime-load surplus | 0 |
| min prefix top-two surplus | 0 |
| max prefix support depth | 78 |
| max depth/sqrt(P) | 2.321387 |
| min exact pressure margin | 1 |

## 4. 最紧区间供给边界

| P | side | W_req | prefix load | top-two load | support q | depth | atoms |
| ---: | --- | ---: | ---: | ---: | --- | ---: | --- |
| 23 | `plus` | 1 | 1 | 1 | `19-19` | 4 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 1 | 1 | 1 | `31-35` | 6 | `plus_only_noslot:k0:33-35#0,both_offband_middle:k0:31-31#1` |
| 73 | `plus` | 1 | 1 | 1 | `59-65` | 14 | `both_offband_middle:k0:65-65#0,minus_only_noslot:k0:63-63#0,minus_only_noslot:k1:59-59#1` |
| 523 | `plus` | 1 | 1 | 1 | `485-501` | 38 | `both_offband_middle:k0:501-501#0,minus_only_noslot:k0:493-499#1,both_offband_middle:k1:485-485#0` |
| 683 | `plus` | 1 | 1 | 1 | `639-657` | 44 | `both_offband_middle:k0:657-657#0,minus_only_noslot:k0:649-655#1,both_offband_middle:k1:639-639#0` |
| 733 | `plus` | 2 | 2 | 2 | `675-705` | 58 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1,both_offband_middle:k2:675-675#0` |
| 43 | `minus` | 1 | 2 | 2 | `37-41` | 6 | `plus_only_noslot:k0:39-41#1,both_offband_middle:k0:37-37#1` |
| 47 | `minus` | 1 | 2 | 2 | `41-45` | 6 | `plus_only_noslot:k0:43-45#1,both_offband_middle:k0:41-41#1` |
| 113 | `plus` | 1 | 2 | 2 | `95-103` | 18 | `both_offband_middle:k0:103-103#1,minus_only_noslot:k0:99-101#1,minus_only_noslot:k1:95-95#0` |
| 293 | `plus` | 1 | 2 | 2 | `261-275` | 32 | `minus_only_noslot:k0:271-275#1,both_offband_middle:k1:265-265#0,minus_only_noslot:k1:261-263#1` |
| 421 | `plus` | 1 | 2 | 2 | `387-401` | 34 | `both_offband_middle:k0:401-401#1,minus_only_noslot:k0:393-399#1,both_offband_middle:k1:387-387#0` |
| 73 | `minus` | 1 | 3 | 3 | `61-71` | 12 | `plus_only_noslot:k0:67-71#2,both_offband_middle:k0:65-65#0,plus_only_noslot:k1:61-61#1` |
| 157 | `minus` | 1 | 3 | 3 | `139-155` | 18 | `plus_only_noslot:k0:147-155#2,both_offband_middle:k0:145-145#0,plus_only_noslot:k1:139-139#1` |
| 271 | `minus` | 1 | 3 | 3 | `245-269` | 26 | `plus_only_noslot:k0:257-269#3,both_offband_middle:k0:255-255#0,plus_only_noslot:k1:245-247#0` |
| 419 | `minus` | 1 | 3 | 3 | `387-417` | 32 | `plus_only_noslot:k0:401-417#2,both_offband_middle:k0:399-399#0,plus_only_noslot:k1:387-391#1` |
| 313 | `plus` | 1 | 3 | 3 | `273-295` | 40 | `minus_only_noslot:k0:289-295#1,minus_only_noslot:k1:281-283#2,minus_only_noslot:k2:273-275#0` |
| 691 | `minus` | 2 | 4 | 4 | `649-689` | 42 | `plus_only_noslot:k0:667-689#3,both_offband_middle:k0:665-665#0,plus_only_noslot:k1:649-653#1` |
| 199 | `minus` | 1 | 4 | 4 | `177-197` | 22 | `plus_only_noslot:k0:187-197#3,both_offband_middle:k0:185-185#0,plus_only_noslot:k1:177-179#1` |
| 487 | `plus` | 1 | 4 | 4 | `445-465` | 42 | `both_offband_middle:k0:465-465#0,minus_only_noslot:k0:457-463#3,minus_only_noslot:k1:445-449#1` |
| 673 | `minus` | 2 | 5 | 4 | `619-671` | 54 | `plus_only_noslot:k0:649-671#3,plus_only_noslot:k1:631-637#1,plus_only_noslot:k2:619-623#1` |
| 1129 | `plus` | 1 | 5 | 4 | `1051-1095` | 78 | `minus_only_noslot:k0:1083-1095#3,minus_only_noslot:k1:1065-1071#1,minus_only_noslot:k2:1051-1055#1` |

## 5. 深度边界

| P | side | W_req | prefix load | q support | depth | depth/sqrt(P) |
| ---: | --- | ---: | ---: | --- | ---: | ---: |
| 1129 | `plus` | 1 | 5 | `1051-1095` | 78 | 2.321387 |
| 733 | `plus` | 2 | 2 | `675-705` | 58 | 2.142279 |
| 673 | `minus` | 2 | 5 | `619-671` | 54 | 2.081547 |
| 683 | `plus` | 1 | 1 | `639-657` | 44 | 1.683613 |
| 487 | `plus` | 1 | 4 | `445-465` | 42 | 1.903202 |
| 691 | `minus` | 2 | 4 | `649-689` | 42 | 1.597755 |
| 313 | `plus` | 1 | 3 | `273-295` | 40 | 2.260934 |
| 523 | `plus` | 1 | 1 | `485-501` | 38 | 1.661624 |
| 421 | `plus` | 1 | 2 | `387-401` | 34 | 1.657059 |
| 419 | `minus` | 1 | 3 | `387-417` | 32 | 1.563302 |
| 293 | `plus` | 1 | 2 | `261-275` | 32 | 1.869460 |
| 271 | `minus` | 1 | 3 | `245-269` | 26 | 1.579388 |
| 199 | `minus` | 1 | 4 | `177-197` | 22 | 1.559539 |
| 157 | `minus` | 1 | 3 | `139-155` | 18 | 1.436556 |
| 113 | `plus` | 1 | 2 | `95-103` | 18 | 1.693298 |
| 73 | `plus` | 1 | 1 | `59-65` | 14 | 1.638576 |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `prefix_capacity_refinement_gate` | `closed` | If W_required<=2 and the first 3 off-band atoms have total prime-load at least W_required, then their top-two atom load reaches W_required. |
| `explicit_prefix_interval_formula` | `closed` | Each prefix atom is an explicit interval q=P-2b with fixed k=floor(2b^2/(P-2b)) and one quadratic band inequality. |
| `prefix_interval_shortage_pdec_registration` | `closed` | A prefix prime-load failure is exactly a shortage of primes in at most 3 explicit early q-intervals. |
| `finite_no_prefix_interval_prime_shortage` | `finite_evidence` | The finite audit finds no such explicit interval shortage up to the tested bound. |
| `global_first_prefix_interval_prime_supply` | `open` | A global proof still needs enough primes in these first prefix q-intervals, or exclusion of the corresponding short-q interval shortage PDEC. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PrefixCapacityRefinementGateClosed` | `true` | `true` | 前三 atom 不必先证明 loaded atom 个数；总 prime-load 达标且 W_required<=2 就推出双 atom 容量达标。 | closed |
| `ExplicitPrefixIntervalFormulaClosed` | `true` | `true` | 前三 off-band atom 已写成固定 k 与固定 band 的显式 q=P-2b 区间。 | closed |
| `FiniteNoPrefixIntervalPrimeShortagePDEC` | `true` | `false` | 有限扫描中显式前三 q 区间总素数负载均达到阈值。 | finite evidence only |
| `GlobalPrefixIntervalPrimeSupplyClosed` | `false` | `false` | 仍需全局证明前三 q 区间素数供给，或排斥显式短区间缺口 PDEC。 | FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成容量口径精炼和区间公式化，不关闭全局行/列命题。 | FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC |

## 8. 下一步

- 主攻：`FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC`。
- 需证明正阈值处前三个显式 q 区间的 prime-load 达到 `W_required`。
- 若失败，反例必须给出最多三个靠近 P 的短 q 区间素数短缺证书。
- 该输入本质上仍是短区间素数供给问题；当前未推出全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_interval_formula_router.py` | `04121893b93d66564ec607141bb0e8ea81fa64743d85356a3191f800518e0430` |
| `experiments/prime_matrix_square_phase_offband_prefix_atom_supply_router.py` | `33417272aa7d1e270c90c0bb2fa86c67dbd622a7fee93ac61be632a61abd7a45` |
| `experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py` | `35fef62e68c422f78266fc5866a18e5024d1cde1565e8e5aedcf3bfe34fff3cb` |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `data/square-phase-offband-prefix-interval-formula-ledger.json` | `13ecbea878cd9d4c82a60af0729d0024514fbad6e9f184c6f1a94835885d7fae` |
