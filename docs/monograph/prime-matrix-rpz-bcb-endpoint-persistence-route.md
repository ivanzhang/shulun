# RPZ-BCB 端点持久失败路由

**状态：** `rpz_bcb_endpoint_persistence_routes_to_sae_or_pdec_columncrt`

本文承接 `prime-matrix-rpz-bcb-grid-endpoint-criterion.md`。上一节已经证明，BCB 中心区间
`J=[u,v]` 含完整 `h` 对齐行当且仅当

\[
N\ge \delta_h(u)+h,\qquad
\delta_h(u)\equiv 1-u\pmod h.
\tag{Grid}
\]

因此 `(Grid)` 失败不是内部筛容量失败，而是有限端点相位失败。本文把该失败路由为：

```text
endpoint grid failure
=> sparse SAE
   or persistent endpoint phase defect
=> PDEC/ColumnCRT。
```

## 1. 端点失败相位

对每个 BCB 中心区间 `J=[u,v]`，定义端点相位

\[
\tau(J)=
\bigl(h,\ N\bmod h,\ u\bmod h,\ \Delta_h(J)\bigr),
\]

其中

\[
N=v-u+1,\qquad
\Delta_h(J)=\max\{0,\delta_h(u)+h-N\}.
\]

若 `\Delta_h(J)>0`，则 `J` 是一个不含完整 `h` 对齐行的半宽零核心，称为端点失败。

## 2. 稀疏/持久二分

设 `\mathcal E` 是正式反例抽取中出现的端点失败集合，`B_{\rm SAE}` 是孤立逃逸阈值。
定义相位负载

\[
M(\tau)=\#\{J\in\mathcal E:\tau(J)=\tau\}.
\]

**Theorem BCB-EndpointRoute（端点持久失败路由）。**
若 `\mathcal E` 非空，则至少一项成立：

1. `M(\tau)\le B_{\rm SAE}` 对所有端点相位成立，整个端点失败集合进入 `SAE` 稀疏包；
2. 存在端点相位 `\tau` 使 `M(\tau)>B_{\rm SAE}`，进入 `PersistentEndpointDefect(\tau)`；
3. 该持久端点缺陷按低模端点相位集中进入 `PDEC/ColumnCRT`。

**证明。**
前两项是对有限相位负载的完全二分：若所有相位负载不超过阈值，则按定义是稀疏包；
否则存在超阈值相位。对第三项，固定 `\tau=(h,N_0,a,\Delta)` 意味着所有相应中心区间的
左端点满足同一个低模残基 `u≡a (mod h)`，长度也在同一 `N mod h` 类，且都以同一缺口
避开完整 `h` 行。这正是端点 sawtooth/低模缝合缺陷：孤立时是 `SAE`，持久时给出同一
低模测试函数上的相位集中，按 `PDEC/ColumnCRT` 证书对象处理。证毕。

该定理不排除 `PDEC/ColumnCRT`；它只是证明端点失败不能作为未命名第三出口保留。

## 3. 有限相位账本

新增审计：

```text
experiments/prime_matrix_rpz_bcb_endpoint_phase_ledger.py；
docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.json；
docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.md。
```

该脚本对每条 `BCB-Core` 样本固定 `(h,N)` 后枚举全部 `u mod h`，列出可能导致 `(Grid)`
失败的端点相位。审计结果：

| 指标 | 数值 |
|---|---:|
| 实际端点失败记录 | `0/5` |
| 可能失败相位总数 | `2` |
| 单记录最大可能失败相位数 | `2` |
| 最大失败相位密度 | `0.181818` |
| 不同可能失败相位键数 | `2` |

所有可能失败相位都来自 `h=11,N=19` 的两个左端残基；实际样本没有落入这些残基。

## 4. 审稿边界

本文完成：

```text
BCB endpoint failure => SAE or PersistentEndpointDefect
PersistentEndpointDefect => PDEC/ColumnCRT routing object。
```

本文没有完成：

```text
SAE 稀疏包排斥；
PDEC/ColumnCRT 持久端点缺陷排斥；
下层 h-筛零行递归后的最终矛盾闭合。
```

下一步最小硬点因此不再是端点失败路由，而是回到既有最终出口：

```text
SAE/PDEC/ColumnCRT certificate closure
or lower-level recursive zero-row descent。
```

对 RPZ 链条而言，端点分支已经命名化；剩余关键是决定走“出口证书排斥”还是继续沿
`h`-筛零行做递归下降。

## 5. 后续推进：双轨路线

新增 `prime-matrix-rpz-dual-track-closure-route.md` 与审计
`prime-matrix-rpz-lower-zero-descent-audit.md` 后，两条路线已同步推进：

```text
Track A：SAE/PDEC/ColumnCRT certificate materialization；
Track B：lower h-zero-row recursive descent。
```

Track A 给出 `RPZ-SAE finite package`、`RPZ-PDEC endpoint phase row`、
`RPZ-ColumnCRT endpoint displacement row` 三个证书接口。Track B 证明条件下层 `p` 零行若含
不带端点穿孔的前一素数 `r` 对齐行，则下降为 `r` 零行。有限审计中，BCB-Core 给出的
`6` 条条件下层零行全部下降到 `p=2` 直接矛盾，阻断节点数为 `0`。
