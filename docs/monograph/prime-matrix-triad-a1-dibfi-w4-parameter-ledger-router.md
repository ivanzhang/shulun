# Triad-A1 DI/BFI W4 parameter ledger 路由器

**状态：** `w4_parameter_ledger_reduced_to_current_wfd_maynard_conditions_open`

W4 参数模板与 J-bound 简化已固定；剩余为当前 WFD 到 W4 的对象等式、变量翻译表，以及一条对角条件和两条非对角条件。

## 1. 结构律

The Maynard-W4 parameter template is now explicit. The final DI scale work is no longer to search for a theorem or formula, but to prove that the present uncentered WFD block generates the W4 off-diagonal variables and satisfies three concrete Maynard inequalities after a non-conflicting variable translation.

```text
previous terminal:
  CurrentWFDToMaynardW4ParameterLedger;

new terminal:
  CurrentWFDSatisfiesMaynardW4Conditions;

expansion:
  ['CurrentWFDMatchesW4OffDiagonalForm', 'CurrentWFDMaynardVariableTranslation', 'MaynardDiagonalCondition', 'MaynardOffDiagonalCondition1', 'MaynardOffDiagonalCondition2'].
```

## 2. 汇总

- `w4_parameter_ledger_closed=false`。
- `closed_w4_gates=['MaynardW4TemplateExtracted', 'W4JBoundSimplified', 'SourceSymbolsReadyForTranslation']`。
- `open_w4_gates=['CurrentWFDMatchesW4OffDiagonalForm', 'CurrentWFDMaynardVariableTranslation', 'MaynardDiagonalCondition', 'MaynardOffDiagonalCondition1', 'MaynardOffDiagonalCondition2', 'JBoundDominanceAfterW4Substitution']`。
- `terminal_gap_after_router=CurrentWFDSatisfiesMaynardW4Conditions`。

## 3. W4 账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `MaynardW4TemplateExtracted` | `true` | W4 的 B,C,F,Z,Y 参数和三条最终条件已抽成记录。 | none at Maynard-template level | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `W4JBoundSimplified` | `true` | 在 Maynard factor 条件下，J^2 简化为两项主界。 | none before current-window substitution | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `SourceSymbolsReadyForTranslation` | `true` | 共同变量表与 KZ-E spine 已有 X,Q,N,M,C,S,H、Type-I/II 和 s1/s2/h 接口。 | 符号可翻译，但尚未给出非冲突的 N_May/R_May/S_May/M_May/Q_May 表。 | `CurrentWFDMaynardVariableTranslation` |
| `CurrentWFDMatchesW4OffDiagonalForm` | `false` | 上游 RDN router 已把 DI 变量代入 W4，但当前 E_disp 到 W4 off-diagonal 变量的逐项等式未写出。 | 证明 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 窗口正是当前 WFD 的非对角展开。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `CurrentWFDMaynardVariableTranslation` | `false` | 当前变量表有 X,Q,N,M,C,S,H；Maynard 条件使用 N_May,R_May,S_May,M_May,Q_May。 | 建立非冲突翻译表，避免把本项目 S 与 DI/Maynard 的不同 S 混同。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `MaynardDiagonalCondition` | `false` | 需证明 N_May^2 R_May^2 S_May << x^(1-7eps)。 | 从当前窗口上界推出该对角条件。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `MaynardOffDiagonalCondition1` | `false` | 需证明 N_May R_May^2 S_May^5 Q_May < x^(2-14eps)。 | 从当前窗口上界推出第一条非对角条件。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `MaynardOffDiagonalCondition2` | `false` | 需证明 N_May^2 R_May^3 S_May^4 Q_May < x^(2-14eps)。 | 从当前窗口上界推出第二条非对角条件。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `JBoundDominanceAfterW4Substitution` | `false` | 上游 open_substitution_gates=['CurrentWFDMatchesW4OffDiagonalForm', 'MaynardW4ParameterBoundsForCurrentWFD', 'JBoundDominanceAfterW4Substitution']；W4 条件已显式化但未由当前窗口推出。 | 三条 Maynard 条件全部成立后，该项才可关闭。 | `CurrentWFDSatisfiesMaynardW4Conditions` |

## 4. 当前结论

尺度侧的最窄剩余为：

```text
CurrentWFDSatisfiesMaynardW4Conditions:
  CurrentWFDMatchesW4OffDiagonalForm;
  CurrentWFDMaynardVariableTranslation;
  MaynardDiagonalCondition;
  MaynardOffDiagonalCondition1;
  MaynardOffDiagonalCondition2.
```

这一步关闭了 W4 模板未知和 J-bound 未简化的退路，但未证明当前 WFD 满足三条 Maynard 条件。
