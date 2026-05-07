# SN3-A 中心化低模回流证书

**状态：** `sn3a_centered_lowmod_return_certificate_not_a_proof`

## 来源

- `p_list`: `[5003, 10007, 20011, 50021, 100003, 200003]`
- `w_list`: `[30, 210]`
- `centered_return_share`: `0.75`

## 总结

- `certificate_count`: `8`
- `route_counts`: `{'centered_columncrt_return': 6, 'centered_pdec_return': 2}`
- `total_excess`: `132.550671`
- `total_peak_mass`: `121.448880`
- `total_peak_mass_over_excess`: `0.916245`
- `total_positive_residual_after_peak`: `11.587735`
- `total_positive_residual_over_excess`: `0.087421`
- `min_peak_share`: `0.752736`
- `max_peak_share`: `1.018659`
- `min_contrast_share_lower`: `0.719284`
- `max_contrast_share_lower`: `0.985326`

## 证书表

| P | y | band | route | W | residue | E | peak/E | residual+ | contrast/E | E/R |
|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 50021 | 128 | `[2y,4y)` | `centered_columncrt_return` | 30 | 29 | 16.111747 | 1.018659 | 0.000000 | 0.985326 | 0.032900 |
| 100003 | 147 | `[2y,4y)` | `centered_columncrt_return` | 30 | 28 | 12.104688 | 1.015309 | 0.000000 | 0.981976 | 0.015061 |
| 100003 | 150 | `[1y,2y)` | `centered_columncrt_return` | 30 | 1 | 14.353505 | 0.995960 | 0.057990 | 0.962627 | 0.016239 |
| 200003 | 189 | `[2y,4y)` | `centered_columncrt_return` | 30 | 4 | 16.946479 | 0.938755 | 1.037889 | 0.905422 | 0.011942 |
| 100003 | 172 | `[2y,4y)` | `centered_pdec_return` | 30 | 29 | 26.793706 | 0.893908 | 2.842588 | 0.768908 | 0.028920 |
| 50021 | 125 | `[1y,2y)` | `centered_columncrt_return` | 30 | 2 | 20.326339 | 0.871249 | 2.617027 | 0.837916 | 0.039360 |
| 100003 | 145 | `[2y,4y)` | `centered_pdec_return` | 30 | 23 | 15.023797 | 0.844284 | 2.339438 | 0.719284 | 0.017409 |
| 20011 | 99 | `[2y,4y)` | `centered_columncrt_return` | 30 | 26 | 10.890408 | 0.752736 | 2.692802 | 0.719403 | 0.043678 |

## 证书含义

若某个中心化低模桶 `beta*` 满足 `E_beta* >= theta E_J`，则确定性分裂为：

```text
E_J = E_beta* + (E_J-E_beta*)
E_J-E_beta* <= (1-theta)E_J。
```

因此该带不能继续作为无名分散质量处理：`q mod W` 峰进入 `PDEC`，`d mod W` 峰进入 `ColumnCRT`。表中的 `contrast/E` 是扣除平均桶后仍保留的有限低模对比下界；它只用于定位证书强度，不等于最终排斥证明。
