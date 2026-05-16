# Prime Matrix AffineTwin endpoint-release persistent-family promotion audit

**状态：** `current_sweep_persistent_family_promotion_routed_global_open`

本审计把 `GeneratorCoarrivalFamilyBound` 的推广义务继续拆开：固定支撑图像、固定 q/残基复现、moving epoch-pair SAE、source/pressure/fill 门控分别进入独立账本。当前 sweep 中这些门都已路由，但全局 multiplicity 与 slot-drift 排斥仍开放。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
candidate_product_mass_upper_sum=0.023577117628562343
eta=0.025
candidate_total_eta_slack=0.0014228823714376587
high_density_epoch_pair_count=0
fixed_slot_recurrence_count=0
fixed_residue_slot_drift_pair_count=12
source_gate_blocked_formal_pairs=28
persistent_family_promotion_closed_current_sweep=true
```

## 1. promotion route rows

| gate | closed | evidence | global remaining |
| --- | --- | --- | --- |
| `FixedSupportGraphSchema` | true | fixed graph W=(q+9)/2 stays below sqrt(q(q-2)); formal SuperSqrt subsets=22, actual overload subsets=0 | `PromoteFixedGraphProjectionSchemaToAllPersistentAffineTwinFamilies` |
| `FixedQFixedResidueColumnCRT` | true | fixed_slot_recurrence_count=0; fixed_residue_slot_drift_pair_count=12; all drift gaps divisible by ell=True | `FixedResidueSlotDriftColumnCRT` |
| `MovingEpochPairSparseSAE` | true | candidate_product_mass_upper_sum=0.023577117628562343; eta=0.025; high_density_epoch_pair_count=0 | `GlobalEpochPairMultiplicityBound or HighDensityEpochPair-PDEC` |
| `PairedPressureGate` | true | max_paired_side_pressure_product={'numerator': 144, 'denominator': 899, 'decimal': 0.16017797552836485}; one_sided_pressure_q_values=[43, 103] | `PressureProduct-PDEC` |
| `FillArrivalOrReset` | true | all routes require fill increment=True; total min extra fill=11; total min new fill Rankin mass={'numerator': 23339, 'denominator': 137299, 'decimal': 0.16998667142513785} | `FillCatchupMassPDEC or Reset/ColumnCRT-PDEC` |
| `SourceMaterialization` | true | pass q=[31]; fail q=[43, 103]; blocked formal pairs=28 | `SourceRematerialization-PDEC/SAE` |

## 2. candidate epoch pairs

| q | used upper | capacity | occupancy upper | realized | single SAE mass |
| ---: | ---: | ---: | ---: | --- | ---: |
| 31 | 12 | 899 | 0.0133481646274 | true | 0.00111234705228 |
| 43 | 16 | 1763 | 0.00907543959161 | false | 0.000567214974475 |
| 103 | 12 | 10403 | 0.00115351340959 | false | 9.61261174661e-05 |

## 3. 显式矛盾读数

- 反例链若停在固定图像内，已由 family schema 的 `W<=sqrt(q(q-2))` 阻断。
- 若固定 q/残基反复复现，则不再是匿名容量，而是固定模 ColumnCRT/PDEC；当前 fixed-slot 复现数为 `0`。
- 若 q 或残基移动，则进入 epoch-pair SAE；当前候选总 occupancy 上界 `0.023577...` 低于 `eta=0.025`，高密度行数为 `0`。
- 余下真正全局硬点是证明该稀疏/漂移结构不能无限持久，或把持久失败转成 ColumnCRT/PDEC/SAE 证书。

## 4. 结论边界

当前 sweep 的 persistent-family promotion 已完成路由闭合；这仍不是行/列命题无条件证明。最新剩余被压成 `GlobalEpochPairMultiplicityBound` 与 `FixedResidueSlotDriftColumnCRT`，并保留 `MovingResidueShapeSAE/Rankin` 与 source-rematerialization 出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-ledger.json` | `ac184d081f03f73b275567c62a5b2354974fd984b3885af3cb9963471368af3d` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json` | `8323447f703d339a1ff63e35f0dcaff4d697b295ea79241f67c23d2ecd5c00d3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json` | `fa2485f12eee15af77f301d61a720a4d349ce27c4d9b82e3640f58700c143c03` |
| `data/prime-matrix-affine-twin-source-materialization-gate-ledger.json` | `aaaee80eaba6130fa016758509513449beff23eaefa41fcc79a174e183c5e385` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json` | `bde88833f32da0c028cd0ed8d8a55701e2b0289d20485eac5ced6bd5befb197b` |
