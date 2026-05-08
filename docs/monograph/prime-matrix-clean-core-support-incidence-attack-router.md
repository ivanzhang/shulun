# Prime Matrix clean-core 支撑关联终端攻击路由器

**状态：** `clean_core_support_incidence_reduced_to_exact_layer_transfer_open`

最新真正剩余继续缩小：不是证明普通 squarefree 数量，也不是 K4/K6 incidence，而是证明 clean-core exact 层承认与非零转移。当前材料仍未证明该输入；外部替代仍是 completed、modulus-dependent Full-S KLS。

```text
clean_core_support_incidence_attack_boundary_closed=true
clean_core_exact_layer_transfer_proved=false
clean_core_terminal_support_incidence_proved=false
external_completed_kls_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorTerminalAtomPinned` | `true` | `false` | 上一层已把 exact entropy 失败压成 clean-core terminal support atom。 | 攻击该支撑原子是否可由现有材料排除。 |
| `BalancedRangeAlreadyClosed` | `true` | `true` | full-S regime 下 U,V 超过任意固定对数阈值，range 不是终端障碍。 | 只剩 exact 支撑和层转移。 |
| `RegisteredCapacityBudgetClosed` | `true` | `true` | 所有 Type/Fourier/fiber 乘子已登记为同一 formal unit 的 log-power 成本。 | 不能再用账外乘子解释 moving 原子。 |
| `BroadSupportWouldSuffice` | `true` | `true` | 一旦 exact u/v 支撑下界成立，已有初等不等式会推出 entropy/anti-atom。 | 支撑下界本身未证。 |
| `RawThickSquarefreeCountingClosed` | `true` | `true` | 厚区间内普通 squarefree/Buchstab 计数足够支付对数支撑需求。 | 不是数量问题，而是 exact 层是否承认并给出非零系数。 |
| `NaiveIncidenceBridgeBlocked` | `true` | `true` | 单个 moving (u,v) 可在内部 h,ell,x,z fiber 上平坦，K4/K6 看不见 factor 集中。 | 需要非朴素层承认/非零转移，或 completed KLS。 |
| `CanonicalLayerTransferDoesNotImportToCleanCore` | `true` | `true` | canonical RIW/Buchstab 支撑只服务 canonical-source 分支，不能偷渡到 noncanonical clean-core。 | 必须证明 clean-core 自身的 exact 层承认和非零转移。 |
| `CleanCoreExactLayerAdmissionCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 clean-core exact 层承认足够多 Buchstab products 且系数非零。 | 证明 CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。 |
| `ExternalCompletedKLSNormalFormStillOpen` | `true` | `false` | 外部替代仍是 modulus-dependent completed Full-S KLS，不是泛称 DI/BFI。 | 证明或独立接受 ModulusDependentCompletedFullSKLSInput。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 结构律

clean-core 支撑关联的 range、乘子预算和厚区间原始计数都已不是终端障碍。朴素 factor-residue incidence 被内部 fiber 模型阻断；canonical 层支撑不能导入 noncanonical clean-core。故完全自足路线必须证明 clean-core exact 层承认足够多 Buchstab products、系数非零，并把 thin/rejected blocks 回流到命名出口。

## 3. 最新输入基

条件输入基：

```text
(CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn OR ModulusDependentCompletedFullSKLSInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

其中 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn` 要求：

- exact clean-core 层承认厚 balanced block 中足够多 Buchstab products；
- 这些 products 在 actual alpha/delta 中有非零系数并贡献绝对支撑；
- thin 或 layer-rejected block 必须回流到 edge/PDEC/SAE/ColumnCRT/CleanKLS 等命名出口。

## 4. 内部 fiber 阻断模型

| k | log y | moving pairs | internal atoms | max internal share | required support | K4 flat possible | factor support fails |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 3 | 6.90776 | 1 | 750514 | 1.33242e-06 | 15728 | `True` | `True` |
| 4 | 9.21034 | 1 | 5622504 | 1.77857e-07 | 66279 | `True` | `True` |
| 5 | 11.5129 | 1 | 26810187 | 3.72993e-08 | 202269 | `True` | `True` |
| 6 | 13.8155 | 1 | 96065749 | 1.04095e-08 | 503309 | `True` | `True` |
| 7 | 16.1181 | 1 | 282615581 | 3.53838e-09 | 1087849 | `True` | `True` |
| 8 | 18.4207 | 1 | 719680491 | 1.38951e-09 | 2120940 | `True` | `True` |
| 9 | 20.7233 | 1 | 1641373385 | 6.09246e-10 | 3822003 | `True` | `True` |

该模型说明：即使内部 residue/phase fiber 很大且每个内部原子都很小，质量仍可集中在一个 moving
`(u,v)` 上。因此 K4/K6 型固定投影平坦性不能替代 clean-core exact 层承认与非零转移。

## 5. 当前结论

本步没有证明 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn`。它关闭的是错误方向：
不能再从普通 squarefree 计数、K4/K6 平坦性或 canonical 支撑偷渡推出 clean-core 支撑关联。
