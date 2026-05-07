# Prime Matrix PDEC-CAP 稠密旧洞核共同变量表路由器

**状态：** `dense_old_hole_kernel_reduced_to_common_variable_shell_dichotomy`

稠密旧洞选择核已经化为共同变量表：所有低层同余禁类都作用在同一个壳号变量 `k_b` 上。因此它没有未命名逃逸：无合法壳是容量/Hall 删除，固定壳正密度是 PDEC/ColumnCRT，无固定壳则是多壳分散，非平坦回 PDEC/ColumnCRT，平坦进入自足 SC-9。这仍不排除 PDEC/ColumnCRT 或 SC-9 终端，所以不是完整行/列无条件闭合。

## 1. 共同变量律

For a dense old-hole selector kernel, write the selected column as c_b=rho_b+r k_b, where rho_b is the affine residue forced by ((t+bQ-1)P+c_b)=0 mod r. For every old prime q|Q, the old-hole condition is equivalent to one forbidden shell residue k_b != r^{-1}(a_q(t)-rho_b) mod q. Thus all low-prime constraints are stored in the same variable k_b. If many b have no legal shell, capacity/Hall deletion fires. If a fixed shell or finite shell packet has positive mass, the low-mod signature is persistent and routes to PDEC or ColumnCRT. If no shell packet persists, the mass is genuinely multishell; non-flat multishell frequency returns to PDEC/ColumnCRT, while the flat case is exactly the self-contained SC-9 large-sieve atom.

```text
DenseOldHoleKernel:
  for (1-o(1))r residues b choose c_b in H_Q(t);
  ((t+bQ-1)P+c_b)=0 mod r.

Write:
  c_b = rho_b + r k_b,
  rho_b == -((t+bQ-1)P) mod r.

For each old prime q|Q:
  c_b != a_q(t) mod q
  <=> k_b != r^{-1}(a_q(t)-rho_b) mod q.

Therefore all low-prime bans act on one shell variable k_b.
```

## 2. 分流

```text
No legal k_b for many b
  => capacity/Hall deletion;

positive mass on fixed shell or finite shell packet
  => persistent low-mod signature
  => PDEC / ColumnCRT;

no fixed shell packet persists
  => genuine multishell dispersion;
  non-flat frequency => PDEC / ColumnCRT;
  flat frequency     => SelfContainedKuznetsovLSAtomSC9.
```

## 3. 汇总

- `dense_kernel_no_unnamed_escape_closed=true`。
- `dense_kernel_exclusion_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_dense_kernel_hardpoint=FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9`。
- `open_final_gates=['FixedShellLowModPersistencePDECOrColumnCRT', 'SelfContainedKuznetsovLSAtomSC9']`。
- `tail_pressure_summary={'row_count': 6, 'consistency_mismatch_count': 0, 'max_hall_uncertified_dead_slots': 0, 'min_hall_certified_dead_rate': 0.6871794871794872, 'max_survivor_kl_floor': 7.121387069923752, 'all_current_dead_slots_named_by_capacity_or_hall': True}`。
- `multishell_summary={'sn3c_pair_route_counts': {'kls_multishell_candidate': 2, 'lowmod_multiband_sync_candidate': 1}, 'sn3c_pair_count': 3, 'sn3d_kls_multishell_record_count': 2, 'sn3d_max_top_frequency_abs_over_excess': 2.0561747296635677, 'sn3d_max_partial_fourier_l2_over_excess': 14.275461495589605, 'multishell_interfaces_materialized': True}`。

## 4. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `DenseOldHoleKernelActive` | `true` | `false` | DenseOldHoleKernelCapacityPDECOrColumnCRT | 上一层已把占位饱和压成稠密旧洞选择核。 |
| `CommonVariableTableDerived` | `true` | `false` | c_b = rho_b + r k_b; k_b != r^{-1}(a_q(t)-rho_b) mod q | 对每个近满 occupied residue，列选择可唯一拆成仿射余数 rho_b 与壳号 k_b；低层每个素数只禁止 k_b 的一个线性残基。 |
| `CapacityFailureBranchNamed` | `true` | `false` | {'row_count': 6, 'consistency_mismatch_count': 0, 'max_hall_uncertified_dead_slots': 0, 'min_hall_certified_dead_rate': 0.6871794871794872, 'max_survivor_kl_floor': 7.121387069923752, 'all_current_dead_slots_named_by_capacity_or_hall': True} | 若共同变量表在大量 b 上没有合法 k，或 residual holes 的 Tail set-cover/Hall 条件失败，则直接支付删除势或容量失败。 |
| `FixedShellConcentrationRoutesToPDECColumnCRT` | `true` | `false` | positive shell mass gives persistent low-mod phase/residue signature | 若某个有限壳或有限壳簇承载正密度 b，则共同变量表在低模上持久复现，成为 PDEC 相位偏斜或 ColumnCRT 列位移输入。 |
| `MultishellDispersionRoutesToSC9OrHighFreqColumnPDEC` | `true` | `false` | {'sn3c_pair_route_counts': {'kls_multishell_candidate': 2, 'lowmod_multiband_sync_candidate': 1}, 'sn3c_pair_count': 3, 'sn3d_kls_multishell_record_count': 2, 'sn3d_max_top_frequency_abs_over_excess': 2.0561747296635677, 'sn3d_max_partial_fourier_l2_over_excess': 14.275461495589605, 'multishell_interfaces_materialized': True} | 若没有固定壳集中，选择核只能跨多壳分散；多壳同步若有低模/高频峰则回 PDEC/ColumnCRT，若平坦则进入自足 SC-9 大筛原子。 |
| `DenseKernelNoUnnamedEscape` | `true` | `false` | capacity / fixed-shell PDEC-ColumnCRT / multishell SC9 | 稠密旧洞选择核已经没有未命名第四出口；剩余是命名终端证书而非局部样本或概率缺口。 |
| `FixedShellLowModPersistencePDECOrColumnCRT` | `false` | `true` | terminal PDEC/ColumnCRT exclusion not submitted | 固定壳低模持久偏斜仍需提交同 formal unit 的 PDEC 或 ColumnCRT 排斥证书。 |
| `SelfContainedKuznetsovLSAtomSC9` | `false` | `true` | flat multishell clean atom remains open | 多壳完全平坦时仍落入自足 SC-9 谱大筛原子；外部深定理版不能冒充自足闭合。 |

## 5. 剩余

本路由器关闭的是稠密旧洞核的“无名逃逸”。剩余真正终端是固定壳低模持久偏斜的 PDEC/ColumnCRT 排斥，以及多壳平坦时的自足 `SelfContainedKuznetsovLSAtomSC9`。
