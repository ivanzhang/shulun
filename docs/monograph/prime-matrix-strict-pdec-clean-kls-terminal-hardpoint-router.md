# Prime Matrix strict PDEC/CleanKLS 终端硬点路由器

**状态：** `pdec_clean_kls_terminal_split_closed_both_arms_open`

`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 的终端门已被精确二分：PDEC 手臂需要证明 strict acyclic 证书与 canonical same-set PDEC 证书的同口径作用域匹配；CleanKLS 手臂已经压到 `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。两条手臂当前都未闭合，外部 DI/BFI/Kuznetsov 只能给条件线。因此下一最窄自足主攻点是自足 Kuznetsov/DLS 大筛原子，同时并行保留 PDEC 作用域匹配、模型余量账本和 DStructure/Rankin 验收门。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
terminal_split_router_closed=true
direct_pdec_protocol_audited=true
acyclic_same_set_scope_match_proved=false
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 终端二分

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
  -> PDEC arm:
     AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
  -> CleanKLS arm:
     SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
  -> external conditional arm:
     DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalGateActiveFromDownstreamSync` | `true` | `true` | alpha signed 权重律下游同步后，当前首要终端门正是 PDEC-CAP 或内部 CleanKLS/DLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `GlobalTerminalFamilySplitImported` | `true` | `true` | 全局终端家族已把 LocalSurvivor/NC-BLK 等宽泛出口拆成 PDEC-CAP 或 CleanKLS/DLS。 | DirectAcyclicSameSetPDECCapDualCertificate OR AcyclicWindowedKloostermanDLSInternalEstimate |
| `DirectPDECProtocolAuditedButScopeOpen` | `true` | `false` | 同集 PDEC 协议可导入，但 strict acyclic 证书与 canonical same-set 证书的作用域匹配仍未证。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `DirectPDECScopeMatchNotProved` | `false` | `false` | 要用 PDEC 手臂，必须同 formal unit、同坏窗集合、同 U_CRT/L_PDEC、同质量推前。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `CleanKLSReducedToWindowedDLS` | `true` | `false` | clean KLS/DLS 手臂已剥离低维缺陷，严格自足剩余是 acyclic windowed DLS。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `WindowedDLSNormalFormClosed` | `true` | `true` | 窗口双线性型、相位/可逆变量、L2 系数范数和失败回流字母表已固定。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `SelfContainedKuznetsovDLSAtomNotProved` | `false` | `false` | 真正解析原子是自足 Kuznetsov/DLS 大筛不等式；当前语料没有证明。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `ExternalDIBFINotStrictSelfContained` | `false` | `false` | 外部 DI/BFI/Kuznetsov 可成为条件线，但不能替代 strict 自足闭合。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| `ModelGapLedgerStillParallel` | `true` | `false` | 即使终端门某一手臂证明，ExplicitModelGapAndFiniteDPRCLedger 仍需同口径支付。 | ExplicitModelGapAndFiniteDPRCLedger |
| `PDECCapOrCleanKLSLargeSieveProved` | `false` | `false` | PDEC 手臂和 CleanKLS/DLS 手臂当前均未给出可闭合证明。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 尚未产生足以排除早期零行反例链的终端矛盾。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 二分后开放基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks) AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一主攻点

```text
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
```
