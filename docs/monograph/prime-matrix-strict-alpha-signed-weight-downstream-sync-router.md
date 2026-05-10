# Prime Matrix strict alpha signed 权重律下游同步路由器

**状态：** `alpha_signed_weight_downstream_synced_to_terminal_modelgap_open`

`AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger` 的下游链条已同步：权重律缺口先到独立 pre-Cauchy 恒等式陈述，再到 actual noncanonical moving-block/NC-BLK，再到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 与 `ExplicitModelGapAndFiniteDPRCLedger`。因此后续不应再把 weight law、identity 或 NC-BLK 当作新的终端硬点；真正剩余是全局 PDEC-CAP/内部 CleanKLS 大筛门、模型余量账本，以及独立 DStructure/Rankin 验收门。本步只关闭路由同步，不给出行/列无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
downstream_sync_router_closed=true
alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved=false
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同步链

```text
AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LiftFailureReturnsToAlphaWeightLaw` | `true` | `true` | signed lift 失败登记纪律闭合后，首个未证输入回到 alpha signed 权重律。 | AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger |
| `AlphaWeightLawReducedToIndependentIdentity` | `true` | `true` | 权重律已被拆成独立 pre-Cauchy 恒等式、精确公式、非零符号局部因子、反推禁用和失败回流。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger |
| `IndependentIdentityTaxonomyReducedToActualMoving` | `true` | `true` | 独立恒等式陈述不是第五类来源；strict 自足线剩 actual noncanonical moving-block/NC-BLK。 | ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn |
| `NCBLKNotNewTerminal` | `true` | `true` | NC-BLK/source antiatom 不是新终端；它只能回到 moving/source 账本或全局终端门。 | ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn / PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `ActualMovingBlockNoUnnamedExit` | `true` | `true` | actual moving-block/NC-BLK 不能再作为无名出口，已压到全局终端容量/大筛门与模型余量账本。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `GlobalTerminalFamilyStillOpen` | `true` | `false` | 全局终端家族已拆成 PDEC-CAP 或内部 CleanKLS/DLS，但该二选一尚未证明。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `ExplicitModelGapDPRCLedgerRetained` | `true` | `false` | moving-block 替换没有删除模型余量账本；它仍需独立证明或有限证书。 | ExplicitModelGapAndFiniteDPRCLedger |
| `DStructureRankinGateRetained` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是行/列无条件升级的独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `DownstreamSyncClosedButTheoremOpen` | `true` | `true` | 中间节点已同步到同一开放基；这只关闭路由循环，不关闭反例终端矛盾。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 同步后开放基

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

保留 clean DLS 侧线时：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND AcyclicWindowedKloostermanDLSInternalEstimate AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一主攻点

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```
