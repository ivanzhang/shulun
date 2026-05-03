# RPZ-BCB 网格端点判据

**状态：** `rpz_bcb_grid_endpoint_exact_criterion`

本文承接 `prime-matrix-rpz-boundary-compressed-core-route.md`。上一节已经把无 TailAnchor 的
边界压缩分支转化为半宽筛零核心：

```text
no TailAnchor
=> J_{T0} is an h-sieve zero interval。
```

本节攻下一层：何时能从这个零区间推出完整下层 `h` 对齐零行；若不能，端点失败如何进入
可证书化的 seam 缺陷。

## 1. 精确网格包含判据

令

\[
J=[u,v],\qquad N=v-u+1,
\]

并以 `h` 为下层行宽。`h` 对齐行是

\[
[(r-1)h+1,rh].
\]

定义

\[
\delta_h(u)\equiv 1-u\pmod h,\qquad 0\le \delta_h(u)<h.
\]

则从 `u` 往右遇到的第一条 `h` 对齐行起点是 `u+\delta_h(u)`，终点是
`u+\delta_h(u)+h-1`。

**Lemma BCB-GridCriterion（精确网格包含判据）。**
区间 `J=[u,v]` 完整包含一条 `h` 对齐行，当且仅当

\[
N\ge \delta_h(u)+h.
\tag{Grid}
\]

若 `(Grid)` 失败，则失败缺口为

\[
\Delta_h(J)=\delta_h(u)+h-N>0.
\tag{EndpointDeficit}
\]

**证明。**
任何完整包含的第一条候选 `h` 对齐行只能从 `u` 右侧第一个同余 `1 mod h` 的点开始；
其起点为 `u+\delta_h(u)`。若它的终点不超过 `v`，则已经完整包含；若它的终点超过 `v`，
后续行起点更靠右，也不可能完整包含。因此完整包含等价于

\[
u+\delta_h(u)+h-1\le v,
\]

即 `N>=\delta_h(u)+h`。证毕。

## 2. 自动长度闭合与端点缺陷

**Corollary BCB-Length（纯长度闭合）。**
若

\[
N\ge 2h-1,
\]

则 `J` 对任意端点相位都完整包含一条 `h` 对齐行。

**证明。**
因为 `\delta_h(u)<=h-1`，所以 `\delta_h(u)+h<=2h-1`。代入 Lemma BCB-GridCriterion。
证毕。

**Corollary BCB-Endpoint（端点 seam 缺陷）。**
若 `J` 是 `h`-筛零区间但不完整包含 `h` 对齐行，则该失败完全由有限端点相位

\[
(h,\ u\bmod h,\ N\bmod h,\ \Delta_h(J))
\]

决定。该分支进入 `SeamEndpoint/SAE`；若同类端点相位在多个正式平台中持续复现，则进入
`PDEC/ColumnCRT`。

**证明。**
不含完整行等价于 `\Delta_h(J)>0`。这个量由 `u mod h` 与 `N` 决定；同时 `N mod h`
给出右端相位。因此失败不是内部筛容量问题，而是端点网格缝合失败。孤立失败按
`SAE` 处理；持续同相失败给出低模端点相位集中，按 `PDEC/ColumnCRT` 处理。证毕。

## 3. 接回 BCB-Core

对 `BCB-Core` 的中心区间

\[
J_{T_0}=[L+A+T_0,\ R+B-T_0]
\]

有

\[
N=q+|S|-1-2T_0.
\]

因此：

```text
BCB-Core
=> if N>=delta_h(L+A+T0)+h: lower aligned h-zero-row
=> else: endpoint seam defect with deficit Delta_h(J).
```

这一步是无损二分；没有第三种网格逃逸。

## 4. 有限审计

新增审计：

```text
experiments/prime_matrix_rpz_bcb_grid_endpoint_audit.py；
docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit.json；
docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit.md。
```

同批 `5` 个样本中：

| 指标 | 数值 |
|---|---:|
| 精确判据含完整半宽行 | `5/5` |
| 端点缺陷记录 | `0/5` |
| 判据与枚举不一致 | `0` |
| 最小判据余量 | `0` |
| 纯长度自动闭合记录 | `4/5` |

解释：样本全部闭合到下层对齐零行，但其中只有部分可由 `N>=2h-1` 自动推出；
其余必须使用端点相位 `\delta_h(u)` 的精确余量。

## 5. 后续推进：端点持久失败路由

新增 `prime-matrix-rpz-bcb-endpoint-persistence-route.md` 与审计
`prime-matrix-rpz-bcb-endpoint-phase-ledger.md` 后，端点失败分支已被命名化：

```text
endpoint grid failure
=> sparse SAE
   or persistent endpoint phase defect
=> PDEC/ColumnCRT。
```

固定 `(h,N)` 后，失败只由 `u mod h` 决定。有限相位账本显示同批样本实际端点失败为 `0/5`；
所有可能失败相位总数为 `2`，且都来自 `h=11,N=19` 的两个左端残基。由此端点失败不再是
未命名出口；剩余转回 `SAE/PDEC/ColumnCRT` 证书闭合或下层零行递归下降。

新增 `prime-matrix-rpz-dual-track-closure-route.md` 后，下层递归下降也已启动：
`prime-matrix-rpz-lower-zero-descent-audit.md` 显示，样本中 `6` 条 BCB 条件下层零行均可
递归到 `p=2` 直接矛盾，无端点/网格阻断。全局剩余变为：证明下降网格条件持久成立，
或把阻断相位送入 Track A 的 `SAE/PDEC/ColumnCRT` 证书。

## 6. 审稿边界

本文完成：

```text
BCB-Core 到下层对齐零行 / endpoint seam defect 的精确无损二分。
endpoint seam defect 到 SAE/PDEC/ColumnCRT 的持久路由。
```

本文没有完成：

```text
SAE/PDEC/ColumnCRT 出口排斥；
下层 h-筛零行如何继续递归并最终矛盾闭合；
正式坏窗抽取保证平台参数满足判据的全局证明。
```

下一步最小硬点更新为：

```text
SAE/PDEC/ColumnCRT certificate closure
or lower-level recursive zero-row descent。
```
