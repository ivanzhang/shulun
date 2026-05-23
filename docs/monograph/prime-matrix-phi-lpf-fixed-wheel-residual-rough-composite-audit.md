# Prime Matrix Phi-LPF fixed-wheel rough-composite residual 审计

**状态：** `fixed_wheel_capacity_gap_equals_rough_composite_residual`
**核验日期：** `2026-05-23`

## 1. 原子分解

设 `S` 为固定 wheel primes，`C_S(P,k)` 为删去 `S` 强迫合成 cofactor 后的容量。
把剩余候选分成两类：prime cofactor forest holes 与仍未被删掉的合成 cofactor。
记后者为 `R_S(P,k)`，则有精确恒等式：

```text
C_S(P,k)=|F(P,k)|+R_S(P,k)
DeltaPhi_half(P,k)-C_S(P,k)=N(P,k)-R_S(P,k)
N(P,k)=pi((k+1)P-1)-pi(kP)
```

因此固定 wheel 的 `DeltaPhi_half>C_S` 不是目标本身，而是更强的
`N(P,k)>R_S(P,k)`。这就是当前可见的 rough-composite residual 硬点。

## 2. 有限审计

```text
max_prime=1009
row_count=76789
all_sqrt_residual_zero=true
all_fixed_capacity_decomposition_holds=true
all_delta_minus_capacity_equals_prime_minus_residual=true
finite_evidence_not_used_as_global_proof=true
```

| layer | residual>0 rows | max R | min primes-R | total R | R/primes | max-R row |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2-wheel | 56619 | 46 | 0 | 892548 | 0.213913 | P=997, k=996 |
| 6-wheel | 54897 | 31 | 1 | 469209 | 0.112453 | P=971, k=936 |
| 30-wheel | 52697 | 23 | 1 | 299977 | 0.071894 | P=971, k=936 |
| 210-wheel | 49388 | 18 | 1 | 203277 | 0.048718 | P=773, k=755 |
| 2310-wheel | 45472 | 14 | 1 | 151197 | 0.036237 | P=769, k=759 |
| 30030-wheel | 39964 | 12 | 1 | 107093 | 0.025666 | P=983, k=929 |
| sqrt(2P)-wheel | 0 | 0 | 1 | 0 | 0.000000 | P=11, k=2 |

代表样本：

| P | k | Delta | primes | holes | R_30 | R_210 | R_2310 | R_sqrt | primes-R_30 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 10 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 19 | 15 | 3 | 1 | 2 | 0 | 0 | 0 | 0 | 1 |
| 101 | 100 | 16 | 12 | 4 | 1 | 1 | 0 | 0 | 11 |
| 257 | 256 | 29 | 23 | 6 | 3 | 3 | 2 | 0 | 20 |
| 1009 | 1008 | 89 | 70 | 19 | 9 | 8 | 7 | 0 | 61 |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sample_sqrt_residual_zero=true
large_samples_are_evidence_not_global_proof=true
```

| layer | residual>0 rows | max R | min primes-R | total R | R/primes | max-R row |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2-wheel | 4 | 7172 | 1769 | 11293 | 0.115343 | P=300007, k=300006 |
| 6-wheel | 4 | 4302 | 2781 | 6793 | 0.069381 | P=300007, k=300006 |
| 30-wheel | 4 | 3213 | 3215 | 5050 | 0.051579 | P=300007, k=300006 |
| 210-wheel | 4 | 2552 | 3453 | 4019 | 0.041049 | P=300007, k=300006 |
| 2310-wheel | 4 | 2197 | 3598 | 3437 | 0.035104 | P=300007, k=300006 |
| 30030-wheel | 4 | 1930 | 3691 | 3016 | 0.030804 | P=300007, k=300006 |
| sqrt(2P)-wheel | 0 | 0 | 4385 | 0 | 0.000000 | P=100003, k=2 |

## 4. 极限含义

当 wheel primes 覆盖所有 `ell<=sqrt(2P-1)` 时，每个合成 `m<2P` 都被删去，
所以 `R_S(P,k)=0`，容量退化为 `C_S=|F|`。这给出精确目标等价式，
但不提供新的正性来源。

对任何固定 wheel，剩下的 `R_S` 是 LPF 大于 wheel 边界的 rough composite。
继续加有限 wheel 只是在缩小 `R_S`；全局闭合必须证明同一行的素数数
支配这些 residual，或引入真正的 signed/dispersion/平方相位结构输入。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FixedWheelResidualDecomposition | `true` | `true` | 任意固定 wheel 的容量精确拆成 prime-cofactor holes 加 rough-composite residual。 | C_S(P,k)=\|F(P,k)\|+R_S(P,k) |
| FixedWheelPositivityRequiresPrimeDominatesResidual | `true` | `true` | DeltaPhi_half>C_S 等价于行内素数数 N(P,k) 严格大于 R_S(P,k)。 | PrimeCountDominatesFixedWheelRoughCompositeResidual |
| SqrtWheelResidualVanishes | `true` | `true` | wheel primes 覆盖所有 ell<=sqrt(2P-1) 时，每个合成 m<2P 被删除，R_S=0。 | dynamic exact wheel |
| FixedWheelResidualDominanceProvedGlobally | `false` | `false` | 有限审计显示固定 wheel residual 被素数数支配，但尚无全局证明。 | signed dispersion or special square-phase lower bound required |
| PhiLPFParityBarrierBrokenGlobally | `false` | `false` | 本层只是把奇偶障碍剩余项显式物化；没有证明全局半窗素数存在。 | same-object prime-minus-rough-composite separation required |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 6. 当前最窄口

```text
PrimeCountDominatesFixedWheelRoughCompositeResidual OR same-object signed dispersion OR special square-phase lower bound
```

```text
fixed_wheel_residual_decomposition_closed=true
sqrt_wheel_residual_zero_closed=true
fixed_wheel_residual_dominance_global_closed=false
primorial_limit_independent_proof=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
