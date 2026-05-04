# 互补因子负载的短区间化

**状态：** `alpha_tail_cofactor_intervalization_reduction_open`

本文把 `CofactorLoad` 再压缩一层。固定互补因子 `m` 后，列变量消失，负载完全等价于：

```text
低素平方自由数 d 落入一个长度约 (p-1)/m 的短区间。
```

这把高核心补洞问题从二维 `(k,d)` 几何，降成一族一维短区间的 squarefree-smooth 计数偏差。

## 1. 固定 m 的精确公式

沿用

\[
H=p-1,\qquad y=\lfloor0.9p\rfloor,\qquad I=(B,2B],\qquad B>H.
\tag{CIN-1}
\]

令

\[
\mathcal D_y^\pm=\{d:d\mid M_y,\ d\ {\rm squarefree},\ \mu(d)=\pm1\}.
\tag{CIN-2}
\]

由 `k=md-p^2` 可知，固定 `m` 时

\[
1\le k\le H
\quad\Longleftrightarrow\quad
{p^2\over m}<d\le {p^2+H\over m}.
\tag{CIN-3}
\]

因此互补因子负载有精确公式

\[
L_I^\pm(m)=
\#\left(
\mathcal D_y^\pm\cap I\cap
\left({p^2\over m},{p^2+H\over m}\right]
\right).
\tag{CIN-4}
\]

**证明。**  
`m in M_I^\pm(k)` 等价于 `d=n_k/m` 是整数、`d in I`、`d in D_y^\pm`。
把 `n_k=p^2+k` 代入，`1<=k<=H` 正好给出 `(CIN-3)`，于是得到 `(CIN-4)`。证毕。

## 2. 区间长度刚性

固定 `m` 的区间长度为

\[
\Delta_m={H\over m}.
\tag{CIN-5}
\]

而高块 `I=(B,2B]` 强制

\[
{p^2+1\over 2B}<m\le {p^2+H\over B}.
\tag{CIN-6}
\]

所以

\[
{B H\over p^2+H}
\le
\Delta_m
<
{2B H\over p^2+1}.
\tag{CIN-7}
\]

当 `B=lambda p` 时，`Delta_m` 被锁在约 `lambda` 到 `2lambda` 的常数长度区间。
这说明高块 CoreLoad 的每个互补因子只查看一段很短的 `d`-区间，不能自由复用长斜线覆盖能力。

## 3. WSS 缺陷定义

定义窗口化 squarefree-smooth 偏差

\[
\mathrm{WSS}_I^\pm(m)=
L_I^\pm(m)-
\sum_{d\in I\cap(p^2/m,(p^2+H)/m]\cap\mathcal D_y^\pm}{1\over d}\,m.
\tag{CIN-8}
\]

右侧第二项是把 harmonic 模型 `H/d` 在固定 `m` 的短区间中按局部长度 `H/m`
重标定后的期望量。它不作为已证均匀估计，只是定义偏差对象。

## 4. 过剩负载的区间化

若 `HCL-8` 成立，即

\[
\sum_m L_I^-(m)\ge H R_I^-+{\tau\over2},
\tag{CIN-9}
\]

则固定 `m` 的短区间计数总和超过全局 harmonic 模型。于是必有以下至少一项：

1. **短区间 WSS 过剩。**  
   某些 `m` 的 `WSS_I^-(m)` 为正且总量达到 `tau/4` 量级；
2. **模型错配。**  
   局部重标定模型与全局 harmonic 模型之间的差达到 `tau/4` 量级。

这是恒等式二分：把 `(CIN-9)` 中的 `L_I^-(m)` 加减 `(CIN-8)` 的局部模型后立即得到。

## 5. 结构意义

`CIN` 暴露了真正硬点：

```text
反例必须让大量长度约 B/p 的短区间
异常富含奇 Möbius 的 y-smooth squarefree 数。
```

如果这些短区间异常集中在少数 `m`，就是 `cofactor-anchor`；如果分散在许多 `m`，就是
`WSS/PDEC`。二者都比原始 “高标签覆盖能力” 更窄：

1. 区间端点由 `p^2/m` 刚性决定；
2. 区间长度由 `B/p` 刚性决定；
3. 被计数对象必须是 `<=0.9p` 素因子生成的 squarefree 数；
4. Möbius 奇偶符号还必须产生单向偏斜。

## 6. 审稿边界

已证明：

```text
Distributed-cofactor load
=> WSS short-interval excess 或 local/global model mismatch.
```

尚未证明：

```text
WSS short-interval excess 与 model mismatch 不可能。
```

下一步最小硬点是对 `(CIN-8)` 的窗口族建立符号平衡不等式，或证明失败必进入
`PDEC/ColumnCRT/SAE`。
