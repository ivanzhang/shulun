# Prime Matrix square-phase off-band prefix gap shadow selector H lower phase bridge excess source router

**状态：** `phase_bridge_excess_source_identity_closed_current_sweep_global_bound_open`

本步把唯一 phase bridge 超标的来源继续压缩：超标量等于生成端 margin，也等于 `3*rho_jump`；超标被吸收后的剩余 slack 等于 `|delta_b|`。因此当前超标不是自由相位漂移，而是由 margin、rho 翻转和 b 槽位移锁定的单原子。全局剩余是证明该来源身份的吸收界，或排斥持久 Source-PDEC/SAE。

```text
phase_bridge_excess_source_count=1
unique_phase_bridge_excess_source_key_count=1
repeated_phase_bridge_excess_source_key_count=0
all_excess_equals_generator_margin=true
all_excess_equals_three_rho_jump=true
all_post_absorption_slack_equals_abs_delta_b=true
row_column_unconditional_closed=false
```

## 1. 来源身份

| gap ell | excess | generator margin | 3*rho jump | slack after | |delta b| | source key |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 15 | 15 | 15 | 13 | 13 | `dir=lower|gap=31|rho=5|gm=15|db=-13|slack=13` |

## 2. 结构结论

- 当前唯一超标量被生成端 margin 精确解释，同时由 `rho` 从 2 到 7 的翻转给出。
- 超标吸收后剩余的 13 不是松散余量，而是等于 `b` 槽位移的绝对值。
- 若全局出现不可吸收超标，必须破坏这些来源身份或复现更短的 Source-PDEC 键。

## 3. 下一步

- 主攻：`GeneratorMarginRhoSlotAbsorptionBoundOrSourcePDECExclusion`。
- 将 `excess=generator_margin=3*rho_jump` 与 `slack=|delta_b|` 作为硬约束，继续排斥持久来源原子。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_phase_bridge_excess_source_router.py` | `70d38598ac67b953da835e93fd2badce00a748489034cb578f9d06a4a026f52e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json` | `67ab0cebcf763917e8d47ad1da598e9a836d7b7138a56e100e84d9f9a0c11218` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json` | `3db447d1c8fc9bfb346b90cd809f88f0e21999c6618937f7b798ca17091787bf` |
