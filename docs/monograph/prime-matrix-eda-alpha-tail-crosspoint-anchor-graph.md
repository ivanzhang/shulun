# 跨点锚点相关的图化

**状态：** `alpha_tail_crosspoint_anchor_graph_reduction_open`

本文继续压缩 `distributed anchor energy` 的跨点相关分支。固定高素锚点 `q` 后，两个点同时被
`q` 锚住，等价于它们分别落入 `0` 或 `-r mod q` 两个类。因此跨点相关是一张显式二部/二类图的
带符号能量。

## 1. 锚点类图

对固定 `q`，定义两个类

\[
C_{q,0}=\{d\in A_r:d\equiv0\pmod q\},
\qquad
C_{q,1}=\{d\in A_r:d\equiv-r\pmod q\}.
\tag{CAG-1}
\]

令 `W_q(d)` 为单锚权。则

\[
A_q(r)=-2\left(\sum_{d\in C_{q,0}}W_q(d)+\sum_{d\in C_{q,1}}W_q(d)\right).
\tag{CAG-2}
\]

平方展开为

\[
{1\over4}|A_q(r)|^2
=
\sum_{\epsilon,\epsilon'\in\{0,1\}}
\sum_{d_1\in C_{q,\epsilon}}
\sum_{d_2\in C_{q,\epsilon'}}
W_q(d_1)W_q(d_2).
\tag{CAG-3}
\]

## 2. 差值同余结构

若 `d_i in C_{q,\epsilon_i}`，则

\[
d_1-d_2\equiv
\begin{cases}
0\pmod q,& \epsilon_1=\epsilon_2,\\
r\pmod q,& (\epsilon_1,\epsilon_2)=(0,1),\\
-r\pmod q,& (\epsilon_1,\epsilon_2)=(1,0).
\end{cases}
\tag{CAG-4}
\]

因此跨点锚点相关只能沿三类差值同余发生：

```text
d1-d2 ≡ 0, r, -r mod q.
```

这就是 ColumnCRT 的明确入口。

## 3. 二分

若跨点相关大，则至少发生一项：

1. **差值热门。**  
   存在非零差值 `s=d1-d2`，被大量锚点 `q` 命中，且 `s≡0,±r mod q`；
2. **符号相关。**  
   差值不热门，但 `W_q(d1)W_q(d2)` 在许多边上同号累积，形成低模符号 PDEC；
3. **孤窗逃逸。**  
   上述异常只发生在单个有限窗口，进入 SAE。

## 4. 差值热门约束

固定差值 `s`。能锚住该差值的 `q` 必须满足

\[
q\mid s,\qquad q\mid s-r,\qquad \text{或}\qquad q\mid s+r.
\tag{CAG-5}
\]

因此

\[
\#\{q:R<q\le y:q\ {\rm can\ anchor}\ s\}
\le
\omega_{>R}(s(s-r)(s+r)).
\tag{CAG-6}
\]

这是非常强的互质/短窗不可复用约束：一个固定差值不能被许多高素锚点复用，除非
`s(s-r)(s+r)` 有很多大素因子。这进入 Rankin/Tail 或 ColumnCRT。

## 5. 当前最小硬点

跨点相关被压成：

```text
hot difference with many high prime divisors of s(s-r)(s+r),
or low-mod signed edge correlation,
or SAE.
```

下一步应对 `(CAG-6)` 做 Rankin 上界；若失败，输出具体热门差值 `s` 与高素因子列表作为
`ColumnCRT` 证书。
