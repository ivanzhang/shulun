# Prime Matrix strict 新 actual-source 熵定理非递归守门路由器

**状态：** `strict_new_actual_source_entropy_nonrecursive_guard_closed_energy_input_open`

继续硬攻后，发现并删除一个循环证明出口：`ExactUVPairMassDispersion` 的失败已经由既有路由对齐为 clean-core moving atom，因此不能再用 moving-atom 排斥或 exact entropy 来证明 pair-mass 分散，否则只是把 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 绕回自身。合法的同命题内部推进必须给出不依赖目标结论的 `IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed`，再接初等支撑能量引理。当前材料尚未证明该独立能量界，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
nonrecursive_guard_closed=true
pair_mass_return_loop_detected=true
circular_entropy_proof_rejected=true
independent_exact_pair_l2_or_max_atom_bound_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 非递归纪律

禁止的循环公式：

```text
NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem => ExactUVPairMassDispersionOrMaxAtomBoundLedger => NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

允许的非递归公式：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed => ActualNoncanonicalExactUVSupportLowerBound => NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DirectAttackSpineImported` | `true` | `true` | 上一层已保持目标不变，并把源熵定理内部压到 ExactUV 支撑脊柱。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `PairMassReturnLoopDetected` | `true` | `true` | pair-mass 分散失败等价于 clean-core moving atom；若用 moving-atom 排斥证明 pair-mass，就回到源熵目标自身。 | 禁止把 PairMassDispersion 当作独立黑箱反复引用。 |
| `CircularEntropyProofRejected` | `true` | `true` | 不能用 NewActualSourceEntropy/MovingAtomExclusion/ExactEntropy 作为 pair-mass 的证明输入。 | 必须给独立 L2/max-pair 能量账本，或命名回流。 |
| `ElementarySupportEnergyStillAvailable` | `true` | `true` | 初等 Cauchy/最大原子到支撑下界的推理可用，但只在独立能量界已经证明后才能使用。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `AcyclicSeedFusionImported` | `true` | `false` | seed 不能作为无名独立出口；若给出合法 seed，后续失败进入终端家族；若不给出 seed，也回流终端家族。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `NonrecursiveEnergyInputCurrentCorpusProved` | `false` | `false` | 当前材料没有证明不依赖源熵目标的 exact pair L2 能量界或最大 pair 原子界。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `TargetStillOpenAfterGuard` | `true` | `false` | 非递归守门只删除循环证明出口，不证明新 actual-source 熵定理。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 源熵目标仍未证明，DStructure/Rankin 与高段自足尾项仍为独立门。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新同命题内部硬点

```text
IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

完整 strict 基仍保持：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
