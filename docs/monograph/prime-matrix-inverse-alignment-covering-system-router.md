# Prime Matrix 逆元对齐覆盖系统路由器

**状态：** `inverse_alignment_gcd_equivalence_closed_min_x_gt_P_reduced_to_prime_gap_input`

新的逆元对齐想法有一个严格可用的核心：`xP+r` 有小于 `P` 的素因子，等价于存在 `a` 使 `gcd(ax+r,P-a)>1`；也等价于每个 `r` 被有限并集 `x=-r P^{-1} (mod q)` 覆盖。因此最小对齐行是一个模小素数 primorial 的有限 CRT 覆盖最小值。若要证明最小对齐行必大于 `P`，在 `x<P` 区间内该问题化为：每个短区间 `(xP,(x+1)P)` 含有一个素数。这个输入很有解释力，但当前不能由 CRT 形式自动推出，所以它是新的可攻硬点，而不是已闭合证明。

```text
gcd_system_equivalence_closed=true
inverse_residue_formula_closed=true
alignment_period_primorial_closed=true
global_minimal_alignment_x_gt_P_proved=false
row_column_unconditional_closed=false
```

## 1. 等价式

对任意小素数 `q<P`，`q | xP+r` 等价于

```text
x == -r * P^{-1} (mod q).
```

令 `a=P mod q`，则 `q | P-a` 且 `q | ax+r`，所以它也等价于某个 `a` 满足 `gcd(ax+r,P-a)>1`。

## 2. 结论表

| name | statement | status |
| --- | --- | --- |
| `gcd_system_equivalence` | q<P prime divides xP+r iff for a=P mod q, q divides both ax+r and P-a. | proved |
| `inverse_residue_cover` | for fixed r and q<P, allowed x is x == -r*P^{-1} mod q. | proved |
| `periodicity` | the all-r coverage predicate is periodic modulo product_{q<P} q. | proved |
| `x_less_P_prime_interval_equivalence` | for x<P, coverage fails iff interval (xP,(x+1)P) contains a prime. | proved_reduction |
| `global_x_min_gt_P` | minimal alignment x is always greater than P. | not_proved_here_reduces_to_prime_gap_below_P2 |

## 3. 最小对齐样本

| P | period exhausted | min x in bound | min x > P | first uncovered r at x=P |
| ---: | --- | ---: | --- | ---: |
| 3 | `true` | none | `unknown` | 2 |
| 5 | `true` | none | `unknown` | 4 |
| 7 | `true` | none | `unknown` | 4 |
| 11 | `true` | none | `unknown` | 6 |
| 13 | `true` | 168 | `true` | 4 |
| 17 | `true` | 1210 | `true` | 4 |
| 19 | `false` | 3658 | `true` | 6 |
| 23 | `false` | 58 | `true` | 12 |
| 29 | `false` | 5209 | `true` | 12 |
| 31 | `false` | 60794 | `true` | 6 |
| 37 | `false` | 73916 | `true` | 4 |
| 41 | `false` | 170880 | `true` | 12 |
| 43 | `false` | 162932 | `true` | 12 |
| 47 | `false` | none | `unknown` | 4 |

## 4. x<P 边界

若 `x<P`，则 `xP+r<P^2` 且不被 `P` 整除。此时 `xP+r` 有小于 `P` 的素因子当且仅当它是合数。
所以要证明不存在 `x<=P` 的全覆盖，等价于证明每个区间 `(xP,(x+1)P)` 都至少含一个素数。

```text
checked_primes_up_to=199
checked_prime_count=45
all_checked_have_no_alignment_x_le_P=true
```

## 5. P=13, r=1 的逆元类示例

| q | P mod q | allowed x mod q |
| ---: | ---: | ---: |
| 2 | 1 | 1 |
| 3 | 1 | 2 |
| 5 | 3 | 3 |
| 7 | 6 | 1 |
| 11 | 2 | 5 |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `GCDSystemEquivalenceClosed` | `true` | `true` | 用户给出的 gcd 组可严格改写为小素因子覆盖条件；gcd(x,r)>1 是冗余但正确的充分子句。 | none for equivalence |
| `InverseResidueAlignmentFormulaClosed` | `true` | `true` | 每个 r 的允许 x 类为有限并集 `x=-r P^{-1} mod q`。 | CRT hitting-set minimization |
| `MinimalAlignmentFiniteCRTProblemClosed` | `true` | `true` | 最小对齐解可在模小素数 primorial 的周期内定义为有限覆盖最小值。 | efficient/global formula not derived |
| `SampleMinimalAlignmentsComputed` | `true` | `true` | 样本显示最小对齐解高度非单调，不能由单个固定系数公式描述。 | larger P search optional |
| `XGreaterThanPGlobalProved` | `false` | `false` | 该命题等价/强相关于每个 `(xP,(x+1)P), x<P` 含素数的短区间素数输入。 | PrimeGapBelowP2ForAllPBlocks |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本路线给出新压缩与计算证据，但尚未排除热窗口/PDEC/SAE 等终端。 | TerminalCoreHotDivisorWindowPDECorSAE AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 7. 下一步

- 主线仍回到 `TerminalCoreHotDivisorWindowPDECorSAE`。
- 这条新路线的可攻硬点是 `PrimeGapBelowP2ForAllPBlocks`，即证明 `x<P` 时每个 `(xP,(x+1)P)` 有素数。
- 边界：本步不声明全局 `min x>P` 已证明，也不声明行/列命题无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-covering-system-sample-ledger.json` | `e1a0d939b424b57cf8c1f97c8d0a0e973c3f91896789011e786fa833ade10f9a` |
| `experiments/prime_matrix_inverse_alignment_covering_system_router.py` | `5d989c22bd9e58f06547f0b3afd76d1fdfb04fd231c8fa701b25828db1e99caf` |
