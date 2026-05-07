# Triad-A1 连续弧 ColumnTail 桥接

**状态：** `continuous_dualcap_columntail_bridge_materialized`

连续方向弧 DualCap 已接到 column-tail 暴露账本。当前步骤仍未证明最终 U_CRT<L_PDEC，但把下一硬点推进为 ActualPaymentSelection：真实支付若集中则进 PDEC，若不集中则进 CleanKLS/DLS。

## 1. 递归剥离律

对连续方向 persistent cap 的每个低洞，真实反例必须选择某个 tail prime residue 支付。若某个 payment signature 在无限子族中持久占正比例，则该签名给出 column/tail PDEC 行；若任意固定签名的比例都被递归剥离到 0，则支付测度扩散，进入 CleanKLS/DLS。该接口不依赖预设全局常数，而依赖 limsup 正质量或 diffuse 极限二分。

```text
continuous cap C
=> low-hole demand D_C
=> actual tail payment measure mu_C on (prime,residue,column-residue)
=> limsup positive signature -> column/tail PDEC
=> all fixed signatures vanish -> diffuse CleanKLS/DLS。
```

本文登记的是暴露账本：所有真实支付签名都必须落在这些候选桶中；actual payment 选择仍是下一硬点。

## 2. 汇总

- `cap_report_count=9`。
- `all_cap_recomputations_match=True`。
- `route_counts={'ContinuousCapActualPaymentSelectionDichotomy': 8, 'NoTailDemandSparseOrLocalSurvivor': 1}`。
- `parameters={'top_rows_per_p': 1, 'top_limit': 5}`。

## 3. P 级桥接读数

| P | caps | positive demand caps | max U_box/M | max payment sig share | min effective sig support | routes |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 1 | 0 | 0.998391 | 0 | n/a | `{'NoTailDemandSparseOrLocalSurvivor': 1}` |
| 17 | 1 | 1 | 0.920824 | 0.0357143 | 28 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 19 | 1 | 1 | 0.875267 | 0.0441176 | 22.6667 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 23 | 1 | 1 | 0.871343 | 0.0274159 | 36.4752 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 29 | 1 | 1 | 0.849387 | 0.0357788 | 27.9495 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 31 | 1 | 1 | 0.807475 | 0.024914 | 40.1381 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 37 | 1 | 1 | 0.848953 | 0.0195775 | 51.079 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 43 | 1 | 1 | 0.730057 | 0.0105805 | 94.5139 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |
| 47 | 1 | 1 | 0.70571 | 0.0164943 | 60.627 | `{'ContinuousCapActualPaymentSelectionDichotomy': 1}` |

## 4. Cap 明细

| P | top | h | zeta | phases | mass share | demand | max sig share | eff sig support | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 0 | 377 | 0.418398 | 4 | 1 | 0 | n/a | n/a | `NoTailDemandSparseOrLocalSurvivor` |
| 17 | 0 | 1309 | 0.716667 | 28 | 1 | 28 | 0.0357143 | 28 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 19 | 0 | 847 | 0.318866 | 137 | 0.987903 | 748 | 0.0441176 | 22.6667 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 23 | 0 | 1045 | 0.272541 | 188 | 0.923611 | 7368 | 0.0274159 | 36.4752 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 29 | 0 | 1595 | 0.655463 | 145 | 0.981297 | 22136 | 0.0357788 | 27.9495 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 31 | 0 | 1085 | 0.764017 | 400 | 0.907874 | 597416 | 0.024914 | 40.1381 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 37 | 0 | 1015 | 0.279846 | 549 | 0.944427 | 5096664 | 0.0195775 | 51.079 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 43 | 0 | 805 | 0.324739 | 1094 | 0.88754 | 3710420992 | 0.0105805 | 94.5139 | `ContinuousCapActualPaymentSelectionDichotomy` |
| 47 | 0 | 665 | 0.357868 | 1142 | 0.862747 | 114112801296 | 0.0164943 | 60.627 | `ContinuousCapActualPaymentSelectionDichotomy` |

## 5. Top 暴露签名

### P=13 top=0 h=377 zeta=0.418398

- `phase_count_by_holes={0: 4}`。
- top payment signatures: `[]`。
- top residues: `[]`。
- top column residues: `[]`。

### P=17 top=0 h=1309 zeta=0.716667

- `phase_count_by_holes={1: 28}`。
- top payment signatures: `[{'key': '13:1:7', 'count': 1}, {'key': '13:2:8', 'count': 1}, {'key': '13:5:6', 'count': 1}, {'key': '13:4:12', 'count': 1}, {'key': '13:10:3', 'count': 1}]`。
- top residues: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column residues: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=19 top=0 h=847 zeta=0.318866

- `phase_count_by_holes={1: 8, 2: 129}`。
- top payment signatures: `[{'key': '17:2:9', 'count': 33}, {'key': '13:11:10', 'count': 33}, {'key': '17:7:10', 'count': 33}, {'key': '17:9:9', 'count': 33}, {'key': '13:1:9', 'count': 33}]`。
- top residues: `[{'key': '17:8', 'count': 90}, {'key': '13:7', 'count': 75}, {'key': '13:5', 'count': 75}, {'key': '13:8', 'count': 73}, {'key': '13:4', 'count': 73}]`。
- top column residues: `[{'key': '13:9', 'count': 110}, {'key': '17:9', 'count': 110}, {'key': '13:10', 'count': 106}, {'key': '17:10', 'count': 106}, {'key': '13:8', 'count': 67}]`。

### P=23 top=0 h=1045 zeta=0.272541

- `phase_count_by_holes={2: 24, 3: 164}`。
- top payment signatures: `[{'key': '13:0:1', 'count': 202}, {'key': '13:12:9', 'count': 202}, {'key': '19:1:12', 'count': 190}, {'key': '13:8:12', 'count': 190}, {'key': '19:17:11', 'count': 190}]`。
- top residues: `[{'key': '13:12', 'count': 756}, {'key': '13:0', 'count': 750}, {'key': '13:10', 'count': 706}, {'key': '13:4', 'count': 706}, {'key': '13:2', 'count': 700}]`。
- top column residues: `[{'key': '13:9', 'count': 858}, {'key': '13:1', 'count': 840}, {'key': '17:5', 'count': 662}, {'key': '13:5', 'count': 662}, {'key': '17:1', 'count': 644}]`。

### P=29 top=0 h=1595 zeta=0.655463

- `phase_count_by_holes={3: 8, 4: 117, 5: 20}`。
- top payment signatures: `[{'key': '17:8:6', 'count': 792}, {'key': '13:0:4', 'count': 540}, {'key': '13:12:12', 'count': 540}, {'key': '17:2:10', 'count': 498}, {'key': '17:14:2', 'count': 498}]`。
- top residues: `[{'key': '13:2', 'count': 2352}, {'key': '13:10', 'count': 2352}, {'key': '13:1', 'count': 2182}, {'key': '13:11', 'count': 2158}, {'key': '17:2', 'count': 2076}]`。
- top column residues: `[{'key': '13:1', 'count': 2364}, {'key': '13:2', 'count': 2340}, {'key': '13:3', 'count': 1966}, {'key': '13:0', 'count': 1966}, {'key': '13:11', 'count': 1848}]`。

### P=31 top=0 h=1085 zeta=0.764017

- `phase_count_by_holes={4: 32, 5: 237, 6: 131}`。
- top payment signatures: `[{'key': '13:7:2', 'count': 14884}, {'key': '13:5:3', 'count': 14860}, {'key': '13:2:4', 'count': 14584}, {'key': '13:10:1', 'count': 14416}, {'key': '23:11:4', 'count': 13132}]`。
- top residues: `[{'key': '13:5', 'count': 57918}, {'key': '13:7', 'count': 57750}, {'key': '13:10', 'count': 51160}, {'key': '13:2', 'count': 51112}, {'key': '13:8', 'count': 44342}]`。
- top column residues: `[{'key': '13:2', 'count': 72356}, {'key': '13:3', 'count': 72044}, {'key': '13:4', 'count': 70602}, {'key': '13:1', 'count': 69594}, {'key': '17:13', 'count': 49924}]`。

### P=37 top=0 h=1015 zeta=0.279846

- `phase_count_by_holes={5: 24, 6: 197, 7: 304, 8: 24}`。
- top payment signatures: `[{'key': '13:4:3', 'count': 99780}, {'key': '13:8:8', 'count': 99540}, {'key': '13:7:2', 'count': 97092}, {'key': '13:5:9', 'count': 97092}, {'key': '13:3:10', 'count': 95076}]`。
- top residues: `[{'key': '13:4', 'count': 462880}, {'key': '13:8', 'count': 462640}, {'key': '13:1', 'count': 435836}, {'key': '13:11', 'count': 434996}, {'key': '13:7', 'count': 422692}]`。
- top column residues: `[{'key': '13:2', 'count': 487792}, {'key': '13:9', 'count': 487672}, {'key': '13:4', 'count': 463714}, {'key': '13:7', 'count': 460234}, {'key': '17:1', 'count': 448278}]`。

### P=43 top=0 h=805 zeta=0.324739

- `phase_count_by_holes={6: 8, 7: 156, 8: 394, 9: 441, 10: 95}`。
- top payment signatures: `[{'key': '13:0:1', 'count': 39257934}, {'key': '13:12:3', 'count': 39248574}, {'key': '23:10:14', 'count': 38731680}, {'key': '23:12:6', 'count': 38699616}, {'key': '23:22:7', 'count': 36776376}]`。
- top residues: `[{'key': '13:12', 'count': 305293008}, {'key': '13:0', 'count': 304950288}, {'key': '13:10', 'count': 293709356}, {'key': '13:2', 'count': 292384364}, {'key': '13:9', 'count': 289147926}]`。
- top column residues: `[{'key': '13:3', 'count': 343370112}, {'key': '13:1', 'count': 342117864}, {'key': '13:2', 'count': 312427360}, {'key': '13:0', 'count': 297964144}, {'key': '13:4', 'count': 294259192}]`。

### P=47 top=0 h=665 zeta=0.357868

- `phase_count_by_holes={7: 32, 8: 201, 9: 397, 10: 392, 11: 112, 12: 8}`。
- top payment signatures: `[{'key': '13:4:4', 'count': 1882211832}, {'key': '13:8:4', 'count': 1872343872}, {'key': '13:0:5', 'count': 1714704504}, {'key': '13:12:3', 'count': 1713419304}, {'key': '13:2:5', 'count': 1264698096}]`。
- top residues: `[{'key': '13:0', 'count': 10864474128}, {'key': '13:12', 'count': 10834486608}, {'key': '13:8', 'count': 9559963392}, {'key': '13:4', 'count': 9556689744}, {'key': '13:3', 'count': 9348034056}]`。
- top column residues: `[{'key': '13:4', 'count': 11677842336}, {'key': '13:3', 'count': 10712374608}, {'key': '13:5', 'count': 10696036512}, {'key': '13:11', 'count': 9048882144}, {'key': '13:10', 'count': 9021242736}]`。

## 6. 当前硬点

这一步关闭的是“连续 cap 与 column-tail 无关”的退路。剩余真正硬点是：

```text
ActualPaymentSelection:
  从暴露候选桶提升到真实支付测度；
  证明 limsup 正质量签名产生合法 PDEC 行；
  证明所有签名递归剥离为 0 时满足 CleanKLS/DLS 输入条件。
```
