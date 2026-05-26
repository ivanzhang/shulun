# Prime Matrix Phi-LPF parity barrier prime-distribution contract 路由

**状态：** `parity_barrier_contract_pinned_prime_distribution_formula_open`
**核验日期：** `2026-05-26`

## 1. 本质裁定

无符号粗数信息即使在 LPF/Phi 层面完全精确，也不能把素数从两个或更多大素因子的乘积中分离出来。缺失的数据不是另一个 Euler-product 支撑计数，而是有符号除子/trace 相消，或逐点素数分布下界。

```text
lpf_bucket_exact_formula=C_p(N)=Phi(floor(N/p); primes< p)-1
lpf_correction_closed=true
legendre_periodic_boundary_not_half_main=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
pure_power_selector_supplies_additive_signed_distribution_family=false
pointwise_psi_row_lower_bound_beyond_tail_proved=false
trace_or_typeii_family_admissible_now=false
row_column_unconditional_closed=false
```

## 2. 真正需要的素数分布合同

| contract | formula | why it breaks parity | current status |
| --- | --- | --- | --- |
| `PointwiseThetaShortIntervalAtSqrtScale` | theta((kP,(k+1)P))>0 for every odd prime P and 1<k<P | 直接数素数，而不是数粗数 survivor | 未证明；在硬区间内等价于逐行素数存在目标 |
| `PsiBeyondPrimePowerTail` | psi((kP,(k+1)P)) > prime_power_tail((kP,(k+1)P)) | von Mangoldt 质量超过纯素幂尾巴时强制出现素数 | 尾巴等价已审计；点态 psi 下界仍未证明 |
| `SignedMobiusVonMangoldtTypeITypeII` | uniform Type-I/II or Vaughan/Heath-Brown decomposition with source-key consistency | 有符号除子相消能区分素数与 P2/P3 粗合数 | 当前 PM payload 尚未构造 admissible family |
| `TraceKloostermanFamilyFromQSpineHinge` | completed source-keyed Kloosterman/trace sums with conductor and coefficient control | 谱/trace 相消能分离 LPF 支撑不可见的有符号相位 | formal Jordan kernel 与 shared hinge 仍是有限账本；admissible family 未构造 |
| `NamedPDECOrSAEReturn` | failure of a uniform law returns to a controlled PDEC/SAE/local-survivor contradiction | 把 parity-blind 失败变成结构不可能性，而不是继续计数 | 多个有限 PDEC 接口已命名；尚无全局回流闭合目标命题 |

## 3. 可绕行路线

| route | move | hard atom |
| --- | --- | --- |
| Spectral/Kuznetsov or trace-function route | 把 terminal/q-spine 相位提升为 completed signed trace 或 Kloosterman family | source-key lift、Type-II 系数可分解性、conductor control |
| Harman/Vaughan signed-sieve route | 在同一 row load 上用 Lambda/Mobius 加权分解替代 LPF 支撑计数 | 逐行点态下界，或零例外 AP/短区间定理 |
| Shared-pivot PDEC route | 证明 shared-pivot hinge 或 endpoint slack law 的失败会产生命名不可能 packet | uniform hinge law 或 controlled PDEC/SAE return |
| Finite-group/expander route | 把 q-spine motion 编码成具有 expansion 与 anti-concentration 的真实 group orbit | 构造 group action；当前 q-spine 只是有限 hinge ledger |
| Dynamical adjacent-run cancellation route | 证明 terminal signed payload 的 uniform adjacent-run cancellation | same-trace-key consistency 与关于 P 的 uniform family |

## 4. 外部前沿输入边界

| input | url | directly closes now | blocker |
| --- | --- | --- | --- |
| Fouvry-Kowalski-Michel-Sawin trace functions | https://arxiv.org/abs/2511.09459 | `false` | terminal/hinge ledger is finite and not yet a uniform trace-function family |
| Milićević-Qin-Wu arbitrary-modulus Kloosterman bilinear forms | https://arxiv.org/abs/2511.07550 | `false` | current PM object is a finite pivot/right-tail/adjacent-run ledger, not a completed bilinear family |
| Wright trilinear Kloosterman fractions | https://arxiv.org/abs/2604.25177 | `false` | no source-key lift, no trilinear convolution, and no beta-sequence equidistribution object has been constructed |
| Runbo Li large-modulus AP primes and Harman sieve refinements | https://arxiv.org/abs/2602.20917 | `false` | Prime Matrix needs pointwise row/column actual load at x=P^2, not almost-all moduli distribution |
| Becker-Breuillard uniform spectral gaps and anti-concentration | https://arxiv.org/abs/2512.15364 | `false` | the present q-spine pivot ledger is not a group orbit and has no Cayley/expander model |
| Pascadi weighted Type-II / smooth-number distribution | https://arxiv.org/abs/2505.00653 | `false` | current target is pointwise row/column positivity and source-keyed signed load |

## 5. 最新开放口

```text
ParityBarrierContractPinned AND NeedPointwiseThetaOrPsiRowLowerBoundBeyondPrimePowerTail AND NeedAdmissibleSignedDivisorTraceOrTypeIIFamily AND BridgeRootSharedPivotHingeLawOrPDEC AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/external-theorem-index.md` | `c322555581fcd106f1fa740f6f1a7acdae550524c1f10e094c6d9a7f10b531ed` |
| `docs/monograph/prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json` | `ea96150bd831cd8bc6bad2fe47b848ba78ea11325b97faeb5961be4046515c88` |
| `docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json` | `231294a3f0a9cfe6d8af17db958a40f71b1bbfdabcefe3dc5d7c2d1a7a15b72a` |
| `docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json` | `04179593260192cfa899fe1b15997d1467ec678ba64de7c8fc762b2b921ede99` |
| `docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json` | `92468974eceab624e5a553bb3a24e20a85b9e3f5424b674bb9f00057a53ccfc5` |
| `docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json` | `975aa118af686bd729414f291af1efd9fa60082d622ac687d7f87772246acd6e` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json` | `1e885c90848019792545d7e406ae517658a47e8f65b40a94a376b676956c7f5f` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json` | `68d92a76de9afa0228d9e9dae12de19bb4b8189e69397c66c7d967ce4b915b0e` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json` | `5cc56c562ce7145f6a1b8095beb924eae41624e285efa26e67db7c155bddd565` |
| `docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json` | `09d96abf6eb42659f55a40043b65eb521de0da1a706878bd169bde499488ac4f` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `d78c96554009c273d1c5a63939fbc42f00caabb9420acba0d4f15070dc008991` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `da179f2a133401b7e2c8917ea2bac4cc8c891fd3e58ceec6157f668447f145b2` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `c265b1ed5b95883428f692245da7f820feb689dd7f4c969193cab8e7f04d574c` |
| `experiments/prime_matrix_phi_lpf_parity_barrier_prime_distribution_contract_router.py` | `5e8cedf71078548770b227ab757f02a9eb44f6118a7f21c276139aa45f96c0ea` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `2e60d7470e34fd258a18b0ab00a9679ef5d3d5fd02ba2b4d6eb15c0dd996c84c` |

三命题仍未无条件闭合。
