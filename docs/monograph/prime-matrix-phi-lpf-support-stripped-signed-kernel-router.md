# Prime Matrix Phi-LPF support-stripped signed kernel 证书

**状态：** `phi_lpf_support_closed_signed_bucket_law_open`

Phi/LPF 精确分桶把 noncircular signed kernel 中的无符号支撑、容量和候选行索引全部剥离。每个合数 candidate 支撑键唯一为 `(p,m)`，其中 `p` 是最小素因子、`m` 为 p-rough，容量为 `Phi(floor(N/p),p)-1`。因此最新缺口不再是找行、数行或证明粗数容量，而是对这些 Phi-LPF support keys 正向赋 signed coefficient、sign/local factor 和推前前 alpha/delta 求和恒等式。

```text
phi_recursive_lpf_ownership_imported=true
lpf_candidate_row_map_imported=true
phi_lpf_support_bijection_proved=true
support_and_capacity_components_closed=true
phi_lpf_bucket_signed_coefficient_law_proved=false
noncircular_signed_coefficient_emission_kernel_proved=false
row_column_unconditional_closed=false
```

## 1. 支撑剥离

Phi-LPF 层给出的 support key 是 `(p,m)`，其中 `p<=sqrt(N)`，`m<=floor(N/p)`，`m>1`，且 `m` 没有小于 `p` 的素因子。该 key 对应唯一合数 `pm`，不同 key 不重叠。

```text
NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
  ->
PhiLPFPrimitiveRowSupportAndCapacityLedger AND PhiLPFBucketSignedCoefficientLawBeforePushforward
```

## 2. 样本审计

| N | pi(N) | composites | support keys | bijection |
| ---: | ---: | ---: | ---: | --- |
| 30 | 10 | 19 | 19 | `true` |
| 100 | 25 | 74 | 74 | `true` |
| 997 | 168 | 828 | 828 | `true` |
| 5003 | 670 | 4332 | 4332 | `true` |
| 10000 | 1229 | 8770 | 8770 | `true` |

## 3. signed law 剩余字段

| field | meaning |
| --- | --- |
| `bucket_key` | LPF/Phi 已闭合的 `(p,m)` primitive row support key。 |
| `signed_coefficient_value` | 对该 key 的 Cauchy 前 signed coefficient 正向赋值。 |
| `sign_local_factor` | sign、local factor、非零条件与失败回流标签。 |
| `alpha_delta_side_and_branch_key` | 该 key 属于 alpha/delta 哪侧、哪个 branch key、哪个 `(u,v)` 输出。 |
| `prepushforward_sum_identity` | 对全部 Phi-LPF keys 的 signed 求和在推前前等于 actual alpha/delta 贡献。 |
| `no_downstream_recovery` | 赋值律不读取 payment skeleton、零行覆盖、来源恒等式或终端反推。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NoncircularKernelImported | `true` | `false` | 现有非循环 kernel 路由已把 signed-source 固定点的第一入口钉到 pre-Cauchy declaration。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| SignedSourceFixedPointImported | `true` | `true` | 旧 signed-source 链已确认会从 row-level 表绕回自身，不能作为证明。 | fixed-point cut imported |
| PhiRecursiveLPFOwnershipImported | `true` | `true` | Phi 递推已证明 LPF rough-count 桶公式和素数计数恒等式。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| LPFCandidateRowMapImported | `true` | `true` | LPF ownership 已给 alpha-side candidate row 的非后验支撑索引。 | LPFOwnershipAlphaCandidateRowEmissionMapLedger |
| PhiLPFSupportBijectionClosed | `true` | `true` | 每个合数 candidate 支撑键唯一写成 `(p,m)`，其中 `p=LPF(pm)` 且 `m` 为 p-rough；样本逐项验证。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| SupportAndCapacityNoLongerSignedKernelGap | `true` | `true` | 行支撑、容量和 p>sqrt(N) 零质量已由 Phi-LPF 层支付，不能再混入 signed kernel 缺口。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| PrimitiveSummandSignedExpressionStillOpen | `true` | `false` | signed expression 仍未证明；现在其无符号 support 子问题已剥离。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| PhiLPFBucketSignedCoefficientLawStillOpen | `true` | `false` | 剩余必须对每个 Phi-LPF support key 正向赋 signed coefficient、local factor 和推前前求和恒等式。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| NoncircularKernelReducedToSignedLawOnPhiLPFBuckets | `true` | `false` | 非循环 signed kernel 被收窄为 Phi-LPF support 上的 signed coefficient law，而非找行或数行问题。 | PhiLPFPrimitiveRowSupportAndCapacityLedger AND PhiLPFBucketSignedCoefficientLawBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步没有证明 signed coefficient law、alpha/delta pairing、ExactUV fixed-key 或终端排斥。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |

## 5. 下一真正单点

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_support_stripped_signed_kernel_router.py` | `eace123278eba8003829747f6caf4e0b24c8a5aa138a384dd54f5c88ce713386` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
| `docs/monograph/prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json` | `96d6dadbc5add815f8623295aae5ae519c0b5e44db556d85d657259db97a9773` |
| `docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json` | `b0b1264cf6f3fbad60724a440f0dc9872dbc577376ed466e5dcac0cf66caa5ff` |
| `docs/monograph/prime-matrix-strict-signed-source-fixed-point-breaker-router.json` | `a07743b021b11f13f19d791fc43d4268f551878c43f3340bd54664254311185f` |
