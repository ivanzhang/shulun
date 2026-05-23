# Prime Matrix Phi-LPF LPF shell decrement 审计

**状态：** `fixed_wheel_residual_split_into_lpf_shell_decrement_law`
**核验日期：** `2026-05-23`

## 1. 原子分解

对每个合成 cofactor `m`，令 `r=LPF(m)`。唯一分解为：

```text
m=r*a,  a>=r,  every prime divisor of a is >=r
```

因此 fixed-wheel residual 是 LPF shell 尾和：

```text
R_y(P,k)=sum_{r>y} Shell_r(P,k)
C_y(P,k)-C_y'(P,k)=sum_{y<r<=y'} Shell_r(P,k)
```

这把 residual 从黑箱尾项拆成互斥 LPF 桶；继续加 primorial wheel 的每一步
都只是剥离一个或一段 LPF shell。

## 2. 有限审计

```text
max_prime=1009
row_count=76789
all_lpf_factorizations_ordered=true
all_capacity_reconstructed_from_lpf_shells=true
all_adjacent_decrements_equal_lpf_shells=true
finite_evidence_not_used_as_global_proof=true
```

有限 LPF shell 汇总：

```text
2=1269907
3=423339
5=169232
7=96700
11=52080
13=44104
tail_ge_17=107093
```

代表样本：

| P | k | Delta | N | holes | W_int | C_30 | R_30 | R_210 | R_2310 | R_sqrt | shells |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 10 | 2 | 1 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 2:1 |
| 19 | 15 | 3 | 1 | 2 | 5 | 2 | 0 | 0 | 0 | 0 | 2:2, 3:1 |
| 101 | 100 | 16 | 12 | 4 | 14 | 5 | 1 | 1 | 0 | 0 | 2:7, 3:2, 11:1 |
| 257 | 256 | 29 | 23 | 6 | 34 | 9 | 3 | 3 | 2 | 0 | 2:18, 3:4, 5:3, 11:1, 13:1, tail_ge_17:1, tail_to_sqrt:1 |
| 1009 | 1008 | 89 | 70 | 19 | 101 | 28 | 9 | 8 | 7 | 0 | 2:47, 3:20, 5:6, 7:1, 11:1, 13:2, tail_ge_17:5, tail_to_sqrt:5 |

最小 `N-R_30` 行：

| P | k | Delta | N | holes | W_int | C_30 | R_30 | R_210 | R_2310 | R_sqrt | shells |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 10 | 2 | 1 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 2:1 |

最大 `tail_ge_17` 行：

| P | k | Delta | N | holes | W_int | C_30 | R_30 | R_210 | R_2310 | R_sqrt | shells |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 983 | 929 | 65 | 51 | 14 | 95 | 29 | 15 | 12 | 12 | 0 | 2:43, 3:18, 5:5, 7:3, tail_ge_17:12, tail_to_sqrt:12 |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_lpf_factorizations_ordered=true
all_capacity_reconstructed_from_lpf_shells=true
all_adjacent_decrements_equal_lpf_shells=true
large_samples_are_evidence_not_global_proof=true
```

大样本 LPF shell 汇总：

```text
2=13391
3=4500
5=1743
7=1031
11=582
13=421
tail_ge_17=3016
```

## 4. 外部定理验收边界

Rough-number 短区间与方差理论可作为密度诊断，但本文需要的是
`reciprocal-window` 加权、逐行点态、同对象的 prime-minus-shell-tail 支配。
因此现有 rough-number 方差输入不能直接替代：

```text
PrimeCountDominatesLPFTailShellSum
```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LPFShellOrderedFactorization | `true` | `true` | 每个合成 cofactor 唯一写成 m=r*a，其中 r=LPF(m)，a>=r 且 a 为 r-rough。 | ordered LPF shell ledger |
| AdjacentWheelDropEqualsNewLPFShell | `true` | `true` | primorial wheel 从 y 加到 y' 时，容量下降等于 y<LPF(m)<=y' 的 shell。 | C_y-C_yprime=shell(y,yprime] |
| ResidualEqualsTailLPFShellSum | `true` | `true` | 固定 wheel residual 等于 LPF 大于 wheel cutoff 的 shell 尾和。 | R_y=sum_{r>y} Shell_r |
| PrimeDominatesEveryTailGlobally | `false` | `false` | 有限审计中 N>R_30，但尚未证明所有 P,k 的同对象素数数支配 LPF 尾和。 | PrimeCountDominatesLPFTailShellSum |
| ExternalRoughNumberTheoremClosesPointwiseRows | `false` | `false` | 现有 rough-number 短区间/方差结果控制普通 rough 集合，尚不匹配本文 reciprocal-window 加权同对象 residual。 | same-row signed residual theorem required |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 6. 当前最窄口

```text
PrimeCountDominatesLPFTailShellSum OR signed shell cancellation OR square-phase endpoint lower bound
```

```text
lpf_shell_decrement_law_closed=true
fixed_wheel_residual_dominance_global_closed=false
external_rough_number_theorem_closes_pointwise_rows=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
