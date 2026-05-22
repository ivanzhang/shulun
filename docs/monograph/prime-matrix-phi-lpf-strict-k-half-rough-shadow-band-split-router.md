# Prime Matrix Phi-LPF strict-k half-rough shadow band split 证书

**状态：** `strict_k_prime_count_equals_half_rough_survivor_excess_over_two_prime_shadow`

本层把上一层留下的高 `k` 平方边界带继续 half-rough 化。对素数底 `P` 和 `1<k<P`，定义

```text
R_half(P,k)=#{1<=t<P: gcd(kP+t, product_{q<=P/2} q)=1}
T_half(P,k)=#{q,m prime: P/2<q<=m<2P, kP<qm<(k+1)P}.
```

则有精确恒等式：

```text
pi((k+1)P-1)-pi(kP)=R_half(P,k)-T_half(P,k).
```

## 1. 结构证明读法

若 `kP+t` 避开所有 `q<=P/2` 而仍合成，则其最小素因子 `q` 必满足 `P/2<q<P`。
写 `kP+t=qm`，由 `k<P` 得 `m<2P`。当 `P>=11` 时，`m` 不可能合成；
否则 `m` 的素因子都至少为 `q>P/2`，从而 `m>=q^2>P^2/4>2P`。
为避免双计数，shadow 只取 `q<=m`。于是每个 composite half-rough survivor
与一个唯一的双素数 shadow 对应。

同时，如果

```text
4*((k+1)P-1)<=P^2,
```

则整行低于 `P^2/4`，而任意 `q,m>P/2` 的乘积都大于 `P^2/4`，所以 `T_half(P,k)=0`。
这把 BHP bulk 之后的高 `k` 带再分成 shadow-free survivor 非空问题和 upper-band
semiprime-shadow excess 问题。

## 2. 有限审计

```text
max_prime=1009
prime_base_count=165
all_half_rough_shadow_identities_hold=true
identity_failure_count=0
finite_evidence_not_used_as_global_proof=true
```

最小余量样本：

```text
P=11, k=10, R=2, T=1, direct=1
```

高带最小余量读数：

```text
P=11, first_high_k=9, min_high_margin=1
```

## 3. 样本表

| P | k | R_half | T_shadow | R-T | direct primes | high band | shadow-free |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 11 | 2 | 3 | 0 | 3 | 3 | `false` | `false` |
| 11 | 9 | 4 | 0 | 4 | 4 | `true` | `false` |
| 11 | 10 | 2 | 1 | 1 | 1 | `true` | `false` |
| 101 | 2 | 16 | 0 | 16 | 16 | `false` | `true` |
| 101 | 66 | 14 | 2 | 12 | 12 | `true` | `false` |
| 101 | 100 | 16 | 4 | 12 | 12 | `true` | `false` |
| 257 | 2 | 39 | 0 | 39 | 39 | `false` | `true` |
| 257 | 152 | 31 | 4 | 27 | 27 | `true` | `false` |
| 257 | 256 | 29 | 6 | 23 | 23 | `true` | `false` |
| 1009 | 2 | 128 | 0 | 128 | 128 | `false` | `true` |
| 1009 | 523 | 80 | 9 | 71 | 71 | `true` | `false` |
| 1009 | 1008 | 89 | 19 | 70 | 70 | `true` | `false` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| StrictKHalfRoughShadowIdentityClosed | `true` | `true` | 对每个 1<k<P，N_P(k) 精确等于 q<=P/2 后的 half-rough survivor 减去 q,m>P/2 的双素数 shadow。 | exact identity |
| CompositeHalfRoughSurvivorForcesTwoPrimeShadow | `true` | `true` | 若 kP+t 避开所有 q<=P/2 且仍合成，则其 LPF q 在 (P/2,P)，商 m<2P 且必须为素数。 | none for structural split |
| BHPRemainingHighBandShadowFreeSubbandSeparated | `true` | `true` | 当整行位于 P^2/4 以下时，q,m>P/2 的 shadow 不可能出现；该子带只剩 half-rough survivor 非空性。 | HalfRoughSurvivorExistenceInShadowFreeHighBand |
| UpperSquareBandReducedToSemiprimeShadowExcess | `true` | `true` | 在 P^2/4 以上的高 k 带，失败必须表现为双素数 shadow 吃掉全部 half-rough survivor excess。 | HighKHalfRoughSurvivorExcessOverTwoPrimeShadow |
| FiniteSweepIdentityMatchesDirectPrimeCount | `true` | `true` | 有限审计确认 exact identity 与直接素数计数一致，但不作为全局证明。 | finite audit only |
| HighKSquareBandPositivityProved | `false` | `false` | 本层没有证明 half-rough survivor 非空性或 shadow excess 的全局下界。 | HalfRoughSurvivorExistenceInShadowFreeHighBand OR HighKHalfRoughSurvivorExcessOverTwoPrimeShadow |
| UnifiedPositiveCoreProved | `false` | `false` | 本层继续压缩非循环剩余，但不证明三目标命题无条件闭合。 | sqrt-scale theorem or structural high-k half-rough excess |

## 5. 结论

高 k 平方边界带现在不再需要完整 LPF 树。每一行的素数数等于 half-rough survivor 减去唯一的 q,m>P/2 双素数 shadow。低于 P^2/4 的剩余子带 shadow 为零，只需证明 half-rough survivor 非空；高于 P^2/4 的子带则变成 survivor 严格多于 two-prime shadow。

当前最窄直接主攻口更新为：

```text
HalfRoughSurvivorExistenceInShadowFreeHighBand OR HighKHalfRoughSurvivorExcessOverTwoPrimeShadow
```

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把高 `k` 真剩余
压成更短的 survivor 非空和 two-prime shadow excess 两个接口。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json` | `f3f48c40a68ca892665fdc763803d616619ac104127aebb783f7f921c6fcbf54` |
| `docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json` | `c5ca8b97bf9f6dc2c5abaec3dd7f4ba612a3996df98696b3b01167e2b076f936` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json` | `8ab6da3a1ad8bb73f3b4511f503c5914984cfeb1d8b62e05dcb63ce41ea6b381` |
