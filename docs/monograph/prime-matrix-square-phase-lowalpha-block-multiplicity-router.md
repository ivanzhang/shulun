# Prime Matrix square-phase low-alpha block multiplicity 路由

**状态：** `block_multiplicity_reduced_to_omega_block_weighted_density_open`

固定 `(D_-,u)` 后，一阶负载的重复命中只能来自 `D_-` 中属于当前 dyadic 块的原始素数因子。因此实际 multiplicity 被 `omega_B(D_-)` 控制；样本中该上界无失败。剩余硬点从无结构重复计数压成 `omega_B(D_-)` 加权的 Buchstab 短区间密度上界，或失败形成块素数因子 PDEC。

```text
block_multiplicity_bound_closed=true
multiplicity_bound_failure_count=0
omega_weighted_density_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 总体容量

| hits | u capacity | hits/u capacity | omega weighted capacity | hits/weighted |
| ---: | ---: | ---: | ---: | ---: |
| 21504 | 203463 | 0.105690 | 210424 | 0.102194 |

## 2. 最坏 low-alpha 块

| P | block | hits | unique (D,u) | active D | weighted capacity | weighted density | max mult | max omega | top mult key |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 200003 | `(31,62]` | 4540 | 4264 | 1173 | 47014 | 0.096567 | 3 | 3 | `{'d_minus': 106079, 'u': 377089, 'multiplicity': 3, 'omega_block': 3, 'q_values': [37, 47, 61]}` |

## 3. 每个 P 的总结

| P | low blocks | hits | weighted capacity | hits/weighted | worst block |
| ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 412 | 3090 | 0.133333 | `(31,62]` |
| 36739 | 3 | 2040 | 17832 | 0.114401 | `(31,62]` |
| 83561 | 4 | 5659 | 53104 | 0.106564 | `(31,62]` |
| 200003 | 4 | 13393 | 136398 | 0.098191 | `(31,62]` |

## 4. 证明边界

- 已闭合：固定 `(D_-,u)` 的重复命中数不超过 `omega_B(D_-)`。
- 未闭合：需要证明 `omega_B(D_-)` 加权后的 Buchstab 短区间密度上界。
- 下一目标：`OmegaBlockWeightedBuchstabDensityBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json` | `0efba46c4858a88fed2f05dd6d6563563d1d04a4715edcd2904c9e35f2717522` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json` | `b9530d634cb41da605749e7f5738f97378dd58b1570d08e2c82959d01c22bf95` |
| `experiments/prime_matrix_square_phase_lowalpha_block_multiplicity_router.py` | `629eb11566200fca5ff1a557eed3ec1e78448ffad5553229205765b9a5a13f6a` |
