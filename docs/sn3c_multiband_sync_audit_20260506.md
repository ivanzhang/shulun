# SN3-C 多真分散带同步审计

**状态：** `sn3c_multiband_sync_audit_not_a_proof`

## 参数

- `p_list`: `[5003, 10007, 20011, 50021, 100003, 200003]`
- `w_list`: `[30, 210]`
- `cosine_threshold`: `0.75`

## 摘要

- `multi_true_row_count`: `3`
- `pair_count`: `3`
- `pair_route_counts`: `{'kls_multishell_candidate': 2, 'lowmod_multiband_sync_candidate': 1}`
- `max_multirow_true_excess_over_required`: `0.187188`
- `max_pair_lowmod_cosine`: `0.834817`
- `min_pair_q_shell_gap`: `2525`

## 多带行

| P | y | true bands | true E/R | pair routes |
|---:|---:|---:|---:|---|
| 10007 | 75 | 2 | 0.187188 | `{'kls_multishell_candidate': 1}` |
|  |  | `[4y,8y) q=[1237, 2444]` | 0.120145 | E=15.894240 |
|  |  | `[1y,2y) q=[4970, 9500]` | 0.067043 | E=8.869280 |
| 50021 | 128 | 2 | 0.070956 | `{'kls_multishell_candidate': 1}` |
|  |  | `[1y,2y) q=[25310, 48875]` | 0.049704 | E=24.341283 |
|  |  | `[4y,8y) q=[6223, 12289]` | 0.021252 | E=10.407462 |
| 100003 | 131 | 2 | 0.051451 | `{'lowmod_multiband_sync_candidate': 1}` |
|  |  | `[4y,8y) q=[12513, 24215]` | 0.025730 | E=23.087459 |
|  |  | `[1y,2y) q=[50586, 87922]` | 0.025721 | E=23.079181 |

## 最强低模同步对

- `P=100003, y=131, [4y,8y) vs [1y,2y), route=lowmod_multiband_sync_candidate, q_gap=26370, qwin_cos=0.000000, max_lowmod_cos=0.834817 (q_mod W=30)`
- `P=10007, y=75, [4y,8y) vs [1y,2y), route=kls_multishell_candidate, q_gap=2525, qwin_cos=0.000000, max_lowmod_cos=0.432620 (q_mod W=30)`
- `P=50021, y=128, [1y,2y) vs [4y,8y), route=kls_multishell_candidate, q_gap=13020, qwin_cos=0.000000, max_lowmod_cos=0.244054 (d_mod W=30)`

## 解释

若两个真分散带的 q 壳相交，则多带同步可回到短窗/SAE；若 q 壳不相交但低模签名余弦很高，则回到 PDEC/ColumnCRT；两者都不发生时，剩余只能登记为多壳 KLS/dispersion 候选。

该审计不是证明；它把 SN3-B 的多带叠加硬点进一步路由为 `lowmod_multiband_sync` 或 `kls_multishell`。
