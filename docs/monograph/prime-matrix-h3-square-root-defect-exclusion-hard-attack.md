# H3 Square-root Defect Exclusion 硬攻稿

**状态：** `dy_branch_reduced_by_linear_sieve_tail_energy_barrier_exposed_not_closed`

本文不转换命题，只直接攻击当前唯一闭合目标：

```text
Square-root Defect Exclusion:
D_y <= eta*q/log q
and
F_y(d) <= d*lambda*q/log q.
```

结论分两层：

1. `D_y` 粗筛计数缺陷可在小筛层 `y=q^theta` 用一维区间筛基本引理压住；
2. `F_y` 尾标签 Fourier 能量在自然模数选择下与尾标签总数 `T_y` 只差常数因子，因此不能靠普通
   Fourier 均匀性免费排斥。这里就是当前真正硬核。

## 1. 小筛层的 `D_y` 可控

令 `X=#A_s`。对任意平方自由 `d`，若 `(d,6)=1`，则完整 3 行六轮候选满足

\[
\#\{n\in A_s:d\mid n\}={X\over d}+O(1).
\tag{H3-DIST}
\]

这是纯周期事实：`A_s` 在模 `d` 上按比例 `1/d` 命中 `d|n`，端点只贡献 `O(1)`。

取

\[
y=q^\theta,\qquad 0<\theta<1,
\]

并取筛水平

\[
D=q^{1-\varepsilon}.
\]

设

\[
u={\log D\over\log y}={1-\varepsilon\over\theta}.
\]

由一维 Rosser--Iwaniec/Brun 线性筛基本引理，结合 `(H3-DIST)` 的余项和 `D=o(q/log q)`，得到

\[
R_y
=
X\prod_{5\le r\le y}\left(1-{1\over r}\right)
\left(1+O(e^{-u})\right)
 +O(D).
\tag{H3-LS}
\]

也就是

\[
D_y=V_y-R_y
\ll e^{-u}V_y+D.
\tag{H3-DY}
\]

因此固定任意 `eta>0`，只要先取 `theta` 足够小使 `e^{-(1-\varepsilon)/theta}/theta` 足够小，再取
`q` 足够大，就有

\[
|D_y|\le \eta {q\over\log q}.
\tag{H3-DY-OK}
\]

这说明第一出口不是最终障碍：在小筛层，`D_y` 可以由标准区间筛控制。

## 2. 选择无尾标签碰撞的低模 `d`

令

\[
U_y=\left\lfloor {q\over \ell_+(y)}\right\rfloor+1.
\]

取 `d` 为满足

\[
2U_y\le d<4U_y
\tag{H3-DMOD}
\]

的 `2` 的幂。因为所有尾标签 `ell>y>=5` 为奇素数，所以 `(ell,d)=1`。

固定 `ell>y`。若 `n_1=ell m_1`、`n_2=ell m_2` 均在同一长度 `q` 行窗口内，且

\[
n_1\equiv n_2\pmod d,
\]

则 `d|(m_1-m_2)`。但

\[
|m_1-m_2|< {q\over \ell}< {q\over y}\le U_y<d.
\]

所以 `m_1=m_2`，即同一 `ell` 的尾标签点在模 `d` 下无碰撞。

因此每个残基计数 `mu_ell(b;d)` 只能是 `0` 或 `1`。

## 3. 尾能量等价于尾标签总数

记

\[
T_y=\#\{n\in A_s:y<P^-(n)\le p\}
=\sum_{\ell>y}N_\ell.
\]

由无碰撞性，

\[
\sum_{b\bmod d}\mu_\ell(b;d)^2=N_\ell.
\]

于是

\[
E_y(d)
=
\sum_{\ell>y}\left(N_\ell-{N_\ell^2\over d}\right).
\tag{H3-TE-ID}
\]

又因 `N_ell<=U_y<=d/2`，

\[
{1\over2}T_y
\le
E_y(d)
\le
T_y.
\tag{H3-TE-T}
\]

通过 Parseval，

\[
F_y(d)=dE_y(d),
\]

所以尾 Fourier 缺陷与尾标签总量只差常数因子。

## 4. 参数闭合张力

统一缺陷判据要求同时有

\[
D_y\le V_y-B-2L,
\qquad
E_y(d)\le L.
\tag{H3-UDC}
\]

若 `D_y` 已由第 1 节压小，则 `R_y=V_y+O(eta q/log q)`。若假设反例 `M<B`，则

\[
T_y=R_y-M\approx V_y-M.
\]

而第 3 节给出

\[
E_y(d)\ge {1\over2}T_y.
\]

因此若要让 `E_y(d)<=L`，至少需要

\[
L\gtrsim {V_y-B\over2}.
\tag{H3-L-LOW}
\]

但统一判据的第一条件需要可用余量

\[
V_y-B-2L>0.
\tag{H3-MARGIN}
\]

将 `(H3-L-LOW)` 代入 `(H3-MARGIN)`，只剩零级余量。也就是说：

```text
仅靠 D_y 小 + 尾标签普通 Fourier 均匀性，
无法推出正的 B。
```

这不是计算失败，而是结构性张力。尾能量出口若只等价于尾标签总数，就会与统一判据的 `2L` 门槛
相互抵消。

## 5. 真正剩余硬核

要完成 H3 逐行正余量，必须证明比 `(H3-TE-T)` 更强的结构性事实。等价地，至少要证明以下二者之一：

1. **尾标签总数削减：**

\[
T_y\le V_y-B-\delta {q\over\log q};
\]

这已经接近直接证明 `M>=B`。

2. **尾标签不可全补洞的结构排斥：**

即使 `T_y` 数量足够，尾标签点也不能在同一 `q` 行窗口内覆盖所有 H3 缺口；否则必须触发比
`F_y` 更强的 ColumnCRT、端点相位或双粗互补因子结构矛盾。

这表明最后硬核不在 `D_y`，而在尾标签/双粗补洞的几何结构：尾标签数量本身可以达到自然尺度，
必须利用方阵斜线、互补商互质、端点镜像、ColumnCRT 位移等额外刚性排斥其“刚好补满一整行”。

## 6. 当前严格结论

本次硬攻实际完成：

```text
D_y branch: reducible by standard one-dimensional interval sieve.
F_y branch: reduced to tail-count / double-rough filling barrier.
```

因此下一步不能再写“证明 D_y/F_y 皆小”这种过粗目标；必须直接证明：

```text
Tail labels with y<P^-(n)<=p cannot form an exact full-row filler
without producing ColumnCRT/endpoint/semiprime-cofactor contradiction.
```

这是同一个 `Square-root Defect Exclusion` 目标的内部硬核，不是转换命题。

进一步内部硬攻见：

```text
docs/monograph/prime-matrix-h3-tail-filler-rigidity-hardcore.md
```

该文件证明相邻与二步 H3 候选若均由尾标签补洞，则其大因子族完全互斥；同一尾标签复用间距至少
为 `y/4`；三连补洞等价于互素 `y`-rough 合数的 `2/4/6` 短差值方程。剩余硬核是把这些局部刚性
全局化为 ColumnCRT、端点相位或互补商容量矛盾。
