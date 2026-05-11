# Prime Matrix strict alpha-prefix 负载缺陷到 PDEC/TV 路由器

**状态：** `alpha_prefix_load_deficit_forces_tv_or_pdec_defect_surplus_open`

容量反超失败不是自由出口。对 z=alpha P>P/2，早期零行迫使 |R_alpha(x)|<=2(pi(P)-pi(alpha P))；而 prefix lower-weight 公式给出 |R_alpha(x)|>=(P-1)W^-_alpha-TV_alpha。因此若不能直接容量反超，就必须有 TV_alpha 至少达到主项减高标签容量的间隙。这正是一个强端点/PDEC/SAE 缺陷，而不是新的无名逃逸。

```text
capacity_failure_to_tv_defect_implication_closed=true
pdec_registration_route_defined=true
alpha_prefix_load_lower_bound_proved=false
alpha_prefix_tv_defect_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 二择公式

对 `alpha>1/2`，早期零行必须满足

```text
|R_alpha(x)| <= 2(pi(P)-pi(alpha P)).
```

另一方面，prefix lower weights 给出

```text
|R_alpha(x)| >= (P-1)W^-_alpha - TV_alpha.
```

合并得到反例必要条件：

```text
TV_alpha >= (P-1)W^-_alpha - 2(pi(P)-pi(alpha P)).
```

所以闭合路线不再模糊：要么证明 TV 小于这个间隙得到直接矛盾；要么这个大 TV 必须作为端点/PDEC/SAE 缺陷被登记并排斥。

## 2. 精确蕴含

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `early_zero_capacity_necessity` | Assume EarlyZeroRowWithinP and z=alpha P> P/2. Then \|R_alpha(x)\|<=2(pi(P)-pi(alpha P)). | `closed_imported` | 来自高标签容量反超路由；这是早期零行的必要条件。 |
| `lower_weight_main_error` | \|R_alpha(x)\| >= (P-1) W^-_alpha - TV_alpha. | `closed_imported` | 来自统一 prefix 粗筛余路由；TV 汇总 CRT 端点/筛权总变差。 |
| `defect_forced_if_no_surplus` | If EarlyZeroRowWithinP, then TV_alpha >= (P-1)W^-_alpha - 2(pi(P)-pi(alpha P)). | `closed_implication` | 若没有容量反超矛盾，反例必须支付一个强负端点/总变差缺陷。 |
| `closure_if_tv_budget_beats_gap` | If TV_alpha < (P-1)W^-_alpha - 2(pi(P)-pi(alpha P)), then early zero row is impossible. | `closed_implication` | 这把当前硬点变成一个明确的 TV/PDEC 排斥输入。 |
| `pdec_registration` | Failure of the TV budget must be registered as LowMod/Endpoint/Dyadic PDEC or SAE, not as a free escape. | `registered_route` | 与既有 LowMod、dyadic endpoint 证书路线对接。 |

## 3. alpha 间隙诊断

下表仍是目标定位，不是证明。正间隙表示若获得 Mertens 级粗筛主项并控制 TV，就会触发容量反超或强缺陷。

| alpha | hit cap | capacity constant | Mertens main reference | reference defect gap | positive |
| --- | ---: | ---: | ---: | ---: | --- |
| 0.750000 | 2 | 0.500000 | 0.561459 | 0.061459 | `true` |
| 0.800000 | 2 | 0.400000 | 0.561459 | 0.161459 | `true` |
| 0.850000 | 2 | 0.300000 | 0.561459 | 0.261459 | `true` |
| 0.900000 | 2 | 0.200000 | 0.561459 | 0.361459 | `true` |
| 0.950000 | 2 | 0.100000 | 0.561459 | 0.461459 | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍只在早期零行假设链条下推出必要缺陷。 | 保持 row_column_unconditional_closed=false。 |
| `CapacityFailureToTVDefectClosed` | `true` | `true` | 早期零行若不被容量反超立即击败，则必须满足 TV_alpha 大于主项-容量间隙。 | AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion |
| `PDECRouteRegistered` | `true` | `false` | 大 TV/端点偏差已有 LowMod、dyadic endpoint、SAE 路由对象；但尚未全局排斥。 | LowMod/DyadicEndpoint/FarTail-Core PDEC exclusion |
| `AlphaLoadLowerBoundCurrentCorpusProved` | `false` | `false` | 主项常数、TV 预算、有限段证书仍未合取闭合。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND B3RemainderTotalVariationBudgetForLengthP AND FiniteBoundaryPrefixRoughCountCertificate |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 已得到二择结构：容量反超直接矛盾，或强缺陷登记；缺陷排斥尚未完成。 | AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity OR AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion |

## 5. 最新最窄输入

```text
AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion
```

并行保留：

```text
B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND B3RemainderTotalVariationBudgetForLengthP AND FiniteBoundaryPrefixRoughCountCertificate
```

审稿边界：本步只证明“容量不反超则强缺陷”的二择结构；它没有排斥该强缺陷，因此不能声明无条件闭合。
