# Terminal-SAE 单尾抵消恒等式与最终硬核压缩

**状态：** `proved_exact_identity_reduces_TSI_to_reserve_vs_collision`

本文接续 `prime-matrix-terminal-sae-split-inequality.md` 与
`prime-matrix-terminal-tail-cofactor-identity.md`。核心结论是：
`TSI` 的差值不是一般的筛余估计，而有一个精确抵消结构。

```text
一尾因子项完全抵消；
终端覆盖只能由“多尾碰撞超额”压倒“无尾储备”导致。
```

这把当前硬点从一般的 `G_y(h)>T_y(h)` 压缩为一个更窄的
`reserve > collision` 不等式。

## 1. 变量与端点修正

设 `p<q` 为相邻奇素数，取

\[
y=\max(2,\lfloor p/e\rfloor).
\]

在终端镜像变量 `m=q^2-n` 中，镜像块

\[
B_h=[(h-1)q,hq-1]
\]

对应 `n` 区间

\[
I_h=[q^2-hq+1,\ q^2-(h-1)q],
\qquad 1\le h\le q .
\]

为了从旧 `p`-筛幸存者推出素数，必须排除两个端点：

- `n=1`：不是素数；
- `n=q^2`：对应镜像点 `m=0`，不是旧筛可用幸存者。

因此下面所有计数均在

\[
I_h^\ast=I_h\setminus\{1,q^2\}
\]

上进行。

## 2. 精确重写

令

\[
R_y(I_h)=\{n\in I_h^\ast: r\nmid n\ \text{for every prime } r\le y\}.
\]

这与低筛骨架完全相同，因为

\[
m\not\equiv q^2\pmod r
\quad\Longleftrightarrow\quad
q^2-m=n\not\equiv0\pmod r.
\]

再令

\[
\omega_T(n)=\#\{\ell:\ y<\ell\le p,\ \ell\ \text{prime},\ \ell\mid n\}
\]

为 `n` 的不同尾素因子数。

于是

\[
G_y(h)=\sum_{n\in R_y(I_h)}1,
\qquad
T_y(h)=\sum_{n\in R_y(I_h)}\omega_T(n),
\]

并得到精确恒等式

\[
G_y(h)-T_y(h)
=
\sum_{n\in R_y(I_h)}(1-\omega_T(n)).
\tag{CCI}
\]

**证明。**
第一式是 `m=q^2-n` 的变量替换。第二式中，尾命中
`m≡q^2 (mod ell)` 等价于 `ell|n`；对所有 `y<ell<=p`
求和正是不同尾素因子的重数。两式相减即得 `(CCI)`。证毕。

## 3. 单尾抵消

把 `R_y(I_h)` 按 `\omega_T(n)` 分层：

\[
R_j(h)=\{n\in R_y(I_h):\omega_T(n)=j\}.
\]

则 `(CCI)` 变为

\[
G_y(h)-T_y(h)
=
|R_0(h)|-\sum_{j\ge2}(j-1)|R_j(h)|.
\tag{CCI'}
\]

特别地，所有 `j=1` 的点贡献为 `0`。这说明：

- 形如 `n=ell*t`、恰有一个尾素因子 `ell` 的大量半素数不是障碍；
- 真正负项只来自含至少两个尾素因子的碰撞；
- 正项是完全没有尾素因子的低筛储备。

因此 `TSI` 等价于

\[
|R_0(h)|
>
\sum_{j\ge2}(j-1)|R_j(h)|.
\tag{RCI}
\]

这就是当前最窄的反例排斥不等式。

## 4. 双尾化阈值

若

\[
y^3>q^2,
\tag{2T}
\]

则每个 `n<q^2` 至多含两个不同尾素因子。因为三个尾素因子的
乘积严格大于 `y^3`，从而大于 `q^2`。

在 `(2T)` 下，

\[
G_y(h)-T_y(h)=|R_0(h)|-|R_2(h)|.
\tag{2RCI}
\]

所以终端覆盖的最终硬核进一步简化为：

```text
每个终端 q 块中，无尾储备数 > 双尾碰撞数。
```

这比原来的“尾素数能否覆盖低筛骨架”更锋利，因为所有一尾项已经
从方程中严格消失。

## 5. 反例的必要形态

若某个终端块违反 `TSI`，则由 `(CCI')` 必有

\[
|R_0(h)|
\le
\sum_{j\ge2}(j-1)|R_j(h)|.
\tag{F}
\]

在双尾区间内，这等价于

\[
|R_0(h)|\le |R_2(h)|.
\tag{F2}
\]

因此反例必须同时满足两个强约束：

1. 无尾储备异常偏小；
2. 双尾乘积异常集中在同一长度 `q` 的终端块内。

这给出了新的 `PDEC/Tail-anchor` 出口：若 `(F2)` 发生，则双尾乘积
`ell_1 ell_2` 在一个短块中密集聚集，而无尾储备没有同步增长。
这种失衡不能再由一尾半素数解释，必须表现为端点相位或尾锚相位
的持续偏置。

## 6. 实验核查

审计脚本：

```text
experiments/prime_matrix_terminal_sae_cancellation_audit.py
```

最新报告：

```text
docs/monograph/prime-matrix-terminal-sae-cancellation-audit.md
```

参数 `max_p=1500`、`y=floor(p/e)` 下：

- `p>=7` 未认证记录数为 `0`；
- `p>=7` 最小余量为 `1`；
- 严格排除 `n=1,q^2` 后余量仍为正；
- 从 `p=11` 起样本中实际 `omega_tail<=2`；
- 由简单条件 `y^3>q^2` 保证双尾化的最后例外样本为 `p=31`。

这说明当前实验证据并不依赖端点误算，也不依赖一尾项；真正余量来自
`无尾储备 > 多尾碰撞超额`。

## 7. 剩余证明义务

本文已经证明精确恒等式与硬点压缩，但尚未证明 `(RCI)` 对所有
相邻 `p<q` 与全部 `h` 成立。正式闭合仍需完成下列二选一：

1. **直接证明 `RCI`：**
   \[
   |R_0(h)|
   >
   \sum_{j\ge2}(j-1)|R_j(h)|.
   \]
2. **异常出口证明：**
   若 `RCI` 失败，则双尾碰撞集中与无尾储备亏损必然产生可检测的
   `PDEC/Tail-anchor` 持续缺陷，并由既有端点缺陷排斥机制排除。

下一步最优攻坚对象因此不是一般筛余下界，而是：

```text
RCI/PDEC:
无尾储备—双尾碰撞不等式，或其失败触发持续端点/尾锚缺陷。
```

这是目前递推证明链条中最小、最具体、可逐项审查的剩余硬核。
