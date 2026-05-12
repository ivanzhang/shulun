# Prime Matrix strict fixed-pair fiber bound 路由器

**状态：** `strict_fixed_pair_fiber_bound_reduced_to_complete_key_partition_and_fixed_key_multiplicity_open`

`ExactUVMapFixedPairPolylogFiberBoundLedger` 被压成两个真正原子：`RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger` 与 `FixedKeyExactUVLocalMultiplicityO1Ledger`。其中 key-to-fiber 的形式不等式已闭合，但 actual complete key 分区和固定 key 局部 O(1) 原像证明尚未给出；因此行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
fixed_pair_fiber_bound_router_closed=true
deterministic_key_fiber_inequality_closed=true
registered_complete_primitive_emitter_key_partition_polylog_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 形式引理

```text
Let D be the actual primitive pre-Cauchy emitter domain, pi:D->Omega_exact the exact `(u,v)` map, and kappa:D->K a complete primitive emitter key. If |K|<=L^C and sup_{(u,v),k}|{d in D: pi(d)=(u,v), kappa(d)=k}|<=C0, then sup_{(u,v)}|pi^{-1}(u,v)|<=C0*L^C=log^O(1).
```

## 2. 原子化

拆分前：

```text
ExactUVMapFixedPairPolylogFiberBoundLedger
```

拆分后：

```text
RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FixedPairFiberTargetActive` | `true` | `false` | 上一层已把 bounded incidence 拆成源域熵账本与 fixed-pair 纤维上界账本。 | ExactUVMapFixedPairPolylogFiberBoundLedger |
| `DeterministicKeyFiberInequalityClosed` | `true` | `true` | 若 primitive emitter 被完整 key 分区，key 数为 log^C，且每个固定 `(u,v,key)` 最多 O(1) 个源原像，则每个固定 `(u,v)` 纤维至多 log^O(1)。 | 这是形式不等式，不提供 actual key 表或局部 O(1) 原像证明。 |
| `CompleteKeyPartitionIsNecessary` | `true` | `true` | branch key 必须是 complete key：包含 formal unit、branch path、sign/local factor、dyadic/truncation 与 exact `(u,v)` map 口径。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger。 |
| `PaymentSkeletonNotACompleteKeyPartition` | `true` | `true` | payment skeleton 只给 completion-hole/first-cover 计数，不给 pre-Cauchy primitive summand 的 complete key。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger。 |
| `DisintegrationDictionaryNotAFiberBound` | `true` | `true` | 逐纤维字典即使形式可写，也可在同一 `(u,v)` 中塞入任意多 summand；还需要 complete key 与固定 key 局部重数。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `ReverseProvenanceNoGoImported` | `true` | `true` | 从 Gamma 或有限投影反推 primitive preimage 不唯一，不能由下游图推出 fixed-pair 纤维 polylog。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `SignedPhiReductionIdentifiesSameEmitter` | `true` | `true` | actual signed/Phi 预算已被压到同一个 pre-pushforward emitter，说明本步没有改换证明对象。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `BranchBudgetCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明 actual noncanonical primitive emitter 的 complete branch/key 数为 log^O(1)。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger。 |
| `FixedKeyLocalMultiplicityCurrentCorpusProved` | `false` | `false` | 当前材料没有 actual emitter 公式/Jacobian/三角恢复律来证明固定 complete key 与 fixed `(u,v)` 下只有 O(1) 原像。 | FixedKeyExactUVLocalMultiplicityO1Ledger。 |
| `CurrentCorpusFixedPairFiberBoundProved` | `false` | `false` | complete key 分区与固定 key 局部 O(1) 重数都未证明，所以 fixed-pair polylog fiber bound 仍开放。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |

## 4. 结构结论

fixed-pair 纤维上界不是 payment 计数，也不是 CRT 位置刚性。它必须在 Cauchy/dispersion 前的 actual primitive emitter 上证明：先有完整 key 的 polylog 分区，再有固定 key 下 exact-UV map 的 O(1) 局部重数。缺任一项都会允许大量 preimage 坍缩到同一个 `(u,v)`。

## 5. 下一主攻点

```text
RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
```
