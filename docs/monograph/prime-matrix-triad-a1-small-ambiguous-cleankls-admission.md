# Triad-A1 Small-Ambiguous CleanKLS 准入合同

**状态：** `small_ambiguous_cleankls_admission_contract_open`

本文补齐 `ActualPaymentStitching` 的一个窄口：`Gamma` 的选择自由已经很小，但这并不自动证明
`Gamma` 命中某个 MFU 候选行。正确用法是把小自由度变成二分门槛。

## 1. 对象

对 forced cap `C`，写：

```text
Gamma = Gamma_forced union Gamma_amb；
D     = completion-hole demand；
a     = ambiguous_gamma_share_upper_bound。
```

`Gamma_forced` 是唯一覆盖强制的支付边；`Gamma_amb` 是覆盖数 `k>=2` 的可选择部分。已有
`GammaFreedom` 给出：

```text
|Gamma_amb| <= aD；
a <= 0.0552843；
|Gamma_forced| >= 0.944716D。
```

## 2. 小 ambiguous 二分

令 `R` 为任意有限层签名行，例如 phase-bucket、residue-bucket、column-residue-bucket 或其升层投影。

```text
Gamma(R) = Gamma_forced(R) + Gamma_amb(R)；
Gamma_amb(R) <= aD。
```

因此：

```text
若 Gamma(R) > aD + eta D，
则 Gamma_forced(R) >= eta D。
```

也就是说，超过 ambiguous 预算的持久签名质量不能由自由选择噪声解释，必须包含 forced fiber 主体，
从而进入 `PersistentStitching => MFU/PDEC`。

反过来，若所有固定有限签名都满足：

```text
limsup Gamma(R_n)/D_n <= a_n
```

或在升层后趋零，则实际支付没有持久有限签名，只能把责任分散到不断新增的桶/壳/频率中。这正是：

```text
SmallAmbiguousDistributedPayment；
CleanKLS/DLS admission。
```

## 3. 当前物化门控

新增 `experiments/prime_matrix_triad_a1_forced_gamma_signature_router.py` 后，当前账本为：

```text
signature_matrix_row_count=48；
missing_key_count=0；
route_counts={ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission: 48}；
all_rows_routed_to_forced_signature_or_small_ambiguous_clean=True。
```

关键余量：

```text
global_max_ambiguous_gamma_share_upper_bound=0.0552843；
global_min_forced_gamma_share_lower_bound=0.944716；
global_min_signature_signal_minus_ambiguous_budget=0.130733；
global_min_signature_signal_to_ambiguity_ratio=3.51497。
```

这里的 `signature_signal` 是 MFU 候选暴露矩阵中的归一化有限层相关信号，不等同于
`Gamma(R)/D`。它的作用不是替代 actual-payment 证明，而是说明：当前所有有限候选行都已经有
超过 ambiguous 预算的结构信号，下一步只需判定 actual `Gamma` 是否持久缝合这些信号。

## 4. 准入方程

```text
ActualPaymentGamma
=> exists finite R with Gamma(R) > aD + etaD
   or no finite R persists above aD。
```

第一支：

```text
finite persistent R
=> forced主体承担正质量
=> multi-bucket MFU
=> PDEC/refined PDEC。
```

第二支：

```text
no persistent finite R above ambiguous budget
=> small-ambiguous distributed residual
=> CleanKLS/DLS。
```

若 `CleanKLS/DLS` 的对偶失败，它必须输出一个有限签名峰，回到第一支。因此小 ambiguous 分支不产生第四出口。

## 5. 剩余终端硬点

本合同完成的是准入二分，不是最终闭合。仍需提交：

```text
PDEC family 的同集容量上界；
或 CleanKLS/DLS 的平坦大筛证书；
或 LocalSurvivor/TotalDescent 的局部排斥证书。
```
