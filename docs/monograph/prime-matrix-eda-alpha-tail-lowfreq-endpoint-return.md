# AlphaTail 低频模型错配返回端点 PDEC

**状态：** `alpha_tail_lowfreq_endpoint_return_proved`

本文处理频率分割合同中的 `LowFreq-ModelMismatch`。结论：低频模型错配不是新黑箱；把互补因子
变量重新求和后，它精确等于原始 dyadic 端点 sawtooth 缺陷。

## 1. 固定 d 的精确计数

固定高块 `I=(B,2B]`、`B>H=p-1`，以及 `D subset I`。令

\[
S(D)=\#\{(m,d):d\in D,\ 1\le md-p^2\le H\}.
\tag{LFE-1}
\]

对固定 `d`，

\[
\#\{m:1\le md-p^2\le H\}
=
\left\lfloor {p^2+H\over d}\right\rfloor
-
\left\lfloor {p^2\over d}\right\rfloor.
\tag{LFE-2}
\]

因此

\[
S(D)=
\sum_{d\in D}
\left(
\left\lfloor {p^2+H\over d}\right\rfloor
-
\left\lfloor {p^2\over d}\right\rfloor
\right).
\tag{LFE-3}
\]

## 2. Sawtooth 恒等式

由 `floor(x)-x=-{x}` 得

\[
\left\lfloor {p^2+H\over d}\right\rfloor
-
\left\lfloor {p^2\over d}\right\rfloor
-
{H\over d}
=
\left\{ {p^2\over d}\right\}
-
\left\{ {p^2+H\over d}\right\}.
\tag{LFE-4}
\]

所以

\[
S(D)-H\sum_{d\in D}{1\over d}
=
\sum_{d\in D}
\left(
\left\{ {p^2\over d}\right\}
-
\left\{ {p^2+H\over d}\right\}
\right).
\tag{LFE-5}
\]

右侧正是端点 sawtooth 缺陷。

## 3. 与高块单命中的一致性

因 `d>H`，固定 `d` 在短窗中至多命中一次。令 `rho_d(p)` 为 `-p^2 mod d` 的正代表，则

\[
\left\lfloor {p^2+H\over d}\right\rfloor
-
\left\lfloor {p^2\over d}\right\rfloor
=\mathbf 1_{\rho_d(p)\le H}.
\tag{LFE-6}
\]

于是 `(LFE-5)` 等同于

\[
\sum_{d\in D}\left(\mathbf 1_{\rho_d(p)\le H}-{H\over d}\right),
\tag{LFE-7}
\]

即 `HDL` 中的端点 PDEC 对象。

## 4. 频率分割的闭环

频率分割合同中的低频大值，本质上是在 Fourier 侧重建 `(LFE-5)` 的平滑端点贡献。因此：

```text
LowFreq-ModelMismatch
=> Endpoint sawtooth defect
=> dyadic PDEC / SAE.
```

这一步消除了一个潜在黑箱：低频分支不需要新的素数分布输入，也不需要新的大筛估计；它回到已经
命名的端点缺陷。

## 5. 当前剩余

低频分支已经回流。剩余高频分支为：

```text
HighFreq-BohrCap:
对低素 squarefree 高块 D，排斥差集 Bohr-cap 聚集，
或证明聚集触发 ColumnCRT/PDEC/SAE 并被排斥。
```

因此 AlphaTail 当前最窄未闭合点不再是低频模型错配，而是高频 Bohr-cap 差集聚集。
