# Prime Matrix square-phase off-band prefix gap shadow selector H lower transport-cell reset-PDEC router

**状态：** `transport_reset_pdec_registered_current_atoms_empty`

本步把非连续 transport 复现登记为 reset-PDEC：若同一 transport cell 不沿同一链连续复现，仍要重复完整 cell key。当前 12 个 transport cell key 全部唯一，reset-PDEC atom 数为 0。因此 transport 分支的当前样本没有未吸收 atom；全局仍需证明 reset atom 不会持久出现，或转入 SAE/Rankin。

```text
transport_cell_count=12
unique_transport_cell_key_count=12
repeated_transport_cell_key_count=0
reset_pdec_atom_count=0
chained_transport_persistence_excluded_current_sweep=true
row_column_unconditional_closed=false
```

## 1. reset-PDEC 口径

非连续 transport 复现必须重复完整 key：

```text
side, ell, crt_residue, p_lift, slot_sum_lift, b_residue_step, lo_translate_defect, hi_translate_defect, common_lower_active, common_upper_active
```

## 2. 当前 atom

当前 reset-PDEC atom 数为 `0`。

## 3. 结构判断

- 链式 transport 已由深度漂移给出有限寿命。
- 非连续 transport 被登记为完整 key 重复的 reset-PDEC。
- 当前扫描 reset atom 缺席；全局仍需排斥或给 SAE/Rankin 可求和。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `transport_reset_pdec_formal_unit` | `closed` | A non-chained transport recurrence must repeat the full transport-cell key, including side, ell, residue, lifts, residue step, edge defects, and active edge modes. |
| `current_sweep_transport_reset_atoms_empty` | `closed_on_current_sweep` | No transport-cell key repeats in the current sweep after chained persistence has been bounded. |
| `global_transport_reset_pdec_exclusion_open` | `open` | A global proof must exclude reset-PDEC atoms, or route their sparse occurrence to SAE/Rankin. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TransportResetFormalUnitClosed` | `true` | `true` | 非连续复现必须重复完整 transport cell key，不再有未命名自由度。 | closed |
| `CurrentResetPDECAtomsEmpty` | `true` | `false` | 当前扫描中 transport reset atom 缺席。 | finite evidence only |
| `GlobalResetPDECExcluded` | `false` | `false` | 仍需全局排斥 transport reset atom，或证明其 SAE/Rankin 可求和。 | TransportResetPDECExclusion |
| `SingletonResidueSAESummabilityProved` | `false` | `false` | singleton residue packet 仍需独立 SAE/Rankin 账本。 | SingletonResidueSAE/Rankin |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步登记 reset-PDEC 口径，不关闭全局命题。 | TransportResetPDECExclusionOrSingletonResidueSAESummability |

## 6. 下一步

- 主攻：`TransportResetPDECExclusionOrSingletonResidueSAESummability`。
- 若继续攻 transport 分支，目标是全局排斥 reset-PDEC atom。
- 若转入另一门，目标是 singleton residue SAE/Rankin 可求和。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_transport_cell_reset_pdec_router.py` | `731a19cbc67950eb32dd31d6c41663c4d9145d4e317e5c9237e5379fbd59e865` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json` | `7a6af4c73819b3e86322f0b0e40032dc0e98a3f114eab5b163284c85e2b6f23b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json` | `45e0a3f337d03dbc6317776e3350aa75a018d155062b6ce4c24fd8b65bbca692` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json` | `e6f6e91cf374354bf5834506a580029f1c9518c04f79d4df741d5e11549fac6b` |
