# B1 DBA 最终接受复核

**状态：** `B1_row_sawtooth_route_reduced_to_final_editorial_acceptance_of_existing_certificates`

B1 行侧 sawtooth 硬路线的局部技术义务已压缩为接受既有证书链：DBA-A1--A5、FS8-Disp/FNL-KS/DBA、R1a/R1b 与 R2a 终审。仍不能推出全局主定理，因为 B2/B3 R5 全局化、B4 列侧 LC、B5 显式阈值与有限验证仍独立阻塞。

## 复核项
### A1_source_coverage
- 命题：6.10--6.18、4.3.6/FS8 与 FS8-polymer 已列失败方式都有合法 atlas/budget 去向。
- 状态：`passed_for_listed_sources_32_of_32_unknown_0`
- 剩余：终稿人工确认正文未新增未列失败方式。
- 证据：docs/dba-A1-source-coverage-certificate.md

### A2_fixed_degree_height
- 命题：所有 DBA 多项式 atlas 项变量数和次数只依赖 r，resultant 高度为 P^{O_r(1)}。
- 状态：`passed_with_fixed_degree_table`
- 剩余：接受标准 Macaulay/resultant 高度界引用。
- 证据：docs/dba-A2-fixed-degree-table.md, docs/dba-A2-A5-parameter-ledger.md

### A3_step_frequency_budget
- 命题：步长/频率共振的 1/q+1/T 损失由 Rankin 与 B4 余量吸收。
- 状态：`passed_margin_B4_600`
- 剩余：无新增预算；需终稿保持所有共振引用均指向 A3。
- 证据：docs/dba-closure-finite-generated-atlas.md, docs/dba-A2-A5-parameter-ledger.md

### A4_layering_low_volume_budget
- 命题：层化端点/低体积盒由 C_L/C_KS 与 KS 余量吸收。
- 状态：`passed_KS_margins_220_140`
- 剩余：无新增预算；需终稿保持低体积口径不被重复计入正常层。
- 证据：docs/dba-closure-finite-generated-atlas.md, docs/dba-A2-A5-parameter-ledger.md

### A5_numeric_absorption
- 命题：B1,B2,B4 大于高度、Rankin、KS 与层化损失常数。
- 状态：`passed_positive_margins_except_B5_equality_not_used_here`
- 剩余：B5_min 等号属于 Stieltjes/阈值接口，不阻塞 B1 sawtooth DBA。
- 证据：docs/dba-A2-A5-parameter-ledger.md, docs/r2-Cpoly-absorption-scan.md

### C6_row_interface
- 命题：R1a/R1b 与 R2a 终审证书已生成，行侧短块接口归入 FS8/DBA/参数账本接受。
- 状态：`passed_modulo_existing_FS8_DBA_parameter_acceptance`
- 剩余：与 A1--A5 同步接受；不再是独立 B1 局部硬点。
- 证据：docs/c6-row-hard-route-audit.md, docs/r1-gap-word-capacity-audit.md, docs/r2a-weighted-fnl-ks-interface-audit.md
