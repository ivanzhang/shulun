# Prime Matrix square-phase off-band prefix gap shadow BadPSet PDEC schema router

**状态：** `bad_p_set_pdec_schema_registered_open`

本步把 actual P 避开 BadPSet 的剩余标准化为 PDEC/ColumnCRT 证书输入。有限前沿仍显示 actual P 命中数为 0，但 BadPSet 可非空且可含素数；因此不能靠局部空集或无素数断言闭合。若正式反例族中 actual P 持久命中 BadPSet，必须提交同一坏窗集合上的PDEC/ColumnCRT 证书；否则需要证明 formal-unit selector 全局避开 BadPSet。

```text
record_count=11
actual_p_in_bad_set_count=0
bad_prime_packet_count=6
unique_bad_offset_pattern_count=8
unique_family_key_count=8
max_bad_p_density_in_phase_window=0.250000
row_column_unconditional_closed=false
```

## 1. PDEC 输入对象

若 actual `P` 持久命中 BadPSet，则证书对象按 H4-PDEC 模板登记：`X` 为同一 formal-unit 坏窗索引集，`tau` 为低模或精确覆盖词相位，`S` 为命中 BadPSet 的 actual `P` 集合。

## 2. Schema 前沿

| P | side | family | bad density | bad primes | actual hit | offsets |
| ---: | --- | --- | ---: | --- | ---: | --- |
| 733 | `plus` | `side=plus\|atom=minus_only_noslot:k1:681-687\|L=4\|width=8` | `0.250` | `[]` | `false` | `[1, 3]` |
| 523 | `plus` | `side=plus\|atom=minus_only_noslot:k0:493-499\|L=4\|width=96` | `0.031` | `[499, 541, 563]` | `false` | `[18, 60, 82]` |
| 691 | `minus` | `side=minus\|atom=plus_only_noslot:k1:649-653\|L=3\|width=117` | `0.154` | `[677, 709, 727]` | `false` | `[14, 19, 23, 33, 38, 42, 44, 61, 63, 65, 74, 78, 80, 83, 93, 98, 101, 111]` |
| 683 | `plus` | `side=plus\|atom=minus_only_noslot:k0:649-655\|L=4\|width=172` | `0.064` | `[613, 727]` | `false` | `[0, 44, 54, 61, 63, 84, 97, 99, 114, 132, 159]` |
| 733 | `plus` | `side=plus\|atom=minus_only_noslot:k0:697-705\|L=5\|width=100` | `0.020` | `[]` | `false` | `[27, 87]` |
| 673 | `minus` | `side=minus\|atom=plus_only_noslot:k2:619-623\|L=3\|width=28` | `0.071` | `[]` | `false` | `[4, 14]` |
| 733 | `plus` | `side=plus\|atom=minus_only_noslot:k1:681-687\|L=4\|width=8` | `0.250` | `[]` | `false` | `[1, 3]` |
| 313 | `plus` | `side=plus\|atom=minus_only_noslot:k1:281-283\|L=2\|width=32` | `0.188` | `[317]` | `false` | `[1, 7, 13, 16, 28, 30]` |
| 1129 | `plus` | `side=plus\|atom=minus_only_noslot:k1:1065-1071\|L=4\|width=72` | `0.139` | `[1117]` | `false` | `[5, 7, 16, 28, 29, 35, 37, 50, 52, 54]` |
| 691 | `minus` | `side=minus\|atom=plus_only_noslot:k1:649-653\|L=3\|width=117` | `0.154` | `[677, 709, 727]` | `false` | `[14, 19, 23, 33, 38, 42, 44, 61, 63, 65, 74, 78, 80, 83, 93, 98, 101, 111]` |
| 673 | `minus` | `side=minus\|atom=plus_only_noslot:k2:619-623\|L=3\|width=28` | `0.071` | `[]` | `false` | `[4, 14]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `bad_p_set_pdec_schema_registered` | `closed` | Every local BadPSet packet is registered as a concrete PDEC/ColumnCRT certificate input object. |
| `finite_actual_hits_absent` | `finite_evidence` | The current finite frontier has no actual-P hit inside BadPSet. |
| `bad_p_set_not_empty_or_prime_free` | `closed` | BadPSet may be nonempty and may contain primes, so avoidance cannot be replaced by local primality or empty-set claims. |
| `persistent_hit_pdec_exclusion` | `open` | A global proof still needs a PDEC/ColumnCRT certificate excluding persistent actual-P hits, or a selector theorem proving they never occur. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `BadPSetPDECInputRegistered` | `true` | `true` | BadPSet 命中已被登记为可审查的 PDEC/ColumnCRT 输入对象。 | closed |
| `FiniteNoActualBadPSetHit` | `true` | `false` | 有限前沿无 actual P 命中，但这不是无限族证明。 | finite evidence only |
| `LocalEmptyOrPrimeFreeRouteRejected` | `true` | `true` | BadPSet 非空且可含素数，局部空集/无素数路线已排除。 | closed |
| `PersistentHitPDECExcluded` | `false` | `false` | 仍需真正提交 PDEC/ColumnCRT 证书或 formal-unit selector 排斥定理。 | BadPSetPersistentHitPDECCertificateOrFormalUnitSelectorExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成证书输入标准化，不关闭全局命题。 | BadPSetPersistentHitPDECCertificateOrFormalUnitSelectorExclusion |

## 5. 下一步

- 主攻：`BadPSetPersistentHitPDECCertificateOrFormalUnitSelectorExclusion`。
- 二选一：证明 formal-unit selector 全局避开 BadPSet，或对 persistent hit 提交 H4-PDEC/ColumnCRT 证书。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router.py` | `9b43e6ceca2e9f272b6411bc89c08d1b4166b4eb12e471adcc5b563e9bd27f4c` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router.py` | `25c726eb6a571e1b2cbadeb35b25a2622ce08edadfa7c0c3ef8f14c2076f413a` |
| `docs/monograph/h4-pdec-certificate-template.md` | `6cc441f072b84210293d3d2f61e0279b4e8663d69c58612f13bf2bafc539882e` |
| `data/square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json` | `71d8f20aff9da2560c540af14ddc4e99f11bee2be4aedad1a2023b3e0a4133a6` |
| `data/square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json` | `4b952c155cc1f1b1824a7acf19f75cc1e19fe49c2172cd92e5e371261c0a1f5b` |
