# Prime Matrix cross-carrier fifty-unit residue saturation router

**状态：** `cross_carrier_fifty_unit_current_band_saturates_to_two_spare_global_open`

重建完整 singleton 物理记录后，minus:71 已用 residue 确认为 22 个，与 capacity ledger 完全一致。跨载体 support lattice 在当前 minus:71 P 区间内可进入 64 个互异 residue；其中 17 个已在既有 singleton 集中，新增 47 个，合并后为 69/71。因此当前带并不直接溢出，而是留下 residue 0 和 62 两个空位。若端点再向外延伸到 P=9647 与 P=9727，这两个空位依次被填满；再继续持久同步则只能触发重复 residue 并进入 transport reset-PDEC，或提前回到 SAE/unused-target/moving-carrier 出口。

```text
row_column_unconditional_closed=false
shape_key=size=1|side=minus|ells=71
used_residue_count_reconstructed=22
exact_used_matches_capacity_ledger=true
admitted_step_range=[19, 82]
admitted_p_range_on_support_lattice=[4207, 9247]
admitted_distinct_residue_count=64
admitted_intersection_existing_count=17
admitted_new_residue_count=47
union_size_after_admitted_band=69
spare_after_admitted_band=2
missing_residues_after_admitted_band=[0, 62]
direct_fifty_overflow_current_blocks=false
min_block_new_residue_count=34
max_block_new_residue_count=40
max_block_union_size=62
min_block_spare_after=9
p_extension_to_first_missing_residue=390
p_extension_to_full_capacity=470
p_extension_to_post_full_repeat=550
next_direct_attack_target=TwoResidueSpareEndpointExtensionOrTransportResetPDEC
```

## 1. minus:71 已用 residue

| p | residue | slot keys |
| ---: | ---: | --- |
| 4177 | 59 | `['358:74:71']` |
| 4217 | 28 | `['345:67:71']` |
| 4507 | 34 | `['294:44:71']` |
| 4517 | 44 | `['440:106:71']` |
| 4547 | 3 | `['279:39:71']` |
| 4597 | 53 | `['415:91:71']` |
| 4637 | 22 | `['402:84:71']` |
| 5077 | 36 | `['499:122:71']` |
| 5107 | 66 | `['490:116:71']` |
| 5417 | 21 | `['387:64:71']` |
| 5857 | 35 | `['537:120:71']` |
| 6047 | 12 | `['474:88:71']` |
| 6217 | 40 | `['565:125:71']` |
| 6257 | 9 | `['552:118:71']` |
| 6287 | 39 | `['590:136:71']` |
| 6427 | 37 | `['495:90:71']` |
| 7607 | 10 | `['693:154:71']` |
| 7757 | 18 | `['644:128:71']` |
| 7907 | 26 | `['740:170:71']` |
| 7927 | 46 | `['780:191:71']` |
| 8017 | 65 | `['705:150:71']` |
| 9257 | 27 | `['785:160:71']` |

## 2. 50 步块扫描

| start step | p range | new residues | intersection | union size | spare |
| ---: | --- | ---: | ---: | ---: | ---: |
| 19 | `4207..8127` | 34 | 16 | 56 | 15 |
| 20 | `4287..8207` | 35 | 15 | 57 | 14 |
| 21 | `4367..8287` | 36 | 14 | 58 | 13 |
| 22 | `4447..8367` | 37 | 13 | 59 | 12 |
| 23 | `4527..8447` | 37 | 13 | 59 | 12 |
| 24 | `4607..8527` | 37 | 13 | 59 | 12 |
| 25 | `4687..8607` | 37 | 13 | 59 | 12 |
| 26 | `4767..8687` | 37 | 13 | 59 | 12 |
| 27 | `4847..8767` | 37 | 13 | 59 | 12 |
| 28 | `4927..8847` | 37 | 13 | 59 | 12 |
| 29 | `5007..8927` | 38 | 12 | 60 | 11 |
| 30 | `5087..9007` | 39 | 11 | 61 | 10 |
| 31 | `5167..9087` | 40 | 10 | 62 | 9 |
| 32 | `5247..9167` | 40 | 10 | 62 | 9 |
| 33 | `5327..9247` | 40 | 10 | 62 | 9 |

## 3. 当前带外的后续到达

| step | p | residue | new against current union | union size | spare |
| ---: | ---: | ---: | --- | ---: | ---: |
| 83 | 9327 | 26 | `false` | 69 | 2 |
| 84 | 9407 | 35 | `false` | 69 | 2 |
| 85 | 9487 | 44 | `false` | 69 | 2 |
| 86 | 9567 | 53 | `false` | 69 | 2 |
| 87 | 9647 | 62 | `true` | 70 | 1 |
| 88 | 9727 | 0 | `true` | 71 | 0 |
| 89 | 9807 | 9 | `false` | 71 | 0 |
| 90 | 9887 | 18 | `false` | 71 | 0 |
| 91 | 9967 | 27 | `false` | 71 | 0 |
| 92 | 10047 | 36 | `false` | 71 | 0 |
| 93 | 10127 | 45 | `false` | 71 | 0 |
| 94 | 10207 | 54 | `false` | 71 | 0 |
| 95 | 10287 | 63 | `false` | 71 | 0 |
| 96 | 10367 | 1 | `false` | 71 | 0 |
| 97 | 10447 | 10 | `false` | 71 | 0 |

## 4. 证明边界

- 当前 50 步块都不能直接造成 `minus:71` 溢出；最大并集只有 `62/71`。
- 当前 support lattice 能进入的整个 `minus:71` 带只达到 `69/71`，留下两个空位。
- 若端点外延填满两个空位，之后的持久同步必须变成重复 residue，即 reset-PDEC；若不能外延，则回到 endpoint/SAE/unused-target 出口。
- 下一主攻点：`TwoResidueSpareEndpointExtensionOrTransportResetPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json` | `770d67c3ede972e73a22e141f61e99a24263c5229269021416ea5e681bce4a61` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json` | `2b7ba1295e2d498da7265aa73d7e39b6a5add3a31ae60f947b4fbc4cf212b373` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py` | `b0c8c4981326d393ce93cd7256bb00ef2ee55eda8d87f8649bdad67cebcd12bd` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_unique_representative_persistence_split_router.py` | `e52231333293c3b6993dda65d7f1e0d339752660fa8c84ba489efbc1b08ed210` |
