# Prime Matrix affine `2n+1` Euler-LPF parity audit

**状态：** `affine_2n_plus_1_sieve_bijection_closed_half_main_is_missing_p2_not_error`
**核验日期：** `2026-05-25`

## 1. 关键修正

对奇素数 `P`，若

```text
n = kP + (P-1)/2,
```

则

```text
2n+1 = (2k+1)P.
```

`P` 是 `2n+1` 的因子，不是 `n` 的因子。若 `k>=1` 且 `2k+1` 没有小于 `P` 的素因子，则 `P=LPF(2n+1)`。

## 2. affine 筛余双射

映射 `m=2n+1` 给出精确等价：

```text
p | m  <=>  n == (p-1)/2 mod p       (p odd)
```

因此 `m` 避开所有 `0 mod p` 等价于 `n` 避开所有 `(p-1)/2 mod p`。

## 3. 有限审计读数

| P | x=P^2 | survivors | prime m | rough composite | forced class | LPF(2n+1)=P | naive missing-p2 gap/main |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 121 | 51 | 48 | 2 | 10 | 4 | 0.494985 |
| 31 | 961 | 290 | 282 | 7 | 30 | 8 | 0.506693 |
| 101 | 10201 | 2355 | 2279 | 75 | 100 | 21 | 0.515537 |
| 251 | 63001 | 12099 | 11765 | 333 | 250 | 42 | 0.521583 |
| 1009 | 1018081 | 155132 | 151285 | 3846 | 1008 | 138 | 0.529033 |

所有样本均满足：

```text
affine_sieve_bijection_verified_all_samples=true
euler_product_half_main_error_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

## 4. 半主项现象的解释

若在 `m` 侧用长度约 `2x` 的区间却只乘奇素数部分的欧拉乘积，就会得到约为正确主项两倍的 naive main term。这时 exact count 与 naive main term 的差看起来约为 naive main 的 `1/2`。

但这不是有限欧拉乘积截断误差的主项级定理；它只是漏掉 `p=2` 或没有先限制到奇数样本空间造成的归一化错误。在正确的 odd-space 或含 `p=2` 的公式中，`m` 侧和 `n` 侧主项已经对齐。

## 5. 与 LPF/Phi 递推的关系

该恒等式可以作为 shifted-residue Phi-LPF 账本迭代：每个奇素数 `p` 的零类在 `m` 侧变成 `n` 侧的 `(p-1)/2` 类。它能精确登记 `2n+1` 的 LPF owner，尤其是强制类 `n=(P-1)/2 mod P`。

但它仍只给筛余集合。样本中 `rough_composite` 大量存在，说明 affine 转移没有把 rough survivors 分离成素数。要变成突破，仍需构造 signed payload/trace family 或 named PDEC/SAE return。

## 6. 最新开放口

```text
AffineShiftedResidueSieveSignedPayloadConstructorOrReturn AND PrimeExtractionFrom2nPlus1RoughSurvivorsBeyondParity
```

状态边界：

```text
euler_product_half_main_error_proved=false
prime_extraction_from_2n_plus_1_rough_survivors_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
