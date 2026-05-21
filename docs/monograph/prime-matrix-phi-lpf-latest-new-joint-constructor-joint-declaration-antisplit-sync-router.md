# Prime Matrix Phi-LPF latest constructor joint-declaration antisplit sync 证书

**状态：** `phi_lpf_latest_constructor_joint_declaration_synced_to_builtin_pairing_open`

本步把 current constructor 的 `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple` 接到 anti-split 下游。普通 declaration 只同步到 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple`，继续展开会回到 signed-source 固定点；非循环路线必须给 `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing`，其首个 signed 缺口压到 `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`。`ActualEmitterSourceDomainEntropyLedger` 与 `ExactUVMapFixedPairPolylogFiberBoundLedger` 仍是并行 ExactUV 门；canonical lock、independent bridge、PDEC/外部谱、signed survival、row-mass、模型、Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

```text
current_constructor_joint_declaration_imported=true
strict_antisplit_downstream_imported=true
ordinary_joint_declaration_synced_to_constructor_rule=true
ordinary_constructor_route_rejected_as_fixed_point=true
antisplit_firewall_imported=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
pre_cauchy_joint_declaration_line_proved=false
atomic_antisplit_declaration_proved=false
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple` | `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple` | 普通 joint declaration 同步到显式 joint alpha/delta constructor rule。 |
| `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple` | `signed-source fixed point unless anti-split route is supplied` | 普通 constructor 展开回到 signed-source 固定点，不能作为非循环证明。 |
| `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` | `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing` | 要避开普通固定点，声明行必须内置 atomic rows 与 word/coefficient pairing。 |
| `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing` | `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` | atomic joint rows 的首个 signed 缺口是每条 row 的 built-in coefficient/pairing 闭式。 |
| `ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem` | `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger` | ExactUV incidence 并行拆成 actual source entropy 与 fixed-pair polylog fiber bound。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentConstructorJointDeclarationImported` | true | false | 当前 constructor triad-unified 层已把直接主攻压到 pre-Cauchy joint declaration line。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `StrictAntisplitDownstreamImported` | true | false | 既有 strict 下游同步已把 joint declaration 的非循环路线压到 anti-split atomic rows 与 built-in pairing。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `OrdinaryJointDeclarationSyncedToConstructorRule` | true | false | 普通 joint declaration 只同步到显式 constructor rule，不是独立闭合。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `OrdinaryConstructorRouteRejectedAsFixedPoint` | true | true | 显式 constructor 普通展开经 alpha-side/same-row/row-level 回到 signed-source 固定点。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing |
| `AntiSplitFirewallImported` | true | false | anti-split firewall 要求声明行内置 atomic rows、word/coefficient 同源和 split firewall。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing |
| `AtomicRowsReducedToBuiltinPairing` | true | false | atomic joint rows 的 signed 首缺口已同步为 built-in signed coefficient/pairing 闭式。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `ExactUVEntropyFiberSplitImported` | true | false | built-in pairing 不支付 ExactUV；source-domain entropy 与 fixed-pair fiber bound 仍是并行门。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `BuiltInPairingCurrentCorpusProved` | false | false | 当前语料没有每条 atomic joint row 的 signed coefficient 闭式值及 word/coefficient 同源证明。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `ExactUVEntropyFiberCurrentCorpusProved` | false | false | 当前语料没有 actual source-domain entropy 与 fixed exact-pair polylog fiber bound 的合取证明。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `RowColumnUnconditionalClosureReached` | false | false | 本层只完成 constructor joint declaration 到 anti-split/builtin pairing 的同步，不是三目标命题无条件闭合。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新保留基

```text
((BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger) OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

并行主攻：

```text
ActualEmitterSourceDomainEntropyLedger
ExactUVMapFixedPairPolylogFiberBoundLedger
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ExternalDIBFIKuznetsovDispersionTheoremMatch
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 依赖哈希

```json
{
  "experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_joint_declaration_antisplit_sync_router.py": "adc6305715234acbb98046de262dac9767449c808388bbbf83a671a0bb499eae",
  "docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json": "3988516231db8e282718f74ff3586961ec24b7fed23ab516408a9320fce3d8a3",
  "docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json": "72261ef1a6ba980a674636e9ec70064a59d827009b4fde0ae7acf06801c9d90e",
  "docs/monograph/prime-matrix-strict-joint-declaration-constructor-sync-router.json": "dbca8167a10b42d83c9734c13100d6376b5f91a905d2ebd3f5c9b8621ada1401",
  "docs/monograph/prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json": "7124b422ea771e65f65319b24363e617b947c3a3b3e041af5e3cb168b192ff8b",
  "docs/monograph/prime-matrix-strict-antisplit-joint-declaration-firewall-router.json": "dd12ca2ff0316f1833578addbaeeecb1319e6f513604cd485b2291487b663d77",
  "docs/monograph/prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json": "fa7ad8fc05db9226702248fe8cca0f6870ae51e50afa0a3161cefa3235c6587b",
  "docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json": "6f2a1790c735dacb3d3c3104dd6ae6469abe97a23853e073a57fb4990e4bf769",
  "docs/monograph/prime-matrix-strict-actual-emitter-incidence-entropy-router.json": "36b03764e66ea8e57d010d38829004c62a1ab72c363f1e73a9cce92126f6ab7d"
}
```
