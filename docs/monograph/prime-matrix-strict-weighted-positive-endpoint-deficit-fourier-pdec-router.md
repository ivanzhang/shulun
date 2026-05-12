# Prime Matrix strict 正权端点亏损到 Fourier/PDEC 路由器

**状态：** `weighted_positive_endpoint_deficit_converted_to_centered_fourier_pdec_input_upper_bound_open`

正权端点命中亏损已经可以严格写成一个完整 CRT 周期上的零均值测试函数 Phi_I^+。若某个早期零行反例点使 Phi_I^+<=-kappa，则非零 Fourier 能量至少为 kappa^2/(Q_I-1)；若这类亏损在 formal family 中持久出现，就形成标准 PDEC 输入，若只孤立出现则进入 SAE。当前尚未完成的是匹配的 Fourier 上界或 SAE 排斥。

```text
centered_fourier_pdec_object_closed=true
fourier_energy_lower_bound_closed=true
persistent_or_sae_route_defined=true
weighted_positive_endpoint_deficit_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 中心化测试函数

对正权支撑块定义

```text
Phi_I^+(x)=sum_{d in I} w_d^+ (1_{rho_d(x)<=H}-H/d).
```

其中 `Q_I=lcm{d in supp_+(I)}`。在完整 `x mod Q_I` 周期上，`Phi_I^+` 均值为零。

若正权端点亏损达到 `kappa`，即

```text
Phi_I^+(x0)<=-kappa,
```

则 `Phi_I^+` 的非零 Fourier 能量不能为零；这是 PDEC 证书的标准入口。

## 2. 闭合蕴含

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `centered_positive_endpoint_test` | Phi_I^+(x)=sum_{d in I} w_d^+(1_{rho_d(x)<=H}-H/d). | `closed_definition` | 正权端点命中亏损就是中心化端点测试函数取负大值。 |
| `zero_mean_on_full_crt_period` | Average_{x mod Q_I} Phi_I^+(x)=0, Q_I=lcm{d in supp_+(I)}. | `closed` | 因为 xP mod d 是单位旋转，端点弧在完整 CRT 周期上的均值正好是 H/d。 |
| `deficit_to_fourier_energy` | If Phi_I^+(x0)<=-kappa, then sum_{h!=0}\|hat Phi(h)\|^2 >= kappa^2/(Q_I-1). | `closed_implication` | 单个强亏损点也强制非零 Fourier 能量；持续出现时即 PDEC。 |
| `persistent_bad_set_h4_input` | For S={x:Phi_I^+(x)<=-kappa}, F=-Phi_I^+ gives F(x)>=kappa on S and mean(F)=0. | `closed_template` | 这逐项匹配 H4/PDEC 的零均值测试函数输入。 |
| `isolated_deficit_route` | If the bad set is not persistent across the formal family, it is registered as SAE rather than a global PDEC. | `registered_route` | 防止单窗异常被误当作全局 Fourier 定理。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链下处理正权端点亏损。 | 保持 row_column_unconditional_closed=false。 |
| `CenteredFourierPDECObjectClosed` | `true` | `true` | 正权亏损已写成完整 CRT 周期上的零均值测试函数。 | WeightedPositiveEndpointHitDeficitPDEC |
| `FourierEnergyLowerBoundClosed` | `true` | `true` | 亏损点给出非零 Fourier 能量下界；持续亏损给出 H4/PDEC 输入。 | WeightedPositiveEndpointFourierPDECUpperBound |
| `PersistenceOrSAERouteClosed` | `true` | `false` | 持久出现走 PDEC；孤立出现走 SAE。是否可排斥两者尚未证明。 | DeficitPersistenceOrSAEClassification |
| `PositiveEndpointDeficitExcludedCurrentCorpus` | `false` | `false` | 尚未提交匹配的 Fourier 上界，也未完成 SAE 排斥。 | WeightedPositiveEndpointFourierPDECUpperBound AND DeficitPersistenceOrSAEClassification AND PositiveWeightSupportLowComplexityLedger |
| `RowColumnClosed` | `false` | `false` | 本步是标准 PDEC 输入化，不是 PDEC 排斥。 | WeightedPositiveEndpointFourierPDECUpperBound OR SAE exclusion; parallel WeightedNegativeEndpointHitSurplusCoreLoad |

## 4. 最新最窄输入

```text
WeightedPositiveEndpointFourierPDECUpperBound
```

并行保留：

```text
DeficitPersistenceOrSAEClassification AND PositiveWeightSupportLowComplexityLedger AND WeightedNegativeEndpointHitSurplusCoreLoad
```

审稿边界：本步只把正权亏损转成标准 PDEC/SAE 输入；没有提交 Fourier 上界，也没有排斥 SAE。
