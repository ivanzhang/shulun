# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin prime gate router

**状态：** `affine_twin_prime_gate_closed_current_sweep_global_bound_open`

本步把仿射塌缩原子压成 twin-prime 型必要条件门：当前 `q=31`，`generator_ell=q-2=29` 与 `fill_ell=q=31` 均为素数，且 `q≡3 mod 4`，从而所有仿射参数为整数。全局剩余是证明此类 AffineTwin 门无法持久复现，或排斥持久 AffineTwin-PDEC/SAE。

```text
affine_twin_gate_row_count=1
unique_affine_twin_gate_key_count=1
repeated_affine_twin_gate_key_count=0
all_twin_prime_gates_closed_current_sweep=true
all_gap_congruent_3_mod_4=true
all_affine_integrality_gates_closed=true
row_column_unconditional_closed=false
```

## 1. twin-prime 型门

| q | generator ell | fill ell | q prime | q-2 prime | q mod 4 | key |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 29 | 31 | `true` | `true` | 3 | `q=31|twin=29,31|qmod4=3` |

## 2. 结构结论

- 当前仿射塌缩不是一般整数模式，而要求 `q` 与 `q-2` 同时为素数。
- `q≡3 mod 4` 是 `|delta_u|=(q-3)/4` 的整数门。
- 这不是全局孪生素数定理；这里只是把持久仿射失败的必要条件登记为更窄 PDEC 入口。

## 3. 下一步

- 主攻：`AffineTwinPrimeGateBoundOrAffineTwinPDECExclusion`。
- 将 AffineTwin 门与 slot-depth/CRT 相位条件合并，证明其不可持久或登记为最终 AffineTwin-PDEC。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_prime_gate_router.py` | `fdcbc14c64f857554af2ddf40767644694f9b233f100db0bf222ba5e43260a17` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json` | `ffe10c92b29452a7e91fee637f355909cbbf890e61a75c270f82b7bf913722ec` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json` | `223a7643a7779a06880ff1790997d2bfd3b4416f62ca6a65e35c57c8fac3b94c` |
