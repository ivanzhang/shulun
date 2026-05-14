# Prime Matrix square-phase low-alpha 正交余量合同

**状态：** `selberg_constant_margin_reduced_to_uniform_angle_bound_open`

Selberg 常数 `C` 的剩余要求可精确写成角度合同：若 `|<c,R>|/(||c||_2||R||_2)` 不超过每个 `z` 的 required angle，则 `Q_direct<=C*Mertens`。默认 `C=1.35` 下最紧行是 `z=61`，只需统一角度界约 `0.181432`；这比样本观测角度 `0.001089` 宽很多。剩余不再是模糊取消，而是证明该统一角度界，或证明违反该角度界即 VectorSquarefree-PDEC。

```text
selberg_constant_margin_contract_closed=true
sample_satisfies_margin_contract=true
uniform_angle_bound_proved=false
vector_squarefree_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 角度合同

| z | model/M | direct/M | margin/M | Cauchy/M | required angle | observed angle | slack |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 1.049513 | 1.047772 | 0.300487 | 0.035313 | 8.509258 | 0.049281 | 8.459977 |
| 13 | 1.073183 | 1.071388 | 0.276817 | 0.108525 | 2.550721 | 0.016545 | 2.534176 |
| 31 | 1.123223 | 1.125625 | 0.226777 | 0.469452 | 0.483066 | 0.005116 | 0.477950 |
| 61 | 1.179339 | 1.180363 | 0.170661 | 0.940637 | 0.181431 | 0.001089 | 0.180343 |

## 2. 证明边界

- 最紧验收行为 `z=61`，所需统一角度界为 `0.181431`。
- 已闭合：角度界推出 `Q_direct<=C*Mertens` 的合同推理。
- 未闭合：证明该统一角度界本身。
- 未闭合：若角度界失败，证明失败向量形成可排斥的 `VectorSquarefree-PDEC`。
- 下一目标：`UniformCoefficientRemainderAngleBoundTheta0182OrVectorSquarefreePDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json` | `84244d3cf8123184df947d08b0a51ad00be6febc247b5672a519ee23a19e6fea` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.json` | `cec2e980f4c745ba72127216f53911a90c41de70b3f1c800b72675287edc1733` |
| `experiments/prime_matrix_square_phase_lowalpha_orthogonality_margin_contract_router.py` | `39652e8b927a14b3838ceff3b2a3bd7efd16bb2e8865cdbb44f6f07ca28d3249` |
