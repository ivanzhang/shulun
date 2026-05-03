# 不相交 singleton 走廊的 Selberg 二次型闭合引理

**状态：** `singleton_corridor_sieve_inlined_to_finite_quadratic_form`

本文补齐 `singleton-prime corridor` 小硬点中的最后一层标准上筛接口。结论不是宣称 `ASB/RPD` 已闭合，而是把 singleton 走廊侧严格化为一个有限 Selberg 二次型常数和一个低模端点缺陷能量。

## 1. 设置

设

\[
\mathcal C=\bigsqcup_{j=1}^K [A_j,B_j]\cap\mathbb Z
\]

是不相交整数区间并集，记

\[
X=|\mathcal C|,\qquad P(z)=\prod_{\ell\le z}\ell .
\]

目标是估计

\[
S(\mathcal C,z)=\#\{m\in\mathcal C:(m,P(z))=1\}.
\]

对平方自由整数 `r|P(z)`，定义

\[
A(r)=\#\{m\in\mathcal C:r\mid m\},\qquad
\rho(r)=A(r)-{X\over r}.
\]

因为每个区间中 `r` 的倍数个数等于区间长度除以 `r` 加至多一个端点误差，所以

\[
|\rho(r)|\le K .
\tag{1}
\]

这是后续低模端点缺陷的唯一来源。

## 2. Selberg 二次型上界

取参数 `\xi\ge 1`。令权重 `\lambda_d` 支撑在

\[
d\mid P(z),\qquad d<\xi ,
\]

并满足 `\lambda_1=1`。若 `(m,P(z))=1`，则在所有 `d|P(z)` 中只有 `d=1` 可整除 `m`，故

\[
1_{(m,P(z))=1}
\le
\left(\sum_{\substack{d<\xi\\ d\mid P(z)\\ d\mid m}}\lambda_d\right)^2 .
\]

求和得

\[
S(\mathcal C,z)
\le
\sum_{d,e<\xi}\lambda_d\lambda_e A([d,e]).
\]

代入 `A([d,e])=X/[d,e]+\rho([d,e])`，得到精确分解

\[
S(\mathcal C,z)
\le
X Q_z(\lambda;\xi)+E_{\mathcal C,z}(\lambda;\xi),
\tag{2}
\]

其中

\[
Q_z(\lambda;\xi)=
\sum_{\substack{d,e<\xi\\ d,e\mid P(z)}}
{\lambda_d\lambda_e\over [d,e]},
\]

\[
E_{\mathcal C,z}(\lambda;\xi)=
\sum_{\substack{d,e<\xi\\ d,e\mid P(z)}}
\lambda_d\lambda_e\,\rho([d,e]).
\]

由 `(1)` 还可得无符号端点界

\[
|E_{\mathcal C,z}(\lambda;\xi)|
\le
K\left(\sum_{\substack{d<\xi\\ d\mid P(z)}}|\lambda_d|\right)^2 .
\tag{3}
\]

这一步完全有限、完全代数，不使用任何素数分布输入。

## 3. 有效 Selberg 常数

定义有限维有效常数

\[
\Lambda_z(\xi)=
\inf_{\lambda_1=1}
Q_z(\lambda;\xi),
\]

其中下确界取遍上一节的同一支撑条件。取达到或逼近该下确界的 Selberg 权 `\lambda^\ast`，则

\[
S(\mathcal C,z)
\le
X\Lambda_z(\xi)+E_{\mathcal C,z}(\lambda^\ast;\xi).
\tag{4}
\]

若使用标准一维 Selberg 筛的显式最小化公式，可将

\[
\Lambda_z(\xi)
\le {1\over G_z(\xi)},\qquad
G_z(\xi)=
\sum_{\substack{d<\xi\\ d\mid P(z)}}
{\mu^2(d)\over \varphi(d)} .
\tag{5}
\]

再由 Mertens 型乘积估计把 `1/G_z(\xi)` 转写为

\[
{1\over G_z(\xi)}
\le C_{\rm Sel}(u)\,V(z),
\qquad
u={\log \xi\over\log z},\quad
V(z)=\prod_{\ell\le z}\left(1-{1\over \ell}\right).
\tag{6}
\]

因此标准写法

\[
S(\mathcal C,z)
\le C_{\rm Sel}(u)X V(z)+E_{\rm end}
\]

在本文中被内联为 `(2)--(6)`：主项来自有限二次型常数，误差来自端点缺陷。

## 4. 端点缺陷出口

把 `(2)` 中同一最小化权重按 `r=[d,e]` 合并，定义非负缺陷权

\[
\beta_r(\lambda^\ast)=
\sum_{\substack{d,e<\xi\\ d,e\mid P(z)\\ [d,e]=r}}
|\lambda^\ast_d\lambda^\ast_e|.
\]

若端点误差无法进入预算，则必有

\[
\sum_{r<\xi^2,\ r\mid P(z)}
\beta_r(\lambda^\ast)\,|\rho(r)|
\]

达到相同量级。也就是说，走廊并集在一批低模 `r|P(z)` 上系统性偏离均匀倍数计数。这个结论给出精确出口：

```text
Selberg 主项 + 端点误差进入预算
or
低模端点缺陷能量过大 => CRTDefect / Tail-anchor / OSPC.
```

它不是新的猜测，而是 `(2)` 的二分重写。

## 5. 应用于 singleton 走廊

在 `docs/monograph/prime-matrix-singleton-corridor-closure-lemma.md` 中，固定 ASB 窗口 `J` 后，不同尾值 `d` 的走廊 `C_d(J)` 已证明两两不相交。令

\[
\mathcal C(J,D)=\bigcup_{d\in D}C_d(J)
\]

并记 `K=|D|`、`X=|\mathcal C(J,D)|`。由唯一分解引理和不相交并集上界，

\[
\sum_{d\in D}N_d(J;z)
\le S(\mathcal C(J,D),z).
\]

再套用 `(4)`，得到

\[
\sum_{d\in D}N_d(J;z)
\le
X\Lambda_z(\xi)+E_{\mathcal C(J,D),z}(\lambda^\ast;\xi).
\tag{SC-Selberg}
\]

这就是 singleton 走廊侧的严格闭合形式。它具有三个优点：

1. 不需要有限模板覆盖无限情形；
2. 不需要走廊重叠校正，因为重叠已由商层唯一性排除；
3. 若失败，失败必表现为低模端点缺陷，而不是模糊的“筛常数不够”。

## 6. 审稿状态

当前小硬点从

```text
standard upper sieve on disjoint singleton-corridor unions
```

进一步闭合为

```text
finite Selberg quadratic bound (SC-Selberg)
or weighted low-mod endpoint defect => CRTDefect/Tail-anchor/OSPC.
```

仍未闭合的是更上游命题：素互补因子短区间上界、聚合 Mertens 包络常数、异常出口排斥、`Annulus(p,q)`，以及这些输入合成后的 `ASB/RPD` 全链。
