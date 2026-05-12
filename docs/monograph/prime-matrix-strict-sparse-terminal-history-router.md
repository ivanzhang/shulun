# Prime Matrix strict 稀疏终端历史 SAE/PDEC 路由器

**状态：** `sparse_terminal_history_encoded_pdec_or_sae_budget_open`

稀疏终端历史已经被压成有限词编码。每条终端分支由商型历史 W=((b_1,c_1),...,(b_r,c_r)) 加有限方向元数据确定；深度 r<=floor(log_2|h_0|)，每层字母表大小 A_{Lambda_i}<=8Lambda_i^2。若同一 W 跨 formal unit 持久复现，则进入固定历史 PDEC/ColumnCRT；若都不持久，则总质量由有限历史数与单历史重数上界控制，进入 SAE 预算比较。

```text
history_word_encoding_closed=true
depth_cap_closed=true
alphabet_cap_closed=true
history_count_cap_closed=true
persistent_history_pdec_route_registered=true
nonpersistent_history_sae_reduction_closed=true
fixed_type_history_pdec_excluded=false
sparse_terminal_history_sae_budget_proved=false
sparse_terminal_history_absorbed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 有限历史词

稀疏终端历史可写成

```text
W=((b_1,c_1),...,(b_r,c_r))
```

以及有限方向元数据。深度和字母表满足

```text
r <= floor(log_2 |h_0|),
#{(b_i,c_i)} <= A_{Lambda_i} <= 8 Lambda_i^2.
```

所以历史类型数有显式上界：

```text
#Histories(depth<=R) <= sum_{r<=R} prod_{i<=r} A_{Lambda_i}.
```

## 2. PDEC/SAE 二分

同一历史词若跨 formal unit 持久复现，就形成固定历史 `PDEC/ColumnCRT`。若每个历史词都不持久，则总残留质量被历史类型数和单历史重数上界控制，进入 `SAE` 预算。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `history_word_encoding` | A terminal sparse branch is encoded by W=((b_1,c_1),...,(b_r,c_r)) plus orientation metadata. | `closed` | 稀疏终端对象有规范有限词编码。 |
| `depth_cap` | r<=floor(log_2 \|h_0\|), because each b_i c_i>=2. | `closed` | 历史词长度有限，不能无限增长。 |
| `alphabet_cap` | At depth i, #{(b_i,c_i)}<=A_{Lambda_i}<=8Lambda_i^2. | `closed` | 每层商型字母表已由上一层闭合。 |
| `history_count_cap` | #Histories(depth<=R)<=sum_{r<=R} prod_{i<=r} A_{Lambda_i}. | `closed` | 非持久稀疏历史总类型数有显式上界。 |
| `persistent_history_pdec` | If the same W recurs above the persistence threshold across formal units, it is FixedTypeHistoryPDEC. | `registered_route_open` | 历史词持久化就是命名 PDEC/ColumnCRT 证书。 |
| `nonpersistent_history_sae_budget` | If every W has multiplicity <T_PDEC, total sparse mass <=T_PDEC sum_W cap(W). | `open_budget` | 非持久分支剩余为 SAE 总量预算比较。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的阈值坍缩稀疏历史分支内。 | 保持 row_column_unconditional_closed=false。 |
| `HistoryWordEncodingClosed` | `true` | `true` | 稀疏终端历史可规范编码为有限商型词。 | 无。 |
| `DepthAndAlphabetCapClosed` | `true` | `true` | 历史深度与每层字母表均有显式上界。 | AdaptiveLambdaBalanceForIteratedCoreDensity |
| `PersistentHistoryPDECRouteRegistered` | `true` | `false` | 同一历史词持久复现应进入 PDEC/ColumnCRT。 | FixedTypeHistoryPDECExclusion |
| `NonpersistentHistorySAEReductionClosed` | `true` | `false` | 非持久历史已压成 SAE 总量预算，但预算比较未完成。 | SparseTerminalHistorySAEBudgetComparison AND FormalUnitSparseHistoryMultiplicityCap |
| `SparseTerminalHistoryAbsorbed` | `false` | `false` | 尚未排斥持久历史 PDEC，也未证明非持久历史总量小于 SAE 预算。 | FixedTypeHistoryPDECExclusion AND SparseTerminalHistorySAEBudgetComparison |

## 5. 下一步最窄点

```text
SparseTerminalHistorySAEBudgetComparison
```

并列需要补齐：

```text
FixedTypeHistoryPDECExclusion
```

并行保留：

```text
FormalUnitSparseHistoryMultiplicityCap AND AdaptiveLambdaBalanceForIteratedCoreDensity
```

审稿边界：本步闭合稀疏历史的有限编码与 PDEC/SAE 二分；未证明 SAE 预算小于允许阈值，也未排斥固定历史 PDEC。
