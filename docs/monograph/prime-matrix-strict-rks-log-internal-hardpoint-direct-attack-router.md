# Prime Matrix strict RKS-log 内部硬点直接攻击证书

**状态：** `rks_log_internal_hardpoint_reduced_to_rks2_rks3_bg_blocks`

RKS-log 内部自足硬点进一步缩窄：RKS1 短侧 Weil 和 RKS4 低体积/端点吸收已经移出，对数预算 `74<128` 已闭合。唯一真正深点是 RKS2/RKS3 的 BG 型双/多线性倒数 Kloosterman 固定对数节省。外部接受 EXT-BG 可关闭它；严格内部路线只能重证 BG 型深估计，或证明 Baker 大谱/倒数频率平均替代。

```text
rks1_short_side_weil_closed=true
rks4_low_volume_closed=true
rks2_rks3_deep_blocks_isolated=true
rks2_rks3_self_contained_proved=false
row_column_unconditional_closed=false
```

## 1. 精确剩余原子

| field | value |
| --- | --- |
| `name` | SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving |
| `rks2` | BG bilinear reciprocal Kloosterman log saving for divisor-bounded Vaughan Type II blocks |
| `rks3` | BG multilinear / Kloost 1/2 reciprocal product log saving for balanced or further split blocks |
| `required_strength` | enough fixed log saving to pay RKS loss 74 and leave Tail-log4 log^-44; prior conservative target log^-118 is sufficient |
| `closed_parts_removed` | RKS1 short-side Weil and RKS4 low-volume/endpoint absorption |
| `external_shortcut` | EXT-BG closes this if accepted, but strict internal line must prove it or prove Baker-frequency average replacement |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RKSLogTargetActive` | `true` | `true` | 上一层已把唯一内部自足线压成 TL4-L/RKS-log。 | SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving |
| `RKSLogStatementFixed` | `true` | `true` | RKS-log 已有精确定理模式：素数模数、倒数乘积相位、固定对数节省。 | statement fixed |
| `RKS1ShortSideWeilClosed` | `true` | `true` | 短侧变量由完成和/Weil 吸收，不是内部深点。 | removed from hardpoint |
| `RKS4LowVolumeClosed` | `true` | `true` | 低体积和端点块由平凡估计/Tail-log4 余量吸收。 | removed from hardpoint |
| `RKS2RKS3DeepBlocksIsolated` | `true` | `true` | 剩余深块精确为 RKS2 双线性 BG 与 RKS3 多线性 BG，且对数预算 74<128 已闭合。 | SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving |
| `EXTBGExternalShortcutReady` | `true` | `true` | 接受 EXT-BG 时 RKS2/RKS3 外部闭合。 | AcceptEXTBGForRKSLogFixedSaving |
| `BakerOnlyStillInsufficient` | `true` | `true` | Baker 单频率不能直接替代 coherent 平均；旧 Baker/F4S+ 路线只是备选重证策略。 | BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `BakerAverageFrontierKnown` | `true` | `true` | 旧研究已定位 Baker 大谱、F4S+ 和临界拼接路径，但未形成完整内部证明。 | BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving` | `false` | `false` | 当前材料没有内部证明 RKS2/RKS3 的 BG 型固定对数节省。 | SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving` | `false` | `false` | RKS-log 自足闭合等价于补上 RKS2/RKS3 深块内部证明。 | SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只继续压缩唯一内部硬点，未证明 BG 深估计。 | SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving |

## 3. 下一最精确硬攻点

```text
SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving
```
