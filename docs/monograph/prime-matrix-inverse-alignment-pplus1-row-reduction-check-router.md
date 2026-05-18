# Prime Matrix inverse alignment 第 P+1 行归约检查证书

**状态：** `pplus1_row_reduction_checked_transfer_missing_open`

旧仓库确实已经把 x=P 特化为第 P+1 行/平方后前半窗问题，并证明该行无全覆盖等价于 (P^2,P^2+P) 内存在素数。但旧仓库没有证明“第 P+1 行非零 => 全部 x<P 非零”。这个方向还需要一个新的非循环相位转移定理：任一早期零行要么强制平方锚 x=P 也零行，要么进入命名 PDEC/SAE/ColumnCRT/source-rank 出口。

```text
old_minrep_equivalence_closed=true
pplus1_row_is_x_equals_p=true
x_equals_p_no_cover_equivalent_to_first_half_prime_square=true
pplus1_nonzero_suffices_for_all_early_rows_proved=false
row_column_unconditional_closed=false
```

## 1. 结论

按当前仓库记号，行乘数 `x` 的窗口是 `xP+r, 1<=r<P`；因此 `x=P` 是一编号第 `P+1` 行，也就是平方锚后首行。
旧材料已经证明 `x=P` 无全覆盖等价于平方后前半窗有素数；这回答了“第 P+1 行”本身的强度。

但这不是全早期窗口的充分条件。若 `x` 改变，所有小素数的覆盖相位同步变为 `rho_q(x)=-xP mod q`；
`x=P` 的负平方相位只是一条特殊相位线，不能自动支配 `1<=x<P` 的全部相位线。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| OldMinRepEquivalenceClosed | `true` | `true` | 旧稿已闭合：最小对齐解 X_0(P)>P 等价于 1<=x<=P 全部非零行，也等价于每个 P 对齐短区间有素数。 | none for equivalence |
| PPlusOneRowIsXEqualsP | `true` | `true` | 按仓库记号，x=P 是一编号第 P+1 行，窗口为 P^2+r, 1<=r<P。 | none for notation |
| XEqualsPNoCoverEquivalentToFirstHalfPrimeSquare | `true` | `true` | 旧稿已闭合：x=P 无全覆盖等价于 (P^2,P^2+P) 内存在素数。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| FinalTailRouteNeedsPPlusOneAsHardInput | `true` | `true` | final-tail 统一下界若要闭合，代入 x=P 必须先得到平方后前半窗素数输入；这是必要阻塞，不是充分归约。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| PPlusOneNonzeroImpliesAllEarlyRowsNonzero | `false` | `false` | 旧仓库没有证明第 P+1 行非零可推出全部 x<P 非零；不同 x 给出不同相位 rho_q(x)=-xP mod q，不能由 x=P 的负平方相位自动控制。 | AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn |
| ValidConditionalReduction | `true` | `false` | 若新增证明：任一 x<P 零行必转移到 x=P 零行，或进入命名 PDEC/SAE/ColumnCRT/source-rank 出口；再排除这些出口，则可由第 P+1 行非零推出早期无零行。 | AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn AND NoZeroRowAtXEqualsP_PlusOneRowAfterSquare |
| LatestNoncycleFrontierPreserved | `true` | `false` | 该检查只新增一个旧路线回流接口；exact-UV 后的 signed-row/source-table/fixed-key 主前沿仍保持开放。 | (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward OR AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步确认旧稿没有把第 P+1 行非零提升为全早期窗口排斥；行/列命题仍未无条件闭合。 | (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward OR AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn OR ActualNoncanonicalPrimitiveEmitterSourceTableLedger OR FixedKeyExactUVLocalMultiplicityO1Ledger OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 有效条件归约

可安全使用的条件命题是：

```text
EarlyZero(x<P)
=> ZeroAtXEqualsP OR NamedReturn(PDEC/SAE/ColumnCRT/source-rank)
```

在该转移定理与命名出口排斥都闭合后，`x=P` 非零才可推出早期无零行。当前缺失项为：

```text
AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn
```

因此本分支的条件闭合基为：

```text
AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn AND NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND PDEC_SAE_ColumnCRT_NamedReturnExclusion
```

与 exact-UV 后最新非循环前沿合并后的活动基为：

```text
((AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward OR AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn) OR ActualNoncanonicalPrimitiveEmitterSourceTableLedger OR FixedKeyExactUVLocalMultiplicityO1Ledger OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一直接主攻

本分支下一主攻：

```text
AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn
```

全局上一主攻仍保留：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
```

并行保留：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward OR ActualNoncanonicalPrimitiveEmitterSourceTableLedger OR FixedKeyExactUVLocalMultiplicityO1Ledger OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch OR SquarePhaseRoughSurvivorUniformLowerBound
```

## 5. 诚实边界

- 本证书确认旧稿存在 `x=P`/第 `P+1` 行等价链。
- 本证书同时确认旧稿没有证明第 `P+1` 行非零足以排除所有 `x<P` 零行。
- 行/列命题仍未全局无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_inverse_alignment_pplus1_row_reduction_check_router.py` | `2891f1f93cd09e75b727ec991351432beb22e4707ab36c32c2675dcf868fd33a` |
| `docs/monograph/prime-matrix-zero-row-minrep-route-review.md` | `cff5609900bcfaa796b6b586c44458727b9807f2f1afd2210e52360dbe5bef26` |
| `docs/monograph/prime-matrix-inverse-alignment-min-x-phase-scan-router.md` | `85b667536392eb61197912532b775a79dabc2c4e4030768d2d3085da7d821083` |
| `docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json` | `ff08e13fd2dbbd7dbbdaf7a1648fc8f339cd2e52eec84a5ba3a0df7873c05d9c` |
| `docs/monograph/prime-matrix-prime-square-x-equals-p-wheel-router.json` | `4544ff30590a112ac0c5329c61505989403a8c2f33942d5769cd77fa9a04e01c` |
| `docs/monograph/prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json` | `2faaae72cd649b0d469ce260b380b6180570c3c180a054ea092f3d0f9af48bd3` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json` | `328ee462d76cb6213f976eee33133885f20109157d16cf80d236ae27d78d8993` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
