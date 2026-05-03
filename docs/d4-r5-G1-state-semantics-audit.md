# D4/R5 G1a 状态语义审计

**状态：** `G1a_state_definitions_fixed_transitivity_not_yet_proved`

G1a 的第一步已经完成：状态变量和归一化口径固定。它尚未证明全局传递性；下一步应证明投影同型性与分层 Cauchy 的尺度无关 A_eff。

## 状态变量
### `S_j`
- 定义：第 j 尺度的候选/危险冻结成员单元，等于旧尺度单元与新壳层非零同余约束的交。
- 递归作用：递归剥离的对象；剥离新壳层应投影到 S_{j-1} 的同型冻结成员单元。
- 状态：`definition_fixed_projection_not_yet_proved`

### `L_j`
- 定义：付款口径活动容量：positive_contract_sum，按层分解后为各层正收缩质量之和。
- 递归作用：stable 支付项 L_{j-1} Delta L_j / 10 使用同一 L；危险阈值采用 L_cap=0.48。
- 状态：`definition_fixed_local_evidence_available`

### `E_j^*`
- 定义：平方根层资源：transition_high_tail_l2_sqrt + transition_low_start_l2_sqrt + short_chain_l2_sqrt + light_l2_sqrt。
- 递归作用：高容量强迫能量的辅助 Lyapunov 口径；避免使用局部可为负的裸 layer_l2。
- 状态：`definition_fixed_needs_derivation_from_layer_Cauchy`

### `D_j^*`
- 定义：容量缺陷 D_j^*=E_j^*-L_j^2/20。
- 递归作用：若 L_j>L_cap，则希望 D_j^*>=eta_*=0.015，从危险类退出。
- 状态：`local_margin_observed_global_proof_missing`

### `B_j`
- 定义：坏度向量：light_over_026、potential_deficit、U_over_0182、V_over_0074、L_highmass 等阈值超额。
- 递归作用：jump/backflow 递推的单调或可回传对象。
- 状态：`definition_fixed_boundary_count_missing`

### `C_j`
- 定义：层分类标签：light/short_chain/transition/highmass 及其阈值边界。
- 递归作用：判定 stable 或 jump；jump 是 C_j 改变或阈值穿越。
- 状态：`definition_fixed_global_jump_count_missing`

## 归一化契约
- `single_weight_convention`：所有 L_j 与 E_j^* 使用同一 positive_contract_sum / layer l2_sqrt 付款口径，不再混用裸 layer_l2。
- `stable_step`：C_j=C_{j-1} 且新壳层只增加同型层质量；要求 Delta L_j>=0。
- `jump_step`：C_j 改变或穿越 tau_sum/count/U/V/L 阈值。
- `backflow_step`：非 stable 支付且非 jump 吸收时，需构造 pi_j:S_j -> S_{j-1}。

## 最小剩余
- 证明 S_j 剥离新壳层后仍投影到同型冻结成员单元
- 从分层 Cauchy 推导每层 B_i <= A_i e_i 并给出全局 A_eff；需先处理 E_* 未覆盖 heavy/ordinary 正质量的问题
- 证明 E_j^* 与 stable 支付恒等式兼容或作为辅助排除泛函传递
