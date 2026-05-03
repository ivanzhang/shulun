# R2a 加权 FNL-KS 接口审计

**状态：** `R2a_interfaces_review_passed_modulo_DBA_and_parameter_ledger_acceptance`

在 DBA 与 C_poly 扫描之后，R2a 不再是新的 atlas 问题。WLV-piece 三步复核已把加权 LV/AE 传递归入确定性旋转、低体积 atlas 与 C_poly 账本；4.3.11g 投影终审也已给出。当前 R2a 仅依赖既有 DBA-A1/A5 与参数账本的最终接受。

## 三个接口
### R2a-I1_weight_peeling
- 命题：W_Gamma 可分解为盒指示/Stieltjes 片，且总变差由 (C8 s)^(C8 s) log^(C8 s) P 控制。
- 状态：`structurally_reduced_by_KS_W_poly`
- 剩余：把 Hardy--Krause 分解写到足够显式，使每个片都可用于 LV-KS，且不改变两个主 Kloosterman 坐标。
- 证据：docs/final-proof-draft.md:5509, docs/final-proof-draft.md:1807

### R2a-I2_phase_inheritance
- 命题：冻结非主 skeleton 变量后，相位仍是 FS8/Kloosterman 互易相位，分母、Jacobian、rank 与共振 atlas 类型不变。
- 状态：`projection_review_passed_modulo_DBA_A1_A5_acceptance`
- 剩余：最终接受 DBA-A1/A5 与 6.14.2c-FS8 覆盖表；不再是独立 R2a 投影缺口。
- 证据：docs/final-proof-draft.md:4.3.11g, docs/r2a-effective-fs-edge-projection-review.md, docs/final-proof-draft.md:1466, docs/final-proof-draft.md:1814, docs/dba-A1-source-coverage-certificate.md

### R2a-I3_weighted_LV_AE_transfer
- 命题：大的加权 connected-skeleton 和推出 KS-ARC-fail，再推出 KS-4E，且只损失 C_poly 支付的对数幂。
- 状态：`review_passed_modulo_existing_atlas_and_parameter_ledger`
- 剩余：最终接受 6.14.2c-FS8 低体积 atlas 与 C_poly 参数账本；不再是独立 R2a 数学接口。
- 证据：docs/final-proof-draft.md:6.18.1d-WLV, docs/r2a-wlv-piece-review.md, docs/final-proof-draft.md:5619, docs/final-proof-draft.md:5663, docs/r2-Cpoly-absorption-scan.md

## 最小剩余
- R2a-I3：WLV-piece 三步复核已生成，剩既有 atlas/账本最终接受
- R2a-I2：4.3.11g 投影终审已生成，剩 DBA-A1/A5 最终接受
- 随后接入既有 LV-KS/AE-KS/DBA 链并由 C_poly 吸收
