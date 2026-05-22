# Prime Matrix Phi-LPF 组合精确性与奇偶屏障评审吸收证书

**状态：** `review_absorbed_phi_lpf_exactness_is_not_positivity`

## 1. 评审结论

评审结论应被吸收为硬约束：Phi-LPF/LPF 桶恒等式是组合精确，不是正性定理。刚生成的 parity capacity 证书是有效的非循环压缩，因为它把 forest holes 上界从整数窗压到奇偶窗；但它仍没有突破 Bombieri 奇偶屏障。当前真正剩余应表述为 DeltaPhi_half(P,k)>C_par(P,k) 的特殊 square-phase/reciprocal-forest 下界，或失败时的 reciprocal prime-pair saturation PDEC。

需要修正的一点是数值前沿：Baker--Harman--Pintz 的 `0.525` 已有 Runbo Li
`0.52` 级 arXiv 更新；但 `0.52>1/2`，所以对本项目的平方根尺度硬点没有本质改变。

## 2. 屏障几何

```text
strict_interval=[kP,(k+1)P]
worst_edge=k≈P, x=kP≈P^2, target length P≈sqrt(x)
lpf_sieve_scale=sieving threshold z≈P/2 to P
linear_sieve_issue=available unsigned lower-bound level is at or below the parity-critical range; lower sieve gives no positive prime lower bound.
```

因此，继续把 `N_P(k)` 改写成新的无符号 LPF/Phi 容量账本不会自动产生正性。
正性必须来自以下之一：平方根尺度短区间输入、特殊 square-phase 结构下界、
或真正带符号的 dispersion/transport 取消。

## 3. 路线判定

| route | status | required input | verdict |
| --- | --- | --- | --- |
| External sqrt-scale short interval input | `open_external` | 对所有相关 x=kP 给出长度 <=P≈sqrt(x) 的素数存在或计数下界。 | 这等同于 Legendre-scale 输入；当前语料和通用外部定理没有给出。 |
| Special square-phase/CRT structural lower bound | `open_internal` | 利用 P 为素数、端点相位 -P^2 mod q、reciprocal forest 的特殊结构证明 DeltaPhi_half>C_par。 | 这是当前最有价值的自足方向；必须产生新分布/相关性信息，不能只重排 LPF 恒等式。 |
| Signed transport / dispersion source route | `open_internal_or_external` | 提交 pointwise signed coefficient 表、Type-II/DI-BFI/Kloosterman 型取消，或把失败转成 PDEC/SAE。 | 若能给出真正带符号取消，它可以绕过线性筛奇偶屏障。 |
| Finite verification after theta>1/2 | `rejected_as_global_closure` | 固定阈值以下全验证，上方引用 theta>1/2 短区间。 | 仍留下无限顶端带，不能作为闭合路线。 |
| Capacity-only LPF/Phi rewriting | `rejected_as_global_closure` | 继续把同一个 exact count 改写为新的无符号容量表达式。 | 只能缩小剩余口；若没有新正性来源，就是同一奇偶屏障改名。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PhiLPFCombinatorialExactnessAccepted | `true` | `true` | LPF 分桶和 Phi 端点差给出精确等式，不含误差项。 | positivity not included |
| ExactIdentityDoesNotImplyPositiveLowerBound | `true` | `true` | 从 exact count 表达式推出 >=1 需要额外下界，不是代数化简。 | positive source required |
| LinearSieveParityBarrierRecognized | `true` | `true` | 在 H=P、z≈P 的 strict 顶端带，自然线性筛 level 参数不超过临界区，lower sieve 不给正下界。 | requires non-sieve parity breaking input |
| ThetaGreaterThanHalfShortIntervalRouteRejectedAsClosure | `true` | `true` | 0.525 或 0.52 级短区间定理代入 X≈P^2 后仍长于 P，不能闭合 k≈P。 | sqrt-scale or structural substitute |
| ParityCapacityLayerClassifiedAsNarrowingNotProof | `true` | `true` | 奇偶容量扣除是真正上界改进，但剩余正性仍是 prime-pair saturation/奇偶屏障口。 | PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC |
| UnconditionalTargetClosureReached | `false` | `false` | 评审吸收后仍未得到三目标命题无条件闭合。 | LegendreScaleInput OR structural signed/dispersion/PDEC contradiction |

## 5. 当前最窄口

```text
PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC
```

本证书不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它防止把组合恒等式误读为
正性证明，并把之后的硬攻方向限制到真正可能越过奇偶屏障的输入。

## 6. 外部来源记录

| name | fact | url |
| --- | --- | --- |
| Baker-Harman-Pintz 2001 | [x,x+x^0.525] contains a prime for sufficiently large x. | https://doi.org/10.1112/plms/83.3.532 |
| Runbo Li 2025 arXiv v8 | [x-x^0.52,x] contains primes for sufficiently large x, according to the arXiv abstract. | https://arxiv.org/abs/2308.04458 |
| linear sieve lower function | standard lower-bound function f(s) is zero in the initial parity-critical range. | https://www.sciencedirect.com/science/article/pii/S0022314X17303189 |

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.json` | `5a7b904f7e6feff82f6539fa8bb809178284793bfbd422663ebefa727bf60a5d` |
| `docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json` | `e822cff58c42d46384ab9fe12a91c7f4eb0c9987b7a08e1c3c65c80ff6ea748b` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json` | `9c8b4ae328fe2254bf81e16e4f058921efc6c3ea616a97f196a42482151dd028` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json` | `762c7de91c70ae99628279eb52aa2b5a94185e4d5ed2c32921f08ce6f0133881` |
| `docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json` | `37d15f13627b753f3c8c322e7836e888f06f1824212537a1fe87e77b58880aee` |
