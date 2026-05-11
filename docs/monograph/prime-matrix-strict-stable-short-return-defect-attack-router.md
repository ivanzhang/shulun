# Prime Matrix strict 稳定短复现/相位缺陷硬点拆分路由器

**状态：** `stable_short_return_or_phase_defect_reduced_to_type_compression_label_product_drift_defect_open`

`StableShortSameLabelRecurrenceOrRegisteredPhaseDefect` 被继续拆开：短稳定同标签复现一旦成立就由 CRT 立刻矛盾，这部分已经不是硬点。真正硬点是证明早期零行强制产生这种复现；形式上需要边界帽 formal-unit 类型压缩、稳定复现保留标签集的乘积下界，以及不复现/漂移时进入已登记相位缺陷。这三项均未由当前语料证明，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
crt_short_recurrence_contradiction_imported=true
boundary_2p_recurrence_not_independent_exit=true
type_compression_dichotomy_proved=false
stable_return_large_label_product_proved=false
signature_drift_to_registered_phase_defect_proved=false
early_zero_forces_stable_short_return_or_defect_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 硬点拆分

拆分前：

```text
StableShortSameLabelRecurrenceOrRegisteredPhaseDefect
```

拆分后：

```text
BoundaryCapFormalUnitTypeCompressionDichotomy AND StableReturnLargeLabelSupportProductLowerBound AND SignatureDriftToRegisteredPhaseDefectTheorem
```

CRT 短复现矛盾的后半段已清楚；缺的是上游强制机制。若只说边界 2P 短复现，命题与首零行 >P 同强；若只引用实验，不能替代正式证明。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ShortReturnHardpointActive` | `true` | `false` | 上一层把直接矛盾首选点压成同 formal unit 短稳定复现或登记相位缺陷。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect |
| `CRTPayloadContradictionImported` | `true` | `true` | 若同标签稳定复现保留素标签集 Q，则 prod(Q)\|Delta；短于 prod(Q) 即矛盾。 | 要证明的是短复现或相位缺陷的产生机制。 |
| `Boundary2PRecurrenceNotIndependentExit` | `true` | `true` | 边界 2P 短复现禁止与首零行超过 P 同强，不能作为独立证明出口。 | 必须改攻边界帽 formal-unit 类型压缩或相位非覆盖。 |
| `EarlyZeroNamedContradictionMatrixImported` | `true` | `true` | 早期零行已进入 CLB、formal unit、carry-shell、anchor-collar、PDEC/SAE/ColumnCRT 命名矩阵。 | AnchorCollarPrimeFiberCapacityBoundOrPDECReturn |
| `FormalUnitRecordsAvailableButNotCompressed` | `true` | `true` | 任意假设 witness 可抽取稳定 formal unit 记录，且哈希命名稳定。 | 尚未证明边界帽内 formal unit 类型数小于强制实例数。 |
| `PhaseRecurrenceScanImportedAsDiagnosticOnly` | `true` | `true` | 诊断显示大标签乘积超过 P 的后半段压力强；但自然短步长不自动给全覆盖复现。 | 不能用实验样本替代类型压缩证明。 |
| `TypeCompressionDichotomyCurrentCorpusProved` | `false` | `false` | 尚未证明边界帽中 forced formal units 的规范类型数足够小，从而鸽巢得到同 formal unit 短复现。 | BoundaryCapFormalUnitTypeCompressionDichotomy |
| `StableReturnLargeLabelProductCurrentCorpusProved` | `false` | `false` | 即便得到稳定复现，还需证明被保持的标签集 Q 的乘积超过位移上界。 | StableReturnLargeLabelSupportProductLowerBound |
| `SignatureDriftToDefectCurrentCorpusProved` | `false` | `false` | 若类型不复现或标签漂移，尚未证明漂移必产生已登记 PDEC/SAE/ColumnCRT 相位缺陷。 | SignatureDriftToRegisteredPhaseDefectTheorem |
| `StableShortReturnOrDefectCurrentCorpusProved` | `false` | `false` | 短复现硬点已拆成类型压缩、标签乘积下界、漂移缺陷三原子；三者尚未合取证明。 | BoundaryCapFormalUnitTypeCompressionDichotomy AND StableReturnLargeLabelSupportProductLowerBound AND SignatureDriftToRegisteredPhaseDefectTheorem |

## 3. 下一步证明计划

| step | content |
| --- | --- |
| `BoundaryCapFormalUnitTypeCompressionDichotomy` | 在边界帽内固定 source_family、phase_key、anchor/carry-shell 字段，证明规范类型数小于被迫覆盖实例数；否则超类型增长必须登记为新 layer/phase defect。 |
| `StableReturnLargeLabelSupportProductLowerBound` | 对重复的同 formal unit，提取保持的高标签子集 Q；用覆盖无漏和短纤维容量证明 prod(Q) 超过允许位移上界。 |
| `SignatureDriftToRegisteredPhaseDefectTheorem` | 若不能保持 Q，则记录标签替换、列位移或相位键变化；证明其给出 PDEC/SAE/ColumnCRT 的显式坏窗集合与同账本权重。 |

首要硬攻点：

```text
BoundaryCapFormalUnitTypeCompressionDichotomy
```
