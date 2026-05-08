# Prime Matrix clean-core exact entropy 原子路由器

**状态：** `clean_core_exact_entropy_reduced_to_terminal_support_incidence_open`

最新终局输入的可行动证明包继续向内压到一个可审查的支撑-关联定理：必须证明 clean-core 内部不能存在正质量、无回流、同一 moving (u,v) 承载过大容量的终端支撑原子。当前材料仍未证明该定理，所以 exact entropy 和无条件行/列命题仍未闭合。

```text
clean_core_exact_entropy_atom_boundary_closed=true
clean_core_terminal_support_incidence_proved=false
exact_clean_core_entropy_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalExactEntropyPinned` | `true` | `false` | 上一层已把内部终局标准形固定为 exact clean-core source entropy。 | 审查该熵命题失败时的最小原子。 |
| `EntropyFailureIsCleanCoreMovingAtom` | `true` | `false` | exact entropy 失败等价于存在 clean-core moving same-(u,v) 大原子。 | 排除这个大原子，或给出可回流证书。 |
| `BroadSupportContradictsMovingAtom` | `true` | `false` | 已有条件链说明：balanced range、divisor bound、registered multiplier 与 exact u/v 支撑下界合在一起会推出 source entropy。 | 真正未证的是 clean-core 内部的 exact u/v 支撑-关联下界。 |
| `RegisteredMultiplierEscapeRemoved` | `true` | `true` | Type/Fourier/fiber 乘子已登记进同一 formal unit 的 log-power 账本。 | 熵失败不能再归咎于账外容量乘子。 |
| `ExactUVSupportStillNotProved` | `true` | `false` | ExactUVSupport 已被审查为源侧终端输入，不能由 K4/K6、formal WFD 或 canonical 支撑偷渡推出。 | 需要新的 clean-core 支撑-关联定理。 |
| `SupportFailurePacketizationAvailable` | `true` | `false` | 若支撑下界失败，必须生成带 source class、formal unit、block key 和容量剖面的 packet。 | packet 仍可能是 clean-core 终端 packet。 |
| `NonCleanCoreReturnClosed` | `true` | `true` | 非 clean-core packet 已回流到有限孤立、持久签名、ColumnCRT/位移、漂移 CleanKLS/DLS 或已阻断逃逸。 | 只剩通过全部回流测试的 clean-core 终端原子。 |
| `CleanCoreTerminalSupportIncidenceCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 clean-core 内部每个正质量 block 都有足够 exact u/v 支撑扩散。 | 证明 CleanCoreTerminalSupportIncidenceTheorem。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧输入完成后仍需独立验收。 |

## 2. 原子律

若 ExactCleanCoreFullSNonAPWFDSourceEntropy 失败，则存在 clean-core moving 大原子。由于乘子逃逸已登记、非 clean-core packet 已回流，失败只能落到通过全部回流测试的 clean-core terminal support atom。

## 3. 最新可行动自足输入

```text
CleanCoreTerminalSupportIncidenceTheorem
```

每个通过全部回流测试的正质量 actual clean-core full-S non-AP WFD block，在同一 formal unit 内必须给出 exact u/v 支撑乘积的对数幂下界，足以抵消 divisor bound 与所有 registered capacity multipliers；否则它就是一个可复现的 clean-core terminal support atom。

连同独立晋级门，形成可行动证明包：

```text
CleanCoreTerminalSupportIncidenceTheorem AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 当前结论

本步没有证明 `CleanCoreTerminalSupportIncidenceTheorem`。它完成的是原子化：
exact clean-core entropy 的失败不再是无名失败，只能表现为通过全部回流测试的 clean-core
terminal support atom。
