# Q2 阶端点替换债务与孔径增长路由

**状态：** `endpoint_replacement_aperture_growth_routed_not_global_proof`

Q2 阶全轮复制不只是杀掉原素端点；它把 [Q1,Q2] 复制为闭复合块。因此真实相邻素数端点必须替换到块外，下一载体间隙至少增加 2。同一有限孔径的端点稳定复现被排除；无限反例链若继续，只能扩孔/移动，并被路由到 moving-aperture PDEC/ColumnCRT、SAE 或 H3-DSB/KLS 出口。

```text
previous_hardpoint=Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;GlobalFinalInputsStillOpen
corrected_endpoint_bound=Q1<=kP-P, with equality possible at k=2; Q2>kP
full_q2_replay_makes_closed_carrier_composite=true
endpoint_replacement_gap_growth_per_replay_at_least=2
same_aperture_replay_impossible=true
bounded_aperture_replay_finite=true
persistent_moving_aperture_routes_to_pdec_columncrt=true
sparse_replacement_routes_to_sae=true
unbounded_replacement_routes_to_h3_dsb=true
row_column_unconditional_closed=false
next_direct_attack_target=EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;GlobalFinalInputsStillOpen
```

## 1. 端点边界修正

若早期第 `k` 行 `[(k-1)P+1,kP]` 无素数，则左侧最近素数满足

\[
Q_1\le (k-1)P=kP-P,
\]

右侧最近素数满足 `Q2>kP`。左端一般严格小于 `(k-1)P`；唯一需要单独记住的是 `k=2` 时
`(k-1)P=P` 本身为素数，所以可能有 `Q1=P`。这个修正不影响后续 gap 结论。

## 2. 闭复合块与 +2 债务

在 `Q2<P^2` 主分支中，开间隙 `(Q1,Q2)` 内每个合数的最小素因子小于 `P`，因此由 `P` 阶小因子覆盖。
完整 `Q2` 阶轮又包含 `Q1,Q2` 本身，所以对任意 `t>=1`，闭区间

\[
[Q_1+tM_{\le Q_2},\ Q_2+tM_{\le Q_2}]
\]

全部为复合点。真实链的相邻素数端点只能位于该闭块之外：

\[
A_t\le Q_1+tM_{\le Q_2}-1,\qquad B_t\ge Q_2+tM_{\le Q_2}+1.
\]

于是

\[
B_t-A_t\ge Q_2-Q_1+2.
\]

这就是端点替换债务：一次完整 Q2 阶复现至少把真实载体间隙扩大 `2`。

## 3. 样本孔径读数

| P | x0 | Q1 | Q2 | initial gap | closed width | first replay width lower | same aperture replay | same aperture max replays | double aperture max replays |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 13 | 168 | 2179 | 2203 | 24 | 25 | 27 | `false` | 0 | 12 |
| 17 | 1210 | 20563 | 20593 | 30 | 31 | 33 | `false` | 0 | 15 |
| 19 | 3658 | 69499 | 69539 | 40 | 41 | 43 | `false` | 0 | 20 |
| 23 | 58 | 1327 | 1361 | 34 | 35 | 37 | `false` | 0 | 17 |

这些样本只验证孔径增长机制。结论是结构性的：同一闭载体孔径一次也不能容纳端点替换后的真实端点；
任何固定宽度 `W` 只能容纳有限次，次数上界为 `floor((W-W0)/2)`。

## 4. 三分流

| behavior | route | reason |
| --- | --- | --- |
| 端点稳定且孔径不变 | `impossible` | 第一次复现后闭载体宽度至少增加 2。 |
| 固定有限规则扩孔/移动并持久复现 | `ColumnCRT/PDEC` | 扩孔轨道、端点位移和覆盖相位成为同一 formal unit。 |
| 只在孤立窗口发生替换 | `SAE` | 不能支撑无限反例链。 |
| 孔径无界增长或素层持续换新 | `moving-family/H3-DSB/KLS` | 回到尾补洞、短窗 dispersion、Rankin 或外部 DI/BFI。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CorrectEarlyZeroCarrierEndpointBounds | `true` | `true` | 早期零行 [(k-1)P+1,kP] 无素数时，左端相邻素数满足 Q1<=kP-P，除 k=2 可有 Q1=P 外通常为严格小于；右端满足 Q2>kP。 | closed |
| FullQ2ReplayMakesClosedCarrierComposite | `true` | `true` | 在 Q2<P^2 主分支中，开间隙由小于 P 的素因子覆盖；全 Q2 轮又杀掉 Q1,Q2，故 [Q1,Q2]+tM_{<=Q2} 对 t>=1 是闭复合块。 | closed |
| EndpointReplacementDebtPlusTwo | `true` | `true` | 闭复合块的真实相邻素数端点必须落在块外，因此新相邻素数间隙至少为旧间隙加 2。 | closed |
| SameApertureReplayImpossible | `true` | `true` | 第一次全 Q2 复现后闭载体宽度已至少增加 2，不能仍占用原同一有限孔径。 | closed |
| BoundedApertureReplayFinite | `true` | `true` | 若孔径宽度被固定为 W，则最多 floor((W-W0)/2) 次端点替换；无限链必须移动或扩孔。 | closed as bounded-aperture no-go |
| PersistentMovingApertureRoutesToPDECColumnCRT | `true` | `true` | 若扩孔/移动以固定有限相位规则持久复现，则形成 moving aperture 的 ColumnCRT/PDEC formal unit。 | closed as router |
| SparseReplacementRoutesToSAE | `true` | `true` | 若端点替换只在孤立窗口发生，则为 SAE 单窗原子。 | closed as router |
| UnboundedReplacementRoutesToH3DSB | `true` | `true` | 若孔径持续无界增长而不固定相位，则回到 tail filler、H3-DSB/KLS、Rankin 或外部 DI/BFI 分支。 | H3-DSB-NCBLK or moving-family global input |
| GlobalRowColumnUnconditionalClosureReached | `false` | `false` | 本步排除固定有界孔径复现，不排斥所有 moving aperture、PDEC、SAE 与 H3-DSB 出口。 | EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;GlobalFinalInputsStillOpen |

## 6. 最新剩余

```text
EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;GlobalFinalInputsStillOpen
```

本证书排除固定有界孔径的无限复现；它没有排斥 moving aperture、PDEC/ColumnCRT、SAE 与 H3-DSB/KLS 出口，
因此不构成行/列命题的全局无条件证明。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.json` | `6f8c7992da2fcdc0925902c500eb5f568601db52cda061b8c21b38d87becf914` |
| `docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json` | `9f10be0a0445eef5185d4e9d03dab884b330a0ae06b9ff9c7a0ffb910086a804` |
| `docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.json` | `937d22f5dc0bbd7d7c0e6caf3cf7740ed4f0e0f5ca5cc28d6edcf8a42222af2c` |
| `docs/monograph/prime-matrix-zero-row-full-crt-diagonal-minrep.md` | `8fed996d49bd3da39370eb919cac7601759d12152d44d2a39854f3fd236515ab` |
