# Triad-A1 PDEC DualCap 路由

**状态：** `pdec_dualcap_route_materialized_terminal_open`

本文继续攻击真正终端硬点 `PDEC family U_CRT<L_PDEC`。当前还不能提交完整 `U_CRT<L_PDEC` 证书；但已经把固定 `Q=2310` 的对偶失败形态物化为 `DualCap` 账本。

核心目标：

```text
PDEC 上界失败不能停在 DualGap；
必须输出具体 Fourier/Bohr cap 相位块；
该 cap 必须路由到 LocalSurvivor、refined PDEC、column/tail 行、升层或 CleanKLS。
```

## 1. DualCap 对象

在 LHB 分支中已有：

```text
g(t)<=M(t)；
supp(g) subset supp(M)。
```

若某个非零频率方向的对偶上界失败，则由 PDEC dual-failure 合同，质量必须集中在某个方向帽：

```text
C_{h,alpha,dir}={t: cos(2*pi*h*t/Q+dir)>=alpha}。
```

因此合法失败对象是：

```text
DualCap = C_{h,alpha,dir} cap supp(M)。
```

它必须携带：

```text
h, alpha, direction；
cap size；
intersection size；
intersection mass；
density-barrier lower bound；
route。
```

## 2. 路由规则

```text
EmptyCap:
  当前方向在 LHB 分支闭合；

SparseCap:
  进入 LocalSurvivor 或 explicit finite PDEC；

PersistentCap:
  进入 refined PDEC、column/tail 相位兼容行；

ForcedPersistentByDensityBarrier:
  固定 Q 投影太稠导致任何正密度 cap 都持久；
  不能同层循环，必须升层、加 column/tail 行或进入 CleanKLS。
```

这与 `PDEC cap no-cycle` 一致：固定签名层内 cap 只能有限细化；若必须升层，就进入 new-layer PDEC/CleanKLS 账本。

## 3. 当前审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_pdec_dualcap_extractor.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-pdec-dualcap-extractor.md/json
```

汇总：

```text
aggregate_class_counts={
  'SparseCap': 16,
  'PersistentCap': 68,
  'ForcedPersistentByDensityBarrier': 24
}

aggregate_route_counts={
  'LocalSurvivorOrExplicitPDEC': 16,
  'RefinedPDECOrColumnTailRows': 68,
  'LiftOrColumnTailOrCleanKLS': 24
}
```

代表性读数：

| P | top route | top mass share | top intersection | density lower bound |
| ---: | --- | ---: | ---: | ---: |
| 13 | LocalSurvivorOrExplicitPDEC | 1.000000 | 4 | 0 |
| 17 | RefinedPDECOrColumnTailRows | 1.000000 | 28 | 0 |
| 19 | RefinedPDECOrColumnTailRows | 0.971774 | 133 | 0 |
| 23 | RefinedPDECOrColumnTailRows | 0.928819 | 191 | 0 |
| 29 | RefinedPDECOrColumnTailRows | 0.966334 | 141 | 0 |
| 31 | RefinedPDECOrColumnTailRows | 0.908994 | 407 | 0 |
| 37 | RefinedPDECOrColumnTailRows | 0.945645 | 559 | 0 |
| 43 | LiftOrColumnTailOrCleanKLS | 0.880485 | 1077 | 893 |
| 47 | LiftOrColumnTailOrCleanKLS | 0.828184 | 1150 | 1114 |

## 4. 结构结论

固定 `Q=2310` 的 PDEC 终端现在不再是抽象的：

```text
对偶成功:
  U_CRT<L_PDEC，PDEC 分支排除；

对偶失败:
  输出 DualCap；
  SparseCap      => LocalSurvivor / explicit PDEC；
  PersistentCap  => refined PDEC / column-tail rows；
  DensityBarrier => lift / column-tail / CleanKLS。
```

特别是 `P=43,47` 的 top cap 已由密度屏障强制：

```text
|supp(M)|+|C|-Q 很大；
固定 Q 层无法靠同一普通 cap 闭合。
```

所以继续在固定 `Q=2310` 上寻找一个全局方向常数已经被排除；正确动作是：

```text
升层；
或补 column/tail 相位兼容行；
或进入 CleanKLS；
或对 sparse cap 给 LocalSurvivor witness。
```

## 5. 当前未闭合项

本文完成的是 `PDEC 失败输出` 的物化，不是 PDEC 排斥全集。剩余具体义务：

```text
PDEC-1. 对 RefinedPDECOrColumnTailRows cap 补 column/tail 行；
PDEC-2. 对 SparseCap 生成 LocalSurvivor 或 explicit finite PDEC；
PDEC-3. 对 ForcedPersistentByDensityBarrier cap 执行升层门控或 CleanKLS admission；
PDEC-4. 对真实 theta 的连续方向弧提交区间化 U_CRT<L_PDEC 或同格式 DualCap。
```

这把 PDEC 终端硬点从“证明一个抽象上界”推进为具体 cap 列表和路由义务。

## 6. SparseCap 路由推进

后续新增：

```text
experiments/prime_matrix_triad_a1_sparsecap_local_survivor_audit.py
docs/monograph/prime-matrix-triad-a1-sparsecap-local-survivor.md/json
```

该审计已把 `SparseCap` 去重为 `3` 个有限相位集，并逐相位检查真实 lift：

```text
early_completion_conflict_count=0；
unique_early_completion_conflict_count=0；
all_sparse_caps_closed_for_pxP=True；
local_survivor_witness_count=1；
unique_local_survivor_witness_count=1；
finite_pdec_atom_count=35；
unique_finite_pdec_atom_count=25。
```

所以 `PDEC-2` 在 `P×P` 早期出口上已经关闭：若 sparse 原子落到 `phase<=P`，则 `y=0` 不完成并给出 `LocalSurvivor` 列见证；若完成，则完成行都在 `P` 之后，转为 finite PDEC packet。

## 7. ForcedPersistentByDensityBarrier 升层推进

后续新增：

```text
experiments/prime_matrix_triad_a1_forcedcap_lift_audit.py
docs/monograph/prime-matrix-triad-a1-forcedcap-lift-audit.md/json
```

该审计把 `P=43,47` 的 `24` 个 ForcedPersistentByDensityBarrier cap 从 `Q=2310`
lift 到 `Q'=30030`，并以 support 是否非空为门控：

```text
all_old_intersections_recomputed=True；
lift_class_counts={
  LiftPersistentNeedsColumnTailOrNextLift: 24
}。
```

结论不是“forced cap 已排除”，而是：

```text
一层 lift 没有直接稀疏化；
但每个 forced cap 都已有 fiber survival/deletion 账本；
继续持久时必须进入 column-tail 行、next-lift、PDECEntropy 或 CleanKLS；
不能再回到固定 Q=2310 同层循环。
```

## 8. PersistentCap 的 column-tail 支付行

后续新增：

```text
experiments/prime_matrix_triad_a1_persistent_columntail_payment_audit.py
docs/monograph/prime-matrix-triad-a1-persistent-columntail-payment.md/json
```

该审计把 `68` 个 `PersistentCap` 全部转成低洞支付方程：

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|。
```

结果：

```text
unique_phase_signature_count=1915；
all_intersections_recomputed=True；
all_phase_m_counts_match=True；
route_counts={
  ColumnTailPigeonholeRowOrDistributedCleanKLS: 68
}。
```

结构意义：

```text
若某个 tail / column residue 的 top 支付签名持久复现：
  进入 TailAnchor / ColumnCRT displacement PDEC；

若 top 支付签名不持久而需求仍被支付：
  支付必跨多 residue/多壳分散，进入 CleanKLS/DLS。
```

这一步把 `PDEC-1` 从“补 column/tail 行”推进为可复核的支付账本。

## 9. TopPrime 持久支付的晋升吸收

后续新增：

```text
experiments/prime_matrix_triad_a1_topprime_promotion_gate.py
docs/monograph/prime-matrix-triad-a1-topprime-promotion-gate.md/json
```

该审计发现 `PersistentCap` 的 top-prime 支付签名全部等于当前 `Q=2310` 之外的最小新素数：

```text
all_top_prime_is_next_high_prime=True；
cap_count=68。
```

把 `13` 晋升到 `Q'=30030` 后，所有 cap 的 lift 都进入删除门控：

```text
promotion_class_counts={
  PromotionFiberDeletion: 68
}。
```

因此 `top-prime payment persists` 不是新的 PDEC 终端，而是递归剥离动作：

```text
top prime = next new prime
  => promote Q to rQ
  => fiber deletion / sparse；

若升层后仍出现新的 top-prime 持久支付：
  => 重复晋升；

若升层后不再有固定 top-prime / residue：
  => CleanKLS/DLS；

若某个 residue 或 cap 固定持久：
  => Tail/Column PDEC。
```
