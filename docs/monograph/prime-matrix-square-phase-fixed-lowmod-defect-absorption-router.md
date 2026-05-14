# Prime Matrix square-phase 固定低模亏损吸收路由器

**状态：** `fixed_lowmod_prefix_defect_absorbed_moving_cutoff_defect_open`

固定低模前缀不能是 LDG 持续亏损的终端来源。对任意固定 cutoff D，设 M_D=prod_{q<=D}q，则避开全部 `-P^2 mod q` 的列数是 `floor((P-1)/M_D)phi(M_D)+O(M_D)`，因此固定前缀偏差为 O(M_D)。任何 `P/logP` 级持续亏损最终都必须来自随 P 增长的 moving cutoff 或尾筛层，而不是某个固定 CRT 周期。该 moving defect 尚未排斥。

```text
fixed_lowmod_prefix_exact_crt_counting_closed=true
fixed_lowmod_persistent_defect_absorbed=true
moving_cutoff_defect_is_necessary=true
negative_square_phase_defect_excluded=false
row_column_unconditional_closed=false
```

## 1. 固定低模精确计数

固定 `D`，记

```text
M_D = prod_{q<=D} q,
H_D(P) = #{1<=k<P: k != -P^2 mod q for every q<=D}.
```

每个完整 `M_D` 周期内恰有 `phi(M_D)` 个允许列，故

```text
H_D(P)=floor((P-1)/M_D) phi(M_D)+E_D(P), |E_D(P)|<=M_D.
```

这说明固定低模只产生有界周期误差；若出现 `P/logP` 级持续亏损，必然不是固定周期相位可解释的。

## 2. 样本阈值

下表用保守余量尺度 `0.01 P/logP` 比较固定周期误差 `M_D`。

| D | primes<=D | M_D | phi(M_D)/M_D | error bound | threshold for M_D<=cP/logP |
| ---: | --- | ---: | ---: | ---: | ---: |
| 5 | `[2, 3, 5]` | 30 | 0.266666666667 | 30 | 31028 |
| 7 | `[2, 3, 5, 7]` | 210 | 0.228571428571 | 210 | 261998 |
| 11 | `[2, 3, 5, 7, 11]` | 2310 | 0.207792207792 | 2310 | 3479409 |
| 13 | `[2, 3, 5, 7, 11, 13]` | 30030 | 0.191808191808 | 30030 | 53435331 |
| 17 | `[2, 3, 5, 7, 11, 13, 17]` | 510510 | 0.180525356996 | 510510 | 1060964564 |
| 19 | `[2, 3, 5, 7, 11, 13, 17, 19]` | 9699690 | 0.171024022417 | 9699690 | 23148500131 |
| 23 | `[2, 3, 5, 7, 11, 13, 17, 19, 23]` | 223092870 | 0.163588195356 | 223092870 | 605225685680 |
| 29 | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]` | 6469693230 | 0.157947223102 | 6469693230 | 19808340104455 |
| 31 | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]` | 200560490130 | 0.152852151389 | 200560490130 | 685127181413609 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedLowModPrefixExactCRTCountingClosed` | `true` | `true` | 固定 D 时，避开 q<=D 的负平方相位列数等于完整 CRT 周期计数加 O(M_D)。 | none |
| `FixedLowModPersistentDefectAbsorbed` | `true` | `true` | 对任何固定 D，O(M_D) 误差最终小于任意 cP/logP 级亏损；低范围只能进有限 SAE。 | finite threshold for chosen D |
| `MovingCutoffDefectIsNecessary` | `true` | `false` | 若 LDG 亏损无限持续，不能归咎于固定低模周期；必须在 D 随 P 增长的 moving cutoff 或尾筛层发生。 | MovingCutoffNegativeSquarePhaseDefectOrTailSievePDEC |
| `NegativeSquarePhaseDefectExcluded` | `false` | `false` | moving cutoff 负平方相位亏损尚未排斥。 | MovingCutoffNegativeSquarePhaseDefectOrTailSievePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未排除 LDG moving defect 与 RFP reciprocal-floor defect。 | moving LDG defect + RFP defect |

## 4. 下一步

- 主攻 `MovingCutoffNegativeSquarePhaseDefectOrTailSievePDEC`：证明随 `P` 增长的负平方相位 moving cutoff 亏损不可能持续，或把它登记为可排斥 PDEC/SAE。
- 固定低模分支已经不是无限尾段硬点；低范围阈值以下只能作为有限 SAE 处理。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` | `8e9a5381b104901ab29fd2734fd159bb1a9ddff93907e750834283f970ebf92c` |
| `docs/monograph/prime-matrix-square-phase-ldg-mertens-product-margin-router.json` | `4adf2c1f55f8d273de3261b7662a8bfe6cd216be6add4e30e1af2a079b1871b3` |
| `docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json` | `1262152377e4b7477fef34bd370861bd1829bb06a3b964c19dc833db2cb2128d` |
| `experiments/prime_matrix_square_phase_fixed_lowmod_defect_absorption_router.py` | `d0a85d7ddb90455df0c8ac818cba49020fd9c3364f904f2a1bd35e01c7c1b7c4` |
