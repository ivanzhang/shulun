# MFAC 全局自由乘法 Mellin 增长模反模型设计

## 目标

把下列精确 divisor-lattice 交替展开与 RH 级平方根消去严格分开：

```text
psi(x) = -sum_{d<=x} mu(d) log(d) floor(x/d)
```

建立一个条件性自由乘法反模型族：它保持唯一分解、Möbius 符号交替、全局 payload 守恒与多维 divisor 叠加，却允许 Chebyshev 型误差具有 `X^beta cos(tau log X)`（`1/2 < beta < 1`）的增长轮廓。该模型用于证明：若没有实际整数算术产生的 Mellin 收缩律，则“局部递推 + 符号交替 + 全局零和”不能单独排除 RH 外侧的增长模。

## 非目标

- 不构造自然数素数的反例，不反驳 RH，也不声称反模型对应实际 zeta 零点。
- 不把自由原子模型称为 Beurling 素数系的完整定理，除非另行给出离散化、Euler product 与解析延拓的独立证明。
- 不从 `X^beta cos(tau log X)` 的形式轮廓推出实际存在 `Re(rho)=beta` 的零点。
- 不证明 `psi(x)-x` 的平方根界、零点排除、行/列无条件命题或 RH。

## 精确的多维交替结构

在自然数上，下式为精确恒等式：

```text
Lambda(n) = -sum_{d|n} mu(d) log(d)
psi(x)    = -sum_{d<=x} mu(d) log(d) floor(x/d)
```

对 squarefree `d=p_1...p_r`，有 `-mu(d)=(-1)^(r+1)`，故第二式可看作所有维数 `r` 的素因子选择叠加。这个“多维波动 + 交替符号”仅规定了 divisor-lattice 的代数关系；它没有规定这些层在 Mellin 频率上必须相消，更没有给出能量耗散或谱半径上界。

## 自由乘法反模型的工作定义

令 `A` 是可数的、带标签的自由原子集合；每个原子 `a` 带正尺度 `N(a)>1`。要求存在 `lambda>1` 使 `N(a)>=lambda`，且对每个有限 `X`，集合 `{a in A:N(a)<=X}` 有限。由 `A` 生成自由交换单子 `M(A)`；这些局部有限条件保证对每个 `X`，满足 `N(m)<=X` 的单子元素有限，并定义：

```text
N(a_1^e1 ... a_k^ek) = N(a_1)^e1 ... N(a_k)^ek
mu_A(m) = 0                    若某个 ei>=2
mu_A(m) = (-1)^k               若 m 是 k 个不同原子的乘积
Lambda_A(m) = log N(a)         若 m=a^j, j>=1
Lambda_A(m) = 0                否则
```

于是对 `M(A)` 的每个元素仍有完全形式化的恒等式：

```text
Lambda_A(m) = -sum_{d|m} mu_A(d) log N(d)
```

并可按 `N(m)<=X` 定义自由 Chebyshev 函数 `psi_A(X)`。该身份只使用自由唯一分解，因此不蕴含 `A` 是自然数中的实际素数集合。

## 对抗性 Mellin 轮廓

固定参数：

```text
1/2 < beta < 1
tau != 0
0 < epsilon < 1
```

考虑目标一阶原子质量轮廓：

```text
Theta_target(X) = X + epsilon X^beta cos(tau log X)
```

其导数为：

```text
1 + epsilon X^(beta-1) [beta cos(tau log X) - tau sin(tau log X)]
```

由于 `beta<1`，对充分大的 `X`，该导数严格为正；有限前缀可单独调整。因此它可作为正的连续 shell 质量轮廓，或作为离散、带标签自由原子的近似目标。任何后续离散实现都必须明确记录其近似误差；本规格不把连续轮廓自动升级为真实 prime system。

在对数变量 `t=log X` 下，归一化增长模为：

```text
E_beta,tau(t) = e^(-t/2) [Theta_target(e^t) - e^t]
                = epsilon e^((beta-1/2)t) cos(tau t)
```

当 `beta>1/2` 时，该模不有界。它是一个 Mellin 型增长轮廓，不是实际零点存在的证明。

## 条件性 no-go 命题

令一个“全局递推证明系统”只使用：

1. 自由唯一分解与 divisor-lattice 关系；
2. Möbius 交替符号和 `Lambda=-mu*log`；
3. 有限层或所有层的形式叠加；
4. 对全局 payload 的总和守恒；
5. 不使用自然数嵌入、固定实际 Chebyshev 测度、实际 residue/trace 输入、Mellin 正定性或等价的谱收缩估计。

则该系统允许上述自由原子模型与 `beta>1/2` 的增长轮廓，故不能仅从这些公理推出：

```text
psi(x)-x = O_epsilon(x^(1/2+epsilon))
```

或任何可排除 `Re(rho)>1/2` 的等价估计。

该命题是关于公理强度的条件性结论，不是关于自然数素数的反例或 RH 否定。

## 必须额外支付的实际算术收缩门

要从多维交替结构直接攻击 RH，必须产生一个独立且非循环的：

```text
ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula
```

最低合同为：

```text
fixed_actual_integer_embedding
fixed_actual_chebyshev_measure
exact_error_recurrence_on_actual_rows
non_tagged_signed_kernel
positive_or_coercive_energy_identity
Mellin_half_plane_spectral_contraction
no_use_of_RH_or_zero_free_input
```

该合同必须说明为什么实际整数的递推不允许自由模型中的增长模，而不能仅把 `X^beta cos(tau log X)` 命名为“后续会相消”的波峰波谷。

## 与 MFAC source 门的关系

本反模型不取代：

```text
ActualAlphaDeltaRowRealizationRigidityBeforePushforward
SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

相反，它解释为何这些 source 门仍不可绕过：若 signed row 与其实际 alpha/delta 语义未被固定，自由原子模型可以任意制造带符号递推行；若没有可求和的 actual signed family，也没有办法从纯交替组合结构得到 Mellin 收缩。

## 最小审计设计

后续审计器要实现或检查：

1. 自由交换单子上的 `Lambda_A=-mu_A*log N` 逐点恒等式；
2. 最小多维 divisor 分层的符号交替与总和投影守恒；
3. `beta>1/2` Mellin 轮廓在归一化变量中的增长；
4. 自由模型没有 `fixed_actual_integer_embedding`，故不得被误报为 RH 反例；
5. 当前语料没有 `ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula`；
6. 完整 synthetic contraction fixture 只能验证合同判据，不表示实际整数上已证明收缩。

当前语料预期：

```text
exact_divisor_lattice_identity_available=true
free_mellin_growth_countermodel_constructed=true
alternation_only_implies_sqrt_cancellation=false
actual_chebyshev_mellin_contraction_present=false
mathematical_nonexistence_proved=false
rh_proved=false
row_column_unconditional_closed=false
next_positive_gate=ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula
```

## 产物与验证

用户审阅本规格后，实施阶段新增：

- `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py`
- `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py`
- `docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.json`
- `docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.md`

测试必须分别覆盖 exact identity、free-model 增长模、自然数嵌入缺失拒绝、synthetic contraction fixture 与 non-RH 边界。全族回归命令保持：

```bash
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
```
