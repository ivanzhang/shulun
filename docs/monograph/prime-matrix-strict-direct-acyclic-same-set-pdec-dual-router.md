# Prime Matrix strict direct acyclic 同集 PDEC 对偶路由器

**状态：** `direct_acyclic_same_set_pdec_scope_audited_scope_match_or_external_dibfi_open`

`DirectAcyclicSameSetPDECCapDualCertificate` 已完成作用域匹配审查。已有 same-set PDEC 协议和 canonical-source 同集前沿可导入为工具，但 strict acyclic 分支不能自动调用；必须先证明 acyclic 终端证书与 canonical same-set 证书在 formal unit、坏窗集合、U_CRT、L_PDEC 和质量推前上完全同口径。若不能证明该作用域匹配，剩余只能走 acyclic windowed DLS/CleanKLS 或外部 DIBFI 无投影窗口证书。因此 direct PDEC 本轮未闭合，下一最窄点回到 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。

```text
scope_audit_closed=true
same_set_pdec_protocol_imported=true
canonical_source_same_set_pdec_closed_but_scoped=true
acyclic_same_set_scope_match_proved=false
direct_acyclic_same_set_pdec_cap_dual_certificate_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在早期零行反例链的 strict acyclic 终端门内做作用域匹配。 | 保持 row_column_unconditional_closed=false。 |
| `DirectAcyclicSameSetPDECActive` | `true` | `false` | 上一层把 E_named 持久部分的首攻点压成 direct acyclic same-set PDEC 对偶。 | DirectAcyclicSameSetPDECCapDualCertificate |
| `SameSetPDECProtocolImported` | `true` | `true` | 同集 PDEC 比较必须作用在同一坏窗推前计数；失败要输出 DualCap 或缺失行。 | U_CRT<L_PDEC protocol. |
| `CurrentMaterializedPDECFrontierRouted` | `true` | `true` | 当前已物化的 canonical/source PDEC 中间门均已路由，不再是无名 Fourier 常数搜索。 | strict acyclic scope still required. |
| `CanonicalSourceSameSetClosedButScoped` | `true` | `true` | canonical-source 口径下的同集 PDEC-CAP 可用，但不能自动导入 acyclic noncanonical 分支。 | AcyclicCanonicalExactSameSetPromotionCertificate |
| `AcyclicSameSetScopeMatchProved` | `false` | `false` | 若要调用 canonical same-set 对偶，必须证明 acyclic 终端证书同 formal unit、同坏窗集合、同 U_CRT/L_PDEC 推前。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `GenericExternalDIBFIRemainsExternal` | `false` | `false` | 不经 canonical scope 的 generic/external 同集路线仍缺 DI/BFI 无投影窗口量化证书。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| `DirectCleanFallbackNotClosed` | `false` | `false` | 若 direct PDEC 作用域不匹配，fallback 是 acyclic clean KLS/DLS；当前也尚未自足证明。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `DirectAcyclicSameSetPDECCapDualCertificateProved` | `false` | `false` | direct acyclic PDEC 不是已闭合定理；它已压成同集作用域匹配或外部 DI/BFI 证书。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 尚未得到反例链与真实结构链的无条件终端矛盾。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicWindowedKloostermanDLSInternalEstimate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY OR DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 下一真正最窄点

首攻：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
```

并行保留：

```text
AcyclicWindowedKloostermanDLSInternalEstimate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY OR DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只完成 direct PDEC 的作用域匹配审查；它没有证明 strict acyclic same-set PDEC 对偶，也没有升级行/列命题为无条件定理。
