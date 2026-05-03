# Signed-LowMod-Bridge 最终硬点严写

**状态：** `signed_lowmod_bridge_reduced_to_endpoint_sawtooth_exclusion`

本文专攻递推链最后硬点：

```text
large signed low-mod endpoint defect
=> directed CRTDefect/Tail-anchor/OSPC.
```

目标是把它从口号拆成可审稿的恒等式、动力系统和最后仍需证明的排斥不等式。

## 1. 有符号低模端点缺陷

对整数区间

\[
I=[L,R]\cap\mathbb Z,\qquad N=|I|=R-L+1,
\]

以及素数阈值 `T`，令

\[
P_T=\prod_{\ell<T}\ell,\qquad
R_T(I)=\#\{n\in I:(n,P_T)=1\},
\]

\[
V_T=\prod_{\ell<T}\left(1-{1\over\ell}\right),\qquad
D_T(I)=R_T(I)-NV_T.
\]

`D_T(I)>0` 是低模剩余偏多，`D_T(I)<0` 是低模剩余亏损。

## 2. 精确 Möbius-端点恒等式

**Lemma SLM-1（端点场恒等式）。**
对任意区间 `I=[L,R]`，

\[
D_T(I)
=
\sum_{d\mid P_T}\mu(d)
\left(
\left\lfloor {R\over d}\right\rfloor
-
\left\lfloor {L-1\over d}\right\rfloor
-
{N\over d}
\right).
\tag{SLM}
\]

等价地，定义

\[
\varepsilon_d(I)
=
\left\{{L-1\over d}\right\}
-
\left\{{R\over d}\right\},
\qquad |\varepsilon_d(I)|<1,
\]

则

\[
D_T(I)=\sum_{d\mid P_T}\mu(d)\varepsilon_d(I).
\tag{SLM'}
\]

**证明。**
由 Möbius 反演，

\[
1_{(n,P_T)=1}=\sum_{d\mid (n,P_T)}\mu(d).
\]

对 `n∈I` 求和得

\[
R_T(I)=\sum_{d\mid P_T}\mu(d)
\#\{n\in I:d\mid n\}.
\]

而

\[
\#\{n\in I:d\mid n\}
=
\left\lfloor {R\over d}\right\rfloor
-
\left\lfloor {L-1\over d}\right\rfloor.
\]

同时

\[
V_T=\sum_{d\mid P_T}{\mu(d)\over d}.
\]

相减即得 `(SLM)`。用 `floor(x)=x-{x}` 得 `(SLM')`。证毕。

该恒等式说明：低模缺陷完全由端点在 CRT 小模上的锯齿相位决定。

## 3. q 行段的锯齿动力系统

对完整 `q` 行

\[
I_s=[(s-1)q+1,sq],
\]

有

\[
L-1=(s-1)q,\qquad R=sq.
\]

因此

\[
\varepsilon_d(s)
=
\left\{{(s-1)q\over d}\right\}
-
\left\{{sq\over d}\right\}.
\tag{1}
\]

若 `d|P_T` 且 `T\le p<q`，则 `(q,d)=1`。所以当 `s` 变化时，`sq mod d` 在模 `d` 上以单位步长旋转。于是：

1. `\varepsilon_d(s)` 是周期 `d` 的 sawtooth 差分；
2. 对完整周期有
   \[
   \sum_{s=1}^{d}\varepsilon_d(s)=0;
   \]
3. 因而
   \[
   \sum_{s=1}^{d}D_T(I_s)=0
   \]
   对任意固定 `T` 的完整共同周期成立。

这就是“行号旋转刚性”：任意局部大亏损必须由同一低模周期内的正偏补偿；它不能成为周期平均现象。

## 4. 与 ASB/RPD 和 Annulus 的统一

### 4.1 ASB/RPD 正缺陷

ASB/RPD 的第一锚 FAC 尖峰在低模截断下表现为

\[
D_T^{FAC}(J)>0.
\]

审计显示最尖峰窗口在小 `T` 已捕获大部分最终缺陷。因此它是正向 endpoint sawtooth 集中。

### 4.2 Annulus-Rough 负缺陷

若壳层行段

\[
I=A_s\setminus\{q^2\}
\]

没有旧 `p`-筛幸存者，则

\[
R_{p^+}(I)=0,
\]

故

\[
D_{p^+}(I)=-|I|V_{p^+}.
\]

这是负向 endpoint sawtooth 集中。

两者统一为：

```text
endpoint sawtooth field has large signed excursion.
```

## 5. 已可严格推出的 CRTDefect 形式

由 `(SLM')`，若

\[
|D_T(I)|\ge \Delta,
\]

则必有

\[
\sum_{d\mid P_T}|\varepsilon_d(I)|\ge \Delta.
\tag{2}
\]

更强地，对任意模数集合 `\mathcal D\subseteq\{d:d|P_T\}`，若尾部

\[
\left|
\sum_{\substack{d\mid P_T\\d\notin\mathcal D}}
\mu(d)\varepsilon_d(I)
\right|\le E_{\rm tail},
\]

且 `\Delta>E_tail`，则

\[
\left|
\sum_{d\in\mathcal D}\mu(d)\varepsilon_d(I)
\right|
\ge \Delta-E_{\rm tail}.
\tag{3}
\]

这给出完全严格的低模投影桥：

```text
large D_T + tail controlled
=> large signed endpoint projection on selected low moduli.
```

这一步已经是定理，不依赖启发式。

## 6. 最后仍需证明的排斥不等式

真正未闭合的是下面的强排斥：

**Signed Endpoint Sawtooth Exclusion（SESE）。**
对递推产生的 ASB 窗口与 Annulus 壳层行段，若某个低模投影满足 `(3)` 的大偏差，则必触发已有出口：

```text
CRTDefect / Tail-anchor / OSPC.
```

要证明 SESE，必须利用全部刚性：

1. **q 行旋转刚性：** `sq mod d` 对每个 `d|P_T` 是单位旋转；
2. **相邻素数壳层刚性：** 壳层旧筛幸存者除 `q^2` 外自动为素数；
3. **旧核心 seam 刚性：** 旧核心中真实素数不能被新筛删除，失败只能来自行边界漂移；
4. **相邻互质刚性：** 连续合数解释不能复用同一大因子；
5. **CRT 周期均衡刚性：** 完整周期内非零同余类严格均衡；
6. **低模端点刚性：** `D_T` 只由端点 sawtooth 相位给出，非内部随机噪声。

## 7. 为什么 SESE 不能用普通平均代替

Annulus 审计显示完整壳层行的最小旧筛幸存者数可低至 `1`。因此任何常数级平均损失都会丢失非空性。

此外，壳层行长约为 `q`，位置约为 `q^2`。证明每个这样的行段含旧筛幸存者，本质上接近 `\sqrt{x}` 长度短区间素数问题。普通 PNT、Bertrand、现有短区间素数定理都不能直接给出该尺度。

所以最终闭合必须真正使用上面的**递推特殊结构**，而不能把全局素数分布定理当黑箱。

## 8. 当前最短可攻命题

把最后硬点压缩成以下可攻版本：

**SESE-low（低模锯齿排斥）。**
存在可选低模集合 `\mathcal D_T` 与显式尾界 `E_tail`，使得对每个递推坏窗口 `I`：

1. 若 `I` 是 ASB/RPD 坏窗口，则 `D_T(I)` 的正偏差超过阈值；
2. 若 `I` 是 Annulus-Rough 坏窗口，则 `D_T(I)` 的负偏差超过阈值；
3. 该偏差在 `\mathcal D_T` 上留下大投影；
4. 大投影按 q 行旋转和 CRT 均衡传播到邻近采样窗口；
5. 传播结果与 `ASB/Core-Seam`、`Tail-anchor` 或 `OSPC` 矛盾。

这就是最后的真正硬点。本文已经严写了 1--3 的确定部分；4--5 是仍需突破的排斥不等式。

## 9. 审稿结论

本轮推进的实质成果：

```text
large signed low-mod defect
= exact Möbius endpoint sawtooth field
=> low-mod projection if tail controlled.
```

尚未完成：

```text
large low-mod projection
=> contradiction by q-rotation + CRT rigidity.
```

因此不能宣称递推证明已闭合；但最后硬点已经被精确压缩为 `SESE-low`，这是下一步唯一应攻目标。

## 10. SESE-low 到命名出口的桥接

后续严写见 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md`。该文档把 `SESE-low` 的后半段定义为可审稿的命名出口：

```text
Directed Endpoint CRTDefect.
```

具体地，把低模端点原子

\[
e_d(I)=\{(L-1)/d\}-\{R/d\}
\]

按有限低模字典 `\mathfrak B_T` 分块，定义

\[
\mathcal E_B(I)=\sum_{d\in B}\mu(d)e_d(I).
\]

若 `|D_T(I)|>=Delta` 且字典外尾项 `<=E_tail<Delta`，则鸽巢原理严格推出某个块满足

\[
|\mathcal E_B(I)|\ge {Delta-E_{\rm tail}\over |\mathfrak B_T|}.
\]

这就是 `Directed Endpoint CRTDefect`。若该块带有辅助模 Fourier 结构，则进一步触发修正归一化的 `OSPC*`，或直接登记为端点型 CRTDefect。

因此当前已闭合的是：

```text
large signed low-mod endpoint defect
=> Directed Endpoint CRTDefect / OSPC*.
```

仍未由本文闭合的是：

```text
Directed Endpoint CRTDefect / OSPC*
=> contradiction.
```

如果主链已有对该命名出口的排斥定理，则递推链可继续闭合；否则最终剩余已转移为出口排斥，而不是低模桥接本身。

后续出口排斥审查见 `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md`。该审查说明单个 `Directed Endpoint CRTDefect` 不能仅凭完整 CRT 周期零均值排除；真正剩余应写为 `PDEC-or-SAE`，即持续端点缺陷或单窗锚逃逸排斥。
