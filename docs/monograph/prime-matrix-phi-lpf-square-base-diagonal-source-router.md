# Prime Matrix Phi-LPF square-base diagonal source 证书

**状态：** `phi_lpf_unit_seed_reduced_to_square_base_diagonal_source_open`

virtual-unit seed 不能作为独立 composite signed row：`(p,1)` 是被 Phi-LPF 计数公式减掉的 prime row。每个 owner bucket 的最小真实 support key 是 square-base diagonal root `(p,p)`，它没有更小的 composite support predecessor；唯一 predecessor 是 virtual `(p,1)`。因此 seed 硬点进一步收窄为 `PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward`：必须在 Cauchy/Phi/payment 前对 `(p,p)` 同时给出 source tuple、basis word、signed coefficient、orientation/local factor、alpha/delta branch、ExactUV、推前前恒等式和 prime-row leak guard。

```text
virtual_unit_not_composite_support_proved=true
square_base_minimal_support_root_proved=true
no_support_predecessor_below_square_base_proved=true
virtual_seed_collapses_to_square_base_declaration=true
square_base_diagonal_root_signed_source_declaration_proved=false
phi_lpf_rough_cofactor_signed_transport_law_proved=false
row_column_unconditional_closed=false
```

## 1. diagonal root 结构

`(p,1)` 不是 composite support。对 owner bucket `p`，`1<m<p` 的 cofactor 一定含有小于 `p` 的素因子，
所以最小真实 support cofactor 是 `m=p`。因此 `(p,p)` 是 transport forest 的 diagonal root。

## 2. 样本 root 审计

| N | layers | square roots | root identity |
| ---: | ---: | ---: | --- |
| 30 | 3 | 3 | `true` |
| 100 | 4 | 4 | `true` |
| 997 | 11 | 11 | `true` |
| 5003 | 19 | 19 | `true` |
| 10000 | 25 | 25 | `true` |

## 3. declaration 字段

| field | meaning |
| --- | --- |
| `diagonal_root_key` | 每个 owner bucket 的最小真实 support key `(p,p)`。 |
| `actual_source_tuple` | 同 formal-unit、Cauchy/Phi/payment 前的 actual noncanonical source tuple。 |
| `primitive_basis_word` | 平方基 diagonal root 生成的 primitive basis word。 |
| `signed_coefficient_value` | 该 diagonal root 的 signed coefficient 正向值。 |
| `orientation_local_factor` | orientation parity、local factor、截断因子和非零条件。 |
| `alpha_delta_branch_exactuv` | alpha/delta side、branch key 和 exact `(u,v)` 输出。 |
| `prepushforward_identity` | 证明 root 声明在推前前已经等于目标 signed 贡献。 |
| `prime_row_leak_guard` | 证明没有把 prime row `p` 或 virtual `(p,1)` 当成 composite signed source。 |
| `return_tag` | 声明缺失、local factor 为零、符号冲突或后验依赖时的命名回流。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| UnitSeedTargetImported | `true` | `false` | 上一层已把 signed transport 启动压到 virtual-unit 或 square-base signed coefficient。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| VirtualUnitNotCompositeSupport | `true` | `true` | `(p,1)` 对应 prime row `p`，不在 composite support 中，不能独立携带 composite signed coefficient。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| SquareBaseIsMinimalSupportRoot | `true` | `true` | 每个 LPF owner bucket 的最小真实 support cofactor 是 `m=p`，即 diagonal root `(p,p)`。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| NoSupportPredecessorBelowSquareBase | `true` | `true` | `(p,p)` 没有更小的 composite support predecessor；唯一 predecessor 是 virtual `(p,1)`。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| VirtualSeedCollapsesToSquareBaseDeclaration | `true` | `true` | 合法 virtual seed 若存在，必须作为 square-base root 的声明前像出现，不能作为独立 signed row。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| SourceDeclarationPacketStillOpen | `false` | `false` | common pre-Cauchy source declaration packet 仍未证明；square-base root 也必须满足该 packet。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| BuiltInPairingStillOpen | `false` | `false` | source packet 下游仍缺 atomic row 的 built-in word/coefficient pairing 闭式。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| PrimitiveSummandExpressionStillOpen | `true` | `false` | primitive summand signed expression 未证明，不能自动给 diagonal root signed coefficient。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| PointwiseBucketValueTableStillOpen | `true` | `false` | 直接提交整个 Phi-LPF support 的 pointwise signed value table 仍未完成。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| SquareBaseDiagonalSourceDeclarationCurrentCorpusProved | `false` | `false` | 当前材料没有提交 `(p,p)` diagonal root 的同源 basis word/signed coefficient source declaration。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| UnitSeedCurrentCorpusProved | `false` | `false` | virtual-unit 口径已归约到 square-base declaration；该 declaration 未证明，unit seed 仍未闭合。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步没有证明 signed coefficient law、step update、ordered coherence、ExactUV fixed-key 或三命题无条件闭合。 | PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward |

## 5. 下一真正单点

```text
PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward
```

等价并行入口：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_square_base_diagonal_source_router.py` | `f6830252ae34b9a29bbccb230bca817decde5688c1c7aca76a05ae4392ad4faf` |
| `docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.json` | `ae2cac674830906635ecbf85c8105659d16d70ef0592a9fd817eb625d4d51fcb` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json` | `d9e042ffccaaf050e72788abdb0a10a5776a3cb4d8a37fc949c9710a4a832f44` |
| `docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json` | `6f2a1790c735dacb3d3c3104dd6ae6469abe97a23853e073a57fb4990e4bf769` |
| `docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json` | `b0b1264cf6f3fbad60724a440f0dc9872dbc577376ed466e5dcac0cf66caa5ff` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-value-table-router.json` | `c44a6e986d59cd068f19cdb58427f779721bb1cf984ff1edb4d67be28cb6dc8c` |
