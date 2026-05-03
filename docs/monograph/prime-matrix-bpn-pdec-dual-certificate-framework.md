# BPN-PDEC Fourier 上界双证书框架

**状态：** `pdec_upper_reduced_to_explicit_or_dual_certificate`

本文专攻 `PDEC-Cert` 的真正硬点：

\[
\max_{h\ne0}|\widehat{1_S}(h)|
\le \mathcal U_{\rm CRT}
<
\mathcal L_{\rm PDEC}.
\]

核心结论是：`PDEC` 不能只靠“完整 CRT 周期均衡”排除；必须提交同一坏窗集合 `S`
的显式 Fourier 上界证书，或提交对所有允许坏窗集合统一有效的对偶上界证书。

## 1. 为什么全周期均衡不足

完整 CRT 均衡只给出全周期背景集合的非零 Fourier 系数为零或很小。但 `PDEC` 中的对象是
坏窗指示函数 `1_S`，其中 `S` 是由边界零行诱导出的缺陷窗口族。即使背景全集均衡，
子集 `S` 仍可能在某个低模频率上高度集中。

因此以下推理是无效的：

```text
CRT full period balanced
=> every bad-window subset balanced。
```

有效证明必须利用 `S` 的来源约束：

```text
S is induced by boundary zero rows
+ mirror endpoint rigidity
+ column nonzero residue balance
+ tail-anchor non-reuse
+ core-overlap return
+ Rankin low-mod spike routing。
```

## 2. 显式 PDEC 证书

令 `Q` 为低模周期，`g(t)=#{x in S: tau(x)=t}`。定义

\[
\widehat g(h)=\sum_{t\bmod Q}g(t)e^{2\pi iht/Q}.
\]

已由 PDEC persistent 分支给出下界

\[
\mathcal L_{\rm PDEC}
=
{\kappa |S|\over \sqrt{Q-1}\|F\|_2}.
\]

**Definition PDEC-Explicit-Cert。**
一个显式证书包含：

```text
Q, kappa, ||F||_2, count vector g(0),...,g(Q-1), claimed U_CRT。
```

并通过以下验收：

\[
\max_{1\le h<Q}|\widehat g(h)|\le U_{\rm CRT}<\mathcal L_{\rm PDEC}.
\]

**Theorem PDU-1（显式 PDEC 证书验收）。**
若某 persistent 缺陷块的坏窗相位计数向量 `g` 通过 `PDEC-Explicit-Cert`，则该
persistent 分支不可能发生。

**证明。**
Persistent 分支强制存在非零频率满足
`|\widehat g(h)|>=L_PDEC`；显式证书又给出所有非零频率 `<L_PDEC`。矛盾。证毕。

该证书适合有限验证、有限候选族、或由正式反例链实际抽出的坏窗集合。

## 3. 对偶 PDEC 证书

显式证书只验证一个具体 `S`。要证明无限族，需要证明所有满足结构约束的 `g` 都满足同一
Fourier 上界。

设允许坏窗计数向量满足线性约束

\[
Ag\le b,\qquad Eg=e,\qquad g(t)\ge0.
\]

这些约束应来自：

- 镜像两端帽；
- 列非零同余类均衡；
- 尾锚不可复用容量；
- 固定核心高重叠回流；
- Rankin 失败相位尖峰已转入 low-mod core CRTDefect。

对每个非零频率 `h` 与单位复数 `zeta`，若存在非负对偶权重 `lambda>=0` 和自由权重
`mu`，使得逐相位成立

\[
\Re\{\zeta e^{2\pi iht/Q}\}
\le
(A^\top\lambda)(t)+(E^\top\mu)(t),
\]

且

\[
\lambda\cdot b+\mu\cdot e\le U_{\rm CRT},
\]

则

\[
\Re\{\zeta\widehat g(h)\}\le U_{\rm CRT}
\]

对所有允许 `g` 成立。若该证书对所有 `h\ne0` 和单位方向 `zeta` 成立，则得到
`|\widehat g(h)|<=U_CRT`。

**Theorem PDU-2（对偶 PDEC 证书验收）。**
若允许坏窗族的约束系统存在上述对偶主控证书，并且
`U_CRT<L_PDEC`，则对应 persistent PDEC 分支被排除。

**证明。**
逐相位不等式乘以 `g(t)>=0` 后求和，得到每个方向投影
`\Re{\zeta \widehat g(h)}<=U_CRT`。对所有单位方向取上确界得到
`|\widehat g(h)|<=U_CRT`。再与 PDEC 下界矛盾。证毕。

## 4. 方向连续性的处理

单位方向 `zeta` 连续，正式稿不能只检查有限角度网格。可接受方案有两种：

1. **解析主控：** 给出对任意 `zeta` 的闭式对偶权重；
2. **外向角弧证书：** 用有限角弧覆盖单位圆，并在每个角弧上加入余弦 Lipschitz 外向误差。

第二种证书必须明确角弧半径 `delta`，并把误差

\[
\sum_t g(t)\cdot O(\delta)
\]

纳入 `U_CRT`，不得用浮点网格直接替代连续方向。

## 5. 当前最小硬点

`PDEC` 的最终硬点现在压缩为：

```text
构造来自边界零行的允许坏窗约束 A,E,b,e；
提交 PDEC-Explicit-Cert 或 PDEC-Dual-Cert；
核验 U_CRT<L_PDEC。
```

若无法构造该证书，则必须输出失败的频率、相位方向和约束松弛项；该失败项就是下一轮
应回流的 `SAE` 或 `Rankin low-mod spike` 目标。

## 6. 约束账本与机器审计

补充文档 `prime-matrix-bpn-pdec-constraint-ledger.md` 已把对偶约束拆成五类原子：

```text
mass；
mirror；
column-balance；
tail-anchor non-reuse；
core-overlap / Rankin low-mod routing。
```

脚本 `experiments/prime_matrix_bpn_pdec_dual_certificate_audit.py` 已提供有限对偶证书审计：

```text
输入 A,b,E,e 和每个 h,zeta 的 lambda,mu；
逐相位验证 c_{h,zeta}(t)<=A^T lambda+E^T mu；
计算 U_dual=lambda*b+mu*e；
核验 U_dual<L_PDEC。
```

该脚本只验证“给定线性约束下”的对偶证明。正式无条件闭合仍需逐条证明这些线性约束
确实由边界零行结构强制产生，并覆盖全部非零频率和连续方向。
