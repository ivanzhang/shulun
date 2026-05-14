# Prime Matrix square-phase low-alpha semiprime 四分之一门

**状态：** `semiprime_envelope_split_by_quarter_gate_open`

先验前驱 envelope 进一步被 `P^(1/4)` 门切开：若 block 左端 `z` 满足 `z^4>=P`，则任何复合尾 `E>1` 都会给出 `D_-=qE>z^2>=sqrt(P)`，与 semiprime regime 的 `D_-<sqrt(P)` 矛盾。因此这些块只剩 `D_-=q` 的 prime-D 轴；真正的复合前驱尾项只能存在于 `z<P^(1/4)` 的 ultra-low-alpha 块。当前样本全部处在四分之一门内，复合尾容量为零。

```text
quarter_gate_inequality_proved=true
upper_quarter_composite_predecessor_eliminated=true
prime_d_interval_capacity_bound_proved=false
ultra_low_composite_tail_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局分裂

| quarter rows | ultra-low rows | prime-D reps | composite-E reps | prime-D cap | composite-E cap | composite share |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 0 | 171 | 0 | 12471 | 0 | 0.000000 |

## 2. 最坏 low-alpha 块

| P | block | quarter gate | prime-D cap | composite-E cap | top prime-D | top composite |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 200003 | `(124,248]` | true | 2083 | 0 | `{'d_minus': 131, 'q': 131, 'e': 1, 'capacity': 127, 'h': 1526.7404580152672}` | `None` |

## 3. 每个 P 的总结

| P | low rows | quarter rows | ultra-low rows | prime-D cap | composite-E cap | worst block |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 2 | 0 | 267 | 0 | `(31,62]` |
| 36739 | 3 | 3 | 0 | 1227 | 0 | `(62,124]` |
| 83561 | 4 | 4 | 0 | 3166 | 0 | `(124,248]` |
| 200003 | 4 | 4 | 0 | 7811 | 0 | `(124,248]` |

## 4. 证明边界

- 已闭合：`z>=P^(1/4)` 的块中，semiprime predecessor 只能是 `D_-=q`。
- 未闭合：prime-D 轴上的 prime-u/semiprime-u 短区间容量全局上界。
- 未闭合：`z<P^(1/4)` ultra-low-alpha 中复合 `E` 尾项的容量上界或 PDEC 排除。
- 下一目标：`PrimeDIntervalCapacityBoundAndUltraLowCompositeTailOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json` | `ef5019a7213b88a515692b4e2234c5be6c593552dfac7b856de5c8fa26c87e72` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json` | `88054fba3c7adeea2a5f3d834af2172b157af81f2be8b023c846a6843c5c1780` |
| `experiments/prime_matrix_square_phase_lowalpha_semiprime_quarter_gate_router.py` | `950126e9a766e4c760f90759d70ff465d3dbe824651e46159681583dd06267b7` |
