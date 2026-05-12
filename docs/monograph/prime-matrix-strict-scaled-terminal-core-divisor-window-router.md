# Prime Matrix strict 缩频终端核心除数窗口路由器

**状态：** `scaled_terminal_core_divisor_window_split_to_cold_budget_or_hot_core_open`

缩频终端核心除数窗口已被拆成冷预算和热异常两类。对历史词 W，令 H_W=h_0/D(W)，终端核心必须整除 H_W 并落在窗口 I_W。若 N_{H_W}(I_W)<=C_core(W)，则 Cap(W)<=C_core(W) 可直接插入 SAE 供给预算；若超过该阈值，则它是 TerminalCoreHotDivisorWindow，必须回流到 LCM 高度矛盾、固定历史 PDEC 或 SAE，而不能作为自由容量保留。

```text
scaled_core_frequency_closed=true
terminal_core_window_closed=true
cold_hot_split_closed=true
cold_core_budget_insertion_closed=true
hot_core_route_registered=true
scaled_terminal_core_divisor_window_count_cap_proved=false
terminal_core_hot_divisor_window_excluded=false
cold_core_threshold_budget_gap_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 核心窗口

对历史词 `W`，定义

```text
H_W = h_0 / D(W).
```

终端核心计数是

```text
N_{H_W}(I_W)=#{k: k|H_W, k in I_W}.
```

## 2. 冷/热分裂

对每个 `W` 固定阈值 `C_core(W)`：

```text
cold: N_{H_W}(I_W)<=C_core(W);
hot:  N_{H_W}(I_W)> C_core(W).
```

冷分支进入 SAE 预算，热分支回流到 LCM/PDEC/SAE。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `scaled_core_frequency` | H_W=h_0/D(W), and every terminal core counted for W divides H_W. | `closed` | 终端核心除数窗口有明确缩频频率。 |
| `terminal_core_window` | Cores lie in I_W=(Y_W^-,Y_W^+] with endpoints inherited from the product window ledger. | `closed` | 终端核心落在明确窗口内。 |
| `cold_hot_split` | N_{H_W}(I_W)<=C_core(W) or N_{H_W}(I_W)>C_core(W). | `closed_dichotomy` | 单历史容量被拆成冷核心预算或热核心异常。 |
| `cold_core_insert` | In the cold case, Cap(W)<=C_core(W) is valid in the SAE budget. | `closed_conditional` | 冷核心阈值可直接进入供给上界。 |
| `hot_core_to_lcm_or_pdec` | Hot terminal core windows route to LCM-height contradiction, fixed-history PDEC, or SAE. | `registered_route_open` | 热核心窗口不是新黑箱，回流到已有矛盾场。 |
| `budget_gap_after_cold_insert` | After cold insertion, prove L_forced > sum_W (T_PDEC(W)-1) C_core(W). | `open_input` | 剩余供需比较转为冷核心阈值预算缺口。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的单历史重数上界分支内。 | 保持 row_column_unconditional_closed=false。 |
| `ScaledCoreFrequencyAndWindowClosed` | `true` | `true` | 终端核心窗口已写成 `H_W` 上的除数窗口。 | 无。 |
| `ColdHotSplitClosed` | `true` | `true` | 核心窗口计数被拆成冷阈值或热异常。 | ColdCoreThresholdBudgetGapComparison OR TerminalCoreHotDivisorWindowPDECorSAE |
| `ColdCoreBudgetInsertionClosed` | `true` | `true` | 冷核心阈值可替换 `Cap(W)` 插入 SAE 预算。 | ColdCoreThresholdBudgetGapComparison |
| `HotCoreRouteRegistered` | `true` | `false` | 热核心窗口进入 LCM/PDEC/SAE，但尚未排斥。 | TerminalCoreHotDivisorWindowPDECorSAE AND TerminalCoreLCMHeightContradictionOrPDEC |
| `ScaledTerminalCoreDivisorWindowCountCapProved` | `false` | `false` | 尚未证明所有核心窗口均冷，也未排斥热核心回流。 | TerminalCoreHotDivisorWindowPDECorSAE AND ColdCoreThresholdBudgetGapComparison |

## 5. 下一步最窄点

```text
ColdCoreThresholdBudgetGapComparison
```

并列需要补齐：

```text
TerminalCoreHotDivisorWindowPDECorSAE
```

并行保留：

```text
SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND TerminalCoreLCMHeightContradictionOrPDEC
```

审稿边界：本步闭合核心窗口的冷/热分裂；未证明冷预算缺口，也未排斥热核心回流。
