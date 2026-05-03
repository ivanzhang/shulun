# BPN LHB 低范围最终证书

`13<=P<61` 的 low-hole zero bucket 已分解为整洞集亏损、桥洞临界、精确 DP 临界三类并全部闭合。

## 1. 总览

- `all_pass`: `True`
- `total_zero`: `15414`
- `total_whole_deficit`: `15282`
- `total_bridge_critical`: `108`
- `total_exact_dp_critical`: `24`
- `summary_sha256`: `74c6277349f9ef14a9578598f3250bb67ffb98257f0af34a923d74ddf073efb1`

## 2. 分项表

| P | zero | whole deficit | critical | bridge | exact DP | negative | affine failures | pass |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 2306 | 2306 | 0 | 0 | 0 | 0 | 0 | `True` |
| 17 | 2282 | 2282 | 0 | 0 | 0 | 0 | 0 | `True` |
| 19 | 2170 | 2170 | 0 | 0 | 0 | 0 | 0 | `True` |
| 23 | 2078 | 2078 | 0 | 0 | 0 | 0 | 0 | `True` |
| 29 | 2160 | 2160 | 0 | 0 | 0 | 0 | 0 | `True` |
| 31 | 1714 | 1714 | 0 | 0 | 0 | 0 | 0 | `True` |
| 37 | 1500 | 1500 | 0 | 0 | 0 | 0 | 0 | `True` |
| 41 | 892 | 812 | 80 | 56 | 24 | 0 | 0 | `True` |
| 43 | 260 | 220 | 40 | 40 | 0 | 0 | 0 | `True` |
| 47 | 44 | 32 | 12 | 12 | 0 | 0 | 0 | `True` |
| 53 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `True` |
| 59 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | `True` |

## 3. 证书解释

- `whole deficit`：整洞集满足 `Delta(H)>0`，直接 Hall 亏损闭合。
- `bridge`：`Delta(H)=0`，但存在桥洞使删一洞后容量下降至少 `2`。
- `exact DP`：有限临界例外；由完整残基类 set-cover DP 证明无补洞选择。

`P=41` 出现 `24` 个非桥洞临界相位，这是旧“整洞集或桥洞”表述的唯一低范围修正点；
这些相位已由精确 DP 有限证书闭合，不再作为结构性未证缺口。

## 4. 临界样例

### P=41

| phase | holes | delta | bridge candidates |
| ---: | --- | ---: | --- |
| 70 | `[2, 4, 8, 10, 14, 22, 28, 32, 38, 40]` | 0 | `[]` |
| 99 | `[1, 3, 9, 13, 15, 25, 31, 33, 39]` | 0 | `[{'col': 39, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 0, 'cols': [13, 39]}], '19': [{'residue': 1, 'cols': [1, 39]}]}}]` |
| 100 | `[2, 4, 10, 14, 20, 28, 32, 34, 38, 40]` | 0 | `[]` |
| 111 | `[1, 3, 7, 9, 13, 21, 27, 31, 37, 39]` | 0 | `[]` |

### P=43

| phase | holes | delta | bridge candidates |
| ---: | --- | ---: | --- |
| 40 | `[2, 4, 14, 16, 20, 22, 26, 32, 34, 40]` | 0 | `[{'col': 40, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 1, 'cols': [14, 40]}], '19': [{'residue': 2, 'cols': [2, 40]}]}}]` |
| 153 | `[3, 5, 11, 15, 17, 21, 27, 33, 35, 41]` | 0 | `[{'col': 41, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 2, 'cols': [15, 41]}], '19': [{'residue': 3, 'cols': [3, 41]}]}}]` |
| 185 | `[1, 7, 9, 15, 21, 25, 27, 31, 37, 39]` | 0 | `[{'col': 1, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 1, 'cols': [1, 27]}], '19': [{'residue': 1, 'cols': [1, 39]}]}}]` |
| 224 | `[4, 10, 12, 18, 24, 28, 30, 34, 40, 42]` | 0 | `[{'col': 4, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 4, 'cols': [4, 30]}], '19': [{'residue': 4, 'cols': [4, 42]}]}}]` |

### P=47

| phase | holes | delta | bridge candidates |
| ---: | --- | ---: | --- |
| 76 | `[2, 4, 8, 14, 16, 22, 26, 32, 34, 44, 46]` | 0 | `[{'col': 8, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 8, 'cols': [8, 34]}], '19': [{'residue': 8, 'cols': [8, 46]}]}}]` |
| 126 | `[4, 6, 16, 18, 22, 24, 28, 34, 36, 42, 46]` | 0 | `[{'col': 42, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 3, 'cols': [16, 42]}], '19': [{'residue': 4, 'cols': [4, 42]}]}}]` |
| 479 | `[3, 5, 15, 17, 21, 23, 27, 33, 35, 41, 45]` | 0 | `[{'col': 41, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 2, 'cols': [15, 41]}], '19': [{'residue': 3, 'cols': [3, 41]}]}}]` |
| 505 | `[1, 5, 11, 13, 19, 23, 25, 29, 31, 41, 43]` | 0 | `[{'col': 5, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 5, 'cols': [5, 31]}], '19': [{'residue': 5, 'cols': [5, 43]}]}}]` |

## 5. 审稿结论

该证书完成 `P<61` 低范围义务。结合窄带、尾段有限证书与显式常数包后，
low-hole bucket 主线剩余只剩 `P>=13208` 的外部显式 Mertens/prime-count 引用核验。
