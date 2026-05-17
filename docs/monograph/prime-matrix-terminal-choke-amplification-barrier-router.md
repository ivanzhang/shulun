# Prime Matrix terminal choke amplification barrier router

**状态：** `terminal_choke_amplification_barriers_current_sweep_closed_global_open`

五个终端 choke 的当前复现门槛可以量化为放大屏障。最窄 raw phase jump 是 CRT 空窗到支撑窗的 2 倍距离，但它不是独立终端，会立即进入 unused-target/window-edge 路由。真正终端侧最窄门槛是 one-slot transport overflow：最拥挤 epoch 为 minus:71，已用 22/71，还需 50 个新增 residue 才能越界；support motion 的最小端点释放额外量也正好是 50。因此最新显式交叉点是 fifty-unit cross-lock：反例链若继续复现，必须支付同一个 50-unit release/residue 包，或进入 reset/PDEC/SAE。

```text
barrier_count=5
terminal_chokes_closed_current_sweep=true
row_column_unconditional_closed=false
narrowest_barrier=CRTWindowPhaseJump
narrowest_barrier_factor=2.000000000000
narrowest_terminal_barrier=OneSlotTransportOverflow
narrowest_terminal_factor=3.227272727273
tight_epoch_key=minus:71
tight_epoch_used=22
tight_epoch_capacity=71
tight_epoch_unused=49
tight_epoch_overflow_new_units=50
support_endpoint_release_extra_units=50
fifty_unit_cross_lock=true
support_release_factor=3.500000000000
crt_window_phase_jump_factor=2.000000000000
moving_slot_crt_factor=7.028846153846
pressure_amplification_to_failure=6.243055555556
fill_total_min_rankin_mass_if_all_cross=0.169986671425
transport_reset_pdec_atom_count=0
```

## 1. 放大屏障表

| barrier | terminal choke | factor | additive units | current readout | route if persistent |
| --- | --- | ---: | ---: | --- | --- |
| `CRTWindowPhaseJump` | `SourceAndCRTMaterialization` | 2.000000000000 | 40 | min_empty_window_distance=40, support_width=20, modulus_factor=44.950000, edge_candidates=11 | `UnusedTargetArrival or WindowEdgeCollision-PDEC/SAE` |
| `OneSlotTransportOverflow` | `TransportSingletonActiveEll` | 3.227272727273 | 50 | tight_epoch=minus:71, used=22, capacity=71, unused=49, transport_reset_atoms=0 | `TransportReset-PDEC or SingletonResidueSAE/Rankin` |
| `SupportEndpointRelease` | `SupportMotionPrimitiveIdentity` | 3.500000000000 | 50 | min_endpoint_release=70, support_width=20, min_depth_defect=70, breaks_both_identities=true | `PrimitiveIdentityShift-PDEC/SAE or MovingSlot-ColumnCRT` |
| `EpochPairPairedPressure` | `EpochPairPairedPressure` | 6.243055555556 | 1 | max_pressure_product=0.160177975528, pressure_slack=0.839822024472, fill_extra_range=1..8, min_fill_spare=0.870967741935 | `PressureProduct-PDEC/ColumnCRT or FillCatchUpMass-PDEC` |
| `FixedMovingSlotCRT` | `SupportMotionPrimitiveIdentity` | 7.028846153846 | 703 | min_highfactor_crt_modulus=731, max_phase_width=104, fixed_pattern_failures=0 | `MovingSlotFamily-PDEC/ColumnCRT` |

## 2. 排序

```text
CRTWindowPhaseJump -> OneSlotTransportOverflow -> SupportEndpointRelease -> EpochPairPairedPressure -> FixedMovingSlotCRT
```

## 3. 证明边界

- 本证书只量化 terminal choke 的当前放大门槛，不证明全局行/列命题。
- 最窄终端接口是 one-slot transport overflow；它与 support endpoint release 共享 50-unit 门槛。
- 下一主攻点：`FiftyUnitCrossLockOrTerminalPDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-global-named-exit-terminal-choke-ledger.json` | `ff9f195f64e41baa0bc44c94bc7e201b5c4eeec0851b8b4a40a8a6023a3ec328` |
| `data/prime-matrix-formal-to-actual-global-cutset-ledger.json` | `1461801b41d428b52d8307fc42353ff7e4ad7730289e0e7946f309d93f365c4c` |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json` | `f2c69912fe26fc88d0f02df98c514cfa7ba407226b67de20b9b1db98ff8b3b08` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json` | `fa2485f12eee15af77f301d61a720a4d349ce27c4d9b82e3640f58700c143c03` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json` | `e6f6e91cf374354bf5834506a580029f1c9518c04f79d4df741d5e11549fac6b` |
