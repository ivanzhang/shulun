# Prime Matrix strict Deléglise-Rivat psi 节点数据路由器

**状态：** `psi_algorithm_source_built_smoke_passed_batch_node_archive_hash_open`

Deléglise-Rivat 等价计算路线向前推进了一层：PsiTheta 源码和论文来源已经可定位，但这还不是节点证书。本环境已可构建并通过基础 smoke test，但仓库没有 646258 个节点的机器可读表；还必须补完整节点归档、节点表 hash，以及与 Dusart psi 口径和外向舍入的一致性证明。

```text
external_psi_theta_source_identified=true
local_source_checkout_signature_closed=true
buildable_psi_theta_toolchain_closed=true
compiled_psi_theta_binaries_present=true
psi_theta_smoke_test_closed=true
canonical_batch_psi_node_runner_closed=true
canonical_node_table_audit_checker_closed=true
machine_readable_node_archive_closed=false
deleglise_rivat_psi_node_data_or_equivalent_hash_closed=false
middle_psi_fine_mesh_node_slack_floor_hash_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 外部来源

| key | value |
| --- | --- |
| `source_page` | https://math.univ-lyon1.fr/~deleglis/calculs.html |
| `source_repo` | https://github.com/mhdeleglise/PsiTheta |
| `source_commit_observed` | 21f4f6553851f218801a733f607426c3dba9ba11 |
| `paper_citation` | M. Deléglise and J. Rivat, Computing Psi(x), Mathematics of Computation 67(224), 1998, 1691-1696. |

## 2. 构建与节点表画像

```text
[checkout_profile]
candidate_checkouts=['/tmp/PsiTheta', '/opt/code/shulun/external/PsiTheta']
existing_checkouts=['/tmp/PsiTheta']
checkout_present=true
chosen_checkout=/tmp/PsiTheta
source_file_hashes={'README.md': '61d7cd1bfe30996001e13c3e0331f4ac034b9223c515ea1d11270800285e42a9', 'makefile': '38e69a4e6dfb98375754f60f411e30e47571b31d112134f5e20a7b91591d71da', 'psi.cc': '7f81caa5c0f1e20bf4e32da3cd560e56d2722bf6c2ed1dda92e40ca529636595', 'theta.cc': 'c092b5bd38c08111616a4a0b403845b16faca57647750e08fda9ee5d20bf5708', 'psitheta.h': 'a05b847c6960aab55cca16b649e4b948077fbb7f5fc9a3cd1e2234479e13b324', 'tst_psi.cpp': 'c99c7f65f82d11060e058f5aeb09f5fc8ec9c6dc20d21879434491003a213bf1', 'tst_theta.cpp': 'af62896a9f17f33fda179a0fac8fe4058e02d8b0c710a9e550de0cf8eeb3b753'}
missing_source_files=[]
required_source_files_present=true

[toolchain_profile]
make_present=true
gpp_present=true
clangpp_present=false
compiler_present=true
make_path=/usr/bin/make
gpp_path=/usr/bin/g++
clangpp_path=None
requires_gmp_mpfr=true
note=GMP/MPFR runtime libraries were observed externally, but headers/compiler must be verified by build.

[binary_profile]
psi_binary_present=true
theta_binary_present=true
psi_binary_hash=e35085f321fa472c3e96a1e674e99bb02e603045bb5e3c5f25cf66df696ea4cb
theta_binary_hash=c80de3cad924a47f8498683fda1374e3d32e8855badefa6a3c037d6ab5d306bc

[smoke_test_profile]
smoke_test_closed=true
theta_readme_output=1.234518946373189641192934e9
theta_readme_expected=1.234518946373189641192934e9
theta_readme_match=true
psi_1e6_output=9.995865974956329220330615e5
psi_1e6_naive_float=9.995865974956310e+05
psi_1e6_relative_error=1.979878957977467e-15

[batch_runner_profile]
batch_runner_script_present=true
sample_node_table=/tmp/middle-psi-nodes-sample.jsonl
sample_node_table_present=true
sample_record_count=1.000000000000000e+00
sample_output_sha256=a3e3a64a0e5ddf761d90b043b3896681a42e4df044412ccff03caa57ebbdba11
sample_slack_ok=true
sample_records=[{'i': 0, 'psi_exe_sha256': 'e35085f321fa472c3e96a1e674e99bb02e603045bb5e3c5f25cf66df696ea4cb', 'psi_precision_decimal_digits': 30, 'psi_raw_output': '8.00000037979274743740661814686e11', 'psi_rounding_error_bound': '1E-18', 'psi_rounding_mode': 'MPFR_RNDN_output_wrapped_up_by_one_ulp_for_slack_lower_bound', 'psi_upper_for_slack': '800000037979.274743740661814687', 'psi_value': '800000037979.274743740661814686', 'required_node_slack_floor': '3073386.85452651', 'slack_ge_required_floor': True, 'slack_lower_bound': '22690020.725256259338185313', 'source_commit': '21f4f6553851f218801a733f607426c3dba9ba11', 'x_i': 800000000000}]

[node_table_profile]
candidate_paths=['docs/monograph/prime-matrix-strict-middle-psi-fine-mesh-node-table.json', 'docs/monograph/prime-matrix-strict-middle-psi-fine-mesh-node-table.jsonl', 'data/middle-psi-fine-mesh-node-table.jsonl']
existing_paths=[]
node_table_present=false
node_table_sizes={}
node_table_hashes={}

[workload_profile]
x_left=8.000000000000000e+11
x_right=1.446257064291475e+12
mesh_h=1.000000000000000e+06
expected_start_node_count=6.462580000000000e+05
first_start_node=8.000000000000000e+11
last_start_node=1.446257000000000e+12
required_node_slack_floor=3.073386854526510e+06
single_cli_program_not_sufficient_for_hash_certificate=true
batch_adapter_required=true
canonical_output_format=jsonl, one sorted record per i, UTF-8, LF line ending, SHA256 over exact bytes
required_record_fields=['i', 'x_i', 'psi_value', 'psi_rounding_mode', 'psi_precision_decimal_digits', 'slack_lower_bound', 'slack_ge_required_floor', 'source_commit', 'source_chunk_hash']

```

## 3. 剩余替换

```text
DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger
  =>
BuildablePsiThetaToolchain AND PsiThetaSmokeTestLedger AND CanonicalBatchPsiNodeRunnerLedger AND MachineReadableNodeArchiveLedger AND SourceAlgorithmToDusartConventionMatch

MiddlePsiFineMeshNodeSlackFloorAndHashLedger
  =>
DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger AND NodeSlackFloorAuditLedger AND MeshCompletenessAndIndexHashLedger AND MiddlePsiUpperDirectedRoundingLedger

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只处理中段 psi 节点数据来源，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ExternalPsiThetaSourceLocated` | `true` | `true` | Deléglise 本人页面与 mhdeleglise/PsiTheta 仓库给出 psi/theta 计算源码入口。 | source is identified, not yet a node certificate |
| `PublishedAlgorithmCitationLocated` | `true` | `true` | 源码 README 对应 Deléglise-Rivat Computing Psi(x) 论文，算法来源边界可登记。 | paper proof not rederived here |
| `LocalSourceCheckoutSignature` | `true` | `true` | 本地若有源码 checkout，则登记关键源码文件 hash。 | checkout or vendored source tree |
| `BuildablePsiThetaToolchain` | `true` | `true` | 当前环境已需要 make、C++ 编译器和 psi/theta 可执行文件共同验收。 | install/build toolchain or use a prebuilt audited container |
| `PsiThetaSmokeTestLedger` | `true` | `true` | README theta 示例和 psi(1e6) 朴素筛对照已作为基础 smoke test。 | target-scale and full node table still required |
| `CanonicalBatchPsiNodeRunnerLedger` | `true` | `true` | 已新增批处理 runner，并用目标区间首节点生成 JSONL 样本；完整归档仍未生成。 | full node archive generation still required |
| `CanonicalNodeTableAuditScriptLedger` | `true` | `true` | 已新增机械验收脚本，可检查 JSONL 节点表的索引、x_i、余量下界、节点数和 SHA256。 | requires actual node table to pass |
| `MachineReadableNodeArchiveLedger` | `false` | `false` | 仓库当前仍未发现中段百万网格完整节点表。 | generate or import node jsonl archive |
| `SourceAlgorithmToDusartConventionMatch` | `false` | `false` | 需要证明源码输出的 psi 口径、端点跳变、舍入方向与 Dusart 表使用口径一致。 | MiddlePsiUpperDirectedRoundingLedger |
| `DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger` | `false` | `false` | 算法源已定位，但构建、批量节点生成、节点表 hash、口径/舍入验收尚未闭合。 | BuildablePsiThetaToolchain AND PsiThetaSmokeTestLedger AND CanonicalBatchPsiNodeRunnerLedger AND MachineReadableNodeArchiveLedger AND SourceAlgorithmToDusartConventionMatch |
| `MiddlePsiFineMeshNodeSlackFloorAndHashLedger` | `false` | `false` | 节点数据源未闭合时，节点余量/hash 守门不能升级。 | DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger AND NodeSlackFloorAuditLedger AND MeshCompletenessAndIndexHashLedger AND MiddlePsiUpperDirectedRoundingLedger |
| `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger` | `false` | `false` | BT 外部输入和素数幂修正已处理，但短区间总包仍卡在节点余量/hash。 | MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 节点数据源定位不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
MachineReadableNodeArchiveLedger
```
