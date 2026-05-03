# WSH-Hall SCB-2 短块局部证书

**状态：** `finite_scb2_local_certificate_not_global_proof`

本文档专攻 `SCB-2`：对 `|B|<=3` 的连续平衡双尾半素数短块逐项审计 Hall 余量与出口压力。

## 参数

- `max_p`: `2000`
- `min_p`: `17`
- `y_ratio`: `0.36787944117144233`
- `radius_factor`: `3.0`
- `tight_surplus`: `2`
- `max_block_size`: `3`
- `wheel_primes`: `[2, 3, 5, 7, 11, 13]`

## 摘要

- 检查素数记录数：`297`。
- 含平衡半素数的行数：`215074`。
- 按块长计数：`{1: 1496400, 2: 1281326, 3: 1088870}`。
- 按块长最小 Hall 余量：`{'1': 1, '2': 1, '3': 2}`。
- 负余量块数：`0`。
- 零余量块数：`0`。
- 小余量块数：`45`。
- 小余量签名：`[{'surplus': 1, 'size': 1, 'count': 4}, {'surplus': 1, 'size': 2, 'count': 3}, {'surplus': 2, 'size': 1, 'count': 24}, {'surplus': 2, 'size': 2, 'count': 10}, {'surplus': 2, 'size': 3, 'count': 4}]`。
- 压力标签计数：`{'Endpoint-margin': 45, 'Fixed-offset-full-load': 17, 'Tail-repeat': 3}`。
- 连通性计数：`{'connected': 3539352, 'disconnected': 327244}`。
- 小余量最大尾标签负载：`2`。
- 小余量最大固定允许偏移负载：`3`。

## 最紧短块样本

| p | q | row | R | size | primes | surplus | connected | labels | semis | mirror span |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 17 | 19 | 5 | 27 | 2 | 3 | 1 | True | Endpoint-margin,Tail-repeat,Fixed-offset-full-load | [77, 91] | [243, 311] |
| 19 | 23 | 6 | 30 | 2 | 3 | 1 | True | Endpoint-margin,Tail-repeat,Fixed-offset-full-load | [119, 133] | [366, 440] |
| 1721 | 1723 | 853 | 167 | 2 | 3 | 1 | True | Endpoint-margin,Fixed-offset-full-load | [1468003, 1468013] | [1500549, 1500893] |
| 17 | 19 | 7 | 27 | 1 | 2 | 1 | True | Endpoint-margin | [119] | [215, 269] |
| 19 | 23 | 15 | 30 | 1 | 2 | 1 | True | Endpoint-margin | [323] | [176, 236] |
| 379 | 383 | 94 | 107 | 1 | 2 | 1 | True | Endpoint-margin | [35621] | [110961, 111175] |
| 673 | 677 | 587 | 128 | 1 | 2 | 1 | True | Endpoint-margin | [396731] | [61470, 61726] |
| 61 | 67 | 21 | 54 | 3 | 5 | 2 | True | Endpoint-margin,Tail-repeat,Fixed-offset-full-load | [1357, 1363, 1403] | [3032, 3186] |
| 41 | 43 | 17 | 43 | 3 | 5 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [697, 703, 713] | [1093, 1195] |
| 61 | 67 | 38 | 54 | 3 | 5 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [2491, 2501, 2537] | [1898, 2052] |
| 1721 | 1723 | 853 | 167 | 3 | 5 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [1468003, 1468013, 1468031] | [1500531, 1500893] |
| 19 | 23 | 10 | 30 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [209, 221] | [278, 350] |
| 23 | 29 | 8 | 35 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [209, 221] | [585, 667] |
| 31 | 37 | 15 | 40 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [527, 551] | [778, 882] |
| 47 | 53 | 26 | 48 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [1333, 1363] | [1398, 1524] |
| 233 | 239 | 150 | 90 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [35621, 35639] | [21392, 21590] |
| 347 | 349 | 103 | 103 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [35611, 35621] | [86077, 86293] |
| 359 | 367 | 98 | 105 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [35611, 35621] | [98963, 99183] |
| 379 | 383 | 94 | 107 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [35621, 35639] | [110943, 111175] |
| 773 | 787 | 570 | 134 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [448559, 448573] | [170662, 170944] |
| 1361 | 1367 | 489 | 157 | 2 | 4 | 2 | True | Endpoint-margin,Fixed-offset-full-load | [668431, 668443] | [1200089, 1200415] |
| 17 | 19 | 5 | 27 | 1 | 3 | 2 | True | Endpoint-margin | [77] | [257, 311] |
| 17 | 19 | 5 | 27 | 1 | 3 | 2 | True | Endpoint-margin | [91] | [243, 297] |
| 17 | 19 | 10 | 27 | 1 | 3 | 2 | True | Endpoint-margin | [187] | [147, 201] |
| 17 | 19 | 12 | 27 | 1 | 3 | 2 | True | Endpoint-margin | [221] | [113, 167] |
| 19 | 23 | 6 | 30 | 1 | 3 | 2 | True | Endpoint-margin | [119] | [380, 440] |
| 19 | 23 | 6 | 30 | 1 | 3 | 2 | True | Endpoint-margin | [133] | [366, 426] |
| 23 | 29 | 12 | 35 | 1 | 3 | 2 | True | Endpoint-margin | [323] | [483, 553] |
| 29 | 31 | 18 | 36 | 1 | 3 | 2 | True | Endpoint-margin | [551] | [374, 446] |
| 31 | 37 | 25 | 40 | 1 | 3 | 2 | True | Endpoint-margin | [899] | [430, 510] |
| 53 | 59 | 43 | 50 | 1 | 3 | 2 | True | Endpoint-margin | [2491] | [940, 1040] |
| 233 | 239 | 150 | 90 | 1 | 3 | 2 | True | Endpoint-margin | [35621] | [21410, 21590] |
| 293 | 307 | 117 | 99 | 1 | 3 | 2 | True | Endpoint-margin | [35621] | [58529, 58727] |
| 613 | 617 | 407 | 124 | 1 | 3 | 2 | True | Endpoint-margin | [250517] | [130048, 130296] |
| 619 | 631 | 398 | 125 | 1 | 3 | 2 | True | Endpoint-margin | [250517] | [147519, 147769] |
| 653 | 659 | 603 | 127 | 1 | 3 | 2 | True | Endpoint-margin | [396731] | [37423, 37677] |
| 859 | 863 | 430 | 138 | 1 | 3 | 2 | True | Endpoint-margin | [370229] | [374402, 374678] |
| 1367 | 1373 | 983 | 157 | 1 | 3 | 2 | True | Endpoint-margin | [1349653] | [535319, 535633] |
| 1637 | 1657 | 687 | 165 | 1 | 3 | 2 | True | Endpoint-margin | [1138349] | [1607135, 1607465] |
| 1721 | 1723 | 853 | 167 | 1 | 3 | 2 | True | Endpoint-margin | [1468003] | [1500559, 1500893] |
| 1721 | 1723 | 853 | 167 | 1 | 3 | 2 | True | Endpoint-margin | [1468013] | [1500549, 1500883] |
| 1861 | 1867 | 1617 | 171 | 1 | 3 | 2 | True | Endpoint-margin | [3018937] | [466581, 466923] |
| 1871 | 1873 | 1429 | 171 | 1 | 3 | 2 | True | Endpoint-margin | [2674657] | [833301, 833643] |
| 1901 | 1907 | 820 | 172 | 1 | 3 | 2 | True | Endpoint-margin | [1561843] | [2074634, 2074978] |
| 1987 | 1993 | 1126 | 174 | 1 | 3 | 2 | True | Endpoint-margin | [2244113] | [1727762, 1728110] |

## 审稿解释

在有限范围内，`SCB-2` 的所有短块都有正 Hall 余量：单点、双点、三点块的最小余量均为 `1`。小余量块没有负余量或零余量；其中双点和三点紧块会显示尾标签重复或固定偏移满载压力。

这支持下一步证明模板：若短块失败，则单点失败直接是端点素数亏损；双点和三点失败若不分解为单点失败，则必须出现尾标签重复、固定偏移满载或小轮相位集中，进而进入命名出口。该文件仍是有限证书，不是全局证明。
