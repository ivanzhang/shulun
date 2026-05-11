# Prime Matrix strict acyclic NC-BLK/source anti-atom 去重路由器

**状态：** `strict_acyclic_ncblk_source_antiatom_deduplicated_to_global_terminal_open`

`AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom` 被继续硬攻后，不能作为已经证明的反原子使用；但它也不再是独立无名终端。generic WFD 版反原子已被 moving-delta 阻断；actual acyclic 版若失败，就等价于同一 formal unit 的 exact (u,v) 大原子，即 clean-core moving atom。既有 moving-atom 路由把该对象接回全局 PDEC/sparse 终端和模型/DPRC 账本。因此当前 strict 自足链的真正剩余是 acyclic pre-Cauchy source seed、acyclic noncanonical 终端家族、高段 Mertens/PNT 自足尾项和 DStructure/Rankin 替代包。行/列命题仍未无条件闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
acyclic_ncblk_not_separate_terminal=true
acyclic_ncblk_actual_block_nonconcentration_proved=false
acyclic_strengthened_source_antiatom_proved=false
acyclic_pre_cauchy_seed_proved=false
strict_acyclic_terminal_family_proved=false
self_contained_mertens_tail_proved=false
self_contained_dstructure_rankin_replacement_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger
```

## 1. 去重链

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom fails
  -> generic WFD anti-atom route blocked by moving-delta no-go
  -> actual acyclic route produces sign-refined exact (u,v) large atom
  -> ActualNoncanonicalCleanCoreMovingAtomExclusion
  -> GlobalPDECorSparseTerminalExclusion
  -> ExplicitModelGapAndFiniteDPRCLedger
  -> strict scope: PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

这说明 NC-BLK/source anti-atom 不是已经闭合的定理，也不是新的第四终端；它被去重到已有全局终端门。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AcyclicNCBLKSourceAntiAtomInputActive` | `true` | `false` | 上一层 strict acyclic Kuznetsov/DLS 原子已压到实际块非集中或强化源反原子。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只在假设早期零行反例链内做对象替换和回流；不使用真实零行缺席。 | 所有失败态必须进入命名终端或保留为开放输入。 |
| `GenericWFDNoGoImported` | `true` | `true` | generic full-S/WFD 形式反原子已被 moving-delta 模型阻断，不能作为 strict 自足证明。 | 必须使用 actual acyclic source 结构，或转条件外部谱线。 |
| `ExactPairLargeAtomEquivalenceImported` | `true` | `true` | actual NC-BLK/反原子失败等价于同一 formal unit 中出现 sign-refined exact (u,v) 大原子。 | 该大原子就是 clean-core moving atom。 |
| `MovingAtomNormalFormImported` | `true` | `true` | registered capacity multiplier discipline 与 failure-packet 字母表把大原子标准化为 clean-core moving atom。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `MovingAtomReturnImported` | `true` | `true` | strict moving-atom 路由已把 clean-core moving atom 接回全局 PDEC/sparse 终端与模型/DPRC 账本。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| `SeedNoGoScopeImported` | `true` | `true` | 早期零行假设只给 unsigned 覆盖数据，不能反向生成 pre-Cauchy signed source seed。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn 仍是独立输入。 |
| `IndependentIdentityTaxonomyImported` | `true` | `true` | 独立 pre-Cauchy 来源恒等式的合法来源类已穷尽；非 canonical 自足路线最终汇合到 moving-block/NC-BLK。 | 不能把来源恒等式当作隐藏第四出口。 |
| `AcyclicNCBLKNotSeparateTerminal` | `true` | `true` | 在当前 strict 语料中，NC-BLK/source anti-atom 失败不是新终端；它去重为 moving atom，再接回全局终端门。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| `AcyclicNCBLKActualBlockNonconcentrationCurrentCorpusProved` | `true` | `false` | 本步没有证明 NC-BLK 块非集中；只是证明其失败对象已有命名回流位置。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| `StrictGlobalTerminalScopeImported` | `true` | `true` | 全局终端门在 strict noncanonical 口径下继续校准为 acyclic PDEC-CAP/CleanKLS 家族。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `HighTailCorpusImported` | `true` | `false` | 若不接受外部 Mertens/theta 定理，高段尾项仍需自足 PNT/Mertens 内联证明。 | SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `StrictTerminalFamilyCurrentCorpusProved` | `true` | `false` | strict acyclic 终端家族仍未证明；canonical-source 闭合不能直接导入 noncanonical seed。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | NC-BLK 去重后仍缺 acyclic source seed、strict 终端家族、高段自足尾项或外部输入、DStructure/Rankin 替代包。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基更新为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`AcyclicPreCauchySeed_AND_AcyclicTerminalFamily`。

必须证明：
- 提交不依赖 downstream 覆盖图的 acyclic pre-Cauchy actual noncanonical source seed。
- 证明 acyclic noncanonical 终端家族的 PDEC-CAP/CleanKLS 全局排斥，或把失败全部命名回流。
- 若坚持严格自足，还要内联 Mertens/theta 高段尾项证明。
- 提交 SelfContainedDStructureTailLog4FiniteRankinReplacementPackage 或明确接受独立验收门。
- 全过程保持假设链条与真实链条分离。

不能作为证明使用：
- 把 generic WFD/formal Type/Fourier 反原子当作已证。
- 把 NC-BLK 名称反复作为新黑箱引用。
- 把 canonical-source 终端闭合直接导入 acyclic noncanonical seed。
- 从早期零行 unsigned 覆盖图反推出 signed pre-Cauchy source。
- 把外部 DI/BFI/FullS-KLS 或 Mertens 定理冒充为 strict 自足证明。
