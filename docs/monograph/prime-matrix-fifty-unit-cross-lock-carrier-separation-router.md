# Prime Matrix fifty-unit cross-lock carrier separation router

**状态：** `fifty_unit_cross_lock_carrier_separated_crosscarrier_sync_open`

50-unit cross-lock 不是同一载体上的直接矛盾：support 原子在 q=31/source_pair=19:12 和 P≈2687 的 below 端点释放上，而最拥挤一槽 epoch 是 minus:71 且 P 区间为 4177..9257。二者要同步必须穿过互素模数 31*71=2201 的跨载体 CRT 门。固定 p_delay=80 在模 71 上为 9，前 50 步互异且可放入当前 71-epoch P 区间；所以短路的重复 residue 矛盾不会自动出现。若这 50 个到达都作为新 residue 同步进入 minus:71，则 22+50>71，立即越过 one-slot 容量；若不是新 residue 或不能同步，就分别回到 TransportReset-PDEC、SingletonResidue-SAE、SupportMotion/UnusedTarget 或 MovingCarrier-ColumnCRT 出口。

```text
row_column_unconditional_closed=false
support_atom_key=19:12
support_q=31
support_generator_residue=19
support_fill_residue=12
support_generator_p=2687
support_endpoint_release_extra_units=50
tight_epoch_key=minus:71
tight_epoch_used=22
tight_epoch_capacity=71
tight_epoch_overflow_new_units=50
same_q_or_ell=false
same_side_taxonomy=false
same_p_band=false
direct_same_carrier_contradiction=false
cross_carrier_sync_required=true
combined_carrier_modulus=2201
combined_modulus_over_fifty_units=44.020000000000
p_delay_mod_tight_epoch=9
p_delay_gcd_tight_epoch=1
fifty_distinct_residue_count=50
fifty_step_ramp_is_reset_free=true
first_enter_epoch_p=4207
last_fifty_block_p=8127
fifty_step_block_can_fit_current_epoch_p_range=true
if_fifty_new_residues_sync_then_one_slot_overflow=true
newness_against_existing_epoch_residues_proved=false
next_direct_attack_target=CrossCarrierFiftyUnitSynchronizationPDECOrSAE
```

## 1. 分流门

| gate | closed current sweep | readout | remaining if fails |
| --- | --- | --- | --- |
| `SameCarrierDirectContradiction` | `true` | support q=31, epoch ell=71, support_p_band=(2629, 2687), epoch_p_range=(4177, 9257) | `DirectSameCarrierCRTContradiction` |
| `FixedDelayResetFreeBeforeFifty` | `true` | p_delay=80, p_delay mod 71=9, gcd=1, distinct_first_50=50 | `TransportResetPDECOrMovingCarrierColumnCRT` |
| `FiftyBlockRangeAdmission` | `true` | first_enter_epoch_p=4207, last_fifty_block_p=8127, epoch_p_range=(4177, 9257) | `SupportMotionRangeSlipOrUnusedTargetArrivalSAE` |
| `FiftyNewResidueOverflowIfSynchronized` | `true` | used=22, new_units=50, capacity=71 | `OneSlotCapacityNoOverflow` |
| `NewnessAgainstExistingEpochResidues` | `false` | capacity ledger records used count and sample, but not a full existing-residue set; global proof must show the 50 arrivals are new or route duplicates to reset/PDEC | `TransportResetPDECOrSingletonResidueSAE` |

## 2. 证明边界

- 本证书关闭的是同载体直接矛盾路线；它没有证明行/列命题。
- 固定 `p_delay=80` 在 `mod 71` 上前 50 步互异，因此重复 residue 的短路 PDEC 不能免费使用。
- 真正剩余是证明这 50 个跨载体到达若持久同步则必须为新 residue 并越界，或把非新/不同步形态登记为 PDEC/SAE/ColumnCRT。
- 下一主攻点：`CrossCarrierFiftyUnitSynchronizationPDECOrSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-terminal-choke-amplification-barrier-ledger.json` | `0fb990e267c7b8c10f6730f8d1bb823e37243384d59539a7f2468ba9455a385d` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json` | `2f86d0b8f43e35626243749be133068f651966d90c31896795c984d5801d0991` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json` | `2b7ba1295e2d498da7265aa73d7e39b6a5add3a31ae60f947b4fbc4cf212b373` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json` | `fa2485f12eee15af77f301d61a720a4d349ce27c4d9b82e3640f58700c143c03` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json` | `e6f6e91cf374354bf5834506a580029f1c9518c04f79d4df741d5e11549fac6b` |
