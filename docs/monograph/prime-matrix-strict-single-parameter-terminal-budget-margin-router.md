# Prime Matrix strict 单参数终端预算正余量路由器

**状态：** `single_parameter_margin_normal_form_closed_positive_margin_not_proved`

单参数终端预算正余量已被严格固定为 D_prefix-E_named-U_cold>0。现有材料关闭了标准形、终端无静默塌缩和冷供给调参纪律；连续 beta 主项已闭合，B3/TV 有外部条件路线。但当前没有证明同参数显式正余量：离散 B3 误差、有限 prefix 证书、命名回流排斥、热核心/固定历史出口与 DStructure/Rankin 晋级仍未全部完成。因此还不能声明反例链与真实链产生无条件终端矛盾。

```text
single_parameter_margin_normal_form_closed=true
continuous_beta_demand_closed=true
external_b3_tv_lane_available=true
strict_prefix_demand_proved=false
terminal_no_silent_collapse_closed=true
cold_supply_same_parameter_discipline_closed=true
named_return_exclusion_proved=false
explicit_positive_terminal_budget_margin_proved=false
unified_terminal_budget_strict_inequality_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 终端余量

唯一可闭合口是同参数不等式：

```text
D_prefix - E_named - U_cold > 0.
```

其中所有项必须使用同一个 `z,D,Lambda,T_PDEC` 账本。

## 2. 公式槽位

| slot | formula | needed | status |
| --- | --- | --- | --- |
| `prefix demand` | D_prefix=((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z) | explicit lower bound D_prefix >= D0(P,z)>0 | open: rough count/finite boundary not fully proved |
| `terminal projection` | L_forced>=D_prefix-E_named | no silent collapse and bounded named returns | no-silent-collapse closed; named exclusion open |
| `cold supply` | U_cold<=sum_W (T_PDEC(W)-1)C_core(W) | explicit same-parameter upper bound U_cold<=U0(P,z) | envelope and lambda discipline closed; numeric dominance open |
| `strict margin` | D0(P,z)-E0(P,z)-U0(P,z)>0 | one signed inequality under one parameter ledger | not proved in current corpus |

## 3. 阻塞点

| obstruction | closed | why_it_matters | effect_on_margin |
| --- | --- | --- | --- |
| `B3DiscretePrimeSumUniformErrorPGe100000` | `false` | 连续 beta 主项有 1% 余量，但离散素和误差未内联证明。 | D_prefix 不能升级为严格自足显式 D0。 |
| `B3RemainderTotalVariationBudgetForLengthP` | `false` | 外部 Mertens/Dusart 可条件关闭 TV；严格自足尾段仍开放。 | TV(lambda^-) 的自足扣除项未定。 |
| `FiniteBoundaryPrefixRoughCountCertificate` | `false` | 显式常数路线留下有限 P 段；没有证书就不能宣称全局。 | D0(P,z)>0 不能覆盖所有 P。 |
| `NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` | `false` | E_named 目前被压缩但未排斥；它可吞掉正余量。 | 无法证明 D_prefix-E_named 仍为正。 |
| `ColdPositiveDominance` | `false` | 冷供给有上界公式，但还没有同参数数值反超 D_prefix-E_named。 | 无法证明 D_prefix-E_named-U_cold>0。 |

## 4. 定理边界

| name | proved | statement | role |
| --- | --- | --- | --- |
| `SingleParameterMarginNormalForm` | `true` | 早期零行反例链的终端矛盾等价于同参数正余量 D_prefix-E_named-U_cold>0。 | 这是必要且充分的终端供需闭合口。 |
| `NoConditionalInputPromotion` | `true` | 外部 B3/TV 条件、命名回流压缩、冷供给纪律不能自动合成为无条件正余量。 | 防止把条件接口误认为最终证明。 |
| `TerminalContradictionCurrentCorpus` | `false` | 当前语料尚未证明 D_prefix-E_named-U_cold>0。 | 行/列命题仍未作者侧无条件闭合。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍只在 Assume EarlyZeroRowWithinP 的反例链内比较终端需求与供给。 | 保持 row_column_unconditional_closed=false。 |
| `MarginNormalFormClosed` | `true` | `true` | 终局矛盾已固定为 D_prefix-E_named-U_cold>0。 | ExplicitPositiveTerminalBudgetMarginInequality |
| `ContinuousBetaDemandClosed` | `true` | `true` | alpha=0.43 的连续线性下界筛主项余量已闭合。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| `ExternalB3TVLaneAvailable` | `true` | `false` | 接受外部 Mertens/Dusart 时，B3/TV 需求链有条件可用；严格自足仍缺尾段。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| `StrictPrefixDemandProved` | `false` | `false` | 当前尚未完成统一 prefix 粗筛余下界和有限边界证书。 | NormalizedPrefixResidualPotentialLowerBound AND FiniteBoundaryPrefixRoughCountCertificate |
| `TerminalNoSilentCollapseClosed` | `true` | `true` | prefix 标签到稀疏终端历史的重数守恒已闭合。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `NamedReturnExcluded` | `false` | `false` | 命名回流已压缩成持久全局终端包与非持久预算，但未全部排斥。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitPositiveTerminalBudgetMarginInequality |
| `ColdSupplySameParameterDisciplineClosed` | `true` | `true` | 冷供给和 Lambda 调参纪律已锁入同一余量账本。 | ColdPositiveDominance |
| `ExplicitPositiveMarginProved` | `false` | `false` | 没有同参数数值不等式证明 D_prefix-E_named-U_cold>0。 | B3DiscretePrimeSumUniformErrorPGe100000 AND FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion |
| `RowColumnUnconditionalClosed` | `false` | `false` | 终端正余量和 DStructure/Rankin 晋级门尚未同时完成。 | ExplicitPositiveTerminalBudgetMarginInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一真正最窄点

首攻：

```text
ExplicitPositiveTerminalBudgetMarginInequality
```

并行保留：

```text
B3DiscretePrimeSumUniformErrorPGe100000 AND FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件关闭单参数终端余量标准形，但不证明正余量。
