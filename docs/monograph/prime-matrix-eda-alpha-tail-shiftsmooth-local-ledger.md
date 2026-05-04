# ShiftSmooth 的局部状态账本

**状态：** `alpha_tail_shiftsmooth_local_ledger_reduction_open`

本文处理 `ShiftSmooth(r)` 的第一层刚性：对每个素数 `q`，位移 `r` 是否被 `q` 整除会改变
`d` 与 `d+r` 的局部状态数量。这是二点筛中“二禁降一禁”现象在 AlphaTail 加法能量层的精确版本。

## 1. ShiftSmooth 对象

固定

\[
D_\sigma=\{d\in(B,2B]:d\mid M_y,\ d\ {\rm squarefree},\ \mu(d)=\sigma\},
\qquad \sigma\in\{\pm1\}.
\tag{SSL-1}
\]

位移相关为

\[
C_\sigma(r)=\#\{d\in D_\sigma:d+r\in D_\sigma\}.
\tag{SSL-2}
\]

也就是 `d` 与 `d+r` 同时为 `y`-smooth squarefree，且 Möbius 符号相同。

## 2. 单素数局部状态

先只看模 `q` 的可除性状态。

若 `q\nmid r`，则

\[
d\equiv0\pmod q
\quad\Longleftrightarrow\quad
d+r\not\equiv0\pmod q,
\tag{SSL-3}
\]

并且两种单边可除状态分别是两个不同剩余类：

\[
d\equiv0\pmod q,\qquad d\equiv-r\pmod q.
\tag{SSL-4}
\]

因此局部状态分为：

```text
neither: q-2 个剩余类；
left-only: 1 个剩余类；
right-only: 1 个剩余类；
both: 0 个剩余类。
```

若 `q|r`，则

\[
d\equiv0\pmod q
\quad\Longleftrightarrow\quad
d+r\equiv0\pmod q.
\tag{SSL-5}
\]

局部状态塌缩为：

```text
neither: q-1 个剩余类；
both: 1 个剩余类；
left-only/right-only: 0 个剩余类。
```

这就是本层的二禁降一禁：`q\nmid r` 时两个单边零类分开；`q|r` 时它们合并为同一个零类。

## 3. 平方自由局部约束

平方自由还要求

\[
q^2\nmid d,\qquad q^2\nmid d+r.
\tag{SSL-6}
\]

在模 `q^2` 上，被禁止的平方零类个数为

\[
a_q(r)=
\begin{cases}
1,& q^2\mid r,\\
2,& q^2\nmid r.
\end{cases}
\tag{SSL-7}
\]

因此平方自由对的局部密度因子为

\[
1-{a_q(r)\over q^2}.
\tag{SSL-8}
\]

这给出严格的局部奇异因子来源。

## 4. 同符号条件的精确代数化

在平方自由支撑上，

\[
\mathbf 1_{\mu(d)=\sigma}\mathbf 1_{\mu(d+r)=\sigma}
=
{1\over4}
\left(
1+\sigma\mu(d)+\sigma\mu(d+r)+\mu(d)\mu(d+r)
\right).
\tag{SSL-9}
\]

因此 `ShiftSmooth(r)` 可分解为四个通道：

1. 无符号双光滑平方自由通道；
2. 左侧 Möbius 通道；
3. 右侧 Möbius 通道；
4. 双 Möbius 相关通道。

`q|r` 时，局部可除性同步，第四项更容易为正；`q\nmid r` 时，单边状态会制造符号翻转。

## 5. 筛模型接口

定义奇异因子账本

\[
\mathfrak S(r;y)
=
\prod_{q\le y}
\left(1-{a_q(r)\over q^2}\right)
\cdot
\mathfrak M_\sigma(r;y),
\tag{SSL-10}
\]

其中第一因子来自平方自由，`\mathfrak M_sigma` 记录 `(SSL-9)` 的 Möbius 同符号通道。
本文不把该乘积声称为已证渐近式；它只是下一步上界筛的精确局部输入。

若某个 `r` 的 `C_sigma(r)` 大幅超过由 `(SSL-10)` 给出的可接受包络，则失败只能来自：

```text
Möbius 同符号相关异常；
y-smooth 尾部异常；
端点/ColumnCRT 相位集中。
```

这些分别进入 `PDEC/ColumnCRT/SAE` 或后续 `ShiftSmooth` 上界义务。

## 6. 审稿边界

已证明：

```text
ShiftSmooth(r) 的局部状态与 q|r / q^2|r 的奇异因子账本。
```

尚未证明：

```text
C_sigma(r) 满足所需全局上界。
```

下一步最小硬点是把 `(SSL-10)` 变成可用的 Selberg/Rankin 上界包络；若失败，则输出具体
Möbius 相关、smooth-tail 或 ColumnCRT 缺陷。
