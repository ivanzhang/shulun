# Prime Matrix strict acyclic 终端家族主攻路由器

**状态：** `strict_acyclic_terminal_family_reduced_to_canonical_lock_or_direct_dual_open`

本步继续主攻 strict acyclic 终端家族。已有 canonical-source PDEC/CleanKLS 闭合不能直接偷渡；要么证明 acyclic terminal certificates canonical-lock 到 canonical-source 边界，要么直接证明 acyclic 同集 PDEC 对偶，要么直接证明 acyclic clean residual 的内部 KLS/DLS 大筛吸收并把失败命名回流。这把宽口径终端门压成三个可审稿原子，但当前仍未完成其中任何一个。

```text
strict_acyclic_terminal_family_boundary_refined=true
canonical_promotion_scope_guard_preserved=true
acyclic_terminal_canonical_lock_proved=false
direct_acyclic_same_set_pdec_dual_proved=false
direct_acyclic_clean_kls_dls_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

## 1. 三选一主攻口

原终端门：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

压缩后：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictAcyclicTerminalFamilyGateActive` | `true` | `false` | 上一层 strict 基的全局终端门是 acyclic noncanonical 口径下的 PDEC-CAP 或内部 CleanKLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `GlobalSplitImportedButNotProof` | `true` | `true` | GlobalPDECorSparseTerminalExclusion 已被拆成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。 | 拆分不是排斥证明，仍需同作用域终端估计。 |
| `CanonicalPromotionAvailableOnlyUnderCanonicalSource` | `true` | `true` | canonical-source 分支内 PDEC-CAP/CleanKLS 已可接到 NoFurtherCanonicalSourceTerminalPromotionGap。 | 不能直接导入 acyclic noncanonical 分支。 |
| `CanonicalImportRequiresLock` | `true` | `false` | 若要复用 canonical 闭合，必须证明每个 acyclic terminal certificate 保持同集质量、formal unit 和层转移地嵌入 canonical-source 边界。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary。 |
| `DirectPDECCapAlternativePinned` | `true` | `false` | 不走 canonical-lock 时，可直接对 acyclic terminal family 证明同一坏窗集合上的 U_CRT<L_PDEC 对偶证书。 | DirectAcyclicSameSetPDECCapDualCertificate。 |
| `DirectCleanKLSAlternativePinned` | `true` | `false` | 若 terminal family 为 diffuse clean residual，则必须证明 K1--K9 准入后内部 KLS/DLS 大筛吸收，失败要命名回流 PDEC/SAE/ColumnCRT。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn。 |
| `ExternalDIBFINotStrictSelfContained` | `true` | `false` | generic DI/BFI/Kuznetsov 可作为外部条件线，但不能关闭 strict 自足终端门。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY。 |
| `AcyclicTerminalFamilyReducedToThreeAtoms` | `true` | `false` | 宽终端门被压成 canonical-lock、直接 PDEC 对偶、直接 CleanKLS 三个互斥主攻方向。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `StrictAcyclicTerminalFamilyCurrentCorpusProved` | `true` | `false` | 当前仓库尚未证明三者之一，故 strict acyclic terminal family 仍未闭合。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 即便接受外部 Mertens 解析线，完整 strict 链还需 acyclic seed、终端三选一和 DStructure/Rankin 替代门。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`AcyclicTerminalCanonicalLock_THEN_DirectDualIfLockFails`。

- 第一优先：`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。
- 失败回退：`DirectAcyclicSameSetPDECCapDualCertificate`。
- 并行备线：`DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。

必须保持：
- 同一 formal unit。
- 同一坏窗集合。
- 同一推前质量 U_CRT 与 L_PDEC。
- 不从真实零行缺席取证。
- 不把 canonical-source 闭合直接导入 noncanonical 分支。
