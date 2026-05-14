# Prime Matrix square-phase moving cutoff dyadic 缺陷路由器

**状态：** `moving_cutoff_defect_reduced_to_dyadic_negative_square_phase_deletion_excess_pdec_open`

moving cutoff 亏损可由归一化幸存比的 telescoping 精确抽取到某个 dyadic 素数块。若固定低模前缀已吸收，而最终 `G(P)` 仍低于 Mertens 主项安全余量，则至少一个移动块 `(z,2z]` 的实际条件删除率超过独立模型，形成`DyadicNegativeSquarePhaseDeletionExcessPDEC`。该 dyadic 块缺陷尚未排斥。

```text
moving_cutoff_telescoping_identity_closed=true
deficit_forces_dyadic_block_drop=true
dyadic_negative_square_phase_defect_excluded=false
row_column_unconditional_closed=false
```

## 1. 抽取引理

取 dyadic cutoff `z_0<z_1<...<z_J=floor(P/e)`，定义

```text
G_j = #{1<=k<P: k != -P^2 mod q for all q<=z_j}
V_j = prod_{q<=z_j}(1-1/q)
R_j = G_j / ((P-1)V_j).
```

则

```text
R_J/R_0 = prod_{j=0}^{J-1} R_{j+1}/R_j.
```

所以若 `R_0` 已由固定低模吸收而 `R_J` 仍异常低，则某个 dyadic block 的 `R_{j+1}/R_j` 异常小；这就是单块条件过删证书。

## 2. 样本 profile

| P | y | cutoffs | final survivors | final normalized | worst block cutoff | worst block ratio |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 3681 | 8 | 660 | 0.966756 | 3681 | 0.966283 |
| 36739 | 13515 | 10 | 2040 | 0.941552 | 7936 | 0.969395 |
| 83561 | 30740 | 11 | 4183 | 0.921632 | 30740 | 0.965832 |
| 200003 | 73576 | 13 | 9512 | 0.949484 | 63488 | 0.969569 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `MovingCutoffTelescopingIdentityClosed` | `true` | `true` | 归一化幸存比 R_j=G_{z_j}/((P-1)V(z_j)) 满足 R_J/R_0=prod_j R_{j+1}/R_j。 | none |
| `DeficitForcesDyadicBlockDrop` | `true` | `true` | 若 fixed 前缀正常而 final 亏损，则某个 dyadic block 的条件删除率超过独立模型平均。 | DyadicNegativeSquarePhaseDeletionExcessPDEC |
| `DyadicBlockDefectMaterializedAsPDEC` | `true` | `false` | 该单块过删是固定端点负平方相位在一个移动素数块中的非零频率/二次字符偏置。 | DyadicNegativeSquarePhaseDeletionExcessPDEC |
| `DyadicNegativeSquarePhaseDefectExcluded` | `false` | `false` | 尚未证明所有移动 dyadic 块都无过删，或排斥其 PDEC 证书。 | DyadicNegativeSquarePhaseDeletionExcessPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未排除 dyadic LDG defect 与 reciprocal-floor RFP defect。 | LDG dyadic defect + RFP reciprocal-floor defect |

## 4. 下一步

- 直接攻 `DyadicNegativeSquarePhaseDeletionExcessPDEC`：对单个移动 dyadic 素数块证明条件删除率不可能持续超过独立模型，或把失败登记为 PDEC。
- 这一步已经把 moving cutoff 的全局亏损压成单块局部相位偏差，不再是整条筛链的模糊亏损。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.json` | `2dc182ebbbc8cbe41ffb06bd569bb7871a33519e2b1d4fb0d678a31703488c0e` |
| `docs/monograph/prime-matrix-square-phase-ldg-mertens-product-margin-router.json` | `4adf2c1f55f8d273de3261b7662a8bfe6cd216be6add4e30e1af2a079b1871b3` |
| `docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json` | `1262152377e4b7477fef34bd370861bd1829bb06a3b964c19dc833db2cb2128d` |
| `experiments/prime_matrix_square_phase_moving_cutoff_dyadic_defect_router.py` | `ef53d5618f76059b34632c128253d8c35089e77baa0545faf187bd5223ce4f3b` |
