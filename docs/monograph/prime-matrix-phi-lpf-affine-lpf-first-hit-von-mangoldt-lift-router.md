# Prime Matrix Phi-LPF affine LPF first-hit von Mangoldt lift 证书

**状态：** `von_mangoldt_lift_exact_global_divisor_payload_required`
**核验日期：** `2026-05-25`

本证书审计 LPF first-hit 分割能否直接升级为 prime extraction。结论是：
von Mangoldt lift 是精确的，但它需要全局 Mobius divisor signed payload，
不是 LPF-local unsigned count。

## 1. 精确身份

```text
Lambda(m) = sum_{d|m} mu(d) log(m/d)
Lambda(m) = log p  if m=p^a
Lambda(m) = 0      otherwise
```

端点素数 `m=p` 的 `log p` 质量被分离出来；合数尾中的 prime powers 仍携带
`Lambda` 质量，非 prime powers 只能通过 Mobius divisor signed sum 抵消。

## 2. 审计读数

```text
mobius_von_mangoldt_identity_closed=true
lpf_first_hit_identity_imported_and_verified=true
tail_prime_power_leak_present=true
nonprimepower_tail_cancelled_only_by_mobius_divisor_sum=true
lpf_local_unsigned_count_sufficient_for_prime_extraction=false
global_divisor_signed_payload_required=true
admissible_typeii_or_trace_family_constructed=false
row_column_unconditional_closed=false
```

| X | M | endpoint primes | composite tails | tail prime powers | tail non-prime-powers | prime-power Lambda fraction |
| --- | --- | --- | --- | --- | --- | --- |
| 100 | 201 | 45 | 55 | 8 | 47 | 0.066686 |
| 1000 | 2001 | 302 | 698 | 21 | 677 | 0.024339 |
| 10000 | 20001 | 2261 | 7739 | 53 | 7686 | 0.008123 |
| 50000 | 100001 | 9591 | 40409 | 93 | 40316 | 0.003556 |

## 3. 外部前沿边界

| input | usable now | reason |
| --- | --- | --- |
| [Milicevic-Qin-Wu arbitrary-modulus Kloosterman bilinear forms](https://arxiv.org/abs/2511.07550) | `false` | requires a completed bilinear Kloosterman family; raw LPF first-hit tail is not such a family |
| [Pascadi non-abelian composite-modulus Kloosterman Type-II](https://arxiv.org/abs/2511.08445) | `false` | requires composite-modulus Type-II sums with admissible coefficients, not unsigned LPF bucket counts |
| [Matomaki-Radziwill-Shao-Tao-Teravainen 2026 almost-all short-interval Lambda uniformity](https://link.springer.com/article/10.1007/s00222-026-01408-6) | `false` | almost-all short interval uniformity does not give pointwise every-residue positivity at x=P^2 |
| [Dong-Robles-Zeindler Kloosterman fractions 2601.00292](https://arxiv.org/abs/2601.00292) | `false` | withdrawn; cannot be used as an active theorem input |

这些输入都要求先有 admissible signed family、Type-II family 或 completed
trace/Kloosterman family。当前 LPF first-hit tail 只是精确分割后的无符号对象。

## 4. 最新开放口

```text
VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount AND PointwiseThetaAPPositivityAtP2OrAdmissibleSignedDivisorPayloadTypeIIFamily AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_affine_lpf_first_hit_von_mangoldt_lift_router.py` | `42aee67259e3249116df8c63ae2511f2b12b34c385a0bd401bb759c860a26832` |
| `docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json` | `984f9ab9a328383ff5f21275dcf054fae0ed8e4349170bf2c7f70d53a4e2c251` |
| `docs/monograph/prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json` | `6f0a674fbf664cebc3a17c49a62fb8757a8ca3dd004403d023c0fc1746c23ecc` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-router.json` | `e6acbc156cd7658d81046c8f5269a1999908e12e9c9cca3ea71a5f154fbdc16c` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `9a8508a1b3bd0bc866101b0d1cb0ba5b349d39f57279e482184c192b88fbf7e0` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `f29b3902f2ca585ee50338b5a58ba412f3d6003412b433fbc1f4e17e38560879` |
| `docs/monograph/external-theorem-index.md` | `07b5aecd9b826b58ff73dea05d2610bf3a710d4101a9f688e381112af9d2bb45` |
