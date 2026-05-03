# TotalDescent-H3 六轮余量路线

**状态：** `conditional_h3_six_wheel_route_supported_not_global_proof`

本文把 `TotalDescent-TM` 的当前最窄硬点进一步压缩到固定 `h=3` 的六轮候选余量。该路线的价值是把 aligned、seam、末行穿孔统一成一个完全显式的计数不等式；它还不是全局无条件证明，因为该不等式本质上要求排除早期 `p`-筛长度 `q` 零窗。

## 1. 相邻壳层入口

设 `p<q` 为相邻奇素数，假设 `q×q` 方阵第 `s` 行，`2<=s<=q`，为 `q`-筛零行：

\[
I_s=[(s-1)q+1,sq].
\]

由相邻壳层单点性，`q^2` 内旧 `p`-筛唯一合数幸存者是 `q^2`。因此非末行 `I_s` 是旧 `p`-筛零窗，末行只需额外允许右端点 `q^2` 穿孔。对固定 `h=3`，右端点 `q^2\equiv1\pmod 3`，包含 `q^2` 的 3 对齐行不是完整包含在 `I_q` 内，所以固定 `h=3` 的完整行计数不受该穿孔影响。

## 2. 六轮候选公式

第 `R` 条完整 3 对齐行为

\[
J_R=[3R-2,3R].
\]

其中唯一避开 `2,3` 的候选数为

\[
c_R=
\begin{cases}
3R-2,&R\text{ 为奇数},\\
3R-1,&R\text{ 为偶数}.
\end{cases}
\]

令

\[
\mathcal C_3(I_s)=\{R:J_R\subset I_s\}.
\]

由于 `J_R` 中另外两个数必被 `2` 或 `3` 覆盖，`J_R` 在从 `p` 层下降到 `3` 层时是否被复活点打断，完全由 `c_R` 决定：

\[
J_R\text{ 被打断}
\quad\Longleftrightarrow\quad
5\le P^-(c_R)\le p.
\]

若 `P^-(c_R)>p`，则 `c_R` 是旧 `p`-筛幸存点。于是，在 `I_s` 为旧 `p`-筛零窗的反设下，单个这样的 `R` 已经给出矛盾。

## 3. H3 余量不等式

固定 `h=3` 的最窄全局命题可写为：

\[
\#\mathcal C_3(I_s)>
\#\{R\in\mathcal C_3(I_s):5\le P^-(c_R)\le p\}.
\tag{H3-SWR}
\]

若 `(H3-SWR)` 成立，则存在 `R∈C_3(I_s)` 使 `P^-(c_R)>p`，从而 `I_s` 不是旧 `p`-筛零窗，反设的 `q` 零行被排除。

这比早期 `TailMirror-SMD` 更窄：不再寻找任意下降层，也不再需要一般尾镜像相位；`h=3` 已把证明义务压成六轮候选线上 `[5,p]` 小素因子覆盖能力不足。

## 4. 有限账本

对应脚本与报告：

```text
experiments/prime_matrix_total_descent_h3_margin_audit.py
docs/monograph/prime-matrix-total-descent-h3-margin-audit.md
docs/monograph/prime-matrix-total-descent-h3-margin-audit.json
```

全量 `p<=5000` 审计结果：

```text
q rows checked = 1552462
h3 closed = 1552462
h3 failures = 0
min margin = 1
max margin = 561
terminal q^2 rows = 667
```

最紧样本余量为 `1`，例如 `p=5,q=7,s=2` 和 `p=7,q=11,s=11`。这说明固定 `h=3` 在有限账本中已经覆盖 aligned、seam 与末行全部分支。

## 5. 为什么它仍是硬点

`(H3-SWR)` 的正余量等价于：每个早期长度 `q` 的 `q` 行窗口中，至少有一个六轮候选数的最小素因子大于 `p`。由于窗口位于 `1..q^2`，这样的数除末端 `q^2` 外只能是素数。因此该命题实质上接近“每个 `q` 宽行窗口含素数”的原行命题。

普通外部素数间隙定理不能直接给出 `(H3-SWR)`。例如已知的无条件短区间素数定理通常给出长度 `x^\theta`、`\theta>1/2` 的区间，而这里在 `x≈q^2` 附近要求长度 `q≈x^{1/2}`。因此不能把有限账本或通用素数间隙输入误写成全局证明。

## 6. 下一步真实硬攻目标

正式证明只能走两条路之一：

1. **直接证明 `(H3-SWR)`。** 对六轮候选线证明 `[5,p]` 素因子的并集覆盖数严格小于完整 3 行数。
2. **证明失败相位进入命名出口。** 若 `[5,p]` 素因子覆盖全部六轮候选，则这种精确覆盖必须产生低模过载、端点缺陷、固定偏移 PDEC 或 ColumnCRT 位移缺陷。

因此当前最窄硬点应命名为：

```text
H3-SixWheel-Roughness
or
H3 full blocking => SAE/PDEC/ColumnCRT.
```

该命名比“继续递归寻找某层零行”更精确：一旦固定 `h=3`，剩余障碍就是六轮候选全覆盖的排斥不等式或其缺陷路由。
