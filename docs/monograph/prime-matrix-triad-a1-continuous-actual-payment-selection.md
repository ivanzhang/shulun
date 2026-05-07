# Triad-A1 连续弧 ActualPaymentSelection 审计

**状态：** `continuous_actual_payment_measure_constructed`

连续方向弧 cap 的 actual payment measure 已精确构造；暴露账本不再只是候选集合。剩余硬点被压成两个终端引理：limsup 正签名 => PDEC；全部签名递归消散 => CleanKLS/DLS。

## 1. 选择律

对每个完成态和每个低洞，按 high prime 的固定顺序选择第一个覆盖该洞的 residue。这把暴露候选桶提升为真实支付测度；总质量恒等式为 payment_count=sum_phase M(phase)*|H_low(phase)|。

```text
completion y=(y_ell)_ell；
hole c in H_low(t)；
pay(c,y)=first ell such that ell covers c under y_ell；
mu_C(bucket)=# canonical payments in bucket。
```

## 2. 递归二分

若 canonical payment measure 的某个有限签名在无限反例子族中具有正 limsup 质量，该签名进入 column/tail PDEC；若所有固定签名的质量递归趋零，则支付测度扩散，进入 CleanKLS/DLS admission。

这一步不依赖固定全局常数；它依赖无限子族上的 `limsup > 0` 或所有固定签名趋零。

## 3. 汇总

- `cap_report_count=9`。
- `all_cap_recomputations_match=True`。
- `all_payment_counts_match_demand=True`。
- `route_counts={'ActualPaymentMeasureDichotomySubmitted': 8, 'NoTailDemandSparseOrLocalSurvivor': 1}`。
- `parameters={'top_rows_per_p': 1, 'top_limit': 5, 'p_filter': None}`。

## 4. P 级 actual payment 读数

| P | caps | positive demand caps | max actual sig share | min effective sig support | min L2 sig support | routes |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 1 | 0 | 0 | n/a | n/a | `{'NoTailDemandSparseOrLocalSurvivor': 1}` |
| 17 | 1 | 1 | 0.0357143 | 28 | 28 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 19 | 1 | 1 | 0.0254011 | 39.3684 | 112.803 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 23 | 1 | 1 | 0.0103149 | 96.9474 | 260.521 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 29 | 1 | 1 | 0.0122877 | 81.3824 | 330.763 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 31 | 1 | 1 | 0.0180444 | 55.4189 | 391.834 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 37 | 1 | 1 | 0.0122645 | 81.5362 | 473.332 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 43 | 1 | 1 | 0.00316956 | 315.501 | 1539.39 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |
| 47 | 1 | 1 | 0.00598387 | 167.116 | 1342.9 | `{'ActualPaymentMeasureDichotomySubmitted': 1}` |

## 5. Cap 明细

| P | h | phases | mass share | demand | payment count | max sig share | eff sig support | L2 sig support | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 377 | 4 | 1 | 0 | 0 | n/a | n/a | n/a | `NoTailDemandSparseOrLocalSurvivor` |
| 17 | 1309 | 28 | 1 | 28 | 28 | 0.0357143 | 28 | 28 | `ActualPaymentMeasureDichotomySubmitted` |
| 19 | 847 | 137 | 0.987903 | 748 | 748 | 0.0254011 | 39.3684 | 112.803 | `ActualPaymentMeasureDichotomySubmitted` |
| 23 | 1045 | 188 | 0.923611 | 7368 | 7368 | 0.0103149 | 96.9474 | 260.521 | `ActualPaymentMeasureDichotomySubmitted` |
| 29 | 1595 | 145 | 0.981297 | 22136 | 22136 | 0.0122877 | 81.3824 | 330.763 | `ActualPaymentMeasureDichotomySubmitted` |
| 31 | 1085 | 400 | 0.907874 | 597416 | 597416 | 0.0180444 | 55.4189 | 391.834 | `ActualPaymentMeasureDichotomySubmitted` |
| 37 | 1015 | 549 | 0.944427 | 5096664 | 5096664 | 0.0122645 | 81.5362 | 473.332 | `ActualPaymentMeasureDichotomySubmitted` |
| 43 | 805 | 1094 | 0.88754 | 3710420992 | 3710420992 | 0.00316956 | 315.501 | 1539.39 | `ActualPaymentMeasureDichotomySubmitted` |
| 47 | 665 | 1142 | 0.862747 | 114112801296 | 114112801296 | 0.00598387 | 167.116 | 1342.9 | `ActualPaymentMeasureDichotomySubmitted` |

## 6. Top actual payment 签名

### P=13 top=0 h=377 zeta=0.418398

- `phase_count_by_holes={0: 4}`。
- `max_dp_state_count=1`。
- `distinct_payment_signature_count=0`。
- `payment_signature_l2_energy=n/a`。
- `inverse_l2_payment_signature_support=n/a`。
- top payment signatures: `[]`。
- top residues: `[]`。
- top column residues: `[]`。

### P=17 top=0 h=1309 zeta=0.716667

- `phase_count_by_holes={1: 28}`。
- `max_dp_state_count=2`。
- `distinct_payment_signature_count=28`。
- `payment_signature_l2_energy=0.0357143`。
- `inverse_l2_payment_signature_support=28`。
- top payment signatures: `[{'key': '13:1:7', 'count': 1}, {'key': '13:2:8', 'count': 1}, {'key': '13:5:6', 'count': 1}, {'key': '13:4:12', 'count': 1}, {'key': '13:10:3', 'count': 1}]`。
- top residues: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column residues: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=19 top=0 h=847 zeta=0.318866

- `phase_count_by_holes={1: 8, 2: 129}`。
- `max_dp_state_count=4`。
- `distinct_payment_signature_count=325`。
- `payment_signature_l2_energy=0.00886499`。
- `inverse_l2_payment_signature_support=112.803`。
- top payment signatures: `[{'key': '13:11:10', 'count': 19}, {'key': '13:1:9', 'count': 19}, {'key': '13:4:11', 'count': 18}, {'key': '13:8:8', 'count': 18}, {'key': '13:10:9', 'count': 17}]`。
- top residues: `[{'key': '13:7', 'count': 40}, {'key': '17:8', 'count': 40}, {'key': '13:5', 'count': 40}, {'key': '13:8', 'count': 39}, {'key': '13:4', 'count': 39}]`。
- top column residues: `[{'key': '13:9', 'count': 60}, {'key': '13:10', 'count': 58}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 48}, {'key': '13:8', 'count': 36}]`。

### P=23 top=0 h=1045 zeta=0.272541

- `phase_count_by_holes={2: 24, 3: 164}`。
- `max_dp_state_count=8`。
- `distinct_payment_signature_count=748`。
- `payment_signature_l2_energy=0.00383846`。
- `inverse_l2_payment_signature_support=260.521`。
- top payment signatures: `[{'key': '13:0:1', 'count': 76}, {'key': '13:12:9', 'count': 76}, {'key': '13:8:12', 'count': 72}, {'key': '13:4:11', 'count': 72}, {'key': '13:10:11', 'count': 70}]`。
- top residues: `[{'key': '13:12', 'count': 278}, {'key': '13:0', 'count': 276}, {'key': '13:10', 'count': 257}, {'key': '13:4', 'count': 257}, {'key': '13:2', 'count': 255}]`。
- top column residues: `[{'key': '13:9', 'count': 312}, {'key': '13:1', 'count': 306}, {'key': '13:5', 'count': 238}, {'key': '13:2', 'count': 226}, {'key': '13:8', 'count': 226}]`。

### P=29 top=0 h=1595 zeta=0.655463

- `phase_count_by_holes={3: 8, 4: 117, 5: 20}`。
- `max_dp_state_count=32`。
- `distinct_payment_signature_count=1083`。
- `payment_signature_l2_energy=0.00302332`。
- `inverse_l2_payment_signature_support=330.763`。
- top payment signatures: `[{'key': '13:0:2', 'count': 272}, {'key': '13:12:1', 'count': 272}, {'key': '17:8:6', 'count': 204}, {'key': '13:0:4', 'count': 148}, {'key': '13:12:12', 'count': 148}]`。
- top residues: `[{'key': '13:2', 'count': 640}, {'key': '13:10', 'count': 640}, {'key': '13:12', 'count': 594}, {'key': '13:0', 'count': 594}, {'key': '13:1', 'count': 552}]`。
- top column residues: `[{'key': '13:1', 'count': 838}, {'key': '13:2', 'count': 832}, {'key': '13:3', 'count': 492}, {'key': '13:0', 'count': 492}, {'key': '13:11', 'count': 488}]`。

### P=31 top=0 h=1085 zeta=0.764017

- `phase_count_by_holes={4: 32, 5: 237, 6: 131}`。
- `max_dp_state_count=64`。
- `distinct_payment_signature_count=2081`。
- `payment_signature_l2_energy=0.0025521`。
- `inverse_l2_payment_signature_support=391.834`。
- top payment signatures: `[{'key': '13:2:4', 'count': 10780}, {'key': '13:7:2', 'count': 10732}, {'key': '13:5:3', 'count': 10732}, {'key': '13:10:1', 'count': 10708}, {'key': '13:12:4', 'count': 3120}]`。
- top residues: `[{'key': '13:5', 'count': 21232}, {'key': '13:7', 'count': 21112}, {'key': '13:2', 'count': 20272}, {'key': '13:10', 'count': 20248}, {'key': '13:8', 'count': 11280}]`。
- top column residues: `[{'key': '13:4', 'count': 29968}, {'key': '13:1', 'count': 29344}, {'key': '13:2', 'count': 28540}, {'key': '13:3', 'count': 28468}, {'key': '17:1', 'count': 8807}]`。

### P=37 top=0 h=1015 zeta=0.279846

- `phase_count_by_holes={5: 24, 6: 197, 7: 304, 8: 24}`。
- `max_dp_state_count=256`。
- `distinct_payment_signature_count=3129`。
- `payment_signature_l2_energy=0.00211268`。
- `inverse_l2_payment_signature_support=473.332`。
- top payment signatures: `[{'key': '13:7:2', 'count': 62508}, {'key': '13:5:9', 'count': 62508}, {'key': '13:8:8', 'count': 62388}, {'key': '13:4:3', 'count': 62388}, {'key': '13:3:10', 'count': 60132}]`。
- top residues: `[{'key': '13:7', 'count': 144036}, {'key': '13:5', 'count': 143796}, {'key': '13:1', 'count': 137312}, {'key': '13:11', 'count': 136712}, {'key': '13:8', 'count': 127068}]`。
- top column residues: `[{'key': '13:4', 'count': 144636}, {'key': '13:7', 'count': 142596}, {'key': '13:10', 'count': 142596}, {'key': '13:2', 'count': 141132}, {'key': '13:9', 'count': 141132}]`。

### P=43 top=0 h=805 zeta=0.324739

- `phase_count_by_holes={6: 8, 7: 156, 8: 394, 9: 441, 10: 95}`。
- `max_dp_state_count=1024`。
- `distinct_payment_signature_count=6200`。
- `payment_signature_l2_energy=0.000649608`。
- `inverse_l2_payment_signature_support=1539.39`。
- top payment signatures: `[{'key': '13:5:1', 'count': 11760408}, {'key': '13:7:3', 'count': 11755368}, {'key': '13:0:1', 'count': 11450880}, {'key': '13:12:3', 'count': 11450160}, {'key': '13:2:2', 'count': 11323512}]`。
- top residues: `[{'key': '13:5', 'count': 67650948}, {'key': '13:7', 'count': 66902244}, {'key': '13:0', 'count': 64373724}, {'key': '13:12', 'count': 64268148}, {'key': '13:1', 'count': 62402254}]`。
- top column residues: `[{'key': '13:1', 'count': 76637856}, {'key': '13:3', 'count': 76618776}, {'key': '13:2', 'count': 72019560}, {'key': '13:7', 'count': 59024128}, {'key': '13:12', 'count': 57417792}]`。

### P=47 top=0 h=665 zeta=0.357868

- `phase_count_by_holes={7: 32, 8: 201, 9: 397, 10: 392, 11: 112, 12: 8}`。
- `max_dp_state_count=4096`。
- `distinct_payment_signature_count=8049`。
- `payment_signature_l2_energy=0.00074466`。
- `inverse_l2_payment_signature_support=1342.9`。
- top payment signatures: `[{'key': '13:4:4', 'count': 682835712}, {'key': '13:8:4', 'count': 681090552}, {'key': '13:0:5', 'count': 618189720}, {'key': '13:12:3', 'count': 618149400}, {'key': '13:12:12', 'count': 406006896}]`。
- top residues: `[{'key': '13:0', 'count': 2527881096}, {'key': '13:12', 'count': 2523805032}, {'key': '13:4', 'count': 2427860664}, {'key': '13:8', 'count': 2425539504}, {'key': '13:3', 'count': 1916205552}]`。
- top column residues: `[{'key': '13:4', 'count': 3604934544}, {'key': '13:5', 'count': 3019072104}, {'key': '13:3', 'count': 3017207664}, {'key': '13:6', 'count': 1820077128}, {'key': '13:2', 'count': 1790617368}]`。

## 7. 当前硬点

ActualPaymentSelection 的构造部分已经完成。剩余不是数据问题，而是终端结构引理：

```text
A. positive-limsup finite signature -> legal column/tail PDEC row；
B. all finite signatures vanish -> CleanKLS/DLS admission + large-sieve close。
```
