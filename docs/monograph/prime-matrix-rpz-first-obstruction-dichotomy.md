# RPZ 首阻断全局二分

**状态：** `first_obstruction_is_grid_fail_or_path_descends`

本文承接 `prime-matrix-rpz-formal-descent-phase-inequality.md`。目标是闭合“路径存在性”中可直接证明的
部分，并把真正未闭合项压到唯一类型的首阻断相位。

## 1. 端点穿孔不能阻断完整下层行

设 `p>r` 为相邻素数，`I_p(a)=[(a-1)p+1,ap]` 是一条 `p` 对齐行。剥去顶层素数 `p`
后，唯一可能复活点是端点

\[
ap.
\]

它实际复活只可能在 `a` 避开所有 `<=r` 素数时发生，特别地此时

\[
r\nmid a.
\tag{Rough}
\]

若某条完整 `r` 对齐行

\[
J_r(b)=[(b-1)r+1,br]
\]
被包含在 `I_p(a)` 中且含有端点 `ap`，则由于 `ap` 是 `I_p(a)` 的右端点且
`J_r(b)\subset I_p(a)`，必有

\[
br=ap.
\]

于是 `r|ap`。因 `r\ne p` 且 `r,p` 都是素数，所以 `r|a`，这与 `(Rough)` 矛盾。

因此：

```text
只要 I_p(a) 含完整 r 对齐行，端点穿孔 ap 不可能阻断该完整 r 行。
```

这把先前账本中的 `puncture_block` 从可能出口降为全局空出口。有限审计中
`puncture_block_density=0` 是该定理的样本反映，而不是偶然现象。

## 2. 路径存在性的精确等价

令 `r=p^-` 为 `p` 的前一素数，`g=p-r`。由网格判据：

\[
\delta_{p,r}(a)=-(a-1)g\pmod r,
\qquad
I_p(a)\text{ 含完整 }r\text{ 行}
\Longleftrightarrow
\delta_{p,r}(a)\le g.
\tag{Grid}
\]

由第 1 节，若 `(Grid)` 成立，则至少存在一条不被端点穿孔阻断的完整下层行。因此：

```text
p 零行可向 r 层下降
iff
delta_{p,r}(a)<=p-r。
```

所以路径存在性不再有两个阻断类型；它只差一个 `grid_fail` 相位控制。

## 3. 首阻断二分

从任意条件 `p_0` 零行出发，递归尝试下降到前一素数层。由于素数层严格递减，过程有限。

若每个遇到的节点都满足 `(Grid)`，则可逐层选择完整下层行，得到正式下降路径直到 `p=2`。
到达 `p=2` 时，任意 `2` 对齐行 `[2m-1,2m]` 含奇数 `2m-1`，不可能是 `2`-筛零行，
从而矛盾。

若不能下降到 `p=2`，取第一处不能继续下降的节点。由第 1 节，失败不可能是端点穿孔阻断；
因此必为

\[
\delta_{p,r}(a)>p-r.
\tag{First-GF}
\]

这就是首个 `grid_fail` seam 相位。

于是全局二分为：

```text
每个条件零行分支
=> 存在正式下降路径 => p=2 矛盾；
or
=> 存在首个 grid_fail seam 相位 => SAE/PDEC/ColumnCRT 证书义务。
```

## 4. 证书路由

首个 `grid_fail` 相位只依赖

\[
(p,r,a\bmod r)
\]

或更强地依赖行号模

\[
P(r)=\prod_{\ell\le r}\ell.
\]

因此它是有限相位账本对象。后续只有三种合法处理：

1. **SAE**：若该首阻断相位只产生低负载孤立窗口，则逐窗给出局部证书；
2. **PDEC**：若同一首阻断相位持久重复，则提交同相位坏窗集合的 `U_CRT<L_PDEC` 证书；
3. **ColumnCRT**：若同一首阻断相位携带列位移或吸收标签，则提交位移负载阈值证书。

这一步没有排除这些证书义务，但它关闭了一个逻辑缺口：

```text
不存在“端点穿孔阻断”第三逃逸；
不存在未命名的下降失败；
所有不下降分支都是 first-grid-fail 证书分支。
```

## 5. 当前最终剩余

RPZ 下层下降链现在可写成：

```text
BCB 条件零行
=> formal descent to p=2 contradiction
or first-grid-fail seam phase
=> SAE/PDEC/ColumnCRT certificate exclusion。
```

因此下一最小硬点不是再研究端点穿孔，而是直接攻：

```text
first-grid-fail seam phase 的 PDEC/ColumnCRT 排斥证书。
```
