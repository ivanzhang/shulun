# Prime Matrix AffineTwin source materialization gate audit

**状态：** `current_sweep_source_materialization_gate_classified_global_open`

本审计把 formal-pair pruning 中的 `SourceMaterializationFailure` 继续拆成可检查的源门控不变量。
一个 formal residue product 要成为 actual packet，必须有 matching gap-fill source，并同时满足 `generator=q-2`、`fill=q`、方向、仿射 `p_delay` 和 slot-lock source key。

```text
candidate_q_values=[31, 43, 103]
source_gate_pass_q_values=[31]
source_gate_fail_q_values=[43, 103]
formal_pairs_blocked_by_source_gate=28
same_gap_wrong_source_formal_pair_count=16
no_gap_source_formal_pair_count=12
all_source_failures_classified_current=true
row_column_unconditional_closed=false
```

## 1. source gate 表

| q | route | M_form | blocked | same-gap sources | exact sources | failed invariants |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 31 | `ExactSourceMaterialized` | 12 | 0 | 1 | 1 | `none` |
| 43 | `SameGapWrongSource-MaterializationGate` | 16 | 16 | 1 | 0 | `generator_ell_match,generator_side_match,fill_side_match,p_delay_match` |
| 103 | `NoGapSource-MaterializationGate` | 12 | 12 | 0 | 0 | `gap_source_absent` |

## 2. q=43 的错源诊断

`q=43` 有同 gap source，但它不是 AffineTwin 期望源：

```text
expected: generator=41, fill=43, sides=minus->plus, p_delay=113
actual:   generator=47, fill=43, sides=plus->minus, p_delay=74
```

因此 `q=43` 的 `16` 个 formal residue products 全部被源门控删除；它们不是 actual packets。

## 3. q=103 的无源诊断

`q=103` 当前没有任何 gap-fill source row，因此 `12` 个 formal residue products 全部归入 `NoGapSource-MaterializationGate`。

## 4. 结论边界

- 当前 source gate 解释了 formal-pair pruning 中全部 `28` 个 source 未物化配对。
- 这不是全局行/列证明；全局仍需证明 source gate 的失败必路由到 `SameGapWrongSource-PDEC/SAE`、`NoGapSource-PDEC/SAE` 或 primitive support escape。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json` | `ed8532ade7e13ad9fe14068c545d961ba90a47895b395673cf69169c0967ac38` |
