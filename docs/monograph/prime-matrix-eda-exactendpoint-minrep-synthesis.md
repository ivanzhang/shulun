# EDA ExactEndpoint-MinRep 缺陷综合归约

**状态：** `exactendpoint_minrep_synthesis_reduction_open`

本文把当前最小硬点集中到一个审稿级接口：

```text
证明不存在 1<=x<=p 使 U_p(x)=0。
```

变量阶布尔消尾已经证明固定阶尾项不是本质障碍。剩余不是“再调一个 Bonferroni 阶数”，而是必须排斥
精确端点完全抵消，即完整 CRT 覆盖证书在对角段 `1<=x<=p` 命中。

## 1. 基本对象

令 `p` 为奇素数，

\[
M_p=\prod_{q<p}q,\qquad
I_{p,x}=\{px+1,\ldots,px+p-1\}.
\tag{EEMS-1}
\]

定义精确筛余

\[
U_p(x)=\#\{1\le k<p:(px+k,M_p)=1\}.
\tag{EEMS-2}
\]

`U_p(x)=0` 等价于 `I_{p,x}` 中每个点都有某个 `<p` 的素因子。若 `1<=x<=p`，则任意
未覆盖点 `px+k` 都满足

\[
p<px+k<p^2+p,
\tag{EEMS-3}
\]

且没有 `<p` 素因子；因此它必为素数。这就是早期对角避让与短区间素数存在性的精确等价。

## 2. ExactEndpoint 命中定理

一个完整覆盖证书是映射

\[
\tau:\{1,\ldots,p-1\}\to\{q:q<p\ \text{素数}\}
\tag{EEMS-4}
\]

并满足同余系统

\[
px+k\equiv0\pmod{\tau(k)},\qquad 1\le k<p.
\tag{EEMS-5}
\]

记该系统的 CRT 最小正代表为 `r_tau^+`。

**定理 EEMS-1（早期零行就是 MinRep 命中）。**  
若 `1<=x<=p` 且 `U_p(x)=0`，则存在完整覆盖证书 `tau` 使

\[
x\equiv r_\tau\pmod{D_\tau},\qquad r_\tau^+\le p,
\tag{EEMS-6}
\]

其中 `D_tau` 是证书实际使用素数的乘积。

**证明。**  
对每个 `k`，由 `U_p(x)=0` 选取一个 `<p` 素因子 `tau(k)|px+k`。这给出 `(EEMS-5)`。
CRT 相容性已经由实际整数 `x` 保证，所以 `x` 落在证书残基类中。该残基类的最小正代表
不超过任何正代表，故 `r_tau^+<=x<=p`。证毕。

因此当前硬点可完全表述为：

```text
排斥所有完整覆盖证书的 r_tau^+<=p。
```

## 3. 变量阶消尾后的精确形式

令

\[
K_p=\min\{K\ge \lfloor\log_2(p^2+p-1)\rfloor:K\ \text{为奇数}\}.
\tag{EEMS-7}
\]

由变量阶布尔消尾定理，

\[
S_{K_p}(p,x)=U_p(x)
\tag{EEMS-8}
\]

对所有 `1<=x<=p` 精确成立。于是若早期反例存在，则不是“尾项估计不够强”，而是

```text
所有点的非空小素因子布尔格逐点相消，且没有任何空布尔格点。
```

这把剩余硬点压成 ExactEndpoint-MinRep 缺陷：精确端点函数在整行上完全覆盖。

## 4. 因子对偶降阶的严格边界

用户提出的降阶直觉可以精确写成以下定理。它是有效约束，但不是自动闭合。

设 `x=pi y`，其中 `pi<p` 为素数。对 `1<=j<pi`，

\[
px+j=p\pi y+j=\pi(p y)+j.
\tag{EEMS-9}
\]

令

\[
L_{\pi,p}(x)=
\{1\le j<\pi:(\pi(p y)+j,M_\pi)=1\},
\qquad
M_\pi=\prod_{q<\pi}q.
\tag{EEMS-10}
\]

**定理 EEMS-2（对偶降阶二分）。**  
假设 `p` 是最小早期反例素数，`1<x<=p` 且 `U_p(x)=0`。对每个素因子 `pi|x`，至少发生一项：

1. `Leakage(pi,p,x)`: `L_{pi,p}(x)` 非空；
2. `RangeEscape(pi,p,x)`: `rho_pi(p x/pi)>pi`，其中 `rho_pi` 是模 `M_pi` 的最小正代表。

**证明。**  
若 `L_{pi,p}(x)=\varnothing`，则 `(EEMS-9)` 的前 `pi-1` 列全部由 `<pi` 素数覆盖，所以
`X=p x/pi` 是 `pi`-筛零行乘数。若同时 `rho_pi(X)<=pi`，零行条件按模 `M_pi` 周期复现，
于是 `pi` 出现早期零行，矛盾于 `p` 的最小性。因此二者至少一项发生。证毕。

这个定理解释了为什么“`x` 有小因子，所以立刻降阶矛盾”尚不充分：中高标签泄漏和最小代表逃逸
是两个真实出口。下一步必须证明这些出口不能对所有 `pi|x` 同时支付。

## 5. 低骨架洞与高标签补洞容量

给定低骨架素数集

\[
\mathcal Q_0=\{q\le y:q<p\},
\qquad
M_0=\prod_{q\in\mathcal Q_0}q,
\tag{EEMS-11}
\]

定义低骨架残洞

\[
H_y(p,x)=\{1\le k<p:(px+k,M_0)=1\}.
\tag{EEMS-12}
\]

若 `U_p(x)=0`，则每个 `k in H_y(p,x)` 必须被某个高标签素数 `y<q<p` 覆盖。对固定 `q`，集合

\[
C_q(p,x)=\{1\le k<p:q\mid px+k\}
\tag{EEMS-13}
\]

是 `[1,p-1]` 中的一个模 `q` 等差类，因此

\[
|C_q(p,x)|\le \left\lceil {p-1\over q}\right\rceil.
\tag{EEMS-14}
\]

于是得到必要容量不等式：

\[
|H_y(p,x)|
\le
\sum_{y<q<p}
\left\lceil {p-1\over q}\right\rceil.
\tag{EEMS-15}
\]

这只是必要条件，通常还不足以矛盾；它的作用是把反例压入更精确的相位问题：

```text
低骨架若留下大量洞，高标签必须以固定等差类补齐；
若低骨架留下很少洞，则 x mod M_0 已经处于低模端点缺陷坏集。
```

因此 `(EEMS-15)` 是 `LowMod/PDEC` 与 `HighLabel-MinRep` 的接口，而不是终点。

## 6. 被 x 因子钉住的标签

若 `q|x` 且 `q<p`，则

\[
q\mid px+k \quad\Longleftrightarrow\quad q\mid k.
\tag{EEMS-16}
\]

所以 `x` 的素因子作为覆盖标签时相位完全失去自由，只能覆盖固定列 `q,2q,3q,...`。
特别地，若 `pi` 是 `x` 的一个素因子，则 `pi` 不能覆盖前 `pi-1` 列。

这给因子降阶增加了刚性解释：前 `pi-1` 列若不能由 `<pi` 骨架覆盖，就必须由不整除 `x` 的
中高标签补洞；这些补洞正是 `Leakage(pi,p,x)`。

## 7. 当前最窄可闭合命题

综合所有已证条件，最小反例必须同时满足：

1. `MinRepHit`: 存在完整证书 `tau` 且 `r_tau^+<=p`；
2. `ExactEndpoint`: 变量阶精确筛余 `S_{K_p}=U_p=0`；
3. `Low-or-High`: 对每个低骨架 cutoff，要么低模坏集命中，要么高标签按 `(EEMS-15)` 精确补洞；
4. `FactorDefect`: 对每个 `pi|x`，发生 `Leakage` 或 `RangeEscape`；
5. `PinnedDivisor`: 所有 `q|x` 的覆盖相位被固定为 `k≡0 mod q`。

因此下一步真正要证明的不是新等价命题，而是以下缺陷排斥：

```text
ExactEndpoint-MinRep Defect Exclusion:
MinRepHit、Low-or-High、FactorDefect、PinnedDivisor
不能在同一个 1<=x<=p 的早期行同时成立。
```

## 8. 诚实边界

本文件完成的是严格归约和新的必要条件综合，尚未证明 `U_p(x)>0`。特别地，取 `x=p` 时，
`U_p(p)>0` 等价于区间

\[
(p^2,p^2+p)
\tag{EEMS-17}
\]

中存在素数，这是 Oppermann 第一半区间在素数平方处的子命题。因此任何声称全局闭合的证明，
必须在本文的 ExactEndpoint-MinRep 缺陷排斥中真正提供新不等式；不能只重复 CRT 相容性、
变量阶消尾或形式降阶。
