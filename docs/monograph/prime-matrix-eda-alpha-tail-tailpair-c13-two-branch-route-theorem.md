# AlphaTail 固定 gap `C13` 二分路由定理

**状态：** `c13_two_branch_route_reduction_closed_exits_open`

本文合成 `C_local=1.3` 固定 gap 分支的最新结果。目标是把“证明所有中尺度素对局部常数
`<=1.3`”替换为一个更窄、确定的二分路由。

## 1. 输入对象

设固定 gap 责任区间为

\[
J=J(g,j_1,j_2),\qquad d=qu-j_1r,\qquad u>0.
\tag{TBR-1}
\]

原始窗口为 `I=[A,B]`。定义

\[
B_g(J)=\mathfrak S_g {|J|\over\log^2J_-},
\qquad
\Delta_{13}(g,J)=\lfloor 1.3B_g(J)\rfloor+1-N_g(J).
\tag{TBR-2}
\]

`C13` 失败当且仅当 `Delta_13<=0`。

## 2. 二分路由

**定理 TBR-1（固定 gap C13 二分路由）。**  
固定 `theta=0.1`。任何触及 `C13` 整数门槛的目标区间，即任何满足

\[
\Delta_{13}(g,J)\le L
\tag{TBR-3}
\]

的近门槛区间，必落入以下两类之一：

```text
Endpoint branch:
  u<=0.1|I|，该区间自动进入 EndpointGate；

Short-q branch:
  u>0.1|I|，该区间满足 |J|<=10，
  因而是 finite short-q SAE/PDEC 证书对象。
```

特别地，真正的 `C13` 失败 `Delta_13<=0` 也满足同一二分。

**证明。**  
若 `u<=0.1|I|`，由格点端点几何推论 `LEG-2`，责任区间自动满足 `EndpointGate(0.1)`。
若 `u>0.1|I|`，由 `LEG-3` 得 `|J|<1/0.1+1`，即 `|J|<=10`。二者互补并穷尽所有
`u>0` 情况。□

## 3. 奇偶剪枝

在 `Short-q branch` 中，若 `gap` 为奇数，则由 `ISL-2` 直接有

\[
N_g(J)=0.
\tag{TBR-4}
\]

因此短分支的实质对象只有：

```text
偶 gap、至多 10 个 q 候选、且 q,q+g 同为尾素的有限窗口。
```

这类对象可逐项列入 `InteriorSAE`，若同相位持久出现，则进入 `Short-q PDEC/ColumnCRT`。

## 4. 样本验收

当前样本链条给出：

```text
C13 integer slack:
  intervals=870, positive_even=167, failures=0, global_min_slack=1；

Endpoint gate:
  slack<=40 的 near=123，全部 endpoint，interior=0；

Large-u short exception:
  large_u=12, positive=0, failures=0, parity_void=9, max_q_length=10。
```

所以样本中 `C13` 分支已经完全按定理二分并清空：

```text
近门槛压力全部 small-u endpoint；
large-u 短窗口无正素对命中；
C13 failure 为 0。
```

## 5. 对行命题主链的影响

`C13` 分支现在不应再表述为：

```text
需要证明所有固定 gap 中尺度素对上界 <=1.3。
```

更精确的主链接口应表述为：

```text
TailPairLocalSpike(C13)
=> EndpointGate/PDEC/SAE/ColumnCRT
   or finite short-q SAE/PDEC.
```

这是真正的压缩：普通 Brun/Selberg 常数包被替换为端点 CRT 缺陷与至多 `10` 点短窗口证书。

## 6. 审稿边界

已完成：

```text
C13 整数门槛化；
奇 gap 排除；
格点端点距离引理；
small-u 自动端点化；
large-u 短窗口化；
样本 C13 分支全链清空。
```

仍未完成：

```text
EndpointGate/PDEC/SAE/ColumnCRT 的最终排斥；
全局 finite short-q SAE/PDEC 证书全集。
```

因此本文关闭的是 `C13` 的分支路由，不是 Prime Matrix 行命题的最终无条件闭合。

