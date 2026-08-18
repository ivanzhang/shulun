# MFAC 截断 Möbius--log 系数族强制性设计

**日期：** 2026-08-12

**状态：** 已确认，待用户审阅书面规格

## 1. 目的

本规格推进 MFAC 闭环攻击面中的 W1（结构化强制性）。目标是对一个固定、可复算且不读取目标误差的截断 Möbius--log 系数族，建立或证伪中心化整除能量的统一下界。

本工作不证明 Chebyshev 误差界、Mellin 收缩、零自由半平面或 RH。有限尺度扫描只能作为反例搜索或有限证书，不能升级为全尺度定理。

## 2. 固定对象与依赖合同

取固定参数

\[
0<\vartheta<\tfrac12,\qquad D_X=\lfloor X^\vartheta\rfloor,
\]

并取一次固定的截断函数 \(w:[0,1]\to\mathbb R\)。初始允许类为满足

\[
\lVert w\rVert_\infty\le 1,\qquad
\operatorname{Lip}(w)\le L,\qquad
w(0)=1,\quad w(1)=0
\]

的有理分段线性函数，其中 \(L\) 是预注册常数。为防止事后选择，第一轮只使用

\[
w_\star(u)=1-u.
\]

对 \(2\le d\le D_X\)，定义

\[
a^{(w)}_{X,d}=-\mu(d)\log d\;w\!\left(\frac{\log d}{\log D_X}\right).
\]

该构造只允许读取 `X`、`d`、整数分解得到的 \(\mu(d)\)、自然对数和预先固定的 \(w\)。以下输入一律禁止：

```text
psi(X)-X
Chebyshev_error
Mellin
zeta_zero
explicit_formula
RH
任何由目标误差拟合、反推或校准的参数
```

## 3. 精确能量与主命题

定义中心化整除负载

\[
F_{X,w}(n)=
\sum_{2\le d\le D_X}a^{(w)}_{X,d}
\left(\mathbf 1_{d\mid n}-\frac{\lfloor X/d\rfloor}{X}\right),
\]

及其精确有限能量

\[
Q_X(w)=\sum_{n\le X}|F_{X,w}(n)|^2.
\]

它等价于中心化协方差二次型

\[
Q_X(w)=
\sum_{d,e\le D_X}a^{(w)}_{X,d}a^{(w)}_{X,e}
\left(
\left\lfloor\frac X{[d,e]}\right\rfloor-
\frac{\lfloor X/d\rfloor\lfloor X/e\rfloor}{X}
\right).
\]

定义加权质量

\[
N_X(w)=X\sum_{2\le d\le D_X}\frac{|a^{(w)}_{X,d}|^2}{d}.
\]

本轮待证/待证伪命题为：是否存在明确常数
\(c>0\)、\(\eta\in[0,1)\) 与 \(X_0\)，使得全部 \(X\ge X_0\) 都满足

\[
Q_X(w_\star)\ge cN_X(w_\star)-R_X,
\qquad 0\le R_X\le \eta cN_X(w_\star).
\]

等价地，必须给出严格正的、尺度一致的有效常数 \(c(1-\eta)\)。若只能得到随 \(X\) 消失的常数，或只在有限窗口成立，则命题不成立或状态只能是 `numerical_only`。

## 4. 允许的辅助分解

为了证明或证伪主命题，可将核拆成极限部分和取整误差：

\[
\frac1X C_X(d,e)=
\frac{(d,e)}{[d,e]}-\frac1{de}+E_X(d,e).
\]

每一项的上界必须只由 `floor` 恒等式、\(d,e\le D_X\) 及已声明的初等估计推出。若采用筛法、均值值定理或其他外部结果，须逐条记录定理原文、适用范围及使用位置。

不允许以有限维最小特征值、拟合幂律或数值趋势替代此处所需的全称不等式。

## 5. 双向审计

### 正向义务

1. 对 \(w_\star\) 明确给出 \(c,\eta,X_0\) 和 \(R_X\) 的公式或上界；
2. 将所有隐常数表示为仅依赖 \(\vartheta,L\) 与已命名外部定理的常数；
3. 证明截断系数在后续确定性 Chebyshev 桥接中可被逐项嵌入，或诚实标记该接口尚未建立；
4. 输出机器可读 `uses` 合同，验证禁止输入未出现。

### 反向义务

1. 计算并保存有限尺度比率 \(Q_X(w_\star)/N_X(w_\star)\)，不将其外推为证明；
2. 将平方自由 Möbius、primorial、单素数层与高约数复合数方向作为对照见证，与本系数族分开报告；
3. 若发现一列明确的 \(X_j\to\infty\) 和解析可验证上界使比率趋于零，则将该具体命题标记为 `refuted`；
4. 不因全空间统一谱隙失败而推断本受限系数族失败，也不因本族有限正值而推断全空间谱隙成立。

## 6. 状态协议与停止条件

初始状态固定为：

```text
coefficient_family_status=specified
coefficient_independence_verified=false
structured_coercivity_status=unproved
finite_profile_status=not_run
chebyshev_bridge_status=not_started
mellin_status=not_started
rh_proved=false
```

只有完成独立的解析证明后，`structured_coercivity_status` 才能变为 `proved`。下列任一情形必须停止正向升级：

- 系数、截断点或权重读取被禁止输入；
- 余项无法相对主项一致吸收；
- 最佳下界常数随尺度趋零；
- 证明只覆盖有限 \(X\) 或数值样本；
- 后续桥接在代数重排中重新使用待估的 Chebyshev 误差。

## 7. 分阶段交付

1. **合同与精确计算：** 实现 \(a^{(w_\star)}\)、\(Q_X\)、\(N_X\)、依赖审计和精确小尺度恒等式测试；
2. **有限反例压力测试：** 生成有限尺度剖面和四类退化见证对照；
3. **解析余项预算：** 单独证明核极限近似和余项可吸收所需范围；
4. **主不等式审计：** 仅当第三步给出足够强的解析界后，尝试给出 \(c,\eta,X_0\) 或明确反证；
5. **桥接接口：** 仅在主不等式为 `proved` 后，研究无循环 Chebyshev 嵌入。

## 8. 验收标准

- 所有计算输出都附带参数 \(X,\vartheta,w_\star\) 与 `uses`；
- 小尺度上，直接平方和与协方差二次型严格一致；
- 禁止输入会被合同审计拒绝；
- 有限结果始终标为 `numerical_only`；
- 任何正向解析结论显式给出量词、常数、范围和余项来源；
- 所有产物保持 `rh_proved=false`，直至 W1、W2、W3 各自完成独立定理。

## 使用示例

计划中的审计命令形式：

```bash
python3 experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py \
  --limit 4096 --theta 0.25 --window linear --json-out /tmp/mfac-coercivity.json
```

该命令只能输出固定 \(X\) 的精确能量、归一化比率、依赖合同和有限证书；不会输出 Chebyshev、Mellin 或 RH 的正向结论。
