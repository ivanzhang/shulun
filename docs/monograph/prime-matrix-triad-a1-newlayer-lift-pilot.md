# Triad-A1 新层提升试验：从 Q=2310 到 Q=30030

**状态：** `newlayer_lift_pilot_supports_entropy_route_not_proof`

本文承接 `prime-matrix-triad-a1-fixed-q-density-barrier.md`。固定 `Q` 密度屏障说明：

```text
当 supp(M_Q) 在固定相位层变稠时，普通正密度方向支撑必然 Persistent。
```

这不是终点，而是提示必须升到新层 `Q'=rQ`。本文用 `Q=30030=13*2310` 的小范围试验验证：
加入新素因子层后，相位纤维被细分，`supp(M)` 在新层上重新变稀疏。

## 1. 试验文件

本轮生成了独立试验产物：

```text
prime-matrix-triad-a1-q30030-column-phase-blocks.md/json；
prime-matrix-triad-a1-q30030-multiplicity-cap.md/json；
prime-matrix-triad-a1-q30030-lp-skeleton.md/json；
prime-matrix-triad-a1-q30030-direction-support-audit.md/json。
```

这些文件只覆盖：

```text
Q=30030；
P in {17,19,23,29}。
```

它们是有限试验与接口验证，不是全局证明。

## 2. 支撑密度对比

同一 `P` 在 `Q=2310` 与 `Q=30030` 下的 `supp(M)` 密度为：

| P | density Q=2310 | density Q=30030 | drop factor |
|---:|---:|---:|---:|
| 17 | 0.012121 | 0.000932 | 13.00 |
| 19 | 0.060606 | 0.012254 | 4.95 |
| 23 | 0.100433 | 0.031169 | 3.22 |
| 29 | 0.064935 | 0.020313 | 3.20 |

具体计数：

| P | nonzero M Q=2310 | nonzero M Q=30030 | zero M Q=30030 |
|---:|---:|---:|---:|
| 17 | 28 | 28 | 30002 |
| 19 | 140 | 368 | 29662 |
| 23 | 232 | 936 | 29094 |
| 29 | 150 | 610 | 29420 |

虽然新层相位总数扩大 `13` 倍，非零支撑没有按 `13` 倍膨胀；因此密度明显下降。

## 3. 零块方向仍闭合

`prime-matrix-triad-a1-q30030-direction-support-audit.md` 验证默认方向支撑

```text
C_F = WHOLEDEF union BRIDGED
```

在全部试验 `P` 上仍为：

```text
EmptyCap。
```

也就是说，零容量块支撑方向不仅在 `Q=2310` 闭合，在提升到 `Q=30030` 后仍闭合。

## 4. 结构解释

提升 `Q -> rQ` 时，旧相位 `t mod Q` 被拆成 `r` 个新纤维：

\[
t' \equiv t \pmod Q,\qquad t'\bmod r。
\]

若新增素因子 `r` 提供真实新约束，则允许完成的纤维不会均匀填满全部 `r` 个分支，`supp(M_{rQ})`
密度下降。若新增层没有提供新信息，则密度不降，偏斜成本进入 `new-layer entropy` 账本。

因此升层分支有二分：

```text
new layer re-sparsifies:
  回到 Empty/Sparse/更细 PDEC 支撑审计；

new layer does not re-sparsify:
  新层条件分布接近均匀，进入 CleanKLS/DLS；
  或偏斜持续累计，形成 profinite/new-layer PDEC。
```

这正是 `prime-matrix-newlayer-pdec-tower-entropy-contract.md` 的局部可计算版本。

## 5. 对固定 Q 屏障的回应

固定 `Q` 密度屏障排除了“停在同一层靠正密度 Fourier cap 闭合”的路线；本试验显示正确动作不是放弃，
而是：

```text
提升新素因子层；
重新检查 supp(M) 的稀疏性；
若仍持久，则继续升层或转 column/tail/CleanKLS。
```

这符合“素数规律无穷迭代、无穷层叠”的结构图景：每个固定层只能提供有限分辨率，证明必须允许层级提升，
并用熵/能量账本防止无穷无效循环。

## 6. 下一步硬点

下一步应把本试验从小范围推进到证书接口：

```text
Lift-A:
  证明 Q -> rQ 后 supp(M) 密度下降的符号条件；

Lift-B:
  若密度不降，输出新增层 fiber 偏斜并进入 new-layer PDEC；

Lift-C:
  若新增层偏斜可求和，转入 CleanKLS/DLS。
```

当前最可攻的是 `Lift-A`：把 `M_{rQ}(t,b)` 的 fiber 完成数写成旧相位完成集合上的新增素因子筛除，
给出可验证的 fiber deletion inequality。

## 7. 结论

本轮新发现：

```text
固定 Q 方向支撑有密度屏障；
提升到 Q=30030 后，小范围 supp(M) 明显重新稀疏；
零块方向支撑仍 EmptyCap；
下一硬点是把“新层重新稀疏或熵累计”写成一般 fiber 定理。
```

这推进了 A1-LHB 从固定层 LP 问题到 new-layer 递归结构问题。

## 8. Lift-A 后续落地

新增 `prime-matrix-triad-a1-newlayer-fiber-deletion-lemma.md` 后，本文的试验读数已被整理成一般门控：

```text
Q'=rQ；
|supp(M_Q')| = sum_{t in supp(M_Q)} s(t) + |N|；
若 N=empty 且平均 s(t)/r<1，则新层按精确恒等式重新稀疏。
```

同步新增机器审计：

```text
prime_matrix_triad_a1_newlayer_fiber_audit.py；
prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.md/json。
```

在 `P={17,19,23,29}` 上审计得到 `N=empty`，密度下降完全来自 fiber 删除账本。

随后小范围继续提升到 `Q=510510=17*30030`：

```text
P={19,23}；
30030 -> 510510 仍为 FiberDeletionLayer；
min density drop = 6.13889；
默认 WHOLEDEF/BRIDGED 方向仍 EmptyCap。
```

新增 `prime-matrix-triad-a1-newlayer-projection-monotonicity-lemma.md` 进一步说明：对同一个全周期完成集合
`C_P` 的投影，`N=empty` 是一般投影单调性，而不是实验偶然。
