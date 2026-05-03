# H3 逐行正余量的闭合边界与精确剩余定理

**状态：** `proved_equivalence_and_boundary_not_pointwise_closure`

本文回答两个审稿级问题：

1. `prime-matrix-h3-first-row-scale-bridge.md` 是否已经严格证明？
2. 为什么“平均 H3 余量约为第一行素数数目的一半”仍不能推出每一行逐行有正余量？

结论：

```text
第一行尺度桥已严格证明为全局平均定理；
逐行正余量还需要一个新的局部尺度转移/低模缺陷排斥定理。
```

## 1. 已严格证明的部分

设 `p<q` 为相邻素数，`2<=s<=q`，令

\[
I_s=[(s-1)q+1,sq].
\]

由相邻壳层单点性，若 `1<n<q^2` 且 `P^-(n)>p`，则 `n` 必为素数；闭端点唯一例外是 `q^2`。
因此 H3 余量满足

\[
M_{H3}(p,s)
=
\#\{n\in I_s:n\text{ 为素数}\}+O(1),
\tag{PCB-1}
\]

其中 `O(1)` 仅来自左右端点不完整 3 块。

对 `s=2,...,q` 求和得

\[
\sum_{s=2}^{q}M_{H3}(p,s)
=
\pi(q^2)-\pi(q)+O(q).
\tag{PCB-2}
\]

由素数定理，

\[
{1\over q-1}\sum_{s=2}^{q}M_{H3}(p,s)
\sim {q\over 2\log q}
\sim {1\over2}\pi(q).
\tag{PCB-3}
\]

所以“第一行素数尺度的一半”是严格的全局平均结论。

## 2. 平均定理不能推出逐行定理

逐行 H3 正余量要求

\[
M_{H3}(p,s)\ge 1
\qquad(2\le s\le q).
\tag{PCB-4}
\]

而 `(PCB-3)` 只控制总和。逻辑上，以下情形与同一个总平均完全兼容：

```text
某一行 M_H3(p,s0)=0，
其他行平均多出约 (q/(2log q))/(q-2)。
```

因此平均尺度守恒只能说明“总质量足够大”，不能排除“单行质量被搬走”。要排除单行零余量，必须控制
行间波动或证明质量搬移会产生低模缺陷。

## 3. 逐行命题的精确等价形式

由 `(PCB-1)`，除固定端点误差外，逐行 H3 正余量等价于：

\[
\pi(sq)-\pi((s-1)q)\ge 1
\qquad(2\le s\le q).
\tag{PCB-5}
\]

也就是每个对齐长度 `q` 的窗口都含素数。这是 `x≈q^2` 处长度 `sqrt x` 的短区间素数存在问题。

若存在统一常数 `c>0` 使

\[
\pi(sq)-\pi((s-1)q)
\ge c{q\over\log q}
\qquad(2\le s\le q),
\tag{PCB-6}
\]

则 H3/行命题立即闭合。反过来，H3 正余量至少给出 `(PCB-5)` 的对齐版本。

## 4. 第一行尺度转移定理

把 `(PCB-6)` 写成与第一行的关系：

\[
M_{H3}(p,s)\ge \kappa\,\pi(q)
\qquad(2\le s\le q)
\tag{PCB-7}
\]

其中任意固定 `0<kappa<1/2` 都足够。因为 `pi(q)~q/log q`，`(PCB-7)` 就是把第一行尺度
逐行转移到平方壳层。

当前已证的是平均版：

\[
{1\over q-1}\sum_{s=2}^{q}M_{H3}(p,s)
\sim {1\over2}\pi(q).
\tag{PCB-8}
\]

未证的是点态版：

\[
M_{H3}(p,s)
\ge \kappa\,\pi(q)
\quad\text{for every }s.
\tag{PCB-9}
\]

这就是最后未闭合的真实数学内容。

## 5. 与统一缺陷判据的关系

`prime-matrix-h3-unified-defect-criterion.md` 已证明：

\[
D_y\le V_y-B-2L
\quad\text{and}\quad
\mathcal F_y(d)\le dL
\quad\Longrightarrow\quad
M_{H3}(p,s)\ge B.
\tag{PCB-10}
\]

取

\[
B=\kappa\pi(q)\asymp \kappa {q\over\log q},
\]

则 `(PCB-10)` 给出完整的逻辑闭合路线：

```text
第一行平均尺度桥
+ 逐行低模缺陷排斥
=> 第一行尺度逐行转移
=> H3 正余量
=> 行命题闭合。
```

所以最终要证明的不是“平均尺度是否正确”，而是：

```text
任何把某一行的第一行尺度质量压到 0 的配置，
必然产生 D_y 或 F_y 缺陷；
并且这些缺陷由 CRT/方阵刚性排斥。
```

## 6. 不能跳过的审稿缺口

如果不证明 `(PCB-9)` 或等价的缺陷排斥，则以下推理是无效的：

```text
平均 H3 余量 ~ q/(2log q)
therefore 每行 H3 余量 > 0.
```

这是从平均到点态的非法跳跃。顶级期刊审稿会立即要求补充局部波动上界、短区间素数定理，或
`D_y/F_y` 缺陷排斥证书。

## 7. 当前最小闭合定理

可作为下一步硬攻的最小定理是：

```text
H3 Pointwise Scale Transfer.
There exist constants theta, kappa, lambda, eta>0 such that for
y=q^theta and d>=2(floor(q/ell_+(y))+1), every adjacent p<q and
every 2<=s<=q satisfy
  D_y <= eta*q/log q
  and F_y(d) <= d*lambda*q/log q,
with V_y >= (kappa+2lambda+eta)*q/log q.
```

由统一缺陷判据，这个定理将推出

\[
M_{H3}(p,s)\ge \kappa {q\over\log q}>0
\]

并完成行命题。该定理目前尚未证明；它是“平均尺度桥”之后唯一真正剩余的数学硬点。

补充硬边界见：

```text
docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md
```

该文件说明逐行 H3 闭合等价于 `x≈q^2`、窗口长度 `sqrt x` 的对齐短区间素数下界。现有普通
PNT、RH 型误差和已知无条件短区间素数输入都不能直接推出这一点；必须证明方阵/CRT 低模缺陷排斥。
