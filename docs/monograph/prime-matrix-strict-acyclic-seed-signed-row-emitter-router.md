# Prime Matrix strict acyclic seed signed row emitter 路由器

**状态：** `acyclic_seed_signed_row_emitter_reduced_to_primitive_row_signed_coefficient_law_open`

本步继续下钻 seed signed row emitter。seed 不存在时已有终端回流；若 seed 存在，unsigned skeleton 已能定位候选行，但仍没有每条 primitive row 的 signed coefficient law。该 law 必须给出筛权来源、符号、local factor、截断/相位收费和推前前 alpha/delta 求和恒等式。当前材料未证明该 law，因此行/列命题仍未无条件闭合。

```text
acyclic_seed_signed_row_emitter_router_closed=true
acyclic_seed_primitive_row_signed_coefficient_law_proved=false
acyclic_seed_signed_row_emitter_rule_proved=false
row_level_clean_core_origin_generation_table_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity 的 seed 缺失分支已回流终端家族；在合法 seed 分支内，真正剩余是 `AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward`。unsigned skeleton、ExactUV key 和解积分都不能反向生成该 law。

## 2. signed coefficient law 字段

| field | meaning |
| --- | --- |
| `basis_weight_source` | 系数来自哪个 pre-Cauchy 算术基函数/筛权，而不是 payment 原像。 |
| `sign_rule` | 每行符号由 seed 内部规则决定，并与 branch key 同步。 |
| `local_factor_rule` | 每行 local factor 的闭式公式和非零条件。 |
| `truncation_and_phase_charge` | 截断、相位过滤和 branch 变差收费的同口径登记。 |
| `alpha_delta_sum_identity` | 逐行 signed 系数求和后在推前前等于 actual alpha/delta 系数。 |
| `named_return` | 零系数、符号冲突、local factor 缺失或超预算全部命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SeedSignedEmitterTargetActive` | `true` | `false` | 上一层已把逐行生成表压成 acyclic seed 自带 signed row emitter。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SeedAbsentBranchAlreadyTerminalReturn` | `true` | `true` | 若合法 seed 无法提交，既有融合证书已把该分支回流终端家族。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `ZeroRowUnsignedSeedNoGoImported` | `true` | `true` | 早期零行覆盖不能当作 signed source seed。 | 只分析合法 seed 已提交的分支。 |
| `UnsignedRowSkeletonAvailableForSeedBranch` | `true` | `true` | source tuple/carry-shell/P列锚/layered-wheel 已给候选 row 的 unsigned skeleton。 | 仍缺 signed coefficient law。 |
| `SignedWeightLawStillOpen` | `true` | `false` | alpha signed weight law 已拆开，但 exact signed formula 与 pre-Cauchy 恒等式仍未证明。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `SignedLiftStillNeedsPointwiseValues` | `true` | `false` | signed lift 仍需要逐 skeleton row 的 signed value table。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `PrimitiveSummandExpressionStillOpen` | `true` | `false` | primitive summand 推前前 signed expression 未给出。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `UVKeySyncIsDownstreamAfterCoefficientLaw` | `true` | `false` | complete key 与 ExactUV/rank 只能在 row 的 signed coefficient 已给出后同步验证。 | 不能反向生成 coefficient law。 |
| `DisintegrationWaitsForSignedCoefficients` | `true` | `false` | 解积分形式需要已登记 signed coefficients 才能求和。 | 不能由解积分反推 coefficient law。 |
| `AcyclicSeedPrimitiveRowSignedCoefficientLawCurrentCorpusProved` | `false` | `false` | 当前材料没有给合法 seed 分支内每条 primitive row 的 signed coefficient law。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `SeedSignedEmitterCurrentCorpusProved` | `false` | `false` | 没有 signed coefficient law，seed signed row emitter 与推前前求和恒等式仍未证明。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |

## 4. 下一真正单点

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
