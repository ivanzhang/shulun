# Prime Matrix Phi-LPF boundary ratio q-spine pivot reduction 路由

**状态：** `boundary_ratio_reduced_to_qspine_pivot_enclosure_uniform_law_open`
**核验日期：** `2026-05-26`

## 1. 总裁定

```text
boundary_ratio_source_key_law_reduced_to_qspine_pivot=true
old_residual_side_closed=true
new_residual_tail_alignment_partial_closed=true
bulk_carry_chain_normal_form_closed=true
carry_break_source_packet_reduction_closed=true
bridge_root_qspine_pivot_enclosure_reduction_closed=true
bridge_root_uniform_qspine_pivot_enclosure_law_proved=false
trace_or_typeii_family_admissible_now=false
row_column_unconditional_closed=false
```

## 2. residual flow 摘要

```text
q_boundary_synthetic_split_event_count=47
new_residual_side_event_count=42
old_residual_side_event_count=5
new_residual_mass_total=13.264539470882 (41926303295575689754715570945220742196966577484713147368977982770741/3160780921765953306422353215107991553097814357054137917186575616177)
old_residual_mass_total=0.215539338772 (4672783399294642/21679492133206013)
net_new_minus_old_residual_mass=13.049000132111 (54957153409114568024198549894917703765637866355953735626792659191/4211598808546086562597811196363849161858214943368430057167809509)
finite_boundary_local_opposite_side_cancellation_refuted=true
```

## 3. return/bulk 摘要

```text
old_residual_return_aligned_event_count=5
new_residual_tail_matched_event_count=6
new_residual_unmatched_after_tail_event_count=36
new_residual_unmatched_after_tail_mass=11.684494473663 (48967251418543203254061941388483988569929566712414232303496831012/4190789043455521398233821685192850236361315067355978489004650201)
carry_segment_count=11
carry_transition_count=31
carry_break_count=4
bridge_root_debt_break_count=2
bridge_root_debt_still_open=0.209830550963 (4650291309275317106/22162126954053594199)
```

## 4. q-spine pivot 摘要

```text
q_spine_nodes=[577, 607, 631]
shared_pivot_q=607
shared_pivot_index=1
pivot_enclosure_row_count=2
exact_pivot_contact_count=1
finite_pivot_enclosure_closed=true
endpoint_slack_equals_pivot_gap_sum_closed=true
```

## 5. 依赖门

| gate | closed | proved | load | remaining |
| --- | --- | --- | --- | --- |
| ResidualFlowSideLedger | true | true | 42 new-side, 5 old-side | local conservation refuted; route to residual transport |
| OldResidualReturnAlignment | true | true | 5 old residuals | old-side transport closed only |
| NewResidualTailAlignment | true | true | 6 matched, 36 unmatched | bulk new residual source law |
| BulkCarryChainNormalForm | true | true | 11 carry segments, 31 transitions | carry segment roots and breaks |
| CarryBreakSourcePackets | true | true | 2 bridge debts, 2 unit echoes | bridge-root debt source law |
| BridgeRootQSpinePivotEnclosure | true | true | 2 pivot rows, 1 exact contact | uniform pivot enclosure law |
| TerminalSiblingQSpinePayment | true | false | right m769/m773 q-spine packet | terminal sibling q-spine payment law |

## 6. 最新开放口

```text
BoundaryRatioQSpinePivotReductionClosed AND BridgeRootQSpinePivotEnclosureLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND TerminalSiblingQSpinePaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_boundary_ratio_qspine_pivot_reduction_router.py` | `16c9a834bce770b8fe42fa68690c35635ed7df19a0eb0ee7c6329a8ece506bdc` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json` | `5cc56c562ce7145f6a1b8095beb924eae41624e285efa26e67db7c155bddd565` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json` | `4023c41551ce51476161cd01fce05b5de460b37c42c870000d0a1c853544ef88` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json` | `4f2f4be70956f3ab1da6e3fd1cd790630014cc1213eb83a1d0111e61cdca5641` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json` | `a6abbc588de0905e4f96855b5bfe7f0594d2f46351732cf3bc3c9a34048c508f` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json` | `e2482fea4f855b9e66c2c8d16f5d6ae7f020a83a8b0d16cbb29f02562f72539e` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json` | `e352152ebee0b366126014257df6013cd054e827004ff882dc67e943dde1ea4c` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json` | `23ca4dfcd8fe7771e24bb62c0e0a4bc8aa0fbb57b5406690c9175bec78eb5440` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json` | `8ee3a54cdd7ed21521fee953ef6d2f3433235a0e6a7a81b4055f89e31e1603da` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `6b0a97fcb5fb067219a82fc343b45df73606193998b4b5c0434e8a9b46557c0a` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `cd8203915f41647026f245527713e74ca1b13214a2aee61302290c01819c7bf2` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `d3544b8c6f70e63344f48fdd0bb81c1e11893480008b83d8f8820f6f7f48d4be` |
| `docs/monograph/external-theorem-index.md` | `6af8fe925c9ef00db9c643ec0157d71790dd03d120c5e26f682ef5d7d7198dd2` |
