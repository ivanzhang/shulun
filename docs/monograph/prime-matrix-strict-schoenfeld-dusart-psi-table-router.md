# Prime Matrix strict Schoenfeld/Dusart psi 表内化路由器

**状态：** `schoenfeld_dusart_psi_table_internalization_split_into_four_table_inputs`

无条件高尾路线已回到 Schoenfeld/Dusart 显式 psi 表。P5.1 需要四类作者侧输入：`eps_psi(28)<=0.00002224`、`8e11<=x<=e^28` 的 `psi<1.00002841x`、`psi-theta>0.9999sqrt(x)`、以及 `theta(x)<x` 到 `8e11` 的有限表。其中中段拼接余量只有约 `4.46e-11`，因此表值生成器和舍入方向必须单独验收。

```text
schoenfeld_dusart_psi_table_self_contained_closed=false
p51_arithmetic_splice_ready=true
table_rounding_margin_audit_closed=true
high_tail_eps_table_closed=false
middle_psi_upper_table_closed=false
psi_theta_gap_self_contained_closed=false
theta_less_than_identity_to_8e11_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 表值责任

| input | claim | used for | margin | closed |
| --- | --- | --- | ---: | --- |
| `PsiEpsilonHighTailB28TableCertificate` | psi(x)-x <= 0.00002224 x for x>=e^28 | high tail | `5.338599007170e-06` | `false` |
| `PsiUpperMiddle8e11ToE28TableCertificate` | psi(x) < 1.00002841 x for 8e11<=x<=e^28 | middle strip before subtracting psi-theta | `4.457340209481e-11` | `false` |
| `PsiMinusThetaLowerGap09999SqrtSelfContainedLedger` | psi(x)-theta(x)>0.9999 sqrt(x) on the middle strip | middle strip subtraction | `4.457340209481e-11` | `false` |
| `ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger` | theta(x)<x for x<=8e11 | finite left range | `n/a` | `false` |

## 2. 拼接余量

| item | value |
| --- | ---: |
| target relative `1/36260` | `2.757859900717e-05` |
| eps high b=28 | `2.224000000000e-05` |
| high margin | `5.338599007170e-06` |
| middle raw psi upper | `2.841000000000e-05` |
| middle psi-theta gap at e^28 | `8.314455662317e-07` |
| middle result relative | `2.757855443377e-05` |
| middle margin | `4.457340209481e-11` |

## 3. 外部边界

- `Dusart arXiv:1002.0442`：https://arxiv.org/abs/1002.0442；source boundary for Proposition 5.1 and the epsilon/table values
- `Schoenfeld 1976 Math. Comput. 30(134)`：https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf；source boundary for classical Chebyshev-function estimates used by the table lineage

## 4. 自足替换

```text
SchoenfeldDusartPsiEpsilonTableInternalizationLedger
  =>
PsiEpsilonHighTailB28TableCertificate AND PsiUpperMiddle8e11ToE28TableCertificate AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger AND ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger AND DusartP51TableRoundingMarginAuditLedger

PsiEpsilonHighTailB28TableCertificate
  =>
SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger

PsiUpperMiddle8e11ToE28TableCertificate
  =>
SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger

```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只内化无条件 psi 表输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `UnconditionalPsiTableGateActive` | `true` | `true` | 平方根核已被标记为 RH-level，故无条件主线回到 Schoenfeld/Dusart 显式 psi 表。 | SchoenfeldDusartPsiEpsilonTableInternalizationLedger |
| `P51ArithmeticSpliceAlreadyReady` | `true` | `true` | Dusart P5.1 的拼接算术已经完成，剩余是表值本身和证明来源。 | DusartP51TableRoundingMarginAuditLedger |
| `HighTailTableValueNeeded` | `false` | `false` | 需要作者侧证明或可复算证书给出 eps_psi(28)<=0.00002224。 | SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger |
| `MiddlePsiUpperTableNeeded` | `false` | `false` | 需要证明 8e11<=x<=e^28 上 psi(x)<1.00002841x；该常数因中段余量很薄，不能粗化。 | SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger |
| `PsiThetaGapNeeded` | `false` | `false` | 中段还必须内化 psi-theta>0.9999sqrt(x)，否则 0.00002841 不能降到 1/36260 以下。 | PsiMinusThetaLowerGap09999SqrtSelfContainedLedger |
| `ThetaFiniteTableTo8e11Needed` | `false` | `false` | 仓库只有 x<=20000 的有限 theta 桥；Dusart P5.1 左段需要 theta(x)<x 到 8e11。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `RoundingMarginAuditActive` | `true` | `true` | 高尾余量约 5.34e-6，中段余量仅约 4.46e-11；表值必须保留足够有效数字和舍入方向。 | DusartP51TableRoundingMarginAuditLedger |
| `SchoenfeldDusartPsiEpsilonTableInternalizationLedger` | `false` | `false` | Schoenfeld/Dusart psi 表尚未作者侧自足内化；当前只完成了责任拆包与余量审查。 | PsiEpsilonHighTailB28TableCertificate AND PsiUpperMiddle8e11ToE28TableCertificate AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger AND ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger AND DusartP51TableRoundingMarginAuditLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | psi 表内化拆包不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一最窄点

```text
SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger
```
