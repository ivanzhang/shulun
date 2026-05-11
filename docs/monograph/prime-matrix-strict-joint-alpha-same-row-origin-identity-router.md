# Prime Matrix strict joint alpha same-row 来源恒等式路由器

**状态：** `joint_alpha_same_row_origin_identity_reduced_to_row_level_origin_table_open`

本步把 joint same-row word/coefficient 来源恒等式回收到统一逐行原始生成表。这张表必须在同一 row 中同时列出 basis_word_id、signed_coefficient、source_tuple_hash、`(u,v)`、branch key、sign/local factor 和推前前恒等式。已有 unsigned skeleton 与 signed origin 路线分别只给两半，不能证明同一行同源；当前逐行表仍未证明。

```text
joint_alpha_same_row_origin_identity_router_closed=true
row_level_clean_core_origin_generation_table_proved=false
acyclic_seed_signed_row_emitter_rule_proved=false
joint_alpha_same_row_word_coefficient_origin_identity_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward` 与 primitive summand 来源恒等式、basis word 来源恒等式会合；共同所需对象是 `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`。

## 2. same-row 表字段

| field | meaning |
| --- | --- |
| `same_row_id` | 同一 actual noncanonical primitive row 的唯一编号。 |
| `basis_word_id` | 由 carry-shell/anchor/phase skeleton 绑定的 primitive basis word。 |
| `signed_coefficient` | 该同一行的 signed coefficient 来源公式。 |
| `source_tuple_hash` | word 与 coefficient 共享同一 formal unit/source tuple。 |
| `uv_branch_sign_local_factor` | 同一行同步输出 exact `(u,v)`、branch key、sign 和 local factor。 |
| `prepushforward_identity` | 同一行在 Phi/payment 推前前参与 alpha/delta 求和恒等式。 |
| `return_tag` | 缺 word、缺 coefficient、零因子、后验读取或跨来源时命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameRowOriginIdentityTargetActive` | `true` | `false` | 上一层已把 joint alpha-side 规则压成 same-row word/coefficient 来源恒等式。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `PrimitiveCoefficientOriginRouteImported` | `true` | `true` | primitive summand signed coefficient 来源恒等式已经压到逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `BasisWordOriginRouteImported` | `true` | `true` | basis word signed coefficient 来源恒等式也压到同一逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `SameRowTableFieldsPinned` | `true` | `true` | 逐行原始生成表字段包含 basis_word、source tuple、signed coefficient、u/v、sign/local factor 与推前前恒等式。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `UnsignedWordSkeletonAvailable` | `true` | `true` | unsigned carry-shell/anchor/phase skeleton 可以给 basis word 候选。 | 它仍需同一 row 上的 signed coefficient 来源。 |
| `FormalUnitSourceTupleContainersReady` | `true` | `true` | formal unit/source tuple 容器可承载 same-row hash。 | 容器不能替代逐行表。 |
| `ReverseRecoveryBlocked` | `true` | `true` | payment、零行覆盖、来源环和有限投影不能反推出 same-row 来源恒等式。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelOriginTableStillOpen` | `true` | `false` | 当前材料仍未证明逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `SameRowOriginIdentityCurrentCorpusProved` | `false` | `false` | 没有逐行原始生成表，无法证明 word 与 signed coefficient 是同一 pre-Cauchy primitive row。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `AfterRowTableNextAtomImported` | `true` | `false` | 既有 row-level 表证书已说明若继续下钻，下一原子是无环 seed signed row emitter。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |

## 4. 下一真正单点

首攻：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

若继续内部下钻该表，既有下一原子：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity
```

当前严格自足基：

```text
((RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance); if RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands is attacked internally, next atom is AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity
```

审稿边界：本文件只证明 same-row 桥接等价回收到逐行原始生成表；它没有证明该表，也没有证明行/列命题无条件闭合。
