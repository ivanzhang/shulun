# C6 行侧硬路线审计

**状态：** `row_route_reduced_to_existing_FS8_DBA_parameter_acceptance; threshold_enhancements_separate`

R1a/R1b 与 R2a 的终审证书均已生成；行侧硬路线现在主要依赖既有 FS8-Disp/FNL-KS/DBA、A1--A5 与参数账本的最终接受。

## 主链
### R1_gap_word_capacity_gap
- 命题：gap-word 总容量缺口 (4.3.8e) 给出短块的 alpha<1。
- 状态：`R1_interfaces_review_passed_modulo_existing_FS8_DBA_parameter_acceptance`
- 证据：final-proof-draft.md:4.3.8, final-proof-draft.md:4.3.10, docs/r1-gap-word-capacity-audit.md

### R2_short_block_cumulant
- 命题：对 s<=c log P 的短块 cumulant 界 (4.3.9a)。
- 状态：`R2a_interfaces_review_passed_modulo_DBA_and_parameter_ledger; C_poly_absorption_scanned`
- 证据：final-proof-draft.md:4.3.9, final-proof-draft.md:4.3.11, docs/r2-fs8-polymer-cumulant-audit.md, docs/r2-Cpoly-absorption-scan.md, docs/r2a-weighted-fnl-ks-interface-audit.md

### R3_FS8_polymer_mechanisms
- 命题：FS8-polymer connected 机制归约为 overlap/LF/SK/FS；FS 坏层进入 DBA atlas。
- 状态：`mechanism_atlas_verified_for_listed_failures; needs acceptance of polymer cumulant expansion`
- 证据：final-proof-draft.md:4.3.11, docs/dba-A1-source-coverage-certificate.md

### R4_row_window_exclusion
- 命题：容量缺口与短块 cumulant 集中排除正常行窗口全覆盖。
- 状态：`conditional_on_R1_R2`
- 证据：final-proof-draft.md:4.3.7, final-proof-draft.md:4.3.8a--c

### R5_row_theorem
- 命题：正常窗口排除加 B.4 强尾界推出每行含素数。
- 状态：`conditional_on_R4_and_existing_row_tail_interfaces`
- 证据：final-proof-draft.md:4.1--4.2, final-proof-draft.md:B.4

## 阈值增强链
### E1_CH_tail_chernoff1
- 命题：strong CH-tail / chernoff1 package lowers finite verification threshold.
- 状态：`separate_threshold_enhancement_not_required_for_sufficiently_large_sawtooth_chain`
- 证据：final-proof-draft.md:7.2.T1, final-proof-draft.md:7.2.CH-FS

### E2_strong_CH_FS_activity
- 命题：normal FS skeleton has per-edge fixed loss lambda_FS<1e-2 via Hall/leaf variable selection.
- 状态：`not_fully_closed; needed_for_chernoff1_not_for_basic_log_power_cumulant_bound`
- 证据：final-proof-draft.md:7.2.CH-FS4--FS9

## 最小剩余
- R1a/R1b 复核证书均已生成；剩既有 FS8-Disp/FNL-KS/DBA 与参数账本最终接受
- R2a 的 WLV-piece 与 4.3.11g 终审证书均已生成；剩既有 DBA-A1/A5 与参数账本最终接受
- 随后 R4/R5 行侧硬路线由既有 B.4 行尾界机制推出
