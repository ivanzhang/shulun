# BPN-BK 到 Directed CRTDefect 的严格桥接

**状态：** `bk_dec_bridge_closed_to_named_endpoint_defect`

本文只证明确定桥接：

```text
边界零行 + BK 低阶尾项预算
=> BK-DEC 端点锯齿缺陷
=> Directed Endpoint CRTDefect。
```

注意：这不是 `BPN(P)` 的完整无条件证明。它闭合的是“进入命名缺陷出口”的环节；
剩余仍是 `Directed CRTDefect/Tail-anchor/PDEC-or-SAE` 的排斥。

## 1. BK 截断分解

令

\[
I_r=[(r-1)P+1,rP-1]\cap\mathbb Z,\qquad 2\le r\le P.
\]

对奇数 `K` 与 level `D` 定义

\[
\mathcal D_{K,D}=\{d:d|M_{<P},\ \mu(d)^2=1,\ \omega(d)\le K,\ d\le D\}.
\]

记

\[
A_d(r)=\#\{n\in I_r:d|n\}.
\]

由于 `|I_r|=P-1`，

\[
A_d(r)=\frac{P-1}{d}+e_d(r),
\qquad
e_d(r)=
\left\{\frac{(r-1)P}{d}\right\}
-
\left\{\frac{rP-1}{d}\right\}.
\tag{1}
\]

令

\[
V_{K,D}=\sum_{d\in\mathcal D_{K,D}}\frac{\mu(d)}d,
\qquad
E_{K,D}(r)=\sum_{d\in\mathcal D_{K,D}}\mu(d)e_d(r).
\]

则低阶 BK 截断有精确分解

\[
S_{K,\le D}(r)=
\sum_{d\in\mathcal D_{K,D}}\mu(d)A_d(r)
=(P-1)V_{K,D}+E_{K,D}(r).
\tag{2}
\]

## 2. 零行推出 BK-DEC

完整 BK 和低阶 BK 的差记为

\[
R_{K,>D}(r)=
\sum_{\substack{d|M_{<P}\\ \omega(d)\le K\\ d>D}}\mu(d)A_d(r).
\]

因此

\[
S_K(r)=S_{K,\le D}(r)+R_{K,>D}(r).
\tag{3}
\]

**Theorem BK-DEC-1（零行到端点缺陷）。**
假设 `I_r` 是边界零行，即

\[
\gcd(n,M_{<P})>1\qquad(n\in I_r).
\]

若存在尾项预算 `T_{K,D}` 使

\[
|R_{K,>D}(r)|\le T_{K,D},
\tag{4}
\]

并且主项余量

\[
\Delta_{K,D}=(P-1)V_{K,D}-T_{K,D}>0,
\tag{5}
\]

则

\[
E_{K,D}(r)\le -\Delta_{K,D}.
\tag{BK-DEC}
\]

**证明。**
奇阶 Bonferroni 的逐点权

\[
b_K(m)=\sum_{j=0}^K(-1)^j\binom mj
\]

满足 `b_K(0)=1`，且对 `m>=1` 有 `b_K(m)<=0`。零行中每个 `n`
都有 `\omega_P(n)>=1`，故

\[
S_K(r)=\sum_{n\in I_r}b_K(\omega_P(n))\le0.
\]

由 `(2)`、`(3)` 得

\[
(P-1)V_{K,D}+E_{K,D}(r)+R_{K,>D}(r)\le0.
\]

于是

\[
E_{K,D}(r)
\le -(P-1)V_{K,D}-R_{K,>D}(r)
\le -(P-1)V_{K,D}+T_{K,D}
=-\Delta_{K,D}.
\]

证毕。

该定理说明：一旦低阶 BK 主项在扣除尾项后仍有正余量，边界零行不能“安静”
存在；它必须制造一个负向端点锯齿异常。

## 3. BK-DEC 到低模块缺陷

取 `\mathfrak B` 为 `\mathcal D_{K,D}` 的任意有限不交分块。对块 `B` 定义

\[
\mathcal E_B(r)=\sum_{d\in B}\mu(d)e_d(r).
\]

**Theorem BK-DEC-2（鸽巢投影）。**
若 `(BK-DEC)` 成立，则存在 `B\in\mathfrak B` 使

\[
|\mathcal E_B(r)|
\ge
\frac{\Delta_{K,D}}{|\mathfrak B|}.
\tag{6}
\]

更一般地，若只保留子字典 `\mathcal G=\bigcup_{B\in\mathfrak B}B`，且

\[
\left|\sum_{d\in\mathcal D_{K,D}\setminus\mathcal G}\mu(d)e_d(r)\right|
\le E_{\rm dict}<\Delta_{K,D},
\tag{7}
\]

则存在 `B` 使

\[
|\mathcal E_B(r)|
\ge
\frac{\Delta_{K,D}-E_{\rm dict}}{|\mathfrak B|}.
\tag{8}
\]

**证明。**
由 `(BK-DEC)`，

\[
|E_{K,D}(r)|\ge \Delta_{K,D}.
\]

若使用全字典，则

\[
E_{K,D}(r)=\sum_{B\in\mathfrak B}\mathcal E_B(r).
\]

若所有块均小于 `\Delta_{K,D}/|\mathfrak B|`，三角不等式给出
`|E_{K,D}(r)|<\Delta_{K,D}`，矛盾。子字典情形先用 `(7)` 扣除字典外尾项，
再同理应用三角不等式。证毕。

这正是 `Directed Endpoint CRTDefect` 的块投影定义。取

\[
\kappa_B\le\frac{\Delta_{K,D}-E_{\rm dict}}{|\mathfrak B|}
\]

即得

```text
BK-DEC => DEC_{K,D}(I_r;\mathfrak B,\kappa)。
```

## 4. 端点场的 CRT/Fourier 形式

对每个 `d\in\mathcal D_{K,D}`，因为 `d|M_{<P}` 且 `P` 是更大的素数，故 `(P,d)=1`。
函数

\[
r\mapsto e_d(r)
=
\left\{\frac{(r-1)P}{d}\right\}
-
\left\{\frac{rP-1}{d}\right\}
\]

是模 `d` 周期函数，并且在完整模 `d` 周期上均值为 `0`：两项分别遍历同一个
剩余系。于是每个块投影 `\mathcal E_B(r)` 是模

\[
Q_B=\operatorname{lcm}_{d\in B}d
\]

的零均值周期函数，并有有限 Fourier 展开

\[
\mathcal E_B(r)=\sum_{\chi\ne1}\widehat{\mathcal E}_B(\chi)\chi(r)
\]

其中 `\chi` 取模 `Q_B` 的非平凡加性角色。若 `(6)` 或 `(8)` 成立，则至少存在
一个非平凡角色满足

\[
|\widehat{\mathcal E}_B(\chi)|
\ge
\frac{|\mathcal E_B(r)|}{Q_B-1}.
\tag{9}
\]

这把 `BK-DEC` 精确转化为低 CRT 坐标上的非零频率异常，即已有文档中的
`Directed Endpoint CRTDefect/OSPC*` 入口。

## 5. 已闭合与未闭合

已严格闭合：

```text
边界零行
+ |R_{K,>D}|<=T_{K,D}
+ (P-1)V_{K,D}>T_{K,D}
=> BK-DEC
=> Directed Endpoint CRTDefect。
```

仍未闭合：

```text
Directed Endpoint CRTDefect
=> 矛盾。
```

该最后一步不能只靠完整 CRT 周期零均值完成；单点端点尖峰可以存在。必须继续证明
`PDEC-or-SAE`：要么缺陷在坏行集合上持续并形成真实 CRT 频率缺陷，要么孤立尖峰由
单窗锚逃逸排斥。
