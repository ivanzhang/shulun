# Prime Matrix square-phase LDG Mertens 乘积余量路由器

**状态：** `ldg_mertens_product_margin_external_closed_phase_discrepancy_open`

接受 Rosser-Schoenfeld 型外部 Mertens 乘积不等式时，`y=floor(P/e)` 的完整周期密度从 `P>=2003` 起严格高于 `0.48/logP`。代数余量本身很宽，因此 LDG 剩余不再是主项常数，而是短区间负平方相位实际计数 `G(P)` 相对完整周期主项的亏损。严格自足路线仍需内联该外部乘积不等式的证明。

```text
rosser_schoenfeld_product_inequality_matched=true
algebraic_margin_for_p_ge_2003_closed=true
explicit_mertens_product_ledger_external_closed=true
explicit_mertens_product_ledger_self_contained_proved=false
ldg_lower_current_corpus_proved=false
row_column_unconditional_closed=false
```

## 1. 外部输入

使用的外部口径为 Rosser-Schoenfeld/Dusart 型显式 Mertens 乘积下界：

```text
prod_{q<=x}(1-1/q) > 1/(e^gamma log x + 2.50637/log x).
```

本文件只完成该输入与 LDG 常数的参数匹配；若走严格自足路线，还必须内联证明该外部不等式。

## 2. 余量样本

| P | y=floor(P/e) | RS lower | 0.48/logP | surplus | ratio |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2003 | 736 | 0.082393015126 | 0.063137945342 | 0.019255069784 | 1.304968 |
| 5003 | 1840 | 0.072872207140 | 0.056352625540 | 0.016519581601 | 1.293147 |
| 10007 | 3681 | 0.066981363295 | 0.052111378669 | 0.014869984626 | 1.285350 |
| 20011 | 7361 | 0.061957594916 | 0.048465083536 | 0.013492511380 | 1.278397 |
| 100000 | 36787 | 0.052735259590 | 0.041692270263 | 0.011042989327 | 1.264869 |
| 1000000 | 367879 | 0.043438744025 | 0.034743558552 | 0.008695185473 | 1.250268 |
| 10000000 | 3678794 | 0.036910980474 | 0.029780193045 | 0.007130787429 | 1.239447 |

## 3. 单调代数

令 `L=logP`。因 `floor(P/e)<=P/e` 且乘积下界分母在本区间单调递增，只需验证

```text
F(L)=L-0.48(e^gamma(L-1)+2.50637/(L-1)) > 0.
```

`P>=2003` 时 `L>=log2003`，且 `F(log2003)>0`、`F'(L)>0`，故全尾段成立。

| item | value | meaning |
| --- | ---: | --- |
| `L0` | 7.602401335666 | L=log P at P0=2003 |
| `t0` | 6.602401335666 | t=L-1 upper bound for log floor(P/e) |
| `F(L0)` | 1.775695820554 | F(L)=L-0.48(e^gamma(L-1)+2.50637/(L-1)) |
| `coarse_derivative_lower` | 0.145085239365 | 1-0.48e^gamma; positive lower bound for F'(L) after dropping the positive term |
| `exact_derivative_at_L0` | 0.172683555242 | F'(L0), also positive |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RosserSchoenfeldProductInequalityMatched` | `true` | `false` | 若接受外部乘积不等式 prod_{q<=x}(1-1/q)>1/(e^gamma log x+2.50637/log x)，则可接入本门。 | external theorem accepted OR self-contained proof |
| `AlgebraicMarginForPGe2003Closed` | `true` | `true` | 用 y=floor(P/e)<=P/e 与单调性，P>=2003 时外部乘积下界严格大于 0.48/logP。 | none |
| `ExplicitMertensProductLedgerExternalClosed` | `true` | `false` | 在接受 Rosser-Schoenfeld 外部输入时，LDG 主项常数余量关闭。 | self-contained Rosser-Schoenfeld/Dusart proof appendix if strict route |
| `LDGLowerStillNeedsPhaseDiscrepancy` | `false` | `false` | 完整周期主项余量不等于短区间实际 G(P) 下界；还需排斥负平方相位覆盖过量。 | NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 没有排除相位亏损和 RFP 过密出口，不能声明行/列命题无条件闭合。 | NegativeSquarePhase defect AND ReciprocalFloor defect exclusions |

## 5. 下一步

- 主项常数余量在外部 Mertens 输入下已经不是硬点；继续攻 `NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC`。
- 严格自足路线若不接受外部输入，则需补 `SelfContainedRosserSchoenfeldMertensProductProofAppendix`。
- 即使 Mertens 主项关闭，LDG 仍需证明短区间负平方相位实际亏损不会吞掉该余量。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-b3-explicit-prime-reciprocal-mertens-router.md` | `d7a0900a55a3d0765a9fc8ee80f3e0b492d9266ac0b3ccb61feda4d06ef1ad5f` |
| `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` | `8e9a5381b104901ab29fd2734fd159bb1a9ddff93907e750834283f970ebf92c` |
| `docs/monograph/prime-matrix-square-phase-ldg-beta-level-barrier-router.json` | `a1ec417a7099e683d4053147b2ac6dce5f88e7b23c4e2867a61bc86190ef8779` |
| `docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json` | `1262152377e4b7477fef34bd370861bd1829bb06a3b964c19dc833db2cb2128d` |
| `experiments/prime_matrix_square_phase_ldg_mertens_product_margin_router.py` | `695c751614b2cc203a84e1ab5a859a9c3937fa086698df72dceabcfff9e17564` |
