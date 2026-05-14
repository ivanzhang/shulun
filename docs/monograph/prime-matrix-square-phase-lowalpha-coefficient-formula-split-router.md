# Prime Matrix square-phase low-alpha Selberg 系数公式拆分

**状态：** `full_support_coefficient_formula_closed_tail_angle_bound_open`

Selberg lcm 系数已拆成两个严格对象：当 `m<=D` 时，全支撑部分满足显式公式 `c_m=mu(m)(1-sum_{q|m}(log q)^2/(log D)^2)`；`m>D` 的部分完全来自 `d,e<=D` 但 `lcm(d,e)>D` 的截断尾。因此统一角度界可进一步拆成核心 Möbius-log 余项角度与截断尾角度。默认样本两部分均远低于所需 equal-split 角度；剩余是分别证明核心角度界和截断尾角度界，或把失败登记为 VectorSquarefree-PDEC。

```text
full_support_mobius_log_coefficient_formula_closed=true
core_tail_angle_split_contract_closed=true
sample_satisfies_core_tail_split_contract=true
core_mobius_log_residual_angle_bound_proved=false
truncation_tail_angle_bound_proved=false
vector_squarefree_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 核心/截断尾拆分

| z | core count | tail count | formula max err | core angle | tail angle | required split angle | split Cauchy / total Cauchy |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 16 | 0 | 0.000000 | 0.049281 | n/a | 8.509258 | 1.000000 |
| 13 | 49 | 15 | 0.000000 | 0.019868 | 0.051287 | 2.715323 | 0.939380 |
| 31 | 153 | 963 | 0.000000 | 0.007544 | 0.002264 | 0.591273 | 0.816993 |
| 61 | 250 | 5476 | 0.000000 | 0.003372 | 0.002074 | 0.221522 | 0.819023 |

## 2. 证明边界

- 已闭合：`m<=D` 全支撑系数的显式 Möbius-log 公式。
- 已闭合：把总角度合同无损替换为 core/tail equal-split 充分合同。
- 最紧 equal-split 行为 `z=61`，需要 core 与 tail 角度均不超过 `0.221522`。
- 未闭合：核心 Möbius-log 余项角度界。
- 未闭合：`m>D` 截断尾角度界。
- 未闭合：若任一角度界失败，证明其形成可排斥的 `VectorSquarefree-PDEC`。
- 下一目标：`CoreMobiusLogResidualAngleAndTruncationTailAngleBoundOrVectorPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.json` | `c878fa116d9ed2febc51f7933e096c3b366ad1027079cc91febd46c01fa3806f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `experiments/prime_matrix_square_phase_lowalpha_coefficient_formula_split_router.py` | `f2666b0db97c0507500b15012c25d37c499b721b7102296a8c8d3a73c60ccf2f` |
