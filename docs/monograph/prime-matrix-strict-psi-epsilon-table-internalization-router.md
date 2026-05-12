# Prime Matrix strict psi 误差表内化压力路由器

**状态：** `psi_epsilon_table_internalization_reduced_to_verified_zero_or_schoenfeld_dusart_table_proof`

psi 误差表不能由当前 C=1280,C_Z=65536 的粗自足 contour 推出：在 `x=e^28` 处，当前相对包络约为目标 `0.00002224` 的 `2.78e12` 倍；在 `8e11` 处约为目标 `0.00002841` 的 `2.09e12` 倍。因此本步把最窄缺口压成 `PsiEpsilonHighTailB28`、`PsiUpperMiddle8e11ToE28` 与 verified-zero/Turing 输入，而不宣布 Dusart 内部化闭合。

```text
psi_epsilon_table_self_contained_closed=false
current_strict_perron_zero_sum_tail_components_ready=true
current_c1280_c65536_template_beats_psi_epsilon_targets=false
direct_internal_dusart_theta_pnt_envelope_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 压力诊断

| site | x | needed relative | current relative | gap factor | beats |
| --- | ---: | ---: | ---: | ---: | --- |
| high tail b=28 | `1.446257064291e+12` | `2.224000000000e-05` | `6.182503282754e+07` | `2.779902555195e+12` | `false` |
| middle left 8e11 | `8.000000000000e+11` | `2.841000000000e-05` | `5.948296345828e+07` | `2.093733314265e+12` | `false` |

## 2. 自足替换

```text
PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger
  =>
PsiEpsilonHighTailB28SelfContainedLedger AND PsiUpperMiddle8e11ToE28SelfContainedLedger AND CriticalLineAndStripVerifiedZeroInputForPsiEpsilonTableLedger

PsiEpsilonHighTailB28SelfContainedLedger
  =>
SchoenfeldDusartPsiEpsilonTableInternalizationLedger

PsiUpperMiddle8e11ToE28SelfContainedLedger
  =>
SchoenfeldDusartPsiEpsilonTableInternalizationLedger

SchoenfeldDusartPsiEpsilonTableInternalizationLedger
  =>
SharpVerifiedZeroPsiContourEnvelopeLedger AND CriticalLineAndStripVerifiedZeroInputForPsiEpsilonTableLedger

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审查解析输入表，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `PsiEpsilonTableGateActive` | `true` | `true` | Dusart 解析拼接证书已把下一最窄点压到 psi 显式误差表。 | PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger |
| `CurrentStrictPerronZeroSumTailComponentsReady` | `true` | `true` | 非平滑 Perron 常数、高高度零点和、平凡/素数幂尾项已经 strict 自足同步。 | 这些只是粗模板组件，不等于 Dusart 误差表。 |
| `CurrentC1280C65536TemplateBeatsPsiEpsilonTargets` | `false` | `false` | 当前 C=1280,C_Z=65536 模板在 e^28 和 8e11 处均比目标大约 10^12 倍，不能推出 psi 表。 | SchoenfeldDusartPsiEpsilonTableInternalizationLedger OR SharpVerifiedZeroPsiContourEnvelopeLedger |
| `PsiEpsilonHighTailB28SelfContainedLedger` | `false` | `false` | 需要证明对所有 x>=e^28 有 \|psi(x)-x\|/x<=0.00002224 或足够的单侧上界。 | SchoenfeldDusartPsiEpsilonTableInternalizationLedger |
| `PsiUpperMiddle8e11ToE28SelfContainedLedger` | `false` | `false` | 需要证明 8e11<=x<=e^28 上 psi(x)<1.00002841x。 | SchoenfeldDusartPsiEpsilonTableInternalizationLedger |
| `PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger` | `false` | `false` | psi 误差表尚未自足内化；必须引入可复算的 Schoenfeld/Dusart 表证明或更尖锐的 verified-zero contour。 | PsiEpsilonHighTailB28SelfContainedLedger AND PsiUpperMiddle8e11ToE28SelfContainedLedger AND CriticalLineAndStripVerifiedZeroInputForPsiEpsilonTableLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | psi 表压力审查不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
PsiEpsilonHighTailB28SelfContainedLedger
```
