# Prime Matrix strict 中段 psi 上界 1.00002841 来源路由器

**状态：** `middle_psi_upper_100002841_use_site_closed_source_and_interval_cover_open`

1.00002841 的使用点已明确，但来源尚未闭合。Table 6.3 的 b=27 界太弱，b=28 界只从 e^28 起有效；用 b=27/28 舍入值做线性或 log-线性插值也不能证明该常数。Table 6.2 的 8e11 和 1e12 点值很强，但点值不是整段覆盖。因此中段必须补一个有限区间 psi 覆盖证书，或提供 Deléglise-Rivat 等价精确计算数据和 hash。

```text
middle_psi_upper_use_site_closed=true
tiny_splice_slack_makes_source_critical=true
table63_interpolation_not_enough=true
table62_point_values_not_interval_cover=true
middle_finite_interval_psi_cover_closed=false
deleglise_rivat_psi_data_hash_closed=false
middle_psi_upper_directed_rounding_closed=false
middle_psi_upper_100002841_source_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 数值上下文

```text
x_left=8.000000000000000e+11
x_right_e28=1.446257064291475e+12
log_x_left=2.740787756461434e+01
target_ratio=1.000028410000000e+00
target_eps=2.841000000000000e-05
psi_8e11_ratio=1.000000047474093e+00
psi_1e12_ratio=1.000000040136765e+00
```

## 2. 候选来源检验

| candidate | formula | ratio | defect_vs_target | sufficient | reason |
| --- | --- | ---: | ---: | --- | --- |
| Table 6.3 b=27 bound | 1 + 3.368e-5 | `1.000033680000000e+00` | `5.269999999946151e-06` | `false` | valid from e^27, but too weak for the P5.1 middle constant |
| Table 6.3 b=28 bound | 1 + 2.224e-5 | `1.000022240000000e+00` | `-6.170000000027542e-06` | `false` | numerically strong, but only valid from e^28, not on 8e11<=x<e^28 |
| linear interpolation of rounded b=27,28 eps | eps27 + (log(8e11)-27)(eps28-eps27) | `1.000029013880661e+00` | `6.038806608099634e-07` | `false` | weaker than the target and no interpolation theorem is registered |
| log-linear interpolation of rounded b=27,28 eps | exp((1-t)log eps27 + t log eps28) | `1.000028435268399e+00` | `2.526839848471241e-08` | `false` | still slightly above target and no interpolation theorem is registered |
| Table 6.2 point value at 8e11 | (theta(8e11)+psi-theta(8e11))/(8e11) | `1.000000047474093e+00` | `-2.836252590676658e-05` | `true` | strong at the point, but does not cover the whole interval |
| Table 6.2 point value at 1e12 | (theta(1e12)+psi-theta(1e12))/(1e12) | `1.000000040136765e+00` | `-2.836986323462298e-05` | `true` | strong at the point, but does not cover jumps between points |

## 3. 外部边界

- `Dusart arXiv:1002.0442`：https://arxiv.org/pdf/1002.0442；use-site and tables source; not a reproducible middle interval cover

## 4. 自足替换

```text
MiddlePsiUpper100002841SourceLedger
  =>
MiddleFiniteIntervalPsiCover8e11ToE28Ledger AND DelegliseRivatPsiComputationDataAndHashLedger AND MiddlePsiUpperDirectedRoundingLedger

MiddleFiniteIntervalPsiCover8e11ToE28Ledger
  =>
finite interval cover of psi(x)/x on 8e11<=x<=e^28 with directed rounding

```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计假设反例链可调用的中段 psi 上界来源，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `MiddlePsiUpperSourceGateActive` | `true` | `true` | psi epsilon 表算法证书已把下一最窄点压到 1.00002841 的来源账本。 | MiddlePsiUpper100002841SourceLedger |
| `P51UseSiteLocated` | `true` | `true` | P5.1 中段确实需要 psi(x)<1.00002841x 覆盖 8e11<=x<=e^28。 | use site closed, source still open |
| `TinySpliceSlackMakesSourceCritical` | `true` | `true` | 该常数经 psi-theta 下界接入 theta 目标后只剩约 4.46e-11 余量，不能粗化。 | MiddlePsiUpperDirectedRoundingLedger |
| `Table63InterpolationNotEnoughFor100002841Ledger` | `true` | `true` | Table 6.3 的 b=27/28 舍入值和简单插值都不能自足推出 1.00002841。 | MiddleFiniteIntervalPsiCover8e11ToE28Ledger |
| `Table62ExactPointValuesNotIntervalCoverLedger` | `true` | `true` | Table 6.2 在 8e11 和 1e12 的点值远强于目标，但点值不是整段覆盖证书。 | MiddleFiniteIntervalPsiCover8e11ToE28Ledger |
| `MiddleFiniteIntervalPsiCover8e11ToE28Ledger` | `false` | `false` | 需要覆盖 8e11<=x<=e^28 的有限区间 psi 上界证书，含节点、跳点、最大值和间隙控制。 | DelegliseRivatPsiComputationDataAndHashLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger |
| `DelegliseRivatPsiComputationDataAndHashLedger` | `false` | `false` | 需要 Deléglise-Rivat 或等价 psi 精确计算数据、算法、版本和 hash；当前仓库没有该数据。 | machine-readable psi computation archive |
| `MiddlePsiUpperDirectedRoundingLedger` | `false` | `false` | 需要证明 1.00002841 是外向上舍入值，且舍入误差仍保留中段拼接余量。 | directed rounding log |
| `MiddlePsiUpper100002841SourceLedger` | `false` | `false` | 当前只定位到使用点并排除几个不足来源；尚未证明 1.00002841 的生成或覆盖。 | MiddleFiniteIntervalPsiCover8e11ToE28Ledger AND DelegliseRivatPsiComputationDataAndHashLedger AND MiddlePsiUpperDirectedRoundingLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 中段 psi 常数来源审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一最窄点

```text
MiddleFiniteIntervalPsiCover8e11ToE28Ledger
```
