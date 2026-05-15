# Prime Matrix square-phase effective capacity refinement

**状态：** `square_phase_total_capacity_refined_to_effective_capacity_prime_nonempty_open`

总容量路线已被精炼：尾素总容量 `C_total` 分成真正命中低洞的有效容量 `C_eff=GoodShell` 和已经被低筛杀掉的废容量 `Waste=BadTail`。因此逐侧有 `H-C_eff=Prime`。此前的 `Prime>BadTail` 是证明 `H>C_total` 的强充分条件，但不是命题闭合的必要目标；真正剩余回到有效容量口径下的 `Prime>0`，或证明 `Prime=0` 时有效容量完全贴合低洞会产生 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
total_identity_failure_count=0
effective_prime_nonempty_proved=false
row_column_unconditional_closed=false
```

## 1. 有效容量恒等式

设 `H` 为 `q<=floor(4P/5)` 低筛后幸存列数，`C_total` 为 `floor(4P/5)<q<P` 的全部高尾槽数。高尾槽只有命中低洞时才有能力覆盖 `H`；命中已被低筛杀掉的列只是废容量。

逐侧精确分解为：

```text
H = Prime + GoodShell
C_total = GoodShell + BadTail
C_eff = GoodShell
H - C_eff = Prime
C_total - C_eff = BadTail.
```

因此 `H>C_total` 等价于 `Prime>BadTail`，只是一个强充分判据；真正有效容量口径下，目标就是 `Prime>0`。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `effective_capacity_refinement` | `closed` | The only tail slots that can cover low survivors are exactly the GoodShell semiprime slots; all BadTail slots are waste capacity for the low-hole covering problem. |
| `exact_effective_identity` | `closed` | For each sign, H_y-C_eff = square-anchor-prime-count, where C_eff is tail capacity restricted to low survivors. |
| `total_capacity_sufficient_only` | `closed` | The older criterion H_y>C_total is sufficient but stronger than needed; it asks Prime>Waste, while the exact target is Prime>0. |
| `remaining_effective_prime_nonempty` | `open` | A global proof still needs the effective identity to have positive right side, or a PDEC/SAE contradiction if Prime=0. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| square-anchor primes | 97145 | 97396 | 194541 |
| effective tail capacity | 5046 | 5343 | 10389 |
| waste tail capacity | 38232 | 37738 | 75970 |

## 4. 样本表

| P | sign | H | Prime | C_eff | Waste | H-C_eff | Prime-Waste |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 3 | 0 | 1 | 3 | 2 |
| 13 | `minus` | 3 | 3 | 0 | 1 | 3 | 2 |
| 17 | `plus` | 1 | 1 | 0 | 0 | 1 | 1 |
| 17 | `minus` | 3 | 3 | 0 | 0 | 3 | 3 |
| 19 | `plus` | 3 | 3 | 0 | 1 | 3 | 2 |
| 19 | `minus` | 4 | 4 | 0 | 1 | 4 | 3 |
| 23 | `plus` | 3 | 2 | 1 | 1 | 2 | 1 |
| 23 | `minus` | 3 | 3 | 0 | 1 | 3 | 2 |
| 29 | `plus` | 4 | 4 | 0 | 0 | 4 | 4 |
| 29 | `minus` | 5 | 5 | 0 | 0 | 5 | 5 |
| 31 | `plus` | 5 | 5 | 0 | 1 | 5 | 4 |
| 31 | `minus` | 4 | 4 | 0 | 1 | 4 | 3 |
| 101 | `plus` | 11 | 11 | 0 | 4 | 11 | 7 |
| 101 | `minus` | 12 | 12 | 0 | 3 | 12 | 9 |
| 499 | `plus` | 42 | 40 | 2 | 16 | 40 | 24 |
| 499 | `minus` | 45 | 44 | 1 | 17 | 44 | 27 |
| 1009 | `plus` | 79 | 72 | 7 | 25 | 72 | 47 |
| 1009 | `minus` | 77 | 70 | 7 | 27 | 70 | 43 |
| 2003 | `plus` | 132 | 125 | 7 | 47 | 125 | 78 |
| 2003 | `minus` | 144 | 139 | 5 | 52 | 139 | 87 |
| 4999 | `plus` | 317 | 300 | 17 | 117 | 300 | 183 |
| 4999 | `minus` | 303 | 289 | 14 | 114 | 289 | 175 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `EffectiveCapacityRefinementClosed` | `true` | `true` | 高尾总容量已精确拆成有效 GoodShell 与废容量 BadTail。 | closed |
| `TotalCapacityRouteMarkedSufficientOnly` | `true` | `true` | `Prime>BadTail` 只是强充分路线，不是命题闭合的必要目标。 | closed |
| `EffectivePrimeNonempty` | `false` | `false` | 仍需证明 `H-C_eff=Prime` 的右侧全局为正。 | SquarePhaseEffectiveCapacityPrimeNonempty |
| `PrimeVoidEffectiveCapacityPDEC` | `false` | `false` | 若 `Prime=0`，需要把有效容量完全贴合低洞抽取为相位缺陷。 | SquarePhaseEffectiveCapacityDefectPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只校准容量口径，不关闭全局行/列命题。 | SquarePhaseEffectiveCapacityPrimeNonempty OR SquarePhaseEffectiveCapacityDefectPDECSAEReturn |

## 6. 下一步

- 主攻：`SquarePhaseEffectiveCapacityPrimeNonempty`。
- 备选回流：`SquarePhaseEffectiveCapacityDefectPDECSAEReturn`。
- 后续不应把废容量 BadTail 当作必须战胜的终端对象；它只服务于强充分的总容量判据。真正闭合必须证明有效容量剩余 `Prime` 非空，或把 `Prime=0` 的有效容量完全贴合抽成 PDEC/SAE。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-effective-capacity-refinement-ledger.json` | `863b86a223a33a1f469f4358c5b14e70ce07b2badf08905196a8563fb0f104e7` |
| `experiments/prime_matrix_square_phase_effective_capacity_refinement_router.py` | `2da8ebe5804bdd15d2cb28bf31f3747dc0bd807bcf821b7cad65fab733422dfc` |
