# Prime Matrix actual 容量账本微原子路由器

**状态：** `actual_capacity_ledger_microatom_boundary_closed_core_open`

最窄自足源核心继续收紧：`支撑宽` 不是充分条件，必须同时证明所有 Type/Fourier/fiber 容量乘子已在同一 formal unit 账本中登记且不会让单个 moving `(u,v)` 对额外放大。因此最新单原子是 `ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS`；可行证明包是 `ActualNoncanonicalExactUVSupportLowerBound` 加 `ActualTypeFourierRegisteredCapacityMultiplierDiscipline`。当前二者仍未证明，DStructure/Rankin 晋级验收也仍独立开放。

```text
microatom_boundary_closed=true
support_only_suffices=false
registered_multiplier_discipline_would_suffice_with_support=true
exact_uv_support_proved=false
registered_multiplier_discipline_proved=false
actual_final_capacity_antiatom_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 微原子判定表

| gate | boundary closed | proved | meaning | consequence |
| --- | --- | --- | --- | --- |
| `PreviousActualSupportCapacityCorePinned` | `true` | `false` | 上一层已把完全自足源核心压到 actual noncanonical 支撑/容量合同。 | 可继续检查该合同内部是否还有支撑与容量口径偷换。 |
| `SupportOnlyDoesNotImplyAntiAtom` | `true` | `false` | 存在支撑很宽但单个 moving pair 获得隐藏容量乘子的模型。 | 不能把 exact u/v 支撑下界单独当作 source anti-atom 证明。 |
| `RegisteredMultiplierDisciplineWouldRestoreImplication` | `true` | `false` | 若所有 Type/Fourier/fiber 乘子都登记进同一 formal unit 且至多多对数损失，则支撑下界可推出最终容量反原子。 | 证明路线应写成 exact 支撑下界 + 已登记容量乘子纪律。 |
| `ExactUVSupportStillOpen` | `true` | `false` | 当前 ledger 尚无 actual noncanonical exact u/v 支撑下界。 | 该支撑下界仍是一个真实微输入，不能由 K4/K6 或朴素 incidence 免费推出。 |
| `TypeFourierMultiplierDisciplineStillOpen` | `true` | `false` | Type/Fourier capacity compatibility 仍未作为同一 actual formal unit 乘子账本证明。 | 未登记乘子必须被证明不存在，或直接在最终 M_{u,v} 容量测度上证明无大原子。 |
| `FinalCapacityMeasureIsSharpStatement` | `true` | `false` | 把所有已登记 Type/Fourier/fiber 成本吸收到最终 M_{u,v} 后，最锐利命题就是 max M_{u,v}/sum M <= log^{-2A}。 | 最新单原子应表述为 actual final capacity anti-atom ledger，而不是 raw support-only lemma。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 即使源容量微原子完成，也还需要独立验收才能升级为完整行/列定理。 |

## 2. 上一层输入基

```text
ActualNoncanonicalFullSFactorSupportCapacityTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 最新单原子输入基

```text
ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 可行证明包

```text
ActualNoncanonicalExactUVSupportLowerBound AND ActualTypeFourierRegisteredCapacityMultiplierDiscipline
```

## 5. 条件不等式

若 |alpha_u|,|delta_v| <= L^C，登记乘子 W_{u,v} <= L^E，且 S_u*S_v >= L^(2A+4C+E)，则 max M_{u,v}/sum M_{u,v} <= L^(-2A)。

## 6. 支撑-only 阻断律

raw u/v 支撑下界只控制有多少 factor pair；若 Type/Fourier/fiber 阶段允许某个 moving pair 获得未登记容量乘子，则最终 M_{u,v} 仍可集中。

| k | log y | required share | support pairs | hidden multiplier | top capacity share | support broad | antiatom violated |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 3 | 6.90776 | 0.00043919 | 750514 | 563271264196 | 0.999999 | `True` | `True` |
| 4 | 9.21034 | 0.000138962 | 5622504 | 31612551230016 | 1 | `True` | `True` |
| 5 | 11.5129 | 5.6919e-05 | 26810188 | 718786180595344 | 1 | `True` | `True` |
| 6 | 13.8155 | 2.74494e-05 | 96065750 | 9228628323062500 | 1 | `True` | `True` |
| 7 | 16.1181 | 1.48165e-05 | 282615581 | 79871566623967561 | 1 | `True` | `True` |
| 8 | 18.4207 | 8.68515e-06 | 719680491 | 517940009126001081 | 1 | `True` | `True` |
| 9 | 20.7233 | 5.4221e-06 | 1641373385 | 2694106588986358225 | 1 | `True` | `True` |

## 7. 结构律

ActualNoncanonicalFullSFactorSupportCapacityTheoremInput 的最锐利表述应是最终 actual 容量测度 M_{u,v} 的反原子账本。证明它可以走两步：exact u/v 支撑下界加 registered Type/Fourier capacity multiplier discipline。当前材料二者都没有完成；但支撑-only 偷换已被阻断，且条件蕴含公式已固定。

## 8. 当前结论

这一步闭合的是支撑与容量口径的边界：raw factor support 不能单独替代最终 source anti-atom。
完整自足路线现在必须直接证明 final capacity anti-atom ledger，或证明 exact 支撑下界加已登记乘子纪律。
当前材料尚未证明这些微原子，也未完成 DStructure/Rankin 独立验收。
