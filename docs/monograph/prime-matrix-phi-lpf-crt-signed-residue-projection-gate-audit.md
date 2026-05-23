# Prime Matrix Phi-LPF CRT signed residue projection gate 审计

**状态：** `fixed_crt_unit_class_dominance_rejected_signed_character_dispersion_required`
**核验日期：** `2026-05-23`

## 1. 原子结论

对固定 wheel `S` 与 `W_S=prod(S)`，定义同一行 signed residue measure：

```text
mu_S(a;P,k) = #{row primes n: n≡a mod W_S}
              - #{S-wheel residual composites n=q*m: n≡a mod W_S}
sum_a mu_S(a;P,k)=N(P,k)-R_S(P,k)
```

若 `P>2 max(S)`，row primes 与 residual atoms 全部落在 `W_S` 的单位剩余类。
因此固定 CRT 逐类支付路线会要求所有单位类 `mu_S(a;P,k)>=0`。
有限审计显示该逐类要求为假：总和为正，但许多单位剩余类为负。

## 2. 有限审计

```text
max_prime=1009
[30-wheel]
modulus=30
stable_row_count=76789
stable_active_residual_row_count=52697
stable_total_prime_count=4172483
stable_total_residual_count=299977
stable_total_surplus=3872506
stable_rows_with_negative_unit_cell_surplus=976
stable_negative_unit_cell_count=998
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=false
[210-wheel]
modulus=210
stable_row_count=76769
stable_active_residual_row_count=49388
stable_total_prime_count=4172431
stable_total_residual_count=203277
stable_total_surplus=3969154
stable_rows_with_negative_unit_cell_surplus=37115
stable_negative_unit_cell_count=67547
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=false
[2310-wheel]
modulus=2310
stable_row_count=76737
stable_active_residual_row_count=45472
stable_total_prime_count=4172321
stable_total_residual_count=151197
stable_total_surplus=4021124
stable_rows_with_negative_unit_cell_surplus=45472
stable_negative_unit_cell_count=151197
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=false
[30030-wheel]
modulus=30030
stable_row_count=76716
stable_active_residual_row_count=39964
stable_total_prime_count=4172236
stable_total_residual_count=107093
stable_total_surplus=4065143
stable_rows_with_negative_unit_cell_surplus=39964
stable_negative_unit_cell_count=107093
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=false
finite_evidence_not_used_as_global_proof=true
```

各层最坏负单位格：

### 30-wheel

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 313 | 183 | 25 | 5 | 20 | 1 | {'residue': 11, 'prime_count': 0, 'residual_count': 4, 'surplus': -4} |

最大 residual 行：

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 971 | 936 | 80 | 23 | 57 | 0 | None |

### 210-wheel

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 463 | 448 | 43 | 5 | 38 | 1 | {'residue': 167, 'prime_count': 0, 'residual_count': 3, 'surplus': -3} |

最大 residual 行：

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 773 | 755 | 52 | 18 | 34 | 9 | {'residue': 31, 'prime_count': 1, 'residual_count': 2, 'surplus': -1} |

### 2310-wheel

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 97 | 92 | 12 | 1 | 11 | 1 | {'residue': 2027, 'prime_count': 0, 'residual_count': 1, 'surplus': -1} |

最大 residual 行：

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 769 | 759 | 51 | 14 | 37 | 14 | {'residue': 1567, 'prime_count': 0, 'residual_count': 1, 'surplus': -1} |

### 30030-wheel

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 157 | 145 | 15 | 1 | 14 | 1 | {'residue': 22831, 'prime_count': 0, 'residual_count': 1, 'surplus': -1} |

最大 residual 行：

| P | k | N | R | N-R | negative unit cells | worst negative cell |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 983 | 929 | 51 | 12 | 39 | 12 | {'residue': 12361, 'prime_count': 0, 'residual_count': 1, 'surplus': -1} |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
[30-wheel]
modulus=30
stable_row_count=10
stable_active_residual_row_count=6
stable_total_prime_count=96550
stable_total_residual_count=10782
stable_total_surplus=85768
stable_rows_with_negative_unit_cell_surplus=0
stable_negative_unit_cell_count=0
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=true
[210-wheel]
modulus=210
stable_row_count=10
stable_active_residual_row_count=6
stable_total_prime_count=96550
stable_total_residual_count=8552
stable_total_surplus=87998
stable_rows_with_negative_unit_cell_surplus=0
stable_negative_unit_cell_count=0
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=true
[2310-wheel]
modulus=2310
stable_row_count=10
stable_active_residual_row_count=6
stable_total_prime_count=96550
stable_total_residual_count=7334
stable_total_surplus=89216
stable_rows_with_negative_unit_cell_surplus=2
stable_negative_unit_cell_count=4
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=false
[30030-wheel]
modulus=30030
stable_row_count=10
stable_active_residual_row_count=6
stable_total_prime_count=96550
stable_total_residual_count=6406
stable_total_surplus=90144
stable_rows_with_negative_unit_cell_surplus=6
stable_negative_unit_cell_count=1505
all_stable_atoms_in_unit_classes=true
fixed_crt_classwise_dominance_holds_on_stable_rows=false
large_samples_are_evidence_not_global_proof=true
```

## 4. 外部定理验收边界

Ford--Maynard prime-producing sieve 的价值在于说明需要目标序列自己的
Type-I/Type-II 信息。本文这一层证明，固定 CRT 单位格逐类匹配不是这种信息：
它只把 `N-R_S` 分解成剩余类 signed mass，而 signed mass 可在局部为负。
因此下一步必须进入 character 平均、跨剩余类的同对象 dispersion，或回到
square-phase endpoint lower bound。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SignedResidueProjectionIdentity | `true` | `true` | 固定 wheel 下 sum_a mu_S(a;P,k)=N(P,k)-R_S(P,k)。 | signed residue ledger |
| StableUnitClassSupportAfterWheel | `true` | `true` | 当 P>2 max(S) 时，row primes 与 S-wheel residual atoms 都落在 W_S 的单位类。 | stable finite exceptions removed |
| FixedCRTClasswiseDominance | `false` | `false` | 有限审计已出现 mu_S(a)<0 的单位类，逐类非负支付路线失败。 | global signed/character dispersion required |
| CRTProjectionBreaksParityBarrier | `false` | `false` | 固定 CRT 投影只重排 signed mass，不提供 prime-minus-tail 全局下界。 | SameRowReciprocalWindowTypeIIDispersionForLPFTail |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 6. 当前最窄口

```text
CharacterAveragedSameRowCRTDispersionForLPFTail OR SameRowReciprocalWindowTypeIIDispersionForLPFTail OR SquarePhaseEndpointLowerBound
```

```text
signed_residue_projection_identity_closed=true
stable_unit_class_support_closed=true
fixed_crt_classwise_dominance_proved=false
character_averaged_dispersion_required=true
prime_count_dominates_lpf_tail_shell_sum_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
