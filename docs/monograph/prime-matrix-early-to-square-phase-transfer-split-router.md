# Prime Matrix early-to-square 相位转移首破裂分裂证书

**状态：** `early_to_square_transfer_split_to_first_break_phase_slip_open`

早期零行到平方锚的抽象转移已被压成首破裂分裂：若零行块从某个 x0<P 一直延续到 x=P，则得到 square-zero；否则存在首个破裂行 y，释放列形成单位相位滑移缺陷，并按旧 early-zero phase-defect schema 进入 PDEC/SAE/ColumnCRT/LocalSurvivor 命名回流。因此当前剩余不再是抽象 transfer，而是排斥 first-break phase-slip 命名终端。

```text
contiguous_zero_block_dichotomy_closed=true
persist_to_square_implies_square_zero=true
first_break_release_set_nonempty=true
unit_phase_slip_formula_closed=true
phase_slip_schema_admission_imported=true
transfer_proved_as_contradiction=false
row_column_unconditional_closed=false
```

## 1. 分裂定理

假设存在早期零行 `x0<P`。从 `x0` 逐行推进到 `P`：

```text
若所有 x0<=t<=P 都是零行 => x=P 是平方锚零行。
否则令 y 为首个非零行；则 y-1 是零行，y 有非空释放列集。
```

对释放列 `c`，上一行由某个 `q<P` 覆盖，而当前行不再被任何 `q<P` 覆盖。
相位公式为：

```text
rho_q(t) = -tP mod q,   rho_q(t+1)=rho_q(t)-P mod q.
```

因此首破裂不是新的自由出口，而是单位相位滑移造成的边界非覆盖缺陷。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TransferTargetImported | `true` | `false` | 上一证书确认第 P+1 行非零不能直接推出全早期非零；缺失项就是早期零行到平方锚的非循环转移。 | AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn |
| ContiguousZeroBlockDichotomyClosed | `true` | `true` | 若某个 x0<P 是零行，则从 x0 向 P 前进：要么每一行都保持零行直到 x=P，要么存在首个破裂行 y<=P。 | ZeroAtXEqualsP OR RegisteredFirstBreakUnitPhaseSlipPDECSAELocalSurvivorReturn |
| PersistToSquareImpliesSquareZero | `true` | `true` | 若零行块一直延续到 x=P，则平方锚第 P+1 行就是零行；这正是已分离的 square-anchor 分支。 | ZeroAtXEqualsP |
| FirstBreakReleaseSetNonempty | `true` | `true` | 若 x=P 非零且前面存在零行，则首个破裂行 y 有非空释放列集；上一行 y-1 仍为零行。 | RegisteredFirstBreakUnitPhaseSlipPDECSAELocalSurvivorReturn |
| ReleasedColumnsArePrimeSurvivorsBeforeOrAtSquare | `true` | `true` | 释放列 c 在行 y 不再被任何 q<P 覆盖；若 y<P，则 yP+c<P^2 且为素数，若 y=P，则为平方锚幸存素数。 | prime survivor / square-anchor survivor |
| UnitPhaseSlipFormulaClosed | `true` | `true` | 从 y-1 到 y，每个小模 q 的覆盖相位按 rho_q(y)=rho_q(y-1)-P mod q 单位滑移；释放列正是该滑移造成的边界非覆盖。 | none for formula |
| PhaseSlipSchemaAdmissionImported | `true` | `true` | 早期零行的同 formal-unit 相位缺陷准入旧证书已把稳定短复现/无自同构边界缺陷登记到 PDEC/SAE/ColumnCRT。 | EarlyZeroTerminalExclusionPackage |
| AbstractTransferReduced | `true` | `false` | 抽象 transfer 不再保留：它被分裂为 square-zero 分支或首破裂 phase-slip 命名回流。 | NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND FirstBreakPhaseSlipNamedReturnExclusion |
| TransferProvedAsContradiction | `false` | `false` | 本步只完成分裂和命名回流；尚未排斥首破裂 phase-slip 的 PDEC/SAE/LocalSurvivor 终端。 | FirstBreakPhaseSlipNamedReturnExclusion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 first-break 命名终端，或继续完成 signed-row/source-rank 主前沿。 | (FirstBreakPhaseSlipNamedReturnExclusion OR AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward OR ActualNoncanonicalPrimitiveEmitterSourceTableLedger OR FixedKeyExactUVLocalMultiplicityO1Ledger OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 新活动基

抽象 transfer 分支压成：

```text
(NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND FirstBreakPhaseSlipNamedReturnExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND FirstBreakPhaseSlipNamedReturnExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一直接主攻

本分支下一主攻：

```text
FirstBreakPhaseSlipNamedReturnExclusion
```

全局上一主攻仍保留：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
```

并行保留：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward OR ActualNoncanonicalPrimitiveEmitterSourceTableLedger OR FixedKeyExactUVLocalMultiplicityO1Ledger OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch
```

## 5. 诚实边界

- 本证书不证明早期零行不存在。
- 本证书只把早期到平方锚的抽象转移压成 square-zero 或 first-break phase-slip 命名回流。
- 仍需排斥 `FirstBreakPhaseSlipNamedReturnExclusion`，或完成 signed-row/source-rank 主前沿。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_early_to_square_phase_transfer_split_router.py` | `a4022b805ce6061849f6eddce2b2f4990140a1f59f30a55de732f1a14ba57acc` |
| `docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json` | `3b4788e5d5ca0887a903422eff12882a5e41c2040c760df61cdda575cf4109e4` |
| `docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json` | `b38bc33611a384f5d925c2005c5e9df9cff5fee0af0b8bc5da4acc8bff88b681` |
| `docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json` | `ff08e13fd2dbbd7dbbdaf7a1648fc8f339cd2e52eec84a5ba3a0df7873c05d9c` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json` | `328ee462d76cb6213f976eee33133885f20109157d16cf80d236ae27d78d8993` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
| `docs/monograph/prime-matrix-zero-row-minrep-route-review.md` | `cff5609900bcfaa796b6b586c44458727b9807f2f1afd2210e52360dbe5bef26` |
| `docs/front-window-branch-potential.md` | `b24f94beaf9bedb2b3ff03570d92681bc34565a9a9abbfbe03c3185b76d971b9` |
| `docs/phase-delay-minimal-solution-route.md` | `c6329437cbb7679440bb7d43f3ae865bd198a25dca180fa112c09a11bd441e21` |
