# Prime Matrix Phi-LPF primorial-wheel limit 审计

**状态：** `primorial_wheel_ladder_tightens_but_limit_is_exact_tautology`
**核验日期：** `2026-05-23`

## 1. 直接回答

可以继续从 `30` 推进到 `210, 2310, ...`，而且容量会单调收紧。
但这条路线的极限不是自动证明；当 wheel primes 覆盖到 `sqrt(2P)` 后，
`C_wheel(P,k)` 已经等于真实 forest-hole 数 `|F(P,k)|`。
于是 `DeltaPhi_half(P,k)>C_wheel(P,k)` 正好等价于行内素数存在。

## 2. 有限层审计

```text
max_prime=1009
row_count=76789
all_exact_capacity_equals_holes=true
all_exact_margin_equals_direct_prime_count=true
finite_evidence_not_used_as_global_proof=true
```

| layer | closed | not closed | min Delta-C | min row |
| --- | ---: | ---: | ---: | --- |
| 2-wheel | 76788 | 1 | 0 | P=19, k=15 |
| 6-wheel | 76789 | 0 | 1 | P=11, k=10 |
| 30-wheel | 76789 | 0 | 1 | P=11, k=10 |
| 210-wheel | 76789 | 0 | 1 | P=11, k=10 |
| 2310-wheel | 76789 | 0 | 1 | P=11, k=10 |
| 30030-wheel | 76789 | 0 | 1 | P=11, k=10 |
| sqrt(2P)-wheel | 76789 | 0 | 1 | P=11, k=10 |

代表样本：

| P | k | Delta | W_int | C_30 | C_210 | C_2310 | C_sqrt | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 10 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| 19 | 15 | 3 | 5 | 2 | 2 | 2 | 2 | 2 | 1 |
| 101 | 100 | 16 | 14 | 5 | 5 | 4 | 4 | 4 | 12 |
| 257 | 256 | 29 | 34 | 9 | 9 | 8 | 6 | 6 | 23 |
| 1009 | 1008 | 89 | 101 | 28 | 27 | 26 | 19 | 19 | 70 |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sample_exact_capacity_equals_holes=true
large_samples_are_evidence_not_global_proof=true
```

大样本 layer 最小余量：

```text
2-wheel: min Delta-C=1769, all_positive=true
6-wheel: min Delta-C=2781, all_positive=true
30-wheel: min Delta-C=3215, all_positive=true
210-wheel: min Delta-C=3453, all_positive=true
2310-wheel: min Delta-C=3598, all_positive=true
30030-wheel: min Delta-C=3691, all_positive=true
sqrt(2P)-wheel: min Delta-C=4385, all_positive=true
```

## 4. 极限判定

若 wheel primes 覆盖到 `sqrt(2P-1)`，则每个合数 `m<2P` 都有一个已覆盖素因子。
因此 reciprocal cofactor 窗中未被删除的 `m` 恰好是素数，容量上界变成精确等式：

```text
C_sqrt(P,k)=|F(P,k)|
DeltaPhi_half(P,k)-C_sqrt(P,k)=pi((k+1)P-1)-pi(kP)
```

这说明 primorial ladder 的极限是目标命题的等价重述，不是独立闭合证明。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FinitePrimorialWheelLadderMonotoneTightening | `true` | `true` | 2,6,30,210,2310,... wheel 只会删除 forced-composite cofactor 候选，容量单调不增。 | capacity ladder registered |
| SqrtCofactorWheelEqualsActualForestHoles | `true` | `true` | 当 wheel primes 覆盖到 sqrt(2P) 时，每个 m<2P 的合数都有已覆盖小因子，故容量等于真实 prime-cofactor forest holes。 | exact hole count |
| InfinitePrimorialLimitIsIndependentProof | `false` | `false` | 极限容量等于 \|F(P,k)\| 后，DeltaPhi_half>C_limit 正是行内素数存在本身。 | positivity still required |
| PhiLPFParityBarrierBrokenGlobally | `false` | `false` | primorial wheel 极限是精确化，不是 signed dispersion、sqrt-scale 短区间或新自守端点证明。 | signed/dispersion or structural lower bound required |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 6. 当前最窄口

```text
PuncturedSqrtWheelExactForestHolePositivityOrSignedDispersionOrSpecialSquarePhaseLowerBound
```

```text
primorial_wheel_ladder_tightened=true
sqrt_wheel_limit_exact=true
primorial_limit_independent_proof=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
