# H4-PDEC Q=2310 LHB Column Phase Blocks

**状态：** `q2310_lhb_column_phase_blocks_materialized_finite_certificate`

Q=2310 的 LHB column rows 已输出机器可读 phase_block 与 bound。空异常块可作为有限 A 行；整洞集亏损与桥洞临界块仍是诊断支撑，需进一步证明正式坏窗集合 S 的投影关系后才能进入全局 PDEC-Dual-Cert。

## 1. 来源指纹

| source | sha256 |
| --- | --- |
| `phase_block_script` | `d842a5a8f219c9deb5c74c0ba96fcff497fbb94a9328eb511e59ac295298ab9d` |
| `rigidity_audit_script` | `6426a098d4245a6b183be85c6e802e875f195216ebf43e9a07a27c80c74d06f7` |
| `capacity_script` | `6b00cd84807501d7a1f228aef5f24c23642a55caf56e7a6f957ef63ba8fcc568` |

## 2. P 汇总

| P | zero | whole deficit | critical | bridged | unbridged | negative delta | affine failures |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 30002 | 30002 | 0 | 0 | 0 | 0 | 0 |
| 19 | 29662 | 29662 | 0 | 0 | 0 | 0 | 0 |
| 23 | 29094 | 29094 | 0 | 0 | 0 | 0 | 0 |
| 29 | 29420 | 29420 | 0 | 0 | 0 | 0 | 0 |

## 3. 机器行摘要

| row_id | block | size | bound | admissibility | pass |
| --- | --- | ---: | ---: | --- | --- |
| `CC-LHB-AFFINE-Q30030-P17` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q30030-P17` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q30030-P17` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q30030-P17` | `whole_deficit_phases` | 30002 | 30002 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q30030-P17` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q30030-P19` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q30030-P19` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q30030-P19` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q30030-P19` | `whole_deficit_phases` | 29662 | 29662 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q30030-P19` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q30030-P23` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q30030-P23` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q30030-P23` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q30030-P23` | `whole_deficit_phases` | 29094 | 29094 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q30030-P23` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |
| `CC-LHB-AFFINE-Q30030-P29` | `affine_rigidity_failure_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-NEGDELTA-Q30030-P29` | `negative_delta_zero_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-UNBRIDGED-Q30030-P29` | `unbridged_critical_phases` | 0 | 0 | `A-ready-empty-anomaly-block` | `True` |
| `CC-LHB-WHOLEDEF-Q30030-P29` | `whole_deficit_phases` | 29420 | 29420 | `diagnostic-phase-support` | `True` |
| `CC-LHB-BRIDGED-Q30030-P29` | `bridged_critical_phases` | 0 | 0 | `diagnostic-phase-support` | `True` |

## 4. 审稿边界

- `A-ready-empty-anomaly-block` 行已经有 `phase_block` 与 `bound=0`；在有限 `Q=2310` 范围内可作为空异常块约束。
- `diagnostic-phase-support` 行只登记支撑相位；若要进入 `A,b,E,e`，还需证明正式坏窗集合 `S` 投影到这些相位块并给出对应容量界。
- `diagnostic-phase-support` 行表中的 `bound=phase_block_size` 只是支撑大小，不是 persistent 计数向量 `g(t)` 的容量界；转移条件见 `h4-pdec-lhb-support-to-capacity-transfer.md`。
- 本文件不证明全局 `PDEC exclusion`，也不把有限相位块推广到无限 `P`。
