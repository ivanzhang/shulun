# Prime Matrix strict table_012 theta 极值 runner 前沿证书

**状态：** `table012_full_extremal_archive_closed_interval_arithmetic_open`

table_012 自足路线继续推进：独立 theta 极值扫描器已经物化，第一行、前 9 行、前 18 行以及完整 34 行归档均已通过工程审计并登记 hash。但严格 log 区间舍入仍未闭合；尤其第一行绝对余量只有约 76，不能把普通浮点/Kahan 归档冒充为最终自足证明。

```text
table012_theta_extremal_runner_algorithm_closed=true
table012_extremal_archive_audit_tool_closed=true
table012_first_row_extremal_smoke_certificate_closed=true
table012_prefix9_rows_to_1e9_archive_audit_closed=true
table012_prefix18_rows_to_1e10_archive_audit_closed=true
full_table012_theta_extremal_archive_run_hash_closed=true
certified_log_summation_interval_arithmetic_closed=false
theta_less_than_identity_to_8e11_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 第一行样本

| field | value |
| --- | --- |
| `label` | `1E+08` |
| `left` | `100000000` |
| `right` | `200000000` |
| `passed_raw` | `True` |
| `passed_with_guard` | `True` |
| `raw_margin` | `7.634811345658090431e+01` |
| `margin_after_guard` | `7.534810237764390431e+01` |
| `max_x` | `179845447` |
| `max_kind` | `prime_jump` |
| `max_required_b1` | `-4.480691230598484582e-04` |
| `b1_minus_max_required_b1` | `8.069123059848458226e-06` |
| `row_prime_count` | `5317482` |
| `global_prime_count` | `11078937` |
| `sha256` | `27d1d0174950c5766c46bcfed4daeafd98d18c8e6fd2149db5865f9e9dfee5b0` |

## 2. 前缀归档

| archive | closed | rows | last_right | min_guard_margin | min_guard_label | sha256 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `prefix9` | `true` | `9` | `1000000000` | `5.507003791407393599e+01` | `3E+08` | `54d15fa3855ee0d3c5718fb50e3e2d856e47243420e80a94d4ff317333e5d5da` |
| `prefix18` | `true` | `18` | `10000000000` | `5.507003791407393599e+01` | `3E+08` | `ea1136fd4c8e1168ed8e97e2bedfe0f3928ea23b42a1cc9f2d473fa1c6ba0667` |
| `full34` | `true` | `34` | `800000000000` | `5.507003791407393599e+01` | `3E+08` | `2d1e955a6fa533c4e68bf9d786617d4d090dc91b52e224447eebaff849ddc1a3` |

## 3. 自足替换

```text
IndependentThetaExtremalArchiveForTable012IntervalsLedger
  =>
FullTable012ThetaExtremalArchiveRunAndHashLedger AND CertifiedLogSummationIntervalArithmeticForThetaLedger AND Table012DirectedRoundingAndIntervalPropagationLedger

Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger
  =>
PublishedTable012GeneratorArtifactAndHashLedger OR IndependentThetaExtremalArchiveForTable012IntervalsLedger
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只推进 table_012 自足计算输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `Table012SelfContainedFrontierImported` | `true` | `true` | 上一证书已把 P5.1 低段自足缺口压成 table_012 原始生成器或独立 theta 极值归档。 | Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger |
| `Table012ThetaExtremalRunnerAlgorithmLedger` | `true` | `true` | 已物化独立扫描器：从 theta(1e8) 开始，按 table_012 区间扫描素数跳点并记录最大缺陷。 | 0220b7cdc9c5b7ed88acb99571370e72ebc0b046032cc7f4905f9085fca9c392 |
| `Table012FirstRowExtremalSmokeCertificateLedger` | `true` | `true` | 第一行 [1e8,2e8] 样本已跑通；最危险点与余量已落盘，验证极值口径可执行。 | 27d1d0174950c5766c46bcfed4daeafd98d18c8e6fd2149db5865f9e9dfee5b0 |
| `Table012ExtremalArchiveAuditToolLedger` | `true` | `true` | 已新增归档审计器，检查行数、区间、b1、最大点、原始余量、保护余量和 hash。 | 1774788e77e9f2ee1a06f3cbb4cc0695db2720c42e76edaf9d1853f5b5d01f4e |
| `Table012Prefix9RowsTo1e9ArchiveAuditLedger` | `true` | `true` | 前 9 行 [1e8,1e9] 已生成并通过归档审计。 | 54d15fa3855ee0d3c5718fb50e3e2d856e47243420e80a94d4ff317333e5d5da |
| `Table012Prefix18RowsTo1e10ArchiveAuditLedger` | `true` | `true` | 前 18 行 [1e8,1e10] 已生成并通过归档审计；仍只是完整归档前缀。 | ea1136fd4c8e1168ed8e97e2bedfe0f3928ea23b42a1cc9f2d473fa1c6ba0667 |
| `ThinFirstRowMarginDetected` | `true` | `true` | 第一行 published b1 的绝对余量只有约 76，说明后续必须补严格 log 区间舍入纪律。 | CertifiedLogSummationIntervalArithmeticForThetaLedger |
| `FullTable012ThetaExtremalArchiveRunAndHashLedger` | `true` | `true` | 完整 34 行极值归档需读满 table_012 全部区间，且每行通过工程保护余量检查并登记 hash。 | 2d1e955a6fa533c4e68bf9d786617d4d090dc91b52e224447eebaff849ddc1a3 |
| `CertifiedLogSummationIntervalArithmeticForThetaLedger` | `false` | `false` | 当前样本使用 long double/Kahan 与工程保护，不等同于严格外向 log 区间算术证明。 | interval log table or directed MPFR/arb-style summation certificate |
| `IndependentThetaExtremalArchiveForTable012IntervalsLedger` | `false` | `false` | 独立归档需要完整运行/hash与区间舍入同时闭合；当前仍卡在严格 log 区间舍入。 | FullTable012ThetaExtremalArchiveRunAndHashLedger AND CertifiedLogSummationIntervalArithmeticForThetaLedger |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 本步仍只是解析输入自足化，不产生早期零行反例链终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosed` | `false` | `false` | 行/列命题仍未作者侧无条件闭合。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
CertifiedLogSummationIntervalArithmeticForThetaLedger
```

