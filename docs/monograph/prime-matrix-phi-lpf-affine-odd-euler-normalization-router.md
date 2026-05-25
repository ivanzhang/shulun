# Prime Matrix Phi-LPF affine odd Euler normalization 证书

**状态：** `affine_odd_euler_normalization_closed_no_half_error_saving`
**核验日期：** `2026-05-25`

本证书审计 `m=2n+1` 仿射提升与有限欧拉乘积截断之间的关系。

## 1. 结论

```text
affine_forbidden_class_bijection_verified=true
finite_euler_product_full_with_p2_equals_affine_odd_main=true
finite_euler_product_half_error_claim_supported=false
p2_normalization_explains_factor_two=true
lpf_bucket_identity_verified=true
phi_lpf_iteration_route_closes_parity_barrier=false
row_column_unconditional_closed=false
```

关键判断：有限欧拉乘积中长度为两倍的区间并不会推出“截断误差是主项的 `1/2` 量级”。等式来自

```text
2X*(1-1/2)*prod_{3<=p<=Y}(1-1/p) = X*prod_{3<=p<=Y}(1-1/p)
```

也就是完整区间里的 `p=2` 因子把长度 `2X` 归一化为奇数轴长度 `X`。

## 2. 仿射双射审计

| X | Y | odd primes | survivors | primes 2n+1 | product-main | full-with-p2-main | remainder/main |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 14 | 5 | 40 | 45 | 38.361638 | 38.361638 | 0.042708 |
| 1000 | 44 | 13 | 289 | 302 | 283.438798 | 283.438798 | 0.019620 |
| 10000 | 141 | 33 | 2228 | 2261 | 2227.306808 | 2227.306808 | 0.000311 |
| 50000 | 316 | 64 | 9527 | 9591 | 9651.938697 | 9651.938697 | -0.012944 |

`survivors` 同时是 `n<=X` 避开所有 `n=(p-1)/2 mod p` 的数量，
也是 `m=2n+1<=2X+1` 避开所有奇素数零同余类的数量。二者逐点相同，
不是渐近相同。

## 3. LPF 桶定位审计

```text
n=kP+(P-1)/2 gives 2n+1=P(2k+1); for k>=1 and LPF(2k+1)>=P, LPF(2n+1)=P
```

| P | rough cofactor cases | LPF identity verified | failures |
| --- | --- | --- | --- |
| 3 | 400 | true | 0 |
| 5 | 266 | true | 0 |
| 7 | 213 | true | 0 |
| 11 | 182 | true | 0 |
| 17 | 151 | true | 0 |
| 31 | 129 | true | 0 |
| 61 | 122 | true | 0 |
| 97 | 115 | true | 0 |

`k=0` 是端点例外：此时 `2n+1=P` 为素数，不是合数；LPF 仍为 `P`。

## 4. 对 Phi-LPF 路线的含义

这条仿射归一化可以与 Phi 递推和 LPF 分桶迭代：每个奇素数的零类
`m=0 mod p` 精确拉回为 `n=(p-1)/2 mod p`。因此它适合用来校准
row/column 账本、避免把 `p=2` 归一化误读成误差。

但它不产生奇偶性突破所需的 signed cofactor saving：避开小素数后的 surviving
集合仍混合 primes、P2 与更高合数。要继续推进，必须把该仿射账本接到
terminal payment/PDEC、moving Beatty numerator 的相位节省，或构造可调用
Kloosterman/Type-II 的 admissible signed trace family。

## 5. 最新开放口

```text
AffineOddLiftOnlyNormalizesParityNoSignedSaving AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_affine_odd_euler_normalization_router.py` | `bfa69328e638144e50f1ad0913d276c00f2f9f4955743efa5268ed25c1eb187d` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-router.json` | `e6acbc156cd7658d81046c8f5269a1999908e12e9c9cca3ea71a5f154fbdc16c` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `dc558499b99cc0e926cae0ba4356218fdbf6419b578bd39fd6c48f53deb34190` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `78e390501b1403c478b0d7b5e8320790f266c03eb1195a8e450ed65c025a8a96` |
| `docs/monograph/external-theorem-index.md` | `9469c102d6d6de757d73e883948d419684095620357355d900b11bd05dfb7f73` |
