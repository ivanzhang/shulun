# Prime Matrix strict 高尾 b=28 放松平方根核路由器

**状态：** `high_tail_b28_reduced_from_full_epsilon_table_to_verified_zero_sqrt_kernel`

b=28 高尾不必完整复现 Dusart 表值 0.00002224；对行命题当前拼接而言，只需证明 `psi(x)-x<x/36260` for `x>=e^28`。这等价于在 RH 型平方根核 `C sqrt(x) log^2 x` 中取得 `C<=0.042304`；Schoenfeld 的 `1/(8pi)` 形状会有约 6.3% 常数余量。但这是 verified-zero 平方根核输入，当前 C=1280,C_Z=65536 粗 contour 仍远远不足。

```text
high_tail_b28_relaxed_arithmetic_closed=true
schoenfeld_rh_shape_would_fit_b28=true
high_tail_b28_self_contained_closed=false
psi_epsilon_table_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 常数诊断

| item | value |
| --- | ---: |
| target relative `1/36260` | `2.757859900717e-05` |
| Dusart eps high | `2.224000000000e-05` |
| Dusart eps margin | `5.338599007170e-06` |
| allowed sqrt kernel C | `4.230375168021e-02` |
| Schoenfeld RH-shape C | `3.978873577297e-02` |
| sqrt C slack ratio | `1.063209243983e+00` |
| RH-shape relative at b=28 | `2.593901356977e-05` |
| RH-shape margin | `1.639585437402e-06` |
| current C1280/C65536 relative | `6.182503282754e+07` |
| current gap factor vs relaxed target | `2.241775690326e+12` |

## 2. 自足替换

```text
PsiEpsilonHighTailB28SelfContainedLedger
  =>
VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger OR SchoenfeldDusartPsiEpsilonTableInternalizationLedger

PsiHighTailB28OneSidedTargetRelativeLedger
  =>
VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只放松高尾解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `HighTailB28GateActive` | `true` | `true` | 上一证书把下一最窄点设为 b=28 高尾 psi 上界。 | PsiEpsilonHighTailB28SelfContainedLedger |
| `PsiHighTailB28OneSidedTargetRelativeLedger` | `true` | `true` | 高尾为了接 Dusart P5.1 只需 psi(x)-x<x/36260；完整 0.00002224 表值是更强输入。 | PsiEpsilonHighTailB28SelfContainedLedger |
| `SchoenfeldRHShapeWouldFitB28` | `true` | `true` | 若能无条件内化 verified-zero 平方根核常数 1/(8pi)，则 b=28 高尾有正余量。 | VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger |
| `AllowedSqrtKernelConstantComputed` | `true` | `true` | b=28 处允许平方根核常数 C<=0.042304；Schoenfeld RH 型常数约 0.039789，余量约 6.3%。 | VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger |
| `CurrentC1280C65536TemplateStillFailsRelaxedHighTail` | `false` | `false` | 即使用放松目标，当前粗 contour 在 e^28 处仍比目标大约 2.24e12 倍。 | VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger |
| `PsiEpsilonHighTailB28SelfContainedLedger` | `false` | `false` | 高尾仍未自足闭合；最窄替代是证明 verified-zero 平方根核，或完整内化 Schoenfeld/Dusart psi 表。 | VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger OR SchoenfeldDusartPsiEpsilonTableInternalizationLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 高尾放松不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger
```
