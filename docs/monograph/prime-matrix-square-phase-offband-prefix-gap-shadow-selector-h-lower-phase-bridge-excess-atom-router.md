# Prime Matrix square-phase off-band prefix gap shadow selector H lower phase bridge excess atom router

**状态：** `phase_bridge_excess_atom_materialized_current_sweep_global_bound_open`

本步把唯一相位桥超标登记为显式原子：`gap_ell=31` 的 phase bridge 超出一个 gap 的量为 15，而左右深度余量合计为 28，吸收后仍余 13。当前没有重复超标原子。全局剩余是证明这种超标总能被深度余量吸收，或排斥持久 PhaseBridgeExcess-PDEC/SAE。

```text
phase_bridge_excess_atom_count=1
unique_phase_bridge_excess_atom_key_count=1
repeated_phase_bridge_excess_atom_key_count=0
all_excess_atoms_absorbed_current_sweep=true
max_phase_bridge_gap_excess=15
min_absorbing_spare_after_bridge_excess=13
row_column_unconditional_closed=false
```

## 1. 超标原子

| gap ell | bridge gap | excess | right spare | left spare | spare after excess | key |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 46 | 15 | 25 | 3 | 13 | `dir=lower|gap=31|gen=29|fill=31|bridge=46|excess=15|gr=6|fl=28|slack=13` |

## 2. 结构结论

- 当前 phase bridge 超标只有一个原子，且已被左右深度余量吸收。
- 这个原子是 `3*gap_ell` 短走廊余量最紧来源；若全局复现或失控，就是下一层 PDEC 入口。
- 全局闭合仍需证明超标吸收界，而不是把当前单例直接外推。

## 3. 下一步

- 主攻：`PhaseBridgeExcessAbsorptionBoundOrExcessPDECExclusion`。
- 对 phase bridge excess 的可吸收性建立全局不等式，或证明重复 excess key 不可持久。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_phase_bridge_excess_atom_router.py` | `89ce78311940ce6080acae9b101b28ae797d57a8b5f91341da752f4d484af7c1` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json` | `53a5e2b1c0a7fb57d210885b9719c9aefa93cdaa5e34ff579e9df37187fdb969` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json` | `67ab0cebcf763917e8d47ad1da598e9a836d7b7138a56e100e84d9f9a0c11218` |
