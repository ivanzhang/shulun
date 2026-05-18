# Prime Matrix terminal-square downstream frontier sync router

**状态：** `terminal_square_phase_synced_to_downstream_frontier_global_open`

本步把 terminal-row square-phase bridge 从旧的 `SquarePhaseSpecialPhaseLongBlockPDECExclusion` 同步到仓库已有下游前沿：half-grid/phase-band 路由、localized P-CRT/AP 零点包路线、以及 global CRT signed-payload 路线。因此该旧硬点应视为上游接口别名；当前 consolidated 剩余仍是 AP 零点包、signed payload、same-set PDEC 及若干全局输入的无条件化，不是行/列命题闭合。

```text
frontier_file_count=10
square_phase_longblock_synced_downstream=true
row_column_unconditional_closed=false
```

## 1. 同步表

| label | role | status | remaining/status |
| --- | --- | --- | --- |
| Terminal-row CRT atom | closes specified terminal atoms small-factor absorption | specified_terminal_atoms_closed_but_global_localization_open | TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer |
| Terminal-row square-phase bridge | maps terminal missing rows to P^2 +/- r square-phase survivors | terminal_row_localization_routed_to_square_phase_special_jacobsthal_or_pdec_open | SquarePhaseSpecialPhaseLongBlockPDECExclusion |
| Square-phase half-grid boundary word | reduces special long block to signed even half-grid survivor pressure | square_phase_special_longblock_reduced_to_even_halfgrid_boundary_word_open | HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC |
| No-slot phase-band PDEC | rewrites no-slot load as tail-prime quadratic phase-band count | halfgrid_pressure_reduced_to_noslot_tailprime_phaseband_density_pdec_open | NoSlotTailPrimePhaseBandDensityPDECExclusion |
| Global CRT signed payload sync | routes internal CRT skeleton to signed payload / same-set PDEC frontiers | global_crt_internal_route_reduced_to_signed_payload_with_external_pdec_retained | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| Localized P-CRT / Linnik=2 barrier | identifies pointwise AP least-prime below P^2 as a barrier | localized_pcrt_transfer_reduced_to_pointwise_linnik2_ap_or_structural_frontier_open | PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 |
| Linnik=2 rank-one phase capacity | separates total energy capacity from rank-one negative evaluation projection | pointwise_nonprincipal_projection_reduced_to_rankone_phase_coherence_open | RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2 |
| Three-claims rank-one explicit formula | routes rank-one AP obstruction to explicit AP zero-packet bounds | three_claim_frontiers_synthesized_rankone_routed_to_explicit_ap_zero_packet_open | ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2 |
| Explicit AP zero-packet Siegel split | splits AP zero packet into Siegel bias and nonreal phase concentration | explicit_ap_zero_packet_split_into_siegel_and_nonreal_phase_branches_open | ExplicitAPZeroPacketSiegelNonrealDichotomyAtP2 |
| Beta-gap Page sparsity | routes ultra-close real-zero multi-carrier risk to Page singleton or nonreal residual | beta_gap_budget_routed_to_page_sparsity_singleton_or_zero_packet_open | PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget |

## 2. Consolidated 剩余基

| remaining input |
| --- |
| `PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget` |
| `AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn` |
| `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` |
| `ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem` |
| `ExplicitModelGapAndFiniteDPRCLedger` |
| `RatePreservationLedger_FOR_moving_atom_packet` |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `terminal_square_phase_downstream_sync` | `closed_routing` | The terminal-row square-phase bridge is synchronized with the already materialized half-grid, phase-band, AP-zero-packet, and signed-payload frontiers. |
| `square_phase_longblock_not_latest_terminal_basis` | `closed_routing` | SquarePhaseSpecialPhaseLongBlockPDECExclusion is retained as an upstream alias, not as the deepest active terminal-row frontier in the repository. |
| `downstream_frontier_unconditional_closure` | `open` | A full row/column proof still needs the remaining AP zero-packet, signed payload, same-set PDEC, and accepted global input frontiers to close. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TerminalSquarePhaseDownstreamSyncClosed` | true | true | 终端行平方相位桥接已和仓库下游前沿同步。 | closed routing |
| `SquarePhaseLongBlockStillDeepestFrontier` | true | false | `SquarePhaseSpecialPhaseLongBlockPDECExclusion` 只是上游别名，不应再作为最深硬点。 | downstream basis |
| `RowColumnUnconditionalClosureReached` | false | false | 本步只同步前沿，不关闭全局行/列命题。 | TerminalSquarePhaseDownstreamFrontierBasis: PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |

## 5. 结论边界

- 本步只做前沿同步与口径纠偏。
- 不能把 downstream frontier 的存在误读为行/列命题已闭合。
- 下一步应直接攻击 consolidated 剩余基中的 AP 零点包、signed payload 或 same-set PDEC 输入。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_terminal_square_phase_downstream_frontier_sync_router.py` | `a77b0f500fc82c4fd0c5bc3a6108d1c28ff0ab8af66675a77b9080c05e5d6079` |
| `data/prime-matrix-terminal-square-phase-downstream-frontier-sync-ledger.json` | `f3a290e6307e3f532afed6692822d061413f31933c1e17e2062a91acbe02fe4f` |
| `docs/monograph/prime-matrix-terminal-row-crt-atom-router.json` | `9cd30547530777703ba8019a20b7eee3bfa2c82da4bd8136178b73b64250193d` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json` | `328ee462d76cb6213f976eee33133885f20109157d16cf80d236ae27d78d8993` |
| `docs/monograph/prime-matrix-square-phase-halfgrid-boundary-word-router.json` | `7ec1d6e1235bc0bb4d822006ad50b7ad0aa621d6463aec23d8227606de5d8bd6` |
| `docs/monograph/prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.json` | `023ca63e33901275c0c34440d00a671d6ea9b523ec07256c5a0bba2b12b41b74` |
| `docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json` | `969459391db184ef4250b42c88f9947e1884ac92523320b47f887f729e8c6c56` |
| `docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json` | `98232747aaf27a93f4cc68cc5bc8d29d80c5d0786bfeead635a6b42293ba6107` |
| `docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json` | `5c1a653d7367788f233fb0ca0eee1147b75a2c1ae8c614919bb0a78be7e0a2c4` |
| `docs/monograph/three-claims-frontier-rankone-explicit-formula-router.json` | `8634e16e1bcf7cd0d4ef6342b61bc73055246991c64d1940efb981f4c88c0390` |
| `docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json` | `5c277929e4739d9e6829a9137d4115f974fc1df3260c7f31e57f6a7f3bc879db` |
| `docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json` | `eb53bcf1653d6b09c9d09c021a8418a1883bdc8cb3eba102ba0810ea3cefdc44` |
