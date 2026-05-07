# Triad-A1 Lift-A：新层 fiber 删除引理

**状态：** `fiber_deletion_identity_proved_global_closure_open`

本文把 `prime-matrix-triad-a1-newlayer-lift-pilot.md` 中的升层直觉压成一个一般结构引理。核心目标不是再找固定常数，
而是给出可持续迭代的三分出口：

```text
真实 fiber 删除      => 新层重新稀疏；
fiber 近均匀不删除   => CleanKLS/DLS；
旧零相位新增激活     => Stitching/坐标商/复用缺陷吸收。
```

这正是固定 `Q` 密度屏障之后的递归剥离机制。

## 1. 设置

令

```text
Q' = rQ,   pi: Z/Q'Z -> Z/QZ。
```

旧层完成容量支撑为

```text
A_Q = {t mod Q : M_Q(t)>0}。
```

新层完成容量支撑为

```text
A_Q' = {u mod Q' : M_Q'(u)>0}。
```

对每个旧相位 `t`，其新层 fiber 是

```text
pi^{-1}(t) = {t+bQ : 0<=b<r}。
```

定义幸存 fiber 数

```text
s(t)=#{b : M_Q'(t+bQ)>0}。
```

再定义旧零相位新增激活集合

```text
N = A_Q' \ pi^{-1}(A_Q)。
```

`N` 是关键口径检查：若 `N` 非空，则新层容量不是旧层容量的单纯细化，必须先进入 Stitching/坐标商归一化。

## 2. 精确恒等式

对任意 `Q' = rQ` 都有：

\[
|A_{Q'}|
=
\sum_{t\in A_Q}s(t)+|N|.
\tag{LFD-1}
\]

证明只需按投影 `pi` 分解 `A_Q'`。落在 `pi^{-1}(A_Q)` 内的点按旧相位 fiber 计数，落在其外的点正是 `N`。

除以 `Q'=rQ`，得密度恒等式：

\[
\delta_{Q'}
=
\delta_Q\cdot {1\over |A_Q|}\sum_{t\in A_Q}{s(t)\over r}
 + {|N|\over rQ}.
\tag{LFD-2}
\]

这条公式是结构恒等式，不是概率估计。

## 3. 删除引理

若新层是旧层的单调细化，即

```text
N=empty，
```

并且存在删除量

\[
\sum_{t\in A_Q}(r-s(t))\ge \eta r |A_Q|,
\tag{LFD-3}
\]

则

\[
\delta_{Q'}\le (1-\eta)\delta_Q.
\tag{LFD-4}
\]

这就是 `Lift-A` 的硬核：不需要固定全局常数，只要每次升层能证明一个正删除账本，支撑密度就按可迭代恒等式下降。

## 4. 熵二分

若 `(LFD-3)` 失败，即多数活跃旧相位几乎保留全部 fiber，则新层没有提供足够删除。此时看 fiber 条件分布：

```text
p_t(b)=M_Q'(t+bQ) / sum_b M_Q'(t+bQ)。
```

相对均匀分布 `mu(b)=1/r` 的 KL 成本为

\[
D(p_t||\mu)=\log r-H(p_t).
\tag{LFD-5}
\]

于是出现二分：

```text
KL 在正质量上持续偏大
  => 新层偏斜累计，形成 refined/new-layer PDEC；

KL 趋零且 fiber 近均匀
  => 新层只剩高维分散，进入 CleanKLS/DLS。
```

这与 `prime-matrix-newlayer-pdec-tower-entropy-contract.md` 完全一致：无穷层叠允许存在，但每层若要帮助覆盖，必须支付可累计的信息成本。

## 5. 旧零相位新增激活

若 `N` 非空，不能直接使用删除引理。此时说明 `M_Q` 与 `M_Q'` 的口径不是单纯 quotient/fiber 关系，必须证明以下三者之一：

```text
ProjectionCompatibility:
  修正旧层定义，使 pi(A_Q') subset A_Q；

CoordinateQuotient:
  说明新增激活来自坐标投影改变，转入 primitive/physical PDEC 或 CleanKLS；

ReuseDefect:
  说明新增激活来自补洞变量复用，转入 ColumnCRT/SAE/TailAnchor/CofactorAnchor。
```

所以 `N` 也不是新出口；它是 Multiplicity-Stitching 的触发器。

新增 `prime-matrix-triad-a1-newlayer-projection-monotonicity-lemma.md` 后，对当前 LHB allowed-set 的
`M_Q(t)` 支撑，这个坏项已经被进一步压掉：若 `Q|Q'|B_P` 且两层都来自同一个全周期完成集合 `C_P`，
则

```text
pi(supp(M_Q')) subset supp(M_Q)，即 N=empty。
```

因此在同一 `C_P` 口径的 LHB 分支内，升层门控可简化为：

```text
FiberDeletion or NoDeletion；
NoDeletion => new-layer PDEC entropy or CleanKLS。
```

## 6. 已物化升层审计

新增审计与塔汇总文件：

```text
experiments/prime_matrix_triad_a1_newlayer_fiber_audit.py
docs/monograph/prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.md/json
docs/monograph/prime-matrix-triad-a1-newlayer-fiber-audit-q30030-q510510.md/json
experiments/prime_matrix_triad_a1_newlayer_tower_gate.py
docs/monograph/prime-matrix-triad-a1-newlayer-tower-gate.md/json
```

第一层机器结果：

| P | old support | lifted support | survival | deletion | density drop | fiber shape |
|---:|---:|---:|---:|---:|---:|---|
| 17 | 28 | 28 | 0.076923 | 0.923077 | 13.000 | `{1: 28}` |
| 19 | 140 | 368 | 0.202198 | 0.797802 | 4.94565 | `{2: 132, 13: 8}` |
| 23 | 232 | 936 | 0.310345 | 0.689655 | 3.22222 | `{3: 208, 13: 24}` |
| 29 | 150 | 610 | 0.312821 | 0.687179 | 3.19672 | `{1: 20, 3: 2, 4: 120, 13: 8}` |

共同结论：

```text
all_support_identities_hold=True；
all_monotone_lift_support=True；
all_classified_resparse=True。
```

因此本次提升的密度下降不是统计拟合，而是 `N=empty` 下的 `(LFD-2)` 精确核算。

第二层 `30030 -> 510510` 的小范围复核：

| P | old support | lifted support | survival | deletion | density drop | fiber shape |
|---:|---:|---:|---:|---:|---:|---|
| 19 | 368 | 496 | 0.079284 | 0.920716 | 12.6129 | `{1: 360, 17: 8}` |
| 23 | 936 | 2592 | 0.162896 | 0.837104 | 6.13889 | `{2: 888, 17: 48}` |

两层塔汇总均为：

```text
FiberDeletionLayer。
```

## 7. 对行命题主线的作用

固定层 `Q` 上，`supp(M_Q)` 变稠后会触发方向支撑密度屏障；继续在同一层寻找固定 Fourier cap 没有全局前途。
Lift-A 给出正确的递归动作：

```text
升到 Q'=rQ；
检查 pi(A_Q') 是否仍落在 A_Q；
核算 fiber 删除量；
若删除足够，回到稀疏/局部证书；
若删除不足，按 KL 熵进入 PDEC 或 CleanKLS；
若投影不兼容，进入 Stitching 吸收。
```

这是一条一般结构链，不依赖某个固定区段或固定常数。它把“素数在逐层轮筛中的无穷缠绕”转化成：

```text
每一层要么删除支撑；
要么留下可累计偏斜；
要么趋于高维平坦；
要么暴露口径不一致。
```

## 8. 闭合边界

本文完成：

```text
Q -> rQ fiber 删除恒等式；
单调细化时的密度下降引理；
非删除时的熵/PDEC/CleanKLS 二分；
Q=2310 -> 30030 -> 510510 的机器证据。
```

仍未完成：

```text
对任意后继轮筛层证明 N=empty 或给出 Stitching 证书；
对任意最小反例族证明删除量、KL 偏斜、CleanKLS 三者必有一个可闭合；
Triad-A1 的最终 U_CRT<L_PDEC 对偶证书全集。
```

所以当前推进不是最终无条件闭合，而是把 `Lift-A` 从经验升层变成了可迭代的结构门控。
