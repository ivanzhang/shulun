# Triad-A1 ForcedCap ColumnTail 暴露审计

**状态：** `forced_caps_columntail_exposure_materialized`

ForcedCap 的旧层低洞需求暴露已物化为 column-tail 签名账本。这是轻量 exposure ledger，不声称已经枚举完成态实际支付选择；它把 forced cap 的下一终端输入压成固定签名 PDEC 或分散 CleanKLS/DLS。

## 1. 结构语义

对 `ForcedPersistentByDensityBarrier`，固定 `Q` 同层 cap 已由密度屏障判定不能闭合；但 cap 内低洞仍必须由高素数 residue 支付。
本文先登记轻量暴露账本：对每个低洞列和每个高素数，计算可覆盖该洞的唯一 fiber residue，并按 `M(phase)` 加权。

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|；
exposure(prime,residue,column) += M(phase)。
```

暴露账本不是完整支付选择枚举；它给出 forced cap 后续 PDEC/ColumnTail 证书必须面对的候选签名。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `forcedcap_columntail_exposure_script` | `f51677c648fdc5c9e8a680ac0133e6bf74e2691015cd9b5c4cd8f4cc7cc0ed90` |
| `dualcap_json` | `b6bf0fc2a4305656fa7aef8cac33aa9b7dd1867617611fe7b96a23e8ba251c53` |
| `multiplicity_cap_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |

## 3. 汇总

- `forced_cap_count=24`。
- `all_intersections_recomputed=True`。
- `route_counts={'ForcedColumnTailExposurePDECOrDistributedCleanKLS': 24}`。

## 4. P 级有效暴露支撑

| P | caps | min eff prime exposure | min eff residue exposure | min eff column-residue exposure | max residue exposure share | max colres exposure share |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | 12 | 1 | 10.9309 | 9.86521 | 0.0914834 | 0.101366 |
| 47 | 12 | 1 | 10.4218 | 8.46328 | 0.0959528 | 0.118157 |

## 5. Cap 明细

| P | alpha | h | dir | mass | demand | exposure/demand | max residue exposure/demand | max colres exposure/demand | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 0 | 805 | 0.25 | 520444886 | 3681774070 | 8 | 0.082822 | 0.0927079 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0 | 1505 | 0.75 | 520266260 | 3680568532 | 8 | 0.0828344 | 0.0929628 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.5 | 805 | 0.25 | 417617864 | 2927527528 | 8 | 0.087153 | 0.0953805 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.5 | 1505 | 0.75 | 417617864 | 2927527528 | 8 | 0.087153 | 0.0953805 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0 | 770 | 0.5 | 382559424 | 2767127028 | 8 | 0.0887159 | 0.0998313 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0 | 1540 | 0.5 | 382559424 | 2767127028 | 8 | 0.0887159 | 0.0998313 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.5 | 1155 | 0 | 295544368 | 2122220360 | 8 | 0.0914834 | 0.101366 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.5 | 1155 | 0.5 | 295544368 | 2122220360 | 8 | 0.0914834 | 0.101366 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 295544368 | 2122220360 | 8 | 0.0914834 | 0.101366 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 295544368 | 2122220360 | 8 | 0.0914834 | 0.101366 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 295544368 | 2122220360 | 8 | 0.0914834 | 0.101366 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 295544368 | 2122220360 | 8 | 0.0914834 | 0.101366 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0 | 665 | 0.25 | 14307723048 | 109225010520 | 9 | 0.0949491 | 0.0997327 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0 | 1645 | 0.75 | 14240169000 | 108692179512 | 9 | 0.09516 | 0.10002 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0 | 770 | 0.5 | 12484093560 | 96599086824 | 9 | 0.0959528 | 0.107084 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0 | 1540 | 0.5 | 12484093560 | 96599086824 | 9 | 0.0959528 | 0.107084 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1001 | 0.25 | 10529907264 | 79296544896 | 9 | 0.0923769 | 0.118157 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1309 | 0.75 | 10529907264 | 79296544896 | 9 | 0.0923769 | 0.118157 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1155 | 0 | 8638014624 | 67088446560 | 9 | 0.094961 | 0.100214 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.5 | 1155 | 0.5 | 8638014624 | 67088446560 | 9 | 0.094961 | 0.100214 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 8638014624 | 67088446560 | 9 | 0.094961 | 0.100214 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 8638014624 | 67088446560 | 9 | 0.094961 | 0.100214 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 8638014624 | 67088446560 | 9 | 0.094961 | 0.100214 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 8638014624 | 67088446560 | 9 | 0.094961 | 0.100214 | `ForcedColumnTailExposurePDECOrDistributedCleanKLS` |

## 6. Top 暴露签名

### P=43 alpha=0 h=805 dir=0.25 source=top_by_mass

- `phase_count_by_holes={6: 8, 7: 150, 8: 404, 9: 433, 10: 82}`。
- top prime exposure: `[{'key': '13', 'count': 3681774070}, {'key': '17', 'count': 3681774070}, {'key': '19', 'count': 3681774070}, {'key': '23', 'count': 3681774070}, {'key': '29', 'count': 3681774070}]`。
- top residue exposure: `[{'key': '13:12', 'count': 304931934}, {'key': '13:0', 'count': 301083666}, {'key': '13:2', 'count': 292353776}, {'key': '13:10', 'count': 289165742}, {'key': '13:9', 'count': 288637686}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 341329716}, {'key': '13:1', 'count': 339957516}, {'key': '13:2', 'count': 312123748}, {'key': '13:4', 'count': 294761626}, {'key': '13:0', 'count': 290936308}]`。

### P=43 alpha=0 h=1505 dir=0.75 source=top_by_mass

- `phase_count_by_holes={6: 8, 7: 150, 8: 400, 9: 437, 10: 86}`。
- top prime exposure: `[{'key': '13', 'count': 3680568532}, {'key': '17', 'count': 3680568532}, {'key': '19', 'count': 3680568532}, {'key': '23', 'count': 3680568532}, {'key': '29', 'count': 3680568532}]`。
- top residue exposure: `[{'key': '13:12', 'count': 304877604}, {'key': '13:0', 'count': 300659520}, {'key': '13:2', 'count': 292540046}, {'key': '13:10', 'count': 289022606}, {'key': '13:9', 'count': 288441540}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 342155970}, {'key': '13:1', 'count': 339864420}, {'key': '13:2', 'count': 312813058}, {'key': '13:4', 'count': 295070986}, {'key': '13:0', 'count': 290977618}]`。

### P=43 alpha=0.5 h=805 dir=0.25 source=top_by_mass

- `phase_count_by_holes={6: 8, 7: 120, 8: 270, 9: 286, 10: 50}`。
- top prime exposure: `[{'key': '13', 'count': 2927527528}, {'key': '17', 'count': 2927527528}, {'key': '19', 'count': 2927527528}, {'key': '23', 'count': 2927527528}, {'key': '29', 'count': 2927527528}]`。
- top residue exposure: `[{'key': '13:12', 'count': 255142800}, {'key': '13:3', 'count': 238362384}, {'key': '13:9', 'count': 237289758}, {'key': '13:1', 'count': 235000148}, {'key': '13:10', 'count': 234278744}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 279229134}, {'key': '13:4', 'count': 260443780}, {'key': '13:1', 'count': 255721014}, {'key': '13:2', 'count': 244531588}, {'key': '17:1', 'count': 243562384}]`。

### P=43 alpha=0.5 h=1505 dir=0.75 source=top_by_mass

- `phase_count_by_holes={6: 8, 7: 120, 8: 270, 9: 286, 10: 50}`。
- top prime exposure: `[{'key': '13', 'count': 2927527528}, {'key': '17', 'count': 2927527528}, {'key': '19', 'count': 2927527528}, {'key': '23', 'count': 2927527528}, {'key': '29', 'count': 2927527528}]`。
- top residue exposure: `[{'key': '13:12', 'count': 255142800}, {'key': '13:3', 'count': 238362384}, {'key': '13:9', 'count': 237289758}, {'key': '13:1', 'count': 235000148}, {'key': '13:10', 'count': 234278744}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 279229134}, {'key': '13:4', 'count': 260443780}, {'key': '13:1', 'count': 255721014}, {'key': '13:2', 'count': 244531588}, {'key': '17:1', 'count': 243562384}]`。

### P=43 alpha=0 h=770 dir=0.5 source=top_by_size

- `phase_count_by_holes={6: 4, 7: 104, 8: 468, 9: 648, 10: 146}`。
- top prime exposure: `[{'key': '13', 'count': 2767127028}, {'key': '17', 'count': 2767127028}, {'key': '19', 'count': 2767127028}, {'key': '23', 'count': 2767127028}, {'key': '29', 'count': 2767127028}]`。
- top residue exposure: `[{'key': '13:0', 'count': 245488180}, {'key': '13:4', 'count': 243261422}, {'key': '13:2', 'count': 226983132}, {'key': '13:11', 'count': 223483024}, {'key': '13:9', 'count': 218937226}]`。
- top column-residue exposure: `[{'key': '13:1', 'count': 276245928}, {'key': '13:3', 'count': 262230472}, {'key': '13:2', 'count': 227889224}, {'key': '17:8', 'count': 227429668}, {'key': '13:0', 'count': 222496712}]`。

### P=43 alpha=0 h=1540 dir=0.5 source=top_by_size

- `phase_count_by_holes={6: 4, 7: 104, 8: 468, 9: 648, 10: 146}`。
- top prime exposure: `[{'key': '13', 'count': 2767127028}, {'key': '17', 'count': 2767127028}, {'key': '19', 'count': 2767127028}, {'key': '23', 'count': 2767127028}, {'key': '29', 'count': 2767127028}]`。
- top residue exposure: `[{'key': '13:0', 'count': 245488180}, {'key': '13:4', 'count': 243261422}, {'key': '13:2', 'count': 226983132}, {'key': '13:11', 'count': 223483024}, {'key': '13:9', 'count': 218937226}]`。
- top column-residue exposure: `[{'key': '13:1', 'count': 276245928}, {'key': '13:3', 'count': 262230472}, {'key': '13:2', 'count': 227889224}, {'key': '17:8', 'count': 227429668}, {'key': '13:0', 'count': 222496712}]`。

### P=43 alpha=0.5 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={6: 4, 7: 82, 8: 347, 9: 478, 10: 114}`。
- top prime exposure: `[{'key': '13', 'count': 2122220360}, {'key': '17', 'count': 2122220360}, {'key': '19', 'count': 2122220360}, {'key': '23', 'count': 2122220360}, {'key': '29', 'count': 2122220360}]`。
- top residue exposure: `[{'key': '13:12', 'count': 194147974}, {'key': '13:3', 'count': 176075540}, {'key': '13:8', 'count': 173936322}, {'key': '13:10', 'count': 171323882}, {'key': '13:11', 'count': 163192294}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 215121760}, {'key': '13:1', 'count': 215121760}, {'key': '13:10', 'count': 197375836}, {'key': '13:8', 'count': 197375836}, {'key': '17:4', 'count': 195565128}]`。

### P=43 alpha=0.5 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={6: 4, 7: 82, 8: 347, 9: 478, 10: 114}`。
- top prime exposure: `[{'key': '13', 'count': 2122220360}, {'key': '17', 'count': 2122220360}, {'key': '19', 'count': 2122220360}, {'key': '23', 'count': 2122220360}, {'key': '29', 'count': 2122220360}]`。
- top residue exposure: `[{'key': '13:0', 'count': 194147974}, {'key': '13:9', 'count': 176075540}, {'key': '13:4', 'count': 173936322}, {'key': '13:2', 'count': 171323882}, {'key': '13:1', 'count': 163192294}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 215121760}, {'key': '13:0', 'count': 215121760}, {'key': '13:7', 'count': 197375836}, {'key': '13:9', 'count': 197375836}, {'key': '17:3', 'count': 195565128}]`。

### P=43 alpha=0.9 h=1155 dir=0 source=top_by_mass

- `phase_count_by_holes={6: 4, 7: 82, 8: 347, 9: 478, 10: 114}`。
- top prime exposure: `[{'key': '13', 'count': 2122220360}, {'key': '17', 'count': 2122220360}, {'key': '19', 'count': 2122220360}, {'key': '23', 'count': 2122220360}, {'key': '29', 'count': 2122220360}]`。
- top residue exposure: `[{'key': '13:12', 'count': 194147974}, {'key': '13:3', 'count': 176075540}, {'key': '13:8', 'count': 173936322}, {'key': '13:10', 'count': 171323882}, {'key': '13:11', 'count': 163192294}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 215121760}, {'key': '13:1', 'count': 215121760}, {'key': '13:10', 'count': 197375836}, {'key': '13:8', 'count': 197375836}, {'key': '17:4', 'count': 195565128}]`。

### P=43 alpha=0.9 h=1155 dir=0.5 source=top_by_mass

- `phase_count_by_holes={6: 4, 7: 82, 8: 347, 9: 478, 10: 114}`。
- top prime exposure: `[{'key': '13', 'count': 2122220360}, {'key': '17', 'count': 2122220360}, {'key': '19', 'count': 2122220360}, {'key': '23', 'count': 2122220360}, {'key': '29', 'count': 2122220360}]`。
- top residue exposure: `[{'key': '13:0', 'count': 194147974}, {'key': '13:9', 'count': 176075540}, {'key': '13:4', 'count': 173936322}, {'key': '13:2', 'count': 171323882}, {'key': '13:1', 'count': 163192294}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 215121760}, {'key': '13:0', 'count': 215121760}, {'key': '13:7', 'count': 197375836}, {'key': '13:9', 'count': 197375836}, {'key': '17:3', 'count': 195565128}]`。

### P=43 alpha=0.9 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={6: 4, 7: 82, 8: 347, 9: 478, 10: 114}`。
- top prime exposure: `[{'key': '13', 'count': 2122220360}, {'key': '17', 'count': 2122220360}, {'key': '19', 'count': 2122220360}, {'key': '23', 'count': 2122220360}, {'key': '29', 'count': 2122220360}]`。
- top residue exposure: `[{'key': '13:12', 'count': 194147974}, {'key': '13:3', 'count': 176075540}, {'key': '13:8', 'count': 173936322}, {'key': '13:10', 'count': 171323882}, {'key': '13:11', 'count': 163192294}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 215121760}, {'key': '13:1', 'count': 215121760}, {'key': '13:10', 'count': 197375836}, {'key': '13:8', 'count': 197375836}, {'key': '17:4', 'count': 195565128}]`。

### P=43 alpha=0.9 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={6: 4, 7: 82, 8: 347, 9: 478, 10: 114}`。
- top prime exposure: `[{'key': '13', 'count': 2122220360}, {'key': '17', 'count': 2122220360}, {'key': '19', 'count': 2122220360}, {'key': '23', 'count': 2122220360}, {'key': '29', 'count': 2122220360}]`。
- top residue exposure: `[{'key': '13:0', 'count': 194147974}, {'key': '13:9', 'count': 176075540}, {'key': '13:4', 'count': 173936322}, {'key': '13:2', 'count': 171323882}, {'key': '13:1', 'count': 163192294}]`。
- top column-residue exposure: `[{'key': '13:3', 'count': 215121760}, {'key': '13:0', 'count': 215121760}, {'key': '13:7', 'count': 197375836}, {'key': '13:9', 'count': 197375836}, {'key': '17:3', 'count': 195565128}]`。

### P=47 alpha=0 h=665 dir=0.25 source=top_by_mass

- `phase_count_by_holes={7: 32, 8: 184, 9: 386, 10: 422, 11: 120, 12: 6}`。
- top prime exposure: `[{'key': '13', 'count': 109225010520}, {'key': '17', 'count': 109225010520}, {'key': '19', 'count': 109225010520}, {'key': '23', 'count': 109225010520}, {'key': '29', 'count': 109225010520}]`。
- top residue exposure: `[{'key': '13:12', 'count': 10370815032}, {'key': '13:0', 'count': 10218421512}, {'key': '13:4', 'count': 9177929232}, {'key': '13:8', 'count': 9146062272}, {'key': '13:9', 'count': 8970109464}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 10893302856}, {'key': '13:3', 'count': 10251477336}, {'key': '13:5', 'count': 9954323208}, {'key': '13:10', 'count': 8999857608}, {'key': '17:6', 'count': 8885515992}]`。

### P=47 alpha=0 h=1645 dir=0.75 source=top_by_mass

- `phase_count_by_holes={7: 32, 8: 181, 9: 385, 10: 420, 11: 121, 12: 6}`。
- top prime exposure: `[{'key': '13', 'count': 108692179512}, {'key': '17', 'count': 108692179512}, {'key': '19', 'count': 108692179512}, {'key': '23', 'count': 108692179512}, {'key': '29', 'count': 108692179512}]`。
- top residue exposure: `[{'key': '13:12', 'count': 10343152224}, {'key': '13:0', 'count': 10149042624}, {'key': '13:4', 'count': 9136705824}, {'key': '13:8', 'count': 9086578032}, {'key': '13:9', 'count': 8959761624}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 10871344008}, {'key': '13:3', 'count': 10169213256}, {'key': '13:5', 'count': 9919331592}, {'key': '13:10', 'count': 8969516568}, {'key': '17:6', 'count': 8800870872}]`。

### P=47 alpha=0 h=770 dir=0.5 source=top_by_size

- `phase_count_by_holes={7: 24, 8: 204, 9: 501, 10: 606, 11: 167, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 96599086824}, {'key': '17', 'count': 96599086824}, {'key': '19', 'count': 96599086824}, {'key': '23', 'count': 96599086824}, {'key': '29', 'count': 96599086824}]`。
- top residue exposure: `[{'key': '13:12', 'count': 9268955568}, {'key': '13:0', 'count': 9115890504}, {'key': '13:3', 'count': 8449096200}, {'key': '13:4', 'count': 8375003616}, {'key': '13:1', 'count': 7638176640}]`。
- top column-residue exposure: `[{'key': '13:5', 'count': 10344227400}, {'key': '13:4', 'count': 8390218992}, {'key': '13:3', 'count': 8079070128}, {'key': '19:5', 'count': 8012214696}, {'key': '13:11', 'count': 7964145792}]`。

### P=47 alpha=0 h=1540 dir=0.5 source=top_by_size

- `phase_count_by_holes={7: 24, 8: 204, 9: 501, 10: 606, 11: 167, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 96599086824}, {'key': '17', 'count': 96599086824}, {'key': '19', 'count': 96599086824}, {'key': '23', 'count': 96599086824}, {'key': '29', 'count': 96599086824}]`。
- top residue exposure: `[{'key': '13:12', 'count': 9268955568}, {'key': '13:0', 'count': 9115890504}, {'key': '13:3', 'count': 8449096200}, {'key': '13:4', 'count': 8375003616}, {'key': '13:1', 'count': 7638176640}]`。
- top column-residue exposure: `[{'key': '13:5', 'count': 10344227400}, {'key': '13:4', 'count': 8390218992}, {'key': '13:3', 'count': 8079070128}, {'key': '19:5', 'count': 8012214696}, {'key': '13:11', 'count': 7964145792}]`。

### P=47 alpha=0.5 h=1001 dir=0.25 source=top_by_mass

- `phase_count_by_holes={7: 26, 8: 178, 9: 316, 10: 184, 11: 48, 12: 5}`。
- top prime exposure: `[{'key': '13', 'count': 79296544896}, {'key': '17', 'count': 79296544896}, {'key': '19', 'count': 79296544896}, {'key': '23', 'count': 79296544896}, {'key': '29', 'count': 79296544896}]`。
- top residue exposure: `[{'key': '13:12', 'count': 7325166288}, {'key': '13:0', 'count': 7257005616}, {'key': '13:9', 'count': 6972721152}, {'key': '13:8', 'count': 6659261112}, {'key': '13:7', 'count': 6371909640}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 9369477384}, {'key': '13:3', 'count': 7934982936}, {'key': '13:5', 'count': 7800867240}, {'key': '19:5', 'count': 7234295808}, {'key': '19:4', 'count': 6921292224}]`。

### P=47 alpha=0.5 h=1309 dir=0.75 source=top_by_mass

- `phase_count_by_holes={7: 26, 8: 178, 9: 316, 10: 184, 11: 48, 12: 5}`。
- top prime exposure: `[{'key': '13', 'count': 79296544896}, {'key': '17', 'count': 79296544896}, {'key': '19', 'count': 79296544896}, {'key': '23', 'count': 79296544896}, {'key': '29', 'count': 79296544896}]`。
- top residue exposure: `[{'key': '13:12', 'count': 7325166288}, {'key': '13:0', 'count': 7257005616}, {'key': '13:9', 'count': 6972721152}, {'key': '13:8', 'count': 6659261112}, {'key': '13:7', 'count': 6371909640}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 9369477384}, {'key': '13:3', 'count': 7934982936}, {'key': '13:5', 'count': 7800867240}, {'key': '19:5', 'count': 7234295808}, {'key': '19:4', 'count': 6921292224}]`。

### P=47 alpha=0.5 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={7: 16, 8: 141, 9: 366, 10: 462, 11: 138, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 67088446560}, {'key': '17', 'count': 67088446560}, {'key': '19', 'count': 67088446560}, {'key': '23', 'count': 67088446560}, {'key': '29', 'count': 67088446560}]`。
- top residue exposure: `[{'key': '13:12', 'count': 6370789056}, {'key': '13:9', 'count': 6300843432}, {'key': '13:8', 'count': 6195261024}, {'key': '13:0', 'count': 5870877288}, {'key': '13:7', 'count': 5393977224}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 6723201048}, {'key': '13:5', 'count': 6723201048}, {'key': '13:10', 'count': 6176688168}, {'key': '13:12', 'count': 6176688168}, {'key': '17:6', 'count': 6102092160}]`。

### P=47 alpha=0.5 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={7: 16, 8: 141, 9: 366, 10: 462, 11: 138, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 67088446560}, {'key': '17', 'count': 67088446560}, {'key': '19', 'count': 67088446560}, {'key': '23', 'count': 67088446560}, {'key': '29', 'count': 67088446560}]`。
- top residue exposure: `[{'key': '13:0', 'count': 6370789056}, {'key': '13:3', 'count': 6300843432}, {'key': '13:4', 'count': 6195220704}, {'key': '13:12', 'count': 5870836968}, {'key': '13:5', 'count': 5394017544}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 6723201048}, {'key': '13:3', 'count': 6723201048}, {'key': '13:11', 'count': 6176688168}, {'key': '13:9', 'count': 6176688168}, {'key': '17:7', 'count': 6102092160}]`。

### P=47 alpha=0.9 h=1155 dir=0 source=top_by_mass

- `phase_count_by_holes={7: 16, 8: 141, 9: 366, 10: 462, 11: 138, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 67088446560}, {'key': '17', 'count': 67088446560}, {'key': '19', 'count': 67088446560}, {'key': '23', 'count': 67088446560}, {'key': '29', 'count': 67088446560}]`。
- top residue exposure: `[{'key': '13:12', 'count': 6370789056}, {'key': '13:9', 'count': 6300843432}, {'key': '13:8', 'count': 6195261024}, {'key': '13:0', 'count': 5870877288}, {'key': '13:7', 'count': 5393977224}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 6723201048}, {'key': '13:5', 'count': 6723201048}, {'key': '13:10', 'count': 6176688168}, {'key': '13:12', 'count': 6176688168}, {'key': '17:6', 'count': 6102092160}]`。

### P=47 alpha=0.9 h=1155 dir=0.5 source=top_by_mass

- `phase_count_by_holes={7: 16, 8: 141, 9: 366, 10: 462, 11: 138, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 67088446560}, {'key': '17', 'count': 67088446560}, {'key': '19', 'count': 67088446560}, {'key': '23', 'count': 67088446560}, {'key': '29', 'count': 67088446560}]`。
- top residue exposure: `[{'key': '13:0', 'count': 6370789056}, {'key': '13:3', 'count': 6300843432}, {'key': '13:4', 'count': 6195220704}, {'key': '13:12', 'count': 5870836968}, {'key': '13:5', 'count': 5394017544}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 6723201048}, {'key': '13:3', 'count': 6723201048}, {'key': '13:11', 'count': 6176688168}, {'key': '13:9', 'count': 6176688168}, {'key': '17:7', 'count': 6102092160}]`。

### P=47 alpha=0.9 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={7: 16, 8: 141, 9: 366, 10: 462, 11: 138, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 67088446560}, {'key': '17', 'count': 67088446560}, {'key': '19', 'count': 67088446560}, {'key': '23', 'count': 67088446560}, {'key': '29', 'count': 67088446560}]`。
- top residue exposure: `[{'key': '13:12', 'count': 6370789056}, {'key': '13:9', 'count': 6300843432}, {'key': '13:8', 'count': 6195261024}, {'key': '13:0', 'count': 5870877288}, {'key': '13:7', 'count': 5393977224}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 6723201048}, {'key': '13:5', 'count': 6723201048}, {'key': '13:10', 'count': 6176688168}, {'key': '13:12', 'count': 6176688168}, {'key': '17:6', 'count': 6102092160}]`。

### P=47 alpha=0.9 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={7: 16, 8: 141, 9: 366, 10: 462, 11: 138, 12: 10}`。
- top prime exposure: `[{'key': '13', 'count': 67088446560}, {'key': '17', 'count': 67088446560}, {'key': '19', 'count': 67088446560}, {'key': '23', 'count': 67088446560}, {'key': '29', 'count': 67088446560}]`。
- top residue exposure: `[{'key': '13:0', 'count': 6370789056}, {'key': '13:3', 'count': 6300843432}, {'key': '13:4', 'count': 6195220704}, {'key': '13:12', 'count': 5870836968}, {'key': '13:5', 'count': 5394017544}]`。
- top column-residue exposure: `[{'key': '13:4', 'count': 6723201048}, {'key': '13:3', 'count': 6723201048}, {'key': '13:11', 'count': 6176688168}, {'key': '13:9', 'count': 6176688168}, {'key': '17:7', 'count': 6102092160}]`。

## 7. 读法

这一步没有排除 forced cap；它把 forced cap 的 column-tail 终端义务物化为轻量签名账本。
若某个暴露签名在正式反例族中持久承担实际支付，就进入 TailAnchor/ColumnCRT PDEC。
若实际支付不能固定在这些 top 签名上，则 forced cap 只能继续升层或进入分散 CleanKLS/DLS。
