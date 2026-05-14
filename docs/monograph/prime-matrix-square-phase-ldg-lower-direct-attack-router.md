# Prime Matrix square-phase LDG-Lower 直接下钻路由器

**状态：** `ldg_lower_reduced_to_square_phase_beta_sieve_remainder_or_pdec_open`

`LDG-Lower` 已下钻为一个明确的下筛余项问题：`G(P)` 是避开所有 `q<=P/e` 的负平方相位禁类的列数，可精确写成 `sum mu(d)N_d(P)`。Mertens 主项自然给 `e^{-gamma}P/logP`，而目标常数 `0.48` 留出安全余量。但全 inclusion-exclusion 过宽，有限 CRT 相位也不能给矛盾；真正剩余是证明 square-phase beta-sieve 余项受控，或把 `G(P)<0.48P/logP` 的持续负偏抽取为 LowSkeletonDeficit/PDEC。

```text
exact_square_phase_inclusion_exclusion_closed=true
finite_local_crt_contradiction_rejected=true
beta_sieve_remainder_bound_proved=false
ldg_lower_current_corpus_proved=false
row_column_unconditional_closed=false
```

## 1. 公式

| name | formula | status |
| --- | --- | --- |
| `low_skeleton` | `G(P)=#{1<=r<P: r != -P^2 mod q for every prime q<=y}` | `closed_definition` |
| `crt_residue_for_d` | `for squarefree d\|Q_y, a_d == -P^2 mod d is the unique forbidden CRT class` | `closed` |
| `exact_inclusion_exclusion` | `G(P)=sum_{d\|Q_y} mu(d) N_d(P), N_d(P)=#{1<=r<P: r==a_d mod d}` | `closed_identity` |
| `mertens_main` | `P*prod_{q<=y}(1-1/q) ~ e^{-gamma} P/log y` | `closed_main_term_shape` |
| `ldg_target` | `G(P)>=0.48 P/log P` | `open_lower_bound` |

## 2. 阻塞与路由

| obstruction | detail | route |
| --- | --- | --- |
| `full inclusion-exclusion too wide` | d\|Q_y 有 2^pi(y) 个项；单纯逐项误差 O(1) 无法求和。 | `use lower beta-sieve weights supported on d<=D` |
| `finite CRT phase no contradiction` | 任意有限平方相位可由素数 P 实现，不能靠有限模排除坏相位。 | `must prove growing sieve remainder bound` |
| `interval length equals P` | 窗口长度与筛到 y~P/e 同阶，余项纪律是核心而非常数微调。 | `SquarePhaseBetaSieveRemainderBound` |
| `if LDG fails` | G(P) 低于主项安全常数，等价于固定负平方相位的低模骨架持续负偏。 | `LowSkeletonDeficitPDECOrSAE` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LDGTargetImportedFromDimensionGap` | `true` | `true` | 维数差闭合需要 LDG-Lower 与 RFP-Upper；本步专攻 LDG。 | LDG-Lower |
| `ExactSquarePhaseInclusionExclusionClosed` | `true` | `true` | G(P) 已写成固定负平方相位的精确 CRT inclusion-exclusion。 | SquarePhaseBetaSieveRemainderBound |
| `FiniteLocalCRTContradictionRejected` | `true` | `true` | 有限相位模式可由素数 P 实现，不能作为 LDG 的终端矛盾。 | not FiniteSquarePhaseCRTContradiction |
| `BetaSieveRemainderBoundProved` | `false` | `false` | 尚未证明下筛权余项足够小，从而保留 0.48P/logP 的低骨架。 | SquarePhaseBetaSieveRemainderBound |
| `LDGLowerCurrentCorpusProved` | `false` | `false` | LDG 的主项形态和失败路由清楚，但尾段全局不等式未闭合。 | SquarePhaseBetaSieveRemainderBound OR LowSkeletonDeficitPDECOrSAE |
| `SquarePhaseDimensionGapClosed` | `false` | `false` | 即便 LDG 闭合，仍需并行 RFP-Upper；本步不声明最终命题。 | LDG-Lower AND RFP-Upper |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 没有得到全局无条件终端矛盾。 | (LDG-Lower AND RFP-Upper) OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 4. 下一步

- 主攻 `SquarePhaseBetaSieveRemainderBound`：构造下筛权并证明固定负平方相位的加权余项不吞掉 `0.48P/logP` 余量。
- 若余项异常偏负，则抽取 `LowSkeletonDeficitPDECOrSAE` 并接回 PDEC/SAE。
- 并行保留 `RFP-Upper`；维数差最终需要 LDG 与 RFP 同时闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` | `8e9a5381b104901ab29fd2734fd159bb1a9ddff93907e750834283f970ebf92c` |
| `docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json` | `37d15f13627b753f3c8c322e7836e888f06f1824212537a1fe87e77b58880aee` |
| `docs/monograph/prime-matrix-prime-square-x-equals-p-wheel-router.json` | `4544ff30590a112ac0c5329c61505989403a8c2f33942d5769cd77fa9a04e01c` |
| `docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.json` | `447849c4b4f88cb1b930e20183d7060acc4fc85ed3d46759930093af03d1b467` |
| `experiments/prime_matrix_square_phase_ldg_lower_direct_attack_router.py` | `988566a3d22ffe9fdba06b93fb2072373e0bedf6ca14428e2ff3cebca15f3b09` |
