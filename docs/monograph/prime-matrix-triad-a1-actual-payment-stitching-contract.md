# Triad-A1 ActualPaymentStitching 合同

**状态：** `actual_payment_stitching_contract_open`

本文处理 `MFU` 之后暴露出的真实硬点：`Exposure` 只说明某个 bucket 可以支付某个低洞原子；
`ActualPayment` 必须选择一组真实支付边覆盖全部低洞。不能把二者混同。

## 1. 三层对象

对 forced cap `C`：

```text
Omega_C = 低洞需求原子；
B_C     = 可支付 bucket；
E       subset Omega_C x B_C，可支付暴露边；
Gamma   subset E，实际支付边。
```

满足：

```text
每个 omega in Omega_C 必须由 Gamma 中至少一条边支付；
ActualPayment(b) <= Exposure(b)；
Gamma 只能使用 E 中已有的边。
```

当前已完成的是 `E` 的结构审计，不是 `Gamma` 的选择证明。

## 1.1 Fiber 一致性

`Gamma` 还不能是任意边覆盖。固定 phase `t` 时，真实完成态必须来自同一个：

```text
row = t + Qy；
y mod high_period。
```

因此同一 phase 的全部低洞支付边必须由同一个 `y` 同时诱导。新增审计
`prime_matrix_triad_a1_forcedcap_fiber_consistent_payment_audit.py` 已把这一约束物化为
fiber-consistent cover incidence。

当前核验：

```text
forced_cap_count=24；
unique_phase_cache_count=4316；
all_completion_counts_match_m_vector=True；
route_counts={FiberConsistentPaymentMFUOrDistributedCleanKLS: 24}。
```

进一步的 fiber 支配路由给出：

```text
global_min_actual_residue_buckets_by_fiber=42；
global_min_actual_column_residue_buckets_by_fiber=24；
global_max_residue_fiber_cover_share=0.0240372；
global_max_column_residue_fiber_cover_share=0.0433302。
```

这说明加入同一 `y` 后，实际支付必须高度多桶化；但它仍没有替代 `Gamma` 的最小选择证明。

## 1.2 Gamma 自由度上界

对每个完成态-低洞对，令 `k>=1` 为覆盖该洞的高素数边数。若 `k=1`，这条边被唯一覆盖强制决定；
只有 `k>=2` 时才存在选择自由。于是：

```text
D = completion-hole demand；
C = fiber-consistent cover incidence = sum k；
ambiguous_pairs <= C-D；
ambiguous_share <= C/D - 1；
forced_share >= 2 - C/D。
```

新增 `prime_matrix_triad_a1_forcedcap_gamma_freedom_router.py` 后，当前读数为：

```text
global_max_ambiguous_gamma_share_upper_bound=0.0552843；
global_min_forced_gamma_share_lower_bound=0.944716。
```

因此实际支付图 `Gamma` 的大部分不是任意选择，而是被唯一覆盖强制决定；真正自由选择部分至多约 `5.53%`。

## 1.3 Forced Gamma 签名压力

新增 `prime_matrix_triad_a1_forced_gamma_signature_router.py` 后，把四个账本拼接到同一行：

```text
MFU finite signature；
fiber-consistent completion；
fiber bucket dominance；
Gamma forced/ambiguous budget。
```

当前核验：

```text
signature_matrix_row_count=48；
missing_key_count=0；
route_counts={ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission: 48}；
global_min_signature_signal_minus_ambiguous_budget=0.130733；
global_min_signature_signal_to_ambiguity_ratio=3.51497。
```

这里的 `signature_signal` 仍来自有限层候选行，不等于 `Gamma(R)`。它的严格作用是门控：

```text
若 actual Gamma 持久命中某有限签名且超过 ambiguous 预算，
则该质量不能由选择自由解释，必须含 forced fiber 主体，进入 MFU/PDEC；

若 actual Gamma 不持久命中任何有限签名，
则剩余为 small-ambiguous distributed payment，进入 CleanKLS/DLS。
```

## 1.4 Small-Ambiguous 后继门控

新增 `prime_matrix_triad_a1_small_ambiguous_clean_admission_router.py` 后，small-ambiguous 分支继续接到
NoDeletion-KL 账本：

```text
small ambiguous residual
  => FiberDeletion 继续推进；
  or NoDeletion + KL/MI 偏斜 => refined/new-layer PDEC；
  or NoDeletion + KL/MI flat => CleanKLS/DLS。
```

当前核验：

```text
all_current_small_ambiguous_routed=True；
gate_counts={FiberDeletion: 6}；
current_nodeletion_triggered=False；
shape_route_counts={PhaseResidueMutualPDECWitness: 6}；
min_phase_residue_mutual_normalized_kl=0.412500。
```

因此当前已物化层尚未触发 clean KLS 终端；若未来删除势停止，只有 KL/互信息平坦时才允许进入
CleanKLS/DLS，否则回流 PDEC。

## 2. 候选行

MFU 候选审计给出有限层相关行：

```text
R_j subset E；
I(phase;bucket)>0。
```

这些行只是候选。真正需要证明的是：

```text
Gamma(R_j) 在反例塔中是否持久承担正质量。
```

## 3. Stitching 二分

### 3.1 PersistentStitching

若存在候选行族 `R_{j,n}`，沿升层投影兼容，并且：

```text
|Gamma_n cap R_{j,n}| >= eta |Omega_n|
```

在无限多层成立，则：

```text
R_{j,n} => multi-bucket formal unit；
```

必须进入：

```text
multi-bucket PDEC；
TailAnchor / ColumnCRT / cofactor refined row；
U_CRT^multi < L_PDEC^multi。
```

### 3.2 NoPersistentStitching

若对任意固定有限候选行 `R_j`：

```text
|Gamma_n cap pi^{-1}(R_j)| / |Omega_n| -> 0，
```

则实际支付不能锁定任何有限签名，只能向不断新增的 bucket、residue、column-tail 签名扩散。

这就是：

```text
DistributedPayment；
CleanKLS/DLS admission。
```

若 CleanKLS/DLS 的大筛对偶失败，则它会输出某个集中签名，回到 `PersistentStitching`。

## 4. 无循环方程

```text
ActualPaymentGamma
=> PersistentStitching
   or NoPersistentStitching。
```

其中：

```text
PersistentStitching    => MFU/PDEC/refined row；
NoPersistentStitching  => CleanKLS/DLS；
CleanKLS 对偶失败      => PersistentStitching。
```

因此 `ActualPaymentStitching` 也不产生第四出口。

## 5. 当前输入状态

已知：

```text
单桶 actual payment 排除；
裸多桶 LP 投影坍缩；
48 个有限层 phase-bucket 相关候选行已物化；
fiber-consistent 完成态 incidence 已物化；
实际支付至少需要 42 个 residue 桶或 24 个 column-residue 桶；
Gamma 至少约 94.47% 由唯一覆盖强制决定；
48 个有限签名行全部超过 ambiguous 预算门槛；
small-ambiguous 后继当前由 FiberDeletion 或 phase-residue PDEC witness 吸收；
所有候选仍处于 exposure 层。
```

仍缺：

```text
Gamma 的持久缝合进入 PDEC；
或 small-ambiguous distributed residual 的 CleanKLS/DLS 证书。
```

所以下一步硬点是：

```text
APS-1: 对实际支付图 Gamma 做有限签名鸽巢/投影塔二分；
APS-2: 持久签名进入 MFU/PDEC；
APS-3: 无持久签名进入 CleanKLS/DLS。
```
