# Triad-A1 PDEC 同集容量前沿路由器

**状态：** `same_set_capacity_frontier_materialized_terminal_dual_open`

Triad-A1 的 PDEC same-set capacity 已被压到一个明确前沿：当前合法行足以闭合零块子支并输出/路由 DualCap，连续方向弧也已精确物化为 persistent cap，连续 cap 已接入 column-tail 暴露账本，且 canonical actual payment measure 已精确构造。终端二分已说明没有第三出口；positive-limsup 分支也已生成具体 PDEC 输入行。prime-lift 刚性显示这些输入可升层路由，选择性晋升也已回到有限拆分，标准晋升支付正删除势；NoDeletion-KL 已作为独立出口消除。A1 clean KLS 外部输入已登记，SC-9 也已展开路由到 NC-BLK/外部 DI-BFI。NC-BLK 的 fixed-projection 到 moving-block 缺口也已命名。MovingBlockSpread 不能由 fixed-projection diffuse 直接推出。SourceBlockEntropy 虽能推出 NC-BLK，但不由当前形式 WFD 输入自动推出。下一步不再是 A1 内部路由，而是证明 ExactWFDSourceEntropy 或给出外部 DI/BFI 原始 dispersion 引用。

## 1. 结构律

同集容量上界只允许作用在同一个 g(t) 上。当前 LHB 分支的 Attachment、零块容量行、DualCap 输出、P×P 出口和终端回流均已接线；box-only 行结构上不足，连续方向弧精确审计已排除离散采样不足这一退路；连续 cap 也已接到 column-tail 暴露账本。actual payment measure 已由 canonical 选择律构造，终端投影塔二分也已闭合。positive-limsup 有限签名的 PDEC 输入账本已物化。这些签名又进一步满足 prime-lift 同余；唯一选择性晋升已由 CRT 交换律有限拆分；标准 prime-lift 已接入正删除势；删除势停止后的 NoDeletion 口也已路由到 KL/PDEC 或 CleanKLS/DLS。A1 clean KLS 外部输入也已登记：外部深定理版接入窗口化 DI/BFI/Kuznetsov；SC-9 又已展开到 KZ-A--KZ-E，NC-BLK 又被核查为 fixed-projection diffuse 到 moving-block spread 的真实缺口。MovingBlockSpread 进一步被投影不可见模型阻断。SourceBlockEntropy 可推出 NC-BLK，但形式 WFD/Type-I-II/Fourier 输入不强制该熵；当前无黑箱版只剩 ExactWFDSourceEntropy，外部版只剩带局部方差扣除的 DI/BFI 原始 dispersion 引用。

```text
Same-set capacity upper:
  only rows on the same g(t) are legal；
  box-only rows are insufficient；
  failure must output DualCap or missing row；
  continuous cap exposes column-tail payment buckets；
  canonical actual payment measure is constructed；
  actual payment concentration returns to PDEC；
  recursive diffusion returns to CleanKLS/DLS；
  no third terminal route remains after finite-projection dichotomy；
  positive-limsup finite signatures materialize legal PDEC input rows；
  finite signatures force prime-lift congruence rows；
  selective promotion commutes after finite splitting；
  standard prime-lift pays positive deletion potential；
  NoDeletion-KL is routed to recursive PDEC or CleanKLS/DLS；
  A1 clean KLS is reduced to Kuznetsov-LS atom or external citation；
  SC-9 is reduced to NC-BLK or external DI/BFI dispersion；
  NC-BLK needs moving-block spread or external original dispersion；
  MovingBlockSpread needs source-block entropy or external DI/BFI；
  SourceBlockEntropy needs exact WFD source entropy or external DI/BFI。
```

## 2. 汇总

- `all_known_frontiers_routed=True`。
- `terminal_dual_gap=ExactWFDSourceEntropyOrExternalDIBFIOriginalDispersion`。
- `status_counts={'actual_payment_measure_constructed': 1, 'actual_payment_selection_materialized': 1, 'closed': 1, 'closed_subbranch': 1, 'continuous_dualcap_materialized_not_closed': 1, 'dualcap_materialized': 1, 'exact_wfd_source_entropy_or_external_dibfi_required': 1, 'external_kls_input_registered_self_contained_atom_open': 1, 'moving_block_spread_or_external_dibfi_required': 1, 'no_fourth_exit': 1, 'nodeletion_terminal_routed_clean_kls_open': 1, 'positive_deletion_potential_or_nodeletion_kl': 1, 'positive_limsup_pdec_inputs_materialized_capacity_open': 1, 'prime_lift_deletion_kl_ready_with_selective_commutation_gap': 1, 'ready_current_lhb_branch': 1, 'sc9_routed_to_ncblk_or_external_dibfi': 1, 'selective_promotion_resolved_by_finite_split': 1, 'source_block_entropy_or_external_dibfi_required': 1, 'structurally_insufficient': 1, 'terminal_dichotomy_admission_closed_capacity_open': 1}`。
- `lp_summary={'q': 2310, 'p_count': 9, 'all_zero_blocks_ready': True, 'box_only_global_closure': False, 'box_only_obstruction_count': 9, 'row_generators_ready': ['nonnegativity', 'phase_caps_g_le_M', 'WHOLEDEF_zero_block', 'BRIDGED_zero_block']}`。
- `fourier_summary={'q': 2310, 'p_count': 9, 'class_counts': {'EmptyCap': 8267, 'PersistentCap': 192813, 'SparseCap': 48292}, 'has_persistent_cap': True}`。
- `dualcap_summary={'aggregate_class_counts': {'ForcedPersistentByDensityBarrier': 24, 'PersistentCap': 68, 'SparseCap': 16}, 'aggregate_route_counts': {'LiftOrColumnTailOrCleanKLS': 24, 'LocalSurvivorOrExplicitPDEC': 16, 'RefinedPDECOrColumnTailRows': 68}}`。

## 3. 前沿表

| frontier | status | evidence | next action |
| --- | --- | --- | --- |
| `SameSetAttachment` | `ready_current_lhb_branch` | 当前 DualCap 三族都有同一 M_Q 质量来源。 | 新 formal PDEC 分支仍必须先证明 S subset Z_theta。 |
| `ZeroBlockCapacityRows` | `closed_subbranch` | WHOLEDEF/BRIDGED 与 supp(M) 交集为空。 | 真实 PDEC 方向若落在零块并集，该 LHB 分支直接空。 |
| `BoxOnlyCapacity` | `structurally_insufficient` | 9 个 P 都存在单相位 box-only 可行见证。 | 必须补方向、column/tail/cofactor、NoDeletion-KL 或 CleanKLS 行。 |
| `FourierCapDualFailure` | `dualcap_materialized` | class_counts={'ForcedPersistentByDensityBarrier': 24, 'PersistentCap': 68, 'SparseCap': 16}；route_counts={'LiftOrColumnTailOrCleanKLS': 24, 'LocalSurvivorOrExplicitPDEC': 16, 'RefinedPDECOrColumnTailRows': 68}。 | SparseCap 进 LocalSurvivor；Persistent/Forced 进 refined PDEC、升层或 CleanKLS。 |
| `CurrentPXPExit` | `closed` | 当前 DualCap 的 P×P 早期出口由 SparseLocalSurvivor/BTLS/LFTE 接住。 | 剩余不是 P 行出口，而是终端 PDEC/LocalSurvivor/CleanKLS 证书。 |
| `TerminalConfluence` | `no_fourth_exit` | APS、DualCap、升层删除、NoDeletion-KL、promotion 均汇入三终端。 | 直接攻三终端证书；首要为 PDEC same-set U_CRT<L_PDEC。 |
| `ContinuousDirectionArcDual` | `continuous_dualcap_materialized_not_closed` | 连续方向弧精确审计已提交；route_counts={'PersistentContinuousDualCapNeedsColumnTailOrCleanKLS': 8, 'SparseContinuousDualCapToLocalSurvivor': 1}；max U_box/M=0.998391。 | 方向采样退路关闭；下一步补 column/tail/cofactor 同集结构行或转 CleanKLS。 |
| `ContinuousColumnTailBridge` | `actual_payment_selection_materialized` | 连续 cap 已接到 column-tail 暴露账本；route_counts={'ContinuousCapActualPaymentSelectionDichotomy': 8, 'NoTailDemandSparseOrLocalSurvivor': 1}；all_cap_recomputations_match=True。 | 从暴露候选桶提升到真实支付测度：集中给 PDEC，递归扩散给 CleanKLS/DLS。 |
| `ContinuousActualPaymentSelection` | `actual_payment_measure_constructed` | canonical actual payment measure 已构造；route_counts={'ActualPaymentMeasureDichotomySubmitted': 8, 'NoTailDemandSparseOrLocalSurvivor': 1}；all_payment_counts_match_demand=True。 | 终端只剩两引理：positive-limsup finite signature=>PDEC；diffuse=>CleanKLS/DLS。 |
| `ContinuousTerminalDichotomy` | `terminal_dichotomy_admission_closed_capacity_open` | 终端二分已路由；route_counts={'NoTailDemandSparseOrLocalSurvivor': 1, 'PositiveLimsupPDECOrDiffuseCleanKLSDichotomy': 8}；open=['PDEC-CAP: prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC', 'KLS-EXT: prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures']。 | 直接攻 PDEC-CAP 容量不等式，或攻/引用 KLS-EXT 大筛估计。 |
| `ContinuousPDECSignatureInput` | `positive_limsup_pdec_inputs_materialized_capacity_open` | positive-limsup 有限签名已生成 PDEC 输入账本；signature_rows=40；route_counts={'FiniteSignaturePDECInputMaterialized': 40}；min Fourier/total=0.986379。 | 对这些 g_b(t) 证明 U_CRT<L_PDEC；失败则输出更窄 DualCap/缺失行/KLS 回流。 |
| `ContinuousPrimeLiftCongruence` | `prime_lift_deletion_kl_ready_with_selective_commutation_gap` | positive-limsup 签名均满足 prime-lift 同余；route_counts={'SelectivePrimePromotionNeedsCommutationBeforeDeletionKL': 1, 'StandardNextPrimePromotionDeletionKLReady': 39}；promoted_prime_counts={'13': 39, '17': 1}。 | 39 行接标准晋升删除/KL；1 行补选择性晋升交换律或 cofactor-order PDEC。 |
| `SelectivePromotionCommutation` | `selective_promotion_resolved_by_finite_split` | 选择性晋升行已由 CRT 交换律有限拆分；route_counts={'FiniteSplitThenStandardPromotionOrDiffuseKLS': 1}；max_successor_count=13。 | 选择性行回到标准 prime-lift 或 diffuse KLS；继续攻标准晋升删除/KL 或 KLS-EXT。 |
| `StandardPrimeLiftDeletion` | `positive_deletion_potential_or_nodeletion_kl` | 标准 prime-lift 删除势已物化；deletion_rows=52；min_D=2.564949；route_counts={'PositiveDeletionPotentialOrNoDeletionKL': 52}。 | 无限标准晋升支付删除势；若删除停止则进入 NoDeletion-KL/PDEC 或 diffuse KLS。 |
| `ContinuousNoDeletionTerminal` | `nodeletion_terminal_routed_clean_kls_open` | NoDeletion 终端已接入 KL/PDEC/CleanKLS 门控；route_counts={'PositiveDeletionPotentialOrNoDeletionPDECOrCleanKLS': 52}；terminal_gap=CleanKLSDLSLargeSieveOrExternalKLSInput。 | NoDeletion-KL 不再是独立出口；继续提交 CleanKLS/DLS 大筛证书或外部 KLS 输入。 |
| `A1CleanKLSExternalInput` | `external_kls_input_registered_self_contained_atom_open` | A1 clean KLS 外部输入已登记；all_admission_verified_or_routed=True；terminal_gap=KuznetsovLSAtomSC9OrExternalCitation。 | 外部深定理版接入 DI/BFI/Kuznetsov；完全自足版只剩证明 Kuznetsov-LS atom (SC-9)。 |
| `A1KuznetsovLSAtomFrontier` | `sc9_routed_to_ncblk_or_external_dibfi` | SC-9 已展开并路由；terminal_gap=NCBLKOrExternalDIBFIOriginalDispersion；self_contained=open_at_ncblk_actual_block_nonconcentration。 | 无黑箱版直接证明 NC-BLK；外部版引用 DI/BFI 原始 dispersion 或等价窗口 KLS。 |
| `A1NCBLKProjectionGap` | `moving_block_spread_or_external_dibfi_required` | fixed-projection diffuse 到 moving-block NC-BLK 存在缺口；terminal_gap=MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion。 | 内部版证明 MovingBlockSpreadNCBLK；外部版引用带局部方差扣除的 DI/BFI dispersion。 |
| `A1MovingBlockSpreadObstruction` | `source_block_entropy_or_external_dibfi_required` | MovingBlockSpread 不能由 fixed-projection diffuse 直接推出；terminal_gap=SourceBlockEntropyNCBLKOrExternalDIBFIOriginalDispersion。 | 内部版证明 SourceBlockEntropyNCBLK；外部版引用 DI/BFI 原始 dispersion。 |
| `A1SourceBlockEntropyRouter` | `exact_wfd_source_entropy_or_external_dibfi_required` | SourceBlockEntropy 可推出 NC-BLK，但不能由形式 WFD 输入强制；terminal_gap=ExactWFDSourceEntropyOrExternalDIBFIOriginalDispersion。 | 内部版证明 exact WFD/source 筛权反集中；外部版引用 DI/BFI 原始 dispersion。 |

## 4. 当前结论

A1 的同集容量上界已经不再是一个模糊缺口。当前状态是：

```text
Attachment ready for current LHB branch；
zero-block subbranch closed；
box-only structurally insufficient；
DualCap materialized and routed；
P×P exits closed；
no fourth exit in current A1 chain；
continuous direction-arc dual materialized but not closed；
continuous column-tail bridge materialized；
canonical actual payment measure constructed；
terminal finite-projection dichotomy closed；
positive-limsup PDEC input rows materialized；
prime-lift congruence routed；
selective promotion commutation resolved；
standard prime-lift deletion potential materialized；
NoDeletion terminal routed；
A1 clean KLS external input registered；
SC-9 routed to NC-BLK / external DI-BFI；
NC-BLK projection gap named；
MovingBlockSpread obstruction materialized；
SourceBlockEntropy router materialized；
remaining independent gap is ExactWFDSourceEntropy or external DI/BFI original dispersion。
```

所以下一步唯一值得硬攻的 A1 目标是精确源头结构行：
证明 ExactWFDSourceEntropy，或给出可复核的外部 DI/BFI 原始 dispersion 引用。
