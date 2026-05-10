# Prime Matrix strict RKS23 非循环 RNRS/Rudnev 接口证书

**状态：** `noncircular_reciprocal_energy_reduced_to_rudnev_rnrs_incidence_interface`

非循环剩余继续压窄：当前不再需要泛泛地重证 BG/RKS23，而只需一个独立的倒数区间能量定理。精确接口是：对平方根对数颈部中的区间 `J`，证明 `E_+(J^{-1})` 有任意固定幂节省；典型 Rudnev/RNRS 形态 `E_+(J^{-1})<=C|J|^(5/2)P^eps` 已足够。接受外部 Rudnev/RNRS 可闭合这一输入；严格自足路线则必须内联 Rudnev 点-平面 incidence 及其 reciprocal-energy 推论，不能再回用已经检测到回环的 RKS23/inverse-sumproduct 链。

```text
rnrs_rudnev_interface_statement_closed=true
rnrs_parameter_sufficiency_closed=true
self_contained_rnrs_rudnev_proof_closed=false
row_column_unconditional_closed=false
```

## 1. 精确接口

| field | value |
| --- | --- |
| `set` | B=J^{-1} in F_P, where J is an integer interval |
| `collar` | \|J\|=N with P^(1/2)/log^236(P)<=N<=P^(1/2)log^236(P) |
| `target_energy` | E_+(B)=#{b1+b2=b3+b4: bi in B} |
| `sufficient_bound` | E_+(J^{-1}) <= C*N^(5/2)*P^eps, or any E_+<=N^(3-delta_E) with fixed delta_E>0 |
| `why_sufficient` | N^delta_E dominates every fixed log power in the square-root log collar |
| `rudnev_input` | point-plane incidence I(R,Pi)<=C_Rud(\|R\|^(1/2)\|Pi\|+k\|Pi\|), plus RNRS reciprocal-energy corollary |
| `noncircular_requirement` | the proof must be imported from incidence/sum-product geometry, not from the RKS23 inverse-sumproduct chain itself |
| `accepted_external_route` | AcceptRudnevRNRSReciprocalIntervalEnergyEstimateWithParameterMatch |

## 2. 非循环审计

| field | value |
| --- | --- |
| `cycle_guard` | previous router detected that RKS-log -> balanced energy -> Mobius overlap returns to the same inverse-sumproduct frontier |
| `allowed` | a direct self-contained proof of Rudnev point-plane incidence and its reciprocal-energy corollary |
| `allowed_external` | explicit acceptance of Rudnev/RNRS with parameter match |
| `not_allowed` | reusing the already cyclic RKS23/slope-conic/character-moment route as the proof of the same energy input |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonCircularEnergyTargetActive` | `true` | `true` | 上一证书已把真正剩余固定为非循环倒数区间能量输入。 | NonCircularSelfContainedReciprocalIntervalEnergyPowerSaving |
| `FixedPowerEnergyReductionImported` | `true` | `true` | 只需固定幂节省，不必直接证明 log^-472。 | UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23 |
| `MobiusAndInverseSumproductDictionaryImported` | `true` | `true` | 倒数能量、Möbius 重叠谱、反演小和集字典已经闭合。 | dictionary closed |
| `RNRSRudnevInterfaceStatementClosed` | `true` | `true` | 所需非循环输入已精确为 Rudnev/RNRS 倒数区间能量固定幂节省接口。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |
| `RNRSParameterSufficiencyClosed` | `true` | `true` | `E_+(J^{-1})<=C N^(5/2)P^eps` 或任意固定幂节省足以推出当前目标。 | parameter ledger closed |
| `ExternalRudnevRNRSWouldCloseIfAccepted` | `true` | `true` | 若接受外部 Rudnev/RNRS 定理并完成参数匹配，本输入可外部闭合。 | AcceptRudnevRNRSReciprocalIntervalEnergyEstimateWithParameterMatch |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | 严格内部自足版仍未内联 Rudnev 点-平面 incidence 及 RNRS 倒数能量推论。 | SelfContainedRudnevPointPlaneIncidenceProofWithReciprocalEnergyCorollary |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是接口和参数充分性；未补入自足 incidence 证明。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 4. 下一真正自足目标

```text
SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling
SelfContainedRudnevPointPlaneIncidenceProofWithReciprocalEnergyCorollary
```
