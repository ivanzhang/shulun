# Prime Matrix anchor interval 证书文件路由器

**状态：** `anchor_interval_certificate_file_closed_enumeration_ready`

AnchorIntervalCertificateFileLedger 已闭合：每个 source tuple 的锚区间证书文件由端点公式确定性生成，空锚集、空区间和相位过滤均登记为记录。下一步可回收 `ConcreteAnchorIntervalEnumerationLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
anchor_interval_certificate_file_ledger_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
AnchorIntervalCertificateFileLedger => EndpointFormula AND SourceTupleParameterLedger AND AnchorSetReconstruction AND CanonicalFileHash AND EmptyPhaseRegistration.
```

## 2. 证书记录族

| record_type | coverage | rule |
| --- | --- | --- |
| source_tuple_header | 每个 source_tuple_hash 一条。 | 记录 formal_unit_id、P/range、window_id、I=[L,R]、A、D0、phase_rule、anchor_set_hash。 |
| anchor_interval_row | 每个 a in sorted(A) 一条。 | left_d=max(D0,ceil(L/a)); right_d_exclusive=min(2D0,floor(R/a)+1)。 |
| phase_filtered_segment_row | phase_rule 非 identity 时逐个最大保留段或 residue 条件记录。 | phase_rule(d)=true 的 d 保留；不可判定则进入 PhaseFilterReturn。 |
| empty_interval_row | left_d>=right_d_exclusive 时必须显式记录。 | 空区间不是缺文件，写 empty_interval_flag=true。 |
| empty_anchor_set_row | A=empty 时必须显式记录。 | 空锚集不是缺 source tuple，写 empty_anchor_set_flag=true。 |

## 3. 文件闭合纪律

| law | formula | meaning |
| --- | --- | --- |
| same_source_tuple_lock | all rows inherit the same source_tuple_hash and anchor_set_hash. | 锚集合、窗口、D0 和相位规则不能跨 formal unit 拼接。 |
| endpoint_total_function | J_a=[max(D0,ceil(L/a)), min(2D0,floor(R/a)+1)). | 给定 source tuple 与 anchor 后，端点是全函数，没有选择余地。 |
| per_anchor_totality | File(s) contains one row for every a in sorted(A). | 证书文件逐锚覆盖；漏掉任一锚都不能算 complete。 |
| empty_case_is_data | A=empty or J_a=empty is represented by explicit empty flags. | 空锚集和空区间被登记为数据，不形成无名缺口。 |
| phase_filter_totality | identity phase is written; non-identity phase emits segments/residue clauses or a named return. | 相位过滤不会把点静默删除。 |
| canonical_file_hash | file_id=H('anchor_interval_file', source_tuple_hash, sorted(endpoint_proof_hashes)). | 证书文件由规范哈希固定，枚举顺序不影响文件身份。 |

## 4. 哈希合同

| hash | formula |
| --- | --- |
| endpoint_proof_hash | H(source_tuple_hash,a,L,R,D0,phase_rule,left_d,right_d_exclusive,empty_flag,segments)。 |
| anchor_interval_certificate_file_id | H(formal_unit_id,source_tuple_hash,sorted(endpoint_proof_hashes))。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AnchorIntervalCertificateGateActive | `true` | `false` | 上一层已把最窄点推进到 anchor interval 证书文件。 | AnchorIntervalCertificateFileLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| EndpointFormulaImported | `true` | `true` | J_a 的左右端点已由 ceil/floor 与 [D0,2D0) 裁剪唯一确定。 | 公式口径固定。 |
| SourceTupleParameterLedgerImported | `true` | `true` | source tuple 已锁定 P/range、window、I=[L,R]、A、D0 与 phase_rule。 | 不能后验改锚或改窗口。 |
| AnchorSetReconstructionImported | `true` | `true` | A 与 anchor_set_hash 可由同一 formal unit 的有限来源族 payload 复算。 | 逐锚枚举域固定。 |
| CanonicalHashImported | `true` | `true` | formal_unit_id、source_tuple_hash 与 endpoint_proof_hash 使用分层哈希。 | 文件身份稳定。 |
| EmptyAndPhaseCasesRegistered | `true` | `true` | A=empty、J_a=empty 和非 identity phase 都有显式记录或命名回流。 | 无静默删除口。 |
| AnchorIntervalCertificateFileLedger | `true` | `true` | anchor interval 证书文件由 source tuple 与端点公式确定性生成；逐锚、空区间和相位过滤均有记录。 | ConcreteAnchorIntervalEnumerationLedger |

## 6. 下一步

当前回收目标为 `ConcreteAnchorIntervalEnumerationLedger`；随后才是 `LowOverlapMultiplicityTableLedger`。

审稿边界：本步只关闭假设链条中的 anchor interval 证书文件生成律；不证明真实早期零行存在或缺席，也不关闭行列无条件定理。
