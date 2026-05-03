# BPN 最终出口验收合约

**状态：** `final_exits_reduced_to_checkable_inequality_certificates`

本文把 `BPN-BK` 最后两个非证书出口写成可审稿的验收不等式：

```text
PDEC exclusion
+ SAE local escape exclusion。
```

本文不宣称这些不等式已经自动成立；它给出最终证明必须提交的精确定理格式。

## 1. PDEC 能量排斥证书

沿用统一低模测试函数框架。设 `Q` 为低模周期，`F` 为零均值测试函数，
坏窗集合 `S` 满足

\[
\Re F(\tau(x))\ge \kappa,\qquad x\in S.
\]

令 `\beta=|S|/|X|`。由统一 PDEC 定理，persistent 分支给出非零 Fourier 下界

\[
\mathcal L_{\rm PDEC}
=
\frac{\kappa |S|}{\sqrt{Q-1}\,\|F\|_2}.
\tag{1}
\]

**Definition PDEC-Cert（PDEC 排斥证书）。**
若能从 CRT 均衡、列见证、镜像端点刚性或已证方阵约束推出同一坏窗指示函数的
非零 Fourier 上界

\[
\max_{h\ne0}|\widehat{1_S}(h)|\le \mathcal U_{\rm CRT},
\tag{2}
\]

且

\[
\mathcal U_{\rm CRT}<\mathcal L_{\rm PDEC},
\tag{3}
\]

则该 PDEC 分支被排除。

**Theorem FXA-1（PDEC 验收）。**
若对每个 persistent 低模缺陷块都存在 `PDEC-Cert`，则所有 persistent 分支被排除。

**证明。**
Persistent 分支由 `(1)` 强制存在某个非零频率达到至少 `\mathcal L_{\rm PDEC}`；
证书 `(2)--(3)` 又要求所有非零频率都小于该值，矛盾。证毕。

因此 PDEC 的最终任务不是再重命名缺陷，而是提交上界 `(2)`，并核验严格余量 `(3)`。

## 2. SAE 局部逃逸证书

Sparse 分支只含少量孤立坏窗，不能靠全局 Fourier 能量排斥。对每个孤立坏窗 `I`
定义三类可接受证书。

**Definition SAE-Cert（单窗逃逸证书）。**
坏窗 `I` 通过 SAE 验收，若至少给出以下一项：

1. **Survivor 证书：** 明确给出 `n\in I`，满足

\[
\gcd(n,M_{<P})=1,
\]

且 `n` 不属于被允许排除的端点例外；

2. **Lift 证书：** 证明 `I` 的低模缺陷在相邻漂移窗或同相位窗中复现，因而 sparse
分支升级为 PDEC；

3. **Higher-defect 证书：** 证明 `I` 触发更高层尾锚复用、固定核心高重叠或
low-mod core CRTDefect，并已由前文桥接回 PDEC/SAE 主接口。

**Theorem FXA-2（SAE 验收）。**
若每个 sparse bad window 都有 `SAE-Cert`，则 sparse 分支被排除或回流到 PDEC
分支。

**证明。**
第 1 类直接否定坏窗为空；第 2 类把 sparse 假设改写成 persistent 分支，交给
`FXA-1`；第 3 类把单窗异常送入已建立的尾锚/core 低模桥，再回到统一 PDEC/SAE
二分。证毕。

## 3. Rankin 证书接入

Rankin 颜色类证书的最终验收规则为：

```text
rankin_budget_pass=true
=> 颜色类闭合；

rankin_budget_pass=false + low-mod spike
=> low-mod core CRTDefect
=> PDEC/SAE；

rankin_budget_pass=false + no spike
=> 常数账本未闭合，必须细分或调参。
```

因此 Rankin 失败不能被忽略。它要么转成最终出口，要么保留为常数缺口。

## 4. BPN-BK 最终闭合定理格式

**Theorem FXA-3（BPN-BK 最终验收合约）。**
若对某个素数范围或全体素数同时满足：

1. 所有正式着色走廊 Rankin 证书通过，或失败者已转入 `PDEC/SAE`；
2. 所有 persistent 低模缺陷块有 `PDEC-Cert`；
3. 所有 sparse bad window 有 `SAE-Cert`；

则 `BPN-BK` 链条排除边界零行，从而证明该范围内的 `BPN(P)`。

**证明。**
边界零行经前文链条必进入三类之一：Rankin 走廊预算失败、persistent 低模缺陷、
sparse 单窗逃逸。第 1 项处理 Rankin 分支，第 2 项排除 persistent 分支，第 3 项
排除或回流 sparse 分支。三类均无可存活反例，故边界零行不存在。证毕。

## 5. 审稿边界

当前真正未提交的是：

```text
具体 PDEC-Cert 上界；
具体 SAE-Cert 列表；
正式反例诱导走廊的 Rankin 证书全集。
```

因此 `BPN(P)` 仍不能标为无条件定理。但最终剩余已变成明确的证书型验收义务，
而不是新的未定义数学出口。
