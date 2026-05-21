# Prime Matrix Phi-LPF latest current built-in pairing to branch trace sync 证书

**状态：** `phi_lpf_latest_current_builtin_pairing_synced_to_branch_trace_cycle_exit_open`

本步把当前 latest `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` 桥接到既有 built-in pairing/branch-trace 同步证书。内置 signed pairing 的直接前沿是 `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`；但该 trace 若沿现有 signed payload/origin/common packet 子线展开，会回到 signed-lane 自证环。因此最新非循环主硬点变成 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`，或受控出口 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`、`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`。并行 ExactUV 门仍是 `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger`，其中 fixed fiber 已原子化为 complete key 与 fixed-key 局部重数。行/列命题仍未无条件闭合。

```text
current_latest_builtin_pairing_imported=true
legacy_builtin_trace_router_same_target=true
strict_builtin_frontier_imported=true
odd_signed_data_boundary_imported=true
global_branch_trace_frontier_aligned=true
signed_lane_cycle_imported=true
branch_trace_self_proof_rejected=true
new_primitive_payload_or_trace_artifact_present=false
exactuv_entropy_fiber_pair_carried=true
row_column_unconditional_closed=false
intermediate_primary_attack_target=ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CurrentLatestBuiltInPairingImported` | `true` | `false` | 当前 latest new-joint/antisplit 下游已经把直接 signed 主攻压到 built-in pairing。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `LegacyBuiltInTraceRouterSameTarget` | `true` | `true` | 既有 latest built-in trace 同步证书的输入目标与当前目标相同，可作为下游桥接证据。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `StrictBuiltInFrontierImported` | `true` | `true` | strict built-in frontier 将内置 signed pairing 压到 exact atomic branch trace。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `OddSignedDataBoundaryImported` | `true` | `true` | LPF/Phi unsigned bucket 与旧 signed-value/origin-table 路线不能生成取向/local factor 奇数据。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `GlobalBranchTraceFrontierAligned` | `true` | `false` | global CRT 前沿同样把 new-joint/built-in pairing 侧压到 same-set PDEC 或 exact branch trace。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `SignedLaneCycleImported` | `true` | `true` | common packet、built-in pairing、branch trace、signed payload、origin identity 已形成自证环。 | cycle is diagnostic, not proof |
| `BranchTraceSelfProofRejected` | `true` | `true` | branch trace 不能由环内 payload/origin/common packet 自证；必须新增 primitive trace/payload 或走受控出口。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `NewPrimitivePayloadOrTraceCurrentCorpusProved` | `false` | `false` | 当前语料没有提交新 primitive atomic signed payload 或 trace formula 工件。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `ExactUVEntropyFiberPairCarried` | `true` | `false` | 当前并行 ExactUV 门与既有 trace 同步保持同一个 source entropy/fixed fiber 合取。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `SourceEntropyStillSignedRowLaw` | `true` | `false` | actual source-domain entropy 仍下钻到 signed row law、row-mass normalization 与 row support。 | ActualEmitterSourceDomainEntropyLedger |
| `FixedPairFiberAtomized` | `true` | `false` | fixed-pair fiber 已原子化为 complete key polylog 分区与 fixed-key O(1) 局部重数。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把当前 latest built-in pairing 接到 branch-trace/闭环出口；没有得到无条件闭合。 | (NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 最新开放基

```text
(NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

受控出口：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

## 3. 边界

- 本层是桥接同步，不重新证明 branch trace 下游。
- LPF/Phi 桶恒等式仍不生成 signed coefficient 或 trace 奇数据。
- 行/列命题仍未无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_new_joint_builtin_pairing_trace_sync_router.py` | `62f6e8ee9b05cf9c65963dfd776b512baa41b7810f384c0279ed7c508f1d815e` |
| `docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json` | `78cda26ba38bcf8446f487c7c7f723e4b14766d2d66f4e8d788ba962c698441e` |
| `docs/monograph/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json` | `b12d1fc23b3b15f98e938024af2bf048332cbc3225d9209be0f7a34de7b358a6` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json` | `6437fc285617d3a363361ed354cbba400ab588ee7ea6f3cd8cbb07582d196084` |
| `docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json` | `17e1966e5e4dad0a168abc867d451291be4991c999f28bfbaf494d5875447bf1` |
| `docs/monograph/prime-matrix-strict-fixed-pair-fiber-bound-router.json` | `ca413ebdcac1df1baf57319fbfe828d92bc272ef1b326215de5cd514316d49bd` |
| `docs/monograph/prime-matrix-strict-actual-source-domain-entropy-atom-router.json` | `0eaacb65ce36ad81475e8fb8806bdd90570f24939b224d6f59c38262cf2374a9` |
