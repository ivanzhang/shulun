# EDA 因子降阶：条件下降与两类阻塞

**状态：** `factor_descent_conditional_leakage_and_range_obstruction`

本文分析新的降阶想法：

```text
若 P 的早期零行乘数 x<P，且 x 有素因子 pi<P，
是否能把 P-零行转换为 pi-零行，从而递归矛盾？
```

结论是：这个方向有价值，但不能自动闭合。严格下降需要同时满足两个额外条件：

1. **无层级泄漏：** 前 `pi-1` 列必须已经被 `<pi` 素数覆盖，而不是只被 `[pi,P)` 中素数覆盖；
2. **早期代表保持：** 降阶后的 `pi`-行乘数在 `mod M_pi` 的最小正代表必须仍落在 `<=pi`。

若任一条件失败，就得到新的结构缺陷：中高标签泄漏或 CRT 最小代表逃逸。

## 1. 基本设置

固定奇素数 `P`。设

\[
Z_P=\{x\ge1:\forall 1\le k<P,\ \exists q<P,\ q\mid Px+k\}.
\tag{FD-1}
\]

假设 `x in Z_P` 且 `x=pi y`，其中 `pi<P` 是素数。对 `1<=j<pi`，

\[
Px+j=P\pi y+j=\pi(P y)+j.
\tag{FD-2}
\]

因此，若只看前 `pi-1` 个列，`P`-零行给出一个 `pi`-宽窗口：

\[
\pi X+j,\qquad X=P y.
\tag{FD-3}
\]

但 `P`-零行只保证每个 `(FD-2)` 有某个 `<P` 的素因子，不保证该素因子 `<pi`。

补充：若讨论早期反例 `1<=x<P`，则 `x=1` 可由 Bertrand 定理排除，因为区间
`(P,2P)` 中存在素数，所以第一行不可能是零行。因此任何早期反例必有 `x>=2`，从而
确实有某个素因子 `pi|x`。

## 2. 弱下降与强下降

定义层级泄漏集合

\[
L_{\pi,P}(x)=
\{1\le j<\pi:\ (\pi(P y)+j,\ M_\pi)=1\},
\qquad
M_\pi=\prod_{q<\pi}q.
\tag{FD-4}
\]

若 `j in L_{\pi,P}(x)`，则该列没有 `<pi` 的素因子。由于原来 `x in Z_P`，它仍必须有
某个 `<P` 的素因子，因此覆盖它的素因子只能落在

\[
\pi\le q<P.
\tag{FD-5}
\]

这就是中高标签泄漏。

**引理 FD-1（条件强下降）。**  
若 `x=pi y in Z_P` 且

\[
L_{\pi,P}(x)=\varnothing,
\tag{FD-6}
\]

则

\[
X=P y
\tag{FD-7}
\]

是 `pi`-筛的零行乘数，即

\[
\forall 1\le j<\pi,\quad \exists q<\pi,\ q\mid \pi X+j.
\tag{FD-8}
\]

**证明。**  
`L_{\pi,P}(x)=\varnothing` 正是说每个 `1<=j<pi` 都有 `(pi X+j,M_pi)>1`。
因此存在某个 `q<pi` 整除 `pi X+j`。证毕。

## 3. 为什么这还不是早期递归矛盾

即使 `(FD-8)` 成立，得到的 `pi`-零行乘数也是

\[
X=P y=P{x\over \pi}.
\tag{FD-9}
\]

若原反例只满足 `x<P`，则

\[
X < {P^2\over \pi},
\tag{FD-10}
\]

通常远大于 `pi`。而较小素数层已知或待证的早期命题是：

\[
X_0(\pi)>\pi,
\tag{FD-11}
\]

它只排除 `1<=X<=pi` 的早期零行，不能排除 `X=P y` 这样的晚期零行。

因此还需要额外条件：令 `rho_pi(X)` 为 `X mod M_pi` 的最小正代表，若

\[
\rho_\pi(P y)\le \pi,
\tag{FD-12}
\]

才会与 `EDA(pi)` 矛盾。

**引理 FD-2（早期代表下降）。**  
若 `x=pi y in Z_P`，并且 `(FD-6)` 与 `(FD-12)` 同时成立，则 `EDA(pi)` 失败。

**证明。**  
由 FD-1，`X=P y` 是 `pi`-零行乘数。零行条件只依赖于 `X mod M_pi`，所以其最小正代表
`rho_pi(X)` 也是 `pi`-零行乘数。若 `rho_pi(X)<=pi`，则出现 `pi` 的早期零行，正是
`EDA(pi)` 失败。证毕。

## 4. 首个反例强制的二分

若 `P` 是最小的早期反例素数，并且存在 `x<P`、`x in Z_P`。取任意素因子 `pi|x`。
由于 `pi<P`，`EDA(pi)` 成立。由 FD-2 可知，至少发生以下一项：

```text
Leakage(pi,P,x): L_{pi,P}(x) 非空；
RangeEscape(pi,P,x): rho_pi(Px/pi)>pi。
```

这就是新的反例矛盾场：

```text
每个 x 的小素因子 pi 都必须付出
中高标签泄漏 或 CRT 代表逃逸 的代价。
```

## 5. 可攻方向

该降阶路线不能直接闭合，但提供了新的强约束：

1. **泄漏容量约束。**  
   若许多 `pi|x` 都发生泄漏，则很多早期小列 `j<pi` 必须由 `[pi,P)` 的中高素数覆盖。
   这些素数在短列段中的复用受列差整除刚性限制。

2. **代表逃逸约束。**  
   若泄漏很少，则多数因子 `pi|x` 必须满足
   \[
   \rho_\pi(Px/\pi)>\pi.
   \]
   这是多层 CRT 最小代表同时逃逸，可能触发新的 MinRep/PDEC 缺陷。

3. **反例最小性约束。**  
   对最小反例 `P`，每个 `pi|x` 都已经有 `EDA(pi)`。因此任何成功下降都会立即矛盾；
   失败则留下可计数缺陷。

当前最小可攻命题变为：

```text
FactorDescent-Defect:
For x<P, not all prime factors pi|x can simultaneously pay Leakage/RangeEscape
without creating LowMod/Tail/PDEC defect.
```

## 6. 样本审计

脚本：

```text
experiments/prime_matrix_factor_descent_audit.py
```

命令：

```text
python3 experiments/prime_matrix_factor_descent_audit.py --pairs 23:58,13:168,17:1210,19:3658
```

这些是已知首零行样本，不是早期反例；它们用于检查降阶机制。输出显示：

| P | x | pi | leakage count | reduced rep | early rep hit | strong descent |
|---:|---:|---:|---:|---:|---|---|
| 23 | 58 | 2 | 1 | 1 | true | false |
| 13 | 168 | 2 | 1 | 1 | true | false |
| 13 | 168 | 3 | 1 | 2 | true | false |
| 13 | 168 | 7 | 1 | 12 | false | false |
| 17 | 1210 | 5 | 1 | 4 | true | false |
| 17 | 1210 | 11 | 1 | 190 | false | false |
| 19 | 3658 | 2 | 1 | 1 | true | false |

审计结论：

1. 已知零行样本中，每个可见降阶都被至少一个泄漏列阻断；
2. 某些因子还同时发生代表逃逸，例如 `P=13, pi=7` 与 `P=17, pi=11`；
3. 这支持本文二分：若要递归下降，必须同时消除泄漏和代表逃逸；
4. 对假设的最小早期反例，所有因子 `pi|x` 都必须被这两类阻塞保护，否则会下降到更小
   `EDA(pi)` 反例并矛盾。

所以该路线下一步不是声称“必然递归矛盾”，而是证明这些阻塞无法在 `x<P` 的早期区段中
对所有因子同时存在而不触发 `LowMod/Tail/PDEC`。
