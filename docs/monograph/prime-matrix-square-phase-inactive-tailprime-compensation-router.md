# Prime Matrix square-phase inactive tail-prime compensation

**状态：** `square_phase_lowhole_tailprime_target_reduced_to_prime_beats_inactive_tail_open`

本步把 `Alpha45LowHoleCountBeatsTailPrimeCount` 精确改写为补偿恒等式：`H-tail = PrimeWindow-InactiveTailPrime`。因此若低洞数不能压过尾素数，不是槽容量本身还缺一项，而是必须出现 `PrimeWindow<=InactiveTailPrime` 的终端缺陷。有限审计中该缺陷未出现；全局仍需证明平方端点素数数压过未激活尾素数，或把相反情况登记为可排斥的 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
low_decomposition_failure_count=0
compensation_identity_failure_count=0
finite_prime_inactive_failure_count=0
global_prime_beats_inactive_tail_proved=false
row_column_unconditional_closed=false
```

## 1. 补偿恒等式

沿用 `alpha=4/5` 与单尾素容量屏障。对每个方向都有

```text
H = PrimeWindow + GoodTailSlot
TailPrimeCount = GoodTailSlot + InactiveTailPrime
H - TailPrimeCount = PrimeWindow - InactiveTailPrime.
```

因此当前目标 `H>TailPrimeCount` 等价于

```text
PrimeWindow > InactiveTailPrime.
```

反例链若继续存在，就必须把短区间素数数量压到不超过未激活尾素数数量。

## 2. 判定行

| name | status | statement |
| --- | --- | --- |
| `lowhole_prime_goodslot_decomposition` | `closed` | H_alpha45^sign(P)=PrimeWindow^sign(P)+GoodTailSlot^sign(P). |
| `inactive_tail_compensation_identity` | `closed` | H_alpha45^sign(P)-TailPrimeCount_alpha45(P)=PrimeWindow^sign(P)-InactiveTailPrime^sign(P). |
| `failure_forces_prime_deficit` | `closed` | If H_alpha45^sign(P)<=TailPrimeCount_alpha45(P), then PrimeWindow^sign(P)<=InactiveTailPrime^sign(P). |
| `prime_beats_inactive_tail_input` | `open` | A global proof still needs PrimeWindow^sign(P)>InactiveTailPrime^sign(P), or a PDEC/SAE exclusion of the opposite defect. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| H low survivors | 102191 | 102739 | 204930 |
| PrimeWindow | 97145 | 97396 | 194541 |
| TailPrimeCount | 38678 | 38678 | 77356 |
| GoodTailSlot | 5046 | 5343 | 10389 |
| InactiveTailPrime | 33632 | 33335 | 66967 |

全扫描最紧 `PrimeWindow-InactiveTail`：`P=3`，`sign=plus`，`PrimeWindow=1`，`InactiveTail=0`，`margin=1`。
`P>=23` 最紧样本：`P=23`，`sign=plus`，`PrimeWindow=2`，`InactiveTail=0`，`margin=2`。

## 4. 样本表

| P | sign | H | PrimeWindow | tail | good slots | inactive | no slot | composite slot | margin |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 3 | 1 | 0 | 1 | 1 | 0 | 2 |
| 13 | `minus` | 3 | 3 | 1 | 0 | 1 | 0 | 1 | 2 |
| 17 | `plus` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 17 | `minus` | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| 19 | `plus` | 3 | 3 | 1 | 0 | 1 | 1 | 0 | 2 |
| 19 | `minus` | 4 | 4 | 1 | 0 | 1 | 0 | 1 | 3 |
| 23 | `plus` | 3 | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 23 | `minus` | 3 | 3 | 1 | 0 | 1 | 0 | 1 | 2 |
| 29 | `plus` | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 4 |
| 29 | `minus` | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 5 |
| 31 | `plus` | 5 | 5 | 1 | 0 | 1 | 1 | 0 | 4 |
| 31 | `minus` | 4 | 4 | 1 | 0 | 1 | 0 | 1 | 3 |
| 101 | `plus` | 11 | 11 | 3 | 0 | 3 | 1 | 2 | 8 |
| 101 | `minus` | 12 | 12 | 3 | 0 | 3 | 2 | 1 | 9 |
| 499 | `plus` | 42 | 40 | 16 | 2 | 14 | 9 | 5 | 26 |
| 499 | `minus` | 45 | 44 | 16 | 1 | 15 | 6 | 9 | 29 |
| 1009 | `plus` | 79 | 72 | 29 | 7 | 22 | 17 | 5 | 50 |
| 1009 | `minus` | 77 | 70 | 29 | 7 | 22 | 9 | 13 | 48 |
| 2003 | `plus` | 132 | 125 | 51 | 7 | 44 | 28 | 16 | 81 |
| 2003 | `minus` | 144 | 139 | 51 | 5 | 46 | 18 | 28 | 93 |
| 4999 | `plus` | 317 | 300 | 118 | 17 | 101 | 58 | 43 | 199 |
| 4999 | `minus` | 303 | 289 | 118 | 14 | 104 | 46 | 58 | 185 |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LowholePrimeGoodSlotDecompositionClosed` | `true` | `true` | 低洞精确拆成平方端点素数与有效尾素-素余因子槽。 | closed |
| `InactiveTailCompensationIdentityClosed` | `true` | `true` | `H-tail` 与 `PrimeWindow-inactive tail` 完全相同。 | closed |
| `FinitePrimeBeatsInactiveTail` | `true` | `false` | 有限扫描 P<=5000 中 PrimeWindow 均压过 inactive tail。 | finite evidence only |
| `GlobalPrimeBeatsInactiveTail` | `false` | `false` | 仍需全局证明平方端点素数数压过未激活尾素数。 | PrimeWindowCountBeatsInactiveTailPrimeCount |
| `InactiveTailPrimeDefectPDEC` | `false` | `false` | 若 PrimeWindow<=InactiveTail，则必须把未激活尾素优势登记为相位缺陷并排斥。 | InactiveTailPrimeDefectPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭补偿恒等式，不关闭全局行/列命题。 | PrimeWindowCountBeatsInactiveTailPrimeCount OR InactiveTailPrimeDefectPDECSAEReturn |

## 6. 下一步

- 主攻：`PrimeWindowCountBeatsInactiveTailPrimeCount`。
- 备选回流：`InactiveTailPrimeDefectPDECSAEReturn`。
- 这里明确显示：若不引用或证明平方根长度端点素数下界，闭合必须转为排斥 `InactiveTailPrime` 的相位缺陷。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-inactive-tailprime-compensation-ledger.json` | `40c4fb503a2497f6a1e91bd3619570e1a947cf079c4ad0ed569486ff187999c2` |
| `experiments/prime_matrix_square_phase_inactive_tailprime_compensation_router.py` | `576d92751f765da0c830ac8070c13d18fbe5fbb8182e8bcadd5db4fb4da9de7c` |
