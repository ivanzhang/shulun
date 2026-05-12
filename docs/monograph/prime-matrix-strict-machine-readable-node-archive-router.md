# Prime Matrix strict 机器可读 psi 节点归档路由器

**状态：** `node_archive_spec_sample_audit_ready_full_archive_open`

机器可读节点归档已经压成一个明确的工程-数学证书：规格、目标首节点样本和验收器就绪，但完整 646258 行表尚未生成。单点 CLI 路线不能作为完整归档策略；原生 range 批量可执行文件已跑通样本，下一步应生成完整归档并验收 hash，或导入外部完整归档。

```text
archive_specification_closed=true
target_scale_single_node_sample_closed=true
node_table_audit_checker_available=true
native_range_psi_theta_batch_executable_closed=true
machine_readable_node_archive_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 归档规格

```text
expected_node_count=6.462580000000000e+05
x_left=8.000000000000000e+11
x_right=1.446257064291475e+12
mesh_h=1.000000000000000e+06
first_index=0.000000000000000e+00
last_index=6.462570000000000e+05
min_records_per_required_archive=6.462580000000000e+05
canonical_serialization=JSONL sorted by i, UTF-8, LF, one record per start node
minimum_required_fields=['i', 'x_i', 'psi_value', 'psi_upper_for_slack', 'slack_lower_bound', 'slack_ge_required_floor', 'psi_exe_sha256', 'source_commit']
```

## 2. 样本

```text
sample_path=/tmp/middle-psi-nodes-sample.jsonl
sample_present=true
sample_sha256=a3e3a64a0e5ddf761d90b043b3896681a42e4df044412ccff03caa57ebbdba11
sample_count=1
sample_all_slack_ok=true
sample_records=[{'i': 0, 'psi_exe_sha256': 'e35085f321fa472c3e96a1e674e99bb02e603045bb5e3c5f25cf66df696ea4cb', 'psi_precision_decimal_digits': 30, 'psi_raw_output': '8.00000037979274743740661814686e11', 'psi_rounding_error_bound': '1E-18', 'psi_rounding_mode': 'MPFR_RNDN_output_wrapped_up_by_one_ulp_for_slack_lower_bound', 'psi_upper_for_slack': '800000037979.274743740661814687', 'psi_value': '800000037979.274743740661814686', 'required_node_slack_floor': '3073386.85452651', 'slack_ge_required_floor': True, 'slack_lower_bound': '22690020.725256259338185313', 'source_commit': '21f4f6553851f218801a733f607426c3dba9ba11', 'x_i': 800000000000}]

[native_range_profile]
native_source=experiments/prime_matrix_middle_psi_native_range_runner.cpp
native_source_present=true
native_source_sha256=0a9e48ee092d5ab07d8bf86ecfb30df0ff65cd6d59dc85a48f4e4b2e2ac818a0
native_executable=/tmp/PsiTheta/psi_range_jsonl
native_executable_present=true
native_executable_sha256=63dfb335717d8872909c3bbe4b202c7ef1dcf1a0fbb7c4be9775d3c96cefb541
native_sample=/tmp/middle-psi-native-range-sample.jsonl
native_sample_present=true
native_sample_sha256=f84cd89576611083f75926f730cada3d44e5c6c3fe6b4e56e615e7a13901693c
native_sample_count=1
native_sample_all_slack_ok=true
native_sample_records=[{'i': 0, 'psi_precision_decimal_digits': 30, 'psi_raw_output': '8.00000037979274743740661814686126645242e+11', 'psi_rounding_error_bound': '1.00000000000000000000000000000000000000e-18', 'psi_rounding_mode': 'MPFR_RNDN_value_wrapped_up_by_one_decimal_ulp_for_slack_lower_bound', 'psi_upper_for_slack': '8.00000037979274743740661814687126645242e+11', 'psi_value': '8.00000037979274743740661814686126645242e+11', 'required_node_slack_floor': '3073386.85452651', 'slack_ge_required_floor': True, 'slack_lower_bound': '2.26900207252562593381853128733547583280e+07', 'source_commit': '21f4f6553851f218801a733f607426c3dba9ba11', 'x_i': 800000000000}]
```

## 3. 剩余替换

```text
MachineReadableNodeArchiveLedger
  =>
(NativeRangePsiThetaBatchExecutableLedger OR ExternalPrecomputedPsiNodeArchiveWithHashLedger) AND FullNodeArchiveCompletenessAndHashLedger

DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger
  =>
MachineReadableNodeArchiveLedger AND SourceAlgorithmToDusartConventionMatch

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只处理 psi 节点归档的机器可读性，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ArchiveSpecificationLedger` | `true` | `true` | 完整归档必须覆盖 646258 个百万网格起始节点，并采用稳定 JSONL/hash 口径。 | FullNodeArchiveCompletenessAndHashLedger |
| `TargetScaleSingleNodeSampleLedger` | `true` | `true` | 目标区间首节点样本已生成并过余量门槛，但样本不是完整归档。 | MachineReadableNodeArchiveLedger |
| `AuditCheckerAvailable` | `true` | `true` | 已有节点表验收器可检查节点数、索引、x_i、余量和 SHA256。 | requires full archive as input |
| `PerNodeCliArchiveRouteRejected` | `true` | `true` | 原单点 CLI 即使可运行，也不能作为完整归档策略；需要原生 range 批量程序或外部预计算归档。 | NativeRangePsiThetaBatchExecutableLedger OR ExternalPrecomputedPsiNodeArchiveWithHashLedger |
| `NativeRangePsiThetaBatchExecutableLedger` | `true` | `true` | 已新增并编译 C++ 原生 range runner，目标首节点样本输出通过余量门槛。 | full archive generation still required |
| `ExternalPrecomputedPsiNodeArchiveWithHashLedger` | `false` | `false` | 或者导入外部已计算的完整节点表，并登记来源、版本和整体 SHA256。 | precomputed full archive |
| `FullNodeArchiveCompletenessAndHashLedger` | `false` | `false` | 需要完整 646258 行通过 audit 脚本，并固定整体 hash。 | full archive must exist |
| `MachineReadableNodeArchiveLedger` | `false` | `false` | 归档规格、样本和验收器已就绪，但完整机器可读节点归档仍未生成。 | (NativeRangePsiThetaBatchExecutableLedger OR ExternalPrecomputedPsiNodeArchiveWithHashLedger) AND FullNodeArchiveCompletenessAndHashLedger |
| `DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger` | `false` | `false` | 节点归档未闭合时，等价计算数据/hash 仍不能升级。 | MachineReadableNodeArchiveLedger AND SourceAlgorithmToDusartConventionMatch |
| `MiddlePsiFineMeshNodeSlackFloorAndHashLedger` | `false` | `false` | 节点归档未闭合时，节点余量/hash 守门仍开放。 | MachineReadableNodeArchiveLedger AND NodeSlackFloorAuditLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 节点归档路由不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
FullNodeArchiveCompletenessAndHashLedger
```
