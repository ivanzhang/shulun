# Prime Matrix Phi-LPF orientation trace payload source-rank sync 证书

**状态：** `phi_lpf_orientation_law_synced_to_trace_payload_source_rank_open`

本步把最新 `PrimitiveOrientationLocalFactorProductLawBeforePushforward` 同步到已有 trace/payload/source-rank 更深前沿。完整 branch trace 只是取向律的正确格式；在当前内部材料中，其 signed payload 部分会回到 row-level/source packet 闭环，不能自证。若要新增真正 primitive payload/trace 工件，它必须携带 `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger`，也就是 source-domain entropy、complete key partition 和 fixed-key exact-UV local multiplicity 三原子。LPF/Phi 精准桶恒等式已固定无符号支撑，但不能生成 signed orientation；所以下一直接主攻为 `ActualPreCauchySourceDomainAbsoluteEntropyLedger`。行/列命题仍未无条件闭合。

```text
orientation_reduced_to_actual_branch_trace=true
trace_payload_cycle_imported=true
visible_trace_cannot_generate_odd_payload=true
common_packet_need_imported=true
new_primitive_artifact_aligned_to_source_rank=true
source_rank_atom_package_imported=true
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
orientation_local_factor_law_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PrimitiveOrientationLocalFactorProductLawBeforePushforward` | `ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn` | 取向/local-factor 乘积律必须由完整 actual branch trace 正向生成。 |
| `ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn` | `SignedPayloadTraceConstructorBeforeAssignmentOrReturn` | trace 的可见坐标已定位；signed payload 仍是未给出的奇数据。 |
| `SignedPayloadTraceConstructorBeforeAssignmentOrReturn` | `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` | payload 与 ExactUV 都需要同一 pre-Cauchy actual source packet。 |
| `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` | `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | 若新增 primitive payload/trace 工件，必须同时给 source entropy、complete key 与 fixed-key local multiplicity。 |
| `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | `ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger` | source rank/no-collapse 包的首攻项是 actual source-domain absolute entropy。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LatestOrientationLawImported | `true` | `false` | 上一 Phi-LPF 同步层已把逐点 signed 表压到 primitive orientation/local-factor 乘积律。 | PrimitiveOrientationLocalFactorProductLawBeforePushforward |
| OrientationLawReducedToActualBranchTrace | `true` | `false` | 取向/local-factor 若要正向生成，必须由 actual noncanonical primitive branch trace 同时登记 orientation、local factor、sign、UV 与 return。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| TracePayloadCycleImported | `true` | `true` | 当前内部展开中，branch trace 的可见坐标可定位，但 signed payload 会经 slot/value-map/origin 回到 row-level 表。 | SignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| VisibleTraceCannotGenerateOddPayload | `true` | `true` | anchor、D0/K/Omega、phase、word-coordinate 都是可见坐标字段，不能生成反变号 orientation 或 signed coefficient。 | SignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| CommonPacketNeedImported | `true` | `false` | signed payload 与 ExactUV 线合流到同一个 pre-Cauchy actual source declaration packet；该 packet 当前未证明。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| NewPrimitiveArtifactAlignedToSourceRank | `true` | `false` | 若要新增 primitive payload/trace 工件，它不能只改名 trace 或 origin；必须携带 source rank/no-collapse 包。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| SourceRankAtomPackageImported | `true` | `false` | preterminal fiber-dispersion 审查已把 source rank/no-collapse 拆成 source entropy、complete key partition、fixed-key local multiplicity 三原子。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| BranchTraceSelfProofAlreadyEliminated | `true` | `true` | 全局前沿已把 branch trace 自证从活动证明路径删除；不能把 trace 格式本身当作非循环证明。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| LPFPhiBucketsOnlyFixUnsignedSupport | `true` | `true` | LPF/Phi 桶恒等式给出合数最小素因子归属、容量和支撑前像；它不提供 signed orientation payload。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger |
| ActualSourceDomainEntropyCurrentCorpusProved | `false` | `false` | 当前材料尚未证明 actual pre-Cauchy source 域的绝对质量不集中账本。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger |
| CompleteKeyPartitionCurrentCorpusProved | `false` | `false` | complete key 必须在发射前登记 formal unit、branch path、exact UV、sign/local factor 和 truncation 状态。 | CompletePrimitiveEmitterKeyPartitionLedger |
| FixedKeyLocalMultiplicityCurrentCorpusProved | `false` | `false` | 固定 complete key 与 fixed exact UV 下的 O(1) 局部重数尚未证明。 | FixedKeyExactUVLocalMultiplicityO1Ledger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层只同步并压窄 hardpoint；source 三原子、terminal/PDEC/外部谱出口、RatePreservation 与 DStructure/Rankin 仍未全部闭合。 | (ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch; RatePreservationLedger_FOR_moving_atom_packet; DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新 strict 基

```text
((ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

并行主攻：

```text
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ExternalDIBFIKuznetsovDispersionTheoremMatch
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 结论边界

- 本层不是取向律证明，而是把取向律接入更深的 trace/payload/source-rank 审查。
- LPF/Phi 桶恒等式在这里的作用是封死无符号支撑自由度，不产生 signed coefficient。
- 行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_orientation_trace_payload_source_rank_sync_router.py` | `1bfb30b8c165af0b9fb4977c91a2d94f3be22e8a4bf7b755234125e4ab74601c` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json` | `7c76acab60f95b655941cb563439aca48116d80cd4dc1733a0210d96e4a45fb0` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-branch-trace-signed-payload-cycle-router.json` | `67da3805e5bdb503d768a79b95a3408bbdfede3254557e2e89080e2229d0e3b0` |
| `docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json` | `d9e042ffccaaf050e72788abdb0a10a5776a3cb4d8a37fc949c9710a4a832f44` |
| `docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json` | `3194b1509c245cd42f607bbab6b96a1e17420454c3ae40245fb859985d38a601` |
| `docs/monograph/prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json` | `62c6b5b1712c00216487e7c68b72d8cb97a61e58ba78f08538f697c49232142a` |
| `docs/monograph/prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json` | `094823b99842eeb4525d7ea868658fa39ba3d5ac0e7c0163499ab2b70b6f4b5b` |
