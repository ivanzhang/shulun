# BPN(P) 显式有限闭合证书

**状态：** `bpn_finite_closure_certified_p_le_29`

## 1. 命题

**定理 (BPN 有限闭合)**：对所有奇素数 P ∈ [13, 29]，row_min(P) > P 严格成立。

其中 row_min(P) := 最小 x ≥ 1 使行 N_x := [xP+1, xP+P-1] 内每个整数
都被某 q < P 素数整除。这等价于用户命题 (A) 中对所有 r ∈ {1,...,P-1}, xP+r 有 <P 素因子的最小 x。

## 2. 参数

- `max_p`: `29`
- `max_x_factor`: `200.0` (每个 P 搜索到 x = max_x_factor·P)
- 奇素数总数 P ∈ [13, max_p]: `5`

## 3. 总结

- 在 (P, max_x_factor·P] 内找到 row_min 的 P 数: `5`
- 未在搜索界内找到 row_min 的 P 数: `0`
- BPN(P) 通过 (row_min > P 或未在界内出现) 的 P 数: `5`
- BPN(P) 失败的 P 数: `0`
- BPN 失败的 P: `[]`
- row_min/P 比值范围: `2.5217391304347827` ~ `192.52631578947367`
- row_min/P 比值均值: `91.75365841727861`
- 全部 BPN(P) 严格闭合: `True`

## 4. 算法

1. 构造 SPF[n] = n 的最小素因子，n ∈ [0, max_x_factor·max_p²+max_p]；
2. 对每个奇素数 P ∈ [13, max_p]，扫描 x ∈ [1, max_x_factor·P]；
3. 对每个 x，检查行 [xP+1, xP+P-1] 内每个数 n 是否 SPF[n] < P；
4. 若全部 < P 则 x 是零行；首个这样的 x 即为 row_min(P)；
5. 若无 x ∈ [1, max_x_factor·P] 是零行，则 row_min(P) > max_x_factor·P > P。

**关键修正**：SPF 检测避免漏算 P-coarse 合数。例如 1349 = 19·71
对 P=17 是 P-coarse 合数（最小素因子 19 ≥ P=17），普通素数判定会漏掉它。

## 5. 含 row_min 的具体记录

| P | row_min(P) | row_min/P | 零行窗口 | BPN |
|---:|---:|---:|---|---|
| 13 | 168 | 12.923 | `[2185, 2196]` | ✓ |
| 17 | 1210 | 71.176 | `[20571, 20586]` | ✓ |
| 19 | 3658 | 192.526 | `[69503, 69520]` | ✓ |
| 23 | 58 | 2.522 | `[1335, 1356]` | ✓ |
| 29 | 5209 | 179.621 | `[151062, 151089]` | ✓ |

## 7. 审稿边界

本证书闭合���是：BPN(P) for P ∈ [13, 29] 的逐点数值严格性。

**本证书未闭合**：
- P > max_p 的全局闭合（仍需 BHP/Cramér 类小区间素数下界或独立晋级输入）；
- 闭合的最终原子见 `prime-matrix-three-final-atoms-hard-attack-router.md`。

## 8. 与 monograph 主线的接续

- `BPN(P)` 等价于 (a) 前 P 行无零行；
- (b) 每个 `[xP+1, xP+P-1]` 含 ≥P 素数 OR P-coarse 合数（本范围内只有 P²）；
- (c) 完整覆盖证书最小代表元 ≥ P；
- 见 `prime-matrix-zero-row-full-crt-diagonal-minrep.md`；
- 本证书在 P ∈ [13, max_p] 把上述等价命题闭合为纯计算结果；
- 全局闭合仍需 RKS-log / D-Structure 等数论级开放原子。
