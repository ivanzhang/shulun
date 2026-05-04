# KFLS-core：平方核与中心化四模数相关硬攻

**状态：** `kfls_reduced_to_block_centered_four_modulus_core_not_closed`

本文继续只攻击同一个剩余：

```text
KFLS-core: balanced Kloosterman-fraction large sieve logarithmic saving.
```

本步不回退到 Kloosterman 和符号层，也不更换命题。我们把 `(KFA-17a)`--`(KFA-17b)` 直接平方化，
暴露四模数相关核。关键结论有两点：

1. 全核的绝对 Schur 上界不能给出 `log^{-A}`，因为精确对角层只恢复 raw 二范数尺度；
2. 真正剩余不是“再做普通大筛”，而是中心化后的四模数非对角相位相关估计，记为 `CFQK-core`。

这一步关闭的是错误路线：不能用正核/绝对值 Schur 伪造任意对数节省。正确的无黑箱硬点必须
证明带符号的中心化四模数核。
后续 `prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md` 进一步指出：同一 `(u,v)` 块
内半对角不能被要求 `log^{-A}` 估小，必须作为块对角局部方差中心化扣除。当前剩余因此
细化为 `BD-CEN + OSQK-core + TFQK-core`。
再后续 `prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 已核查：当前 KZ-E spine
尚未证明 `BD-CEN`，所以第一阻断点是 `(BDC-5)`。

## 1. 非退化 KFLS 和的统一索引

把 `(KFA-17b)` 中的非退化原子记为

\[
\xi=(u,v,h,\ell,x,z),
\tag{SQK-1}
\]

其中

\[
u\sim U,\quad v\sim V,\quad (u,v)=1,\quad 0<|h|\le H,\quad
\ell\bmod uv,
\tag{SQK-2}
\]

且 `x mod u`、`z mod v` 为单位并满足

\[
R_\xi:=R_{h,\ell,u}(x)\not\equiv0\pmod u,\qquad
T_\xi:=T_{h,\ell,v}(z)\not\equiv0\pmod v.
\tag{SQK-3}
\]

定义权重与相位

\[
A_\xi
=
\alpha_u\delta_v\omega_h\,{1\over uv}\,\widehat\beta_{uv}(\ell),
\tag{SQK-4}
\]

\[
\Phi(\xi)
=
{\bar v R_\xi\over u}+{\bar u T_\xi\over v}.
\tag{SQK-5}
\]

非退化目标和为

\[
\mathcal S_{\rm nd}
=
\sum_{\xi\in\Xi_{\rm nd}}A_\xi e(\Phi(\xi)).
\tag{SQK-6}
\]

`KFLS-core` 的非退化部分要求

\[
|\mathcal S_{\rm nd}|
\ll_A
{\mathcal B(UV,S,H)\over\log^A y}.
\tag{SQK-7}
\]

退化部分 `(KFA-17a)` 同样可以用下面的平方核方法处理，只是 `R_\xi=0` 或 `T_\xi=0` 的根数
权要按 `(KFA-13)` 先并入权重账本。

## 2. 精确平方展开

平方得到恒等式

\[
|\mathcal S_{\rm nd}|^2
=
\sum_{\xi,\xi'\in\Xi_{\rm nd}}
A_\xi\overline{A_{\xi'}}
e\!\left(\Phi(\xi)-\Phi(\xi')\right).
\tag{SQK-8}
\]

写

\[
\xi'=(u',v',h',\ell',x',z'),
\tag{SQK-9}
\]

则相位差为

\[
\Delta(\xi,\xi')
=
{\bar v R_\xi\over u}
+
{\bar u T_\xi\over v}
-
{\overline{v'} R_{\xi'}\over u'}
-
{\overline{u'} T_{\xi'}\over v'}.
\tag{SQK-10}
\]

这是四模数核：

\[
(u,v,u',v').
\tag{SQK-11}
\]

因此任何自足证明都必须控制 `(SQK-10)` 的带符号相关，而不是只控制单个 Kloosterman 和。

## 3. 对角层不是节省来源

精确对角

\[
\xi=\xi'
\tag{SQK-12}
\]

贡献

\[
\mathcal D
=
\sum_{\xi\in\Xi_{\rm nd}}|A_\xi|^2.
\tag{SQK-13}
\]

由 `(BSA-7)` 与 dyadic 支持，

\[
\mathcal D
\ll
\log^{O(1)}y\,
\mathcal B(UV,S,H)^2.
\tag{SQK-14}
\]

这正是 KZ-D/raw 二范数尺度的平方。它说明：

```text
绝对值 Schur / 正核 TT* 只能恢复 raw scale，
不能推出任意 log^{-A} saving。
```

若有人试图证明

\[
\sum_{\xi'}|K(\xi,\xi')|
\ll
{\mathcal B(UV,S,H)^2\over\log^{2A}y}
\tag{SQK-15}
\]

这会直接被 `(SQK-13)` 的对角质量阻断，除非先做 dispersion 中心化并把主对角从目标核中
剥离。因此 `(SQK-15)` 不是正确路线。

## 4. 中心化核

定义对角投影

\[
\Pi_{\rm diag}(\xi,\xi')=1_{\xi=\xi'}.
\tag{SQK-16}
\]

在实际 dispersion 链条中，`h=0` 主项已经剥离，剩下的 `h\ne0` 核还必须剥离平方展开中的
自相关对角。令

\[
K^\circ(\xi,\xi')
=
A_\xi\overline{A_{\xi'}}
e(\Delta(\xi,\xi'))
-
1_{\xi=\xi'}|A_\xi|^2.
\tag{SQK-17}
\]

更宽的半对角也必须单独列账。半对角包括：

\[
(u,v)=(u',v'),\quad (h,\ell)\ne(h',\ell'),
\tag{SQK-18}
\]

以及

\[
u=u',\,v\ne v'
\quad\text{或}\quad
v=v',\,u\ne u'.
\tag{SQK-19}
\]

这些层仍保留一侧逆元相位，不能用全对角估计替代。它们进入 `CFQK-core` 的分层核。

## 5. 四模数中心化核心：CFQK-core

**CFQK-core（centered four-modulus Kloosterman-fraction correlation core）。** 在 `(SQK-1)`--`(SQK-5)`
的同一 clean HLC 支持上，平方核满足：

1. **对角账本。**
   \[
   \mathcal D
   \le
   \mathcal D_{\rm raw}
   \ll
   \log^{O(1)}y\,\mathcal B(UV,S,H)^2,
   \tag{SQK-20}
   \]
   且该 raw 对角已在 dispersion 主项/方差归一化中被扣除或转入自然二范数尺度。
2. **半对角账本。** `(SQK-18)`--`(SQK-19)` 的全部贡献满足
   \[
   |\mathcal K_{\rm semi}|
   \ll_A
   {\mathcal B(UV,S,H)^2\over\log^{2A}y}.
   \tag{SQK-21}
   \]
3. **真非对角中心化核。**
   对
   \[
   (u,v)\ne(u',v'),\qquad u\ne u',\qquad v\ne v'
   \tag{SQK-22}
   \]
   的层，有
   \[
   \left|
   \sum_{\xi,\xi'\ {\rm satisfying}\ (SQK-22)}
   K^\circ(\xi,\xi')
   \right|
   \ll_A
   {\mathcal B(UV,S,H)^2\over\log^{2A}y}.
   \tag{SQK-23}
   \]

该核心是比 `KFLS-core` 更低层的同一命题内部形式。它不再允许把对角质量误当作可消失的误差；
它要求真正证明中心化后的四模数相位相关抵消。

## 6. `CFQK-core => KFLS-core`

**命题。** 若 CFQK-core 成立，则 KFLS-core 成立。

**证明。**

1. 对非退化和 `(SQK-6)` 作精确平方展开 `(SQK-8)`。
2. 对角层由 `(SQK-20)` 识别为 raw 二范数尺度；在 dispersion 方差恒等式中，该层不是目标
   对数节省的来源，而是被主项/自然范数账本扣除。若写成独立估计，必须保持中心化形式
   `(SQK-17)`。
3. 半对角由 `(SQK-21)` 控制。
4. 真非对角由 `(SQK-23)` 控制。
5. 合并后得到
   \[
   |\mathcal S_{\rm nd}|^2
   \ll_A
   {\mathcal B(UV,S,H)^2\over\log^{2A}y},
   \tag{SQK-24}
   \]
   取平方根即得 `(SQK-7)`。
6. 退化层按同样平方核分层，并使用 `(KFA-13)` 的根数包络进入权重账本，得到 `(KFA-17a)`。

因此 KFLS-core 成立。证毕。

## 7. 当前审稿边界

本步完成了：

```text
BCFQK-core => KFLS-core => BSC-core => BWFD-core => WFD-core => KZ-E.
```

本文本身把 `KFLS-core` 平方化为 `CFQK-core`；后续块中心化文件进一步修正并证明
`BCFQK-core=>KFLS-core`。当前真正剩余已经不是“怎么展开 Kloosterman 和”，也不是“能不能用
普通谱大筛”，而是：

```text
BD-CEN + OSQK-core + TFQK-core.
```

下一步若继续硬攻，必须先证明 `BD-CEN` 块中心化身份 `(BDC-5)`；随后才可处理三模数的
`OSQK-core` 和真四模数的 `TFQK-core`。若不能证明这些中心化核，完全自足无黑箱闭合仍不能
宣称完成。
