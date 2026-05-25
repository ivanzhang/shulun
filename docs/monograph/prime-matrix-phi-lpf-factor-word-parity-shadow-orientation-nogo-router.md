# Prime Matrix Phi-LPF factor-word parity shadow orientation no-go 证书

**状态：** `factor_word_parity_shadow_rejected_as_orientation_or_builtin_pairing_law`
**核验日期：** `2026-05-25`

本证书检验一个最自然的捷径：把 LPF factor word 给出的 Möbius、Liouville、depth parity 或 squarefree 状态直接升级为 orientation/local-factor signed law。
结论是否定的：这些 shadow 全部闭合，但都只依赖无符号 factor word。

```text
factor_word_mobius_shadow_closed=true
factor_word_liouville_shadow_closed=true
depth_parity_shadow_closed=true
shadow_depends_only_on_unsigned_factor_word=true
shadow_lacks_precauchy_source_key=true
shadow_lacks_orientation_branch_trace=true
shadow_lacks_exactuv_payload=true
factor_word_shadow_proves_orientation_local_factor_law=false
factor_word_shadow_proves_builtin_pairing=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 1. shadow 候选

| shadow | formula | unsigned only | source key | branch trace | ExactUV | can be signed law |
| --- | --- | --- | --- | --- | --- | --- |
| `MobiusFactorWordShadow` | `0 if factor_word has repeated prime else (-1)^len(factor_word)` | `true` | `false` | `false` | `false` | `false` |
| `LiouvilleFactorWordShadow` | `(-1)^len(factor_word)` | `true` | `false` | `false` | `false` | `false` |
| `DepthParityShadow` | `len(factor_word) mod 2` | `true` | `false` | `false` | `false` | `false` |
| `SquarefreeZeroShadow` | `1 if factor_word has no repeated prime else 0` | `true` | `false` | `false` | `false` | `false` |

## 2. orientation twin collision

```text
support_keys_in_largest_sample=26781
abstract_orientation_states_per_key=2
abstract_twin_state_count=53562
factor_word_shadow_collision_count=26781
```

含义：当前已闭合合同中，factor word 不含 orientation 字段；而 signed coefficient 对 orientation/local factor 敏感。任何只读 factor word 的函数都会把取向槽压成同一值。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FactorWordParityShadowsClosed` | `true` | `true` | small-to-large 剥离已闭合 Möbius、Liouville、depth parity 与 squarefree 等自然 shadow。 | `closed unsigned factor-word state table` |
| `ShadowsDependOnlyOnUnsignedFactorWord` | `true` | `true` | 这些 shadow 的输入只有非降素因子词和重复素因子信息，不读取 source、orientation、UV 或 branch tag。 | `post-factorization labels` |
| `OrientationFlipContractImported` | `true` | `true` | 既有 row-level 证书登记：无符号几何在取向翻转下不变，而 signed coefficient 对取向敏感。 | `PrimitiveOrientationLocalFactorProductLawBeforePushforward` |
| `PointwiseSignedTableStillNeedsOrientationLaw` | `true` | `false` | Phi-LPF support 上的逐点 signed table 首字段仍是 primitive orientation/local-factor product law。 | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` |
| `BranchTraceStillMissing` | `true` | `false` | orientation/local-factor law 已压到 actual noncanonical complete branch trace formula 或命名回流。 | `ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn` |
| `BuiltInPairingStillNeedsAtomicTrace` | `true` | `false` | atomic joint rows 的 built-in signed pairing 仍需 ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn。 | `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` |
| `PreviousParityKernelRejectionsImported` | `true` | `true` | 既有 noncircular kernel 证书已拒绝 Mobius truncation 与 three-edge parity audit 作为 exact kernel。 | `parity shadow is not a kernel` |
| `ShadowLacksPreCauchySourceKey` | `true` | `true` | factor word 不声明同 formal unit 的 pre-Cauchy source tuple 或 emitter source key。 | `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` |
| `ShadowLacksExactUVPayload` | `true` | `false` | factor word 不输出 exact `(u,v)`、fixed-pair multiplicity、branch key 或 nonzero condition。 | `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger` |
| `FactorWordShadowProvesOrientationLocalFactorLaw` | `false` | `false` | 只读 factor word 的 parity shadow 在 orientation twin 上取同值，不能给反变号取向/local-factor 乘积律。 | `PrimitiveOrientationLocalFactorProductLawBeforePushforward` |
| `FactorWordShadowProvesBuiltInPairing` | `false` | `false` | built-in pairing 要同一 atomic trace 同时给 word、signed coefficient、alpha/delta payload 与 ExactUV；shadow 不足。 | `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只排除了 parity shadow 直升 signed law 的捷径；三命题仍未无条件闭合。 | `PrimitiveOrientationLocalFactorProductLawBeforePushforward OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |

## 4. 外部前沿适配边界

| external input | usable after | not supplied by shadow |
| --- | --- | --- |
| DI/BFI/Kuznetsov, FKMS, Milicevic-Qin-Wu, Pascadi, Wright-type trace or Kloosterman tools | 提交 admissible averaged trace/Kloosterman/Type-II family with signed payload | factor-word parity shadow is a pointwise post-factorization label, not an averaged trace family |
| Maynard small gaps or Li short intervals | 转化为目标尺度的行/列或 residue-level positivity statement | does not provide fixed row/AP positivity or signed coefficient generation |
| linear or beta-sieve parity inputs | 出现 independent odd data or named return beyond support saturation | Möbius/Liouville visibility remains exactly parity-shadow information |

## 5. 最新开放口

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

保留严格基底：

```text
(PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR (BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance)
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_factor_word_parity_shadow_orientation_nogo_router.py` | `6ac9ecbb0110dbf81028d0268b509ae2919df13c045005ba57f3592584d7f57d` |
| `docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json` | `bee6ba7d14330a7a2cf52547f8b37902314ba8ffa9b10186ae5d1e71efe4a534` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json` | `7c76acab60f95b655941cb563439aca48116d80cd4dc1733a0210d96e4a45fb0` |
| `docs/monograph/prime-matrix-strict-row-level-noncircular-orientation-law-router.json` | `9c03e809ea7c2a1b9edc2863b065f3f93f1fa07d9487ec96753c6b140e62bfff` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json` | `96d6dadbc5add815f8623295aae5ae519c0b5e44db556d85d657259db97a9773` |

行/列命题仍未无条件闭合。
