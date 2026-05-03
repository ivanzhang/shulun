# WSH-Hall 扩张余量账本

**状态：** `finite_margin_certificate_and_uniform_proof_target`

本文承接 `WSH-Hall Defect Trichotomy`。本轮推进的关键变化是：

```text
不再只证明“有匹配”，而是逐个连续半素数块计算 Hall 余量。
```

这把目标从存在性匹配推进到可审查的不等式：

\[
  \mathcal M_R(B):=|N_R(B)|-|B|\ge 0.
\tag{WSH-M}
\]

## 1. 精确定义

固定相邻素数层 `p<q`，行宽为 `q`。在某行 `I_h` 内：

```text
B_h = balanced two-tail semiprimes ell_1 ell_2, y<ell_i<=p,
P_h = no-tail survivors, hence primes below q^2.
```

取

\[
  R=\lceil C\log^2 q\rceil,\qquad C=3。
\]

对任意连续半素数块

\[
  B=\{b_i,b_{i+1},\ldots,b_j\}\subset B_h
\]

定义邻域

\[
  N_R(B)=P_h\cap\bigcup_{b\in B}[b-R,b+R]。
\]

若对所有连续 `B` 有 `(WSH-M)`，则一维区间图 Hall 条件成立，从而存在从 `B_h`
到 `P_h` 的注入匹配。

## 2. 本轮有限证书

新增脚本：

```text
experiments/prime_matrix_wsh_expansion_margin_audit.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-expansion-margin-audit.md
docs/monograph/prime-matrix-wsh-expansion-margin-audit.json
```

参数：

```text
17<=p<=2000
y=floor(p/e)
R=ceil(3 log^2 q)
wheel primes = 2,3,5,7,11,13
```

全量审计结果：

```text
prime records = 297
rows with balanced semiprimes = 215074
contiguous semiprime blocks = 8440419
global minimum Hall surplus = 1
zero-surplus blocks = 0
tight blocks with surplus <=1 = 7
max tight block semiprime count = 2
```

这比之前的匹配证书更强：匹配证书只说明 Hall 条件没有失败；余量证书直接扫描
全部连续块并证明在有限范围内实际有 `+1` 的正余量。

## 3. 七个最紧块的结构含义

审计范围内只有 `7` 个块达到最小余量 `1`。它们具有两个特征：

1. 块很短：最多 `2` 个平衡双尾半素数；
2. 压力可见：低层样本出现尾标签负载 `2`，大层紧块出现固定偏移允许通道负载 `2`。

这说明真正硬点不是“大块随机缺素数”，而是很短半素数簇在端点邻域内刚好只有
`|B|+1` 个素数。全局证明应围绕这个短簇结构，而不是继续扩大枚举范围。

## 4. 五个投影共同约束临界块

任意临界块 `B` 同时受以下投影约束：

### 4.1 行几何投影

`B` 是同一 `q` 宽行中的有序连续块。因此邻域是区间并集，Hall 最坏子集可取连续块。
这是把一般匹配问题压成一维区间不等式的核心。

### 4.2 尾因子投影

每个 `b in B` 有唯一分解 `b=ell_1 ell_2`。若同一 `ell` 反复出现，则进入
`Tail-anchor`；若没有反复出现，则尾锚无法提供大规模补洞，半素数块必须依赖端点素数邻域。

### 4.3 固定偏移投影

若多个 `b` 只能通过同一偏移 `d` 获得邻域素数，则粗相位容量受

\[
  \rho_z(d)=\prod_{r\le z,\ r\nmid d}{r-2\over r-1}
\]

约束。超载时进入固定偏移 CRT/PDEC 缺陷。

### 4.4 小轮镜像投影

真实边必须满足

\[
  d\not\equiv -b\pmod r,\quad r\le z。
\]

所以一个临界块若没有足够邻域素数，只能是：

```text
允许偏移通道不足；
或允许通道存在但素数缺席。
```

前者是轮筛相位/PDEC，后者是端点亏损。

### 4.5 终端镜像投影

映射 `n -> q^2-n` 把终端缺陷转写为早期非零类块。它保留端点亏损的可计量性，
但不把缺陷变成旧方阵零行。这个区分必须在主稿中保持。

## 5. 当前最小定理目标

有限证书建议把下一步定理写成：

**WSH Positive Expansion or Named Defect.**
存在绝对常数 `C=3` 与显式阈值函数 `T_tail,T_phase,T_offset`，使得对所有充分大相邻素数
`p<q`、所有行 `I_h`、所有连续半素数块 `B`，至少一项成立：

```text
(1) |N_R(B)| >= |B|;
(2) Tail-anchor threshold fires;
(3) fixed-offset / wheel-phase PDEC threshold fires;
(4) q^2-n mirror block gives Endpoint/PDEC deficit.
```

其中 `R=ceil(C log^2 q)`。

若能证明 `(2)--(4)` 均被已有出口吸收，则 `(1)` 给出 `WSH-Hall`，进而闭合
`Distributed-RCI` 的当前最窄分支。

## 6. 仍未闭合的真实硬点

当前仍缺一个统一扩张下界：

\[
  |P_h\cap U_R(B)|\ge |B|
\]

在排除 Tail-anchor 与固定偏移/PDEC 集中后成立。有限审计显示该不等式甚至有正余量，
但正式证明必须给出以下至少一种输入：

1. 对端点镜像非零类块的短区间素数下界；
2. 对固定偏移通道的容量上界加总后仍小于可用素数邻域；
3. 对尾因子双曲线的局部不可复用上界；
4. 若以上任一失败，严格导出 `PDEC/Tail-anchor/Endpoint`。

这就是下一轮应继续严攻的唯一数学缺口。
