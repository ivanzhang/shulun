# Prime Matrix square-phase residual LPF reciprocal router

**状态：** `square_phase_residual_lpf_reduced_to_reciprocal_short_intervals_open`

残余 LPF 坏槽已进一步改写成倒数短区间对象：若 `m=ell*h`，plus 侧要求 `P^2<q ell h<P^2+P`，minus 侧要求 `P^2-P<q ell h<P^2`。由于 `ell*h=m>P`，每个 `(ell,h)` 对应的 q-区间长度小于 `1`，所以至多有一个整数候选。因此残余层过密不可能来自同一 `(ell,h)` 的多重复用，只能来自大量倒数短区间的唯一整数候选同时为尾素；这正是下一步的 PDEC/SAE 对象。

```text
max_p=5000
finite_prime_count=668
total_interval_failure_count=0
total_ell_h_reuse_failure_count=0
prime_beats_forced_plus_residual_intervals_proved=false
row_column_unconditional_closed=false
```

## 1. 倒数短区间公式

残余坏槽有 `m=ell*h`，其中 `ell` 是 `m` 的奇最小素因子。于是

```text
plus:  P^2 < q*ell*h < P^2+P
minus: P^2-P < q*ell*h < P^2
```

等价地，固定 `(ell,h)` 后，`q` 必须落入一个长度小于 `1` 的倒数短区间。所以同一 `(ell,h)` 在同侧至多给出一个整数候选，更不可能产生高重数覆盖。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `residual_lpf_reciprocal_interval_formula` | `closed` | A residual slot with m=ell*h is equivalent to q lying in the reciprocal interval P^2/(ell*h)<q<(P^2+P)/(ell*h) on plus, or (P^2-P)/(ell*h)<q<P^2/(ell*h) on minus. |
| `single_integer_candidate_per_ell_h` | `closed` | Since ell*h=m>P, each reciprocal interval has length P/(ell*h)<1, so it contains at most one integer q. |
| `residual_overdensity_pdec_object` | `open` | Residual LPF over-density must appear as many distinct reciprocal intervals whose unique integer candidate is a tail prime. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| residual LPF slots | 15333 | 17440 | 32773 |
| max ell | 73 | 73 | - |
| max h | 2081 | 2063 | - |

## 4. 样本表

| P | sign | residual slots | max ell | max h | interval failures | ell,h reuse failures |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 0 | 0 | 0 | 0 | 0 |
| 13 | `minus` | 1 | 3 | 5 | 0 | 0 |
| 17 | `plus` | 0 | 0 | 0 | 0 | 0 |
| 17 | `minus` | 0 | 0 | 0 | 0 | 0 |
| 19 | `plus` | 0 | 0 | 0 | 0 | 0 |
| 19 | `minus` | 1 | 3 | 7 | 0 | 0 |
| 23 | `plus` | 0 | 0 | 0 | 0 | 0 |
| 23 | `minus` | 1 | 3 | 9 | 0 | 0 |
| 29 | `plus` | 0 | 0 | 0 | 0 | 0 |
| 29 | `minus` | 0 | 0 | 0 | 0 | 0 |
| 31 | `plus` | 0 | 0 | 0 | 0 | 0 |
| 31 | `minus` | 1 | 3 | 11 | 0 | 0 |
| 101 | `plus` | 2 | 5 | 41 | 0 | 0 |
| 101 | `minus` | 1 | 3 | 35 | 0 | 0 |
| 499 | `plus` | 5 | 5 | 207 | 0 | 0 |
| 499 | `minus` | 9 | 13 | 197 | 0 | 0 |
| 1009 | `plus` | 5 | 29 | 387 | 0 | 0 |
| 1009 | `minus` | 13 | 31 | 413 | 0 | 0 |
| 2003 | `plus` | 16 | 41 | 817 | 0 | 0 |
| 2003 | `minus` | 28 | 37 | 831 | 0 | 0 |
| 4999 | `plus` | 43 | 71 | 2081 | 0 | 0 |
| 4999 | `minus` | 58 | 71 | 2057 | 0 | 0 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ResidualReciprocalFormulaClosed` | `true` | `true` | 每个残余 LPF 坏槽都等价于一个倒数短区间中的唯一整数尾素候选。 | closed |
| `EllHNonreuseClosed` | `true` | `true` | 固定同侧 `(ell,h)` 不复用 q 候选。 | closed |
| `PrimeBeatsForcedPlusResidualIntervals` | `false` | `false` | 仍需证明平方锚素数数压过强制奇偶层与这些残余倒数区间命中。 | SquarePhasePrimeBeatsForcedParityPlusResidualReciprocalIntervals |
| `ResidualReciprocalIntervalPDEC` | `false` | `false` | 若残余倒数区间命中过密，需抽取尾素在倒数短区间族中的相位缺陷。 | ResidualLPFReciprocalIntervalPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭残余 LPF 的倒数区间化，不关闭全局行/列命题。 | SquarePhasePrimeBeatsForcedParityPlusResidualReciprocalIntervals OR ResidualLPFReciprocalIntervalPDECSAEReturn |

## 6. 下一步

- 主攻：`SquarePhasePrimeBeatsForcedParityPlusResidualReciprocalIntervals`。
- 备选回流：`ResidualLPFReciprocalIntervalPDECSAEReturn`。
- 当前不能把倒数区间有限审计升级为全局素数下界；它只提供残余 LPF 过密时的精确 PDEC/SAE 载体。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-residual-lpf-reciprocal-ledger.json` | `c5e7b223a65c9b1323bab9968a6d93f998937667890fd8a8d552137ea4b73cbe` |
| `experiments/prime_matrix_square_phase_residual_lpf_reciprocal_router.py` | `9ed52ce4a6e16fadb38e76a539fa10c07ce1fb96c5767c7eb6c2e99d6170e197` |
