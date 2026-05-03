# 相邻壳层递归下降路线

**状态：** `adjacent_shell_singleton_proved_seam_guard_elimination_open`

本文回应“若 `q^2` 内存在零行，能否利用相邻壳层单点性、CRT 镜像和大周期包小周期刚性，
递归推出更小 `p^2` 内也存在零行”的路线。结论是：最关键的壳层单点性已经可严格证明；
递归闭合的唯一实质断点被压缩为 `SeamGuard-Elimination`。

## 1. 相邻壳层单点引理

设 `p<q` 是相邻素数。若 `1<n<q^2` 且 `n` 避开所有 `<=p` 的素因子，则 `n` 要么是素数，
要么没有合数情形；在闭端点 `n<=q^2` 内，唯一合数旧筛幸存者是 `q^2`。

**证明。**  
若 `n` 合数，设 `a=P^-(n)`。旧 `p`-筛幸存给出 `a>p`。因 `p<q` 相邻，`a>=q`。
若 `n=ab` 且 `b>=a`，则 `n>=q^2`。所以在 `n<q^2` 内不可能合数；在 `n=q^2` 时唯一可能是
`q*q`。证毕。

因此从 `p`-筛升级到 `q`-筛时，在 `q^2` 窗口内真正新增筛掉的旧筛幸存点只有：

```text
第一行的 q；
最后一行端点 q^2。
```

对非第一行零行而言，唯一新增穿孔就是 `q^2`。

## 2. q 零行到旧 p 零窗

令

\[
I_s^{(q)}=[(s-1)q+1,sq],\qquad 2\le s\le q.
\]

若第 `s` 条 `q` 行在 `q`-筛下为零，则由相邻壳层单点引理：

```text
s<q:  I_s^(q) 已经是旧 p-筛零窗；
s=q:  I_q^(q) 去掉 q^2 后是旧 p-筛穿孔零窗。
```

这严格实现了用户提出的核心观察：降阶时不是重新面对任意复杂合数结构，而是面对一个旧筛零窗，
最多带一个端点穿孔 `q^2`。

## 3. q 窗口降到 p 行的无损二分

写

\[
(s-1)q=mp+a,\qquad 0\le a<p,\qquad g=q-p.
\]

则 `I_s^(q)` 完整包含一条 `p` 对齐行当且仅当

\[
a=0\quad\text{or}\quad a\ge p-g.
\tag{Contain}
\]

若 `(Contain)` 成立，旧 `p`-筛零窗立即推出完整 `p` 对齐零行；若已经知道 `Row(p)`，这就是矛盾。

若 `(Contain)` 失败，则

\[
0<a<p-g,
\]

并且 `I_s^(q)` 只覆盖一条 `p` 行的后缀和下一条 `p` 行的前缀。两个未被覆盖的外侧 guard 长度为

\[
G_L=a,\qquad G_R=p-g-a.
\tag{Guard}
\]

这就是 seam zero window。它不是下层零行，但它把下层两条相邻行的幸存者全部压到两个端点 guard
里。

## 4. CRT 周期嵌套与镜像刚性

记

\[
M_p=\prod_{\ell\le p}\ell,\qquad M_q=qM_p.
\]

旧 `p`-筛图案在 `M_q` 周期内重复 `q` 次；新加入的 `q` 层只增加一个模 `q` 的零类。
这说明大周期确实包住小周期，但它只给出周期嵌套，不自动把 seam window 变成完整下层行。

CRT 镜像 `n -> -n mod M_p` 把旧 `p`-筛零窗送到周期尾部的镜像零窗。对 seam window，它交换左右端点
压力：左 guard 与右 guard 在镜像中互换。因此镜像给出的真实刚性是：

```text
若 seam guard 能长期吸收反例，
则其镜像 seam guard 也必须长期吸收反例；
持续同相端点吸收进入 PDEC/ColumnCRT；
孤立端点吸收进入 SAE。
```

镜像本身不直接产生更小 `p^2` 内零行；它产生的是两端端点压力账本。

## 5. 条件递归下降定理

**定理 ASRD（相邻壳层递归下降，条件版）。**  
假设对所有相邻素数 `p<q`，以下 `SeamGuard-Elimination(p,q)` 成立：

```text
任何旧 p-筛 seam zero window 若由 q 方阵零行诱导，
则要么两个 guard 不能同时承载 Row(p) 所需幸存者，
从而产生完整 p 对齐零行；
要么该 guard 吸收在低负载时进入 SAE，
在持久同相时进入 PDEC/ColumnCRT。
```

则任何 `q^2` 内非第一行 `q` 零行都会递归下降为更小素数层的零行或命名出口；若
`SAE/PDEC/ColumnCRT` 出口也被排除，则最终下降到 `p=2` 的不可能零行，矛盾。

**证明。**  
由第 2 节，`q` 零行给出旧 `p`-筛零窗，最多带端点穿孔 `q^2`。由第 3 节，该零窗无损二分：
若含完整 `p` 行，完成一步下降；若为 seam window，应用 `SeamGuard-Elimination`，得到完整
`p` 行或命名出口。对下降得到的完整 `p` 行重复同一论证。素数层严格下降，故有限步到达
`2`。宽 `2` 的非第一零行不可能存在。证毕。

## 6. 有限账本支撑

新增：

```text
experiments/prime_matrix_adjacent_shell_descent_ledger.py
docs/monograph/prime-matrix-adjacent-shell-descent-ledger.md/json
```

在 `p<=2000` 的 `302` 个相邻素数对上：

```text
singleton failures = 0
max seam fraction = 0.9984984984984985
min positive guard = 1
```

这说明壳层单点性完全稳定；同时也说明绝大多数行相位都是 seam 分支，不能寄希望于
`Contain` 分支自动闭合。终极硬点确实是 guard 吸收排斥。

## 7. 下一步唯一硬攻点

现在路线图已经很窄：

```text
SeamGuard-Elimination
```

可攻方向只有三类：

1. **端点容量：** 两个 guard 总长度为 `p-g`，若持续承载 Row(p) 幸存者，端点相位负载产生
   `PDEC/ColumnCRT`；
2. **镜像双端：** seam 的镜像要求另一端 guard 同时承载同类压力，形成两端帽坏窗集合；
3. **递归压缩：** guard 若继续降阶，其长度严格小于当前行宽，连续多层后要么变成完整下层行，
   要么形成持久同相端点逃逸。

因此当前不应再把目标写成泛泛的“零行自动递归”，而应直接证明：

```text
seam guards cannot absorb all forced survivors without triggering SAE/PDEC/ColumnCRT.
```

这是把用户递归剥离路线推进到可审稿定理形态后的最小剩余。

## 8. Seam 多层下降更新

新增 `docs/monograph/prime-matrix-seam-multilevel-descent-route.md` 与对应审计后，`SeamGuard-Elimination`
可以进一步改写为 `SMD-Global Inequality`。若 seam 区间 `I` 已经是旧 `p`-筛零窗，则降到
任意 `h<p` 后，条件复活点精确为

```text
Rev_{h,p}(I)={n in I : P^-(n)>h 且 P^-(n)<=p}
```

最后一条 `q` 行另加 `q^2` 端点穿孔。若某条完整 `h` 对齐行避开 `Rev_{h,p}(I)` 与端点穿孔，
则该行被强制为 `h` 零行。

有限审计显示：

```text
p<=500 全量 seam: 21339/21339 下降为强制零行；
p<=2000,row_stride=25 抽样 seam: 11488/11488 下降为强制零行；
阻断样本数均为 0。
```

这强烈支持“缝合零窗继续降阶会在某层变零行”的机制。但它仍不是全局无条件证明：如果首次
强制零行在下层方阵外，还必须继续接入下层零行延迟、递归下降或 `SAE/PDEC/ColumnCRT` 出口。
