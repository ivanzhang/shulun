# MFAC LCM 去常数投影循环审计设计

**状态：** `design_approved_implementation_pending_user_spec_review`

## 1. 目标

本轮将上一轮的常数方向障碍压缩为一个精确的实际整数命题：

```text
ActualLCMGramOffConstantProjectionCircularityAudit
```

它只审计基于 LCM Gram 核、以 `e_1` 为常数方向的**直接秩一正交化**。目标是证明该模板的正交化系数与待控制的 Chebyshev 误差完全等价，从而排除把后验中心化误称为独立强制能量的循环捷径。

本轮不证明 RH、不证明 `psi(X)-X` 的界、不证明不存在一切非循环能量，也不否定未来的非秩一实际算术结构。

## 2. 固定实际对象与精确恒等式

令 `X>=1`，对 `1<=d,e<=X` 定义：

```text
K_X(d,e) = floor(X / lcm(d,e))
w_d = -mu(d) log(d)
g_d = w_d - 1_{d=1}
e_1(d) = 1_{d=1}.
```

采用 LCM Gram 双线性型：

```text
<a,b>_K = sum_{d,e<=X} a_d b_e K_X(d,e).
```

由 `K_X(d,1)=floor(X/d)`、`Lambda(n)=-sum_{d|n}mu(d)log(d)` 得到实数域精确恒等式：

```text
<w,e_1>_K = psi(X)
<g,e_1>_K = psi(X)-X
<e_1,e_1>_K = X.
```

因此，对任意实数 `alpha`，有：

```text
<g-alpha e_1,e_1>_K = psi(X)-X-alpha X.
```

这些是初等实际整数恒等式；程序只能对有限范围作浮点数值审计，并必须记录数值残差。

## 3. 唯一性与循环证书

`g-alpha e_1` 与 `e_1` 正交，当且仅当：

```text
alpha = (psi(X)-X)/X.
```

故直接 `e_1`-正交投影的系数唯一，且正是目标误差的归一化值。若一个候选中心化合同以如下输入定义或恢复该系数：

```text
psi(X)
E_psi(X)
psi(X)-X
target_error
zero_location
zero_free_region
explicit_formula_remainder
```

它必须被分类为：

```text
direct_e1_projection_uses_target_or_forbidden_analytic_input
```

该分类仅说该中心化不是 `ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula` 的独立输入；它不等价于任何自然数素数反例或 RH 否定。

## 4. 直接投影模板的精确障碍

给定一个不读取目标的候选系数 `alpha`，其正交缺陷为：

```text
orthogonality_defect = psi(X)-X-alpha X.
```

因此，如果该模板试图以“缺陷精确为零”取得 off-constant 能量，它已经等价于给出 `psi(X)-X=alpha X`。独立证明这个等式本身可构成未来的真正算术输入；但 schema、有限表、后验残差、数值拟合或重命名都不能充当该证明。

## 5. 下一正向出口

本轮完成后，真正尚未闭合的门收紧为：

```text
NoncircularActualOffConstantCoerciveWitnessBeforeMellin
```

它至少需要：

```text
fixed_actual_integer_embedding
independent_actual_arithmetic_source
non_target_defined_off_constant_family
positive_or_coercive_energy_identity
target_projection_control_without_e1_posterior_centering
no_use_of_RH_or_zero_free_input
```

若候选仍只是 `g-alpha e_1` 的精确正交化，则必须先独立证明其 `alpha`，否则会被本审计的唯一性证书拒绝。真正突破只能来自非秩一、非后验、能控制目标投影的实际算术结构。

## 6. 实施范围

新增审计模块与测试，内容为：

1. 有限 `X` 上逐点验证 `K_X(d,1)=floor(X/d)`；
2. 独立计算 `psi(X)` 后验证三条 LCM 投影恒等式；
3. 验证任意 `alpha` 的正交缺陷公式；
4. 验证唯一正交系数与 `E_psi(X)/X` 数值一致；
5. 对目标/零点输入的中心化合同给出最小循环证书；
6. 对独立性声明不足的合同保持 `unverified`，不得升级为数学不存在性；
7. 生成 JSON/Markdown 证书、更新状态表和内部索引。

建议文件：

```text
experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py
experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py
docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.json
docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.md
```

## 7. 验证命令

```bash
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
```
