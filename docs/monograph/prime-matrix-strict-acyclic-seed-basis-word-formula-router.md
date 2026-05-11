# Prime Matrix strict acyclic seed basis word formula 路由器

**状态：** `basis_word_formula_reduced_to_word_coordinate_formula_open`

本步把 basis_word_formula 再压到 word_coordinate_formula。参数和锚可以复算，但当前材料没有把这些参数映射为 primitive basis word 坐标；unsigned row 坐标、signed lift、alpha/delta rule 和后验反推都不能替代该公式。

```text
basis_word_formula_router_closed=true
parameter_domain_closed=true
word_coordinate_formula_proved=false
basis_word_formula_from_source_tuple_parameters_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility` 已有参数域，真正首缺口是 `AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters`：必须把 A、D0/K/Omega、phase_rule 等 source tuple 参数转成 primitive basis word 的坐标向量。

## 2. word_coordinate_formula 字段

| field | meaning |
| --- | --- |
| `anchor_input_rule` | 明确从 A、窗口端点和 phase_rule 选取哪些锚参数作为坐标输入。 |
| `dyadic_truncation_coordinate` | 把 D0、K、Omega 转成 basis word 的 dyadic/truncation 坐标。 |
| `phase_coordinate` | 把 phase_rule 转成 word 的相位坐标，而不是只给 unsigned row phase。 |
| `signed_weight_coordinate_slot` | 为后续 coefficient assignment 预留 signed weight/local factor 槽位。 |
| `coordinate_nonposthoc_certificate` | 证明坐标公式不读取 payment、零行覆盖、推前后投影或 terminal 数据。 |
| `coordinate_failure_return` | 坐标未定义、冲突、多值或超预算时的命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BasisWordFormulaTargetActive` | `true` | `false` | 上一层已把 source tuple 到 word constructor 压到 basis_word_formula。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `ParameterDomainClosed` | `true` | `true` | source tuple 参数域已经锁定；A、D0/K/Omega、phase_rule 和 hash 可读取。 | 参数域不是当前首缺口。 |
| `WordCoordinateFormulaIsFirstOpenField` | `true` | `true` | 有参数域还不够，必须先给出把参数转成 primitive basis word 坐标的公式。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `AnchorReconstructionDoesNotEmitWordCoordinates` | `true` | `false` | anchor reconstruction 可复算 A 与参数，但不输出 basis word coordinate vector。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `SourceLawRequiresFormulaButDoesNotProvideIt` | `true` | `false` | source law 说明需要来源公式；它本身不是 coordinate formula。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `UnsignedSkeletonGivesRowCoordinatesOnly` | `true` | `false` | unsigned skeleton 给 carry-shell row/phase 几何坐标，不给 primitive basis word 的算术坐标和 signed 槽位。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `SignedWeightSlotStillOpen` | `true` | `false` | signed coefficient lift 与 local factor 仍未闭合，因此不能把 signed 槽位后验补入 formula。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `ActualCoordinateFormulaCurrentCorpusMissing` | `true` | `false` | 当前材料没有 actual noncanonical primitive constructor formula，也没有独立 word coordinate formula。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `PosthocCoordinateRecoveryBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖恢复坐标公式。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `WordCoordinateFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有提交从 A、D0/K/Omega、phase_rule 到 primitive basis word 坐标的公式。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `BasisWordFormulaCurrentCorpusProved` | `false` | `false` | 没有 coordinate formula，arithmetic weight slot、非后验证书和失败回流仍不能合取证明。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |

## 4. 下一真正单点

```text
AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters
```

并行依赖：

```text
AcyclicSeedSignedWeightCoordinateSlotLedger
AcyclicSeedCoordinateNonposthocCertificateLedger
AcyclicSeedCoordinateFailureReturnLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
