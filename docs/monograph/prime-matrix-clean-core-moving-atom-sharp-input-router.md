# Prime Matrix clean-core moving atom 精确输入路由器

**状态：** `clean_core_moving_atom_sharp_input_pinned_open`

最新最窄剩余从 clean-core 低支撑 packet 排斥校准为 clean-core moving atom 排斥。这更贴近最终容量反原子目标：低支撑但不造成容量集中的 packet 不必作为终局障碍；必须排斥的是通过所有回流测试后仍承载最终 M_{u,v} 大原子的 actual moving block。当前材料尚未证明该 sharp 输入。

```text
clean_core_moving_atom_sharp_boundary_closed=true
clean_core_moving_atom_exclusion_proved=false
actual_final_capacity_antiatom_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CleanCorePacketFrontierPinned` | `true` | `true` | 上一层已把非 clean-core 的支撑失败 packet 全部回流到命名出口。 | 只需处理通过全部回流测试的 clean-core 残余。 |
| `RegisteredMultiplierDisciplineAvailable` | `true` | `true` | Type/Fourier/fiber 乘子已登记为同一 formal unit 的 log-power 成本。 | 最终容量大原子若存在，不能归因于账外乘子。 |
| `CapacityAtomImpliesSupportFailurePacket` | `true` | `true` | 由已登记乘子条件不等式的逆否命题，final M_{u,v} 大原子会产生低于阈值的 exact u/v 支撑失败 packet。 | 该逆否只定位 witness，不证明 witness 不存在。 |
| `SupportPacketExclusionIsSufficientButOverstrong` | `true` | `true` | 排斥所有 clean-core 低支撑 packet 足以闭合，但比最终目标更强；最终只需排斥会产生容量大原子的 packet。 | 把源侧输入改写为 clean-core moving atom exclusion。 |
| `SharpMovingAtomInputPinned` | `true` | `true` | 最终 sharp 源侧命题是 clean-core 最终容量测度无 moving same-(u,v) 大原子。 | 证明该 actual clean-core anti-atom。 |
| `FormalTemplateNoGoRetained` | `true` | `true` | formal WFD/Type/Fourier 与固定投影仍不能推出 moving-block entropy；moving-delta 阻断保留。 | 不能把 sharp 输入偷换成 generic WFD 引理。 |
| `CleanCoreMovingAtomExclusionCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 actual noncanonical clean-core moving atom exclusion。 | 证明 ActualNoncanonicalCleanCoreMovingAtomExclusion，或接受精确 FullS KLS 外部输入。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧 sharp 输入完成后仍需独立验收。 |

## 2. sharp 输入律

clean-core 支撑失败 packet 排斥是足够条件，但不是最终 sharp 目标。在 registered multiplier discipline 已闭合后，final capacity 大原子的逆否会给出支撑失败 packet；因此最终源侧 sharp 输入是排斥 clean-core final capacity measure 的 moving same-(u,v) 大原子。

## 3. moving atom 定义

ActualNoncanonicalCleanCoreMovingAtom 是一个通过所有回流测试的正质量 actual noncanonical full-S non-AP balanced block 中的 pair (u,v)，其最终登记容量 M_{u,v}/sum M_{u,v} 超过所需 log^{-2A} 阈值。

## 4. 最新输入基

上一层源侧微输入：

```text
ActualNoncanonicalCleanCoreSupportFailurePacketExclusion
```

当前 sharp 源侧微输入：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
```

连同独立晋级门：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 阈值样本

| k | log y | atom share threshold | support threshold | required pair support |
| ---: | ---: | --- | --- | ---: |
| 3 | 6.90776 | `L^(-2A)` | `L^17` | 185664143359702 |
| 4 | 9.21034 | `L^(-2A)` | `L^17` | 24699408928878996 |
| 5 | 11.5129 | `L^(-2A)` | `L^17` | 1096874099498946944 |
| 6 | 13.8155 | `L^(-2A)` | `L^17` | 24335370598442758144 |
| 7 | 16.1181 | `L^(-2A)` | `L^17` | 334451684862452432896 |
| 8 | 18.4207 | `L^(-2A)` | `L^17` | 3237400927126027763712 |
| 9 | 20.7233 | `L^(-2A)` | `L^17` | 23976697736727197908992 |

## 6. 阻断律

该 sharp 输入不能由 formal WFD、Type 分解、Fourier 平滑或固定投影 diffuse 免费推出；moving-delta 模型仍可在每个尺度选择新的 (u,v) 标签集中。

## 7. 当前结论

本步没有证明 `ActualNoncanonicalCleanCoreMovingAtomExclusion`；它关闭的是输入口径：
从过强的 low-support packet 排斥改为最终容量反原子所需的 sharp moving-atom 排斥。
