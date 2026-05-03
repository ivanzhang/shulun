# R1a 正常层 FS 平均放大界复核

**状态：** `R1a_review_passed_modulo_FS8_Disp_and_existing_DBA_acceptance`

R1a 已归约到既有 FS8-Disp/FNL-KS/DBA 链条：主项乘法归一，非零 sawtooth 频率在正常层相消，全部退化项排除出 N_FS 并由 R1b 处理。

## 复核项
### N1_main_term_normalization
- 命题：FS8 主项 |I|/Q 与八个单点 Stieltjes 主项乘法归一，正常层平均为 1+o(1)。
- 状态：`closed_by_FS8_normal_form`
- 证据：docs/final-proof-draft.md:4.3.FS8-4, docs/final-proof-draft.md:4.3.10d-R1a

### N2_nonzero_sawtooth_cancellation
- 命题：所有非主项都含非零 sawtooth 频率；正常层由 FS8-Disp 给 o(1)。
- 状态：`closed_modulo_FNL_KS_DBA_chain`
- 证据：docs/final-proof-draft.md:4.3.FS8-5, docs/final-proof-draft.md:FS8-Disp

### N3_no_bad_layer_double_counting
- 命题：若分母/CRT/Jacobian/rank/共振失败，则该项不在 N_FS，而进入 R1b 带权坏层吸收。
- 状态：`closed_by_normal_bad_partition`
- 证据：docs/final-proof-draft.md:4.3.10d-R1a, docs/r1b-weighted-bad-layer-absorption-review.md
