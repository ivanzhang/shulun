# PM-R2B 尾段锚定工作台

## 0. 目标

本工作台继续专攻 `PM-RHI` 中唯一真正硬点：

```text
PM-R2B:  P/Y < p <= P 的尾段大素数补洞上界。
```

上一轮已经确认：当 `p>P/Y` 时，互补商窗口长度

\[
H/p<Y
\]

小于小素筛阈值，不能逐个 `p` 使用普通上界筛得到粗数密度因子。因此必须改用尾锚、除数切换、圆柱螺旋相位块与大因子短窗不可复用。

## 1. 尾段的精确除数切换

令目标窗口

\[
I=[X,X+H),\qquad H\asymp P,
\]

并取

\[
Y=P^\alpha,\qquad e^{-1}<\alpha<1/2.
\]

尾段补洞量为

\[
B_Y^{tail}(I)=
\sum_{P/Y<p\le P}
\#\{m:P^-(m)>Y,\ pm\in I\}.
\]

交换求和得

\[
B_Y^{tail}(I)=
\sum_{\substack{m\\P^-(m)>Y}}
\#\left\{p\in\mathbb P:
\frac PY<p\le P,\quad
\frac Xm\le p<\frac{X+H}{m}
\right\}.
\]

这说明尾段不是自由覆盖问题，而是“粗互补商 `m` 锚定的短素数区间”问题。

## 2. Dyadic `m` 分解

取 `m~M`。对应素数区间长度为

\[
L_M=\frac HM.
\]

尾段约束 `P/Y<p<=P` 等价于

\[
\frac XP \lesssim m \lesssim \frac{XY}{P}.
\]

因为 `X<=P^2`，所以

\[
m\lesssim PY=P^{1+\alpha}.
\]

于是 `M` 位于从行高量级到 `P^{1+\alpha}` 的 dyadic 区间内。

对 dyadic 桶定义

\[
T(M)=
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\left(\pi\left(\frac{X+H}{m}\right)
-\pi\left(\frac Xm\right)\right)_{(P/Y,P]}.
\]

目标是证明

\[
\sum_M T(M)
\le
(\log(1/(1-\alpha))+\eta_2)|G_Y(I)|.
\tag{TSS}
\]

这里主常数 `log(1/(1-alpha))` 对应尾段

\[
\sum_{P/Y<p\le P}\frac1p.
\]

## 3. 纯几何尾锚为什么还不够

对固定 `m`，若 `M>=P`，则

\[
L_M=H/M\le1,
\]

所以每个 `m` 至多锚定 `O(1)` 个整数 `p`。这给出纯几何界

\[
T(M)\le \#\{m\sim M:P^-(m)>Y\}.
\]

但该界缺少素数密度因子 `1/log P`。因为

\[
\#\{m\sim M:P^-(m)>Y\}
\asymp M V(Y),
\]

而目标平均应含有

\[
\frac{H}{M\log P}
\]

级别的素数命中概率。

因此：

```text
大因子短窗不可复用只能给 O(1) 命中；
要达到 TSS 目标，还必须证明这些 O(1) 潜在命中不能都落在素数上。
```

这就是 `PM-R2B` 的核心困难。

## 4. 最小可审查尾锚引理

尾段真正需要的不是逐点短区间素数定理，而是一个加权平均形式。

**PTA（Prime Tail Anchor bound）。** 对所有 dyadic `M`，成立

\[
T(M)
\le
(1+\varepsilon_M)
\frac{H}{\log P}
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m
+E_M,
\tag{PTA}
\]

且

\[
\sum_M E_M=o(|G_Y(I)|),
\qquad
\sum_M \varepsilon_M
\frac{H}{\log P}
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m
\le \eta_2 |G_Y(I)|.
\]

若 `PTA` 成立，则

\[
\sum_M T(M)
\le
(1+\eta_2)
\frac{H}{\log P}
\sum_{\substack{m\\P^-(m)>Y\\X/P\lesssim m\lesssim XY/P}}\frac1m.
\]

由 Buchstab/Mertens 型粗数调和和估计，

\[
\sum_{\substack{m\le Z\\P^-(m)>Y}}\frac1m
\approx
V(Y)\log\frac{\log Z}{\log Y}.
\]

代回即可得到尾段主常数 `log(1/(1-alpha))`。

## 5. PTA 可用的方阵刚性输入

`PTA` 比短区间素数定理弱，因为它只需要在 `m` 锚的平均上控制素数出现。可用刚性如下。

### 5.1 圆柱螺旋相位块

对于固定 `m`，条件 `pm∈I` 等价于 `p` 落在一个由方阵行窗口诱导的短区间。随着 `m` 在 dyadic 桶内变化，这些短区间端点沿双曲线滑动。

若大量锚点命中素数，则对应产品 `pm` 在方阵中形成一族近似平行的尾部斜线。圆柱螺旋相位块公式可用于检测它们是否与小素锁相位异常避让。

### 5.2 大因子短窗不可复用

若两个产品

\[
p_1m_1,\quad p_2m_2
\]

落在同一长度 `H` 窗口中，并且共享某个大因子或互补商过近，则会产生短差值整除约束：

\[
|p_1m_1-p_2m_2|<H.
\]

这限制尾锚簇的局部密度。

### 5.3 互补商 `Y`-rough 约束

锚 `m` 不是任意整数，而是 `Y`-rough。若素数命中在某些相位上异常密集，则 `m` 集合必须在小素数模上表现出异常避让。该异常可回传给 GSL 小素锁层或 CRT 均衡缺陷。

### 5.4 Tail anchors

当 `m` 很小或位于边界层时，`H/m` 较长，普通 dyadic 平均不够稳定。这部分应送入既有 Tail anchors 账本，而不是在 `PTA` 中重复处理。

## 6. 目前能严格得到什么

无额外深输入时，当前可严格写下：

\[
T(M)\le
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\left(\frac HM+1\right).
\]

这只是几何界。它足以说明尾锚不可无限复用，但不足以提供素数密度节省。

要闭合 `PM-R2B`，必须进一步证明平均素数命中：

\[
\pi((X+H)/m)-\pi(X/m)
\]

在粗锚 `m` 上不能系统性地超过 `H/(m\log P)`。

这就是当前最小新增硬点。

## 7. 与外部定理的关系

`PTA` 可有两种版本。

### 7.1 外部解析输入版

若允许使用大筛/Bombieri--Vinogradov 型平均素数分布，可尝试把 `PTA` 写成加权素数短区间平均定理。该版本应明确：

- 权重为 `1_{P^-(m)>Y}` 或其筛权近似；
- 区间为倒数滑动区间 `[X/m,(X+H)/m]`；
- 平均变量是 `m`；
- 误差需小于 `|G_Y(I)|`。

### 7.2 自足矛盾场版

若不引入外部解析定理，则必须从方阵刚性推出：尾锚素数命中异常会产生

```text
小素锁避让异常
或大因子短窗复用异常
或 CRT 相位块不均衡
或 Tail-anchor 低商异常
```

并分别排除。

## 8. 本轮结论

`PM-R2B` 已被压缩为单一可审查引理：

```text
PTA: 粗互补商锚上的平均素数尾命中不超过模型主项。
```

这比原来的 `Structured-EHPD` 更明确。它也说明了具体问题在哪里：

- 纯几何非复用少一个 `1/log P`；
- 普通逐素数筛法在 `H/p<Y` 时失效；
- 必须证明粗锚平均上的素数密度节省，或把异常导入方阵 CRT 矛盾场。

下一步若继续第一优先级，应专攻 `PTA` 的两条路线之一：外部解析平均版，或完全自足的相位异常排除版。

## 9. 扩展斜线锁后的 PTA-GSL 强化

最新的广义斜率锁还能作用到尾段中的 `p` 变量本身。若 `p<=P` 是合数，则它有素因子 `q<=sqrt(P)`。把 `P±t` 斜线锁扩展到 `t<=sqrt(P)` 后，所有这种小因子层都能由圆柱螺旋相位块标记。

因此尾段可改写为：

```text
先用 GSL 删除 p-变量中的 q<=sqrt(P) 合数层；
剩余 p 候选即为素数候选；
再对粗锚 m 平均计数。
```

这给出更精确的最小接口：

**PTA-GSL。** 扩展斜线锁删除 `p` 变量中所有 `q<=sqrt(P)` 的合数相位块后，剩余候选在粗锚 `m` 平均上满足

\[
T(M)
\le
(1+\varepsilon)
\frac{H}{\log P}
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m
E_M.
\]

这一步仍不是纯代数结论。GSL 说明哪些位置被小素锁标记；要得到 `1/log P` 密度，还必须证明未锁位置在粗锚平均上不超过 Selberg 上界筛主项，或证明超额会触发 CRT 相位块异常。

所以当前真正最小硬点从 `PTA` 强化为：

```text
PTA-GSL: GSL 小素层删除后，p 候选平均密度满足 1/log P 上界。
```
