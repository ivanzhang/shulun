# Early-Diagonal-Avoidance：早期对角段避开 CRT 零行集合

**状态：** `reduced_to_prime-in-p-aligned-short-intervals_not_closed`

本文继续攻击上一轮得到的新最窄硬点：

```text
Early-Diagonal-Avoidance:
the diagonal segment x=1,...,p in Z/M_pZ avoids the zero-row covering set.
```

这里

\[
M_p=\prod_{q<p,\ q\ {\rm prime}}q.
\tag{EDA-1}
\]

## 1. 零行的 CRT 覆盖表达

对奇素数 `p` 与 `1<=x<=p`，考虑行窗口

\[
I_{p,x}=\{px+1,\ldots,px+p-1\}.
\tag{EDA-2}
\]

第 `p` 列 `px+p` 自动被 `p` 覆盖，所以行命题只需要研究 `(EDA-2)`。

对每个 `q<p`，因为 `p` 在 `mod q` 中可逆，

\[
q\mid px+k
\quad\Longleftrightarrow\quad
k\equiv -px\pmod q.
\tag{EDA-3}
\]

于是 `q` 在列集合 `[1,p-1]` 中覆盖一个算术进位类

\[
C_q(x)=\{1\le k\le p-1:\ k\equiv -px\pmod q\}.
\tag{EDA-4}
\]

早期零行等价于

\[
[1,p-1]=\bigcup_{q<p}C_q(x)
\quad\text{for some }1\le x\le p.
\tag{EDA-5}
\]

这就是“早期对角段穿过 CRT 零行覆盖证书集合”。

## 2. 早期未覆盖点必为素数

**引理 EDA-1。** 若 `1<=x<=p`、`1<=k<p`，且 `px+k` 没有 `<=p` 的素因子，则 `px+k` 是
大于 `p` 的素数。

**证明。** 令

\[
n=px+k.
\tag{EDA-6}
\]

则

\[
p<n\le p^2+p-1.
\tag{EDA-7}
\]

若 `n` 合成且没有 `<=p` 的素因子，则 `n` 的两个最小素因子都大于 `p`。由于 `p` 为奇素数，
大于 `p` 的最小可能素数至少为 `p+2`，从而

\[
n\ge (p+2)^2=p^2+4p+4>p^2+p-1,
\tag{EDA-8}
\]

矛盾。因此 `n` 只能为素数。证毕。

由此得出精确等价：

\[
\#\{k\in[1,p-1]:(px+k,M_p)=1\}
=
\pi(px+p-1)-\pi(px).
\tag{EDA-9}
\]

所以早期对角避让等价于

\[
\forall 1\le x\le p,\qquad
\pi(px+p-1)-\pi(px)\ge 1.
\tag{EDA-10}
\]

这是一条 `p` 对齐、长度约 `p`、位于 `<=p^2+p` 的短区间素数存在命题。

## 3. 互质结构刚性

若 `I_{p,x}` 中两列 `a<b` 同时被同一个素数 `q<p` 覆盖，则

\[
q\mid (px+b)-(px+a)=b-a.
\tag{EDA-11}
\]

因此：

1. `q>b-a` 时，`q` 不可能同时覆盖这两列；
2. `q>p/2` 时，`q` 在 `[1,p-1]` 中最多覆盖一列；
3. `q>p/m` 时，`q` 最多覆盖 `m-1` 列；
4. 同一个 `q` 的覆盖列必须形成公差 `q` 的列内等差骨架。

这说明零行覆盖不是任意集合覆盖，而是受列差整除关系严格限制的 CRT 覆盖。

同时，若某列未被所有 `q<p` 覆盖，则由引理 EDA-1 它不是双粗合数，而是素数。因此早期边界帽
没有“粗数补洞自由度”：所有残洞都是真实素数。

## 4. 精确包含排除公式

定义

\[
U_p(x)=\#\{1\le k\le p-1:(px+k,M_p)=1\}.
\tag{EDA-12}
\]

由 Möbius 反演，

\[
U_p(x)=
\sum_{d\mid M_p}\mu(d)\,
\#\{1\le k\le p-1:\ px+k\equiv0\pmod d\}.
\tag{EDA-13}
\]

若

\[
r_d(x)\equiv -px\pmod d,\qquad 0\le r_d(x)<d,
\tag{EDA-14}
\]

则内层计数为

\[
N_d(x)=
\begin{cases}
\left\lfloor {p-1-r_d(x)\over d}\right\rfloor+1,&1\le r_d(x)\le p-1,\\
\left\lfloor {p-1\over d}\right\rfloor,&r_d(x)=0,\\
0,&r_d(x)>p-1.
\end{cases}
\tag{EDA-15}
\]

因此

\[
U_p(x)=\sum_{d\mid M_p}\mu(d)N_d(x).
\tag{EDA-16}
\]

`Early-Diagonal-Avoidance` 的完全自足证明就是证明

\[
\min_{1\le x\le p}U_p(x)>0.
\tag{EDA-17}
\]

这给出了一个无黑箱的精确目标，但还不是闭合证明。

## 5. 为什么不能只用完整 CRT 覆盖能力

完整 CRT 周期中零行已经存在。例如全周期审计给出：

| p | 首个零行乘数 x | 首个一编号行 r=x+1 |
|---:|---:|---:|
| 13 | 168 | 169 |
| 17 | 1210 | 1211 |
| 19 | 3658 | 3659 |
| 23 | 58 | 59 |

所以不能证明“CRT 覆盖证书不存在”。正确命题是：覆盖证书集合存在，但它不与早期对角段
`1<=x<=p` 相交。

这就是比普通覆盖容量更细的“小代表元对角刚性”：完整 CRT 环面中各 `x mod q` 可以组合出覆盖
证书；早期 `x<=p` 时，所有模 `q` 的残基来自同一个小整数 `x`，相位独立性被强烈限制。

## 6. 实验审计

脚本

```text
experiments/prime_matrix_early_diagonal_avoidance_audit.py
```

利用 `(EDA-9)` 直接统计每个早期行中的素数数目。默认扫描到 `p<=2000`，输出：

```text
zero_row_count=0
global_min={'p': 19, 'min_prime_count': 1, 'min_rows': [15]}
```

选点最小余量如下：

| p | 最小早期行素数数 | 达到行 x |
|---:|---:|---|
| 23 | 2 | 14, 23 |
| 101 | 7 | 73 |
| 199 | 12 | 179 |
| 499 | 29 | 362 |
| 997 | 54 | 916 |
| 1999 | 110 | 1881 |

数据支持 `U_p(x)` 的典型量级为 `p/log p`，但最小行常在靠后对角段出现，说明早期对角避让是
短区间素数余量问题，而不是简单的前几行问题。

## 7. 证明边界

`(EDA-10)` 形如：

\[
\text{每个 }(px,px+p)\text{ 中有素数，且 }px\le p^2.
\tag{EDA-18}
\]

这是长度约为平方根尺度的短区间素数命题。普通 CRT 容量、完整周期镜像、完整周期零行稀疏性
都不能单独推出它。若引用外部短区间素数定理，只能覆盖部分早期行：

1. Bertrand 可闭合 `x=1`；
2. Nagura 型 `n` 到 `1.2n` 可闭合固定小 `x`，如 `x<=5`；
3. 现有一般短区间素数定理不足以直接给出全部 `x<=p` 的长度 `p` 窗口。

因此完全自足路线必须继续利用 `(EDA-16)` 的特殊 CRT 对角结构，而不是把它降成普通短区间素数
黑箱。

## 8. 下一步最窄可攻目标

当前最合适的下一接口是：

```text
EDA-Dual:
construct a uniform lower-bound certificate for U_p(x)
from the exact CRT inclusion-exclusion formula (EDA-16),
using the small-representative constraint 1<=x<=p.
```

具体可攻方向：

1. **低阶 Bonferroni 证书。** 对 `(EDA-16)` 截断到可变阶 `K≈c log log p`，证明尾项不能吃掉
   主余量；
2. **列差互质约束。** 利用 `(EDA-11)` 控制高素标签的重复覆盖，防止它们补完最后残洞；
3. **小代表元相位锁。** 对 `q>x` 的层使用 `x mod q=x`，对 `q<=x` 的层控制折返次数；
4. **PDEC/SAE 出口。** 若 `U_p(x)=0`，则 `(EDA-16)` 必有负端点异常，把它路由到已有的
   `Directed Endpoint CRTDefect` 或 `SAE` 证书体系。

本步的核心进展是把“早期对角段不穿过 CRT 零行”严格转为 `(EDA-17)`。它保留了同余覆盖与互质
刚性，也明确指出：全局无条件闭合仍需要一个真正的 `EDA-Dual` 下界证书。
