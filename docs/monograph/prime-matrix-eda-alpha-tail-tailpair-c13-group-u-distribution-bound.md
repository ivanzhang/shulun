# AlphaTail `C13` group 数与 `u` 分布确定性上界

**状态：** `c13_group_u_distribution_bound_input_ready`

本文接续确定性 `Omega` 上界。目标是把“目标族中会出现多少 group、这些 group 的 `u` 如何分布”
从实际 witness 数据中剥离，改写成纯几何除数和。

## 1. 四层候选宇宙

固定窗口 `(P,B,r,m)`，记 `R=|r|`。对一对点位 `j_1>j_2`，设

\[
\Delta=j_1-j_2,\qquad \Delta R=g u.
\tag{GUD-1}
\]

每个正因子 `u|\Delta R` 决定一个固定 gap

\[
g={\Delta R\over u}.
\tag{GUD-2}
\]

若 `g` 为偶数且对应 q 区间非空，则得到一个几何候选责任区间。由端点方向和残差
`epsilon`，它再给出一个 envelope group。

本文分四层：

```text
GeometricCandidate : 只用 (GUD-1) 与端点带几何；
PositiveCandidate  : 几何候选中 actual>0；
NarrowCandidate    : PositiveCandidate 且 integer_slack<=slack_cut；
C13Failure         : 真正 local_C 失败记录。
```

显然有嵌套关系

\[
\mathcal G_{\rm fail}
\subset
\mathcal G_{\rm narrow}
\subset
\mathcal G_{\rm positive}
\subset
\mathcal G_{\rm geo}.
\tag{GUD-3}
\]

因此只要控制 `GeometricCandidate` 的 group 数与 `u` 分布，就自动控制全部真实失败 group。

## 2. 除数和上界

对固定 `m`，几何候选记录数满足

\[
\#\mathcal R_{\rm geo}(m)
\le
\sum_{\Delta=1}^{m-1}
(m-\Delta)\,
\#\{u:u\mid \Delta R,\ (\Delta R/u)\equiv0\pmod2\}.
\tag{GUD-4}
\]

若忽略偶性条件，则有更粗但完全显式的上界

\[
\#\mathcal R_{\rm geo}(m)
\le
\sum_{\Delta=1}^{m-1}(m-\Delta)\tau(\Delta R).
\tag{GUD-5}
\]

同时，对任一几何 group，

\[
\Omega(E)
\le
1+
\left\lfloor
{\beta L_{\max}\over u_E}
\right\rfloor ,
\qquad
L_{\max}=\max_{m\in M}|I_m|.
\tag{GUD-6}
\]

故有确定性 envelope 总量上界

\[
\sum_{E\in \mathcal G_{\rm fail}}\Omega(E)
\le
\sum_{m\in M}
\sum_{\Delta=1}^{m-1}
(m-\Delta)
\sum_{\substack{u\mid \Delta R\\ \Delta R/u\ {\rm even}}}
\left(1+\left\lfloor{\beta L_{\max}\over u}\right\rfloor\right).
\tag{GUD-7}
\]

**引理 GUD-1（失败 group 的纯几何支配）。**  
`C13Failure` 的 group 数、`u` 分布和 `Omega` 总量均由 `(GUD-4)--(GUD-7)` 支配，不依赖实际
尾素对 witness 的位置。

**证明。**  
每个 `C13Failure` 必先来自某个固定点位差 `Delta` 与除数分解 `Delta R=gu`，且满足偶 gap
与非空 q 区间条件。因此它属于 `GeometricCandidate`。每条几何记录至多生成一个
`(shape,epsilon,side)` group，去重只会减少数量；对每个 group 应用 `(GUD-6)` 并求和，即得
`(GUD-7)`。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_group_u_distribution.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_group_u_distribution.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --eta 0.04 \
  --slack-cut 40 --format table
```

输出摘要：

```text
mode       records groups deterministic_env capacity
geometric  612     402    68241             5459.28
positive   167     105    48380             3870.40
narrow     131      83    39750             3180.00
failure     57      38    24641             1971.28
```

`failure` 层的 `u` 分布为：

```text
u=1 : 21 groups, 21359 slots；
u=2 :  8 groups,  2085 slots；
u=3 :  9 groups,  1197 slots。
```

而纯几何上界层为：

```text
u=1 : 30 groups, 25770 slots；
u=2 : 30 groups, 12900 slots；
u=3 : 30 groups,  8590 slots；
u=6 : 30 groups,  4300 slots；
u=9 : 30 groups,  2870 slots；
u=18: 30 groups,  1440 slots。
```

这说明样本中真实失败 group 已被一个完全几何的 `u` 分布外壳覆盖，后续全局论证可只处理
`(GUD-7)` 的除数和，而不再引用实际 witness group 数。

## 4. 对主链的影响

SparseSAE 付款链现在变成：

```text
C13Failure groups
=> geometric divisor envelope G_geo
=> deterministic u-distribution sum
=> |M|*eta*sum Omega payment。
```

当前仍未闭合的是：

```text
把 (GUD-7) 对全局目标窗口族求和；
证明其乘 |M|*eta 后小于 C13 主链预算；
或进一步用 slack/positive 层把 geometric 外壳压小。
```

## 5. 审稿边界

已完成：

```text
失败 group 到纯几何候选 group 的嵌套证明；
group 数与 u 分布的除数和上界；
样本中 geometric/positive/narrow/failure 四层审计。
```

仍未完成：

```text
全局窗口族上的 (GUD-7) 求和常数；
几何外壳付款与最终预算的常数对接；
HighDensityEnvelope 有限验证的完整目标族清单。
```

所以本文完成的是 group/u 分布的确定性上界接口，不是行命题最终闭合。
