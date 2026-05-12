# Prime Matrix strict 迭代阈值坍缩账本路由器

**状态：** `iterated_threshold_collapse_reduced_to_sparse_terminal_history_pdec_or_sae_open`

阈值坍缩已经从模糊缺口压成显式乘积账本。第 r 层有效核心数下界为 M_r >= rho_0 Y_0 / prod(A_i M_i)，其中 A_i<=8Lambda_i^2、M_i=max(b_i,c_i)<2Lambda_i。故坍缩等价于 prod(A_i M_i)>rho_0 Y_0。若实际反例链在最早坍缩层后仍有残留，它已不再是高密度窗口，只能是稀疏终端历史。同一历史持久复现进入固定历史 PDEC/ColumnCRT；不持久历史进入 SAE 总量账本。

```text
effective_core_lower_bound_closed=true
collapse_inequality_closed=true
adaptive_lambda_balance_registered=true
sparse_terminal_reduction_closed=true
persistent_history_pdec_route_registered=true
nonpersistent_history_sae_route_registered=true
threshold_collapse_excluded=false
sparse_terminal_history_absorbed=false
fixed_type_history_pdec_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 坍缩不等式

第 `r` 层核心窗口的有效数量下界为

```text
M_r >= rho_0 Y_0 / prod_{i<=r}(A_i M_i),
A_i <= 8 Lambda_i^2,
M_i=max(b_i,c_i)<2 Lambda_i.
```

所以阈值坍缩的精确账本形式是

```text
prod_{i<=r}(A_i M_i) > rho_0 Y_0.
```

粗略充分生存条件为

```text
prod_{i<=r} 16 Lambda_i^3 <= rho_0 Y_0.
```

这个条件只是参数纪律，不作为无条件闭合证明。

## 2. 稀疏终端历史

在最早坍缩层之后，密度账本已不能提供高密度窗口；若假设反例链仍留下实际对象，它只能是一个有限深度、有限商型字母表中的稀疏终端历史。

持久的同一历史是 `PDEC/ColumnCRT`；不持久历史是 `SAE`。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `effective_core_lower_bound` | M_r >= rho_0 Y_0 / prod_{i<=r}(A_i M_i), where A_i<=8Lambda_i^2 and M_i=max(b_i,c_i)<2Lambda_i. | `closed` | 核心数量下界同时登记密度损耗和窗口缩短。 |
| `collapse_inequality` | Threshold collapse at depth r means prod_{i<=r}(A_i M_i) > rho_0 Y_0. | `closed` | 阈值坍缩等价于显式乘积账本超出初始质量预算。 |
| `coarse_lambda_sufficient_collapse_condition` | Since A_i M_i <=16 Lambda_i^3, survival is guaranteed if prod_i 16Lambda_i^3 <= rho_0 Y_0. | `closed_sufficient` | 给出可调 Lambda 纪律；粗界只作充分条件，不当作最终证明。 |
| `minimal_collapse_sparse_terminal` | At the first depth r with M_r<1, any actual surviving branch is a sparse terminal history, not a dense window. | `closed_reduction` | 阈值坍缩不再是第四种高密度出口，而是稀疏终端历史。 |
| `persistent_history_to_pdec` | A sparse terminal history recurring for the same quotient-type history across formal units is a fixed-type-history PDEC. | `registered_route_open` | 同一历史若持久，必须进入 PDEC/ColumnCRT，不可作为自由残留。 |
| `nonpersistent_history_to_sae` | Nonpersistent terminal histories are counted by finite depth and finite quotient alphabet, hence route to SAE. | `registered_route_open` | 不持久残留是稀疏异常，需由 SAE 总量账本吸收。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的迭代缩频阈值分支内。 | 保持 row_column_unconditional_closed=false。 |
| `CollapseInequalityClosed` | `true` | `true` | 阈值坍缩已写成显式乘积不等式。 | AdaptiveLambdaBalanceForIteratedCoreDensity |
| `SparseTerminalReductionClosed` | `true` | `true` | 最早坍缩层后的实际残留只能是稀疏终端历史。 | SparseTerminalHistorySAEAbsorptionOrPDECExclusion |
| `PersistentHistoryPDECRouteRegistered` | `true` | `false` | 同一商型历史持久复现应进入 PDEC/ColumnCRT。 | FixedTypeHistoryPDECExclusion |
| `NonpersistentHistorySAERouteRegistered` | `true` | `false` | 非持久终端历史应由有限深度/有限字母表 SAE 账本吸收。 | SparseTerminalDescentSAEAbsorptionLedger |
| `ThresholdCollapseExcluded` | `false` | `false` | 尚未排斥持久历史 PDEC，也未闭合非持久历史 SAE 总量吸收。 | FixedTypeHistoryPDECExclusion AND SparseTerminalDescentSAEAbsorptionLedger |

## 5. 下一步最窄点

```text
SparseTerminalHistorySAEAbsorptionOrPDECExclusion
```

并列参数纪律：

```text
AdaptiveLambdaBalanceForIteratedCoreDensity
```

并行保留：

```text
DepthwiseLCMExplosionAgainstScaledFrequencyHeight AND FixedTypeHistoryPDECExclusion AND SparseTerminalDescentSAEAbsorptionLedger
```

审稿边界：本步闭合阈值坍缩的乘积账本与稀疏终端归约；未排斥 PDEC，也未完成 SAE 总量吸收。
