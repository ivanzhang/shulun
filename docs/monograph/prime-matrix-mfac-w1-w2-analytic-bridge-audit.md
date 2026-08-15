# MFAC W1→W2 解析桥合同审计

## 已登记输入

- 声明来源：`tail_l2_upper_lemma`, `coprime_restricted_tail_bound_lemma`, `euler_phi_aggregation_lemma`, `chebyshev_transfer_lemma`
- 截断统一性变量：`truncation`
- 常数依赖：`fixed_test_function`

## 外部解析引理

- `tail_l2_upper`：外部证明包已登记。
- `coprime_restricted_tail_bound`：外部证明包已登记。
- `euler_phi_aggregation`：外部证明包已登记。
- `chebyshev_transfer`：外部证明包已登记。

## 状态边界

```text
w1_to_w2_status=assumption_chain_registered
chebyshev_energy_bridge_status=unproved
rh_proved=false
```

本证书仅登记外部解析证明包及其防循环合同；它不证明 Möbius 尾和 L²--Upper、
互素限制尾和界、Euler--φ 聚合、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py
```
