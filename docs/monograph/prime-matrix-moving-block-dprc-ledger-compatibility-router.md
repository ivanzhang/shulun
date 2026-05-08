# Prime Matrix moving-block 与 DPRC 账本兼容性路由器

**状态：** `moving_block_dprc_ledger_compatibility_closed_modelgap_open`

本步关闭的是兼容性接口，不是 DPRC 模型余量账本自身。从 moving-block 到早期零行终端包、再到 global PDEC/sparse、PDEC-CAP/internal-KLS、最后到 canonical 终端晋级，所有替换都只发生在终端原子上；ExplicitModelGapAndFiniteDPRCLedger 一直作为同名、同位的独立输入保留。因此 ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock 可从活动输入基中删除，下一最窄目标转为 ExplicitModelGapAndFiniteDPRCLedger 本身。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
exact_model_gap_dprc_compatibility_proved=true
explicit_model_gap_and_finite_dprc_ledger_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
closed_input_removed=ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock
closed_interface_atom=NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation
```

## 1. 兼容性引理

```text
ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock
  =>
NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation
  => 从活动输入基删除该兼容性门，保留 ExplicitModelGapAndFiniteDPRCLedger。
```

严格含义：本引理只说明 moving-block 终端替换没有引入新的 DPRC 账本对象。它不证明 `ExplicitModelGapAndFiniteDPRCLedger`，也不关闭完整行列无条件定理。

## 2. 账本轨迹

```text
ActualNoncanonicalMovingBlockSpreadNCBLK
  -> EarlyZeroTerminalExclusionPackage + ExactCompatibility
  -> GlobalPDECorSparseTerminalExclusion + ExactCompatibility
  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve + ExactCompatibility
  -> NoFurtherCanonicalSourceTerminalPromotionGap + ExactCompatibility
  -> NoFurtherCanonicalSourceTerminalPromotionGap

ExplicitModelGapAndFiniteDPRCLedger 在每一层均作为独立原子保留。
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExactCompatibilityGateActive | `true` | `false` | 最新最窄点正是 moving-block 替换与 DPRC 模型账本的精确兼容性。 | ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内做账本调和，不用真实样本缺席。 | 保持 row_column_unconditional_closed=false。 |
| MovingBlockRouterSeparatedTerminalAndLedger | `true` | `true` | moving-block 路由只把运动块终端压到早期零行终端包，并把兼容性门单列；模型账本仍是独立原子。 | ExplicitModelGapAndFiniteDPRCLedger |
| SchemaReconciliationPreservedDPRCLedgerAtom | `true` | `true` | 早期零行终端包到全局 PDEC/sparse 的调和只替换终端原子，兼容性门和模型账本各出现一次。 | 无额外 DPRC 口径变化。 |
| GlobalPDECSparseSplitPreservedDPRCLedgerAtom | `true` | `true` | GlobalPDEC/sparse 到 PDEC-CAP/internal-KLS 的拆分没有重命名或吸收 ExplicitModelGapAndFiniteDPRCLedger。 | 无 moving-block 专属模型账本。 |
| TerminalPromotionPreservedDPRCLedgerAtom | `true` | `true` | 当前 canonical 终端晋级只关闭终端侧，不改写模型余量/有限 DPRC 账本。 | 终端闭合不能被误读为模型账本证明。 |
| DPRCModelLedgerObjectPinned | `true` | `true` | DPRC 路由把 ExplicitModelGapAndFiniteDPRCLedger 固定为 RSM 模型余量与有限证书接口。 | 证明该模型账本自身仍是独立义务。 |
| NoMovingBlockSpecificDPRCRelabelingGap | `true` | `true` | 从 moving-block 到 canonical 终端晋级，变化只发生在终端原子；DPRC 账本对象同名、同位、同用途保留。 | NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation |
| ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock | `true` | `true` | 兼容性门闭合为接口事实：没有新增 moving-block 专属 DPRC 账本缺口。 | NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation |
| ExplicitModelGapAndFiniteDPRCLedger | `false` | `false` | 模型余量/有限 DPRC 账本本身尚未由本路由证明；P<2003 有限表与 P>=2003 模型余量仍需正式闭合。 | ExplicitModelGapAndFiniteDPRCLedger |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ExplicitModelGapAndFiniteDPRCLedger) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

当前最窄目标变为 `ExplicitModelGapAndFiniteDPRCLedger`：把 `P<2003` 的有限证书和 `P>=2003` 的 `S(1-H)>3sqrt(S)` 模型余量写成可独立审查的正式账本。并行保留 generic/external DI/BFI 分支和 DStructure/Rankin 最终验收门。
