# H3 分散孤立尾点的有符号双线性障碍

**状态：** `distributed_singleton_bilinear_obstruction_formalized_signed_estimate_open`

本文继续只攻击当前唯一剩余硬障碍：

```text
Distributed Singleton Signed Excess.
```

上一层已经证明：尾标签集中与夹逼低模集中都能进入命名缺陷；真正剩下的是分散孤立尾点仍可在
自然量级容纳双粗半素数。本文把这部分写成精确的尾标签--互补商双线性计数，并证明：

```text
若坏行仍成立且无集中缺陷，则必须存在一个有符号双线性分布缺陷。
```

这不是转换命题；它是 `Singleton Tail Exclusion` 内部的最后形式。

## 1. 高 cutoff 下的半素数化

取

\[
y>q^{2/3}.
\tag{DSB-1}
\]

若孤立尾点 `a` 满足

\[
a=\ell m,\qquad y<\ell=P^-(a)\le p,\qquad P^-(m)\ge \ell,\qquad a<q^2,
\tag{DSB-2}
\]

则 `m` 必为素数。否则 `m` 至少含两个不小于 `ell` 的素因子，从而

\[
a\ge \ell^3>y^3>q^2,
\]

矛盾。

因此在本层，分散孤立尾点就是一族双素乘积

\[
a=\ell m,\qquad y<\ell\le p,\qquad m\in\mathbb P,\qquad m\ge\ell .
\tag{DSB-3}
\]

这把“尾粗合数”精确半素数化。

## 2. 夹逼单元中的双线性计数

固定夹逼单元

\[
c=(\delta_-,\delta_+,r_-,r_+),
\qquad r_\pm\le y,
\tag{DSB-4}
\]

并令

\[
R(c)=\operatorname{lcm}(r_-,r_+),\qquad \rho(c)\pmod{R(c)}
\tag{DSB-5}
\]

为左右小骨架夹逼给出的低模类。若夹逼同余不相容，则该 `c` 不贡献。

设行窗口为 `I`，长度 `H<=q+O(1)`。定义半素数通道

\[
\operatorname{Semi}(c)
=
\sum_{y<\ell\le p\atop \ell\in\mathbb P}
\sum_{m\in\mathbb P}
1_I(\ell m)\,
1_{\ell m\equiv\rho(c)\,(\bmod R(c))}\,
1_{\mathrm{iso}}(\ell m;c).
\tag{DSB-6}
\]

这里 `1_iso` 表示该点确为孤立尾点，即左右相邻 H3 候选由小骨架覆盖；它只删点，不增点。

定义同一夹逼单元中的素数幸存通道

\[
\operatorname{Prime}(c)
=
\sum_{n\in I\cap\mathbb P}
1_{n>p}\,
1_{n\equiv\rho(c)\,(\bmod R(c))}\,
1_{\mathrm{iso\text{-}slot}}(n;c).
\tag{DSB-7}
\]

`1_iso-slot` 表示 `n` 位于同样的 H3 候选槽且左右小骨架夹逼相同。它是与半素数通道对偶的
素数幸存槽。

定义有符号差

\[
\Delta(c)=\operatorname{Semi}(c)-\operatorname{Prime}(c).
\tag{DSB-8}
\]

坏行假设 `M_y=empty` 意味着所有应由素数幸存通道承载的质量都被半素数通道替代。因此在无
尾标签集中、无夹逼低模集中的分散分支中，存在一族夹逼单元 `C_*` 使

\[
\sum_{c\in C_*}\Delta(c)
\gg {q\over\log y}
\tag{DSB-9}
\]

除去已由长链二维上筛控制的 `O(q/log^2 y)` 边误差。

## 3. 双线性展开

对每个 `c` 和 `ell`，由

\[
\ell m\equiv\rho(c)\pmod{R(c)}
\tag{DSB-10}
\]

且 `(ell,R(c))=1`，得到互补商同余

\[
m\equiv \ell^{-1}\rho(c)\pmod{R(c)}.
\tag{DSB-11}
\]

所以

\[
\operatorname{Semi}(c)
=
\sum_{y<\ell\le p\atop \ell\in\mathbb P}
\pi\!\left(
{I\over \ell};
R(c),\ell^{-1}\rho(c)
\right)
+\operatorname{Endpoint}(c)+\operatorname{IsoDel}(c),
\tag{DSB-12}
\]

其中 `I/ell` 是互补商短区间

\[
I/\ell=\{m:\ell m\in I\},
\tag{DSB-13}
\]

其长度为

\[
|I/\ell|\le {q+O(1)\over \ell}.
\tag{DSB-14}
\]

`Endpoint(c)` 是端点取整误差，`IsoDel(c)<=0` 是孤立条件删除项。

这一步是确定性的：孤立半素数过剩等价于许多互补商短区间中，素数落入由 `ell^{-1}\rho(c)`
决定的移动同余类。

## 4. 若无命名缺陷，则必须满足的有符号估计

设 `Main(c)` 是对应通道的局部主项。例如可取

\[
\operatorname{Main}(c)
=
\sum_{y<\ell\le p\atop \ell\in\mathbb P}
{ |I/\ell| \over \varphi(R(c))\log(q^2/\ell)}
-
{ |I| \over \varphi(R(c))\log(q^2)}.
\tag{DSB-15}
\]

这个主项只用于定义缺陷；不同平滑主项只改变端点误差。

定义分散有符号误差

\[
\mathcal E(C_*)
=
\sum_{c\in C_*}
\left(\Delta(c)-\operatorname{Main}(c)\right).
\tag{DSB-16}
\]

则有确定性二分：

```text
若 (DSB-9) 成立而 Main 总量不足以解释该正差，
则 E(C_*) 必为 q/log y 级正异常。
```

该异常只能来自以下位置：

1. **短互补商素数偏差**：

\[
\pi(I/\ell;R(c),\ell^{-1}\rho(c))
\]

在大量 `ell,c` 上同时偏大；

2. **端点 sawtooth 偏差**：`I/ell` 的端点取整误差同号累积；
3. **夹逼低模偏差**：`rho(c) mod R(c)` 的槽位分布非 CRT 均衡；
4. **互补商相位偏差**：`ell^{-1}\rho(c)` 在 `R(c)` 上非均匀。

后三项正是 `endpoint / PDEC / ColumnCRT / cofactor` 缺陷。若它们都被排除，剩下的就是第一项：
互补商短区间中的有符号素数偏差。

## 5. 与奇偶障碍的关系

这里必须保持审稿诚实。`(DSB-12)` 仍然要求控制长度

\[
|I/\ell|\le {q\over\ell}
\tag{DSB-17}
\]

的短区间素数计数，且 `ell` 可接近 `p~q`，于是许多互补区间长度为常数级或对数级。
普通 PNT、Mertens 乘积、二维 rough 对上筛都不能给出所需的逐行有符号下界。

因此本层真正证明的是：

```text
Distributed singleton bad row
=> signed bilinear prime-distribution defect
=> endpoint/PDEC/ColumnCRT/cofactor, unless one proves a new signed short-cofactor estimate.
```

它没有闭合最后一项，但把最后一项从“半素数过剩”压成明确的双线性素数分布估计。

## 6. 最终硬输入的精确形式

当前唯一剩余可写为：

```text
H3 Distributed Singleton Bilinear Exclusion.
For y>q^(2/3), every distributed singleton family C_* satisfying the no-concentration
conditions has
sum_{c in C_*} Delta(c) <= O(q/log^2 y)
unless it produces endpoint/PDEC/ColumnCRT/cofactor defect.
```

若该定理被证明，则孤立尾点分支闭合，连同前面的宏观尾链排斥即可闭合尾分支。
若该定理未证明，H3/行命题仍不能宣称无条件闭合。

## 7. 本步实际推进

本步完成：

1. 高 cutoff 下孤立尾点严格半素数化；
2. 把孤立尾点计数写成 `ell,m` 双线性素数计数；
3. 把夹逼相位转化为互补商移动同余类 `m≡ell^{-1}rho(c) mod R(c)`；
4. 把分散半素数过剩压成有符号双线性误差 `E(C_*)`；
5. 明确最后未闭合项是短互补商素数偏差，而不是平均尺度、有限模板或尾链容量。

这一步继续保持在当前唯一闭合目标内部。
