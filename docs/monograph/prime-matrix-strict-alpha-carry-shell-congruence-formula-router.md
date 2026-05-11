# Prime Matrix strict alpha carry-shell 同余 row 公式路由器

**状态：** `strict_alpha_carry_shell_congruence_formula_closed_overload_terminal_gap_open`

`AlphaFormulaCarryShellCongruenceRowFormulaLedger` 已在 unsigned 层闭合：source tuple/anchor 参数、carry-shell 恒等式、P列距离坐标和 layered-wheel 相位可共同给出确定性候选 row skeleton。这正是早期零行反例链被真实结构链挤压出的几何公式；但它不提供 signed alpha 系数，也不排斥 anchor-collar 短纤维过载。下一最窄点转为 `AlphaFormulaAnchorCollarOverloadNamedReturnLedger`，同时保留终端容量/模型余量和 DStructure/Rankin 验收门。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
counterexample_assumption_only=true
alpha_formula_carry_shell_congruence_formula_router_closed=true
alpha_formula_carry_shell_congruence_row_formula_proved=true
alpha_formula_signed_coefficient_lift_proved=false
alpha_formula_anchor_collar_overload_named_return_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同余公式

| name | formula | meaning |
| --- | --- | --- |
| `row height` | `h=P-x` | 把早期零行行号 x 转成底部距离 h。 |
| `high factor coordinates` | `q=P-a, m=P-b, 1<=a,b<h` | 双高因子 q,m in (x,P) 等价为 a,b 落在同一 h 壳内。 |
| `carry index` | `k=floor(ab/P)` | 进位层 k 决定该点位于哪条 carry shell。 |
| `row congruence` | `h=a+b-k, c=ab mod P` | 合法 shell pair 给出唯一候选列 residue c。 |
| `P-column distance` | `xP+c=P(x+1)-(P-c)` | 把同一候选点登记到 P 列锚的距离坐标 d=P-c。 |

## 2. 公式边界

The carry-shell congruence formula is an unsigned geometric indexing theorem. It maps each double-high filler atom to h=P-x, q=P-a, m=P-b, k=floor(ab/P), h=a+b-k and c=ab mod P, then records the same point by P-column distance d=P-c. This closes the row skeleton, but it does not create a signed pre-Cauchy alpha coefficient.

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍在 Assume EarlyZeroRowWithinP 的反例链中传递，只证明反例强制的候选行几何公式。 | 不使用真实零行缺席。 |
| `CarryShellCongruenceTargetActive` | `true` | `false` | signed-lift 分支回流终端后，当前非回流首攻点重排为 carry-shell 同余 row 公式。 | AlphaFormulaCarryShellCongruenceRowFormulaLedger |
| `SourceTupleVariableBindingImported` | `true` | `true` | source tuple 的 A、D0/K/Omega、phase_rule 与 hash 可复算，并能作为 h,a,b,k,c 的筛选输入。 | AlphaFormulaSourceTupleToCarryShellVariableBindingLedger |
| `ExactCarryShellIdentityImported` | `true` | `true` | 任何双高因子补洞 xP+c=(P-a)(P-b) 都满足 h=a+b-floor(ab/P), c=ab mod P。 | carry-shell row 公式的代数核心已闭合。 |
| `PColumnDistanceCoordinateImported` | `true` | `true` | 候选点 xP+c 可无损写成 P 列锚 Py 左侧距离 d=P-c，便于同 formal unit 登记。 | P-column distance coordinate。 |
| `PhaseWheelCompatibilityImported` | `true` | `true` | P列圆柱平移与 layered-wheel 相位字母表已能和 carry-shell residue 同步登记。 | AlphaFormulaPhaseWheelCompatibilityLedger |
| `AnchorCollarRestrictionImported` | `true` | `true` | 若进入大分支真双素 carry-shell，最小高素 anchor 被限制到 canonical collar，cofactor 落在短素数纤维。 | 这给过载回流输入，但不排斥过载。 |
| `CarryShellCongruenceRowSkeletonClosed` | `true` | `true` | 给定 source tuple 与 phase 过滤后，carry-shell 同余和 P列距离坐标给出确定性候选 row skeleton。 | 该结论仍是 unsigned/geometric。 |
| `AlphaFormulaCarryShellCongruenceRowFormulaClosed` | `true` | `true` | 目标 ledger 在 unsigned row 公式层闭合：它覆盖并只覆盖由双高因子 carry-shell 与相位过滤登记的合法候选点。 | 不等于 signed alpha primitive row 证明。 |
| `SignedLiftBranchAlreadySyncedToTerminal` | `true` | `false` | signed coefficient lift 仍未证明；已有同步只说明该分支当前回到全局终端容量/模型缺口，而不是非循环出口。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `AnchorCollarOverloadReturnStillOpen` | `true` | `false` | 短纤维满载、phase 过载或同参数复用仍需命名回流并被容量门排斥。 | AlphaFormulaAnchorCollarOverloadNamedReturnLedger |
| `DirectContradictionNotYetReached` | `true` | `false` | 本步关闭了几何同余公式，但没有排斥终端容量/模型账本，也没有证明 signed pre-Cauchy 源。 | AlphaFormulaAnchorCollarOverloadNamedReturnLedger AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一主攻点

```text
AlphaFormulaAnchorCollarOverloadNamedReturnLedger
```

并行保留：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```
