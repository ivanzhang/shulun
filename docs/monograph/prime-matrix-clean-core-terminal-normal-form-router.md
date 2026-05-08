# Prime Matrix clean-core 终局输入标准形路由器

**状态：** `clean_core_terminal_normal_form_closed_inputs_open`

最新终局输入已归一化：完全自足路线必须证明 exact clean-core full-S non-AP WFD source entropy；外部路线必须证明或接受 completed、modulus-dependent 的 full-S KLS 输入。当前材料只关闭命名和等价边界，没有证明任一输入。

```text
clean_core_terminal_normal_form_closed=true
internal_exact_entropy_proved=false
external_completed_kls_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved/accepted | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SharpMovingAtomPinned` | `true` | `false` | 上一层已把 self-contained sharp 输入固定为 clean-core moving atom 排斥。 | 判断它的最清晰标准形。 |
| `MovingAtomEqualsSourceEntropy` | `true` | `false` | 无 moving 大原子就是 max_b M_b/M <= log^{-2A} 的 exact source entropy 表述。 | 证明 actual clean-core 系数满足该熵界。 |
| `SourceEntropyImpliesNCBLK` | `true` | `false` | source entropy 一旦证明，立即给出 NC-BLK 块能量节省。 | source entropy 本身仍未证明。 |
| `ExactWFDSourceEntropyReduced` | `true` | `false` | exact source entropy 可由 exact factor support 与容量兼容推出。 | exact factor support 不是当前 ledger 已证事实。 |
| `NoCanonicalOrFormalShortcut` | `true` | `false` | canonical 偷渡、APSourceLift 与 formal WFD 推出 source entropy 的路线已阻断。 | 必须证明 actual clean-core exact entropy，而非 generic 模板。 |
| `ExternalKLSNormalFormPinned` | `true` | `false` | 外部 FullS KLS 输入已被完成分解压成 c-dependent completed KLS。 | 证明或引用 ModulusDependentCompletedFullSKLSInput。 |
| `InternalExternalNormalFormComplete` | `true` | `false` | 内部 moving-block 与外部 FullS KLS 两线已归一化为 exact entropy 或 completed KLS。 | 二者至少一项仍需证明或独立接受。 |
| `TerminalNormalFormCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 exact clean-core source entropy，也没有接受 completed KLS 外部输入。 | 证明 ExactCleanCoreFullSNonAPWFDSourceEntropy，或接受 ModulusDependentCompletedFullSKLSInput。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 数学输入完成后仍需独立验收。 |

## 2. 标准形律

ActualNoncanonicalCleanCoreMovingAtomExclusion 的内部标准形就是 exact clean-core source entropy：max_b M_b/M <= log^{-2A}。外部替代标准形不是泛称 DI/BFI，而是 full-S 完成后带 c-dependent residue weights 的 ModulusDependentCompletedFullSKLSInput。

## 3. 输入基

上一层源侧微输入：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
```

内部标准形：

```text
ExactCleanCoreFullSNonAPWFDSourceEntropy
```

外部标准形：

```text
ModulusDependentCompletedFullSKLSInput
```

条件终局输入基：

```text
(ExactCleanCoreFullSNonAPWFDSourceEntropy OR ModulusDependentCompletedFullSKLSInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ExactCleanCoreFullSNonAPWFDSourceEntropy AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 当前结论

本步没有证明 exact source entropy，也没有接受 completed KLS；它关闭的是终局输入标准形。
下一步若坚持完全自足，应直接证明 `ExactCleanCoreFullSNonAPWFDSourceEntropy`。
