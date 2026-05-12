# Prime Matrix strict 短窗口倒数除数密度路由器

**状态：** `windowed_reciprocal_divisor_envelope_reduced_to_short_window_density_pdec_sae_open`

短窗口倒数除数封套进一步压成除数密度阈值。对 Y<g<=2Y，倒数和至多为 N_h(Y,2Y]/Y；若它超过 eta，则 h 在这个短乘法窗口中至少有 eta Y 个除数。因而低有效模若无法由倒数封套吸收，就物化为热频率除数密度证书。这个证书必须进入 PDEC/ColumnCRT 或 SAE，不能作为普通 tau(h) 粗估计自由处理。

```text
reciprocal_to_divisor_count_closed=true
hot_density_certificate_closed=true
generic_tau_closure_rejected=true
windowed_divisor_envelope_proved=false
hot_density_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 短窗口密度阈值

对任意窗口 `Y<g<=2Y`，有

```text
sum_{g|h, Y<g<=2Y} 1/g <= N_h(Y,2Y]/Y.
```

所以若该倒数和大于 `eta`，就强制

```text
N_h(Y,2Y] >= eta Y.
```

这把低有效模失败变成短窗口除数密度证书。

## 2. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `reciprocal_to_count` | For Y<g<=2Y, sum_{g\|h}1/g <= N_h(Y,2Y]/Y. | `closed` | 倒数封套由短窗口除数个数控制。 |
| `count_threshold` | If sum_{g\|h,Y<g<=2Y}1/g >= eta, then N_h(Y,2Y] >= eta Y. | `closed` | 倒数和过大强制频率 h 在该短窗口内有线性多除数。 |
| `multi_s_threshold` | LowEff_R(h)>Xi implies some s has N_h(B/s,2B/s] >= (2Xi/(R-1))(B/s). | `closed_implication` | 低有效失败等价于某条小商线上的短窗口除数密度异常。 |
| `density_to_structural_defect` | Many divisors g of h in one short multiplicative window give a hot frequency divisor-density certificate. | `registered_route` | 该证书持久出现是 PDEC/ColumnCRT，孤立出现是 SAE。 |
| `no_free_global_divisor_bound` | A generic tau(h) bound alone is insufficient unless compared with the actual PDEC lower threshold. | `discipline_closed` | 防止用无参数除数函数估计偷关当前缺口。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的低有效模封套内部。 | 保持 row_column_unconditional_closed=false。 |
| `ReciprocalToDivisorCountClosed` | `true` | `true` | 窗口倒数和已经转成短窗口除数个数。 | ShortWindowDivisorDensityEnvelopeForFrequencyH |
| `HotDensityCertificateClosed` | `true` | `false` | 除数密度若超过阈值，得到热频率除数密度证书。 | HotFrequencyDivisorDensityPDECorSAE |
| `GenericTauClosureRejected` | `true` | `true` | 没有实际阈值比较时，不能用普通 tau(h) 估计宣称闭合。 | WeightedPositiveEndpointPDECLowerBoundComparison |
| `WindowedDivisorEnvelopeCurrentCorpusProved` | `false` | `false` | 尚未证明所有正式频率的短窗口除数密度低于 PDEC 阈值。 | ShortWindowDivisorDensityEnvelopeForFrequencyH AND WeightedPositiveEndpointPDECLowerBoundComparison |
| `HotDensityExcludedCurrentCorpus` | `false` | `false` | 尚未排斥热除数密度的 PDEC/ColumnCRT/SAE 出口。 | HotFrequencyDivisorDensityPDECorSAE AND LowQuotientColumnCRTOrPDECRoute |

## 4. 最新最窄输入

```text
ShortWindowDivisorDensityEnvelopeForFrequencyH
```

并行保留：

```text
WeightedPositiveEndpointPDECLowerBoundComparison AND HotFrequencyDivisorDensityPDECorSAE AND LowQuotientColumnCRTOrPDECRoute
```

审稿边界：本步只把窗口倒数封套转成除数密度证书；尚未证明正式频率族没有热除数窗口。
