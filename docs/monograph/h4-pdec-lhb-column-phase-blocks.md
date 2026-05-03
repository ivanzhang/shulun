# H4-PDEC Q=2310 LHB Column Phase Blocks

**状态：** `q2310_lhb_column_phase_blocks_materialized_finite_certificate`

Q=2310 的 LHB column rows 已输出机器可读 phase_block 与 bound。空异常块可作为有限 A 行；整洞集亏损与桥洞临界块仍是诊断支撑，需进一步证明正式坏窗集合 S 的投影关系后才能进入全局 PDEC-Dual-Cert。

## 1. 来源指纹

| source | sha256 |
| --- | --- |
| `phase_block_script` | `61d1c115eb01e6d7a1004d65e441319e52f678a1a8f9a229db3887318fccd534` |
| `rigidity_audit_script` | `6426a098d4245a6b183be85c6e802e875f195216ebf43e9a07a27c80c74d06f7` |
| `capacity_script` | `6b00cd84807501d7a1f228aef5f24c23642a55caf56e7a6f957ef63ba8fcc568` |

## 2. P 汇总

| P | zero | whole deficit | critical | bridged | unbridged | negative delta | affine failures |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 2306 | 2306 | 0 | 0 | 0 | 0 | 0 |
| 17 | 2282 | 2282 | 0 | 0 | 0 | 0 | 0 |
| 19 | 2170 | 2170 | 0 | 0 | 0 | 0 | 0 |
| 23 | 2078 | 2078 | 0 | 0 | 0 | 0 | 0 |
| 29 | 2160 | 2160 | 0 | 0 | 0 | 0 | 0 |
| 31 | 1714 | 1714 | 0 | 0 | 0 | 0 | 0 |
| 37 | 1500 | 1500 | 0 | 0 | 0 | 0 | 0 |
| 43 | 260 | 220 | 40 | 40 | 0 | 0 | 0 |
| 47 | 44 | 32 | 12 | 12 | 0 | 0 | 0 |

## 3. 机器行摘要

| row_id | block | size | bound | admissibility | pass |
| --- | --- | ---: | ---: | --- | --- |
| `CC-LHB-AFFINE-Q2310-P13` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P13` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P13` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P13` | `whole_deficit_phases` | 2306 | 2306 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P13` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P17` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P17` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P17` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P17` | `whole_deficit_phases` | 2282 | 2282 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P17` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P19` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P19` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P19` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P19` | `whole_deficit_phases` | 2170 | 2170 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P19` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P23` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P23` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P23` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P23` | `whole_deficit_phases` | 2078 | 2078 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P23` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P29` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P29` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P29` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P29` | `whole_deficit_phases` | 2160 | 2160 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P29` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P31` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P31` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P31` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P31` | `whole_deficit_phases` | 1714 | 1714 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P31` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P37` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P37` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P37` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P37` | `whole_deficit_phases` | 1500 | 1500 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P37` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P43` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P43` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P43` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P43` | `whole_deficit_phases` | 220 | 220 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P43` | `bridged_critical_phases` | 40 | 40 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q2310-P47` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q2310-P47` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q2310-P47` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q2310-P47` | `whole_deficit_phases` | 32 | 32 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q2310-P47` | `bridged_critical_phases` | 12 | 12 | `diagnostic-phase-support` | `True` |

## 4. 审稿边界

- `A-ready-empty-anomaly-block` 行已经有 `phase_block` 与 `bound=0`；在有限 `Q=2310` 范围内可作为空异常块约束。
- `diagnostic-phase-support` 行只登记支撑相位；若要进入 `A,b,E,e`，还需证明正式坏窗集合 `S` 投影到这些相位块并给出对应容量界。
- 本文件不证明全局 `PDEC exclusion`，也不把有限相位块推广到无限 `P`。
