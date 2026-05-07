# Triad-A1 Lift-C：无限塔删除-熵二分

**状态：** `infinite_tower_deletion_entropy_dichotomy_proved_terminal_bounds_open`

本文承接 `Lift-A` fiber 删除恒等式与 `Lift-B` 投影单调性。现在攻下一硬点：如果素数轮筛结构必须无限升层，
是否会重新变成“无穷缠绕、无法闭合”的逃逸？

结论是：不会。沿同一个全周期完成集合 `C_P` 的投影塔，升层只能落入两类极限：

```text
删除势发散  => 支撑密度趋零；
删除势可求和 => NoDeletion，随后进入 KL/PDEC 或 CleanKLS。
```

这一步仍不是最终行命题证明，但它把“无穷层叠”变成了一个可审计的极限账本。

## 1. 投影塔

固定 `P`，令

```text
B_P=prod_{ell<P} ell；
C_P subset Z/B_P Z 为全周期完成集合；
Q_0 | Q_1 | Q_2 | ... | B_P；
A_n = pi_{Q_n}(C_P) = supp(M_{Q_n})。
```

记

```text
Q_{n+1}=r_n Q_n。
```

对每个 `t in A_n` 定义 fiber 幸存数

```text
s_n(t)=#{b in [0,r_n): t+bQ_n in A_{n+1}}。
```

由投影单调性，`A_{n+1}` 不会投到 `A_n` 外，所以：

\[
|A_{n+1}|=\sum_{t\in A_n}s_n(t).
\tag{ITD-1}
\]

定义平均幸存率：

\[
a_n={1\over |A_n|}\sum_{t\in A_n}{s_n(t)\over r_n}.
\tag{ITD-2}
\]

则密度满足精确乘法公式：

\[
\delta_{n+1}=\delta_n a_n,\qquad
\delta_N=\delta_0\prod_{n<N}a_n.
\tag{ITD-3}
\]

## 2. 删除势

定义删除势：

\[
D_n=-\log a_n\ge 0.
\tag{ITD-4}
\]

于是

\[
\delta_N=\delta_0\exp\left(-\sum_{n<N}D_n\right).
\tag{ITD-5}
\]

因此有严格二分：

```text
sum D_n = infinity
  => delta_N -> 0；

sum D_n < infinity
  => D_n -> 0, a_n -> 1。
```

第一支是 `FiberDeletion` 极限闭合：若坏窗支撑必须在所有新层继续存活，而支撑密度趋零，则任何正比例
PDEC 责任无法停留在这个塔上，只能退回 Sparse/LocalSurvivor 或已有 PDEC/Column/SAE 出口。

## 3. NoDeletion 分支

若 `sum D_n<infinity`，则 `a_n->1`。这意味着大多数活跃旧相位的 fiber 几乎全保留：

```text
s_n(t)/r_n -> 1  在平均意义下成立。
```

删除不再提供结构压力，此时只能看 fiber 条件分布。令正式坏窗质量在 fiber 上的条件分布为

```text
p_{n,t}(b)。
```

以均匀或结构基准 `mu_{n,t}(b)` 为参考，定义 KL 成本：

\[
H_n=\sum_{t\in A_n}{g_n(t)\over M}
\sum_b p_{n,t}(b)\log {p_{n,t}(b)\over \mu_{n,t}(b)}.
\tag{ITD-6}
\]

此时只有两支：

```text
sum H_n = infinity
  => fiber 偏斜持续累计，形成 profinite/new-layer PDEC；

sum H_n < infinity
  => 新层条件偏斜趋零，进入高维平坦 CleanKLS/DLS。
```

这与 `prime-matrix-newlayer-pdec-tower-entropy-contract.md` 一致，但本文补上了删除势前置：先用
`D_n` 判定支撑是否被无限剥离；只有剥离不够时才进入 KL 熵账。

## 4. 不能无穷无名循环

沿 LHB `M_Q` 同口径投影塔，`ProjectionStitching` 已被 `Lift-B` 消掉。因此无限升层没有第五出口：

```text
1. sum D_n = infinity
   => 支撑密度趋零，回到 Sparse/LocalSurvivor/容量矛盾；

2. sum D_n < infinity and sum H_n = infinity
   => new-layer/profinite PDEC；

3. sum D_n < infinity and sum H_n < infinity
   => CleanKLS/DLS；

4. 若 formal unit 换口径
   => 不属于同一 C_P 塔，回到 Multiplicity-Stitching 吸收合同。
```

因此“素数规律无穷迭代、无穷层叠”可以存在，但每层都必须支付 `D_n` 删除成本或 `H_n` 信息成本；
若两者都不支付，就只剩平坦高维分散。

## 5. 有限预算证据

新增脚本：

```text
experiments/prime_matrix_triad_a1_infinite_tower_budget.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-infinite-tower-budget.md/json
```

已物化塔预算：

| P | layers | Q start | Q end | product survival | product drop | deletion potential |
|---:|---:|---:|---:|---:|---:|---:|
| 17 | 1 | 2310 | 30030 | 0.0769231 | 13 | 2.56495 |
| 19 | 2 | 2310 | 510510 | 0.016031 | 62.379 | 4.13323 |
| 23 | 2 | 2310 | 510510 | 0.0505539 | 19.7809 | 2.98472 |
| 29 | 1 | 2310 | 30030 | 0.312821 | 3.19672 | 1.16213 |

特别是 `P=19,23` 已连续两层强删除：

```text
P=19: density drop 62.379；
P=23: density drop 19.7809。
```

这些数据不是全局证明，只是验证 `(ITD-3)` 的当前层账本确实处于删除分支。

## 6. 对行命题主线的意义

此前固定 `Q` 密度屏障说明：不能停在一个低模层靠普通 Fourier cap 闭合。现在无限塔二分说明：

```text
持续升层也不能无名逃逸。
```

若持续升层总是删除，则坏窗支撑被剥到零密度；若删除停止，则必须在新增素因子 fiber 上留下偏斜，
偏斜累计就是 PDEC；若没有偏斜，就是 CleanKLS 平坦残差。

因此当前 Triad-A1 的剩余硬点不再是“如何描述无穷素数规律”，而是更窄的二选一证明：

```text
Deletion divergence；
或 NoDeletion 下的 KL/PDEC vs CleanKLS 终端证书。
```

## 7. 闭合边界

本文完成：

```text
无限投影塔的密度乘法公式；
删除势发散 => 支撑密度趋零；
删除势可求和 => NoDeletion；
NoDeletion => KL/PDEC 或 CleanKLS；
两层有限预算审计。
```

本文未完成：

```text
证明任意最小反例族必有 sum D_n = infinity；
或在 sum D_n < infinity 时完成 H_n 分支的 PDEC/CleanKLS 终端排斥；
把 Sparse/LocalSurvivor 与最终行命题完全接合。
```

所以当前目标继续压缩为 `NoDeletion-KL`：若支撑不再被删除，证明坏窗质量不能在所有新增素因子层上同时
保持低 KL 且仍承担正比例行覆盖责任。

## 8. Lift-D 接入

新增 `prime-matrix-triad-a1-nodeletion-kl-dichotomy.md` 后，本文最后留下的 `NoDeletion-KL` 已被写成
正式门控：

```text
cap excess over baseline => positive KL cost；
sum KL = infinity        => new-layer/profinite PDEC；
sum KL < infinity        => CleanKLS/DLS admission。
```

同步新增 `experiments/prime_matrix_triad_a1_nodeletion_kl_gate.py`，当前两层审计给出：

```text
gate_counts={'FiberDeletion': 6}；
current_nodeletion_triggered=False。
```

因此当前已物化层仍在删除分支；`NoDeletion-KL` 是未来删除停止时的强制路由，不是新的开放出口。

## 9. TopPrimePromotion 接入

新增 `prime-matrix-triad-a1-topprime-promotion-gate.md/json` 与
`prime-matrix-triad-a1-recursive-promotion-dichotomy.md` 后，删除势塔获得了一个新的入口：

```text
PersistentCap top-prime payment persists
=> top prime is next new prime
=> promote Q to rQ
=> fiber deletion gate。
```

当前 `Q=2310` 层：

```text
cap_count=68；
all_top_prime_is_next_high_prime=True；
promotion_class_counts={PromotionFiberDeletion:68}。
```

所以 top-prime 持久支付不会绕开本文的删除势二分；它正是触发下一层 `Q_{n+1}=r_n Q_n`
的结构机制。若这种机制无限持续，则删除势按本文第 2 节累积；若某层不再删除，则进入
NoDeletion-KL / CleanKLS；若某层转为固定 residue 或 column 签名，则回到 PDEC。

## 10. 晋升删除势账本

新增 `prime-matrix-triad-a1-promotion-deletion-potential-ledger.md/json` 后，TopPrimePromotion
已经直接写入本文的势函数：

```text
D_n=-log(a_n)。
```

当前晋升层：

```text
cap_count=68；
all_positive_deletion_potential=True；
global_min_deletion_potential_current_layer=0.8800788718999966。
```

该数值只是当前层读数，不是全局常数。全局使用方式是：

```text
沿晋升塔逐层登记 D_n；
若 D_n 累加发散，走删除势闭合；
若 D_n 可求和，则 a_n->1，正好触发本文 NoDeletion-KL 二分。
```

因此“晋升但删除越来越弱”的情况也不是新出口；它自动转换成 NoDeletion。
