# Prime Matrix square-phase low-alpha z=61 positive lift factor gate bridge

**状态：** `z61_positive_lift_root_selector_reduced_to_prime_factor_lift_gates_open`

MissingLift 的唯一根选择可进一步压成两个素因子提升门：q4=37 门是普通平方根从 M 提升到 M*q4，q2=71 门是带偏移项 `2Mq4` 的平方根提升到 M*q2。在当前 32 个一级 CRT 根上，这两个门各自单独唯一选中同一根 r=26951，合并提升门也唯一。剩余因此变成素因子提升门的全局容量界，或 MissingLift-PDEC。

```text
secondary_congruence_candidate_count=1
full_gate_candidate_count=1
q4_gate_already_unique=true
q2_gate_already_unique=true
combined_lift_unique=true
positive_lift_factor_gate_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. 二级同余与商门

| M | delta | selected r | secondary factor | gate modulus | target gate | full gate roots |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 57684 | 527 | 26951 | 5254 | 5254 | 5180 | 1 |

## 2. 素因子门

| gate | pass residues | unique |
| --- | --- | --- |
| q4=37 | `[26951]` | true |
| q2=71 | `[26951]` | true |

## 3. 提升模数

| lift | modulus | unique |
| --- | ---: | --- |
| q4 plain | 2134308 | true |
| q2 shifted | 4095564 | true |
| combined | 151535868 | true |

## 4. 证明边界

- 已闭合：当前 MissingLift 根选择器与素因子提升门严格同一对象。
- 未闭合：全局素因子提升门容量界，或 MissingLift-PDEC 排斥。
- 下一目标：`PrimeFactorLiftGateGlobalBoundOrMissingLiftPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json` | `c66831f311c44073cdb40319bbf5be0d2b2871fa38f41759c97898b14a39289b` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json` | `13e9c08af07e9334f12512d78c5f75889a0e4b17fb1669d15f308044a28d4502` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json` | `470a79443beba230550a0ecdb6607b9aeedbee15221fe893d7c798783db6388d` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json` | `7f446ac49e7adea229ea0c83f7b5a1620d4aa7140d09ca5a435bf28a1c29c67e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_factor_gate_bridge_router.py` | `1d4ebd1ae5e75f43dce4a4726ffe850288f4a4795e4919969233bff857e88ed3` |
