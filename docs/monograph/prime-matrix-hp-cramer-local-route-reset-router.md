# Prime Matrix H_P/Cramér-local 路线重置证书

**状态：** `hp_cramer_local_route_reset_after_parity_barrier_review`

## 1. 核心结论

本层接受评审核心结论：H_P 的最坏 strict 顶端带就是 sqrt(x) 局部短区间素数问题，Phi-LPF/LPF/Eratosthenes 恒等式只能提供组合精确 reduction，不能提供正性。此前所有无符号重排成果保留为 reduction library 和反例结构定位，不再被当成闭合。后续主攻必须转到精确外部 theorem-match、DI/BFI/Kuznetsov/自守 dispersion 新输入，或真正 special square-phase 结构下界。

```text
top_strict_band=k≈P, x=kP≈P^2, target interval length P≈sqrt(x)
hp_scale=Legendre/Cramer-local short interval scale
phi_lpf_role=exact Eratosthenes-equivalent combinatorial count/reduction
missing_input=positive lower bound beyond unsigned sieve parity barrier
```

这意味着：直接宣称 H_P 主命题无条件闭合，在当前仓库和当前数学前沿下都不允许。
能闭合的是 reduction、有限范围、条件性定理，或外部深定理精确匹配后的条件链。

## 2. 路线重置表

| route | status | role | risk | next action |
| --- | --- | --- | --- | --- |
| Route A: exact external theorem-match | `primary` | 把 H_P 需要的对象写成精确可引用定理：sqrt-scale short interval 或 full-S non-AP WFD KLS/dispersion。 | 高；多数现有定理只给平均或 AP/平滑/投影版本，未必匹配。 | 建立 theorem-match checklist：变量、权重、模数范围、窗口、投影、误差保存逐项验收。 |
| Route B: DI/BFI/Kuznetsov self-contained appendix | `primary_high_risk` | 直接证明当前 full-S non-AP WFD Kloosterman/dispersion 估计，产生带符号取消。 | 极高；相当于重证深层自守/谱大筛技术。 | 先只证明足够的模型 BE2-3K/KLS-window 命题；不再声称完整自足闭合。 |
| Route C: Maynard/GPY transference | `secondary` | 尝试把每个 H_P 窗口转为可控 admissible tuple 与分布估计问题。 | 高；仓库已有 Maynard-S compression no-go，不能直接移植 bounded gaps。 | 只保留为新变量翻译研究，不作为当前主闭合路线。 |
| Route D: automorphic L-functions / trace formula | `primary_high_risk` | 用 Kuznetsov/GL(2) 或更高阶谱技术处理 windowed Kloosterman、Type-II balanced convolution。 | 极高；需要证明精确窗口和权重下的任意对数节省。 | 把目标拆成 KLS-window theorem statement 与可引用文献匹配。 |
| Route E: Phi-LPF/Eratosthenes capacity rewriting | `demoted` | 保留为证书化 reduction、有限审计、反例结构定位。 | 不能突破奇偶屏障。 | 停止把该类步骤命名为闭合；只用于定义待证 analytic object。 |
| Route F: finite verification + theta>1/2 | `rejected` | 验证有限前缀，尾段用 BHP/Li 0.525/0.52。 | 留下无限顶端带。 | 仅保留为有限范围定理，不作为 H_P 无条件闭合路线。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| HPRecognizedAsCramerLocalScale | `true` | `true` | strict 顶端带 k≈P 等价于 x≈P^2 后长度 P≈sqrt(x) 的局部素数存在问题。 | not closed by Phi-LPF exactness |
| PhiLPFEratosthenesEquivalenceClassDemotedToReductionLibrary | `true` | `true` | LPF/Phi/Eratosthenes 型公式保留为精确 reduction，不再被标为正性闭合。 | positive input required |
| CapacityOnlyRenamingRejectedAsClosure | `true` | `true` | 继续重排无符号桶、窗口、孔容量只是在等价类内移动未证口。 | parity barrier |
| FiniteVerificationPlusKnownThetaGtHalfRejected | `true` | `true` | 有限验证配合 0.525 或 0.52 级短区间定理仍留下无限 k≈P 顶端带。 | sqrt-scale theorem needed |
| ExistingFIMaynardAutomorphicSourcesDoNotDirectlyCloseHP | `true` | `true` | FI/DI/BFI/Maynard/自守工具是可攻技术族；现有仓库没有 ready-made theorem 覆盖 H_P 主命题。 | exact theorem-match or new theorem |
| UnconditionalHPClosureClaimAllowed | `false` | `false` | 当前数学和当前仓库都不允许宣称 H_P 主命题无条件闭合。 | ExternalSqrtScaleOrNewDispersionAutomorphicInput |

## 4. 新主攻口

```text
ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof OR SpecialSquarePhaseStructuralLowerBoundBeyondParity
```

该主攻口的含义不是继续改写 Phi-LPF，而是提交能真正越过奇偶屏障的带符号分布输入。

## 5. 外部来源入口

| source | role | url |
| --- | --- | --- |
| Baker--Harman--Pintz 2001 | 通用短区间素数，指数 0.525 级；不达 sqrt 尺度。 | https://doi.org/10.1112/plms/83.3.532 |
| Runbo Li 2025 arXiv v8 | 通用短区间素数改进到 0.52 级；仍大于 1/2。 | https://arxiv.org/abs/2308.04458 |
| Friedlander--Iwaniec x^2+y^4 prime values | parity-sensitive sieve/深层分布技术代表；不是 H_P 直接闭合定理。 | https://annals.math.princeton.edu/1998/148-3/p04 |
| Maynard 2015 small gaps | 多维筛/GPY-Maynard 技术代表；证明 bounded gaps infinitely often，不给 every sqrt-window。 | https://annals.math.princeton.edu/2015/181-1/p07 |
| Deshouillers--Iwaniec / BFI dispersion class | Kloosterman/dispersion/autorphic 技术族；需精确匹配当前 full-S non-AP WFD 对象。 | https://link.springer.com/article/10.1007/BF01458321 |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json` | `32f567650dd0448dccece88e36059db053b1294a98409d32a235886286200ace` |
| `docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json` | `e822cff58c42d46384ab9fe12a91c7f4eb0c9987b7a08e1c3c65c80ff6ea748b` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json` | `9c8b4ae328fe2254bf81e16e4f058921efc6c3ea616a97f196a42482151dd028` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json` | `762c7de91c70ae99628279eb52aa2b5a94185e4d5ed2c32921f08ce6f0133881` |
| `docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json` | `37d15f13627b753f3c8c322e7836e888f06f1824212537a1fe87e77b58880aee` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json` | `980b3cce2da33b14c1590365cb582816a522fb6c458ced7cc9e35a5848b1f519` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.json` | `7ef81127aa9ab59739c9a54b905d1330a3335b5074c25d8420149bad1c2c2c59` |
| `docs/monograph/prime-matrix-strict-structured-ehpd-final-interface-audit-router.json` | `e43af88c19ad8230317071c18f31568ade7837ed2b242b4b12902c3d7071bfb3` |
| `docs/monograph/external-theorem-index.md` | `14398a2be18a7cb3e77327a0f60672636ef576527f5311e7cb9bc4d6375f6cf0` |
| `docs/generalized_framework.md` | `0edce545af5ce60a5f67b3376f292c801ebfb60564b70d52639f58a0f9cf2152` |
