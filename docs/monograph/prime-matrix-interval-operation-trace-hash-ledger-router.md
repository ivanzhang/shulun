# Prime Matrix 区间操作 trace/hash 账本路由器

**状态：** `interval_operation_trace_hash_ledger_closed_theta_tail_next`

IntervalOperationTraceHashLedger 已压成并闭合为 canonical DAG 账本：所有区间端点、Taylor 阶数、尾界、父节点和 root hash 都有可复放规则。由此复球核的 trace 缺口消失；主线剩余转为 Gaussian theta 尾项账本和紧致 theta-Mellin 积分分段账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
interval_operation_trace_hash_ledger_closed=true
theta_mellin_transcendental_kernel_closed=true
certified_complex_ball_kernel_closed=true
theta_mellin_interval_engine_closed=false
row_column_self_contained_closed=false
```

## 1. 替换与晋级

```text
IntervalOperationTraceHashLedger => IntervalOperationTraceHashLedgerClosedCanonicalDAGv1
CertifiedComplexBallArithmeticKernel closes once dyadic algebra, ThetaMellinElementaryTranscendentalTaylorKernel0To14, and IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 are present.
```

## 2. 节点语法

| node type | fields / operations | invariant |
| --- | --- | --- |
| `DyadicInterval` | `['lo_num', 'hi_num', 'scale', 'closed']` | lo_num <= hi_num; value set is [lo_num/2^scale, hi_num/2^scale]. |
| `ComplexRectangle` | `['re_interval_hash', 'im_interval_hash']` | complex box is Re interval x Im interval. |
| `PrimitiveRationalOp` | `['add', 'sub', 'mul', 'div', 'neg', 'abs_bound']` | output interval is verified by integer endpoint inequalities. |
| `TaylorOracleCall` | `['log_atanh', 'pi_machin', 'sin', 'cos', 'exp']` | stores range_box_id, order, rational_tail_bound, output_hash. |
| `ThetaMellinComposite` | `['complex_power', 'gaussian_exp', 'theta_term', 'finite_sum']` | parents are already hashed interval nodes; output is outward rounded. |
| `TraceRoot` | `['ordered_node_hashes', 'target', 'source_hashes']` | root hash fixes the whole replay transcript. |

## 3. 复放规则

1. 按 ordered_node_hashes 的顺序读取节点，要求每个 parent_hash 已在前面出现。
2. 对每个节点重新执行 canonical JSON 序列化并核对 node_hash。
3. 所有 dyadic 端点只允许整数和 2 的幂分母，不允许浮点舍入或隐式库状态。
4. PrimitiveRationalOp 由有限整数不等式验证外包包含关系。
5. TaylorOracleCall 必须引用已闭合范围盒和尾阶表，且记录截断阶数与尾界。
6. TraceRoot 的哈希作为后续边界非零证书、winding 证书和积分分段证书的父哈希。

## 4. 样例 trace

```text
sample_node_count=8
sample_root_hash=2f3dfe2e58f74a4a34b9051f510b8c3275ea9cfc55f732044cf41ebdd87dc7a3
```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TraceHashLedgerGateActive` | `true` | `true` | Taylor 尾阶闭合后，当前最窄点正是区间操作调用的可复核登记账本。 | IntervalOperationTraceHashLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本账本只规定假设链条中的计算证书格式，不以真实零行缺席作为输入。 | 保持 row_column_self_contained_closed=false。 |
| `DyadicAndComplexNodeSchemaClosed` | `true` | `true` | dyadic 实区间和复矩形区间已经可由整数端点外包，trace 节点只记录规范端点。 | DyadicRationalIntervalArithmeticCoreClosed AND ComplexRectangularIntervalPropagationClosed |
| `TranscendentalTemplatesImported` | `true` | `true` | log/pi/trig/exp 模板、范围盒和尾阶表已经齐全，每次调用只需引用对应账本编号。 | ThetaMellinElementaryTranscendentalTaylorKernel0To14 |
| `CanonicalDAGAndParentHashClosed` | `true` | `true` | 每个节点哈希由规范 JSON 决定，父节点必须先出现，root hash 固定整条复放轨迹。 | IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 |
| `ReplayInductionLemmaClosed` | `true` | `true` | 若所有原子节点外包真值且每个操作节点满足有理包含验证，则按拓扑归纳 root 区间外包目标函数值。 | 后续 xi 边界证书可引用 root_hash。 |
| `TraceDoesNotPayThetaTailOrQuadrature` | `false` | `false` | trace/hash 只保证可复核与无隐藏调用；t>64、n>20 尾项和积分分段误差仍需单独付费。 | GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14 |
| `IntervalOperationTraceHashLedger` | `true` | `true` | 区间操作 trace/hash 账本已由规范 DAG、父哈希、尾阶引用和复放归纳闭合。 | IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 |

## 6. 下一步

当前最窄点：`GaussianThetaTailBoundLedger`。
随后补：`CompactThetaMellinQuadratureSubdivisionLedger0To14`。
再后续进入：`XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：trace/hash 是证书纪律门，已经闭合；它没有替代 theta 尾项或积分分段误差。
