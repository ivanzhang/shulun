# Prime Matrix strict formal-unit 稀疏历史重数上界路由器

**状态：** `formal_unit_sparse_history_multiplicity_reduced_to_scaled_core_divisor_cap_open`

formal-unit 稀疏历史重数已经压成缩频终端核心除数窗口计数。对历史词 W，令 D(W)=prod b_i c_i，则同一 formal unit 内该历史的终端核心 都必须整除 h_0/D(W)，并落在由窗口乘积账本给出的区间 I_W。因此 Mult_U(W)<=N_{h_0/D(W)}(I_W)。若该窗口计数过大，就回流为 TerminalCoreHotDivisorWindowPDECorSAE；若不过大，冷核心阈值可插入 SAE 预算。

```text
history_product_identity_closed=true
terminal_core_interval_closed=true
multiplicity_to_divisor_count_closed=true
hot_core_route_registered=true
cold_core_capacity_inserted=true
formal_unit_sparse_history_multiplicity_cap_proved=false
scaled_terminal_core_divisor_window_count_cap_proved=false
terminal_core_hot_divisor_window_excluded=false
fixed_type_history_pdec_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 单历史容量

对历史词

```text
W=((b_1,c_1),...,(b_r,c_r)),
D(W)=prod_i b_i c_i.
```

同一 formal unit 内的终端核心必须满足

```text
k | h_0/D(W),  k in I_W.
```

所以

```text
Mult_U(W) <= N_{h_0/D(W)}(I_W).
```

这把抽象 `Cap(W)` 改写为缩频终端核心除数窗口计数。

## 2. 出口

若该除数窗口热，则进入 `TerminalCoreHotDivisorWindowPDECorSAE`；若不热，则用冷核心阈值 `C_core(W)` 进入 SAE 预算。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `history_product_identity` | For W=((b_i,c_i)), D(W)=prod_i b_i c_i and terminal cores divide h_0/D(W). | `closed` | 历史词决定唯一缩频分母。 |
| `terminal_core_interval` | Terminal cores k lie in an explicit interval I_W inherited from the product window ledger. | `closed` | 单历史容量变成缩频上的窗口除数计数。 |
| `multiplicity_to_divisor_count` | Mult_U(W) <= N_{h_0/D(W)}(I_W). | `closed` | 同一 formal unit 内同一历史词的重数不超过缩频终端核心除数数。 |
| `hot_core_route` | If N_{h_0/D(W)}(I_W) exceeds the cap, it is a terminal core hot divisor window and routes to PDEC/SAE. | `registered_route_open` | 单历史容量过大不是自由预算，而是回流到热除数/PDEC/SAE。 |
| `cold_core_capacity` | If no hot core window occurs, Cap(W) is bounded by the registered cold-core threshold C_core(W). | `closed_conditional` | 在排除热核心出口后，单历史容量有可插入 SAE 预算的上界。 |
| `cap_to_budget_gap` | Insert Cap(W)<=C_core(W) into U_sparse <= sum_W (T_PDEC(W)-1)Cap(W). | `closed_reduction` | 单历史重数上界已接回供需预算缺口。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的稀疏历史 SAE 预算分支内。 | 保持 row_column_unconditional_closed=false。 |
| `HistoryProductIdentityClosed` | `true` | `true` | 历史词给出缩频分母 `D(W)`。 | 无。 |
| `MultiplicityToDivisorCountClosed` | `true` | `true` | 单历史重数已压成缩频终端核心窗口除数计数。 | ScaledTerminalCoreDivisorWindowCountCap |
| `HotCoreRouteRegistered` | `true` | `false` | 核心窗口计数过大时回流 PDEC/SAE。 | TerminalCoreHotDivisorWindowPDECorSAE |
| `ColdCoreCapacityInserted` | `true` | `false` | 无热核心时可把冷核心阈值插回 SAE 预算，但阈值比较未完成。 | ScaledTerminalCoreDivisorWindowCountCap AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `FormalUnitSparseHistoryMultiplicityCapProved` | `false` | `false` | 尚未排斥热核心窗口，也未给出足够强的冷核心容量阈值。 | TerminalCoreHotDivisorWindowPDECorSAE AND ScaledTerminalCoreDivisorWindowCountCap |

## 5. 下一步最窄点

```text
ScaledTerminalCoreDivisorWindowCountCap
```

并行保留：

```text
TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow
```

审稿边界：本步闭合单历史重数到缩频除数窗口的改写；未排斥热核心窗口，也未证明冷核心阈值足以闭合 SAE 预算。
