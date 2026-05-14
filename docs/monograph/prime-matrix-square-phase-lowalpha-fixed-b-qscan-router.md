# Prime Matrix square-phase low-alpha fixed-b q-scan 路由

**状态：** `fixed_b_qscan_normal_form_closed_prime_density_open`

固定 b 后，全部 occupied 记录可由活跃 q 轴的一维扫描精确重建：若整数区间 P^2/(bq)<a<=(P^2+P-1)/(bq) 与 P/q<a<=b 相交，则交集自动是单点；该单点为素数时正好给出 occupied 记录，再要求 b 为素数即给出最终 semiprime-u 贡献。样本中 q-scan 与原 occupied/prime-b 账本完全一致；剩余是证明该 q-scan 相位稀疏、prime-a/prime-b 素性上筛，或把持续尖峰登记并排斥为 PDEC。

```text
fixed_b_qscan_exact_for_occupied_records_closed=true
fixed_b_qscan_exact_for_prime_b_records_closed=true
valid_candidate_singleton_closed=true
phase_sparse_bound_proved=false
prime_a_selberg_bound_proved=false
row_column_unconditional_closed=false
```

## 1. q-scan 分层账本

| active q axes | distinct b | phase fibers | prime-a fibers | prime-b fibers | phase/prime-a | prime-b/prime-a |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 42315 | 86844 | 43666 | 4173 | 1.988824 | 0.095566 |

## 2. 精确匹配与重数

| singleton failures | missing occupied | extra occupied | missing prime-b | extra prime-b | max phase mult | max prime-a mult | max prime-b mult |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 | 0 | 11 | 3 | 3 |

## 3. 最大纤维样本

| kind | data |
| --- | --- |
| phase | `{'b': 38099, 'multiplicity': 11, 'sample': [{'q': 41, 'a': 25608, 'b': 38099, 'n': 1049928, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [25608, 25608], 'raw_a_interval': [25608, 25608], 'singleton_ok': True, 'a_interval_width': 0.1280380574613379, 'n_interval': [1049928, 1049933]}, {'q': 43, 'a': 24417, 'b': 38099, 'n': 1049931, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [24417, 24417], 'raw_a_interval': [24417, 24417], 'singleton_ok': True, 'a_interval_width': 0.12208279897476404, 'n_interval': [1049928, 1049933]}, {'q': 47, 'a': 22339, 'b': 38099, 'n': 1049933, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [22339, 22339], 'raw_a_interval': [22339, 22339], 'singleton_ok': True, 'a_interval_width': 0.11169277353010326, 'n_interval': [1049928, 1049933]}, {'q': 53, 'a': 19810, 'b': 38099, 'n': 1049930, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [19810, 19810], 'raw_a_interval': [19810, 19810], 'singleton_ok': True, 'a_interval_width': 0.09904830860216704, 'n_interval': [1049928, 1049933]}, {'q': 61, 'a': 17212, 'b': 38099, 'n': 1049932, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [17212, 17212], 'raw_a_interval': [17212, 17212], 'singleton_ok': True, 'a_interval_width': 0.08605836649040743, 'n_interval': [1049928, 1049933]}, {'q': 89, 'a': 11797, 'b': 38099, 'n': 1049933, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [11797, 11797], 'raw_a_interval': [11797, 11797], 'singleton_ok': True, 'a_interval_width': 0.058983824223762395, 'n_interval': [1049928, 1049933]}, {'q': 97, 'a': 10824, 'b': 38099, 'n': 1049928, 'prime_a': False, 'prime_b': False, 'valid_a_interval': [10824, 10824], 'raw_a_interval': [10824, 10824], 'singleton_ok': True, 'a_interval_width': 0.05411917892695725, 'n_interval': [1049928, 1049933]}, {'q': 167, 'a': 6287, 'b': 38099, 'n': 1049929, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [6287, 6287], 'raw_a_interval': [6287, 6287], 'singleton_ok': True, 'a_interval_width': 0.03143449314919074, 'n_interval': [1049928, 1049933]}]}` |
| prime-a | `{'b': 4533, 'multiplicity': 3, 'sample': [{'q': 73, 'a': 4079, 'b': 4533, 'n': 297767, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [4079, 4079], 'raw_a_interval': [4079, 4079], 'singleton_ok': True, 'a_interval_width': 0.1110244810506816, 'n_interval': [297762, 297769]}, {'q': 131, 'a': 2273, 'b': 4533, 'n': 297763, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [2273, 2273], 'raw_a_interval': [2273, 2273], 'singleton_ok': True, 'a_interval_width': 0.06186860394427296, 'n_interval': [297762, 297769]}, {'q': 191, 'a': 1559, 'b': 4533, 'n': 297769, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [1559, 1559], 'raw_a_interval': [1559, 1559], 'singleton_ok': True, 'a_interval_width': 0.04243344040156941, 'n_interval': [297762, 297769]}]}` |
| prime-b | `{'b': 9733, 'multiplicity': 3, 'sample': [{'q': 101, 'a': 7103, 'b': 9733, 'n': 717403, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [7103, 7103], 'raw_a_interval': [7103, 7103], 'singleton_ok': True, 'a_interval_width': 0.08500325014521384, 'n_interval': [717399, 717407]}, {'q': 151, 'a': 4751, 'b': 9733, 'n': 717401, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [4751, 4751], 'raw_a_interval': [4751, 4751], 'singleton_ok': True, 'a_interval_width': 0.05685647857395098, 'n_interval': [717399, 717407]}, {'q': 233, 'a': 3079, 'b': 9733, 'n': 717407, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [3079, 3079], 'raw_a_interval': [3079, 3079], 'singleton_ok': True, 'a_interval_width': 0.036846902423461794, 'n_interval': [717399, 717407]}]}` |

## 4. 每个 P 的总结

| P | active q | distinct b | phase | prime-a | prime-b | max phase | max prime-a | max prime-b |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 14 | 766 | 1060 | 777 | 99 | 5 | 2 | 1 |
| 36739 | 32 | 3927 | 6760 | 4013 | 429 | 7 | 3 | 2 |
| 83561 | 50 | 10410 | 20015 | 10697 | 1025 | 9 | 3 | 3 |
| 200003 | 75 | 27212 | 59009 | 28179 | 2620 | 11 | 3 | 3 |

## 5. 证明边界

- 已闭合：固定 `b` 后，原 occupied 记录与一维 q-scan 的 prime-a 单点候选完全一致。
- 已闭合：固定 `b` 后，再加 `b` 为素数即可精确恢复 prime-b 贡献。
- 已闭合：任意合法 `(b,q)` 候选自动是单点，因为合法性强制 `bq>P`。
- 未闭合：固定 `b` 的 phase 候选总数全局稀疏上界。
- 未闭合：prime-a 与 prime-b 的一维 Selberg/Brun 型上筛，或持续尖峰的 PDEC 排除。
- 下一目标：`FixedBPhaseSparseQScanSelbergBoundOrPrimeBSpikePDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.json` | `3bb04e739c690a2eeafdf6fe75bdd2eb5133785fc91cd2e4fae50392d9a8c83b` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-occupied-b-sequence-router.json` | `8fe89eaab334cdee38f6b5d2b9a54e7f00082a7bdfbeaf460eb9b64ff03fa631` |
| `experiments/prime_matrix_square_phase_lowalpha_fixed_b_qscan_router.py` | `df3068955bc91c32769303a5404c5a3fdc53407f6ae8e68ad4d658b6547b456a` |
