# BPN 尾锚持续化二分

**状态：** `tailanchor_reduced_to_sae_or_persistent_tail_defect`

本文处理 `Tail-anchor concentration` 出口。关键审稿点是：单个尾锚走廊可以存在，
不能仅凭完整 CRT 周期均衡排斥。因此必须证明：

```text
尾锚集中
=> 单窗锚逃逸 SAE
   或 Persistent Tail-anchor defect。
```

这一步把“单个异常走廊”与“可进入 CRT/Fourier 缺陷的持续异常”分开。

## 1. 饱和尾锚集合

沿用 `prime-matrix-bpn-tailcore-corridor-reduction.md`。固定边界短窗 `I`、核心尺度
`D_0` 与互补锚尺度 `A_0`。对互补因子 `a`，走廊为

\[
\mathcal J_a(I;D_0)=\{d:D_0\le d<2D_0,\ ad\in I\}.
\]

设 `W_a=|\mathcal J_a(I;D_0)\cap\mathbb Z|`。给定 `0<\theta\le1`，若

\[
N_a=\#\{d\in\mathcal J_a(I;D_0):d|M_{<P},\omega(d)\le K,\text{phase}(d)\}
\ge \theta W_a,
\]

称 `a` 为 `\theta`-饱和尾锚。饱和尾锚集合记为 `\mathcal A_\theta(I)`。

## 2. 单窗 SAE 与持续尾锚缺陷

取低模 `Q`，通常为若干小素数乘积。定义尾锚相位

\[
\rho_Q(a)=a\bmod Q.
\]

**Definition SAE-anchor（单窗锚逃逸）。**
若某个饱和尾锚 `a` 的贡献已经足以承担反例预算中指定比例 `\beta T`，但该锚没有在
邻近坏窗或同相位坏窗中复现，则称其触发单窗锚逃逸 `SAE-anchor`。

**Definition PTA（持续尾锚缺陷）。**
若存在低模相位 `\rho`，使

\[
\#\{a\in\mathcal A_\theta(I):a\equiv \rho\pmod Q\}\ge H_Q,
\]

则称触发 `Persistent Tail-anchor defect`，记为 `PTA(Q,\rho,H_Q)`。

该定义是尾锚版的 `PDEC`：不是单个端点值大，而是锚集合在低模相位上出现可被
Fourier/CRT 检测的集中。

## 3. 尾锚持续化二分

**Theorem TAD-1（尾锚集中二分）。**
设饱和尾锚总贡献为

\[
M_\theta(I)=\sum_{a\in\mathcal A_\theta(I)}N_a.
\]

给定参数 `\beta\in(0,1)`、低模 `Q` 与相位阈值 `H_Q`。若

\[
M_\theta(I)>T_{\rm anchor},
\tag{1}
\]

则至少发生以下一项：

1. 存在单锚 `a` 满足 `N_a>\beta T_anchor`，从而触发 `SAE-anchor`；
2. 存在相位 `\rho mod Q` 满足

\[
\#\{a\in\mathcal A_\theta(I):a\equiv \rho\pmod Q\}
>
\frac{(1-\beta)T_{\rm anchor}}{Q\,W_{\max}},
\tag{2}
\]

其中 `W_max=max_a W_a`。特别地，若

\[
H_Q\le \frac{(1-\beta)T_{\rm anchor}}{Q\,W_{\max}},
\]

则触发 `PTA(Q,\rho,H_Q)`。

**证明。**
若第一项不发生，则每个饱和尾锚贡献 `N_a<=\beta T_anchor`，且总贡献仍大于
`T_anchor`，所以除去任意单个锚后，剩余饱和锚总贡献大于
`(1-\beta)T_anchor`。又每个锚最多贡献 `W_max`，故饱和锚个数超过
`(1-\beta)T_anchor/W_max`。按 `Q` 个低模相位鸽巢，存在某个 `\rho` 中的锚数超过
`(1-\beta)T_anchor/(Q W_max)`。证毕。

## 4. PTA 到低模 Fourier 缺陷

令

\[
B_\rho(a)=1_{a\equiv\rho\pmod Q}-\frac1Q.
\]

若 `PTA(Q,\rho,H_Q)` 发生，且总饱和锚数为 `A`，则

\[
\sum_{a\in\mathcal A_\theta(I)}B_\rho(a)
\ge H_Q-\frac{A}{Q}.
\tag{3}
\]

当右侧为正比例时，饱和锚指示函数与非平凡低模函数相关。将 `B_\rho` 展开为模 `Q`
的非平凡加性角色，即得到尾锚版 `Directed CRTDefect`。

因此：

```text
Persistent Tail-anchor defect
=> low-mod Fourier/CRT defect。
```

这一步是确定 Fourier 分解，不使用启发式。

## 5. 当前剩余

本文已严格证明：

```text
Tail-anchor concentration
=> SAE-anchor
   或 Persistent Tail-anchor defect
=> SAE
   或 Directed CRTDefect。
```

因此尾锚出口已经并回主链的同一个最终硬点：

```text
PDEC-or-SAE 排斥。
```

剩余不是“尾锚如何命名”，而是最终排斥：

1. 证明 `SAE-anchor` 不可能单独承担边界零行反例；
2. 证明 `Persistent Tail-anchor defect` 与已证 CRT/列见证/端点刚性冲突。
