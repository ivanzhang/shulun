# Prime Matrix square-phase 低骨架二次相位缺陷路由器

**状态：** `low_skeleton_deficit_reduced_to_negative_square_phase_covering_defect_open`

`LowSkeletonDeficit` 的最窄形式已经不是普通短区间筛下界，而是负平方相位单残基覆盖过量：每个 `q<=P/e` 只允许删除 `k=-P^2 mod q`。同时，任意被覆盖的非零列满足 Legendre 锁 `chi_q(k)=chi_q(-1)`。因此若 `G(P)<0.48P/logP` 在反例链中持续发生，必须表现为负平方相位覆盖的非零 Fourier/二次字符偏置，或进入有限 SAE。该出口尚未排斥。

```text
low_skeleton_exact_negative_square_phase_closed=true
quadratic_character_lock_imported=true
negative_square_phase_defect_excluded=false
low_skeleton_deficit_excluded=false
row_column_unconditional_closed=false
```

## 1. 结构行

| name | formula | meaning |
| --- | --- | --- |
| `negative_square_residue` | `q \| P^2+k iff k == -P^2 mod q` | 每个小素数只删除一个由 P 锁定的负平方相位。 |
| `legendre_lock` | `q \| P^2+k and q not\| k => chi_q(k)=chi_q(-1)` | 被覆盖列在每个命中模上满足固定二次字符方向。 |
| `low_skeleton` | `G(P)=sum_{1<=k<P} prod_{q<=P/e} 1_{k!=-P^2 mod q}` | 低骨架是负平方相位单残基覆盖的精确补集。 |
| `deficit` | `G(P)<0.48P/logP` | 负平方相位覆盖比完整周期密度多吞掉固定比例余量。 |
| `pdec_route` | `persistent deficit => nonzero Fourier/character defect` | 若亏损持续且非有限 SAE，则必须产生可登记的相位偏置。 |

## 2. 主项余量形状

下表只登记 `e^{-gamma}P/log(floor(P/e))` 相对 `0.48P/logP` 的主项形状，不是显式 Mertens 证明。

| P | y | Mertens shape | target | surplus | relative surplus |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2003 | 736 | 170.362694 | 126.465305 | 43.897389 | 0.257670 |
| 10007 | 3681 | 684.273084 | 521.478566 | 162.794517 | 0.237909 |
| 100000 | 36787 | 5340.671881 | 4169.227026 | 1171.444855 | 0.219344 |
| 1000003 | 367880 | 43811.059954 | 34743.655238 | 9067.404715 | 0.206966 |
| 10000019 | 3678801 | 371383.074160 | 297802.461167 | 73580.612993 | 0.198126 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LowSkeletonExactNegativeSquarePhase` | `true` | `true` | LDG 低骨架已精确写成 k 避开全部 -P^2 mod q 的单残基补集。 | none |
| `QuadraticCharacterLockImported` | `true` | `true` | 若 q 覆盖 k 且 q 不整除 k，则 k 的 Legendre 方向被锁为 chi_q(-1)。 | none |
| `LDGFailureForcesQuadraticCoveringDefect` | `true` | `true` | 若 G(P)<0.48P/logP，则负平方相位覆盖必须超过 Mertens 主项安全余量。 | NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC |
| `ExplicitMertensProductLedgerClosedForThisGate` | `false` | `false` | 需要把 V(floor(P/e)) 与 0.48P/logP 的显式余量写成全阈值账本；当前只登记主项形状。 | ExplicitMertensProductLedgerForYEqualsFloorPOverE |
| `NegativeSquarePhaseDefectExcluded` | `false` | `false` | 尚未证明持续负平方相位覆盖过量不可能，也未排斥对应 PDEC/SAE。 | NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC |
| `LowSkeletonDeficitExcluded` | `false` | `false` | 低骨架亏损出口仍未关闭。 | ExplicitMertensProductLedgerForYEqualsFloorPOverE AND exclude NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 本步只把 LDG 亏损精确化为二次相位覆盖缺陷。 | exclude LowSkeletonDeficitPDECOrSAE |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 行/列命题仍未无条件闭合。 | LowSkeletonDeficit exclusion AND RFPExcess exclusion |

## 4. 下一步

- 直接攻 `NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC`：证明负平方相位覆盖过量会产生可排斥的 Fourier/Legendre 缺陷。
- 补齐 `ExplicitMertensProductLedgerForYEqualsFloorPOverE`，把完整周期主项余量做成显式常数账本。
- 该出口与 RFP 过密出口必须同时排除，才能闭合 square-phase 反例。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` | `8e9a5381b104901ab29fd2734fd159bb1a9ddff93907e750834283f970ebf92c` |
| `docs/monograph/prime-matrix-eda-diagonal-quadratic-phase-lock.md` | `8cad338c519c35c1e5f8c5a5b01c6e222fa227c10345299e3b6a8edcdaf4c936` |
| `docs/monograph/prime-matrix-square-phase-ldg-lower-direct-attack-router.json` | `fa9905a4a06b4150ba3fca3bdb757b19328df4d2c081709956f810dacdbfc7a7` |
| `docs/monograph/prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json` | `abc24466fce3fb754f690af980a96c6fe29e24fdbe36adcd8221b403aea312e2` |
| `experiments/prime_matrix_square_phase_low_skeleton_quadratic_defect_router.py` | `a7aac61c49e791ed04e3cb59cda3a2d3f181b1ac0cc10f03298e02be86b4779a` |
