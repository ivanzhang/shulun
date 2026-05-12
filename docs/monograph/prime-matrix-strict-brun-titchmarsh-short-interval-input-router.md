# Prime Matrix strict 短区间 Brun-Titchmarsh 输入登记器

**状态：** `brun_titchmarsh_external_input_registered_self_contained_proof_open_node_hash_still_open`

Brun-Titchmarsh 短区间素数计数输入可以在外部黑箱路线中登记：用 pi(x+h)-pi(x)<=2h/log h，并乘以 log(e^28+h)，得到与原短区间账本相同的素数 theta 增量上界。严格自足版仍未重证该定理；在外部路线中，短区间总包现在只剩细网格节点余量/hash。

```text
brun_titchmarsh_short_interval_input_external_closed=true
brun_titchmarsh_short_interval_input_self_contained_closed=false
prime_power_short_interval_correction_closed=true
middle_psi_fine_mesh_node_slack_floor_hash_closed=false
certified_short_interval_psi_increment_upper_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 参数匹配

```text
x_left=8.000000000000000e+11
x_right=1.446257064291475e+12
mesh_h=1.000000000000000e+06
h_gt_one=true
short_interval_inside_positive_range=true
bt_prime_count_bound=1.447648273010839e+05
log_weight_bound=2.800000069143977e+01
theta_prime_increment_bound=4.053415264526510e+06
```

## 2. 外部来源

| name | url | statement_used |
| --- | --- | --- |
| Montgomery-Vaughan large sieve / explicit Brun-Titchmarsh interval form | https://doi.org/10.1112/S0025579300004708 | pi(x+y)-pi(x) <= 2y/log(y) for the q=1 short interval form |
| MathOverflow pointer to the Montgomery-Vaughan explicit interval form | https://mathoverflow.net/a/370956 | secondary pointer only; not a replacement for the theorem source |

## 3. 剩余替换

```text
CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger
  =>
MiddlePsiFineMeshNodeSlackFloorAndHashLedger

BrunTitchmarshShortIntervalPrimeCountUpperLedger
  =>
closed on the external theorem lane; self-contained proof remains open

MiddlePsiFineMeshNodeSlackFloorAndHashLedger
  =>
DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger AND NodeSlackFloorAuditLedger AND MeshCompletenessAndIndexHashLedger AND MiddlePsiUpperDirectedRoundingLedger

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只登记短区间素数计数外部输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ExternalBrunTitchmarshTheoremRegistered` | `true` | `true` | 采用 Montgomery-Vaughan 显式 Brun-Titchmarsh 的 q=1 区间形式作为外部黑箱。 | not self-contained |
| `ParameterMatchToMillionMesh` | `true` | `true` | h=1e6>1，且所有起始点均在正区间内；每段素数个数用 2h/log h 控制。 | none |
| `ThetaWeightConversionArithmetic` | `true` | `true` | 再乘以 log(x_right+h) 得到与短区间账本一致的素数部分 theta 权重上界。 | none |
| `BrunTitchmarshSelfContainedProof` | `false` | `false` | 本文没有重证 Montgomery-Vaughan 大筛/Brun-Titchmarsh 定理；严格自足版仍需内部证明或可接受的定理引用政策。 | internal large sieve proof or accepted external theorem status |
| `BrunTitchmarshShortIntervalPrimeCountUpperLedger` | `true` | `true` | 在外部黑箱路线中，短区间素数计数输入已完成登记和参数匹配。 | self-contained proof remains open |
| `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger` | `false` | `false` | BT 外部输入和素数幂修正已经处理后，短区间总包仍卡在细网格节点余量/hash。 | MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | BT 输入登记不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
MiddlePsiFineMeshNodeSlackFloorAndHashLedger
```
