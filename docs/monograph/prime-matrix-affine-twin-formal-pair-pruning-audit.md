# Prime Matrix AffineTwin formal-pair pruning audit

**状态：** `current_sweep_formal_pair_gap_fully_pruned_global_open`

本审计继续压缩 PM-ALC 的 `ProductAccountingTightening` 缺口：
形式乘积 `M_form` 只计入两侧 residue 的笛卡尔积；actual packet 还必须同时有 gap-fill source materialization 与双槽 CRT 相位代表。

```text
candidate_q_values=[31, 43, 103]
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
crt_window_empty_pair_total_current=11
source_unmaterialized_pair_total_current=28
unresolved_formal_pair_total_current=0
current_formal_gap_fully_pruned=true
```

## 1. pruning 表

| q | route | M_form | actual | CRT empty | source unmaterialized | unresolved | note |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | `CRTWindowExactPruning` | 12 | 1 | 11 | 0 | 0 | slot CRT support enumerated exactly |
| 43 | `SourceMaterializationFailure` | 16 | 0 | 0 | 16 | 0 | SameGapButWrongGeneratorOrOrientation |
| 103 | `SourceMaterializationFailure` | 12 | 0 | 0 | 12 | 0 | NoGapFillSourceForQ |

## 2. q=31 的精确 CRT 删除

`q=31` 的 `M_form=12` 来自 `3 x 4` 个 residue 配对。逐个 CRT 合并后，只有一对在 pair support `[2669,2688]` 中有代表：

| generator residue | fill residue | shifted fill residue | CRT residue | representatives |
| ---: | ---: | ---: | ---: | --- |
| 19 | 8 | 21 | 889 | `[2687]` |

其余 `11` 对 residue 的 CRT 代表均落在该支撑窗外，所以是 `CRTWindowEmpty` 虚配对。

## 3. 结论边界

- 当前 sweep 的 `formal_to_actual_gap=39` 已完全分解：`11` 个 `CRTWindowEmpty`，`28` 个 `SourceMaterializationFailure`。
- 这关闭的是当前证书的形式账本收紧，不是全局行/列命题。
- 全局仍需证明所有未来形式配对也必须进入 `CRTWindowEmpty`、`SourceMaterializationFailure-PDEC/SAE` 或 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/prime-matrix-affine-twin-actual-packet-contract-ledger.json` | `245368f75f2d1d0b9ad59fd7e2d6242cf3944985cc0b23e8de483f2ff70bd86d` |
