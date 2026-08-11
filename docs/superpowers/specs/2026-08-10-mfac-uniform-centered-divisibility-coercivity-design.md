# MFAC 中心化整除协方差统一强制性双轨审计设计

**日期：** 2026-08-10

## 研究目标

将当前有限尺度的中心化整除协方差谱读数，缩减为一个精确、可证伪且不读取
Chebyshev 误差、Mellin、零点或显式公式的统一强制性问题。研究首先要判断朴素的
常数谱隙是否成立；若不成立，必须给出可复算的衰减证书，并将正向目标收缩到带明确
尺度损失的最强幸存版本。

本设计不把有限计算、经验趋势或后验拟合升级为外部定理，更不构成 Mellin 收缩、
零点排除或 RH 证明。

## 精确对象与目标命题

对整数 `X >= 2`、`2 <= d,e <= D <= X`，沿用现有精确中心化核

\[
C_X(d,e)=\left\lfloor\frac{X}{[d,e]}\right\rfloor-
\frac{\left\lfloor X/d\right\rfloor\left\lfloor X/e\right\rfloor}{X}.
\]

定义标准化有限核与其算术极限核：

\[
K_X(d,e)=\frac{\sqrt{de}}{X}C_X(d,e),\qquad
K_\infty(d,e)=\frac{\gcd(d,e)-1}{\sqrt{de}}.
\]

给定 `0 < theta < 1`，令 `D=floor(X^theta)`。本轮的中心问题是：

> **UDC（待审计，不预设为真）**：是否存在独立于 `D` 的常数 `c > 0`，使得
> \(\lambda_{\min}(K_\infty^{[2,D]})\ge c\) 对所有 `D >= 2` 成立？

只有 UDC 获得完整、独立的解析证明，才可将相应的常数下界经由有限尺度误差转回
`K_X`。反之，必须记录最小特征值衰减，而不得以有限正性代替统一强制性。

## 双轨设计

### 轨道 A：有限尺度归约与反例搜索

1. 从取整项直接推导 `K_X-K_infinity` 的逐项误差，再给出可检查的算子范数上界
   `E(X,D)`；禁止从数值拟合声称误差阶。
2. 在 `D` 的增长序列上计算 `K_infinity` 的最小特征值、对应向量和 Rayleigh 比。
3. 按整除结构、素数层与高约数复合数层分类近退化支持，尝试抽取明确的候选向量族。
4. 对每个候选族，在精确或带验证误差的数值框架中输出可重算证书；只记录“反例候选”
   直到获得对全部尺度成立的解析论证。

### 轨道 B：极限核的正向下界

使用恒等式

\[
\gcd(d,e)-1=\sum_{\substack{q\mid d,\ q\mid e\\q\ge2}}\varphi(q)
\]

将极限二次型写成整除关联矩阵的加权平方和。研究以下两种互斥结果：

1. 给出与 `D` 无关的逆矩阵/最小奇异值控制，从而证明 UDC；或
2. 证明这种控制必然随 `D` 衰减，并显式给出最强有效损失函数 `c(D)`。

任何正向界必须列出常数的来源、适用向量空间、权重和全部边界项；不得由有限谱读数
或随机代理外推。

## 交付物

- 一个只处理 `K_X`、`K_infinity`、误差上界和 Rayleigh 证书的新审计模块及单元测试。
- JSON 证书：参数、矩阵定义、误差界、最小谱读数、候选支持和禁止升级状态。
- Markdown 说明：归约证明、反例候选、正向分解与未闭合义务。
- `external-theorem-index.md` 中只新增审计状态，不修改既有 RH 主线结论。

## 验收条件

- 有限尺度归约以精确公式或逐项可验证不等式实现；其误差不依赖 Chebyshev/Mellin 输入。
- 反例侧的每项证书均可用固定参数独立复算，并包含候选向量与 Rayleigh 比。
- 正向侧要么给出完整证明，要么明确标记为未证明并输出最强已证损失。
- 所有默认产物必须保留：

```text
uniform_centered_divisibility_coercivity_proved=false
actual_chebyshev_energy_bridge_proved=false
actual_mellin_contraction_present=false
rh_proved=false
```

## 使用示例（规划后的接口）

```bash
python3 experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit.py \
  --limit 4096 --theta 0.25 --mode both
```

该命令预期只生成有限尺度归约和候选谱证书；它不接受、也不读取任何 RH 目标量。

## 非目标

- 不构造 Chebyshev 误差到能量的桥接。
- 不构造 dyadic 到 Mellin 的可和性引理。
- 不宣称零点排除、Mellin 收缩或 RH。
- 不通过修改既有有限协方差模块来掩盖统一性缺口。
