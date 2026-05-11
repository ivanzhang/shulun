# Prime Matrix strict acyclic canonical-lock 原子化路由器

**状态：** `acyclic_canonical_lock_reduced_to_source_embedding_and_same_set_pushforward_open`

本步把 acyclic terminal canonical-lock 从宽泛作用域问题压成三个必要子原子：acyclic seed 必须是 canonical A1/KZ-E pre-Cauchy 源的有限测度因子；终端证书必须保持同集推前恒等式；canonical 投影后不能残留未登记 noncanonical payload。哈希稳定和 canonical-source 来源闭合都是可用材料，但它们本身不足以证明当前 acyclic noncanonical 分支已经 canonical-lock。

```text
acyclic_canonical_lock_boundary_refined=true
hash_stability_imported=true
canonical_source_provenance_imported_with_scope=true
known_transverse_embedding_not_universal=true
acyclic_seed_canonical_source_embedding_proved=false
terminal_certificate_same_set_pushforward_proved=false
no_noncanonical_payload_survives_projection_proved=false
acyclic_terminal_canonical_lock_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=((AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn)
```

## 1. lock 拆分

拆分前：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
```

拆分后：

```text
((AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AcyclicCanonicalLockGateActive` | `true` | `false` | 上一层第一优先点是把 acyclic terminal family 锁入 canonical-source 边界。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `HashStabilityNotEnough` | `true` | `true` | canonical formal unit hash stability 只保证记录不改名；它不证明 noncanonical payload 是 canonical 源的因子。 | 仍需源头因子嵌入。 |
| `CanonicalSourceProvenanceImportedWithScope` | `true` | `true` | canonical-source 的来源账本已经闭合，条件是 pre-Cauchy lambda 按定义等于 RIW/Buchstab 决策树系数。 | acyclic noncanonical seed 必须证明满足这个条件或被投影成其有限因子。 |
| `KnownTransverseEmbeddingNotUniversal` | `true` | `true` | PDEC-CAP 横向 formal unit 嵌入 canonical 源的函子性已在特定横向商对象上闭合。 | 不能自动覆盖当前 acyclic clean-core/moving-block terminal family。 |
| `SourceSeedEmbeddingAtomPinned` | `true` | `false` | 必须证明 acyclic seed 是 canonical A1/KZ-E pre-Cauchy 源的限制、商、条件化或确定性推前。 | AcyclicSeedCanonicalSourceFiniteFactorEmbedding。 |
| `SameSetPushforwardAtomPinned` | `true` | `false` | 即便源可嵌入，还必须证明终端证书下的 U_CRT、L_PDEC、坏窗集合和权重质量推前后完全同口径。 | TerminalCertificateSameSetPushforwardIdentity。 |
| `NoNoncanonicalPayloadAtomPinned` | `true` | `false` | canonical 投影后不得残留未登记的 moving same-(u,v) 原子、Type/Fourier 容量乘子或 non-AP payload。 | NoNoncanonicalPayloadSurvivesCanonicalProjection。 |
| `CanonicalLockReducedToThreeSubatoms` | `true` | `false` | canonical-lock 被压成源因子嵌入、同集推前恒等式、无 noncanonical 残留三项。 | AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection |
| `CanonicalLockCurrentCorpusProved` | `true` | `false` | 当前材料尚未证明这三项，因此不能把 canonical 终端闭合导入 acyclic noncanonical 分支。 | AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |

## 3. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

主攻名：`AcyclicSeedCanonicalSourceFiniteFactorEmbedding`。

必须证明：
- 从假设早期零行反例生成的 acyclic pre-Cauchy seed 是 canonical A1/KZ-E 源的有限测度因子。
- 源因子嵌入保持同一 formal unit 与 branch key。
- 终端证书的坏窗集合、U_CRT、L_PDEC 和权重质量在推前前后一致。
- 任何未能嵌入的 noncanonical payload 必须回流 direct PDEC dual 或 direct CleanKLS/DLS。

不能作为证明使用：
- 只给 formal_unit_id 哈希稳定。
- 只引用 canonical-source 终端闭合。
- 只证明某个横向 PDEC-CAP 子对象可嵌入。
- 把 generic WFD 或 noncanonical full-S 补集当成 canonical RIW/Buchstab 源。
