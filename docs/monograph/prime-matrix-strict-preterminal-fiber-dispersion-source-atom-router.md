# Prime Matrix strict preterminal fiber dispersion 源域原子化证书

**状态：** `strict_preterminal_fiber_dispersion_reduced_to_source_rank_atom_package_open`

本步把当前唯一内部自足线的真正剩余继续压窄：`PreTerminalExactUVFiberAbsoluteMassDispersionTheorem` 等价地需要一个源域 rank/no-collapse 包。形式求和蕴含已闭合；未闭合的是 actual source domain absolute entropy、complete key 分区、fixed-key exact-UV 局部 O(1) 重数三项。行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
preterminal_fiber_dispersion_source_atomization_closed=true
deterministic_source_atom_implication_closed=true
actual_precauchy_source_domain_absolute_entropy_ledger_proved=false
complete_primitive_emitter_key_partition_ledger_proved=false
fixed_key_exact_uv_local_multiplicity_o1_ledger_proved=false
preterminal_exact_uv_fiber_absolute_mass_dispersion_proved=false
actual_noncanonical_exact_uv_support_closed=false
row_column_unconditional_closed=false
```

## 1. 当前压缩

压缩前：

```text
PreTerminalExactUVFiberAbsoluteMassDispersionTheorem
```

压缩后：

```text
ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger
```

## 2. 源域原子包

| atom | proved | role |
| --- | --- | --- |
| `ActualPreCauchySourceDomainAbsoluteEntropyLedger` | `false` | 给出 actual pre-Cauchy source 的绝对质量不集中账本，排除少数 primitive rows 承载总质量。 |
| `CompletePrimitiveEmitterKeyPartitionLedger` | `false` | 把所有 primitive summands 在发射前分到多对数个 complete keys，禁止后验补标签。 |
| `FixedKeyExactUVLocalMultiplicityO1Ledger` | `false` | 证明固定 complete key 与固定 exact `(u,v)` 下没有大原像坍缩。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreTerminalFiberDispersionTargetActive` | `true` | `false` | 最终推广后 ExactUV 的作者侧核心已经压到 preterminal exact `(u,v)` fiber 绝对质量分散。 | PreTerminalExactUVFiberAbsoluteMassDispersionTheorem |
| `RegisteredCapacityMultiplierImported` | `true` | `true` | Type/Fourier/fiber/系数等乘子已登记到同一 formal unit；它们只提供 log-power 成本账本。 | ActualNoncanonicalExactUVSupportLowerBound |
| `OptionalAbsoluteToMultiplicityFrontierSeen` | `true` | `false` | 历史工作树中已有把绝对质量问题转成 primitive emitter 原像 multiplicity 的草稿路由；本证书只吸收其结构，不把它当作最终证明。 | PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem |
| `OptionalRankNoCollapseFrontierSeen` | `true` | `false` | 历史工作树中已有把 multiplicity 继续压到 exact-UV map rank/no-collapse 的草稿路由；当前仍未证明。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |
| `DeterministicSourceAtomImplicationClosed` | `true` | `true` | 若同一源表同时给出源域绝对熵、complete key 多对数分区、固定 key 下 exact-UV 局部 O(1) 重数，则按 key 求和立即得到每个 `(u,v)` 的绝对质量上界。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `FixedPairFormalInequalityRecognized` | `true` | `true` | fixed-pair 形式不等式本身只是代数求和：key 数乘以固定 key 局部重数给出 fiber 上界。 | CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `ActualSourceDomainEntropyCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出 actual pre-Cauchy source 域的绝对质量熵账本；没有该账本，O(1) 原像也不能转成总质量小比例。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger |
| `CompletePrimitiveEmitterKeyPartitionCurrentCorpusProved` | `false` | `false` | complete key 必须在发射前登记 formal unit、branch path、exact `(u,v)`、sign/local factor 和 truncation 状态；当前未证明。 | CompletePrimitiveEmitterKeyPartitionLedger |
| `FixedKeyExactUVLocalMultiplicityCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明固定 complete key 与固定 exact `(u,v)` 下只有 O(1) 个 actual primitive source 原像。 | FixedKeyExactUVLocalMultiplicityO1Ledger |
| `ActualPrimitiveSourceTableStillUpstreamOpen` | `false` | `false` | 若没有 actual noncanonical primitive emitter 源表，domain entropy、complete key 与局部重数都只是后验标签。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger |
| `PointwiseKernelTableStillUpstreamOpen` | `false` | `false` | 同一 formal unit 的逐 primitive 核表仍未提交；它是把 signed source、Phi 和 exact-UV rank 对齐的上游字段。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `FalseSourceRoutesRejected` | `true` | `true` | raw Buchstab 计数、canonical 支撑导入、signed-only 相消、terminal packet 回流、CRT/轮筛位置刚性都不能生成源域绝对熵或 no-collapse。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `PreTerminalExactUVFiberAbsoluteMassDispersionCurrentCorpusProved` | `false` | `false` | 三个源域原子未合取证明前，preterminal exact-UV fiber 绝对质量分散仍未闭合。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | ExactUV 源域分散与 DStructure/Rankin 独立验收门未完成前，行/列命题不能标为无条件闭合。 | ActualNoncanonicalExactUVSupportLowerBound AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 4. 确定性蕴含

```text
Let D be the actual pre-Cauchy primitive source rows in one formal unit, pi:D->Omega_exact the exact (u,v) map, kappa:D->K a complete key map, and M_abs=sum_D |w(d)|. If |K|<=L^C, single-row absolute weights are registered into the same log budget, and every fixed pair/key fiber pi^{-1}(u,v) cap kappa^{-1}(k) has O(1) admissible source rows with no heavy-row exception, then M_abs(u,v)<=M_abs/L^A after choosing the stored log slack. Thus the remaining burden is exactly source entropy plus no-fiber-collapse, not CRT position counting.
```

## 5. 结构律

preterminal exact-UV 绝对 fiber 分散不是短区间统计或 signed cancellation；它是同一 formal unit 内 actual pre-Cauchy source 的源域熵与 exact-UV 映射无坍缩命题。早期零行、斜线覆盖、圆柱螺旋和轮筛刚性只能给位置/回流约束，不能替代源表、complete key 或局部重数证明。

## 6. 下一主攻顺序

1. `ActualPreCauchySourceDomainAbsoluteEntropyLedger`
2. `CompletePrimitiveEmitterKeyPartitionLedger`
3. `FixedKeyExactUVLocalMultiplicityO1Ledger`
