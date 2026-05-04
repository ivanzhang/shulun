# EDA 高标签容量的第二命中结构

**状态：** `highcap_second_hit_structure_reduction_open`

本文专攻 Alpha-Lift 后的高标签容量项。对 `alpha>1/2`，令 `q` 为高标签素数：

\[
\alpha p<q<p,\qquad r=p-q.
\tag{HSH-1}
\]

则 `0<r<(1-\alpha)p<q`，且高标签覆盖列满足

\[
k\equiv -p^2\equiv -r^2\pmod q.
\tag{HSH-2}
\]

由于区间 `[1,p-1]=[1,q+r-1]` 长度小于 `2q`，每个高标签最多命中两列。

## 1. 第二命中判据

令

\[
s_q=r^2\bmod q.
\tag{HSH-3}
\]

第一正残基为

\[
a_q=(-r^2\bmod q)=
\begin{cases}
q-s_q,&s_q>0,\\
q,&s_q=0.
\end{cases}
\tag{HSH-4}
\]

因为 `q` 为素数且 `0<r<q`，有 `s_q>0`。第二命中存在当且仅当

\[
a_q+q\le p-1=q+r-1,
\tag{HSH-5}
\]

即

\[
s_q\ge q-r+1.
\tag{HSH-6}
\]

这就是 `DSC-10` 的第二命中条件。

## 2. r 变量的显式不等式

写

\[
m=\left\lfloor {r^2\over q}\right\rfloor
=\left\lfloor {r^2\over p-r}\right\rfloor.
\tag{HSH-7}
\]

则 `s_q=r^2-m(p-r)`。第二命中等价于

\[
r^2-m(p-r)\ge p-2r+1,
\tag{HSH-8}
\]

即

\[
r^2+(m+2)r-(m+1)p\ge1.
\tag{HSH-9}
\]

同时 `m` 还满足

\[
m(p-r)\le r^2<(m+1)(p-r).
\tag{HSH-10}
\]

因此第二命中不是任意事件，而是 `r` 落入由二次不等式 `(HSH-9)` 与层条件 `(HSH-10)`
切出的薄集合。

## 3. 容量公式

记

\[
S_\alpha(p)=
\#\{q\ \text{prime}:\alpha p<q<p,\ r=p-q\ \text{satisfies }(HSH-6)\}.
\tag{HSH-11}
\]

则

\[
C_\alpha(p)=
\bigl(\pi(p-1)-\pi(\lfloor\alpha p\rfloor)\bigr)
 + S_\alpha(p).
\tag{HSH-12}
\]

`Alpha-Lift` 的主量间隙问题等价于给 `S_alpha(p)` 建立尖锐上界。

## 4. 样本结构

整数支撑审计显示第二命中支撑密度随 `alpha` 增大而下降：

| alpha | integer second-hit density, typical |
|---:|---:|
| 0.75 | about `0.15` of `r<(1-alpha)p` |
| 0.80 | about `0.12` |
| 0.85 | about `0.08--0.10` |

同时高标签区间本身也缩短。因此 `alpha=0.8` 或 `0.85` 给出更大容量余量。

## 5. 权衡

增大 `alpha` 有利于减小 `C_alpha(p)`，但 `H_alpha(p)` 更接近原始对角素数幸存集合。
因此不能把 `alpha` 推到 `1` 后声称问题变简单；那会退化为原短区间素数命题。

当前实用选择：

```text
alpha in [0.75,0.85]
```

它同时保留：

1. 明显高标签容量余量；
2. 低洞复合壳层仍有宽度可分析；
3. 端点缺陷桥仍适用；
4. 固定低模自动排除仍可走 MainGap。

## 6. 下一步

高标签容量出口已压成：

```text
HSH-bound:
prove S_alpha(p) is small enough that
C_alpha(p)<(1-eta)(p-1)V_alpha(p).
```

若 `HSH-bound` 与低洞 PDEC 下界合并，则对角分支闭合。
