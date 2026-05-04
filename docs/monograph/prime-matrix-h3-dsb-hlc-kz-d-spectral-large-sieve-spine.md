# KZ-D：spectral large sieve 的自足化证明脊柱

**状态：** `kz_d_closed_by_pretrace_lpc_ghlc_schur_chain`

本文继续只攻击 `Kuznetsov-LS atom (SC-9)` 的子原子：

```text
KZ-D: spectral large sieve with oldform/Eisenstein.
```

目标是把 KZ-D 从一句“谱大筛”拆成对偶化、预迹核、oldform 分解、Eisenstein 连续谱四个
可审查部分。本文完成前三类普通线性代数/账本归约，并把真正剩余压成单一 `PTK-D`
预迹核上界；后续 PTK/LPC/GHLC 文件已经闭合该预迹核上界，所以 KZ-D 分支现在在本文
脊柱中闭合。

## 1. KZ-D 的目标形式

本文需要的 KZ-D 是：对任意支撑在 `n<=N_0` 的系数 `\alpha_n`，

\[
\sum_{|t_j|\le T}
\left|\sum_{n\le N_0}\alpha_n\rho_j(n)\right|^2
+\int_{-T}^{T}
\left|\sum_{n\le N_0}\alpha_n\rho_t(n)\right|^2dt
\ll
(T^2+N_0)\log^{C_D}y\sum_{n\le N_0}|\alpha_n|^2.
\tag{KD-1}
\]

holomorphic 谱同型，oldform 与 level 损失必须并入 `log^{C_D}y`。

## 2. 对偶化

令 `\Omega_T` 表示截断后的 Maass、holomorphic 与 Eisenstein 谱参数集合，统一记谱系数为
`\rho_\omega(n)`，谱测度为 `d\mu(\omega)`。KZ-D 等价于算子

\[
\mathcal T:\ell^2([1,N_0])\to L^2(\Omega_T,d\mu),
\qquad
(\mathcal T\alpha)(\omega)=\sum_{n\le N_0}\alpha_n\rho_\omega(n)
\tag{KD-2}
\]

满足

\[
\|\mathcal T\|^2\ll (T^2+N_0)\log^{C_D}y.
\tag{KD-3}
\]

由 Hilbert 空间对偶性，这等价于

\[
\|\mathcal T^*\mathcal T\|_{\ell^2\to\ell^2}
\ll (T^2+N_0)\log^{C_D}y.
\tag{KD-4}
\]

其核矩阵为

\[
K_T(n,m)=\int_{\Omega_T}\rho_\omega(n)\overline{\rho_\omega(m)}\,d\mu(\omega).
\tag{KD-5}
\]

因此 KZ-D 归结为证明

\[
\sum_{m\le N_0}|K_T(n,m)|
\ll (T^2+N_0)\log^{C_D}y
\tag{KD-6}
\]

以及对列同样的上界。由 Schur test 即得 `(KD-4)`。

## 3. 预迹核原子 PTK-D

**PTK-D（pretrace kernel bound）。** 对本文 level、nebentypus、窗口和归一化，谱投影核满足

\[
K_T(n,m)
=
\delta_{n=m}\,\mathcal W_T
+\mathcal O_T(n,m),
\tag{KD-7}
\]

其中

\[
\mathcal W_T\ll T^2\log^{C_1}y,
\tag{KD-8}
\]

并且非对角核满足行和列的 Schur 上界：

\[
\sum_{m\le N_0}|\mathcal O_T(n,m)|
\ll N_0\log^{C_2}y,
\qquad
\sum_{n\le N_0}|\mathcal O_T(n,m)|
\ll N_0\log^{C_2}y.
\tag{KD-9}
\]

若 PTK-D 成立，则由 `(KD-6)`：

\[
\sum_{m\le N_0}|K_T(n,m)|
\ll (T^2+N_0)\log^{C_D}y,
\tag{KD-10}
\]

从而得到 KZ-D。

PTK-D 是 spectral large sieve 的真正内核。后续文件已把它展开为 pre-trace formula、
Selberg/Harish-Chandra 正核、局部 Weyl 对角项、空间侧 LPC-D，以及 GHLC-D 的局部
`L^1`--Schur 核质量闭合。

## 4. oldform 账本

设 level `Q` 的谱按 newform level `q|Q` 与 oldform 提升参数 `d|Q/q` 分解。oldform 归一化
矩阵在每个 `(q,d)` 层满足

\[
\sum_{\text{old lifts }r}
|\rho_{f,r}(n)|^2
\ll \tau(Q)^C\sum_{d|Q/q}|\rho_f(n/d)|^2\,1_{d|n}.
\tag{KD-11}
\]

因此 oldform 层对 `(KD-1)` 的贡献至多增加

\[
\tau(Q)^C\ll \log^{C_3}y,
\tag{KD-12}
\]

因为 clean HLC admission 的 K5/K6 已把 level 与 dyadic 分裂限制在多对数账本内。

结论：oldform 不是新的解析硬点；它只改变 `C_D`。

## 5. Eisenstein 账本

Eisenstein 系数在本文归一化下有 divisor 型包络

\[
|\rho_t(n)|\ll_\epsilon n^\epsilon \tau(n),
\tag{KD-13}
\]

并满足与 Maass 谱相同的连续谱正交/Plancherel 公式。对偶化后，连续谱核为

\[
K_T^{\rm Eis}(n,m)
=\int_{-T}^{T}\rho_t(n)\overline{\rho_t(m)}\,dt.
\tag{KD-14}
\]

其 diagonal 体积为 `O(T^2 log^{C}y)`，非对角行和列由同一个 PTK-D 型核上界控制。连续谱
积分只把离散求和换成 `dt`，不改变 `(T^2+N_0)` 的尺度。

结论：Eisenstein 也不是单独硬点；若 PTK-D 包含连续谱核，则它进入同一 Schur 上界。

## 6. holomorphic 谱

holomorphic 谱的 Petersson kernel 与 Maass 预迹核同型。权重 `k<=T` 的计数贡献

\[
\sum_{k\le T}(k-1)\ll T^2,
\tag{KD-15}
\]

非对角 Bessel kernel 比 Maass 情形更短，进入 `(KD-9)` 的同一行/列上界。因此 holomorphic
谱也只改变多对数常数。

## 7. KZ-D 证明

**命题。** 若 PTK-D 成立，则 KZ-D 成立。

**证明。**

1. 由对偶化 `(KD-2)`--`(KD-5)`，KZ-D 等价于核算子 `K_T` 的 `\ell^2` 范数上界。
2. 由 PTK-D，`K_T` 分为 diagonal 体积项和非对角项。
3. diagonal 项的行和为 `O(T^2 log^{C_1}y)`。
4. 非对角项的行和、列和由 `(KD-9)` 为 `O(N_0 log^{C_2}y)`。
5. Schur test 给出
   \[
   \|K_T\|_{\ell^2\to\ell^2}
   \ll (T^2+N_0)\log^{C_D}y.
   \]
6. oldform、Eisenstein、holomorphic 谱由第 4--6 节并入 `log^{C_D}y`。

所以 `(KD-1)` 成立。证毕。

## 8. 当前闭合度

本文完成：

1. KZ-D 的 Hilbert 空间对偶化；
2. KZ-D 到 PTK-D 的 Schur kernel 归约；
3. oldform、Eisenstein、holomorphic 谱的多对数账本定位；
4. PTK-D 推出 KZ-D 的逐行证明。

本文接入后续 PTK/LPC/GHLC 文件后还完成：

```text
PTK-D: pretrace kernel bound (KD-7)--(KD-9).
```

下一步若继续完全自足无黑箱硬攻，不再是 KZ-D；应回到 `Kuznetsov-LS atom` 中仍未内联的
`KZ-B` Kuznetsov trace formula 专门化与 `KZ-E` BFI/well-factorable dispersion 对数节省。

进一步压缩见 `docs/monograph/prime-matrix-h3-dsb-hlc-ptk-d-pretrace-kernel-bound.md`。该文
构造谱截断测试函数，写出预迹/Poincare 系数核展开，证明对角 `T^2` 体积账本，并把
`PTK-D` 的唯一剩余压成空间侧 `LPC-D` 行列和上界；同时证明 `LPC-D=>PTK-D`。随后 LPC-D
分解文件与 GHLC-D 局部 Schur 文件闭合该空间侧上界。
