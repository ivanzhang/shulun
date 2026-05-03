# H3 小骨架过载到 PDEC 的全局桥接引理

**状态：** `proved_deterministic_bridge_not_pdec_exclusion`

本文补齐 `prime-matrix-h3-global-tail-energy-lemma.md` 中第一出口的组合桥接：

```text
SmallSkeletonOverload
=> y-rough 计数亏损
=> 低模 CRT/PDEC 缺陷函数为正。
```

该结论是全局、无限尺度、确定性的；它不排斥 PDEC，只把小骨架过载精确转化为 PDEC 入口。

## 1. 设置

设 `p<q` 为相邻奇素数，`2<=s<=q`，`A_s` 为第 `s` 个 `q` 行窗口中的完整 3 行六轮候选集合。
对 cutoff `y<p`，令

\[
W_y=\prod_{5\le r\le y} r,
\qquad
\nu_y=\prod_{5\le r\le y}\left(1-{1\over r}\right).
\]

定义

\[
C_y=\#\{n\in A_s:5\le P^-(n)\le y\},
\]

\[
R_y=\#\{n\in A_s:P^-(n)>y\}.
\]

于是恒等式为

\[
\#A_s=C_y+R_y.
\tag{SSP-1}
\]

注意这里的 `P^-(n)>y` 已自动排除 `2,3`，因为 `A_s` 本身只含六轮候选。

## 2. PDEC 缺陷函数

定义 `y`-rough 模型体积

\[
V_y=\#A_s\,\nu_y.
\]

定义低模缺陷

\[
D_y=V_y-R_y
=
\sum_{n\in A_s}
\left(
\nu_y-\mathbf 1_{(n,W_y)=1}
\right).
\tag{SSP-2}
\]

由 Möbius 展开，

\[
\mathbf 1_{(n,W_y)=1}
=
\sum_{d\mid W_y}\mu(d)\mathbf 1_{d\mid n}.
\]

因此

\[
D_y=
\sum_{d\mid W_y}
\mu(d)
\left(
{\#A_s\over d}-\#\{n\in A_s:d\mid n\}
\right)
\tag{SSP-3}
\]

这里用到恒等式 `nu_y=sum_{d|W_y}mu(d)/d`。由于每个 `d|W_y` 与 `6` 互素，六轮候选在完整
CRT 周期中落入 `d|n` 的比例正是 `1/d`；有限窗口中的偏差全部由 `(SSP-3)` 的低模项记录。
关键点是：`D_y` 是只由 `d|W_y` 的 divisibility 投影组成的低模 CRT 缺陷函数。

## 3. 小骨架过载推出 PDEC 亏损

取任意 `B,L>0`。若小骨架过载

\[
C_y>\#A_s-B-2L,
\tag{SSP-4}
\]

则由 `(SSP-1)` 得

\[
R_y<B+2L.
\]

代入 `(SSP-2)`：

\[
D_y>V_y-B-2L.
\tag{SSP-5}
\]

这就是所需桥接：小首因子覆盖过多，等价于 `y`-rough 六轮候选低于其 CRT/Mertens 模型体积，
从而强制一个低模 PDEC 缺陷。

## 4. 代入全局尺度

令

\[
B=c{q\over\log q},
\qquad
L=\lambda {q\over\log q}.
\]

若存在常数 `eta>0` 使

\[
V_y\ge (c+2\lambda+\eta){q\over\log q},
\tag{SSP-6}
\]

则 `(SSP-4)` 推出

\[
D_y>\eta {q\over\log q}.
\tag{SSP-7}
\]

这给出全局无限通用尺度的第一出口：

```text
SmallSkeletonOverload at scale c,lambda
=> PDEC defect of size eta*q/log q.
```

## 5. 与 Mertens 尺度的匹配

因

\[
\#A_s={q\over3}+O(1),
\]

且

\[
\prod_{5\le r\le y}\left(1-{1\over r}\right)
\sim {3e^{-\gamma}\over\log y},
\]

有

\[
V_y\sim e^{-\gamma}{q\over\log y}.
\tag{SSP-8}
\]

若取 `y=q^theta`，`0<theta<1`，则

\[
V_y\sim {e^{-\gamma}\over\theta}{q\over\log q}.
\]

因此只要选择

\[
c+2\lambda < {e^{-\gamma}\over\theta},
\]

则 `(SSP-6)` 在充分大 `q` 后成立。小 `q` 部分仍需有限阈值账本处理；这与当前主链的有限验证包口径一致。

## 6. 当前闭合状态

结合全局尾标签能量引理，低余量反例现在满足：

```text
M_H3(p,s)<c*q/log q
=> PDEC defect D_y > eta*q/log q
   or tail-label energy E_y(d)>lambda*q/log q.
```

仍未闭合的是最后排斥：

1. `PDEC defect D_y>eta*q/log q` 不可能在坏窗集合中持续；
2. `TailEnergy(d,L)` 必进入 `H3-PDEC/ColumnCRT` 并被排除。

因此本文完成的是第一出口的全局尺度桥接，不是 H3 正下界本身。
