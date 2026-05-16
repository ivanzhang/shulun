# Prime Matrix AffineTwin moving-key source-rematerialization audit

**状态：** `current_sweep_moving_key_source_rematerialization_closed_global_open`

本审计继续下钻 `MovingPrimitiveKey` 的剩余出口：即使把同向深度公式给出的单侧候选 `q` 当成新 key，候选也必须重新通过 AffineTwin prime gate 与 source materialization gate。

```text
moving_depth_row_count=11
moving_q_formula_occurrence_count=19
unique_moving_q_candidate_count=19
prime_candidate_q_values=[61, 181, 293, 761, 1499, 1747]
affine_twin_prime_gate_q_values=[]
exact_rematerialized_q_values=[]
route_histogram={'CompositeQ': 13, 'PrimeButNotTwinAffine': 6}
min_nearest_available_gap_source_delta=2
moving_key_source_rematerialization_closed_current_sweep=true
```

## 1. candidate q gate 表

| q | route | occ | q prime | q-2 prime | q mod 4=3 | delay integral | same-gap source | exact source | nearest gap source | failed invariants |
| ---: | --- | ---: | --- | --- | --- | --- | ---: | ---: | --- | --- |
| 61 | `PrimeButNotTwinAffine` | 1 | true | true | false | false | 0 | 0 | 59 (delta=-2) | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| 65 | `CompositeQ` | 1 | false | false | false | false | 0 | 0 | 59 (delta=-6) | `gap_source_absent,q_composite` |
| 96 | `CompositeQ` | 1 | false | false | false | false | 0 | 0 | 59 (delta=-37) | `gap_source_absent,q_composite` |
| 111 | `CompositeQ` | 1 | false | true | true | true | 0 | 0 | 59 (delta=-52) | `gap_source_absent,q_composite` |
| 119 | `CompositeQ` | 1 | false | false | true | true | 0 | 0 | 59 (delta=-60) | `gap_source_absent,q_composite` |
| 123 | `CompositeQ` | 1 | false | false | true | true | 0 | 0 | 59 (delta=-64) | `gap_source_absent,q_composite` |
| 154 | `CompositeQ` | 1 | false | false | false | false | 0 | 0 | 59 (delta=-95) | `gap_source_absent,q_composite` |
| 181 | `PrimeButNotTwinAffine` | 1 | true | true | false | false | 0 | 0 | 59 (delta=-122) | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| 235 | `CompositeQ` | 1 | false | true | true | true | 0 | 0 | 59 (delta=-176) | `gap_source_absent,q_composite` |
| 293 | `PrimeButNotTwinAffine` | 1 | true | false | false | false | 0 | 0 | 59 (delta=-234) | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 297 | `CompositeQ` | 1 | false | false | false | false | 0 | 0 | 59 (delta=-238) | `gap_source_absent,q_composite` |
| 355 | `CompositeQ` | 1 | false | true | true | true | 0 | 0 | 59 (delta=-296) | `gap_source_absent,q_composite` |
| 386 | `CompositeQ` | 1 | false | false | false | false | 0 | 0 | 59 (delta=-327) | `gap_source_absent,q_composite` |
| 575 | `CompositeQ` | 1 | false | false | true | true | 0 | 0 | 59 (delta=-516) | `gap_source_absent,q_composite` |
| 699 | `CompositeQ` | 1 | false | false | true | true | 0 | 0 | 59 (delta=-640) | `gap_source_absent,q_composite` |
| 761 | `PrimeButNotTwinAffine` | 1 | true | false | false | false | 0 | 0 | 59 (delta=-702) | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 1375 | `CompositeQ` | 1 | false | true | true | true | 0 | 0 | 59 (delta=-1316) | `gap_source_absent,q_composite` |
| 1499 | `PrimeButNotTwinAffine` | 1 | true | false | true | true | 0 | 0 | 59 (delta=-1440) | `gap_source_absent,q_minus_2_is_prime` |
| 1747 | `PrimeButNotTwinAffine` | 1 | true | false | true | true | 0 | 0 | 59 (delta=-1688) | `gap_source_absent,q_minus_2_is_prime` |

## 2. 最窄 atom 的源重物化读数

上一层最窄 depth atom 是 `19:12`；其 moving-depth 公式给出的候选 `q` 为 `[61, 111]`。
其中 `q=111` 为合数；`q=61` 虽然 `61` 与 `59` 均为素数，但 `61≡1 mod 4`，使 `p_delay=(11q-21)/4` 非整数，并且当前没有 gap `q=61` 的 matching source。
最接近的已物化 gap source 是 `q=59`，但它的角色是 `generator=61, fill=59, sides=minus->minus, p_delay=70`，不是 `q=61` AffineTwin 期望的 `generator=59, fill=61, sides=minus->plus`。

## 3. 结论边界

- 当前 moving-depth 公式产生 `19` 个唯一候选 `q`：`13` 个合数，`6` 个素数但全部不是同向 AffineTwin key。
- 没有任何候选 `q` 同时通过 AffineTwin prime gate 与 source materialization gate；当前 sweep 的 source-rematerialization 吸收通道关闭。
- 这仍不是全局行/列无条件证明；剩余是方向改变、source 重物化全局非持久性或 endpoint release coupling 的排斥/路由。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-moving-key-depth-formula-ledger.json` | `a7b409c9a56a1d073c4cc77577aa128bc872b7b2c688381d3467e85ddd665583` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/prime-matrix-affine-twin-source-materialization-gate-ledger.json` | `aaaee80eaba6130fa016758509513449beff23eaefa41fcc79a174e183c5e385` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
