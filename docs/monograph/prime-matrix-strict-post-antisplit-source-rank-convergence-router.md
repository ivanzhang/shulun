# Prime Matrix strict post-antisplit source-rank 收敛前沿

**状态：** `post_antisplit_source_rank_paths_converge_to_pointwise_kernel_open`

本步把刚完成的 antisplit trace/ExactUV 原子化前沿与仓库中已有的 new primitive、terminal descent、source-rank、source entropy、complete key 和 source table 证书重新合并。`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 已不是独立新主攻点；它和 terminal descent 都回到同一 source-rank/no-collapse 包。该包的非后验共同变量表是 `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate`，当前第一硬点为 `AlphaRowAnchorPhaseEmissionFormulaLedger`。行/列命题仍未无条件闭合。

```text
new_primitive_exit_absorbed_to_source_rank=true
terminal_descent_converges_to_source_rank=true
source_rank_package_atomized=true
all_internal_source_rank_routes_meet_at_pointwise_kernel_table=true
alpha_row_anchor_phase_emission_formula_proved=false
independent_noncircular_precauchy_arithmetic_identity_statement_proved=false
same_unit_exact_uv_rank_multiplicity_certificate_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger
parallel_direct_attack_targets=IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger, SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

## 1. 收敛边

| from | to | meaning |
| --- | --- | --- |
| `AntiSplitTraceExactUVAtomizedFrontier` | `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch` | antisplit built-in pairing 已落入 signed-lane trace cycle，非循环出口只能走这些命名门。 |
| `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` | `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | 独立 new primitive 工件若要破环，必须携带同一 pre-Cauchy actual source 的 rank/no-collapse 包。 |
| `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` | `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | terminal descent 的当前非循环叶子已经同步到相同 source-rank/no-collapse 包。 |
| `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | `ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger` | source-rank 包的实际内容是源域熵、complete key 分区和 fixed-key 局部重数。 |
| `ActualPreCauchySourceDomainAbsoluteEntropyLedger` | `AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward` | 源域绝对熵的第一生产性字段回到 primitive signed row coefficient law。 |
| `CompletePrimitiveEmitterKeyPartitionLedger / RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger` | `ActualNoncanonicalPrimitiveEmitterSourceTableLedger` | registered complete key 分区不能后验补标签，必须来自 actual emitter source table。 |
| `ActualPreCauchySourceDomainAbsoluteEntropyLedger / CompletePrimitiveEmitterKeyPartitionLedger / RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger / FixedKeyExactUVLocalMultiplicityO1Ledger` | `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | 三条源域/no-collapse 线在同 formal-unit 的逐 primitive alpha/delta 核表上汇合。 |
| `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | 逐点核表的当前第一硬点是 alpha row anchor/phase 发射公式，并行还需算术恒等式与同表 rank/multiplicity。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PostAntiSplitFrontierImported` | true | false | 最新 antisplit trace/ExactUV 证书没有闭合行/列命题，只给出 new-primitive/terminal/PDEC/external 与 ExactUV 三原子的合取前沿。 | ((NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `NewPrimitiveExitAlreadyAbsorbed` | true | false | `NewPrimitive...` 不是新的独立主攻点；旧证书已要求它提交 source-rank/no-collapse 包或转入命名出口。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `TerminalDescentConvergesToSameSourceRankPackage` | true | false | terminal descent 非循环叶子也回到相同的 source-rank/no-collapse 包，不能作为独立闭合点。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `SourceRankPackageAtomized` | true | false | source-rank/no-collapse 包已被拆成源域熵、complete key 与 fixed-key 局部重数。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `DomainEntropyReturnsToSignedRowLaw` | true | false | 源域熵首攻点回到 primitive signed row coefficient law；这解释了为什么 signed trace cycle 与 source entropy 是同一底层障碍。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `RegisteredKeyNeedsActualSourceTable` | true | false | complete key 的多对数分区不能由 payment/CRT 后验标签生成，必须先有 actual source table。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger |
| `SourceTableNeedsPreCauchyDeclaration` | true | false | actual source table 的首行是 pre-Cauchy constructor declaration；没有该行，summand/权重/return 都只是后验表。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| `FixedPairFiberStillUsesSameKeyMultiplicityAtoms` | true | false | fixed-pair fiber 的形式不等式已闭合，但 registered key 与 fixed-key multiplicity 仍是实际数学缺口。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `AllInternalSourceRankRoutesMeetAtPointwiseKernelTable` | true | false | new primitive、terminal descent、source entropy、complete key 与 fixed-key multiplicity 的非后验共同变量表是逐 primitive alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `LatestPriorityAtomPinned` | true | false | 当前第一可攻原子是 alpha row anchor/phase 发射公式；并行还需 pre-Cauchy 算术恒等式和同表 rank/multiplicity。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `RowColumnUnconditionalClosureReached` | false | false | 本步只完成 post-antisplit 后的旧出口吸收与共同核表定位；未证明 alpha 发射、算术恒等式、rank/multiplicity、PDEC/外部谱或最终晋级门。 | row/column theorem still open |

## 3. 当前共同核表

```text
PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
```

核表后仍需：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

## 4. 统一保留剩余基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows) OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 结论边界

- 本文件只完成 post-antisplit 后的旧出口吸收和共同变量表定位。
- `NewPrimitive...` 与 terminal descent 不再作为独立闭合点；二者都回到 source-rank/no-collapse。
- 仍未证明 alpha row 发射公式、pre-Cauchy 算术恒等式、同表 rank/multiplicity、PDEC/外部谱输入或最终晋级门。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_post_antisplit_source_rank_convergence_router.py` | `f77ae502bb74552c3bfb7e84d8d135e289647e70fd1862f2973a997efc20d41f` |
| `docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json` | `8e147c15b7a2b06ea52c356a9571416ca0eabda9c6323d88df4aea94b7578064` |
| `docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json` | `3194b1509c245cd42f607bbab6b96a1e17420454c3ae40245fb859985d38a601` |
| `docs/monograph/prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json` | `62c6b5b1712c00216487e7c68b72d8cb97a61e58ba78f08538f697c49232142a` |
| `docs/monograph/prime-matrix-strict-actual-source-domain-entropy-atom-router.json` | `0eaacb65ce36ad81475e8fb8806bdd90570f24939b224d6f59c38262cf2374a9` |
| `docs/monograph/prime-matrix-strict-complete-emitter-key-partition-router.json` | `8eb78dba1a3383b509b4b968fc51daaadbb683830ea480eb1cc418ca92e426c8` |
| `docs/monograph/prime-matrix-strict-actual-emitter-source-table-router.json` | `e327b1a80aef83a36279378e5892334fa305d92d5ac1bcbb8601eaab2f18ab3e` |
| `docs/monograph/prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json` | `64c0baf4ed2c463ec6eb69b95ebb14f16da4c5aa909fc6b7f244035d1db041cf` |
| `docs/monograph/prime-matrix-strict-fixed-pair-fiber-bound-router.json` | `ca413ebdcac1df1baf57319fbfe828d92bc272ef1b326215de5cd514316d49bd` |
