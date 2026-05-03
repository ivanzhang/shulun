# H3 全局尾标签能量引理

**状态：** `proved_deterministic_defect_lemma_not_final_h3_proof`

本文给出当前 H3 链条中第一个不依赖有限数据的全局确定性不等式。它证明：

```text
若 H3 余量低于目标尺度 B，
则要么小首因子骨架覆盖异常大，
要么中尾 first-factor 标签必产生定量低模能量。
```

这不是最终 H3 正余量证明；它是把“低于 `c q/log q`”严格推入 `Tail/PDEC` 或 `H3-PDEC` 的桥接公式。

## 1. 设置

设 `p<q` 为相邻奇素数，`2<=s<=q`。令 `A_s` 为第 `s` 个 `q` 行窗口中的 H3 六轮候选集合，记

\[
M=M_{H3}(p,s)=\#\{n\in A_s:P^-(n)>p\}.
\]

对 cutoff `y`，定义小骨架负载与尾标签负载：

\[
C_y=\#\{n\in A_s:5\le P^-(n)\le y\},
\]

\[
T_y=\#\{n\in A_s:y<P^-(n)\le p\}.
\]

于是有恒等式

\[
\#A_s=M+C_y+T_y.
\tag{H3-MCT}
\]

## 2. 尾标签短窗容量

令 `ell_+(y)` 为大于 `y` 的下一素数，并设

\[
U_y=\left\lfloor {q\over \ell_+(y)}\right\rfloor+1.
\]

对任意 first factor `ell>y`，集合

\[
A_{s,\ell}=\{n\in A_s:P^-(n)=\ell\}
\]

满足

\[
\#A_{s,\ell}\le U_y.
\tag{H3-U}
\]

原因是 `ell|n` 在长度 `q` 的整数区间内最多命中 `floor(q/ell)+1` 次，而 `ell>=ell_+(y)`。

## 3. 全局尾能量引理

取任意整数 `d` 满足

\[
d\ge 2U_y.
\tag{H3-d}
\]

对 `ell>y`，定义

\[
\mu_{\ell}(b;d)=\#\{n\in A_{s,\ell}:n\equiv b\pmod d\},
\qquad
N_\ell=\#A_{s,\ell}.
\]

定义尾标签低模能量

\[
E_y(d)=
\sum_{y<\ell\le p}
\sum_{b\bmod d}
\left(\mu_{\ell}(b;d)-{N_\ell\over d}\right)^2.
\]

**引理。**

\[
E_y(d)\ge {1\over 2}T_y.
\tag{H3-TE}
\]

**证明。** 对固定 `ell`，

\[
\sum_{b\bmod d}\left(\mu_\ell(b;d)-{N_\ell\over d}\right)^2
=
\sum_{b\bmod d}\mu_\ell(b;d)^2-{N_\ell^2\over d}.
\]

因为 `mu_l(b;d)` 是非负整数且总和为 `N_l`，有 `sum_b mu_l(b;d)^2>=N_l`。由 `(H3-U)` 和 `(H3-d)`，`N_l<=U_y<=d/2`，故

\[
N_\ell-{N_\ell^2\over d}\ge {N_\ell\over2}.
\]

对所有 `ell>y` 求和，得到 `(H3-TE)`。证毕。

## 4. 尺度缺陷公式

给定目标尺度 `B>0` 和能量阈值 `L>0`。若 `M<B` 且

\[
C_y\le \#A_s-B-2L,
\tag{No-SSO}
\]

则

\[
T_y=\#A_s-M-C_y>2L.
\]

代入 `(H3-TE)` 得 `E_y(d)>L`。因此得到全局确定性二分：

\[
M<B
\quad\Longrightarrow\quad
C_y>\#A_s-B-2L
\quad\text{or}\quad
E_y(d)>L.
\tag{H3-SD}
\]

该不等式对所有相邻 `p<q`、所有行 `s`、所有 cutoff `y` 和所有满足 `d>=2U_y` 的模数成立。

## 5. 代入 `q/log q` 尺度

取

\[
B=c{q\over\log q},\qquad L=\lambda {q\over\log q}.
\]

则 `(H3-SD)` 变为：若

\[
M_{H3}(p,s)<c{q\over\log q},
\]

则二者之一成立：

1. **小骨架过载**

\[
C_y>\#A_s-(c+2\lambda){q\over\log q};
\]

2. **尾标签能量**

\[
E_y(d)>\lambda {q\over\log q}.
\]

若选择 `y=p^theta`，则可取 `d` 量级为 `q/y=q^{1-theta}`。所以尾能量模数仍显著低于顶层 `p`，可接入 `H3-PDEC/ColumnCRT` 的低模出口。

## 6. 证明链含义

该引理把“全局尺度低于 `c q/log q`”严格转化为两个缺陷：

```text
low H3 margin
=> small skeleton overload
   or tail-label low-mod energy.
```

剩余未闭合部分不再是组合层，而是两个出口的最终排斥：

1. `SmallSkeletonOverload=>Tail/PDEC`；
2. `TailEnergy=>H3-PDEC/ColumnCRT`。

这比单纯 Mertens 期望强：它不声称直接有正余量，而是证明任何低余量反例都必须付出可量化的缺陷能量或小骨架过载。

补充文件 `docs/monograph/prime-matrix-h3-small-skeleton-pdec-bridge.md` 已把第一出口的组合桥接写成
确定性不等式：小骨架过载推出 `y`-rough 计数亏损
`D_y>V_y-B-2L`。因此后续真正剩余是排斥该 PDEC 缺陷，以及排斥尾标签能量缺陷。
