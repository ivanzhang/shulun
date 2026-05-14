# Prime Matrix square-phase low-alpha rough-b Selberg 二次型路由

**状态：** `rough_b_selberg_quadratic_upper_materialized_remainder_uniformity_open`

本步把 rough-b 幸存者上界写成真正的维数一 Selberg 二次型。对任意 `z`-rough 的 b，只有 `d=1` 贡献，因此 `1_rough(b) <= (sum_{d|b} lambda_d)^2`；样本中所有 z 行均满足该上界。二次型再拆成随机主项 `A_m=N/m` 与 squarefree 低模余项。当前样本常数包覆盖，但全局仍需证明 Selberg 余项统一上界，或把余项过大命名为 Squarefree-LowMod-PDEC 并排斥。

```text
selberg_quadratic_upper_identity_closed=true
sample_constant_covers_selberg_quadratic=true
selberg_remainder_uniform_bound_proved=false
squarefree_lowmod_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. Selberg 二次型账本

| z | D | support | rough | direct Q | model Q | Mertens | Q/rough | Q/Mertens | remainder/Mertens | covered |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 7 | 1000 | 16 | 9965 | 10457.605581 | 10474.974863 | 9980.800000 | 1.049434 | 1.047772 | -0.001740 | true |
| 13 | 1000 | 49 | 8365 | 8973.404100 | 8988.442386 | 8375.496503 | 1.072732 | 1.071388 | -0.001796 | true |
| 31 | 1000 | 153 | 6712 | 7512.921115 | 7496.890000 | 6674.442043 | 1.119327 | 1.125625 | 0.002402 | true |
| 61 | 1000 | 250 | 5750 | 6782.239511 | 6776.355588 | 5745.893306 | 1.179520 | 1.180363 | 0.001024 | true |

## 2. 汇总

| values | D level | constant | upper failures | constant failures | worst direct row | worst remainder row |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 43666 | 1000 | 1.350000 | 0 | 0 | `{'z': 61, 'd_level': 1000, 'support_size': 250, 'value_count': 43666, 'rough_count': 5750, 'direct_selberg_quadratic': 6782.2395112634385, 'model_selberg_quadratic': 6776.355587834045, 'mertens_model': 5745.893305893899, 'selberg_remainder': 5.88392342939369, 'upper_bound_verified': True, 'direct_over_rough': 1.1795199150023372, 'direct_over_mertens': 1.180362939267685, 'rough_over_mertens': 1.0007147181277953, 'model_over_mertens': 1.1793389168718362, 'remainder_over_mertens': 0.0010240223958489108, 'covered_by_constant': True, 'constant': 1.35}` | `{'z': 31, 'd_level': 1000, 'support_size': 153, 'value_count': 43666, 'rough_count': 6712, 'direct_selberg_quadratic': 7512.9211154188515, 'model_selberg_quadratic': 7496.890000129352, 'mertens_model': 6674.442042551466, 'selberg_remainder': 16.031115289499212, 'upper_bound_verified': True, 'direct_over_rough': 1.1193267454438098, 'direct_over_mertens': 1.1256253432903969, 'rough_over_mertens': 1.0056271306588762, 'model_over_mertens': 1.123223477308597, 'remainder_over_mertens': 0.0024018659817998706, 'covered_by_constant': True, 'constant': 1.35}` |

## 3. 证明边界

- 已闭合：给定权重后 `rough_count <= Selberg quadratic` 是确定性不等式。
- 已物化：样本中二次型主项与 squarefree 余项拆分账本。
- 未闭合：全局证明 squarefree 低模余项足够小，使二次型由维数一 Mertens 包络支付。
- 未闭合：排斥持久 Squarefree-LowMod-PDEC/SAE。
- 下一目标：`SelbergQuadraticRemainderUniformBoundOrSquarefreeLowModPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json` | `74d26984ec6cb02e19f3f3d51f798d965b34bc9650451ab73d1bbb5fba081e3a` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json` | `e3fd8819110a576f1a5ea953b553ef1acb3493a6c7b8b8d6b2c7644d99b4b77c` |
| `experiments/prime_matrix_square_phase_lowalpha_rough_b_selberg_quadratic_router.py` | `2b25bbf437c730cc44ae7a28a16144ffa61f682275027d234da6656f5bb90271` |
