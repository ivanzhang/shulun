# R2a 有效 FS 边投影终审

**状态：** `projection_review_passed_modulo_DBA_A1_A5_acceptance`

4.3.11g 的有效 FS 边投影没有生成新坏层：正常情形投影到 FS8-Disp-poly；非正常情形分别由 cumulant 抵消、overlap/LF/SK、低体积、Hall/rank-defect 或 DBA 分母/Jacobian/ramification atlas 覆盖。

## 分情况归宿
### P1_normal_effective_edge
- 情形：存在一条 FS 边在冻结其它 skeleton 变量后仍保留两个主 Kloosterman 坐标。
- 归宿：`normal_projection_to_FS8_Disp_poly`
- 状态：`closed_normal_case`
- 证据：docs/final-proof-draft.md:4.3.11g, docs/final-proof-draft.md:FS8-Disp-poly

### P2_component_phase_separates
- 情形：所有 FS 相位按 connected 分量分离。
- 归宿：`cumulant_Mobius_cancellation`
- 状态：`closed_by_connected_cumulant_cancellation`
- 证据：docs/final-proof-draft.md:4.3.11e, docs/final-proof-draft.md:4.3.11g

### P3_overlap_LF_SK_contraction
- 情形：候选 FS 连接实为 overlap/LF/SK 收缩、对角或低体积项。
- 归宿：`4.3.11b_c_or_low_volume_atlas`
- 状态：`closed_by_existing_mechanisms`
- 证据：docs/final-proof-draft.md:4.3.11b, docs/final-proof-draft.md:4.3.11c, docs/final-proof-draft.md:6.14.2c-FS8

### P4_Hall_matching_failure
- 情形：多条 FS 边争用叶变量，Hall 子集满足 |N(E0)|<|E0|。
- 归宿：`four_point_rank_failure or jacobian_common_branch`
- 状态：`verified_by_DBA_A1_row_30`
- 证据：docs/dba-A1-source-coverage-certificate.md:41, docs/dba-closure-finite-generated-atlas.md:66, docs/final-proof-draft.md:7.2.CH-FS7

### P5_branch_or_denominator_merger
- 情形：多父关系来自分母分支合并、ramification 或 Jacobian 退化。
- 归宿：`denominator_pole or ramification or jacobian_common_branch`
- 状态：`covered_by_DBA_atlas`
- 证据：docs/dba-closure-finite-generated-atlas.md, docs/final-proof-draft.md:6.14.2c-FS8

## 覆盖核查
- DBA-A1 Hall 行：`verified`
- DBA atlas 未知去向数：`0`
- 新坏层类型数：`0`
