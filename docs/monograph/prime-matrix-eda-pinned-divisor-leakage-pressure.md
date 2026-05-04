# EDA 钉扎因子与泄漏见证压力

**状态：** `pinned_divisor_leakage_pressure_reduction_open`

本文继续专攻 ExactEndpoint-MinRep 的最窄缺陷。核心目标是把“`x` 有小素因子即可对偶降阶”的直觉
改写成严格可用的压力不等式。

结论：

```text
若早期零行 x 有素因子 pi，则前 pi-1 列要么已经给出 pi-筛下降，
要么必须由不整除 x 的中高标签素数补洞。
```

特别地，`x` 自身的素因子在这些泄漏列上完全不能作为补洞标签。这是一个新的“一阶刚性”。

## 1. 设置

固定最小早期反例素数 `p`，假设存在

\[
1<x\le p,\qquad U_p(x)=0.
\tag{PDL-1}
\]

取 `x=pi y`，其中 `pi<p` 是 `x` 的素因子。令

\[
M_\pi=\prod_{q<\pi}q,
\qquad
L_{\pi,p}(x)=
\{1\le j<\pi:(px+j,M_\pi)=1\}.
\tag{PDL-2}
\]

由于 `px+j=\pi(p y)+j`，集合 `L_{\pi,p}(x)` 正是降到 `pi` 层时仍未被 `<pi`
素数覆盖的泄漏列。

注意：本文只处理 `x` 有内部素因子 `pi<p` 的分支。若反例恰好是 `x=p`，则没有可用的
`pi|x, pi<p` 因子；该对角分支等价于证明 `(p^2,p^2+p)` 中存在素数，仍需由
ExactEndpoint-MinRep 或外部对角屏障单独排斥。

## 2. 钉扎因子不能补泄漏列

**引理 PDL-1（`x` 的因子相位钉扎）。**  
若 `q|x` 且 `q<p`，则

\[
q\mid px+j \quad\Longleftrightarrow\quad q\mid j.
\tag{PDL-3}
\]

**证明。**  
因为 `q|x` 且 `q\ne p`，有 `q|px`。故 `q|px+j` 当且仅当 `q|j`。证毕。

**引理 PDL-2（泄漏列不能由 `x` 的因子补洞）。**  
若 `j in L_{\pi,p}(x)`，则任何覆盖 `px+j` 的素数 `q<p` 都满足 `q\nmid x` 且 `q\ge\pi`。

**证明。**  
先证 `q` 不能小于 `pi`。若 `q<pi` 且 `q|px+j`，则 `q|M_pi`，这与
`(px+j,M_pi)=1` 矛盾。

再证 `q` 不能整除 `x`。若 `q|x`，由 PDL-1 得 `q|j`。若 `q<pi`，已矛盾；若 `q\ge pi`，
则 `1<=j<pi<=q`，不可能有 `q|j`。因此 `q\nmid x`。证毕。

这说明泄漏列不是自由洞：它们只能由 `[pi,p)` 中、且不属于 `x` 因子集合的外部标签补齐。

## 3. 单标签在一个降阶前缀内不可复用

**引理 PDL-3（前缀单标签唯一性）。**  
固定 `q\ge pi`。在列段 `1<=j<pi` 中，同一个 `q` 至多覆盖一个泄漏列。

**证明。**  
若 `q` 覆盖两个不同列 `j_1,j_2`，则 `q|(j_1-j_2)`。但
`0<|j_1-j_2|<pi<=q`，不可能。证毕。

于是对每个因子 `pi|x`，泄漏列数等于所需外部中高标签见证数的下界。

## 4. 与最小反例下降的结合

令

\[
m(\pi)=\min_{1\le r\le \pi} U_\pi(r).
\tag{PDL-4}
\]

由于 `p` 是最小早期反例，对所有素数 `pi<p` 有 `m(pi)>0`。

**定理 PDL-4（泄漏/逃逸量化二分）。**  
对每个素因子 `pi|x`，令

\[
R_\pi=\rho_\pi(px/\pi)
\tag{PDL-5}
\]

为模 `M_pi` 的最小正代表。则：

1. 若 `R_pi<=pi`，则
   \[
   |L_{\pi,p}(x)|=U_\pi(R_\pi)\ge m(\pi)>0;
   \tag{PDL-6}
   \]
2. 若 `R_pi>pi`，则发生 `RangeEscape(pi,p,x)`。

**证明。**  
零行/泄漏条件只依赖乘数模 `M_pi` 的残基。若 `R_pi<=pi`，则
`L_{\pi,p}(x)` 的大小等于 `pi` 层早期行 `R_pi` 的精确筛余 `U_pi(R_pi)`，
故至少为 `m(pi)`。若 `R_pi>pi`，这正是代表逃逸。证毕。

结合 PDL-2 与 PDL-3，非逃逸因子 `pi` 强制至少 `m(pi)` 个外部中高标签见证。

## 5. 泄漏见证预算

设

\[
\mathcal A(x)=\{\pi:\pi|x,\ R_\pi\le\pi\}.
\tag{PDL-7}
\]

则任何早期零行必须满足必要预算

\[
\sum_{\pi\in\mathcal A(x)}m(\pi)
\le
\#\{(\pi,j,q):
\pi\in\mathcal A(x),\ j\in L_{\pi,p}(x),\
q\mid px+j,\ \pi\le q<p,\ q\nmid x\}.
\tag{PDL-8}
\]

并且对固定 `(pi,q)`，最多有一个 `j` 可出现。等价地，反例必须在多个降阶前缀中安排大量
外部标签相位命中：

```text
q >= pi, q not | x, and -px mod q lies in the pi-prefix leakage set.
```

这就是新的可攻接口：如果这些外部标签命中不够，就强下降到更小 `pi` 的早期反例；如果命中过多，
则形成高标签相位拥塞，应回流到 `HighLabel-MinRep/PDEC`。

## 6. 对当前主线的作用

PDL 不单独闭合 `U_p(x)>0`，但它把因子降阶出口从“至少一个泄漏”强化为：

1. 泄漏见证必须来自 `x` 因子集合之外；
2. 每个非逃逸因子至少要求 `m(pi)` 个见证；
3. 每个中高标签在同一前缀中不能复用；
4. 若许多因子逃逸，则产生多层 MinRep 代表同时逃逸；
5. 若许多因子不逃逸，则产生外部高标签相位拥塞。

因此 ExactEndpoint-MinRep 的下一步最小硬点可以进一步压成：

```text
RangeEscape 多层同发
或
External Leakage Witness Congestion
必触发 LowMod/PDEC/HighLabel-MinRep 缺陷。
```

这比原始“`x` 有因子所以递归矛盾”的说法严格得多，也保留了可继续计数的压力项。
