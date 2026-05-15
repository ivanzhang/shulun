# Prime Matrix square-phase effective even-slot normal form

**状态：** `square_phase_full_tiling_reduced_to_even_half_grid_prime_pair_tiling_open`

Full effective semiprime tiling 已被压成偶数半网格素对铺砖：低筛幸存列全在 `r=2s` 上；有效半素数槽必须有 `a=2b,t=2u`，于是尾素与余因子为 `P-2b`、`P+2(b+u)`，plus 半列 `s=uP-2b(u+b)`，minus 半列 `s=2b(u+b)-uP`。因此反例必须由这族非常受限的素对曲线完全铺满低洞半网格；全局排斥或 PDEC/SAE 回流仍未完成。

```text
max_p=5000
finite_prime_count=668
total_failure_count=0
total_odd_low_survivor_count=0
even_prime_pair_tiling_excluded_proved=false
row_column_unconditional_closed=false
```

## 1. 偶数半网格正规形

`q=2` 已在低筛内，而 `P` 为奇素数，所以所有低洞列都是偶数列 `r=2s`。
有效半素数槽要求 `q=P-a` 和 `m=P+a+t` 都是奇素数；由于 `a` 为偶数，必须 `t` 为偶数。

写

```text
a=2b,   t=2u,   r=2s.
```

则有效槽统一写成素对

```text
q=P-2b,        m=P+2(b+u).
```

plus/minus 半列公式分别为

```text
plus:  s = uP - 2b(u+b)
minus: s = 2b(u+b) - uP
```

完全铺砖反例因此必须用这族 `(b,u)` 素对曲线铺满低洞半网格。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `low_survivors_live_on_even_half_grid` | `closed` | Since q=2 is in the low sieve and P is odd, every low survivor has even r, hence r=2s with 1<=s<=(P-1)/2. |
| `effective_slots_have_even_t` | `closed` | For a good effective slot, q and m are odd primes; with a=P-q even, m=P+a+t odd forces t even. |
| `even_half_grid_normal_form` | `closed` | Writing a=2b and t=2u, effective slots are prime pairs q=P-2b, m=P+2(b+u), with s=uP-2b(u+b) on plus and s=2b(u+b)-uP on minus. |
| `remaining_even_prime_pair_tiling` | `open` | A prime-void counterexample must tile the even low-survivor half-grid by this restricted prime-pair normal form. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| effective even slots | 5046 | 5343 | 10389 |
| max b | 499 | 493 | - |
| max u | 125 | 122 | - |

## 4. 样本表

| P | sign | low survivors | effective slots | odd low | failures | max b | min u | max u |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 13 | `minus` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 17 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 17 | `minus` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 19 | `plus` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 19 | `minus` | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 23 | `plus` | 3 | 1 | 0 | 0 | 2 | 1 | 1 |
| 23 | `minus` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 29 | `plus` | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 29 | `minus` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| 31 | `plus` | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| 31 | `minus` | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 101 | `plus` | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| 101 | `minus` | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| 499 | `plus` | 42 | 2 | 0 | 0 | 28 | 2 | 4 |
| 499 | `minus` | 45 | 1 | 0 | 0 | 34 | 5 | 5 |
| 1009 | `plus` | 79 | 7 | 0 | 0 | 100 | 1 | 25 |
| 1009 | `minus` | 77 | 7 | 0 | 0 | 93 | 0 | 21 |
| 2003 | `plus` | 132 | 7 | 0 | 0 | 188 | 3 | 44 |
| 2003 | `minus` | 144 | 5 | 0 | 0 | 192 | 0 | 45 |
| 4999 | `plus` | 317 | 17 | 0 | 0 | 499 | 1 | 125 |
| 4999 | `minus` | 303 | 14 | 0 | 0 | 490 | 0 | 119 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `EvenHalfGridNormalFormClosed` | `true` | `true` | 有效半素数槽已全部写成偶数半网格素对正规形。 | closed |
| `EvenPrimePairTilingExcluded` | `false` | `false` | 仍需全局排除该正规形对低洞半网格的完全铺砖。 | EvenHalfGridPrimePairTilingExclusion |
| `EvenPrimePairTilingPDEC` | `false` | `false` | 若完全铺砖存在，需抽取 `(b,u)` 素对曲线的相位缺陷。 | EvenHalfGridPrimePairTilingPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭正规形，不关闭全局行/列命题。 | EvenHalfGridPrimePairTilingExclusion OR EvenHalfGridPrimePairTilingPDECSAEReturn |

## 6. 下一步

- 主攻：`EvenHalfGridPrimePairTilingExclusion`。
- 备选回流：`EvenHalfGridPrimePairTilingPDECSAEReturn`。
- 需要排除这族 `(b,u)` 素对曲线对低洞半网格的完全铺砖；若不能直接排除，则把铺砖所需的相位贴合登记为 PDEC/SAE。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-effective-even-slot-normal-form-ledger.json` | `18b110354d489c9a212ec595599fab948cbab4e0ad07449c421338250ba5368b` |
| `experiments/prime_matrix_square_phase_effective_even_slot_normal_form_router.py` | `639a50e2277ede1cdd40d64ca5c47890e99a1c79e1bbdcc4f322c7cf54a88cb1` |
