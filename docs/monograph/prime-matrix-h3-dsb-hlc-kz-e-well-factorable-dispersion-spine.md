# KZ-E：well-factorable dispersion 对数节省的无黑箱攻坚脊柱

**状态：** `kz_e_reduced_to_balanced_wfd_core_not_yet_self_contained_closed`

本文继续只攻击同一个剩余：

```text
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

本步不换命题。目标是把 KZ-E 中可内联的筛权分解、dispersion 恒等式、gcd 层、端点平滑和
损失吸收全部写成逐行义务，并诚实定位唯一仍未内联的深核。结论是：KZ-E 已被压缩为一个
窗口化 well-factorable dispersion 核 `WFD-core`；在该核未证明前，不能宣称完全自足闭合。

## 1. KZ-E 目标

上游 KZ-A--KZ-D 已给出 raw 谱平均界

\[
|\mathcal Q|
\ll
\left(\sum_{R,u}|\eta_{R,u}|^2\right)^{1/2}
\mathfrak W_{\rm raw}(\mathcal D)\log^{C_4}y.
\tag{KE-1}
\]

KZ-E 需要证明：对任意 `A>0`，可选择分解参数 `B(A)`，使

\[
\mathfrak W_{\rm raw}(\mathcal D)
\le
\frac{\mathfrak W(\mathcal D)}{\log^{A+C_4+10}y}.
\tag{KE-2}
\]

这样 `(KE-1)` 立即给出 `(KZ-2)`。因此 KZ-E 的本质不是再证明 trace formula 或谱大筛；
它只负责把 clean HLC 的 well-factorable/Type-I/II 结构转化成任意对数节省。

## 2. 可内联部分 A：well-factorable 分解

Clean HLC 中进入模数方向的筛权记为 `\lambda_R`，支撑在 `R\le R_{\max}`。`KZ-E` 只使用
以下 well-factorable 性质：

对任意分解

\[
R_{\max}=R_1R_2\cdots R_J
\tag{KE-3}
\]

存在系数 `\lambda^{(j)}_{r_j}`，满足 `|\lambda^{(j)}_{r_j}|\le\tau(r_j)^{C}`、
`r_j\le R_j`，并且

\[
\lambda_R
=
\sum_{R=r_1\cdots r_J}
\lambda^{(1)}_{r_1}\cdots\lambda^{(J)}_{r_J}.
\tag{KE-4}
\]

Rosser--Iwaniec/Buchstab 型线性筛权具有该性质；在本文内部使用时，它应作为筛权构造的
代数定义，而不是作为解析黑箱。`(KE-4)` 的证明只需从递归构造筛权的卷积定义展开；每层
除数损失为 `\log^{O(1)}y`。

## 3. 可内联部分 B：dispersion 恒等式

把 clean block 的模数权按 `(KE-4)` 分解，并把 von Mangoldt 权用 Vaughan/Heath-Brown
分解为 Type-I/II 块。对每个块，Cauchy--Schwarz 后的方差项形如

\[
\mathcal E
=
\sum_{r_1,r_2}
\lambda_{r_1}\overline{\lambda_{r_2}}
\sum_{s_1,s_2}
\beta_{s_1}\overline{\beta_{s_2}}
\sum_{0<|h|\le H}
\omega_h\,
\mathcal C(h;s_1,s_2;r_1,r_2).
\tag{KE-5}
\]

CRT 展开同余交叉后，互素主层 `(r_1,r_2)=1` 的相位为

\[
\mathcal C_{\rm main}
=
e\!\left(
-h\,\rho_1(s_1)\frac{\overline{s_1}\,\overline{r_2}}{r_1}
-h\,\rho_2(s_2)\frac{\overline{s_2}\,\overline{r_1}}{r_2}
\right),
\tag{KE-6}
\]

其中 `rho_i` 是 clean block 固定的单位相位。CRT 合并变量

\[
s\equiv s_1\pmod{r_1},\qquad s\equiv s_2\pmod{r_2}
\tag{KE-7}
\]

把 `(KE-6)` 化为模 `r_1r_2` 的标准 Kloosterman 逆元相位

\[
e_{r_1r_2}(a(h)s+b(h)\bar s).
\tag{KE-8}
\]

这一步完全代数化：它只用 CRT、可逆类唯一性和 Fourier 展开。非主频 `h=0` 已与主项抵消；
`h\ne0` 是唯一需要谱平均抵消的部分。

## 4. 可内联部分 C：gcd、端点和平滑

若 `g=(r_1,r_2)>1`，两个交叉同余在公共因子上强迫

\[
s_1\equiv s_2\pmod g.
\tag{KE-9}
\]

不相容层贡献为零；相容层带来密度因子 `1/g` 和除数损失。因此

\[
\sum_g \frac{\tau(g)^C}{g}\ll \log^{C'}y.
\tag{KE-10}
\]

端点 sawtooth 展开截断到 `|h|\le H`，尾部由

\[
\sum_{|h|>H}\frac1{|h|}\ll H^{-1}\log^{C}y
\tag{KE-11}
\]

和 K3 平滑窗口导数账本吸收。dyadic 分块、Type 分解、unit 层和 oldform/cusp 层都只贡献
`\log^{O(1)}y`。这些都是普通账本，不是 KZ-E 的真正深核。

## 5. 唯一剩余核：WFD-core

经第 2--4 节，KZ-E 的唯一非账本部分变为：

**WFD-core（windowed well-factorable dispersion core）。** 对任意 `A>0`，令
`C,S,H` 位于 clean HLC 准入范围

\[
C\asymp R_0,\qquad S\asymp L_0\ \text{或 completion 频率长度},\qquad
0<|h|\le H_0,
\tag{KE-12}
\]

且 `\lambda_c` well-factorable、`\beta_s` divisor-bounded、`\omega_h` 平滑并满足
`\ell^1` 多对数账本。则互素主层 Kloosterman 窗口满足

\[
\left|
\sum_{c\sim C}\lambda_c
\sum_{0<|h|\le H}\omega_h
\sum_{\substack{s\sim S\\(s,c)=1}}
\beta_s e_c(a_hs+b_h\bar s)
\right|
\ll_A
\frac{\mathcal B(C,S,H)}{\log^A y},
\tag{KE-13}
\]

其中 `\mathcal B(C,S,H)` 是 KZ-D 谱大筛给出的自然二范数尺度。等价地，二次型版本给
`(KE-2)`。

这就是 BFI/DI 方法在本文窗口上的精确内核。点态 Weil 只给单模平方根抵消；普通大筛在
平衡 Type-II 块差一个主尺度；因此 `(KE-13)` 不是前文 KZ-B--KZ-D 的形式推论。

## 6. `WFD-core => KZ-E`

**命题。** 若 WFD-core 成立，则 KZ-E 成立。

**证明。**

1. 用 `(KE-4)` 展开 well-factorable 模权。层数 `J=J(A)` 固定，卷积层只造成
   `\log^{C_1J}y` 损失。
2. 对 `\Lambda` 作 Type-I/II 分解。分块数为 `\log^{C_2}y`。
3. 对每个 Type 块应用 dispersion 恒等式 `(KE-5)`，主项与 `h=0` 抵消，非零频进入
   `(KE-8)`。
4. gcd 层由 `(KE-9)`--`(KE-10)` 吸收，端点由 `(KE-11)` 吸收。
5. 对互素主层调用 WFD-core，取指数
   \[
   A_* = A+C_1J+C_2+C_3+C_4+20.
   \tag{KE-14}
   \]
6. 汇总所有层，得到 `(KE-2)`。

证毕。

## 7. 当前审稿边界

本文完成了 KZ-E 的所有非深账本：

1. well-factorable 卷积分解接口；
2. dispersion 方差恒等式；
3. CRT 到标准 Kloosterman 相位的归一化；
4. gcd 相容层与端点平滑账本；
5. `WFD-core=>KZ-E`。

但本文尚未证明 `(KE-13)`。因此当前不能诚实宣称：

```text
KZ-E closed;
SC-9 closed;
CORE-5 closed;
HLC completely self-contained closed.
```

当前剩余已经由后续五步继续压缩为：

```text
BD-CEN + OSQK-core + TFQK-core.
```

后续 `docs/monograph/prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md` 已把
`WFD-core` 用平方根 well-factorable 分解、gcd 剥离和 CRT 因子化压缩为 `BWFD-core`；
`docs/monograph/prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md` 又把
`BWFD-core` 通过 `s` 变量精确完成和完整 Kloosterman 乘法公式压缩为 `BSC-core`；
`docs/monograph/prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md` 再把
`BSC-core` 展开为互逆分数相位并压缩为 `KFLS-core`；
`docs/monograph/prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md` 最后把 `KFLS-core`
平方化为中心化四模数相关核 `CFQK-core`；
`docs/monograph/prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md` 进一步指出同块
半对角必须中心化扣除，并把当前剩余修正为 `BD-CEN + OSQK-core + TFQK-core`。因此下一步
若继续不换命题硬攻，必须先证明 `BD-CEN` 身份 `(BDC-5)`；当前
`docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 已核查现有 KZ-E
spine 只给出 `h=0` 主项抵消，尚未给出同 `(u,v)` 块方差扣除。`OSQK/TFQK` 只能在
`BD-CEN` 成立后继续推进。
