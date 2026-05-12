# Prime Matrix strict 表尾项显式零点自由区路由器

**状态：** `explicit_zero_free_table_tail_external_kadiri_available_internal_table_constants_open`

表尾项零点自由区路线已拆清：Kadiri 外部来源可登记，但作者侧还需表尾项所用常数、有限 RH 验证终点到零点自由尾项的高度拼接、尾项预算，以及与 epsilon 表生成器同口径的 contour 匹配。现有 C=1280,C_Z=65536 粗预算虽已自足，但此前压力诊断显示远不足以给出 Dusart 表值。

```text
kadiri_external_source_identified=true
explicit_zero_free_table_tail_closed=false
table_tail_zero_free_constants_closed=false
tail_height_transition_closed=false
psi_epsilon_tail_remainder_budget_closed=false
zero_free_tail_to_table_contour_match_closed=false
existing_internal_zero_free_chain_present_but_coarse=true
existing_zero_sum_contour_budget_not_enough_for_table=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 外部边界

- `Kadiri 2004`：https://arxiv.org/abs/math/0401238
- role：external zero-free region source for table tail, not repository self-contained table-tail budget

## 2. 自足替换

```text
ExplicitZeroFreeRegionForTableTailLedger
  =>
TableTailZeroFreeConstantsLedger AND ZeroFreeTailHeightRangeAndTransitionLedger AND PsiEpsilonTailRemainderBudgetLedger AND ZeroFreeTailToPsiEpsilonTableContourMatchLedger

FiniteVerifiedZerosToZeroFreeTailTransitionLedger
  =>
LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger AND SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计 epsilon 表尾项零点自由区输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ExplicitZeroFreeTableTailGateActive` | `true` | `true` | 大高度有限 RH 输入外部通道登记后，下一并列硬点是表尾项显式零点自由区。 | ExplicitZeroFreeRegionForTableTailLedger |
| `KadiriExternalSourceIdentified` | `true` | `false` | Dusart 文献登记 Kadiri 显式零点自由区；可作为外部条件来源。 | Kadiri2004ExplicitZeroFreeRegionExternalAcceptedForTableTail |
| `ExistingInternalZeroFreeChainIsCoarse` | `true` | `true` | 仓库已有零点自由常数拆包和 C=1280 粗预算，但它不是 Dusart epsilon 表尾项的精确常数账本。 | TableTailZeroFreeConstantsLedger AND ZeroFreeTailToPsiEpsilonTableContourMatchLedger |
| `ExistingZeroSumContourBudgetNotEnoughForTable` | `true` | `true` | C=1280,C_Z=65536 粗零点和预算已自足，但前面压力诊断显示它距离 eps_psi 表值约 10^12 倍。 | PsiEpsilonTailRemainderBudgetLedger |
| `TableTailZeroFreeConstantsLedger` | `false` | `false` | 需要明确表尾项使用的零点自由区公式、常数、适用高度和舍入方向。 | Kadiri2004ExplicitZeroFreeRegionExternalAcceptedForTableTail |
| `ZeroFreeTailHeightRangeAndTransitionLedger` | `false` | `false` | 需要把大高度有限 RH 验证的终点与零点自由区尾项起点精确拼接。 | FiniteVerifiedZerosToZeroFreeTailTransitionLedger |
| `PsiEpsilonTailRemainderBudgetLedger` | `false` | `false` | 需要把零点自由区尾项、零点密度/和、平凡尾项分配到 eps_psi(28) 与中段表值预算。 | ZeroFreeTailToPsiEpsilonTableContourMatchLedger |
| `ZeroFreeTailToPsiEpsilonTableContourMatchLedger` | `false` | `false` | 需要证明该尾项常数与 epsilon 表生成器的显式公式同口径，而不是另一个粗 contour 模板。 | PsiEpsilonTableComputationAlgorithmLedger |
| `ExplicitZeroFreeRegionForTableTailLedger` | `false` | `false` | 当前只登记 Kadiri 外部来源和粗内部链不足；表尾项零点自由区尚未作者侧闭合。 | TableTailZeroFreeConstantsLedger AND ZeroFreeTailHeightRangeAndTransitionLedger AND PsiEpsilonTailRemainderBudgetLedger AND ZeroFreeTailToPsiEpsilonTableContourMatchLedger |
| `ExternalConditionalLaneAvailable` | `true` | `false` | 若接受 Kadiri/Dusart 外部常数和表算法，可条件推进到 finite-zero/tail 桥接审查。 | Kadiri2004ExplicitZeroFreeRegionExternalAcceptedForTableTail |
| `RowColumnUnconditionalClosed` | `false` | `false` | 表尾项零点自由区审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
FiniteVerifiedZerosToZeroFreeTailTransitionLedger
```
