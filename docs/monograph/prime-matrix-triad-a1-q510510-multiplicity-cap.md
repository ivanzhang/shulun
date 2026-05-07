# H4-PDEC Q=2310 LHB 多重度容量证书

**状态：** `q2310_lhb_multiplicity_caps_materialized_for_allowed_set`

WHOLEDEF/BRIDGED 支撑相位已配套同一 Q=2310 的 M(t) 投影容量。在 LHB allowed-set 分支中这些支撑块给出 bound=0 的容量行；全局 PDEC 仍需单独证明当前 S subset Z_LHB。

## 1. 证书语义

M(t) 是 LHB 允许全集 Z_LHB(p,Q) 在相位 t 上的投影计数，即高层 CRT 补洞完成数。若正式坏窗集合 S 已证明包含于 Z_LHB，则 g(t)<=M(t)。

本证书使用 `M(t)=completion_count(t)`。因此对任意已证明 `S subset Z_LHB(p,Q)` 的坏窗族，

\[
g(t)\le M(t)
\]

逐相位成立。注意：这不是全局 PDEC 排除证明；它只物化 LHB allowed-set 投影容量。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `multiplicity_cap_script` | `c85fc317d8c20da6e823cf46166bfac3db72a6a6034ec62ed07b58bbd1e2a109` |
| `capacity_script` | `6b00cd84807501d7a1f228aef5f24c23642a55caf56e7a6f957ef63ba8fcc568` |
| `phase_blocks_json` | `c23421c9ddd39473292f9ac29056bb8aa802c931b3f3252e661b5f4e70bfbddd` |

## 3. `M(t)` 汇总

| P | high primes | total allowed rows | nonzero M phases | max M |
| ---: | --- | ---: | ---: | ---: |
| 19 | `[]` | 496 | 496 | 1 |
| 23 | `[19]` | 3456 | 2592 | 19 |

## 4. 升级容量行

| row_id | block | phase count | bound | all M=0 | pass |
| --- | --- | ---: | ---: | --- | --- |
| `CC-LHB-WHOLEDEF-MULT-Q510510-P19` | `whole_deficit_phases` | 510014 | 0 | `True` | `True` |
| `CC-LHB-BRIDGED-MULT-Q510510-P19` | `bridged_critical_phases` | 0 | 0 | `True` | `True` |
| `CC-LHB-WHOLEDEF-MULT-Q510510-P23` | `whole_deficit_phases` | 507918 | 0 | `True` | `True` |
| `CC-LHB-BRIDGED-MULT-Q510510-P23` | `bridged_critical_phases` | 0 | 0 | `True` | `True` |

## 5. 审稿边界

- 本证书把 `WHOLEDEF/BRIDGED` 的容量界从支撑大小替换为 `sum_C M(t)`。
- 本轮全部升级行均满足 `bound=0`，因为这些相位块位于 `completion_count(t)=0` 的支撑内。
- 这些行的正式使用条件是 `S subset Z_LHB(p,Q)`；没有该包含关系时不能用于任意 PDEC 坏窗集合。
- 本证书仍是有限 `Q=2310`、有限 `P` 范围证书，不推广到无限族。
