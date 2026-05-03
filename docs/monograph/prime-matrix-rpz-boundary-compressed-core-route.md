# RPZ-BCB 边界压缩核心路由

**状态：** `rpz_bcb_routes_to_half_zero_core_or_endpoint_defect`

本文承接 `prime-matrix-rpz-sliding-plateau-barrier.md`。上一节证明：

```text
滑动平台中的 Distributed-RPZ
=> TailAnchor
   or boundary-compressed source-deleted Distributed-RPZ。
```

本文继续攻下一层：若排除 `TailAnchor`，边界压缩不仅是“复活源靠边”，还会强制中间出现一个
半宽筛零核心区间。

## 1. 强制核心区间

设顶层零窗平台为

\[
I_s=[L+s,R+s],\qquad s\in S=[A,B]\cap\mathbb Z,
\]

其中 `R-L+1=q`。令 `m=|S|=B-A+1`，低负载阈值为 `T_0`，半宽层为 `h<q`。

定义强制核心区间

\[
J_{T_0}=[L+A+T_0,\ R+B-T_0].
\tag{BCB-Core}
\]

当 `m>T_0` 时，`J_{T_0}` 是平台并集去掉左右 `T_0` 边界层后的中心部分，长度为

\[
|J_{T_0}|=q+m-1-2T_0.
\tag{BCB-Length}
\]

## 2. 核心零区间定理

**Theorem BCB-Core（边界压缩强制半宽零核心）。**
假设：

1. 每个 `I_s` 都是顶层 `q`-筛零窗；
2. 平台内所有 `h`-筛复活源都被上层标签吸收；
3. `m>T_0`；
4. 没有 `TailAnchor` 事件，即任一复活源的平台多重度都不超过 `T_0`。

则

\[
\mathcal R_h(J_{T_0})=\varnothing.
\]

也就是说，`J_{T_0}` 是一个半宽层 `h`-筛零区间。

**证明。**
若 `n\in J_{T_0}` 且 `(n,P(h))=1`，则 `n` 是平台并集中某个窗口的 `h`-筛复活源。
由滑动平台多重度公式，`n` 距平台并集两端均超过 `T_0-1`，所以它被至少 `T_0+1` 个
滑动窗口包含，即 `m_S(n)>T_0`。若该复活源被吸收，则同一吸收标签在这些窗口中重复出现
超过 `T_0` 次，触发 `TailAnchor`。这与第 4 条矛盾。因此这样的 `n` 不存在。证毕。

## 3. 对齐零行或端点缺陷二分

**Corollary BCB-Grid（半宽零核心的网格出口）。**
在 Theorem BCB-Core 条件下，至少一项成立：

1. `J_{T_0}` 完整包含一条 `h` 对齐行，于是得到下层 `h`-筛零行；
2. `J_{T_0}` 不完整包含任何 `h` 对齐行，于是两端端点落入同一个或相邻的 `h` 网格缝合区，
   形成 `SeamEndpoint/SAE` 型端点缺陷；
3. 若该端点缝合缺陷在多个平台中持续，则其端点相位进入 `PDEC/ColumnCRT`。

**证明。**
由 Theorem BCB-Core，`J_{T_0}` 中没有 `h`-筛幸存者。若存在完整包含的 `h` 对齐行，则该行
也是 `h`-筛零行，得到第一项。

否则 `J_{T_0}` 的长度和位置不足以覆盖完整 `h` 对齐行；这完全由两端相对 `h` 网格的残基决定。
该失败不是内部容量现象，而是端点缝合现象，按已有 `Seam/SAE/PDEC` 账本进入第二项。
若同类端点残基在漂移族或多平台中持续复现，则得到同口径低模端点相位集中，进入
`PDEC/ColumnCRT`。证毕。

## 4. 有限审计

新增审计：

```text
experiments/prime_matrix_rpz_bcb_core_audit.py；
docs/monograph/prime-matrix-rpz-bcb-core-audit.json；
docs/monograph/prime-matrix-rpz-bcb-core-audit.md。
```

在同批 `5` 个样本中：

| 指标 | 数值 |
|---|---:|
| 删除尾锚核心源后中心区间干净的记录数 | `5/5` |
| 强制中心区间含完整半宽行的记录数 | `5/5` |
| 中心区间实际半宽幸存者总数 | `11` |
| 其中尾锚核心源总数 | `11` |
| 非尾锚核心源总数 | `0` |
| 最大强制中心区间长度 | `25` |

解释：样本中的中心区间并非天然为空；它们的幸存者正是上一层触发 TailAnchor 的持久源。
在条件分支“无 TailAnchor”下，这些中心源被禁止，于是强制中心区间变成半宽筛零区间。

## 5. 审稿边界

本文完成：

```text
RPZ-BCB => half-sieve zero core
half-sieve zero core => aligned lower zero row or endpoint seam defect。
```

本文没有完成：

```text
全局证明 J_{T_0} 必含完整 h 对齐行；
端点 seam 缺陷的全局排斥；
下层 h-筛零行的最终矛盾闭合。
```

下一步最小硬点更新为：

```text
BCB-Grid/Endpoint exclusion。
```

具体应证明：在正式坏窗抽取出的平台中，`|J_{T_0}|` 与端点相位不能同时避开所有完整
`h` 对齐行；若避开，则端点残基持续集中，进入 `SAE/PDEC/ColumnCRT`。
