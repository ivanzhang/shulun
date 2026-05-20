# Prime Matrix LPF ownership sieve source declaration 证书

**状态：** `lpf_ownership_unsigned_declaration_closed_signed_constructor_open`

LPF ownership sieve 给出严格非重叠分桶：每个合数按唯一最小素因子 p 归入 p 层，且 p 层新筛掉的正是 p*m<=N、m>=p、m 的最小素因子不小于 p 的数。因此素数计数恒等式闭合，并且该恒等式可作为 pre-Cauchy unsigned source ownership 声明。但它不产生 signed alpha/delta coefficient、local factor 或 exact-UV fixed-key 重数控制；最新直接主攻转为显式 alpha/delta primitive constructor rule。

```text
pre_cauchy_declaration_line_imported=true
ascending_lpf_ownership_partition_proved=true
prime_count_identity_from_lpf_ownership_proved=true
quotient_condition_matches_user_sieve_proved=true
lpf_ownership_unsigned_declaration_line_closed=true
lpf_ownership_to_signed_alpha_delta_lift_proved=false
explicit_alpha_delta_primitive_constructor_rule_proved=false
row_column_unconditional_closed=false
```

## 1. 精确 ownership 恒等式

对任意 `N>=2`，每个合数 `n<=N` 有唯一最小素因子 `p<=sqrt(N)`。写 `n=p*m`，则 `m>=p`，且 `m` 没有小于 `p` 的素因子。反过来，任意满足这些条件的 `p*m<=N` 的数，其最小素因子正是 `p`。

```text
pi(N)=N-1-sum_{p<=sqrt(N)} #{n<=N: n composite and least_prime_factor(n)=p}
LPF_p(N)=#{m: p*m<=N, m>=p, and m has no prime factor < p}
```

这正是从小到大筛入每个素数时的“新筛掉”集合；不同 `p` 的集合互不相交，合并后正好是 `N` 以内所有合数。

## 2. 样本审计

| N | pi(N) | bucket sum | identity | quotient buckets |
| ---: | ---: | ---: | --- | --- |
| 10 | 4 | 5 | `true` | `true` |
| 30 | 10 | 19 | `true` | `true` |
| 100 | 25 | 74 | `true` | `true` |
| 997 | 168 | 828 | `true` | `true` |
| 5003 | 670 | 4332 | `true` | `true` |

## 3. 对 source declaration 的影响

```text
PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter
  ->
LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger AND ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger AND SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger AND PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger
```

LPF ownership 关闭 declaration line 的 unsigned 分桶字段；真正仍缺的是 actual noncanonical primitive constructor 的 signed `alpha/delta` 规则、定义域、逐行 `(u,v)`/key/sign/local-factor 输出和失败回流。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreCauchyDeclarationLineTargetImported | `true` | `false` | actual emitter source table 的第一合法字段仍是 pre-Cauchy constructor declaration line。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| AscendingLeastPrimeFactorOwnershipPartition | `true` | `true` | 每个合数按唯一最小素因子进入且只进入一个筛层；p 层新筛数为 p*m<=N、m>=p、且 m 无小于 p 的素因子。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| PrimeCountingIdentityFromLPFOwnership | `true` | `true` | 因此 pi(N)=N-1-sum_{p<=sqrt(N)} #{n<=N: n composite and LPF(n)=p}，样本审计也逐项通过。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| LeastFactorCutoffImported | `true` | `true` | 逐行最小因子激活截止已记录：超过 sqrt 窗口的斜线只是 shadow hit，不产生新的独立 ownership。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| LPFOwnershipIsPreCauchyUnsignedDeclaration | `true` | `true` | LPF ownership 只读取自然数、整除关系和筛层顺序；不依赖 Cauchy、Phi、payment 或零行反推。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| UnsignedSkeletonCompatibilityImported | `true` | `true` | 现有 unsigned skeleton 已能承接 source tuple、carry shell、P 列相位和 layered-wheel 兼容字段。 | AlphaRowUnsignedSkeletonLedger |
| LPFOwnershipDoesNotEmitSignedAlphaDelta | `true` | `true` | LPF 分桶只给合数 ownership 与候选行索引；它不产生 orientation、signed coefficient、local factor 或 alpha/delta 权重。 | AlphaFormulaSignedCoefficientLiftLedger |
| ActualConstructorFormulaLineRouterImported | `true` | `false` | actual constructor formula line 已有路由：必须继续给显式 alpha/delta primitive constructor rule、定义域、行输出和失败回流。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger |
| SourceDeclarationCommonPacketStillOpen | `true` | `false` | payload/ExactUV 合流所需的 common pre-Cauchy source declaration packet 仍未由当前语料证明。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| DeclarationLineReducedToLPFOwnershipAndExplicitFormula | `true` | `false` | 本步把 declaration line 的 unsigned ownership 字段闭合，并把真正剩余压回显式 signed constructor 公式与回流纪律。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger AND ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger AND SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger AND PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger |
| ExplicitAlphaDeltaPrimitiveRuleStillOpen | `false` | `false` | 当前材料尚未写出 actual noncanonical primitive constructor 的显式 alpha/delta 规则。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| RowColumnUnconditionalClosureReached | `false` | `false` | LPF ownership 是精确筛法恒等式，但还不是 source signed-lift、ExactUV fixed-key 或全局终端排斥证明。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger AND ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger AND SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger AND PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger |

## 5. 诚实边界

- 本证书证明的是 LPF ownership 精确分桶和素数计数恒等式。
- 本证书没有证明 signed alpha/delta primitive constructor rule。
- 本证书没有证明 actual emitter source table、complete key partition 或 fixed-key exact-UV local multiplicity。
- 行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_lpf_ownership_sieve_source_declaration_router.py` | `06a0cf9f3fd5cb571095f5b90fccf1aa6653679ac645eab38e5759292252c78e` |
| `docs/monograph/prime-matrix-strict-actual-emitter-source-table-router.json` | `e327b1a80aef83a36279378e5892334fa305d92d5ac1bcbb8601eaab2f18ab3e` |
| `docs/monograph/prime-matrix-strict-actual-constructor-formula-line-router.json` | `ac19ab81150df61902058d6c890195592b25400f04a32562b1fa32b966a89913` |
| `docs/monograph/prime-matrix-strict-alpha-row-unsigned-skeleton-router.json` | `98f6fa7be381de7d3170bc0abf7e37bde6b1f87351c3ad4bc2c2d4ce62e71c87` |
| `docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json` | `d9e042ffccaaf050e72788abdb0a10a5776a3cb4d8a37fc949c9710a4a832f44` |
| `docs/monograph/prime-matrix-least-factor-activation-cutoff.md` | `bde0d039b80af454aa671cfc1d7cf4288826690ce5e958a0e7a74544f99bb7a2` |
