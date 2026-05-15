# Prime Matrix square-phase total pressure support PDEC router

**状态：** `total_pressure_defect_registered_as_activated_tail_support_pdec_open`

本步把 `PrimeWindow<=2*NoSlotLoad` 的总压力缺陷登记为精确的激活尾支撑 PDEC。对固定 `P,side`，每个 no-slot 层原子都是互不重叠的 b 区间，`q=P-2b` 给出到尾素支撑的双射；因此 `NoSlotLoad` 正是该支撑里的素数个数。任意终端反例现在必须满足 `W_side(P)<=2*pi(Q_side(P))`，其中 `Q_side(P)` 已由同一 formal unit 显式给出。有限审计未发现这种支撑 PDEC，但全局仍需证明它不可能持久发生，或把持久失败继续送入相位/SAE/ColumnCRT 证书。

```text
max_p=5000
finite_prime_count=668
total_pressure_support_pdec_count=0
support_identity_failure_count=0
support_overlap_failure_count=0
b_q_bijection_failure_count=0
row_column_unconditional_closed=false
```

## 1. 激活尾支撑正规形

令 `q=P-2b`。固定 `b` 后存在唯一商余数

```text
2b^2 = k(P-2b)+s,  0<=s<P-2b.
```

plus 侧 no-slot 条件是 `0<=s<(P+1)/2-2b`；minus 侧条件是 `(P-1)/2<s<P-2b`。因此每个 `b` 至多进入一个 floor layer，层原子互不重叠，且 `b -> q=P-2b` 是双射。

于是对每个 `P,side` 有精确恒等式

```text
NoSlotLoad_side(P) = #{q in Q_side(P): q prime}.
```

## 2. 总压力 PDEC 正规形

记

```text
W_side(P)=#{1<=r<P: P^2 ± r is prime},
N_side(P)=#{q in Q_side(P): q prime}.
```

上一层总压力门给出终端反例当且仅当

```text
W_side(P) <= 2*N_side(P).
```

所以真正剩余已经不是抽象的 `NoSlotLoad`，而是一个带完整支撑表的 formal unit：平方锚最终幸存素数过少，同时激活尾支撑素数负载过大。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| record count | 1336 |
| combined PrimeWindow | 194541 |
| combined support prime load | 34194 |
| combined support size | 136412 |
| total pressure support PDEC count | 0 |
| support identity failures | 0 |
| support overlap failures | 0 |
| b-q bijection failures | 0 |
| min total pressure margin | 1 |
| max total pressure margin | 225 |
| max support fraction | 0.100000 |
| max required square survivor fraction to fail | 0.166667 |

## 4. 最窄边界记录

| label | P | side | W | support primes | support size | W-2N | support gap | required fraction |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| worst margin | 3 | `minus` | 1 | 0 | 0 | 1 | -1 | 0.000000 |
| best margin | 4969 | `minus` | 307 | 41 | 204 | 225 | -113 | 0.016506 |
| max support fraction | 11 | `plus` | 2 | 0 | 1 | 2 | -1 | 0.000000 |
| max required fraction | 13 | `plus` | 3 | 1 | 1 | 1 | -1 | 0.166667 |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `activated_tail_support_bijection` | `closed` | For each P and side, every no-slot atom is a disjoint b-interval and q=P-2b gives a bijection to the activated tail support. |
| `noslot_load_support_identity` | `closed` | NoSlotLoad equals the number of primes q in the activated tail support Q_side(P). |
| `total_pressure_support_pdec_normal_form` | `closed` | A total pressure defect is exactly W_side(P)<=2*pi(Q_side(P)), with Q_side(P) explicitly registered. |
| `finite_total_pressure_support_pdec_absence` | `finite_evidence` | The finite audit finds no registered total pressure support PDEC up to the tested bound. |
| `support_pdec_exclusion` | `open` | A global proof still needs to exclude W_side(P)<=2*pi(Q_side(P)) for the activated support, or route persistent failures to phase/SAE/ColumnCRT certificates. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ActivatedTailSupportBijectionClosed` | `true` | `true` | no-slot 支撑不是多重负载；每个支撑点有唯一 b 和唯一 q=P-2b。 | closed |
| `NoSlotLoadSupportIdentityClosed` | `true` | `true` | 总 no-slot 负载已经精确化为激活尾支撑上的素数计数。 | closed |
| `TotalPressureSupportPDECRegistered` | `true` | `true` | 若 `PrimeWindow<=2*NoSlotLoad` 失败发生，formal unit 已有唯一支撑证书格式。 | closed |
| `FiniteNoTotalPressureSupportPDEC` | `true` | `false` | 有限扫描 P<=5000 中未发现总压力支撑 PDEC。 | finite evidence only |
| `TotalPressureSupportPDECExcludedGlobally` | `false` | `false` | 仍需全局证明平方窗最终幸存数不能小于两倍激活尾支撑素数负载。 | TotalPressureSupportPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把总压力缺陷登记为更尖锐的支撑 PDEC，不关闭全局行/列命题。 | TotalPressureSupportPDECExclusion |

## 7. 下一步

- 主攻：`TotalPressureSupportPDECExclusion`。
- 也就是排斥 `W_side(P)<=2*pi(Q_side(P))`：平方锚最终幸存数不能被同一 formal unit 的激活尾支撑素数负载压过。
- 若不能直接排斥，应继续抽取 `Q_side(P)` 的持久相位密度、短簇、端点 SAE 或 ColumnCRT 证书。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_total_pressure_support_pdec_router.py` | `d9b99993d2fd23fae04ae5a2a81b68385ae39cd87416aca90c75c9068c1de348` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `experiments/prime_matrix_square_phase_total_noslot_pressure_gate_router.py` | `f32c6b8f3f24f0d74afc0bb2a37207d45fd302b4f6c88f5306f2e1e9a3c4c5e4` |
| `data/square-phase-total-pressure-support-pdec-ledger.json` | `88c1889ced03b4523d5c0f60db54b773eb8425608a6865cb5f8acab84947d3e1` |
