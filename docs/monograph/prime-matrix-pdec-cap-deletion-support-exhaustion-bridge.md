# Prime Matrix PDEC-CAP 删除势-支撑耗尽桥

**状态：** `deletion_support_exhaustion_bridge_closed_divergence_lower_bound_open`

删除势发散到支撑耗尽的逻辑链条已闭合：乘法公式给出支撑密度趋零，actual-payment 账本给出正需求责任，二者不能继续作为 diffuse 正责任终端共存。若剩余质量集中或稀疏化，则回流已命名 LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS 入口。因此原来的 `GlobalDeletionDivergenceOrSupportExhaustion` 可继续压窄为 `GlobalDeletionPotentialDivergenceLowerBound`。

## 1. 桥接律

On a same-source lift tower, density(A_QN)=density(A_Q0)*prod a_n. If sum -log a_n diverges, the active support density tends to zero. A branch with positive actual-payment demand cannot keep being a diffuse positive-responsibility terminal on zero-density support: either the responsibility is exhausted, or the remaining mass becomes singular/sparse or has a persistent finite signature, which is already routed to LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS contracts. Therefore the support exhaustion implication is closed; the only deletion-side self-contained mathematical obligation left is to prove the global divergence lower bound.

```text
same-source lift tower:
  density(A_QN)=density(A_Q0)*prod a_n;
sum -log a_n = infinity
  => density(A_QN)->0;
positive actual-payment demand on zero-density support
  => exhausted support or singular/sparse concentration;
singular/sparse concentration
  => named LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS return;
therefore remaining deletion hardpoint
  => prove GlobalDeletionPotentialDivergenceLowerBound.
```

## 2. 汇总

- `deletion_support_exhaustion_bridge_closed=true`。
- `global_deletion_divergence_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_deletion_hardpoint=GlobalDeletionPotentialDivergenceLowerBound`。
- `open_final_gates=['GlobalDeletionPotentialDivergenceLowerBound']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `APSDiffuseGateActive` | `true` | `false` | ['SameSetPDECDualComparisonForPersistentMFU', 'DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL'] | APS 投影塔已把不持久 Gamma 分支送入 diffuse 删除/NoDeletion/CleanKLS 终端。 |
| `DensityProductFormulaRegistered` | `true` | `false` | finite_budget_for_infinite_tower_dichotomy | 同源投影塔上有精确乘法公式 density(A_QN)=density(A_Q0)*prod a_n。 |
| `DivergentDeletionImpliesZeroSupport` | `true` | `false` | sum -log a_n = infinity => density(A_QN)->0 | 删除势发散时，同源活跃支撑密度趋零；这是乘法公式的直接结论。 |
| `ActualPaymentResponsibilityConstructed` | `true` | `false` | {'ActualPaymentMeasureDichotomySubmitted': 8, 'NoTailDemandSparseOrLocalSurvivor': 1} | actual payment measure 已按需求精确构造；有正需求的 cap 不能继续停留为无名责任。 |
| `ZeroSupportCannotRemainDiffusePositiveResponsibility` | `true` | `false` | zero density support versus normalized actual-payment demand | 若支撑密度趋零而仍有责任质量，则它不再是 diffuse 正密度终端，只能耗尽或集中成稀疏/PDEC 签名。 |
| `SparseOrSingularReturnIsNamed` | `true` | `false` | no_additional_unnamed_local_survivor_entry_route_not_global_proof | 支撑耗尽后的稀疏/孤窗回流已有 SAE/LocalSurvivor/PDEC/ColumnCRT/CleanKLS 准入口，不产生新出口。 |
| `CurrentMaterializedSparseBoundaryRegistered` | `true` | `false` | materialized_frontier_exhausted_terminal_family_exclusion_open | 当前已物化 LocalSurvivor/SAE 包与已知 sparse 入口已经耗尽；未来 sparse 只能带 schema 进入命名合同。 |
| `DeletionSupportExhaustionBridgeClosed` | `true` | `false` | deletion divergence => exhausted or named sparse/PDEC return | 支撑耗尽桥接闭合：发散删除势不再是独立终端，只剩证明删除势确实全局发散。 |
| `GlobalDeletionPotentialDivergenceLowerBound` | `false` | `true` | not proved for every diffuse counterexample tower | 仍需证明任意不持久 Gamma 反例塔若持续 FiberDeletion，则 sum -log a_n 必发散。 |

## 4. 剩余

本文件没有证明任意 diffuse 反例塔都满足 `sum -log a_n=infinity`。它只关闭后半段逻辑：一旦发散成立，支撑耗尽不再是独立未命名出口。下一步应直接攻 `GlobalDeletionPotentialDivergenceLowerBound`，即从 promoted-prime 必要性、TailIndependentCompletion 和 HoleResidueOccupancy 中推出删除势不可求和。
