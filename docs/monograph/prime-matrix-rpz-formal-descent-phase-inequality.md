# RPZ 正式下降路径相位不等式

**状态：** `formal_descent_paths_satisfy_grid_phase_inequality`

本文承接 `prime-matrix-rpz-lower-grid-fail-avoidance-certificate.md`。上一证书给出闭式判据：

```text
delta = -(a-1)(p-r) mod r；
grid_success iff delta<=p-r。
```

本文件澄清“证明正式下降路径全局满足 `delta<=p-r`”的精确含义。

## 1. 网格判据定理

令 `p>r` 为相邻素数，`g=p-r`，`p` 对齐行号为 `a`，

\[
I_p(a)=[(a-1)p+1,\ ap].
\]

记 `L=(a-1)p+1`，并令

\[
\delta_{p,r}(a)=(1-L)\bmod r.
\]

则 `I_p(a)` 含完整 `r` 对齐行当且仅当

\[
\delta_{p,r}(a)\le p-r.
\tag{GD}
\]

又因为 `p≡p-r (mod r)`，有

\[
\delta_{p,r}(a)\equiv -(a-1)(p-r)\pmod r.
\tag{Phase}
\]

**证明。**
从 `L` 往右的第一条 `r` 对齐行从 `L+\delta_{p,r}(a)` 开始，终点为
`L+\delta_{p,r}(a)+r-1`。它包含于长度为 `p` 的区间 `I_p(a)` 当且仅当

\[
\delta_{p,r}(a)+r-1\le p-1,
\]

即 `\delta_{p,r}(a)<=p-r`。同余式由
`1-L=-(a-1)p≡-(a-1)(p-r) (mod r)` 直接得到。证毕。

## 2. 正式下降路径的相位不等式

定义一条正式下降路径为相邻素数链

```text
p0 > p1 > ... > pm=2
```

及行号链 `a_j`，满足每一步都有完整包含：

\[
I_{p_{j+1}}(a_{j+1})\subset I_{p_j}(a_j),
\tag{Path}
\]

并且该子行不被端点穿孔 `p_j a_j` 阻断。

由第 1 节定理，任意正式下降路径自动满足

\[
\delta_{p_j,p_{j+1}}(a_j)\le p_j-p_{j+1}
\quad (0\le j<m).
\tag{Path-GD}
\]

所以“正式下降路径满足 `delta<=p-r`”不是额外猜想，而是正式路径定义与网格判据的直接推论。

## 3. 真正未闭合项：路径存在性

需要避免一个逻辑误差：任意 `p` 零行不一定给出正式下降路径。若 `p -> r` 下降失败，第一次失败
只有两类：

```text
grid_fail：delta_{p,r}(a)>p-r，故没有完整 r 子行；
puncture_block：存在完整 r 子行，但全部被端点 p*a 穿孔。
```

其中 `grid_fail` 只依赖 `a mod r`；`puncture_block` 还依赖 `a` 是否避开所有 `<=r` 素数，
因此两者都落入行号模

\[
P(r)=\prod_{\ell\le r}\ell
\]

的有限相位账本。

## 4. 首阻断二分

给定任何形式反例分支，从上层 BCB 条件零行开始尝试下降。若存在正式下降路径，则每一步满足
`(Path-GD)`，最终到达 `p=2` 时产生直接矛盾。

若不存在正式下降路径，取第一处失败的相邻转换 `p -> r`。在
`prime-matrix-rpz-first-obstruction-dichotomy.md` 中进一步证明：端点穿孔不可能阻断完整下层行，
因此第一失败实际只能是 `grid_fail` 相位。因此：

```text
formal descent path exists
=> p=2 contradiction；

formal descent path does not exist
=> first grid_fail seam phase
=> SAE if sparse；
=> PDEC/ColumnCRT if persistent or carrying displacement structure。
```

这就是目前可严格提交的全局二分。它没有排除 `PDEC/ColumnCRT`，但已经证明：

1. 正式下降路径一旦存在，`delta<=p-r` 全程成立；
2. 任何违反 `delta<=p-r` 的分支不是未命名逃逸，而是首个 `grid_fail` seam 相位；
3. 首阻断相位已被接入 `SAE/PDEC/ColumnCRT` 证书接口。

## 5. 下一硬点

现在剩余不应再表述为“证明正式路径满足相位不等式”，而应表述为：

```text
证明每个正式反例分支都存在下降路径；
或排除首阻断相位的 SAE/PDEC/ColumnCRT 证书。
```

这也是 Prime Matrix RPZ 链条当前的最小未闭合接口。
