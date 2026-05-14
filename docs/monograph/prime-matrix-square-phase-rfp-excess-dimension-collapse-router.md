# Prime Matrix square-phase RFP 过密维数塌缩路由器

**状态：** `rfp_excess_reduced_to_single_curve_dimension_collapse_or_reciprocal_floor_pdec_open`

在平方端点反例链中，若不发生低骨架亏损，则 `B(P)>=0.48P/logP`。三条倒数地板曲线中至少一条必须贡献 `0.16P/logP` 级素值，这比正常二维筛尺度 `P/log^2P` 高一个 `logP` 因子，是维数塌缩。该塌缩的最具体表达为：对 `m_s(ell)=floor(P^2/ell)+s`，`q|m_s(ell)` 精确等价于 `ell` 落入一族倒数端点短区间。因此 RFP 过密必须由 `RFP-SelbergConstantLedger` 失败，或由 reciprocal-floor 端点相位/PDEC 缺陷承担；尚未完成出口排斥。

```text
prime_void_no_low_defect_forces_rfp_dimension_collapse=true
single_curve_positive_scale_forced=true
reciprocal_floor_divisibility_interval_formula_closed=true
rfp_excess_excluded=false
row_column_unconditional_closed=false
```

## 1. 反例态强度

在 `P>=23` 的平方端点，如果假设前半窗无素数且没有 LDG 亏损，则

```text
B(P)=G(P)>=0.48 P/logP.
```

写 `B(P)=B_1(P)+B_2(P)+B_3(P)`，其中

```text
B_s(P)=#{ell prime: y<ell<P, floor(P^2/ell)+s prime, 1<=ell*s-(P^2 mod ell)<P}.
```

因此某个 `s` 必满足 `B_s(P)>=0.16P/logP`。

| P | 单曲线强制下界 | RFP正常总预算 | 单曲线/正常总预算 | 维数塌缩因子 |
| ---: | ---: | ---: | ---: | ---: |
| 23 | 1.173659 | 3.509192 | 0.334453 | 0.334453 |
| 101 | 3.501534 | 7.112897 | 0.492280 | 0.492280 |
| 1009 | 23.340560 | 31.636080 | 0.737783 | 0.737783 |
| 10007 | 173.826189 | 176.920358 | 0.982511 | 0.982511 |
| 1000003 | 11581.218413 | 7858.840872 | 1.473655 | 1.473655 |

## 2. reciprocal-floor 整除公式

| object | formula | meaning |
| --- | --- | --- |
| `curve_value` | `m_s(ell)=floor(P^2/ell)+s, s in {1,2,3}` | 三条倒数地板素对曲线的互补因子。 |
| `divisibility` | `q \| m_s(ell) iff floor(P^2/ell)=q*u-s for some u` | 素性筛的第二坐标坏事件。 |
| `reciprocal_interval` | `P^2/(q*u-s+1) < ell <= P^2/(q*u-s)` | 每个坏事件是倒数端点短区间，不是任意残基。 |
| `range` | `y<ell<P and P<m_s(ell)<eP` | u 只在长度约 P/q 的短区间内取值。 |
| `defect` | `bad count - expected local density` | 若 Selberg 分布账本失败，即得到 reciprocal-floor PDEC。 |

这个公式是本步的实际下钻点：第二坐标素性不再写成抽象的 `m_s(ell) is prime`，而是写成一套随 `q` 变化的倒数短区间避让问题。若这些短区间在素数 `ell` 上有正常局部分布，则二维 Selberg 上筛给 `P/log^2P`；若不正常，异常本身就是 reciprocal-floor PDEC。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PrimeVoidNoLowDefectForcesRFPDimensionCollapse` | `true` | `true` | 由 prime-void 二分，若反例不走低骨架亏损，则 B(P)>=0.48P/logP。 | ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE |
| `SingleCurvePositiveScaleForced` | `true` | `true` | 三条曲线相加为 B(P)，故某个 s 有 B_s(P)>=0.16P/logP。 | PositiveDensityPrimeValuesOfReciprocalFloorCurve |
| `ReciprocalFloorDivisibilityIntervalFormula` | `true` | `true` | q\|floor(P^2/ell)+s 精确等价于 ell 落在倒数端点短区间并集中。 | none |
| `SelbergDistributionWouldContradictCollapse` | `true` | `false` | 若 reciprocal-floor 坏事件有二维筛正常分布，则 B_s 为 P/log^2P 级，不能达到 P/logP 级。 | RFP-SelbergConstantLedger |
| `RFPExcessRoutedToConcreteDefect` | `true` | `false` | RFP 过密不再是无名过密；它等价于某条曲线的素值维数塌缩，或 reciprocal-floor 局部分布缺陷。 | ReciprocalFloorCongruencePDECOrSelbergDistributionLedger |
| `RFPExcessExcluded` | `false` | `false` | 尚未证明 Selberg 分布账本，也未排斥 reciprocal-floor PDEC。 | RFP-SelbergConstantLedger OR exclude ReciprocalFloorCongruencePDECOrSelbergDistributionLedger |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 本步闭合的是 RFP 过密的结构定位，不是最终出口排斥。 | exclude LowSkeletonDeficitPDECOrSAE and ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 行/列命题仍未无条件闭合。 | LowSkeletonDeficitPDECOrSAE exclusion AND ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE exclusion |

## 4. 下一步

- 直接攻 `ReciprocalFloorCongruencePDECOrSelbergDistributionLedger`：证明倒数短区间坏事件满足二维 Selberg 分布，或把失败登记为端点相位缺陷。
- 若接受外部二维 Selberg/Brun 上筛及该序列的分布账本，则 RFP 过密出口关闭；自足路线仍需内联该账本。
- 该步仍未处理 `LowSkeletonDeficitPDECOrSAE`，所以不能宣称行/列命题无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md` | `4d6f95b7c545e525d9ae34bc3065d11c807ef752ddefdc3186b344979c7caf78` |
| `docs/monograph/prime-matrix-diagonal-postsquare-ero-low-bprocess-envelope.md` | `8c2f41e2c6060662aa222d0257eb330e08911695308aaaf481f3c5dc165e3c45` |
| `docs/monograph/prime-matrix-diagonal-postsquare-rfp-selberg-route.md` | `e94ee4bb9b45dd441f151c88b99c23ebcf60b7c618d1c293c739a9fa20eba147` |
| `docs/monograph/prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json` | `abc24466fce3fb754f690af980a96c6fe29e24fdbe36adcd8221b403aea312e2` |
| `docs/monograph/prime-matrix-square-phase-rfp-upper-direct-attack-router.json` | `c8ecab3fdc5e787f3b7cef1d73d34868d48878e48a7b9c8b6cc88218ebcfed81` |
| `experiments/prime_matrix_square_phase_rfp_excess_dimension_collapse_router.py` | `cbc84b23c9b7778a91d7ce8d8504119d757e03c7ca233f023d377342019650ef` |
