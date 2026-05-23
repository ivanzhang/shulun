# Prime Matrix Phi-LPF complete leaf phase collapse 审计

**状态：** `complete_leaf_phase_collapsed_to_prime_q_support_phase_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQCompleteRoughFactorTreeLeafPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | CompleteLeafPhaseCollapseToPrimeQSupport | true | the complete leaf phase has an immediate q-only congruence, so internal factor-tree oscillation is not a real source of saving |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | no faster deterministic phase-collapse gate than the current Phi-LPF leaf phase |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | not a same-object leaf-phase gate |

本轮继续选择行/列 Phi-LPF，因为完整因子树层之后仍有一个可无条件关闭的相位门：叶子相位对因子链本身塌缩，只剩 prime-q 支撑集合。

## 2. 叶子相位塌缩

```text
congruence=For every complete leaf edge, D=q*m-kP satisfies D == -kP (mod q).
phase_identity=For every integer h, e(-hD/q)=e(h*kP/q).
support_form=The complete factor tree only supplies a 0/1 prime-q support set in the audited row model.
no_internal_leaf_oscillation=Leaves with the same q have the same phase; in fact the audited residual graph has max q-leaf multiplicity 1.
not_enough=The remaining hard point is nontrivial control of the prime-q support set, or a completion to external Kloosterman/Vaughan Type-II estimates.
```

这一步是非循环下钻后的剪枝：继续分解 LPF 叶子不会产生新的相位振荡。真正剩余转为 actual prime-q 支撑集合的 signed/oscillatory 控制。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
actual_total_edges_R30=299977
support_q_total=299977
support_q_total_equals_edge_total=true
max_q_leaf_multiplicity=1
q_multiplicity_totals={'1': 299977}
max_phase_residue_count_per_q=1
phase_residue_q_only_for_every_leaf=true
all_predicted_displacements_in_1_to_Pminus1=true
all_factor_leaves_valid=true
depth_totals={'2': 274812, '3': 25165}
leaf_signature_top20={'7*109': 3204, '13*59': 3182, '19*41': 3178, '19*37': 3173, '7*107': 3173, '11*71': 3169, '7*103': 3165, '7*97': 3162, '23*31': 3161, '11*67': 3160, '13*53': 3159, '17*41': 3157, '17*43': 3151, '7*101': 3148, '7*113': 3145, '13*61': 3139, '23*29': 3134, '17*47': 3133, '11*73': 3115, '7*7*17': 3114}
bad_phase_residue_total=0
bad_displacement_total=0
bad_factor_leaf_total=0
```

有限审计只验证实现与账本一致性；全局相位塌缩来自恒等式 `D=qm-kP`。

代表行：

| P | k | actual_edge_count_R30 | support_q_count | max_q_leaf_multiplicity | max_phase_residue_count_per_q | depth_counter | samples |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 1 | 1 | 2:1 | q=71,m=143,D=53,Dmodq=53,expected=53,phase=e(h*kP/q),factors=11*13 |
| 257 | 256 | 3 | 3 | 1 | 1 | 2:3 | q=151,m=437,D=195,Dmodq=44,expected=44,phase=e(h*kP/q),factors=19*23 \| q=193,m=341,D=21,Dmodq=21,expected=21,phase=e(h*kP/q),factors=11*31 \| q=137,m=481,D=105,Dmodq=105,expected=105,phase=e(h*kP/q),factors=13*37 |
| 971 | 936 | 23 | 23 | 1 | 1 | 2:21, 3:2 | q=673,m=1351,D=367,Dmodq=367,expected=367,phase=e(h*kP/q),factors=7*193 \| q=677,m=1343,D=355,Dmodq=355,expected=355,phase=e(h*kP/q),factors=17*79 \| q=919,m=989,D=35,Dmodq=35,expected=35,phase=e(h*kP/q),factors=23*43 \| q=523,m=1739,D=641,Dmodq=118,expected=118,phase=e(h*kP/q),factors=37*47 \| q=683,m=1331,D=217,Dmodq=217,expected=217,phase=e(h*kP/q),factors=11*11*11 \| q=491,m=1853,D=967,Dmodq=476,expected=476,phase=e(h*kP/q),factors=17*109 |
| 1009 | 1008 | 9 | 9 | 1 | 1 | 2:8, 3:1 | q=991,m=1027,D=685,Dmodq=685,expected=685,phase=e(h*kP/q),factors=13*79 \| q=941,m=1081,D=149,Dmodq=149,expected=149,phase=e(h*kP/q),factors=23*47 \| q=743,m=1369,D=95,Dmodq=95,expected=95,phase=e(h*kP/q),factors=37*37 \| q=617,m=1649,D=361,Dmodq=361,expected=361,phase=e(h*kP/q),factors=17*97 \| q=761,m=1337,D=385,Dmodq=385,expected=385,phase=e(h*kP/q),factors=7*191 \| q=887,m=1147,D=317,Dmodq=317,expected=317,phase=e(h*kP/q),factors=31*37 |

## 4. 外部前沿匹配

| source | source_url | verified_status | useful_part | closes_this_gate | reason_not_direct |
| --- | --- | --- | --- | --- | --- |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | https://arxiv.org/abs/2511.07550 | power-saving estimates for general bilinear Kloosterman forms modulo arbitrary q | possible target after converting the q-support reciprocal phase into a genuine bilinear Kloosterman family | false | this layer shows the leaf phase is q-only; it does not yet provide the required completion identity |
| Pascadi 2025 arXiv:2511.08445 | https://arxiv.org/abs/2511.08445 | Type-II Kloosterman sums with composite moduli via non-abelian amplification | candidate only after the q-support phase is reorganised into Type-II sums | false | the present object is a prime-denominator support phase, not the input Type-II family |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | https://arxiv.org/abs/2411.12113 | Kloosterman sums over square-free and smooth integer parameters; Cambridge version online in 2025 | possible comparison after a bridge from LPF support to completed square-free/smooth parameter sums | false | q-only reciprocal phase is still not their completed parameter family |
| Ford--Maynard 2024 arXiv:2407.14368 | https://arxiv.org/abs/2407.14368 | prime-producing sieve framework with required Type-I/II hypotheses | guidance for the support-set theorem one would need | false | does not automatically verify Type-I/II estimates for this q-support set |

这些外部结果仍是后续 completion 的候选工具；本层闭合的是内部叶子相位塌缩，不是 q 支撑集合相位节省。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CompleteLeafPhaseDependsOnlyOnPrimeQ | true | true | The matched displacement phase of every complete leaf equals e(h*kP/q). | none |
| NoInternalFactorTreeOscillation | true | true | The LPF factor chain changes support membership, not the phase at fixed q. | none |
| LeafTreePhaseSavingReducedToPrimeQSupportPhase | true | true | Complete-leaf phase saving is reduced to cancellation/separation over the prime-q support set. | none |
| PrimeQSupportSetReciprocalPhaseSavingBeyondParity | false | false | Prove nontrivial signed control of the actual q-support set, not an arbitrary subset. | object-sensitive q-support theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the q-support reciprocal phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQSupportSetReciprocalPhaseSavingBeyondParity
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
complete_leaf_phase_collapsed=true
internal_factor_tree_oscillation_available=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
