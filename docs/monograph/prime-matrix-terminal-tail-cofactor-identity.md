# Terminal-SAE 尾互补因子恒等式

**状态：** `tail_incidence_exactly_short_yrough_cofactor_intervals`

本文继续压缩 `TSI-or-PDEC` 中的尾命中项 `T_y(h)`。核心结论是：尾命中不是抽象 CRT 覆盖，而是精确等于一族极短互补因子区间中的 `y`-rough 计数。

## 1. 尾命中到乘法分解

仍设终端镜像块

\[
B_h=[(h-1)q,hq-1],
\]

并取

\[
y=\max(2,\lfloor p/e\rfloor).
\]

若骨架点 `m∈B_h` 被尾素数 `y<\ell<=p` 命中，则

\[
m\equiv q^2\pmod\ell.
\]

等价地

\[
q^2-m=\ell t.
\tag{1}
\]

由于 `m` 已避开所有 `r<=y` 的坏类，`q^2-m` 不被任何 `r<=y` 整除。又 `\ell>y`，故互补因子 `t` 也避开所有 `r<=y`：

\[
P^-(t)>y.
\]

因此

\[
T_y(h)=
\sum_{y<\ell\le p}
\#\left\{
t:
\left\lceil {q^2-hq+1\over \ell}\right\rceil
\le t\le
\left\lfloor {q^2-(h-1)q\over \ell}\right\rfloor,
\ P^-(t)>y
\right\}.
\tag{2}
\]

这是精确恒等式，不是估计。

## 2. 极短区间长度

每个互补因子区间长度最多为

\[
1+{q\over \ell}
<
1+{q\over y}.
\]

取 `y=floor(p/e)` 且由 Bertrand `q<2p`，得长度小于 `1+2e<7`。因此尾项实际由常数长度的 `y`-rough 互补区间组成。

更强的外部素数间隙输入会把 `q/p` 压到接近 `1`，从而把长度压到约 `1+e<4`。实验 `docs/monograph/prime-matrix-terminal-tail-cofactor-audit.md` 在 `p<=1000` 中的最大区间长度为 `4`。

## 3. 互补因子素性阈值

若

\[
t<y^2,
\tag{3}
\]

则 `P^-(t)>y` 的 `t` 必为素数。由 `(2)`，

\[
t\le {q^2\over y}.
\]

因此只要

\[
{q^2\over y}<y^2,
\tag{4}
\]

尾互补因子全部为素数。

用 Bertrand 的 `q<2p` 与 `y≈p/e`，`(4)` 对所有充分大 `p` 成立；小 `p` 可有限验证。若使用 Nagura 型 `q<6p/5`，阈值进一步降到很小范围。

实验显示，在 `p<=1000` 中，复合 `y`-rough 互补因子只出现在 `p<=19`，最后一次为 `p=19`。

## 4. TSI 的新形式

由 `(2)`，`TSI`

\[
G_y(h)>T_y(h)
\]

变成：

```text
低筛骨架点数
>
尾素数 ell 对常数长度互补 y-rough 区间的总计数。
```

对 `p` 超过素性阈值后，右侧进一步变成：

```text
尾素数 ell 对常数长度互补素数区间的总计数。
```

这比原来的 CRT 覆盖问题更窄：右侧不是任意尾类覆盖，而是一族极短互补素数窗口。

## 5. 审稿边界

本文证明了尾项的精确恒等式与极短区间化，但没有证明 `G_y(h)>T_y(h)`。剩余仍是两个定量输入：

1. 低筛骨架 `G_y(h)` 的短块下界；
2. 极短互补 `y`-rough/素数区间总和的上界。

若其中任一项出现异常，则应进入 `PDEC`：低筛骨架异常偏小对应低模端点持续亏损；尾互补区间异常偏大对应尾锚持续集中。
