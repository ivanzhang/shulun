# SN3-D KLS-Multishell 高频列相位审计

**状态：** `sn3d_kls_multishell_frequency_audit_not_a_proof`

## 摘要

- `kls_multishell_record_count`: `2`
- `max_top_frequency_abs_over_excess`: `2.056175`
- `max_partial_fourier_l2_over_excess`: `14.275461`
- `min_flatness`: `0.004695`
- `max_flatness`: `0.014668`

## KLS 候选

| P | y | bands | E/R | excess | l2 | flatness | top h | top/E | partial/E |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 10007 | 75 | `['[1y,2y)', '[4y,8y)']` | 0.187188 | 24.763520 | 16.878125 | 0.014668 | 49 | 1.374721 | 10.546860 |
|  |  | top frequencies |  |  |  |  |  | `h=49:abs=34.043, h=85:abs=33.237, h=232:abs=32.622, h=250:abs=31.799, h=167:abs=30.824, h=197:abs=29.851` |  |
| 50021 | 128 | `['[1y,2y)', '[4y,8y)']` | 0.070956 | 34.748745 | 33.094412 | 0.004695 | 119 | 2.056175 | 14.275461 |
|  |  | top frequencies |  |  |  |  |  | `h=119:abs=71.449, h=128:abs=68.012, h=38:abs=64.691, h=239:abs=62.990, h=246:abs=57.381, h=97:abs=57.003` |  |

## 解释

该审计把 KLS-Multishell 候选重构为列位移 `d=Py-qm` 上的中心化残余，并扫描 `d mod P` 的非零 Fourier 频率。若非零频率持续偏大，则进入高频 Column/PDEC 证书；若频率平坦，则该候选满足 clean KLS/dispersion 输入的形态。

这不是证明；它把 `KLS-Multishell` 的失败形态物化为可检查的高频列相位证书，或把无峰残余送入外部/待证 KLS 估计。
