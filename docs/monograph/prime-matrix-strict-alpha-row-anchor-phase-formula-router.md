# Prime Matrix strict alpha row anchor/phase 公式路由器

**状态：** `strict_alpha_row_anchor_phase_formula_reduced_to_carry_shell_phase_signed_lift_return_open`

`AlphaRowAnchorPhaseEmissionFormulaLedger` 被继续压成 source tuple 到 carry-shell 变量绑定、carry-shell 同余 row 公式、P列/圆柱/层叠轮相位兼容、unsigned 到 signed alpha 系数提升、短纤维过载命名回流五项。早期零行反例链与真实刚性链的直接压力已经进入本公式审查：候选 row 必须同时满足 carry-shell、anchor-collar 和 layered-wheel；但这仍只给 unsigned 形状。当前最窄点为 `AlphaFormulaSignedCoefficientLiftLedger`。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
alpha_row_anchor_phase_formula_router_closed=true
alpha_row_anchor_phase_emission_formula_proved=false
deterministic_alpha_primitive_row_emission_map_proved=false
actual_noncanonical_alpha_side_primitive_rule_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 上游矛盾放大器

If an early zero row is assumed, the true geometry forces every candidate alpha row shape through carry-shell, anchor-collar and P-column/layered-wheel constraints. This amplifies the contradiction pressure, but it is still unsigned: the missing strict self-contained step is a signed pre-Cauchy coefficient lift or a named overload return.

## 2. 公式内部拆分

拆分前：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

拆分后：

```text
AlphaFormulaSourceTupleToCarryShellVariableBindingLedger AND AlphaFormulaCarryShellCongruenceRowFormulaLedger AND AlphaFormulaPhaseWheelCompatibilityLedger AND AlphaFormulaSignedCoefficientLiftLedger AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AlphaRowAnchorPhaseFormulaTargetActive` | `true` | `false` | 上一层已把当前最窄点固定为 A/D0/K/Omega/phase_rule 到 alpha row 的显式发射公式。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `EarlyZeroContradictionMatrixImported` | `true` | `true` | 早期零行若存在，已被 CLB、formal unit、carry-shell、cofactor-depth、anchor-collar 压到命名终端。 | 该矩阵只给 unsigned 刚性，不直接给 signed alpha 公式。 |
| `CarryShellIdentityImportedForFormulaShape` | `true` | `true` | 任何从早期零行抽取的候选 row 形状必须满足 h=a+b-floor(ab/P), c=ab mod P。 | 需要把该形状变成 signed alpha primitive row 公式。 |
| `AnchorCollarShortFiberImported` | `true` | `true` | 大分支的候选 row 必须落入 canonical collar 短素数纤维，否则进入 PDEC/SAE/ColumnCRT。 | 需要容量排斥或命名回流。 |
| `PColumnLayeredWheelCompatibilityImported` | `true` | `true` | P列锚、圆柱相位和 layered wheel 固定了候选公式必须遵守的相位字母表。 | 仍需公式级相位兼容等式。 |
| `UnsignedZeroRowSeedExtractionBlocked` | `true` | `true` | 早期零行覆盖证书不能直接生成 pre-Cauchy signed alpha/delta source seed。 | AlphaFormulaSignedCoefficientLiftLedger。 |
| `AlphaSourceTupleToCarryShellVariableBindingCurrentCorpusProved` | `false` | `false` | 当前材料尚未把 source tuple 字段 A、D0/K/Omega、phase_rule 逐项绑定到 h,a,b,k,c 的 row 变量。 | AlphaFormulaSourceTupleToCarryShellVariableBindingLedger。 |
| `AlphaCarryShellCongruenceRowFormulaCurrentCorpusProved` | `false` | `false` | 当前材料尚未写出 alpha row 的显式同余/索引公式并证明它覆盖且只覆盖合法 carry-shell row。 | AlphaFormulaCarryShellCongruenceRowFormulaLedger。 |
| `AlphaPhaseWheelCompatibilityCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明该 row 公式与 P列锚、圆柱相位、层叠轮筛和 phase_rule 同步兼容。 | AlphaFormulaPhaseWheelCompatibilityLedger。 |
| `AlphaSignedCoefficientLiftCurrentCorpusProved` | `false` | `false` | 当前材料尚未把 unsigned carry-shell/anchor-collar row 提升为 pre-Cauchy signed alpha 系数行。 | AlphaFormulaSignedCoefficientLiftLedger。 |
| `AlphaAnchorCollarOverloadReturnCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明短纤维满载或公式过载时必进入可排斥的 PDEC/SAE/ColumnCRT 命名回流。 | AlphaFormulaAnchorCollarOverloadNamedReturnLedger。 |
| `AlphaRowAnchorPhaseFormulaCurrentCorpusProved` | `false` | `false` | 变量绑定、同余公式、相位兼容、signed 提升和过载回流五项尚未合取证明。 | AlphaFormulaSourceTupleToCarryShellVariableBindingLedger AND AlphaFormulaCarryShellCongruenceRowFormulaLedger AND AlphaFormulaPhaseWheelCompatibilityLedger AND AlphaFormulaSignedCoefficientLiftLedger AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger |

## 4. 下一主攻点

```text
AlphaFormulaSignedCoefficientLiftLedger
```
