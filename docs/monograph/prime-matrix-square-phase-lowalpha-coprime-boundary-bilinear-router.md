# Prime Matrix square-phase low-alpha coprime boundary 双线性路由

**状态：** `coprime_boundary_bilinear_balance_blocks_materialized_bounds_open`

coprime boundary lcm edge 已化为双线性形式 `sum_{(d,e)=1,D<de<=16D} lambda_d lambda_e R_de`。按 `max(d,e)/min(d,e)` 拆成 balanced/mid/unbalanced/far 四块后，失败只能来自 balanced 双线性离散偏差或 unbalanced endpoint PDEC。

```text
coprime_boundary_bilinear_identity_closed=true
balance_block_ledger_materialized=true
balanced_bilinear_dispersion_bound_proved=false
unbalanced_endpoint_pdec_excluded=false
coprime_boundary_edge_angle_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 双线性平衡块

| z | bucket | edges | positive | abs | signed | signed/abs | abs share |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | `balanced<=2` | 0 | 0 | 0.000000 | 0.000000 | n/a | n/a |
| 7 | `mid<=4` | 0 | 0 | 0.000000 | 0.000000 | n/a | n/a |
| 7 | `unbalanced<=8` | 0 | 0 | 0.000000 | 0.000000 | n/a | n/a |
| 7 | `far>8` | 0 | 0 | 0.000000 | 0.000000 | n/a | n/a |
| 13 | `balanced<=2` | 38 | 16 | 10.393002 | 4.165415 | 0.400790 | 0.157450 |
| 13 | `mid<=4` | 38 | 16 | 11.547476 | 0.144162 | 0.012484 | 0.174940 |
| 13 | `unbalanced<=8` | 28 | 10 | 9.461482 | -0.001003 | 0.000106 | 0.143338 |
| 13 | `far>8` | 140 | 58 | 34.606321 | 1.641645 | 0.047438 | 0.524272 |
| 31 | `balanced<=2` | 422 | 196 | 160.904830 | 4.411586 | 0.027417 | 0.179123 |
| 31 | `mid<=4` | 480 | 234 | 175.460017 | 0.377080 | 0.002149 | 0.195326 |
| 31 | `unbalanced<=8` | 486 | 232 | 179.948351 | 14.402770 | 0.080038 | 0.200323 |
| 31 | `far>8` | 1916 | 912 | 381.977827 | 0.027719 | 0.000073 | 0.425227 |
| 61 | `balanced<=2` | 1232 | 612 | 470.584874 | 14.927665 | 0.031722 | 0.249309 |
| 61 | `mid<=4` | 1238 | 616 | 404.420714 | -8.532183 | 0.021097 | 0.214256 |
| 61 | `unbalanced<=8` | 1220 | 588 | 334.174118 | 9.612867 | 0.028766 | 0.177040 |
| 61 | `far>8` | 3790 | 1830 | 678.378013 | -30.086033 | 0.044350 | 0.359395 |

## 2. 证明边界

- 已闭合：coprime boundary edge 的双线性恒等式。
- 已物化：balanced/mid/unbalanced/far 四类平衡块。
- 未闭合：balanced/mid 块的双线性离散偏差界。
- 未闭合：unbalanced/far 块的 endpoint PDEC 排斥或吸收。
- 当前样本最大 signed/abs 桶为 `z=13, balanced<=2`，值 `0.400790`。
- 下一目标：`CoprimeBoundaryBilinearDispersionBlocksOrEndpointPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json` | `586cbd19ff15c98e5c81dc5b0448d76c781b47b7855dacd241c292150e7a94ae` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.json` | `bd599e5a085628b2f6ef912ef825ec6a16e95a4a486691a5cb2aaa8c4ad8d46c` |
| `experiments/prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router.py` | `93f0606519cd129f78bcaa2a990e4c0adc71237b67ce59ef03c1de3fbdaa6dd3` |
