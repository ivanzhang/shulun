# Prime Matrix square-phase off-band prefix gap shadow selector H/T external input match router

**状态：** `selector_ht_hardpoint_reduced_to_square_window_tail_dominance_open_global`

本步把 W 专属 H/T 硬点精确改写为平方窗-尾素数支配：`H=pi(P^2±window)`，`T=pi(P-1)-pi(floor(4P/5))`。常见外部短区间存在性输入不直接匹配；真正需要的是 selector residue 上的平方窗计数支配。

```text
max_p=5000
prime_rho_hit_count=344
formula_failure_count=0
dominance_failure_count=0
min_square_window_tail_dominance_margin=0
zero_margin_count=1
known_standard_external_match_count=0
row_column_unconditional_closed=false
```

## 1. 精确计数接口

对 `side=plus`：

```text
H = pi(P^2+P-1)-pi(P^2)
```

对 `side=minus`：

```text
H = pi(P^2-1)-pi(P^2-P)
```

共同的尾素数项为：

```text
T = pi(P-1)-pi(floor(4P/5))
```

因此下一层目标不是普通“有一个素数”，而是 selector rho 命中时的计数支配：

```text
H - 2T - (3-2W) >= 0.
```

## 2. side/W 余量

| side | W | hits | min margin | max margin | zero margin | p at min |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| minus | 2 | 252 | 1 | 84 | 0 | `[157]` |
| plus | 1 | 92 | 0 | 81 | 1 | `[173]` |

## 3. 外部输入匹配审查

| input | matches | reason |
| --- | ---: | --- |
| `Baker-Harman-Pintz x^0.525 prime gap` | `false` | 可给长度约 (P^2)^0.525=P^1.05 的存在性，不能推出长度 P 的平方窗素数计数下界，更不能比较到 2T。 |
| `Legendre-type prime in every (n^2,(n+1)^2)` | `false` | 即使给每个平方间隙至少一个素数，也远弱于 H >= 2T + O(1) 的计数支配。 |
| `RH/Schoenfeld-style explicit formula error` | `false` | 平方窗长度为 sqrt(x)；RH 级误差通常仍大于主项 P/log P，不能直接保证该短窗计数下界。 |
| `ordinary PNT or arithmetic progression PNT` | `false` | 只给长区间或平均意义，不能逐点控制每个 selector residue 上的 P 长度平方窗。 |
| `SelectorResidueSquareWindowTailDominance` | `true` | 精确需要证明 selector rho 命中时，平方窗计数 H 至少支配尾素数计数 2T 加 W 专属常数。 |

## 4. 低余量样本

| template | p | side | rho | W | H | T | margin | slack |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 173 | plus | 2 | 1 | 13 | 6 | 0 | 0 |
| 1 | 157 | minus | 7 | 2 | 12 | 6 | 1 | 1 |
| 2 | 157 | plus | 7 | 1 | 14 | 6 | 1 | 1 |
| 3 | 157 | plus | 7 | 1 | 14 | 6 | 1 | 1 |
| 6 | 157 | minus | 7 | 2 | 12 | 6 | 1 | 1 |
| 2 | 1777 | plus | 7 | 1 | 104 | 51 | 1 | 1 |
| 3 | 1777 | plus | 7 | 1 | 104 | 51 | 1 | 1 |
| 0 | 677 | minus | 2 | 2 | 45 | 22 | 2 | 2 |
| 5 | 677 | minus | 2 | 2 | 45 | 22 | 2 | 2 |
| 2 | 1327 | plus | 7 | 1 | 79 | 38 | 2 | 2 |
| 3 | 1327 | plus | 7 | 1 | 79 | 38 | 2 | 2 |
| 1 | 277 | minus | 7 | 2 | 24 | 11 | 3 | 3 |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `h_t_prime_count_identity` | `closed` | H equals the P-length square-window prime count and T equals the tail prime count pi(P-1)-pi(floor(4P/5)). |
| `external_input_shape_audit` | `closed` | Common short-interval existence inputs do not match the required square-window tail-dominance count inequality. |
| `selector_residue_square_window_tail_dominance` | `open` | A global proof must establish the dominance inequality on selector rho hits, or register recurrent boundary failure as PDEC. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `HTPrimeCountIdentityClosed` | `true` | `true` | H/T 已精确写成素数计数函数差。 | closed |
| `KnownExternalInputsMatch` | `false` | `false` | BHP、Legendre 型存在性、RH/PNT 误差均不直接给所需计数支配。 | need exact square-window tail-dominance input |
| `CurrentDominanceHolds` | `true` | `true` | 当前有限前沿的 selector rho 命中满足平方窗-尾素数支配。 | closed on current finite sweep |
| `GlobalDominanceProved` | `false` | `false` | 仍需全局证明该支配，或把反复失败登记为边界 PDEC。 | SelectorResidueSquareWindowTailDominanceOrBoundaryPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成外部输入形状匹配审查，不关闭全局行/列命题。 | SelectorResidueSquareWindowTailDominanceOrBoundaryPDEC |

## 7. 下一步

- 主攻：`SelectorResidueSquareWindowTailDominanceOrBoundaryPDEC`。
- 内部路线：利用 selector residue、低轮、prefix atom 与平方窗相位共同约束证明上述计数支配。
- 外部路线：必须提供同形状的平方窗-尾素数支配输入；普通短区间存在性、BHP、RH/PNT 不能直接替代。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py` | `5f53bd13fef7ac641fb9bf25f0d67d25e79d4e2d8977b667785fd6c93ded5529` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_boundary_source_router.py` | `2bceab09fed0b827d59f89c9773ff04445231ad8a632d28c345858d49382b9c3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-boundary-source-ledger.json` | `289702f6150d001371716152f404434422d303fd31397394119cdcad90d596d3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json` | `dcdf4b1ded2c507ba24399bf075a29d392a08c69174fbfcc6aef9dd96a1e5e4b` |
