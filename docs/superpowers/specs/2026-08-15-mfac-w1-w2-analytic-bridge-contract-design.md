# MFAC W1→W2 解析桥合同审计设计

## 目标

新增一个独立的 Python 审计器，将 RH 主链的 `W1 → W2` 边拆成最小、可机检的
解析合同。它只登记将 Möbius 尾和整体 `L²` 控制传递到 Chebyshev 能量桥所需的
前提，不以有限数值剖面、Mertens 型假设、Mellin、零点信息或目标误差反向填补
缺失步骤。

产物必须明确保持：

```text
w1_to_w2_status=assumption_chain_registered
chebyshev_energy_bridge_status=unproved
rh_proved=false
```

## 背景与问题

现有 `mobius_tail_l2` 审计仅验证有限 Euler--φ 二次型恒等式；
`mertens_conditional_l2_upper` 仅登记全 ε Mertens 型假设后的三项开放义务。
主链图则显示 `W1 → W2` 没有已登记支持模块。

因此，下一步不是把有限剖面外推成统一结论，而是把桥梁的必要输入、量词、常数
依赖和禁止循环来源显式登记。这样可以准确区分“已给出足够解析引理”与“只写入
了目标结论名称”。

## 合同模型

审计器接受一个 `Mapping`，其中必须包含：

- `uses`：非空字符串序列，声明已使用的输入；
- `tail_l2_upper`：`True`，表示 W1 的整体 L²--Upper 已作为外部前提登记；
- `coprime_restricted_tail_bound`：`True`，表示已提供带参数的互素限制尾和界；
- `euler_phi_aggregation`：`True`，表示已提供与 Euler--φ 权重相容的聚合引理；
- `chebyshev_transfer`：`True`，表示已提供从该聚合到 Chebyshev 能量形式的传递引理；
- `uniformity_variable`：固定为 `"truncation"`，要求常数对截断统一；
- `constant_dependency`：仅允许有限预注册依赖（例如 `"fixed_test_function"`）；
- `claimed_bridge_uses`：实际声明为桥梁来源的 `uses` 子集。

审计器不验证上述解析引理本身；布尔字段是可审计的“已提供证明包”声明，而不是
定理证明。返回载荷会逐项列出仍需人工/形式化证明的义务。

## 防循环规则

`uses` 和 `claimed_bridge_uses` 必须拒绝：

- `RH`、`zeta_zero`、`zero_free_region`、`explicit_formula`、`Mellin`；
- `Chebyshev_error`、`target_energy_bridge`、`chebyshev_energy_bridge`；
- `finite_profile`、`numerical_experiment`。

同时拒绝：缺失任一桥梁引理、非统一截断常数、裸字符串/非字符串序列、未声明来源、
非内建 `bool` 以及试图以 `rh_proved=True` 提升状态的输入。

## 证书与命令行

新增：

- `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py`
- `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.py`
- `docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.json`
- `docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.md`

默认 CLI 生成 JSON 和 Markdown。使用示例：

```bash
python3 experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py
```

Markdown 必须列出 W1 的外部前提、三项桥梁引理、禁止输入与未证明边界。

## 测试策略

1. 合法合同生成 `assumption_chain_registered`，且永不把状态提升到已证明。
2. 每一项缺失引理、错误统一性、伪造 RH 状态均被拒绝。
3. 禁止循环来源与未声明 `claimed_bridge_uses` 均被拒绝。
4. `write_certificate`、默认 CLI 和脚本路径 CLI 写出可解析 JSON、含边界的 Markdown。

## 非目标

- 不证明 Möbius 尾和 `L²`--Upper、互素限制尾和界、Euler--φ 聚合或 Chebyshev 传递。
- 不构造或验证零自由区域、Mellin 收缩、显式公式或 RH。
- 不以有限截断数值、随机性模型或已知目标误差作为证明输入。
