# MFAC 中心化整除协方差强制性设计

**日期：** 2026-08-09

## 研究目标

将“素数分布的全局自筛、自反馈、自约束”表述为实际整数区间中的一个精确、可反驳的线性代数问题。目标不是把正半定性误称为 RH 证明，而是判断中心化整除特征的协方差核能否在增长索引窗中拥有统一的加权强制下界。

## 精确对象

给定整数 \(X\ge2\) 与 \(2\le d,e\le D\le X\)，定义

\[
A_X(d)=\left\lfloor\frac Xd\right\rfloor,
\qquad
K_X(d,e)=\left\lfloor\frac X{[d,e]}\right\rfloor,
\]

并定义中心化协方差核

\[
C_X(d,e)=K_X(d,e)-\frac{A_X(d)A_X(e)}X.
\]

对任意实系数 \(a=(a_d)_{2\le d\le D}\)，其二次型满足精确恒等式

\[
\sum_{d,e\le D}a_da_e C_X(d,e)
=\sum_{n\le X}
\left(
\sum_{d\le D}a_d\mathbf 1_{d\mid n}
-\frac1X\sum_{d\le D}a_dA_X(d)
\right)^2.
\]

右端非负是“自约束”的唯一已确认来源：每个整除筛选事件同时通过公共倍数重叠进入全局方差。该恒等式本身不包含 Möbius 消去、Chebyshev 误差界、Mellin 收缩或零点信息。

## 待证主命题

定义加权最小强制比

\[
\lambda_*(X,D)=
\inf_{a\ne0}
\frac{\sum_{d,e\le D}a_da_eC_X(d,e)}
{X\sum_{d\le D}a_d^2/d}.
\]

研究命题为：是否存在明确的 \(\theta>0\)、\(c>0\) 与 \(X_0\)，使得对所有
\(X\ge X_0\) 都有

\[
\lambda_*(X,\lfloor X^\theta\rfloor)\ge c?
\]

该命题尚未证明。有限 `X,D` 扫描只能估计或反驳候选尺度，不可外推为该全称命题。

## 自筛—反馈—波动机制

| 术语 | 精确对应 | 可审计输出 |
| --- | --- | --- |
| 自筛 | `d|n` 的局部整除特征与其中心化 | `A_X(d)`、候选索引窗 |
| 自反馈 | 两个筛选条件的交集由 `[d,e]|n` 给出 | `K_X(d,e)` 与 `C_X(d,e)` |
| 自约束 | 中心化总负载的平方和 | 精确方差二次型、主子式、广义特征值 |
| 波动极限 | `lambda_*(X,D(X))` 的尺度剖面或退化率 | 下确界、最坏向量、dyadic 比率 |

此处“波动极限”仅指可计算强制比的尺度行为，不是对 \(M(X)\)、\(\psi(X)-X\) 或素数间隔的已证极限律。

## 三阶段研究设计

### 阶段 A：精确谱剖面与反例搜索

对 \(D=\lfloor X^\theta\rfloor\) 的多个固定 \(\theta\) 值，使用精确有理数生成 `C_X`、加权广义 Gram 数据、主子式、最坏近似特征向量及其支持模式。扫描必须输出尺度窗口、浮点估计误差说明与原始精确条目。

**成功判据：** 找到可复算的正下界候选或显式退化向量；二者都属于有效研究结果。

### 阶段 B：尺度反馈命题

比较 \((X,D)\) 与 \((2X,\lfloor(2X)^\theta\rfloor)\)，将差异拆成：旧索引核条目的 floor 跳变、新增索引壳层、中心化均值变化。目标是提出可逐项证明或逐项否定的递推不等式；不得由数值单调性直接推断全尺度下界。

### 阶段 C：与算术误差的非循环桥接

仅在阶段 A/B 得到独立统一强制性定理后，研究 Möbius--von Mangoldt 除数恒等式是否能产生一个进入 `C_X` 能量的对象。候选构造不得读取 `psi(X)-X`、`Chebyshev_error`、`Mellin`、`zeta_zero` 或 `explicit_formula`。

## 拒绝条件与退出准则

- 若存在 \(X_j\to\infty\) 与归一化向量 \(a^{(j)}\) 使 \(\lambda_*(X_j,D(X_j))\to0\)，则当前权重/索引窗的统一命题失败，必须记录退化机制而非更换措辞。
- 若正下界只能在固定有限窗观察到，状态为 `finite_profile_only`。
- 即使主命题成立，若无法建立非循环的 Chebyshev 能量桥接，仍不得讨论 Mellin 收缩。

## 不变量

```text
finite_covariance_identity_available=true
uniform_weighted_coercivity_proved=false
actual_chebyshev_energy_bridge_proved=false
actual_mellin_contraction_present=false
rh_proved=false
```

## 使用示例

后续审计器的目标调用形式为：

```bash
python3 experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py \
  --limit 4096 --theta 0.25 --json-out /tmp/covariance.json
```

该命令的合法输出只能是有限尺度的谱剖面或退化证书，不是 RH 结论。
