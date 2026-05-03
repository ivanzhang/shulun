# RPZ 复活点吸收缺陷路由

**状态：** `rpz_absorption_routes_to_distributed_or_named_defect`

本文承接 `prime-matrix-recursive-peeling-zero-row-hardpoint.md`。上一阶段已经澄清：
递归剥离不会自动推出连续零行；真正对象是带少数复活点的 `punctured zero window`。
本文进一步攻下一层硬点：

```text
若复活点被继续稳定吸收，
它何时进入 TailAnchor / ColumnCRT / ColumnRadius？
```

结论是：单窗吸收在样本中是分散型，不能直接推出尾锚集中。可审稿的路由必须引入漂移窗口族和列见证位移：

```text
RPZ absorption
=> survivor remains
   or TailAnchor load
   or ColumnCRT displacement load
   or ColumnRadius
   or Distributed-RPZ obligation.
```

其中最后一支是新的真实硬点，不可被省略。

## 1. RPZ 复活点与吸收标签

固定上层素数 `q` 和剥离层 `h<q`。设 `I` 是一个在 `q`-筛下为零的窗口。剥到 `h` 后的复活点为

\[
U_h(I)=\{n\in I:(n,P(h))=1,\ n>1\}.
\]

若 `I` 仍被上层筛完全覆盖，则每个 `n\in U_h(I)` 必有某个吸收标签

\[
\lambda(n)\in(h,q],\qquad \lambda(n)\mid n.
\]

选定一个标签选择器 `\lambda`。定义单窗标签负载

\[
L_T(I)=\max_{\ell\in(h,q]}\#\{n\in U_h(I):\lambda(n)=\ell\}.
\]

若 `|I|<2\ell`，则固定 `\ell` 在 `I` 中至多命中两个点。因此当 `h≈q/2` 时，单窗
`L_T` 天然很小；尾锚缺陷必须来自漂移族中的持续重复，而不是单个窗口内的粗负载。

## 2. 有限审计结论

新增审计：

```text
experiments/prime_matrix_rpz_absorption_defect_audit.py；
docs/monograph/prime-matrix-rpz-absorption-defect-audit.json；
docs/monograph/prime-matrix-rpz-absorption-defect-audit.md。
```

审计输入为 `prime-matrix-scaled-peeling-halfwidth-audit.json` 的 `5` 个已知首零行样本。
半宽层复活点统计为：

```text
total_resurrected_points = 15；
records_with_missing_absorber = 0；
global_max_local_label_load = 1；
global_max_top_column_load = 1。
```

逐例标签负载均为分散型：

| top P | half | resurrected | max label load | absorber labels |
|---:|---:|---:|---:|---|
| 13 | 5 | 3 | 1 | `{7,11,13}` |
| 17 | 7 | 2 | 1 | `{11,13}` |
| 19 | 7 | 3 | 1 | `{11,13,19}` |
| 23 | 11 | 4 | 1 | `{13,17,19,23}` |
| 29 | 13 | 3 | 1 | `{17,19,23}` |

这说明下一步不能把 `RPZ-Absorption` 简化为单窗 `TailAnchor`。如果存在矛盾，必须来自
漂移族中的重复标签、同列位移余类或远距离列见证。

## 3. 漂移族吸收账本

令 `\mathcal W=\{I_j\}` 是由相邻行漂移、缝合窗口或端点镜像产生的一族 RPZ 窗口。
每个窗口有复活点集合 `U_h(I_j)` 与吸收标签选择器 `\lambda_j`。

定义总吸收多重集

\[
\mathcal A
=
\{(j,n,\ell):n\in U_h(I_j),\ \ell=\lambda_j(n)\}.
\]

三个负载函数：

1. **尾标签负载**

\[
L_T(\mathcal W)=\max_\ell \#\{(j,n,\ell')\in\mathcal A:\ell'=\ell\}.
\]

2. **列位移余类负载。** 若同列素数见证 `\pi_c=r_cq+c` 可用，且 `n=H_jq+c` 被
`\ell` 吸收，设 `d_c=r_c-H_j`。由同列见证刚性，除小例外外

\[
d_c\not\equiv0\pmod\ell.
\]

定义

\[
L_D(\mathcal W)=
\max_{\ell,a\ne0}
\#\{(j,n,\ell)\in\mathcal A:d_c\equiv a\pmod\ell\}.
\]

3. **列半径负载。** 给定半径阈值 `D_0`，统计需要 `|d_c|>D_0` 的吸收事件数：

\[
L_R(\mathcal W;D_0)=\#\{(j,n,\ell)\in\mathcal A:|d_c|>D_0\}.
\]

这些量正好对接 `h4-pdec-column-defect-routing-contract.md` 中的
`TailAnchor / ColumnCRT / ColumnRadius` 出口。

## 4. 条件路由定理

**Theorem RPZ-AbsRoute（复活点吸收条件路由）。**
设 `\mathcal W` 是同口径 RPZ 漂移窗口族。若每个复活点都被吸收，即 `\mathcal A`
覆盖所有 `U_h(I_j)`，则以下至少一项成立：

1. `\mathcal W` 中某窗口仍有未吸收的 `h`-筛幸存者，反例失败；
2. `L_T(\mathcal W)>T_0`，进入 `TailAnchorDefect`；
3. `L_D(\mathcal W)>D_1`，进入 `ColumnCRTDefect`；
4. `L_R(\mathcal W;D_0)>0`，进入 `ColumnRadiusDefect`；
5. 三个负载均低于阈值，进入 `Distributed-RPZ(T_0,D_1,D_0)`。

**证明。**
若有复活点未被吸收，则得到下层旧筛幸存者，当前零窗反例失败。否则全部复活点贡献到
`\mathcal A`。按 `L_T,L_D,L_R` 是否超过阈值三分：超过即按定义进入对应命名出口；均未超过时，
剩余正是分散吸收分支 `Distributed-RPZ`。证毕。

该定理是路由闭合，不是最终排斥。它的作用是把含糊的“复活点被吸收会矛盾”改成唯一剩余硬点：

```text
Distributed-RPZ cannot persist.
```

## 5. 当前真正硬点

有限审计显示单窗标签负载最大为 `1`，所以最短闭合路线不是：

```text
RPZ-Absorption => TailAnchor
```

而是：

```text
RPZ-Absorption
=> Distributed-RPZ
=> ColumnCRT/ColumnRadius or survivor.
```

新增 `prime-matrix-rpz-sliding-plateau-barrier.md` 后，`Distributed-RPZ` 的第一层已经被进一步二分。
若漂移族来自同一零窗的连续滑动平台，则同一复活源在多个滑动窗口中重复出现；按窗口事件计数时，
这会形成持久源 `TailAnchor`。若坚持源删除账本，则低负载分支必须退化为边界压缩。

因此要继续推进，真正需要证明的是源删除后的分散吸收不等式：

**RPZ-BCB（boundary-compressed barrier）.**
若漂移平台中 `L_T<=T_0`、`L_D<=D_1` 且 `L_R=0`，则所有复活源被压到平台并集的两端
`T_0` 边界层。需要证明这种边界压缩要么保留公共核心中的 `h`-筛幸存者，要么进入
`SAE/PDEC/ColumnCRT` 端点缺陷。

这就是下一步最小可攻命题。它比原始 `Distributed-RPZ` 更窄，因为滑动平台已把非边界的
分散吸收强制转回 TailAnchor。

新增 `prime-matrix-rpz-boundary-compressed-core-route.md` 后，该命题的第一步已闭合为
`BCB-Core`：在无 TailAnchor 条件下，中心区间
`J_{T0}=[L+A+T0,R+B-T0]` 必为 `h`-筛零区间。剩余不再是任意边界压缩，而是：

```text
BCB-Grid/Endpoint exclusion。
```

即证明 `J_{T0}` 必含完整 `h` 对齐行，或端点缝合失败进入 `SAE/PDEC/ColumnCRT`。

新增 `prime-matrix-rpz-bcb-grid-endpoint-criterion.md` 后，`J_{T0}` 是否含完整下层行已有精确判据：
若 `J=[u,v]`、`N=v-u+1`、`\delta_h(u)\equiv1-u mod h`，则含完整 `h` 行当且仅当
`N>=\delta_h(u)+h`。失败缺口 `\Delta_h(J)=\delta_h(u)+h-N` 是端点 seam 相位。
同批样本 `5/5` 满足该判据，端点缺陷为 `0`。剩余硬点更新为
`BCB-Endpoint persistence exclusion`。

## 6. 审稿边界

本文完成：

```text
RPZ 复活点吸收标签定义；
有限样本吸收负载审计；
TailAnchor / ColumnCRT / ColumnRadius / Distributed-RPZ 五分支路由。
```

本文没有完成：

```text
源删除后的边界压缩 Distributed-RPZ 排斥；
全局 T_0,D_1,D_0 阈值；
正式 q-grid 零行到 RPZ 漂移窗口族的抽取映射。
```

下一步应直接攻 `BCB-Grid/Endpoint exclusion`，并把它写成“完整下层零行或端点缺陷”的
网格相位不等式。
