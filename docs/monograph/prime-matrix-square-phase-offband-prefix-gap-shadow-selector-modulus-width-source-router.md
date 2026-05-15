# Prime Matrix square-phase off-band prefix gap shadow selector modulus-width source router

**状态：** `selector_modulus_width_source_split_open_global`

本步把一跳模数屏障 M>W 的来源拆成两个可攻输入：cover-word 标签乘积/CRT 模数下界，以及 fixed small-k phase 窗口宽度上界。当前前沿按标签词长度分为 4 类，全部满足 min(M)>max(W)，最小长度类余量为 45。这不是全局证明；全局剩余是证明同一 formal-unit 族的标签下界与宽度 envelope，或将 M<=W 的小模数重叠登记为 PDEC/ColumnCRT。

```text
barrier_atom_count=49
length_class_count=4
family_class_count=8
length_class_dominance_failure_count=0
min_length_class_margin=45
row_column_unconditional_closed=false
```

## 1. 长度类屏障

| L | atoms | min M | max W | minM-maxW | min atom M-W | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 4 | 77 | 32 | 45 | 45 | `true` |
| 3 | 26 | 231 | 117 | 114 | 114 | `true` |
| 4 | 17 | 231 | 172 | 59 | 159 | `true` |
| 5 | 2 | 7293 | 100 | 7193 | 7193 | `true` |

## 2. Family 屏障

| family | atoms | min M | max W | min M-W | min M/W | closed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `minus\|plus_only_noslot:k1:649-653\|L=3` | 22 | 231 | 117 | 114 | 1.974359 | `true` |
| `minus\|plus_only_noslot:k2:619-623\|L=3` | 4 | 273 | 28 | 245 | 9.750000 | `true` |
| `plus\|minus_only_noslot:k0:493-499\|L=4` | 1 | 4389 | 96 | 4293 | 45.718750 | `true` |
| `plus\|minus_only_noslot:k0:649-655\|L=4` | 1 | 7293 | 172 | 7121 | 42.401163 | `true` |
| `plus\|minus_only_noslot:k0:697-705\|L=5` | 2 | 7293 | 100 | 7193 | 72.930000 | `true` |
| `plus\|minus_only_noslot:k1:1065-1071\|L=4` | 9 | 231 | 72 | 159 | 3.208333 | `true` |
| `plus\|minus_only_noslot:k1:281-283\|L=2` | 4 | 77 | 32 | 45 | 2.406250 | `true` |
| `plus\|minus_only_noslot:k1:681-687\|L=4` | 6 | 561 | 8 | 553 | 70.125000 | `true` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_length_class_modulus_width_dominance` | `closed_on_current_frontier` | For each observed label-word length, the minimum word modulus exceeds the maximum phase width. |
| `modulus_width_source_split` | `closed` | The M>W barrier splits into a label lower bound and a fixed phase-width envelope. |
| `global_label_lower_bound` | `open` | A global proof must lower-bound non-structural cover-word moduli by length/family. |
| `global_phase_width_envelope` | `open` | A global proof must upper-bound fixed small-k phase window widths by the same length/family classes. |
| `small_modulus_overlap_pdec` | `open` | If either bound fails, the remaining object is a concrete small-modulus overlap PDEC/ColumnCRT certificate. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteLengthClassDominanceClosed` | `true` | `true` | 当前每个长度类都满足 min(M)>max(W)。 | closed on current finite frontier |
| `SourceSplitClosed` | `true` | `true` | M>W 已拆为标签乘积下界与 phase 宽度上界两个输入。 | closed |
| `GlobalLabelLowerBoundProved` | `false` | `false` | 尚未证明 formal-unit 族中的非结构冲突词模数下界。 | LengthClassLabelLowerBoundAndPhaseWidthEnvelopeOrSmallModulusPDEC |
| `GlobalPhaseWidthEnvelopeProved` | `false` | `false` | 尚未证明 formal-unit 族中的 fixed phase 宽度上界。 | LengthClassLabelLowerBoundAndPhaseWidthEnvelopeOrSmallModulusPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步继续压缩证明义务，不关闭全局行/列命题。 | LengthClassLabelLowerBoundAndPhaseWidthEnvelopeOrSmallModulusPDEC |

## 5. 下一步

- 主攻：`LengthClassLabelLowerBoundAndPhaseWidthEnvelopeOrSmallModulusPDEC`。
- 直接证明目标 A：非结构冲突 cover words 的标签乘积给出长度/族下界。
- 直接证明目标 B：fixed small-k phase 窗口宽度受同一长度/族 envelope 控制。
- 若 A 或 B 失败，则失败对象就是 small-modulus overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router.py` | `69d98f70c0d1d4ceafebe32d35541a0f306d41c4a3ef0c34d76d5c66162b9b38` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router.py` | `1ca7e61999663032eecab0d856aa1543020323ba27d2910fbf06afc8a35e4eb9` |
| `data/square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json` | `f28ab6070f5e6e8b1f6bce16c9855098fd6a95e4b24b79c5b1716d4223626fc1` |
| `data/square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json` | `9b74bc89311d215f67e9cd6a8c9c731cbeff3a114533eca56e8140929afcd161` |
