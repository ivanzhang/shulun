# BPN-B5 高重小素因子核心审计

**状态：** `high_omega_penalty_has_small_core_tail_anchor_structure`

BPN-B5 的负项集中在含至少六个小素因子的数。这些数都有六小素核心 core6<P^2；样本最薄行的高重惩罚可按 core6 桶分解。这支持下一步把惩罚过大转化为小核心乘积过密或 Tail-anchor/CRTDefect。

## 1. 结构恒等式

五阶下界已经化为

\[
S_5(I)=\#\{n\in I:\omega_P(n)=0\}
-\sum_{n\in I,\omega_P(n)\ge6}\binom{\omega_P(n)-1}{5}.
\]

在边界帽 `n<P^2` 中，第一项就是该行内素数数目。第二项的每个贡献都有六小素核心

\[
core_6(n)=q_1q_2q_3q_4q_5q_6<P^2.
\]

若第二项过大，则某类 `core_6` 桶必须在短窗中过密。

## 2. 审计总表

| P | min S5 row | row | prime_like | penalty | S5 | core bins |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 503 | 360 | 251 | 43 | 1 | 42 | `{'<=P^2/2': {'count': 1, 'penalty': 1, 'min_core': 125970, 'max_core': 125970}}` |
| 503 | 360 | 360 | 29 | 1 | 28 | `{'<P^2': {'count': 1, 'penalty': 1, 'min_core': 180642, 'max_core': 180642}}` |
| 503 | 360 | 502 | 39 | 0 | 39 | `{}` |
| 503 | 360 | 503 | 39 | 0 | 39 | `{}` |
| 1009 | 906 | 504 | 75 | 3 | 72 | `{'<=P^2/2': {'count': 2, 'penalty': 2, 'min_core': 507990, 'max_core': 508530}, '<=P^2/4': {'count': 1, 'penalty': 1, 'min_core': 84630, 'max_core': 84630}}` |
| 1009 | 906 | 906 | 52 | 3 | 49 | `{'<=P^2/2': {'count': 2, 'penalty': 2, 'min_core': 304590, 'max_core': 456918}, '<P^2': {'count': 1, 'penalty': 1, 'min_core': 913710, 'max_core': 913710}}` |
| 1009 | 906 | 1008 | 71 | 5 | 66 | `{'<=P^2/2': {'count': 2, 'penalty': 2, 'min_core': 338910, 'max_core': 508530}, '<P^2': {'count': 3, 'penalty': 3, 'min_core': 1016610, 'max_core': 1017030}}` |
| 1009 | 906 | 1009 | 70 | 2 | 68 | `{'<=P^2/4': {'count': 1, 'penalty': 1, 'min_core': 67830, 'max_core': 67830}, '<P^2': {'count': 1, 'penalty': 1, 'min_core': 1017870, 'max_core': 1017870}}` |
| 2003 | 1674 | 1001 | 138 | 10 | 128 | `{'<=P^2/2': {'count': 4, 'penalty': 4, 'min_core': 2003001, 'max_core': 2004990}, '<=P^2/4': {'count': 6, 'penalty': 6, 'min_core': 286230, 'max_core': 1001946}}` |
| 2003 | 1674 | 1674 | 113 | 17 | 96 | `{'<=P^2/2': {'count': 7, 'penalty': 7, 'min_core': 1117410, 'max_core': 1676490}, '<=P^2/4': {'count': 4, 'penalty': 4, 'min_core': 186186, 'max_core': 838110}, '<P^2': {'count': 6, 'penalty': 6, 'min_core': 3351414, 'max_core': 3352710}}` |
| 2003 | 1674 | 2002 | 126 | 16 | 110 | `{'<=P^2/2': {'count': 4, 'penalty': 4, 'min_core': 1336335, 'max_core': 2004990}, '<=P^2/4': {'count': 3, 'penalty': 3, 'min_core': 267330, 'max_core': 400890}, '<P^2': {'count': 9, 'penalty': 9, 'min_core': 4008030, 'max_core': 4009830}}` |
| 2003 | 1674 | 2003 | 139 | 17 | 122 | `{'<=P^2/2': {'count': 3, 'penalty': 3, 'min_core': 1337154, 'max_core': 2005770}, '<=P^2/4': {'count': 7, 'penalty': 7, 'min_core': 71610, 'max_core': 1003002}, '<P^2': {'count': 7, 'penalty': 7, 'min_core': 4010510, 'max_core': 4011546}}` |
| 5003 | 4822 | 2501 | 311 | 62 | 249 | `{'<=P^2/2': {'count': 25, 'penalty': 25, 'min_core': 12507990, 'max_core': 12511785}, '<=P^2/4': {'count': 32, 'penalty': 37, 'min_core': 43890, 'max_core': 6255678}}` |
| 5003 | 4822 | 4822 | 272 | 95 | 177 | `{'<=P^2/2': {'count': 13, 'penalty': 13, 'min_core': 8040570, 'max_core': 12062190}, '<=P^2/4': {'count': 30, 'penalty': 55, 'min_core': 51870, 'max_core': 6031014}, '<P^2': {'count': 27, 'penalty': 27, 'min_core': 24119810, 'max_core': 24124386}}` |
| 5003 | 4822 | 5002 | 288 | 83 | 205 | `{'<=P^2/2': {'count': 12, 'penalty': 12, 'min_core': 8340090, 'max_core': 12511590}, '<=P^2/4': {'count': 28, 'penalty': 43, 'min_core': 53130, 'max_core': 6255678}, '<P^2': {'count': 28, 'penalty': 28, 'min_core': 25020030, 'max_core': 25024710}}` |
| 5003 | 4822 | 5003 | 281 | 79 | 202 | `{'<=P^2/2': {'count': 15, 'penalty': 15, 'min_core': 8341710, 'max_core': 12514890}, '<=P^2/4': {'count': 28, 'penalty': 38, 'min_core': 67830, 'max_core': 6257370}, '<P^2': {'count': 26, 'penalty': 26, 'min_core': 25025070, 'max_core': 25030005}}` |

## 3. 最薄行样本

### P=503, row=360
- omega_hist=`{0: 29, 1: 157, 2: 155, 3: 76, 4: 66, 5: 18, 6: 1}`
- samples=`[{'n': 180642, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 7, 11, 17, 23], 'core6': 180642, 'bucket': '<P^2'}]`

### P=1009, row=906
- omega_hist=`{0: 52, 1: 308, 2: 296, 3: 153, 4: 141, 5: 55, 6: 3}`
- samples=`[{'n': 913710, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 19, 229], 'core6': 913710, 'bucket': '<P^2'}, {'n': 913770, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 11, 13, 71], 'core6': 304590, 'bucket': '<=P^2/2'}, {'n': 913836, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 7, 11, 23, 43], 'core6': 456918, 'bucket': '<=P^2/2'}]`

### P=2003, row=1674
- omega_hist=`{0: 113, 1: 536, 2: 567, 3: 378, 4: 275, 5: 116, 6: 17}`
- samples=`[{'n': 3351180, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 79, 101], 'core6': 1675590, 'bucket': '<=P^2/2'}, {'n': 3351348, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 7, 11, 13, 31], 'core6': 186186, 'bucket': '<=P^2/4'}, {'n': 3351414, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 11, 17, 29, 103], 'core6': 3351414, 'bucket': '<P^2'}, {'n': 3351530, 'omega': 6, 'weight': 1, 'first_factors': [2, 5, 7, 13, 29, 127], 'core6': 3351530, 'bucket': '<P^2'}, {'n': 3351720, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 17, 31, 53], 'core6': 837930, 'bucket': '<=P^2/4'}, {'n': 3351790, 'omega': 6, 'weight': 1, 'first_factors': [2, 5, 13, 19, 23, 59], 'core6': 3351790, 'bucket': '<P^2'}, {'n': 3351810, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 11, 1451], 'core6': 3351810, 'bucket': '<P^2'}, {'n': 3352020, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 23, 347], 'core6': 1676010, 'bucket': '<=P^2/2'}, {'n': 3352230, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 17, 313], 'core6': 1117410, 'bucket': '<=P^2/2'}, {'n': 3352440, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 13, 307], 'core6': 838110, 'bucket': '<=P^2/4'}, {'n': 3352570, 'omega': 6, 'weight': 1, 'first_factors': [2, 5, 13, 17, 37, 41], 'core6': 3352570, 'bucket': '<P^2'}, {'n': 3352650, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 31, 103], 'core6': 670530, 'bucket': '<=P^2/4'}]`

### P=5003, row=4822
- omega_hist=`{0: 272, 1: 1190, 2: 1444, 3: 927, 4: 738, 5: 361, 6: 65, 7: 5}`
- samples=`[{'n': 24119480, 'omega': 6, 'weight': 1, 'first_factors': [2, 5, 7, 11, 41, 191], 'core6': 6029870, 'bucket': '<=P^2/4'}, {'n': 24119550, 'omega': 7, 'weight': 6, 'first_factors': [2, 3, 5, 7, 13, 19, 31], 'core6': 51870, 'bucket': '<=P^2/4'}, {'n': 24119634, 'omega': 7, 'weight': 6, 'first_factors': [2, 3, 7, 11, 17, 37, 83], 'core6': 290598, 'bucket': '<=P^2/4'}, {'n': 24119732, 'omega': 6, 'weight': 1, 'first_factors': [2, 7, 13, 23, 43, 67], 'core6': 12059866, 'bucket': '<=P^2/2'}, {'n': 24119810, 'omega': 6, 'weight': 1, 'first_factors': [2, 5, 11, 13, 101, 167], 'core6': 24119810, 'bucket': '<P^2'}, {'n': 24119930, 'omega': 6, 'weight': 1, 'first_factors': [2, 5, 19, 37, 47, 73], 'core6': 24119930, 'bucket': '<P^2'}, {'n': 24119940, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 13, 17, 107], 'core6': 709410, 'bucket': '<=P^2/4'}, {'n': 24119970, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 7, 331, 347], 'core6': 24119970, 'bucket': '<P^2'}, {'n': 24120054, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 7, 23, 29, 41], 'core6': 1148574, 'bucket': '<=P^2/4'}, {'n': 24120096, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 7, 11, 13, 251], 'core6': 1507506, 'bucket': '<=P^2/4'}, {'n': 24120120, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 19, 71, 149], 'core6': 6030030, 'bucket': '<=P^2/4'}, {'n': 24120300, 'omega': 6, 'weight': 1, 'first_factors': [2, 3, 5, 37, 41, 53], 'core6': 2412030, 'bucket': '<=P^2/4'}]`

## 4. 后续义务

- 证明高重惩罚若超过素数数目，则某个 core6 桶在长度 P 窗口中过密。
- 将 core6 过密改写为固定小核心 d 的短倍数/尾锚集中。
- 证明该集中触发 CRTDefect/Tail-anchor，或给出可吸收的统一上界。
