# Triad-A1 PDEC DualCap 提取账本

**状态：** `pdec_dualcap_candidates_materialized`

PDEC 对偶上界失败必须输出 DualCap。当前提取器把固定 Q Fourier-cap 的最重/最大失败帽重建为完整相位块，并按 Empty/Sparse/Persistent/密度屏障强制进行路由。

## 1. 结构语义

若固定 `Q` 的 `PDEC` 对偶上界 `U_CRT<L_PDEC` 失败，失败必须显化为 Fourier/Bohr cap 中的质量集中。
本账本从 LHB Fourier-cap 扫描中抽取最重/最大 cap，并重建完整相位交集：

```text
DualCap = C_{h,alpha,dir} cap supp(M)。
```

路由规则：

```text
EmptyCap      => 当前方向在 LHB 分支闭合；
SparseCap     => LocalSurvivor 或 explicit PDEC；
PersistentCap => refined PDEC / column-tail rows；
DensityBarrier forced Persistent => 不能同层循环，必须升层、加行或 CleanKLS。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `pdec_dualcap_extractor_script` | `972c4f297cb13f2b1ea27e65874738348237ec39c6fb738f027c6e8532733a68` |
| `multiplicity_cap_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |
| `fourier_cap_scan_json` | `fe47050ce4b60f5c5651228f7e940eb20898506149f830d86448375984b7e502` |

## 3. 汇总

- `aggregate_class_counts={'SparseCap': 16, 'PersistentCap': 68, 'ForcedPersistentByDensityBarrier': 24}`。
- `aggregate_route_counts={'LocalSurvivorOrExplicitPDEC': 16, 'RefinedPDECOrColumnTailRows': 68, 'LiftOrColumnTailOrCleanKLS': 24}`。

| P | candidates | classes | routes | top mass share | top intersection | top route |
| ---: | ---: | --- | --- | ---: | ---: | --- |
| 13 | 12 | `{'SparseCap': 12}` | `{'LocalSurvivorOrExplicitPDEC': 12}` | 1 | 4 | `LocalSurvivorOrExplicitPDEC` |
| 17 | 12 | `{'PersistentCap': 8, 'SparseCap': 4}` | `{'RefinedPDECOrColumnTailRows': 8, 'LocalSurvivorOrExplicitPDEC': 4}` | 1 | 28 | `RefinedPDECOrColumnTailRows` |
| 19 | 12 | `{'PersistentCap': 12}` | `{'RefinedPDECOrColumnTailRows': 12}` | 0.971774 | 133 | `RefinedPDECOrColumnTailRows` |
| 23 | 12 | `{'PersistentCap': 12}` | `{'RefinedPDECOrColumnTailRows': 12}` | 0.928819 | 191 | `RefinedPDECOrColumnTailRows` |
| 29 | 12 | `{'PersistentCap': 12}` | `{'RefinedPDECOrColumnTailRows': 12}` | 0.966334 | 141 | `RefinedPDECOrColumnTailRows` |
| 31 | 12 | `{'PersistentCap': 12}` | `{'RefinedPDECOrColumnTailRows': 12}` | 0.908994 | 407 | `RefinedPDECOrColumnTailRows` |
| 37 | 12 | `{'PersistentCap': 12}` | `{'RefinedPDECOrColumnTailRows': 12}` | 0.945645 | 559 | `RefinedPDECOrColumnTailRows` |
| 43 | 12 | `{'ForcedPersistentByDensityBarrier': 12}` | `{'LiftOrColumnTailOrCleanKLS': 12}` | 0.880485 | 1077 | `LiftOrColumnTailOrCleanKLS` |
| 47 | 12 | `{'ForcedPersistentByDensityBarrier': 12}` | `{'LiftOrColumnTailOrCleanKLS': 12}` | 0.828184 | 1150 | `LiftOrColumnTailOrCleanKLS` |

## 4. Top DualCaps

### P=13

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 3 | 0 | `top_by_mass` | `SparseCap` | `LocalSurvivorOrExplicitPDEC` | 1155 | 4 | 1 | 0 | `[169, 702, 1609, 2142]` |
| 0 | 13 | 0 | `top_by_mass` | `SparseCap` | `LocalSurvivorOrExplicitPDEC` | 1155 | 4 | 1 | 0 | `[169, 702, 1609, 2142]` |
| 0 | 3 | 0 | `top_by_size` | `SparseCap` | `LocalSurvivorOrExplicitPDEC` | 1155 | 4 | 1 | 0 | `[169, 702, 1609, 2142]` |
| 0 | 13 | 0 | `top_by_size` | `SparseCap` | `LocalSurvivorOrExplicitPDEC` | 1155 | 4 | 1 | 0 | `[169, 702, 1609, 2142]` |
| 0.5 | 13 | 0 | `top_by_mass` | `SparseCap` | `LocalSurvivorOrExplicitPDEC` | 770 | 4 | 1 | 0 | `[169, 702, 1609, 2142]` |
| 0.5 | 26 | 0 | `top_by_mass` | `SparseCap` | `LocalSurvivorOrExplicitPDEC` | 770 | 4 | 1 | 0 | `[169, 702, 1609, 2142]` |

### P=17

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 374 | 0 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1166 | 28 | 1 | 0 | `[13, 124, 260, 378, 401, 551, 611, 613, 673, 710, 823, 828, 964, 1100, 1211, 1347]` |
| 0 | 1936 | 0 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1166 | 28 | 1 | 0 | `[13, 124, 260, 378, 401, 551, 611, 613, 673, 710, 823, 828, 964, 1100, 1211, 1347]` |
| 0 | 374 | 0 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1166 | 28 | 1 | 0 | `[13, 124, 260, 378, 401, 551, 611, 613, 673, 710, 823, 828, 964, 1100, 1211, 1347]` |
| 0 | 1936 | 0 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1166 | 28 | 1 | 0 | `[13, 124, 260, 378, 401, 551, 611, 613, 673, 710, 823, 828, 964, 1100, 1211, 1347]` |
| 0.5 | 1001 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 28 | 1 | 0 | `[13, 124, 260, 378, 401, 551, 611, 613, 673, 710, 823, 828, 964, 1100, 1211, 1347]` |
| 0.5 | 1309 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 28 | 1 | 0 | `[13, 124, 260, 378, 401, 551, 611, 613, 673, 710, 823, 828, 964, 1100, 1211, 1347]` |

### P=19

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 847 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1159 | 133 | 0.971774 | 0 | `[7, 18, 62, 89, 97, 100, 111, 122, 133, 149, 182, 226, 237, 250, 299, 307]` |
| 0 | 1463 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1150 | 133 | 0.971774 | 0 | `[7, 18, 62, 89, 97, 100, 111, 122, 133, 149, 182, 226, 237, 250, 299, 307]` |
| 0 | 847 | 0.25 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1159 | 133 | 0.971774 | 0 | `[7, 18, 62, 89, 97, 100, 111, 122, 133, 149, 182, 226, 237, 250, 299, 307]` |
| 0 | 1463 | 0.75 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1150 | 133 | 0.971774 | 0 | `[7, 18, 62, 89, 97, 100, 111, 122, 133, 149, 182, 226, 237, 250, 299, 307]` |
| 0.5 | 847 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 113 | 0.891129 | 0 | `[18, 62, 89, 100, 111, 122, 133, 149, 182, 226, 237, 250, 299, 310, 321, 324]` |
| 0.5 | 1463 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 113 | 0.891129 | 0 | `[18, 62, 89, 100, 111, 122, 133, 149, 182, 226, 237, 250, 299, 310, 321, 324]` |

### P=23

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 1045 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1160 | 191 | 0.928819 | 0 | `[6, 15, 37, 50, 59, 79, 92, 101, 110, 119, 123, 132, 152, 174, 179, 187]` |
| 0 | 1045 | 0.25 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1160 | 191 | 0.928819 | 0 | `[6, 15, 37, 50, 59, 79, 92, 101, 110, 119, 123, 132, 152, 174, 179, 187]` |
| 0 | 1265 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1161 | 188 | 0.923611 | 0 | `[6, 15, 37, 50, 59, 79, 92, 101, 110, 119, 123, 132, 152, 174, 179, 187]` |
| 0 | 1265 | 0.75 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1161 | 188 | 0.923611 | 0 | `[6, 15, 37, 50, 59, 79, 92, 101, 110, 119, 123, 132, 152, 174, 179, 187]` |
| 0.5 | 1045 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 176 | 0.902778 | 0 | `[6, 15, 37, 50, 59, 79, 92, 101, 110, 119, 123, 132, 152, 174, 187, 192]` |
| 0.5 | 1265 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 176 | 0.902778 | 0 | `[6, 15, 37, 50, 59, 79, 92, 101, 110, 119, 123, 132, 152, 174, 187, 192]` |

### P=29

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 715 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1156 | 141 | 0.966334 | 0 | `[5, 12, 18, 41, 73, 80, 112, 128, 164, 167, 199, 222, 228, 235, 244, 251]` |
| 0 | 715 | 0.25 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1156 | 141 | 0.966334 | 0 | `[5, 12, 18, 41, 73, 80, 112, 128, 164, 167, 199, 222, 228, 235, 244, 251]` |
| 0 | 1595 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1154 | 139 | 0.958853 | 0 | `[5, 12, 18, 41, 73, 80, 112, 128, 164, 167, 199, 222, 228, 235, 244, 251]` |
| 0 | 1595 | 0.75 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1154 | 139 | 0.958853 | 0 | `[5, 12, 18, 41, 73, 80, 112, 128, 164, 167, 199, 222, 228, 235, 244, 251]` |
| 0.5 | 1295 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 104 | 0.839152 | 0 | `[5, 12, 80, 112, 128, 167, 228, 235, 244, 251, 312, 319, 351, 360, 367, 392]` |
| 0.5 | 1015 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 104 | 0.839152 | 0 | `[5, 12, 80, 112, 128, 167, 228, 235, 244, 251, 312, 319, 351, 360, 367, 392]` |

### P=31

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 1085 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1151 | 407 | 0.908994 | 0 | `[7, 9, 11, 26, 37, 39, 41, 50, 52, 60, 64, 71, 75, 79, 86, 90]` |
| 0 | 1225 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1152 | 402 | 0.908834 | 0 | `[7, 9, 11, 26, 37, 39, 41, 50, 52, 60, 64, 71, 75, 79, 86, 90]` |
| 0.5 | 1225 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 304 | 0.825665 | 0 | `[7, 9, 11, 26, 37, 39, 41, 60, 71, 75, 79, 86, 90, 107, 109, 111]` |
| 0.5 | 1085 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 304 | 0.825665 | 0 | `[7, 9, 11, 26, 37, 39, 41, 60, 71, 75, 79, 86, 90, 107, 109, 111]` |
| 0 | 1287 | 0.25 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1151 | 438 | 0.793997 | 0 | `[7, 10, 14, 16, 21, 37, 39, 41, 50, 52, 64, 68, 71, 75, 82, 86]` |
| 0 | 1023 | 0.75 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1152 | 437 | 0.792557 | 0 | `[7, 10, 14, 16, 21, 37, 39, 41, 50, 52, 64, 68, 71, 75, 82, 86]` |

### P=37

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 1015 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1163 | 559 | 0.945645 | 0 | `[4, 6, 13, 20, 25, 27, 29, 31, 34, 38, 43, 45, 49, 54, 59, 63]` |
| 0 | 1015 | 0.25 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1163 | 559 | 0.945645 | 0 | `[4, 6, 13, 20, 25, 27, 29, 31, 34, 38, 43, 45, 49, 54, 59, 63]` |
| 0 | 1295 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1158 | 555 | 0.945353 | 0 | `[4, 6, 13, 20, 25, 27, 29, 31, 34, 38, 43, 45, 49, 54, 59, 63]` |
| 0 | 1295 | 0.75 | `top_by_size` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 1158 | 555 | 0.945353 | 0 | `[4, 6, 13, 20, 25, 27, 29, 31, 34, 38, 43, 45, 49, 54, 59, 63]` |
| 0.5 | 1015 | 0.25 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 408 | 0.90221 | 0 | `[4, 6, 13, 20, 27, 29, 31, 38, 43, 45, 54, 63, 68, 70, 72, 77]` |
| 0.5 | 1295 | 0.75 | `top_by_mass` | `PersistentCap` | `RefinedPDECOrColumnTailRows` | 770 | 408 | 0.90221 | 0 | `[4, 6, 13, 20, 27, 29, 31, 38, 43, 45, 54, 63, 68, 70, 72, 77]` |

### P=43

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 805 | 0.25 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1153 | 1077 | 0.880485 | 893 | `[2, 5, 8, 11, 13, 14, 16, 17, 19, 20, 22, 25, 28, 31, 33, 34]` |
| 0 | 1505 | 0.75 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1154 | 1081 | 0.880183 | 894 | `[2, 5, 8, 11, 13, 14, 16, 17, 19, 20, 22, 25, 28, 31, 34, 36]` |
| 0.5 | 805 | 0.25 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 770 | 734 | 0.706523 | 510 | `[2, 5, 8, 11, 14, 19, 22, 25, 28, 31, 34, 37, 39, 42, 45, 48]` |
| 0.5 | 1505 | 0.75 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 770 | 734 | 0.706523 | 510 | `[2, 5, 8, 11, 14, 19, 22, 25, 28, 31, 34, 37, 39, 42, 45, 48]` |
| 0 | 770 | 0.5 | `top_by_size` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1540 | 1370 | 0.647211 | 1280 | `[2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25]` |
| 0 | 1540 | 0.5 | `top_by_size` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1540 | 1370 | 0.647211 | 1280 | `[2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25]` |

### P=47

| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |
| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 0 | 665 | 0.25 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1158 | 1150 | 0.828184 | 1114 | `[0, 2, 3, 6, 9, 10, 13, 16, 17, 20, 23, 24, 27, 30, 31, 34]` |
| 0 | 1645 | 0.75 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1153 | 1145 | 0.824273 | 1109 | `[2, 3, 6, 9, 10, 13, 16, 17, 20, 23, 24, 27, 30, 31, 33, 34]` |
| 0 | 770 | 0.5 | `top_by_size` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1540 | 1512 | 0.722625 | 1496 | `[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23]` |
| 0 | 1540 | 0.5 | `top_by_size` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 1540 | 1512 | 0.722625 | 1496 | `[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23]` |
| 0.5 | 1001 | 0.25 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 770 | 757 | 0.60951 | 726 | `[2, 4, 6, 9, 11, 13, 18, 20, 25, 27, 32, 34, 36, 39, 41, 43]` |
| 0.5 | 1309 | 0.75 | `top_by_mass` | `ForcedPersistentByDensityBarrier` | `LiftOrColumnTailOrCleanKLS` | 770 | 757 | 0.60951 | 726 | `[2, 4, 6, 9, 11, 13, 18, 20, 25, 27, 32, 34, 36, 39, 41, 43]` |

## 5. 结论

本账本没有排除全部 PDEC；它完成的是 PDEC 失败的强制输出。
以后若固定 `Q` 对偶比较失败，必须引用这里的 `DualCap` 或生成同格式新 cap，不能停在抽象 `DualGap`。
