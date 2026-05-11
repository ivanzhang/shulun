# Prime Matrix strict 逐点 signed alpha value table 路由器

**状态：** `pointwise_signed_alpha_value_table_reduced_to_nonrecursive_row_weight_formula_open`

本步继续硬攻逐点 signed value table。结论是：表的 Phi atom、变差收费和解积分都只能在 signed weight 已给出后验证；失败命名纪律也已闭合。真正首要缺口是每条 skeleton row 的 signed_alpha_weight 值。现有独立恒等式路线会经 moving-block/NCBLK 回到 PDEC/CleanKLS 固定点，不能作为非递归证明。因此最新最精确单点是逐行非递归 signed alpha 权重公式。

```text
pointwise_signed_alpha_value_table_router_closed=true
failure_ledger_names_missing_values=true
independent_identity_route_is_fixed_point=true
exact_alpha_signed_weight_formula_proved=false
pointwise_nonrecursive_signed_alpha_weight_formula_proved=false
pointwise_signed_alpha_coefficient_value_table_proved=false
alpha_formula_signed_coefficient_lift_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton 的真正首字段是 signed_alpha_weight。当前最精确单点为 `PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow`：对每条 unsigned carry-shell skeleton row，给出非递归 signed 权重公式、pre-Cauchy 恒等式证明、非零符号局部因子和同 formal-unit 兼容。

## 2. 逐行公式字段

| field | meaning |
| --- | --- |
| `row_domain` | 输入为已闭合 unsigned carry-shell skeleton row，而不是 payment-side atom。 |
| `closed_weight_expression` | 给出 signed_alpha_weight 的显式表达式或有限递推公式。 |
| `identity_proof` | 证明表达式来自 pre-Cauchy 算术恒等式，早于 Cauchy/dispersion/Phi 推前。 |
| `nonzero_sign_local_factor` | 证明非零、符号和 local factor 与 row 同步；失败时命名回流。 |
| `no_reverse_recovery` | 证明没有使用零行覆盖、payment skeleton、terminal certificate 后验恢复权重。 |
| `same_unit_compatibility` | 权重公式与 source_tuple_hash、Phi atom、variation charge 使用同一 formal unit。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PointwiseValueTableTargetActive` | `true` | `false` | 上一层把 signed coefficient lift 压成逐 skeleton row 的 signed alpha value table。 | PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton |
| `ValueTableWouldCloseFourLegs` | `true` | `true` | 若逐行权重值表存在，则 signed source、权重律、Phi 推前和变差收费可以在同表上合取。 | 需要先给 signed_alpha_weight 值。 |
| `FailureLedgerAlreadyNamesMissingValues` | `true` | `true` | 缺少 signed value、Phi 不兼容、变差超预算已有命名出口。 | 命名出口尚未被排斥。 |
| `WeightLawDecompositionImported` | `true` | `false` | 权重律已经拆成独立恒等式、精确公式、非零符号局部因子、反推禁用和失败回流。 | ExactAlphaSignedWeightFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。 |
| `IndependentIdentityRouteIsFixedPoint` | `true` | `false` | 现有独立恒等式路线经 actual moving-block/NCBLK 回到 PDEC/CleanKLS 终端门。 | 不能用该循环证明逐行权重值。 |
| `PhiAndDisintegrationWaitForValues` | `true` | `false` | Phi 基底和解积分形式只有在 signed value 已给出后才能求和验证。 | 不能反向生成 signed_alpha_weight。 |
| `ReverseRecoveryBlocked` | `true` | `true` | payment skeleton 和早期零行 unsigned cover 都不能作为权重来源。 | 必须正向给出逐行非递归公式。 |
| `ExactWeightFormulaCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出每条 skeleton row 的 exact signed weight 公式。 | ExactAlphaSignedWeightFormulaLedger。 |
| `PointwiseNonrecursiveFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有逐 skeleton row 的非递归 signed 权重公式及其恒等式证明。 | PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow |
| `PointwiseSignedValueTableCurrentCorpusProved` | `false` | `false` | 没有逐行 signed 权重公式，整张 signed value table 不能成立。 | PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow |

## 4. 下一真正单点

```text
PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow
```
