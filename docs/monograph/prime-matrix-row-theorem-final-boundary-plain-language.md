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
pdec_cap_same_set_global_dual_closed=false；
narrowest_next_hardpoint=
  TransverseSourceSupportNonconcentrationCertificate_OR_DIBFIQuantifiedNoProjectionWindowCertificate。
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
