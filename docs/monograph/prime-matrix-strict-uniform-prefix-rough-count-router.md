# Prime Matrix strict 统一 prefix 粗筛余下界路由器

**状态：** `uniform_prefix_rough_count_reduced_to_beta_main_total_variation_finite_certificate_open`

`UniformPrefixRoughCountLowerBound` 已接到已有 beta-sieve lower-weight 体系：逐点支配性已闭合；对 prefix 序列 A_d(x) 的 CRT 计数误差逐项不超过 1。因此 |R_{x,z}| 的下界等于 beta 主项减 lower weights 总变差。剩余比原命题窄：B3 主系数尾段、总变差预算、有限小 P 证书。

```text
beta_sieve_lower_weight_dominance_imported=true
prefix_sequence_remainder_formula_closed=true
main_error_split_closed=true
b3_main_coefficient_tail_proved=false
b3_remainder_total_variation_budget_proved=false
finite_boundary_prefix_rough_count_certificate_proved=false
uniform_prefix_rough_count_lower_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 筛权公式

对 prefix 序列 `n_c=xP+c`，已有 lower weights 给出逐点支配：

```text
1_{(n_c,P(z))=1} >= sum_{d|(n_c,P(z))} lambda_d^-.
```

求和并使用 CRT 余类计数，得到

```text
|R_{x,z}| >= (P-1) W^-(z,D) - TV(lambda^-),
TV(lambda^-)=sum_{d in supp lambda^-} |lambda_d^-|.
```

所以粗筛余下界现在只需要主项大、总变差小、有限段可证。

## 2. 公式表

| equation | formula | status |
| --- | --- | --- |
| `lower_weight_dominance` | 1_{(n,P(z))=1} >= sum_{d\|(n,P(z))} lambda_d^-. | `imported_closed` |
| `prefix_count_lower_sum` | \|R_{x,z}\| >= sum_d lambda_d^- A_d(x), A_d(x)=#{1<=c<P: d divides xP+c}. | `closed` |
| `crt_residue_count` | A_d(x)=(P-1)/d + r_d(x), \|r_d(x)\|<=1 for squarefree d<P and gcd(d,P)=1. | `closed` |
| `main_error_split` | \|R_{x,z}\| >= (P-1)W^-(z,D) - sum_{d in supp lambda^-}\|lambda_d^-\|. | `closed_as_reduction` |
| `positive_rough_count_contract` | Need (P-1)W^- - TV(lambda^-) >= c P/log z. | `open` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `UniformPrefixRoughCountInputActive` | `true` | `false` | 上一层把 M# 归一化势的核心输入定为 prefix 粗筛余统一下界。 | UniformPrefixRoughCountLowerBound |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在假设链条里证明筛余计数输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `BetaSieveLowerWeightDominanceImported` | `true` | `true` | 已有 beta-sieve lower weights 的逐点支配性：lower sum 不超过筛剩余指示函数。 | 支配性已不是当前硬点。 |
| `PrefixSequenceRemainderFormulaClosed` | `true` | `true` | 对每个 squarefree d<P，因 P mod d 可逆，A_d(x) 是单个 CRT 余类计数，误差绝对值 <=1。 | 需要总变差预算。 |
| `MainErrorSplitClosed` | `true` | `true` | \|R_{x,z}\| 被下界为主项 (P-1)W^- 减去 lower weights 总变差。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND B3RemainderTotalVariationBudgetForLengthP |
| `B3MainCoefficientTailCurrentCorpusProved` | `false` | `false` | 已有 checkpoint 很强，但尾段证明仍压成连续 beta 主项余量与离散素和误差。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError |
| `B3RemainderTotalVariationCurrentCorpusProved` | `false` | `false` | 尚未证明 lower weight 支撑总变差相对 P/log z 足够小；这是从筛主系数到短窗口粗余量的新增必要账本。 | B3RemainderTotalVariationBudgetForLengthP |
| `FiniteBoundaryPrefixRoughCountCurrentCorpusProved` | `false` | `false` | 任何显式常数路线都要留下有限 P 段；该边界 prefix 证书尚未生成。 | FiniteBoundaryPrefixRoughCountCertificate |
| `UniformPrefixRoughCountCurrentCorpusProved` | `false` | `false` | 统一 prefix 粗筛余下界已接入 beta-sieve 公式，但主系数、总变差和有限段仍未闭合。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND B3RemainderTotalVariationBudgetForLengthP AND FiniteBoundaryPrefixRoughCountCertificate |
| `DownstreamStillOpen` | `false` | `false` | 即便粗筛余下界完成，还需类型阈值比较与标签到类型抗塌缩。 | NormalizedPrefixResidualPotentialLowerBound THEN FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse |

## 4. 下一最窄点

```text
B3RemainderTotalVariationBudgetForLengthP
```

并行保留：

```text
B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse
```

审稿边界：本步只把 prefix 粗筛余下界压成 beta 主项、总变差和有限证书；尚未证明这些输入。
