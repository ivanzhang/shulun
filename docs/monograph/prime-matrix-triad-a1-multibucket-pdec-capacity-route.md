# Triad-A1 多桶 PDEC 容量路线

**状态：** `triad_a1_multibucket_pdec_capacity_route_open`

本文细化 `MBCS-1`：当 ForcedCap 的实际支付不能由单桶完成，但存在投影兼容的持久多桶签名时，
怎样把它转成可比较的 PDEC 容量问题。

## 1. 从单向量到多桶向量

旧 PDEC 使用同一坏窗推前计数：

```text
g(t)=#{x in S: tau(x)=t}。
```

多桶支付必须改用支付图：

```text
Gamma subset Omega_C x B_C；
(omega,b) in Gamma 表示原子 omega 由 bucket b 支付。
```

对持久多桶签名 `S subset B_C`，定义：

```text
g_b(t)=#{omega: tau(omega)=t and (omega,b) in Gamma},  b in S；
G(t)=sum_{b in S} g_b(t)。
```

因此多桶 PDEC 的变量不是一个 `g(t)`，而是向量 `g=(g_b(t))_{b in S}`。

## 2. 合法容量行

所有容量行仍必须满足 Same-Set Law。多桶情形的基本约束为：

```text
g_b(t)>=0；
g_b(t)<=E_b(t)；
sum_{b in S} g_b(t)<=M(t)；
sum_t sum_{b in S} g_b(t)=|Gamma_S|。
```

其中：

```text
E_b(t)=#{omega: tau(omega)=t and omega 可由 b 支付}；
M(t)=#{omega: tau(omega)=t}。
```

若某个约束事件不是 `tau` 的函数，就必须细化：

```text
tau'=(tau, bucket label, column displacement, tail/cofactor signature)。
```

不能把点级列位移或尾锚事件硬投影到旧 `tau`。

## 3. 多桶 PDEC 上界

对非零频率 `h` 与方向 `zeta`，定义：

```text
U_CRT^multi(h,zeta;S)
= sup Re zeta * sum_t G(t)e(ht)
```

上确界在以下多桶约束系统上取：

```text
P_S={
  g_b(t)>=0；
  g_b(t)<=E_b(t)；
  sum_b g_b(t)<=M(t)；
  column/tail/cofactor/displacement 条件行；
  formal-unit compatibility 行
}。
```

多桶 PDEC 闭合目标为：

```text
U_CRT^multi(h,zeta;S) < L_PDEC^multi(S)
```

对全部 `h!=0` 与方向弧成立。

## 4. 多桶下界

若多桶 formal unit 持久承担支付，则存在同一口径测试函数 `F_S`，使：

```text
sum_t G(t)F_S(t) >= kappa_S |Gamma_S|。
```

于是：

```text
L_PDEC^multi(S)
= kappa_S |Gamma_S| / (sqrt(|G|-1)*||F_S||_2)。
```

这里的关键不是桶数本身，而是：

```text
同一 formal unit；
同一 tau'；
同一 Gamma_S；
同一测试函数 F_S。
```

若这些同一性缺一项，则不能提交 PDEC 比较，必须回到 refined signature 或 CleanKLS。

## 5. 失败输出

若 `U_CRT^multi >= L_PDEC^multi`，失败不能成为新终端，必须输出下列之一：

```text
SingleBucketReturn:
  对偶极值集中到一个 bucket；
  与 ExposureDominance 的单桶排除冲突，或回到单桶 PDEC。

CorrelatedBucketBlock:
  极值集中到固定多桶块；
  细化为更小 formal unit，继续 multi-bucket PDEC。

ColumnTailMissingRow:
  需要 column/tail/cofactor/displacement 条件行；
  回到 TailAnchor / ColumnCRT / cofactor PDEC 行生成。

DiffuseExtremizer:
  极值由许多小桶分散贡献；
  进入 CleanKLS/DLS，而不是 PDEC 同层循环。
```

因此 MBCS-1 也满足无循环原则：每次失败都细化 formal unit、补条件行、返回已排除的单桶形态，或转入大筛分散证书。

## 6. 与当前 ForcedCap 的接口

当前 `24` 个 forced cap 已满足：

```text
forced_dominance_cap_count=24；
min column-residue actual buckets >= 9；
route_counts={MultiBucketPDECOrDistributedCleanKLS: 24}。
```

所以它们若进入持久 PDEC，必须提交：

```text
S: 至少多桶的投影兼容签名；
Gamma_S: 实际支付图或等价 formal-unit 质量；
E_b(t): 每桶暴露上界；
M(t): 同一 Omega_C 的总质量；
tau': 相位兼容细化；
U_CRT^multi < L_PDEC^multi 证书。
```

缺少其中任一项时，不能宣称 PDEC 闭合；但也不能停滞，必须按第 5 节输出可路由失败。

## 7. 下一步最小硬点

最窄可执行目标是：

```text
为 ForcedCap column-residue bucket 构造 tau'；
生成 g_b(t)<=E_b(t) 与 sum_b g_b(t)<=M(t)；
跑一个多桶 LP/对偶骨架；
若失败，输出 SingleBucketReturn / CorrelatedBucketBlock / ColumnTailMissingRow / DiffuseExtremizer。
```

这会把 MBCS-1 从文字合同推进到机器可复核的多桶 PDEC 证书格式。

## 8. 机器骨架物化

新增审计：

```text
experiments/prime_matrix_triad_a1_multibucket_pdec_skeleton.py
docs/monograph/prime-matrix-triad-a1-multibucket-pdec-skeleton.md/json
```

该脚本从原始 `dualcap` 与 `multiplicity` 数据重算每个 forced cap 的全量 `phase-bucket`
暴露矩阵，不依赖旧报告中的 top bucket 摘要。对每个 cap 同时生成：

```text
residue bucket；
column-residue bucket。
```

当前核验：

```text
forced_cap_count=24；
matrix_row_count=48；
all_existing_exposure_references_match=True；
all_phase_exposure_identities_hold=True；
all_single_bucket_payments_excluded=True。
```

桶类型汇总：

```text
residue:
  global_min_actual_buckets_by_exposure=11；
  global_max_bucket_exposure_share=0.0959528；
  global_max_variable_count=125486；

column_residue:
  global_min_actual_buckets_by_exposure=9；
  global_max_bucket_exposure_share=0.118157；
  global_max_variable_count=125486。
```

结构意义：

```text
E_b(t) 与 M(t) 已有可复核哈希；
g_b(t)<=E_b(t)、sum_b g_b(t)<=M(t)、total payment row 已物化；
下一步可直接进入 U_CRT^multi/L_PDEC^multi 对偶比较。
```

若对偶比较失败，仍按第 5 节路由，不产生新出口。

## 9. 裸多桶投影坍缩

新增审计：

```text
experiments/prime_matrix_triad_a1_multibucket_projection_collapse_router.py
docs/monograph/prime-matrix-triad-a1-multibucket-projection-collapse-router.md/json
```

该审计确认一个关键结构事实：若只使用裸约束

```text
0<=g_b(t)<=E_b(t)；
sum_b g_b(t)<=M(t)
```

且目标只依赖

```text
G(t)=sum_b g_b(t)，
```

那么只要

```text
sum_b E_b(t)>=M(t)
```

就有精确投影：

```text
{G(t)} = {0<=G(t)<=M(t)}。
```

当前机器核验：

```text
matrix_row_count=48；
all_single_bucket_payments_excluded=True；
all_phase_capacity_surplus=True；
all_bare_projection_collapses=True；
route_counts={NeedsFormalUnitCompatibilityOrCleanKLS: 48}。
```

结构意义：

```text
单桶支付排除是真的；
但裸多桶变量本身不会降低 U_CRT；
必须加入 formal-unit compatibility、TailAnchor/ColumnCRT/cofactor 条件行或实际支付图约束；
否则无持久兼容签名的部分进入 CleanKLS/DLS。
```

所以 `MBCS-1` 的真实下一硬点进一步收窄为：

```text
构造并证明持久多桶 formal-unit compatibility 行；
或证明不存在持久兼容行，从而进入 DistributedPayment => CleanKLS/DLS。
```

## 10. MFU 候选行与 ActualPaymentStitching

新增：

```text
prime-matrix-triad-a1-multibucket-formal-unit-dichotomy.md
experiments/prime_matrix_triad_a1_multibucket_mfu_candidate_audit.py
docs/monograph/prime-matrix-triad-a1-multibucket-mfu-candidate-audit.md/json
```

多桶 formal unit 被定义为升层投影兼容的正质量桶组：

```text
pi_n(S_{n+1}) subset S_n；
limsup mu_n(S_n) >= eta > 0。
```

当前有限层审计显示：

```text
matrix_row_count=48；
all_rows_have_finite_layer_correlation=True；
route_counts={FiniteLayerMFUCandidateNeedsActualPaymentStitching: 48}。
```

两种桶模型的 `phase-bucket` 互信息都为正：

```text
residue normalized MI >= 0.221783；
column_residue normalized MI >= 0.182715。
```

这说明暴露图中确实存在有限层相关候选行；但它仍不是实际支付证明。下一步必须补：

```text
ActualPaymentStitching:
  若实际支付 Gamma 持久落入某个候选相关行
    => multi-bucket formal unit / PDEC；

  若 Gamma 对所有候选行都不持久
    => DistributedPayment / CleanKLS-DLS。
```

因此 `U_CRT^multi<L_PDEC^multi` 之前还缺一个必要桥：把 exposure 候选行缝合到 actual payment 图。
