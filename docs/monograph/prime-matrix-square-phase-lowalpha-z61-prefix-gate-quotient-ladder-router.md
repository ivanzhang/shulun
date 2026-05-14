# Prime Matrix square-phase low-alpha z=61 PrefixGate quotient ladder

**状态：** `z61_prefix_gate_signed_phase_balance_reduced_to_quotient_ladder_count_open`

PrefixGate signed phase balance 已进一步压成 quotient ladder 计数问题：三个命中全部贡献同一 target 权重，quotient 分别为 `1,2,4`。负侧只有 quotient `1`，正侧有 quotient `2,4`，因此样本中的正/负相位实际比 完全等于命中计数比 `2/1`。下一步应证明这种 dyadic quotient ladder 在全局上给出计数平衡，或登记 Ladder-PDEC。

```text
quotients=[1, 2, 4]
all_quotients_are_powers_of_two=true
constant_per_hit_contribution_closed=true
positive_quotients=[2, 4]
negative_quotients=[1]
positive_minus_negative_count=1
signed_actual_balance_reduced_to_count_identity_closed=true
row_column_unconditional_closed=false
```

## 1. Quotient Ladder

| quotient | p | b | sign | contribution | power of 2 |
| ---: | ---: | ---: | --- | ---: | --- |
| 1 | 36739 | 28842 | `negative` | 0.555427 | true |
| 2 | 200003 | 57684 | `positive` | 0.555427 | true |
| 4 | 200003 | 115368 | `positive` | 0.555427 | true |

## 2. 证明边界

- 已闭合：signed phase balance 到 dyadic quotient 计数的样本恒等式。
- 未闭合：dyadic quotient count balance 的全局证明，或 Ladder-PDEC 排斥。
- 下一目标：`DyadicPhaseQuotientCountBalanceOrLadderPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json` | `7470bdf7651a2cdc84f388e336e7c4273cbb2aa2836bb149c17330950fe3365f` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_quotient_ladder_router.py` | `e74952b4e33e723e4980e4ab7f00799e5b2678c1d481ed3faad7d7ffc8608ff6` |
