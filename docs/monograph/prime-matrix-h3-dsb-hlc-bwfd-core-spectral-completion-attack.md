# BWFD-core：谱完成攻击与双线性相关核心

**状态：** `bwfd_reduced_to_kloosterman_fraction_large_sieve_core_not_closed`

本文继续只攻击同一个剩余：

```text
BWFD-core: balanced two-modulus well-factorable Kloosterman dispersion mean estimate.
```

本步不再重复筛权分解、gcd 剥离或 CRT 归一化。那些内容已经在
`prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md` 中完成。这里直接处理
`(WB-11)` 的解析内核：先对 `s` 变量作精确有限 Fourier 完成，再把模数 `uv` 的 Kloosterman
和乘法分裂。结论是：普通 KZ-D 谱大筛只能恢复 raw 二范数尺度；任意 `log^{-A}` 节省必须
来自一个更窄的 balanced spectral bilinear correlation 核，记为 `BSC-core`。后续
`prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md` 已把 `BSC-core` 逐项展开为
互逆 Kloosterman 分数相位，并进一步压缩为 `KFLS-core`；再后续
`prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md` 把 `KFLS-core` 平方化为
`CFQK-core`；`prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md` 又把同块半对角修正为
块中心化账本；`prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 已进一步核查：
当前 KZ-E spine 尚未证明 `BD-CEN`。

## 1. 起点

互素平衡层为

\[
\mathcal W_{U,V}
=
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
\sum_{\substack{s\sim S\\(s,uv)=1}}
\beta_s
e_{uv}(a_hs+b_h\bar s),
\tag{BSA-1}
\]

其中

\[
U,V=C^{1/2}\log^{O(1)}y,\qquad UV\asymp C.
\tag{BSA-2}
\]

目标仍是

\[
|\mathcal W_{U,V}|
\ll_A
\frac{\mathcal B(UV,S,H)}{\log^A y}.
\tag{BSA-3}
\]

## 2. `s` 变量的精确完成

令 `W` 为支撑在 `[1/2,3]`、等于 `1` 于目标 dyadic 区间上的平滑截断，并把 `\beta_s` 外延为
零。对任意 `c=uv` 定义有限 Fourier 系数

\[
\widehat\beta_c(\ell)
=
\sum_{n\in\mathbb Z}\beta_n W(n/S)e_c(-\ell n),
\qquad \ell\bmod c.
\tag{BSA-4}
\]

有限群 `\mathbb Z/c\mathbb Z` 上的 Fourier 反演给出恒等式

\[
\sum_{\substack{s\in\mathbb Z\\(s,c)=1}}
\beta_s W(s/S)e_c(a_hs+b_h\bar s)
=
\frac1c\sum_{\ell\bmod c}
\widehat\beta_c(\ell)S(a_h+\ell,b_h;c),
\tag{BSA-5}
\]

其中

\[
S(A,B;c)=\sum_{x\bmod c}^{*}e_c(Ax+B\bar x).
\tag{BSA-6}
\]

这是精确恒等式，不是估计。Parseval 与每个剩余类中至多 `1+S/c` 个 `s` 给出账本

\[
\sum_{\ell\bmod c}|\widehat\beta_c(\ell)|^2
=c\sum_{r\bmod c}\left|\sum_{n\equiv r(c)}\beta_nW(n/S)\right|^2
\ll c(1+S/c)\sum_n|\beta_n|^2W(n/S)^2.
\tag{BSA-7}
\]

因此完成步骤没有损失主尺度；它只把不完整逆元相位变成完整 Kloosterman 和。

## 3. 平衡双模数的完整 Kloosterman 形

当 `(u,v)=1` 时，Kloosterman 和满足乘法公式

\[
S(A,B;uv)
=
S(A\bar v,B\bar v;u)\,
S(A\bar u,B\bar u;v).
\tag{BSA-8}
\]

把 `(BSA-5)` 与 `(BSA-8)` 代入 `(BSA-1)`，得到等价的完整双模数形式

\[
\mathcal W_{U,V}
=
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
\frac1{uv}\sum_{\ell\bmod uv}\widehat\beta_{uv}(\ell)
S((a_h+\ell)\bar v,b_h\bar v;u)
S((a_h+\ell)\bar u,b_h\bar u;v).
\tag{BSA-9}
\]

这一步是真正的“硬核显形”：两个平方根模数都进入完整 Kloosterman 和，但二者仍通过
`\bar u mod v` 与 `\bar v mod u` 交叉耦合。

## 4. 普通 KZ-D 为什么不够

若只把 `(BSA-5)` 送入 KZ-B/KZ-D，再对模数权作 Cauchy，则得到的是 raw 谱大筛尺度

\[
|\mathcal W_{U,V}|
\ll
\mathcal B(UV,S,H)\log^{O(1)}y.
\tag{BSA-10}
\]

这个推导没有使用 `\lambda_c=\sum_{uv=c}\alpha_u\delta_v` 的平衡结构；它只是把每个模数
`c` 当作独立对象处理。因此 `(BSA-10)` 不能推出 `(BSA-3)` 的任意 `log^{-A}` 节省。

点态 Weil 也不够。由

\[
|S(A,B;u)S(A',B';v)|
\ll \tau(uv)(uv)^{1/2}(A,B,u)^{1/2}(A',B',v)^{1/2}
\tag{BSA-11}
\]

逐项求和至多给平方根级单点抵消，不能压出 well-factorable dispersion 所需的任意对数节省。
所以剩余硬点不是 trace formula 正规化，也不是谱大筛本身，而是平衡 `u,v` 族中的双线性相关
抵消。

## 5. 平衡屏障

把 `v` 按模 `u` 的剩余类分组时，由 `V\asymp U`，每个剩余类平均只含 `O(1)` 个 `v`。
所以不能在固定 `u` 后依靠一个长的 `v mod u` 平均获得大筛节省。同理，固定 `v` 后也没有
长的 `u mod v` 平均。

这解释了为什么 `(BSA-9)` 是真正的 balanced Type-II 障碍：节省必须来自两个模数同时运动时
交叉逆元相位

\[
(\bar v\bmod u,\ \bar u\bmod v)
\tag{BSA-12}
\]

的二阶相关消散，而不是来自任一单变量的大筛平均。

## 6. 最小新核心：BSC-core

**BSC-core（balanced spectral bilinear correlation core）。** 对 `(BSA-2)` 的平衡块，令
`\widehat\beta_{uv}` 必须来自同一个全局 `\beta_sW(s/S)` 的有限 Fourier 完成 `(BSA-4)`，
并满足 Parseval 账本 `(BSA-7)`。则完整双模数和 `(BSA-9)` 满足

\[
\left|
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
\frac1{uv}\sum_{\ell\bmod uv}\widehat\beta_{uv}(\ell)
S((a_h+\ell)\bar v,b_h\bar v;u)
S((a_h+\ell)\bar u,b_h\bar u;v)
\right|
\ll_A
\frac{\mathcal B(UV,S,H)}{\log^A y}.
\tag{BSA-13}
\]

这是比 `BWFD-core` 更显式的同一硬点：不再有不完整 `s` 逆元和，不再有 gcd 层，也不再有
CRT 归一化义务；唯一剩余是完整 Kloosterman 双线性相关估计。

## 7. `BSC-core => BWFD-core`

**命题。** 若 BSC-core 成立，则 BWFD-core 成立。

**证明。**

1. 对 `(WB-11)` 的每个互素平衡块取平滑 dyadic 截断 `W(s/S)`；端点误差已在 K3/KZ-E 的
   endpoint 账本中吸收。
2. 用有限 Fourier 反演得到 `(BSA-5)`。该步骤精确，Parseval 账本为 `(BSA-7)`。
3. 对 `c=uv` 使用 Kloosterman 乘法公式 `(BSA-8)`，把每个完整和化为 `(BSA-9)`。
4. 对 `(BSA-9)` 调用 BSC-core，指数取 `A+C_{\rm end}+C_{\rm dyad}+10`，吸收端点和平滑分块的
   多对数损失。

得到 `(BSA-3)`，即 BWFD-core。证毕。

## 8. 当前审稿边界

本步完成了：

```text
BSC-core => BWFD-core => WFD-core => KZ-E.
```

并且证明了普通 KZ-D 与点态 Weil 不足以自动产生 `(BSA-3)` 的 `log^{-A}` 节省。完全自足
无黑箱闭合的唯一剩余现在进一步定位为：

```text
BD-CEN identity (BDC-5), then OSQK-core + TFQK-core.
```

若允许引用 Deshouillers--Iwaniec/Bombieri--Friedlander--Iwaniec 型 well-factorable dispersion
定理，该核心可作为外部深定理适配点；若要求文内完全自足，则必须继续证明后续文件中的
`(BDC-5)`；然后才是 `(BCF-14)`--`(BCF-16)`。在这些核未证明前，不能宣称 H3-HLC、SC-9
或 CORE-5 已完全无黑箱闭合。
