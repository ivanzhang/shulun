# Prime Matrix noncanonical 源核心原子化路由器

**状态：** `noncanonical_source_core_atomized_to_actual_support_capacity_open`

最窄自足剩余再原子化：`source entropy` 与 `strengthened anti-atom` 不是两条路，它们共同等价地要求 actual noncanonical full-S 源的精确因子支撑与 Type/Fourier 容量兼容。balanced range 已闭合；K4/K6、朴素 incidence、canonical 支撑偷渡都不能证明它。因此当前真正数学原子是 `ActualNoncanonicalFullSFactorSupportCapacityTheoremInput`，另加 DStructure/Rankin 独立验收。

```text
source_core_atomization_closed=true
entropy_antiatom_duality_removed=true
balanced_range_threshold_closed=true
k4_k6_or_naive_incidence_suffices=false
canonical_import_allowed=false
actual_support_capacity_core_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | meaning | consequence |
| --- | --- | --- | --- |
| `NarrowestSelfContainedCorePinned` | `true` | 上一层已把无外部黑箱的全局剩余压成 actual noncanonical 源核心 + Rankin。 | 可继续判断 entropy 与 anti-atom 是否是两个不同输入。 |
| `ExactEntropyReducedToSupportPackage` | `true` | exact full-S source entropy 已降为精确支撑包。 | entropy 不是新的谱黑箱；它由支撑/容量包支付。 |
| `BalancedRangeRemoved` | `true` | full-S regime 中 balanced range 阈值已闭合。 | 剩余支撑包只含 exact factor support 与 Type/Fourier capacity compatibility。 |
| `AntiAtomSameAsSupportCapacity` | `true` | 强化源反原子正是 final source capacity measure 无 moving same-(u,v) 原子。 | anti-atom 与 entropy 共同指向同一个支撑/容量核心。 |
| `K4K6DoNotProveExactSupport` | `true` | K4 固定 residue flatness 与 K6 dyadic bookkeeping 不能推出 moving factor support。 | 不能把已有 clean admission 直接升级为源核心证明。 |
| `NaiveIncidenceBridgeBlocked` | `true` | 朴素 factor-residue incidence 被一个 (u,v) 块内的大内部 fiber 阻断。 | 支撑失败不会自动回流 K4/K6；需要直接证明 actual 支撑/容量包。 |
| `DStructureRankinStillIndependent` | `true` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源核心证明完成后仍需独立验收才能升级为完整全局定理。 |

## 2. 上一层输入基

```text
ActualNoncanonicalFullSSourceEntropyOrStrengthenedAntiAtomTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 原子化后输入基

```text
ActualNoncanonicalFullSFactorSupportCapacityTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. actual 支撑/容量合同

对每个幸存的 actual noncanonical full-S non-AP balanced block，证明精确 u、v 因子有对数幂级绝对支撑下界，并证明 Type/Fourier 容量兼容，使任何 moving (u,v) 对都不能获得未登记的容量乘子。

## 5. 结构律

actual noncanonical source entropy 与 strengthened anti-atom 是同一个剩余源容量核心的两种命名。full-S regime 中 balanced range 已闭合；唯一内部数学原子是 actual noncanonical 系数的精确支撑/容量定理。K4/K6、朴素 incidence 与 canonical RIW/Buchstab 偷渡都已作为捷径被阻断。

## 6. 当前结论

这一步闭合的是命名二义性和伪捷径排除，不是证明 actual 支撑/容量核心。
完整行/列无条件定理仍需该核心输入与 DStructure/Rankin 独立验收。
