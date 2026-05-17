# Prime Matrix global CRT branch trace 前沿路由器

**状态：** `global_crt_latest_frontier_reduced_to_pdec_scope_or_atomic_branch_trace_open`

最新 global CRT 活动基继续收窄：PDEC same-set 作用域匹配仍可作为独立新证书输入，但当前未证；另一侧 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 已经被压成`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`。这要求对每条 atomic joint row 在同一 formal unit 和 Cauchy/Phi/payment 前给出完整 branch trace，同时输出 basis word、signed coefficient、alpha/delta pairing、orientation/local factor、exact UV 与回流。行/列命题仍未无条件闭合。

```text
global_crt_terminal_saturation_imported=true
pdec_scope_branch_still_open=true
new_joint_formula_terminal_obligation_imported=true
new_joint_reduced_to_antisplit_formula=true
antisplit_reduced_to_atomic_declaration=true
atomic_declaration_reduced_to_builtin_pairing=true
builtin_pairing_reduced_to_exact_branch_trace=true
acyclic_same_set_scope_match_proved=false
exact_atomic_joint_branch_trace_signed_coefficient_formula_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate_OR_ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
```

## 1. 同步链

| from | to |
| --- | --- |
| `global CRT terminal saturation basis` | `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` |
| `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` | `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` |
| `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` | `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing` |
| `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing` | `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |
| `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` | `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `GlobalCRTTerminalSaturationImported` | `true` | `false` | 上一层已把 Q1/Q2-CRT 路线同步到 PDEC 作用域匹配或新 joint 公式二选一。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `PDECScopeBranchStillExternalOrNewCertificate` | `true` | `false` | PDEC same-set 作用域分支在当前内部语料中已饱和；仍可作为新 scope 证书输入，但当前未证。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `NewJointFormulaTerminalObligationImported` | `true` | `false` | 没有新 joint 公式时，旧 declaration/alpha-side/same-row 路线回到 signed-source 固定点。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NewJointReducedToAntiSplitFormula` | `true` | `false` | 新公式若沿旧 alpha-side 分裂路线展开就回到来源环；真正剩余是反分裂同排公式。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `AntiSplitReducedToAtomicDeclaration` | `true` | `false` | 普通 declaration line 仍会降解到旧分裂循环；必须要原子 joint rows 声明。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing |
| `AtomicDeclarationReducedToBuiltinPairing` | `true` | `false` | unsigned skeleton 已闭合；真正缺口是每条 atomic row 的内置 signed coefficient/pairing 闭式。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `BuiltinPairingReducedToExactBranchTrace` | `true` | `false` | signed coefficient 是取向/local factor 敏感数据；必须给出 Cauchy 前 exact atomic branch trace。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `BranchTraceCurrentCorpusProved` | `false` | `false` | 当前没有每条 atomic joint row 的 exact branch trace signed coefficient 公式。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本证书只把二选一活动基进一步压到 PDEC scope 或 branch trace；未产生全局无条件终端矛盾。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新严格活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate_OR_ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
```

审稿边界：本文件只完成当前活动基的前沿压缩；它没有证明 PDEC 作用域匹配，
没有给出 exact atomic branch trace，也没有关闭 ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.json` | `3605fe49f0b89505270295a7768785093069442c79ee02c153f86211a541eb02` |
| `docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `3c7602bf11d29d837d1a05964368f085de2c10dc5e786bd518b55a85b4ce3cbf` |
| `docs/monograph/prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json` | `7a72bed5901b1c6b5575db7161c23108f5f4fc17e1848d75cb00b20fd1e6c993` |
| `docs/monograph/prime-matrix-strict-new-joint-formula-terminal-obligation-router.json` | `1db15fd070caa0101e4af1921587d03cbdb8ca5eb28ffdf394094207954ca882` |
| `docs/monograph/prime-matrix-strict-new-joint-formula-antisplit-atom-router.json` | `3d469a4d75bef80450fca102700a378ef1e1ec210dd05299cea59d50e13f5004` |
| `docs/monograph/prime-matrix-strict-antisplit-joint-declaration-firewall-router.json` | `dd12ca2ff0316f1833578addbaeeecb1319e6f513604cd485b2291487b663d77` |
| `docs/monograph/prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json` | `fa7ad8fc05db9226702248fe8cca0f6870ae51e50afa0a3161cefa3235c6587b` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
