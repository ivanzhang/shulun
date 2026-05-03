# H3 分散单点双线性误差的大筛缺陷桥

**状态：** `bilinear_large_sieve_defect_bridge_proved_kloosterman_window_reduction_added`

本文继续只攻击当前唯一闭合目标中的最后硬障碍：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层已经把分散孤立尾点坏行写成短互补商区间上的有符号双线性素数偏差。本文继续推进一步：
证明若该双线性误差达到 `q/log y` 级，而端点、尾标签集中、夹逼低模集中都不存在，则必然产生
一个可审查的非零低模频率缺陷。换言之，最后硬障碍被压缩为：

```text
排除该非零频率/大筛缺陷，或引用能覆盖本窗口族的 dispersion/Kloosterman 型估计。
```

## 1. 双线性误差回顾

对夹逼单元 `c`，记

\[
R=R(c),\qquad \rho=\rho(c).
\]

分散孤立尾点半素数通道为

\[
\operatorname{Semi}(c)
=
\sum_{y<\ell\le p\atop \ell\in\mathbb P}
\pi\!\left(I/\ell;R,\ell^{-1}\rho\right)
+\operatorname{Endpoint}(c)+\operatorname{IsoDel}(c).
\tag{LSB-1}
\]

对应素数幸存通道为 `Prime(c)`，有符号差为

\[
\Delta(c)=\operatorname{Semi}(c)-\operatorname{Prime}(c).
\tag{LSB-2}
\]

上一层证明：若坏行在分散孤立尾点层仍成立，则存在夹逼族 `C_*` 使

\[
\sum_{c\in C_*}\Delta(c)\gg {q\over\log y}
\tag{LSB-3}
\]

除非已经触发尾标签集中、夹逼低模集中或端点缺陷。

## 2. 零均值误差函数

对每个 `c` 和 `ell`，定义互补商短区间

\[
J_{\ell,c}=I/\ell
\]

和移动剩余类

\[
a_{\ell,c}\equiv \ell^{-1}\rho(c)\pmod{R(c)}.
\tag{LSB-4}
\]

定义零均值误差

\[
E_{\ell,c}
=
\pi(J_{\ell,c};R(c),a_{\ell,c})
-
{ |J_{\ell,c}| \over \varphi(R(c))\log(q^2/\ell)} .
\tag{LSB-5}
\]

端点与孤立删除项单独记入

\[
\mathcal B(C_*)=\sum_{c\in C_*}\operatorname{Endpoint}(c)+\operatorname{IsoDel}(c)
-\sum_{c\in C_*}\operatorname{Prime}(c)+\operatorname{PrimeMain}(c).
\tag{LSB-6}
\]

于是大偏差 `(LSB-3)` 可写成

\[
\sum_{c\in C_*}\sum_{y<\ell\le p}E_{\ell,c}
+\mathcal B(C_*)
\gg {q\over\log y}.
\tag{LSB-7}
\]

若 `\mathcal B(C_*)` 不大，则主误差来自 `E_{\ell,c}`。

## 3. 有限 Fourier 展开

对每个模 `R`，把剩余类指示函数写为

\[
1_{m\equiv a\pmod R}-{1\over\varphi(R)}1_{(m,R)=1}
=
{1\over\varphi(R)}
\sum_{\chi\ne\chi_0\pmod R}
\overline{\chi(a)}\chi(m)
\tag{LSB-8}
\]

其中只在 `(a,R)=1`、`(m,R)=1` 的单位类上展开；非单位端点或小素冲突并入夹逼低模缺陷。

因此

\[
E_{\ell,c}
=
{1\over\varphi(R(c))}
\sum_{\chi\ne\chi_0\pmod{R(c)}}
\overline{\chi(a_{\ell,c})}
\sum_{m\in J_{\ell,c}\cap\mathbb P}\chi(m)
+\operatorname{SmoothErr}_{\ell,c}.
\tag{LSB-9}
\]

注意

\[
\chi(a_{\ell,c})
=
\chi(\ell^{-1}\rho(c))
=
\chi(\rho(c))\,\overline{\chi(\ell)}.
\tag{LSB-10}
\]

于是非主项具有真正双线性形态：

\[
\sum_{\ell}\overline{\chi(\ell)}
\sum_{m\in J_{\ell,c}\cap\mathbb P}\chi(m).
\tag{LSB-11}
\]

这就是当前硬点的精确频率形态。

## 4. 大误差推出非零频率缺陷

设无端点大误差、无夹逼低模集中且平滑误差总和为

\[
O\!\left({q\over(\log y)^2}\right).
\tag{LSB-12}
\]

若仍有

\[
\left|\sum_{c\in C_*}\sum_{\ell}E_{\ell,c}\right|
\ge \eta {q\over\log y},
\tag{LSB-13}
\]

则由 `(LSB-9)` 与三角不等式，存在某个模 `R`、某个非主角色 `chi mod R`、以及一族夹逼单元
`C_R`，使

\[
\left|
\sum_{c\in C_R}
{\overline{\chi(\rho(c))}\over\varphi(R)}
\sum_{y<\ell\le p\atop \ell\in\mathbb P}
\overline{\chi(\ell)}
\sum_{m\in J_{\ell,c}\cap\mathbb P}\chi(m)
\right|
\gg_\eta
{q\over\log y\,\mathcal M},
\tag{LSB-14}
\]

其中 `\mathcal M` 是参与夹逼模和角色数量的显式对数型账本因子。

这就是非零频率缺陷。它不是启发式，而是有限 Fourier 反演的直接结果。

## 5. 大筛上界为什么仍差一步

对 `(LSB-14)` 做普通 Cauchy--Schwarz 与大筛，只能得到形如

\[
\sum_{\chi\ne\chi_0}
\left|
\sum_{\ell} \alpha_\ell\overline{\chi(\ell)}
\sum_{m\in J_\ell\cap\mathbb P}\chi(m)
\right|
\le
\text{LargeSieveBound}.
\tag{LSB-15}
\]

但在本问题中，`J_\ell` 的长度为

\[
|J_\ell|\le {q\over\ell},
\tag{LSB-16}
\]

当 `ell` 接近 `q` 时是常数级；当 `ell` 较小时也只是短互补商窗口。普通大筛会损失一个过大的
模数因子，不能自动给出 `O(q/log^2 y)` 的目标误差。

因此本层诚实结论是：

```text
当前最后硬输入不是普通大筛；
而是带短窗口、移动互补商同余和素数权的 dispersion/Kloosterman 型抵消。
```

这与二次筛中已出现的 BMD/KLS-window 障碍同型，但这里仍在 H3 行命题的单点尾块分支内部。

## 6. 最终可引用输入模板

可把最后硬输入写成如下定理模板。

**H3-DSB-LS/KLS 输入。** 对所有相邻素数 `p<q`、所有 `y>q^(2/3)`、所有无集中夹逼族 `C_*`，
有

\[
\sum_{c\in C_*}\sum_{y<\ell\le p}E_{\ell,c}
=
O\!\left({q\over(\log y)^2}\right),
\tag{LSB-17}
\]

除非 `(LSB-14)` 的非零频率缺陷触发 `PDEC/ColumnCRT/cofactor`。

若该输入证明或可由外部 dispersion/Kloosterman 定理覆盖，则

```text
Distributed Singleton Bilinear Exclusion
=> Singleton Tail Exclusion
=> H3 tail branch closure.
```

若该输入未证明，H3/行命题仍不能宣称无条件闭合。

## 7. 本步实际推进

本步完成：

1. 把分散双线性误差写成零均值互补商误差 `E_{ell,c}`；
2. 对夹逼模 `R(c)` 做有限 Fourier/角色展开；
3. 利用 `a_{\ell,c}=ell^{-1}rho(c)` 得到真正双线性相位；
4. 证明大误差必推出非主角色上的非零频率缺陷 `(LSB-14)`；
5. 明确普通大筛仍不足，最后需要短窗口 dispersion/Kloosterman 抵消或缺陷排斥。

这一步没有转换命题，只把最后硬障碍压到可引用、可审查的频率估计层。

## 8. Kloosterman 窗口化

后续文件

```text
docs/monograph/prime-matrix-h3-dsb-kloosterman-window-reduction.md
```

把第 6 节的非主角色频率缺陷进一步改写为加性逆元相位。由

\[
m\equiv \rho\bar\ell\pmod R
\]

的有限加性展开得到 Kloosterman 核

\[
e\!\left(-{h\rho\bar\ell\over R}\right).
\]

这给出短互补商窗口上的 Kloosterman 双线性和，并把最后硬点拆成四个同一命题内部的分支：
`KLS-window` 覆盖、`high-lcm clamp`、`high-frequency endpoint`、`coefficient concentration`。
