# Prime Matrix inverse alignment final-tail 粗幸存阻塞路由器

**状态：** `final_tail_uniform_bound_reduced_to_first_half_prime_square_input_open`

`UniformFinalTailRoughSurvivorLowerBound` 已被压到一个明确的强输入边界：只要取 `x=P`，final-tail 残洞中任何非最大尾素数倍数的幸存者都必须是区间 `(P^2,P^2+P)` 内的素数。因此若要用 final-tail 路线直接闭合，就必须证明每个素数 `P` 的平方后前半窗含素数，或证明等价强度的 primorial cutoff 粗幸存下界。当前语料没有该作者侧无条件证明，所以本路线不能在此处宣布行/列命题闭合；下一步只能新增这个强短区间输入，或回到 PDEC/SAE/非持久预算放大路线寻找不依赖 first-half prime-square 的矛盾。

```text
final_tail_uniform_bound_implies_first_half_prime_square_input=true
first_half_prime_square_input_current_corpus_proved=false
uniform_final_tail_rough_survivor_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 阻塞链

| name | status | statement |
| --- | --- | --- |
| `x_equals_P_specialization` | `closed` | The final-tail lower bound must hold in particular for x=P, i.e. for the interval P^2< n <P^2+P. |
| `nontail_residual_is_prime` | `closed` | After the final-tail cutoff, a residual n=P^2+r not hit by the largest tail prime cannot be composite; otherwise its non-P prime factors exceed P and their product is too large. |
| `final_tail_implies_first_half_prime_square` | `closed` | Therefore a uniform final-tail rough survivor lower bound implies a prime in (P^2,P^2+P) for every prime P. |
| `finite_probe_boundary` | `diagnostic_only` | The P<=251 probe supports the pattern but cannot be promoted to a proof of the first-half prime-square input. |
| `self_contained_closure_status` | `open` | The current corpus has no self-contained proof of this first-half square short-interval input, so final-tail cannot close the row/column theorem by itself. |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FinalTailDecompositionImported` | `true` | `true` | 上一层已经证明 final-tail 残洞二分为最大尾素数倍数或真正素数。 | UniformFinalTailRoughSurvivorLowerBoundOrRegisteredPhaseDefect |
| `FinalTailUniformBoundImpliesFirstHalfPrimeSquare` | `true` | `true` | 把 final-tail 下界代入 x=P，立即要求 P^2 后长度 P 的前半窗有素数。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| `FirstHalfPrimeSquareInputCurrentCorpusProved` | `false` | `false` | 当前合著语料没有给出该短区间素数输入的作者侧证明。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| `UniformFinalTailRoughSurvivorLowerBoundProved` | `false` | `false` | final-tail 有限探针不能升级为全局 Jacobsthal/rough survivor 下界。 | PrimorialCutoffJacobsthalRoughSurvivorLowerBoundForPBlocks |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 若不新增该强短区间输入，就必须走非 final-tail 的 PDEC/SAE/预算放大矛盾路线。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 3. 下一步

- 若坚持 final-tail 直接路线，必须证明 `PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP` 或等价强度的 `PrimorialCutoffJacobsthalRoughSurvivorLowerBoundForPBlocks`。
- 若不引入该强输入，则应转攻 `NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction`，从低模缺陷、相位漂移或非持久预算侧寻找矛盾。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-final-tail-capacity-probe-ledger.json` | `9f38c983499bff7fa3bc553c67afcf50ad2b28645116471235d3d10be68a1874` |
| `docs/monograph/prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.json` | `3ee8454fe3f5f222c3f6cd07a8495ddcbf9b44c4f9339da42d836592b8747cb7` |
| `docs/monograph/prime-matrix-inverse-alignment-min-x-phase-scan-router.json` | `81175f0cc0257e65e6183e6f9ea05f717c205f0a6dce6fc89afb3672df24d387` |
| `docs/monograph/prime-matrix-zero-row-minrep-route-review.md` | `cff5609900bcfaa796b6b586c44458727b9807f2f1afd2210e52360dbe5bef26` |
| `experiments/prime_matrix_inverse_alignment_final_tail_rough_survivor_obstruction_router.py` | `43ad90bb7672bb059083e4b1348b66aab7422905fa816551bc3a7f9f0011edb8` |
