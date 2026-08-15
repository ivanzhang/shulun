# MFAC W2→W3 实际 Mellin 传递合同审计设计

## 目标

新增独立审计器，把主链 `W2 → W3` 中“实际 Chebyshev 的 dyadic 能量控制传递到
Mellin 半平面范数”的最小证明义务显式化、机检化。模块只登记外部解析证明包，
禁止把有限 LCM/协方差数值、自由乘法模型、零点信息、零自由区域、显式公式或 RH
作为桥接来源。

默认结果必须保持：

```text
w2_to_w3_status=assumption_chain_registered
actual_mellin_half_plane_contraction_status=unproved
w3_spectral_contraction_status=unproved
rh_proved=false
```

## 为什么选择这一边

`W1→W2` 已有两份合同审计，分别登记外部解析引理和 Chebyshev 能量桥的最小无条件
结构，但均不证明实际桥。现有自由 Mellin 增长反模型进一步表明：Möbius 交替、
divisor-lattice 恒等式和有限数值剖面不足以强制平方根级收缩。

因此，下一步须针对实际对象固定从 dyadic 能量到 Mellin 半平面范数所需的测度、
尺度求和与 Plancherel 型传递；不能用“存在 Mellin 收缩”作为未展开的结论名称。

## 最小合同

审计器接受一个 `Mapping`。以下四项必须是内建 `True`，并只表示相应的外部证明
包已经登记：

1. `actual_dyadic_chebyshev_energy_bound`：对固定实际 Chebyshev 误差和所有充分大
   dyadic 尺度的统一能量上界；
2. `dyadic_scale_partition`：正尺度覆盖、无遗漏/重叠计账的 dyadic 分解；
3. `weighted_scale_summability`：携带半平面参数的尺度级数可和性；
4. `mellin_plancherel_transfer`：与预注册测度一致的 Mellin/Plancherel 型范数传递。

其余字段：

- `uses`：非空字符串序列；
- `claimed_transfer_uses`：`uses` 的子集，列出该结论真正读取的来源；
- `actual_error_object`：固定为 `"psi_minus_identity"`；
- `dyadic_scale_variable`：固定为 `"X_to_2X"`；
- `mellin_measure`：固定为 `"dt_over_t_squared"`；
- `half_plane_parameter`：有限内建实数，严格位于 `(1/2, 1)`；
- `constant_dependency`：固定为 `"fixed_test_function_and_half_plane_parameter"`，
  不得依赖 dyadic 截断指数。

审计器不计算 `psi`，不验证上述外部引理，也不根据字段自动推出收缩。它只说明：
如要把 W2 的实际能量结果用于 W3，证明包必须同时交代这四条边及其量词。

## 防循环

在 `uses` 与 `claimed_transfer_uses` 中禁止：

- `RH`、`zeta_zero`、`zero_free_region`、`explicit_formula`；
- `Mellin_contraction`、`target_mellin_bound`、`w3_spectral_contraction`；
- `finite_profile`、`numerical_experiment`、`free_multiplicative_model`；
- `Mertens_cancellation`、`PNT`。

同时拒绝 `rh_proved`、`w3_closed` 或 `actual_mellin_half_plane_contraction` 等目标结论
字段；拒绝错误测度、端点/非有限半平面参数、裸字符串、未声明来源以及非内建布尔值。

## 产物与测试

新增：

- `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py`
- `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.py`
- `docs/monograph/prime-matrix-mfac-w2-w3-mellin-transfer-audit.json`
- `docs/monograph/prime-matrix-mfac-w2-w3-mellin-transfer-audit.md`

测试覆盖：合法合同不提升 W3/RH；四项引理、测度、参数、常数依赖的严格验证；
所有禁止来源与未声明来源的拒绝；以及 `write_certificate` 和脚本路径 CLI 的输出。

使用示例：

```bash
python3 experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py \
  --half-plane-parameter 0.75
```

## 非目标

- 不证明 W2 的实际 Chebyshev 能量界。
- 不证明尺度级数可和性、Mellin/Plancherel 传递或半平面收缩。
- 不计算零点、零自由区域、显式公式或 RH。
- 不把有限实验、自由模型或经验随机性升级为实际解析结论。
