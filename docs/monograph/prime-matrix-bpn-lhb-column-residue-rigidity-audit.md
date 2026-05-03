# BPN low-hole bucket 列残基刚性与桥洞交叉审计

**状态：** `bridge_hole_reduced_to_column_residue_max_block_intersection`

补洞残基块由列残基 `c mod ell` 决定。样本中 zero bucket 要么整洞集已有 Hall 亏损，要么处于 Delta(H)=0 临界态且存在桥洞；桥洞是两个高素数最大残基块的公共列。

## 1. 总表

| P | Q | high primes | zero | Delta(H)>0 | Delta(H)=0 | bridged critical | Delta(H)<0 | affine failures | bridge supports |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 2310 | `[]` | 2306 | 2306 | 0 | 0 | 0 | 0 | `{}` |
| 17 | 2310 | `[13]` | 2282 | 2282 | 0 | 0 | 0 | 0 | `{}` |
| 19 | 2310 | `[13, 17]` | 2170 | 2170 | 0 | 0 | 0 | 0 | `{}` |
| 23 | 2310 | `[13, 17, 19]` | 2078 | 2078 | 0 | 0 | 0 | 0 | `{}` |
| 29 | 2310 | `[13, 17, 19, 23]` | 2160 | 2160 | 0 | 0 | 0 | 0 | `{}` |
| 31 | 2310 | `[13, 17, 19, 23, 29]` | 1714 | 1714 | 0 | 0 | 0 | 0 | `{}` |
| 37 | 2310 | `[13, 17, 19, 23, 29, 31]` | 1500 | 1500 | 0 | 0 | 0 | 0 | `{}` |
| 43 | 2310 | `[13, 17, 19, 23, 29, 31, 37, 41]` | 260 | 220 | 40 | 40 | 0 | 0 | `{'(13, 19)': 40}` |
| 47 | 2310 | `[13, 17, 19, 23, 29, 31, 37, 41, 43]` | 44 | 32 | 12 | 12 | 0 | 0 | `{'(13, 19)': 12}` |

## 2. 列残基刚性

由

\[
a_{\ell,c,t}=(1-cP^{-1}-t)Q^{-1}\pmod\ell
\]

可知 `a_{ell,c,t}=a_{ell,c',t}` 当且仅当 `c≡c' mod ell`。
因此高素数 `ell` 的最大覆盖能力为

\[
m_\ell(H)=\max_b |H\cap(b\bmod\ell)|,
\]

与行相位 `t` 只通过低洞集 `H=H_Q(t)` 相关。

## 3. 桥洞交叉命题

若 `Delta(H)=0`，且两个高素数的唯一最大残基块有公共列 `c_*`，
删除 `c_*` 会使两个最大块同时下降，故总容量下降至少 `2`，从而
`Delta(H\{c_*})>0`。

## 4. 临界样例

### P=43

| phase | holes | max blocks | bridge candidates |
| ---: | --- | --- | --- |
| 40 | `[2, 4, 14, 16, 20, 22, 26, 32, 34, 40]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 1, 'cols': [14, 40]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [2, 40]}]}}` | `[{'col': 40, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 1, 'cols': [14, 40]}], '19': [{'residue': 2, 'cols': [2, 40]}]}}]` |
| 153 | `[3, 5, 11, 15, 17, 21, 27, 33, 35, 41]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [15, 41]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 3, 'cols': [3, 41]}]}}` | `[{'col': 41, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 2, 'cols': [15, 41]}], '19': [{'residue': 3, 'cols': [3, 41]}]}}]` |
| 185 | `[1, 7, 9, 15, 21, 25, 27, 31, 37, 39]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 1, 'cols': [1, 27]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 1, 'cols': [1, 39]}]}}` | `[{'col': 1, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 1, 'cols': [1, 27]}], '19': [{'residue': 1, 'cols': [1, 39]}]}}]` |
| 224 | `[4, 10, 12, 18, 24, 28, 30, 34, 40, 42]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 4, 'cols': [4, 30]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 4, 'cols': [4, 42]}]}}` | `[{'col': 4, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 4, 'cols': [4, 30]}], '19': [{'residue': 4, 'cols': [4, 42]}]}}]` |
| 268 | `[2, 8, 10, 16, 22, 26, 28, 32, 38, 40]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [2, 28]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [2, 40]}]}}` | `[{'col': 2, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 2, 'cols': [2, 28]}], '19': [{'residue': 2, 'cols': [2, 40]}]}}]` |
| 407 | `[1, 3, 9, 13, 15, 19, 25, 31, 33, 39]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 0, 'cols': [13, 39]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 1, 'cols': [1, 39]}]}}` | `[{'col': 39, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 0, 'cols': [13, 39]}], '19': [{'residue': 1, 'cols': [1, 39]}]}}]` |
| 416 | `[4, 6, 16, 18, 22, 24, 28, 34, 36, 42]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 3, 'cols': [16, 42]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 4, 'cols': [4, 42]}]}}` | `[{'col': 42, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 3, 'cols': [16, 42]}], '19': [{'residue': 4, 'cols': [4, 42]}]}}]` |
| 460 | `[2, 4, 14, 16, 20, 22, 26, 32, 34, 40]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 1, 'cols': [14, 40]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [2, 40]}]}}` | `[{'col': 40, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 1, 'cols': [14, 40]}], '19': [{'residue': 2, 'cols': [2, 40]}]}}]` |

### P=47

| phase | holes | max blocks | bridge candidates |
| ---: | --- | --- | --- |
| 76 | `[2, 4, 8, 14, 16, 22, 26, 32, 34, 44, 46]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 8, 'cols': [8, 34]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 8, 'cols': [8, 46]}]}}` | `[{'col': 8, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 8, 'cols': [8, 34]}], '19': [{'residue': 8, 'cols': [8, 46]}]}}]` |
| 126 | `[4, 6, 16, 18, 22, 24, 28, 34, 36, 42, 46]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 3, 'cols': [16, 42]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 4, 'cols': [4, 42]}]}}` | `[{'col': 42, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 3, 'cols': [16, 42]}], '19': [{'residue': 4, 'cols': [4, 42]}]}}]` |
| 479 | `[3, 5, 15, 17, 21, 23, 27, 33, 35, 41, 45]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [15, 41]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 3, 'cols': [3, 41]}]}}` | `[{'col': 41, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 2, 'cols': [15, 41]}], '19': [{'residue': 3, 'cols': [3, 41]}]}}]` |
| 505 | `[1, 5, 11, 13, 19, 23, 25, 29, 31, 41, 43]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 5, 'cols': [5, 31]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 5, 'cols': [5, 43]}]}}` | `[{'col': 5, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 5, 'cols': [5, 31]}], '19': [{'residue': 5, 'cols': [5, 43]}]}}]` |
| 1059 | `[1, 3, 7, 13, 15, 21, 25, 31, 33, 43, 45]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 7, 'cols': [7, 33]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 7, 'cols': [7, 45]}]}}` | `[{'col': 7, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 7, 'cols': [7, 33]}], '19': [{'residue': 7, 'cols': [7, 45]}]}}]` |
| 1109 | `[3, 5, 15, 17, 21, 23, 27, 33, 35, 41, 45]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [15, 41]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 3, 'cols': [3, 41]}]}}` | `[{'col': 41, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 2, 'cols': [15, 41]}], '19': [{'residue': 3, 'cols': [3, 41]}]}}]` |
| 1202 | `[2, 6, 12, 14, 20, 24, 26, 30, 32, 42, 44]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 6, 'cols': [6, 32]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 6, 'cols': [6, 44]}]}}` | `[{'col': 6, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 6, 'cols': [6, 32]}], '19': [{'residue': 6, 'cols': [6, 44]}]}}]` |
| 1252 | `[2, 4, 14, 16, 22, 26, 32, 34, 40, 44, 46]` | `{'13': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 1, 'cols': [14, 40]}]}, '19': {'max_size': 2, 'winner_count': 1, 'winners': [{'residue': 2, 'cols': [2, 40]}]}}` | `[{'col': 40, 'capacity_drop': 2, 'support_primes': [13, 19], 'support_blocks': {'13': [{'residue': 1, 'cols': [14, 40]}], '19': [{'residue': 2, 'cols': [2, 40]}]}}]` |
