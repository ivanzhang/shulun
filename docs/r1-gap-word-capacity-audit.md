# R1 Gap-word 容量缺口审计

**状态：** `R1_interfaces_review_passed_modulo_existing_FS8_DBA_parameter_acceptance`

R1 的两个接口均已生成复核证书：R1a 归约到 FS8-Disp/FNL-KS/DBA 链条，R1b 归约到 DBA-A3/A4/A5 与 C_poly 预算接受。当前 R1 不再是独立新硬点；剩余并入既有 FS8/DBA/参数账本最终接受。

## 接口
### R1a_normal_FS_average
- 命题：正常层 gap-word 加权平均的 FS singular factor 为 1+o(1)，即 (4.3.10d)。
- 状态：`review_passed_modulo_FS8_Disp_and_existing_DBA_acceptance`
- 剩余：最终接受 FS8-Disp/FNL-KS/DBA 链条；不再是独立 R1a 缺口。
- 证据：docs/final-proof-draft.md:4.3.10d-R1a, docs/r1a-normal-fs-average-review.md, docs/final-proof-draft.md:FS8-Disp, docs/r2a-weighted-fnl-ks-interface-audit.md

### R1b_weighted_bad_layer_absorption
- 命题：坏层满足带权吸收 (4.3.10e+)，即 sum_B N_g S_g^FS=o(sum N_g)。
- 状态：`reduced_to_existing_DBA_A3_A4_A5_budget_acceptance`
- 剩余：最终接受 4.3.10f 的逐类支配与既有 DBA-A3/A4/A5 在 singular-factor 加权口径下的适用性。
- 证据：docs/final-proof-draft.md:4.3.10f, docs/r1b-weighted-bad-layer-absorption-review.md, docs/dba-A2-A5-parameter-ledger.md, docs/dba-A1-source-coverage-certificate.md

### R1c_capacity_arithmetic
- 命题：若 K_sing<=2，则 alpha_8<=2 Theta_rough^8=0.735733...，得到 gamma>=0.132133...。
- 状态：`closed_numeric_arithmetic`
- 剩余：无；只需保持 Theta_rough 常数来源可复核。
- 证据：docs/final-proof-draft.md:4.3.9g

## 最小剩余
- R1b：4.3.10f 支配证书已生成，剩既有 DBA-A3/A4/A5 加权预算最终接受
- R1a：4.3.10d-R1a 复核证书已生成，剩 FS8-Disp/FNL-KS/DBA 链条最终接受
- 随后由 K_sing<=2 的数值预算推出 alpha_8<1
