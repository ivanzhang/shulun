# Prime Matrix 前素数间隙 P-CRT 均匀性路由

**状态：** `predecessor_gap_pcrt_uniformity_routed_to_local_transfer_or_signed_payload_open`

大前素数间隙路线给出的核心事实是局部第一行实际素数缺口，而不是完整 P-wheel 的失衡。完整 M_{<=P} 周期内，CRT 交集在每个非 P 列精确等量，并且 c 与 P-c 精确反射对称；这些恒等式与 P 的前素数间隙无关。若要从该全周期均匀性推出初始 P x P 方阵内的补偿、非 P 列均匀或相位矛盾，必须新增局部化转移定理。当前语料没有该转移定理；该路线回流到 PDEC same-set scope 或 signed payload/ExactUV 前沿。行/列命题仍未无条件闭合。

```text
complete_wheel_non_p_uniformity_proved=true
complete_wheel_reflection_symmetry_proved=true
localized_transfer_to_initial_square_proved=false
large_predecessor_gap_symmetry_contradiction_found=false
non_p_column_uniformity_contradiction_found=false
row_column_unconditional_closed=false
next_direct_attack_target=LocalizedPCRTColumnUniformityTransferToInitialPxPSquare
```

## 1. 完整 P-wheel 恒等式

| item | statement |
| --- | --- |
| `period` | M_{<=P}=P*M_{<P} |
| `before_adding_P` | 在完整 M_{<=P} 周期中，对每个 c mod P，与 M_{<P} 互素的交集数均为 phi(M_{<P})。 |
| `after_adding_P` | 加入 P 的零类后，c=0 列全部删除；每个 c in F_P^* 仍精确保留 phi(M_{<P}) 个非零同余类交集元素。 |
| `reflection` | n -> -n mod M_{<=P} 给出 c <-> P-c 的精确全周期对称。 |
| `gap_dependence` | 前素数间隙 P-p^- 不改变上述全周期恒等式；它只说明第一行的若干实际素数原子缺失。 |

## 2. 最大前素数间隙样本（P <= 5000）

| P | previous | gap | first-row gap cols | gap/log P | min/max non-P col primes | zero cols | max c/P-c diff | gap repairs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1361 | 1327 | 34 | 33 | 4.712 | 82/121 | 0 | 29 | 33/33 |
| 4861 | 4831 | 30 | 29 | 3.534 | 267/345 | 0 | 52 | 29/29 |
| 4327 | 4297 | 30 | 29 | 3.583 | 240/314 | 0 | 52 | 29/29 |
| 3299 | 3271 | 28 | 27 | 3.456 | 190/251 | 0 | 47 | 27/27 |
| 2999 | 2971 | 28 | 27 | 3.497 | 172/232 | 0 | 42 | 27/27 |
| 3163 | 3137 | 26 | 25 | 3.226 | 176/241 | 0 | 49 | 25/25 |
| 2503 | 2477 | 26 | 25 | 3.323 | 147/203 | 0 | 42 | 25/25 |
| 4783 | 4759 | 24 | 23 | 2.833 | 262/339 | 0 | 57 | 23/23 |
| 4547 | 4523 | 24 | 23 | 2.850 | 253/322 | 0 | 53 | 23/23 |
| 4201 | 4177 | 24 | 23 | 2.877 | 231/306 | 0 | 57 | 23/23 |
| 2203 | 2179 | 24 | 23 | 3.118 | 129/180 | 0 | 34 | 23/23 |
| 1693 | 1669 | 24 | 23 | 3.228 | 104/145 | 0 | 30 | 23/23 |

样本只用于定位风险形态；证明不依赖经验无反例。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactCompletePWheelNonPColumnUniformity` | `true` | `true` | 完整 M_{<=P} 周期中，所有非 P 列的非零 CRT 交集元素数精确相等。 | closed as full-period identity |
| `ExactCompletePWheelReflectionSymmetry` | `true` | `true` | 映射 n -> -n mod M_{<=P} 精确配对 c 与 P-c 两个非零列。 | closed as full-period identity |
| `PredecessorGapOnlyCreatesFirstRowLocalDeficit` | `true` | `true` | 若 p^-<P 为前一素数，则第一行列 p^-+1,...,P-1 没有实际素数；这不是全周期 CRT 失衡。 | LocalizedPCRTColumnUniformityTransferToInitialPxPSquare |
| `FullWheelUniformityDoesNotLocalizeByItself` | `true` | `true` | 完整周期均匀性不能自动推出初始 P x P 短弧的列均匀或补偿位置。 | LocalizedPCRTColumnUniformityTransferToInitialPxPSquare OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `LargePredecessorGapSymmetryContradictionFound` | `false` | `false` | 大前素数间隙没有改变完整 P-wheel 的精确均匀恒等式，也没有单独推出局部反例矛盾。 | LocalizedPCRTColumnUniformityTransferToInitialPxPSquare |
| `NonPColumnUniformityContradictionFound` | `false` | `false` | 非 P 列全周期均匀性是真恒等式；局部非 P 列分布需要额外 actual-source 转移定理。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `LatestSignedPayloadFrontierImported` | `true` | `false` | 最新 global CRT 路线已压到 signed payload；局部化转移若要自足，必须给出 payload 或新 PDEC scope。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `PDECScopeStillExternalOrNewInput` | `true` | `false` | PDEC same-set 作用域仍可作为新证书输入，但当前内部语料未证。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `PredecessorGapPCRTCurrentCorpusClosesRowColumn` | `false` | `false` | 本证书关闭的是把大前素数间隙和完整 P-wheel 均匀性误当成最终矛盾的跳步。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明局部化转移定理，也没有证明 PDEC scope、signed payload、ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json` | `969459391db184ef4250b42c88f9947e1884ac92523320b47f887f729e8c6c56` |
| `docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.json` | `0c48c47fe0fbf1853cc8ade6d61967081693bdcc8e1fad1068452ef163a68351` |
| `docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json` | `9f10be0a0445eef5185d4e9d03dab884b330a0ae06b9ff9c7a0ffb910086a804` |
| `docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `3c7602bf11d29d837d1a05964368f085de2c10dc5e786bd518b55a85b4ce3cbf` |
