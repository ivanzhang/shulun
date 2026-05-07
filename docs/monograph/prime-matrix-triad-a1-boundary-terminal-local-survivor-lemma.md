# Triad-A1 边界终端 LocalSurvivor 引理

**状态：** `boundary_terminal_reduced_to_y0_local_survivor`

本文把“方阵斜线覆盖 / 圆柱面环绕覆盖”中的一个关键边界事实抽象为可反复调用的引理：
一旦相位模数 `Q>P`，任何想落入前 `P` 行的终端零行，都不可能来自圆柱绕行后的代表，只能是该相位类的
`y=0` 首端代表。于是早期出口不需要展开整层巨大 CRT fiber，只需要检查有限个 `1<=u<=P` 的首端行是否仍有
LocalSurvivor 列。

## 1. 设置

固定奇素数 `P`。令 `Q>P` 是某一层轮筛/CRT 相位模数。对一个相位 `u mod Q`，取标准代表

```text
0<=u<Q。
```

同一相位类中的候选终端行写成

```text
r = u + yQ,  y>=0，
```

其中 `u=0` 时正代表从 `Q` 开始。第 `r` 行的列点为

```text
n(r,c)=(r-1)P+c,  1<=c<P。
```

若第 `r` 行是零行，则每个列点都被某个允许覆盖素因子解释。对行命题的早期区域，只关心

```text
1<=r<=P。
```

## 2. 边界终端引理

**BTLS-1（边界代表唯一性）。**
若 `Q>P` 且 `1<=r<=P`，则 `r` 在 `mod Q` 下的标准代表就是 `r` 本身。因此任意相位类
`u mod Q` 若要产生前 `P` 行内的终端零行，必要条件是

```text
1<=u<=P,  y=0,  r=u。
```

证明：由 `0<r<Q`，`r mod Q=r`。若 `r=u+yQ` 且 `y>=1`，则 `r>=Q>P`，矛盾。`u=0` 的正代表为
`Q>P`，也不可能落入前 `P` 行。

**BTLS-2（LocalSurvivor 排除）。**
设 `A_Q` 是某一层可能产生完整终端零行的相位支撑。若对每个

```text
u in A_Q cap {1,...,P}
```

都存在一列 `c(u)`，使

```text
ell 不整除 n(u,c(u))  对所有 ell<P，
```

则 `A_Q` 的全部相位类都不能在前 `P` 行内产生零行。

证明：若存在前 `P` 行零行 `r`，由 BTLS-1 得 `r=u in A_Q cap [1,P]`。但 BTLS-2 的假设给出该行
有一列 `c(u)` 没有任何 `ell<P` 覆盖，和零行定义矛盾。

## 3. 可计算判据

对每个支撑相位 `u` 定义首端洞集

```text
H_0(u)={c: 1<=c<P,  n(u,c) 未被任何 ell<P 覆盖}。
```

则边界早期出口完全等价于：

```text
存在前 P 行终端零行
<=> 存在 u in A_Q cap [1,P] 且 H_0(u)=empty。
```

所以审计接口可以写成：

```text
A_Q cap [1,P] = empty
  => 自动关闭；

A_Q cap [1,P] 非空但每个 H_0(u) 非空
  => LocalSurvivor witness 关闭；

某个 H_0(u)=empty
  => 找到真实前 P 行零行候选，必须进入最终反例矛盾或更强排斥。
```

同一相位类的正终端下界也立刻得到：

```text
u=0                         => lower_bound=Q>P；
1<=u<=P 且 H_0(u) 非空      => lower_bound>=u+Q>P；
u>P                         => lower_bound>=u>P。
```

这解释了为什么完整 CRT 终端可以在 `P^2` 前出现，例如 `P=23` 的第 `59` 行；只要它仍满足
`59>P`，就不违背行命题。

## 4. 几何读法

在圆柱模型中，`Q` 是圆柱周长。`Q>P` 以后，前 `P` 行只是圆柱上尚未绕行的一段短弧：

```text
绕行一次会把行号增加 Q；
但 Q 已超过 P；
因此绕行后的点不可能回到前 P 行。
```

所以“斜线尚未全部画出之前不能覆盖整行”的可证明核心，不是单纯数斜线条数，而是：

```text
若某相位 u<=P 的首端行还有一个 LocalSurvivor 列，
则所有后续绕行补洞都只能发生在 u+Q, u+2Q, ...，
已经全部晚于第 P 行。
```

这正是方阵首端局部洞与圆柱后继 fiber 的夹击：首端洞阻止早期零行，后继 fiber 只能给远处
finite/profinite PDEC 数据包。

## 5. 与升层递归的接口

对任意后继层 `Q_n>P`，若已经有相位支撑 `A_n`，则前 `P` 行出口只依赖有限集合

```text
A_n cap {1,...,P}。
```

因此无限升层不需要每次生成完整 `m_vector` 才能排除早期出口。可迭代接口为：

```text
BoundaryTerminal(A_n,Q_n):
  1. 检查 Q_n>P；
  2. 提取 A_n cap [1,P]；
  3. 对每个首端相位 u 找 LocalSurvivor 列；
  4. 若全部找到，前 P 行出口关闭；
  5. 若找不到，则该 u 是真实早期零行硬点，必须进入反例矛盾或终端证书排斥。
```

这与 `ProjectionMonotonicity / LocalFiberTerminalExpansion` 兼容：后继层只能细分已经存在的相位类；
一旦边界首端被 LocalSurvivor 关闭，后继 CRT fiber 不会把该相位的完成态搬回前 `P` 行。

## 6. 当前物化验证

`prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.md/json` 已对当前物化层执行该判据：

```text
Q=2310,30030,510510；
prime_row_count=15；
total_phase_le_p_count=113；
total_y0_completion_le_p_count=0；
all_phase_le_p_have_local_survivor=True；
all_terminal_lower_bounds_gt_p=True。
```

其中少数 `u<=P` 支撑相位都给出显式未覆盖列；没有一个 `y=0` 首端行在 `row<=P` 内完整覆盖。

这说明当前物化的 `Q=2310,30030,510510` 支撑层已经满足：

```text
BoundaryTerminalExcluded；
前 P 行出口关闭；
后续完成态只能作为 P 行之后的 finite/profinite PDEC packet。
```

## 7. 闭合边界

本文完成的是一个一般结构引理：

```text
Q>P 后，早期终端零行完全归约到 y=0 首端 LocalSurvivor 检查。
```

它没有单独完成全局行命题，因为还需处理：

```text
所有可能 PDEC 支撑相位的 A_Q 构造；
CleanKLS/DLS 平坦残余；
LocalSurvivor 证书全集；
TotalDescent 与其他终端证书的最终拼接。
```

但它关闭了一个重要无名逃逸：后继层无限环绕不能把一个已由首端 LocalSurvivor 排除的相位重新变成
前 `P` 行零行。前 `P` 行的唯一入口就是 `y=0`。
