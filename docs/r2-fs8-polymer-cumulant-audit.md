# R2 FS8-polymer 短块 Cumulant 审计

**状态：** `reduced_to_weighted_FNL_KS; C_poly_absorption_scanned`

Overlap/LF/SK mechanisms are closed or reduced to existing conditions. C_poly numeric absorption has passed the scanned ledger values. The real remaining work is R2a: prove 4.3.11d uniformly for connected skeleton polymer weights.

## 四类机制
### M1_overlap_diagonal
- 命题：overlapping short blocks contract to a connected super-block and lose a free start coordinate
- 状态：`closed_by_combinatorial_count`
- 证据：final-proof-draft.md:4.3.11, final-proof-draft.md:4.3.11b

### M2_LF_large_factor
- 命题：non-overlapping blocks cannot share a >sqrt(P) factor inside the row window; LF edges reduce to overlap/diagonal
- 状态：`closed_modulo_existing_large_factor_mutex`
- 证据：final-proof-draft.md:4.3.11, large-factor mutual exclusion lemma in prior sections

### M3_SK_small_sieve
- 命题：small-sieve admissibility is conditioned into the candidate skeleton; incompatible CRT patterns have zero count
- 状态：`closed_as_conditioned_weight_not_connected_noise`
- 证据：final-proof-draft.md:4.3.11, final-proof-draft.md:B.0.3e+

### M4_FS_floor_sum
- 命题：FS connected skeletons reduce to FNL-KS with polymer weights; bad layers go to DBA atlas
- 状态：`reduced_to_4_3_11d; C_poly_absorption_scanned`
- 证据：final-proof-draft.md:4.3.11d--f, final-proof-draft.md:6.18.1d-KS-poly, docs/dba-A1-source-coverage-certificate.md, docs/r2-Cpoly-absorption-scan.md, docs/r2a-weighted-fnl-ks-interface-audit.md

## 最小剩余
### R2a_4_3_11d_weighted_FNL_KS
- 任务：Prove FNL-KS uniformly for connected skeleton weights W_Gamma with complexity (C8 s)^(C8 s).
- 当前归约：R2a audit splits the task into weight peeling, phase inheritance, and weighted LV/AE transfer. WLV-piece and 4.3.11g projection reviews have passed modulo existing DBA atlas and C_poly ledger acceptance.

### R2b_C_poly_numeric_absorption
- 任务：Choose C_poly and rerun/verify that C_star, B1, B2, B4, KS margins remain positive.
- 状态：`numeric_absorption_passed_for_scanned_values`
- 当前归约：Parameter scan docs/r2-Cpoly-absorption-scan.md passes for C_poly=0,80,160,240,320,480; this is now a ledger choice, not a core analytic obstruction.
