# Prime Matrix square-phase 维数差攻坚路由器

**状态：** `square_phase_reduced_to_dimension_gap_ldg_rfp_open`

`SquarePhaseRoughSurvivorUniformLowerBound` 已被进一步压缩：x=P 的小素数全覆盖等价于低筛骨架 `G(P)` 被一尾素-素互补曲线完美覆盖。对 `P>=23`，多尾碰撞消失，互补因子必为素数，且只落在三条倒数地板曲线。因此若能证明 `G(P)>B(P)`，平方后前半窗立即有素数。同时，有限 CRT 平方相位不能产生矛盾，因为任意有限平方相位模式可由无限多个素数 P 实现。真正剩余不是局部同余，而是 `LDG-Lower` 与 `RFP-Upper` 的尾段常数证明，或证明任一失败会生成 PDEC/SAE/预算缺陷。

```text
square_phase_reduced_to_dimension_gap=true
finite_crt_square_phase_contradiction_excluded=true
ldg_lower_current_corpus_proved=false
rfp_upper_current_corpus_proved=false
square_phase_rough_survivor_uniform_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 压缩链

| name | status | statement |
| --- | --- | --- |
| `x_equals_p_wheel` | `closed` | x=P 全覆盖等价于每个 1<=r<P 的 P^2+r 都有某个小素因子 q<P。 |
| `low_skeleton_split` | `closed` | 先筛掉 q<=y=floor(P/e) 后，剩余低筛骨架 G(P) 只可能是素数或一尾项。 |
| `no_multi_tail_collision` | `closed_for_P_ge_23` | P>=23 时低筛骨架中不存在两个尾素因子的多尾碰撞。 |
| `prime_cofactor_identity` | `closed_for_P_ge_23` | P>=23 时一尾项唯一形如 P^2+r=ell*m, y<ell<P<m，且 m 为素数。 |
| `three_reciprocal_floor_curves` | `closed` | 每个一尾项落在三条曲线 m=floor(P^2/ell)+s, s=1,2,3 上。 |
| `dimension_gap_equivalence` | `closed_as_reduction` | 若 G(P)>B(P)，则存在低筛骨架点逃出所有尾素数，因位于 (P^2,(P+1)^2) 内而为素数。 |

## 2. 有限 CRT 障碍

| name | status | statement |
| --- | --- | --- |
| `finite_square_phase_flexibility` | `closed_barrier` | 对任意有限小素数集合 S 和任意非零平方相位选择，CRT 给出 P 的同余类实现这些 P^2 mod q。 |
| `dirichlet_prime_realization` | `closed_barrier` | 只要 CRT 类与模数互素，Dirichlet 定理给出无限多个素数 P 落在该类中。 |
| `no_finite_local_contradiction` | `closed_barrier` | 因此任何只检查有限小模平方相位的论证都不能推出全局矛盾；必须使用随 P 增长的筛余量或 PDEC 异常。 |

## 3. 剩余攻坚目标

| target | formula | route | status |
| --- | --- | --- | --- |
| `PostSquareEndpointDimensionGapGMinusBPositive` | `G(P)-B(P)>0` | 直接维数差；若成立则平方后短窗有素数。 | `open` |
| `LDG-Lower` | `G(P)>=0.48 P/log P` | 低模骨架下界；失败进入 LowSkeletonDeficit/PDEC。 | `open` |
| `RFP-Upper` | `B(P)<=1.50 P/log^2 P` | 三条倒数地板素-素曲线上界；失败进入 TailAnchor/PDEC。 | `open` |
| `finite_low_band` | `P<=2003 checked` | 低段已有有限端点素数与 G-B 正余量证书。 | `closed_finite` |
| `dimension_constants` | `1.50/0.48=3.125<log(23)` | 若 LDG/RFP 常数从 P>=23 成立，则全局闭合。 | `closed_conditional` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SquarePhaseReducedToDimensionGap` | `true` | `true` | x=P 全覆盖已压成低筛骨架被三条素-素互补曲线完美吃掉；G(P)>B(P) 即闭合。 | PostSquareEndpointDimensionGapGMinusBPositive |
| `FiniteCRTPhaseContradictionExcluded` | `true` | `true` | 有限平方相位模式可由素数 P 的 CRT 类实现，不能作为终端矛盾来源。 | not FiniteSquarePhaseCRTContradiction |
| `LowBandFiniteCertificateImported` | `true` | `false` | P<=2003 的有限端点素数和 G-B 正余量证书可用，但不替代尾段解析证明。 | tail P>=2003 |
| `LDGLowerCurrentCorpusProved` | `false` | `false` | 低筛骨架下界仍未从作者侧全局证明。 | LDG-Lower OR LowSkeletonDeficitPDECOrSAE |
| `RFPUpperCurrentCorpusProved` | `false` | `false` | 三条倒数地板素对上界仍未以 1.50 常数闭合。 | RFP-Upper OR ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE |
| `SquarePhaseRoughSurvivorUniformLowerBoundProved` | `false` | `false` | 维数差条件已清楚，但 LDG 与 RFP 两个常数输入尚未同时闭合。 | (LDG-Lower AND RFP-Upper) OR (LowSkeletonDeficitPDECOrSAE AND ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE) |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 尚未得到全局无条件终端矛盾。 | PostSquareEndpointDimensionGapGMinusBPositive OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 5. 下一步

- 主攻 `LDG-Lower`：证明 `G(P)>=0.48P/logP`，或把低模骨架亏损路由到 `LowSkeletonDeficitPDECOrSAE`。
- 并行攻 `RFP-Upper`：证明 `B(P)<=1.50P/log^2P`，或把素对过密路由到 `ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE`。
- 不再寻找有限小模 CRT 直接矛盾；该路由已被素数 CRT 灵活性排除。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md` | `387ce4c609d73b447c374db4b53986a72b2655427cbc6d64c449eaee9d19f1e5` |
| `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` | `8e9a5381b104901ab29fd2734fd159bb1a9ddff93907e750834283f970ebf92c` |
| `docs/monograph/prime-matrix-diagonal-postsquare-primepair-dimension-gap.md` | `dd371a21974ac3122a738012444d7d9785ee13bc4f5dd84045dfe4b4e710a5d6` |
| `docs/monograph/prime-matrix-diagonal-postsquare-rfp-selberg-route.md` | `e94ee4bb9b45dd441f151c88b99c23ebcf60b7c618d1c293c739a9fa20eba147` |
| `docs/monograph/prime-matrix-diagonal-postsquare-tail-cofactor-identity.md` | `f71607d32d90cdd5738d5ccdd61c483f5e7498108438f7e0bdcc2e06403acd90` |
| `docs/monograph/prime-matrix-diagonal-postsquare-tail-collision-vanishing.md` | `8509cb1141a6672fa2b9eade4125aeab8a2b4da3c7254f1113eb80595f79c450` |
| `docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json` | `37d15f13627b753f3c8c322e7836e888f06f1824212537a1fe87e77b58880aee` |
| `docs/monograph/prime-matrix-prime-square-x-equals-p-wheel-router.json` | `4544ff30590a112ac0c5329c61505989403a8c2f33942d5769cd77fa9a04e01c` |
| `experiments/prime_matrix_square_phase_dimension_gap_attack_router.py` | `8d947a9c53e83f5f1bc1acd3ebba124083ea70a8dbe3b2125f560a769b5bed56` |
