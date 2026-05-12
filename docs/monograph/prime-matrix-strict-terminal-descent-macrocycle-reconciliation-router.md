# Prime Matrix strict 终端下降宏循环调和证书

**状态：** `terminal_descent_current_attack_spine_reconciled_as_macrocycle_new_break_inputs_open`

本轮直接攻 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 的当前最窄链条。同步后发现，沿终端叶子、actual-source、exact entropy、pair-energy 和 joint constructor 继续下钻，会形成 TERMINAL -> SOURCE -> PAIR -> JOINT -> TERMINAL 宏循环。因此当前脊柱不能作为 well-founded descent 证明；非循环破环必须来自 canonical-lock 全证书、新的显式 actual joint alpha/delta 公式工件，或不经过 ExactUV/pair-energy/joint 回环的独立 actual-source 桥。

```text
terminal_descent_macrocycle_detected=true
current_terminal_descent_attack_spine_is_recursive=true
acyclic_terminal_return_well_founded_descent_proved=false
acyclic_terminal_canonical_lock_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
independent_actual_source_bridge_outside_pair_energy_loop_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
rate_preservation_ledger_proved=false
dstructure_independent_gate_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 宏循环链

| from | to |
| --- | --- |
| AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate | TerminalLeafFirewallInputs_OR_CanonicalLock |
| TerminalLeafFirewallInputs_OR_CanonicalLock | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn |
| IndependentActualSourceBridgeNotFactoredThroughAlphaReturn | A1CleanBranchCanonicalSourceAdmission OR ExactCleanCoreFullSNonAPWFDSourceEntropy |
| ExactCleanCoreFullSNonAPWFDSourceEntropy | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple | signed-source fixed point |
| signed-source fixed point | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |

## 2. 非循环破环字段

| field | meaning |
| --- | --- |
| `canonical_lock_full_certificate` | 证明 acyclic 终端同集推前、有限因子图、branch key 锁定和无 noncanonical payload 残留。 |
| `new_joint_formula` | 提交 actual joint alpha/delta 正向公式；同一行给出 basis word、signed coefficient、u/v、branch、sign/local factor。 |
| `independent_actual_source_bridge` | 在进入 ExactUV/pair-energy/alpha 回边前证明 actual source 恒等或强化反原子。 |
| `parallel_exactuv_rate_dstructure` | 即使破环成功，仍需 ExactUV bounded multiplicity、RatePreservation 和 DStructure/Rankin 独立门。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalDescentStillActiveAsAlternative` | `true` | `false` | 显式 joint 构造器直接攻坚后，非循环替代仍指向终端下降证书。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `DescentLeafAlphaRouteIsBackedge` | `true` | `true` | 终端下降的旧 pointwise/alpha 下钻已被登记为回边，不能计为 well-founded 进展量。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn |
| `IndependentBridgeReducedToSourceAdmissionOrEntropy` | `true` | `false` | independent actual-source 桥已具体化为 A1 source admission 或 exact entropy，但二者均未证明。 | A1CleanBranchCanonicalSourceAdmission OR ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `ExactEntropyRouteReturnsToPairEnergyInput` | `true` | `true` | exact entropy 经非递归守门后不能用自身回证 pair-mass，只剩独立 pair L2/max-atom 能量输入。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `PairEnergyCurrentSpineReturnsToJointConstructor` | `true` | `true` | 现有 pair-energy/rate-packet/terminal 脊柱为递归脊柱，已重钉到 joint constructor 工件。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `JointConstructorReturnsToTerminalDescent` | `true` | `true` | 没有新的显式 joint 公式时，joint-alpha/signed-source 路线回到终端下降替代门。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `TerminalDescentMacrocycleDetected` | `true` | `true` | 当前终端下降直攻链形成 TERMINAL -> SOURCE -> PAIR -> JOINT -> TERMINAL 宏循环。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop |
| `CurrentTerminalDescentAttackSpineRejectedAsProof` | `true` | `true` | 该宏循环只能作为路线审查结论，不能作为终端矛盾或 well-founded descent 证明。 | 必须提交破环输入。 |
| `CanonicalLockStillOpenParallel` | `true` | `false` | canonical-lock 仍是并行破环路线，但其同集推前、有限因子图和无 payload 残留未证。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `NewJointFormulaStillOpen` | `true` | `false` | 显式 joint 构造器需要新的正向公式工件；当前语料没有该工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `IndependentBridgeOutsidePairEnergyLoopStillOpen` | `true` | `false` | 若继续走 actual-source 桥，必须在 ExactUV/pair-energy/joint 回环前独立证明源恒等或强化反原子。 | IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 宏循环已暴露但未产生矛盾；ExactUV、RatePreservation 与 DStructure/Rankin 门仍未全部闭合。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 当前严格活动基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只证明当前终端下降直攻脊柱是宏循环，不能把宏循环本身当作矛盾或闭合证明。
