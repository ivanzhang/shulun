# B1 闭合链审计

**状态：** `B1_row_sawtooth_route_reduced_to_existing_certificate_acceptance; global_theorem_not_closed`

DBA-A1--A5、R1a/R1b 与 R2a 终审证书已支撑行侧 B1 sawtooth 硬路线的局部闭合；剩余是接受既有证书链，而非新的 B1 局部硬点。全局主定理仍受 R5 全局化、列侧 LC、显式阈值与有限验证阻塞。

## 主链
### C1_DBA_closure
- 命题：DBA-closure 吸收分母、导数、ramification、rank、Jacobian、共振与低体积坏层。
- 状态：`A1_A5_reviews_passed_modulo_final_editorial_acceptance`
- 证据：docs/dba-closure-finite-generated-atlas.md, docs/dba-A1-source-coverage-certificate.md, docs/dba-A2-fixed-degree-table.md, docs/dba-A2-A5-parameter-ledger.md, docs/b1-dba-final-acceptance-review.md

### C2_4E_DISP
- 命题：离散 coarea、局部 rank 与 DBA-closure 推出四点厚化分散 4E-DISP。
- 状态：`conditional_on_C1_and_standard_local_rank/coarea_acceptance`
- 证据：final-proof-draft.md:6.10, final-proof-draft.md:6.13, final-proof-draft.md:6.14.7

### C3_UAS
- 命题：4E-DISP 通过 LV/AE 能量放大排除短弧集中，给出 sawtooth 路线的 UAS。
- 状态：`conditional_on_C2_and_LV_AE_chain`
- 证据：final-proof-draft.md:6.9.5, final-proof-draft.md:6.18.1--6.18.3

### C4_FNL_NL
- 命题：UAS/DBA 排除大 Fourier 值并推出 FNL，继而得到 NL。
- 状态：`conditional_on_C3_and_admissibility_6_17_6`
- 证据：final-proof-draft.md:6.17, final-proof-draft.md:6.18.4

### C5_B004_star
- 命题：FNL/NL 闭合硬边界 sawtooth 接口 B.0.4*。
- 状态：`sawtooth_route_conditionally_closed; does_not_close_smooth_prime_weight_route`
- 证据：final-proof-draft.md:6.18.4, final-proof-draft.md:6.16.2

### C6_row_hard_route
- 命题：B.0.4* 接入行侧硬路线；R1/R2 终审证书已生成。
- 状态：`row_hard_route_reduced_to_existing_FS8_DBA_parameter_acceptance`
- 证据：docs/c6-row-hard-route-audit.md, docs/r1-gap-word-capacity-audit.md, docs/r2a-weighted-fnl-ks-interface-audit.md

## 独立接口
### S1_smooth_prime_weight_route
- 说明：带 dπ(p) 的 B.0.4S-short 需要素数权/AP 双线性输入；UAS/DBA 只闭合硬 sawtooth 边界。
- 状态：`separate_not_closed`
- 证据：final-proof-draft.md:6.16

### S2_chernoff_threshold_enhancements
- 说明：7.2 chernoff1 / CH-tail / strong CH-FS 是阈值压缩增强链；不是当前 sawtooth 链的必要条件，但低阈值方案需要它们。
- 状态：`separate_enhancement_chain_not_fully_closed`
- 证据：final-proof-draft.md:7.2.T1, final-proof-draft.md:7.2.CH-FS

### S3_column_LC
- 说明：列侧点态容量 LC 独立于行侧 B1 sawtooth 链。
- 状态：`separate_global_blocker`
- 证据：final-proof-draft.md:C.2, docs/global-unconditional-closure-audit.md
