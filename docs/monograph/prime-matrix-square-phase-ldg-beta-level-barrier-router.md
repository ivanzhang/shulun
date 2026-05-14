# Prime Matrix square-phase LDG beta-sieve 层级障碍路由器

**状态：** `ldg_beta_sieve_level_barrier_identified_near_full_rough_lower_bound_open`

`SquarePhaseBetaSieveRemainderBound` 不能按旧 alpha=0.43 beta-sieve 包直接关闭 LDG。LDG 的低筛阈值是 `z=P/e`；若分布层级只到 `D=P`，则 `s=logD/logz` 接近 `1`，处在线性下筛正主系数为零的区域。要让标准下筛产生正主项需 `D>z^2≈P^2/e^2`，这远超长度 `P` 的可控层级。因此真正剩余应改写为 `PostSquareNearFullRoughSkeletonLowerBound`，或证明 `G(P)<0.48P/logP` 会产生 `LowSkeletonDeficit/PDEC`。

```text
alpha043_beta_package_applicable_to_ldg=false
standard_linear_lower_sieve_positive_at_d_equals_p=false
required_level_compatible_with_length_p=false
square_phase_beta_sieve_remainder_bound_replaced=true
ldg_lower_current_corpus_proved=false
row_column_unconditional_closed=false
```

## 1. 层级读数

| P | z=P/e | s at D=P | positive lower f(s) | D needed for s>2 | D/P |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2003 | 736.863 | 1.151460 | `false` | 542966.374 | 271.077 |
| 10007 | 3681.370 | 1.121787 | `false` | 13552481.895 | 1354.300 |
| 100000 | 36787.944 | 1.095121 | `false` | 1353352832.366 | 13533.528 |
| 1000000 | 367879.441 | 1.078030 | `false` | 135335283236.613 | 135335.283 |

## 2. 障碍

| name | statement | effect |
| --- | --- | --- |
| `alpha043_package_mismatch` | 已有 beta-sieve 包使用 z=P^0.43, D=P, s=2.325...；LDG 使用 z=P/e。 | 不能把旧 0.43 粗骨架下界直接导入 LDG。 |
| `linear_sieve_zero_region` | 一维线性下筛的正主系数需要 s=logD/logz>2；s<=2 时 lower function 为 0。 | 取 D=P、z=P/e 时 s->1，标准下筛不给正下界。 |
| `required_level_too_high` | 若 z=P/e，要使 s>2 至少需要 D>z^2≈P^2/e^2。 | 这远超过长度 P 的平凡分布层级，绝对 floor 余项会吞掉主项。 |
| `cutoff_relaxation_breaks_tail_identity` | 把 z 降到 P^0.43 可恢复 beta-sieve，但多尾结构回来，三曲线素对 B(P) 不再是同一对象。 | 会离开当前 square-phase 维数差路线，必须转入非 final-tail 预算/PDEC 体系。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LDGBetaTargetImported` | `true` | `true` | 上一层把 LDG 暂压成 beta-sieve 余项；本步检查该适配是否合法。 | SquarePhaseBetaSieveRemainderBound |
| `Alpha043BetaPackageApplicableToLDG` | `false` | `false` | LDG 的筛阈值是 P/e，不是 P^0.43；旧 beta 包参数不匹配。 | PostSquareNearFullRoughSkeletonLowerBound |
| `StandardLinearLowerSievePositiveAtDEqualsP` | `false` | `false` | D=P、z=P/e 给 s≈1<2，线性下筛主系数为零。 | need D>z^2 or new structure |
| `RequiredLevelCompatibleWithLengthP` | `false` | `false` | D>z^2≈P^2/e^2 远超长度 P 的可控 floor 余项层级。 | PostSquareNearFullRoughSkeletonLowerBound |
| `SquarePhaseBetaSieveRemainderBoundReplaced` | `true` | `false` | 旧目标应替换为近全阈值粗骨架下界，或失败进入低骨架 PDEC。 | PostSquareNearFullRoughSkeletonLowerBound OR LowSkeletonDeficitPDECOrSAE |
| `LDGLowerCurrentCorpusProved` | `false` | `false` | LDG 仍未闭合；当前最窄点比 beta 余项更强，是 P/e 阈值的短区间 rough 下界。 | PostSquareNearFullRoughSkeletonLowerBound OR LowSkeletonDeficitPDECOrSAE |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 没有得到全局无条件终端矛盾。 | (LDG-Lower AND RFP-Upper) OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 4. 下一步

- 主攻 `PostSquareNearFullRoughSkeletonLowerBound`：直接证明 `z=P/e` 的平方端点低筛骨架下界。
- 若该近全阈值下界失败，必须抽取 `LowSkeletonDeficitPDECOrSAE`，不能回到有限 CRT 矛盾。
- 若改用 `P^0.43` 阈值，则必须离开三曲线维数差，回到 `NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-b3-continuous-beta-sieve-surplus-router.json` | `f890f23fc5f9a4820fbe2b1153efc03e071afcc60afaf518b1934132c8f6f66d` |
| `docs/monograph/prime-matrix-beta-sieve-lower-bound-dominance-router.json` | `ba91e91d25b9525c2f27748a46bc49dfdde2dadb5b073ee78d5044f3494d6420` |
| `docs/monograph/prime-matrix-linear-sieve-tail-remainder-gap-router.md` | `1d513d2ed43de02f00a09682f467ae94b93e43394a3cd122012ed197f2b88f75` |
| `docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.json` | `447849c4b4f88cb1b930e20183d7060acc4fc85ed3d46759930093af03d1b467` |
| `docs/monograph/prime-matrix-square-phase-ldg-lower-direct-attack-router.json` | `fa9905a4a06b4150ba3fca3bdb757b19328df4d2c081709956f810dacdbfc7a7` |
| `experiments/prime_matrix_square_phase_ldg_beta_level_barrier_router.py` | `318791f084a198d96e13a6fabe88a8519f71dc84a90e4e84fb100248bd6dcd8d` |
