# Prime Matrix two-residue spare prime-anchor filter router

**状态：** `two_residue_spare_prime_anchor_filter_closes_near_fill_global_ap_open`

加入 P 必须为素数的锚限制后，上一证书的两空位外延进一步收窄。当前 admitted lattice 的 64 个步号中只有 17 个素数锚，新增 residue 只有 13 个；与既有 22 个 residue 合并后仅为 35/70 个非零 residue。原先两个空位中的 residue 0 对 P>71 素数锚结构性不可能，因为它强制 71|P；residue 62 的近端候选 P=9647 也是合数，首个素数锚要到 P=26687。因此近端 two-residue fill 不能作为真实链；若要最终填满全部非零 residue，必须进入长 AP 素数锚到达问题，当前扫描中最后一个非零 residue 到 P=98047 才出现，之后首个素数锚重复在 P=98207，才会进入 transport reset-PDEC。

```text
row_column_unconditional_closed=false
admitted_lattice_step_count=64
admitted_prime_anchor_count=17
admitted_prime_anchor_new_residue_count=13
prime_filtered_union_size=35
prime_filtered_nonzero_spare=35
residue_zero_prime_anchor_impossible=true
residue_zero_p_class_mod_5680=4047
residue_zero_gcd_class_modulus=71
first_prime_hit_for_residue_62={'step': 300, 'p': 26687, 'residue': 62}
first_full_nonzero_capacity_row={'residue': 67, 'step': 1192, 'p': 98047, 'extension_beyond_epoch_p_max': 88790}
first_repeat_after_full_nonzero_capacity={'step': 1194, 'p': 98207, 'residue': 14, 'extension_beyond_epoch_p_max': 88950}
next_direct_attack_target=PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC
```

## 1. 当前 admitted 带内的素数锚

| step | P | residue | already used |
| ---: | ---: | ---: | --- |
| 22 | 4447 | 45 | `false` |
| 30 | 5087 | 46 | `true` |
| 31 | 5167 | 55 | `false` |
| 34 | 5407 | 11 | `false` |
| 37 | 5647 | 38 | `false` |
| 39 | 5807 | 56 | `false` |
| 42 | 6047 | 12 | `true` |
| 45 | 6287 | 39 | `true` |
| 46 | 6367 | 48 | `false` |
| 49 | 6607 | 4 | `false` |
| 57 | 7247 | 5 | `false` |
| 60 | 7487 | 32 | `false` |
| 63 | 7727 | 59 | `true` |
| 70 | 8287 | 51 | `false` |
| 72 | 8447 | 69 | `false` |
| 73 | 8527 | 7 | `false` |
| 79 | 9007 | 61 | `false` |

## 2. 两空位近端候选

| step | P | residue | prime P | structural status |
| ---: | ---: | ---: | --- | --- |
| 87 | 9647 | 62 | `false` | `composite_or_unavailable` |
| 88 | 9727 | 0 | `false` | `divisible_by_ell` |
| 89 | 9807 | 9 | `false` | `composite_or_unavailable` |

## 3. 当前缺失非零 residue 的首个素数锚

| residue | step | P | extension beyond current p_max |
| ---: | ---: | ---: | ---: |
| 30 | 115 | 11887 | 2630 |
| 31 | 123 | 12527 | 3270 |
| 14 | 129 | 13007 | 3750 |
| 50 | 133 | 13327 | 4070 |
| 68 | 135 | 13487 | 4230 |
| 6 | 136 | 13567 | 4310 |
| 33 | 139 | 13807 | 4550 |
| 70 | 151 | 14767 | 5510 |
| 54 | 165 | 15887 | 6630 |
| 64 | 174 | 16607 | 7350 |
| 29 | 178 | 16927 | 7670 |
| 57 | 189 | 17807 | 8550 |
| 13 | 192 | 18047 | 8790 |
| 49 | 196 | 18367 | 9110 |
| 60 | 213 | 19727 | 10470 |
| 25 | 217 | 20047 | 10790 |
| 52 | 220 | 20287 | 11030 |
| 63 | 237 | 21647 | 12390 |
| 1 | 238 | 21727 | 12470 |
| 2 | 246 | 22367 | 13110 |
| 24 | 280 | 25087 | 15830 |
| 42 | 282 | 25247 | 15990 |
| 62 | 300 | 26687 | 17430 |
| 47 | 322 | 28447 | 19190 |
| 16 | 358 | 31327 | 22070 |
| 43 | 361 | 31567 | 22310 |
| 19 | 382 | 33247 | 23990 |
| 8 | 436 | 37567 | 28310 |
| 41 | 487 | 41647 | 32390 |
| 20 | 532 | 45247 | 35990 |
| 15 | 634 | 53407 | 44150 |
| 58 | 694 | 58207 | 48950 |
| 17 | 792 | 66047 | 56790 |
| 23 | 1053 | 86927 | 77670 |
| 67 | 1192 | 98047 | 88790 |

## 4. 证明边界

- `residue 0` 不是可填空位；在 `P>71` 的素数锚线上它结构性不可能。
- 近端 `P=9647,9727,9807` 都不是素数锚，因此不能作为真实链到达。
- 若反例链仍要靠 `minus:71` 饱和触发 reset，必须证明长 AP 素数锚覆盖全部非零 residue；当前 finite scan 中这要到 `P=98047` 才发生。
- 下一主攻点：`PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
