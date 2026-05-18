# Prime Matrix strict new primitive payload source-atom alignment router

**状态：** `strict_new_primitive_payload_reduced_to_actual_source_rank_atom_open`

本步直接审计 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`。若它只是 signed-lane 环内的 trace、payload、origin 或 common packet 的改名，则不能破环；若它要作为真正的新 primitive 工件，就必须在 Cauchy/Phi/payment 前声明同一 actual source object，并给出 source entropy、complete key partition 与 fixed-key exact-UV local multiplicity。因而该出口对齐到 `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger`，或转入 terminal descent、PDEC、外部谱输入。当前语料没有独立 new primitive 工件，行/列命题仍未无条件闭合。

```text
new_primitive_artifact_independent_terminal_present=false
new_primitive_artifact_reduced_to_source_rank_atom=true
source_rank_atom_imported=true
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

## 1. New primitive 最低字段合同

| field | minimum requirement | current alignment | remaining |
| --- | --- | --- | --- |
| `same_formal_unit_lock` | 锁定同一 actual counterexample formal unit、atomic branch trace、primitive source rows 与 exact `(u,v)` 口径。 | 已有 trace/source 证书说明该锁不能由可见坐标或 terminal 回流补出。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `pre_cauchy_source_object` | 在 Cauchy、Phi、payment、零行恢复前声明 actual noncanonical primitive source object。 | source declaration packet 与 final exact-source 原子都要求该对象。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger |
| `signed_payload_formula` | 正向给出 orientation、signed coefficient、local factor、truncation weight 与 nonzero/return tags。 | 若只给 coefficient 表，会回到 origin/common-packet 闭环。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `complete_key_partition` | 发射前把 primitive rows 分入 complete keys，禁止后验补标签。 | preterminal source atom 已把它列为三原子之一。 | CompletePrimitiveEmitterKeyPartitionLedger |
| `source_domain_absolute_entropy` | 证明 actual source 质量不能集中在少数 primitive rows 或少数 key/fiber。 | 这是 source rank/no-collapse 包的首攻项。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger |
| `fixed_key_exact_uv_local_multiplicity` | 固定 complete key 与 fixed exact `(u,v)` 下只有 O(1) 个 admissible actual primitive source 原像。 | 缺该项时 new payload 只能命名单个原像，不能排除 fiber 坍缩。 | FixedKeyExactUVLocalMultiplicityO1Ledger |
| `no_cycle_or_terminal_recovery` | 证明没有调用 signed-lane 环、row-level origin table、terminal descent、PDEC 或外部谱输入反推。 | 若调用这些输入，工件不再是独立 new primitive artifact。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SignedLaneCycleImported` | true | true | signed/payload 子线已闭环，new primitive 工件只有在闭环外正向产生 payload/source 时才有意义。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `VisibleTraceCannotServeAsNewArtifact` | true | true | 可见 branch trace 只给坐标，不给 signed coefficient、orientation、local factor 或 source entropy。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `OriginIdentityWithoutSourceRankReturnsToCycle` | true | true | 仅提交 basis-word/signed-coefficient 来源恒等式会与 ExactUV 一起回到 common source declaration packet。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `NewArtifactMustContainPreCauchySourceObject` | true | false | 若工件不声明 Cauchy 前 actual source object，它只是后验标签或 terminal 回流，不能破环。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger |
| `NewArtifactRequiresExactUVFiberAperiodicity` | true | false | 破环工件必须控制同一 source 在 exact `(u,v)` fiber 上的质量分散；CRT/轮筛位置刚性不能替代。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| `SourceRankAtomPackageImported` | true | false | fiber 非集中已被仓库压成 source entropy、complete key partition、fixed-key local multiplicity 三原子包。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `Q2AndFinalInputAlignmentImported` | true | false | Q2/CRT 路线的无名终端已回接到 final exact-source 原子或外部谱输入；new primitive 不能形成第三个无名终端。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| `CurrentCorpusHasIndependentNewPrimitiveArtifact` | false | false | 当前语料没有提交同时满足 source object、complete key、source entropy、fixed-key exact-UV multiplicity 与 no-cycle 条件的新工件。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `NewPrimitiveExitReducedToSourceAtomOrExternalRoutes` | true | false | 因此 new primitive 出口不是独立闭合点；它要么证明 source rank/no-collapse 包，要么转入 terminal descent、PDEC 或外部谱输入。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| `RowColumnUnconditionalClosureReached` | false | false | 本步只完成出口对齐；source 三原子、外部谱输入与 DStructure/Rankin 独立验收均未证明。 | (ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR ExternalDIBFIKuznetsovDispersionTheoremMatch; DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新剩余基

```text
((ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻顺序：

| order | target |
| ---: | --- |
| 1 | `ActualPreCauchySourceDomainAbsoluteEntropyLedger` |
| 2 | `CompletePrimitiveEmitterKeyPartitionLedger` |
| 3 | `FixedKeyExactUVLocalMultiplicityO1Ledger` |

## 4. 结论边界

- 本步只把 new primitive signed payload/trace 出口对齐到 actual-source rank/no-collapse 原子。
- 当前没有证明 source entropy、complete key partition、fixed-key exact-UV local multiplicity、外部谱输入或 DStructure/Rankin 独立验收。
- 因而行/列命题仍不能标记为无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_new_primitive_payload_source_atom_alignment_router.py` | `9a6f5e8a8ba634309a3dc905ef8627454737339dd0c250b77fc5d5df2c5ba935` |
| `docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json` | `17e1966e5e4dad0a168abc867d451291be4991c999f28bfbaf494d5875447bf1` |
| `docs/monograph/prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json` | `fe1d86442d7936662a55cd5b8279e339f5bfd21142bd079ec80280c06423df92` |
| `docs/monograph/prime-matrix-strict-atomic-payload-origin-identity-router.json` | `b5e6909a3aab66eef258b360a1dc599dc6bdd28cf415f6c21f630abe989ce65a` |
| `docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json` | `d9e042ffccaaf050e72788abdb0a10a5776a3cb4d8a37fc949c9710a4a832f44` |
| `docs/monograph/prime-matrix-strict-preterminal-support-capacity-attack-router.json` | `f642eddd58ab9bea4dede92715b64d3ff4b1ec8e42eb8e7e63bcbd84f613858b` |
| `docs/monograph/prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json` | `62c6b5b1712c00216487e7c68b72d8cb97a61e58ba78f08538f697c49232142a` |
| `docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.json` | `bf2b854951b33fd1b8f3d3341e73a5c236e54d0640c0b91501d0871dc0dd29df` |
| `docs/monograph/prime-matrix-active-final-inputs-router.json` | `33c703c7d7ffd716b44b43b52c3177de87b94883d2c1ac505cf203b0165095d8` |
