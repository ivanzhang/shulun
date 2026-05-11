# Prime Matrix 严格 moving-atom 到全局终端门路由器

**状态：** `strict_moving_atom_reduced_to_global_terminal_and_model_dprc_open`

严格 moving-atom 输入已经接回反例链：若 acyclic source seed 下仍存在 clean-core moving atom，它作为 actual same-(u,v) moving block 必须进入已登记的低维签名终端，或无签名 L2-flat 终端包；抽象 EarlyZeroTerminalExclusionPackage 已被后续 schema 调和为 GlobalPDECorSparseTerminalExclusion，而 moving-block 专属 DPRC 兼容门已闭合并可删除。因此 moving atom 排斥不再是当前最窄项；剩余转为 GlobalPDECorSparseTerminalExclusion 与 ExplicitModelGapAndFiniteDPRCLedger，另保留 acyclic source seed 和自足 DStructure/Rankin 替代包。当前仍没有无条件闭合。

```text
strict_moving_atom_boundary_closed=true
dprc_compatibility_gate_removed=true
acyclic_pre_cauchy_seed_proved=false
global_pdec_sparse_terminal_exclusion_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger
```

## 1. 压缩链

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
  -> actual same-(u,v) moving block contradiction branch
  -> EarlyZeroTerminalExclusionPackage
  -> GlobalPDECorSparseTerminalExclusion
  -> ExplicitModelGapAndFiniteDPRCLedger remains independent
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictMovingAtomInputActive` | `true` | `false` | 上一层严格源侧剩余包含 Acyclic seed 与 ActualNoncanonicalCleanCoreMovingAtomExclusion。 | 攻击 moving atom 排斥本身。 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在 Assume EarlyZeroRowWithinP 的假设链条内推理，不用真实样本缺席。 | 所有输出必须是反例链内的命名终端或账本。 |
| `AcyclicSeedOnlyProvidesObject` | `true` | `true` | 无环 source seed 只保证 actual source 对象准入；它本身不排斥 moving atom。 | moving atom 若存在，必须继续通过终端回流测试。 |
| `MovingBlockTerminalReductionImported` | `true` | `true` | actual same-(u,v) moving block 有低维签名则进 PDEC/SAE/ColumnCRT；无签名则进早期零行终端包。 | EarlyZeroTerminalExclusionPackage。 |
| `EarlyZeroPackageReconciledImported` | `true` | `true` | 抽象 EarlyZeroTerminalExclusionPackage 已与命名 schema 调和，收缩为 GlobalPDECorSparseTerminalExclusion。 | GlobalPDECorSparseTerminalExclusion。 |
| `DPRCCompatibilityImported` | `true` | `true` | ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock 已闭合为接口事实，可删除该兼容性门。 | ExplicitModelGapAndFiniteDPRCLedger 仍保留为独立账本。 |
| `MovingAtomExclusionReducedToGlobalTerminal` | `true` | `true` | 在反例链内，排斥 clean-core moving atom 足以转为排斥全局 PDEC/sparse 终端证书并支付模型账本。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger。 |
| `GlobalTerminalCurrentCorpusProved` | `true` | `false` | 当前材料尚未无条件排斥已物化的 persistent PDEC、ColumnCRT、SAE/LocalSurvivor 或 sparse packet 终端证书。 | GlobalPDECorSparseTerminalExclusion。 |
| `ExplicitModelGapDPRCCurrentCorpusProved` | `true` | `false` | 模型余量/有限 DPRC 账本自身仍未闭合。 | ExplicitModelGapAndFiniteDPRCLedger。 |

## 3. 下一主攻合同

下一数学主攻点：`GlobalPDECorSparseTerminalExclusion_WITH_ExplicitModelGapAndFiniteDPRC`。

必须证明：
- 排斥已物化的 persistent primitive PDEC 终端证书，或给出全量 PDEC 容量上界。
- 排斥 ColumnCRT/位移/endpoint/cofactor 终端证书，或证明其必回流到 PDEC/SAE。
- 排斥 SAE/LocalSurvivor/sparse packet 终端证书，或提交有限全集 extractor。
- 闭合 P<2003 有限 DPRC 证书与 P>=2003 模型余量账本。
- 保持所有步骤在假设早期零行反例链内，不使用真实样本缺席。

不能作为证明使用：
- 把 acyclic source seed 当作 moving atom 排斥。
- 把 EarlyZeroTerminalExclusionPackage 当作已排斥。
- 重复引用已删除的 ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock。
- 把外部 KLS/DI/BFI 作为严格自足证明。
- 把命名回流 schema 当作终端家族不存在的证明。

严格自足数学基更新为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
