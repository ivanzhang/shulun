# Prime Matrix square-phase low-alpha ultra-low 复合尾项

**状态：** `ultralow_composite_tail_reduced_to_next_prime_birth_and_rankin_selberg_open`

ultra-low 复合前驱尾项有更精确的出生门：设 `p_+(z)` 为大于 block 左端 `z` 的最小素数。若 `p_+(z)^4>=P`，则任意复合 `E>1` 与 block 素数 `q` 都满足 `D_-=qE>=p_+(z)^2>=sqrt(P)`，不可能进入 semiprime regime。因此复合尾项只在 `p_+(z)^4<P` 后出生；出生后其候选为 `D_-=qE<sqrt(P)`、`E` 为 `z`-rough。样本第一次出生在 `P=1874177` 的 `(31,62]` 块，唯一表示为 `37*37`，精确 prime/semiprime 容量为 102，整数容量为 1369。

```text
next_prime_quarter_gate_proved=true
composite_tail_birth_materialized=true
composite_tail_rankin_selberg_bound_proved=false
composite_tail_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局尾项容量

| closed rows | open ultra-low rows | composite reps | exact cap | integer cap | exact/integer |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 24 | 1 | 1 | 102 | 1369 | 0.074507 |

## 2. 最坏 ultra-low 块

| P | block | next prime | open | reps | exact cap | integer cap | top representation |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1874177 | `(31,62]` | 37 | true | 1 | 102 | 1369 | `{'q': 37, 'e': 37, 'd_minus': 1369, 'prime_u_capacity': 68, 'semiprime_u_capacity': 34, 'exact_capacity': 102, 'integer_capacity': 1369, 'h': 1369.0116873630386}` |

## 3. 每个 P 的总结

| P | low rows | gate-closed rows | open ultra-low rows | composite reps | exact cap | worst block |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 2 | 0 | 0 | 0 | `(31,62]` |
| 36739 | 3 | 3 | 0 | 0 | 0 | `(31,62]` |
| 83561 | 4 | 4 | 0 | 0 | 0 | `(31,62]` |
| 200003 | 4 | 4 | 0 | 0 | 0 | `(31,62]` |
| 1000003 | 6 | 6 | 0 | 0 | 0 | `(31,62]` |
| 1874177 | 6 | 5 | 1 | 1 | 102 | `(31,62]` |

## 4. 证明边界

- 已闭合：下一素数四分之一门 `p_+(z)^4>=P` 排除复合尾。
- 已闭合：复合尾出生后的候选 envelope 为 `D_-=qE<sqrt(P)`、`E` 为 `z`-rough。
- 未闭合：出生后复合尾的 Rankin/Selberg 全局容量上界。
- 未闭合：若复合尾容量尖峰持续出现，对应 PDEC 的排除。
- 下一目标：`UltraLowCompositeTailRankinSelbergBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json` | `33dfbaed09353024edee0ccc717a184111e0611f8cb4f4ff49cf802b2f83d526` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json` | `1ee763007af6d4aa7f09b483e088b5bb35744c0f255e189bce7e07c9414e7ac6` |
| `experiments/prime_matrix_square_phase_lowalpha_ultralow_composite_tail_router.py` | `6faae453655f8f5fa4efed578204876678d7ce6ee312a35beeb867ec98d09a83` |
