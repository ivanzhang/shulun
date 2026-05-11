# Prime Matrix strict signed-source 固定点切断证书

## 1. 结论

本步没有改换命题，而是把最新一圈下钻结果合并审查。几何锚输入已经闭合，但 signed coefficient 来源链从逐行原始表出发，经 seed/emitter、basis word、assignment、value map、origin identity 后又回到同一逐行原始表。因此不能把这条链当作证明；必须新增一个不读取下游 payment/来源表/早期零行覆盖的 pre-Cauchy signed coefficient 发射核。

## 2. 状态

- same_theorem_target_preserved=true
- current_internal_route_is_signed_source_fixed_point=true
- geometric_anchor_branch_closed=true
- reverse_and_zero_row_recovery_blocked=true
- noncircular_signed_coefficient_emission_kernel_proved=false
- row_level_clean_core_origin_generation_table_proved=false
- direct_unconditional_contradiction_found=false
- row_column_unconditional_closed=false

## 3. 固定点判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RowLevelGenerationTableIsActiveTarget` | `true` | `false` | 最新 basis word 来源恒等式已回收到逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `SignedSourceSpineMaterialized` | `true` | `true` | 从 row-level 表到 seed/emitter、coefficient law、basis source、basis word 构造的依赖脊柱已全部登记。 | 登记脊柱不等于生成 signed coefficient。 |
| `GeometricAnchorBranchClosed` | `true` | `true` | 锚选择、窗口端点、phase pullback 和低重叠收费已闭合。 | 几何闭合只给 unsigned word 输入，不给 signed coefficient。 |
| `SignedAssignmentSpineReturnsToRowLevel` | `true` | `true` | signed slot、assignment、value map、origin identity 最终回到同一逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `ReverseAndZeroRowRecoveryBlocked` | `true` | `true` | 来源环、payment 反推、早期零行 unsigned cover 均不能生成 signed seed/rows。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `CurrentInternalRouteIsSignedSourceFixedPoint` | `true` | `true` | 现有内部路线形成 RowLevel -> ... -> RowLevel 的 signed-source 固定点。 | 固定点切断后必须提交非循环 signed coefficient emission kernel。 |
| `NoncircularSignedCoefficientEmissionKernelCurrentCorpusProved` | `false` | `false` | 当前材料没有不读取下游表/来源恒等式/payment 的 pre-Cauchy signed coefficient 发射核。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `RowLevelOriginalGenerationTableCurrentCorpusProved` | `false` | `false` | 没有非循环发射核，逐行原始生成表仍未证明。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |

## 4. 非循环发射核合同

| field | meaning |
| --- | --- |
| `domain` | 只读取 actual noncanonical seed/source tuple 及已闭合 primitive basis word 坐标。 |
| `signed_coefficient_formula` | 在 Cauchy/payment/Phi 推前之前正向输出 signed coefficient。 |
| `sign_and_local_factor` | 同步给出 sign、local factor、非零条件和 branch key。 |
| `prepushforward_sum_identity` | 证明输出 rows 的求和已等于目标 alpha/delta 贡献。 |
| `no_self_reference` | 公式不得读取 row-level 表、来源恒等式、payment/Phi 下游结果或早期零行覆盖。 |
| `named_return_tags` | 缺 seed、零局部因子、符号冲突、超预算或作用域冲突必须命名回流。 |

## 5. 下一真正单点

NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows

若该 kernel 不能提交，则按命名纪律回流：

PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily

