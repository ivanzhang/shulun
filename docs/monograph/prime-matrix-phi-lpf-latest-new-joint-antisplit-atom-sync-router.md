# Prime Matrix Phi-LPF latest new-joint to antisplit atom sync 证书

**状态：** `phi_lpf_latest_new_joint_synced_to_antisplit_atom_open`

本步把 latest Phi-LPF terminal saturation 留下的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 接到 strict new-joint 反分裂原子证书。旧 alpha/delta、alpha-side、row-level、signed-source 展开已经同步为固定点，不能作为非循环证明；因此真实最窄原子压成 `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection`。该原子必须在 alpha-side 投影前同一行同时给出 primitive basis word、signed coefficient、alpha/delta pairing、exact `(u,v)`、branch key、sign/local factor、prepushforward identity 和 no-split 证书。LPF/Phi 桶恒等式仍只提供无符号 support/capacity，当前语料未给出该反分裂公式，行/列命题仍未无条件闭合。

```text
latest_new_joint_target_imported=true
terminal_obligation_imported=true
old_split_formula_route_synced=true
old_split_formula_route_is_nonproof_cycle=true
antisplit_joint_formula_target_imported=true
antisplit_fields_imported=true
lpf_phi_unsigned_boundary_retained=true
non_split_actual_joint_formula_proved=false
known_antisplit_downstream_available=true
built_in_signed_pairing_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
rate_preservation_ledger_proved=false
dstructure_independent_gate_closed=false
row_column_unconditional_closed=false
next_primary_attack_target=NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection
```

## 1. 同步链

| from | to |
| --- | --- |
| `Phi-LPF latest terminal saturation frontier` | `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` |
| `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` | `old split alpha/delta route OR antisplit joint row formula` |
| `old split alpha/delta route` | `row-level/signed-source fixed point` |
| `antisplit joint row formula` | `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` |
| `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` | `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing -> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |
| `ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem` | `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestNewJointTargetImported` | `true` | `false` | 上一层 Phi-LPF latest 终端饱和已把严格内部主攻压成 new-joint 公式工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `TerminalObligationImported` | `true` | `false` | new-joint 义务证书确认当前没有已提交的显式 joint formula 工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `OldSplitFormulaRouteSynced` | `true` | `false` | 沿旧 actual constructor、explicit alpha/delta、alpha-side、anchor/phase、signed lift 展开已全部同步。 | old split route |
| `OldSplitFormulaRouteIsNonproofCycle` | `true` | `true` | 旧分裂路线回到 row-level/signed-source 固定点，不能登记为非循环证明。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `AntisplitJointFormulaTargetImported` | `true` | `false` | 真正的新公式必须在 alpha-side 投影前同一行同时给出 primitive word 与 signed coefficient。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `AntiSplitFieldsImported` | `true` | `false` | 反分裂字段合同已列出 source tuple、word/coefficient、alpha/delta payload、exact UV、prepushforward identity 与 no-split 证书。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `LPFPhiUnsignedBoundaryStillUnsigned` | `true` | `true` | LPF/Phi 精准桶恒等式仍只支付无符号 ownership/support/capacity，不能生成 signed joint coefficient。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `NonSplitFormulaCurrentCorpusProved` | `false` | `false` | 当前仓库没有不经 alpha-side/row-level/signed-source 分裂的同排 primitive word/coefficient 公式。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `KnownAntiSplitDownstreamAvailable` | `true` | `false` | 若继续下钻，已有 strict 下游会把反分裂原子压到 atomic rows、built-in pairing 与 ExactUV entropy/fiber。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `ExactUVEntropyFiberStillParallel` | `true` | `false` | ExactUV incidence 仍是并行门；其下游 source-domain entropy 与 fixed-pair fiber bound 未由反分裂公式自动给出。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `ModelRateDStructureStillParallel` | `true` | `false` | 模型余量、RatePreservation 与 DStructure/Rankin 独立验收仍保持开放。 | ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把 latest new-joint 主线同步到反分裂原子；没有得到无条件全局矛盾。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND FixedKeyExactUVLocalMultiplicityO1Ledger AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新开放基

严格内部主攻基：

```text
NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND FixedKeyExactUVLocalMultiplicityO1Ledger AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

反分裂后已知可继续下钻基：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

下一直接主攻：

```text
NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection
```

反分裂下游首攻：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

并行仍需：

```text
ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
FixedKeyExactUVLocalMultiplicityO1Ledger
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
ActualEmitterSourceDomainEntropyLedger
ExactUVMapFixedPairPolylogFiberBoundLedger
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 边界

- 本层只把 latest new-joint 主线同步到反分裂原子。
- LPF/Phi 精准桶恒等式仍只支付无符号 ownership、support 与 capacity。
- 已有下游说明反分裂原子若继续展开，会进入 atomic rows / built-in pairing 与 ExactUV entropy/fiber；这仍不是已证闭合。
- 行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_new_joint_antisplit_atom_sync_router.py` | `5b4fcdb7797d7bc0352d60d98b9202d4b8a2b8dd3e13be6e410737346a71edb1` |
| `docs/monograph/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.json` | `71c86bde660683a0413acbf0d34308265488761e2d90351eff8c7b6cb62923bf` |
| `docs/monograph/prime-matrix-strict-new-joint-formula-terminal-obligation-router.json` | `1db15fd070caa0101e4af1921587d03cbdb8ca5eb28ffdf394094207954ca882` |
| `docs/monograph/prime-matrix-strict-new-joint-formula-antisplit-atom-router.json` | `3d469a4d75bef80450fca102700a378ef1e1ec210dd05299cea59d50e13f5004` |
| `docs/monograph/prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json` | `7124b422ea771e65f65319b24363e617b947c3a3b3e041af5e3cb168b192ff8b` |
| `docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json` | `72261ef1a6ba980a674636e9ec70064a59d827009b4fde0ae7acf06801c9d90e` |
| `docs/monograph/prime-matrix-strict-antisplit-joint-declaration-firewall-router.json` | `dd12ca2ff0316f1833578addbaeeecb1319e6f513604cd485b2291487b663d77` |
| `docs/monograph/prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json` | `fa7ad8fc05db9226702248fe8cca0f6870ae51e50afa0a3161cefa3235c6587b` |
| `docs/monograph/prime-matrix-strict-actual-emitter-incidence-entropy-router.json` | `36b03764e66ea8e57d010d38829004c62a1ab72c363f1e73a9cce92126f6ab7d` |
