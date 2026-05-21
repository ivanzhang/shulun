# Prime Matrix Phi-LPF latest new-joint antisplit downstream sync 证书

**状态：** `phi_lpf_latest_new_joint_antisplit_synced_to_builtin_pairing_open`

本步把 latest 反分裂原子 `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` 接入 strict 下游。反分裂同排行若要避免旧 split 固定点，必须升级为 `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing`；而 atomic rows 的首个 signed 缺口是 `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`。并行 ExactUV 门同步为 `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger`。这些输入当前均未证明，complete/fixed-key、模型余量、Rate 与 DStructure 仍开放，行/列命题未无条件闭合。

```text
latest_antisplit_atom_imported=true
strict_antisplit_downstream_edges_imported=true
antisplit_firewall_to_atomic_rows_imported=true
atomic_rows_reduced_to_builtin_pairing=true
signed_origin_table_loop_blocked=true
exactuv_entropy_fiber_split_imported=true
non_split_actual_joint_formula_proved=false
atomic_antisplit_declaration_proved=false
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

## 1. 同步边

| from | to | meaning |
| --- | --- | --- |
| `NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` | `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing` | 反分裂同排行必须内置 rows formula、word/coefficient pairing、prepushforward identity 与 split firewall。 |
| `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing` | `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` | atomic rows 的 signed 首缺口是每行内置 coefficient/pairing 闭式。 |
| `ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem` | `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger` | bounded ExactUV incidence 拆成 source-domain entropy 与 fixed exact-pair fiber bound。 |
| `retained alternatives` | `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch` | canonical-lock、independent bridge、same-set PDEC 与外部谱仍是独立保留输入。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestAntiSplitAtomImported` | `true` | `false` | 上一层 latest new-joint 同步已经把主攻压到反分裂同排原子，并确认有 strict 下游可继续追击。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `StrictAntiSplitDownstreamEdgesImported` | `true` | `true` | strict 下游同步边覆盖 NonSplit -> atomic rows -> built-in pairing，以及 ExactUV -> entropy/fiber。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `AntiSplitFirewallToAtomicRowsImported` | `true` | `false` | 反分裂 firewall 表明普通 declaration 不够，必须提交 atomic pre-Cauchy rows 声明。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing |
| `AtomicRowsReducedToBuiltInPairing` | `true` | `false` | atomic rows 的 row skeleton、防回退 firewall 已有；缺口集中到每行 built-in signed pairing 闭式。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `SignedOriginTableLoopBlocked` | `true` | `true` | 旧 signed-value/origin-table 路线被登记为回到 signed-source 固定点，不能替代 built-in pairing。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `ExactUVEntropyFiberSplitImported` | `true` | `false` | ExactUV bounded multiplicity 已拆为 source-domain entropy 与 fixed-pair polylog fiber bound 两个账本。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `BuiltInPairingCurrentCorpusProved` | `false` | `false` | 当前语料没有每条 atomic joint row 的 signed coefficient 闭式值及 word/coefficient 同源证明。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `EntropyFiberCurrentCorpusProved` | `false` | `false` | 当前语料没有证明 actual source-domain entropy 与 fixed exact-pair polylog fiber bound 的合取。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `ExternalAndTerminalAlternativesRetained` | `true` | `false` | canonical-lock、independent bridge、same-set PDEC 与外部谱仍作为独立输入保留。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| `ModelRateDStructureStillParallel` | `true` | `false` | complete/fixed-key、模型余量、RatePreservation 与 DStructure/Rankin 仍未由 built-in pairing 自动推出。 | CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只是把反分裂原子同步到 built-in pairing 与 ExactUV entropy/fiber；没有得到无条件闭合。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新开放基

严格内部基：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

带保留替代输入的基：

```text
((BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger) OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

并行主攻：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

## 4. 边界

- 本层只同步反分裂下游，不证明 built-in pairing 或 ExactUV entropy/fiber。
- LPF/Phi 桶恒等式仍不生成 signed coefficient。
- 行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_new_joint_antisplit_downstream_sync_router.py` | `827018c54cf76ac2e1580c7ed28912f186e20d03d6c3ed3a52e0b76b7e10e530` |
| `docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.json` | `8bfd13a8b9edfd7cf3643fc82cb08fe6fc35669bafe0c56580deeaf58c468b56` |
| `docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json` | `72261ef1a6ba980a674636e9ec70064a59d827009b4fde0ae7acf06801c9d90e` |
| `docs/monograph/prime-matrix-strict-antisplit-joint-declaration-firewall-router.json` | `dd12ca2ff0316f1833578addbaeeecb1319e6f513604cd485b2291487b663d77` |
| `docs/monograph/prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json` | `fa7ad8fc05db9226702248fe8cca0f6870ae51e50afa0a3161cefa3235c6587b` |
| `docs/monograph/prime-matrix-strict-actual-emitter-incidence-entropy-router.json` | `36b03764e66ea8e57d010d38829004c62a1ab72c363f1e73a9cce92126f6ab7d` |
