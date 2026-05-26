# Prime Matrix Phi-LPF minimal parity-breaker route-forcing 路由

**状态：** `minimal_parity_breaker_route_forcing_pinned_signed_transport_open`
**核验日期：** `2026-05-26`

## 1. 最小破障裁定

无符号粗数信息即使在 LPF/Phi 层面完全精确，也不能把素数从两个或更多大素因子的乘积中分离出来。缺失的数据不是另一个 Euler-product 支撑计数，而是有符号除子/trace 相消，或逐点素数分布下界。

```text
minimal_route_forcing_closed=true
lpf_exact_count_formula=C_p(N)=Phi(floor(N/p); primes< p)-1
legendre_periodic_boundary_not_half_main=true
more_wheel_or_lpf_refinement_rejected_as_first_break=true
row_column_unconditional_closed=false
```

## 2. 必须攻克的精确公式

| formula | equivalent form | minimum strength | current status | why not enough now |
| --- | --- | --- | --- | --- |
| theta((kP,(k+1)P))>0 for every 1<=k<P | h(kP)<P for every 1<=k<P | pointwise sqrt-scale input with constant C<=1 | not available unconditionally in current corpus | known theta>1/2 inputs close only low-row or zero-density bands; C>1 leaves positive-density top band |
| psi((kP,(k+1)P)) > PrimePowerTail((kP,(k+1)P)) | theta((kP,(k+1)P))>0 after removing pure prime powers | pointwise lower bound exceeding an o(P) tail | tail bound closed; pointwise psi lower bound not proved | sublinear tail is bookkeeping unless a positive rowwise psi main term is supplied |

## 3. 路线强制表

| route | minimal object | closed assets | open atom | breaks parity | chosen next |
| --- | --- | --- | --- | --- | --- |
| Pointwise theta / gap route | theta((kP,(k+1)P))>0, equivalently h(kP)<P for all strict rows | C<=1 sqrt-scale threshold contract; top-row/Oppermann subcore separated | unconditional pointwise C<=1 sqrt-scale theorem or row-specific substitute | `true` | `false` |
| Pointwise psi beyond prime-power tail | psi(I_{P,k})>PrimePowerTail(I_{P,k}) rowwise | prime_power_tail(I_{P,k}) = O(sqrt(P)*log(P)+P^(1/3)*log(P)^2)=o(P) | pointwise psi lower bound at exact row scale | `true` | `false` |
| Internal LPF signed cofactor transport | a_p(q*m) transport law with orientation/local-factor/branch updates before pushforward | unsigned cofactor split and formal signed partition identity | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward | `true` | `true` |
| Trace / Kloosterman / Type-II route | completed source-keyed signed trace family with factorable coefficients and conductor control | formal Jordan kernel, prefix-record reflection, finite q-spine kernel | source-key lift plus Type-II factorability and conductor range | `true` | `false` |
| Shared-pivot PDEC/SAE return | uniform hinge/payment law failure returns to controlled contradiction | shared-pivot hinge contract and endpoint slack ledger | BridgeRootSharedPivotHingeLawOrPDEC plus terminal sibling q-spine payment | `true` | `false` |
| More LPF/Phi/wheel refinement | none; this class only refines unsigned support | C_p(N)=Phi(floor(N/p); primes< p)-1 | not a parity-breaking atom | `false` | `false` |

## 4. 当前最快非循环下一手

```text
chosen_next_primary_attack_target=PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward
chosen_parallel_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

这是从小到大 LPF 剥离第一次可能升级为 signed 递推的位置。外部 trace/Type-II 工具必须先拿到这类系数才能接入；外部 theta/psi 路线则需要当前不可用的点态平方根尺度定理。

## 5. 外部前沿输入边界

| input | supplies | project blocker | direct close now | url |
| --- | --- | --- | --- | --- |
| Guth--Maynard zero-density / short intervals | pointwise PNT in intervals x^{17/30+o(1)} | 17/30>1/2, so top P^2 rows still need sqrt-scale strength | `false` | https://arxiv.org/abs/2405.20552 |
| Runbo Li short intervals | prime existence in [x-x^0.52,x] for large x | 0.52>1/2; closes only low-row band after row containment | `false` | https://arxiv.org/abs/2308.04458 |
| Runbo Li large-modulus AP / Harman sieve | mean value theorems beyond x^{1/2} for selected modulus families | Prime Matrix target is pointwise fixed row/column positivity at x=P^2 | `false` | https://arxiv.org/abs/2602.20917 |
| Fouvry--Kowalski--Michel--Sawin trace functions | bilinear trace-function cancellation below Polya-Vinogradov range | no completed source-keyed trace sheaf/family yet | `false` | https://arxiv.org/abs/2511.09459 |
| Milicevic--Qin--Wu Kloosterman bilinear forms | power-saving bilinear Kloosterman estimates modulo arbitrary q | no admissible two-variable Kloosterman family from LPF payload yet | `false` | https://arxiv.org/abs/2511.07550 |
| Wright trilinear Kloosterman fractions | trilinear/unbalanced convolution estimates with partially fixed moduli | no trilinear convolution or equidistributed beta sequence constructed | `false` | https://arxiv.org/abs/2604.25177 |
| Pascadi distribution / non-abelian Type-II inputs | well-factorable prime/smooth distribution and composite-modulus Kloosterman Type-II bounds | current LPF ownership is not a well-factorable signed coefficient family | `false` | https://arxiv.org/abs/2505.00653 and https://arxiv.org/abs/2511.08445 |

## 6. 最新开放口

```text
MinimalParityBreakerRouteForcingClosed AND NeedEitherPointwiseThetaPsiCOneInputOrSignedCofactorTransport AND PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward AND BoundaryRatioSourceKeyLawOrPDEC AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND AdmissibleSignedTraceTypeIIFamilyStillOpen
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/external-theorem-index.md` | `586a1bc03fdb913e27f16918c6772f995336a11608e6c97110f6f91ef63abf66` |
| `docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json` | `3a8f50d512a77ad9eeb8f113226fd0e1c3e33e6637b4accec90f77f381195780` |
| `docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json` | `04179593260192cfa899fe1b15997d1467ec678ba64de7c8fc762b2b921ede99` |
| `docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json` | `8f696d3cb025e8d98790530763d5b87717c945b57c310f6d16f4c49711c8fdcb` |
| `docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json` | `3a52ce41b6380ad6b884271d246183005d023c29eb162d745a54f668acb16120` |
| `docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json` | `6c66e0256c2481244ed42dd3d960241af0cf524643e0dde78aea51e62e0d6223` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json` | `74636f1bc6c8e7088a213b0df5440bf93aadb10482989dca7615eb4edaaf3f06` |
| `docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json` | `22fec026bad79e0d8ec10bff215385c10fdee931213702bd67e4cebea47ec238` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json` | `26d483db1f25930b40cd2389a16de1e30f01973723adcf5afb54d8b18d2f9191` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json` | `5cc56c562ce7145f6a1b8095beb924eae41624e285efa26e67db7c155bddd565` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `097e783c7c94d460be829e022a72edd2689c61892cdd2bec2353648886be6437` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `3b6e0a8cd95d1f527d3a77dc67c99622af788eecebd41713af2c3ccee2a7d09b` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `2254529f1f89975633ae77e3407f2b580cc7a88d2421ef348956d54fac99e3f1` |
| `experiments/prime_matrix_phi_lpf_minimal_parity_breaker_route_forcing_router.py` | `aae4cac385f5fd4faf48d36205a8f6e99d48f8ca08d12338ba2c7e9d9951661a` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `79962e655b583ce8daa771e8bd57d796cded5b68dc1d580e163df3f1aa7f419f` |

三命题仍未无条件闭合。
