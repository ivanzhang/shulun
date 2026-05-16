# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin slot phase lock router

**状态：** `affine_twin_fixed_slot_pair_isolated_moving_family_open`

本步把 AffineTwin 门继续接入 slot-depth/CRT 相位锁：生成槽给出 `P≡a_g (mod q-2)`，修补槽在平移 `p_delay` 后给出 `P≡a_f-p_delay (mod q)`。两模互素，合成模数为 `q(q-2)`；primitive 深度身份把共同相位支撑压成 `(q+9)/2`。当前 `q=31` 时 `29*31=899 > 20`，唯一代表为 `P=2687`，并恢复 `P+80=2767`。因此固定 AffineTwin 双槽原子已孤立；全局剩余是排斥 q/槽随 P 移动的族，或将其作为 SAE/ColumnCRT/PDEC 终端证书处理。

```text
affine_twin_slot_phase_lock_row_count=1
all_generator_fill_slots_are_twin_moduli=true
all_pair_delay_affine_identities_closed=true
all_pair_phase_width_affine_identities_closed=true
all_combined_moduli_exceed_pair_support_width=true
all_current_affine_twin_slot_pairs_isolated=true
min_combined_modulus_minus_pair_support_width=879
moving_affine_twin_family_excluded=false
row_column_unconditional_closed=false
```

## 1. 双槽相位锁

| q | slots | p delay | pair support | CRT conditions | CRT modulus | margin | representative | isolated |
| ---: | --- | ---: | --- | --- | ---: | ---: | --- | ---: |
| 31 | `242:53:29 -> 229:46:31` | 80 | `[2669, 2688]` | `P=19 mod 29; P=21 mod 31` | 899 | 879 | `[2687]` | `true` |

## 2. 闭合身份

- `generator_modulus=q-2` 且 `fill_modulus=q`。
- `p_delay=(11q-21)/4`。
- `generator_left=(q+5)/2`、`generator_right=(q-7)/4`、`fill_left=q-3`、`fill_right=1`。
- 双槽共同支撑宽度为 `(q+9)/2`。
- 合成 CRT 模数为 `q(q-2)`，因此固定双槽图样满足 `q(q-2)>(q+9)/2`。

## 3. 结构判断

- 这一步不是证明或调用全局孪生素数命题；`q,q-2` 只是当前失败原子的必要门。
- 当前固定 AffineTwin 双槽原子已由 CRT 模数超过相位支撑宽度而孤立。
- 若反例链要持久复现，必须让 `q` 和槽图样一起移动；这已经是更窄的 `AffineTwinMovingFamily` 终端。
- 当前仍未证明全局行/列无条件闭合。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `affine_twin_slot_pair_phase_lock` | `closed_current_atom` | In the current AffineTwin atom, generator and fill slots give coprime CRT conditions modulo q-2 and q; after shifting by the affine p-delay, their product modulus exceeds the common phase support. |
| `fixed_affine_twin_slot_pair_isolation` | `closed` | For a fixed affine-twin slot pair satisfying the recorded primitive depth identities, q(q-2)>(q+9)/2 isolates at most one generator P in the pair support. |
| `moving_affine_twin_family_exclusion` | `open` | A global proof must still exclude recurrence where q and the slot pair move with P, or route that family to SAE/ColumnCRT/PDEC. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `AffineTwinSlotPhaseLockClosedCurrentAtom` | `true` | `true` | 当前 AffineTwin 原子已由双槽 CRT/相位支撑判据孤立。 | closed for fixed atom |
| `FixedAffineTwinSlotPairIsolationCriterionClosed` | `true` | `true` | `q(q-2)>(q+9)/2` 给出固定仿射双槽图样唯一代表判据。 | closed |
| `MovingAffineTwinFamilyExcluded` | `false` | `false` | q 与槽图样随 P 移动的族尚未全局排斥。 | AffineTwinMovingFamilySAEOrColumnCRTExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭固定双槽原子，不关闭全局行/列命题。 | AffineTwinMovingFamilySAEOrColumnCRTExclusion |

## 6. 下一步

- 主攻：`AffineTwinMovingFamilySAEOrColumnCRTExclusion`。
- 具体目标：把移动 `q`/移动槽族分流为可求和 SAE 或固定/移动模 ColumnCRT-PDEC，并证明其不能承载反例链。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_slot_phase_lock_router.py` | `eaa0c9fd03c10abc1e7a61828ce45156f1bd337114a45a38928d9d173357988a` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json` | `223a7643a7779a06880ff1790997d2bfd3b4416f62ca6a65e35c57c8fac3b94c` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json` | `c4a2bfa9e30b4444723f339d4501c3ea14b97fc62954ac659095bacc80c2d5f1` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
