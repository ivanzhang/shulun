# Prime Matrix global CRT homogeneity 前沿同步路由器

**状态：** `global_crt_homogeneity_synced_to_exact_source_pointwise_kernel_not_global_proof`

Q1/Q2 相邻素数不对称已经给出强约束：全 Q2 轮不能同时复现覆盖块和素端点。但有限 CRT 前缀本身是同质删相位机制，不能单独制造全局相位矛盾；无穷 Euler 乘积解释临界密度，却不等于短区间 actual occupancy 证明。因此纯 CRT 全局矛盾出口被关闭，剩余必须进入 actual-source exact-UV 非集中，并在 strict 内部链条中同步到逐 primitive alpha/delta 核表；第一硬点是 alpha row anchor/phase 发射公式。

```text
q1_q2_adjacent_carrier_imported=true
full_q2_wheel_endpoint_stable_replay_impossible=true
finite_crt_period_terminal_removed=true
controlled_fresh_layer_tail_sae_imported=true
unnamed_aperture_explosion_forbidden=true
pure_finite_crt_global_phase_contradiction_found=false
global_crt_homogeneity_blocks_pure_phase_contradiction=true
q2_crt_position_rigidity_routed_to_exact_source=true
source_rank_package_synced_to_pointwise_kernel=true
alpha_row_anchor_phase_emission_formula_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger
```

## 1. Q1/Q2 不对称的真实作用

若早期零行给出跨行相邻素数 `Q1<Q2`，全 `Q2` 阶轮会把两个端点复制成被 `Q1,Q2` 自身整除的复合点。
所以端点稳定复现不可能。这是一个真实约束，但它排除的是“同端点 replay”，不是直接推出全局零行不存在。

端点若移动，就进入 fresh endpoint layer；受控且非 PDEC 的 fresh layer 被尾质量 `SAE` 吸收，
持久相关进入 `ColumnCRT/PDEC`，孔径失控必须提交 explicit moving-family schema。

## 2. 纯 CRT 全局矛盾防火墙

设 M_Y 为平方自由轮模，r 不整除 M_Y 且 r 为新素数。对任意旧余类 a，r 个提升 a+tM_Y (0<=t<r) 在模 r 下遍历全部余类，因此恰有一个提升被 r 删除。所以有限轮增长是同质的单余类删除，不是相位矛盾；除非额外方程把同一个 formal unit 强制送入已登记的 PDEC/ColumnCRT 碰撞。

这说明无穷叠加筛确实给出临界密度机制，但有限 CRT 前缀不会自动给出短区间占有证明。
若要从相位/容量走向最终矛盾，必须提供 actual load 或 actual source 的非集中估计。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `Q1Q2AdjacentCarrierImported` | `true` | `true` | 早期零行若给出跨行相邻素数 Q1<Q2，已有链条已把它登记为端点载体，而不是独立最终矛盾。 | Q2 endpoint inversion / moving endpoint routes |
| `FullQ2WheelEndpointStableReplayImpossible` | `true` | `true` | 包含 Q1,Q2 的全 Q2 阶轮会把两个端点复制成分别被自身整除的复合点，故素端点稳定复现被排除。 | closed for endpoint-stable replay |
| `FiniteCRTPeriodTerminalRemoved` | `true` | `true` | 端点替换后 fresh endpoint 层级联扩模，固定有限 CRT 周期不能作为无限反例链终端。 | fresh endpoint cascade |
| `FreshLayerNonPDECTailSAEImported` | `true` | `true` | 无 PDEC 的受控 fresh layer 每层只删一个相位，尾质量按 W_j/B_j 可求和，进入 SAE。 | aperture explosion or support motion if uncontrolled |
| `UnnamedApertureExplosionForbidden` | `true` | `true` | 若孔径增长追赶 fresh modulus，必须提交 moving-family/PDEC 显式 schema；当前无名出口不可保留。 | future explicit moving schema if new |
| `PureFiniteCRTHomogeneityBlocksGlobalPhaseContradiction` | `true` | `true` | 对任意 finite wheel M_Y 与新素数 r，旧允许类 a 的 r 个提升 a+tM_Y 中恰有一个被 r 删除；有限 CRT 前缀是同质删相位，不产生全局相位矛盾，除非出现同素数碰撞即 PDEC/ColumnCRT。 | need actual load/source dispersion |
| `EulerProductCriticalDensityIsNotIntervalOccupancyProof` | `true` | `true` | 无穷轮筛解释临界密度与 1/log x，但乘积密度本身不是长度 P 的移动区间占有下界；它缺少 actual source 在短窗和 exact fiber 上的非集中信息。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| `Q2CRTPositionRigidityRoutedToExactSource` | `true` | `true` | Q2/CRT 刚性只控制位置与相位，不控制 Cauchy/dispersion 前 actual source 在 exact (u,v) fiber 上的质量。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| `ExactSourceFiberAtomizedToSourceRankPackage` | `true` | `false` | exact-UV 非集中已经被压成 source-domain rank/no-collapse 三原子包，但该三原子包尚未证明。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `SourceRankPackageSyncedToPointwiseKernel` | `true` | `false` | 内部 strict 链条显示 source-domain entropy/source table/fixed-key multiplicity 的共同非后验对象是逐 primitive alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `AlphaRowEmissionFormulaStillOpen` | `true` | `false` | 逐点核表的第一优先硬点是 alpha row anchor/phase 发射公式；当前材料尚未给出非循环证明。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `DStructureRankinPromotionStillOpen` | `true` | `false` | 即使源侧核表完成，DStructure/Tail-log4/finite Rankin 仍需独立晋级验收。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本证书关闭的是纯 CRT 全局相位矛盾这条尝试的误出口，并把它同步到 source/kernel 前沿；没有完成行/列无条件证明。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新剩余

首攻：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

完整当前基：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件关闭的是“纯 CRT 全局相位矛盾”作为最终证明的误出口，
并把该路线同步到 source/kernel 前沿；它没有证明 alpha row 发射公式、signed 恒等式、rank/multiplicity 证书，
也没有完成 DStructure/Rankin 独立验收。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json` | `9f10be0a0445eef5185d4e9d03dab884b330a0ae06b9ff9c7a0ffb910086a804` |
| `docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.json` | `937d22f5dc0bbd7d7c0e6caf3cf7740ed4f0e0f5ca5cc28d6edcf8a42222af2c` |
| `docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.json` | `6f8c7992da2fcdc0925902c500eb5f568601db52cda061b8c21b38d87becf914` |
| `docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.json` | `b200710347f0c8931c47081c87433097ee673a2919ec4a1833d887db6b7f73d2` |
| `docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json` | `314cf3aae30e4a5565e4c9e157703622c7fb9fdb630bb09c43ca723879832b43` |
| `docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.json` | `ae3c153bcdd0718bae0ce6cf8558b6f1e1b80b52edce905945f5e0e33e95a29f` |
| `docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.json` | `bf2b854951b33fd1b8f3d3341e73a5c236e54d0640c0b91501d0871dc0dd29df` |
| `docs/monograph/prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json` | `62c6b5b1712c00216487e7c68b72d8cb97a61e58ba78f08538f697c49232142a` |
| `docs/monograph/prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json` | `64c0baf4ed2c463ec6eb69b95ebb14f16da4c5aa909fc6b7f244035d1db041cf` |
| `docs/monograph/prime-matrix-strict-global-internal-cycle-frontier-sync-router.json` | `3e253d5f93a7b1e4e2d410f6fde5d411ad54e99a69900108d48b543549a15133` |
| `docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.json` | `6a25a769df2b107f8a5a31e1374395d99717c4d0dd8188c969111477a648de7a` |
