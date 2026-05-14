# Prime Matrix square-phase low-alpha tail lcm shell 路由

**状态：** `tail_lcm_overflow_shell_ledger_closed_shell_bounds_open`

`m>D` 截断尾不是均匀高维噪声，而是 lcm 超界边界效应。本账本按 `m/D` 的 dyadic 壳层分解 tail：样本中主要绝对质量集中在 `(D,16D]` 低超界壳层，高超界壳层快速变薄。因此 tail 角度失败可进一步定位到具体 low-overflow lcm shell，并登记为 BoundaryLCM-PDEC；远壳层应走 thinning/Rankin 型预算。

```text
tail_lcm_shell_decomposition_closed=true
low_overflow_shells_identified=true
high_overflow_tail_thinning_observed=true
low_overflow_shell_angle_bound_proved=false
boundary_lcm_pdec_excluded=false
truncation_tail_angle_bound_proved=false
row_column_unconditional_closed=false
```

## 1. tail 总览

| z | tail count | tail net | tail abs | tail angle | low abs share | dominant shell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 7 | 0 | 0.000000 | 0.000000 | n/a | n/a | `n/a` |
| 13 | 15 | 1.388320 | 21.630592 | 0.051287 | 0.985611 | `(1D,2D]` |
| 31 | 963 | 1.407346 | 467.428124 | 0.002264 | 0.825150 | `(2D,4D]` |
| 61 | 5476 | -3.443867 | 1231.665658 | 0.002074 | 0.780871 | `(1D,2D]` |

## 2. 壳层明细

| z | shell | count | positive | net | abs | angle | signed/abs |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `(1D,2D]` | 4 | 1 | -5.065904 | 9.671581 | 0.490636 | 0.523793 |
| 13 | `(2D,4D]` | 5 | 3 | 6.764730 | 8.277850 | 0.670955 | 0.817209 |
| 13 | `(4D,8D]` | 3 | 1 | -0.842109 | 2.408423 | 0.331090 | 0.349652 |
| 13 | `(8D,16D]` | 2 | 1 | 0.842857 | 0.961485 | 0.667353 | 0.876620 |
| 13 | `(16D,32D]` | 1 | 0 | -0.311253 | 0.311253 | 1.000000 | 1.000000 |
| 31 | `(1D,2D]` | 52 | 24 | -12.282144 | 121.427137 | 0.084173 | 0.101148 |
| 31 | `(2D,4D]` | 68 | 33 | 1.912437 | 121.626117 | 0.012424 | 0.015724 |
| 31 | `(4D,8D]` | 84 | 34 | 1.097310 | 85.666565 | 0.010005 | 0.012809 |
| 31 | `(8D,16D]` | 94 | 49 | 12.656609 | 56.978664 | 0.164703 | 0.222129 |
| 31 | `(16D,32D]` | 100 | 46 | -2.455587 | 40.571649 | 0.050044 | 0.060525 |
| 31 | `(32D,64D]` | 115 | 55 | -0.703656 | 24.940246 | 0.022684 | 0.028214 |
| 31 | `(64D,128D]` | 124 | 72 | 0.935392 | 12.287688 | 0.068440 | 0.076124 |
| 31 | `(128D,256D]` | 130 | 78 | 0.306839 | 3.447445 | 0.082602 | 0.089005 |
| 31 | `(256D,512D]` | 126 | 64 | -0.054665 | 0.468632 | 0.106523 | 0.116648 |
| 31 | `(512D,1024D]` | 70 | 28 | -0.005190 | 0.013981 | 0.276554 | 0.371258 |
| 61 | `(1D,2D]` | 133 | 67 | 17.088230 | 290.045603 | 0.046173 | 0.058916 |
| 61 | `(2D,4D]` | 189 | 93 | -26.432024 | 273.317953 | 0.075415 | 0.096708 |
| 61 | `(4D,8D]` | 254 | 117 | -5.992807 | 222.204550 | 0.020901 | 0.026970 |
| 61 | `(8D,16D]` | 342 | 170 | 12.912863 | 176.203570 | 0.054611 | 0.073284 |
| 61 | `(16D,32D]` | 469 | 234 | -6.993858 | 129.273229 | 0.041835 | 0.054101 |
| 61 | `(32D,64D]` | 611 | 303 | 2.094907 | 79.601274 | 0.019755 | 0.026318 |
| 61 | `(64D,128D]` | 736 | 348 | 2.750637 | 43.906406 | 0.052576 | 0.062648 |
| 61 | `(128D,256D]` | 896 | 475 | 0.827014 | 14.435275 | 0.048115 | 0.057291 |
| 61 | `(256D,512D]` | 1078 | 643 | 0.297922 | 2.545652 | 0.101231 | 0.117032 |
| 61 | `(512D,1024D]` | 768 | 416 | 0.003249 | 0.132147 | 0.019535 | 0.024589 |

## 3. 证明边界

- 已闭合：tail 的 lcm-overflow dyadic shell 分解。
- 已物化：tail 失败会落到具体 `(2^jD,2^{j+1}D]` 壳层。
- 未闭合：低超界壳层 `(D,16D]` 的统一角度界或 BoundaryLCM-PDEC 排斥。
- 未闭合：高超界壳层的 thinning/Rankin 预算。
- 下一目标：`LowOverflowLCMShellAngleBoundOrBoundaryLCMPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json` | `e9ae5080e5df364181f29c6acdff03bdb8259181f99065df89405a98be3fa2fd` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `experiments/prime_matrix_square_phase_lowalpha_tail_lcm_shell_router.py` | `e08c5b9745b22d61369c628658c59f34a35a7ba41dfa73bcc0f9c2b73e544587` |
