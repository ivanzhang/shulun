# Prime Matrix strict RKS2/RKS3 反演小和集到内部 fiber 前沿同步证书

**状态：** `inverse_smalldoubling_frontier_synced_to_interior_shifted_product_fiber`

本轮没有换题，而是把上一提交的反演小和集能量前沿与仓库中已跟踪的更深链条合并。从 `A=J^{-1}` 的能量出发，现已连续接到仿射等差段倒数自交、`s=0` 退化相位吸收、非零相位 shifted product fiber，以及有符号小相位整数提升吸收。因此当前唯一内部自足剩余不再是完整反演 sum-product 定理，而是内部相位 `min(c,P-c)>max J` 的 shifted product fiber 高谱平均排斥；需要证明 `InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound`。

```text
reduction_chain_closed_to_interior_frontier=true
interior_shifted_product_high_spectrum_proved=false
self_contained_inverse_smalldoubling_proved=false
row_column_unconditional_closed=false
```

## 1. 同步链条

| step | formula | effect |
| --- | --- | --- |
| `inverse-energy` | A=J^(-1), E_+(A)=sum_s r_J(s)^2 | 反演小和集问题等价于 Möbius 重叠谱。 |
| `affine-inverse` | r_J(s)=\|A_s cap A_s^(-1)\|, A_s=sJ-1 | 一般 Möbius 重叠化为仿射等差段的倒数自交。 |
| `degenerate-phase` | s=0 gives b=-a and contributes at most N^2 | 退化仿射相位已被固定幂能量预算吸收。 |
| `shifted-product` | for s!=0, c=s^(-1), (a-c)(b-c)=c^2 mod P | 非零 PGL2 高谱转为 shifted modular hyperbola 纤维。 |
| `signed-small-phase` | \|gamma\|<=max J implies (a-gamma)(b-gamma)=gamma^2+kP with \|k\|<=log^O(P) | 近零/近 P 相位由整数分支和除数界吸收。 |
| `interior-frontier` | min(c,P-c)>max J | 唯一剩余为内部相位的平均型分支/斜率 incidence 或除数包估计。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `InverseSmallDoublingTargetActive` | `true` | `true` | 最新前沿证书已把唯一内部自足剩余命名为反演小和集倒数能量节省。 | SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar |
| `AffineInverseSelfIntersectionImported` | `true` | `true` | 已跟踪证书给出 `A_s=sJ-1` 的倒数自交等价式，并吸收低重叠层。 | affine reduction imported |
| `DegenerateS0PhaseAbsorbedImported` | `true` | `true` | `s=0` 仿射退化相位只贡献 `O(N^2)`，已从高谱硬点移除。 | nonzero PGL2 remains |
| `NonzeroShiftedProductFiberImported` | `true` | `true` | `s!=0` 等价于 shifted product fiber `(a-c)(b-c)=c^2 mod P`。 | InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar |
| `SignedSmallPhaseAbsorbedImported` | `true` | `true` | 有符号小相位由整数提升和除数界吸收；全局点态界不再是必要门。 | InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar |
| `InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar` | `false` | `false` | 内部相位 `min(c,P-c)>max J` 的高谱平均排斥尚未证明。 | InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound |
| `SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar` | `false` | `false` | 原反演小和集自足输入已缩窄，但仍等价依赖内部相位 fiber 高谱输入。 | InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步同步并压缩剩余，不宣称行/列无条件闭合。 | InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar |

## 3. 下一最窄自足目标

```text
InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar
InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound
```
