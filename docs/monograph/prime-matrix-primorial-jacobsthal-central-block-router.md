# Prime Matrix primorial Jacobsthal central block router

**状态：** `primorial_standard_block_closed_global_max_false_special_phase_open`

本步严格吸收 primorial 新思考：`M=prod_{i<=k}p_i` 时，`M±a` 对 `2<=a<p_{k+1}` 必有 `<=p_k` 的素因子，这是标准中心覆盖块。但该块不是周期内全局最长覆盖块；精确扫描在 `k=5,p_k=11,M=2310` 已给出`114..126` 长度 `13` 的覆盖块，超过标准块长度 `11`。因此不能用“标准块最大”直接闭合平方锚命题。可保留的正确接口是 Jacobsthal 接口：对 `P=p_{k+1}`，若能证特殊平方相位 `P^2` 不落入 `prod_{q<P}q` 周期中任何长度 `P-1` 的低筛覆盖块，或该相位对齐必回流 PDEC/SAE/ColumnCRT，则可继续推进。

```text
max_k=8
standard_block_identity_failure_count=0
central_not_global_max_count=4
global_jacobsthal_square_length_failure_count=4
row_column_unconditional_closed=false
```

## 1. 标准中心覆盖块

设

```text
M_k = p_1 p_2 ... p_k.
```

若 `2<=a<p_{k+1}`，则 `a` 的某个素因子必不超过 `p_k`。因此该素因子整除 `M_k` 且整除 `a`，从而整除 `M_k+a` 与 `M_k-a`。所以 `M_k±[2,p_{k+1}-1]` 确实形成标准低筛覆盖块。

## 2. 不能使用的最大块假设

标准块不总是最大块。最早反例为：

```text
k=5, p_k=11, M=2310
standard block length=11
exact max covered run=13
first max block=114..126
```

因此“中心标准块就是周期最大块”不能作为目标命题的闭合输入。它只能提供一个下界和相位对照。

## 3. 精确扫描表

| k | p_k | p_{k+1} | M_k | standard length | exact max run | first max block | central max? | G>=P-1? |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 1 | 2 | 3 | 2 | 1 | 1 | 2..2 | `true` | `false` |
| 2 | 3 | 5 | 6 | 3 | 3 | 2..4 | `true` | `false` |
| 3 | 5 | 7 | 30 | 5 | 5 | 2..6 | `true` | `false` |
| 4 | 7 | 11 | 210 | 9 | 9 | 2..10 | `true` | `false` |
| 5 | 11 | 13 | 2310 | 11 | 13 | 114..126 | `false` | `true` |
| 6 | 13 | 17 | 30030 | 15 | 21 | 9440..9460 | `false` | `true` |
| 7 | 17 | 19 | 510510 | 17 | 25 | 217128..217152 | `false` | `true` |
| 8 | 19 | 23 | 9699690 | 21 | 33 | 60044..60076 | `false` | `true` |

## 4. 与平方锚目标的严格接口

平方锚窗口 `P^2±r, 1<=r<P` 中，若存在一个数与所有 `q<P` 互素，则该数必为素数：因为若它合成，则所有素因子都大于 `P`，乘积已经超过相应平方邻域。

所以一个足够强但通常不可用的闭合条件是：

```text
G(prod_{q<P} q) < P-1.
```

这里 `G(prod_{q<P} q)` 是模低素数 primorial 周期内最长低筛覆盖块长度。精确小样本已显示该全周期强界很快失败，因此真正剩余必须利用 `P^2` 的特殊相位，而不是要求全周期所有相位都安全。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `primorial_standard_block_identity` | `closed` | For M=prod_{i<=k} p_i, every integer M±a with 2<=a<p_{k+1} has a prime factor <=p_k. |
| `standard_block_maximality_refuted` | `closed_by_counterexample` | The standard block 2..p_{k+1}-1 is not always the longest covered block in the primorial period; k=5 already gives a longer block. |
| `jacobsthal_interface_for_square_anchor` | `closed` | For P=p_{k+1}, a global bound G(prod_{q<P}q)<P-1 would imply a square-anchor survivor in every phase, hence a prime in P^2±(1..P-1). |
| `global_jacobsthal_bound_too_strong` | `closed_boundary` | Exact small-k data and known Jacobsthal tables show G(prod_{q<P}q) can exceed P-1, so the target needs special P^2 phase avoidance rather than a uniform period-wide bound. |
| `special_phase_jacobsthal_avoidance` | `open` | A global proof still needs to show the square phase P^2 is not aligned with any length P-1 covered block, or route such alignment to PDEC/SAE/ColumnCRT. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PrimorialStandardBlockIdentityClosed` | `true` | `true` | `M±a` 的标准块确实由 `a` 的小素因子支付。 | closed |
| `CentralBlockGlobalMaxClaimRejected` | `true` | `true` | 标准块不是全局最大块；不能把该直觉作为无条件闭合输入。 | closed by k=5 counterexample |
| `UniformJacobsthalWouldCloseSquareWindow` | `true` | `true` | 若能证 `prod_{q<P}q` 周期内所有低筛覆盖块长度都小于 `P-1`，平方锚窗口自动有素数。 | closed implication only |
| `UniformJacobsthalBoundAvailable` | `false` | `false` | 该强上界与已知/有限 Jacobsthal 数据不兼容，不能作为当前路线。 | not available |
| `SpecialSquarePhaseAvoidanceProved` | `false` | `false` | 真正可攻点变为 `P^2` 特殊相位避开长覆盖块，或长覆盖块相位回流 PDEC。 | SpecialSquarePhaseAvoidsLongPrimorialJacobsthalBlocksOrPhasePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步排除错误最大块假设，并给出 Jacobsthal 接口；不关闭全局行/列命题。 | SpecialSquarePhaseAvoidsLongPrimorialJacobsthalBlocksOrPhasePDEC |

## 7. 下一步

- 主攻：`SpecialSquarePhaseAvoidsLongPrimorialJacobsthalBlocksOrPhasePDEC`。
- 也就是证明特殊相位 `P^2 mod prod_{q<P}q` 不会落入长度 `P-1` 的低筛覆盖块；若落入，则必须登记为相位 PDEC/SAE/ColumnCRT。
- 这条路可以和当前 `TotalPressureSupportPDECExclusion` 合并：长低筛覆盖块若覆盖平方锚窗口，同时必须解释激活尾支撑 `Q_side(P)` 的异常高素负载。
- 当前仍未证明全局行/列无条件闭合。

## 8. 外部参照

- OEIS A058989：最长连续整数段，每个数都被不超过第 n 个素数的某个素数整除。
- OEIS A048670：上述长度加一，即 Jacobsthal 函数作用于前 n 个素数乘积。
- Ziller--Morack, arXiv:1611.03310：Jacobsthal 函数计算算法与附属数据，本仓库已有 RPZ-BCB 接口使用该数据作风险扫描。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_primorial_jacobsthal_central_block_router.py` | `ebcb95e8dea43d0948bf00d25c1b40866fcfc51fff4bd97d7401f00203abf82b` |
| `data/primorial-jacobsthal-central-block-ledger.json` | `6d3166062bd28908f3783e6fdb40e27ec355af8b0cf9504a2378a101d7253fcd` |
