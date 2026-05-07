# Triad-A1 DI/BFI Maynard exponent cone 路由器

**状态：** `maynard_w4_conditions_reduced_to_current_wfd_exponent_cone_open`

Maynard-W4 的三条条件已统一压成指数锥；剩余为当前 WFD 的 W4 非对角对象等式、变量翻译表，以及指数锥准入。

## 1. 结构律

The three Maynard W4 multiplicative conditions are one linear exponent-cone admission after writing N=x^n, R=x^r, S=x^s, M=x^m, Q=x^q. The diagonal condition is exactly the factor condition under n+m=1. The remaining task is to supply the current WFD variable translation and prove the translated exponents lie inside this cone with positive slack.

```text
previous terminal:
  CurrentWFDSatisfiesMaynardW4Conditions;

new terminal:
  CurrentWFDMaynardExponentConeAdmission;

exponent cone:
  ['n+m=1', '2n+2r+s <= 1-eta', 'n+2r+5s+q <= 2-eta', '2n+3r+4s+q <= 2-eta'].
```

## 2. 汇总

- `maynard_exponent_cone_closed=false`。
- `closed_cone_gates=['W4ConditionsConvertedToExponentCone', 'DiagonalEqualsFactorCondition']`。
- `open_cone_gates=['CurrentWFDMatchesW4OffDiagonalForm', 'CurrentWFDMaynardVariableTranslation', 'CurrentWFDFitsMaynardExponentCone', 'JBoundDominanceAfterW4Substitution']`。
- `terminal_gap_after_router=CurrentWFDMaynardExponentConeAdmission`。

## 3. 指数锥账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `W4ConditionsConvertedToExponentCone` | `true` | 三条 Maynard 乘法条件已改写为 n,r,s,q 的线性不等式。 | none at algebraic conversion level | `CurrentWFDFitsMaynardExponentCone` |
| `DiagonalEqualsFactorCondition` | `true` | n+m=1 时，M_May>R_May^2 S_May N_May 等价于 2n+2r+s<1。 | 仍需当前 WFD 给出 n,m,r,s 翻译和正余量 eta。 | `CurrentWFDFitsMaynardExponentCone` |
| `CurrentWFDMatchesW4OffDiagonalForm` | `false` | 上游 W4 ledger 仍将该项列为 open；指数锥只处理尺度，不处理对象等式。 | 证明 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 窗口来自当前 WFD 非对角展开。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `CurrentWFDMaynardVariableTranslation` | `false` | 必须给出 N_May,R_May,S_May,M_May,Q_May 与当前 X,Q,N,M,C,S,H 的非冲突翻译。 | 没有该翻译，指数锥不能代入。 | `CurrentWFDFitsMaynardExponentCone` |
| `CurrentWFDFitsMaynardExponentCone` | `false` | 需要同时满足 n+m=1、2n+2r+s<=1-eta、n+2r+5s+q<=2-eta、2n+3r+4s+q<=2-eta。 | 当前 WFD 的 n,r,s,m,q 尚未提交，因此不能关闭该 cone admission。 | `CurrentWFDSatisfiesMaynardW4Conditions` |
| `JBoundDominanceAfterW4Substitution` | `false` | 上游 open_w4_gates=['CurrentWFDMatchesW4OffDiagonalForm', 'CurrentWFDMaynardVariableTranslation', 'MaynardDiagonalCondition', 'MaynardOffDiagonalCondition1', 'MaynardOffDiagonalCondition2', 'JBoundDominanceAfterW4Substitution']；三条件已合并为 exponent cone。 | 只有 CurrentWFDFitsMaynardExponentCone 关闭后，J-bound dominance 才关闭。 | `CurrentWFDFitsMaynardExponentCone` |

## 4. 当前结论

尺度侧最窄剩余为：

```text
CurrentWFDMaynardExponentConeAdmission:
  CurrentWFDMatchesW4OffDiagonalForm;
  CurrentWFDMaynardVariableTranslation;
  CurrentWFDFitsMaynardExponentCone.
```

这一步关闭了三条 Maynard 条件分散表达的退路，但未证明当前 WFD 的指数落入该锥。
