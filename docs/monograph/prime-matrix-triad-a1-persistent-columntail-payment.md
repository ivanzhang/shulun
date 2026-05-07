# Triad-A1 PersistentCap ColumnTail 支付审计

**状态：** `persistent_caps_columntail_payment_materialized`

PersistentCap 的质量已经被拆成 column-tail 支付账本。每个低洞完成都必须由某个高素数 residue 支付；因此持久分支只能二分为固定 tail/column residue 过载的 PDEC，或支付分散的 CleanKLS/DLS。

## 1. 结构语义

对每个 `PersistentCap`，低模骨架留下的洞必须由不在 `Q` 中的高素数 residue 支付。
设 cap 内总完成质量为 `M_C`，低洞需求为：

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|。
```

每个完成态至少支付这些洞；于是无需猜全局常数，直接得到结构二分：

```text
某个 tail/column residue 持久过载 => TailAnchor / ColumnCRT displacement PDEC；
所有 residue 都分散支付           => CleanKLS / DLS 型大筛入口。
```

本文登记的是这套二分的机器可读输入，不声称已完成 `U_CRT<L_PDEC`。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `persistent_columntail_payment_script` | `7bd96352cd76d525ee24d1706aea261fb7404077cda0b4788091f7da102f1c1e` |
| `dualcap_json` | `b6bf0fc2a4305656fa7aef8cac33aa9b7dd1867617611fe7b96a23e8ba251c53` |
| `multiplicity_cap_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |

## 3. 汇总

- `persistent_cap_count=68`。
- `unique_phase_signature_count=1915`。
- `all_intersections_recomputed=True`。
- `all_phase_m_counts_match=True`。
- `route_counts={'ColumnTailPigeonholeRowOrDistributedCleanKLS': 68}`。

## 4. P 级有效支撑

`effective support = total_hole_demand / max_single_bucket_payment`。它不是固定阈值，而是本层实际需要的分散桶数下界。

| P | caps | min eff prime | min eff residue | min eff column residue | max residue share | max colres share |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 8 | 1 | 7 | 9.33333 | 0.142857 | 0.107143 |
| 19 | 12 | 1.85714 | 14.8571 | 9.28571 | 0.0673077 | 0.107692 |
| 23 | 12 | 2.7234 | 24.7742 | 21.7872 | 0.0403646 | 0.0458984 |
| 29 | 12 | 3.49736 | 28.8469 | 21.5802 | 0.0346657 | 0.0463389 |
| 31 | 12 | 3.35148 | 22.0111 | 12.3753 | 0.0454317 | 0.080806 |
| 37 | 12 | 3.62441 | 28.3519 | 20.5831 | 0.0352711 | 0.0485835 |

## 5. Cap 明细

| P | alpha | h | dir | mass | demand | cover/demand | max prime/demand | max residue/demand | max colres/demand | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | 0 | 374 | 0 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0 | 1936 | 0 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0 | 374 | 0 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0 | 1936 | 0 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0.5 | 1001 | 0.25 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0.5 | 1309 | 0.75 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0.5 | 1001 | 0.25 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 17 | 0.5 | 1309 | 0.75 | 28 | 28 | 1 | 1 | 0.142857 | 0.107143 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0 | 847 | 0.25 | 482 | 732 | 1.01093 | 0.527322 | 0.0560109 | 0.079235 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0 | 1463 | 0.75 | 482 | 732 | 1.01093 | 0.527322 | 0.057377 | 0.079235 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0 | 847 | 0.25 | 482 | 732 | 1.01093 | 0.527322 | 0.0560109 | 0.079235 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0 | 1463 | 0.75 | 482 | 732 | 1.01093 | 0.527322 | 0.057377 | 0.079235 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.5 | 847 | 0.25 | 442 | 652 | 1.01227 | 0.530675 | 0.0613497 | 0.0889571 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.5 | 1463 | 0.75 | 442 | 652 | 1.01227 | 0.530675 | 0.0613497 | 0.0889571 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.5 | 847 | 0.25 | 442 | 652 | 1.01227 | 0.530675 | 0.0613497 | 0.0889571 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.5 | 1463 | 0.75 | 442 | 652 | 1.01227 | 0.530675 | 0.0613497 | 0.0889571 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.9 | 1265 | 0.25 | 376 | 520 | 1.01538 | 0.538462 | 0.0673077 | 0.107692 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.9 | 1045 | 0.75 | 376 | 520 | 1.01538 | 0.538462 | 0.0673077 | 0.107692 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.9 | 1265 | 0.25 | 376 | 520 | 1.01538 | 0.538462 | 0.0673077 | 0.107692 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 19 | 0.9 | 1045 | 0.75 | 376 | 520 | 1.01538 | 0.538462 | 0.0673077 | 0.107692 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0 | 1045 | 0.25 | 3210 | 7422 | 1.0194 | 0.361358 | 0.0374562 | 0.0420372 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0 | 1045 | 0.25 | 3210 | 7422 | 1.0194 | 0.361358 | 0.0374562 | 0.0420372 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0 | 1265 | 0.75 | 3192 | 7368 | 1.01954 | 0.361564 | 0.0377307 | 0.0423453 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0 | 1265 | 0.75 | 3192 | 7368 | 1.01954 | 0.361564 | 0.0377307 | 0.0423453 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.5 | 1045 | 0.25 | 3120 | 7152 | 1.02013 | 0.362416 | 0.038311 | 0.0427852 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.5 | 1265 | 0.75 | 3120 | 7152 | 1.02013 | 0.362416 | 0.038311 | 0.0427852 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.5 | 1045 | 0.25 | 3120 | 7152 | 1.02013 | 0.362416 | 0.038311 | 0.0427852 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.5 | 1265 | 0.75 | 3120 | 7152 | 1.02013 | 0.362416 | 0.038311 | 0.0427852 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.9 | 1045 | 0.25 | 2784 | 6144 | 1.02344 | 0.367188 | 0.0403646 | 0.0458984 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.9 | 1265 | 0.75 | 2784 | 6144 | 1.02344 | 0.367188 | 0.0403646 | 0.0458984 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.9 | 1045 | 0.25 | 2784 | 6144 | 1.02344 | 0.367188 | 0.0403646 | 0.0458984 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 23 | 0.9 | 1265 | 0.75 | 2784 | 6144 | 1.02344 | 0.367188 | 0.0403646 | 0.0458984 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0 | 715 | 0.25 | 6200 | 21752 | 1.0149 | 0.278779 | 0.0291467 | 0.0385252 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0 | 715 | 0.25 | 6200 | 21752 | 1.0149 | 0.278779 | 0.0291467 | 0.0385252 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0 | 1595 | 0.75 | 6152 | 21560 | 1.01503 | 0.279035 | 0.029128 | 0.0388683 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0 | 1595 | 0.75 | 6152 | 21560 | 1.01503 | 0.279035 | 0.029128 | 0.0388683 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.5 | 1295 | 0.25 | 5384 | 18464 | 1.01755 | 0.282929 | 0.0314125 | 0.0369367 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.5 | 1015 | 0.75 | 5384 | 18464 | 1.01755 | 0.282929 | 0.0314125 | 0.0369367 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.5 | 715 | 0.25 | 4808 | 16976 | 1.01484 | 0.282281 | 0.0345193 | 0.0458294 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.5 | 1595 | 0.75 | 4808 | 16976 | 1.01484 | 0.282281 | 0.0345193 | 0.0458294 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.9 | 1295 | 0.25 | 4760 | 15920 | 1.02035 | 0.28593 | 0.0341709 | 0.0364322 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.9 | 1015 | 0.75 | 4760 | 15920 | 1.02035 | 0.28593 | 0.0341709 | 0.0364322 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.9 | 1155 | 0 | 3208 | 11308 | 1.01433 | 0.27768 | 0.0346657 | 0.0463389 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 29 | 0.9 | 1155 | 0.5 | 3208 | 11308 | 1.01433 | 0.27768 | 0.0346657 | 0.0463389 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0 | 1085 | 0.75 | 136400 | 598424 | 1.02778 | 0.289467 | 0.0355601 | 0.0501183 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0 | 1225 | 0.25 | 136376 | 598160 | 1.02779 | 0.289314 | 0.0355758 | 0.0500602 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.5 | 1225 | 0.25 | 123896 | 534608 | 1.02921 | 0.287164 | 0.0369766 | 0.0498608 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.5 | 1085 | 0.75 | 123896 | 534608 | 1.02921 | 0.287164 | 0.0369766 | 0.0498608 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0 | 1287 | 0.25 | 119144 | 530288 | 1.02709 | 0.294934 | 0.0376626 | 0.0533446 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0 | 1023 | 0.75 | 118928 | 529232 | 1.02715 | 0.29516 | 0.0376924 | 0.0534057 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.9 | 1225 | 0.25 | 107624 | 452240 | 1.03156 | 0.283849 | 0.039678 | 0.0478507 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.9 | 1085 | 0.75 | 107624 | 452240 | 1.03156 | 0.283849 | 0.039678 | 0.0478507 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.5 | 1287 | 0.25 | 87992 | 386144 | 1.02913 | 0.298376 | 0.0445119 | 0.0561034 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.5 | 1023 | 0.75 | 87992 | 386144 | 1.02913 | 0.298376 | 0.0445119 | 0.0561034 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.9 | 1155 | 0 | 75028 | 334480 | 1.02485 | 0.282731 | 0.0454317 | 0.080806 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 31 | 0.9 | 1155 | 0.5 | 75028 | 334480 | 1.02485 | 0.282731 | 0.0454317 | 0.080806 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0 | 1015 | 0.25 | 931124 | 5103864 | 1.03126 | 0.274797 | 0.0283103 | 0.028395 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0 | 1015 | 0.25 | 931124 | 5103864 | 1.03126 | 0.274797 | 0.0283103 | 0.028395 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0 | 1295 | 0.75 | 930836 | 5101800 | 1.03127 | 0.274772 | 0.02827 | 0.0284064 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0 | 1295 | 0.75 | 930836 | 5101800 | 1.03127 | 0.274772 | 0.02827 | 0.0284064 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.5 | 1015 | 0.25 | 888356 | 4828728 | 1.03253 | 0.275907 | 0.0289542 | 0.0290735 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.5 | 1295 | 0.75 | 888356 | 4828728 | 1.03253 | 0.275907 | 0.0289542 | 0.0290735 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.5 | 1015 | 0.25 | 888356 | 4828728 | 1.03253 | 0.275907 | 0.0289542 | 0.0290735 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.5 | 1295 | 0.75 | 888356 | 4828728 | 1.03253 | 0.275907 | 0.0289542 | 0.0290735 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.9 | 1015 | 0.25 | 619304 | 3331116 | 1.03423 | 0.275127 | 0.0352711 | 0.0364238 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.9 | 1295 | 0.75 | 619304 | 3331116 | 1.03423 | 0.275127 | 0.0352711 | 0.0364238 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.9 | 1155 | 0 | 492322 | 2724132 | 1.02928 | 0.270708 | 0.0345314 | 0.0485835 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |
| 37 | 0.9 | 1155 | 0.5 | 492322 | 2724132 | 1.02928 | 0.270708 | 0.0345314 | 0.0485835 | `ColumnTailPigeonholeRowOrDistributedCleanKLS` |

## 6. Top 支付签名

### P=17 alpha=0 h=374 dir=0 source=top_by_mass

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0 h=1936 dir=0 source=top_by_mass

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0 h=374 dir=0 source=top_by_size

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0 h=1936 dir=0 source=top_by_size

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0.5 h=1001 dir=0.25 source=top_by_mass

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0.5 h=1309 dir=0.75 source=top_by_mass

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0.5 h=1001 dir=0.25 source=top_by_size

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=17 alpha=0.5 h=1309 dir=0.75 source=top_by_size

- `phase_count_by_holes={1: 28}`。
- `prime_pigeonhole_floor=28`。
- `residue_pigeonhole_floor=2.15385`。
- `max_prime_cover_over_floor=1`。
- `max_residue_cover_over_floor=1.85714`。
- `max_column_residue_cover_over_floor=1.39286`。
- top prime cover: `[{'key': '13', 'count': 28}]`。
- top residue cover: `[{'key': '13:6', 'count': 4}, {'key': '13:2', 'count': 3}, {'key': '13:4', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:8', 'count': 3}]`。
- top column-residue cover: `[{'key': '13:7', 'count': 3}, {'key': '13:8', 'count': 3}, {'key': '13:9', 'count': 3}, {'key': '13:10', 'count': 3}, {'key': '13:6', 'count': 2}]`。

### P=19 alpha=0 h=847 dir=0.25 source=top_by_mass

- `phase_count_by_holes={1: 8, 2: 125}`。
- `prime_pigeonhole_floor=366`。
- `residue_pigeonhole_floor=24.4`。
- `max_prime_cover_over_floor=1.05464`。
- `max_residue_cover_over_floor=1.68033`。
- `max_column_residue_cover_over_floor=2.37705`。
- top prime cover: `[{'key': '13', 'count': 386}, {'key': '17', 'count': 354}]`。
- top residue cover: `[{'key': '17:8', 'count': 41}, {'key': '13:7', 'count': 40}, {'key': '13:5', 'count': 39}, {'key': '13:8', 'count': 38}, {'key': '13:4', 'count': 38}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 58}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 50}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0 h=1463 dir=0.75 source=top_by_mass

- `phase_count_by_holes={1: 8, 2: 125}`。
- `prime_pigeonhole_floor=366`。
- `residue_pigeonhole_floor=24.4`。
- `max_prime_cover_over_floor=1.05464`。
- `max_residue_cover_over_floor=1.72131`。
- `max_column_residue_cover_over_floor=2.37705`。
- top prime cover: `[{'key': '13', 'count': 386}, {'key': '17', 'count': 354}]`。
- top residue cover: `[{'key': '17:8', 'count': 42}, {'key': '13:7', 'count': 40}, {'key': '13:5', 'count': 39}, {'key': '13:8', 'count': 38}, {'key': '13:4', 'count': 38}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 58}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 50}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0 h=847 dir=0.25 source=top_by_size

- `phase_count_by_holes={1: 8, 2: 125}`。
- `prime_pigeonhole_floor=366`。
- `residue_pigeonhole_floor=24.4`。
- `max_prime_cover_over_floor=1.05464`。
- `max_residue_cover_over_floor=1.68033`。
- `max_column_residue_cover_over_floor=2.37705`。
- top prime cover: `[{'key': '13', 'count': 386}, {'key': '17', 'count': 354}]`。
- top residue cover: `[{'key': '17:8', 'count': 41}, {'key': '13:7', 'count': 40}, {'key': '13:5', 'count': 39}, {'key': '13:8', 'count': 38}, {'key': '13:4', 'count': 38}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 58}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 50}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0 h=1463 dir=0.75 source=top_by_size

- `phase_count_by_holes={1: 8, 2: 125}`。
- `prime_pigeonhole_floor=366`。
- `residue_pigeonhole_floor=24.4`。
- `max_prime_cover_over_floor=1.05464`。
- `max_residue_cover_over_floor=1.72131`。
- `max_column_residue_cover_over_floor=2.37705`。
- top prime cover: `[{'key': '13', 'count': 386}, {'key': '17', 'count': 354}]`。
- top residue cover: `[{'key': '17:8', 'count': 42}, {'key': '13:7', 'count': 40}, {'key': '13:5', 'count': 39}, {'key': '13:8', 'count': 38}, {'key': '13:4', 'count': 38}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 58}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 50}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0.5 h=847 dir=0.25 source=top_by_mass

- `phase_count_by_holes={1: 8, 2: 105}`。
- `prime_pigeonhole_floor=326`。
- `residue_pigeonhole_floor=21.7333`。
- `max_prime_cover_over_floor=1.06135`。
- `max_residue_cover_over_floor=1.84049`。
- `max_column_residue_cover_over_floor=2.66871`。
- top prime cover: `[{'key': '13', 'count': 346}, {'key': '17', 'count': 314}]`。
- top residue cover: `[{'key': '17:8', 'count': 40}, {'key': '13:7', 'count': 37}, {'key': '13:8', 'count': 35}, {'key': '13:4', 'count': 34}, {'key': '13:5', 'count': 34}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 48}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0.5 h=1463 dir=0.75 source=top_by_mass

- `phase_count_by_holes={1: 8, 2: 105}`。
- `prime_pigeonhole_floor=326`。
- `residue_pigeonhole_floor=21.7333`。
- `max_prime_cover_over_floor=1.06135`。
- `max_residue_cover_over_floor=1.84049`。
- `max_column_residue_cover_over_floor=2.66871`。
- top prime cover: `[{'key': '13', 'count': 346}, {'key': '17', 'count': 314}]`。
- top residue cover: `[{'key': '17:8', 'count': 40}, {'key': '13:7', 'count': 37}, {'key': '13:8', 'count': 35}, {'key': '13:4', 'count': 34}, {'key': '13:5', 'count': 34}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 48}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0.5 h=847 dir=0.25 source=top_by_size

- `phase_count_by_holes={1: 8, 2: 105}`。
- `prime_pigeonhole_floor=326`。
- `residue_pigeonhole_floor=21.7333`。
- `max_prime_cover_over_floor=1.06135`。
- `max_residue_cover_over_floor=1.84049`。
- `max_column_residue_cover_over_floor=2.66871`。
- top prime cover: `[{'key': '13', 'count': 346}, {'key': '17', 'count': 314}]`。
- top residue cover: `[{'key': '17:8', 'count': 40}, {'key': '13:7', 'count': 37}, {'key': '13:8', 'count': 35}, {'key': '13:4', 'count': 34}, {'key': '13:5', 'count': 34}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 48}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0.5 h=1463 dir=0.75 source=top_by_size

- `phase_count_by_holes={1: 8, 2: 105}`。
- `prime_pigeonhole_floor=326`。
- `residue_pigeonhole_floor=21.7333`。
- `max_prime_cover_over_floor=1.06135`。
- `max_residue_cover_over_floor=1.84049`。
- `max_column_residue_cover_over_floor=2.66871`。
- top prime cover: `[{'key': '13', 'count': 346}, {'key': '17', 'count': 314}]`。
- top residue cover: `[{'key': '17:8', 'count': 40}, {'key': '13:7', 'count': 37}, {'key': '13:8', 'count': 35}, {'key': '13:4', 'count': 34}, {'key': '13:5', 'count': 34}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 58}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 50}, {'key': '17:10', 'count': 48}, {'key': '13:8', 'count': 36}]`。

### P=19 alpha=0.9 h=1265 dir=0.25 source=top_by_mass

- `phase_count_by_holes={1: 8, 2: 72}`。
- `prime_pigeonhole_floor=260`。
- `residue_pigeonhole_floor=17.3333`。
- `max_prime_cover_over_floor=1.07692`。
- `max_residue_cover_over_floor=2.01923`。
- `max_column_residue_cover_over_floor=3.23077`。
- top prime cover: `[{'key': '13', 'count': 280}, {'key': '17', 'count': 248}]`。
- top residue cover: `[{'key': '17:8', 'count': 35}, {'key': '13:4', 'count': 31}, {'key': '13:5', 'count': 30}, {'key': '13:11', 'count': 28}, {'key': '13:8', 'count': 28}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 56}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 48}, {'key': '17:10', 'count': 48}, {'key': '13:7', 'count': 30}]`。

### P=19 alpha=0.9 h=1045 dir=0.75 source=top_by_mass

- `phase_count_by_holes={1: 8, 2: 72}`。
- `prime_pigeonhole_floor=260`。
- `residue_pigeonhole_floor=17.3333`。
- `max_prime_cover_over_floor=1.07692`。
- `max_residue_cover_over_floor=2.01923`。
- `max_column_residue_cover_over_floor=3.23077`。
- top prime cover: `[{'key': '13', 'count': 280}, {'key': '17', 'count': 248}]`。
- top residue cover: `[{'key': '17:8', 'count': 35}, {'key': '13:4', 'count': 31}, {'key': '13:5', 'count': 30}, {'key': '13:11', 'count': 28}, {'key': '13:8', 'count': 28}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 56}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 48}, {'key': '17:10', 'count': 48}, {'key': '13:7', 'count': 30}]`。

### P=19 alpha=0.9 h=1265 dir=0.25 source=top_by_size

- `phase_count_by_holes={1: 8, 2: 72}`。
- `prime_pigeonhole_floor=260`。
- `residue_pigeonhole_floor=17.3333`。
- `max_prime_cover_over_floor=1.07692`。
- `max_residue_cover_over_floor=2.01923`。
- `max_column_residue_cover_over_floor=3.23077`。
- top prime cover: `[{'key': '13', 'count': 280}, {'key': '17', 'count': 248}]`。
- top residue cover: `[{'key': '17:8', 'count': 35}, {'key': '13:4', 'count': 31}, {'key': '13:5', 'count': 30}, {'key': '13:11', 'count': 28}, {'key': '13:8', 'count': 28}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 56}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 48}, {'key': '17:10', 'count': 48}, {'key': '13:7', 'count': 30}]`。

### P=19 alpha=0.9 h=1045 dir=0.75 source=top_by_size

- `phase_count_by_holes={1: 8, 2: 72}`。
- `prime_pigeonhole_floor=260`。
- `residue_pigeonhole_floor=17.3333`。
- `max_prime_cover_over_floor=1.07692`。
- `max_residue_cover_over_floor=2.01923`。
- `max_column_residue_cover_over_floor=3.23077`。
- top prime cover: `[{'key': '13', 'count': 280}, {'key': '17', 'count': 248}]`。
- top residue cover: `[{'key': '17:8', 'count': 35}, {'key': '13:4', 'count': 31}, {'key': '13:5', 'count': 30}, {'key': '13:11', 'count': 28}, {'key': '13:8', 'count': 28}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 56}, {'key': '13:10', 'count': 56}, {'key': '17:9', 'count': 48}, {'key': '17:10', 'count': 48}, {'key': '13:7', 'count': 30}]`。

### P=23 alpha=0 h=1045 dir=0.25 source=top_by_mass

- `phase_count_by_holes={2: 24, 3: 167}`。
- `prime_pigeonhole_floor=2474`。
- `residue_pigeonhole_floor=151.469`。
- `max_prime_cover_over_floor=1.08407`。
- `max_residue_cover_over_floor=1.83535`。
- `max_column_residue_cover_over_floor=2.05982`。
- top prime cover: `[{'key': '13', 'count': 2682}, {'key': '17', 'count': 2490}, {'key': '19', 'count': 2394}]`。
- top residue cover: `[{'key': '13:12', 'count': 278}, {'key': '13:0', 'count': 276}, {'key': '13:10', 'count': 259}, {'key': '13:4', 'count': 259}, {'key': '13:8', 'count': 257}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 312}, {'key': '13:1', 'count': 306}, {'key': '13:5', 'count': 242}, {'key': '13:2', 'count': 226}, {'key': '13:8', 'count': 226}]`。

### P=23 alpha=0 h=1045 dir=0.25 source=top_by_size

- `phase_count_by_holes={2: 24, 3: 167}`。
- `prime_pigeonhole_floor=2474`。
- `residue_pigeonhole_floor=151.469`。
- `max_prime_cover_over_floor=1.08407`。
- `max_residue_cover_over_floor=1.83535`。
- `max_column_residue_cover_over_floor=2.05982`。
- top prime cover: `[{'key': '13', 'count': 2682}, {'key': '17', 'count': 2490}, {'key': '19', 'count': 2394}]`。
- top residue cover: `[{'key': '13:12', 'count': 278}, {'key': '13:0', 'count': 276}, {'key': '13:10', 'count': 259}, {'key': '13:4', 'count': 259}, {'key': '13:8', 'count': 257}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 312}, {'key': '13:1', 'count': 306}, {'key': '13:5', 'count': 242}, {'key': '13:2', 'count': 226}, {'key': '13:8', 'count': 226}]`。

### P=23 alpha=0 h=1265 dir=0.75 source=top_by_mass

- `phase_count_by_holes={2: 24, 3: 164}`。
- `prime_pigeonhole_floor=2456`。
- `residue_pigeonhole_floor=150.367`。
- `max_prime_cover_over_floor=1.08469`。
- `max_residue_cover_over_floor=1.84881`。
- `max_column_residue_cover_over_floor=2.07492`。
- top prime cover: `[{'key': '13', 'count': 2664}, {'key': '17', 'count': 2472}, {'key': '19', 'count': 2376}]`。
- top residue cover: `[{'key': '13:12', 'count': 278}, {'key': '13:0', 'count': 276}, {'key': '13:10', 'count': 257}, {'key': '13:4', 'count': 257}, {'key': '13:2', 'count': 255}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 312}, {'key': '13:1', 'count': 306}, {'key': '13:5', 'count': 238}, {'key': '13:2', 'count': 226}, {'key': '13:8', 'count': 226}]`。

### P=23 alpha=0 h=1265 dir=0.75 source=top_by_size

- `phase_count_by_holes={2: 24, 3: 164}`。
- `prime_pigeonhole_floor=2456`。
- `residue_pigeonhole_floor=150.367`。
- `max_prime_cover_over_floor=1.08469`。
- `max_residue_cover_over_floor=1.84881`。
- `max_column_residue_cover_over_floor=2.07492`。
- top prime cover: `[{'key': '13', 'count': 2664}, {'key': '17', 'count': 2472}, {'key': '19', 'count': 2376}]`。
- top residue cover: `[{'key': '13:12', 'count': 278}, {'key': '13:0', 'count': 276}, {'key': '13:10', 'count': 257}, {'key': '13:4', 'count': 257}, {'key': '13:2', 'count': 255}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 312}, {'key': '13:1', 'count': 306}, {'key': '13:5', 'count': 238}, {'key': '13:2', 'count': 226}, {'key': '13:8', 'count': 226}]`。

### P=23 alpha=0.5 h=1045 dir=0.25 source=top_by_mass

- `phase_count_by_holes={2: 24, 3: 152}`。
- `prime_pigeonhole_floor=2384`。
- `residue_pigeonhole_floor=145.959`。
- `max_prime_cover_over_floor=1.08725`。
- `max_residue_cover_over_floor=1.87724`。
- `max_column_residue_cover_over_floor=2.09648`。
- top prime cover: `[{'key': '13', 'count': 2592}, {'key': '17', 'count': 2400}, {'key': '19', 'count': 2304}]`。
- top residue cover: `[{'key': '13:12', 'count': 274}, {'key': '13:0', 'count': 272}, {'key': '13:4', 'count': 249}, {'key': '13:10', 'count': 247}, {'key': '13:8', 'count': 247}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 306}, {'key': '13:9', 'count': 294}, {'key': '13:2', 'count': 226}, {'key': '13:5', 'count': 226}, {'key': '13:8', 'count': 220}]`。

### P=23 alpha=0.5 h=1265 dir=0.75 source=top_by_mass

- `phase_count_by_holes={2: 24, 3: 152}`。
- `prime_pigeonhole_floor=2384`。
- `residue_pigeonhole_floor=145.959`。
- `max_prime_cover_over_floor=1.08725`。
- `max_residue_cover_over_floor=1.87724`。
- `max_column_residue_cover_over_floor=2.09648`。
- top prime cover: `[{'key': '13', 'count': 2592}, {'key': '17', 'count': 2400}, {'key': '19', 'count': 2304}]`。
- top residue cover: `[{'key': '13:12', 'count': 274}, {'key': '13:0', 'count': 272}, {'key': '13:4', 'count': 249}, {'key': '13:10', 'count': 247}, {'key': '13:8', 'count': 247}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 306}, {'key': '13:9', 'count': 294}, {'key': '13:2', 'count': 226}, {'key': '13:5', 'count': 226}, {'key': '13:8', 'count': 220}]`。

### P=23 alpha=0.5 h=1045 dir=0.25 source=top_by_size

- `phase_count_by_holes={2: 24, 3: 152}`。
- `prime_pigeonhole_floor=2384`。
- `residue_pigeonhole_floor=145.959`。
- `max_prime_cover_over_floor=1.08725`。
- `max_residue_cover_over_floor=1.87724`。
- `max_column_residue_cover_over_floor=2.09648`。
- top prime cover: `[{'key': '13', 'count': 2592}, {'key': '17', 'count': 2400}, {'key': '19', 'count': 2304}]`。
- top residue cover: `[{'key': '13:12', 'count': 274}, {'key': '13:0', 'count': 272}, {'key': '13:4', 'count': 249}, {'key': '13:10', 'count': 247}, {'key': '13:8', 'count': 247}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 306}, {'key': '13:9', 'count': 294}, {'key': '13:2', 'count': 226}, {'key': '13:5', 'count': 226}, {'key': '13:8', 'count': 220}]`。

### P=23 alpha=0.5 h=1265 dir=0.75 source=top_by_size

- `phase_count_by_holes={2: 24, 3: 152}`。
- `prime_pigeonhole_floor=2384`。
- `residue_pigeonhole_floor=145.959`。
- `max_prime_cover_over_floor=1.08725`。
- `max_residue_cover_over_floor=1.87724`。
- `max_column_residue_cover_over_floor=2.09648`。
- top prime cover: `[{'key': '13', 'count': 2592}, {'key': '17', 'count': 2400}, {'key': '19', 'count': 2304}]`。
- top residue cover: `[{'key': '13:12', 'count': 274}, {'key': '13:0', 'count': 272}, {'key': '13:4', 'count': 249}, {'key': '13:10', 'count': 247}, {'key': '13:8', 'count': 247}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 306}, {'key': '13:9', 'count': 294}, {'key': '13:2', 'count': 226}, {'key': '13:5', 'count': 226}, {'key': '13:8', 'count': 220}]`。

### P=23 alpha=0.9 h=1045 dir=0.25 source=top_by_mass

- `phase_count_by_holes={2: 24, 3: 96}`。
- `prime_pigeonhole_floor=2048`。
- `residue_pigeonhole_floor=125.388`。
- `max_prime_cover_over_floor=1.10156`。
- `max_residue_cover_over_floor=1.97786`。
- `max_column_residue_cover_over_floor=2.24902`。
- top prime cover: `[{'key': '13', 'count': 2256}, {'key': '17', 'count': 2064}, {'key': '19', 'count': 1968}]`。
- top residue cover: `[{'key': '13:0', 'count': 248}, {'key': '13:12', 'count': 244}, {'key': '13:8', 'count': 223}, {'key': '13:2', 'count': 221}, {'key': '13:10', 'count': 219}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 282}, {'key': '13:9', 'count': 270}, {'key': '13:2', 'count': 208}, {'key': '13:12', 'count': 184}, {'key': '13:11', 'count': 184}]`。

### P=23 alpha=0.9 h=1265 dir=0.75 source=top_by_mass

- `phase_count_by_holes={2: 24, 3: 96}`。
- `prime_pigeonhole_floor=2048`。
- `residue_pigeonhole_floor=125.388`。
- `max_prime_cover_over_floor=1.10156`。
- `max_residue_cover_over_floor=1.97786`。
- `max_column_residue_cover_over_floor=2.24902`。
- top prime cover: `[{'key': '13', 'count': 2256}, {'key': '17', 'count': 2064}, {'key': '19', 'count': 1968}]`。
- top residue cover: `[{'key': '13:0', 'count': 248}, {'key': '13:12', 'count': 244}, {'key': '13:8', 'count': 223}, {'key': '13:2', 'count': 221}, {'key': '13:10', 'count': 219}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 282}, {'key': '13:9', 'count': 270}, {'key': '13:2', 'count': 208}, {'key': '13:12', 'count': 184}, {'key': '13:11', 'count': 184}]`。

### P=23 alpha=0.9 h=1045 dir=0.25 source=top_by_size

- `phase_count_by_holes={2: 24, 3: 96}`。
- `prime_pigeonhole_floor=2048`。
- `residue_pigeonhole_floor=125.388`。
- `max_prime_cover_over_floor=1.10156`。
- `max_residue_cover_over_floor=1.97786`。
- `max_column_residue_cover_over_floor=2.24902`。
- top prime cover: `[{'key': '13', 'count': 2256}, {'key': '17', 'count': 2064}, {'key': '19', 'count': 1968}]`。
- top residue cover: `[{'key': '13:0', 'count': 248}, {'key': '13:12', 'count': 244}, {'key': '13:8', 'count': 223}, {'key': '13:2', 'count': 221}, {'key': '13:10', 'count': 219}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 282}, {'key': '13:9', 'count': 270}, {'key': '13:2', 'count': 208}, {'key': '13:12', 'count': 184}, {'key': '13:11', 'count': 184}]`。

### P=23 alpha=0.9 h=1265 dir=0.75 source=top_by_size

- `phase_count_by_holes={2: 24, 3: 96}`。
- `prime_pigeonhole_floor=2048`。
- `residue_pigeonhole_floor=125.388`。
- `max_prime_cover_over_floor=1.10156`。
- `max_residue_cover_over_floor=1.97786`。
- `max_column_residue_cover_over_floor=2.24902`。
- top prime cover: `[{'key': '13', 'count': 2256}, {'key': '17', 'count': 2064}, {'key': '19', 'count': 1968}]`。
- top residue cover: `[{'key': '13:0', 'count': 248}, {'key': '13:12', 'count': 244}, {'key': '13:8', 'count': 223}, {'key': '13:2', 'count': 221}, {'key': '13:10', 'count': 219}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 282}, {'key': '13:9', 'count': 270}, {'key': '13:2', 'count': 208}, {'key': '13:12', 'count': 184}, {'key': '13:11', 'count': 184}]`。

### P=29 alpha=0 h=715 dir=0.25 source=top_by_mass

- `phase_count_by_holes={3: 8, 4: 113, 5: 20}`。
- `prime_pigeonhole_floor=5438`。
- `residue_pigeonhole_floor=302.111`。
- `max_prime_cover_over_floor=1.11512`。
- `max_residue_cover_over_floor=2.09857`。
- `max_column_residue_cover_over_floor=2.77381`。
- top prime cover: `[{'key': '13', 'count': 6064}, {'key': '17', 'count': 5476}, {'key': '19', 'count': 5372}, {'key': '23', 'count': 5164}]`。
- top residue cover: `[{'key': '13:2', 'count': 634}, {'key': '13:10', 'count': 634}, {'key': '13:12', 'count': 576}, {'key': '13:0', 'count': 570}, {'key': '13:1', 'count': 546}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 838}, {'key': '13:1', 'count': 838}, {'key': '13:3', 'count': 486}, {'key': '13:0', 'count': 486}, {'key': '13:11', 'count': 482}]`。

### P=29 alpha=0 h=715 dir=0.25 source=top_by_size

- `phase_count_by_holes={3: 8, 4: 113, 5: 20}`。
- `prime_pigeonhole_floor=5438`。
- `residue_pigeonhole_floor=302.111`。
- `max_prime_cover_over_floor=1.11512`。
- `max_residue_cover_over_floor=2.09857`。
- `max_column_residue_cover_over_floor=2.77381`。
- top prime cover: `[{'key': '13', 'count': 6064}, {'key': '17', 'count': 5476}, {'key': '19', 'count': 5372}, {'key': '23', 'count': 5164}]`。
- top residue cover: `[{'key': '13:2', 'count': 634}, {'key': '13:10', 'count': 634}, {'key': '13:12', 'count': 576}, {'key': '13:0', 'count': 570}, {'key': '13:1', 'count': 546}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 838}, {'key': '13:1', 'count': 838}, {'key': '13:3', 'count': 486}, {'key': '13:0', 'count': 486}, {'key': '13:11', 'count': 482}]`。

### P=29 alpha=0 h=1595 dir=0.75 source=top_by_mass

- `phase_count_by_holes={3: 8, 4: 111, 5: 20}`。
- `prime_pigeonhole_floor=5390`。
- `residue_pigeonhole_floor=299.444`。
- `max_prime_cover_over_floor=1.11614`。
- `max_residue_cover_over_floor=2.09722`。
- `max_column_residue_cover_over_floor=2.79852`。
- top prime cover: `[{'key': '13', 'count': 6016}, {'key': '17', 'count': 5428}, {'key': '19', 'count': 5324}, {'key': '23', 'count': 5116}]`。
- top residue cover: `[{'key': '13:10', 'count': 628}, {'key': '13:2', 'count': 622}, {'key': '13:12', 'count': 576}, {'key': '13:0', 'count': 570}, {'key': '13:11', 'count': 546}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 838}, {'key': '13:1', 'count': 832}, {'key': '13:3', 'count': 486}, {'key': '13:11', 'count': 482}, {'key': '13:0', 'count': 474}]`。

### P=29 alpha=0 h=1595 dir=0.75 source=top_by_size

- `phase_count_by_holes={3: 8, 4: 111, 5: 20}`。
- `prime_pigeonhole_floor=5390`。
- `residue_pigeonhole_floor=299.444`。
- `max_prime_cover_over_floor=1.11614`。
- `max_residue_cover_over_floor=2.09722`。
- `max_column_residue_cover_over_floor=2.79852`。
- top prime cover: `[{'key': '13', 'count': 6016}, {'key': '17', 'count': 5428}, {'key': '19', 'count': 5324}, {'key': '23', 'count': 5116}]`。
- top residue cover: `[{'key': '13:10', 'count': 628}, {'key': '13:2', 'count': 622}, {'key': '13:12', 'count': 576}, {'key': '13:0', 'count': 570}, {'key': '13:11', 'count': 546}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 838}, {'key': '13:1', 'count': 832}, {'key': '13:3', 'count': 486}, {'key': '13:11', 'count': 482}, {'key': '13:0', 'count': 474}]`。

### P=29 alpha=0.5 h=1295 dir=0.25 source=top_by_mass

- `phase_count_by_holes={3: 8, 4: 80, 5: 16}`。
- `prime_pigeonhole_floor=4616`。
- `residue_pigeonhole_floor=256.444`。
- `max_prime_cover_over_floor=1.13172`。
- `max_residue_cover_over_floor=2.2617`。
- `max_column_residue_cover_over_floor=2.65945`。
- top prime cover: `[{'key': '13', 'count': 5224}, {'key': '17', 'count': 4660}, {'key': '19', 'count': 4556}, {'key': '23', 'count': 4348}]`。
- top residue cover: `[{'key': '13:2', 'count': 580}, {'key': '13:10', 'count': 580}, {'key': '13:0', 'count': 492}, {'key': '13:12', 'count': 480}, {'key': '17:14', 'count': 478}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 682}, {'key': '13:1', 'count': 682}, {'key': '13:3', 'count': 456}, {'key': '13:0', 'count': 444}, {'key': '13:5', 'count': 404}]`。

### P=29 alpha=0.5 h=1015 dir=0.75 source=top_by_mass

- `phase_count_by_holes={3: 8, 4: 80, 5: 16}`。
- `prime_pigeonhole_floor=4616`。
- `residue_pigeonhole_floor=256.444`。
- `max_prime_cover_over_floor=1.13172`。
- `max_residue_cover_over_floor=2.2617`。
- `max_column_residue_cover_over_floor=2.65945`。
- top prime cover: `[{'key': '13', 'count': 5224}, {'key': '17', 'count': 4660}, {'key': '19', 'count': 4556}, {'key': '23', 'count': 4348}]`。
- top residue cover: `[{'key': '13:2', 'count': 580}, {'key': '13:10', 'count': 580}, {'key': '13:0', 'count': 492}, {'key': '13:12', 'count': 480}, {'key': '17:14', 'count': 478}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 682}, {'key': '13:1', 'count': 682}, {'key': '13:3', 'count': 456}, {'key': '13:0', 'count': 444}, {'key': '13:5', 'count': 404}]`。

### P=29 alpha=0.5 h=715 dir=0.25 source=top_by_size

- `phase_count_by_holes={3: 6, 4: 88, 5: 20}`。
- `prime_pigeonhole_floor=4244`。
- `residue_pigeonhole_floor=235.778`。
- `max_prime_cover_over_floor=1.12912`。
- `max_residue_cover_over_floor=2.48539`。
- `max_column_residue_cover_over_floor=3.29972`。
- top prime cover: `[{'key': '13', 'count': 4792}, {'key': '17', 'count': 4252}, {'key': '19', 'count': 4172}, {'key': '23', 'count': 4012}]`。
- top residue cover: `[{'key': '13:2', 'count': 586}, {'key': '13:12', 'count': 534}, {'key': '13:0', 'count': 528}, {'key': '13:1', 'count': 486}, {'key': '17:14', 'count': 476}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 778}, {'key': '13:2', 'count': 648}, {'key': '13:0', 'count': 474}, {'key': '13:5', 'count': 452}, {'key': '13:4', 'count': 434}]`。

### P=29 alpha=0.5 h=1595 dir=0.75 source=top_by_size

- `phase_count_by_holes={3: 6, 4: 88, 5: 20}`。
- `prime_pigeonhole_floor=4244`。
- `residue_pigeonhole_floor=235.778`。
- `max_prime_cover_over_floor=1.12912`。
- `max_residue_cover_over_floor=2.48539`。
- `max_column_residue_cover_over_floor=3.29972`。
- top prime cover: `[{'key': '13', 'count': 4792}, {'key': '17', 'count': 4252}, {'key': '19', 'count': 4172}, {'key': '23', 'count': 4012}]`。
- top residue cover: `[{'key': '13:2', 'count': 586}, {'key': '13:12', 'count': 534}, {'key': '13:0', 'count': 528}, {'key': '13:1', 'count': 486}, {'key': '17:14', 'count': 476}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 778}, {'key': '13:2', 'count': 648}, {'key': '13:0', 'count': 474}, {'key': '13:5', 'count': 452}, {'key': '13:4', 'count': 434}]`。

### P=29 alpha=0.9 h=1295 dir=0.25 source=top_by_mass

- `phase_count_by_holes={3: 8, 4: 56, 5: 8}`。
- `prime_pigeonhole_floor=3980`。
- `residue_pigeonhole_floor=221.111`。
- `max_prime_cover_over_floor=1.14372`。
- `max_residue_cover_over_floor=2.4603`。
- `max_column_residue_cover_over_floor=2.62312`。
- top prime cover: `[{'key': '13', 'count': 4552}, {'key': '17', 'count': 4036}, {'key': '19', 'count': 3932}, {'key': '23', 'count': 3724}]`。
- top residue cover: `[{'key': '13:2', 'count': 544}, {'key': '13:10', 'count': 544}, {'key': '19:13', 'count': 452}, {'key': '13:12', 'count': 438}, {'key': '13:0', 'count': 438}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 580}, {'key': '13:1', 'count': 574}, {'key': '13:3', 'count': 426}, {'key': '13:0', 'count': 408}, {'key': '13:11', 'count': 350}]`。

### P=29 alpha=0.9 h=1015 dir=0.75 source=top_by_mass

- `phase_count_by_holes={3: 8, 4: 56, 5: 8}`。
- `prime_pigeonhole_floor=3980`。
- `residue_pigeonhole_floor=221.111`。
- `max_prime_cover_over_floor=1.14372`。
- `max_residue_cover_over_floor=2.4603`。
- `max_column_residue_cover_over_floor=2.62312`。
- top prime cover: `[{'key': '13', 'count': 4552}, {'key': '17', 'count': 4036}, {'key': '19', 'count': 3932}, {'key': '23', 'count': 3724}]`。
- top residue cover: `[{'key': '13:2', 'count': 544}, {'key': '13:10', 'count': 544}, {'key': '19:13', 'count': 452}, {'key': '13:12', 'count': 438}, {'key': '13:0', 'count': 438}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 580}, {'key': '13:1', 'count': 574}, {'key': '13:3', 'count': 426}, {'key': '13:0', 'count': 408}, {'key': '13:11', 'count': 350}]`。

### P=29 alpha=0.9 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={3: 4, 4: 61, 5: 10}`。
- `prime_pigeonhole_floor=2827`。
- `residue_pigeonhole_floor=157.056`。
- `max_prime_cover_over_floor=1.11072`。
- `max_residue_cover_over_floor=2.49593`。
- `max_column_residue_cover_over_floor=3.3364`。
- top prime cover: `[{'key': '13', 'count': 3140}, {'key': '17', 'count': 2846}, {'key': '19', 'count': 2794}, {'key': '23', 'count': 2690}]`。
- top residue cover: `[{'key': '17:10', 'count': 392}, {'key': '17:2', 'count': 374}, {'key': '13:3', 'count': 344}, {'key': '13:10', 'count': 338}, {'key': '13:0', 'count': 332}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 524}, {'key': '17:16', 'count': 349}, {'key': '17:14', 'count': 349}, {'key': '19:16', 'count': 339}, {'key': '19:14', 'count': 339}]`。

### P=29 alpha=0.9 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={3: 4, 4: 61, 5: 10}`。
- `prime_pigeonhole_floor=2827`。
- `residue_pigeonhole_floor=157.056`。
- `max_prime_cover_over_floor=1.11072`。
- `max_residue_cover_over_floor=2.49593`。
- `max_column_residue_cover_over_floor=3.3364`。
- top prime cover: `[{'key': '13', 'count': 3140}, {'key': '17', 'count': 2846}, {'key': '19', 'count': 2794}, {'key': '23', 'count': 2690}]`。
- top residue cover: `[{'key': '17:6', 'count': 392}, {'key': '17:14', 'count': 374}, {'key': '13:9', 'count': 344}, {'key': '13:2', 'count': 338}, {'key': '13:12', 'count': 332}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 524}, {'key': '17:15', 'count': 349}, {'key': '17:13', 'count': 349}, {'key': '19:15', 'count': 339}, {'key': '19:13', 'count': 339}]`。

### P=31 alpha=0 h=1085 dir=0.75 source=top_by_mass

- `phase_count_by_holes={4: 32, 5: 237, 6: 138}`。
- `prime_pigeonhole_floor=119685`。
- `residue_pigeonhole_floor=5924.99`。
- `max_prime_cover_over_floor=1.44733`。
- `max_residue_cover_over_floor=3.59157`。
- `max_column_residue_cover_over_floor=5.06195`。
- top prime cover: `[{'key': '13', 'count': 173224}, {'key': '17', 'count': 117088}, {'key': '19', 'count': 114320}, {'key': '23', 'count': 108976}, {'key': '29', 'count': 101440}]`。
- top residue cover: `[{'key': '13:5', 'count': 21280}, {'key': '13:7', 'count': 21160}, {'key': '13:2', 'count': 20272}, {'key': '13:10', 'count': 20224}, {'key': '13:8', 'count': 11328}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 29992}, {'key': '13:1', 'count': 29368}, {'key': '13:3', 'count': 28876}, {'key': '13:2', 'count': 28516}, {'key': '17:13', 'count': 8997}]`。

### P=31 alpha=0 h=1225 dir=0.25 source=top_by_mass

- `phase_count_by_holes={4: 32, 5: 238, 6: 132}`。
- `prime_pigeonhole_floor=119632`。
- `residue_pigeonhole_floor=5922.38`。
- `max_prime_cover_over_floor=1.44657`。
- `max_residue_cover_over_floor=3.59315`。
- `max_column_residue_cover_over_floor=5.05608`。
- top prime cover: `[{'key': '13', 'count': 173056}, {'key': '17', 'count': 117064}, {'key': '19', 'count': 114296}, {'key': '23', 'count': 108952}, {'key': '29', 'count': 101416}]`。
- top residue cover: `[{'key': '13:5', 'count': 21280}, {'key': '13:7', 'count': 21112}, {'key': '13:2', 'count': 20296}, {'key': '13:10', 'count': 20248}, {'key': '13:8', 'count': 11304}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 29944}, {'key': '13:1', 'count': 29368}, {'key': '13:3', 'count': 28588}, {'key': '13:2', 'count': 28540}, {'key': '17:1', 'count': 9039}]`。

### P=31 alpha=0.5 h=1225 dir=0.25 source=top_by_mass

- `phase_count_by_holes={4: 32, 5: 188, 6: 84}`。
- `prime_pigeonhole_floor=106922`。
- `residue_pigeonhole_floor=5293.15`。
- `max_prime_cover_over_floor=1.43582`。
- `max_residue_cover_over_floor=3.73464`。
- `max_column_residue_cover_over_floor=5.03594`。
- top prime cover: `[{'key': '13', 'count': 153520}, {'key': '17', 'count': 105448}, {'key': '19', 'count': 102824}, {'key': '23', 'count': 97768}, {'key': '29', 'count': 90664}]`。
- top residue cover: `[{'key': '13:10', 'count': 19768}, {'key': '13:2', 'count': 19696}, {'key': '13:5', 'count': 19648}, {'key': '13:7', 'count': 19624}, {'key': '13:0', 'count': 9840}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 26656}, {'key': '13:3', 'count': 25852}, {'key': '13:1', 'count': 24424}, {'key': '13:2', 'count': 23644}, {'key': '17:1', 'count': 8613}]`。

### P=31 alpha=0.5 h=1085 dir=0.75 source=top_by_mass

- `phase_count_by_holes={4: 32, 5: 188, 6: 84}`。
- `prime_pigeonhole_floor=106922`。
- `residue_pigeonhole_floor=5293.15`。
- `max_prime_cover_over_floor=1.43582`。
- `max_residue_cover_over_floor=3.73464`。
- `max_column_residue_cover_over_floor=5.03594`。
- top prime cover: `[{'key': '13', 'count': 153520}, {'key': '17', 'count': 105448}, {'key': '19', 'count': 102824}, {'key': '23', 'count': 97768}, {'key': '29', 'count': 90664}]`。
- top residue cover: `[{'key': '13:10', 'count': 19768}, {'key': '13:2', 'count': 19696}, {'key': '13:5', 'count': 19648}, {'key': '13:7', 'count': 19624}, {'key': '13:0', 'count': 9840}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 26656}, {'key': '13:3', 'count': 25852}, {'key': '13:1', 'count': 24424}, {'key': '13:2', 'count': 23644}, {'key': '17:1', 'count': 8613}]`。

### P=31 alpha=0 h=1287 dir=0.25 source=top_by_size

- `phase_count_by_holes={4: 24, 5: 248, 6: 166}`。
- `prime_pigeonhole_floor=106058`。
- `residue_pigeonhole_floor=5250.38`。
- `max_prime_cover_over_floor=1.47467`。
- `max_residue_cover_over_floor=3.80392`。
- `max_column_residue_cover_over_floor=5.3878`。
- top prime cover: `[{'key': '13', 'count': 156400}, {'key': '17', 'count': 102616}, {'key': '19', 'count': 100280}, {'key': '23', 'count': 95800}, {'key': '29', 'count': 89560}]`。
- top residue cover: `[{'key': '13:7', 'count': 19972}, {'key': '13:10', 'count': 19480}, {'key': '13:5', 'count': 19408}, {'key': '13:2', 'count': 18916}, {'key': '13:11', 'count': 10632}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 28288}, {'key': '13:3', 'count': 27952}, {'key': '13:2', 'count': 27928}, {'key': '13:4', 'count': 24484}, {'key': '17:1', 'count': 7545}]`。

### P=31 alpha=0 h=1023 dir=0.75 source=top_by_size

- `phase_count_by_holes={4: 24, 5: 246, 6: 167}`。
- `prime_pigeonhole_floor=105846`。
- `residue_pigeonhole_floor=5239.92`。
- `max_prime_cover_over_floor=1.4758`。
- `max_residue_cover_over_floor=3.80693`。
- `max_column_residue_cover_over_floor=5.39397`。
- top prime cover: `[{'key': '13', 'count': 156208}, {'key': '17', 'count': 102400}, {'key': '19', 'count': 100064}, {'key': '23', 'count': 95584}, {'key': '29', 'count': 89344}]`。
- top residue cover: `[{'key': '13:7', 'count': 19948}, {'key': '13:10', 'count': 19456}, {'key': '13:5', 'count': 19408}, {'key': '13:2', 'count': 18940}, {'key': '13:11', 'count': 10608}]`。
- top column-residue cover: `[{'key': '13:1', 'count': 28264}, {'key': '13:3', 'count': 27952}, {'key': '13:2', 'count': 27880}, {'key': '13:4', 'count': 24508}, {'key': '17:1', 'count': 7503}]`。

### P=31 alpha=0.9 h=1225 dir=0.25 source=top_by_mass

- `phase_count_by_holes={4: 32, 5: 120, 6: 42}`。
- `prime_pigeonhole_floor=90448`。
- `residue_pigeonhole_floor=4477.62`。
- `max_prime_cover_over_floor=1.41925`。
- `max_residue_cover_over_floor=4.00748`。
- `max_column_residue_cover_over_floor=4.83292`。
- top prime cover: `[{'key': '13', 'count': 128368}, {'key': '17', 'count': 90328}, {'key': '19', 'count': 87896}, {'key': '23', 'count': 83224}, {'key': '29', 'count': 76696}]`。
- top residue cover: `[{'key': '13:7', 'count': 17944}, {'key': '13:10', 'count': 16984}, {'key': '13:2', 'count': 16912}, {'key': '13:5', 'count': 16840}, {'key': '13:12', 'count': 8208}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 21640}, {'key': '13:3', 'count': 20836}, {'key': '13:1', 'count': 19432}, {'key': '13:2', 'count': 18676}, {'key': '17:1', 'count': 7897}]`。

### P=31 alpha=0.9 h=1085 dir=0.75 source=top_by_mass

- `phase_count_by_holes={4: 32, 5: 120, 6: 42}`。
- `prime_pigeonhole_floor=90448`。
- `residue_pigeonhole_floor=4477.62`。
- `max_prime_cover_over_floor=1.41925`。
- `max_residue_cover_over_floor=4.00748`。
- `max_column_residue_cover_over_floor=4.83292`。
- top prime cover: `[{'key': '13', 'count': 128368}, {'key': '17', 'count': 90328}, {'key': '19', 'count': 87896}, {'key': '23', 'count': 83224}, {'key': '29', 'count': 76696}]`。
- top residue cover: `[{'key': '13:7', 'count': 17944}, {'key': '13:10', 'count': 16984}, {'key': '13:2', 'count': 16912}, {'key': '13:5', 'count': 16840}, {'key': '13:12', 'count': 8208}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 21640}, {'key': '13:3', 'count': 20836}, {'key': '13:1', 'count': 19432}, {'key': '13:2', 'count': 18676}, {'key': '17:1', 'count': 7897}]`。

### P=31 alpha=0.5 h=1287 dir=0.25 source=top_by_size

- `phase_count_by_holes={4: 18, 5: 184, 6: 104}`。
- `prime_pigeonhole_floor=77228.8`。
- `residue_pigeonhole_floor=3823.21`。
- `max_prime_cover_over_floor=1.49188`。
- `max_residue_cover_over_floor=4.4957`。
- `max_column_residue_cover_over_floor=5.66645`。
- top prime cover: `[{'key': '13', 'count': 115216}, {'key': '17', 'count': 74776}, {'key': '19', 'count': 72968}, {'key': '23', 'count': 69544}, {'key': '29', 'count': 64888}]`。
- top residue cover: `[{'key': '13:7', 'count': 17188}, {'key': '13:5', 'count': 15784}, {'key': '13:2', 'count': 15760}, {'key': '13:10', 'count': 15292}, {'key': '13:11', 'count': 7428}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 21664}, {'key': '13:3', 'count': 21616}, {'key': '13:1', 'count': 17776}, {'key': '13:2', 'count': 17728}, {'key': '17:16', 'count': 5904}]`。

### P=31 alpha=0.5 h=1023 dir=0.75 source=top_by_size

- `phase_count_by_holes={4: 18, 5: 184, 6: 104}`。
- `prime_pigeonhole_floor=77228.8`。
- `residue_pigeonhole_floor=3823.21`。
- `max_prime_cover_over_floor=1.49188`。
- `max_residue_cover_over_floor=4.4957`。
- `max_column_residue_cover_over_floor=5.66645`。
- top prime cover: `[{'key': '13', 'count': 115216}, {'key': '17', 'count': 74776}, {'key': '19', 'count': 72968}, {'key': '23', 'count': 69544}, {'key': '29', 'count': 64888}]`。
- top residue cover: `[{'key': '13:7', 'count': 17188}, {'key': '13:5', 'count': 15784}, {'key': '13:2', 'count': 15760}, {'key': '13:10', 'count': 15292}, {'key': '13:11', 'count': 7428}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 21664}, {'key': '13:3', 'count': 21616}, {'key': '13:1', 'count': 17776}, {'key': '13:2', 'count': 17728}, {'key': '17:16', 'count': 5904}]`。

### P=31 alpha=0.9 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={4: 16, 5: 166, 6: 116}`。
- `prime_pigeonhole_floor=66896`。
- `residue_pigeonhole_floor=3311.68`。
- `max_prime_cover_over_floor=1.41366`。
- `max_residue_cover_over_floor=4.5886`。
- `max_column_residue_cover_over_floor=8.16141`。
- top prime cover: `[{'key': '13', 'count': 94568}, {'key': '17', 'count': 65372}, {'key': '19', 'count': 63988}, {'key': '23', 'count': 61316}, {'key': '29', 'count': 57548}]`。
- top residue cover: `[{'key': '13:7', 'count': 15196}, {'key': '13:2', 'count': 15148}, {'key': '13:4', 'count': 7236}, {'key': '13:5', 'count': 7116}, {'key': '13:11', 'count': 6744}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 27028}, {'key': '13:4', 'count': 27028}, {'key': '17:16', 'count': 7842}, {'key': '19:16', 'count': 7550}, {'key': '23:16', 'count': 7014}]`。

### P=31 alpha=0.9 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={4: 16, 5: 166, 6: 116}`。
- `prime_pigeonhole_floor=66896`。
- `residue_pigeonhole_floor=3311.68`。
- `max_prime_cover_over_floor=1.41366`。
- `max_residue_cover_over_floor=4.5886`。
- `max_column_residue_cover_over_floor=8.16141`。
- top prime cover: `[{'key': '13', 'count': 94568}, {'key': '17', 'count': 65372}, {'key': '19', 'count': 63988}, {'key': '23', 'count': 61316}, {'key': '29', 'count': 57548}]`。
- top residue cover: `[{'key': '13:5', 'count': 15196}, {'key': '13:10', 'count': 15148}, {'key': '13:8', 'count': 7236}, {'key': '13:7', 'count': 7116}, {'key': '13:1', 'count': 6744}]`。
- top column-residue cover: `[{'key': '13:3', 'count': 27028}, {'key': '13:1', 'count': 27028}, {'key': '17:15', 'count': 7842}, {'key': '19:15', 'count': 7550}, {'key': '23:15', 'count': 7014}]`。

### P=37 alpha=0 h=1015 dir=0.25 source=top_by_mass

- `phase_count_by_holes={5: 24, 6: 199, 7: 302, 8: 34}`。
- `prime_pigeonhole_floor=850644`。
- `residue_pigeonhole_floor=38665.6`。
- `max_prime_cover_over_floor=1.64878`。
- `max_residue_cover_over_floor=3.73696`。
- `max_column_residue_cover_over_floor=3.74813`。
- top prime cover: `[{'key': '13', 'count': 1402528}, {'key': '17', 'count': 862480}, {'key': '19', 'count': 802404}, {'key': '23', 'count': 768660}, {'key': '29', 'count': 721164}]`。
- top residue cover: `[{'key': '13:7', 'count': 144492}, {'key': '13:5', 'count': 143580}, {'key': '13:1', 'count': 137288}, {'key': '13:11', 'count': 136976}, {'key': '13:4', 'count': 127452}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 144924}, {'key': '13:7', 'count': 142932}, {'key': '13:10', 'count': 142764}, {'key': '13:9', 'count': 141252}, {'key': '13:1', 'count': 141156}]`。

### P=37 alpha=0 h=1015 dir=0.25 source=top_by_size

- `phase_count_by_holes={5: 24, 6: 199, 7: 302, 8: 34}`。
- `prime_pigeonhole_floor=850644`。
- `residue_pigeonhole_floor=38665.6`。
- `max_prime_cover_over_floor=1.64878`。
- `max_residue_cover_over_floor=3.73696`。
- `max_column_residue_cover_over_floor=3.74813`。
- top prime cover: `[{'key': '13', 'count': 1402528}, {'key': '17', 'count': 862480}, {'key': '19', 'count': 802404}, {'key': '23', 'count': 768660}, {'key': '29', 'count': 721164}]`。
- top residue cover: `[{'key': '13:7', 'count': 144492}, {'key': '13:5', 'count': 143580}, {'key': '13:1', 'count': 137288}, {'key': '13:11', 'count': 136976}, {'key': '13:4', 'count': 127452}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 144924}, {'key': '13:7', 'count': 142932}, {'key': '13:10', 'count': 142764}, {'key': '13:9', 'count': 141252}, {'key': '13:1', 'count': 141156}]`。

### P=37 alpha=0 h=1295 dir=0.75 source=top_by_mass

- `phase_count_by_holes={5: 24, 6: 199, 7: 300, 8: 32}`。
- `prime_pigeonhole_floor=850300`。
- `residue_pigeonhole_floor=38650`。
- `max_prime_cover_over_floor=1.64863`。
- `max_residue_cover_over_floor=3.73164`。
- `max_column_residue_cover_over_floor=3.74965`。
- top prime cover: `[{'key': '13', 'count': 1401832}, {'key': '17', 'count': 862264}, {'key': '19', 'count': 802116}, {'key': '23', 'count': 768372}, {'key': '29', 'count': 720876}]`。
- top residue cover: `[{'key': '13:7', 'count': 144228}, {'key': '13:5', 'count': 143556}, {'key': '13:1', 'count': 137264}, {'key': '13:11', 'count': 136952}, {'key': '13:4', 'count': 127476}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 144924}, {'key': '13:7', 'count': 142908}, {'key': '13:10', 'count': 142764}, {'key': '13:1', 'count': 141180}, {'key': '13:9', 'count': 141012}]`。

### P=37 alpha=0 h=1295 dir=0.75 source=top_by_size

- `phase_count_by_holes={5: 24, 6: 199, 7: 300, 8: 32}`。
- `prime_pigeonhole_floor=850300`。
- `residue_pigeonhole_floor=38650`。
- `max_prime_cover_over_floor=1.64863`。
- `max_residue_cover_over_floor=3.73164`。
- `max_column_residue_cover_over_floor=3.74965`。
- top prime cover: `[{'key': '13', 'count': 1401832}, {'key': '17', 'count': 862264}, {'key': '19', 'count': 802116}, {'key': '23', 'count': 768372}, {'key': '29', 'count': 720876}]`。
- top residue cover: `[{'key': '13:7', 'count': 144228}, {'key': '13:5', 'count': 143556}, {'key': '13:1', 'count': 137264}, {'key': '13:11', 'count': 136952}, {'key': '13:4', 'count': 127476}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 144924}, {'key': '13:7', 'count': 142908}, {'key': '13:10', 'count': 142764}, {'key': '13:1', 'count': 141180}, {'key': '13:9', 'count': 141012}]`。

### P=37 alpha=0.5 h=1015 dir=0.25 source=top_by_mass

- `phase_count_by_holes={5: 24, 6: 178, 7: 188, 8: 18}`。
- `prime_pigeonhole_floor=804788`。
- `residue_pigeonhole_floor=36581.3`。
- `max_prime_cover_over_floor=1.65544`。
- `max_residue_cover_over_floor=3.82196`。
- `max_column_residue_cover_over_floor=3.8377`。
- top prime cover: `[{'key': '13', 'count': 1332280}, {'key': '17', 'count': 816952}, {'key': '19', 'count': 761172}, {'key': '23', 'count': 727908}, {'key': '29', 'count': 681132}]`。
- top residue cover: `[{'key': '13:7', 'count': 139812}, {'key': '13:11', 'count': 134264}, {'key': '13:5', 'count': 134100}, {'key': '13:1', 'count': 133616}, {'key': '13:4', 'count': 123324}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 140388}, {'key': '13:10', 'count': 137892}, {'key': '13:9', 'count': 136692}, {'key': '13:3', 'count': 134628}, {'key': '13:7', 'count': 133428}]`。

### P=37 alpha=0.5 h=1295 dir=0.75 source=top_by_mass

- `phase_count_by_holes={5: 24, 6: 178, 7: 188, 8: 18}`。
- `prime_pigeonhole_floor=804788`。
- `residue_pigeonhole_floor=36581.3`。
- `max_prime_cover_over_floor=1.65544`。
- `max_residue_cover_over_floor=3.82196`。
- `max_column_residue_cover_over_floor=3.8377`。
- top prime cover: `[{'key': '13', 'count': 1332280}, {'key': '17', 'count': 816952}, {'key': '19', 'count': 761172}, {'key': '23', 'count': 727908}, {'key': '29', 'count': 681132}]`。
- top residue cover: `[{'key': '13:7', 'count': 139812}, {'key': '13:11', 'count': 134264}, {'key': '13:5', 'count': 134100}, {'key': '13:1', 'count': 133616}, {'key': '13:4', 'count': 123324}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 140388}, {'key': '13:10', 'count': 137892}, {'key': '13:9', 'count': 136692}, {'key': '13:3', 'count': 134628}, {'key': '13:7', 'count': 133428}]`。

### P=37 alpha=0.5 h=1015 dir=0.25 source=top_by_size

- `phase_count_by_holes={5: 24, 6: 178, 7: 188, 8: 18}`。
- `prime_pigeonhole_floor=804788`。
- `residue_pigeonhole_floor=36581.3`。
- `max_prime_cover_over_floor=1.65544`。
- `max_residue_cover_over_floor=3.82196`。
- `max_column_residue_cover_over_floor=3.8377`。
- top prime cover: `[{'key': '13', 'count': 1332280}, {'key': '17', 'count': 816952}, {'key': '19', 'count': 761172}, {'key': '23', 'count': 727908}, {'key': '29', 'count': 681132}]`。
- top residue cover: `[{'key': '13:7', 'count': 139812}, {'key': '13:11', 'count': 134264}, {'key': '13:5', 'count': 134100}, {'key': '13:1', 'count': 133616}, {'key': '13:4', 'count': 123324}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 140388}, {'key': '13:10', 'count': 137892}, {'key': '13:9', 'count': 136692}, {'key': '13:3', 'count': 134628}, {'key': '13:7', 'count': 133428}]`。

### P=37 alpha=0.5 h=1295 dir=0.75 source=top_by_size

- `phase_count_by_holes={5: 24, 6: 178, 7: 188, 8: 18}`。
- `prime_pigeonhole_floor=804788`。
- `residue_pigeonhole_floor=36581.3`。
- `max_prime_cover_over_floor=1.65544`。
- `max_residue_cover_over_floor=3.82196`。
- `max_column_residue_cover_over_floor=3.8377`。
- top prime cover: `[{'key': '13', 'count': 1332280}, {'key': '17', 'count': 816952}, {'key': '19', 'count': 761172}, {'key': '23', 'count': 727908}, {'key': '29', 'count': 681132}]`。
- top residue cover: `[{'key': '13:7', 'count': 139812}, {'key': '13:11', 'count': 134264}, {'key': '13:5', 'count': 134100}, {'key': '13:1', 'count': 133616}, {'key': '13:4', 'count': 123324}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 140388}, {'key': '13:10', 'count': 137892}, {'key': '13:9', 'count': 136692}, {'key': '13:3', 'count': 134628}, {'key': '13:7', 'count': 133428}]`。

### P=37 alpha=0.9 h=1015 dir=0.25 source=top_by_mass

- `phase_count_by_holes={5: 18, 6: 110, 7: 84, 8: 12}`。
- `prime_pigeonhole_floor=555186`。
- `residue_pigeonhole_floor=25235.7`。
- `max_prime_cover_over_floor=1.65076`。
- `max_residue_cover_over_floor=4.65578`。
- `max_column_residue_cover_over_floor=4.80795`。
- top prime cover: `[{'key': '13', 'count': 916480}, {'key': '17', 'count': 574156}, {'key': '19', 'count': 526296}, {'key': '23', 'count': 502152}, {'key': '29', 'count': 468336}]`。
- top residue cover: `[{'key': '13:5', 'count': 117492}, {'key': '13:7', 'count': 111084}, {'key': '13:1', 'count': 110216}, {'key': '13:4', 'count': 97332}, {'key': '13:9', 'count': 83868}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 121332}, {'key': '13:10', 'count': 117132}, {'key': '13:9', 'count': 115596}, {'key': '13:3', 'count': 111084}, {'key': '13:2', 'count': 101196}]`。

### P=37 alpha=0.9 h=1295 dir=0.75 source=top_by_mass

- `phase_count_by_holes={5: 18, 6: 110, 7: 84, 8: 12}`。
- `prime_pigeonhole_floor=555186`。
- `residue_pigeonhole_floor=25235.7`。
- `max_prime_cover_over_floor=1.65076`。
- `max_residue_cover_over_floor=4.65578`。
- `max_column_residue_cover_over_floor=4.80795`。
- top prime cover: `[{'key': '13', 'count': 916480}, {'key': '17', 'count': 574156}, {'key': '19', 'count': 526296}, {'key': '23', 'count': 502152}, {'key': '29', 'count': 468336}]`。
- top residue cover: `[{'key': '13:5', 'count': 117492}, {'key': '13:7', 'count': 111084}, {'key': '13:1', 'count': 110216}, {'key': '13:4', 'count': 97332}, {'key': '13:9', 'count': 83868}]`。
- top column-residue cover: `[{'key': '13:4', 'count': 121332}, {'key': '13:10', 'count': 117132}, {'key': '13:9', 'count': 115596}, {'key': '13:3', 'count': 111084}, {'key': '13:2', 'count': 101196}]`。

### P=37 alpha=0.9 h=1155 dir=0 source=top_by_size

- `phase_count_by_holes={5: 12, 6: 121, 7: 240, 8: 32}`。
- `prime_pigeonhole_floor=454022`。
- `residue_pigeonhole_floor=20637.4`。
- `max_prime_cover_over_floor=1.62425`。
- `max_residue_cover_over_floor=4.55814`。
- `max_column_residue_cover_over_floor=6.41303`。
- top prime cover: `[{'key': '13', 'count': 737444}, {'key': '17', 'count': 460220}, {'key': '19', 'count': 427962}, {'key': '23', 'count': 411090}, {'key': '29', 'count': 387342}]`。
- top residue cover: `[{'key': '13:7', 'count': 94068}, {'key': '13:8', 'count': 91212}, {'key': '13:1', 'count': 85116}, {'key': '13:3', 'count': 77772}, {'key': '13:11', 'count': 57836}]`。
- top column-residue cover: `[{'key': '13:2', 'count': 132348}, {'key': '13:10', 'count': 132348}, {'key': '13:8', 'count': 130404}, {'key': '13:4', 'count': 130404}, {'key': '13:6', 'count': 73796}]`。

### P=37 alpha=0.9 h=1155 dir=0.5 source=top_by_size

- `phase_count_by_holes={5: 12, 6: 121, 7: 240, 8: 32}`。
- `prime_pigeonhole_floor=454022`。
- `residue_pigeonhole_floor=20637.4`。
- `max_prime_cover_over_floor=1.62425`。
- `max_residue_cover_over_floor=4.55814`。
- `max_column_residue_cover_over_floor=6.41303`。
- top prime cover: `[{'key': '13', 'count': 737444}, {'key': '17', 'count': 460220}, {'key': '19', 'count': 427962}, {'key': '23', 'count': 411090}, {'key': '29', 'count': 387342}]`。
- top residue cover: `[{'key': '13:5', 'count': 94068}, {'key': '13:4', 'count': 91212}, {'key': '13:11', 'count': 85116}, {'key': '13:9', 'count': 77772}, {'key': '13:1', 'count': 57836}]`。
- top column-residue cover: `[{'key': '13:9', 'count': 132348}, {'key': '13:1', 'count': 132348}, {'key': '13:3', 'count': 130404}, {'key': '13:7', 'count': 130404}, {'key': '13:5', 'count': 73796}]`。

## 7. 结构读数

这一步把 `PersistentCap => refined PDEC / column-tail rows` 从口头路由推进为支付方程：

```text
PersistentCap mass + low-hole demand
=> tail residue / column residue payment ledger
=> fixed overload PDEC or distributed CleanKLS/DLS。
```

下一硬点不再是寻找某个固定全局常数，而是证明：沿正式反例族，top 支付签名若持久复现则可提交同一 formal unit 的 PDEC；若不复现，则支付必须跨多壳分散，进入大筛型 CleanKLS/DLS。
