# Prime Matrix strict 多线性倒数 Kloosterman 固定对数节省输入证书

**状态：** `exact_multilinear_reciprocal_kloosterman_input_statement_closed_self_contained_proof_open`

最窄自足数学硬点已压成一个精确定理：对 RKS2/RKS3 的 Vaughan/divisor-bounded 倒数乘积相位块，证明 `|S(M,N)|<=MN/log^118(P)`。这个指数来自 Tail-log4 目标 `44` 加 RKS 总损失 `74`；`K_sieve_log_saving=128` 保留 10 个输入侧安全幂和 54 个最终余量。接受 `EXT-BG` 时该输入足够；严格自足版仍需重证 BG 型多线性倒数 Kloosterman 固定对数节省，或证明 Baker 大谱/倒数频率平均替代。

```text
exact_input_theorem_statement_closed=true
log_power_budget_closed=true
ext_bg_sufficient_if_accepted=true
self_contained_multilinear_reciprocal_kloosterman_proof_closed=false
row_column_unconditional_closed=false
```

## 1. 精确输入定理

| field | value |
| --- | --- |
| `name` | MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks |
| `modulus` | prime P |
| `phase` | e_P(xi*(mn)^(-1)), xi != 0 mod P |
| `bilinear_block` | S(M,N)=sum_{m~M} sum_{n~N} alpha_m beta_n e_P(xi*(mn)^(-1)), MN≈P |
| `coefficients` | Vaughan/divisor-bounded coefficients with dyadic losses already charged |
| `rks2_range` | min(M,N)>P^(1/18) and long side in BG bilinear coverage; in MN≈P this covers the remaining unbalanced range |
| `rks3_range` | balanced or further split multilinear blocks satisfying BG Kloost 1/2 product threshold |
| `required_bound` | \|S(M,N)\| <= MN/log^118(P) on each charged block |
| `reason` | After the RKS loss 74, this implies the Tail-log4 target MN/log^44(P). |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `KloostermanInputGateActive` | `true` | `true` | 上一证书已把唯一自足数学缺口压成多线性倒数 Kloosterman 固定对数节省。 | MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks |
| `ExactInputTheoremStatementClosed` | `true` | `true` | 所需命题已精确到素数模数、倒数乘积相位、Vaughan/divisor-bounded 双线性块和 RKS2/RKS3 范围。 | statement fixed |
| `LogPowerBudgetClosed` | `true` | `true` | 外部输入需提供 log^-118；RKS 损失 74 后剩 log^-44，且 128-74=54 余量为正。 | log-power arithmetic closed |
| `EXTBGSufficientIfAccepted` | `true` | `true` | BG 型固定对数节省强于本输入；接受 EXT-BG 时本原子外部闭合。 | AcceptEXTBGForRKSLogFixedSaving |
| `BakerSingleFrequencyNotEnough` | `true` | `true` | Baker 单频率素变量估计不能直接控制 d 层绝对值平均。 | BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks` | `false` | `false` | 严格自足证明仍未给出；要么重证 BG 多线性定理，要么证明 Baker 大谱/倒数频率平均替代。 | SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步固定了最小输入定理和参数预算，没有发生独立验收或自足重证。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving
```
