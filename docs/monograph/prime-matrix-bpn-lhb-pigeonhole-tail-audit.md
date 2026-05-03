# BPN low-hole bucket 鸽巢尾段审计

纯鸽巢递推已把 LHB-7 的结构硬点压到低素数窄带：在扫描范围内，最后失败为 P=103，P=107 起鸽巢尾段闭合。进一步的 P/5 分割判据在 P>=107 的尾段扫描中无失败；连续乘积上界从 P=233 起在扫描中无失败。

## 1. 判据

令 `Hmax(P)` 为长度 `P-1` 的任意 `Q=2310` 连续残基段中最多的互素残基数。
对高素数升序 `ell_1,ell_2,...` 定义递推：

```text
U_0=Hmax(P)
U_j=U_{j-1}-ceil(U_{j-1}/ell_j)
```

若最终 `U_j=0`，则任意同大小洞集都被固定升序梯覆盖；这是纯鸽巢充分条件。

## 2. 总结

- `max_p`: `100000`
- `last_failure`: `103`
- `stable_tail_from_in_scan`: `107`
- `failure_count`: `10`
- `split_denominator`: `5`
- `split_failure_count`: `10`
- `split_tail_failure_count(P>=107)`: `0`
- `split_min_margin`: `-3`
- `split_tail_min_margin(P>=107)`: `0`
- `product_failure_count`: `28`
- `last_product_failure`: `229`
- `product_stable_from_in_scan`: `233`
- `product_tail_min_margin(P>=233)`: `0.5347204008757984`

## 3. 失败窄带

| P | Hmax | high # | residual | first steps |
| ---: | ---: | ---: | ---: | --- |
| 61 | 15 | 12 | 2 | `[{'prime': 13, 'before': 15, 'hit': 2, 'after': 13}, {'prime': 17, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 19, 'before': 12, 'hit': 1, 'after': 11}, {'prime': 23, 'before': 11, 'hit': 1, 'after': 10}, {'prime': 29, 'before': 10, 'hit': 1, 'after': 9}, {'prime': 31, 'before': 9, 'hit': 1, 'after': 8}, {'prime': 37, 'before': 8, 'hit': 1, 'after': 7}, {'prime': 41, 'before': 7, 'hit': 1, 'after': 6}]` |
| 67 | 16 | 13 | 2 | `[{'prime': 13, 'before': 16, 'hit': 2, 'after': 14}, {'prime': 17, 'before': 14, 'hit': 1, 'after': 13}, {'prime': 19, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 23, 'before': 12, 'hit': 1, 'after': 11}, {'prime': 29, 'before': 11, 'hit': 1, 'after': 10}, {'prime': 31, 'before': 10, 'hit': 1, 'after': 9}, {'prime': 37, 'before': 9, 'hit': 1, 'after': 8}, {'prime': 41, 'before': 8, 'hit': 1, 'after': 7}]` |
| 71 | 17 | 14 | 2 | `[{'prime': 13, 'before': 17, 'hit': 2, 'after': 15}, {'prime': 17, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 19, 'before': 14, 'hit': 1, 'after': 13}, {'prime': 23, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 29, 'before': 12, 'hit': 1, 'after': 11}, {'prime': 31, 'before': 11, 'hit': 1, 'after': 10}, {'prime': 37, 'before': 10, 'hit': 1, 'after': 9}, {'prime': 41, 'before': 9, 'hit': 1, 'after': 8}]` |
| 73 | 18 | 15 | 2 | `[{'prime': 13, 'before': 18, 'hit': 2, 'after': 16}, {'prime': 17, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 19, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 23, 'before': 14, 'hit': 1, 'after': 13}, {'prime': 29, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 31, 'before': 12, 'hit': 1, 'after': 11}, {'prime': 37, 'before': 11, 'hit': 1, 'after': 10}, {'prime': 41, 'before': 10, 'hit': 1, 'after': 9}]` |
| 79 | 19 | 16 | 2 | `[{'prime': 13, 'before': 19, 'hit': 2, 'after': 17}, {'prime': 17, 'before': 17, 'hit': 1, 'after': 16}, {'prime': 19, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 23, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 29, 'before': 14, 'hit': 1, 'after': 13}, {'prime': 31, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 37, 'before': 12, 'hit': 1, 'after': 11}, {'prime': 41, 'before': 11, 'hit': 1, 'after': 10}]` |
| 83 | 20 | 17 | 1 | `[{'prime': 13, 'before': 20, 'hit': 2, 'after': 18}, {'prime': 17, 'before': 18, 'hit': 2, 'after': 16}, {'prime': 19, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 23, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 29, 'before': 14, 'hit': 1, 'after': 13}, {'prime': 31, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 37, 'before': 12, 'hit': 1, 'after': 11}, {'prime': 41, 'before': 11, 'hit': 1, 'after': 10}]` |
| 89 | 21 | 18 | 1 | `[{'prime': 13, 'before': 21, 'hit': 2, 'after': 19}, {'prime': 17, 'before': 19, 'hit': 2, 'after': 17}, {'prime': 19, 'before': 17, 'hit': 1, 'after': 16}, {'prime': 23, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 29, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 31, 'before': 14, 'hit': 1, 'after': 13}, {'prime': 37, 'before': 13, 'hit': 1, 'after': 12}, {'prime': 41, 'before': 12, 'hit': 1, 'after': 11}]` |
| 97 | 23 | 19 | 2 | `[{'prime': 13, 'before': 23, 'hit': 2, 'after': 21}, {'prime': 17, 'before': 21, 'hit': 2, 'after': 19}, {'prime': 19, 'before': 19, 'hit': 1, 'after': 18}, {'prime': 23, 'before': 18, 'hit': 1, 'after': 17}, {'prime': 29, 'before': 17, 'hit': 1, 'after': 16}, {'prime': 31, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 37, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 41, 'before': 14, 'hit': 1, 'after': 13}]` |
| 101 | 24 | 20 | 1 | `[{'prime': 13, 'before': 24, 'hit': 2, 'after': 22}, {'prime': 17, 'before': 22, 'hit': 2, 'after': 20}, {'prime': 19, 'before': 20, 'hit': 2, 'after': 18}, {'prime': 23, 'before': 18, 'hit': 1, 'after': 17}, {'prime': 29, 'before': 17, 'hit': 1, 'after': 16}, {'prime': 31, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 37, 'before': 15, 'hit': 1, 'after': 14}, {'prime': 41, 'before': 14, 'hit': 1, 'after': 13}]` |
| 103 | 25 | 21 | 1 | `[{'prime': 13, 'before': 25, 'hit': 2, 'after': 23}, {'prime': 17, 'before': 23, 'hit': 2, 'after': 21}, {'prime': 19, 'before': 21, 'hit': 2, 'after': 19}, {'prime': 23, 'before': 19, 'hit': 1, 'after': 18}, {'prime': 29, 'before': 18, 'hit': 1, 'after': 17}, {'prime': 31, 'before': 17, 'hit': 1, 'after': 16}, {'prime': 37, 'before': 16, 'hit': 1, 'after': 15}, {'prime': 41, 'before': 15, 'hit': 1, 'after': 14}]` |

## 4. P/5 分割判据

先用 `ell<=floor(P/5)` 的高素数执行鸽巢递推，得到残量 `V`；
若剩余高素数个数不少于 `V`，则每个剩余高素数至少再删除一个洞，从而闭合。
该判据在 `P>=107` 的尾段扫描中无失败；低素数窄带仍需真实碰撞能量处理。

| P | Hmax | split bound | split residual | remaining primes | margin |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 99877 | 20756 | 19975 | 4579 | 7324 | 2745 |
| 99881 | 20757 | 19976 | 4579 | 7325 | 2746 |
| 99901 | 20761 | 19980 | 4579 | 7325 | 2746 |
| 99907 | 20763 | 19981 | 4579 | 7326 | 2747 |
| 99923 | 20766 | 19984 | 4580 | 7327 | 2747 |
| 99929 | 20767 | 19985 | 4581 | 7328 | 2747 |
| 99961 | 20773 | 19992 | 4583 | 7328 | 2745 |
| 99971 | 20776 | 19994 | 4583 | 7328 | 2745 |
| 99989 | 20779 | 19997 | 4583 | 7328 | 2745 |
| 99991 | 20779 | 19998 | 4583 | 7329 | 2746 |

## 5. 有限尾段证书

`107<=P<=229` 由精确 `P/5` 分割递推闭合；该段不能直接用连续乘积上界替代。

| P | Hmax | split residual | remaining primes | margin |
| ---: | ---: | ---: | ---: | ---: |
| 107 | 25 | 19 | 19 | 0 |
| 109 | 25 | 19 | 20 | 1 |
| 113 | 26 | 20 | 21 | 1 |
| 127 | 28 | 20 | 21 | 1 |
| 131 | 29 | 21 | 22 | 1 |
| 137 | 31 | 22 | 23 | 1 |
| 139 | 31 | 22 | 24 | 2 |
| 149 | 34 | 24 | 24 | 0 |
| 151 | 34 | 24 | 25 | 1 |
| 157 | 35 | 24 | 25 | 1 |
| 163 | 37 | 26 | 26 | 0 |
| 167 | 37 | 26 | 27 | 1 |
| 173 | 39 | 27 | 28 | 1 |
| 179 | 40 | 27 | 29 | 2 |
| 181 | 40 | 27 | 30 | 3 |
| 191 | 43 | 28 | 30 | 2 |
| 193 | 43 | 28 | 31 | 3 |
| 197 | 44 | 29 | 32 | 3 |
| 199 | 45 | 29 | 33 | 4 |
| 211 | 46 | 28 | 33 | 5 |
| 223 | 50 | 31 | 33 | 2 |
| 227 | 51 | 32 | 34 | 2 |
| 229 | 52 | 33 | 35 | 2 |

## 6. 连续乘积上界

`Hmax(P) * product_{13<=ell<=P/5}(1-1/ell)` 是分割残量的连续上界。
该上界在低尾段偏保守，最后失败为 `P=229`；从 `P=233` 起扫描无失败。

| P | Hmax | split bound | product lhs | remaining primes | margin |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 151 | 34 | 30 | 25.844114 | 25 | -0.844114 |
| 157 | 35 | 31 | 25.746034 | 25 | -0.746034 |
| 163 | 37 | 32 | 27.217236 | 26 | -1.217236 |
| 167 | 37 | 33 | 27.217236 | 27 | -0.217236 |
| 173 | 39 | 34 | 28.688438 | 28 | -0.688438 |
| 179 | 40 | 35 | 29.424039 | 29 | -0.424039 |
| 191 | 43 | 38 | 30.775954 | 30 | -0.775954 |
| 223 | 50 | 44 | 34.101230 | 33 | -1.101230 |
| 227 | 51 | 45 | 34.783255 | 34 | -0.783255 |
| 229 | 52 | 45 | 35.465280 | 35 | -0.465280 |

## 7. 尾段样本

| P | Hmax | high # | residual |
| ---: | ---: | ---: | ---: |
| 99877 | 20756 | 9577 | 0 |
| 99881 | 20757 | 9578 | 0 |
| 99901 | 20761 | 9579 | 0 |
| 99907 | 20763 | 9580 | 0 |
| 99923 | 20766 | 9581 | 0 |
| 99929 | 20767 | 9582 | 0 |
| 99961 | 20773 | 9583 | 0 |
| 99971 | 20776 | 9584 | 0 |
| 99989 | 20779 | 9585 | 0 |
| 99991 | 20779 | 9586 | 0 |

## 8. 审稿结论

该审计给出两层正式接口：
`107<=P<=229` 可用精确分割递推作为有限尾段证书；
`P>=233` 可尝试用显式素数计数和 Mertens 乘积界证明连续乘积不等式。
更低的 `61<=P<=103` 十个素数进入有限碰撞能量窄带。
