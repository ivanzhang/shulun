# WSH-Hall 短临界块归约

**状态：** `finite_short_critical_reduction_not_global_proof`

本文把 `WSH Positive Expansion or Named Defect` 再压缩一层。上一轮证明目标是：

\[
  |N_R(B)|-|B|\ge 0
\]

或进入 `Tail-anchor / fixed-offset-PDEC / Endpoint`。本轮的新观察是：真正危险的块在有限审计中
全部短化。

## 1. 几何正规形

令 `B={b_i,...,b_j}` 是一行内连续平衡双尾半素数块，`R=ceil(3 log^2 q)`。
定义

\[
  \mathcal M_R(B)=|N_R(B)|-|B|.
\]

若存在 Hall 失败块，则存在一个极小失败块 `B_min`，满足：

1. `B_min` 是连续块；
2. `\mathcal M_R(B_min)<0`；
3. 任意真连续子块 `B'` 满足 `\mathcal M_R(B')>=0`。

此外，如果 `B` 的 `R`-邻域分成多个互不相交分量，则

\[
  \mathcal M_R(B)=\sum_\nu \mathcal M_R(B_\nu),
\]

其中 `B_\nu` 是对应分量中的半素数子块。因此极小失败块必须位于一个连通邻域分量内。

这给出第一层证明化压缩：

```text
全局 Hall 失败
=> 连通短区间内的极小临界半素数簇。
```

## 2. 小余量有限审计

使用同一脚本但改参数：

```text
python3 experiments/prime_matrix_wsh_expansion_margin_audit.py \
  --tight-surplus 2 \
  --out-prefix docs/monograph/prime-matrix-wsh-short-critical-block-audit
```

结果：

```text
17<=p<=2000
rows with balanced semiprimes = 215074
contiguous semiprime blocks = 8440419
global minimum Hall surplus = 1
zero-surplus blocks = 0
tight blocks with surplus <=2 = 45
max tight block semiprime count = 3
```

小余量块按 `(surplus, |B|)` 分布为：

| surplus | semiprime count | block count |
| ---: | ---: | ---: |
| 1 | 1 | 4 |
| 1 | 2 | 3 |
| 2 | 1 | 24 |
| 2 | 2 | 10 |
| 2 | 3 | 4 |

所以在审计范围内：

```text
所有余量 <=2 的临界块都满足 |B|<=3。
```

这比“匹配存在”更接近证明目标，因为它把潜在失败压成极短局部构型。

## 3. 三类短块

### 3.1 单点块

`|B|=1` 时，所需条件是

\[
  |P_h\cap[b-R,b+R]|\ge 1。
\]

有限审计中单点最小余量为 `1`，即邻域内至少有 `2` 个素数。若全局失败，则是直接端点素数亏损。

### 3.2 双点块

`|B|=2` 时，两个半素数的邻域可能重叠。若重叠很强，则固定偏移通道负载上升；
若不重叠，则余量分解为两个单点余量之和。因此双点临界块只能来自：

```text
两个半素数距离 <=2R 且共享很少素数邻域余量。
```

有限审计中最紧双点块的余量为 `1`，并出现尾标签负载 `2` 或固定偏移允许通道负载 `2`。

### 3.3 三点块

`|B|=3` 是当前有限审计中的最大小余量块。所有这类块余量为 `2`，最大尾标签负载为 `2`，
最大固定偏移允许通道负载为 `3`。因此三点临界块已经显示固定偏移通道压力。

## 4. 新的最小证明目标

全局目标可拆成两个更窄命题：

### SCB-1：长块自动扩张或命名缺陷

若 `|B|>=4` 且 `B` 不触发 Tail-anchor、fixed-offset/PDEC 或 Endpoint mirror deficit，则

\[
  \mathcal M_R(B)\ge 3。
\]

这会把所有真正危险块压缩到 `|B|<=3`。

### SCB-2：短块局部排斥

对 `|B|<=3` 的短块，证明：

```text
M_R(B)<0
=> Tail-anchor or fixed-offset-PDEC or Endpoint mirror deficit.
```

这两个命题合起来推出 `WSH Positive Expansion or Named Defect`。

## 5. 可用刚性投影

短临界块应同时使用以下约束，而不是只用短区间素数下界：

1. **尾因子唯一分解：** `b=ell_1 ell_2`，`y<ell_i<=p`；
2. **大因子不可复用：** 相邻短块若共享 `ell`，立即给 Tail-anchor 候选；
3. **固定偏移容量：** 多个 `b` 依赖同一 `d` 时受 `rho_z(d)` 限制；
4. **小轮禁类：** 真实素数边必须避开 `d=-b mod r`；
5. **端点镜像：** `q^2-b` 把终端亏损转为早期非零类端点亏损；
6. **行几何连通性：** 不连通邻域的余量可分解，极小坏块必连通。

## 6. 下一步硬攻点

当前最小硬点已从全体连续块缩成：

```text
SCB-1 长块自动扩张
或
SCB-2 三点以内短块排斥。
```

从可行性看，优先攻 `SCB-2`：它只涉及单点、双点、三点半素数簇，可以逐项写出
尾标签、偏移、轮筛与镜像端点约束。若 `SCB-2` 失败，失败样式会非常明确，适合直接接入
`Endpoint/PDEC` 证书。
