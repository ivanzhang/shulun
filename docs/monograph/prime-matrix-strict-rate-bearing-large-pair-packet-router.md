# Prime Matrix strict rate-bearing 大 pair packet 路由器

**状态：** `strict_rate_bearing_large_pair_packet_reduced_to_terminal_three_atom_open`

`RateBearingLargePairAtomPacketExclusion` 被继续压缩，但目标仍是同一个 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。任何超过 `M/L^K` 的同 formal unit 大 pair packet 必落入四类：canonical payload、持久有限签名、孤立 sparse/ColumnCRT、漂移 clean residual。前三者分别进入 canonical-lock、PDEC 或 sparse schema；最后一类进入 direct CleanKLS/DLS。因而当前内部剩余等价压成三原子终端门 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。这些终端估计仍未证明，不能声明无条件闭合。

```text
same_theorem_target_preserved=true
rate_bearing_packet_split_closed=true
rate_bearing_large_pair_atom_packet_exclusion_proved=false
direct_acyclic_same_set_pdec_dual_proved=false
direct_acyclic_clean_kls_dls_proved=false
acyclic_terminal_canonical_lock_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 同命题内部压缩

```text
RateBearingLargePairAtomPacketExclusion
  -> packet split has no fifth exit
  -> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

## 2. packet 分支表

| branch | trigger | route | status |
| --- | --- | --- | --- |
| `CanonicalPayload` | packet 的 pre-Cauchy 来源可证明为 canonical RIW/Buchstab 因子或其有限推前。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary | `open` |
| `PersistentFiniteSignature` | 同一有限 pair/phase/column/signature 以 log-power 阈值持久复现。 | DirectAcyclicSameSetPDECCapDualCertificate | `open` |
| `IsolatedSparseOrColumnPacket` | packet 只在有限局部窗或列位移中出现，可抽取 witness/blocker-deficit。 | SAE/LocalSurvivor/ColumnCRT absorbed into sparse/PDEC terminal schema | `schema_closed_exclusion_open` |
| `DriftingRateBearingCleanResidual` | 所有有限签名都不持久，但每层仍有超过 `M/L^K` 的 clean exact pair。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn | `open` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RateBearingPacketInputActive` | `true` | `false` | 上一层把独立 pair 能量界压成 rate-bearing 大 pair packet 排斥。 | 排斥该 packet，或证明其进入已命名终端。 |
| `SameTheoremTargetPreserved` | `true` | `true` | 本步仍是 NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem 的内部反证分支，不改换总命题。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `SeedFusionImported` | `true` | `true` | seed 存在/不存在两支均已汇入 acyclic terminal family，packet 不能逃到 seed 缺失第四出口。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `TerminalThreeAtomImported` | `true` | `false` | rate-bearing packet 的合法终端只剩 canonical-lock、direct PDEC 或 direct CleanKLS/DLS 三类。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `PDECInputMaterializationImported` | `true` | `true` | 持久有限签名的大 pair packet 已可物化为同集 PDEC 输入；但 PDEC cap 量界未完成。 | AcyclicFiniteArcCapMassBoundsOrNamedReturn / DirectAcyclicSameSetPDECCapDualCertificate |
| `CleanAdmissionImported` | `true` | `true` | 漂移 clean residual 的对象、窗口化双线性型和 L2 系数账本已物化；但内部 DLS/Kuznetsov 大筛估计未完成。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `SparseSchemaAdmissionImported` | `true` | `true` | 孤立 sparse/SAE/ColumnCRT packet 不能作为隐藏终端；未来新增必须提交显式 schema。 | future schema global nonexistence is not claimed |
| `RateBearingLargePairPacketExclusionCurrentCorpusProved` | `false` | `false` | 当前材料尚未排斥三原子终端中的 PDEC cap、CleanKLS/DLS 或 canonical-lock 残余。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `NewActualSourceEntropyCurrentCorpusProved` | `false` | `false` | rate-bearing packet 排斥未完成，所以新 actual-source 熵定理仍未证明。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |

## 4. 硬边界律

rate-bearing 大 pair packet 没有第五出口：canonical 口进入 canonical-lock；持久有限签名进入 direct PDEC；孤立 sparse/ColumnCRT 进入已登记 schema；漂移 clean residual 进入 direct CleanKLS/DLS。当前未证明的是这些终端排斥估计，不是 packet 定义或 seed 定义。

下一步仍在同一源熵定理内部直攻三原子终端门：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

完整 strict 基仍保持：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
