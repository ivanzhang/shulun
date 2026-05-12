# Prime Matrix strict 平方根核 RH-level 守门路由器

**状态：** `sqrt_kernel_b28_marked_rh_level_unconditional_route_returns_to_dusart_psi_table`

b=28 平方根核常数门完成守门审查：`1/(8pi)` 的数值确实小于允许常数 `0.042304`，但这种对所有 `x>=e^28` 的平方根级 `psi` 误差是 RH-level 输入。有限 verified-zero 窗口不能单独控制无限高尾；若不接受 RH 或等价 PNT 误差输入，就必须回到 Dusart/Schoenfeld 无条件显式 `psi` 误差表内化路线。

```text
sqrt_kernel_constant_arithmetic_fits_b28=true
sqrt_kernel_marked_rh_level=true
finite_verified_zero_window_controls_infinite_tail=false
verified_zero_sqrt_kernel_self_contained_closed=false
psi_epsilon_table_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 常数诊断

| item | value |
| --- | ---: |
| target relative `1/36260` | `2.757859900717e-05` |
| allowed sqrt kernel C | `4.230375168021e-02` |
| Schoenfeld C `1/(8pi)` | `3.978873577297e-02` |
| Schoenfeld relative at b=28 | `2.593901356977e-05` |
| relative margin | `1.639585437402e-06` |
| constant slack ratio | `1.063209243983e+00` |

## 2. 外部边界

- `Schoenfeld 1976 Math. Comput. 30(134)`：https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf；conditional RH square-root psi kernel source boundary
- `Dusart arXiv:1002.0442`：https://arxiv.org/abs/1002.0442；unconditional explicit psi/theta table route boundary

## 3. 自足替换

```text
VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger
  =>
(SchoenfeldRHConditionalPsiSqrtKernelC1Over8PiLedger AND GlobalRHOrVonKochEquivalentPNTErrorInput) OR (FiniteVerifiedZeroWindowPsiKernelLedger AND UnconditionalHighZeroTailDensityFreeBridgeCLe0p042304Ledger)

UnconditionalHighTailRoute
  =>
SchoenfeldDusartPsiEpsilonTableInternalizationLedger

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审查高尾解析核输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `SqrtKernelGateActive` | `true` | `true` | 上一证书把下一最窄点设为 verified-zero 平方根核常数门。 | VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger |
| `SchoenfeldConstantArithmeticFitsB28` | `true` | `true` | 若可使用 Schoenfeld RH 型平方根核常数 1/(8pi)，b=28 高尾常数有正余量。 | SchoenfeldRHConditionalPsiSqrtKernelC1Over8PiLedger |
| `SchoenfeldKernelIsConditionalRHLevel` | `true` | `true` | Schoenfeld 的平方根级 psi 误差是 RH 条件型输入；不能作为无条件 verified-zero 结论直接使用。 | GlobalRHOrVonKochEquivalentPNTErrorInput |
| `FiniteVerifiedZeroWindowDoesNotControlInfiniteTail` | `true` | `true` | 有限高度零点验证只控制有限窗口；高于验证高度的零点仍需全局 RH、零点密度/零点自由尾项或等价 PNT 误差输入。 | UnconditionalHighZeroTailDensityFreeBridgeCLe0p042304Ledger |
| `VerifiedZeroSqrtKernelCanCloseOnlyConditionally` | `true` | `false` | 接受全局 RH 或等价 von-Koch 级 PNT 误差时，该核可条件关闭高尾；作者侧无条件路线不能据此闭合。 | SchoenfeldRHConditionalPsiSqrtKernelC1Over8PiLedger AND GlobalRHOrVonKochEquivalentPNTErrorInput |
| `FiniteWindowPlusTailAlternativeOpen` | `false` | `false` | 若不接受 RH，必须给出有限 verified-zero 窗口加无限高零点尾部的无条件合成预算；当前仓库没有该常数级合成。 | FiniteVerifiedZeroWindowPsiKernelLedger AND UnconditionalHighZeroTailDensityFreeBridgeCLe0p042304Ledger |
| `VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger` | `false` | `false` | 该平方根核路径被标记为 RH-level 分支；不能作为行命题无条件闭合输入。 | (SchoenfeldRHConditionalPsiSqrtKernelC1Over8PiLedger AND GlobalRHOrVonKochEquivalentPNTErrorInput) OR (FiniteVerifiedZeroWindowPsiKernelLedger AND UnconditionalHighZeroTailDensityFreeBridgeCLe0p042304Ledger) |
| `ReturnToUnconditionalDusartPsiTableRoute` | `true` | `true` | 无条件主线应回到 Dusart/Schoenfeld 显式 psi 误差表内化，而不是用 RH 型平方根核冒充自足证明。 | SchoenfeldDusartPsiEpsilonTableInternalizationLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | RH-level 守门审查不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
SchoenfeldDusartPsiEpsilonTableInternalizationLedger
```
