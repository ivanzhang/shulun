# Prime Matrix square-phase 近全粗骨架 prime-void 二分路由器

**状态：** `nearfull_rough_exact_primevoid_defect_dichotomy_closed_defect_exclusion_open`

本步把 `PostSquareNearFullRoughSkeletonLowerBound` 的真实地位校准清楚：在 `P>=23` 的平方端点，低筛骨架精确等于端点素数集合与三曲线素对覆盖集合的无交并。因此若假设反例，即 `(P^2,P^2+P)` 无素数，则必有 `G(P)=B(P)`。常数账本 `c_G=0.48,C_B=1.50` 下，`log(23)>C_B/c_G`，所以反例不能同时满足 LDG 正常下界与 RFP 正常上界；它必须暴露为`LowSkeletonDeficit/PDEC/SAE` 或 `ReciprocalFloorPrimePairExcess/TailAnchor/PDEC/SAE`。这不是最终闭合，因为两个缺陷出口尚未排除；但它切断了把近全 rough 下界当作普通 beta-sieve 余项的误接路线。

```text
nearfull_rough_exact_decomposition_closed=true
prime_void_forces_g_equals_b=true
prime_void_defect_dichotomy_closed=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 精确分解

令 `y=floor(P/e)`，

```text
G(P)=#{1<=r<P: P^-(P^2+r)>y}
B(P)=#{y<ell<P<m: ell,m prime, P^2<ell*m<P^2+P}
A(P)=#{1<=r<P: P^2+r prime}
```

对 `P>=23`，已有一尾互补因子恒等式和多尾碰撞消失给出无交分解：

```text
G(P)=A(P)+B(P).
```

因此反例 `A(P)=0` 强制 `G(P)=B(P)`。这就是当前反例链与真实结构链的最短接口。

## 2. 常数二分

- `c_G=0.48`。
- `C_B=1.5`。
- `C_B/c_G=3.125000`。
- `log(23)=3.135494`，已经超过 `C_B/c_G`。

| P | log P | C_B/c_G | logP>C_B/c_G | 反例且LDG正常时的RFP超额因子 |
| ---: | ---: | ---: | ---: | ---: |
| 23 | 3.135494 | 3.125000 | `true` | 1.003358 |
| 101 | 4.615121 | 3.125000 | `true` | 1.476839 |
| 1009 | 6.916715 | 3.125000 | `true` | 2.213349 |
| 10007 | 9.211040 | 3.125000 | `true` | 2.947533 |
| 1000003 | 13.815514 | 3.125000 | `true` | 4.420964 |

## 3. 反例二分

若 `P>=23` 且 `A(P)=0`，则 `G(P)=B(P)`。于是：

```text
若 G(P) >= 0.48 P/logP，
则 B(P) >= 0.48 P/logP
      = (0.48 logP) P/log^2P
      > 1.50 P/log^2P.
```

所以反例必须落入下面二选一：

```text
G(P) < 0.48 P/logP        -> LowSkeletonDeficit/PDEC/SAE
B(P) > 1.50 P/log^2P      -> ReciprocalFloorPrimePairExcess/TailAnchor/PDEC/SAE
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `NearFullRoughExactDecomposition` | `true` | `true` | 由一尾互补因子恒等式与多尾碰撞消失，P>=23 时 G(P)=PrimeWindow(P)+B(P)。 | none |
| `PrimeVoidForcesGEqualsB` | `true` | `true` | 若平方后前半窗无素数，则低筛骨架全由三曲线素对覆盖，故 G(P)=B(P)。 | none |
| `LDGAndRFPImplyPrime` | `true` | `true` | 若 G(P)>=0.48P/logP 且 B(P)<=1.5P/log^2P，logP>3.125 时得到 G>B。 | LDG-Lower AND RFP-Upper |
| `PrimeVoidDefectDichotomy` | `true` | `true` | 对 P>=23 的反例，必发生 LDG 亏损或 RFP 过密；二者不能同时保持正常。 | LowSkeletonDeficitPDECOrSAE OR ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE |
| `NearFullRoughLowerIndependentClosure` | `false` | `false` | 近全阈值粗骨架下界不是比短区间素数更弱的独立易证对象；反例态下它等价于要求 B(P) 达到一维尺度。 | PostSquareNearFullRoughSkeletonLowerBound OR LowSkeletonDeficitPDECOrSAE |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 本步给出严格二分和路线校准，尚未排除两个命名缺陷出口。 | exclude LowSkeletonDeficitPDECOrSAE AND ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到全局无条件闭合。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP OR (LowSkeletonDeficitPDECOrSAE excluded AND ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE excluded) |

## 5. 下一步

- 主攻 `LowSkeletonDeficitPDECOrSAE`：证明近全低骨架亏损会产生可排斥的端点相位缺陷，或给出低骨架全局下界。
- 并行攻 `ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE`：证明三曲线素对过密会产生可排斥的尾锚/倒数相位缺陷，或给出 RFP 上界。
- 不再把 `PostSquareNearFullRoughSkeletonLowerBound` 当成普通 `P^0.43` beta-sieve 输入；它已经贴近短区间素数主问题。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-primepair-dimension-gap.md` | `dd371a21974ac3122a738012444d7d9785ee13bc4f5dd84045dfe4b4e710a5d6` |
| `docs/monograph/prime-matrix-diagonal-postsquare-tail-cofactor-identity.md` | `f71607d32d90cdd5738d5ccdd61c483f5e7498108438f7e0bdcc2e06403acd90` |
| `docs/monograph/prime-matrix-diagonal-postsquare-tail-collision-vanishing.md` | `8509cb1141a6672fa2b9eade4125aeab8a2b4da3c7254f1113eb80595f79c450` |
| `docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.json` | `447849c4b4f88cb1b930e20183d7060acc4fc85ed3d46759930093af03d1b467` |
| `docs/monograph/prime-matrix-square-phase-ldg-beta-level-barrier-router.json` | `a1ec417a7099e683d4053147b2ac6dce5f88e7b23c4e2867a61bc86190ef8779` |
| `docs/monograph/prime-matrix-square-phase-ldg-lower-direct-attack-router.json` | `fa9905a4a06b4150ba3fca3bdb757b19328df4d2c081709956f810dacdbfc7a7` |
| `docs/monograph/prime-matrix-square-phase-rfp-upper-direct-attack-router.json` | `c8ecab3fdc5e787f3b7cef1d73d34868d48878e48a7b9c8b6cc88218ebcfed81` |
| `experiments/prime_matrix_square_phase_nearfull_rough_primevoid_dichotomy_router.py` | `fcf9b34209a807470c11f3ea72e4f07ab81772fc028c619b6043dcb42f1be302` |
