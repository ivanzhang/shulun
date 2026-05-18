# Prime Matrix strict 反分裂 trace-cycle / ExactUV 原子化前沿

**状态：** `antisplit_builtin_pairing_synced_to_trace_cycle_and_exactuv_atoms_open`

本步把反分裂 built-in pairing 继续同步到 exact atomic branch trace；但 branch trace 已被 signed-lane cycle 证书登记为闭环中的节点，不能自证。因此 signed 侧非循环出口回到 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 或 terminal/PDEC/外部输入。并行 ExactUV 侧被原子化为 signed row-mass entropy、registered complete key 分区和 fixed-key exact-UV 局部重数。上述原子当前均未证明，行/列命题仍未无条件闭合。

```text
built_in_pairing_reduced_to_branch_trace=true
signed_lane_trace_cycle_imported=true
new_primitive_payload_or_trace_artifact_present=false
emitter_entropy_atomized_to_signed_row_mass=true
fixed_pair_fiber_atomized=true
acyclic_seed_primitive_row_signed_coefficient_law_proved=false
registered_complete_primitive_emitter_key_partition_polylog_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
parallel_direct_attack_targets=AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward, RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger, FixedKeyExactUVLocalMultiplicityO1Ledger
```

## 1. 同步边

| from | to | meaning |
| --- | --- | --- |
| `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` | `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` | built-in pairing 的非循环闭式需要 exact atomic branch trace。 |
| `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` | `signed-lane dependency cycle` | exact branch trace 沿 signed payload/origin identity 回到 common source packet，不能自证。 |
| `signed-lane dependency cycle` | `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` | 打破闭环必须提交新 primitive payload/trace、well-founded terminal descent 或 same-set PDEC。 |
| `ActualEmitterSourceDomainEntropyLedger` | `ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger` | source-domain entropy 继承 actual pre-Cauchy signed row-mass entropy 原子化。 |
| `ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger` | `AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward` | row-mass entropy 的当前第一生产性单点是 signed primitive row coefficient law。 |
| `ExactUVMapFixedPairPolylogFiberBoundLedger` | `RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger` | fixed-pair fiber bound 被拆成 registered complete key 分区与 fixed-key exact-UV 局部重数。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `AntiSplitDownstreamBasisImported` | true | false | 上一层已把反分裂 atomic rows 的 signed 缺口压成 built-in pairing。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `BuiltInPairingReducedToBranchTrace` | true | false | built-in pairing 的真正非循环闭式必须给 exact atomic branch trace signed coefficient formula。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `SignedLaneTraceCycleImported` | true | true | exact branch trace 已在 signed-lane 闭环中；环内节点不能互相自证。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `NewPrimitiveTracePayloadStillAbsent` | false | false | 当前材料没有能打破 signed-lane 闭环的新 primitive trace/payload 工件。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `EmitterEntropyAtomizationImported` | true | false | Actual emitter source-domain entropy 已对齐到 signed row-mass entropy 包。 | ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger |
| `SignedRowLawStillOpen` | true | false | signed row-mass entropy 的第一生产性行权重律仍未证明。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `FixedPairFiberAtomized` | true | false | fixed-pair polylog fiber bound 已拆成 complete key 分区和 fixed-key 局部 O(1) 重数。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `RegisteredCompleteKeyStillOpen` | true | false | 当前材料没有证明 actual noncanonical primitive emitter 的 complete key 数为 log^O(1)。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger |
| `FixedKeyMultiplicityStillOpen` | true | false | 当前材料没有证明固定 complete key 与 fixed exact `(u,v)` 下只有 O(1) 原像。 | FixedKeyExactUVLocalMultiplicityO1Ledger |
| `RowColumnUnconditionalClosureReached` | false | false | 本步只完成 trace-cycle 与 ExactUV 原子化同步；未证明新 payload、signed row law、key/fiber 或晋级门。 | row/column theorem still open |

## 3. 粗内部基

```text
(NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

## 4. 细原子基

```text
(NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

## 5. 统一保留剩余基

```text
((NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 结论边界

- 本文件是 trace-cycle 与 ExactUV atomization 同步，不是行/列命题证明。
- exact branch trace 在 signed-lane 闭环内，不能作为自足闭合。
- 下一 signed 侧非循环出口是 new primitive payload/trace；ExactUV 侧并行要求 signed row law、registered key 与 fixed-key multiplicity。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_antisplit_trace_exactuv_atomized_frontier_router.py` | `e08a40f0f1a8382f38fd5c41fa67eefc65f4f9ab42608b9acd74f60fe00164eb` |
| `docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json` | `72261ef1a6ba980a674636e9ec70064a59d827009b4fde0ae7acf06801c9d90e` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json` | `17e1966e5e4dad0a168abc867d451291be4991c999f28bfbaf494d5875447bf1` |
| `docs/monograph/prime-matrix-strict-actual-source-domain-entropy-atom-router.json` | `0eaacb65ce36ad81475e8fb8806bdd90570f24939b224d6f59c38262cf2374a9` |
| `docs/monograph/prime-matrix-strict-fixed-pair-fiber-bound-router.json` | `ca413ebdcac1df1baf57319fbfe828d92bc272ef1b326215de5cd514316d49bd` |
