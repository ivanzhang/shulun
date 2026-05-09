# Prime Matrix Backlund signed crossing 配对 involution 路由器

**状态：** `backlund_signed_pairing_reduced_to_zeta_xi_transport_open`

signed crossing 配对不能直接从低高度 xi 绕数证书搬来。低高度证书证明固定非零边界的总角变化配平；当前 Backlund trace 处理的是高高度移动凹口中的 arg zeta 局部跳变。因此真正下层最窄点是先闭合 `BacklundZetaXiBranchJumpTransportLedger`：把 zeta 分支跳变搬运到 xi 对称零点 orbit，再注册 formal unit 配对。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
signed_pairing_reduction_closed=true
backlund_signed_pairing_involution_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 直接搬运障碍

| barrier | detail |
| --- | --- |
| `object_mismatch` | 低高度绕数证书处理 xi 边界角变化；Backlund 凹口 trace 的原始硬项是 arg zeta。 |
| `contour_mismatch` | 低高度是固定矩形且边界非零；Backlund 是随 T 移动的近零缩进/避让同伦。 |
| `budget_mismatch` | 低高度绕数只证明总 winding；这里需要每个近零 crossing 的局部跳变量和残余成本 hash。 |

## 2. 自足替换

```text
BacklundSignedCrossingPairingInvolutionLedger
  =>
(BacklundZetaXiBranchJumpTransportLedger AND BacklundXiSymmetricFormalUnitContourLedger AND BacklundMirrorOrbitMultiplicityHashLedger)
```

| atom | role |
| --- | --- |
| `BacklundZetaXiBranchJumpTransportLedger` | 把 Backlund 原始 arg zeta 的 branch jump 无损搬运到 xi 语言，并把 Gamma/初等项列为无零确定相位。 |
| `BacklundXiSymmetricFormalUnitContourLedger` | 登记同一 formal unit 内的 contour/homotopy 对 s->1-s 与共轭对称封闭。 |
| `BacklundMirrorOrbitMultiplicityHashLedger` | 对每个近零 cluster 生成 rho,1-rho,conj rho,1-conj rho 的重数 orbit hash。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SignedPairingGateActive` | `true` | `true` | 容量收缩后，当前下层最窄点是带符号 crossing 的配对 involution。 | BacklundSignedCrossingPairingInvolutionLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在早期零行反例假设链条内处理解析 trace，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `XiSymmetricZeroOrbitAvailable` | `true` | `true` | theta-Mellin 函数方程、xi 整函数性和 Hadamard 乘积给出零点 mirror orbit 的结构底座。 | BacklundMirrorOrbitMultiplicityHashLedger |
| `LowHeightWindingPairingImportedAsModelOnly` | `true` | `true` | 低高度 xi 多边形已用函数方程/共轭对称完成角变化配平，但它只能作为结构模型。 | 不能直接替代高高度 Backlund trace。 |
| `DirectLowHeightPairingPortabilityBlocked` | `true` | `true` | 对象、轮廓和预算三重不匹配，直接套用低高度 winding 会混淆假设链条。 | BacklundZetaXiBranchJumpTransportLedger |
| `SignedPairingReducedToTransportAndFormalUnit` | `true` | `false` | 配对 involution 已压成 zeta->xi 跳变搬运、xi 对称 formal unit、mirror orbit hash 三包。 | BacklundZetaXiBranchJumpTransportLedger AND BacklundXiSymmetricFormalUnitContourLedger AND BacklundMirrorOrbitMultiplicityHashLedger |
| `BacklundZetaXiBranchJumpTransportLedger` | `false` | `false` | 尚未证明 arg zeta 的局部 branch jump 可无损改写为 xi 零点跳变加显式无零相位。 | BacklundZetaXiBranchJumpTransportLedger |
| `BacklundXiSymmetricFormalUnitContourLedger` | `false` | `false` | 尚未登记 Backlund 移动凹口 contour 在 s->1-s 与共轭下封闭。 | BacklundXiSymmetricFormalUnitContourLedger |
| `BacklundMirrorOrbitMultiplicityHashLedger` | `false` | `false` | 尚未给出每个近零 cluster 的 mirror orbit multiplicity hash。 | BacklundMirrorOrbitMultiplicityHashLedger |
| `BacklundSignedCrossingPairingInvolutionLedger` | `false` | `false` | 三包闭合后才可证明 branch_jump 在同一 formal unit 内成对抵消。 | BacklundResidualIndentCoefficientZeroLedger |

## 4. 下一步

当前真正最窄点：`BacklundZetaXiBranchJumpTransportLedger`。
同时需要 formal unit 支撑：`BacklundXiSymmetricFormalUnitContourLedger`。
cluster 哈希支撑：`BacklundMirrorOrbitMultiplicityHashLedger`。
配对完成后验收：`BacklundResidualIndentCoefficientZeroLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：配对 involution 已下压到 zeta-xi 跳变搬运；命题尚未自足闭合。
