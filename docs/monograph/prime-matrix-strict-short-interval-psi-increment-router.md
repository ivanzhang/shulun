# Prime Matrix strict 中段短区间 psi 增量上界路由器

**状态：** `short_interval_increment_arithmetic_feasible_node_slack_and_bt_inputs_open`

短区间增量路线出现了可行的数值骨架：用长度 1e6 的网格，Brun-Titchmarsh 型素数增量上界加 20000 的素数幂预留后，每个节点只需约 3.07e6 的绝对余量即可防止点间逃逸。但这还不是闭合证明；仍需 Brun-Titchmarsh 输入、素数幂修正，以及约 646258 个节点的 psi 余量/hash。

```text
million_mesh_increment_arithmetic_closed=true
certified_short_interval_psi_increment_upper_closed=false
brun_titchmarsh_short_interval_input_closed=false
prime_power_short_interval_correction_closed=false
middle_psi_fine_mesh_node_slack_floor_hash_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 百万网格算术画像

```text
mesh_h=1.000000000000000e+06
x_left=8.000000000000000e+11
x_right=1.446257064291475e+12
interval_count=6.462580000000000e+05
bt_prime_increment_bound=4.053415264526510e+06
prime_power_reserve=2.000000000000000e+04
total_increment_bound=4.073415264526510e+06
target_linear_allowance=1.000028410000000e+06
required_node_slack_floor=3.073386854526510e+06
arithmetic_feasible_if_node_slack_floor_available=true
```

## 2. 自足替换

```text
CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger
  =>
BrunTitchmarshShortIntervalPrimeCountUpperLedger AND PrimePowerShortIntervalCorrectionLedger AND MiddlePsiFineMeshNodeSlackFloorAndHashLedger

MiddlePsiFineMeshNodeSlackFloorAndHashLedger
  =>
machine-readable node table on mesh h=1e6 with psi-node slack >= required_node_slack_floor

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计假设反例链可调用的中段短区间增量，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ShortIntervalPsiIncrementGateActive` | `true` | `true` | 中段覆盖证书已把点间逃逸压成短区间 psi 增量上界。 | CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger |
| `MillionMeshBrunTitchmarshIncrementArithmeticLedger` | `true` | `true` | 取百万级网格时，Brun-Titchmarsh 型素数增量加素数幂预留后，只需每个节点保留约 3.07e6 绝对余量。 | MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `BrunTitchmarshShortIntervalPrimeCountUpperLedger` | `false` | `false` | 需要登记或自足证明适用于本区间和网格长度的 Brun-Titchmarsh 短区间素数计数上界。 | classical Brun-Titchmarsh input or internal proof |
| `PrimePowerShortIntervalCorrectionLedger` | `false` | `false` | 需要证明百万网格内素数幂贡献小于预留 20000，或给出更紧可复算包络。 | PrimePowerJumpLocalizationOrUpperEnvelopeLedger |
| `MiddlePsiFineMeshNodeSlackFloorAndHashLedger` | `false` | `false` | 需要约 646258 个百万网格节点的 psi 值或上界，并证明每个节点有足够目标余量。 | MiddlePsiFineMeshComputationAndHashLedger |
| `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger` | `false` | `false` | 增量算术路径可行，但短区间上界输入、素数幂修正和节点余量/hash 尚未闭合。 | BrunTitchmarshShortIntervalPrimeCountUpperLedger AND PrimePowerShortIntervalCorrectionLedger AND MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `FineMeshAlternativeStillOpen` | `false` | `false` | 若不采用 Brun-Titchmarsh 增量包，则需要直接给出全段精细网格、跳点定位和外向舍入证书。 | MiddlePsiFineMeshComputationAndHashLedger AND PrimePowerJumpLocalizationOrUpperEnvelopeLedger AND MiddlePsiUpperDirectedRoundingLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 短区间增量审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
MiddlePsiFineMeshNodeSlackFloorAndHashLedger
```
