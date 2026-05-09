# Prime Matrix Backlund 对称 max 溢价路由器

**状态：** `backlund_symmetric_max_premium_is_unique_constant_obstruction_open`

高幂辅助函数常数核已压到一个精确溢价问题：单个 signed-mean 圆周分子为 7，而 C16 允许分子为 9.305206...，因此对称 max 额外溢价必须不超过 2.305206...。粗略双计或用局部变差控制都超预算；当前严格自足路线的唯一常数剩余就是证明该对称高度 max 溢价小于 C16 余量。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
parent_remaining=BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger
symmetric_boundary_max_identity_closed=true
allowed_c16_numerator=9.305206478445
signed_mean_base_numerator=7.000000000000
available_premium_margin=2.305206478445
naive_double_numerator=14.000000000000
new_unique_internal_remaining=BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger
row_column_self_contained_closed=false
```

## 1. 溢价恒等式

令 `U_T(phi)` 表示单个 shifted xi 圆周的 normalized log 边界项。高幂极限给出：

```text
lim_{N->infty} N^{-1} log |B_{T,theta,N}(z(phi))|
  <= max(U_T(phi), U_T(-phi)).
```

因此

```text
avg max(U(phi), U(-phi))
  = avg U(phi) + 1/2 avg |U(phi)-U(-phi)|.
```

第一项已有 signed-mean C7；第二项就是当前唯一溢价。

## 2. 常数门

| item | value |
| --- | ---: |
| C16 allowed numerator | `9.305206478445` |
| signed-mean base numerator | `7.000000000000` |
| available premium margin | `2.305206478445` |
| naive doubled numerator | `14.000000000000` |

结论：必须证明对称 max 溢价的 log 系数 `<=2.305206478445`；否则 C16 不能通过。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审查高幂辅助函数边界平均的常数结构，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `HighPowerSignedMeanGateActive` | `true` | `true` | 上一层唯一剩余是高幂辅助函数继承 signed-mean C16 预算。 | BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger |
| `SymmetricBoundaryMaxIdentityClosed` | `true` | `true` | N->infty 后边界项为 max(U_T(phi),U_T(-phi))，其中 U_T(-phi) 是共轭高度的同分布项。 | BacklundHighPowerBoundarySymmetricMaxIdentityClosed |
| `SignedMeanBaseC7Available` | `true` | `true` | 单个 U_T 圆周 signed-mean 分子系数已为 7。 | BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 |
| `C16MarginComputed` | `true` | `true` | C16 允许分子为 16 log(4/sqrt(5))=9.305206...，扣掉 C7 后只剩 2.305206... 溢价余量。 | BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger |
| `NaiveDoubleSignedMeanFails` | `true` | `true` | 若用 max<=U^+ + U^- 粗估，分子会接近 14，超过 9.305，不能闭合。 | BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger |
| `LocalVariationPremiumBoundTooLarge` | `true` | `true` | 用既有局部变差 C216 控制高度差 8 的对称差会产生远大于 2.305 的预算，不能作为闭合。 | BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger |
| `SymmetricMaxPremiumStillOpen` | `false` | `false` | 仍需证明平均正部差 1/2 int \|U_T(phi)-U_T(-phi)\| 的 log 系数不超过 2.305206。 | BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger |
| `SelfContainedBacklundStillOpen` | `false` | `false` | 该溢价未闭合前，高幂辅助 Backlund 内部常数不能进入 C16/C_S=8。 | BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger |
| `ExternalBacklundStillAvailable` | `true` | `false` | 外部经典 Backlund 引理整体处理了该对称 max/高幂 Jensen 常数。 | ClassicalBacklundZeroIndentationCostExternalAccepted |

## 4. 下一步

内部唯一最窄点：`BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger`。
外部逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：所有形式层已压实；严格自足版最后剩余是对称 max 溢价常数不等式。
