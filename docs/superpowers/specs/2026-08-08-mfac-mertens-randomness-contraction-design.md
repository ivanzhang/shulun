# MFAC Mertens 随机性缺陷与去常数能量收缩设计

## 目标

建立一个双轨审计框架，研究真实 Möbius 部分和

```text
M(x) = sum_{n<=x} mu(n)
```

的分块符号交替、素因子层叠加和跨尺度相关结构。框架必须严格分开：

1. 有限样本上的随机/正态基线比较；
2. 可被独立证明的、对全部尺度统一的确定性缺陷界；
3. 只有在第二类界成立时才可尝试推出的去常数 coercive 能量不等式。

目标不是假设或宣布 Möbius 符号“服从正态分布”，而是把正态、非高斯和乘法相关都作为可检验模型，并明确记录它们不足以证明 RH 的原因。

## 非目标

- 不从有限范围的直方图、KS 距离、偏度或峰度推出 RH、零点排除或 `M(x)=O(x^(1/2+epsilon))`。
- 不把随机乘法函数、独立 Rademacher 符号或分层重排模型等同于实际整数上的 Möbius 函数。
- 不把均值为零、全局正负抵消或弱收敛到正态分布当作一致尾界、谱收缩或非循环能量来源。
- 不在本阶段调用显式公式、RH、零点自由区或等价结论来验证待证明的缺陷界。
- 不声称本设计已经给出 `psi(x)-x` 的平方根界；该对象只在 Mertens 合同独立成立后进入第二阶段。

## 第一阶段对象

对 dyadic 基点 `X` 和块长 `H`，定义实际整数上的增量：

```text
Delta_M(X,H) = M(X+H) - M(X)
```

令一个尺度桶由满足 `X in [T, 2T)` 的不重叠或固定步长基点组成。对每个桶，记录：

```text
mean(T,H)       = 平均 Delta_M
variance(T,H)   = 平均 (Delta_M - mean)^2
Z(X,H)          = (Delta_M - mean) / sqrt(variance)
```

若经验方差为零，该桶必须显式标记为退化，不能构造 `Z` 或报告高斯拟合。

同时按 squarefree 素因子层数分解：

```text
mu_r(n) = mu(n) * 1_{omega(n)=r}
Delta_{M,r}(X,H) = sum_{X<n<=X+H} mu_r(n)
```

全局增量恒等于所有有限活跃层的精确和：

```text
Delta_M(X,H) = sum_r Delta_{M,r}(X,H)
```

该精确分解只说明代数叠加，不预设各层独立、正态或相互抵消。

## 数值审计轨

每个 `(T,H)` 桶必须报告下列可复现统计量及有效样本量：

```text
sign_bias                 = E[sign(Delta_M)]，零值单列
standardized_skewness     = E[Z^3]
excess_kurtosis           = E[Z^4] - 3
lag_covariance(u)         = Cov(Z(X,H), Z(X+u,H))
cross_scale_covariance    = Cov(Z(X,H), Z(X,H'))
tail_excess(a)            = P(|Z|>=a) - GaussianTail(a)
layer_covariance(r,s)     = Cov(Delta_{M,r}, Delta_{M,s})
layer_cumulant_defect     = 全局 cumulant 与各层/配对分拆之差
```

为避免单一零假设误导，审计必须同时使用三种基线：

1. **独立符号基线**：保留本桶的非零项数或方差尺度，但以独立对称符号替换；
2. **分层重排基线**：在固定 `omega(n)=r` 层内重排真实符号/贡献，保留层大小但破坏原位置关联；
3. **局部约束代理基线**：保留选定的小素数整除/不可整除约束，并显式声明保留了哪些局部结构。

任何“更接近正态”的结论都必须同时说明相对于哪一种基线、在哪个尺度桶、以及尾部样本量是否足够；不同基线给出不同结论时，结论只能标记为模型依赖。

## 理论合同轨

数值审计之外，定义尚未完成的充分条件门：

```text
ActualMertensBlockDefectToOffConstantCoerciveEnergyLawBeforeMellin
```

候选证明只有同时提供下列字段时，才可声称进入去常数能量阶段：

```text
fixed_actual_integer_embedding
exact_mobius_block_decomposition
deterministic_dyadic_block_family
uniform_signed_block_covariance_bound
uniform_higher_cumulant_defect_bound
uniform_large_deviation_or_high_moment_bound
explicit_layer_interaction_identity
noncircular_offconstant_coercive_energy_identity
scale_summability_to_mellin_norm
no_use_of_RH_or_zero_free_input
```

其中 `uniform_*` 必须给出量词、尺度范围、常数依赖和误差级数的可求和性；仅在有限计算窗口上成立的回归式不满足该合同。

## 条件性收缩路线

若能独立证明一个实际、非循环的能量 `E(T)` 与缺陷 `D(T)` 满足：

```text
E(T) >= c * ||offconstant_Mertens_block(T)||^2
E(2T) <= q * E(T) + D(T)
0 <= q < 1
sum_j D(2^j T) < infinity
```

则可以研究由离散尺度收缩到 Mellin 范数的转运。该路线仍需单独证明：

1. `E` 来自固定的实际整数数据，而不是由目标误差拟合；
2. 去常数投影不读取 `M(x)` 或 `psi(x)-x` 的待控值；
3. block 能量到 `psi(x)-x` 的转运具有精确、非循环的算术恒等式；
4. Mellin 半平面收缩不隐含 RH、显式公式的零点输入或零自由区。

在这些步骤全部完成前，结果只能称为“随机性缺陷审计”或“条件性充分条件”，不能称为 RH 证明。

## 失败同样有信息量

以下结果均是有效的研究输出：

- 稳定的偏度、超额峰度或重尾：拒绝独立高斯基线，要求定位对应的乘法相关来源；
- 显著跨尺度或跨层协方差：拒绝无条件独立叠加，要求建立精确相互作用恒等式；
- 代理模型与真实数据在局部约束保留后仍分离：说明缺陷不由该局部结构解释；
- 任何能量候选依赖待控前缀误差：按 MFAC 去常数循环审计拒绝。

这些失败不反驳 RH；它们只排除特定随机化/能量路线的充分性。

## 分阶段交付

### 阶段 A：`M(x)` 双轨审计

- 新建可复现审计器与单元测试；
- 输出 JSON 证书和 Markdown 说明；
- 计算尺度桶统计量、三种基线与分层协方差；
- 检查证书是否把经验结论和定理合同严格分开；
- 默认状态为 `empirical_randomness_model_not_a_rh_proof`。

### 阶段 B：转运到 `psi(x)-x`

只有阶段 A 产生独立的确定性候选界后，才审计 Möbius 加权 divisor 展开到 Chebyshev 误差的精确转运；不得以数值拟合替代转运恒等式。

### 阶段 C：联合桥

仅当阶段 B 的转运和去常数能量均无循环后，才研究 `M(x)`、`psi(x)-x` 与 Mellin 范数的联合收缩。该阶段必须复用并通过现有自由 Mellin 反模型的排除条件。

## 初始实现边界

第一份实现只服务阶段 A，候选文件为：

```text
experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py
experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py
docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.json
docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.md
```

实现必须使用精确整数 Möbius 筛生成 `mu(n)`；随机基线要可设置种子；默认样本范围必须有限并在证书中记录。测试要覆盖：精确分层重构、退化方差拒绝、固定种子可复现、经验状态不能升级为 RH、以及任何缺失理论字段都不能报告实际 Mellin 收缩。

## 验收标准

1. 规格、代码、测试和证书均明确区分“经验基线”“条件性合同”“已证定理”；
2. 对每个样本桶，输出完整参数、样本量、零值数、方差和基线定义；
3. `sum_r Delta_{M,r}=Delta_M` 在每个审计块上精确验证；
4. 固定种子下代理统计量与证书逐次一致；
5. 缺少全部理论合同字段时，证书必须为 `actual_mellin_contraction_present=false`、`rh_proved=false`；
6. 不修改或重写既有 MFAC 去常数循环审计结论。
