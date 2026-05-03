# GJE-SAE 的终端带分解与短区间指数屏障

**状态：** `terminal_band_is_the_true_gje_sae_core`

本文接续 `prime-matrix-qsurv-grid-gap-hardpoint.md`。目标是把 `GJE-SAE` 再拆细：哪些行可由一般短区间素数输入覆盖，哪些行必须用方阵/CRT 矛盾场的专门结构处理。

## 1. GJE-SAE 回顾

对相邻奇素数 `p<q`，`GJE-SAE` 要排除

\[
I_s^{(q)}=[(s-1)q+1,sq],\qquad 1\le s\le q,
\]

为空素数行：

\[
I_s^{(q)}\cap\mathbb P=\varnothing.
\]

这等价于 `QSurv` 失败，也等价于一个素数间隙覆盖完整 `q` 网格单元。

## 2. 一般短区间定理只能覆盖低行段

设有外部短区间输入：

```text
SI(theta,C):
对充分大 x，区间 [x, x+C x^theta] 中含素数。
```

若要用它覆盖第 `s` 个 `q` 行，只需

\[
C((s-1)q)^\theta\le q.
\]

因此可覆盖

\[
s\le 1+C^{-1/\theta}q^{1/\theta-1}.
\tag{1}
\]

这给出一个明确屏障：

- 若 `theta>1/2`，则 `1/theta-1<1`，只能覆盖 `s<=q^{1/theta-1}` 量级的低行段；
- 若要覆盖全部 `s<=q`，必须达到 `theta<=1/2`，且常数在终端 `x≈q^2` 处足够小。

所以任何 `theta>1/2` 的普通短区间素数定理，即使非常强，也不能闭合 `GJE-SAE` 的终端带。RH 型 `sqrt(x) log x` 也不足以给长度正好为 `q` 的每个网格行非空。

## 3. 终端带是唯一真正硬核

令

\[
H_\theta(q)=\left\lfloor C^{-1/\theta}q^{1/\theta-1}\right\rfloor.
\]

一般短区间输入最多给出：

```text
Rows 1 <= s <= H_theta(q) are covered.
```

剩余终端带为

\[
H_\theta(q)<s\le q.
\]

当 `theta=0.525` 量级时，`H_theta(q)` 约为 `q^{0.904...}`，仍留下绝大多数靠近 `q^2` 的行。故最终硬点不是低行段，而是：

```text
near-q^2 terminal q-grid desert exclusion.
```

这解释了为什么本路线必须利用方阵/CRT 的端点、镜像和标签覆盖刚性，而不能只引用普通短区间素数结果。

## 4. 终端带的 q² 镜像 CRT 形式

对终端行写

\[
s=q-h+1,\qquad 1\le h\le q.
\]

则

\[
I_{q-h+1}^{(q)}=[(q-h)q+1,(q-h+1)q].
\]

令

\[
m=q^2-n.
\]

当 `n` 遍历该行时，`m` 遍历

\[
[(h-1)q,\ hq-1],
\]

仍是长度 `q` 的网格块。

对任意旧素数 `\ell<=p`，因为 `q` 与 `\ell` 互素，

\[
\ell\mid n
\quad\Longleftrightarrow\quad
m\equiv q^2\pmod\ell.
\tag{2}
\]

注意 `q^2 mod ell` 是非零类。于是终端空素数行等价于：

```text
在 m 的长度 q 网格块中，
每个 m 都落入某个小素数 ell<=p 的一个非零指定类 q^2 mod ell。
```

这就是终端带的镜像 CRT 标签覆盖形式。它比普通“合数覆盖”更刚性：每个小素数只允许一个非零残基类，并且这些残基类由同一个 `q^2` 相位统一决定。

## 5. 终端 SAE 的精确目标

在镜像变量中，`SAE` 应证明：

**Terminal-SAE.**
不存在 `1<=h<=q` 使

\[
[(h-1)q,hq-1]
\subseteq
\bigcup_{\ell\le p}\{m:m\equiv q^2\pmod\ell\}.
\tag{3}
\]

或者，若 `(3)` 在某个孤立 `h` 上成立，则相邻 `h` 块的端点旋转必产生同一低模块的持续缺陷，从而进入 `PDEC`。

这把最终硬点从“找素数”转写为一个纯 CRT 覆盖命题：

```text
one nonzero residue class per small prime
cannot cover a terminal q-block
without producing persistent endpoint defect.
```

## 6. 已知刚性在终端形式中的位置

| 刚性 | 终端镜像表达 | 用途 |
| --- | --- | --- |
| 非零类约束 | `m≡q^2 mod ell`，且非零 | 排除零类自由度 |
| 同标签间距 | 同一 `ell` 命中间距为 `ell` | 限制单标签密集覆盖 |
| 相邻互质 | 相邻 `n` 不能同由同一小素数解释 | 限制局部补洞模式 |
| 端点旋转 | `h` 增加时端点按步长 `q` 旋转 | 孤立失败若扩散则进入 PDEC |
| 平方壳层 | 避开全部旧素数者自动为素数或 `q^2` | 把粗数命题还原为素数命题 |

## 7. 当前最小路线图

现在的最短攻坚链为：

```text
GJE-SAE
<= low rows by SI(theta,C)
   + terminal rows by Terminal-SAE/PDEC.
```

如果不引用任何外部短区间定理，则低行段也可保留在同一 `Terminal-SAE` 型 CRT 覆盖框架中；但真正困难仍集中在 `s≈q` 的终端带。

## 8. 审稿边界

本文不是 `GJE-SAE` 的证明。它完成的是定位：

1. 普通短区间素数定理若指数 `theta>1/2`，不能闭合全部网格行；
2. 终端带可精确镜像为非零指定类 CRT 覆盖问题；
3. 最终必须证明 `Terminal-SAE`，或证明其失败触发 `PDEC`。

因此当前唯一最小硬点进一步收缩为：

```text
Terminal-SAE/PDEC for the q^2 mirror CRT cover.
```

进一步分层见 `docs/monograph/prime-matrix-terminal-sae-split-inequality.md` 与审计 `docs/monograph/prime-matrix-terminal-sae-split-audit.md`。取 `y=max(2,floor(p/e))`，若低筛骨架数 `G_y(h)` 严格大于尾素数命中重数 `T_y(h)`，则尾素数无法覆盖全部骨架点，从而直接排除该终端行反例。样本 `p<=1000` 中所有终端镜像块均满足正余量。当前最小硬点可进一步写成 `TSI-or-PDEC`。
