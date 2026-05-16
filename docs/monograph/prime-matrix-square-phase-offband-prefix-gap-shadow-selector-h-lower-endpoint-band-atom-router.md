# Prime Matrix square-phase off-band prefix gap shadow selector H lower endpoint band atom router

**状态：** `endpoint_band_atoms_isolated_current_sweep_motion_bound_open`

当前活跃 `ell` 素数带的两个外端点 `[23, 109]` 都不是高占用块，而是 minus-only 单原子：每个端点只有一个物理记录、一个 residue 和一个 slot。双侧核心边缘 `[29, 107]` 则已进入多记录核心带。因此下一层全局硬点可精确表述为：端点若随尺度继续移动，必须证明其移动受限，或把反复出现的端点原子登记并排斥为 EndpointAtom-PDEC/SAE。

```text
active_band_endpoints=[23, 109]
both_side_core_edges=[29, 107]
endpoint_atom_count=2
endpoint_atoms_are_singletons_current_sweep=true
endpoint_residues_are_singletons_current_sweep=true
endpoint_slots_are_singletons_current_sweep=true
endpoint_only_minus_current_sweep=true
row_column_unconditional_closed=false
```

## 1. 外端点行

| side | ell | records | residues | slots | Rankin mass | p range | min margin | min crt-phase gap |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| `minus` | 23 | 1 | 1 | 1 | 0.043478 | `4987..4987` | 45 | 2 |
| `plus` | 23 | 0 | 0 | 0 | 0.000000 | `empty` | None | None |
| `minus` | 109 | 1 | 1 | 1 | 0.009174 | `9817..9817` | 74 | 82 |
| `plus` | 109 | 0 | 0 | 0 | 0.000000 | `empty` | None | None |

## 2. 外端点原子

| ell | p | side | residue | slot | margin | left depth | right depth |
| ---: | ---: | --- | ---: | --- | ---: | ---: | ---: |
| 23 | 4987 | `minus` | 19 | `['484:116:23']` | 45 | 1 | 19 |
| 109 | 9817 | `minus` | 7 | `['853:179:109']` | 74 | 8 | 18 |

## 3. 双侧核心边缘对照

| side | ell | records | residues | slots | Rankin mass | p range |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `minus` | 29 | 3 | 3 | 3 | 0.103448 | `2687..6337` |
| `plus` | 29 | 1 | 1 | 1 | 0.034483 | `3187..3187` |
| `minus` | 107 | 5 | 5 | 5 | 0.046729 | `9277..9907` |
| `plus` | 107 | 1 | 1 | 1 | 0.009346 | `9419..9419` |

## 4. 结构结论

- 外端点是单原子，不是当前 Rankin 主质量来源。
- 双侧核心边缘已经有多 residue、多 slot 支撑，说明端点增长与核心带填充是不同机制。
- 全局证明不能把当前端点孤立性当作定理；下一步必须证明端点移动受限，或把端点复现登记为 EndpointAtom-PDEC/SAE 并排斥。

## 5. 下一步

- 主攻：`EndpointBandMotionBoundOrEndpointAtomPDECExclusion`。
- 直接检查端点移动的完整键是否会在相邻尺度复现；若复现，进入端点 PDEC；若不复现，进入端点 SAE/Rankin。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_band_atom_router.py` | `5ab1848bb4339c189c302b2d6add9cde64c94d26eb0185b2d106393aad1845bb` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json` | `f2876c431b7c4ff762deb76e26f43d974388fab22a1ee854f64fa39944ce280e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json` | `60a85b991523e1af0bdb40c950945b3db3163d1132d1ff441e8ccbc46ade0ac6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json` | `6103b7e8cd2e58cc533135f4fec5d489fa28e6eb6bc9b9c378c748635ecb901d` |
