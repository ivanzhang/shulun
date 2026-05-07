# Triad-A1 DI/BFI Maynard variable translation 路由器

**状态：** `maynard_exponent_cone_reduced_to_wfd_translation_matrix_open`

Maynard 指数锥准入已继续压成 WFD 非对角对象等式、WFD 指数向量提交、以及一张带正余量的线性翻译矩阵。

## 1. 结构律

CurrentWFDMaynardVariableTranslation is now a finite linear feasibility certificate. Once the WFD dyadic exponent vector is supplied, the Maynard translation and exponent-cone admission are checked by one matrix with positive slack; the separate object identity CurrentWFDMatchesW4OffDiagonalForm remains independent.

```text
previous terminal:
  CurrentWFDMaynardExponentConeAdmission;

new terminal:
  CurrentWFDW4ObjectTranslationMatrixAdmission;

expansion:
  ['CurrentWFDMatchesW4OffDiagonalForm', 'WFDWindowExponentVectorSubmitted', 'CurrentWFDMaynardTranslationMatrixFeasibleWithSlack'].
```

## 2. 汇总

- `translation_matrix_closed=false`。
- `closed_translation_gates=['CommonVariableTableAvailable', 'MaynardExponentConeAvailable', 'NoSymbolCollisionDiscipline', 'W4ParameterAnchorsLinearized']`。
- `open_translation_gates=['CurrentWFDMatchesW4OffDiagonalForm', 'WFDWindowExponentVectorSubmitted', 'CurrentWFDMaynardTranslationMatrixFeasibleWithSlack']`。
- `terminal_gap_after_router=CurrentWFDW4ObjectTranslationMatrixAdmission`。

## 3. 翻译约束

```text
n+m=1
q=x_Q
x_B <= n+r
x_C <= n+r+s
x_F <= n-q
x_Z = 2s
x_Y <= n+2r+3s-m
2n+2r+s <= 1-eta
n+2r+5s+q <= 2-eta
2n+3r+4s+q <= 2-eta
```

## 4. 翻译账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `CommonVariableTableAvailable` | `true` | 共同变量表已有 X,Q,N,M,C,S,H 与 Type-I/II、模数、逆元、频率接口。 | none at table-availability level | `WFDWindowExponentVectorSubmitted` |
| `MaynardExponentConeAvailable` | `true` | 上游已把三条 Maynard 条件压成 CurrentWFDMaynardExponentConeAdmission。 | none at cone-algebra level | `CurrentWFDMaynardTranslationMatrixFeasibleWithSlack` |
| `NoSymbolCollisionDiscipline` | `true` | 记录明确分离共同变量表的 N,M,C,S,H 与 Maynard 的 N_May,R_May,S_May,M_May,Q_May。 | none at notation-discipline level | `WFDWindowExponentVectorSubmitted` |
| `W4ParameterAnchorsLinearized` | `true` | B,C,F,Z,Y 的 W4 参数锚点已写成 x_B,x_C,x_F,x_Z,x_Y 的线性约束。 | none until current WFD exponent vector is supplied | `CurrentWFDMaynardTranslationMatrixFeasibleWithSlack` |
| `CurrentWFDMatchesW4OffDiagonalForm` | `false` | 仍需证明当前 WFD 非对角块逐项生成 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 窗口。 | 对象等式未提交；该项独立于线性尺度矩阵。 | `CurrentWFDW4ObjectTranslationMatrixAdmission` |
| `WFDWindowExponentVectorSubmitted` | `false` | 矩阵需要输入 v_WFD=(x_B,x_C,x_F,x_Z,x_Y,x_Q)，当前尚无逐项 dyadic 指数向量。 | 从当前 WFD 窗口定义抽取 B,C,F,Z,Y,Q 的指数上界。 | `CurrentWFDMaynardTranslationMatrixFeasibleWithSlack` |
| `CurrentWFDMaynardTranslationMatrixFeasibleWithSlack` | `false` | 必须存在 n,r,s,m,q,eta>0 同时满足 W4 参数锚点与 Maynard 指数锥。 | 待 v_WFD 提交后检查线性可行性和正余量 eta。 | `CurrentWFDW4ObjectTranslationMatrixAdmission` |

## 5. 当前结论

当前最窄尺度侧剩余为：

```text
CurrentWFDW4ObjectTranslationMatrixAdmission:
  CurrentWFDMatchesW4OffDiagonalForm;
  WFDWindowExponentVectorSubmitted;
  CurrentWFDMaynardTranslationMatrixFeasibleWithSlack.
```

这一步没有证明 WFD 指数落入锥内；它把待证事实固定成一个对象等式和一个线性矩阵可行性证书。
