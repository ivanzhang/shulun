# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin moving family SAE/ColumnCRT router

**状态：** `affine_twin_moving_family_routed_to_epoch_sae_or_columncrt_open`

本步把 AffineTwin moving family 分成两个正式出口：固定 `q` 与固定双残基若复现，就带固定模 `q(q-2)`，进入 ColumnCRT/PDEC；若 `q` 或残基移动，则进入 twin epoch-pair SAE/Rankin 质量账本。当前活跃 epoch 中满足 `q,q-2` 同为素数且 `q≡3 mod 4` 的候选 q 为 [31, 43, 103]；其中实际 AffineTwin 只实现 q=[31]。当前已实现 SAE 质量为 0.001112347052，但全局仍需证明 epoch-pair 乘法占用的 multiplicity 界，或排斥对应 ColumnCRT/PDEC。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
candidate_affine_twin_epoch_pair_count=3
realized_affine_twin_pair_count=1
candidate_epoch_pair_product_mass_upper_sum=0.023577117629
candidate_single_pair_sae_mass_sum=0.001775688144
realized_affine_twin_sae_mass_sum=0.001112347052
fixed_slot_recurrence_count=0
fixed_residue_slot_drift_pair_count=12
row_column_unconditional_closed=false
```

## 1. 候选 twin epoch-pair

| q | epochs | used upper | capacity | occupancy upper | single SAE mass | fixed margin | realized |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | `minus:29 -> plus:31` | 12 | 899 | 0.013348 | 0.001112347 | 879 | `true` |
| 43 | `minus:41 -> plus:43` | 16 | 1763 | 0.009075 | 0.000567215 | 1737 | `false` |
| 103 | `minus:101 -> plus:103` | 12 | 10403 | 0.001154 | 0.000096126 | 10347 | `false` |

## 2. 分流结论

- 固定 `q` 与固定双残基的复现不再是自由移动槽，而是固定模 `q(q-2)` 的 ColumnCRT/PDEC。
- 非复现原子进入 SAE；单个 AffineTwin 双槽原子的自然质量是 `1/(q(q-2))`。
- 当前候选 `q` 的 epoch-pair 账本已经物化；实际只实现 `q=31`。
- 全局仍需 multiplicity 界：证明 moving `q` 的 epoch-pair 占用可求和，或排斥固定/移动 ColumnCRT-PDEC。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `affine_twin_fixed_pair_columncrt_split` | `closed_routing` | If q and the two CRT residues are fixed and the same affine-twin pair recurs, recurrence has fixed modulus q(q-2) and is a ColumnCRT/PDEC object; if it does not recur, it is an isolated SAE atom. |
| `active_twin_epoch_pair_ledger_materialized` | `closed_current_sweep` | The current active epoch ledger lists every q with q and q-2 active, twin-prime, and q=3 mod 4, together with its epoch-pair capacity and realized affine-twin mass. |
| `affine_twin_epoch_pair_multiplicity_bound` | `open` | A global proof must bound multiplicity inside the moving q epoch-pair ledger, or prove the resulting fixed/moving ColumnCRT-PDEC exclusions. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedQFixedResiduePairRoutedToColumnCRT` | `true` | `true` | 固定 q 与固定双残基若复现，必带固定模 q(q-2)，进入 ColumnCRT/PDEC。 | closed routing, exclusion still separate |
| `CurrentActiveTwinEpochLedgerMaterialized` | `true` | `false` | 当前扫描的活跃 twin epoch-pair 已物化为容量/质量账本。 | finite evidence only |
| `CurrentRealizedAffineTwinPairSparse` | `true` | `false` | 当前已实现 AffineTwin 只占候选 epoch-pair 容量的极小部分。 | finite evidence only |
| `GlobalEpochPairMultiplicityBoundProved` | `false` | `false` | 仍需全局证明 moving q epoch-pair 的乘法占用可求和，或转入 ColumnCRT/PDEC 排斥。 | AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 moving family 的 SAE/ColumnCRT 分流，不关闭全局行/列命题。 | AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion`。
- 具体目标：证明 twin epoch-pair 的乘法占用不能达到反例链所需密度；若失败，则输出固定模或移动模 ColumnCRT/PDEC 证书。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_moving_family_sae_columncrt_router.py` | `69d7c0955f6cf9565cf83d9f652502ab842fbdce9f13563ec740b691c8e0f3b7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json` | `2f86d0b8f43e35626243749be133068f651966d90c31896795c984d5801d0991` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
