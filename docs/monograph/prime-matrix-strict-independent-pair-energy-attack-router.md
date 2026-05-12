# Prime Matrix strict 独立 pair 能量界直攻路由器

**状态：** `strict_independent_pair_energy_reduced_to_rate_bearing_large_pair_packet_exclusion_open`

继续在 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 内部攻击，`IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed` 被进一步压缩。抽象 seed 本身不足以推出 pair L2/max-atom 界，因为可形式登记一个全部质量集中在单个 exact pair 上的 seed；有限投影二分也只给定性消散，不能给任意 A 所需的 log-power 速率。因此同命题内部真正剩余变为 `RateBearingLargePairAtomPacketExclusion`：排斥所有超过阈值 `M/L^K` 的同 formal unit 大 pair packet，或证明其必回流到已命名终端。当前仍未无条件闭合。

```text
same_theorem_target_preserved=true
seed_only_insufficient_model_verified=true
large_pair_failure_packetized=true
qualitative_projection_dichotomy_insufficient_for_log_rate=true
independent_exact_pair_l2_or_max_atom_bound_proved=false
rate_bearing_large_pair_atom_packet_exclusion_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 同命题内部压缩

```text
IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
  -> Rate-bearing large exact-pair atom packet cannot exist
  -> RateBearingLargePairAtomPacketExclusion

RateBearingLargePairAtomPacketExclusion => IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed => ActualNoncanonicalExactUVSupportLowerBound => NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameSourceEntropyTargetPreserved` | `true` | `true` | 继续在 NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem 内部攻击，不改换总命题。 | IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed |
| `NonrecursiveGuardImported` | `true` | `true` | 已禁止用源熵目标本身或 moving-atom 排斥反证 pair-mass 分散。 | 必须给独立 pair L2/max-atom 账本或命名回流。 |
| `SeedOnlyInsufficientModel` | `true` | `true` | 抽象 acyclic seed 字段允许所有质量落在单个 exact pair；所以 seed 名称本身不推出 L2/max-atom 界。 | 需要阈值大原子 packet 排斥或独立相消估计。 |
| `ElementaryEnergyLemmaImported` | `true` | `true` | 一旦有独立 L2/max-pair 界，支撑下界和源熵反原子由初等引理推出。 | 证明独立 L2/max-pair 界。 |
| `LargePairFailurePacketized` | `true` | `true` | 独立能量界失败等价于同一 formal unit 下出现超过阈值的 sign-refined exact pair 大原子 packet。 | RateBearingLargePairAtomPacketExclusion。 |
| `NonCleanLargePairReturnsImported` | `true` | `true` | 非 clean-core 或带低维签名的大 pair packet 已接回 PDEC/SAE/ColumnCRT/CleanKLS/DLS 终端门。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger。 |
| `SeedBranchFusionImported` | `true` | `true` | seed 存在/不存在两支均进入 acyclic terminal family；seed 不再是可隐藏的独立出口。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。 |
| `QualitativeProjectionDichotomyInsufficientForLogRate` | `true` | `true` | 有限投影二分只给 positive-limsup 或趋零；本目标需要任意固定 A 的 log-power 速率。 | RateBearingAcyclicPairAtomDecayOrTerminalExclusion。 |
| `IndependentPairEnergyCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 rate-bearing large-pair packet 全部不存在或必导致已排斥终端。 | RateBearingLargePairAtomPacketExclusion。 |
| `NewActualSourceEntropyCurrentCorpusProved` | `false` | `false` | 独立 pair 能量界仍未完成，所以新 actual-source 熵定理仍未证明。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem。 |

## 3. seed-only 阻断模型

| k | log y | threshold L^-K | pair count | max pair mass | L2 energy | violates energy |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 5.38607e-15 | 1 | 1.0 | 1.0 | `True` |
| 4 | 9.21034 | 4.04868e-17 | 1 | 1.0 | 1.0 | `True` |
| 5 | 11.5129 | 9.11682e-19 | 1 | 1.0 | 1.0 | `True` |
| 6 | 13.8155 | 4.10925e-20 | 1 | 1.0 | 1.0 | `True` |
| 7 | 16.1181 | 2.98997e-21 | 1 | 1.0 | 1.0 | `True` |
| 8 | 18.4207 | 3.0889e-22 | 1 | 1.0 | 1.0 | `True` |
| 9 | 20.7233 | 4.17072e-23 | 1 | 1.0 | 1.0 | `True` |

## 4. 大 pair packet 字段

| field | meaning |
| --- | --- |
| `formal_unit_id` | 与 pre-Cauchy seed、registered multipliers 和 terminal ledger 使用同一 formal unit。 |
| `pair_key` | 精确 `(u,v)`、path key、dyadic block、phase key 与 sign-refined branch key。 |
| `mass_profile` | 总绝对质量 M、pair 质量 M_b、L2 能量贡献和阈值 `M/L^K`。 |
| `rate_certificate` | 说明失败是 log-power 阈值失败，而不是仅仅定性 positive-limsup。 |
| `return_tests` | 逐项测试 PDEC、SAE/LocalSurvivor、ColumnCRT、CleanKLS/DLS、canonical-lock 与外部条件线。 |

## 5. 硬边界律

seed-only 不能产生 log-power pair 能量界；定性有限投影消散也不足以支付任意 A。必须排斥每个超过 `M/L^K` 的 rate-bearing exact pair 大原子 packet，或证明它们全部进入已排斥的 PDEC/SAE/ColumnCRT/CleanKLS 终端。

下一步仍在同一源熵定理内部直攻：

```text
RateBearingLargePairAtomPacketExclusion
```

完整 strict 基仍保持：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
