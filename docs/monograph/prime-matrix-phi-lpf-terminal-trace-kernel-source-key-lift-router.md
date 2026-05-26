# Prime Matrix Phi-LPF terminal trace-kernel source-key lift 路由

**状态：** `terminal_trace_kernel_source_key_lift_reduction_closed_kernel_open`
**核验日期：** `2026-05-26`

## 1. 总裁定

```text
formal_jordan_phase_kernel_closed=true
prefix_record_reflection_schema_closed=true
source_key_obstruction_partition_closed=true
boundary_ratio_spectrum_closed=true
sibling_qspine_finite_kernel_closed=true
terminal_run_kernel_formula_reduced_to_actual_source_key_gates=true
terminal_run_kernel_formula_proved=false
same_trace_key_source_consistency_proved=false
trace_or_typeii_family_admissible_now=false
row_column_unconditional_closed=false
```

## 2. event reduction 摘要

```text
terminal_transition_count_total=126
terminal_run_count_total=59
cancellation_event_count=51
synthetic_split_event_count=51
q_boundary_synthetic_split_event_count=47
nonboundary_record_jump_event_count=4
internal_survivor_fragment_count=1
tail_survivor_fragment_count=7
whole_equal_pair_event_count=0
```

## 3. boundary ratio 摘要

```text
ratio_min=0.013003592969 (415829/31978008)
ratio_max=0.967151620496 (169997634/175771441)
boundary_chunk_mass_total=14.631796550631 (11300120486994743871953452237691197733518695954935357389819382388044553919/772298907238916261289587790898356540320031771197428129590077001137691901)
boundary_residual_gap_mass_total=13.480078809654 (18704725831274706221411647651674960542383244116881133974210171827029401/1387582824655253501519413061432408291809940502746766545644906695501703)
boundary_residual_gap_mass_max=0.861355534983 (280062/325141)
finite_margin_after_nonboundary_internal_payment_positive=true
```

## 4. tail/q-spine 摘要

```text
old_residual_return_alignment_closed=true
new_residual_tail_alignment_partial_closed=true
new_residual_event_count=42
new_residual_unmatched_after_tail_event_count=36
terminal_double_awrap_sibling_qspine_kernel_payment_law_proved=false
```

## 5. trace kernel 依赖门

| gate | closed | proved | load | remaining |
| --- | --- | --- | --- | --- |
| FormalJordanPhaseKernel | true | true | 126 transitions, 59 runs | not yet a pre-Cauchy trace kernel |
| PrefixRecordReflectionSchema | true | true | 51 cancellation events | source-key lift still open |
| BoundaryRatioSourceKeyLaw | true | false | 47 q-boundary events | BoundaryAdjacentRunMassRatioLawOrPDEC |
| NonBoundaryRecordJumpSourceKeyLift | true | false | 4 events on 2 atoms | NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC |
| InternalPrefixRecordSurvivor | true | false | 1 internal survivor fragment | InternalPrefixRecordSurvivorPDEC |
| SiblingQSpineKernelPayment | true | false | m769/m773 shared double-Awrap q-spine | TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC |

## 6. 六接口合同降维

| contract | reduced here | proved here | actual dependencies | failure return |
| --- | --- | --- | --- | --- |
| TerminalRunKernelFormula | true | false | FormalJordanPhaseKernel AND BoundaryRatioSourceKeyLaw AND NonBoundaryRecordJumpSourceKeyLift AND InternalPrefixRecordSurvivor AND SiblingQSpineKernelPayment AND PrimitiveOrientationLocalFactorProductLaw | MissingTraceKernelFormulaPDEC |
| SameTraceKeySourceConsistency | true | false | PrefixRecordSourceKeyLift AND BoundaryResidualFlowSourceKeyConservation AND PrimitiveOrientationLocalFactorProductLaw | SameTraceKeySplitPDEC |
| UniformFamilyInP | false | false | only meaningful after a forward source-key kernel exists | FiniteLedgerOnlyLocalSurvivor |
| TypeIICoefficientFactorability | false | false | requires source-keyed signed coefficients before factorability can be tested | TypeIIFactorabilityFailureSAE |
| ConductorOrModulusControl | false | false | requires an actual kernel family before conductor/modulus can be assigned | ConductorRangePDEC |
| UniformAdjacentRunCancellation | true | false | BoundaryRatioSourceKeyLaw AND NonBoundaryRecordJumpSourceKeyLift AND InternalPrefixRecordSurvivor | AdjacentRunCancellationFailureLocalSurvivor |

## 7. 最新开放口

```text
TraceKernelSourceKeyLiftReductionClosed AND BoundaryRatioSourceKeyLawOrPDEC AND NonBoundaryRecordJumpSourceKeyLiftOrPDEC AND InternalSurvivorPDEC AND TerminalSiblingQSpinePaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND UniformAdjacentRunCancellationStillOpen
```

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_terminal_trace_kernel_source_key_lift_router.py` | `ada876e935e589f0ffec67375003742dee43d5711345439a1d3fa568b0814e92` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json` | `68d92a76de9afa0228d9e9dae12de19bb4b8189e69397c66c7d967ce4b915b0e` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json` | `0c18e61b945499886d3f0d3720f0fd5a119a2d264dbb714be71236504fe121c7` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json` | `567dde4948ec2f22e3b4babeccea9e3e667e3ba4261192deddd97e87285f2b3e` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json` | `5f855cce874423998dc3046cbf66f7a3930b939520d1103766f0f0bae77a65e3` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json` | `531aa4dbe2be427b1a131cfc43693df97c4ff8948cd1c48c7c7a2a3e97d5266a` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json` | `8ee3a54cdd7ed21521fee953ef6d2f3433235a0e6a7a81b4055f89e31e1603da` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json` | `a6abbc588de0905e4f96855b5bfe7f0594d2f46351732cf3bc3c9a34048c508f` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json` | `4f2f4be70956f3ab1da6e3fd1cd790630014cc1213eb83a1d0111e61cdca5641` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `9503756696f66a5f98abda8a3b6251d2e9609a7a0ce90ed89ce03b770eb766f2` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `7bee544b3c53514216fa393290d089efedd7dfa4865390ac915413a80e3d6a78` |
| `docs/monograph/external-theorem-index.md` | `13ce2b0f331aa1f7ec5cac227825e4e9b44dcff33c1d8b629dd9302aae28804d` |
