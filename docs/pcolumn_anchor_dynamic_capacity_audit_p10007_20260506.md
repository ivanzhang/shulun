# 第P列锚点动态容量审计

**状态：** `pcolumn_anchor_dynamic_capacity_audit_not_a_proof`

## 参数

- `p_list`: `[10007]`
- `alpha`: `0.43`
- `include_square_plus`: `True`

## 总表

| P | cutoff | rows | low primes | high primes | H | min margin | max T/S | min model/sqrt | max D+/sqrt | C-window | min prime holes | cap fails | union fails |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10007 | 52 | 10007 | 15 | 1214 | 0.821413 | 98 | 0.929446 | 6.602875 | 4.026284 | 2.576591 | 498 | 0 | 0 |

## P=10007

- `cutoff`: `52`
- `H=sum_{P^alpha<q<P}1/q`: `0.821413`
- `min_capacity_margin`: `98`
- `max_hit_ratio`: `0.929446`
- `min_model_over_sqrt`: `6.602875`
- `max_dplus_over_sqrt`: `4.026284`
- `sqrt_c_window`: `2.576591`
- `min_prime_holes`: `498`

最小容量余量行：

- `x=45, y=46, S=1389, T=1291, margin=98, ratio=0.929446, D+/sqrt=4.026284, prime_holes=747, top_q=[{'q': 53, 'hit_count': 27}, {'q': 59, 'hit_count': 23}, {'q': 61, 'hit_count': 21}]`
- `x=62, y=63, S=1383, T=1283, margin=100, ratio=0.927693, D+/sqrt=3.952416, prime_holes=722, top_q=[{'q': 53, 'hit_count': 25}, {'q': 59, 'hit_count': 25}, {'q': 61, 'hit_count': 23}]`
- `x=50, y=51, S=1391, T=1285, margin=106, ratio=0.923796, D+/sqrt=3.818466, prime_holes=754, top_q=[{'q': 67, 'hit_count': 26}, {'q': 53, 'hit_count': 25}, {'q': 59, 'hit_count': 23}]`
- `x=53, y=54, S=1390, T=1282, margin=108, ratio=0.922302, D+/sqrt=3.761405, prime_holes=745, top_q=[{'q': 53, 'hit_count': 28}, {'q': 71, 'hit_count': 26}, {'q': 61, 'hit_count': 23}]`
- `x=56, y=57, S=1383, T=1275, margin=108, ratio=0.921909, D+/sqrt=3.737296, prime_holes=741, top_q=[{'q': 53, 'hit_count': 25}, {'q': 61, 'hit_count': 25}, {'q': 59, 'hit_count': 21}]`
- `x=40, y=41, S=1379, T=1264, margin=115, ratio=0.916606, D+/sqrt=3.534974, prime_holes=752, top_q=[{'q': 53, 'hit_count': 29}, {'q': 59, 'hit_count': 24}, {'q': 61, 'hit_count': 22}]`
- `x=74, y=75, S=1384, T=1268, margin=116, ratio=0.916185, D+/sqrt=3.525705, prime_holes=708, top_q=[{'q': 53, 'hit_count': 27}, {'q': 59, 'hit_count': 23}, {'q': 61, 'hit_count': 22}]`
- `x=59, y=60, S=1396, T=1276, margin=120, ratio=0.914040, D+/sqrt=3.460819, prime_holes=746, top_q=[{'q': 53, 'hit_count': 26}, {'q': 59, 'hit_count': 24}, {'q': 79, 'hit_count': 24}]`

最大 T/S 行：

- `x=45, y=46, S=1389, T=1291, margin=98, ratio=0.929446, D+/sqrt=4.026284, prime_holes=747, top_q=[{'q': 53, 'hit_count': 27}, {'q': 59, 'hit_count': 23}, {'q': 61, 'hit_count': 21}]`
- `x=62, y=63, S=1383, T=1283, margin=100, ratio=0.927693, D+/sqrt=3.952416, prime_holes=722, top_q=[{'q': 53, 'hit_count': 25}, {'q': 59, 'hit_count': 25}, {'q': 61, 'hit_count': 23}]`
- `x=50, y=51, S=1391, T=1285, margin=106, ratio=0.923796, D+/sqrt=3.818466, prime_holes=754, top_q=[{'q': 67, 'hit_count': 26}, {'q': 53, 'hit_count': 25}, {'q': 59, 'hit_count': 23}]`
- `x=53, y=54, S=1390, T=1282, margin=108, ratio=0.922302, D+/sqrt=3.761405, prime_holes=745, top_q=[{'q': 53, 'hit_count': 28}, {'q': 71, 'hit_count': 26}, {'q': 61, 'hit_count': 23}]`
- `x=56, y=57, S=1383, T=1275, margin=108, ratio=0.921909, D+/sqrt=3.737296, prime_holes=741, top_q=[{'q': 53, 'hit_count': 25}, {'q': 61, 'hit_count': 25}, {'q': 59, 'hit_count': 21}]`
- `x=40, y=41, S=1379, T=1264, margin=115, ratio=0.916606, D+/sqrt=3.534974, prime_holes=752, top_q=[{'q': 53, 'hit_count': 29}, {'q': 59, 'hit_count': 24}, {'q': 61, 'hit_count': 22}]`
- `x=74, y=75, S=1384, T=1268, margin=116, ratio=0.916185, D+/sqrt=3.525705, prime_holes=708, top_q=[{'q': 53, 'hit_count': 27}, {'q': 59, 'hit_count': 23}, {'q': 61, 'hit_count': 22}]`
- `x=59, y=60, S=1396, T=1276, margin=120, ratio=0.914040, D+/sqrt=3.460819, prime_holes=746, top_q=[{'q': 53, 'hit_count': 26}, {'q': 59, 'hit_count': 24}, {'q': 79, 'hit_count': 24}]`

最大相对正偏差行：

- `x=45, y=46, S=1389, T=1291, margin=98, ratio=0.929446, D+/sqrt=4.026284, prime_holes=747, top_q=[{'q': 53, 'hit_count': 27}, {'q': 59, 'hit_count': 23}, {'q': 61, 'hit_count': 21}]`
- `x=62, y=63, S=1383, T=1283, margin=100, ratio=0.927693, D+/sqrt=3.952416, prime_holes=722, top_q=[{'q': 53, 'hit_count': 25}, {'q': 59, 'hit_count': 25}, {'q': 61, 'hit_count': 23}]`
- `x=50, y=51, S=1391, T=1285, margin=106, ratio=0.923796, D+/sqrt=3.818466, prime_holes=754, top_q=[{'q': 67, 'hit_count': 26}, {'q': 53, 'hit_count': 25}, {'q': 59, 'hit_count': 23}]`
- `x=53, y=54, S=1390, T=1282, margin=108, ratio=0.922302, D+/sqrt=3.761405, prime_holes=745, top_q=[{'q': 53, 'hit_count': 28}, {'q': 71, 'hit_count': 26}, {'q': 61, 'hit_count': 23}]`
- `x=56, y=57, S=1383, T=1275, margin=108, ratio=0.921909, D+/sqrt=3.737296, prime_holes=741, top_q=[{'q': 53, 'hit_count': 25}, {'q': 61, 'hit_count': 25}, {'q': 59, 'hit_count': 21}]`
- `x=40, y=41, S=1379, T=1264, margin=115, ratio=0.916606, D+/sqrt=3.534974, prime_holes=752, top_q=[{'q': 53, 'hit_count': 29}, {'q': 59, 'hit_count': 24}, {'q': 61, 'hit_count': 22}]`
- `x=74, y=75, S=1384, T=1268, margin=116, ratio=0.916185, D+/sqrt=3.525705, prime_holes=708, top_q=[{'q': 53, 'hit_count': 27}, {'q': 59, 'hit_count': 23}, {'q': 61, 'hit_count': 22}]`
- `x=59, y=60, S=1396, T=1276, margin=120, ratio=0.914040, D+/sqrt=3.460819, prime_holes=746, top_q=[{'q': 53, 'hit_count': 26}, {'q': 59, 'hit_count': 24}, {'q': 79, 'hit_count': 24}]`

最少素数洞行：

- `x=8948, y=8949, S=1396, T=1178, margin=218, ratio=0.843840, D+/sqrt=0.837909, prime_holes=498, top_q=[{'q': 53, 'hit_count': 28}, {'q': 59, 'hit_count': 25}, {'q': 67, 'hit_count': 24}]`
- `x=9426, y=9427, S=1386, T=1174, margin=212, ratio=0.847042, D+/sqrt=0.954121, prime_holes=501, top_q=[{'q': 61, 'hit_count': 26}, {'q': 59, 'hit_count': 25}, {'q': 53, 'hit_count': 23}]`
- `x=9496, y=9497, S=1379, T=1197, margin=182, ratio=0.868020, D+/sqrt=1.730741, prime_holes=501, top_q=[{'q': 53, 'hit_count': 29}, {'q': 59, 'hit_count': 25}, {'q': 61, 'hit_count': 24}]`
- `x=9760, y=9761, S=1382, T=1175, margin=207, ratio=0.850217, D+/sqrt=1.070783, prime_holes=502, top_q=[{'q': 61, 'hit_count': 26}, {'q': 53, 'hit_count': 25}, {'q': 67, 'hit_count': 23}]`
- `x=6755, y=6756, S=1392, T=1185, margin=207, ratio=0.851293, D+/sqrt=1.114796, prime_holes=503, top_q=[{'q': 53, 'hit_count': 26}, {'q': 59, 'hit_count': 24}, {'q': 61, 'hit_count': 24}]`
- `x=7443, y=7444, S=1394, T=1184, margin=210, ratio=0.849354, D+/sqrt=1.043212, prime_holes=505, top_q=[{'q': 53, 'hit_count': 29}, {'q': 61, 'hit_count': 26}, {'q': 59, 'hit_count': 23}]`
- `x=8213, y=8214, S=1381, T=1169, margin=212, ratio=0.846488, D+/sqrt=0.931818, prime_holes=505, top_q=[{'q': 61, 'hit_count': 24}, {'q': 53, 'hit_count': 23}, {'q': 59, 'hit_count': 22}]`
- `x=8831, y=8832, S=1382, T=1169, margin=213, ratio=0.845876, D+/sqrt=0.909385, prime_holes=505, top_q=[{'q': 53, 'hit_count': 26}, {'q': 59, 'hit_count': 26}, {'q': 61, 'hit_count': 24}]`

## 结构解释

该审计是 `PColumn Anchor-Wheel Field` 的动态提升轮版本。对每个锚点行 `Py-d`，先提升全部 `q<=P^alpha`，得到动态粗骨架 `S_Y(P,y)`；再统计剩余 `P^alpha<q<P` 的总命中 `T_Y(P,y)`。若 `T_Y<S_Y`，则即使不利用重叠扣除，也不可能全覆盖该行骨架。

相对筛余量写成 `S-T=S(1-H)-(T-HS)`，其中 `H=sum_{P^alpha<q<P}1/q`。表中的 `min model/sqrt` 是 `S(1-H)/sqrt(S)` 的最小值，`max D+/sqrt` 是 `max(0,T-HS)/sqrt(S)` 的最大值。若存在常数 `C` 落在二者之间，即 `D+<=C sqrt(S)<S(1-H)`，则解析上推出 `T<S`。

因此若所有行均有正容量余量，说明第 `P` 列锚点场不仅有低模平移刚性，还满足一阶高素容量夹击。剩余证明任务是把 `T_Y<S_Y` 的样本余量升级为解析不等式，或把失败路由到 `PDEC/SAE/ColumnCRT`。
