# Prime Matrix square-phase inactive tail-prime defect localization

**状态：** `inactive_tailprime_defect_localized_to_no_slot_or_composite_slot_open`

本步把 `PrimeWindowCountBeatsInactiveTailPrimeCount` 的反例态进一步定位：未激活尾素不是单一黑箱，而是无槽相位带命中与复合余因子槽两类原子。对尾素 `q=P-2b`，无槽当且仅当二次相位 gap `delta_sign(b)` 超过半窗；有槽但未激活则给出 `m=P+2(b+u)` 的复合余因子及 LPF 证书。因此若 `PrimeWindow<=InactiveTailPrime`，必有无槽相位带或复合余因子槽之一至少达到半个 `PrimeWindow`。这仍不是全局闭合；下一步必须排斥这两个命名缺陷分支。

```text
max_p=5000
finite_prime_count=668
partition_failure_count=0
phase_band_failure_count=0
multi_slot_failure_count=0
lpf_bound_failure_count=0
finite_prime_inactive_failure_count=0
row_column_unconditional_closed=false
```

## 1. 两类原子

对尾素 `q=P-2b`，固定 `b` 的槽至多一个。未激活尾素精确拆成

```text
InactiveTailPrime = NoSlotTailPrime + CompositeSlotTailPrime.
```

无槽条件是单个二次相位带条件。令 `h=(P-1)/2`，

```text
delta_plus(b)  = least positive residue of -2b^2 mod q
delta_minus(b) = least positive residue of  2b^2 mod q
NoSlot iff delta_sign(b)>h.
```

若有槽但余因子不是素数，则该尾素登记为复合槽缺陷：

```text
m=P+2(b+u),  ell=P^-(m)<=sqrt(m).
```

## 2. 反例二分

若反例态满足

```text
PrimeWindow <= InactiveTailPrime = NoSlotTailPrime + CompositeSlotTailPrime,
```

则至少一个分支满足

```text
NoSlotTailPrime >= PrimeWindow/2
或 CompositeSlotTailPrime >= PrimeWindow/2.
```

这把终端缺陷固定为两类可审计相位对象。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `inactive_partition_identity` | `closed` | InactiveTailPrime=NoSlotTailPrime+CompositeSlotTailPrime. |
| `no_slot_phase_band` | `closed` | For q=P-2b, no-slot is exactly the phase condition delta_sign(b)>floor((P-1)/2). |
| `composite_slot_lpf_certificate` | `closed` | Every composite-slot inactive tail prime has a concrete cofactor m=P+2(b+u) and LPF ell<=sqrt(m). |
| `prime_inactive_failure_dichotomy` | `closed` | If PrimeWindow<=InactiveTailPrime, then NoSlotTailPrime>=PrimeWindow/2 or CompositeSlotTailPrime>=PrimeWindow/2. |
| `defect_exclusion` | `open` | A global proof still needs to exclude the no-slot phase-band branch and the composite cofactor branch. |

## 4. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| PrimeWindow | 97145 | 97396 | 194541 |
| InactiveTailPrime | 33632 | 33335 | 66967 |
| NoSlotTailPrime | 18299 | 15895 | 34194 |
| CompositeSlotTailPrime | 15333 | 17440 | 32773 |

全扫描最紧 `PrimeWindow-InactiveTail`：`P=3`，`sign=plus`，`PrimeWindow=1`，`InactiveTail=0`，`margin=1`。
`P>=23` 最紧样本：`P=23`，`sign=plus`，`PrimeWindow=2`，`InactiveTail=0`，`margin=2`。

最常见复合槽 LPF：

| LPF | count |
| ---: | ---: |
| 3 | 14798 |
| 5 | 5699 |
| 7 | 3256 |
| 11 | 1798 |
| 13 | 1351 |
| 17 | 962 |
| 19 | 850 |
| 23 | 735 |
| 29 | 552 |
| 31 | 509 |
| 37 | 445 |
| 41 | 375 |

## 5. 样本表

| P | sign | PrimeWindow | inactive | no-slot | composite | margin | threshold | no-slot>=thr | comp>=thr |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 1 | 1 | 0 | 2 | 2 | `false` | `false` |
| 13 | `minus` | 3 | 1 | 0 | 1 | 2 | 2 | `false` | `false` |
| 17 | `plus` | 1 | 0 | 0 | 0 | 1 | 1 | `false` | `false` |
| 17 | `minus` | 3 | 0 | 0 | 0 | 3 | 2 | `false` | `false` |
| 19 | `plus` | 3 | 1 | 1 | 0 | 2 | 2 | `false` | `false` |
| 19 | `minus` | 4 | 1 | 0 | 1 | 3 | 2 | `false` | `false` |
| 23 | `plus` | 2 | 0 | 0 | 0 | 2 | 1 | `false` | `false` |
| 23 | `minus` | 3 | 1 | 0 | 1 | 2 | 2 | `false` | `false` |
| 29 | `plus` | 4 | 0 | 0 | 0 | 4 | 2 | `false` | `false` |
| 29 | `minus` | 5 | 0 | 0 | 0 | 5 | 3 | `false` | `false` |
| 31 | `plus` | 5 | 1 | 1 | 0 | 4 | 3 | `false` | `false` |
| 31 | `minus` | 4 | 1 | 0 | 1 | 3 | 2 | `false` | `false` |
| 101 | `plus` | 11 | 3 | 1 | 2 | 8 | 6 | `false` | `false` |
| 101 | `minus` | 12 | 3 | 2 | 1 | 9 | 6 | `false` | `false` |
| 499 | `plus` | 40 | 14 | 9 | 5 | 26 | 20 | `false` | `false` |
| 499 | `minus` | 44 | 15 | 6 | 9 | 29 | 22 | `false` | `false` |
| 1009 | `plus` | 72 | 22 | 17 | 5 | 50 | 36 | `false` | `false` |
| 1009 | `minus` | 70 | 22 | 9 | 13 | 48 | 35 | `false` | `false` |
| 2003 | `plus` | 125 | 44 | 28 | 16 | 81 | 63 | `false` | `false` |
| 2003 | `minus` | 139 | 46 | 18 | 28 | 93 | 70 | `false` | `false` |
| 4999 | `plus` | 300 | 101 | 58 | 43 | 199 | 150 | `false` | `false` |
| 4999 | `minus` | 289 | 104 | 46 | 58 | 185 | 145 | `false` | `false` |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `InactivePartitionClosed` | `true` | `true` | 未激活尾素被无损拆成无槽尾素与复合余因子尾素。 | closed |
| `NoSlotPhaseBandClosed` | `true` | `true` | 无槽条件已化为单个二次相位 gap 落入上半带。 | closed |
| `CompositeLPFCertificateClosed` | `true` | `true` | 复合余因子槽都有最小素因子证书。 | closed |
| `FiniteNoPrimeInactiveFailure` | `true` | `false` | 有限扫描 P<=5000 未出现 PrimeWindow<=InactiveTail。 | finite evidence only |
| `NoSlotDefectBranchExcluded` | `false` | `false` | 仍需排斥无槽相位带大到可吞掉半数 PrimeWindow 的分支。 | NoSlotTailPrimePhaseBandDefectPDECSAE |
| `CompositeSlotDefectBranchExcluded` | `false` | `false` | 仍需排斥复合余因子槽大到可吞掉半数 PrimeWindow 的分支。 | CompositeSlotCofactorDefectPDECSAE |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只定位缺陷原子，不关闭全局行/列命题。 | NoSlotTailPrimePhaseBandDefectPDECSAE AND CompositeSlotCofactorDefectPDECSAE |

## 7. 下一步

- 主攻：`NoSlotTailPrimePhaseBandDefectPDECSAE`。
- 备选：`CompositeSlotCofactorDefectPDECSAE`。
- 当前仍不能宣称全局无条件闭合；必须排斥这两个缺陷分支，或接入足够强的平方端点素数下界。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-inactive-tailprime-defect-localization-ledger.json` | `8f45fa5099c568cbe9c258536daf8858135b5f9c4f624f4b15d7781dfc750d52` |
| `experiments/prime_matrix_square_phase_inactive_tailprime_defect_localization_router.py` | `194de6d78deba8471b4d307adcf238f32fa69fafa93b16e3f58541f3557791f2` |
