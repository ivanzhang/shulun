# Prime Matrix after-cutset named-exit frontier router

**状态：** `after_cutset_named_exit_frontier_current_sweep_closed_global_open`

cutset 完备后，当前 sweep 不再存在匿名容量缺口：40 个形式配对中 1 个成为 actual packet，28 个进入 source failure，11 个进入 CRT 空窗；空窗后的 11 个边缘候选又被分流到 window-edge、support-motion、primitive-identity 与 moving-slot/transport/epoch/residue 出口。本证书关闭的是 current-sweep after-cutset 前沿；全局行/列命题仍需证明这些命名出口的无条件排斥或可求和吸收。

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
source_unmaterialized_pair_total_current=28
crt_window_empty_pair_total_current=11
unresolved_formal_pair_total_current=0
edge_collision_candidate_count_current=11
support_motion_candidate_count=11
min_endpoint_release_total_required=70
min_endpoint_release_over_support_width=3.500000
min_total_affine_depth_defect=70
fixed_highfactor_slot_pattern_isolation_failure_count_at_p0=0
min_crt_minus_phase_width_at_p0=703
transport_reset_pdec_atom_count=0
candidate_product_mass_upper_sum=0.023577117629
eta=0.025
high_density_epoch_pair_count=0
moving_residue_shape_count=37
singleton_residue_packet_count=300
current_sweep_frontier_closed=true
row_column_unconditional_closed=false
```

## 1. after-cutset 命名出口表

| exit family | current readout | current route | global remaining |
| --- | --- | --- | --- |
| `SourceMaterializationFailure` | source_unmaterialized=28 inside formal_to_actual_gap=39 | already separated by cutset completeness | `SameGapWrongSource-PDEC/SAE or NoGapSource-PDEC/SAE exclusion/summability` |
| `CRTWindowEmpty` | empty_pairs=11, modulus=899, support_width=20, min_empty_distance=40 | phase window empty, not hidden actual load | `CRTWindowEmptyGlobalSupportBound` |
| `WindowEdgeCollision/UnusedTargetArrival` | candidates=11, existing_actual_needed=2, unused_target_needed=9, l1_displacement=1..11 | all current empty windows have positive residue displacement | `global edge-collision bound or unused-target arrival bound` |
| `SupportMotionEndpointRelease` | candidates=11, support_width=20, min_endpoint_release=70, release_over_width=3.500000 | every support motion requires both endpoint releases | `SupportMotionNonpersistence or endpoint-release summability` |
| `PrimitiveIdentityShift` | min_total_depth_defect=70, breaks_both_depth_identities=true, fixed_q_absorbs=false | fixed primitive key cannot absorb current support motion | `PrimitiveIdentityShiftExclusion or PDEC/SAE registration` |
| `MovingSlotFamily` | fixed_pattern_failures=0, equality_atom_isolated=true, min_crt_minus_phase_width=703, max_phase_width=104 | fixed highfactor slot patterns isolated by CRT modulus > phase width | `exclude moving highfactor slot families or route to MovingSlot-PDEC/ColumnCRT` |
| `TransportReset` | transport_cells=12, unique_keys=12, repeated_keys=0, reset_atoms=0 | current transport reset atom set is empty | `TransportResetPDECExclusion and transport SAE/Rankin bound` |
| `EpochPairMultiplicity` | candidate_q=[31, 43, 103], mass_upper_sum=0.023577117629, eta=0.025, high_density_count=0 | current candidate mass is below eta sparse gate | `GlobalEpochPairMultiplicityBound or HighDensityEpochPair-PDEC/ColumnCRT exclusion` |
| `MovingResidue/SingletonSAE` | physical_records=324, singleton_packets=300, recurrent_fixed_residue_packets=12, moving_residue_shapes=37 | identity split has no current representative failure | `MovingResidueShapeSAE/Rankin and SingletonResidueSAE/Rankin` |

## 2. 当前闭合标志

| flag | value |
| --- | ---: |
| `cutset_partition_current_sweep` | `true` |
| `window_edge_displacement_current_sweep` | `true` |
| `support_motion_depth_current_sweep` | `true` |
| `fixed_primitive_absorption_current_sweep` | `true` |
| `fixed_highfactor_slot_isolation_current_sweep` | `true` |
| `epoch_pair_sparse_gate_current_sweep` | `true` |
| `transport_reset_atoms_empty_current_sweep` | `true` |
| `unique_representative_identity_current_sweep` | `true` |

## 3. 全局剩余接口

- `source_materialization_global` -> `SourceMaterializationFailure-PDEC/SAE`
- `crt_window_global` -> `CRTWindowEmptyGlobalSupportBound`
- `window_edge_global` -> `WindowEdgeCollisionOrUnusedTargetArrivalBound`
- `support_motion_global` -> `SupportMotionNonpersistenceOrEndpointReleaseBound`
- `primitive_identity_shift_global` -> `PrimitiveIdentityShiftExclusion`
- `moving_slot_family_global` -> `MovingSlotFamily-PDEC/ColumnCRT`
- `transport_reset_global` -> `TransportResetPDECExclusion`
- `epoch_pair_global` -> `GlobalEpochPairMultiplicityBound`
- `moving_residue_global` -> `MovingResidueShapeSAE/Rankin`
- `singleton_residue_global` -> `SingletonResidueSAE/Rankin`

## 4. 证明边界

- 该证书把 cutset 完备分割后的剩余全部压入命名出口前沿。
- 它证明 current sweep 的匿名容量/相位逃逸已关闭；没有证明全局行/列命题。
- 下一主攻点：`GlobalNamedExitExclusionOrSummability`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-formal-to-actual-global-cutset-ledger.json` | `1461801b41d428b52d8307fc42353ff7e4ad7730289e0e7946f309d93f365c4c` |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json` | `f2c69912fe26fc88d0f02df98c514cfa7ba407226b67de20b9b1db98ff8b3b08` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json` | `8323447f703d339a1ff63e35f0dcaff4d697b295ea79241f67c23d2ecd5c00d3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json` | `d1e5ac2f12b542edc86559cbbb8b75f862f1ee02df351a024bc302a4af01427b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json` | `e6f6e91cf374354bf5834506a580029f1c9518c04f79d4df741d5e11549fac6b` |
