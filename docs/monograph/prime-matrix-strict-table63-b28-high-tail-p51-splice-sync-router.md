# Prime Matrix strict b=28 高尾输入接回 Dusart P5.1 拼接证书

**状态：** `table63_b28_high_tail_input_spliced_into_dusart_p51_psi_pair_closed_nonpsi_inputs_remain`

FK b0=28 的高尾替代已经接回 Dusart P5.1：对 x>=e^28，`|psi(x)-x|/x<=0.00001262`，强于旧表值并严格小于 `1/36260`。因此 P5.1 的 psi 输入对已经闭合：高尾由 FK 替代，中段 `1.00002841` 已由完整节点归档闭合。剩余不再是 b=28 高尾，而是 `psi-theta>0.9999sqrt(x)` 下界与 `theta(x)<x` 到 `8e11` 的有限表证书。

```text
table63_b28_high_tail_input_to_p51_splice_closed=true
psi_relative_error_pair_for_p51_closed=true
dusart_p51_full_theta_statement_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 拼接算术

| field | value |
| --- | ---: |
| `target_1_over_36260` | `0.00002757859900717043574186431329288472145615002757859900717043574186431329` |
| `fk_directed_epsilon_upper` | `0.00001262` |
| `old_table63_epsilon_psi_28` | `0.00002224` |
| `endpoint_tax_14_over_e28` | `9.680160149716284213177618522237972979654138214884526798702266406315309E-12` |
| `fk_high_tail_margin_to_target` | `0.00001495859900717043574186431329288472145615002757859900717043574186431329` |
| `fk_high_tail_margin_to_target_after_endpoint_tax` | `0.00001495858932701028602558010011526619921817704792446079228590894316204688` |
| `middle_upper_delta` | `0.00002841` |
| `middle_gap_relative_09999_e_minus_14` | `8.314455662316575272755787440510057683781975991480743378800117368819665E-7` |
| `middle_result_relative` | `0.00002757855443376834247272442125594899423162180240085192566211998826311803` |
| `middle_margin_to_target` | `4.457340209326913989203693572722452822517774708150831575360119526E-11` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只把 psi 高尾输入接回 P5.1 拼接链，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `HighTailP51SpliceGateActive` | `true` | `true` | 上一证书已把下一最窄点设为 b=28 高尾输入到 Dusart P5.1 的拼接同步。 | Table63B28HighTailInputToDusartP51SpliceSyncLedger |
| `FaberKadiriB28HighTailReplacementClosed` | `true` | `true` | FK 校正版给出 \|psi(x)-x\|/x <= 0.00001262 for x>=e^28。 | external FK high-tail input accepted |
| `HighTailBeatsOldTable63AndP51Target` | `true` | `true` | 0.00001262 同时强于旧 Table 6.3 的 0.00002224，并小于 1/36260；保留端点税后仍有余量。 | Table63B28HighTailInputToDusartP51SpliceSyncLedger |
| `MiddlePsiUpperSourceAlreadyClosed` | `true` | `true` | 中段 psi(x)<1.00002841x 的完整节点归档已闭合，可作为 P5.1 中段 psi 输入。 | middle psi upper source closed |
| `DusartP51ArithmeticSpliceReady` | `true` | `true` | P5.1 高尾和中段的纯算术拼接均已验算；高尾输入现由 FK 替代旧表行。 | arithmetic splice ready |
| `PsiRelativeErrorTableEpsilon28AndMiddle2841ForP51Ledger` | `true` | `true` | P5.1 需要的两个 psi 输入已经闭合：高尾 b=28 由 FK 替代，中段 1.00002841 由完整节点归档给出。 | psi input pair closed for P5.1 |
| `Table63B28HighTailInputToDusartP51SpliceSyncLedger` | `true` | `true` | 高尾段 x>=e^28 已接回 Dusart P5.1：theta(x)<=psi(x)<x+x/36260，故 theta(x)-x<x/36260。 | high-tail splice closed |
| `P51StillNeedsNonPsiInputs` | `false` | `false` | P5.1 全段 theta 结论还需要 psi-theta 下界和 theta(x)<x 到 8e11 的有限表/证书。 | PsiMinusThetaLowerGap09999SqrtSelfContainedLedger AND ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭的是 P5.1 高尾输入接口，不直接产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
PsiMinusThetaLowerGap09999SqrtSelfContainedLedger
```

