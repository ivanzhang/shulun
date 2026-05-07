# SN3-B 真分散残余目标：低模剥离后的高频吸收接口

**状态：** `sn3b_true_distributed_residual_target_not_closed`

本文接续 `SN3-A 中心化低模回流证书`。SN3-A 已把中心化低模峰命名为 `PDEC/ColumnCRT` 并剥离。SN3-B 只处理剩余部分：

```text
低维中心化峰都低；
短 q 窗、qmod、dmod 都不能单独解释正超额；
仍需支付 SN-2 正带责任的高频残余。
```

## 1. 残余对象

对 SN-3 正带 `J`，令

```text
E_J=A_J-M_J>0。
```

取阈值 `theta`。若 SN3-A 命中中心化低模桶 `beta*`，定义残余：

```text
E_J^{res}=max(0,E_J-E_{beta*})。
```

若 SN3-A 未命中，且所有低维峰都低于 `theta E_J`，定义：

```text
E_J^{res}=E_J。
```

真分散族为

```text
D_true(theta)={
  J: q 短窗、qmod、dmod 中心化峰均 < theta E_J
}
```

加上 SN3-A 回流带剥离后的正残余。

## 2. SN3-B 目标不等式

SN3-B 的正式目标不是固定常数，而是行内残余吸收：

```text
sum_{J in D_true} E_J^{res} <= U_true(P,y;Y,B,W,L,theta),
```

并要求

```text
U_true + NamedLowModMass + SAE/Cofactor budgets < R(P,y)
```

或等价地：在已把命名低模峰交给 `PDEC/ColumnCRT` 后，剩余高频残余不能单独支付零行所需余量。

若该不等式失败，由对偶大筛/dispersion 逻辑，失败必须产生：

```text
新的短 q 窗局部化       => SAE；
新的低模 Fourier 峰     => PDEC；
新的列位移同步          => ColumnCRT；
高频双线性相关          => KLS/dispersion 缺陷输入。
```

因此 SN3-B 仍保持“失败即命名出口”，不是统计逼近。

## 3. 当前残余审计

配套脚本：

```text
experiments/prime_matrix_sn3b_true_distributed_residual_audit.py
```

当前报告：

```text
docs/sn3b_true_distributed_residual_audit_20260506.md
docs/sn3b_true_distributed_residual_audit_20260506.json
```

从原 SN-3 分散候选出发：

```text
original_distributed_excess = 561.852711
```

SN3-A 剥离后：

```text
effective_unresolved_after_sn3a = 440.889774
removed_by_sn3a = 120.962937
removed_share = 0.215293
```

残余来源：

```text
true_distributed = 24
lowmod_residual = 8
```

最紧指标：

```text
max_row_effective_unresolved_over_required = 0.187188
max_candidate_unresolved_over_required = 0.132524
max_true_low_projection_peak = 0.746970
```

最紧行是：

```text
P=10007, y=75:
  effective/R = 0.187188,
  effective E = 24.763520,
  true bands = 2,
  lowmod residual = 0。
```

这说明下一步高频吸收要优先攻击的是少数同一行多真分散带的叠加，而不是低模回流残余。

## 4. 结构含义

SN3-B 的残余满足三重排斥条件：

```text
无短 q 窗承担 theta 比例；
无 q mod W 中心化桶承担 theta 比例；
无 d mod W 中心化桶承担 theta 比例。
```

因此若残余仍能支付 `R(P,y)`，它必须依赖跨多个窗口、多个单位类、多个列位移的高频同步。这个同步不是低模轮筛规律，必须表现为双线性/dispersion 型相关：

```text
sum_{m in rough band} sum_{q in I_m} (1_qprime - model) F(m,q)
```

其中 `F` 与低维字典近似正交。

## 5. 下一硬点

SN3-B 的真正闭合口是：

```text
TrueDistributedDLS/KLS:
  对所有满足低维峰排斥的残余权重 F，
  证明 <e,F> 小于行内剩余余量；
  若失败，则给出非零高频证书并回流 SAE/PDEC/ColumnCRT/KLS。
```

当前审计不能替代该定理，但它把最窄攻击目标定位为：

```text
P=10007,y=75 的双真分散带叠加；
以及所有 max low projection peak 接近 theta 的临界残余。
```

## 6. SN3-C：多带同步再分裂

新增 `prime-matrix-sn3c-multiband-sync-split.md` 与
`experiments/prime_matrix_sn3c_multiband_sync_audit.py` 后，多真分散带叠加被进一步分成：

```text
ShellOverlap        => SAE；
LowModSync          => PDEC/ColumnCRT；
KLS-Multishell      => 高频多壳输入。
```

审计结果：

```text
multi_true_row_count = 3
pair_count = 3
pair_route_counts = {
  kls_multishell_candidate: 2,
  lowmod_multiband_sync_candidate: 1
}
```

最紧 `P=10007,y=75` 的两带为：

```text
[4y,8y): q=[1237,2444], E/R=0.120145
[1y,2y): q=[4970,9500], E/R=0.067043
q shell gap = 2525
q-window cosine = 0
max lowmod cosine = 0.432620
route = KLS-Multishell。
```

所以 SN3-B 的当前最窄硬点已经不是“多带叠加”本身，而是 `KLS-Multishell`：相互分离的 q 壳在无低模同步时是否仍能同向产生足够正偏；若能，则必须给出高频非零相位证书。
