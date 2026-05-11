# Prime Matrix strict 逐点 primitive 核表路由器

**状态：** `pointwise_primitive_kernel_table_reduced_to_row_formula_weight_identity_rank_certificate_open`

逐点 primitive 核表被进一步压成三项必要输入：alpha row anchor/phase 发射公式、独立 pre-Cauchy signed 权重恒等式、同一表上的 ExactUV rank/multiplicity 证书。当前最窄优先点是 alpha row 发射公式；因为没有它，核表没有可赋权的 row，也无法对齐 Phi 或 `(u,v)` fiber。因此自足路线仍未闭合。

```text
pointwise_kernel_table_router_closed=true
alpha_row_anchor_phase_emission_formula_proved=false
independent_noncanonical_precauchy_arithmetic_identity_statement_proved=false
same_unit_exact_uv_rank_multiplicity_certificate_proved=false
pointwise_primitive_kernel_table_proved=false
same_formal_unit_kernel_identity_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate => AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows. 其中 `AlphaRowAnchorPhaseEmissionFormulaLedger` 是当前优先硬点：没有行发射公式，核表连行集合都没有，后续权重、Phi 推前和 rank/multiplicity 都无法绑定。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PointwiseKernelTableTargetActive` | `true` | `false` | 上一层已把同 formal-unit 核恒等式压成逐点 primitive alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `AlphaRuleContainerReady` | `true` | `true` | alpha 侧规则字段和失败分类已被列出。 | 仍缺逐行生成和值。 |
| `RowEmissionFormulaMissing` | `true` | `false` | 确定性发射映射已拒绝后验选择，但没有 A/D0/K/Omega/phase 到 row 的公式。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `SignedWeightIdentityMissing` | `true` | `false` | signed weight 必须来自独立 pre-Cauchy 算术恒等式；当前只有 no-go 和字段分解。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger |
| `ExactUVRankMultiplicityMissing` | `true` | `false` | ExactUV/fixed-pair/key partition 路线已定位，但没有同一 primitive 核表上的 rank/multiplicity 证书。 | SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `EmitterSourceTableWouldNeedSameRows` | `true` | `false` | emitter/source table 路线也需要相同 primitive rows，不能反过来自证核表。 | Pointwise primitive rows first; source table second. |
| `DisintegrationNotEnoughWithoutRows` | `true` | `false` | 逐纤维解积分只是有 rows 后的求和形式。 | 先提交逐点核表。 |
| `PointwiseKernelTableCurrentCorpusProved` | `false` | `false` | 当前材料没有同时给出行公式、权重恒等式和同表 rank/multiplicity 的逐点核表。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |

## 3. 核表公理

| axiom | meaning |
| --- | --- |
| `row_existence` | 每个 source tuple 发射有限、有序的 alpha/delta primitive rows。 |
| `weight_value` | 每行 signed weight 来自独立 pre-Cauchy 算术恒等式。 |
| `uv_phi_sync` | 每行同时输出 exact `(u,v)` 与 Phi/payment atom，且符号和重数同口径。 |
| `nonzero_local_factor` | local factor 非零；零权重、符号冲突和未登记项命名回流。 |
| `rank_multiplicity` | 同一表上证明 `(u,v)` fiber 的 bounded multiplicity/rank 或分散。 |
| `same_unit_no_recovery` | 全部字段都在同一 formal unit 中正向给出，不从 payment/零行/终端门反向恢复。 |

## 4. 下一优先硬点

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

并行必要输入：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```
