# Prime Matrix Phi-LPF endpoint interval difference 证书

**状态：** `phi_lpf_endpoint_interval_difference_identity_closed_but_positivity_open`

Phi-LPF 精准桶恒等式可以直接用于两个端点求差，得到 [kP,kP+P] 内素数个数的精确公式。但这只是精确计数表达式；要推出区间内必有素数，还必须证明 LPF 合数桶端点增量之和小于区间长度。该正性不能由恒等式本身给出，而且任意固定 P 都存在 CRT 对齐的 [kP,kP+P] 全合数区间。

## 1. 端点差分公式

闭区间 `2<=A<=B`：

```text
pi(B)-pi(A-1)=(B-A+1)-sum_{p<=sqrt(B)}[Phi(floor(B/p),p)-Phi(floor((A-1)/p),p)] for 2<=A<=B
```

闭区间 `[kP,kP+P]`：

```text
pi(kP+P)-pi(kP-1)=P+1-sum_{p<=sqrt(kP+P)}[Phi(floor((kP+P)/p),p)-Phi(floor((kP-1)/p),p)]
```

半开区间 `[kP,kP+P)`：

```text
pi(kP+P-1)-pi(kP-1)=P-sum_{p<=sqrt(kP+P-1)}[Phi(floor((kP+P-1)/p),p)-Phi(floor((kP-1)/p),p)]
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EndpointDifferenceIdentityClosed` | `true` | `true` | Pi(B)-Pi(A-1) 可写成长度减去所有 LPF 桶的 Phi 端点差分。 | exact identity, not an asymptotic |
| `KPToKPPlusPFormulaClosed` | `true` | `true` | 对闭区间 [kP,kP+P]，长度项为 P+1，合数项为 p<=sqrt(kP+P) 的 Phi 差分和。 | P+1 - sum_p Delta_Phi_p |
| `MechanicalExactComputationAvailable` | `true` | `true` | 给定 k,P 后可机械计算精确素数个数，并与直接筛一致。 | finite endpoint computation |
| `IntervalPositivityFromIdentityAlone` | `false` | `false` | 恒等式本身不提供 Delta_Phi 总和小于长度的全局不等式。 | need upper bound on composite bucket increments |
| `UniversalPrimeInEveryAlignedInterval` | `false` | `false` | 任意固定 P 都可用 CRT 构造某个 k，使 [kP,kP+P] 全为合数；因此该全称命题为假。 | sample P=5 gives prime_count=0 |
| `UsefulFiniteVerificationBoundary` | `true` | `false` | 端点差分适合作为有限验证和局部审计工具；若要突破需另加平均、相位或容量不等式。 | signed/phase lower bound still required |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只建立区间精确计数与 CRT 阻断；未证明三命题无条件闭合。 | offdiagonal signed seed, internal transition, source/side gates, tail package |

## 3. 样本审计

| P | k | interval | length | LPF composite delta | endpoint prime count | direct prime count | ok |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 5 | 2 | [10,15] | 6 | 4 | 2 | 2 | `true` |
| 7 | 10 | [70,77] | 8 | 6 | 2 | 2 | `true` |
| 11 | 30 | [330,341] | 12 | 10 | 2 | 2 | `true` |
| 13 | 40 | [520,533] | 14 | 12 | 2 | 2 | `true` |

## 4. CRT 对齐零素数区间样本

`P=5, k=8166, interval=[40830, 40835]`

```text
all_values_composite_by_witness=true
endpoint_prime_count=0
direct_prime_count=0
```

| r | n=kP+r | witness divisor | composite |
| ---: | ---: | ---: | --- |
| 0 | 40830 | 5 | `true` |
| 1 | 40831 | 7 | `true` |
| 2 | 40832 | 11 | `true` |
| 3 | 40833 | 13 | `true` |
| 4 | 40834 | 17 | `true` |
| 5 | 40835 | 5 | `true` |

## 5. 结论

端点差分公式可以作为精确局部审计器和有限验证器；它不能单独闭合区间正性。下一步若继续沿此路走，必须新增对
`sum Delta_Phi_p` 的结构性上界，或引入平均相位、signed payload、容量压力等额外信息。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_endpoint_interval_difference_router.py` | `6f08a824ec8d29aebbb85a48054383ba401c6eba8bd780eb6a5f768483244610` |
