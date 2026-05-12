# Prime Matrix strict 中段有限区间 psi 覆盖路由器

**状态：** `middle_interval_point_values_good_sparse_monotonic_cover_fails_increment_or_fine_mesh_open`

中段点值本身很强，但不能形成整段证明。Table 6.2 在几个节点的 psi/x 均低于目标，可是只用 psi 单调性和下一稀疏节点值会严重失败；点间最大值必须由短区间增量上界或精细网格加跳点证书控制。因此最新最窄点变为 `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger`。

```text
middle_finite_interval_psi_cover_closed=false
table62_point_values_below_target=true
sparse_point_monotonicity_cover_fails=true
trivial_jump_envelope_requires_fine_mesh=true
certified_short_interval_psi_increment_upper_closed=false
middle_psi_fine_mesh_computation_hash_closed=false
prime_power_jump_control_closed=false
middle_psi_upper_directed_rounding_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 点值余量

| x | psi | psi/x | absolute_slack | beats_target |
| ---: | ---: | ---: | ---: | --- |
| `8.000000000000000e+11` | `8.000000379792747e+11` | `1.000000047474093e+00` | `2.269002072546387e+07` | `true` |
| `9.000000000000000e+11` | `8.999997772318761e+11` | `9.999997524798623e-01` | `2.579176812402344e+07` | `true` |
| `1.000000000000000e+12` | `1.000000040136765e+12` | `1.000000040136765e+00` | `2.836986323474121e+07` | `true` |
| `2.000000000000000e+12` | `2.000000182627336e+12` | `1.000000091313668e+00` | `5.663737266430664e+07` | `true` |

## 2. 稀疏单调覆盖失败

| interval | bound | defect | sufficient |
| --- | ---: | ---: | --- |
| `[800000000000, 900000000000]` | `1.124999721539845e+00` | `1.249713115398450e-01` | `false` |
| `[900000000000, 1000000000000]` | `1.111111155707517e+00` | `1.110827457075170e-01` | `false` |
| `[1000000000000, 1446257064291]` | `2.000000182627336e+00` | `9.999717726273358e-01` | `false` |

## 3. 粗跳跃网格压力

| x | point_slack | max_mesh_under_trivial_integer_weight | meaning |
| ---: | ---: | ---: | --- |
| `8.000000000000000e+11` | `2.269002072546387e+07` | `8.103578830522810e+05` | trivial jump envelope would require very fine certified mesh; sparse 1e11 grid cannot work |
| `9.000000000000000e+11` | `2.579176812402344e+07` | `9.211345758579799e+05` | trivial jump envelope would require very fine certified mesh; sparse 1e11 grid cannot work |
| `1.000000000000000e+12` | `2.836986323474121e+07` | `1.013209401240758e+06` | trivial jump envelope would require very fine certified mesh; sparse 1e11 grid cannot work |

## 4. 自足替换

```text
MiddleFiniteIntervalPsiCover8e11ToE28Ledger
  =>
CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger OR (MiddlePsiFineMeshComputationAndHashLedger AND PrimePowerJumpLocalizationOrUpperEnvelopeLedger AND MiddlePsiUpperDirectedRoundingLedger)

CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger
  =>
explicit upper envelope for psi increments on a certified partition of [8e11,e^28]

```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计假设反例链可调用的中段有限 psi 覆盖，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `MiddleFiniteIntervalPsiCoverGateActive` | `true` | `true` | 上一层已把 1.00002841 的来源缺口压成 8e11 到 e^28 的有限区间覆盖。 | MiddleFiniteIntervalPsiCover8e11ToE28Ledger |
| `DusartTable62PointValuesLedger` | `true` | `true` | Table 6.2 点值在 8e11、9e11、1e12、2e12 均低于 1.00002841，且绝对余量为千万级。 | point values only; interval cover still open |
| `SparsePointMonotonicityCoverFails` | `true` | `true` | 只用 psi 单调性和下一稀疏点值会得到过大的右点/左端上界，不能覆盖点间。 | CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger OR MiddlePsiFineMeshComputationAndHashLedger |
| `TrivialJumpEnvelopeRequiresFineMesh` | `true` | `true` | 若只用每个整数贡献不超过 log x 的极粗跳跃包络，千万级余量要求约百万级网格，1e11 稀疏网格远远不够。 | MiddlePsiFineMeshComputationAndHashLedger AND PrimePowerJumpLocalizationOrUpperEnvelopeLedger |
| `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger` | `false` | `false` | 需要对每个子区间证明 psi(y)-psi(x) <= 1.00002841*y - psi(x) 的短区间上界。 | short interval explicit upper envelope for psi increments |
| `MiddlePsiFineMeshComputationAndHashLedger` | `false` | `false` | 需要机器可读的中段精细网格、每块端点 psi 值、最大跳点包络和 hash。 | fine mesh computation archive |
| `PrimePowerJumpLocalizationOrUpperEnvelopeLedger` | `false` | `false` | 需要定位或上界每个网格块中的素数幂跳跃，防止点间最大值逃逸。 | prime and prime-power jump certificate |
| `MiddlePsiUpperDirectedRoundingLedger` | `false` | `false` | 需要证明 1.00002841 是对整段最大值的外向上舍入，而非仅对少数点值的舍入。 | directed rounding for interval supremum |
| `MiddleFiniteIntervalPsiCover8e11ToE28Ledger` | `false` | `false` | 当前完成点值压力和失败模式审计；整段中段 psi 覆盖尚未自足闭合。 | CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger OR (MiddlePsiFineMeshComputationAndHashLedger AND PrimePowerJumpLocalizationOrUpperEnvelopeLedger AND MiddlePsiUpperDirectedRoundingLedger) |
| `RowColumnUnconditionalClosed` | `false` | `false` | 中段有限区间 psi 覆盖审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一最窄点

```text
CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger
```
