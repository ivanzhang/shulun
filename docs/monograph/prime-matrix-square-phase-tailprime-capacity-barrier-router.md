# Prime Matrix square-phase tail-prime capacity barrier

**状态：** `square_phase_even_layer_tiling_reduced_to_lowhole_beats_tailprime_open`

偶半网格候选槽容量已压到尾素数：由于 `q>P*4/5`，固定 `b` 的 `u` 窗口实长度小于 `5/8`，所以每个尾素每侧最多贡献一个候选槽。完全有效半素数铺砖因此强制 `H<=TailPrimeCount`。有限审计中 `H>TailPrimeCount` 全部成立；全局仍需证明 `Alpha45LowHoleCountBeatsTailPrimeCount`，或证明失败回流为低洞亏损/尾素容量异常的 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
single_slot_failure_count=0
finite_lowhole_tailprime_failure_count=0
global_lowhole_beats_tailprime_proved=false
row_column_unconditional_closed=false
```

## 1. 尾素容量屏障

固定 `b` 后，plus/minus 的 `u` 可行区间实长度都等于

```text
((P-1)/2)/(P-2b).
```

由于尾素层满足 `P-2b>4P/5`，该长度小于 `5/8`，因此每个尾素 `q=P-2b` 每侧最多产生一个候选槽。于是

```text
candidate_slots^sign(P) <= #{q prime: floor(4P/5)<q<P}.
```

若发生 full effective semiprime tiling，则必须有

```text
H_alpha45^sign(P) <= TailPrimeCount_alpha45(P).
```

所以排除完全铺砖的下一输入是证明低洞数超过尾素数。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `single_u_slot_per_tail_prime` | `closed` | For q>P*4/5, the fixed-b u-window has real length <5/8, so each tail prime contributes at most one slot per sign. |
| `candidate_capacity_le_tail_prime_count` | `closed` | For each sign, candidate prime-pair slots are bounded by the number of tail primes q in (floor(4P/5),P). |
| `full_tiling_forces_H_le_tail_prime_count` | `closed` | A full effective semiprime tiling would force H_alpha45^sign(P)<=TailPrimeCount_alpha45(P). |
| `remaining_lowhole_beats_tailprime_input` | `open` | A global proof needs H_alpha45^sign(P)>TailPrimeCount_alpha45(P), or a proof that failure routes to PDEC/SAE. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| low survivors H | 102191 | 102739 | 204930 |
| tail prime count | 38678 | 38678 | 77356 |
| raw layer slots | 20379 | 22783 | 43162 |
| candidate prime-pair slots | 5046 | 5343 | 10389 |

最紧 `H-tail` 样本：`P=3`，`sign=plus`，`H=1`，`tail=0`，`margin=1`。

## 4. 样本表

| P | sign | H | tail primes | raw slots | candidates | H-tail | H-candidates | max slots/b |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 1 | 0 | 0 | 2 | 3 | 0 |
| 13 | `minus` | 3 | 1 | 1 | 0 | 2 | 3 | 1 |
| 17 | `plus` | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| 17 | `minus` | 3 | 0 | 0 | 0 | 3 | 3 | 0 |
| 19 | `plus` | 3 | 1 | 0 | 0 | 2 | 3 | 0 |
| 19 | `minus` | 4 | 1 | 1 | 0 | 3 | 4 | 1 |
| 23 | `plus` | 3 | 1 | 1 | 1 | 2 | 2 | 1 |
| 23 | `minus` | 3 | 1 | 1 | 0 | 2 | 3 | 1 |
| 29 | `plus` | 4 | 0 | 0 | 0 | 4 | 4 | 0 |
| 29 | `minus` | 5 | 0 | 0 | 0 | 5 | 5 | 0 |
| 31 | `plus` | 5 | 1 | 0 | 0 | 4 | 5 | 0 |
| 31 | `minus` | 4 | 1 | 1 | 0 | 3 | 4 | 1 |
| 101 | `plus` | 11 | 3 | 2 | 0 | 8 | 11 | 1 |
| 101 | `minus` | 12 | 3 | 1 | 0 | 9 | 12 | 1 |
| 499 | `plus` | 42 | 16 | 7 | 2 | 26 | 40 | 1 |
| 499 | `minus` | 45 | 16 | 10 | 1 | 29 | 44 | 1 |
| 1009 | `plus` | 79 | 29 | 12 | 7 | 50 | 72 | 1 |
| 1009 | `minus` | 77 | 29 | 20 | 7 | 48 | 70 | 1 |
| 2003 | `plus` | 132 | 51 | 23 | 7 | 81 | 125 | 1 |
| 2003 | `minus` | 144 | 51 | 33 | 5 | 93 | 139 | 1 |
| 4999 | `plus` | 317 | 118 | 60 | 17 | 199 | 300 | 1 |
| 4999 | `minus` | 303 | 118 | 72 | 14 | 185 | 289 | 1 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SingleTailPrimeSlotCapacityClosed` | `true` | `true` | 每个尾素每侧最多贡献一个候选槽。 | closed |
| `FiniteLowHoleBeatsTailPrime` | `true` | `false` | 有限扫描 P<=5000 中 H 均大于尾素数。 | finite evidence only |
| `GlobalLowHoleBeatsTailPrime` | `false` | `false` | 仍需全局证明低洞数超过尾素数，从而排除完全铺砖。 | Alpha45LowHoleCountBeatsTailPrimeCount |
| `LowHoleTailPrimeFailurePDEC` | `false` | `false` | 若 H<=尾素数，必须抽取低洞亏损或尾素容量异常的相位缺陷。 | LowHoleTailPrimeCountFailurePDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭候选槽容量上界，不关闭全局行/列命题。 | Alpha45LowHoleCountBeatsTailPrimeCount OR LowHoleTailPrimeCountFailurePDECSAEReturn |

## 6. 下一步

- 主攻：`Alpha45LowHoleCountBeatsTailPrimeCount`。
- 备选回流：`LowHoleTailPrimeCountFailurePDECSAEReturn`。
- 这里不能把有限 `H>tail` 当成全局证明；下一步要给出低洞数下界与尾素数上界的严格比较，或把失败作为 PDEC/SAE 对象。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-tailprime-capacity-barrier-ledger.json` | `9e185032fd2f1e91f11d43662473e5bdec80f3da0c335e6fdbbbc844ed22bee7` |
| `experiments/prime_matrix_square_phase_tailprime_capacity_barrier_router.py` | `b09fa25c132c2f65369eb6bad4ef3d4b0a016a4cd487a801d878f52b6fcddbe3` |
