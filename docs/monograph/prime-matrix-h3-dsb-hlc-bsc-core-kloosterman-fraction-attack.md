# BSC-core：Kloosterman 分数相位硬攻

**状态：** `bsc_reduced_to_kloosterman_fraction_large_sieve_core_not_closed`

本文继续只攻击同一个剩余：

```text
BSC-core: balanced complete Kloosterman bilinear correlation logarithmic saving.
```

本步不把命题换成新的外部问题，而是把 `(BSA-13)` 的完整 Kloosterman 和逐项展开。这样剩余
不再藏在符号 `S(A,B;u)S(A',B';v)` 中，而显式变成平衡双模数的 Kloosterman 分数相位

\[
e\!\left({\bar v R\over u}+{\bar u T\over v}\right).
\tag{KFA-1}
\]

结论是：`BSC-core` 等价地压缩为一个更内部的 `KFLS-core`，即该分数相位族的任意对数节省。
这一步完成相位显形、退化方程定位和对角/非对角职责切分；但尚未证明 `KFLS-core`，所以仍
不能宣称完全自足闭合。

## 1. 起点：BSC 完整双模数核

从

\[
\mathcal BSC
=
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
{1\over uv}\sum_{\ell\bmod uv}\widehat\beta_{uv}(\ell)
S((a_h+\ell)\bar v,b_h\bar v;u)
S((a_h+\ell)\bar u,b_h\bar u;v)
\tag{KFA-2}
\]

出发，其中

\[
U,V=C^{1/2}\log^{O(1)}y,\qquad UV\asymp C.
\tag{KFA-3}
\]

`\widehat\beta_{uv}` 由同一个全局 `\beta_sW(s/S)` 经有限 Fourier 完成产生，并满足
Parseval 账本 `(BSA-7)`。

## 2. 完整和的逐项展开

展开两个 Kloosterman 和：

\[
S((a_h+\ell)\bar v,b_h\bar v;u)
=
\sum_{x\bmod u}^{*}
e_u\!\left(\bar v((a_h+\ell)x+b_h\bar x)\right),
\tag{KFA-4}
\]

\[
S((a_h+\ell)\bar u,b_h\bar u;v)
=
\sum_{z\bmod v}^{*}
e_v\!\left(\bar u((a_h+\ell)z+b_h\bar z)\right).
\tag{KFA-5}
\]

定义局部相位多项式

\[
R_{h,\ell,u}(x)
\equiv
(a_h+\ell)x+b_h\bar x\pmod u,
\qquad x\in(\mathbb Z/u\mathbb Z)^*,
\tag{KFA-6}
\]

\[
T_{h,\ell,v}(z)
\equiv
(a_h+\ell)z+b_h\bar z\pmod v,
\qquad z\in(\mathbb Z/v\mathbb Z)^*.
\tag{KFA-7}
\]

于是 `(KFA-2)` 等于

\[
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
{1\over uv}\sum_{\ell\bmod uv}\widehat\beta_{uv}(\ell)
\sum_{x\bmod u}^{*}\sum_{z\bmod v}^{*}
e\!\left(
{\bar v\,R_{h,\ell,u}(x)\over u}
+
{\bar u\,T_{h,\ell,v}(z)\over v}
\right).
\tag{KFA-8}
\]

这是 `BSC-core` 的内部矛盾场：`u` 与 `v` 不再只是模数，而是互为相位中的逆元。

## 3. 退化相位的精确方程

一侧失去振荡当且仅当

\[
R_{h,\ell,u}(x)\equiv0\pmod u
\tag{KFA-9}
\]

或

\[
T_{h,\ell,v}(z)\equiv0\pmod v.
\tag{KFA-10}
\]

由于 `x,z` 是单位，`(KFA-9)` 等价于二次同余

\[
(a_h+\ell)x^2+b_h\equiv0\pmod u,
\tag{KFA-11}
\]

`(KFA-10)` 等价于

\[
(a_h+\ell)z^2+b_h\equiv0\pmod v.
\tag{KFA-12}
\]

因此退化相位不是任意大集合，而是平方根型薄集合。由 CRT 分解到素幂，可得初等根数包络：

\[
\#\{x\bmod u: x\in(\mathbb Z/u\mathbb Z)^*,\ (a_h+\ell)x^2+b_h\equiv0(u)\}
\ll
2^{\omega(u)+1}\,(a_h+\ell,b_h,u)^{1/2}.
\tag{KFA-13}
\]

`v` 侧同理。证明只需逐个素幂使用二次同余根数界，再由 CRT 相乘。该界显示：退化层最多
付出除数函数和 gcd 平方根损失；真正需要深平均抵消的是非退化层

\[
R_{h,\ell,u}(x)\not\equiv0\pmod u,
\qquad
T_{h,\ell,v}(z)\not\equiv0\pmod v.
\tag{KFA-14}
\]

## 4. 互逆分数相位的刚性

在非退化层，`u,v` 同时运动时相位为

\[
\Phi_{R,T}(u,v)
=
{\bar v R\over u}+{\bar u T\over v}.
\tag{KFA-15}
\]

若固定 `u`，由于 `V\asymp U`，`v mod u` 的平均长度只有常数级；若固定 `v`，`u mod v`
也只有常数级。因此单侧大筛无法给出任意对数节省。节省必须来自二维相位 Hessian：

\[
(u,v)\mapsto
\left(\bar v\bmod u,\ \bar u\bmod v\right)
\tag{KFA-16}
\]

的联合非线性。换言之，`KFLS-core` 必须同时使用两个模数的互逆耦合，而不是把其中一边视为
固定参数。

## 5. 最小新核心：KFLS-core

**KFLS-core（Kloosterman-fraction large sieve core）。** 设 `U,V` 满足 `(KFA-3)`，系数
`\widehat\beta_{uv}` 满足 `(BSA-7)`。该核心由两个子义务组成：

1. **退化账本。** 将 `(KFA-8)` 限制到 `R_{h,\ell,u}(x)=0` 或 `T_{h,\ell,v}(z)=0` 的部分，结合
   根数包络 `(KFA-13)` 后满足
   \[
   |\mathcal BSC_{\rm deg}|
   \ll_A {\mathcal B(UV,S,H)\over\log^A y}.
   \tag{KFA-17a}
   \]
2. **非退化分数相位。** 在 `(KFA-14)` 下有

\[
\left|
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
{1\over uv}\sum_{\ell\bmod uv}\widehat\beta_{uv}(\ell)
\sum_{\substack{x\bmod u\\R_{h,\ell,u}(x)\ne0}}^{*}
\sum_{\substack{z\bmod v\\T_{h,\ell,v}(z)\ne0}}^{*}
e\!\left(
{\bar v\,R_{h,\ell,u}(x)\over u}
+
{\bar u\,T_{h,\ell,v}(z)\over v}
\right)
\right|
\ll_A
{\mathcal B(UV,S,H)\over\log^A y}.
\tag{KFA-17b}
\]

这就是当前最小未闭合硬点。它已经没有 trace formula 正规化、Bessel 衰减、gcd 剥离、
well-factorable 平衡化或 `s`-completion 的残留义务；只剩平衡互逆分数相位的平均抵消。

## 6. `KFLS-core => BSC-core`

**命题。** 若 KFLS-core 成立，则 BSC-core 成立。

**证明。**

1. 从 `(BSA-13)` 出发，使用 `(KFA-4)`--`(KFA-5)` 展开两个完整 Kloosterman 和，得到
   `(KFA-8)`。这是等式，不产生估计损失。
2. 将求和按 `(KFA-9)`、`(KFA-10)` 分为退化层和非退化层。
3. 退化层由 KFLS-core 的 `(KFA-17a)` 控制；其中 `(KFA-13)` 给出必须进入常数表的根数包络。
4. 非退化层正是 `(KFA-17b)`。调用 KFLS-core，并把退化层、dyadic 和端点损失通过
   `A\mapsto A+C_{\rm deg}+C_{\rm dyad}+10` 吸收。

于是得到 `(BSA-13)`，即 BSC-core。证毕。

## 7. 当前边界

本步完成了：

```text
KFLS-core => BSC-core => BWFD-core => WFD-core => KZ-E.
```

但 `KFLS-core` 本身尚未证明。下一步若继续完全自足硬攻，不能再停留在 Kloosterman 和符号层；
必须直接证明 `(KFA-17a)`--`(KFA-17b)` 的二维互逆分数相位平均抵消，或者把它进一步平方化为可审查的
四模数相关核并关闭非对角 Schur 上界。
