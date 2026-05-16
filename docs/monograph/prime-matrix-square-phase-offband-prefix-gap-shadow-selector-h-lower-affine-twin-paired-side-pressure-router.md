# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin paired side pressure router

**状态：** `affine_twin_sqrt_gate_rewritten_as_paired_side_pressure_product_global_open`

本步把平方根乘积门进一步内化为两侧 residue 压力乘积：令 `g=q-2`、`f=q`，`A_g,A_f` 为两侧已用 residue 数，则 `M_q^2<=q(q-2)` 等价于 `(A_g^2/g)*(A_f^2/f)<=1`。当前最大压力乘积为 0.160177975528，单侧高压但未同步碰撞的 q 为 [43, 103]。因此新的最窄硬点不是单侧 residue 多，而是相邻 twin epochs 两侧压力同步超过 1；若出现则登记为 `PressureProduct-PDEC/ColumnCRT`。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
all_sqrt_product_pressure_equivalences_closed=true
all_current_rows_pass_paired_pressure_gate=true
max_paired_side_pressure_product=144/899 ~= 0.160177975528
min_pressure_product_slack=755/899 ~= 0.839822024472
one_sided_pressure_q_values=[43, 103]
row_column_unconditional_closed=false
```

## 1. 压力乘积表

| q | gen pressure | fill pressure | product | bottleneck | one-sided high | pass |
| ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 31 | `9/29` ~= 0.310345 | `16/31` ~= 0.516129 | `144/899` ~= 0.160178 | `generator` | `false` | `true` |
| 43 | `64/41` ~= 1.560976 | `4/43` ~= 0.093023 | `256/1763` ~= 0.145207 | `fill` | `true` | `true` |
| 103 | `144/101` ~= 1.425743 | `1/103` ~= 0.009709 | `144/10403` ~= 0.013842 | `fill` | `true` | `true` |

## 2. 精确等价

```text
M_q = A_g A_f, g=q-2, f=q.
M_q^2 <= gf
iff (A_g^2/g) * (A_f^2/f) <= 1.
```

这说明单侧 residue 压力偏高还不足以产生反例链；必须与相邻 twin epoch 的另一侧压力同步，才会破坏平方根乘积门。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `sqrt_gate_equals_paired_side_pressure_gate` | `closed` | M_q^2<=q(q-2) is exactly (g_used^2/(q-2))*(f_used^2/q)<=1, so the hardpoint is a two-side synchronized residue-pressure product, not a raw atom count. |
| `current_one_sided_pressure_does_not_collide` | `closed_current_sweep` | The current sweep has generator-side pressure above one for q=43 and q=103, but the paired fill-side pressure is small enough that no q violates the product gate. |
| `pressure_product_pdec_routing` | `closed_routing` | If the paired product exceeds one, the failure is a named PressureProduct-PDEC/ColumnCRT object: adjacent twin epochs simultaneously carry too much compatible residue pressure. |
| `global_paired_pressure_bound` | `open` | A self-contained proof still must show this paired pressure product is always <=1 for persistent AffineTwin atoms, or exclude the named PDEC family. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SqrtGatePressureEquivalenceClosed` | `true` | `true` | 平方根乘积门已精确改写为两侧 residue 压力乘积不超过 1。 | closed |
| `CurrentPressureProductGateClosed` | `true` | `false` | 当前候选 q 没有两侧压力同步碰撞；最大压力乘积低于 1。 | finite evidence only |
| `OneSidedPressureExplained` | `true` | `false` | 样本中的高 generator 压力不是终端矛盾，因相邻 fill 压力不足以同步。 | finite structural diagnosis |
| `PressureProductPDECRouted` | `true` | `true` | 若两侧压力乘积超过 1，失败形态已命名为相邻 twin epoch 的同步 residue 压力碰撞。 | exclusion still separate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把平方根门压成压力乘积门，不关闭全局行/列命题。 | AffineTwinPairedSidePressureBoundOrPressureProductPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinPairedSidePressureBoundOrPressureProductPDECExclusion`。
- 具体目标：证明相邻 twin epochs 的两侧 residue 压力不能同步超过 1。
- 失败形态：若同步超过 1，则输出 `PressureProduct-PDEC/ColumnCRT`，再用相位/列 CRT 约束排斥。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_paired_side_pressure_router.py` | `87bf672718d01270b1fad08d735ff55e9220b11e397998ada1a5835eb51bc4cf` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json` | `44e048bbb9be8b3e2fa427090bf3bfa613575035385807986c0b7a3c664ff50a` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
