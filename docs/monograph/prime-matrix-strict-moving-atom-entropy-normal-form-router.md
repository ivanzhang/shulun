# Prime Matrix strict moving-atom exact entropy 标准形路由器

**状态：** `strict_moving_atom_reduced_to_exact_entropy_open`

`ActualNoncanonicalCleanCoreMovingAtomExclusion` 已经可以替换成更精确的内部标准形 `ExactCleanCoreFullSNonAPWFDSourceEntropy`：无 moving same-(u,v) 大原子等价于 `max_b M_b/M <= log^{-2A}`。外部替代标准形是 `ModulusDependentCompletedFullSKLSInput`，但 strict 自足线不能使用它。因此当前 strict 活动终端从 `canonical-lock OR moving-atom` 更新为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy`。exact entropy 和 canonical-lock 均未证明，行/列命题仍未无条件闭合。

```text
moving_atom_entropy_normal_form_closed=true
strict_self_contained_external_completed_kls_filtered=true
generic_antiatom_no_go_retained=true
fixed_projection_diffuse_insufficient=true
exact_clean_core_source_entropy_proved=false
external_completed_kls_accepted=false
acyclic_terminal_canonical_lock_proved=false
row_column_unconditional_closed=false
strict_self_contained_terminal_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy
```

## 1. 标准形链

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
  <=> ExactCleanCoreFullSNonAPWFDSourceEntropy
      max_b M_b/M <= log^{-2A}

external alternative:
  ModulusDependentCompletedFullSKLSInput

strict self-contained active terminal:
  AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
  OR ExactCleanCoreFullSNonAPWFDSourceEntropy
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MovingAtomStrictLeafActive` | `true` | `false` | 上一层已删除 A1 分支陈述伪终端，活动 strict 叶子为 canonical-lock 或 clean-core moving atom 排斥。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `MovingAtomSharpInputPinned` | `true` | `false` | moving atom 是通过所有回流测试后仍承载最终 M_{u,v} 大原子的 actual clean-core block。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `MovingAtomEqualsExactEntropy` | `true` | `false` | 无 moving 大原子等价于 max_b M_b/M <= log^{-2A} 的 exact clean-core source entropy。 | ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `CompletedKLSExternalNormalFormImported` | `true` | `false` | 外部替代标准形是 completed、modulus-dependent 的 full-S KLS 输入，不是泛称 DI/BFI。 | ModulusDependentCompletedFullSKLSInput |
| `StrictSelfContainedExternalFiltered` | `true` | `true` | 严格自足线过滤 completed KLS 外部黑箱；它只能保留在条件定理线。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `GenericAntiAtomNoGoRetained` | `true` | `true` | moving-delta 反模型说明 formal/generic WFD 版反原子为假；exact entropy 必须是 actual-source 定理。 | ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `FixedProjectionDiffuseInsufficient` | `true` | `true` | 固定投影 diffuse 不能推出 moving-block 非集中；hidden same-(u,v) fiber 可随尺度移动。 | ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `ExactEntropyCurrentCorpusProved` | `true` | `false` | 当前材料尚未证明 actual clean-core exact source entropy。 | ExactCleanCoreFullSNonAPWFDSourceEntropy |
| `CanonicalLockStillParallel` | `true` | `false` | canonical-lock 仍是并行替代路线，但同集推前和无 payload 残留仍未证。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 仍缺 canonical-lock 或 exact entropy、高段自足尾项或外部接受、DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基更新为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

条件外部线可写为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy OR ModulusDependentCompletedFullSKLSInput) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`ExactCleanCoreFullSNonAPWFDSourceEntropy_OR_AcyclicTerminalCanonicalLock`。

必须证明：
- 证明 actual clean-core full-S non-AP WFD 源满足 max_b M_b/M <= log^{-2A}。
- 或证明 canonical-lock 的同集推前与无 noncanonical payload 残留。
- 若走外部线，必须明确接受或证明 ModulusDependentCompletedFullSKLSInput。
- 保留高段 Mertens/PNT 与 DStructure/Rankin 为独立门。

不能作为证明使用：
- 用 fixed-projection diffuse 代替 moving-block entropy。
- 用 unrestricted generic WFD/Type/Fourier 模板代替 actual source entropy。
- 把 completed KLS 外部条件线写成 strict 自足证明。
- 把 canonical-source 分支支撑下界导入 noncanonical exact entropy。
