# Prime Matrix global named-exit terminal choke router

**状态：** `terminal_choke_set_current_sweep_closed_global_open`

after-cutset 的十个命名出口可以进一步合并为五个终端 choke。当前 sweep 中五个 choke 都有显式容量/相位余量或已命名路由：CRT 相位余量 879，端点释放最小额外量 50，transport reset atom 为 0，one-slot epoch 总剩余容量比例约 0.9039、单 epoch 最小剩余比例约 0.6901，paired pressure 最大仅 0.1602。因此最新硬点不是局部容量缺口，而是这些余量能否在全局持久族中被反复复现；若能复现，必须进入对应的 PDEC/SAE/ColumnCRT 终端。

```text
terminal_choke_count=5
all_terminal_chokes_closed_current_sweep=true
row_column_unconditional_closed=false
formal_pair_total=40
formal_to_actual_gap=39
unresolved_formal_pair_total_current=0
crt_phase_margin=879
min_endpoint_release_total_required=70
endpoint_release_extra_over_support_width=50
transport_reset_pdec_atom_count=0
one_slot_epoch_spare_ratio=0.903889304413
one_slot_epoch_min_spare_ratio=0.690140845070
active_ell_band=23..109
endpoint_gap_count=3
max_known_gap_fill_delay=80
candidate_single_pair_sae_mass_sum=0.001775688144
max_paired_side_pressure_product=0.160177975528
paired_pressure_slack=0.839822024472
moving_residue_shape_count=37
```

## 1. terminal choke set

| choke | absorbs exits | current readout | closed current sweep | global obligation |
| --- | --- | --- | ---: | --- |
| `SourceAndCRTMaterialization` | `SourceMaterializationFailure-PDEC/SAE`, `CRTWindowEmptyGlobalSupportBound`, `WindowEdgeCollisionOrUnusedTargetArrivalBound` | formal_gap=39, source_fail=28, crt_empty=11, unresolved=0, crt_phase_margin=879, edge_candidates=11 | `true` | prove persistent source failures and CRT empty windows are PDEC/SAE-summable, or exclude unused-target residue arrival globally |
| `SupportMotionPrimitiveIdentity` | `SupportMotionNonpersistenceOrEndpointReleaseBound`, `PrimitiveIdentityShiftExclusion`, `MovingSlotFamily-PDEC/ColumnCRT` | support_motion_candidates=11, min_endpoint_release=70, release_extra_over_width=50, min_depth_defect=70, fixed_slot_failures=0, min_crt_minus_phase_width=703 | `true` | prove moving supports cannot preserve both primitive depth identities, or route repeated moving-slot patterns to ColumnCRT/PDEC |
| `TransportSingletonActiveEll` | `TransportResetPDECExclusion`, `SingletonResidueSAE/Rankin`, `ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`, `EndpointMotionGapFillBoundOrGapPDECExclusion` | transport_reset_atoms=0, singleton_rankin_mass=4.328474445644, one_slot_mass=4.291749690880, epoch_used=257/2674, epoch_spare_ratio=0.903889304413, active_band=23..109, endpoint_gap_count=3, max_gap_delay=80 | `true` | prove active ell endpoint growth has a fill bound, or show endpoint motion creates reset-PDEC/SAE before singleton Rankin mass can accumulate |
| `EpochPairPairedPressure` | `GlobalEpochPairMultiplicityBound`, `HighDensityEpochPair-PDEC/ColumnCRT`, `AffineTwinPairedSidePressureBoundOrPressureProductPDECExclusion` | candidate_q=[31, 43, 103], sparse_tail_frontier=0.017241379310, candidate_mass=0.001775688144, max_pressure_product=0.160177975528, pressure_slack=0.839822024472, one_sided_pressure_q=[43, 103] | `true` | prove adjacent twin epochs cannot synchronize both-side residue pressure above one, or exclude PressureProduct-PDEC/ColumnCRT |
| `MovingResidueShapeSAE` | `MovingResidueShapeSAE/Rankin`, `FixedResidueSlotDriftColumnCRT` | moving_residue_shapes=37, recurrent_fixed_residue_packets=12, singleton_packets=300, max_residue_packet_multiplicity=2 | `true` | prove moving residue shapes are SAE/Rankin-summable, or turn recurrent fixed residues into ColumnCRT/PDEC |

## 2. 证明边界

- 本证书把 after-cutset 命名出口收缩为五个终端 choke，并记录每个 choke 的当前显式容量/相位余量。
- 它关闭 current sweep 的匿名复现解释；没有证明全局行/列命题。
- 下一主攻点：`TerminalChokeSetGlobalExclusionOrSummability`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-after-cutset-named-exit-frontier-ledger.json` | `d2001a4ad91fffafd97bc57a462805e37e3d4debe4f03933ac09e7e1c230584d` |
| `data/prime-matrix-formal-to-actual-global-cutset-ledger.json` | `1461801b41d428b52d8307fc42353ff7e4ad7730289e0e7946f309d93f365c4c` |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json` | `f2c69912fe26fc88d0f02df98c514cfa7ba407226b67de20b9b1db98ff8b3b08` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json` | `e6f6e91cf374354bf5834506a580029f1c9518c04f79d4df741d5e11549fac6b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json` | `60a85b991523e1af0bdb40c950945b3db3163d1132d1ff441e8ccbc46ade0ac6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json` | `f2876c431b7c4ff762deb76e26f43d974388fab22a1ee854f64fa39944ce280e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json` | `49723eba352f20363d6be36712caf088dbebab1a89f2ed5707d7c0ce76a228e9` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json` | `18a67505beef2a1ba7ec53a6088bb26da6a3955e2f63c02f5e215cfe171a8063` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json` | `d1e5ac2f12b542edc86559cbbb8b75f862f1ee02df351a024bc302a4af01427b` |
