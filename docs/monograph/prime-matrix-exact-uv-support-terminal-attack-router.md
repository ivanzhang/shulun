# Prime Matrix ExactUVSupport 终端攻击路由器

**状态：** `exact_uv_support_is_unique_source_terminal_input_open`

ExactUVSupport 被攻到当前材料的唯一源侧终端输入：乘子纪律已闭合，canonical 分支支撑链已经吸收，但不能导入 noncanonical full-S 补集；generic WFD 点支撑模型阻断形式推论。因此当前不能诚实宣称完整无条件闭合。剩余是新增证明 `ActualNoncanonicalExactUVSupportLowerBound`，或直接证明最终容量反原子；另有 DStructure/Rankin 独立验收门。

```text
exact_uv_support_terminal_boundary_closed=true
registered_capacity_multiplier_discipline_closed=true
exact_uv_support_proved=false
actual_final_capacity_antiatom_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RegisteredMultiplierDisciplineClosed` | `true` | `true` | 上一轮已把 Type/Fourier/fiber 乘子纪律闭合为账本门。 | ExactUVSupport 不再能把失败归因于账外乘子。 |
| `CanonicalImportBlocked` | `true` | `true` | canonical RIW/Buchstab 支撑不能偷渡到 noncanonical full-S 补集。 | 必须证明 actual noncanonical 支撑，或直接证明 final anti-atom。 |
| `K4K6AndNaiveIncidenceStillInsufficient` | `true` | `true` | K4/K6 与朴素 factor-residue incidence 不能推出 moving u/v 支撑。 | 支撑失败不会自动回流为已命名 K4/K6 失败。 |
| `CanonicalSupportChainNotARecentOpenGap` | `true` | `true` | canonical-source 分支上的层准入/非零转移/薄块回流已由 canonical 边界吸收。 | 这只关闭 canonical 分支；不关闭 actual noncanonical 补集。 |
| `RawBuchstabCountingNotEnoughForNoncanonical` | `true` | `true` | 厚区间 squarefree 数量够，但 exact 层承认和非零系数转移只服务已锁定的 canonical 层。 | noncanonical actual 源仍需自己的支撑下界或 final anti-atom。 |
| `ExactUVSupportCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 actual noncanonical exact u/v 支撑下界。 | 这是唯一源侧终端输入。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 即使 ExactUVSupport 完成，仍需独立验收。 |

## 2. 最新输入基

```text
ActualNoncanonicalExactUVSupportLowerBound AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 条件闭合律

在 registered multiplier discipline 已闭合后，若证明 ActualNoncanonicalExactUVSupportLowerBound，则 final capacity anti-atom ledger 随条件不等式成立；再加 DStructure/Rankin 独立验收，当前边界链才可升级。

## 4. 阻断律

ExactUVSupport 不能由 formal WFD、K4/K6、朴素 incidence、raw Buchstab 计数或 canonical 支撑链偷渡推出。generic WFD 允许点支撑因子；canonical 支撑只关闭 canonical-source 分支。

| k | log y | formal factor support | required support | passes WFD template | violates ExactUVSupport |
| ---: | ---: | ---: | ---: | --- | --- |
| 3 | 6.90776 | 1 | 750514 | `True` | `True` |
| 4 | 9.21034 | 1 | 5622504 | `True` | `True` |
| 5 | 11.5129 | 1 | 26810188 | `True` | `True` |
| 6 | 13.8155 | 1 | 96065750 | `True` | `True` |
| 7 | 16.1181 | 1 | 282615581 | `True` | `True` |
| 8 | 18.4207 | 1 | 719680491 | `True` | `True` |
| 9 | 20.7233 | 1 | 1641373385 | `True` | `True` |

## 5. 当前结论

本步没有证明 `ExactUVSupport`；它闭合的是边界审查：现有伪出口均不能推出该输入。
当前唯一源侧终端输入是 `ActualNoncanonicalExactUVSupportLowerBound`。
完整行/列命题还需要该输入或直接 final anti-atom 证明，并需要 DStructure/Rankin 独立验收。
