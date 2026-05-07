# Triad-A1 Lift-D 后终端归约

**状态：** `a1_newlayer_reduced_to_deletion_or_terminal_triad_not_closed`

本文把 `Lift-A/B/C/D` 的结果接入终端三证书合同。目标是防止论证再次分散到“无穷层叠但无名”的状态。

当前结论：

```text
Triad-A1 new-layer 分支
=> FiberDeletion 删除势账本
   or PDEC family
   or CleanKLS/DLS
   or formal-unit gap 回到 Stitching。
```

在 LHB 同一 `C_P` 口径内，formal-unit gap 已由投影单调性消除；因此实际剩余为：

```text
DeletionPotential divergence；
NoDeletion-PDEC；
NoDeletion-CleanKLS。
```

## 1. 已闭合的无名出口

### 1.1 固定 Q 方向支撑屏障

固定 `Q` 上若 `supp(M_Q)` 变稠，则任意正密度方向支撑都会 persistent：

```text
|A cap C| >= |A|+|C|-Q。
```

所以不能继续停在一个固定低模层找全局常数。

### 1.2 升层投影口径

沿同一全周期完成集合

```text
C_P subset Z/B_P Z
```

有：

```text
pi(supp(M_Q')) subset supp(M_Q)。
```

因此 Lift-A 中的 `N` 项在 LHB 同口径分支内为零，升层不是 Stitching 逃逸。

### 1.3 无限塔无名循环

定义每层平均幸存率 `a_n` 和删除势 `D_n=-log a_n`：

```text
density(A_N)=density(A_0)*product a_n。
```

若 `sum D_n=infinity`，支撑密度趋零。若 `sum D_n<infinity`，则 `a_n->1`，进入 NoDeletion。

### 1.4 NoDeletion 无名循环

NoDeletion 下定义 fiber 条件分布 KL：

```text
H_n=sum_t g_n(t)/M * KL(p_{n,t} || mu_{n,t})。
```

若 `sum H_n=infinity`，偏斜累计为 new-layer/profinite PDEC；若 `sum H_n<infinity`，新增层趋平，
进入 CleanKLS/DLS admission。

## 2. 当前机器路由

新增 `experiments/prime_matrix_triad_a1_terminal_router.py` 后，当前已物化层全部路由为：

```text
route_counts={'LiftFiberDeletion': 6}
triad_counts={'ContinueLiftOrSparse': 6}
current_terminal_claim=current_layers_all_deleting。
```

这表示当前没有可提交的 PDEC/CleanKLS 实例；所有已物化层仍在删除势账本中推进。

关键有限读数：

```text
P=19: 2310->510510 product survival 0.016031, deletion potential 4.13323；
P=23: 2310->510510 product survival 0.0505539, deletion potential 2.98472。
```

## 3. 归约定理

**A1 NewLayer Terminal Reduction.**
在 LHB attachment 与同一 `C_P` 投影口径成立时，任意 Triad-A1 new-layer 分支满足以下之一：

```text
1. 删除势发散：
   支撑密度趋零，进入 Sparse/LocalSurvivor 或容量矛盾；

2. 删除势可求和且 KL 发散：
   形成 new-layer/profinite PDEC；

3. 删除势可求和且 KL 可求和：
   满足 CleanKLS/DLS admission，或 admission 失败回流 PDEC/SAE/Column/Tail；

4. formal unit 口径改变：
   不属于同一 LHB C_P 分支，回到 Multiplicity-Stitching 吸收。
```

因此在当前 LHB `M_Q` 分支内，没有第五类出口。

## 4. 对最终行命题的剩余义务

这一步没有完成全局行命题。它把剩余证明压成三类证书全集：

```text
DeletionPotential:
  证明最小反例族的删除势必发散，或在有限层降到 LocalSurvivor/容量矛盾；

PDEC family:
  对 new-layer/profinite/weighted/primitive/displacement/cofactor 等实例提交 U_CRT<L_PDEC；

CleanKLS/DLS:
  对 KL 可求和的平坦残余提交 admission 与大筛证书。
```

当前最可攻的下一硬点是 `DeletionPotential`：尝试证明若每个新增素因子层都来自真实轮筛禁止类，
则 `a_n` 不可能长期过近于 `1`，否则 `C_P` 在无限新增素因子上会逼近乘积满纤维，从而与覆盖需要的
小素因子选择约束冲突。若该路线失败，失败本身应输出 NoDeletion 层并进入 PDEC/CleanKLS。

新增 `prime-matrix-triad-a1-deletion-potential-essentiality.md` 后，这个目标被进一步细化：

```text
promoted prime r 的 residue choice 若不命中旧洞，当前大多死亡；
所以删除势来自 r 必须命中旧洞的必要性。
```

当前两层审计中，zero-cover residue 的幸存率约为：

```text
0, 0.062016, 0.112628, 0.058824, 0.023066, 0.054514。
```

因此下一硬点应攻 `TailIndependentCompletion`：

```text
若 Tail_{>r} 能长期在 zero-cover residue 上完成旧洞集，
则进入 NoDeletion-KL；
否则 zero-cover 大量死亡给出删除势。
```

## 5. 当前边界

本文完成：

```text
Lift-A/B/C/D 到终端三证书的路由归约；
当前有限层全部处于 FiberDeletion 的机器验证；
无穷层叠无名出口的删除。
```

本文未完成：

```text
删除势发散定理；
PDEC 证书全集；
CleanKLS/DLS 证书全集；
LocalSurvivor 与最终行命题的完全拼接。
```

所以后续应继续攻 `DeletionPotential`，而不是回到固定模常数或经验统计。
