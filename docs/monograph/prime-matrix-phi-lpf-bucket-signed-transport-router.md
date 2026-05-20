# Prime Matrix Phi-LPF bucket signed transport 证书

**状态：** `phi_lpf_signed_law_reduced_to_rough_cofactor_signed_transport_open`

Phi/LPF 递推继续给出 signed law 的精确支撑分裂：每个 owner bucket `p` 中，p-rough cofactor 集合按是否含当前递推素因子分成 next-rough 部分和 `m=q*m'` 的回流部分。但这个分裂只移动 domain；要得到 signed 递推，必须正向给出 `a_p(q*m')` 的符号、local factor、alpha/delta side 和 branch 传输律。因而最新硬点从泛化 bucket signed law 收窄为 `PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward`，或等价提交逐 Phi-LPF bucket 的 signed value table。

```text
phi_lpf_support_and_capacity_imported=true
unsigned_cofactor_split_identity_proved=true
signed_bucket_sum_partition_identity_proved=true
phi_lpf_rough_cofactor_signed_transport_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
row_column_unconditional_closed=false
```

## 1. signed Phi 分裂

对 owner prime `p` 写 `a_p(m)` 为待证明的 Cauchy 前 signed coefficient。Phi 递推只给出支撑分裂：

```text
sum_{m p-rough, 1<m<=x} a_p(m)
  = sum_{m p_next-rough, 1<m<=x} a_p(m)
    + sum_{m' p-rough, m'<=floor(x/p)} a_p(p*m')
```

右侧第二项仍含未知的 `a_p(p*m')`，所以 signed 闭合需要 cofactor 乘法传输律。

## 2. 样本支撑分裂审计

| N | support keys | nondivisible | divisible preimages | split | sign-shadow log10 |
| ---: | ---: | ---: | ---: | --- | ---: |
| 30 | 19 | 9 | 10 | `true` | 5.71957 |
| 100 | 74 | 41 | 33 | `true` | 22.27622 |
| 997 | 828 | 498 | 330 | `true` | 249.252836 |
| 5003 | 4332 | 2680 | 1652 | `true` | 1304.061941 |
| 10000 | 8770 | 5468 | 3302 | `true` | 2640.033062 |

## 3. signed transport 字段

| field | meaning |
| --- | --- |
| `owner_bucket_prime` | 外层 LPF owner prime `p`，即 candidate composite 的最小素因子。 |
| `rough_cofactor_step` | Phi 递推中的 cofactor 乘法步 `m -> q*m`，特别是 `q=p_k`。 |
| `signed_coefficient_transport` | 正向给出 `a_p(q*m)` 与 `a_p(m)` 或原始 source row 的关系。 |
| `orientation_parity_update` | cofactor 乘法对 orientation、奇偶分支和符号的更新规则。 |
| `local_factor_multiplier` | 乘入 `q` 后 local factor、截断因子、非零条件的更新。 |
| `alpha_delta_side_branch_transition` | 同一 key 在 alpha/delta 侧、branch key、ExactUV 输出中的传输。 |
| `prepushforward_signed_sum_identity` | 传输后的有限 signed 求和在 Phi/payment 推前前闭合。 |
| `return_tag` | 传输失败、零因子、符号冲突或后验依赖时的命名回流。 |
| `no_downstream_recovery` | 传输律不能读取 payment skeleton、零行覆盖、origin table 固定点或终端反推。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PhiLPFSignedLawTargetImported | `true` | `false` | 上一层已把 signed kernel 的剩余压成 Phi-LPF bucket signed coefficient law。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| PhiRecursiveLPFSupportImported | `true` | `true` | Phi/LPF 递推和 support bijection 已关闭无符号支撑与容量。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| UnsignedCofactorSplitClosed | `true` | `true` | 对每个 owner prime `p`，cofactor 支撑按 `m` 是否被当前递推素数整除精确分裂。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| SignedBucketSumPartitionClosedFormally | `true` | `true` | 任意已给定的 rowwise signed 系数 `a_p(m)` 都可沿同一分裂作有限求和；这是形式恒等式，不产生系数值。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| PhiCountsDoNotDetermineSignedValues | `true` | `true` | 同一 Phi 支撑容量可承载大量 signed decorations；Phi 计数只给 domain，不给 orientation/local factor。 | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward |
| TransportLawIsFirstRecursiveSignedField | `true` | `true` | 若要把 Phi 递推升级为 signed 递推，第一字段必须说明 cofactor 乘法下 signed coefficient 如何传输。 | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward |
| LPFCandidateMapStillUnsigned | `true` | `false` | LPF candidate-row map 给唯一候选行索引，但不输出 signed coefficient。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| PointwiseSignedValueTableStillOpen | `true` | `false` | 现有逐点 signed alpha value table 未闭合；Phi-LPF bucket 版本也未提交。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| SignedLiftAndPrimitiveExpressionStillOpen | `true` | `false` | signed lift 与 primitive summand signed expression 均仍缺正向系数来源。 | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward |
| NoDownstreamRecoveryImported | `true` | `true` | 旧 signed-source 路线会回到自身；不能用 payment、零行或 origin table 反推 signed transport。 | fixed-point cut imported |
| PhiLPFBucketSignedCoefficientLawCurrentCorpusProved | `false` | `false` | 当前材料尚未给出 cofactor signed transport law 或等价 rowwise signed coefficient table。 | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步没有证明 signed coefficient law、ExactUV fixed-key、终端排斥或三命题无条件闭合。 | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |

## 5. 下一真正单点

```text
PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward
```

等价并行入口：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_bucket_signed_transport_router.py` | `c29ed66b199f064eae5869317f5bd083a11a26f2685b855b2b32bfd1200511d8` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-value-table-router.json` | `c44a6e986d59cd068f19cdb58427f779721bb1cf984ff1edb4d67be28cb6dc8c` |
| `docs/monograph/prime-matrix-strict-alpha-formula-signed-lift-router.json` | `bdcb088da6896a5b4ff6653ce0ffecc5c66310e355eece985ac8f635ad48ed7a` |
| `docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json` | `b0b1264cf6f3fbad60724a440f0dc9872dbc577376ed466e5dcac0cf66caa5ff` |
| `docs/monograph/prime-matrix-strict-signed-source-fixed-point-breaker-router.json` | `a07743b021b11f13f19d791fc43d4268f551878c43f3340bd54664254311185f` |
