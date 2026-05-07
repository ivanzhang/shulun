# Triad-A1 CleanKLS 外部输入路由器

**状态：** `a1_clean_kls_external_input_registered_self_contained_atom_open`

A1 的 CleanKLS/DLS 口已经从泛泛的大筛缺口压成外部输入登记表：K1--K9 的失败项都回流到 PDEC/SAE/Multiplicity/Promotion，全部通过时才调用 Kloosterman/dispersion 大筛。外部深定理版可在接受窗口化 DI/BFI/Kuznetsov 输入时闭合；完全自足版仍卡在单一 Kuznetsov-LS atom (SC-9)。

## 1. 结构律

A1 clean branch is invoked only after all finite signatures, column/tail caps, promotable prime residues, and phase-residue mutual-information peaks have been routed away. Under those K1--K9 admission conditions the residual is a dyadic L2-flat Kloosterman/dispersion formal unit. If a windowed DI/BFI/Kuznetsov large-sieve input is accepted, the clean branch is absorbed. Without external input, the remaining self-contained task is exactly the Kuznetsov-LS atom (SC-9).

```text
A1 clean residual
  => K1--K9 admission;
admission failure
  => PDEC / SAE / Multiplicity / Promotion return;
all K1--K9 pass
  => L2-flat Kloosterman/dispersion block;
external DI/BFI/Kuznetsov accepted
  => A1 clean branch absorbed;
self-contained version
  => prove Kuznetsov-LS atom (SC-9).
```

## 2. 汇总

- `all_admission_verified_or_routed=true`。
- `external_kls_input_registered=true`。
- `external_deep_theorem_version_status=closed_for_a1_clean_branch_if_windowed_kloosterman_spectral_dispersion_input_is_accepted`。
- `self_contained_version_status=open_at_kuznetsov_ls_atom_sc9`。
- `terminal_gap_after_router=KuznetsovLSAtomSC9OrExternalCitation`。
- `current_numeric_context={'terminal_route_counts': {'NoTailDemandSparseOrLocalSurvivor': 1, 'PositiveLimsupPDECOrDiffuseCleanKLSDichotomy': 8}, 'global_max_actual_signature_share': 0.03571428571428571, 'global_min_inverse_l2_signature_support': 28.0, 'current_nodeletion_triggered': False, 'nodeletion_shape_route_counts': {'PhaseResidueMutualPDECWitness': 6}}`。

## 3. K1--K9 准入表

| key | condition | status | verified | failure route |
| --- | --- | --- | --- | --- |
| `K1` | dyadic ranges for m, ell, d, R and h | `ExternalTemplateRegistered` | `true` | range/high-lcm failure returns to PDEC/SAE/gcd-stratum ledger |
| `K2` | lowmod orthogonality; no fixed low residue atom persists | `RoutedToPDECOrSatisfiedOnDiffuseBranch` | `true` | positive finite lowmod signature -> column-tail/refined PDEC |
| `K3` | no short-window cap or early P x P local survivor gap | `CurrentExitsClosedFailureNamed` | `true` | short-window cap -> LocalSurvivor/SAE/refined PDEC |
| `K4` | no column/tail displacement cap persists | `RoutedToPDECOrCleanDiffuse` | `true` | column/tail displacement atom -> PDEC/ColumnCRT |
| `K5` | coefficient L2-flat on all fixed finite projections | `L2FlatOnCleanBranch` | `true` | large coefficient atom -> finite signature PDEC/SAE |
| `K6` | gcd/unit strata and dyadic splitting are polylog-accounted | `ExternalTemplateRegistered` | `true` | gcd/unit overrun -> gcd-stratum PDEC or finite exception |
| `K7` | same formal unit as PDEC/SAE/payment ledgers | `FormalUnitVerified` | `true` | 口径不一致 -> Multiplicity/Stitching absorption |
| `K8` | no promotable top-prime or fixed promoted residue remains | `PromotionDeletedOrNoDeletionRouted` | `true` | promotable residue -> prime-lift deletion/PDEC/NoDeletion router |
| `K9` | no persistent phase-residue mutual information | `MutualInformationRoutedOrFlat` | `true` | I(T;B) or KL(B||U_B) persists -> refined/new-layer PDEC |

## 4. 变量适配表

| A1 object | meaning | KLS object | status |
| --- | --- | --- | --- |
| `Omega` | 同一 continuous actual-payment clean residual formal unit | 一个 clean dyadic/Type block 的 formal unit B | `formal_unit_registered` |
| `ell` | 支付尾素数或升层 promoted prime 的单位变量 | Kloosterman 可逆变量 x 或 prime-variable block | `inverse_variable_ready` |
| `m` | 互补因子，满足 Py-d=ell*m 的 completion 变量 | 线性相位/Poisson 后的 m-block | `linear_variable_ready` |
| `d` | 列位移或 completion displacement | 频率/模数标签中的 residue datum | `column_displacement_routed_or_clean` |
| `R` | 低模 CRT、gcd/unit 剥离后的有效模数或 lcm 层 | Kloosterman 模数/dispersion level | `external_level_template_registered` |
| `h` | 非零 Fourier/Bohr 频率 | Kuznetsov/Bessel 频率参数 | `frequency_template_registered` |
| `W(m,ell)` | 行窗口、尾标签与 dyadic 平滑权重 | smooth compact window with polylog derivative loss | `smooth_partition_registered` |
| `a_ell,b_m,gamma` | diffuse payment residual 产生的 L2-flat 系数 | spectral large-sieve coefficient vectors | `l2_flat_coefficients_ready_on_clean_branch` |

## 5. 外部输入与自足边界

| stage | input | output | status |
| --- | --- | --- | --- |
| A1-CleanKLS admission | K1--K9 all verified or failures routed | clean A1 dyadic formal unit | `materialized_by_this_router` |
| A1 clean unit -> Kloosterman window | m, ell, d, R, h, smooth W and L2-flat coefficients | standard inverse-phase Kloosterman/dispersion block | `external_template_registered` |
| External DI/BFI/Kuznetsov input | windowed Kloosterman spectral/dispersion large sieve | O(q/log^2 y) clean residual bound | `closed_if_external_deep_theorem_is_accepted` |
| Self-contained version | do not cite external DI/BFI/Kuznetsov | prove Kuznetsov-LS atom (SC-9) | `self_contained_atom_open` |

## 6. 当前结论

A1 clean 分支现在有明确审稿边界：

```text
外部深定理版：接受窗口化 DI/BFI/Kuznetsov 大筛输入，则 A1 clean branch 吸收；
完全自足版：唯一剩余为证明 Kuznetsov-LS atom (SC-9)。
```

这不是无条件自足证明；它把 `CleanKLS/DLS` 的硬点压成一个单一谱大筛原子或明确外部引用。
