# Prime Matrix Phi-LPF top-row half-rough semiprime shadow 证书

**状态：** `top_row_prime_count_equals_half_rough_survivor_excess_over_reciprocal_semiprime_shadow`

本层把 prime-indexed Oppermann-left 顶行尾段再压缩一层。定义

```text
R_1/2(P)=#{1<=r<P: gcd(P^2-r, product_{q<=P/2} q)=1}
T_1/2(P)=sum_{P/2<q<P, q prime}
  #{m prime: floor((P^2-P)/q)<m<=floor((P^2-1)/q)}.
```

则有精确恒等式：

```text
pi(P^2-1)-pi(P^2-P)=R_1/2(P)-T_1/2(P).
```

因此顶行正性不再需要处理完整 LPF 树；它等价于 half-rough survivor
严格多于 reciprocal prime-semiprime shadow。

## 1. 结构证明读法

若 `P^2-r` 避开所有 `q<=P/2` 而仍合成，则它的最小素因子 `q` 必满足：

```text
P/2<q<P.
```

写 `P^2-r=qm`。由于 `P^2-P<P^2-r<P^2`，得到：

```text
P<m<2P.
```

且 `m` 必为素数；否则 `m` 的素因子都不小于 `q>P/2`，从而 `m>=q^2>2P`
（`P>=11`；小素数底在有限审计中直接覆盖）。对每个固定 `q in (P/2,P)`，
`m` 的可行窗口长度为 `P/q<2`，所以每个 `q` 至多贡献两个 reciprocal 候选。

## 2. 有限审计

```text
max_prime=5003
prime_base_count=668
all_half_rough_identities_hold=true
identity_failure_count=0
minimum_half_rough_minus_shadow=1
finite_evidence_not_used_as_global_proof=true
```

极小余量样本：

```text
P=5, R=2, T=1, direct=1; P=11, R=2, T=1, direct=1
```

最高 shadow 比例样本：

```text
P=37, R=6,
T=4,
ratio=0.666667
```

## 3. 样本表

| P | R_half | T_shadow | R-T | direct primes | high q | max cand/q |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 2 | 1 | 1 | 1 | 1 | 2 |
| 7 | 2 | 0 | 2 | 2 | 1 | 1 |
| 11 | 2 | 1 | 1 | 1 | 1 | 2 |
| 17 | 3 | 0 | 3 | 3 | 2 | 2 |
| 101 | 16 | 4 | 12 | 12 | 10 | 2 |
| 257 | 29 | 6 | 23 | 23 | 23 | 2 |
| 1009 | 89 | 19 | 70 | 70 | 72 | 2 |
| 5003 | 330 | 49 | 281 | 281 | 302 | 2 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| HalfRoughSplitIdentityClosed | `true` | `true` | 顶行素数数精确等于避开 q<=P/2 的平方相位幸存量减去 reciprocal prime-semiprime shadow。 | exact identity |
| CompositeHalfRoughForcesTwoPrimeShadow | `true` | `true` | 若 P^2-r 避开所有 q<=P/2 且仍合成，则其 LPF q 在 (P/2,P)，商 m 在 (P,2P) 且为素数。 | none for structural split |
| EachHighQHasAtMostTwoReciprocalCandidates | `true` | `true` | 对 q in (P/2,P)，m 的 reciprocal window 长度为 P/q<2，因此每个 q 至多给两个候选 m。 | candidate count only; prime filtering remains |
| FiniteSweepIdentityMatchesDirectPrimeCount | `true` | `true` | 有限审计确认 R_{1/2}-T_{1/2} 与直接顶行素数计数一致，但不作为全局证明。 | finite audit only |
| HalfRoughExcessProvedUniformly | `false` | `false` | 尚未证明所有尾段素数 P 都满足 R_{1/2}(P)>T_{1/2}(P)。 | HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow |
| UnifiedPositiveCoreProved | `false` | `false` | 本层只把顶行尾段硬点压成 half-rough excess；没有证明 strict 全行正性。 | SquarePhaseTailLongBlockPDECExclusion OR HalfRoughExcess |

## 5. 结论

当前顶行尾段的真剩余已经从“低筛全覆盖”进一步变为单一不等式：

```text
HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow:
  R_1/2(P)>T_1/2(P) for every remaining prime P.
```

若这个不等式成立，则 `PrimeIndexedOppermannLeftHalf(P)` 成立；若失败，则失败不是
匿名容量问题，而是 `(P/2,P)` 与 `(P,2P)` 的 reciprocal prime-semiprime shadow
铺满了全部 half-rough survivor，应登记为 square-phase/semiprime-shadow PDEC。

本层仍不证明 `UnifiedPositiveCore` 或行/列命题；它只把无限尾段硬点压到更窄的
half-rough excess 接口。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json` | `8ab6da3a1ad8bb73f3b4511f503c5914984cfeb1d8b62e05dcb63ce41ea6b381` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json` | `3ebb0f9350f9f3fd7b67ef5b4bf6d3cc407462439520a5e06e4a810b6f208489` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json` | `6180246c2e8eae53ef5b16c3731190746c95a781e528a85d08188efbc328ee6c` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json` | `328ee462d76cb6213f976eee33133885f20109157d16cf80d236ae27d78d8993` |
