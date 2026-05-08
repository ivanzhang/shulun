# 行命题最终边界闭合的通俗说明

## 1. 一句话结论

当前真正闭合的是一个精确边界命题：

```text
Triad-A1 same-set capacity / full-S terminal
在 canonical RIW/Buchstab source branch 上已经自足闭合。
```

更通俗地说：如果 A1 链条使用的是已经锁定来源的 canonical RIW/Buchstab 决策树权重，那么同一坏窗集合上的容量上界、来源账本、分支覆盖和最终评审已经全部对齐，没有剩余内部门。

## 2. 不能扩大成什么

它不能被改写成下面这个更强命题：

```text
Unrestricted generic full-S well-factorable WFD self-contained theorem
```

原因不是还差一点证明，而是 moving-delta no-go 已经给出反证模型：在当前形式假设下，generic WFD 源可以把容量集中到一个移动块上，从而破坏所需的反原子输入。因此这个宽口径 generic 自足版不是“待闭合缺口”，而是“不能声明的命题”。

## 3. 几何直觉

可以把当前边界理解成三层：

1. **canonical 源头层**：斜线、圆柱绕回、同余覆盖和容量账本都来自同一套 RIW/Buchstab 决策树来源。这里的来源账本已经闭合。
2. **generic WFD 宽口径层**：允许任意 well-factorable 源头。这个层太宽，moving-delta 模型显示它能产生当前证书无法排除的移动原子，所以不能说自足闭合。
3. **外部深定理层**：如果接受 FullS-KLS-ext 外部合同，generic 外部版可走外部定理路由，但这不是 canonical-source 自足证明的一部分。

所以最终边界不是“所有可能源头都被内部证明”，而是“精确限定源头后，内部链条完全闭合；未限定源头的强版本被反证并隔离”。

## 4. 证明链条的核心检查

最终评审文件：

```text
docs/monograph/prime-matrix-triad-a1-self-contained-theorem-boundary-review.md
```

给出的评审裁定是：

```text
APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY
```

七个门控全部通过：

- 定理陈述边界精确；
- final closure certificate 无开放门；
- same-set capacity frontier 已吸收最终边界；
- actual source provenance 已闭合到 canonical RIW/Buchstab；
- canonical/generic 分支没有静默混用；
- unrestricted generic 自足版被记录为反证，不被误称为闭合；
- 外部 FullS-KLS-ext 合同与自足声明保持分离。

终端状态为：

```text
NoFurtherTheoremBoundaryReviewGap
```

## 5. 与完整行命题的关系

这一步闭合的是行命题攻关中的一个终端边界：`Triad-A1` 的 canonical-source self-contained boundary。

它不自动等于整个 Prime Matrix 行/列命题已经无条件闭合。合著主线中仍需单独处理的全局终端证书包括：

- `PDEC family certificates`
- `LocalSurvivorCert family`
- `CleanKLS/DLS certificates or explicit ExternalKLS input`
- 以及主稿中仍标注的 D-structure/Tail-log4/Rankin/referee-block 接口。

因此当前最诚实的说法是：

```text
canonical-source 自足边界已完全闭合；
unrestricted generic 自足版已反证；
整条 Prime Matrix 行/列无条件定理仍需剩余终端证书排斥。
```

## 6. 最新前沿边界

继续接入 `NC-BLK` 边界核查、非二点 `PDEC` 准入审计和全局终端家族边界路由器后，当前前沿进一步压成：

```text
CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen
```

通俗地说：现在已经没有一个“当前已物化的局部样本”可继续消元。`PDEC` 侧当前合法非二点候选为 `0`，`LocalSurvivor` 侧开放包为 `0`，已知 sparse 入口全部有准入路线，`NC-BLK` 也不再是无名出口。

剩下的唯一大门是：

```text
GlobalTerminalFamilyExclusionCertificates
```

也就是必须证明所有未来可能出现的 `PDEC family`、`LocalSurvivorCert family`、`CleanKLS/DLS` 终端对象都能被证书排除，或明确引用外部/referee 输入。这仍不是最终行/列无条件定理闭合，但它把“最后剩余是什么”压到了当前最窄、最清晰的形式。

继续拆分后，这个唯一大门又被压成更具体的三项：

```text
PDEC_CAP:
  证明同一坏窗集合上的容量上界 U_CRT<L_PDEC；

KLS_EXT_OR_INTERNAL_LARGE_SIEVE:
  证明 L2-flat clean residual 的内部大筛吸收，
  或明确外部 KLS/DI/BFI 输入；

DStructureRankinReferee:
  D-structure/Tail-log4/finite Rankin 接口通过独立审稿。
```

其中 LocalSurvivor 当前包、已知 sparse 入口、NC-BLK 旧出口和连续终端二分都不再是独立剩余。完全自足路线的最窄目标现在是：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

最新自足瓶颈路由又把这一项压窄：

```text
experiments/prime_matrix_self_contained_terminal_bottleneck_router.py
docs/monograph/prime-matrix-self-contained-terminal-bottleneck-router.md/json

closed_nonfinal_reductions=true；
internal_clean_kls_independent_blocker_collapsed=true；
self_contained_terminal_bottleneck_is_pdec_cap=true；
narrowest_self_contained_hardpoint=PDEC_CAP_SameSetGlobalDualCertificate。
```

通俗说，`CleanKLS` 现在不再作为完全自足路线里的平行独立终端硬点：它失败时会给出对偶集中并回到 `PDEC/SAE`，在 canonical-source 分支中已经被同集容量边界吸收，而 unrestricted generic 版本已经被反证隔离。剩下的自足核心就是同一批坏窗上的全局容量不等式：

```text
U_CRT < L_PDEC
```

这仍不是完整行/列无条件定理闭合，因为还必须通过 `DStructureRankinReferee` 晋级门。

继续进入这个 `PDEC-CAP` 内部后，最新路由给出：

```text
experiments/prime_matrix_pdec_cap_same_set_global_dual_router.py
docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.md/json

closed_current_materialized_pdec_gates=true；
canonical_source_self_contained_pdec_cap_closed=true；
pdec_cap_same_set_global_dual_closed=false；
narrowest_next_hardpoint=
  DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY。
```

通俗地说，当前已经不是继续调一个固定低模层上的 Fourier 常数。已知的 PDEC 失败帽都能追到同一质量来源，早期行出口已经接线；持久帽进入升层删除势或 NoDeletion-KL；强制持久帽进入多桶实际支付缝合。继续新增的 APS 投影塔二分路由器又把“真实支付图会不会持久缝合”的逻辑二分闭合了：

```text
真实支付图 Gamma 在无穷投影塔中，
要么持久命中某个有限候选签名 -> 多桶 PDEC；
要么对所有有限候选签名都不持久 -> 分散 CleanKLS/DLS；
若升层持续删除，则递推剥离；
若删除停止但 KL/互信息偏斜，则回流 new-layer/refined PDEC。
```

继续攻入不持久 `Gamma` 分支后，新增 diffuse 终端分裂路由器：

```text
experiments/prime_matrix_pdec_cap_diffuse_terminal_split_router.py
docs/monograph/prime-matrix-pdec-cap-diffuse-terminal-split-router.md/json

diffuse_terminal_split_closed=true；
self_contained_diffuse_terminal_closed=false；
narrowest_diffuse_hardpoint=
  FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9。
```

通俗说，不持久分支不再只是“删除势 / NoDeletion / CleanKLS”这个宽口径描述。现在链条已经拆成：

```text
持续删除 -> 若删除势发散，则支撑耗尽或回流命名 sparse/PDEC；
删除停止 + KL/互信息偏斜 -> 回流 refined/new-layer PDEC；
删除停止 + KL/互信息平坦 -> CleanKLS/DLS；
CleanKLS 的 K1--K9 任一失败 -> 回流 PDEC/SAE/Multiplicity/Promotion；
K1--K9 全过 -> 外部 KLS 版可引用深定理，自足版剩 SC-9。
```

进一步桥接“发散删除势为什么足以耗尽 diffuse 责任”：

```text
experiments/prime_matrix_pdec_cap_deletion_support_exhaustion_bridge.py
docs/monograph/prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.md/json

deletion_support_exhaustion_bridge_closed=true；
narrowest_deletion_hardpoint=GlobalDeletionPotentialDivergenceLowerBound。
```

这一步关闭的是后半段逻辑：同源投影塔上 `density(A_QN)=density(A_Q0)*prod a_n`，所以
`sum -log a_n=infinity` 时活跃支撑密度趋零；若 actual-payment 仍有正责任质量，它只能被耗尽，
或集中成已命名的 sparse/PDEC/ColumnCRT/CleanKLS 回流，不能继续作为 diffuse 无名终端。

继续从删除发散下界向内拆，新增：

```text
experiments/prime_matrix_pdec_cap_deletion_divergence_lower_bound_router.py
docs/monograph/prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.md/json

deletion_divergence_lower_bound_reduced=true；
narrowest_deletion_hardpoint=OccupancySaturationPDECOrColumnCRT。
```

这一步使用 HRO 引理：

```text
S_t subset Occ_t union TI_t。
```

如果删除势不发散，就必须在某个正质量子列上 `Occ/r + TI/r -> 1`。其中 `TI/r -> 1`
就是 promoted prime 非必要，已经回流 NoDeletion-KL/CleanKLS；所以删除侧真正剩余只剩：

```text
OccupancySaturation:
  旧洞 residue 在新增素数层近满占用
  => 需要证明触发低层容量矛盾、PDEC 或 ColumnCRT。
```

继续用 HRO 的注入界向内压缩：

```text
experiments/prime_matrix_pdec_cap_occupancy_saturation_kernel_router.py
docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md/json

occupancy_saturation_reduced_to_dense_kernel=true；
narrowest_occupancy_hardpoint=DenseOldHoleKernelCapacityPDECOrColumnCRT。
```

这一步的关键是：

```text
|Occ_t| <= min(|H_Q(t)|, r)。
```

所以只要旧洞数或旧洞 residue 数低于 `(1-eta)r`，占位饱和就不可能发生，HRO 自动给出删除缺口。
若占位仍近满，则必须存在近满 promoted residue 的旧洞选择核：几乎每个新增素数 residue 都能选到一个旧洞列，
并且这些列同时避开所有低层素因子的同余禁类。于是硬点从宽口径“占位饱和”压成更具体的：

```text
DenseOldHoleKernel:
  近满旧洞选择核
  => 需要证明触发低层容量过载、PDEC 相位偏斜或 ColumnCRT 列位移刚性。
```

继续把这个选择核写成共同变量表：

```text
experiments/prime_matrix_pdec_cap_dense_kernel_common_variable_router.py
docs/monograph/prime-matrix-pdec-cap-dense-kernel-common-variable-router.md/json

dense_kernel_no_unnamed_escape_closed=true；
narrowest_dense_kernel_hardpoint=
  FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9。
```

共同变量表的核心是把每个被选择的列写成：

```text
c_b = rho_b + r k_b,
rho_b == -((t+bQ-1)P) mod r。
```

于是对每个旧素数 `q|Q`，旧洞条件等价于：

```text
k_b != r^{-1}(a_q(t)-rho_b) mod q。
```

也就是说，所有低层同余禁类都作用在同一个壳号变量 `k_b` 上。这样就只有三种出口：
大量 `b` 无合法壳号时，容量/Hall 删除；某个固定壳或有限壳包承载正密度时，形成低模持久
`PDEC/ColumnCRT`；没有固定壳持久时，只能是多壳分散，非平坦频率回 `PDEC/ColumnCRT`，
平坦频率进入自足 `SC-9`。

继续新增持久有限签名统一路由器后，这两个持久类分支又被合并：

```text
experiments/prime_matrix_pdec_cap_persistent_signature_unification_router.py
docs/monograph/prime-matrix-pdec-cap-persistent-signature-unification-router.md/json

persistent_signature_unification_closed=true；
narrowest_next_hardpoint=
  PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9。
```

通俗说，持久 `Gamma` 的多桶 MFU 与不持久分支里冒出的固定壳低模持久，本质上都是
“同一个 formal unit 上某个有限签名长期承载正密度”。前者是 phase-bucket/tail-column
签名，后者是 shell/displacement 签名。`ColumnCRT` 已吸收为 displacement PDEC，
PDEC 对偶失败已吸收为 cap refinement，口径不一致已吸收为 formal-unit normalization；
所以它们不是两个平行终端。

继续新增 SC-9 边界调和路由器后，flat clean 的 SC-9 不再是 canonical-source 完全自足路线中的独立阻塞：

```text
experiments/prime_matrix_pdec_cap_sc9_boundary_reconciliation_router.py
docs/monograph/prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.md/json

pdec_cap_sc9_boundary_reconciled=true；
narrowest_next_hardpoint=PersistentFiniteSignaturePDECColumnCRT。
```

原因是：clean 估计失败会回流 PDEC/SAE；clean 成功进入的 SC-9 已展开到 NC-BLK/外部 DI-BFI；
canonical NC-BLK 已被同集容量边界吸收；generic WFD 分支不能偷渡成自足声明。

继续新增持久终端准入路由器后，裸持久有限签名也不能直接作为终端；它必须先通过 primitive 多原子同
formal unit 的准入门：

```text
experiments/prime_matrix_pdec_cap_persistent_terminal_admission_router.py
docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md/json

persistent_terminal_admission_boundary_closed=true；
narrowest_next_hardpoint=PrimitiveMultiAtomSameFormalUnitPDECCertificate。
```

也就是说，列位移要先吸收为 displacement PDEC/SAE，对偶失败要先变成 cap refinement 或 SAE，
多重口径要先规范化；当前已物化 primitive 非二点候选为 `0`。未来只有同 formal unit、去重后三点以上、
非二点 tautology、未被 SAE/Endpoint 吸收的对象才准入最终证书。

继续新增 primitive 多原子秩边界路由器后，这个准入证书又被拆掉一层：

```text
experiments/prime_matrix_pdec_cap_primitive_multiatom_rank_router.py
docs/monograph/prime-matrix-pdec-cap-primitive-multiatom-rank-router.md/json

primitive_multiatom_rank_boundary_closed=true；
current_materialized_primitive_multiatom_instances_closed=true；
narrowest_next_hardpoint=RankTwoCapStablePrimitivePDECKernelInequality。
```

也就是说，`PrimitiveMultiAtomSameFormalUnitPDECCertificate` 现在不是黑箱终端。零秩/一秩
原子结构只能回到重复口径、二点 Fourier tautology、固定壳 `PDEC/ColumnCRT` 或 `SAE`；
若容量比较失败，则必须先输出 cap，并按 `SAE/refined PDEC/ColumnCRT/multiplicity` 回流。

因此当前真正剩余已压成更窄的单一终端估计：

```text
RankTwoCapStablePrimitivePDECKernelInequality:
  对所有二秩以上、同 formal unit、且无可回流 cap 的 primitive PDEC 核，
  证明同一坏窗集合上的 U_CRT<L_PDEC。
```

继续新增二秩 cap-stable 核路由器后，连这个核不等式本身也被写成 cap localization 的逆否命题：

```text
experiments/prime_matrix_pdec_cap_ranktwo_capstable_kernel_router.py
docs/monograph/prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md/json

ranktwo_capstable_kernel_inequality_closed=true；
narrowest_next_hardpoint=UniformCapStabilityCertificateForRankTwoPrimitiveKernels。
```

通俗说：如果某个方向的 `U_CRT` 达到 `L_PDEC`，帽定位立刻给出一个方向帽质量下界
`(L_PDEC-alpha M)/(1-alpha)`；这个帽若稀疏就进 `SAE`，若持久就进 refined `PDEC/ColumnCRT`，
若口径不一致就进 multiplicity 规范化。因此留在 cap-stable 核中的对象，必须所有合法方向帽都低于阈值。

所以最新真正剩余是：

```text
UniformCapStabilityCertificateForRankTwoPrimitiveKernels:
  对每个二秩以上 primitive 同 formal unit 核、每个合法方向和每个阈值 alpha，
  证明方向帽质量低于帽定位阈值；
  或输出 SAE / refined PDEC / ColumnCRT / multiplicity 回流证书。
```

继续新增统一帽稳定有限基路由器后，连续方向帽族不再是无限搜索：

```text
experiments/prime_matrix_pdec_cap_uniform_cap_finite_basis_router.py
docs/monograph/prime-matrix-pdec-cap-uniform-cap-finite-basis-router.md/json

uniform_cap_finite_basis_closed=true；
narrowest_next_hardpoint=FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels。
```

固定一个 finite formal unit 后，非平凡字符 `chi_h` 的像是有限循环集；改变 `zeta` 和
`alpha` 只是在这个有限循环集上移动弧端点。因此所有方向帽只需检查有限个循环弧预像。

继续新增有限弧横向路由器后，高质量有限弧也不再是黑箱：

```text
experiments/prime_matrix_pdec_cap_finite_arc_transverse_router.py
docs/monograph/prime-matrix-pdec-cap-finite-arc-transverse-router.md/json

finite_arc_no_unnamed_exit_closed=true；
narrowest_next_hardpoint=TransverseFiberExpansionForFiniteArcCaps。
```

也就是说，有限字符弧是一个秩一薄片。若弧内横向支撑低，则进入 `SAE/ColumnCRT/固定壳PDEC`；
若横向偏斜持久，则进入 refined `PDEC`；若横向平坦分散，则进入 `CleanKLS/DLS` 或外部大筛输入。

所以最新真正剩余是：

```text
TransverseFiberExpansionForFiniteArcCaps:
  对每个高质量有限字符弧，证明弧内横向纤维无法同时保持
  primitive 二秩、同 formal unit、cap-stable 和足够质量；
  若证明失败，必须输出 SAE / refined PDEC / ColumnCRT / CleanKLS 回流证书。
```

继续新增横向 clean 归约路由器后，横向扩张硬点又压成一个 clean 大筛原子：

```text
experiments/prime_matrix_pdec_cap_transverse_clean_reduction_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-clean-reduction-router.md/json

transverse_expansion_reduced_to_clean_atom=true；
narrowest_next_hardpoint=TransverseQuotientCleanLargeSieveAtom。
```

也就是说，有限弧只固定一个字符方向；二秩以上 primitive 核在弧内仍留下横向商变量。
横向低支撑、横向持久偏斜、横向列/壳集中都已经回流命名出口。若这些都没有，剩下的就是
横向商上的 `L2-flat clean residual`。

所以最新真正剩余是：

```text
TransverseQuotientCleanLargeSieveAtom:
  证明高质量有限弧的横向商在 K1--K9 clean admission 后
  满足内部 LargeSieve/DLS/KLS 界；
  或明确登记外部 KLS/DI/BFI/Kuznetsov 输入；
  若任一 clean admission 失败，则回流 PDEC / SAE / ColumnCRT / Multiplicity。
```

继续新增横向 clean 原子前沿路由器后，这个大筛原子不再作为宽泛黑箱保留：

```text
experiments/prime_matrix_pdec_cap_transverse_clean_atom_frontier_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md/json

transverse_clean_atom_routed_to_named_frontier=true；
narrowest_next_hardpoint=
  TransverseSourceSupportNonconcentrationCertificate_OR_DIBFIQuantifiedNoProjectionWindowCertificate。
```

通俗说，横向商 clean residual 已经接入既有 A1 `CleanKLS/SC-9` 语法：K1--K9 失败就回流
`PDEC/SAE/ColumnCRT/Multiplicity`，K1--K9 通过才进入 `SC-9`。`SC-9` 又已展开为实际系数
`NC-BLK` 或外部 `DI/BFI`。但这里不能直接把 canonical-source 边界拿来吸收，因为还缺一条关键桥：
横向商系数必须被证明继承 canonical `RIW/Buchstab` 源支撑下界，或必须直接证明实际 transverse
`NC-BLK` 块非集中。朴素的 factor-residue incidence 桥已经被内部 fiber 反例阻断。

所以最新真正剩余是：

```text
自足路线：
  TransverseSourceSupportNonconcentrationCertificate
  = 证明横向商系数有 canonical RIW/Buchstab 源支撑下界，
    或直接证明实际 transverse NC-BLK 块非集中；

外部原始 DI/BFI 路线：
  DIBFIQuantifiedNoProjectionWindowCertificate
  = 无投影对象恒等式 + 量化尺度代入。
```

继续新增横向源支撑路由器后，自足路线又被拆到更窄的来源嵌入问题：

```text
experiments/prime_matrix_pdec_cap_transverse_source_support_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-source-support-router.md/json

transverse_source_support_reduced=true；
narrowest_next_hardpoint=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn。
```

也就是说，已有 A1/KZ-E 来源账本已经闭合到 canonical `RIW/Buchstab` pre-Cauchy 源。横向商
formal unit 的来源嵌入也已经由有限测度函子性闭合：actual payment 是确定性推前，有限签名是投影，
方向弧是预像限制，横向商是有限因子/条件化，整个链条没有重新加权、没有替换系数源。

继续新增横向来源嵌入路由器后：

```text
experiments/prime_matrix_pdec_cap_transverse_embedding_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-embedding-router.md/json

transverse_formal_unit_embedding_closed=true；
narrowest_next_hardpoint=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn。
```

继续新增 canonical 层闭合路由器后：

```text
experiments/prime_matrix_pdec_cap_canonical_layer_closure_router.py
docs/monograph/prime-matrix-pdec-cap-canonical-layer-closure-router.md/json

canonical_layer_transfer_closed=true；
self_contained_canonical_branch_closed=true；
open_self_contained_gates=[]；
narrowest_next_hardpoint=
  DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY。
```

通俗地说，嵌入 canonical 源之后，`CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`
不是一个新估计，而是回到既有 A1 链条：selector 保留率、有限签名、决策树、来源账本和分支边界。
这条链已经由 canonical-source final boundary 闭合。剩余的 `DIBFIQuantifiedNoProjectionWindowCertificate`
只属于 generic/external 原始 DI/BFI 路线；完整行/列无条件定理仍没有因此闭合。

继续新增 PDEC-CAP 自足边界提升路由器后：

```text
experiments/prime_matrix_self_contained_pdec_cap_boundary_lift_router.py
docs/monograph/prime-matrix-self-contained-pdec-cap-boundary-lift-router.md/json

canonical_source_self_contained_pdec_bottleneck_closed=true；
narrowest_self_contained_boundary=
  NoFurtherCanonicalSourceSelfContainedPDECCapGap；
generic_external_dibfi_boundary_open=true；
open_final_gates=[
  GlobalTerminalFamiliesStillOpen,
  DStructureRankinRefereeStillOpen
]。
```

这一步的通俗结论是：如果限定在 canonical RIW/Buchstab 来源分支内，PDEC-CAP 已没有新的自足缺口；
如果要证明完整行/列无条件定理，还必须处理“所有未来终端家族都能被排斥”的全局晋级问题，以及
`DStructureRankinReferee`。如果要走 generic/external 路线，则另需提交 DI/BFI 无投影量化证书。

继续新增 canonical 终端晋级闭合路由器后：

```text
experiments/prime_matrix_canonical_terminal_promotion_closure_router.py
docs/monograph/prime-matrix-canonical-terminal-promotion-closure-router.md/json

latest_self_contained_hardpoint_closed=true；
canonical_source_terminal_promotion_closed=true；
open_self_contained_gates=[]；
narrowest_self_contained_boundary=
  NoFurtherCanonicalSourceTerminalPromotionGap；
open_final_gates=[
  DStructureRankinRefereeStillOpen
]。
```

通俗说，最后一个 canonical-source 自足硬点已经闭合：当前已物化终端前沿耗尽，三终端无第四出口，
PDEC-CAP 已由 canonical 边界提升闭合，canonical `CleanKLS/NC-BLK` 也不再是平行硬点。
剩下的不是自足证明内部的数学开门，而是完整行/列定理升级所需的独立审稿门，以及 generic/external
版本的 DI/BFI 输入。

继续新增 canonical-source 自足命题最终闭合路由器后：

```text
experiments/prime_matrix_canonical_source_self_contained_final_theorem_router.py
docs/monograph/prime-matrix-canonical-source-self-contained-final-theorem-router.md/json

canonical_source_self_contained_theorem_closed=true；
open_self_contained_gates=[]；
terminal_boundary=
  NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap。
```

这就是当前可以完整闭合的自足命题：

```text
Prime Matrix canonical-source terminal theorem boundary:
  Triad-A1 same-set/full-S terminal plus canonical terminal promotion
  on the canonical RIW/Buchstab source branch.
```

也就是说，在这个精确边界内已经没有剩余自足硬点。仍不声明的是 unrestricted generic WFD 自足版和
完整 Prime Matrix 行/列无条件定理；它们分别需要另走 generic/external DI/BFI 路线或最终独立审稿晋级。

继续新增完整全局无条件自足闭合阻断路由器后：

```text
experiments/prime_matrix_global_unconditional_self_contained_obstruction_router.py
docs/monograph/prime-matrix-global-unconditional-self-contained-obstruction-router.md/json

current_corpus_global_unconditional_self_contained_closure_possible=false；
row_column_unconditional_closed=false。
```

这给出最后判定：完整全局无条件版现在不能由当前材料直接闭合。若要继续越过这个边界，至少必须新增：

```text
ActualA1FullSSourceLockTheorem_OR_FullSNonAPStrengthenedSourceAntiAtom；
NoProjectionUncenteredDispersionIdentity；
QuantifiedDIBFIWindowSubstitution；
DStructureTailLog4FiniteRankinIndependentAcceptance。
```

所以当前最终结论不是“全局行命题已经无条件证明”，而是“canonical-source 精确自足命题已经闭合；
完整全局无条件版被上述命名门阻断”。

继续新增 actual-source bridge 全局调和路由器后：

```text
experiments/prime_matrix_actual_source_bridge_global_reconciliation_router.py
docs/monograph/prime-matrix-actual-source-bridge-global-reconciliation-router.md/json

actual_source_bridge_closed_for_canonical_branch=true；
actual_source_bridge_closes_global_unrestricted=false；
old_blocker_superseded=ActualFullSSourceBridge；
updated_global_blocking_gates=[
  UnrestrictedGenericWFD,
  NoncanonicalFullSComplementAntiAtomOrExternalDIBFI,
  FullSNonAPStrengthenedSourceAntiAtom,
  DIBFIQuantifiedNoProjectionWindowCertificate,
  DStructureTailLog4FiniteRankinPromotion
]。
```

通俗说，旧清单里的 `ActualFullSSourceBridge` 太宽了。对 canonical 来源分支而言，真实来源已经
由 provenance ledger、source-lock 拆分和最终自足边界证明闭合；所以它不能继续算作 canonical
自足命题的剩余硬点。真正还没闭合的是 canonical 分支之外的 noncanonical full-`S` 补集：
要么证明强化 source anti-atom，要么走外部/量化 DI/BFI 无投影证书。这个调和只缩窄了全局剩余，
不把完整行/列无条件命题升级为已证定理。

继续新增 noncanonical full-`S` 补集输入合同路由器后：

```text
experiments/prime_matrix_noncanonical_complement_input_contract_router.py
docs/monograph/prime-matrix-noncanonical-complement-input-contract-router.md/json

contract_boundary_closed=true；
canonical_branch_removed_from_remainder=true；
generic_wfd_template_available=false；
noncanonical_complement_closed_by_current_corpus=false；
row_column_unconditional_closed=false。
```

这一步把“最后还差什么”说得更窄：不是继续证明一个任意 generic WFD 版本，因为那个版本已经被
moving-delta 模型挡住；也不是继续检查 canonical 分支，因为它已经闭合。真正剩余只剩必要输入：

```text
实际 full-S non-AP 源 = canonical RIW/Buchstab 源；
或实际 noncanonical 源满足强化反原子；
或外部/量化 DI/BFI 无投影证书；
并且最终 DStructure/Tail-log4/Rankin 晋级门被接受。
```

所以当前“自足闭合”的最终诚实表述是：canonical-source 精确命题已闭合，noncanonical 补集的
必要输入边界也已闭合；但这些必要输入本身还没有被当前材料证明，完整无条件行/列定理仍不能声明。

继续新增 noncanonical 补集三歧边界路由器后：

```text
experiments/prime_matrix_noncanonical_complement_trilemma_router.py
docs/monograph/prime-matrix-noncanonical-complement-trilemma-router.md/json

trilemma_boundary_closed=true；
self_contained_noncanonical_package_closed=false；
external_contract_package_closed_if_fulls_kls_ext_accepted=true。
```

也就是说，扣除 canonical `RIW/Buchstab` 分支后，第二包只剩三种合法闭合模式：

```text
实际源恒等：
  actual full-S non-AP source = canonical RIW/Buchstab；

强化实际源反原子：
  最终 source capacity measure 没有 moving same-(u,v) atom；

外部/新深定理：
  接受或证明 FullS-KLS-ext / FullSNonAPWFDKLSTheoremInput。
```

这一步的重要负结论是：generic full-S 自足反原子路线不是单纯“还没证明”，而是在当前 formal
WFD / Type-Fourier / K4-K6 / naive incidence 假设下被 moving-delta capacity 模型反证。故第二包
若不接受外部 `FullS-KLS-ext`，就必须新增并证明实际源恒等或强化实际源反原子；不能再回到
generic WFD 自足模板。

继续新增行命题闭合输入图谱后：

```text
experiments/prime_matrix_closure_input_atlas_router.py
docs/monograph/prime-matrix-closure-input-atlas-router.md/json

canonical_source_self_contained_closed=true；
noncanonical_input_contract_closed=true；
row_column_unconditional_closed=false。
```

这份图谱把我们已经探索的所有主路线收束成三类输入：

```text
1. 终端证书包：
   SAE-Cert、PDEC-Cert、ColumnCRT-Cert、CleanMultishellKLS、
   以及无缺陷时 TotalDescent 到 p=2 或首阻断 seam 吸收。

2. noncanonical full-S 补集输入包：
   实际源恒等、实际源强化反原子，或外部/量化 DI/BFI 无投影路线。

3. DStructure/Rankin 晋级包：
   D-structure、Tail-log4、finite Rankin 接口通过独立晋级门。
```

通俗说，方阵斜线、圆柱覆盖、第 `P` 列锚点、`P^2±k` 层叠轮筛、远尾互补因子和
SN 递归剥离都已经不再指向新的无名方向；它们都落到“终端证书包”。canonical-source
分支已经闭合；剩下的全局化困难在 noncanonical 补集和最终晋级门。下一步若要真正完成全局闭合，
必须直接证明这三包，而不是继续寻找新的固定常数或宽 generic WFD 模板。

继续新增第三包 DStructure/Rankin 晋级验收边界路由器后：

```text
experiments/prime_matrix_dstructure_rankin_promotion_acceptance_router.py
docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.md/json

promotion_package_boundary_closed=true；
promotion_package_independently_accepted=false；
rankin_sample_pass=true。
```

通俗说，第三包已经从“模糊的最后障碍”改写成可检查验收清单：

```text
D-structure / Structured-EHPD 入口与归约被独立接受；
Tail-log4 的 BG/RKS 定理号与适配审计被接受；
有限验证归档与脚本 hash 可复现；
全部正式着色走廊 Rankin 证书通过，或失败者回流 PDEC/SAE；
作者侧 BLOCK-REFEREE 只能由独立审稿接受后升级。
```

这一步闭合的是“验收边界”，不是完成独立验收。Rankin 样本证书已经通过，Rankin 格式也已可验收；
但正式全集、外部定理号、有限验证复现和独立审稿还没有完成，所以完整行/列无条件定理仍不能声明。

继续先补第一包的内部结构后：

```text
experiments/prime_matrix_terminal_certificate_package_compression_router.py
docs/monograph/prime-matrix-terminal-certificate-package-compression-router.md/json

terminal_package_compression_closed=true；
terminal_package_fully_proved=false。
```

这一步把 `TerminalCertificatePackage` 从五个平行输入压成三个真正独立证书族：

```text
SAE：全局孤窗/短窗有限证书族；
PDEC：所有 persistent family 的 U_CRT<L_PDEC 显式或对偶证书；
ColumnCRT：固定非零列位移排斥，或回流 PDEC/SAE。
```

其中 `CleanMultishellKLS` 在 canonical-source 分支已被最终边界吸收；非 canonical 的 clean
分支属于第二包或外部 KLS。`TotalDescent` 也不再是平行终端：能下降就到 `p=2`，不能下降时的
首个 grid-fail seam 已经被材料化为 `PDEC/ColumnCRT/SAE`。所以第一包下一步的硬攻对象非常明确：
直接证明 `SAE/PDEC/ColumnCRT` 三类证书族。

继续吸收 `ColumnCRT` 后，第一包还能再压缩：

```text
experiments/prime_matrix_columncrt_to_pdec_sae_absorption_router.py
docs/monograph/prime-matrix-columncrt-to-pdec-sae-absorption-router.md/json

columncrt_independent_terminal_removed=true。
```

通俗说，固定非零列位移确实是真结构，但它不是第三种终端命运：

```text
持久列位移过载  => displacement PDEC；
孤立列位移过载  => SAE/endpoint；
列位移负载平衡  => PDEC 对偶证书中的合法约束行。
```

所以第一包独立剩余现在只剩两族：

```text
SAE 证书族；
PDEC 证书族，包含 endpoint / displacement / cofactor / primitive 等全部持久有限签名。
```

继续吸收 `SAE` 后，第一包还能进一步压窄：

```text
experiments/prime_matrix_sae_to_local_survivor_pdec_absorption_router.py
docs/monograph/prime-matrix-sae-to-local-survivor-pdec-absorption-router.md/json

sae_independent_terminal_removed=true；
terminal_package_fully_proved=false。
```

通俗说，`SAE` 不是“所有孤窗都已直接证明不存在”，而是不能继续作为独立终端命运：

```text
可抽取的孤窗      => LocalSurvivor packet，并给 witness 或 blocker-deficit；
同有限签名持久复现 => PDEC / ColumnCRT / TailAnchor / CofactorAnchor；
层级持续逃逸      => CleanKLS/DLS 或外部输入包。
```

当前已物化的 `LocalSurvivor/SAE` 包全部清零，已知入口都有 extractor 或合同回流，且当前合同体系内
没有额外无名 sparse 入口。所以第一包的当前结构剩余变成：

```text
PDEC family：包含 endpoint / displacement / cofactor / primitive / non-tautological 证书；
FutureExplicitSparsePacketExtractorSchema：若未来新增真正 sparse 路线，必须同步提交 extractor schema。
```

这仍不是完整行/列无条件闭合；它只是把 `SAE` 从独立终端列表中删除，把真正硬点推回广义 `PDEC`
证书族和未来显式 sparse schema 义务。

继续推进广义 `PDEC` 证书族后：

```text
experiments/prime_matrix_pdec_family_explicit_input_boundary_router.py
docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.md/json

pdec_family_explicit_input_boundary_closed=true；
current_materialized_pdec_frontier_closed=true；
canonical_source_pdec_cap_closed=true；
global_pdec_family_unconditional_closed=false。
```

通俗说，`PDEC family` 也不再是泛称黑箱。当前已物化的合法非二点 primitive `PDEC` 候选为 `0`；
canonical-source 分支内的 `PDEC-CAP` 已经经横向来源嵌入和 canonical 层转移接回最终自足边界。
未来若还要提出真正 `PDEC` 障碍，必须先提交完整字段：

```text
同一个 formal unit，且只有一个固定 phase map；
全部去重后至少三个物理 primitive 原子；
不是二点 Fourier tautology；
不是尚未吸收的 ColumnCRT/displacement；
商去 shell/column 退化后秩至少为 2；
对每个有限循环弧 localization 都 cap-stable；
横向支撑既非 sparse，也非持久偏斜，也未进入 clean 外部化。
```

所以第一包当前已经压成：

```text
FutureExplicitPrimitivePDECSchema；
FutureExplicitSparsePacketExtractorSchema。
```

也就是：当前已知和已物化终端前沿清零；未来若新增 `PDEC` 或 sparse 路线，必须以显式 schema
作为新输入进入，不能作为隐藏终端继续使用。

继续把 `FutureExplicitSparsePacketExtractorSchema` 本身固定成边界后：

```text
experiments/prime_matrix_future_sparse_packet_extractor_schema_boundary_router.py
docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md/json

future_sparse_packet_schema_boundary_closed=true；
current_materialized_sparse_frontier_closed=true；
global_sparse_family_unconditional_closed=false。
```

通俗说，未来的 sparse 路线不能只说“这里有一个孤窗逃逸”。它必须先给出完整有限包：

```text
有限窗口或固定偏移纤维 I；
候选集合 C(I)；
低因子、尾锚、列位移、端点、核心重叠等 blocker 家族；
blocker 到 C(I) 的命中投影规则；
witness n0 且 cover_count(n0)=0，或严格不等式 |union blockers|<|C(I)|；
phase_key、window_shape、formal_unit_id 与去重规则；
有限签名 sigma(I) 的持久性测试；
层级逃逸测试；
可复现脚本、JSON 字段、范围、哈希和 open_obligation_count=0。
```

若同一有限签名无限复现，它不再是 sparse，而要进入 `PDEC/ColumnCRT/Tail/Cofactor` 命名 schema；
若有限包不断升层逃逸，则进入 `CleanKLS/DLS` 或显式外部大筛输入。于是第一包当前两个未来输入都
已经被固定为显式 schema 边界：`PDEC` 需要 primitive 二秩以上 cap-stable 证书，sparse 需要有限
packet extractor 证书。当前前沿清零，但最终晋级仍受 noncanonical/external 输入和 `DStructure/Rankin`
独立验收限制。

最后，把四类剩余输入合成“最终输入防火墙”：

```text
experiments/prime_matrix_final_input_firewall_boundary_router.py
docs/monograph/prime-matrix-final-input-firewall-boundary-router.md/json

final_input_firewall_boundary_closed=true；
current_materialized_terminal_frontier_closed=true；
no_hidden_terminal_remaining=true；
all_final_inputs_independently_accepted=false；
row_column_unconditional_closed=false。
```

这句话的准确含义是：

```text
当前已物化 PDEC 前沿：清零；
当前已物化 sparse/LocalSurvivor 前沿：清零；
noncanonical 分支：已压成三歧输入；
DStructure/Rankin 晋级门：已压成独立验收输入；
隐藏终端：没有剩余；
完整无条件定理：仍未闭合。
```

最终开放输入只剩四类：

```text
FutureExplicitPrimitivePDECSchema；
FutureExplicitSparsePacketExtractorSchema；
NoncanonicalFullSComplementTrilemma；
DStructureRankinPromotion。
```

因此当前最强结论不是“行列无条件定理已证”，而是“当前材料里的已物化终端前沿已清零，且所有未来
剩余都必须穿过四个显式输入防火墙”。这已经完成边界闭合和无隐藏出口闭合；完全无条件闭合还需要
证明/接受上述开放输入。

继续逐项硬攻这四类输入后：

```text
experiments/prime_matrix_four_open_inputs_closure_attack_router.py
docs/monograph/prime-matrix-four-open-inputs-closure-attack-router.md/json

current_materialized_frontier_zero=true；
no_hidden_terminal_remaining=true；
conditional_closure_chain_complete=true；
all_current_obligations_closed=false；
unconditional_closure_possible_from_current_corpus=false。
```

结论进一步变细：

```text
FutureExplicitPrimitivePDECSchema：
  当前没有已物化合法非二点 primitive PDEC 候选；
  只有未来新增 PDEC family 时才触发。

FutureExplicitSparsePacketExtractorSchema：
  当前 sparse/LocalSurvivor 物化前沿清零；
  只有未来新增 sparse route 时才触发。

NoncanonicalFullSComplementTrilemma：
  canonical 实际源分支已闭合；
  unrestricted noncanonical 补集未闭合；
  现有 DI/BFI 主来源不能推出所需 full-S non-AP WFD KLS 估计。

DStructureRankinPromotion：
  晋级包边界闭合，Rankin 样本通过；
  正式全集和独立验收未完成，作者侧不能自我升级。
```

所以当前已经得到一条严格的条件闭合定理：

```text
若未来 PDEC/sparse 新路线均按显式 schema 消解或没有新增；
且 noncanonical full-S 补集三歧中至少一支被证明/接受；
且 DStructureRankinPromotion 被独立接受；
则当前无隐藏终端链可把行/列命题升级为完整闭合。
```

同时也得到当前材料不可能性定理：

```text
不新增 FullSNonAPWFDKLSTheoremInput / APSourceLift / 强化实际源反原子；
且不取得 DStructureRankinPromotion 独立接受；
则当前材料不能诚实推出完整行/列无条件定理。
```

下一最优硬攻点已经不是 PDEC 或 sparse，而是 `NoncanonicalFullSComplementTrilemma`：优先尝试
`APSourceLift` 或实际源强化反原子；若不能新增深解析定理，就只能走显式外部
`FullSNonAPWFDKLSTheoremInput`。

继续硬攻 noncanonical 后，三歧又压成两项真实输入：

```text
experiments/prime_matrix_noncanonical_final_narrowing_router.py
docs/monograph/prime-matrix-noncanonical-final-narrowing-router.md/json

noncanonical_narrowing_boundary_closed=true；
ap_source_lift_rejected=true；
generic_self_contained_antiatom_refuted=true；
exact_source_entropy_closed=false；
external_full_s_contract_closed_if_accepted=true；
self_contained_noncanonical_closed=false。
```

也就是说：

```text
canonical 分支：已闭合并移出 noncanonical；
APSourceLift：被 AP/non-AP 分支定义和对象账本阻断；
generic 自足反原子：被 moving-delta 模型反证；
source anti-atom：已精确化，但尚未证明；
FullSNonAPWFDKLSTheoremInput：已精确化，接受外部合同则对象/尺度/无投影兼容已闭合。
```

所以 noncanonical 的最窄剩余现在只剩：

```text
InternalNewTheorem:
  prove ExactWFDSourceEntropy / FullSNonAPStrengthenedSourceAntiAtom for the actual source；

ExternalDeepInput:
  accept or prove FullSNonAPWFDKLSTheoremInput。
```

这比“四开放输入”又少了一层分叉：`APSourceLift` 和 generic 反原子都不再是可用终端路线。

继续把最后输入原子化后：

```text
experiments/prime_matrix_last_remaining_atoms_router.py
docs/monograph/prime-matrix-last-remaining-atoms-router.md/json

last_remaining_atom_boundaries_closed=true；
conditional_logic_chain_complete=true；
all_last_atoms_proved_or_accepted=false；
row_column_unconditional_closed=false。
```

通俗地说，当前已经没有“没命名的最后硬点”。最后只剩三个原子：

```text
ActualFullSNonAPExactSupportAtom：
  内部自足路线需要证明实际 full-S non-AP 源的精确因子支撑和容量兼容；

ModulusDependentCompletedFullSKLSInput：
  外部/新深定理路线需要完成型、模数依赖权重的 full-S non-AP Kloosterman 大筛输入；

DStructureRankinIndependentAcceptance：
  最终晋级需要 D-structure/Tail-log4/finite Rankin 包被独立验收。
```

因此最终边界闭合可以一句话描述：

```text
若 ActualFullSNonAPExactSupportAtom 或 ModulusDependentCompletedFullSKLSInput 至少一个成立，
并且 DStructureRankinIndependentAcceptance 成立，
则当前无隐藏终端链可把行/列命题升级为完整闭合。
```

但当前材料还没有证明或独立接受这三个最后原子，所以最终状态仍是：

```text
证明逻辑链条边界闭合；
条件闭合定理成立；
完整全局无条件行/列定理尚未成立。
```

继续硬攻这三个最终原子后：

```text
experiments/prime_matrix_three_final_atoms_hard_attack_router.py
docs/monograph/prime-matrix-three-final-atoms-hard-attack-router.md/json

three_atom_attack_boundary_closed=true；
conditional_logic_chain_complete=true；
all_three_atoms_proved_or_accepted=false；
row_column_unconditional_closed=false。
```

这一步把最终形态再压窄一层。第一个原子不再写成泛泛的“精确支撑”，而是：

```text
ActualFullSNonAPSourceCapacityAntiAtomForActualSource
```

也就是证明实际 full-S non-AP 源容量测度没有移动的单个 `(u,v)` 大原子。generic 版本已经被
moving-delta 模型反证，K4/K6 和朴素 incidence 也不能推出它，所以它必须是 actual source 的
新结构定理。

第二个原子不再写成泛泛的 completed KLS，而是：

```text
CDependentResidueWeightSpectralCancellationInput
```

也就是证明依赖模数 `c` 的完成权重 `B_{c,x}=sum_k beta_{x+kc}` 在 `c,h` 谱/dispersion 平均中有
任意对数节省。点态 Weil、L2 预算、普通大筛和平坦 residue 捷径都不足。

第三个原子不再是数学隐藏终端，而是：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

也就是正式全集 Rankin 证书、Tail-log4 适配、有限验证 hash 和独立验收。作者侧不能自我晋级。

所以最终最小无条件输入基被压成：

```text
(ActualFullSNonAPSourceCapacityAntiAtomForActualSource
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这已经是当前材料能达到的最窄结构边界：证明链条条件闭合，但无条件闭合还需要上面这个数学二选一
输入和独立晋级验收输入。

最后把数学二选一继续合并审查：

```text
experiments/prime_matrix_unconditional_closure_final_attempt_router.py
docs/monograph/prime-matrix-unconditional-closure-final-attempt-router.md/json

final_attempt_boundary_closed=true；
math_lanes_collapsed_to_common_core=true；
internal_math_proof_found_in_current_corpus=false；
external_math_match_found_in_current_corpus=false；
independent_promotion_acceptance_completed=false；
row_column_unconditional_closed=false。
```

这一步说明：前面所谓“数学二选一”并不是两个互不相干的深洞。第二条
`CDependentResidueWeightSpectralCancellationInput` 经有限 Fourier 反演、`BWFD -> BSC -> KFLS`
完成链后，又回到 actual same-`(u,v)` block non-concentration 或外部 DI/BFI/Kuznetsov 定理。
第一条 actual-source 反原子本身也正是 moving-block spread/source entropy。

因此最后不可再压缩输入基是：

```text
(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients
 OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

当前材料为什么不能直接无条件闭合：

```text
generic 反原子被 moving-delta 反证；
fixed-projection diffuse 不能控制随尺度移动的 same-(u,v) 块；
仓库没有 full-S/non-AP/未中心化/无投影对象的外部定理逐项匹配；
DStructure/Rankin 晋级验收不能由作者侧自验收。
```

所以最终结论不是“已经无条件证明”，而是“所有隐藏出口已清零，终局输入基已经不可再压缩”。

再继续审查外部输入名称后，最新精化为：

```text
experiments/prime_matrix_irreducible_math_input_refinement_router.py
docs/monograph/prime-matrix-irreducible-math-input-refinement-router.md/json

refinement_boundary_closed=true；
existing_primary_dibfi_match_rejected=true；
ap_source_lift_rejected=true；
new_full_s_kls_theorem_proved_or_cited_in_current_corpus=false；
row_column_unconditional_closed=false。
```

这一步说明，“精确匹配外部 DI/BFI/Kuznetsov”这个名字仍然太宽。已有主来源核查显示：现有
BFI AP 定理、DI/Maynard J-scale 和 APSourceLift 都不能覆盖当前 full-S、non-AP、未中心化、
无投影 WFD 对象。因此外部路线必须改名为一个明确的新输入：

```text
FullSNonAPWFDKLSTheoremInput。
```

最新最终输入基是：

```text
(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients
 OR FullSNonAPWFDKLSTheoremInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

通俗地说：内部路要证明真实系数源不会集中到随尺度移动的块；外部路要新增、证明或明确引用一个
真正覆盖本文对象的 full-S Kloosterman 大筛/dispersion 定理；最后还要 DStructure/Rankin
晋级包被独立验收。缺其中任何一项，都不能把行/列命题宣布为完整无条件定理。

继续把内部 moving-block 路与外部 Full-S KLS 路放在同一张表中硬攻后，最新路由为：

```text
experiments/prime_matrix_fulls_kls_movingblock_joint_attack_router.py
docs/monograph/prime-matrix-fulls-kls-movingblock-joint-attack-router.md/json

joint_attack_boundary_closed=true；
internal_lane_proved_in_current_corpus=false；
external_lane_proved_or_cited_in_current_corpus=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

这一步的新增信息是：canonical RIW/Buchstab 分支确实已经闭合，但它已经从 noncanonical full-S 补集中
扣除了，不能再拿来证明 noncanonical 的 moving-block 反原子。内部路进一步压成：

```text
FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource。
```

也就是要证明 actual noncanonical full-S 源有足够的精确因子支撑、balanced range 阈值、
Type/Fourier 容量兼容，并且小支撑会通过 factor-residue incidence 回流到已有缺陷出口。

外部路仍是：

```text
FullSNonAPWFDKLSTheoremInput。
```

BFI、DI、Maynard 的外部论文给出重要的 AP/dispersion/Kuznetsov 技术来源，但现有审查没有找到一个
可直接逐项覆盖 `c` 依赖完成 residue 权重、未中心化、无投影、full-S、non-AP、任意对数节省的定理。
所以最新最窄输入基变成：

```text
(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource
 OR FullSNonAPWFDKLSTheoremInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

## 7. 已并入合著的文件

主稿已并入：

```text
paper/contradiction-field-monograph/contradiction-field-monograph.tex
```

合著理论总览已并入：

```text
docs/monograph/combined-monograph-directory-and-theory-system.md
```

状态总表已并入：

```text
docs/monograph/claim-status-table.md
```
