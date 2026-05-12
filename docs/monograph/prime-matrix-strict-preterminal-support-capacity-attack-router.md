# Prime Matrix strict pre-terminal 支撑/容量直攻路由器

**状态：** `strict_preterminal_support_capacity_reduced_to_nonterminal_exact_uv_fiber_aperiodicity_open`

`PreTerminalActualFullSFactorSupportCapacityTheorem` 继续被压缩：容量侧和初等支撑推理已闭合，终端回流路线被排除，CRT/轮筛刚性只能控制允许位置而不控制 fiber 质量。因此最新严格自足最窄点是 `NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource`。该估计尚未证明，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
preterminal_support_capacity_attack_closed=true
registered_capacity_multiplier_discipline_imported=true
terminal_exactuv_routes_rejected_as_nonterminal_proof=true
crt_wheel_rigidity_controls_positions_not_fiber_mass=true
nonterminal_exact_uv_fiber_aperiodicity_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 压缩

压缩前：

```text
PreTerminalActualFullSFactorSupportCapacityTheorem
```

压缩后：

```text
NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
```

fiber 非集中合同：

```text
For the actual sign-refined pre-Cauchy source in one formal unit, prove max_{(u,v)} M_{u,v} <= M / L^K, or equivalently an L2 energy bound sum M_{u,v}^2 <= M^2 / L^K, uniformly at the log-power needed for every A.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreTerminalSupportCapacityTargetActive` | `true` | `false` | 上一层已把独立非终端 source entropy 原子化为 pre-terminal actual full-S 支撑/容量定理。 | PreTerminalActualFullSFactorSupportCapacityTheorem |
| `RegisteredCapacityMultiplierDisciplineImported` | `true` | `true` | Type/Fourier/fiber 成本已登记到同一 formal unit，容量侧不再是活动障碍。 | ActualNoncanonicalExactUVSupportLowerBound。 |
| `SupportOnlyPitfallAlreadyRemoved` | `true` | `true` | raw 支撑宽度不能单独证明反原子；但登记乘子纪律已恢复支撑到容量的条件蕴含。 | exact u/v support lower bound。 |
| `ElementaryMassSupportLemmaImported` | `true` | `true` | 若 exact pair 最大质量或 L2 能量界成立，则 pair 支撑和 S_u*S_v 下界由初等引理推出。 | exact pair mass dispersion。 |
| `OldExactUVTerminalRouteRejected` | `true` | `true` | 通过 support failure packet、moving-block return 或 terminal 三原子证明 ExactUV 会回到固定点，不能作为非终端证明。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| `SourceSeedObjectDisciplinePinned` | `true` | `false` | 估计必须作用于 Cauchy/dispersion 前已声明的 actual source；不能从终端覆盖图反推对象。 | ActualPreCauchySourceObjectLedgerForThisEstimate。 |
| `QuantitativeCorePinned` | `true` | `false` | 在容量已登记后，真正数值负担是 pre-terminal exact (u,v) 纤维的最大原子/L2 非集中估计。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| `CRTWheelRigidityInsufficientForFiberMass` | `true` | `true` | CRT/轮筛/层叠筛给允许残基与禁止类结构，不控制 actual signed source 在某个 exact pair fiber 内的质量分配。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| `NonterminalFiberAperiodicityCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出不使用终端回流的 exact fiber 非集中估计。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |

## 3. 结构结论

容量乘子纪律已经关闭，支撑到容量的初等蕴含已经关闭；pre-terminal 支撑/容量定理的唯一数值核心是 exact (u,v) fiber 非集中。CRT/轮筛刚性只给位置结构，不能给 signed source 质量分散；通过终端 packet 回流证明则回到固定点，不能用于非终端证明。

## 4. 下一主攻点

```text
NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
```
