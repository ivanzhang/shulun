# MFAC 全 ε Mertens 条件化 L²--Upper 说明

## 条件的精确量词

对每个 \(\varepsilon>0\)，假设存在 \(C_\varepsilon>0\)，使对所有
\(x\ge1\) 都有

\[
|M(x)|\le C_\varepsilon x^{1/2+\varepsilon},
\qquad M(x)=\sum_{n\le x}\mu(n).
\]

常数 \(C_\varepsilon\) 可以依赖 \(\varepsilon\)，但不得依赖截断 \(D\)；
本说明不声称这些常数对 \(\varepsilon\) 一致。审计器中的 `epsilon` 与
`mertens_constant` 只是这个全称命题的单个合法实例化记录，不能由有限计算
验证该假设。

## 已验证的有限层

既有 Möbius 尾和审计已对每个有限 \(D\) 验证 Euler--\(\varphi\) 分解

\[
E_D=\sum_{2\le r<D}\varphi(r)|T_D(r)|^2.
\]

这是有限代数重排，不使用 Mertens 型界、PNT、零点、显式公式、Mellin 或 RH。
有限恒等式本身不提供对 \(D\to\infty\) 的整体 L² 上界。

## 仍然开放的分析义务

即使接受全 ε Mertens 型假设，要进入整体 L²--Upper，也仍必须逐步证明：

1. 互素限制的 Möbius 和如何由 \(M(x)\) 控制；
2. 分部求和后对数权尾和的指数损失和常数依赖；
3. 各 \(r\) 的界如何在 \(\sum_r\varphi(r)|T_D(r)|^2\) 中聚合。

这三项分别登记为 `CoprimeRestrictedPartialSummation`、
`TailBoundWithParameterDependence` 和 `EulerPhiL2Aggregation`。在提供可逐步
核查的解析引理前，它们都是开放证明义务，而不是由合同字段自动证明的结论。

## 当前结论边界

当前产物只登记条件链：Mertens 型界是外部假设，条件 L²--Upper 链尚有开放
义务，无条件 L²--Upper 保持未证明。因此它不证明 Mertens 假设、
Mass--Lower、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py \
  --epsilon 0.1 \
  --mertens-constant 1.0
```

该命令生成条件链登记证书，不验证或证明 \(M(x)\) 的全局界。
