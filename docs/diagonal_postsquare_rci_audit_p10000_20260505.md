# 对角平方后端点 RCI 审计

**状态：** `experimental_postsquare_rci_support_not_a_proof`

## 参数

- `max_p`: `10000`
- `y_ratio`: `0.36787944117144233`

## 总结

- 检查奇素数个数：`1228`。
- 认证个数：`1228`。
- 未认证个数：`0`。
- 最小 margin：`1`。
- `p>=13` 最小 margin：`1`。
- 最大 `omega_tail`：`2`。
- 满足 `y^3>p^2+p` 的记录数：`1220`。
- 最后一个 `y^3<=p^2+p` 的 p：`23`。

## 最小 margin 样本

| p | y | low | tail | no-tail | one-tail | multi-excess | margin | sample |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 2 | 1 | 0 | 1 | 0 | 0 | 1 | [{'column': 2, 'value': 11}] |
| 5 | 2 | 2 | 1 | 1 | 1 | 0 | 1 | [{'column': 4, 'value': 29}] |
| 7 | 2 | 3 | 2 | 1 | 2 | 0 | 1 | [{'column': 4, 'value': 53}] |
| 17 | 6 | 3 | 2 | 1 | 2 | 0 | 1 | [{'column': 4, 'value': 293}] |
| 11 | 4 | 3 | 1 | 2 | 1 | 0 | 2 | [{'column': 6, 'value': 127}, {'column': 10, 'value': 131}] |
| 13 | 4 | 4 | 2 | 3 | 0 | 1 | 2 | [{'column': 4, 'value': 173}, {'column': 10, 'value': 179}, {'column': 12, 'value': 181}] |
| 23 | 8 | 4 | 2 | 2 | 2 | 0 | 2 | [{'column': 12, 'value': 541}, {'column': 18, 'value': 547}] |
| 19 | 6 | 5 | 2 | 3 | 2 | 0 | 3 | [{'column': 6, 'value': 367}, {'column': 12, 'value': 373}, {'column': 18, 'value': 379}] |
| 37 | 13 | 5 | 2 | 3 | 2 | 0 | 3 | [{'column': 4, 'value': 1373}, {'column': 12, 'value': 1381}, {'column': 30, 'value': 1399}] |
| 29 | 10 | 6 | 2 | 4 | 2 | 0 | 4 | [{'column': 12, 'value': 853}, {'column': 16, 'value': 857}, {'column': 18, 'value': 859}, {'column': 22, 'value': 863}] |
| 31 | 11 | 6 | 1 | 5 | 1 | 0 | 5 | [{'column': 6, 'value': 967}, {'column': 10, 'value': 971}, {'column': 16, 'value': 977}, {'column': 22, 'value': 983}, {'column': 30, 'value': 991}] |
| 41 | 15 | 8 | 3 | 5 | 3 | 0 | 5 | [{'column': 12, 'value': 1693}, {'column': 16, 'value': 1697}, {'column': 18, 'value': 1699}, {'column': 28, 'value': 1709}, {'column': 40, 'value': 1721}] |
| 47 | 17 | 7 | 1 | 6 | 1 | 0 | 6 | [{'column': 4, 'value': 2213}, {'column': 12, 'value': 2221}, {'column': 28, 'value': 2237}, {'column': 30, 'value': 2239}, {'column': 34, 'value': 2243}] |
| 43 | 15 | 9 | 2 | 7 | 2 | 0 | 7 | [{'column': 12, 'value': 1861}, {'column': 18, 'value': 1867}, {'column': 22, 'value': 1871}, {'column': 24, 'value': 1873}, {'column': 28, 'value': 1877}] |
| 53 | 19 | 8 | 1 | 7 | 1 | 0 | 7 | [{'column': 10, 'value': 2819}, {'column': 24, 'value': 2833}, {'column': 28, 'value': 2837}, {'column': 34, 'value': 2843}, {'column': 42, 'value': 2851}] |
| 61 | 22 | 10 | 3 | 7 | 3 | 0 | 7 | [{'column': 6, 'value': 3727}, {'column': 12, 'value': 3733}, {'column': 18, 'value': 3739}, {'column': 40, 'value': 3761}, {'column': 46, 'value': 3767}] |
| 73 | 26 | 10 | 3 | 7 | 3 | 0 | 7 | [{'column': 4, 'value': 5333}, {'column': 18, 'value': 5347}, {'column': 22, 'value': 5351}, {'column': 52, 'value': 5381}, {'column': 58, 'value': 5387}] |
| 59 | 21 | 9 | 1 | 8 | 1 | 0 | 8 | [{'column': 10, 'value': 3491}, {'column': 18, 'value': 3499}, {'column': 30, 'value': 3511}, {'column': 36, 'value': 3517}, {'column': 46, 'value': 3527}] |
| 67 | 24 | 9 | 1 | 8 | 1 | 0 | 8 | [{'column': 4, 'value': 4493}, {'column': 18, 'value': 4507}, {'column': 24, 'value': 4513}, {'column': 28, 'value': 4517}, {'column': 30, 'value': 4519}] |
| 71 | 26 | 11 | 3 | 8 | 3 | 0 | 8 | [{'column': 10, 'value': 5051}, {'column': 18, 'value': 5059}, {'column': 36, 'value': 5077}, {'column': 40, 'value': 5081}, {'column': 46, 'value': 5087}] |

## 审稿解释

对 `p^2+k`，低筛骨架点按尾素因子数分层后精确满足

```text
G_y-T_y = no_tail_reserve - multi_tail_excess。
```

若该差值为正，则存在一个 `p^2+k` 没有任何 `<p` 素因子；由于 `p^2<p^2+k<p^2+p<(p+1)^2`，该点必为素数。
