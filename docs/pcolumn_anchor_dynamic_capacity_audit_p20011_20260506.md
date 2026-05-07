# 第P列锚点动态容量审计

**状态：** `pcolumn_anchor_dynamic_capacity_audit_not_a_proof`

## 参数

- `p_list`: `[20011]`
- `alpha`: `0.43`
- `include_square_plus`: `True`

## 总表

| P | cutoff | rows | low primes | high primes | H | min margin | max T/S | min model/sqrt | max D+/sqrt | C-window | min prime holes | cap fails | union fails |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20011 | 70 | 20011 | 19 | 2243 | 0.826152 | 112 | 0.956857 | 8.802969 | 6.659539 | 2.143430 | 929 | 0 | 0 |

## P=20011

- `cutoff`: `70`
- `H=sum_{P^alpha<q<P}1/q`: `0.826152`
- `min_capacity_margin`: `112`
- `max_hit_ratio`: `0.956857`
- `min_model_over_sqrt`: `8.802969`
- `max_dplus_over_sqrt`: `6.659539`
- `sqrt_c_window`: `2.143430`
- `min_prime_holes`: `929`

最小容量余量行：

- `x=70, y=71, S=2596, T=2484, margin=112, ratio=0.956857, D+/sqrt=6.659539, prime_holes=1366, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 37}, {'q': 79, 'hit_count': 34}]`
- `x=65, y=66, S=2590, T=2400, margin=190, ratio=0.926641, D+/sqrt=5.114096, prime_holes=1402, top_q=[{'q': 73, 'hit_count': 37}, {'q': 71, 'hit_count': 35}, {'q': 79, 'hit_count': 31}]`
- `x=61, y=62, S=2587, T=2396, margin=191, ratio=0.926169, D+/sqrt=5.087145, prime_holes=1398, top_q=[{'q': 71, 'hit_count': 35}, {'q': 83, 'hit_count': 35}, {'q': 73, 'hit_count': 33}]`
- `x=79, y=80, S=2583, T=2385, margin=198, ratio=0.923345, D+/sqrt=4.939668, prime_holes=1365, top_q=[{'q': 71, 'hit_count': 38}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 32}]`
- `x=67, y=68, S=2585, T=2386, margin=199, ratio=0.923017, D+/sqrt=4.924927, prime_holes=1405, top_q=[{'q': 79, 'hit_count': 35}, {'q': 73, 'hit_count': 33}, {'q': 71, 'hit_count': 32}]`
- `x=76, y=77, S=2586, T=2380, margin=206, ratio=0.920340, D+/sqrt=4.789741, prime_holes=1380, top_q=[{'q': 71, 'hit_count': 36}, {'q': 79, 'hit_count': 36}, {'q': 73, 'hit_count': 32}]`
- `x=78, y=79, S=2599, T=2386, margin=213, ratio=0.918045, D+/sqrt=4.684770, prime_holes=1390, top_q=[{'q': 73, 'hit_count': 39}, {'q': 71, 'hit_count': 37}, {'q': 79, 'hit_count': 36}]`
- `x=98, y=99, S=2596, T=2382, margin=214, ratio=0.917565, D+/sqrt=4.657614, prime_holes=1348, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 33}]`

最大 T/S 行：

- `x=70, y=71, S=2596, T=2484, margin=112, ratio=0.956857, D+/sqrt=6.659539, prime_holes=1366, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 37}, {'q': 79, 'hit_count': 34}]`
- `x=65, y=66, S=2590, T=2400, margin=190, ratio=0.926641, D+/sqrt=5.114096, prime_holes=1402, top_q=[{'q': 73, 'hit_count': 37}, {'q': 71, 'hit_count': 35}, {'q': 79, 'hit_count': 31}]`
- `x=61, y=62, S=2587, T=2396, margin=191, ratio=0.926169, D+/sqrt=5.087145, prime_holes=1398, top_q=[{'q': 71, 'hit_count': 35}, {'q': 83, 'hit_count': 35}, {'q': 73, 'hit_count': 33}]`
- `x=79, y=80, S=2583, T=2385, margin=198, ratio=0.923345, D+/sqrt=4.939668, prime_holes=1365, top_q=[{'q': 71, 'hit_count': 38}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 32}]`
- `x=67, y=68, S=2585, T=2386, margin=199, ratio=0.923017, D+/sqrt=4.924927, prime_holes=1405, top_q=[{'q': 79, 'hit_count': 35}, {'q': 73, 'hit_count': 33}, {'q': 71, 'hit_count': 32}]`
- `x=76, y=77, S=2586, T=2380, margin=206, ratio=0.920340, D+/sqrt=4.789741, prime_holes=1380, top_q=[{'q': 71, 'hit_count': 36}, {'q': 79, 'hit_count': 36}, {'q': 73, 'hit_count': 32}]`
- `x=78, y=79, S=2599, T=2386, margin=213, ratio=0.918045, D+/sqrt=4.684770, prime_holes=1390, top_q=[{'q': 73, 'hit_count': 39}, {'q': 71, 'hit_count': 37}, {'q': 79, 'hit_count': 36}]`
- `x=98, y=99, S=2596, T=2382, margin=214, ratio=0.917565, D+/sqrt=4.657614, prime_holes=1348, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 33}]`

最大相对正偏差行：

- `x=70, y=71, S=2596, T=2484, margin=112, ratio=0.956857, D+/sqrt=6.659539, prime_holes=1366, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 37}, {'q': 79, 'hit_count': 34}]`
- `x=65, y=66, S=2590, T=2400, margin=190, ratio=0.926641, D+/sqrt=5.114096, prime_holes=1402, top_q=[{'q': 73, 'hit_count': 37}, {'q': 71, 'hit_count': 35}, {'q': 79, 'hit_count': 31}]`
- `x=61, y=62, S=2587, T=2396, margin=191, ratio=0.926169, D+/sqrt=5.087145, prime_holes=1398, top_q=[{'q': 71, 'hit_count': 35}, {'q': 83, 'hit_count': 35}, {'q': 73, 'hit_count': 33}]`
- `x=79, y=80, S=2583, T=2385, margin=198, ratio=0.923345, D+/sqrt=4.939668, prime_holes=1365, top_q=[{'q': 71, 'hit_count': 38}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 32}]`
- `x=67, y=68, S=2585, T=2386, margin=199, ratio=0.923017, D+/sqrt=4.924927, prime_holes=1405, top_q=[{'q': 79, 'hit_count': 35}, {'q': 73, 'hit_count': 33}, {'q': 71, 'hit_count': 32}]`
- `x=76, y=77, S=2586, T=2380, margin=206, ratio=0.920340, D+/sqrt=4.789741, prime_holes=1380, top_q=[{'q': 71, 'hit_count': 36}, {'q': 79, 'hit_count': 36}, {'q': 73, 'hit_count': 32}]`
- `x=78, y=79, S=2599, T=2386, margin=213, ratio=0.918045, D+/sqrt=4.684770, prime_holes=1390, top_q=[{'q': 73, 'hit_count': 39}, {'q': 71, 'hit_count': 37}, {'q': 79, 'hit_count': 36}]`
- `x=98, y=99, S=2596, T=2382, margin=214, ratio=0.917565, D+/sqrt=4.657614, prime_holes=1348, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 33}]`

最少素数洞行：

- `x=19288, y=19289, S=2599, T=2236, margin=363, ratio=0.860331, D+/sqrt=1.742463, prime_holes=929, top_q=[{'q': 71, 'hit_count': 38}, {'q': 97, 'hit_count': 36}, {'q': 73, 'hit_count': 34}]`
- `x=19643, y=19644, S=2598, T=2196, margin=402, ratio=0.845266, D+/sqrt=0.974240, prime_holes=940, top_q=[{'q': 71, 'hit_count': 40}, {'q': 73, 'hit_count': 33}, {'q': 79, 'hit_count': 33}]`
- `x=15270, y=15271, S=2600, T=2239, margin=361, ratio=0.861154, D+/sqrt=1.784760, prime_holes=946, top_q=[{'q': 71, 'hit_count': 35}, {'q': 73, 'hit_count': 35}, {'q': 79, 'hit_count': 33}]`
- `x=19387, y=19388, S=2580, T=2215, margin=365, ratio=0.858527, D+/sqrt=1.644462, prime_holes=946, top_q=[{'q': 71, 'hit_count': 39}, {'q': 79, 'hit_count': 37}, {'q': 73, 'hit_count': 34}]`
- `x=19410, y=19411, S=2592, T=2224, margin=368, ratio=0.858025, D+/sqrt=1.622702, prime_holes=947, top_q=[{'q': 73, 'hit_count': 39}, {'q': 71, 'hit_count': 38}, {'q': 79, 'hit_count': 34}]`
- `x=16485, y=16486, S=2580, T=2201, margin=379, ratio=0.853101, D+/sqrt=1.368837, prime_holes=948, top_q=[{'q': 71, 'hit_count': 39}, {'q': 73, 'hit_count': 38}, {'q': 79, 'hit_count': 37}]`
- `x=18387, y=18388, S=2590, T=2212, margin=378, ratio=0.854054, D+/sqrt=1.420002, prime_holes=949, top_q=[{'q': 73, 'hit_count': 36}, {'q': 79, 'hit_count': 35}, {'q': 71, 'hit_count': 34}]`
- `x=19107, y=19108, S=2594, T=2172, margin=422, ratio=0.837317, D+/sqrt=0.568652, prime_holes=949, top_q=[{'q': 73, 'hit_count': 40}, {'q': 71, 'hit_count': 38}, {'q': 83, 'hit_count': 32}]`

## 结构解释

该审计是 `PColumn Anchor-Wheel Field` 的动态提升轮版本。对每个锚点行 `Py-d`，先提升全部 `q<=P^alpha`，得到动态粗骨架 `S_Y(P,y)`；再统计剩余 `P^alpha<q<P` 的总命中 `T_Y(P,y)`。若 `T_Y<S_Y`，则即使不利用重叠扣除，也不可能全覆盖该行骨架。

相对筛余量写成 `S-T=S(1-H)-(T-HS)`，其中 `H=sum_{P^alpha<q<P}1/q`。表中的 `min model/sqrt` 是 `S(1-H)/sqrt(S)` 的最小值，`max D+/sqrt` 是 `max(0,T-HS)/sqrt(S)` 的最大值。若存在常数 `C` 落在二者之间，即 `D+<=C sqrt(S)<S(1-H)`，则解析上推出 `T<S`。

因此若所有行均有正容量余量，说明第 `P` 列锚点场不仅有低模平移刚性，还满足一阶高素容量夹击。剩余证明任务是把 `T_Y<S_Y` 的样本余量升级为解析不等式，或把失败路由到 `PDEC/SAE/ColumnCRT`。
