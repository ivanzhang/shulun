# 全局无条件闭合审计

**状态：** `not_unconditionally_closed`

当前文稿仍是条件化/归约型证明框架。若要升级为全局无条件证明，必须逐项闭合 blocking_items。

## 已较强闭合的局部部件
- G2 stable payment telescope 在 G1 与 stable 正质量条件下是代数闭合的。
- H80/current finite candidate outward interval certificates 已局部闭合。
- G1 local audits 给出 L_cap=0.48 与 D_* 正余量的可攻路线。
- 离散 coarea 本身已归约到一变量有理函数分片估计，但依赖 DBA-closure 吸收坏层。
- DBA-closure 已抽取为有限生成 atlas：docs/dba-closure-finite-generated-atlas.md。
- DBA-A5 参数吸收账本已数值通过：docs/dba-A2-A5-parameter-ledger.md。
- DBA-A3/A4 已在 atlas 中预算归类：docs/dba-closure-finite-generated-atlas.md。
- DBA-A1 来源矩阵已扩展到 32 行且 unknown_destinations=0。
- DBA-A2 固定变量数/次数表已生成：docs/dba-A2-fixed-degree-table.md。
- DBA-A1 逐行覆盖证书已生成：docs/dba-A1-source-coverage-certificate.md。
- B1 接回链审计已生成：docs/b1-closure-chain-audit.md。
- C6 行侧硬路线审计已生成：docs/c6-row-hard-route-audit.md。
- R2b C_poly 参数吸收扫描已生成：docs/r2-Cpoly-absorption-scan.md；B1 剩余进一步收缩为 R1 与 R2a。
- R2a WLV-piece 与有效 FS 边投影终审已生成：docs/r2a-wlv-piece-review.md 与 docs/r2a-effective-fs-edge-projection-review.md；R2a 剩余并入既有 DBA/参数账本接受。
- R1a/R1b 复核已生成：docs/r1a-normal-fs-average-review.md 与 docs/r1b-weighted-bad-layer-absorption-review.md；R1 剩余并入既有 FS8/DBA/参数账本接受。
- B1 DBA 最终接受复核已生成：docs/b1-dba-final-acceptance-review.md；B1 从新硬点降为证书链终稿接受问题。
- G1 全局传递性审计已生成：docs/d4-r5-G1-global-transitivity-audit.md；B2 最小缺口为语义不变、backflow、jump/终端覆盖。
- G1a 状态语义审计已生成：docs/d4-r5-G1-state-semantics-audit.md；状态变量口径已固定，剩投影同型性和 A_eff。
- G1 partition refinement 审计已生成：docs/d4-r5-G1-partition-refinement-audit.md；验证互斥分解 L=transition+short+ordinary+light 且 heavy 为父类监控量。
- G1 ordinary、unified exceptional、theoremization 与 O2 审计已生成：docs/d4-r5-G1-ordinary-energy-audit.md、docs/d4-r5-G1-unified-exceptional-energy-audit.md、docs/d4-r5-G1-unified-theoremization-audit.md、docs/d4-r5-G1-O2-effective-support-audit.md；当前最硬为 O2 的 Neff(nonordinary)<=64。

## 阻塞项
### B1_UAS_DBA_four_point_energy：行侧短段双线性/FS8-polymer/B.0.4*
- 状态：`local_certificate_chain_reviewed_modulo_final_acceptance`
- 阻塞命题：行侧 B1 sawtooth 硬路线已压缩为接受既有 DBA-A1--A5、FS8/FNL-KS 与 R1/R2 终审证书；不再是新的局部硬点，但仍需终稿审查接受。
- 剩余义务：
  - 终稿人工接受 A1：确认正文没有新增未列失败方式；当前 32/32 来源行 verified，unknown=0
  - 终稿接受 A2：固定变量数/次数表与标准 resultant 高度界引用
  - 终稿接受 A3/A4/A5：步长频率、低体积、Rankin/KS 参数余量账本
  - 终稿接受 R1/R2：R1a/R1b 与 R2a 终审证书接入 FS8/FNL-KS/DBA 链条
- 证据位置：docs/final-proof-draft.md:3211, docs/final-proof-draft.md:3693, docs/final-proof-draft.md:4160, docs/final-proof-draft.md:4247, docs/b1-dba-final-acceptance-review.md

### B2_G1_global_capacity_defect：D4/R5 递归剥离全局容量闸门
- 状态：`not_closed_global_local_audits_available`
- 阻塞命题：G1 局部容量证据很强，但必须证明递归状态语义不变、backflow 投影可传递、jump/终端窗口族全局覆盖。
- 剩余义务：
  - G1a：状态定义已固定；统一 exceptional A_eff 已压缩为 O1--O4，优先证明 O2 的 Neff(nonordinary)<=64
  - G1d：构造 backflow 投影 pi_j 并证明 eps_j 可求和
  - G1c/G1e：证明 jump 边界计数和终端窗口族覆盖
- 证据位置：docs/d4-r5-G1-capacity-audit.json, docs/d4-r5-G1-lyapunov-energy-audit.json, docs/d4-r5-G1-capacity-route.md:139, docs/d4-r5-G1-global-transitivity-audit.md

### B3_R5_G3_G4_G5_globalization：R5global jump/backflow/base certificate
- 状态：`not_closed`
- 阻塞命题：G3/G4/G5 仍需全局边界穿越计数、backflow 求和、终端窗口族覆盖。
- 剩余义务：
  - jump 阈值穿越次数/误差求和证明
  - backflow 投影损失 eps_j 可求和证明
  - 相位模板枚举器覆盖所有终端坏窗口
  - 对枚举器输出运行外向舍入证书
- 证据位置：docs/d4-r5-global-rpl-gates.json, docs/d4-r5-current-candidate-closure-status.md:25

### B4_column_LC_pointwise_capacity：列命题/非零列点态容量
- 状态：`not_closed_or_conditionally_reduced`
- 阻塞命题：列侧需要点态高阈值筛余容量下界或等价强等差素数/证书输入。
- 剩余义务：
  - C.2 列场 cumulant 常数抽取
  - C.2.3/C.3.1 整数化与容量误差合并
  - 证明所有非零列的点态余量同时成立
- 证据位置：docs/final-proof-draft.md:996, docs/final-proof-draft.md:12189, docs/final-proof-draft.md:12363

### B5_explicit_threshold_and_finite_verification：显式阈值与有限验证
- 状态：`not_closed`
- 阻塞命题：即便高段证明闭合，仍需抽取 P_* 并完成 P<=P_* 的可复核有限验证。
- 剩余义务：
  - 从所有行列接口抽取显式 P_*
  - 实现有限验证证书格式
  - 运行并归档阈值以下全部奇素数验证
- 证据位置：docs/final-proof-draft.md:7, docs/final-proof-draft.md:48, docs/d4-r5-review-grade-status.md:28

## 最小闭合路径
1. 终稿接受 B1 证书链，确保行侧 sawtooth 硬路线表述为条件明确的局部闭合。
2. 优先闭合 B2/B3，把 D4/R5 递归剥离证书全局化。
3. 闭合 B4，完成列侧 LC 点态容量。
4. 抽取显式阈值并完成 B5 有限验证。

## 审稿级结论
当前不能声称已经完成全局无条件证明。下一步最优任务是优先闭合 `B1_UAS_DBA_four_point_energy`，因为它是行侧硬路线的上游主闸门；同时保留 G1/G3/G4/G5 与列侧 LC 作为独立并行闸门。
