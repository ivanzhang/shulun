# Prime Matrix Backlund zeta-xi 分支跳变搬运闭合路由器

**状态：** `backlund_zeta_xi_branch_jump_transport_closed_formal_unit_next`

`BacklundZetaXiBranchJumpTransportLedger` 已闭合：在高高度 Backlund 轮廓中，xi=G*zeta 且 G 无零无极点，所以 zeta 的局部零点 branch jump 与 xi 的局部零点 branch jump 按解析重数完全相同。剩余硬点转为注册 xi 对称 formal unit 和 mirror orbit multiplicity hash。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zeta_xi_branch_jump_transport_closed=true
signed_pairing_involution_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 搬运恒等式

```text
xi(s)=1/2*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)
jump_arg_zeta(rho)=jump_arg_xi(rho), counted with analytic multiplicity
```

| factor | reason |
| --- | --- |
| `1/2` | 常数非零，不产生分支跳变。 |
| `s(s-1)` | 高高度 Backlund 轮廓满足 \|Im s\|>14，避开 s=0,1。 |
| `pi^(-s/2)` | 指数函数处处非零，只贡献连续确定相位。 |
| `Gamma(s/2)` | Gamma 函数无零点；其极点在非正整数，高高度临界带不相交。 |

## 2. 自足替换

```text
BacklundZetaXiBranchJumpTransportLedger
  =>
BacklundZetaXiBranchJumpTransportClosed
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ZetaXiTransportGateActive` | `true` | `true` | signed pairing 路由后，当前真正最窄点是把 arg zeta 的 crossing 跳变搬运到 xi。 | BacklundZetaXiBranchJumpTransportLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只处理假设链条内解析恒等式，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `XiDefinitionAndFunctionalEquationAvailable` | `true` | `true` | theta-Mellin 层已给出 xi(s)=1/2*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)。 | 无 xi 定义剩余。 |
| `LowHeightSeparatedFromBacklundTrace` | `true` | `true` | 0<t<=14 的低高度 xi 子包已关闭；当前搬运只作用于高高度 Backlund trace。 | 无低高度混淆。 |
| `ElementaryGammaFactorNoJumpClosed` | `true` | `true` | G(s)=1/2*s*(s-1)*pi^(-s/2)*Gamma(s/2) 在高高度轮廓无零无极点，不能产生零点 crossing 跳变。 | 只剩连续确定相位预算。 |
| `MultiplicityTransportClosed` | `true` | `true` | xi=G*zeta 且 G 无零无极点，所以 zeta 与 xi 的局部零点重数、branch_jump 完全一致。 | BacklundMirrorOrbitMultiplicityHashLedger |
| `EndpointLimitConventionCompatible` | `true` | `true` | 若端点落零，先避开再取极限，重数由 endpoint convention 吸收，不改变搬运等式。 | EndpointZeroAvoidanceMultiplicityConventionClosedByLimit。 |
| `BacklundZetaXiBranchJumpTransportLedger` | `true` | `true` | arg zeta 的局部分支跳变已可无损搬运到 xi 零点跳变；Gamma/初等项不进入 crossing 配对。 | BacklundXiSymmetricFormalUnitContourLedger |
| `SignedPairingStillOpenAfterTransport` | `false` | `false` | 搬运只解决对象不匹配；仍需 xi 对称 formal unit 和 mirror orbit hash 才能配对抵消。 | BacklundXiSymmetricFormalUnitContourLedger AND BacklundMirrorOrbitMultiplicityHashLedger |

## 4. 下一步

当前真正最窄点：`BacklundXiSymmetricFormalUnitContourLedger`。
支撑哈希：`BacklundMirrorOrbitMultiplicityHashLedger`。
父级配对账本：`BacklundSignedCrossingPairingInvolutionLedger`。
配对完成后验收：`BacklundResidualIndentCoefficientZeroLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：zeta-xi 跳变搬运已闭合；formal unit 配对仍未闭合。
