# Prime Matrix Phi-LPF signed transport unit-seed 证书

**状态：** `phi_lpf_signed_transport_reduced_to_unit_seed_open`

Phi 计数公式中的 `-1` 是 signed transport 的关键边界：`m=1` 被从 composite support 中排除，但 rough cofactor 乘法分支又必须从 `m'=1` 生成平方基 key `(p,p)`。因此递推 signed transport 不能从 Phi 计数自动启动；它首先需要 virtual-unit seed 或 square-base signed coefficient，并明确禁止把 prime row `p` 偷换成 composite signed seed。最新硬点压成 `PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward`。

```text
phi_minus_one_prime_row_guard_imported=true
unit_preimage_square_seed_identity_proved=true
unit_seed_or_square_base_signed_coefficient_proved=false
rough_cofactor_step_local_factor_update_law_proved=false
rough_cofactor_ordered_factorization_coherence_proved=false
phi_lpf_rough_cofactor_signed_transport_law_proved=false
row_column_unconditional_closed=false
```

## 1. unit seed 边界

Phi 桶计数中 `m=1` 被减掉，因为它对应 prime row `p`。但 signed transport 的整除分支需要
`m'=1 -> m=p` 来生成 composite `p^2` 的第一个真实 signed key。因此 transport 必须显式给出
virtual-unit seed 或 square-base coefficient，不能从 prime row 后验偷渡。

## 2. 样本 seed 审计

| N | support keys | square-base seeds | non-square keys | seed fraction | seed identity |
| ---: | ---: | ---: | ---: | ---: | --- |
| 30 | 19 | 3 | 16 | 0.15789474 | `true` |
| 100 | 74 | 4 | 70 | 0.05405405 | `true` |
| 997 | 828 | 11 | 817 | 0.01328502 | `true` |
| 5003 | 4332 | 19 | 4313 | 0.00438596 | `true` |
| 10000 | 8770 | 25 | 8745 | 0.00285063 | `true` |

## 3. seed 字段

| field | meaning |
| --- | --- |
| `owner_bucket_prime` | LPF owner prime `p`。 |
| `virtual_unit_cofactor` | Phi 递推中的 `m'=1`，它不是 composite support row。 |
| `square_base_key` | unit preimage 传输后得到的真实 composite key `(p,p)`，即 `p^2`。 |
| `square_base_signed_coefficient` | 对 `p^2` 的 Cauchy 前 signed coefficient 正向赋值。 |
| `prime_row_leak_guard` | 不得把被 LPF 计数公式减掉的 prime row `p` 当作 signed composite seed。 |
| `orientation_local_factor_base` | 平方基入口的 orientation、local factor、非零条件和 return tag。 |
| `transport_bootstrap_identity` | 证明后续 cofactor transport 从该平方基入口启动，而非从后验 payment 读取。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SignedTransportTargetImported | `true` | `false` | 上一层已把 Phi-LPF signed law 压到 rough cofactor multiplication signed transport。 | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward |
| PhiMinusOnePrimeRowGuardImported | `true` | `true` | `Phi(floor(N/p),p)-1` 中减掉的 `m=1` 是 prime row `p`，不是 composite support。 | prime row cannot seed signed composite coefficient |
| UnitPreimageReentersTransportAsSquareBase | `true` | `true` | signed transport 的整除分支含 `m'=1`，它映到真实 composite key `(p,p)` 即 `p^2`。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| SupportBijectionConfirmsSquareBaseKeys | `true` | `true` | 平方基 key 是 Phi-LPF support 的合法起点，但 unit cofactor 本身不是 support key。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| TransportCannotStartWithoutSeed | `true` | `true` | 若没有 virtual-unit 或 square-base signed coefficient，递推传输无法给出 `a_p(p)`。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| PrimeRowLeakBlocked | `true` | `true` | 不能把计数公式中被减掉的 prime `p` 的状态偷换成 composite coefficient seed。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| StepUpdateAndCoherenceRemainAfterSeed | `true` | `false` | 即使平方基入口给定，后续仍需每个 rough prime step 的 local factor 更新和有序分解一致性。 | PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward |
| PointwiseSignedValueTableAlternativeStillOpen | `true` | `false` | 直接提交 Phi-LPF bucket 逐点 signed value table 仍是等价并行入口，但当前未给出。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| PrimitiveSignedExpressionStillOpen | `true` | `false` | primitive summand signed expression 未证明，因此平方基 signed coefficient 也未由现有语料产生。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| UnitSeedCurrentCorpusProved | `false` | `false` | 当前材料没有提交 virtual-unit/square-base signed coefficient 与 prime-row leak guard 的正向证书。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward |
| SignedTransportCurrentCorpusProved | `false` | `false` | 缺少平方基 seed，rough cofactor signed transport law 尚未证明。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步没有证明 signed coefficient law、ExactUV fixed-key、终端排斥或三命题无条件闭合。 | PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |

## 5. 下一真正单点

```text
PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward
```

等价并行入口：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_signed_transport_unit_seed_router.py` | `54765686bd126a528902d9d1799b4db99e9eb2db8e87b42de4246af5aa78ff83` |
| `docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json` | `8f696d3cb025e8d98790530763d5b87717c945b57c310f6d16f4c49711c8fdcb` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-value-table-router.json` | `c44a6e986d59cd068f19cdb58427f779721bb1cf984ff1edb4d67be28cb6dc8c` |
| `docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json` | `b0b1264cf6f3fbad60724a440f0dc9872dbc577376ed466e5dcac0cf66caa5ff` |
