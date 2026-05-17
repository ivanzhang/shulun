# Prime Matrix H-lower endpoint motion stencil audit

**状态：** `endpoint_motion_stencil_closed_current_sweep_global_open`

本审计把活跃素数带端点的运动拆成三类相邻模板：外向邻素数、端点自身、内向核心边缘。当前 sweep 中外向邻素数没有到达，端点自身是 minus-only 单原子，内向一步立即进入双侧核心支撑。

```text
active_band_endpoints=[23, 109]
outward_neighbor_primes=[19, 113]
inward_core_edge_primes=[29, 107]
outward_neighbors_empty_current_sweep=true
endpoints_are_minus_singletons_current_sweep=true
inward_edges_are_core_absorption_current_sweep=true
endpoint_motion_stencil_closed_current_sweep=true
```

## 1. motion stencil

| label | ell | records | sides | residues | slots | type |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| `lower_outward_neighbor` | 19 | 0 | `[]` | 0 | 0 | `empty` |
| `lower_endpoint_atom` | 23 | 1 | `['minus']` | 1 | 1 | `minus-only singleton` |
| `lower_inward_core_edge` | 29 | 4 | `['minus', 'plus']` | 4 | 4 | `both-side core` |
| `upper_inward_core_edge` | 107 | 6 | `['minus', 'plus']` | 6 | 6 | `both-side core` |
| `upper_endpoint_atom` | 109 | 1 | `['minus']` | 1 | 1 | `minus-only singleton` |
| `upper_outward_neighbor` | 113 | 0 | `[]` | 0 | 0 | `empty` |

## 2. route rows

| gate | closed | evidence | global remaining |
| --- | --- | --- | --- |
| `OutwardNeighborNoArrival` | true | outside primes 19,113 have total records [0, 0] | `EndpointOutwardArrivalBound` |
| `EndpointAtomsMinusSingleton` | true | endpoint primes 23,109 are minus-only singletons | `EndpointAtomPDEC/SAE` |
| `InwardMotionBecomesCoreAbsorption` | true | core edge primes 29,107 have both-side support | `CoreEdgeAbsorptionMultiplicityBound` |

## 3. 结论边界

当前 sweep 中，端点运动不能作为未分类容量来源：外向一步没有物化，端点自身只有两个 minus-only 单原子，内向一步已经进入核心吸收带。

这仍不是全局证明。下一步必须证明外向端点到达受限，或把端点原子复现排斥为 EndpointAtom-PDEC/SAE；核心边缘的多重吸收则需要独立 multiplicity bound。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json` | `60a85b991523e1af0bdb40c950945b3db3163d1132d1ff441e8ccbc46ade0ac6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json` | `f2876c431b7c4ff762deb76e26f43d974388fab22a1ee854f64fa39944ce280e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json` | `6103b7e8cd2e58cc533135f4fec5d489fa28e6eb6bc9b9c378c748635ecb901d` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_band_atom_router.py` | `5ab1848bb4339c189c302b2d6add9cde64c94d26eb0185b2d106393aad1845bb` |
