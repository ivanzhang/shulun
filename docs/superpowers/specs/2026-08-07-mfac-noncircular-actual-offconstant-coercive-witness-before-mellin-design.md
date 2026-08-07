# MFAC 非循环实际去常数强制见证（Mellin 前）设计

## 目标

在有限实际整数 LCM Gram 模型中构造一个不读取
\(\psi(X)-X\)、Mellin 数据、零点数据或任何等价目标误差的去常数见证；
对该见证给出精确正能量恒等式与显式强制下界。该成果只打开
`NoncircularActualOffConstantCoerciveWitnessBeforeMellin` 正向门。

## 前置状态

基线为 `ed281b04`。其前一审计已证明：直接用目标误差确定的 \(e_1\)
投影系数是循环的，不能作为非循环见证。新审计不复用该目标依赖系数。

## 数学对象

对整数 \(X\ge 2\)，令

\[
K_X(d,e)=\left\lfloor\frac{X}{\operatorname{lcm}(d,e)}\right\rfloor,
\qquad m_X=\left\lfloor\frac X2\right\rfloor,
\qquad a_X=\frac{m_X}{X}.
\]

取标准基向量 \(e_1,e_2\)，定义实际去常数见证

\[
h_X=e_2-a_Xe_1.
\]

其系数只读取 `X` 以及等价的实际 Gram 条目
\(K_X(1,1)=X\)、\(K_X(1,2)=m_X\)，不读取任何 Chebyshev 误差或解析输入。

审计必须精确验证

\[
\langle h_X,e_1\rangle_{K_X}=m_X-a_XX=0,
\]

以及

\[
\lVert h_X\rVert_{K_X}^2
=m_X-\frac{m_X^2}{X}
=\frac{m_X(X-m_X)}{X}
\ge \frac{2X}{9}>0.
\]

因此，对任意实数 \(t\)，限制在此一维实际见证方向上的二次型满足

\[
\langle th_X,th_X\rangle_{K_X}
\ge \frac{2X}{9}t^2.
\]

## 实现边界

- 新模块只实现有限整数、LCM Gram 和一维见证方向的精确/有理数审计。
- 见证数据接口返回系数来源、正交残差、精确能量、强制下界和方向性结论。
- 依赖合同接口只接受非裸字符串的字符串可迭代输入；若输入含
  `psi(X)-X`、`Chebyshev_error`、`Mellin`、`zeta_zero` 或定义的同义禁止项，
  则把候选分类为循环/禁止，绝不把它标记为已构造的非循环见证。
- 证书写入 JSON 与 Markdown，明确记录该见证在 `Mellin` 之前构造，及其
  不依赖的输入集合。
- 更新 MFAC 状态表和外部定理索引，使该正向门可追溯。

## 非目标与结论限制

- 不声称整个去常数子空间存在统一谱隙或全空间强制性。
- 不把一维见证能量转译成 \(\psi(X)-X\) 的界。
- 不使用 Mellin 反演、零点信息或任何 RH 等价命题。
- 不声称 `actual_chebyshev_mellin_contraction`、RH 或数学上的完整闭合。

## 测试与验收

1. 在偶数和奇数 `X` 上验证正交恒等式、精确能量公式与 \(2X/9\) 下界。
2. 验证任意标量倍数的方向性强制公式。
3. 验证仅算术/Gram 依赖的合同获准，目标、Mellin 和零点依赖均被拒绝。
4. 验证输入类型与有限性防御，以及 JSON/Markdown 证书字段。
5. 运行新增模块的隔离测试，再运行 MFAC 全族 70/70 测试。
6. 独立审查确认：没有从 \(\psi(X)-X\) 到见证系数或强制常数的隐藏数据路径。
