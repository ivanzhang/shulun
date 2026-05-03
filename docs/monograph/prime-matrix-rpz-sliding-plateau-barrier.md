# RPZ 滑动零窗平台屏障

**状态：** `rpz_sliding_plateau_reduces_distributed_absorption_to_tail_or_boundary`

本文承接 `prime-matrix-rpz-absorption-defect-route.md`。上一阶段发现：单个 RPZ 零窗中，
半宽复活点的吸收标签可以完全分散，不能直接推出 `TailAnchor`。本节加入一个此前没有显式计入的刚性：

```text
若一个零窗能滑动保持为零窗，则同一复活源会在多个滑动窗口中重复出现。
```

因此 `Distributed-RPZ` 不是“自由分散”。它只能有两种形态：

```text
持久源重复 => TailAnchor；
无持久重复 => 复活源被压到滑动平台边界层。
```

第二支才是新的剩余硬点。

## 1. 滑动零窗平台

固定顶层素数 `q`、半宽层 `h<q`。令

\[
I_s=[L+s,R+s],\qquad R-L+1=q,
\]

并设整数位移区间

\[
S=[A,B]\cap\mathbb Z
\]

满足每个 `I_s` 都是 `q`-筛零窗。称 `S` 为滑动零窗平台。

对一个 `h`-筛复活源 `n`，定义其平台多重度

\[
m_S(n)=\#\{s\in S:n\in I_s,\ (n,P(h))=1\}.
\]

由于 `(n,P(h))=1` 与 `s` 无关，若 `n` 被吸收，其吸收标签 `\lambda(n)\in(h,q]`
在所有包含 `n` 的滑动窗口中相同。

## 2. 多重度公式

**Lemma SPB-1（滑动平台多重度公式）。**
若 `S=[A,B]`，则

\[
m_S(n)
=
\max\{0,\ \min(B,n-L)-\max(A,n-R)+1\}.
\]

特别地，在公共核心

\[
C=[L+B,R+A]
\]

中，每个复活源的多重度都是 `|S|=B-A+1`。

**证明。**
`n\in I_s` 等价于

\[
L+s\le n\le R+s
\quad\Longleftrightarrow\quad
n-R\le s\le n-L.
\]

因此允许的位移集合正是整数区间

\[
S\cap[n-R,n-L],
\]

其大小就是公式。若 `n\in[L+B,R+A]`，则对所有 `s\in[A,B]` 均有
`L+s<=n<=R+s`，故多重度为 `|S|`。证毕。

## 3. 尾锚或边界压缩二分

定义滑动平台事件账本

\[
\mathcal A_S=\{(s,n,\lambda(n)):s\in S,\ n\in I_s,\ (n,P(h))=1\}.
\]

令

\[
L_T(S)=\max_\ell \#\{(s,n,\ell')\in\mathcal A_S:\ell'=\ell\}.
\]

**Theorem SPB-2（滑动平台屏障）。**
给定阈值 `T_0`。若滑动平台中全部复活源都被上层标签吸收，则至少一项成立：

1. `L_T(S)>T_0`，进入 `TailAnchor`；
2. 每个复活源 `n` 都满足 `m_S(n)<=T_0`；
3. 若 `|S|>T_0`，则全部复活源都避开公共核心 `C=[L+B,R+A]`，并且被压缩到平台并集
   `[L+A,R+B]` 的两端边界层中。

**证明。**
若某个复活源 `n` 有 `m_S(n)>T_0`，则同一标签 `\lambda(n)` 在
`\mathcal A_S` 中至少出现 `m_S(n)` 次，所以 `L_T(S)>T_0`。这给出第一项。
若第一项不成立，则所有复活源都必须满足 `m_S(n)<=T_0`，得到第二项。
再由 Lemma SPB-1，公共核心中的任一复活源都有多重度 `|S|`。若 `|S|>T_0`，
它不能位于公共核心；更精确地，只有靠近平台并集左右端点的位移深度不超过 `T_0`
的位置才可能满足 `m_S(n)<=T_0`。证毕。

## 4. 有限审计

新增审计：

```text
experiments/prime_matrix_rpz_sliding_plateau_audit.py；
docs/monograph/prime-matrix-rpz-sliding-plateau-audit.json；
docs/monograph/prime-matrix-rpz-sliding-plateau-audit.md。
```

在同批 `5` 个已知首零行样本中，包含原零行的最大连续滑动零窗平台均长为 `5`。
阈值 `T_0=4` 下，五个样本全部触发持久源 `TailAnchor`：

| 指标 | 数值 |
|---|---:|
| 唯一复活源总数 | `16` |
| 吸收事件总数 | `73` |
| 最大滑动零窗平台长度 | `5` |
| 最大复活源多重度 | `5` |
| `T_0=4` 触发 TailAnchor 的记录数 | `5/5` |

这说明单窗分散不是最终形态；一旦加入滑动平台，同一复活源的重复解释会重新变成尾锚负载。

## 5. 审稿边界与下一硬点

本文完成的是一个严格二分：

```text
Distributed-RPZ
=> TailAnchor
   or boundary-compressed source-deleted Distributed-RPZ。
```

本文没有证明：

```text
全局滑动平台必长 > T_0；
边界压缩分支不可能；
TailAnchor/PDEC/SAE 出口排斥证书。
```

下一步最小硬点应改为：

**RPZ-BCB（boundary-compressed barrier）。**
若低负载 `Distributed-RPZ` 避免持久源重复，则所有复活源被压到滑动平台边界层；
需要证明这种边界压缩要么保留公共核心中的 `h`-筛幸存者，要么进入 `SAE/PDEC/ColumnCRT`
端点缺陷。

这比原始 `Distributed-RPZ` 更窄：不再处理任意分散吸收，只处理源删除后的边界层逃逸。

## 6. 后续推进：BCB-Core

新增 `prime-matrix-rpz-boundary-compressed-core-route.md` 后，`RPZ-BCB` 已进一步路由为：

```text
no TailAnchor + sliding platform
=> half-sieve zero core J_{T0}
=> aligned lower zero row or SeamEndpoint/SAE/PDEC/ColumnCRT。
```

有限审计 `prime-matrix-rpz-bcb-core-audit.md` 显示，同批样本的强制中心区间实际幸存者
全部是尾锚核心源；删除尾锚核心源后，`5/5` 个中心区间干净，且 `5/5` 个中心区间含完整半宽行。
因此下一硬点再收窄为 `BCB-Grid/Endpoint exclusion`。
