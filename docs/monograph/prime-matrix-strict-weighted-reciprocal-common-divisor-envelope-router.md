# Prime Matrix strict 加权共同因子倒数封套路由器

**状态：** `weighted_reciprocal_common_divisor_envelope_reduced_to_windowed_divisor_hot_window_open`

共同因子倒数和已被压成完全初等的短窗口除数封套。由于 positive lower-weight 点态不超过 1，低有效模贡献至多为 1/2 * sum_{2<=s<=R} sum_{g|h, B/s<g<=2B/s} 1/g。若该封套小于 PDEC 下界，低有效模出口被排除；若不小，鸽巢原理强制某个小商 s 出现热频率因子窗口，持久时进入 PDEC/ColumnCRT，孤立时进入 SAE。

```text
pointwise_weight_bound_imported=true
windowed_reciprocal_envelope_closed=true
hot_window_pigeonhole_closed=true
reciprocal_envelope_beats_pdec_lower_bound=false
hot_window_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 窗口除数封套

在 dyadic 块 `d in (B,2B]` 中，低有效模已经写成 `d=s g`、`g|h`、`2<=s<=R`。因此

```text
B/s < g <= 2B/s.
```

又因正权点态不超过 1，得到

```text
LowEff_R(h) <= 1/2 sum_{2<=s<=R} sum_{g|h, B/s<g<=2B/s} 1/g.
```

所以当前问题已变成频率 `h` 的短乘法窗口除数倒数和问题。

## 2. 封套表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `positive_weight_pointwise_bound` | 0<=w_d^+<=1 for finite lower weights lambda_d^{low} in {-1,0,1}. | `imported_closed` | 正权部分不能超过 1；这是有限 lower-weight 递归的点态结果。 |
| `exact_windowed_reciprocal_envelope` | LowEff_R(h)<=1/2 sum_{2<=s<=R} sum_{g\|h, B/s<g<=2B/s} 1/g. | `closed` | dyadic 条件 d in (B,2B] 把 g 限在短乘法窗口。 |
| `divisor_count_envelope` | sum_{g\|h, B/s<g<=2B/s} 1/g <= (s/B) N_h(B/s,2B/s]. | `closed` | 若只知道 divisor 个数，也得到窗口计数封套。 |
| `sigma_minus_one_global_envelope` | LowEff_R(h)<=((R-1)/2) sigma_{-1}(h). | `closed_but_weak` | 全局倒数因子和是安全粗上界；通常太弱，只作兜底。 |
| `hot_window_pigeonhole` | If LowEff_R(h)>Xi, then some s has sum_{g\|h, B/s<g<=2B/s}1/g >= 2Xi/(R-1). | `closed_implication` | 低有效模失败会物化为某条小商线上的热频率因子窗口。 |
| `hot_window_route` | Persistent hot windows are PDEC/ColumnCRT; isolated hot windows are SAE. | `registered_route` | 倒数封套失败不是自由出口。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的低有效模出口内部。 | 保持 row_column_unconditional_closed=false。 |
| `PointwiseWeightBoundImported` | `true` | `true` | lower-weight 正部满足点态 <=1。 | 无。 |
| `WindowedReciprocalEnvelopeClosed` | `true` | `true` | 共同因子倒数和已压成 h 的短窗口除数倒数和。 | WindowedReciprocalDivisorEnvelopeForFrequencyH |
| `HotWindowPigeonholeClosed` | `true` | `true` | 封套若仍过大，某个小商 s 的热窗口必须显化。 | HotFrequencyDivisorWindowAnomalyPDECorSAE |
| `ReciprocalEnvelopeBeatsPDECLowerBoundCurrentCorpus` | `false` | `false` | 尚未把窗口除数封套与 PDEC 下界完成常数比较。 | WindowedReciprocalDivisorEnvelopeForFrequencyH AND WeightedPositiveEndpointPDECLowerBoundComparison |
| `HotWindowExcludedCurrentCorpus` | `false` | `false` | 尚未排斥持久热窗口 PDEC/ColumnCRT 或孤立 SAE。 | HotFrequencyDivisorWindowAnomalyPDECorSAE AND LowQuotientColumnCRTOrPDECRoute |

## 4. 最新最窄输入

```text
WindowedReciprocalDivisorEnvelopeForFrequencyH
```

并行保留：

```text
WeightedPositiveEndpointPDECLowerBoundComparison AND HotFrequencyDivisorWindowAnomalyPDECorSAE AND LowQuotientColumnCRTOrPDECRoute
```

审稿边界：本步闭合短窗口除数封套与热窗口显化；尚未证明封套常数足够小，也未排斥热窗口出口。
