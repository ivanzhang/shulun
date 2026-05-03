# Prime Matrix A/B 入口归约定理清单

本文档完成外审前 H1 义务：把行/列全合数反例进入 `Structured-EHPD` 的入口归约整理为可引用定理列表。证明主体见 `docs/row-column-reduction-formal-appendix.md`，定义匹配见 `docs/ab-to-d-interface-match.md`。

## 0. 审稿结论

A/B 入口归约已经达到 `Reduction-closed`：

```text
full-composite row or non-P column
=> small-factor locks + 45-degree small-factor locks + tail anchors + Structured-EHPD bad configuration.
```

该结论只说明反例可以无损进入统一坏配置接口；它不证明 `Structured-EHPD` 坏配置不存在。因此它不能单独推出 Prime Matrix 行列命题。

## 1. 入口对象

设 `P` 为奇素数，方阵点为

```text
n(r,c)=(r-1)P+c, 1<=r,c<=P.
```

列命题只考虑 `1<=c<P`，因为第 `P` 列满足 `n(r,P)=rP`，由因子 `P` 平凡全覆盖。

令

```text
D=floor(sqrt(P)).
```

对合数点的解释分为：

1. 小因子锁定：存在素数 `ell<=D` 整除该点；
2. 双粗主体：剥离小因子后由两个 `>D` 的因子解释；
3. 尾部锚：双粗解释中出现 `q in [tau P,P]` 的尾部因子。

## 2. 引理清单

| 编号 | 名称 | 状态 | 作用 |
|---|---|---|---|
| AB1 | 三层不重不漏 | `Proved-in-text` in appendix | 把每个合数点分入小因子锁定、双粗主体、尾部锚 |
| AB2 | 行短窗大因子互斥 | `Proved-in-text` in appendix | 同一大因子不能解释短距离内两个行点 |
| AB3 | 列截面大因子互斥 | `Proved-in-text` in appendix | 同一大因子在列截面按周期复现，短窗不可复用 |
| AB4 | 第 `P` 列排除 | `Proved-in-text` in appendix | 排除平凡列，固定非第 `P` 列的合法入口 |
| AB5 | CRT 非零类均衡入口 | `Proved-in-text` in appendix | 小因子层剥离后，各非第 `P` 列的非零骨架计数相等 |
| AB6 | 正反 45 度锁定归属 | `Proved-in-text` in appendix | `P±1` 小因子斜线只归入小因子层，不重复算主体容量 |

这些引理均是入口归约引理，不含 D 组终局排斥。

## 3. 定理清单

### 3.1 Theorem A：列反例入口

**Theorem A.** 固定 `1<=c<P`。若第 `c` 列所有点均为合数，则该列在剥离小因子锁定与 Tail-log4 尾部锚后，诱导一个 `Structured-EHPD` 坏配置。

证明来源：`docs/row-column-reduction-formal-appendix.md` 第 5 节。

依赖：

```text
AB1 + AB3 + AB4 + AB5 + Tail-log4 input.
```

状态：`Reduction-closed`。

### 3.2 Theorem B：行反例入口

**Theorem B.** 固定 `1<=r<=P`。若第 `r` 行所有点均为合数，则该行在剥离小因子锁定、正反 45 度小因子锁定与 Tail-log4 尾部锚后，诱导一个 `Structured-EHPD` 坏配置。

证明来源：`docs/row-column-reduction-formal-appendix.md` 第 7 节。

依赖：

```text
AB1 + AB2 + AB6 + Tail-log4 input.
```

状态：`Reduction-closed`。

### 3.3 Corollary AB：入口闭合条件

**Corollary AB.** 若 `Structured-EHPD` 坏配置不存在，且 Tail-log4 尾部估计成立，则任一非第 `P` 列反例或任一行反例均不可能存在。

证明来源：`docs/row-column-reduction-formal-appendix.md` 第 8 节。

状态：条件闭合；终点仍为 H2/H4/H5 的数学硬接口。

## 4. A/B 到 D 的定义匹配

`docs/ab-to-d-interface-match.md` 负责把 A/B 归约后的主体双粗锚坏配置逐项匹配到 D 组 `Structured-EHPD` 标准形式：

| D 标准项 | A/B 来源 | 匹配状态 |
|---|---|---|
| 覆盖性 | 剥离后剩余候选必须由主体双粗锚覆盖 | M1 |
| 非终端性 | 最小坏配置无短簇/高投影/FCT 终端 | M2 |
| 非共振背景 | 大因子相位进入 NRC/FCT 二分 | M3 |
| 能量有界 | 分裂权重与条件期望能量 | M4 |
| 一阶偏差 | 全覆盖迫出 Fourier 一阶偏差 | M5 |

这说明 A/B 入口和 D 标准形式之间没有未命名接口；剩余问题是 D 组排斥是否成立。

## 5. 剥离不重不漏规则

为避免解释层重叠，审稿版固定以下优先级：

```text
small factor lock
=> 45-degree small-factor lock
=> tail anchor
=> body double-rough anchor.
```

若一个点有多个解释，按优先级只登记一次；若主体层需要多锚权重，则使用分裂权重并保持每点权重和为 `1`。该规则保证小因子层、尾部锚层和主体容量账本不重复计数。

## 6. Tail-log4 的边界

Tail-log4 在 A/B 入口中只作为尾部锚剥离输入：

```text
tail anchors contribute to the V_D P/log^4 P ledger.
```

A/B 入口清单不重新证明 Tail-log4，也不把 Tail-log4 写成 D 组排斥。若 Tail-log4 被审稿要求重证，应在 H4/H5 的 Rankin/RRD/OSPC 账本中处理。

## 7. 不可越界声明

可以声明：

```text
A/B entrance reduction is closed as a reduction interface.
```

不能声明：

```text
Prime Matrix row/column theorem is proved.
```

原因是终局仍需要：

```text
Structured-EHPD exclusion
or RHI replacement
plus PDEC/SAE/Rankin/RRD/OSPC closure.
```

## 8. H1 当前状态

H1 作者侧工程义务已完成：

1. A/B 入口已拆成 AB1--AB6、Theorem A、Theorem B、Corollary AB；
2. 剥离优先级与不重不漏规则已明确；
3. A/B 到 D 的定义匹配入口已固定；
4. 主稿状态应标为 `Reduction-closed Statement`，不得升级为终局定理。
