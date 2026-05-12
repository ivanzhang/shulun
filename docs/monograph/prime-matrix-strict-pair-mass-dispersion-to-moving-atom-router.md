# Prime Matrix 严格 pair-mass 分散到 moving-atom 对齐路由器

**状态：** `pair_mass_dispersion_reduced_to_acyclic_seed_and_clean_core_moving_atom_open`

pair-mass 分散失败不会产生一个新的终端硬点。最大 pair 原子界失败，等价于同一 formal unit 中出现 sign-refined exact (u,v) 大原子；registered multiplier discipline 把它与最终容量大原子对齐，支撑失败 packet 回流字母表再排除非 clean-core 出口。剩下的正是既有终端 ActualNoncanonicalCleanCoreMovingAtomExclusion，其内部标准形是 ExactCleanCoreFullSNonAPWFDSourceEntropy。因此严格自足源侧剩余被去重为：无环 pre-Cauchy source seed + clean-core moving atom 排斥。当前二者仍未证明，不能声明行/列无条件闭合。

```text
pair_mass_dispersion_boundary_closed=true
pair_mass_dispersion_not_separate_terminal=true
acyclic_pre_cauchy_seed_proved=false
clean_core_moving_atom_exclusion_proved=false
actual_exact_uv_support_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ActualNoncanonicalCleanCoreMovingAtomExclusion
```

## 1. 去重压缩链

```text
ExactUVPairMassDispersionOrMaxAtomBoundLedger fails
  -> sign-refined exact (u,v) large pair atom
  -> registered capacity large atom
  -> support-failure packet return alphabet
  -> clean-core moving atom
  -> ActualNoncanonicalCleanCoreMovingAtomExclusion
  -> ExactCleanCoreFullSNonAPWFDSourceEntropy
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PairMassDispersionInputActive` | `true` | `false` | 上一层把 ExactUV 支撑数值负担压成 exact pair 最大原子/能量控制。 | 判断 pair-mass 分散失败是否是新终端。 |
| `LargePairAtomEquivalenceClosed` | `true` | `true` | 最大 pair 界失败等价于存在同一 formal unit 内的 sign-refined exact (u,v) 大原子。 | 把该大原子接入已登记容量与回流字母表。 |
| `RegisteredMultiplierBridgeImported` | `true` | `true` | Type/Fourier/fiber 乘子纪律已闭合，exact pair 质量阈值可与最终容量大原子阈值对齐。 | 桥接不排斥大原子，只防止账外乘子解释。 |
| `FailurePacketReturnAlphabetImported` | `true` | `true` | 非 clean-core 的大原子必须回流到 finite sparse、PDEC、SAE/ColumnCRT、CleanKLS/DLS 或外部谱分支。 | 只剩通过全部回流测试的 clean-core moving atom。 |
| `CleanCoreMovingAtomNormalFormImported` | `true` | `true` | clean-core 大 pair 原子的 sharp 标准形是 ActualNoncanonicalCleanCoreMovingAtomExclusion，内部等价为 exact clean-core source entropy。 | 证明 moving atom 排斥或 exact source entropy。 |
| `PairMassDispersionNotSeparateTerminal` | `true` | `true` | ExactUVPairMassDispersionOrMaxAtomBoundLedger 不是新增第三终端；失败对象就是已命名 moving atom。 | 保留源种子 + moving atom 排斥两个真实输入。 |
| `MovingAtomExclusionCurrentCorpusProved` | `true` | `false` | 当前材料没有证明 actual noncanonical clean-core moving atom exclusion 或 exact source entropy。 | ActualNoncanonicalCleanCoreMovingAtomExclusion。 |
| `AcyclicSeedCurrentCorpusProved` | `true` | `false` | 当前材料仍未提交无环 pre-Cauchy actual noncanonical primitive source seed。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。 |

## 3. 下一主攻合同

下一数学主攻点：`ActualNoncanonicalCleanCoreMovingAtomExclusion_FOR_AcyclicPreCauchySeed`。

必须证明：
- 给出无环 pre-Cauchy actual noncanonical primitive source seed。
- 在同一 formal unit 内定义最终登记容量测度 M_{u,v}。
- 证明通过全部回流测试的 clean-core 残余没有 moving same-(u,v) 大原子。
- 等价地证明 exact clean-core full-S non-AP WFD source entropy。
- 把大原子、熵失败、source 缺失、超预算和抵消全部命名回流。

不能作为证明使用：
- 把 ExactUVPairMassDispersion 当作独立新黑箱反复引用。
- formal WFD、K4/K6、Type/Fourier fixed projection 平坦性。
- canonical RIW/Buchstab source entropy 跨分支导入。
- 早期零行真实样本缺席或 payment skeleton 反推 source。
- 未精确匹配的外部 KLS/DI/BFI。

严格自足数学基更新为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ActualNoncanonicalCleanCoreMovingAtomExclusion AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

等价内部标准形：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExactCleanCoreFullSNonAPWFDSourceEntropy
```
