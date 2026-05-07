# Prime Matrix PDEC-CAP Diffuse 终端分裂路由器

**状态：** `pdec_cap_diffuse_terminal_split_reduced_to_occupancy_saturation_or_sc9`

不持久 Gamma 分支已经不再是 `FiberDeletion/NoDeletion/CleanKLS` 的宽口径黑箱。现有账本合成后，非终端门全部接线：持续删除进入删除势账本，删除停止时 KL/MI 偏斜回流 PDEC，只有 KL/MI 平坦才进入 CleanKLS；而 CleanKLS 的 K1--K9 失败项也全部回流命名出口。删除势发散后的支撑耗尽桥也已闭合；全局删除势发散下界又被 HRO 压到占用饱和排斥。剩余自足硬点压成两项：`OccupancySaturationPDECOrColumnCRT`，或 flat clean 分支的 SC-9 谱大筛原子。

## 1. 分裂律

For the nonpersistent Gamma branch, the inverse finite-signature tower gives diffuse payment. Along any same-source lift tower, either the deletion potential sum diverges and the support density is exhausted, or deletion is summable and the branch is NoDeletion. In NoDeletion, persistent KL or phase-residue mutual information returns to refined/new-layer PDEC; only the flat KL/MI case is admitted to CleanKLS/DLS. K1--K9 then route all non-clean failures back to PDEC/SAE/Multiplicity/Promotion. The support-exhaustion bridge closes the implication from divergent deletion to exhaustion or named sparse/PDEC return. The deletion-divergence router then reduces the lower bound to OccupancySaturation, because TailIndependence is already NoDeletion-KL/CleanKLS. Thus the self-contained diffuse terminal is reduced to OccupancySaturation/PDEC/ColumnCRT or the named Kuznetsov-LS atom SC-9; an external DI/BFI/Kuznetsov input would close the flat clean branch only as an external-theorem version.

```text
Nonpersistent Gamma
  => diffuse finite-signature tower;
same-source lift tower
  => sum deletion potential diverges
       => support exhaustion or named sparse/PDEC return;
  or NoDeletion;
NoDeletion + persistent KL/MI
  => refined/new-layer PDEC;
NoDeletion + flat KL/MI
  => CleanKLS/DLS;
CleanKLS K1--K9 failure
  => PDEC / SAE / Multiplicity / Promotion;
all K1--K9 pass
  => external KLS if cited, or self-contained SC-9.
deletion-side remaining hardpoint
  => OccupancySaturationPDECOrColumnCRT.
```

## 2. 汇总

- `diffuse_terminal_split_closed=true`。
- `external_deep_theorem_version_closed_if_accepted=true`。
- `self_contained_diffuse_terminal_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_diffuse_hardpoint=OccupancySaturationPDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9`。
- `open_final_gates=['OccupancySaturationPDECOrColumnCRT', 'SelfContainedKuznetsovLSAtomSC9']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `APSDiffuseBranchIsTheActiveNonpersistentGate` | `true` | `false` | ['SameSetPDECDualComparisonForPersistentMFU', 'DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL'] | APS 投影塔二分已把不持久 Gamma 分支精确送到 diffuse 终端，而不是无名第四出口。 |
| `InfiniteTowerDeletionEntropyDichotomyRegistered` | `true` | `false` | finite_budget_for_infinite_tower_dichotomy | 无限升层只有删除势发散或 NoDeletion 熵/KL 分支两类极限。 |
| `CurrentLayersAreFiberDeletion` | `true` | `false` | {'FiberDeletion': 6} | 当前已物化层仍全部由 FiberDeletion 支付，且每个删除行有正删除势。 |
| `NoDeletionKLHasNoThirdExit` | `true` | `false` | {'PhaseResidueMutualPDECWitness': 6} | 若未来删除停止，KL/互信息偏斜回流 refined/new-layer PDEC；只有平坦分支可进入 CleanKLS/DLS。 |
| `CleanKLSAdmissionK1K9Registered` | `true` | `false` | KuznetsovLSAtomSC9OrExternalCitation | CleanKLS/DLS 不再是黑箱：K1--K9 任一失败都回流 PDEC/SAE/Multiplicity/Promotion。 |
| `ExternalKLSVersionRegistered` | `true` | `false` | closed_for_a1_clean_branch_if_windowed_kloosterman_spectral_dispersion_input_is_accepted | 若明确接受窗口化 DI/BFI/Kuznetsov 大筛输入，flat clean 分支可作为外部深定理版吸收。 |
| `SelfContainedCleanFrontierNamedSC9` | `true` | `false` | a1_sc9_frontier_routed_to_ncblk_or_external_dibfi | 完全自足版的 clean 剩余不是泛化 KLS 缺口，而是命名的 Kuznetsov-LS atom SC-9 / NC-BLK 前沿。 |
| `DeletionSupportExhaustionBridgeRouted` | `true` | `false` | GlobalDeletionPotentialDivergenceLowerBound | 删除势发散后的支撑耗尽/稀疏回流逻辑已闭合，删除侧只剩全局发散下界。 |
| `DeletionDivergenceLowerBoundReduced` | `true` | `false` | OccupancySaturationPDECOrColumnCRT | 全局删除势发散下界已由 HRO 压到占用饱和排斥；TailIndependence 已回流 NoDeletion/CleanKLS。 |
| `OccupancySaturationPDECOrColumnCRT` | `false` | `true` | near-full old-hole residues not globally excluded | 还需证明旧洞 residue 在 promoted prime 层近满占用会触发低层容量矛盾、PDEC 或 ColumnCRT。 |
| `SelfContainedKuznetsovLSAtomSC9` | `false` | `true` | external input registered; self-contained atom open | 若删除势可求和且 KL/MI 平坦，则完全自足版仍需证明 SC-9 谱大筛原子；否则只能声明外部输入版。 |

## 4. 边界

本路由器关闭的是 diffuse 分支中的无名逃逸和 NoDeletion-KL 第三出口。它不证明完整行/列无条件定理，也不证明 PDEC-CAP 同集全局对偶证书。完全自足版仍需提交 `OccupancySaturationPDECOrColumnCRT` 或 `SelfContainedKuznetsovLSAtomSC9` 的最终证明；外部深定理版必须明确登记所引用的 KLS/DI/BFI/Kuznetsov 输入。
