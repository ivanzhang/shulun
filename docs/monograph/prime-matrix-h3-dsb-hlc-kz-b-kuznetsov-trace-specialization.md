# KZ-B：Kuznetsov trace formula 专门化的内联推导

**状态：** `kz_b_closed_by_poincare_unfolding_and_spectral_plancherel`

本文继续只攻击同一个剩余：

```text
KZ-B: Kuznetsov trace formula specialization.
```

目标不是证明新的估计，而是把本文 clean HLC 中出现的 Kloosterman 模数和精确转成谱侧。
因此本步应闭合的是“公式正确性与归一化”，不是 `log^{-A}` 节省；后者仍属于 `KZ-E`。

## 1. 专门化目标

固定 clean dyadic block，令 `Q` 为 K1--K6 准入后的 level，且所有 cusp 数、宽度、nebentypus、
unit 和 gcd 层损失都已在 K5/K6 账本中限制为 `\log^{O(1)}y`。对 `ab\ne0` 与光滑权 `\Phi`
定义

\[
\mathcal K_{a,b}(\Phi)
=
\sum_{\substack{c\ge1\\c\equiv0\pmod Q}}
\frac{S_\chi(a,b;c)}{c}\,
\Phi\!\left(\frac{4\pi\sqrt{|ab|}}{c}\right),
\tag{KB-1}
\]

其中

\[
S_\chi(a,b;c)=
\sum_{\substack{x\bmod c\\(x,c)=1}}
\chi(x)e_c(ax+b\bar x).
\tag{KB-2}
\]

`KZ-B` 要证明 `(KB-1)` 等于同一 level、同一 cusp 归一化下的谱侧：

\[
\mathcal K_{a,b}(\Phi)
=
\mathcal M^{\rm Maa}_{a,b}(\widetilde\Phi)
+\mathcal M^{\rm hol}_{a,b}(\widetilde\Phi)
+\mathcal M^{\rm Eis}_{a,b}(\widetilde\Phi)
+\mathcal D_{a,b}(\Phi),
\tag{KB-3}
\]

其中 `\widetilde\Phi` 是第 5 节给出的 Bessel 变换。`ab=0` 不进入本命题；它已由 K3 的
endpoint/low-frequency 出口剥离。

## 2. 自动核与 Poincare 展开

取径向平滑核 `k_\Phi(u)`，其 Selberg/Harish-Chandra--Bessel 变换为 `\widetilde\Phi`，并使
其 Kloosterman 侧 Bessel 权正是 `\Phi(4\pi\sqrt{|ab|}/c)`。先假设 `k_\Phi` 光滑紧支撑；
一般 Schwartz 衰减权由紧支撑逼近与 KZ-C 的快速衰减通过极限得到。

定义 automorphic kernel

\[
K_\Phi(z,w)
=
\sum_{\gamma\in\Gamma_0(Q)}
\overline{\chi(\gamma)}\,k_\Phi(u(z,\gamma w)).
\tag{KB-4}
\]

紧支撑时 `(KB-4)` 绝对一致收敛；Schwartz 情形由 `(1+d(z,\gamma w))^{-A}` 与基本域体积增长
给出一致可积主控。因此后续换序均由 dominated convergence 支撑。

对第 `a,b` 个 Fourier--Poincare 线性泛函记

\[
\mathcal I_{a,b}(\Phi)
=
\langle P_a,\,K_\Phi P_b\rangle_{X_Q},
\tag{KB-5}
\]

其中 `P_a,P_b` 是在对应 cusp 上由 `e(ax)` 与固定光滑 `y`-包生成的 Poincare 包。K5/K6
保证更换 cusp 或 oldform lift 只改变 `\log^{O(1)}y` 的归一化因子。

## 3. 几何侧展开

将 `(KB-4)` 代入 `(KB-5)`，按双陪集

\[
\Gamma_\infty\backslash\Gamma_0(Q)/\Gamma_\infty
\tag{KB-6}
\]

分解。`c=0` 的双陪集给 diagonal/exceptional 项 `\mathcal D_{a,b}(\Phi)`。对 `c>0`，
代表元可写为

\[
\gamma=\begin{pmatrix} *&*\\ c&d\end{pmatrix},\qquad (c,d)=1,\qquad c\equiv0\pmod Q.
\tag{KB-7}
\]

对 `x` 与 `x'` 两个 horocycle 变量展开 Fourier 因子。固定 `c` 后，`d\bmod c` 的可逆剩余
类给出

\[
\sum_{d\bmod c}^{*}\chi(d)e_c(ad+b\bar d)
=S_\chi(a,b;c).
\tag{KB-8}
\]

剩余的 `y,y'` 积分只依赖

\[
\frac{4\pi\sqrt{|ab|}}{c}
\tag{KB-9}
\]

并按 `k_\Phi` 的定义等于 `\Phi(4\pi\sqrt{|ab|}/c)`。因此几何侧为

\[
\mathcal I_{a,b}(\Phi)
=
\mathcal D_{a,b}(\Phi)
+
\sum_{\substack{c\ge1\\c\equiv0\pmod Q}}
\frac{S_\chi(a,b;c)}{c}
\Phi\!\left(\frac{4\pi\sqrt{|ab|}}{c}\right).
\tag{KB-10}
\]

这一步只使用双陪集分解、CRT 可逆类求和和一维 Bessel 积分定义；没有使用任何估计性黑箱。

## 4. 谱侧展开

同一个核 `(KB-4)` 也是 Laplacian 的平滑函数演算。对 `L^2(X_Q,\chi)` 的 Maass cusp 谱、
Eisenstein 连续谱和 holomorphic 离散谱作 Plancherel 分解：

\[
K_\Phi(z,w)
=
\sum_j\widetilde\Phi(t_j)u_j(z)\overline{u_j(w)}
+
\sum_{\mathfrak a}\frac1{4\pi}\int_{-\infty}^{\infty}
\widetilde\Phi(t)E_{\mathfrak a}(z,1/2+it)
\overline{E_{\mathfrak a}(w,1/2+it)}\,dt
+
K_\Phi^{\rm hol}(z,w).
\tag{KB-11}
\]

`K_\Phi^{\rm hol}` 是正号 Bessel 通道中的 holomorphic 权重谱；当符号组合不产生该通道时该项
为空。Exceptional small eigenvalues 是 Maass 谱的一部分；本文把它们并入
`\mathcal D_{a,b}` 或多对数账本，不单独构成新输入。

将 `(KB-11)` 代入 `(KB-5)` 并展开 Fourier 系数：

\[
u_j(z)=\sum_{n\ne0}\rho_j(n)W_{n,t_j}(z),\qquad
E_{\mathfrak a}(z,1/2+it)=\sum_{n\ne0}\rho_{\mathfrak a,t}(n)W_{n,t}(z)+\cdots .
\tag{KB-12}
\]

Poincare 包的 unfolding 给

\[
\langle P_a,u_j\rangle
=\rho_j(a)\,\mathcal B_a(t_j),
\qquad
\langle P_b,u_j\rangle
=\rho_j(b)\,\mathcal B_b(t_j),
\tag{KB-13}
\]

并且 `\mathcal B_a(t)\overline{\mathcal B_b(t)}` 正是第 5 节的 Bessel 变换权
`\widetilde\Phi(t)`。Eisenstein 与 holomorphic 谱同理。因此

\[
\mathcal I_{a,b}(\Phi)
=
\mathcal M^{\rm Maa}_{a,b}(\widetilde\Phi)
+\mathcal M^{\rm hol}_{a,b}(\widetilde\Phi)
+\mathcal M^{\rm Eis}_{a,b}(\widetilde\Phi).
\tag{KB-14}
\]

## 5. Bessel 变换归一化

符号 `ab>0` 与 `ab<0` 对应 Kuznetsov 的两条 Bessel 通道。本文只需要如下统一记法：

\[
\widetilde\Phi(t)=
\int_0^\infty \Phi(x)\mathcal J_t^\pm(x)\frac{dx}{x},
\tag{KB-15}
\]

其中 `\mathcal J_t^+` 是同号通道的 `J_{2it}`/holomorphic Bessel 组合，
`\mathcal J_t^-` 是异号通道的 `K_{2it}` 组合。具体常数由 `(KB-9)` 的一维积分固定；若采用
不同 Fourier 系数规范化，变化只是在 `\rho(n)` 与 `\widetilde\Phi` 之间移动一个显式因子。

KZ-C 已证明：对本文 clean 平滑权，`\widetilde\Phi(t)` 快速衰减，且谱截断尾为
`O_A(y^{-A})`。因此 `(KB-11)`--`(KB-14)` 的谱积分绝对可截断到本文所需窗口。

## 6. KZ-B 结论

比较几何侧 `(KB-10)` 与谱侧 `(KB-14)`，得到 `(KB-3)`，即 KZ-B。

所有可能的边界项已定位如下：

1. `ab=0`：回到 K3 endpoint/low-frequency 出口；
2. `c=0` 双陪集：进入 diagonal/exceptional 项 `\mathcal D_{a,b}`；
3. 多 cusp、oldform lift、nebentypus、unit/gcd 层：进入 K5/K6 的 `\log^{O(1)}y` 账本；
4. Bessel transform 尾：由 KZ-C 处理；
5. 谱侧二范数估计：由已闭合的 KZ-D 处理。

因此，`KZ-B` 在本文窗口族上已不再是未闭合黑箱。它只提供等式转换；完全自足总链的唯一
剩余深原子更新为：

```text
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```
