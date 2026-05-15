# Prime Matrix square-phase off-band prefix gap shadow selector lowwheel router

**状态：** `selector_lowwheel15_finite_separator_open`

本步在 selector 侧找到当前前沿的最小共同低模分离器：Q=15。所有登记 BadPSet 包中，actual P 的 mod 15 残基均不落入坏集的 mod 15 支撑；而 2、3、5、6、10 都不能统一分离，说明有效刚性来自 3*5 低轮联动相位，不是奇偶、单素模、端点或素性本身。该结论只闭合当前有限前沿；全局仍需把Q=15 分离提升为 formal-unit selector 定理，或对持久重叠提交 PDEC/ColumnCRT 证书。

```text
record_count=11
actual_p_in_bad_set_count=0
q15_separator_packet_count=11
first_global_separator_modulus_le_300=15
actual_inside_bad_value_hull_count=7
row_column_unconditional_closed=false
```

## 1. 低轮分离结论

当前 11 个 BadPSet schema 上，`Q=15` 是 `<=300` 搜索范围内第一个共同分离模数：

| modulus | separates all packets |
| ---: | ---: |
| `2` | `false` |
| `3` | `false` |
| `5` | `false` |
| `6` | `false` |
| `10` | `false` |
| `15` | `true` |
| `30` | `true` |
| `210` | `true` |
| `2310` | `true` |

这说明本层真正可攻的 selector 结构是 `3*5` 联动相位；单独的奇偶、`mod 3`、`mod 5` 或 `mod 10` 都不足以解释 actual `P` 避开坏集。

## 2. 前沿记录

| idx | P | side | width | actual off | P mod 15 | BadPSet mod 15 | min sep | nearest bad | inside bad hull |
| ---: | ---: | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| 0 | 733 | `plus` | 8 | 4 | 13 | `[10, 12]` | 2 | 1 | `false` |
| 1 | 523 | `plus` | 96 | 42 | 13 | `[1, 4, 8]` | 7 | 18 | `true` |
| 2 | 691 | `minus` | 117 | 47 | 1 | `[0, 2, 3, 4, 5, 7, 10, 11, 13]` | 10 | 3 | `true` |
| 3 | 683 | `plus` | 172 | 70 | 8 | `[1, 5, 7, 10, 12, 13, 14]` | 6 | 7 | `true` |
| 4 | 733 | `plus` | 100 | 48 | 13 | `[7]` | 2 | 21 | `true` |
| 5 | 673 | `minus` | 28 | 25 | 13 | `[2, 7]` | 2 | 11 | `false` |
| 6 | 733 | `plus` | 8 | 4 | 13 | `[10, 12]` | 2 | 1 | `false` |
| 7 | 313 | `plus` | 32 | 24 | 13 | `[2, 4, 5, 11]` | 5 | 4 | `true` |
| 8 | 1129 | `plus` | 72 | 40 | 4 | `[1, 3, 7, 8, 10, 14]` | 9 | 3 | `true` |
| 9 | 691 | `minus` | 117 | 47 | 1 | `[0, 2, 3, 4, 5, 7, 10, 11, 13]` | 10 | 3 | `true` |
| 10 | 673 | `minus` | 28 | 25 | 13 | `[2, 7]` | 2 | 11 | `false` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_selector_lowwheel15_separator` | `closed_on_current_frontier` | On every registered BadPSet packet, actual P is separated from BadPSet by residue modulo 15. |
| `single_prime_or_parity_separator` | `rejected` | Modulo 2, 3, 5, 6, and 10 do not separate all packets; the first uniform separator is the coupled 3*5 wheel. |
| `endpoint_or_offset_hull_separator` | `rejected` | Several actual P values lie inside the BadPSet value hull, so endpoint or interval-hull location is not the invariant. |
| `global_formal_unit_lowwheel15_lift` | `open` | A global proof must derive the modulo-15 separation from the formal-unit selector formulas, or route persistent overlaps to PDEC. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteQ15SelectorCertificate` | `true` | `true` | 当前 11 个 BadPSet schema 均由 Q=15 分离 actual P 与坏集。 | closed on current finite frontier |
| `LowerModulusLocalInvariantsSuffice` | `true` | `true` | 2,3,5,6,10 均非共同分离器，单素模/奇偶路线不能闭合。 | closed as rejected |
| `GlobalQ15FormalUnitLiftProved` | `false` | `false` | 尚未证明任意 formal unit 的 actual selector 总避开 BadPSet 的 mod 15 支撑。 | FormalUnitSelectorLowWheel15LiftOrPersistentHitPDEC |
| `PersistentHitPDECExcluded` | `false` | `false` | 若存在 Q=15 重叠的持久族，仍需提交 PDEC/ColumnCRT 证书排斥。 | FormalUnitSelectorLowWheel15LiftOrPersistentHitPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 selector 侧缩窄到低轮 15 提升或 PDEC，不关闭全局行/列命题。 | FormalUnitSelectorLowWheel15LiftOrPersistentHitPDEC |

## 5. 下一步

- 主攻：`FormalUnitSelectorLowWheel15LiftOrPersistentHitPDEC`。
- 直接证明目标：从 fixed band/k 与 BadPSet 覆盖词公式中符号推出 actual `P mod 15` 不在坏残基支撑内。
- 若出现 `mod 15` 重叠族，则不再转题，直接登记为 persistent-hit `PDEC/ColumnCRT` 证书对象。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router.py` | `3b59bdbcedb0ba8195e162437885629c6bb4491edd11e3793ba93bb17723b5ae` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router.py` | `9b43e6ceca2e9f272b6411bc89c08d1b4166b4eb12e471adcc5b563e9bd27f4c` |
| `data/square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json` | `4b952c155cc1f1b1824a7acf19f75cc1e19fe49c2172cd92e5e371261c0a1f5b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json` | `a9aebcbecddfdeed41fc3a33decc08ef206e6161c7e6aa7f2b30c540c8d896d0` |
