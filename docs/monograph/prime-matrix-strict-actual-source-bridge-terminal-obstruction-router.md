# Prime Matrix strict actual-source 桥终端障碍路由器

**状态：** `strict_actual_source_bridge_reduced_to_source_admission_or_moving_atom_open`

本步直接攻击 `ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput`。源锁定线的具体原子是 `A1CleanBranchCanonicalSourceAdmission`：必须在 Cauchy/dispersion 前证明 clean A1 反例分支已经选择 canonical RIW/Buchstab 决策树源，不能从后验覆盖图或 canonical restricted 分支闭合反推。强化反原子线的具体原子是 `ActualNoncanonicalCleanCoreMovingAtomExclusion`：必须排斥通过全部回流测试后的 actual noncanonical clean-core 容量大原子，不能由 formal WFD、Type/Fourier、K4/K6 或支撑能量形式引理免费推出。因此最新 strict 自足终端剩余为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion`。这些原子均未证明，行/列命题仍未无条件闭合。

```text
actual_source_bridge_boundary_sharp=true
source_lock_free_upgrade_blocked=true
zero_row_geometry_source_lock_blocked=true
antiatom_free_upgrade_blocked=true
support_energy_formal_only=true
source_lock_concrete_atom_proved=false
actual_noncanonical_clean_core_moving_atom_exclusion_proved=false
actual_source_bridge_theorem_closed=false
row_column_unconditional_closed=false
strict_self_contained_terminal_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion
```

## 1. 终端障碍链

```text
ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput
  -> A1CleanBranchCanonicalSourceAdmission
  OR ActualNoncanonicalCleanCoreMovingAtomExclusion

plus parallel:
  AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ActualSourceBridgeActive` | `true` | `false` | 上一层 strict noncanonical 叶子已过滤到实际源锁定或实际源强化反原子。 | ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput |
| `SourceLockConcreteAtomImported` | `true` | `false` | source-lock 合同显示 canonical 源头链只在 clean A1 分支被证明准入 canonical RIW/Buchstab 时可用。 | A1CleanBranchCanonicalSourceAdmission |
| `SourceLockFreeUpgradeBlocked` | `true` | `true` | 不能从 canonical restricted 分支闭合、KZ-E 泛 well-factorable 记录或后验 payment 图免费推出 source lock。 | 必须给 pre-Cauchy 分支准入证明。 |
| `ZeroRowGeometryCannotGenerateSourceLock` | `true` | `true` | 早期零行假设、斜线覆盖、圆柱环绕和层叠筛只给 unsigned 覆盖/预算形状，不能反推 signed pre-Cauchy source。 | A1CleanBranchCanonicalSourceAdmission |
| `StrengthenedAntiAtomConcreteAtomImported` | `true` | `false` | source anti-atom 合同已精确为最终 full-S non-AP 容量测度无 moving same-(u,v) 大原子。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `AntiAtomFreeUpgradeBlocked` | `true` | `true` | formal WFD、Type/Fourier、K4/K6、朴素 incidence 和 canonical 支撑导入均不能推出该反原子。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `SupportEnergyLemmaOnlyFormal` | `true` | `true` | 支撑能量/Cauchy 引理只说明最大 pair 原子界可推出支撑下界，不证明 actual source 的最大原子界。 | ExactUVPairMassDispersionOrMaxAtomBoundLedger / clean-core moving atom exclusion。 |
| `MovingAtomSharpInputPinned` | `true` | `false` | 过强的低支撑 packet 排斥已校准为 sharp moving-atom 排斥；该排斥尚未证明。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `CanonicalLockStillParallel` | `true` | `false` | acyclic terminal canonical-lock 仍可作为替代路线，但其同集推前与无 payload 残留仍开放。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `ActualSourceBridgeCurrentCorpusProved` | `true` | `false` | 实际源桥已压到两个具体原子，但没有一个已由当前材料证明。 | A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 仍缺 terminal 三选一、高段自足尾项或外部接受、DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基更新为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`A1CleanBranchCanonicalSourceAdmission_OR_ActualNoncanonicalCleanCoreMovingAtomExclusion`。

必须证明：
- 源锁定线：在 Cauchy/dispersion 前证明 clean A1 反例分支选择 canonical RIW/Buchstab 决策树权重。
- 反原子线：证明通过全部回流测试后的 actual noncanonical clean-core 容量测度没有 moving same-(u,v) 大原子。
- 若任一失败态出现，必须回到 PDEC/SAE/ColumnCRT/CleanKLS 或外部 FullS-KLS 条件线，不能生成第四终端。
- 同步保留 DStructure/Rankin 与高段 Mertens/PNT 自足尾项为独立门。

不能作为证明使用：
- 从真实零行缺席、数值样本或覆盖图直接反推 source。
- 从 canonical 分支闭合静默推出 noncanonical 分支 source lock。
- 把 Cauchy 支撑能量形式引理当成 actual 最大原子界。
- 把低支撑 packet 排斥口径替代 sharp moving-atom 排斥而不证明逆否账本。
- 把外部 FullS-KLS 条件线写成 strict 自足闭合。
