# Prime Matrix square-phase Jacobsthal special phase router

**状态：** `square_phase_special_jacobsthal_phase_checked_global_phase_pdec_open`

本步把 primorial Jacobsthal 风险进一步压到平方锚特殊相位：如果 `P^2±(1..P-1)` 被所有 `q<P` 全覆盖，则 `P^2` 在模 `prod_{q<P}q` 周期中必须从对应方向启动一个长度至少 `P-1` 的低筛覆盖块。有限扫描显示，从 `P=13` 起全周期确实已有长度 `>=P-1` 的长覆盖块，所以全周期短块上界路线失效；但实际 `P^2` 相位没有落入这些长块深处。因此最新硬点是特殊相位避让定理，或把相位对齐登记为 PDEC/SAE/ColumnCRT。

```text
max_k=8
max_square_anchor_prime=23
plus_full_cover_count=0
minus_full_cover_count=0
period_bound_failure_count=4
row_column_unconditional_closed=false
```

## 1. 特殊相位命题

对 `P=p_{k+1}`，令 `M_<P=prod_{q<P}q`。plus 窗口是从 `P^2+1` 开始的长度 `P-1` 区间；minus 窗口按自然数顺序是从 `P^2-(P-1)` 到 `P^2-1` 的长度 `P-1` 区间。

若其中任一窗口被 `q<P` 全覆盖，则该窗口在 `M_<P` 周期中就是一个长度至少 `P-1` 的 Jacobsthal 覆盖块。因此全覆盖反例必然是特殊相位长块命中，而不是普通中心块最大性问题。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| record count | 8 |
| plus full cover count | 0 |
| minus full cover count | 0 |
| period bound failure count | 4 |
| long block but square phase avoids count | 4 |
| max plus run from square phase | 11 |
| max minus run from square phase | 4 |

## 3. 精确扫描表

| k | P | M_<P | P-1 | period max | long blocks | plus run | plus survivor r | minus run | minus survivor r |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 2 | 2 | 1 | 0 | 1 | 2 | 0 | 2 |
| 2 | 5 | 6 | 4 | 3 | 0 | 3 | 4 | 2 | 2 |
| 3 | 7 | 30 | 6 | 5 | 0 | 3 | 4 | 0 | 6 |
| 4 | 11 | 210 | 10 | 9 | 0 | 5 | 6 | 2 | 8 |
| 5 | 13 | 2310 | 12 | 13 | 2 | 3 | 4 | 0 | 12 |
| 6 | 17 | 30030 | 16 | 21 | 10 | 3 | 4 | 4 | 12 |
| 7 | 19 | 510510 | 18 | 25 | 124 | 5 | 6 | 4 | 14 |
| 8 | 23 | 9699690 | 22 | 33 | 1372 | 11 | 12 | 2 | 20 |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `square_phase_full_cover_implies_long_block` | `closed` | If P^2±(1..P-1) is fully covered by q<P, then the corresponding P^2 phase has a covered run of length at least P-1 in the primorial period. |
| `special_phase_audit` | `finite_evidence` | The finite audit checks the actual P^2 phase directly, not only the global Jacobsthal maximum. |
| `long_blocks_exist_but_square_phase_avoids` | `finite_evidence` | In the scanned range, long covered blocks of length >=P-1 exist from P=13 onward, but the square phase does not start inside one deeply enough to cover the whole square window. |
| `global_special_phase_avoidance` | `open` | A global proof still needs to exclude P^2-phase alignment with length P-1 covered blocks, or route such alignment to PDEC/SAE/ColumnCRT. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FullCoverImpliesLongBlockClosed` | `true` | `true` | 平方锚全覆盖已转成特殊相位的长 Jacobsthal 块命中。 | closed |
| `FiniteSpecialPhaseAvoidance` | `true` | `false` | 有限扫描 P<=23 中平方相位未被完整覆盖。 | finite evidence only |
| `GlobalPeriodBoundSuffices` | `false` | `false` | 全周期 Jacobsthal 短块上界已经失败，不能作为闭合路线。 | rejected route |
| `GlobalSpecialPhaseAvoidanceProved` | `false` | `false` | 仍需证明 `P^2` 特殊相位不能对齐长块，或抽取相位缺陷证书。 | SquarePhaseSpecialPhaseLongBlockPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 Jacobsthal 风险定位到平方特殊相位，不关闭全局行/列命题。 | SquarePhaseSpecialPhaseLongBlockPDECExclusion |

## 6. 下一步

- 主攻：`SquarePhaseSpecialPhaseLongBlockPDECExclusion`。
- 需要证明 `P^2 mod M_<P` 不会进入任何长度 `P-1` 的低筛覆盖块深处。
- 若不能直接证明，应把这种命中转成固定相位长块 PDEC、端点 SAE 或 ColumnCRT 证书，并与 `TotalPressureSupportPDECExclusion` 的激活尾支撑负载合并。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_jacobsthal_special_phase_router.py` | `fc032c7bc62095740d10790639956005c8ca0e1b73155639751174beecf85497` |
| `data/square-phase-jacobsthal-special-phase-ledger.json` | `23d965e4c5e9ba70ea1f0331660dec03c63b33048f042b41a88a333dec433a03` |
