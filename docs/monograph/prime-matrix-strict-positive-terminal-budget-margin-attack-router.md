# Prime Matrix strict 正终端预算余量主攻路由器

**状态：** `positive_terminal_budget_attack_b3_external_front_closed_structural_margin_open`

本轮把 B3 外部条件前沿接入正终端预算余量：接受外部 Mertens/Dusart 或标准 beta-sieve 时，B3 离散误差和长度 P 总变差不再是最窄主阻塞；严格自足线仍缺 Mertens 尾段内联证明。真正终端口收缩为同参数耦合余量 D0(P,z)-E0(P,z)-U0(P,z)>0，并且必须同时处理有限 prefix 证书、命名回流/热核心/固定历史出口和 DStructure/Rankin 独立晋级验收。当前仍未推出直接矛盾。

```text
counterexample_assumption_only=true
b3_external_front_no_longer_primary_blocker=true
b3_strict_self_contained_tail_closed=false
strict_prefix_demand_proved=false
finite_boundary_prefix_open=true
named_return_exclusion_proved=false
hot_fixed_terminal_exits_closed=false
rankin_subledger_closed=true
dstructure_rankin_independently_accepted=false
explicit_positive_terminal_budget_margin_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. B3 前沿

| front | closed | proved | effect | remaining |
| --- | --- | --- | --- | --- |
| `continuous beta demand` | `true` | `true` | 连续主项余量可用，不再是正余量主阻塞。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| `B3 discrete/Stieltjes external lane` | `true` | `false` | 接受外部 Mertens/Dusart 或标准 beta-sieve 时，离散误差和边界余项可进入条件闭合。 | DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted |
| `B3 signed delay anchor` | `true` | `true` | 锚点提升到 20000 后，delay-kernel BV 乘子预算小于 1% f(s)。 | closed under external Mertens tail |
| `strict self-contained B3 tail` | `false` | `false` | 若坚持完全自足，不接受 Dusart/Rosser-Schoenfeld 外部定理，这一尾段仍未内联。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |

## 2. 终端余量槽位

正余量只能在同一参数账本下闭合：

```text
D0(P,z) - E0(P,z) - U0(P,z) > 0.
```

| slot | closed | effect_on_margin | remaining |
| --- | --- | --- | --- |
| `prefix lower bound` | `false` | 决定 D_prefix 是否能给出统一显式 D0(P,z)。 | FiniteBoundaryPrefixRoughCountCertificate |
| `named return deduction` | `false` | 决定 E_named 是否可以被排斥或严格计入同参数预算。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion via PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve or unified budget |
| `hot/fixed terminal exits` | `false` | 决定热核心与固定历史是否会吞掉余量。 | TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion |
| `coupled positive margin` | `false` | 需要在同一参数账本下证明 D0(P,z)-E0(P,z)-U0(P,z)>0。 | FinitePrefixNamedReturnCoupledPositiveMarginLedger |
| `independent promotion gate` | `false` | 即使终端余量闭合，行/列定理仍需 DStructure/Rankin 独立验收晋级。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本轮仍只在 Assume EarlyZeroRowWithinP 的反例链内压缩终端余量，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false。 |
| `B3ExternalFrontNoLongerPrimaryBlocker` | `true` | `false` | 若接受外部 Mertens/Dusart 或标准 beta-sieve，B3 离散误差/TV 前沿可条件接入终端余量。 | 严格自足仍需 SelfContainedDusartReciprocalPrimeProofAppendixXGe10372。 |
| `FinitePrefixCertificateStillOpen` | `false` | `false` | 正余量不能只靠渐近主项；有限 P 边界必须有机器证书或严格手算证书。 | FiniteBoundaryPrefixRoughCountCertificate |
| `NamedReturnStillOpen` | `false` | `false` | 命名回流字母表已压缩，但持久 PDEC/CleanKLS 与非持久统一预算尚未同时排斥。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `CoupledPositiveMarginStillOpen` | `false` | `false` | 终端矛盾的必要充分口仍是同参数 D_prefix-E_named-U_cold>0。 | FinitePrefixNamedReturnCoupledPositiveMarginLedger |
| `DStructureRankinPromotionStillOpen` | `false` | `false` | Rankin 子账本已格式化并 pass-or-return，但独立晋级验收仍未接受。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `DirectTerminalContradictionReached` | `false` | `false` | 当前还没有从反例链推出与真实结构链的终端直接矛盾。 | FinitePrefixNamedReturnCoupledPositiveMarginLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新最窄点

外部 B3 路线下：

```text
FinitePrefixNamedReturnCoupledPositiveMarginLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格自足路线下：

```text
SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND FinitePrefixNamedReturnCoupledPositiveMarginLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一步不应回到真实零行直接证明，也不应重跑 psi runner；应直接攻 `FinitePrefixNamedReturnCoupledPositiveMarginLedger`，也就是把有限 prefix 证书、命名回流扣除和冷供给上界放进同一个参数表，证明严格正余量或暴露具体失败回流。

审稿边界：本文件只更新终端余量的最窄硬点，不声明行/列命题无条件闭合。
