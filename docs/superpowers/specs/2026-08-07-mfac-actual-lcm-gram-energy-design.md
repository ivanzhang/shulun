# MFAC 实际 LCM Gram 能量与常数方向障碍审计设计

**状态：** `implemented_and_archived_non_rh_boundary_preserved`

## 1. 研究目标

本轮只攻击自由 Mellin 反模型之后最短、最诚实的实际整数前置门：

```text
ActualLCMGramEnergyAndConstantDirectionObstructionBeforeMellin
```

目标不是证明 RH，也不是证明所有可能的实际收缩律都不存在。目标是从实际自然数上的 Euler--Möbius 分解中提取一个不带人工标签的正半定 LCM Gram 核，并精确审计它是否足以控制 Chebyshev 误差的常数方向。

## 2. 固定实际对象与精确恒等式

令 `X` 为正整数，`d,e` 为不超过 `X` 的正整数。使用：

```text
Lambda(n) = -sum_{d | n} mu(d) log(d)
psi(X) = sum_{n <= X} Lambda(n)
```

定义实际 LCM Gram 核：

```text
K_X(d,e) = floor(X / lcm(d,e)).
```

它来自实际可整除指示函数的 Gram 表示：

```text
K_X(d,e) = sum_{n <= X} 1_{d | n} 1_{e | n}.
```

因此对任意有限实向量 `c` 有：

```text
sum_{d,e <= X} c_d c_e K_X(d,e)
= sum_{n <= X} (sum_{d | n} c_d)^2 >= 0.
```

令 `w_d = -mu(d) log(d)`，则存在逐点可复算的实际恒等式：

```text
sum_{d,e <= X} w_d w_e K_X(d,e)
= sum_{n <= X} Lambda(n)^2.
```

该恒等式给出实际整数嵌入、固定计数测度和非标签化正半定带符号核；但尚未给出 Chebyshev 误差的平方根收缩。

## 3. 最小障碍命题

定义实际 Chebyshev 增量：

```text
a_n = Lambda(n) - 1,
E_psi(X) = sum_{n <= X} a_n = psi(X) - X.
```

最基础的能量控制为：

```text
E_psi(X)^2 <= X * sum_{n <= X} a_n^2.
```

这里的求和泛函在实际 `ell^2({1,...,X})` 中对应常数向量 `(1,...,1)`，其范数精确为 `sqrt(X)`。因此，任何只把 `a` 放入这个未投影的正能量、再施用普通 Cauchy 的论证，都必须额外支付“常数方向消失”或“远强于局部 L2 的强制性”；正半定性本身不产生这种支付。

该结论是一个关于给定推理模板的精确算子范数障碍，不是关于实际 `E_psi(X)` 大小的否定结论。

## 4. 中心化候选的循环判据

审计器应允许候选中心化向量或核，但必须逐项登记其定义输入。

若候选中心化常数、投影或权重读取以下任何待控制对象：

```text
psi(X)
E_psi(X)
未证明的素数计数误差界
零点位置、零自由域或显式公式残差
```

则该候选被分类为：

```text
centered_kernel_uses_target_or_forbidden_analytic_input
```

它不能作为 `ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula` 的独立输入。该判据只排除循环定义；不排除未来从独立算术恒等式导出的真正正交分解。

## 5. 实施范围

新增一个审计模块及其单测，验证：

1. `K_X` 与实际可整除 Gram 表示逐项一致；
2. 小范围内对所有有界整数向量直接验证正半定恒等式；
3. Möbius 权重通过 LCM 核精确恢复 `sum Lambda(n)^2`；
4. 误差增量的 Cauchy 上界及常数向量范数精确成立；
5. `6 | n` 给出无穷多非 prime-power 位置的初等下界见证，防止把局部能量误报为消失能量；
6. 使用 `psi`、误差或零点输入的中心化候选被明确拒绝；
7. 证书将“得到实际 PSD 核”“普通 Cauchy 不足”“未证明全局非存在性”“RH 未证明”严格分层。

建议文件：

```text
experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py
experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py
docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.json
docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.md
```

并对 `claim-status-table.md` 与 `external-theorem-index.md` 追加边界记录。

## 6. 明确非目标

本轮不声称：

- `sum Lambda(n)^2` 的渐近式；
- `E_psi(X)=O(X^(1/2+epsilon))`；
- Mellin 半平面谱收缩；
- 零点排除；
- RH；
- 不存在任何未来可行的非 Cauchy、非循环实际收缩核。

只有在未来独立获得常数方向正交性、非退化强制能量和不依赖零点输入的 Mellin 收缩后，才可能进入下一层 `ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula`。

## 7. 验证命令

```bash
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
```
