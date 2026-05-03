# WSH-Hall 固定偏移/PDEC 吸收账本

**状态：** `finite_fixed_offset_pdec_absorption_ledger_not_global_proof`

本文档审计 `SCB-1` 最紧长块中的 `Fixed-offset-full-load`。它验证满载偏移上的缺失候选并非无来源缺口：每个非素候选都有 `<=p` 的解释因子，因此可进入 Tail-anchor、low-mod CRTDefect 或 PDEC 吸收账本。

## 摘要

- 最紧长块数：`4`。
- 满载固定偏移行数：`11`。
- 满载偏移候选总数：`47`。
- 其中素数候选数：`15`。
- 其中缺失候选数：`32`。
- 无 `<=p` 解释因子的缺失候选数：`0`。
- 单个偏移行最大解释因子负载：`1`。
- 全局最高解释因子负载：`[{'factor': 19, 'load': 4}, {'factor': 199, 'load': 4}, {'factor': 29, 'load': 4}, {'factor': 31, 'load': 3}, {'factor': 67, 'load': 3}, {'factor': 53, 'load': 3}, {'factor': 127, 'load': 2}, {'factor': 83, 'load': 2}, {'factor': 193, 'load': 2}, {'factor': 79, 'load': 2}, {'factor': 397, 'load': 2}, {'factor': 631, 'load': 2}, {'factor': 163, 'load': 2}, {'factor': 131, 'load': 1}, {'factor': 17, 'load': 1}, {'factor': 223, 'load': 1}, {'factor': 439, 'load': 1}, {'factor': 23, 'load': 1}, {'factor': 269, 'load': 1}, {'factor': 157, 'load': 1}]`。

## 满载偏移行

| block | p | q | row | size | offset | allowed | actual same offset | prime | missing | max factor load | top factors | mirror span |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | 1987 | 1993 | 836 | 5 | -126 | 5 | 0 | 2 | 3 | 1 | [{'factor': 19, 'load': 1}, {'factor': 127, 'load': 1}, {'factor': 131, 'load': 1}] | [2307956, 2307978] |
| 1 | 1987 | 1993 | 836 | 5 | 30 | 5 | 1 | 1 | 4 | 1 | [{'factor': 83, 'load': 1}, {'factor': 199, 'load': 1}, {'factor': 193, 'load': 1}, {'factor': 17, 'load': 1}, {'factor': 223, 'load': 1}, {'factor': 439, 'load': 1}] | [2307800, 2307822] |
| 1 | 1987 | 1993 | 836 | 5 | 84 | 5 | 2 | 2 | 3 | 1 | [{'factor': 29, 'load': 1}, {'factor': 79, 'load': 1}, {'factor': 23, 'load': 1}, {'factor': 269, 'load': 1}] | [2307746, 2307768] |
| 2 | 769 | 773 | 325 | 4 | -6 | 4 | 0 | 1 | 3 | 1 | [{'factor': 19, 'load': 1}, {'factor': 31, 'load': 1}, {'factor': 67, 'load': 1}] | [347016, 347052] |
| 2 | 769 | 773 | 325 | 4 | 24 | 4 | 0 | 1 | 3 | 1 | [{'factor': 397, 'load': 1}, {'factor': 631, 'load': 1}, {'factor': 29, 'load': 1}, {'factor': 53, 'load': 1}, {'factor': 163, 'load': 1}, {'factor': 199, 'load': 1}] | [346986, 347022] |
| 3 | 953 | 967 | 260 | 4 | -6 | 4 | 0 | 1 | 3 | 1 | [{'factor': 19, 'load': 1}, {'factor': 31, 'load': 1}, {'factor': 67, 'load': 1}] | [684576, 684612] |
| 3 | 953 | 967 | 260 | 4 | 24 | 4 | 0 | 1 | 3 | 1 | [{'factor': 397, 'load': 1}, {'factor': 631, 'load': 1}, {'factor': 29, 'load': 1}, {'factor': 53, 'load': 1}, {'factor': 163, 'load': 1}, {'factor': 199, 'load': 1}] | [684546, 684582] |
| 4 | 1987 | 1993 | 836 | 4 | -126 | 4 | 0 | 2 | 2 | 1 | [{'factor': 19, 'load': 1}, {'factor': 127, 'load': 1}] | [2307966, 2307978] |
| 4 | 1987 | 1993 | 836 | 4 | 30 | 4 | 1 | 1 | 3 | 1 | [{'factor': 83, 'load': 1}, {'factor': 199, 'load': 1}, {'factor': 193, 'load': 1}] | [2307810, 2307822] |
| 4 | 1987 | 1993 | 836 | 4 | 84 | 4 | 2 | 2 | 2 | 1 | [{'factor': 29, 'load': 1}, {'factor': 79, 'load': 1}] | [2307756, 2307768] |
| 4 | 1987 | 1993 | 836 | 4 | 150 | 4 | 0 | 1 | 3 | 1 | [{'factor': 67, 'load': 1}, {'factor': 157, 'load': 1}, {'factor': 31, 'load': 1}, {'factor': 53, 'load': 1}, {'factor': 1013, 'load': 1}] | [2307690, 2307702] |

## 审稿解释

满载固定偏移 `d` 表示所有 `b in B` 的候选 `b+d` 均避开轮筛小素数禁类。若这些候选已经给出足够素数，则长块扩张成立；若不足，则每个缺失候选必须由某个 `<=p` 素因子解释。当前有限账本中 `missing_without_factor_le_p=0`，所以缺失并非第三种逃逸。

全局证明仍需把这些解释因子的负载转成正式不等式：重复因子进入 Tail-anchor，低模相位持续缺陷进入 PDEC，孤立端点缺失进入 SAE/Endpoint。该文件只闭合有限吸收账本，不排除最终 Endpoint/PDEC。
