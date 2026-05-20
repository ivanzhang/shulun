# Prime Matrix Phi-recursive LPF ownership 证书

**状态：** `phi_recursive_lpf_ownership_closed_signed_summand_expression_open`

Phi 递推把 LPF ownership 从集合分桶提升为可机械计算的 rough-count 账本。每个 p 层容量正是 Phi(floor(N/p),p)-1，p>sqrt(N) 自动为零，所以用户给出的 pi(N) 精确公式闭合。该层仍是无符号 ownership/容量层；它不生成 actual noncanonical primitive summand 的 signed 权重表达式。

```text
lpf_ownership_imported=true
phi_rough_count_definition_proved=true
phi_recursion_identity_proved=true
phi_recursive_lpf_bucket_formula_proved=true
prime_count_identity_from_phi_lpf_proved=true
large_prime_layer_zero_mass_proved=true
sample_audit_all_passed=true
phi_recursive_ownership_to_signed_alpha_delta_lift_proved=false
primitive_summand_signed_weight_expression_proved=false
row_column_unconditional_closed=false
```

## 1. Phi 递推

`Phi(x,p)` 计数 `1<=m<=x` 且所有素因子都不小于 `p` 的整数，并包含 `m=1`。对相邻素数 `p_k,p_{k+1}`，把 `p_k`-rough 数按是否被 `p_k` 整除分为两类：

```text
Phi(x,p_k)=Phi(x,p_{k+1})+Phi(floor(x/p_k),p_k)
```

若 `p_k>x`，则只剩 `m=1`，所以 `Phi(x,p_k)=1`。这给出有限递归基。

## 2. LPF 桶公式

对 `p<=sqrt(N)`，`p` 层新筛掉的合数为 `p*m<=N` 且 `m` 为 `p`-rough 的项；`m=1` 对应素数 `p` 自身，必须扣除：

```text
c_N(p)=Phi(floor(N/p),p)-1
pi(N)=N-1-sum_{p<=sqrt(N)}(Phi(floor(N/p),p)-1)
```

当 `p>sqrt(N)` 时 `floor(N/p)<p`，递归基给出 `Phi(floor(N/p),p)=1`，所以该层没有新合数质量。

## 3. 样本审计

| N | pi(N) | composite count | bucket sum | pi from Phi | recursion | identity |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 10 | 4 | 5 | 5 | 4 | `true` | `true` |
| 30 | 10 | 19 | 19 | 10 | `true` | `true` |
| 100 | 25 | 74 | 74 | 25 | `true` | `true` |
| 997 | 168 | 828 | 828 | 168 | `true` | `true` |
| 5003 | 670 | 4332 | 4332 | 670 | `true` | `true` |
| 10000 | 1229 | 8770 | 8770 | 1229 | `true` | `true` |

## 4. 对最新硬点的影响

```text
LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger
  ->
PhiRecursiveLPFOwnershipRoughCountLedger AND ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

Phi 递推给出的是 LPF ownership 的容量读数和机械递归计算。它可以加强 `LPFOwnershipAlphaCandidateRowEmissionMapLedger` 的源容量基础，但不能把 candidate row 升格为 actual signed alpha primitive row。

最新直接硬点保持为：

```text
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LPFOwnershipImported | `true` | `true` | 上一层已把合数按唯一最小素因子分桶，并关闭 pre-Cauchy unsigned ownership 字段。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| PhiRoughCountDefinitionClosed | `true` | `true` | Phi(x,p) 定义为 1<=m<=x 且无小于 p 的素因子的 rough 计数，包含 m=1。 | PhiRecursiveLPFOwnershipRoughCountLedger |
| PhiRecursionIdentityClosed | `true` | `true` | 按是否被 p_k 整除分拆，得到 Phi(x,p_k)=Phi(x,p_{k+1})+Phi(floor(x/p_k),p_k)。 | PhiRecursiveLPFOwnershipRoughCountLedger |
| LPFBucketEqualsPhiMinusOneClosed | `true` | `true` | p 层新筛合数数 c(p)=Phi(floor(N/p),p)-1；减去的 1 是 cofactor m=1 对应的素数 p。 | PhiRecursiveLPFOwnershipRoughCountLedger |
| PrimeCountingIdentityFromPhiLPFClosed | `true` | `true` | 求和 p<=sqrt(N) 的 Phi 桶后得到 pi(N)=N-1-sum_p(Phi(floor(N/p),p)-1)。 | PhiRecursiveLPFOwnershipRoughCountLedger |
| LargePrimeLayerZeroMassClosed | `true` | `true` | 当 p>sqrt(N) 时 floor(N/p)<p，Phi(floor(N/p),p)=1，故 c(p)=0。 | PhiRecursiveLPFOwnershipRoughCountLedger |
| CandidateRowMapImported | `true` | `true` | Phi 递推加强 LPF candidate-row map 的源计数，但不改变其 unsigned 性质。 | LPFOwnershipAlphaCandidateRowEmissionMapLedger |
| PhiOwnershipDoesNotEmitSignedWeight | `true` | `true` | Phi 递推只计算 rough ownership 容量；它不赋 orientation、signed coefficient、local factor 或 primitive summand。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| PrimitiveSummandSignedExpressionStillOpen | `true` | `false` | 逐行 signed primitive summand 表达式仍是 LPF/Phi 无符号层之后的真正硬点。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步没有证明 signed alpha/delta、pairing、ExactUV fixed-key、DStructure/Rankin 或 endpoint 排斥。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |

## 6. 诚实边界

- 本证书证明 Phi 递推、LPF 桶公式与素数计数恒等式。
- 本证书没有证明 signed alpha/delta primitive constructor rule。
- 本证书没有证明 local factor、ExactUV fixed-key multiplicity 或 endpoint 终端排斥。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_recursive_lpf_ownership_router.py` | `46b7e75f0344cf3da63a1504d6c1ddb84052e3e3431c421a59ca165a3d81f581` |
| `docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json` | `2857cbdeab08a400b1bce9099500290e8c59439ec11553ca0e5678335a5e6806` |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json` | `fb392c7ecb2613c000b1c8696ff285c12cb91c815a08dad700e24c21fec6b66f` |
