# DEC/OSPC* 出口排斥的最后硬点

**状态：** `single_dec_not_enough_persistent_or_local_escape_required`

本文接续 `prime-matrix-directed-endpoint-crtdefect-bridge.md`。前文已经闭合：

```text
large signed low-mod endpoint defect
=> Directed Endpoint CRTDefect / OSPC*.
```

本报告处理下一步是否能直接写成：

```text
Directed Endpoint CRTDefect / OSPC*
=> contradiction.
```

结论必须严格分开：

1. **单个窗口的 DEC 不能仅靠 CRT 零均值排除。**
2. **可攻闭合形式必须是持续缺陷排斥或单窗逃逸排斥。**
3. 因此当前唯一硬点不是再定义新出口，而是证明：

```text
每个递推坏窗口触发 DEC/OSPC*
=> persistent DEC
   or local anchor escape contradiction.
```

只有这条二分闭合后，相邻素数递推链才可升级为定理。

## 1. 为什么单点 DEC 不是矛盾

对完整 `q` 行

\[
I_s=[(s-1)q+1,sq],
\]

任一低模块 `B` 的端点投影为

\[
\mathcal E_B(s)=\sum_{d\in B}\mu(d)
\left(\{(s-1)q/d\}-\{sq/d\}\right).
\]

若 `d|P_T` 且 `T<=p<q`，则 `(q,d)=1`，所以 `s` 在模 `d` 上作单位旋转。于是 `\mathcal E_B` 在周期

\[
Q_B=\operatorname{lcm}_{d\in B}d
\]

上均值为 `0`。

但零均值只说明完整周期内正负相消；它不禁止某个 `s_0` 满足

\[
|\mathcal E_B(s_0)|\ge \kappa_B.
\]

因此如下推理无效：

```text
DEC 是非零 Fourier 模式
=> 完整周期均衡
=> 单个坏窗口矛盾。
```

原因是完整 CRT 周期远大于递推行宽 `q`，而递推反例只需要一个短窗口失败。单点端点尖峰可以是正常锯齿振荡的一部分，不自动违反完整周期均衡。

## 2. 可审稿的强形式：Persistent DEC

定义坏行集合 `S` 为同一个递推层 `p<q` 中触发同一块 `B`、同一符号 `\varepsilon∈{±1}` 的行号集合：

\[
S=\{s:\varepsilon \mathcal E_B(s)\ge \kappa_B\}.
\]

若在一个完整 `Q_B` 周期中

\[
|S|\ge \beta Q_B,
\tag{PDEC}
\]

则称出现 `Persistent Directed Endpoint CRTDefect`。

**Lemma PDEC-1（持续端点缺陷推出真实 CRT 频率缺陷）。**
令

\[
f(s)=\varepsilon\mathcal E_B(s),\qquad g(s)=1_S(s),
\]

并在 `Z/Q_B Z` 上使用归一化内积。若 `(PDEC)` 成立，则

\[
\sum_{h\ne0}|\widehat g(h)|^2
\ge
{(\kappa_B\beta)^2\over \|f\|_2^2}.
\tag{1}
\]

特别存在非零频率 `h` 使

\[
|\widehat g(h)|
\ge
{\kappa_B\beta\over \sqrt{Q_B-1}\,\|f\|_2}.
\tag{2}
\]

**证明。**
由于 `f` 均值为 `0`，

\[
\langle g,f\rangle
=\langle g-\beta,f\rangle.
\]

又由 `S` 的定义，

\[
\langle g,f\rangle
={1\over Q_B}\sum_{s\in S} f(s)
\ge \kappa_B\beta.
\]

Parseval 与 Cauchy--Schwarz 给出

\[
\kappa_B\beta
\le
\left(\sum_{h\ne0}|\widehat g(h)|^2\right)^{1/2}
\left(\sum_{h\ne0}|\widehat f(h)|^2\right)^{1/2}.
\]

而 `f` 零均值，所以第二因子为 `\|f\|_2`。得到 `(1)`。再由鸽巢原理得到 `(2)`。证毕。

这是真正能进入 `CRTDefect/Tail-anchor/OSPC*` 的对象：不是单点端点值大，而是坏行指示函数与低模周期函数发生非零频率相关。

## 3. 稀疏坏窗分支不能忽略

若 `S` 很小，PDEC-1 给出的 Fourier 下界随 `\beta` 消失，无法形成全局 CRT 矛盾。可是行命题只需一个坏行就失败。因此最终闭合必须处理稀疏分支：

```text
single or sparse DEC bad windows
=> local anchor escape contradiction.
```

这里的 local anchor escape 应写成下列形式。

**SAE（单窗锚逃逸排斥）。**
设 `I` 是递推中的 ASB/RPD 坏窗口或 Annulus-Rough 坏行段。若 `I` 触发 DEC/OSPC*，且同一低模块在相邻漂移窗口中不形成 PDEC，则 `I` 必含有：

1. 旧核心素数；或
2. 壳层旧 `p`-筛幸存者 `n\ne q^2`；或
3. 触发更高层 Tail-anchor/复用能量超标。

前两项直接否定坏窗口；第三项送入已有 Tail-anchor 出口。

SAE 是当前不能省略的局部硬输入。它本质上是“孤立短窗口端点尖峰不能单独消灭全部粗剩余”的定量版本；若没有 SAE，单点 DEC 可以存在而不违反 CRT 周期均衡。

## 4. 与 OSPC* 的精确关系

若 DEC 块按辅助模 `r` 的有向残基组织，并满足

\[
E_{\rm dir}(B)
=
{(r-1)\sum_a |C_{B,a}|^2\over \mathcal A_B^2}
\ge 1+\delta_{\rm dir},
\]

则已经进入 `OSPC*`。但 `OSPC*` 仍然是出口名称，不是矛盾本身。要排除它，必须再证明以下一项：

```text
OSPC*
=> persistent bad-row Fourier defect
=> Tail-anchor / CRT rigidity contradiction,
```

或证明：

```text
OSPC* isolated in one short window
=> SAE contradiction.
```

这与 `rse-low-block-exit-criterion.md` 的经验一致：低模块大贡献只能二分为 `OSPC*` 或加权 CRTDefect；真正剩余是证明加权缺陷界，或证明其失败触发 Tail-anchor/CRTDefect。

## 5. 最终递推链的正确写法

目前可审稿的相邻素数递推链应写为：

```text
Row(p)
+ ASB/RPD unless positive DEC/OSPC*
+ Annulus-Rough unless negative DEC/OSPC*
+ DEC/OSPC* exclusion by PDEC-or-SAE
=> Row(q).
```

其中：

- `ASB/RPD unless positive DEC/OSPC*` 已由第一锚恒等式、FAC 预算审计与低模端点桥接压缩到命名出口；
- `Annulus-Rough unless negative DEC/OSPC*` 已由平方壳层引理和负低模亏损方程压缩到命名出口；
- 尚未闭合的是 `PDEC-or-SAE`。

因此当前唯一剩余硬点的最小命题是：

```text
PDEC-or-SAE:
每个递推 DEC/OSPC* 坏窗口，要么在同一低模块上形成正密度持续缺陷，
要么孤立坏窗被局部锚逃逸/壳层旧筛幸存者排除。
```

## 6. 审稿边界

本文没有宣称完成 `DEC/OSPC*` 排斥。它完成的是最后硬点的再压缩：

```text
DEC/OSPC* exclusion
<= PDEC Fourier defect exclusion
   + SAE local escape exclusion.
```

这比原来的 `SESE-low` 更精确。它也排除了一个错误方向：不能只用“完整 CRT 周期均衡”排除单个短窗口端点尖峰。下一步必须直接攻 `SAE`，或证明递推坏窗不可能孤立，从而强制进入 `PDEC`。

## 7. 零行延迟审计接入

后续实验与引理严写见 `docs/monograph/prime-matrix-zero-row-crt-audit.md` 和 `docs/monograph/prime-matrix-zero-row-delay-recursive-lemma.md`。最新审计显示，在 `p<=2000` 的范围内，`q×q` 内旧 `p`-筛 `q` 行失败数为 `0`；对 `p<=200` 扫描到的 `p` 对齐零行均晚于 `ceil(q^2/p)`。

严格结论是：

```text
QSurv(p,q): 每个 q 行含旧 p-筛幸存者且不只含 q^2
=> Row(q).
```

但 `p` 对齐零行延迟本身不能推出 `QSurv`，因为多数 `q` 行会跨越 `p` 行边界。若 `QSurv` 失败，它仍会进入本文的同一个最终接口：

```text
QSurv failure
=> negative endpoint defect
=> DEC/OSPC*
=> PDEC-or-SAE.
```

因此零行延迟实验强化了递推直觉，但没有消除 `PDEC-or-SAE` 证明义务。

更精确的等价改写见 `docs/monograph/prime-matrix-qsurv-grid-gap-hardpoint.md`：`QSurv` 失败等价于某个素数间隙覆盖完整 `q` 网格单元。普通 `prime gap>q` 不足以失败；必须是网格对齐荒漠。因此 `SAE` 的目标是排除这种网格对齐小素标签全覆盖，或证明它必扩散为 `PDEC`。
